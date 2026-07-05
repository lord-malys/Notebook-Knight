# Session Notes — Batch 2 + Boots Combo Sheets

## What was decided

Instead of a separate boots-only art pass, chest and boots art are generated together on combo
sheets: each panel draws one full character wearing a specific chest item + boots item pairing.
Both pieces come from the same drawing, so when cropped into two separate layers (chest+greave,
and boots), the ankle seam matches automatically — no more hand-tuning fade/overlap like the Iron
Plate fix required.

Cramming all items onto one sheet was rejected — 5 chest + 10 boots = 15 panels, well past the
3-6-panel range that's kept prior batches consistent. Split into two 5-panel sheets instead. Each
of the 5 Batch 2 chest items (Scholar's Robes, Steel Plate, Emberplate, Froststeel Plate, Arcane
Vestments) appears once per sheet, paired with a different boots item each time, so all boots in
the main list get covered across the two sheets.

Prompts saved to: `01_Art/WIP/notebook_knight_batch2_and_boots_prompts.md`

- **Sheet A pairings:** Scholar's Robes + Worn Boots, Steel Plate + Copper Greaves, Emberplate +
  Swift Boots, Froststeel Plate + Iron Greaves, Arcane Vestments + Leather Boots.
- **Sheet B pairings:** Scholar's Robes + Fleet Runners, Steel Plate + Steel Sabatons, Emberplate
  + Shadow Treads, Froststeel Plate + Mithril Boots, Arcane Vestments + Celestial Striders.

New rule: chest-armor panels still stop above the ankle (no feet). Boots panels are the opposite —
draw the full foot/shoe shape, extending up to roughly mid-shin, overlapping generously with where
the chest art's greave fades out.

Extraction plan once sheets come back: crop each panel twice (chest+greave layer, boots layer).
The boots layer becomes a normal independent `EQUIP_ART_V2.boots` asset, usable under any chest
piece, not just the one it was drawn next to.

## Boots count correction

The workflow doc said 10 boots items. Re-verified via Grep on the master HTML: there are actually
**11** — the 10 in the main item list, plus one unique item, `bts_windwalker_treads` (Windwalker
Treads, mithril, rare, def 4 / spd 5, value 320, "Bounty hunters need to leave faster than they
arrived"). It's a bounty-hunter reward drop, paired with the unique chest piece `chs_wyrmscale_hauberk`
(Wyrmscale Hauberk) in the same reward bundle. Same pattern as the earlier "13 vs 16 chest items"
miscount — unique items live outside the main list and are easy to undercount.

Windwalker Treads isn't in either combo sheet above — left for a future unique-items pass,
alongside Wyrmscale Hauberk, consistent with how that piece is being handled.

## Still outstanding (carried over, unresolved)

- Master HTML build has never actually been saved as a versioned copy (`_v1`, `_v2`, etc.)
  despite the standing request — bash mount can't reliably read/copy this file, and full
  Read+Write reconstruction is too large to do inline (~280k tokens). Needs a dedicated fix.
- Batch 2 and Batch 3 chest-only prompts (in `notebook_knight_chest_armor_prompts.md`) haven't
  been run yet — this new combo-sheet approach effectively supersedes generating Batch 2 chest
  art on its own, since the combo sheets above cover Batch 2's 5 items already.
- Batch 3 chest items (Shadow Garb, Wyrmscale Hauberk, Mithril Plate, Dragonscale Armor,
  Celestial Plate) still need their own art pass — could use the same combo-sheet approach with
  Windwalker Treads folded in as one of the boots pairings.
- Helmets (11 items) — needs a hair-interaction decision before generating.
- Weapons (~60 items) — biggest remaining category, several holding poses needed.
