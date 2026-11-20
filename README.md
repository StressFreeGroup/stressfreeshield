# Stress Free Shield

Interior Accidental Damage Liability Waiver Program

**Live:** stressfreeshield.com  
**Stack:** Static HTML + one Vercel serverless function (`api/submit.js`)  
**Hosting:** Vercel  
**Organization:** Stress Free Group LLC

## Deployment

Vercel auto-deploys on push to `main`. No build step required.

## Pages

- `/` (single page: Overview, Coverage, File a Claim, Service Network, Terms; deep-linkable as `/#coverage`, `/#claim`, etc.)
- `/coverage` covered-items guide, and `/coverage/<item>` one page per covered item

The coverage pages are generated from `tools/items.py`. Edit the wording there, then run
`python3 tools/gen.py` and commit the regenerated files in `coverage/`.

## Photo examples on covered-item pages

1. Put photos (JPG, roughly 1600px wide) in `coverage/photos/`.
2. List them under the item's key in `coverage/photos/manifest.json`, for example
   `"tv-remote": [{"file": "tv-remote-unit-12.jpg", "alt": "TV remote in Unit 12", "caption": "Unit 12 remote"}]`.
3. Commit and push. The "Photo examples" section appears automatically on that item's page.

## Forms (claims and vendor applications)

Both forms post to `/api/submit`, which emails the submission (with photos and estimate attached)
through Resend. Set these in Vercel > stressfreeshield > Settings > Environment Variables, then redeploy:

- `RESEND_API_KEY` (required)
- `EMAIL_FROM` a sender on a domain verified in Resend, e.g. `Stress Free Shield <shield@stressfreegroup.com>`
- `EMAIL_TO` optional, defaults to Mike@StressFreeGroup.com

Until the key is set, visitors who submit are shown a pre-filled email to send instead, so nothing is lost.
