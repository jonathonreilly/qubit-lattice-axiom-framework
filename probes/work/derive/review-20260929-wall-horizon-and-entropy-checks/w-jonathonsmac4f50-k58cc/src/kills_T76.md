# Kill check on T76

Checker: Claude Sonnet 5.5, same family as attacker and supervisor (same-family check). Read: axioms memo, registry check, L15-W8, L01-W13, attack, probe 19 (`kills/T76_scratch/probe19.md`), all scripts. Scratch: `kills/T76_scratch/`.

## Outcome verdict
**WEAKENED.** STANDS survives (no rule, entropy or 1/4 is supplied), but "no supplied rule gives an area-law count" holds only for count-threshold rules, narrower than the axioms allow. Gadget table, constructions, E counts and shell tests to L=12 reproduce; my rewrite matches E frozen 5,7,27,37,135,289,907,2193 and reachable 1,7,13,27,17,69,87,171. Not re-run: E at L=13, 3D 3x3x3 windows. No run exceeded 10 minutes.

## Route verdicts
| Route | Verdict | Reason |
|---|---|---|
| R1 rigid rule E | wounded; "nearly dead" too strong | Ambiguous shells 1/615, 4/1039, 16/2399. The 40-site swaps are box-spanning nested rings (`ambiguous_pairs_E.py 11`), not local switches. E has no sealed gadget in any window (proof below); undecided. |
| R2 count the surface | wounded (agree) | Needs a record-to-amplitude bridge. |
| R3 misframed | survives | Untested, cheap. |

## Errors found
1. **Rule class.** Axioms ask for a rule covariant under translations and proper rotations, depending on nearest-neighbour conditions (`MINIMAL_AXIOMS:57-61`), not counts. 2D has 6 neighbour-pattern classes: 64 rules, not 32. The other 32 were never searched; no prior art on main or PR 9363.
   - Rule "form unless exactly two opposite neighbours are recorded": frozen = reachable = F_a + F_b - 1 on a x b boxes, all a,b <= 9 (`rect_stripe.py`, checked). Argument (suggested): an empty site forces a full empty row or column between recorded ones. So ln N = L ln(phi) + O(1), fixed by the outer layer. Caveats: not proportional to perimeter for rectangles; N = 1 with a recorded wall (L <= 8); process entropy 0; 3D analogue 1, 20, 139 for L = 2-4 (`cov3d.py`), open.
   - Three covariant rules have no sealed gadget in any window: {0,2adj,3,4}, the stripe rule, E. Proved: with 2adj, 3, 4 allowed, the top-left-most empty site can gain its N and W neighbours (attack said "suggested"). {0,2adj,3,4} has N = 9, 49, 345 (L = 3-5), ln N/L^2 near 0.24: volume-like, unresolved.
   - Gadgets not listed by the attack: {0,2adj,4} (4x5), {0,2opp,3,4} (5x5).
2. **Fit comparison.** "SSE 0.10 against 0.28" pairs a + bL^2 with a no-intercept line. Fair pairs (`fits.py`): L >= 8 0.095 vs 0.140; L >= 6 the line wins (0.441 vs 0.618). Mod-4 oscillation dominates.
3. **Process entropy untested.** For E under uniform random sequential formation, Shannon entropy is 0.43, 0.07, 0.014 at L = 4, 6, 8 and 0 by L = 12 (`mc_process_E.py`): typical outcome is the full box. The flat count is not E's process entropy, and that is not an area law. My volume-rule controls saturated the sample (uninformative).
4. **3D wording.** "27 open" includes rules where peelability hit its budget (`run3d_unresolved2.txt`, A=036 unknown 21).
5. **Inference.** No sealed gadget does not signal a small count ({0,2adj,3,4}); PASS-A is weaker evidence than stated.

## Corrected plain-language verdict
Among rules that count recorded neighbours, 14 of 15 non-trivial 2D rules have a local switch and a volume-growing frozen count; E has none and its scaling is undecided. Among all rotation-covariant neighbour rules, one stripe rule has an exact count growing with box length, but it is shape-dependent, vanishes with a recorded wall and has zero process entropy. No entropy, formation rule or 1/4 is supplied, so the wall stands.
