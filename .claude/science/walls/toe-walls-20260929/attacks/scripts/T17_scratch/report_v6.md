# Attack on T17: One record per site breaks the exact energy-momentum books of interacting matter

Attacker: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family checks, not independent referees).

Read: `docs/MINIMAL_AXIOMS_2026-06-29.md` (all 233 lines) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (all; no primitive touches momentum or exclusion). Notes: blocks 137, 143, 151/152 scopes, block 154 (PR #9287), inertial-clause note, P6 T9, MAP:530-545, 589-616, 895-943, gravity-exercise SUMMARY, T18.

## Verdict in plain words
The wall is real for Hamiltonian walkers and misstated for records whose momentum is a label. In a census of the framework's own two-record walk, every interaction tested, hard-core or soft, leaves no exactly conserved local odd charge, because a walker's momentum is a Fourier variable on a torus. But "exact momentum and angular-momentum books force records that never scatter" holds only for two neighbouring records. On diagonal pairs and 2x2 plaquettes, scattering keeps number, momentum and angular momentum exactly, one record per site, with a local symmetric stress. The classical moving-records clause is repairable at stated costs; the walker's wall stands. Nothing is coupled to the curvature member yet.

## The wall (checked)
- Plain: Gravity needs its source's energy, momentum and turning-momentum conserved exactly at every place. Free walkers do this. When records interact, a walker's momentum survives only lattice-wide; the bookkeeping breaks and the graviton gains a mass.
- Precise: On Z^3 with one record per site, exhibit an interacting, finite-range record dynamics with exact local continuity for energy, momentum and angular momentum and a symmetric local stress. Passing: an exact construction or decisive no-go for a named dynamics; third-order statements (b152) do not pass.
- Real? Yes, with two corrections. L01-W9's exchange-sign half is T18 (PRICED). Its title blames "one record per site", but a soft neighbour force fails too: the cause is interaction plus Fourier momentum. L02-W11 is the trilemma form; L14-W13 the general one.

## Load-bearing premises
| Premise | Kind | Path:line | If wrong | Tested? | Cheapest test |
|---|---|---|---|---|---|
| F: record momentum is a walker's Fourier momentum | supplied model | b137:49-53 | label momentum: books exact | b143 T3/T5 (conditional); C | done |
| E: member's Gauss laws hold exactly | method | MAP:538-542, 900-913 | mass terms allowed: T61 | P6 T6-T9 | Stueckelberg mass |
| Scattering is bond-local | hidden | inertial:57; MAP:936-938 | plaquette events pass | A | done |
| Perpendicular pass-through exchange | supplied | inertial:56, T2:74 | dropped: L exact, correlated equilibrium | B3 | done |
| Records are the sea's walkers | reading | AX:79-80; MAP:589-615 | free Pauli sea keeps books | no | owner reading |

## Routes
| Route | Approach | Premise dropped | Must believe | First artifact | Cost | Changes | Verdict |
|---|---|---|---|---|---|---|---|
| R1 label momentum | Lattice-gas rules (Frisch-Hasslacher-Pomeau, PRL 56, 1505, 1986): perpendicular neighbours wait; converging records swap contents | F, bond-locality | classical clause is the record dynamics | A, A2, B (done) | supplied clause; massless only; correlated equilibrium; no member coupling | T17 classical; T72, T64 partly | wounded: not tied to walker or member |
| R2 drop exactness | Improved stress plus tuning (Caracciolo et al., Ann. Phys. 197, 119, 1990) | E | mass term is small | none new | graviton mass^2 tuned to ~1e-102 M_Pl^2 (reading; LVK GWTC-3 m_g < 1.27e-23 eV) | T61, T14 | dead as protection; alive as price |
| R3 misframed | Source is a conserved additive charge (Pretko, PRB 96, 035119, 2017); cheaper question: label or Fourier momentum? | matter's Fourier momentum as source | records can be that charge | charge match with V* (unchecked) | member coupling | T72, T69 | survives as reframing |

## Test run
- Pre-registered (`T17_scratch/PREREGISTER.md`): A: conserving events beyond the bond head-on swap exist. B: one component per (N, P). C: excluded 2D pair has no odd charge, controls positive.
- Scripts, outputs: `T17_scratch/` (A_, A2_, A3_, B_, B2_, B3_, B4_, C_).
- A (exhaustive): bond pairs move 2 of 36 configurations (head-on reversal only); diagonal pairs 8 of 36; plaquette 4-record events 228 versus 220 by pairs (2D). A2/A3: every conserving event, 2D and 3D, has a compact symmetric stress (residual 1e-15); the original clause's perpendicular exchange does not.
- B: "one component" FAILED, sectors split four ways. Post-hoc: Lz mod 4 is conserved (0 changing events; the original clause has 186368). Amended: 99.1% of generic states (N=4, 4x4 torus) lie in one component per (P, Lz mod 4). B3: original clause keeps the uniform measure; V* does not (TV 0.13, N=3).
- C (torus 7; hops <=2 one-body, <=1 two-body): scalar 2D free 12, excluded 0, soft 0; walker 1D free 5, excluded 3; walker 2D free 16, excluded 0 (gap 1e-15 vs 3e-4), soft SOFT.
- Reading: exactness needs label momentum. C confirms b143 within its class without its bridge.

## Outcome
PRICED. The wall is F together with locality and exactness E. Exits: (a) label momentum, R1; (b) drop E, pay T61; (c) transparent matter.

## Claims and labels
- Proved: b137 T1; b143 T3/T5 (conditional on its bridge).
- Checked: A, A2, A3, B, B3, C, in their ranges only.
- Suggested: 1e-102 tuning; R3 charge match; V* hydrodynamic limit.
- Reading: label versus Fourier momentum is the fork.
