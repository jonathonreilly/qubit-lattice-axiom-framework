# Kill check on T74

Checker: Claude Sonnet 5.5, same family as attacker and supervisor (not independent). Read MINIMAL_AXIOMS and PRIMITIVE_REGISTRY_CHECK in full, plus L15-W1..W5, L14-W11, L16-W1 and the COFRAME, WALD_NOETHER, WALD_NEWTON, AREA_LAW and HALF_FILLING notes. Scratch: `kills/T74_scratch/`.

## Outcome verdict
WEAKENED. The numerics reproduce and the FAIL stands. "MISFRAMED ... dissolves into T70 and T64" overreaches, and the test was not the one the wall named.

## Route verdicts
| Route | Verdict | Reason, with evidence |
|---|---|---|
| R1 induced gravity | dead as a pass; survives as reformulation (agree) | Anisotropy holds under every area measure tried. The Susskind–Uglum identity is literature, untested here. |
| R2 calibrate | dead (agree) | Assumes the conclusion. |
| R3 misframed | wounded | Restates W1(iii) and L15-W5 (a T70 member). Leaves W1(ii), W1(iv) untouched. The "cheaper question" needs an Einstein-Hilbert action (T64) and an entropy (T73). |

## Errors found
1. **Wrong sea.** L15-W3 names the walker sea, H(k) = σ·sin k (block-147 note T1). The attack ran a π-flux model with a hand-added mass, which its source note calls supplied ("no physical sector selection is derived"). I ran the walker sea (`kill_walker_*.py`): exactly 2× the attack's values (torus L = 8, 12; slab Lx = 64: 0.3930 against 2 × 0.19654), so η = 0.393 / 0.435 / 0.462. The quoted 0.197–0.231 and implied G (1.27/1.15/1.08) are species-count artefacts (walker: 0.64/0.57/0.54). The 0.25 ± 2% band could only be met by tuning species count, so the FAIL informs through anisotropy, not the value.
2. **Area convention unflagged.** The attack uses Euclidean area; BP's is a plaquette count, A(P) = n·a² (PLANCK_BOUNDARY_DENSITY_EXTENSION:76-79). Per plaquette (L = 16): 0.196 / 0.153 / 0.132, a 48% spread, not 17%. `kill_orient_scan.py` finds (211) at 0.2348, above (111): still below 0.25, but 0.197–0.231 is not the range.
3. **`bp_algebra.py` is an identity** (G·b = 2^d/(4d)), not a test. Family and hyperbola are prior art (WALD_NEWTON T3; PLANCK_SOURCE_UNIT_NORMALIZATION, cited at L15-W5). (N) is labelled "hidden", but COFRAME:325-380 and W1(iii) state it openly, and the note calls it not tunable.
4. **"Dissolves" is too strong.** W1(ii) (P_1 against P_3) and W1(iv) (time qubit outside the axioms; its own table gives G·b = 2/3 at d = 3) do not reduce to G. W3's residual, that no native entropy exists, is T73.
5. Minor: the Lx = 128 claim has no output on file; my rerun gives 0.19642 (consistent).

Confirmed: scripts rerun to the reported digits (L = 8, 12, 16; Lx = 64); the m² ln m fit matches 0.0133. No prior entanglement computation for these seas in `docs/`, `archive/` or the 36 open PRs. The two-surfaces split is supported by AREA_LAW_QUARTER_BROADER:230-233.

## Corrected plain-language verdict
On both the π-flux sea and the lane's walker sea, the entanglement area coefficient depends on cut direction and species count and is never 1/4, so there is no single number to match. The action side only restates that the count's unit and Newton's constant rescale together (T70). T74 keeps its own open parts: why the cell is 4 of 16 with a time qubit, the P_1 against P_3 choice, and which entropy is meant.
