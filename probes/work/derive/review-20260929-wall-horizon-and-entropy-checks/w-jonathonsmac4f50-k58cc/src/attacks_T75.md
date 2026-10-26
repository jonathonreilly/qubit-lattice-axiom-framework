# Attack on T75: No lattice horizon and no lattice Hawking radiation

Attacker: Claude Sonnet 5.5, same vendor family as the supervisor (Opus 5.5); all checks are same-family, not independent referees.

Read: `MINIMAL_AXIOMS_2026-06-29.md` and `PRIMITIVE_REGISTRY_CHECK.md` (both in full); L15-W6/W7 and their cited notes; blocks 53, 55, 56; probe 19; gravity-wall SUMMARY.

## Verdict in plain words
The wall is two questions. The thermal law T = κ/2π does hold on the framework's own clocked walker, with no absorber, once a rate has a linear zero (checked to 0.3%). But the record dynamics does not give a linear zero. For every smooth scale-covariant stiffness energy, a large stopped region has a double zero, so κ = 0 and T_H = 0. A clock stops at finite mass for one bond energy only, and only at one site (m* = 18/γ, confirmed). A finite temperature needs a master clock or a metric degree of freedom (T64/T67). Priced, not passed.

## The wall (checked)
- Plain: The notes quote Hawking's temperature from smooth spacetime. Can the lattice produce a place where clocks stop, and radiation from it?
- Precise: derive from the axioms a stopped-lapse region of the rate dynamics (blocks 53–56) with κ > 0 and a thermal outgoing flux at κ/2π, with an account of records. Assumed Killing-horizon vocabulary and hand-added absorbers do not count.
- Real? Yes, open (not solved in `docs/`, `archive/`, 36 open PRs). Two corrections: W6's "cheapest test" (does the second bond energy reach φ→0 at finite mass?) is answered below. W7's suggested on-site-potential variant is not the framework's clock, which dresses hopping (block 55 note `:26`); it fails here.

## Load-bearing premises
| Premise | Kind | Path:line | If wrong | Tested? | Cheapest test |
|---|---|---|---|---|---|
| Records permanent; no dynamics | axiom / open gate | `MINIMAL_AXIOMS_2026-06-29.md:77-80,185` | evaporation possible | no | formation law (T01) |
| Clocked amplitude H_w = φHφ | supplied model | block 55 `:26` | no speed→0 | here | done (A) |
| Stiffness weight one (no master clock) | supplied | block 53 `:4,50`; block 55 `:54` | linear zero possible | here | done (B3) |
| Root-rate quadratic bond energy | supplied | block 56 `:96,129` | finite-mass stop | here | done (B2) |
| Fixed flat lattice, no metric dof | axiom + reading | `MINIMAL_AXIOMS…:35-38` | κ>0 via metric | T64 stands | none cheap |
| T_H = κ/2π from a smooth Killing surface | supplied | `AXIOM_FIRST_HAWKING…:42-95` | lattice KMS instead | here | done (A) |

## Routes
| Route | Approach | Premise dropped | Must believe | First artifact | Cost | Changes | Verdict |
|---|---|---|---|---|---|---|---|
| R1 lattice Unruh | Horizon = zero of local speed on a unitary chain; thermality from vacuum entanglement (Bisognano–Wichmann, J. Math. Phys. 16, 985 (1975); Corley–Jacobson, PRD 54, 1568 (1996); Visser, CQG 15, 1767 (1998)) | absorber, one-way membrane | records supply a linear zero | test A | done | W7 kinematics | survives for kinematics; formation and outflow untested |
| R2 stopped clock from the ledger | Ledger completion with finite-mass stop and κ>0 | root-rate energy | F2-type energy physical | B2, B3 | done (statics) | T70, T74, T64, T67 | wounded: F2 stops one site; macroscopic p→2; κ>0 blocked-equivalent to T64/T67 |
| R3 misframed | Ask "what is κ of the coarse lapse?" | that black holes must radiate | κ=0 is a prediction; lapse-only gravity has no horizons (Shapiro–Teukolsky, PRD 47, 1529 (1993), from memory) | lemma below | a note | T76, T03 | survives as a reading; fits permanence |

## Test run
- Pre-registered (`T75_scratch/PREREG.md`): A: β·a/π ∈ [0.97,1.03], residual < 0.05, controls fail. B2: w₀ < 10⁻³ at m within 1% of 18/γ. B3: p(20) ≥ 1.7. B1: exponent 1.8–2.2.
- Scripts and full table: `T75_scratch/*.py`, `RESULTS.md`.
- Result:
  - A as registered **missed**: β·a/π = 0.775 (sign and shape right; half-site offset and far-end mismatch). The exact-geometry rerun is post hoc: β/π = 1.0063…1.0033 for N = 100–800, R² ≥ 0.99996. A double zero drifts (β/π 2.1→3.2, 10× larger deviations); an on-site ramp gives R² = 0.
  - B2 **passed** (41³): m(w₀) monotone, 17.925 at w₀ = 10⁻³; (18−m)/w₀ = 74.63 vs 74.81; neighbours at 0.64; ledger saturates at 4.81.
  - B3 **passed**: p(20) = 1.998, 1.896, 2.146 (F1, F2, F3); a weight-two energy gives p = 1.
  - B1 **missed** the exponent band (curvature-dominated); its ledger matched the note (192.32).
- Reading: the obstruction is the exponent of the lapse zero, not the thermal law.

## Outcome
PRICED. Named premise: weight-one smooth nearest-neighbour stiffness on the fixed flat lattice. Argument (suggested): for bond energy √(w_x w_y) f(u_x−u_y), f even and smooth, block 55's second-order expansion gives p/n² − p²/(2n²) = 0, so a power-law lapse has p = 2 independent of f₂. In the family Σ(w_x^s − w_y^s)², w ~ n^(1/s); p = 1 needs s = 1 (a master clock) or a metric degree of freedom. Siblings moved: T70, T74, T64/T67, T76, T03.

## Claims and labels
- checked: thermal law and controls; F2 threshold m* = 18/γ with w₀ ≈ γ(18/γ−m)/(8Σ1/w_y); B3 exponents; B1 ledger.
- proved (landed, unaudited): 0 < φ ≤ 1, no finite-mass stop for the root-rate energy (block 56 T1, T3, `:64,80`).
- suggested: the p = 2 lemma; extremal ⇒ T_H = 0; F2 stop is a convex-ledger minimum.
- reading: T_H = 0 fits record permanence; the Shapiro–Teukolsky citation is from memory.
