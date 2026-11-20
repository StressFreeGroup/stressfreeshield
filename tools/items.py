# Content for the Stress Free Shield covered-item pages.
# Each "ill" is an SVG body drawn on a 320x220 canvas. Classes: o = outline, f = filled part,
# h = highlighted (covered) part, t = label text, ht = highlighted label text.

INDUSTRY_BASE = ("In the RV and trailer rental industry, small interior items like this are usually treated as the renter's "
  "responsibility. Rental agreements commonly list them on a damage or replacement-fee schedule and deduct the cost from the "
  "security deposit, while the larger protection plans offered with rentals are built around major physical damage and often "
  "carry deductibles higher than the repair itself. A damage waiver such as the Stress Free Shield is designed to fill that gap.")

ITEMS = [
 dict(slug='accidental-interior-damage', name='Accidental interior damage (while parked)', group='General',
  short='Sudden, unintentional damage inside the unit while it is stationary.',
  what='Accidental interior damage is unexpected, unintentional damage to the inside of the RV or trailer that happens during normal use while the vehicle is parked, such as a part that snaps or comes loose. It is the umbrella that every other covered item on this list falls under.',
  covered=['Sudden, accidental damage to the covered interior items listed in the coverage schedule',
           'Damage that happens while the vehicle is stationary (parked, leveled, or set up at camp)',
           'Subject to the $250 deductible per occurrence and the $2,500 maximum per coverage duration'],
  notcov=['Negligence, misuse, willful acts, or rental agreement violations',
          'Damage that happens while the vehicle is in motion',
          'Normal wear and tear, pre-existing damage, and pet or animal damage',
          'Any item not expressly listed as covered'],
  industry='Rental agreements across the industry draw a line between normal wear and tear, which the owner absorbs, and accidental damage, which is typically billed to the renter after the post-trip inspection.',
  cost=None,
  tip='Walk through the unit at pickup and photograph anything already worn or marked, so it is never confused with new damage.',
  ill='''<rect x="40" y="40" width="240" height="62" rx="6" class="f"/><line x1="120" y1="40" x2="120" y2="102" class="o"/><line x1="200" y1="40" x2="200" y2="102" class="o"/>
<circle cx="110" cy="72" r="3.5" class="h"/><circle cx="130" cy="72" r="3.5" class="o2"/><circle cx="190" cy="72" r="3.5" class="o2"/><circle cx="210" cy="72" r="3.5" class="o2"/>
<rect x="30" y="118" width="260" height="14" rx="3" class="f"/><rect x="40" y="132" width="240" height="56" rx="4" class="f"/>
<path d="M96 50 L104 62 L98 66 L108 80" class="h" fill="none"/>
<rect x="234" y="146" width="40" height="30" rx="6" class="hb"/><text x="254" y="167" class="htw" text-anchor="middle">P</text>
<text x="160" y="210" class="t" text-anchor="middle">Damage while parked, during normal use</text>'''),

 dict(slug='fridge-freezer-handle', name='Refrigerator or freezer handle', group='Kitchen',
  short='A cracked or snapped door handle on the RV refrigerator or freezer.',
  what='RV refrigerators use molded plastic door handles, often with a built-in travel latch that keeps the door shut on the road. The handle is the most common part of an RV fridge to break, usually when the door is pulled while the travel latch is still engaged.',
  covered=['Breakage of the refrigerator door handle', 'Breakage of the freezer door handle'],
  notcov=['The refrigerator or freezer unit itself, including cooling problems',
          'Door panels, hinges, seals, or shelves', 'Food loss or spoilage'],
  industry='Fridge handles are a routine line item on rental damage schedules because they break easily and are specific to each refrigerator model.',
  cost='Replacement handles commonly run about $20 to $80 for the part, depending on the refrigerator brand and model.',
  tip='Release the travel latch fully before opening the door, and never hang bags or towels on the handle.',
  ill='''<rect x="50" y="20" width="110" height="180" rx="8" class="f"/><line x1="50" y1="78" x2="160" y2="78" class="o"/>
<rect x="135" y="36" width="12" height="32" rx="5" class="hb"/><rect x="135" y="92" width="12" height="60" rx="5" class="hb"/>
<line x1="150" y1="52" x2="190" y2="52" class="ln"/><text x="194" y="56" class="ht">Freezer handle</text>
<line x1="150" y1="122" x2="190" y2="122" class="ln"/><text x="194" y="126" class="ht">Fridge handle</text>
<text x="160" y="214" class="t" text-anchor="middle">Handles only, not the refrigerator</text>'''),

 dict(slug='microwave-turntable-plate', name='Microwave turntable plate', group='Kitchen',
  short='The round glass plate that spins inside the microwave.',
  what='The turntable plate is the removable round glass tray that sits on a roller ring inside the microwave and rotates food while it heats. In RVs it is the part of the microwave most likely to break, because it is loose glass in a moving vehicle.',
  covered=['The glass turntable plate only, when broken accidentally while the vehicle is parked'],
  notcov=['The microwave unit, its door, electronics, or controls',
          'A plate that breaks while the vehicle is moving'],
  industry='Rental units commonly ask renters to remove and pad the glass plate before driving. Because breakage in transit is so common, rental damage schedules usually list the plate as a separate charge.',
  cost='Replacement glass plates commonly run about $15 to $50, matched to the microwave model.',
  tip='Before you drive, take the plate out and wrap it in a towel in a low cabinet. A plate broken in transit is not covered, because the Shield applies only while the vehicle is stationary.',
  ill='''<rect x="40" y="40" width="240" height="140" rx="10" class="f"/><rect x="58" y="56" width="160" height="108" rx="6" class="o2f"/>
<rect x="234" y="60" width="32" height="100" rx="4" class="o2f"/><circle cx="250" cy="80" r="5" class="o2"/><circle cx="250" cy="100" r="5" class="o2"/>
<ellipse cx="138" cy="136" rx="62" ry="16" class="hb"/><ellipse cx="138" cy="133" rx="48" ry="10" class="hl"/>
<line x1="170" y1="122" x2="196" y2="40" class="ln"/><text x="200" y="32" class="ht">Glass plate</text>
<text x="160" y="206" class="t" text-anchor="middle">Glass plate only, not the microwave</text>'''),

 dict(slug='interior-sliding-door', name='Interior sliding door off track', group='Doors and hardware',
  short='A bathroom or bedroom sliding or pocket door that has come off its track.',
  what='Many RVs use sliding or pocket doors for the bathroom and bedroom to save space. These doors hang on small rollers that run in a track, and a hard pull or slam can pop the rollers out so the door jams, drags, or falls loose.',
  covered=['Re-seating an interior sliding or pocket door that has come off its track',
           'Accidental damage to the door rollers or guides that keep it on the track'],
  notcov=['Slide-out room doors and slide-out mechanisms', 'Exterior entry doors and locks',
          'Doors damaged by force, misuse, or negligence'],
  industry='Off-track sliding doors are one of the most common RV service calls. Most are a quick adjustment rather than a replacement, which is why a review-first process often saves money.',
  cost='Often fixed with an adjustment. Replacement rollers or guides commonly run about $10 to $30.',
  tip='Slide the door gently and evenly. If it sticks, stop and report it rather than forcing it.',
  ill='''<rect x="40" y="30" width="240" height="12" rx="3" class="hb"/><text x="160" y="24" class="ht" text-anchor="middle">Track</text>
<rect x="60" y="42" width="200" height="146" rx="2" class="o2f"/>
<rect x="110" y="56" width="120" height="128" rx="4" class="f" transform="rotate(4 170 120)"/>
<circle cx="132" cy="50" r="7" class="hb"/><circle cx="214" cy="56" r="7" class="hb"/>
<rect x="208" y="112" width="8" height="26" rx="3" class="o2f" transform="rotate(4 170 120)"/>
<text x="160" y="214" class="t" text-anchor="middle">Door slipped off its rollers</text>'''),

 dict(slug='toilet-clog', name='Toilet clog (standard clearing)', group='Bathroom and plumbing',
  short='A standard clog in the RV toilet that can be cleared without pumping the tank.',
  what='RV toilets drop straight into a holding tank through a valve, using far less water than a home toilet. Too much toilet paper or not enough water can create a clog in the bowl or the outlet that a standard clearing will fix.',
  covered=['Standard clearing of a toilet clog'],
  notcov=['Blockages caused by foreign objects (wipes, hygiene products, paper towels) that require a pump-out',
          'Holding tank sensors, valves, and dumping', 'Sensor readings billable by the host'],
  industry='Rental companies commonly charge a cleaning or blockage fee for clogged RV toilets, and a larger fee when a tank must be professionally pumped.',
  cost=None,
  tip='Use only RV-safe, quick-dissolving toilet paper, keep some water in the bowl, and never flush anything else.',
  ill='''<rect x="118" y="26" width="84" height="54" rx="8" class="f"/><path d="M98 96 Q98 84 112 84 H208 Q222 84 222 96 Q222 140 182 150 H138 Q98 140 98 96 Z" class="f"/>
<ellipse cx="160" cy="98" rx="46" ry="10" class="o2f"/><rect x="138" y="150" width="44" height="30" class="f"/>
<circle cx="160" cy="166" r="11" class="hb"/><line x1="172" y1="166" x2="236" y2="166" class="ln"/><text x="240" y="170" class="ht">Outlet</text>
<rect x="104" y="180" width="112" height="12" rx="3" class="o2f"/>
<text x="160" y="212" class="t" text-anchor="middle">Standard clearing only</text>'''),

 dict(slug='minor-scratches-scuffs', name='Minor marks, scrapes, or scuffs', group='Surfaces',
  short='Small interior marks up to 3 inches, one location per occurrence.',
  what='Minor marks are small surface scratches, scrapes, or scuff marks on interior walls, cabinetry, or trim, such as a scrape from a suitcase corner or a scuff from a chair leg. The Shield covers a single mark up to 3 inches long in one location per occurrence.',
  covered=['One interior mark, scrape, or scuff up to 3 inches long', 'One location per occurrence'],
  notcov=['Marks longer than 3 inches, or damage in more than one location in the same occurrence',
          'Exterior body, paint, glass, or roof', 'Gouges, holes, burns, or stains', 'Pet or animal damage'],
  industry='Interior touch-ups are typically assessed at the turnover inspection and billed to the renter as a repair or cleaning charge, often with a minimum fee.',
  cost=None,
  tip='Carry luggage and coolers in rather than sliding them, and keep chair feet off cabinet faces.',
  ill='''<rect x="50" y="30" width="220" height="150" rx="6" class="f"/><line x1="160" y1="30" x2="160" y2="180" class="o"/>
<rect x="138" y="96" width="8" height="26" rx="3" class="o2f"/><rect x="174" y="96" width="8" height="26" rx="3" class="o2f"/>
<path d="M76 70 L132 60" class="hs"/><path d="M80 76 L128 67" class="hs" opacity=".55"/>
<line x1="76" y1="48" x2="132" y2="40" class="ln"/><line x1="76" y1="44" x2="76" y2="52" class="ln"/><line x1="132" y1="36" x2="132" y2="44" class="ln"/>
<text x="104" y="22" class="ht" text-anchor="middle">Max 3 in</text>
<text x="160" y="206" class="t" text-anchor="middle">One mark, one location per occurrence</text>'''),

 dict(slug='interior-hardware', name='Interior hardware', group='Doors and hardware',
  short='Cabinet latches, magnetic catches, drawer pulls, hinges, and handle screws.',
  what='Interior hardware is the small metal and plastic hardware that keeps cabinets and drawers working: push-button or travel latches, magnetic catches, drawer pulls and knobs, cabinet hinges, and the screws that hold handles in place. RV cabinetry is lightweight, so this hardware loosens or breaks more often than in a house.',
  covered=['Cabinet latches and magnetic catches', 'Drawer pulls and knobs', 'Cabinet hinges', 'Handle screws'],
  notcov=['Keys, fobs, and lock hardware', 'Cabinet doors, drawer boxes, or slides themselves', 'Damage from force or misuse'],
  industry='Hardware replacement is a common post-trip charge because RV latches and catches are often specialty parts sized to the cabinetry.',
  cost='Individual latches, catches, pulls, and hinges commonly run about $5 to $25 each, plus labor.',
  tip='Make sure every cabinet latch clicks shut before you drive, and do not hang weight on open cabinet doors.',
  ill='''<rect x="70" y="28" width="180" height="164" rx="6" class="f"/>
<rect x="64" y="44" width="10" height="28" rx="3" class="hb"/><rect x="64" y="150" width="10" height="28" rx="3" class="hb"/>
<rect x="216" y="96" width="14" height="40" rx="6" class="hb"/><circle cx="223" cy="104" r="2.5" class="dot"/><circle cx="223" cy="128" r="2.5" class="dot"/>
<rect x="138" y="30" width="44" height="12" rx="3" class="hb"/>
<text x="160" y="62" class="ht" text-anchor="middle">Latch</text><text x="96" y="114" class="ht">Hinges</text><text x="96" y="160" class="ht">Pull and screws</text>
<text x="160" y="212" class="t" text-anchor="middle">Latches, catches, pulls, hinges, screws</text>'''),

 dict(slug='window-blinds', name='Window blind slats or pull cords', group='Windows',
  short='Broken slats or pull cords on interior window blinds and shades.',
  what='RV windows typically use mini blinds or pleated day and night shades that are raised and lowered with pull cords or a cord tension system. Slats can snap and cords can fray or break, especially when one side is pulled harder than the other.',
  covered=['Accidentally broken blind slats', 'Accidentally broken or snapped pull cords'],
  notcov=['Window glass, frames, and seals', 'Water damage from open vents or windows', 'Wear such as fading or sun damage'],
  industry='Cord and shade repairs are a frequent turnover item for rental units because shades get daily use.',
  cost='Restring kits and replacement slats commonly run about $10 to $40. Full shade replacement costs more.',
  tip='Raise and lower shades evenly from the center rail and never yank a single cord.',
  ill='''<rect x="60" y="22" width="200" height="176" rx="8" class="o2f"/><rect x="72" y="34" width="176" height="12" rx="3" class="f"/>
<g class="slats"><rect x="74" y="52" width="172" height="8" rx="2" class="f"/><rect x="74" y="66" width="172" height="8" rx="2" class="f"/><rect x="74" y="80" width="172" height="8" rx="2" class="hb"/><rect x="74" y="94" width="172" height="8" rx="2" class="f"/><rect x="74" y="108" width="172" height="8" rx="2" class="f"/><rect x="74" y="122" width="172" height="8" rx="2" class="f"/></g>
<line x1="230" y1="46" x2="230" y2="170" class="hc"/><circle cx="230" cy="174" r="5" class="hb"/>
<text x="270" y="88" class="ht">Slat</text><text x="242" y="166" class="ht">Cord</text>
<text x="160" y="214" class="t" text-anchor="middle">Slats and pull cords</text>'''),

 dict(slug='shower-curtain-rod', name='Shower curtain rod or hooks', group='Bathroom and plumbing',
  short='The rod or hooks that hold the shower curtain.',
  what='Many RV showers use a tension rod, curved rod, or ceiling track with hooks or rings to hold the curtain. These pieces are lightweight and can bend, pop loose, or snap if pulled on or used for support.',
  covered=['Accidental breakage of the shower curtain rod or track', 'Accidental breakage of curtain hooks or rings'],
  notcov=['Shower walls, pan, surround, or glass doors', 'Water damage', 'The shower curtain fabric itself'],
  industry='Rods and hooks are typically billed at replacement cost after inspection, since they are usually sized to the specific shower.',
  cost='Replacement rods and hook sets commonly run about $10 to $40.',
  tip='Do not hang wet towels or clothing on the rod, and never use it for balance.',
  ill='''<rect x="40" y="38" width="240" height="10" rx="5" class="hb"/><circle cx="40" cy="43" r="8" class="f"/><circle cx="280" cy="43" r="8" class="f"/>
<g class="h2"><circle cx="72" cy="56" r="7"/><circle cx="112" cy="56" r="7"/><circle cx="152" cy="56" r="7"/><circle cx="192" cy="56" r="7"/><circle cx="232" cy="56" r="7"/></g>
<path d="M64 64 Q84 120 70 190 L250 190 Q236 120 256 64 Z" class="o2f"/>
<path d="M104 66 Q118 130 104 190 M144 66 Q158 130 144 190 M184 66 Q198 130 184 190 M224 66 Q238 130 224 190" class="o" fill="none"/>
<text x="160" y="28" class="ht" text-anchor="middle">Rod and hooks</text>
<text x="160" y="212" class="t" text-anchor="middle">Rod and hooks, not the curtain or shower</text>'''),

 dict(slug='cup-holders-interior-trim', name='Cup holders and small molded trim', group='Surfaces',
  short='Broken cup holders or small molded plastic interior trim pieces.',
  what='Cup holders and small molded trim pieces are the plastic components found throughout an RV interior, such as dash and dinette cup holders, outlet and switch trim rings, vent covers, and small decorative end caps.',
  covered=['Broken cup holders', 'Small molded interior trim components'],
  notcov=['Dashboards, large panels, or cabinetry', 'Seats and upholstery', 'TV, audio, or entertainment system units'],
  industry='Small trim pieces are commonly listed on rental damage schedules at replacement cost and are often model-specific parts.',
  cost='Cup holders and small trim pieces commonly run about $5 to $40 each.',
  tip='Remove drinks from cup holders before driving or moving the unit.',
  ill='''<path d="M70 120 H250 V164 Q250 180 234 180 H86 Q70 180 70 164 Z" class="f"/>
<ellipse cx="128" cy="120" rx="34" ry="10" class="hb"/><ellipse cx="200" cy="120" rx="34" ry="10" class="hb"/>
<path d="M188 120 L192 60 H226 L230 120" class="o2f"/><rect x="190" y="52" width="38" height="10" rx="3" class="f"/>
<rect x="100" y="148" width="36" height="16" rx="5" class="hl"/>
<text x="128" y="100" class="ht" text-anchor="middle">Cup holder</text><text x="160" y="160" class="ht">Trim piece</text>
<text x="160" y="206" class="t" text-anchor="middle">Small molded plastic parts</text>'''),

 dict(slug='fresh-water-hose', name='Fresh water hose and grommet', group='Hookups', new=True,
  short='The drinking-water hose that connects the RV to a water spigot, and its rubber washer.',
  what='The fresh water hose is a drinking-water-safe hose, usually white or blue, that connects a campground spigot to the RV\'s city water inlet. The grommet is the small rubber washer inside each hose fitting that creates the seal; when it is missing or torn, the connection leaks.',
  covered=['The fresh (drinking) water hose', 'Hose grommets (rubber washers) in the fittings'],
  notcov=['Water damage of any kind', 'The RV water pump, lines, tanks, or water heater', 'Using the fresh water hose for anything other than drinking water'],
  industry='Rental units typically include a dedicated drinking-water hose, and lost or damaged hoses are a common checkout charge.',
  cost='Drinking-water hoses commonly run about $20 to $50. Grommets cost a few dollars.',
  tip='Use the pressure regulator if the unit has one, coil the hose when you leave, and never use it to rinse the sewer hose.',
  ill='''<g fill="none" class="hc"><ellipse cx="130" cy="110" rx="78" ry="62"/><ellipse cx="130" cy="110" rx="62" ry="48"/><ellipse cx="130" cy="110" rx="46" ry="34"/></g>
<path d="M208 110 Q240 110 244 140" class="hc" fill="none"/>
<rect x="232" y="140" width="24" height="26" rx="4" class="f"/><ellipse cx="244" cy="172" rx="14" ry="5" class="hb"/>
<line x1="258" y1="172" x2="276" y2="190" class="ln"/><text x="232" y="206" class="ht">Grommet</text>
<text x="60" y="206" class="ht">Fresh water hose</text>'''),

 dict(slug='septic-hose-adaptor', name='Septic (sewer) hose and adaptor', group='Hookups', new=True,
  short='The flexible sewer hose and the fittings that connect it to the RV and the dump station.',
  what='The septic or sewer hose is a flexible, ribbed hose, usually 3 inches wide, used to drain the RV\'s black and gray holding tanks. Adaptors are the fittings on each end: a bayonet or lug fitting that locks onto the RV\'s waste outlet, and an elbow or threaded adaptor that seats into the dump station or campsite sewer.',
  covered=['The sewer hose', 'Sewer hose adaptors and fittings'],
  notcov=['Holding tanks, valves, and tank sensors', 'Spill cleanup or environmental fees', 'Foreign-object blockages that require a pump-out'],
  industry='Sewer hoses wear out and puncture easily, so most rentals list them on the damage schedule, and many require the renter to return them rinsed.',
  cost='Sewer hose kits commonly run about $30 to $100 depending on length and fittings.',
  tip='Carry the hose instead of dragging it, dump the black tank first and the gray tank second, and rinse the hose before storing it.',
  ill='''<path d="M60 70 Q130 60 170 110 Q210 160 262 150" fill="none" class="rib"/>
<path d="M60 70 Q130 60 170 110 Q210 160 262 150" fill="none" class="ribd"/>
<rect x="30" y="54" width="34" height="34" rx="6" class="hb"/><rect x="24" y="62" width="8" height="18" rx="2" class="f"/>
<path d="M258 136 H278 Q290 136 290 148 V190 H270 V156 H258 Z" class="hb"/>
<text x="30" y="44" class="ht">Bayonet adaptor</text><text x="196" y="204" class="ht">Elbow adaptor</text>
<text x="58" y="160" class="t">Sewer hose</text>'''),

 dict(slug='stabilizer-jack-crank', name='Stabilizer jack hand-crank', group='Hookups', new=True,
  short='The removable crank handle used to raise and lower a trailer\'s stabilizer jacks.',
  what='Travel trailers and fifth wheels have scissor-style stabilizer jacks at the corners that are lowered at camp to reduce bounce and sway. The hand-crank is the removable L-shaped handle that turns the jack screw to raise and lower them. It is easy to leave behind at a campsite.',
  covered=['A missing or broken stabilizer jack hand-crank'],
  notcov=['The stabilizer jacks themselves', 'Tongue jacks, power jacks, and leveling systems', 'Damage from driving with jacks down'],
  industry='Stabilizer jacks are for steadying only, not lifting or leveling. Damage from misusing them is usually a renter charge, and lost cranks are a common checkout item.',
  cost='Replacement crank handles commonly run about $10 to $30.',
  tip='Use the jacks to steady the trailer only, never to lift or level it, and put the crank back in its compartment before you leave.',
  ill='''<rect x="30" y="40" width="260" height="14" rx="3" class="f"/>
<path d="M96 54 L176 140 M176 54 L96 140" class="o" stroke-width="6"/><rect x="80" y="140" width="112" height="12" rx="3" class="f"/>
<line x1="70" y1="97" x2="200" y2="97" class="o"/>
<path d="M200 97 H252 V140" class="hc" fill="none" stroke-width="7"/><rect x="242" y="140" width="20" height="30" rx="6" class="hb"/>
<text x="200" y="196" class="ht">Hand-crank</text><text x="78" y="178" class="t">Stabilizer jack</text>'''),

 dict(slug='tv-remote', name='TV remote', group='Electronics', new=True,
  short='A missing or broken remote control for the unit\'s TV.',
  what='The TV remote is the handheld remote control for the television installed in the RV. RV televisions are often 12-volt models with brand-specific remotes, and remotes are one of the items most often left behind or broken.',
  covered=['A missing TV remote', 'A broken TV remote'],
  notcov=['The TV, antenna, or satellite equipment', 'Audio, stereo, or other entertainment system units', 'Batteries'],
  industry='Missing remotes are a standard line item on rental checkout inventories and are typically charged at replacement cost.',
  cost='Replacement remotes commonly run about $10 to $40. Brand-specific remotes can cost more.',
  tip='Keep the remote in the same spot during your stay and check for it during your departure walkthrough.',
  ill='''<rect x="128" y="20" width="64" height="180" rx="18" class="hb"/>
<circle cx="160" cy="46" r="8" class="dotr"/>
<g class="btns"><circle cx="146" cy="76" r="6"/><circle cx="174" cy="76" r="6"/><circle cx="146" cy="98" r="6"/><circle cx="174" cy="98" r="6"/><circle cx="146" cy="120" r="6"/><circle cx="174" cy="120" r="6"/></g>
<rect x="148" y="140" width="24" height="40" rx="10" class="btnw"/>
<text x="210" y="110" class="ht">Remote only</text>
<text x="160" y="214" class="t" text-anchor="middle">Not the TV or entertainment unit</text>'''),

 dict(slug='faucet-fixtures', name='Sink, shower, or tub faucet fixtures', group='Bathroom and plumbing', new=True,
  short='Faucet handles, spouts, and shower fixtures damaged by accident.',
  what='Faucet fixtures are the visible parts of the RV\'s sinks, shower, and tub that you touch and turn: faucet handles, spouts, aerators, and shower heads or hand-held shower wands. RV fixtures are usually lighter-duty plastic or metal and can crack or snap under force.',
  covered=['Accidental damage to sink faucet fixtures', 'Accidental damage to shower or tub faucet fixtures'],
  notcov=['Water lines, plumbing behind walls, the water pump, or water heater', 'Water damage of any kind', 'Sinks, tubs, and shower pans'],
  industry='Fixture repairs are commonly billed to renters at parts plus labor after inspection, since RV fixtures often differ from household sizes.',
  cost='RV faucet fixtures commonly run about $25 to $100, plus labor.',
  tip='Turn handles gently to the stop and never use a faucet or shower wand to pull yourself up.',
  ill='''<rect x="40" y="150" width="240" height="40" rx="6" class="f"/><ellipse cx="160" cy="150" rx="80" ry="12" class="o2f"/>
<rect x="148" y="96" width="24" height="56" rx="4" class="hb"/><path d="M160 100 Q160 64 200 64 H220 V82 H204 Q182 82 182 104" class="hb"/>
<rect x="112" y="122" width="30" height="14" rx="4" class="hb"/><rect x="178" y="122" width="30" height="14" rx="4" class="hb"/>
<text x="226" y="70" class="ht">Spout</text><text x="88" y="114" class="ht">Handles</text>
<text x="160" y="212" class="t" text-anchor="middle">Fixtures only, not plumbing or water damage</text>'''),

 dict(slug='courtesy-service-call', name='One courtesy mobile service call', group='Service',
  short='One visit from a mobile technician, if the host chooses to provide it.',
  what='A mobile service call is a visit from an RV technician to wherever the unit is parked, to diagnose or repair an issue on site instead of towing the RV to a shop. With the Shield, the host may provide one courtesy service call at the host\'s sole discretion.',
  covered=['One courtesy mobile service call, when provided by the host at the host\'s sole discretion'],
  notcov=['Additional service calls beyond the first', 'Towing or roadside assistance', 'Repairs to items that are not covered'],
  industry='Mobile RV technicians commonly charge a trip or call-out fee before any labor or parts, which on its own can exceed the cost of a small repair.',
  cost='Mobile trip fees are often around $100 to $200 before labor, depending on the market and distance.',
  tip='Call or text the host first. They may route you to a pre-screened technician from the Stress Free Shield service network.',
  ill='''<path d="M40 150 V96 Q40 84 52 84 H190 L230 112 H270 Q282 112 282 124 V150 Z" class="f"/>
<rect x="196" y="92" width="26" height="20" rx="3" class="o2f"/><circle cx="92" cy="156" r="18" class="f"/><circle cx="232" cy="156" r="18" class="f"/>
<circle cx="92" cy="156" r="7" class="o2f"/><circle cx="232" cy="156" r="7" class="o2f"/>
<path d="M104 112 l18 -18 a10 10 0 1 1 8 8 l-18 18 a6 6 0 1 1 -8 -8z" class="hb"/>
<text x="160" y="204" class="t" text-anchor="middle">One call, at the host's discretion</text>'''),

 dict(slug='supply-kit-items', name='Missing interior supply kit items', group='Supplies',
  short='Small items from the unit\'s interior supply bin that go missing.',
  what='The interior supply kit is the small bin of everyday items packed with the unit for guests to use during the trip. The Shield covers small items from that bin that are missing at checkout.',
  covered=['Missing small items from the interior supply bin'],
  notcov=['Larger equipment and anything outside the small supply bin', 'Theft of any items', 'Consumables used up as intended'],
  industry='Rentals commonly check supply kits against an inventory at checkout and charge replacement cost for missing items.',
  cost=None,
  tip='Repack the bin before checkout and keep it where you found it.',
  ill='''<path d="M62 92 H258 L244 186 Q242 196 232 196 H88 Q78 196 76 186 Z" class="f"/><rect x="54" y="80" width="212" height="16" rx="4" class="f"/>
<rect x="92" y="44" width="30" height="44" rx="4" class="hb"/><circle cx="160" cy="62" r="20" class="hb"/><rect x="196" y="50" width="34" height="38" rx="4" class="hb"/>
<text x="160" y="150" class="t" text-anchor="middle">Supply bin</text>
<text x="160" y="214" class="t" text-anchor="middle">Small bin items only</text>'''),
]
