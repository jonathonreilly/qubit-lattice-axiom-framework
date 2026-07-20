# Wave Retarded Gravity: Retarded ≠ Instantaneous on the Wave Field

**Date:** 2026-04-07 (revised); 2026-05-28 (comparator corrected to the exact
discrete c=∞ Poisson solve; falsified finite-c *direction* claim withdrawn).
**Type:** bounded_theorem
**Status:** bounded existence-of-difference result — the retarded moving-source
field differs from the EXACT c=∞ instantaneous comparator (discrete static
Poisson solve) by 12–17% on 3 families at the tested (H, v/c); F~M, Born, and
null preserved. The c=∞ comparator is now **derived** (no longer a conditional
input) via the bridge theorem. The *sign* of M−I is configuration-dependent
and is NOT claimed as a finite-c direction.
**Status authority:** independent audit lane only.

## 2026-05-28 Correction (exact c=∞ comparator; finite-c direction withdrawn)

A prior audit flagged the c=∞ comparator identification as a conditional
input. Investigation (4-agent verification panel + machine-precision runner)
established two things:

1. **The previous comparator was wrong.** It set the "instantaneous" field to
   a single LATE-TIME slice of an **undamped** frozen-source wave evolution.
   An undamped wave driven from rest oscillates (each mode as `1−cos(ω_k t)`)
   and **never settles**; that snapshot is ~33–38% off the true static field
   and does not satisfy the static equation. It **overshoots** the static
   value, which is what produced the earlier (spurious) "retarded < instantaneous"
   reading.
2. **The exact c=∞ field is the discrete Poisson solve.** Setting the leapfrog
   second time-difference to zero gives the unique fixed point `lap[f*] = −src`
   (Dirichlet `f*=0`), which is `c`-independent and is therefore the exact
   c=∞ instantaneous field. This is proved and machine-precision certified in
   [`WAVE_POISSON_CINF_BRIDGE_THEOREM_NOTE_2026-05-28.md`](WAVE_POISSON_CINF_BRIDGE_THEOREM_NOTE_2026-05-28.md).
   The runner's comparator (`_make_instantaneous`) now uses this static solve
   (SOR), so the c=∞ identification is **derived**, not admitted.

**What survives (corrected):** M ≠ I_static by 12–17%, robust across the three
grown families (an existence-of-difference between the retarded field and the
exact instantaneous field at this single (H, v/c)). F~M, Born, and the exact
null are unchanged.

**What is withdrawn:** the interpretation "retarded is consistently the smaller
one — consistent with finite-c information transport." Against the correct
comparator the sign is the opposite (M > I here), and that sign is
**configuration-dependent**: it is positive for the large source displacement
used here and crosses zero / reverses for small source motion (verified by
displacement sweep). So no config-independent finite-c *direction* is claimed —
only the existence and (config-specific) magnitude of the difference.

## Artifact chain

- [`scripts/wave_retarded_gravity.py`](../scripts/wave_retarded_gravity.py)
- [`WAVE_POISSON_CINF_BRIDGE_THEOREM_NOTE_2026-05-28.md`](WAVE_POISSON_CINF_BRIDGE_THEOREM_NOTE_2026-05-28.md) — proves the c=∞ comparator is the discrete Poisson solve (now the derived authority for I).
- [`logs/2026-04-07-wave-retarded-gravity.txt`](../logs/2026-04-07-wave-retarded-gravity.txt)

## Question

The wave-equation field carries a finite-c lightcone (certified
separately). When the source moves, does the resulting beam deflection
differ from what the EXACT instantaneous (c=∞) field would produce?

## Decisive comparator (corrected)

The **instantaneous comparator** I is, at each layer `t`, the exact discrete
static Poisson solve `lap[f] = −src` with the source frozen at `iz_of_t(t)`,
solved by SOR. By the bridge theorem this is the unique c=∞ fixed point of the
wave operator — the field everywhere instantaneously tracks the current source
position with no propagation delay. Static slices are cached per source
position.

The retarded field M is the standard undamped wave-equation evolution with the
same `iz_of_t` source motion.

The beam runs through both fields. The decisive metric is `delta_M − delta_I`.

## Result (Fam1, v/c = 0.30)

| Reference | delta_z |
| --- | ---: |
| A: frozen at z_start (intuition only) | +0.008158 |
| B: frozen at z_end (intuition only) | +0.001846 |
| C: frozen at z_mid (intuition only) | +0.006543 |
| **M: moving source, RETARDED** | **+0.008457** |
| **I: moving source, INSTANTANEOUS (c=∞ Poisson)** | **+0.007294** |
| **M − I** | **+0.001163** |
| relative \|M−I\| / max(\|M\|,\|I\|) | **13.75%** |

The retarded and exact-instantaneous fields produce **different** beam
deflections by ~14% at this configuration. The frozen references are kept in
the table as intuition only; they are not the test.

## Family portability

| Family | dM | dI | M − I | relative |
| --- | ---: | ---: | ---: | ---: |
| Fam1 | +0.008457 | +0.007294 | +0.001163 | 13.75% |
| Fam2 | +0.008234 | +0.007233 | +0.001000 | 12.15% |
| Fam3 | +0.008267 | +0.006902 | +0.001365 | 16.51% |

Three independent grown geometries: M and I differ by 12–17%, same sign
(M > I) at this large-displacement configuration. The existence of a
difference is geometry-portable; the sign is configuration-specific (see the
correction header).

## Other observables on the moving-source field

| Property | Value |
| --- | ---: |
| F~M (Fam1) | 0.9965 |
| F~M (Fam2) | 0.9955 |
| F~M (Fam3) | 0.9963 |
| Born \|I3\|/P | 3.59e-16 |
| Null (s=0) | exact |
| v-symmetry (+v vs −v) | +0.0072 vs +0.0085 |

F~M holds, Born stays at machine precision, exact null. The full
weak-field package survives the dynamical, time-translating source.

## What this means

On the wave-equation field, a moving source produces a beam deflection that
differs from the field that would be produced if the field everywhere
instantaneously tracked the current source position (the exact c=∞ Poisson
solve). The two are ~12–17% apart in magnitude on this v/c=0.30, large-
displacement geometry. This is a finite-lattice **existence-of-difference**
between the retarded and exact-instantaneous fields. It does NOT, by itself,
establish a finite-c directional law: the sign of M−I depends on the source
configuration.

## What this DOES NOT show

- A finite-c *direction* law (the sign of M − I is configuration-dependent)
- A continuum-stable retardation magnitude (sibling continuum-limit note shows
  the magnitude is not converged)
- A specific `r/c` light-travel-time match
- The detailed angular profile of the retardation
- Multiple v/c values; only 0.30 is tested
- Strong-field or non-perturbative regime
- Backreaction (source feeling its own field)
- Orbital / accelerated source (translation only)

## Claim boundary

- v/c = 0.30 single value
- Large source displacement (iz 6→0); the M−I sign is specific to this regime
- Linear translation, not orbit
- Single source, no backreaction
- The c=∞ comparator is the exact discrete Poisson solve (7 unique source
  positions over the run), derived via the bridge theorem
- The effect is a +12–17% magnitude difference, not order-of-magnitude — small v/c

## Inputs (cited authorities)

The runner's load-bearing observable is `delta_M − delta_I`, the difference
between the retarded moving-source field and the exact discrete static Poisson
solve (the c=∞ comparator). The primitives the runner imports are each one-hop
authorities on the current dependency surface:

- the exact c=∞ comparator identification (discrete Poisson solve = unique
  c=∞ fixed point of the wave operator):
  [`WAVE_POISSON_CINF_BRIDGE_THEOREM_NOTE_2026-05-28.md`](WAVE_POISSON_CINF_BRIDGE_THEOREM_NOTE_2026-05-28.md);
- standard parallel perturbation propagator and beam-deflection readout for
  the linear gravitational response:
  [`LINEAR_RESPONSE_TRUE_KUBO_NOTE.md`](LINEAR_RESPONSE_TRUE_KUBO_NOTE.md);
- continuum/static-slice and finite-c lightcone claims used here, to the
  extent stated by their own source:
  [`WAVE_RETARDATION_CONTINUUM_LIMIT_NOTE.md`](WAVE_RETARDATION_CONTINUUM_LIMIT_NOTE.md);
- grown-DAG geometry families Fam1/Fam2/Fam3 used for the portability check:
  [`KUBO_CONTINUUM_LIMIT_NOTE.md`](KUBO_CONTINUUM_LIMIT_NOTE.md).

The note's contribution is the bounded numerical M − I existence-of-difference
on three families against the now-derived exact c=∞ comparator. The c=∞
identification is no longer a conditional input; it is supplied by the bridge
theorem above.

The repaired `WAVE_RETARDATION_LAB_PREDICTION_NOTE.md` is finite-sweep
context only.  It supplies neither the lightcone premise nor the numerical
existence result in this note.

## Discrete Green-function context

- Non-load-bearing context note `LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md` records the framework-applied `Z^3` graph-Laplacian normalization certificate for the cubic-lattice Green's function asymptotic `G(r) → 1/(4 π |r|)`. The exact c=∞ comparator (discrete Poisson solve) is the lattice Green's function applied to the source; its leading asymptotic carries the same Maradudin / Spitzer / Lawler coefficient. Finite-lattice corrections (subleading terms) remain inside the bounded scope of this note's runner.
