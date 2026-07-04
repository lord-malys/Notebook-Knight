# Notebook Knight — Equipment Overlay Art Prompts (Round 6)

Context: the paperdoll now supports layered equipment. `drawTownCharacter()` draws, in order: the
bare/tunic base doll -> equipped chest armor art (if loaded) -> equipped weapon art (if loaded).
Weapon and chest overlays are separate transparent PNGs meant to be pixel-aligned to the *same*
1024x1536 canvas as `chr_male/female_paperdoll_base.png`, so they composite with zero offset math.

**Rusty Sword is already done** - it's literally the sword that used to be baked into the tunic
doll, extracted into its own layer now that the base sprite has an empty hand. No art needed there.

**Quilted Vest (`chs_padded_vest`) needs new art.** It's the game's starter chest armor (every new
game equips it immediately alongside the Rusty Sword), so this is the very first thing most
players will see - worth getting right. Flavor text: "Multiple layers of quilted cloth. More
protection than it looks." Common rarity, +2 DEF.

## Practical note on alignment

Don't expect an AI image generation to land pixel-perfect on the existing 1024x1536 canvas from a
text prompt alone - the reference pose isn't something ChatGPT can match exactly. Generate the vest
worn on a character in roughly the framing described below, share it, and the cropping/scaling/
alignment onto the actual base-doll canvas will be handled the same way the sword was extracted -
matching against the existing bare-body sprite directly rather than relying on exact coordinates.

## Prompt (male and female versions - generate both)

Simple hand-drawn pencil sketch of a chibi RPG character, matching an established game's art
style: soft graphite pencil shading with visible cross-hatching, thick clean confident ink
outlines, slightly rough/hand-drawn linework (not a flat single-line doodle style - there should be
real tonal shading and texture, like a considered character illustration, not a quick margin
sketch). Chibi proportions: large head, small compact body, standing in a relaxed three-quarter
turned pose facing slightly to the left, arms hanging naturally at the sides.

Subject: the character wearing ONLY a quilted padded vest as their torso covering (no separate
shirt underneath - the vest itself is the only garment, drawn to cover chest down to the hip/upper
thigh like a short padded tunic, so it reads as a complete outfit on its own, not as an accessory
layered over something else). The vest is simple, undyed, homespun cloth - a starter-tier piece of
armor, not fancy: visible quilted diamond or square stitching pattern across the fabric showing the
padding underneath, a simple front closure (ties, laces, or a couple of toggle buttons), maybe a
frayed or patched edge here or there to sell "cheap but functional." Bare arms and legs visible
below/beside the vest (they belong to the base body layer, not this image - don't draw a full
shirt or sleeves, just the vest itself and whatever bare skin naturally shows around it). No
weapon, no other armor pieces, no background - transparent background, character only.

Generate a male version and a female version separately, both in the same pose, vest style,
and shading approach for consistency.
