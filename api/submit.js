// Stress Free Shield: receives claim and vendor-application forms and emails them
// to the Stress Free team through Resend (https://resend.com).
//
// Environment variables (Vercel > stressfreeshield > Settings > Environment Variables):
//   RESEND_API_KEY  required  Resend API key
//   EMAIL_TO        optional  where submissions go (default Mike@StressFreeGroup.com)
//   EMAIL_FROM      optional  verified sender, e.g. "Stress Free Shield <shield@stressfreegroup.com>"
//
// If the key is missing or Resend refuses the send, this returns ok:false and the
// page offers the visitor a pre-filled email instead, so no submission is lost.

const MAX_ATTACH_BYTES = 4 * 1024 * 1024;

const esc = (v) =>
  String(v == null ? '' : v).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const clean = (v, max = 4000) => String(v == null ? '' : v).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g, '').slice(0, max);
const emailOk = (v) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(v || '').trim());

module.exports = async (req, res) => {
  res.setHeader('Cache-Control', 'no-store');
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false, error: 'method_not_allowed', configured: Boolean(process.env.RESEND_API_KEY) });
  }

  let body = req.body;
  if (typeof body === 'string') {
    try { body = JSON.parse(body); } catch (e) { return res.status(400).json({ ok: false, error: 'bad_json' }); }
  }
  body = body || {};

  // Honeypot: real visitors never fill the hidden field. Pretend success for bots.
  if (body.website) return res.status(200).json({ ok: true });

  const type = body.type === 'vendor' ? 'vendor' : body.type === 'claim' ? 'claim' : null;
  if (!type) return res.status(400).json({ ok: false, error: 'bad_type' });

  const ref = clean(body.ref, 40);
  const fields = body.fields && typeof body.fields === 'object' ? body.fields : {};
  const entries = Object.entries(fields).slice(0, 40).map(([k, v]) => [clean(k, 80), clean(v)]);
  const replyTo = emailOk(body.replyTo) ? String(body.replyTo).trim() : undefined;
  if (!replyTo) return res.status(400).json({ ok: false, error: 'bad_email' });

  const files = Array.isArray(body.files) ? body.files.slice(0, 20) : [];
  let total = 0;
  const attachments = [];
  for (const f of files) {
    if (!f || typeof f.content !== 'string') continue;
    total += Math.floor(f.content.length * 0.75);
    if (total > MAX_ATTACH_BYTES) return res.status(413).json({ ok: false, error: 'too_large' });
    attachments.push({ filename: clean(f.filename, 120).replace(/[\\/]/g, '_') || 'attachment', content: f.content });
  }

  const key = process.env.RESEND_API_KEY;
  if (!key) return res.status(503).json({ ok: false, error: 'not_configured' });

  const name = (entries.find(([k]) => k === 'Name') || [])[1] || '';
  const subject = type === 'claim'
    ? `Shield claim ${ref}: ${name}`
    : `Shield vendor application ${ref}: ${(entries.find(([k]) => k === 'Company') || [])[1] || name}`;

  const rows = entries
    .filter(([, v]) => v !== '')
    .map(([k, v]) => `<tr><td style="padding:6px 12px 6px 0;color:#64748B;font-weight:600;vertical-align:top;white-space:nowrap">${esc(k)}</td><td style="padding:6px 0;color:#334155;white-space:pre-wrap">${esc(v)}</td></tr>`)
    .join('');
  const html = `<div style="font-family:Arial,Helvetica,sans-serif;font-size:14px;max-width:640px">
    <h2 style="color:#042C53;margin:0 0 4px">${type === 'claim' ? 'New Stress Free Shield claim' : 'New service network application'}</h2>
    <p style="color:#64748B;margin:0 0 16px">Submitted from stressfreeshield.com${attachments.length ? ` · ${attachments.length} attachment(s)` : ''}. Reply to this email to answer the ${type === 'claim' ? 'renter' : 'applicant'} directly.</p>
    <table style="border-collapse:collapse">${rows}</table></div>`;
  const text = entries.filter(([, v]) => v !== '').map(([k, v]) => `${k}: ${v}`).join('\n');

  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: process.env.EMAIL_FROM || 'Stress Free Shield <onboarding@resend.dev>',
        to: (process.env.EMAIL_TO || 'Mike@StressFreeGroup.com').split(',').map((s) => s.trim()).filter(Boolean),
        reply_to: replyTo,
        subject,
        html,
        text,
        attachments: attachments.length ? attachments : undefined,
      }),
    });
    if (!r.ok) {
      const detail = await r.text().catch(() => '');
      console.error('Resend error', r.status, detail.slice(0, 500));
      return res.status(502).json({ ok: false, error: 'send_failed' });
    }
    return res.status(200).json({ ok: true, ref });
  } catch (e) {
    console.error('Send exception', e && e.message);
    return res.status(502).json({ ok: false, error: 'send_failed' });
  }
};
