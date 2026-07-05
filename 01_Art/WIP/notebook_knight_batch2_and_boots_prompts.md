# Notebook Knight — Batch 2 Armor + All Boots (Combo Sheets)

## Why combo panels instead of a boots-only batch

Putting a chest item and a boots item in the *same* drawing solves the exact problem we kept
hand-fixing on Iron Plate (fade/overlap at the ankle): if both pieces come from one drawing, the
two extracted layers are guaranteed to line up at the ankle, because they're literally the same
linework split in two, not two separately-generated assets I have to reconcile by eye.

Cramming 5 chest items + all 10 boots onto one sheet (15 panels) would blow past the 3-6-panel
sweet spot that's kept the last few batches consistent — more panels means smaller characters and
more drift. So this is two 5-panel sheets instead of one 15-panel sheet. Each Batch 2 armor
appears once per sheet, paired with a different boots item each time, so all 10 boots get
generated across the two sheets. Same total amount of ChatGPT generation, just split for quality.

**Extraction plan once you send these back:** for each panel I'll crop it twice — once as the
chest+greave layer (same fade-trim technique as Iron Plate, stopping just above the boot), and
once as the boots layer (isolating just the foot/shoe shape). Because both crops come from the
same source image, the ankle interface matches automatically. The boots layer becomes a normal
independent `EQUIP_ART_V2.boots` asset afterward — it'll composite correctly under *any* chest
piece, not just the one it was drawn next to.

## New rule for boots panels specifically

The existing "no feet" rule for chest-armor panels stays the same (greaves stop at the ankle,
never draw the actual foot/shoe). Boots panels are the opposite: they should draw the actual
foot/shoe shape in full, extending up to roughly mid-shin, so there's generous overlap with where
the chest art's greave fades out — that overlap is what makes the two crops splice cleanly.

---

## Sheet A

Reference: attach `chr_reference_male_default.png`.

```
Here is the reference character (attached). I need 5 versions of them, arranged in a clean grid
on one sheet, each in the exact same three-quarter pose facing slightly left, arms hanging
naturally at the sides, same head/hair/face/proportions - only the chest/torso covering and the
boots/lower-leg covering change between panels.

ART STYLE - match the reference exactly, this is the most important instruction: rough,
hand-drawn pencil-and-ink sketch linework, visible pencil texture and cross-hatching for
shading, like a page torn from a sketchbook. This is a FLAT LINE DRAWING, not a painted or
rendered illustration - do not add smooth painterly shading, soft airbrush gradients, dramatic
rim lighting, glow effects, or a dark vignette background. The background must be a single flat
plain light color (light gray or white, no gradient, no vignette, no glow) exactly like the
reference image's plain background - nothing atmospheric.

Each panel shows a full character wearing BOTH a chest garment and a pair of boots together (see
pairings below). The chest piece covers the torso down to roughly hip/upper-thigh (robes may fall
longer, to mid-thigh). For plate-armor chest pieces, also extend matching leg armor down onto the
shins - but stop above the ankle, do NOT draw the foot/shoe shape as part of the chest piece; the
boots below handle the foot. The boots themselves should be drawn in full, covering the actual
foot/shoe shape and extending up to roughly mid-shin, generously overlapping where the chest
piece's leg armor leaves off - this overlap is intentional and needed.

Panel 1: Scholar's Robes + Worn Boots. Robes: a light, flowing robe/tunic falling to mid-thigh,
simple rune symbols stitched along the hem and collar, soft draped cloth folds, a caster's outfit
not a warrior's. Boots: simple scuffed leather boots, worn-in and comfortable-looking, no
ornamentation, entry-level condition.

Panel 2: Steel Plate + Copper Greaves. Chest: a well-crafted steel breastplate, cleaner and
sharper linework than basic iron plate, subtle embossed detail lines, a brighter polished steel
tone. Include matching polished steel greaves over the shins, stopping above the ankle. Boots:
a basic copper-toned pair of foot-guards, simple rounded plates over the shins and feet, dull
warm metal sheen, entry-level protective boots.

Panel 3: Emberplate + Swift Boots. Chest: dark plate armor with faint glowing ember-like cracks
or rune lines scribbled across its surface, a subtle flame motif etched into the metal. Include
matching dark greaves with the same faint ember cracks continuing down the shins, stopping above
the ankle. Boots: light, simple boots drawn with quick loose pencil strokes, low-profile and
nimble-looking, built for speed rather than protection.

Panel 4: Froststeel Plate + Iron Greaves. Chest: pale, frost-blue tinted steel plate armor with
icy crystalline texture or frost patterns etched into the surface, sharper angular plate edges.
Include matching frost-blue greaves over the shins, stopping above the ankle. Boots: heavy iron
foot armor, thick and fully enclosing, riveted seams, duller gray-iron tone, conveys real weight
and thorough coverage.

Panel 5: Arcane Vestments + Leather Boots. Chest: an ornate mage's robe, heavier and more
elaborate than plain robes, glowing rune patterns woven through the fabric, richer layered drape,
small glowing sigils as embellishment. Boots: well-stitched plain leather boots, a reliable and
unremarkable pair, no ornamentation.

Keep every panel's pose, camera framing, and character scale identical so they can be cut apart
and compared directly - no panel zoomed, rotated, or scaled differently. Plain flat light
background per panel as described above, clean gaps between panels so each character can be
cropped out cleanly.
```

---

## Sheet B

Same reference sheet. Same 5 Batch 2 chest items, paired with the remaining 5 boots this time.

```
Here is the reference character (attached). I need 5 versions of them, arranged in a clean grid
on one sheet, each in the exact same three-quarter pose facing slightly left, arms hanging
naturally at the sides, same head/hair/face/proportions - only the chest/torso covering and the
boots/lower-leg covering change between panels.

ART STYLE - match the reference exactly, this is the most important instruction: rough,
hand-drawn pencil-and-ink sketch linework, visible pencil texture and cross-hatching for
shading, like a page torn from a sketchbook. This is a FLAT LINE DRAWING, not a painted or
rendered illustration - do not add smooth painterly shading, soft airbrush gradients, dramatic
rim lighting, glow effects, or a dark vignette background. The background must be a single flat
plain light color (light gray or white, no gradient, no vignette, no glow) exactly like the
reference image's plain background - nothing atmospheric.

Each panel shows a full character wearing BOTH a chest garment and a pair of boots together (see
pairings below). The chest piece covers the torso down to roughly hip/upper-thigh (robes may fall
longer, to mid-thigh). For plate-armor chest pieces, also extend matching leg armor down onto the
shins - but stop above the ankle, do NOT draw the foot/shoe shape as part of the chest piece; the
boots below handle the foot. The boots themselves should be drawn in full, covering the actual
foot/shoe shape and extending up to roughly mid-shin, generously overlapping where the chest
piece's leg armor leaves off - this overlap is intentional and needed.

Panel 1: Scholar's Robes + Fleet Runners. Robes: a light, flowing robe/tunic falling to mid-thigh,
simple rune symbols stitched along the hem and collar, soft draped cloth folds, a caster's outfit
not a warrior's. Boots: sleek, streamlined steel-toned boots built for speed, close-fitting with
minimal bulk, a few sharp linework accents suggesting agility and quick footing.

Panel 2: Steel Plate + Steel Sabatons. Chest: a well-crafted steel breastplate, cleaner and
sharper linework than basic iron plate, subtle embossed detail lines, a brighter polished steel
tone. Include matching polished steel greaves over the shins, stopping above the ankle. Boots:
full-foot steel plate armor, articulated segmented plating over the entire foot, excellent
coverage, matching polish and tone to the breastplate.

Panel 3: Emberplate + Shadow Treads. Chest: dark plate armor with faint glowing ember-like cracks
or rune lines scribbled across its surface, a subtle flame motif etched into the metal. Include
matching dark greaves with the same faint ember cracks continuing down the shins, stopping above
the ankle. Boots: dark, almost featureless soft-soled boots that look woven from solid shadow or
smoke, silent and minimal, faint smoky wisp lines at the edges.

Panel 4: Froststeel Plate + Mithril Boots. Chest: pale, frost-blue tinted steel plate armor with
icy crystalline texture or frost patterns etched into the surface, sharper angular plate edges.
Include matching frost-blue greaves over the shins, stopping above the ankle. Boots: elegant,
lightweight silvery boots with a fine engraved sheen, thin and refined-looking but clearly sturdy
- prized, rare material.

Panel 5: Arcane Vestments + Celestial Striders. Chest: an ornate mage's robe, heavier and more
elaborate than plain robes, glowing rune patterns woven through the fabric, richer layered drape,
small glowing sigils as embellishment. Boots: the most ornate boots of the set - radiant,
finely detailed footwear with subtle divine motifs, soft etched light-ray linework, delicate
filigree, a faint glow suggested through the pencil shading.

Keep every panel's pose, camera framing, and character scale identical so they can be cut apart
and compared directly - no panel zoomed, rotated, or scaled differently. Plain flat light
background per panel as described above, clean gaps between panels so each character can be
cropped out cleanly.
```

---

Once you have both sheets, send them over (note which panel is which combo) and I'll crop each
panel twice - chest+greave layer and boots layer - and align both onto the paperdoll.
