# Notebook Knight — Repeatable Armor Art Workflow

Why this exists: ChatGPT image generation can't hit a pixel-perfect canvas position from a text
prompt alone — every new piece still needs a manual scale/position pass once it comes back
(exactly what happened with the Rusty Sword and Quilted Vest). What text + a reference image
*can* lock down reliably is the pose, proportions, camera framing, and art style. If those four
things match every time, the alignment pass afterward becomes fast and mechanical instead of a
guessing game. That's the whole point of this workflow.

## Step 1 — Always attach the reference sheet

Two reference images are in this folder:
- `chr_reference_male_default.png`
- `chr_reference_female_default.png`

These are the actual in-game body (frame + head + default tunic + default boots), rendered flat
on white. The body itself is shared across genders now (only the head layer differs), so armor
art doesn't need separate male/female versions - attach `chr_reference_male_default.png` (the
default choice) to every ChatGPT image request; this is what keeps the pose, scale, and camera
angle locked across every item you generate, even months apart. The female sheet is kept around
mainly for reference/comparison, or for the rare case an item is meant to look different on the
female head specifically (e.g. hair-dependent helmets).

If ChatGPT supports it in your session, keep re-using the *same conversation thread* for a batch
of related items (e.g. all the chest armors in one thread) rather than starting fresh each time —
image models are noticeably more consistent when they can reference their own prior output, not
just a re-uploaded image.

## Step 2 — Prompt template (fill in the bracketed parts)

```
Here is the reference character (attached). Draw the exact same character - same chibi
proportions, same three-quarter pose facing slightly left, arms hanging naturally at the sides,
same head/hair/face.

ART STYLE - match the reference exactly, this is the most important instruction: rough,
hand-drawn pencil-and-ink sketch linework, visible pencil texture and cross-hatching for
shading, like a page torn from a sketchbook. This is a FLAT LINE DRAWING, not a painted or
rendered illustration - do not add smooth painterly shading, soft airbrush gradients, dramatic
rim lighting, glow effects, or a dark vignette background.

Now show them wearing [ITEM NAME]: [1-2 sentence description of the armor - material, silhouette,
distinguishing details, condition/wear].

Rules:
- Keep the pose, camera framing, and character scale IDENTICAL to the reference image.
- Only change the [SLOT AREA, e.g. "chest/torso covering" or "boots/lower legs"]. Everything else
  (head, hair, face, arms, hands, other leg wear, stance) should match the reference exactly.
- [If chest]: the piece should cover the torso down to roughly [hip / mid-thigh] like the
  reference's own tunic does - it's the only visible torso covering, so it needs to read as a
  complete garment on its own, not as an accessory layered over a shirt. If it's meant to be a
  substantial armor upgrade (metal/plate/scale, not cloth), also extend matching leg armor
  (greaves) down over the shins so the character doesn't look armored on top and bare-legged
  below - see the Notes section for which items warrant this.
- Background must be a single flat plain light color (light gray or white, no gradient, no
  vignette, no glow) exactly like the reference image's plain background, OR fully transparent -
  never an atmospheric/rendered background.
```

## Alternative: batch/single-sheet generation (preferred - gave better consistency for the town
## button icons)

Generating items one request at a time can drift in style/proportions between requests, even
with the same reference attached each time. Putting several items on one sheet in a single
request keeps the model looking at its own in-progress output as it goes, which holds
proportions and style together much better. Use this approach instead of Step 2 when generating
more than one or two items in a sitting.

Template:

```
Here is the reference character (attached). I need [N] versions of them, arranged in a clean
grid on one sheet, each in the exact same three-quarter pose facing slightly left, arms hanging
naturally at the sides, same head/hair/face/proportions - only the [SLOT AREA] (and matching leg
armor where noted) changes between panels.

ART STYLE - match the reference exactly, this is the most important instruction: rough,
hand-drawn pencil-and-ink sketch linework, visible pencil texture and cross-hatching for
shading, like a page torn from a sketchbook. This is a FLAT LINE DRAWING, not a painted or
rendered illustration - do not add smooth painterly shading, soft airbrush gradients, dramatic
rim lighting, glow effects, or a dark vignette background. The background must be a single flat
plain light color (light gray or white, no gradient, no vignette, no glow) exactly like the
reference image's plain background - nothing atmospheric.

For substantial armor-tier panels (metal/plate/scale, not cloth or deliberately-minimal items),
extend matching leg armor down onto the shins so the character doesn't look armored on top and
bare-legged below - note per-panel below which items warrant this and which don't (light cloth
pieces and robes usually don't need separate greaves; anything metal/plate/scale usually does).

Panel 1: [Item 1 name] - [1-2 sentence description, note leg armor yes/no].
Panel 2: [Item 2 name] - [1-2 sentence description, note leg armor yes/no].
Panel 3: [Item 3 name] - [1-2 sentence description, note leg armor yes/no].
...

Keep every panel's pose, camera framing, and character scale identical so they can be cut apart
and compared directly - no panel should be zoomed, rotated, or scaled differently than the
others. Plain flat background per panel as described above, clean gaps or dividers between
panels so each character can be cropped out cleanly.
```

Practical notes:
- Keep batches to around 3-6 items per sheet — enough for the model to stay consistent, but not
  so many that each character gets too small to show real linework/shading detail. Run multiple
  sheets back to back rather than cramming everything into one image.
- One sheet per batch is enough — no need to duplicate per gender, since the body is shared.
- A flat background color instead of transparency-per-panel is fine and often more reliable —
  it's easy for me to key out a flat color during the alignment pass, and asking for
  per-panel transparency on a multi-panel sheet is where models are most likely to mess up.
- Send me the whole sheet along with which panel is which item — I'll crop each character out
  individually and run the same per-item alignment pass as Step 3 below.

## Step 3 — Send the result back for alignment

Once you have the image(s), hand them to me. I'll:
1. Measure the character's shoulder width / collar position / hem position against the known
   in-game body proportions.
2. Scale and position the art onto the 1024x1536 canvas so it lines up with the shared body
   layer, the same way the Rusty Sword and Quilted Vest were done.
3. Composite it over the actual bare-body/frame art and show you the result before it's wired
   into the game, so we catch alignment problems before they're live.

You don't need to worry about hitting exact pixel dimensions or canvas alignment yourself -
matching the pose/style/framing in steps 1-2 is what makes step 3 fast.

## Notes on style consistency

- Match the *Quilted Vest's* rendering style (soft pencil shading, cross-hatching, texture) - not
  the flatter, no-shading doodle style used for the NPC portrait sketches. Those are two
  deliberately different art styles for two different UI purposes; equipment art should always
  look like the vest, not like an NPC doodle.
- Known failure mode: even with the reference attached, ChatGPT can drift toward a smooth
  painterly render with a glowing/vignette background instead of the flat pencil-sketch style -
  this happened on the first chest-armor batch attempt. The explicit "FLAT LINE DRAWING, not
  painted" and "no vignette/glow background" language in the templates above exists specifically
  to correct for this - don't drop those lines even though they look repetitive.
- Bare legs under fully-armored torsos reads oddly once several tiers exist side by side. Default
  to giving metal/plate/scale chest pieces matching leg armor (greaves) down the shins; cloth
  robes and deliberately minimal/stealthy pieces are the exception and can stay bare-legged if
  that fits the item's flavor.
- Keep material/condition language consistent with each item's in-game flavor text and rarity
  tier where you have it (e.g. starter-tier gear should look cheap/homespun; higher-tier gear can
  look more refined/ornate) - this isn't required for the art to work, but it keeps the shop and
  equipment screens feeling coherent as more items stack up.

## What's actually left to generate

The item list is large (~100+ weapons/armor pieces across all rarity tiers), so there's no need
to batch-generate everything at once. A sensible order, following the same "starter gear first"
pattern as the vest and sword:
- **Chest** (16 items, `chs_*`): next few tiers after the Quilted Vest - Leather Armor, Copper
  Breastplate, Bronze Breastplate, etc.
- **Boots** (10 items, `bts_*`): first-ever boots art, starting with Worn Boots / Leather Boots.
- **Helmets** (11 items, `hlm_*`): will need a decision on how they interact with hair (flagged
  earlier) before generating - worth doing a first test piece before committing to a batch.
- **Weapons** (~60 items across dagger/sword/shortsword/longsword/greatsword/axe/greataxe/
  mace/hammer/spear/greatspear/bow/shortbow/crossbow/wand/staff): biggest category by far. One
  held-weapon pose already works (Rusty Sword), but bows/staves/wands are held differently and
  will need their own reference test before mass-producing that class.

Just say which item (or batch) you want to tackle next and I'll pull its name/description/rarity
from the item data so the prompt is accurate, rather than you needing to retype it.
