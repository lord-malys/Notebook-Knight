# Notebook Knight — NPC Portrait Sketch Prompts (Round 5)

Context: the shared NPC dialogue panel (`ui_panel_npc_dialogue_clean.png`) has an empty corner
reserved in its header zone — the `.npc-header` text box only occupies `left: 6%` to `right: 15%`
of the panel width, in the top 20%–58% band. That leaves an unused ~15%-wide, ~38%-tall slot in
the top-right of the name/role area (roughly 200×240px at the panel's native 1350×630 resolution,
~5:6 portrait aspect ratio) — a natural spot for a small per-NPC doodle portrait next to their
name and title. **Note: this slot is currently empty CSS space, not yet wired to display an
image** — these prompts are prep for that art; hooking a portrait into `renderNpcPanel` is a
follow-up code change once art exists.

Each prompt below is self-contained — paste one at a time into ChatGPT image generation.

**Known gotcha:** ChatGPT/DALL-E image gen frequently ignores "transparent background" instructions
and renders on flat white instead. If that happens, run the result through a background remover
(remove.bg, Photopea's magic eraser, etc.) before dropping it in `01_Art/Approved/UI/` — don't
assume the first output is already transparent.

## Shared style block (repeated in every prompt below)

Simple black-and-white pencil/ink sketch, loose and slightly wobbly hand-drawn line art — like a
quick notebook-margin doodle, not a finished illustration. Line work only: no shading, no
cross-hatch fills, no color, no gray fill tones, no background of any kind. Every pixel that isn't
a drawn line must be fully transparent (transparent PNG) — do not fill in skin, hair, or clothing
with flat color or tone; leave those areas as bare transparency, suggested only by outline and a
few interior detail strokes, the way a fast pencil sketch implies form without filling it in. Bust
portrait (head and shoulders only), roughly 5:6 portrait aspect ratio, character facing slightly
to the left (three-quarter angle), as if glancing toward their own name plate. Same rough pencil
line weight and quick, confident sketch style throughout.

---

## 1. Bertram Holt — Innkeeper

Simple black-and-white pencil/ink sketch, loose and slightly wobbly hand-drawn line art — like a
quick notebook-margin doodle, not a finished illustration. Line work only: no shading, no
cross-hatch fills, no color, no gray fill tones, no background of any kind. Every pixel that isn't
a drawn line must be fully transparent (transparent PNG) — do not fill in skin, hair, or clothing
with flat color or tone; leave those areas as bare transparency, suggested only by outline and a
few interior detail strokes. Bust portrait, roughly 5:6 portrait aspect ratio, facing slightly
left, three-quarter angle.

Subject: a middle-aged, broad-shouldered innkeeper. Thick neck, heavy build, warm and genial
expression with a small smile. Balding or short hair, a modest mustache. Simple apron ties sketched
at the shoulders/collar as a couple of outline strokes (not filled). A few small ink-smudge scribble
marks on one hand or sleeve cuff.

## 2. Aldra Ironmark — Master Smith

Simple black-and-white pencil/ink sketch, loose and slightly wobbly hand-drawn line art — like a
quick notebook-margin doodle, not a finished illustration. Line work only: no shading, no
cross-hatch fills, no color, no gray fill tones, no background of any kind. Every pixel that isn't
a drawn line must be fully transparent (transparent PNG) — do not fill in skin, hair, or clothing
with flat color or tone; leave those areas as bare transparency, suggested only by outline and a
few interior detail strokes. Bust portrait, roughly 5:6 portrait aspect ratio, facing slightly
left, three-quarter angle.

Subject: a short, powerfully built woman blacksmith. Thick neck, strong jaw, hair pulled back tight
in a practical knot or bandana. A small scar sketched as a single line across one eyebrow or cheek.
Broad shoulders, a simple leather apron strap outline over one shoulder. Confident, weathered
expression.

## 3. Sister Maeve — Keeper of the Church

Simple black-and-white pencil/ink sketch, loose and slightly wobbly hand-drawn line art — like a
quick notebook-margin doodle, not a finished illustration. Line work only: no shading, no
cross-hatch fills, no color, no gray fill tones, no background of any kind. Every pixel that isn't
a drawn line must be fully transparent (transparent PNG) — do not fill in skin, hair, or clothing
with flat color or tone; leave those areas as bare transparency, suggested only by outline and a
few interior detail strokes. Bust portrait, roughly 5:6 portrait aspect ratio, facing slightly
left, three-quarter angle.

Subject: a quiet, watchful church keeper/nun. Simple hood or wimple framing the face, drawn in
outline only. Calm, downward-tilted, observant eyes. A small pendant or holy symbol on a cord at
the neckline, sketched as a couple of simple line shapes. Serene, still expression.

## 4. Oswin Vane — Head Librarian

Simple black-and-white pencil/ink sketch, loose and slightly wobbly hand-drawn line art — like a
quick notebook-margin doodle, not a finished illustration. Line work only: no shading, no
cross-hatch fills, no color, no gray fill tones, no background of any kind. Every pixel that isn't
a drawn line must be fully transparent (transparent PNG) — do not fill in skin, hair, or clothing
with flat color or tone; leave those areas as bare transparency, suggested only by outline and a
few interior detail strokes. Bust portrait, roughly 5:6 portrait aspect ratio, facing slightly
left, three-quarter angle.

Subject: a thin, ink-stained librarian. Round spectacles, messy uneven hair sticking out in a few
directions. Distracted gaze, looking slightly off to one side rather than at the viewer. A couple
of small ink-smudge scribble marks on one cheek or on the fingers. A quill tucked behind one ear,
drawn as a simple line shape.

## 5. Pip Corder — General Merchant

Simple black-and-white pencil/ink sketch, loose and slightly wobbly hand-drawn line art — like a
quick notebook-margin doodle, not a finished illustration. Line work only: no shading, no
cross-hatch fills, no color, no gray fill tones, no background of any kind. Every pixel that isn't
a drawn line must be fully transparent (transparent PNG) — do not fill in skin, hair, or clothing
with flat color or tone; leave those areas as bare transparency, suggested only by outline and a
few interior detail strokes. Bust portrait, roughly 5:6 portrait aspect ratio, facing slightly
left, three-quarter angle.

Subject: a cheerful, quick-talking merchant with a sly, easy grin. Slightly foxy, sharp features.
A jaunty cap or neckerchief sketched with a couple of loose lines. Bright, mischievous eyes. A
small coin-pouch string looping over one shoulder, drawn minimally.

## 6. Commander Ressa Vale — Guildmaster

Simple black-and-white pencil/ink sketch, loose and slightly wobbly hand-drawn line art — like a
quick notebook-margin doodle, not a finished illustration. Line work only: no shading, no
cross-hatch fills, no color, no gray fill tones, no background of any kind. Every pixel that isn't
a drawn line must be fully transparent (transparent PNG) — do not fill in skin, hair, or clothing
with flat color or tone; leave those areas as bare transparency, suggested only by outline and a
few interior detail strokes. Bust portrait, roughly 5:6 portrait aspect ratio, facing slightly
left, three-quarter angle.

Subject: a retired woman knight and guildmaster with a flat, permanently unimpressed expression.
An eyepatch over one eye (a simple oval plus strap lines). Short, practical hair. A stiff high
collar or gorget shape at the neckline, sketched with a few clean lines. Stern jaw, minimal detail.

## 7. Dorn Fennick — Armorer

Simple black-and-white pencil/ink sketch, loose and slightly wobbly hand-drawn line art — like a
quick notebook-margin doodle, not a finished illustration. Line work only: no shading, no
cross-hatch fills, no color, no gray fill tones, no background of any kind. Every pixel that isn't
a drawn line must be fully transparent (transparent PNG) — do not fill in skin, hair, or clothing
with flat color or tone; leave those areas as bare transparency, suggested only by outline and a
few interior detail strokes. Bust portrait, roughly 5:6 portrait aspect ratio, facing slightly
left, three-quarter angle.

Subject: a meticulous, soft-spoken armorer. Neat, tidy hair and a trim mustache, calm and precise
expression, small round spectacles. A tailor's measuring tape draped loosely over one shoulder — a
single wavy line with a few small tick marks. Composed, careful posture.
