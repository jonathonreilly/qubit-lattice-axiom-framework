# Kinetic Isotropy: the Composition Closure

**Date:** 2026-06-09
**Type:** bounded_theorem
**Scope:** premise reductions on the site-licensed tick dichotomy parent conditional
set, the computed free-sector bridge, and one new declared
single-tick normalization-placement reading.
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/kinetic_isotropy_composition_closure_2026_06_09.py`](../scripts/kinetic_isotropy_composition_closure_2026_06_09.py)
(SCORECARD: PASS=14, FAIL=0; cached:
[`logs/runner-cache/kinetic_isotropy_composition_closure_2026_06_09.txt`](../logs/runner-cache/kinetic_isotropy_composition_closure_2026_06_09.txt))

---

## What this note does (relative to the site-licensed tick dichotomy parent)

The site-licensed tick dichotomy
([`STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md`](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md),
PR #3447) left the conditional set {site-strict reading, unitary-tick reading,
Berezin-Wick bridge, scheme-forcing, a dispersive realized tick, and the
2-site periodicity scope}. This note reduces three entries, computes
the free-sector bridge, and — the load-bearing honesty of the note —
exhibits that the periodicity residual cannot be dissolved, only RELOCATED
into one sharply named new reading: the single-tick normalization-placement
reading. That reading is now the sharpest surviving residual.

### Periodicity reduction — the periodicity scope wall becomes landed structure + one reading

The joint landed pattern {Kawamoto-Smit phases `eta_1 = 1`,
`eta_2 = (-1)^{x_1}`, `eta_3 = (-1)^{x_1+x_2}`; sublattice parity
`epsilon(x) = (-1)^{x_1+x_2+x_3}` — both from
[`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md),
itself `unaudited` on the live ledger — conditionality inherited} breaks
EVERY odd translation (single-site along all three axes AND the mixed odd
shifts) and is invariant under exactly `(2Z)^3` — computed on a 4^3 block
(periodicity subgroup computation). A tick covariant under the realized
structure's unbroken translations has the uniform 2-site Bloch cell per axis —
precisely the site-licensed tick dichotomy parent setting
(periodicity cell consequence). The scope wall is replaced by: {the Lattice axiom's translation
action + the landed `{eta, eps}` pattern (unaudited) + a HOMOGENEITY READING
(the tick respects the realized structure's own unbroken symmetry; a
spontaneously symmetry-breaking tick is not excluded by computation)}.

### Composition reduction — composition: curvature is dynamics, and the honest dial finding

The two-tick composite of two LICENSED single ticks — the flat exchange
cell `U_flat(theta)` and the saturating shift — has the reduced band
equation (derived, composite band-equation derivation)

```text
mu^2 - 2 i sin(theta) cos(K/2) mu - 1 = 0,   lambda = e^{-iK/2} mu :
```

genuinely curved massive bands (nonzero curvature, composite-curvature check),
`|v| <= 1` proved symbolically (the `cos^2(theta) >= 0` identity,
velocity-bound check), while every licensed single tick is flat-or-saturating
(the site-licensed tick dichotomy parent; both factors cross-checked,
single-tick contrast). Curvature requires composition.

**The honest finding (composite-dial witness, hostile witness):** composite-level kinetic
dials exist. `U_shift^2 = e^{-iK} * I` exactly, so shift/identity protocols
give massless composites with tunable cone slope `k/(k+m)` (e.g. 2/3 for
{shift, shift, identity}) — a marginal velocity fully decoupled from mass
and gap. An OS0 normalization placed at the n-tick kernel would read a
tunable ratio. **What excludes composite dials from the regulator
normalization is a placement reading, declared by this note as the new
residual:**

> **Single-tick normalization-placement reading:** the OS0 kinetic
> normalization is the single-tick kernel's.

The single-tick normalization-placement reading is motivated by — not derived
from — the primitive's own self-locating wording ("one tick is one edge in
form") and the landed
[`PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09`](PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md)
one-tick form context. Citing the
primitive's own wording carries a limited-circularity caveat, stated here
explicitly: the single-tick normalization-placement reading localizes where
the normalization lives, while the two kinetic-isotropy parent notes derive
what its value must then be. Under that placement reading, the site-licensed
tick dichotomy parent's dichotomy leaves no dial; without it, the dial returns
at the composite level. The placement reading is the campaign's sharpest
surviving residual.

### Automorphism reduction — unitary-tick reading reduced to the C-linear-automorphism reading

If the one-tick map is a C-LINEAR AUTOMORPHISM of the site algebra (the
Quantum axiom's `M_2(C)` structure preserved), it is inner, hence unitary —
Skolem-Noether, consumed as ADMISSIBLE STANDARD MATH (cited; the
`automorphism => inner` direction is NOT machine-proved here; automorphism consistency exhibit is a
consistency exhibit of the converse direction only). The premise has
content on two sides, both named: the transpose map preserves trace but
REVERSES products (an anti-automorphism, computed, anti-automorphism witness),
and ANTILINEAR (antiunitary, Wigner-allowed) ticks are excluded by the
C-linearity clause, not by computation. The unitary-tick reading's residual
content becomes: "the tick is a C-linear
automorphism of the site algebra" — a reversibility/structure reading
adjacent to the Quantum axiom's own wording.

### Berezin-Wick free-sector bridge — the Berezin-Wick bridge: free sector computed GIVEN a named sub-bridge

The identification of the tick's EUCLIDEAN one-tick kernel with the same
shift structure (the standard Berezin transfer representation) is itself
the free-sector instance of Berezin-Wick — a named standard-math sub-bridge
(**Berezin-Wick free-sector bridge**), assumed not derived. Given that bridge,
the kinetic operator
`1 - e^{-omega_E} e^{iK}` expands to `partial_tau - i partial_x`, the
conjugate cell to `partial_tau + i partial_x` (both coefficients computed,
free-kernel linearization check / conjugate-pair kernel check), the pair
kernel's degree-2 part is exactly `omega_E^2 + K^2` with zero mixed
degree-2 term (conjugate-pair kernel check), and the exact zero locus is
`omega_E = iK` identically — zero artifact corrections at the free kinetic
level (free zero-locus check). **Berezin-Wick interacting bridge**
(the loop surface) remains named.

## The conditional set after this note (complete)

| entry | before (the site-licensed tick dichotomy parent) | after (this note) |
|---|---|---|
| site-strict reading | named reading | unchanged |
| unitary-tick reading | named reading | REDUCED to the C-linear-automorphism reading (Skolem-Noether as admissible standard math) |
| prior residuals | discharged / reduced (the site-licensed tick dichotomy parent) | unchanged |
| Berezin-Wick bridge | named for everything | split: Berezin-Wick free-sector bridge (named sub-bridge) + free-sector computation DONE given it; Berezin-Wick interacting bridge still named |
| scheme-forcing | landed, unaudited | unchanged |
| KS `{eta, eps}` pattern | (not previously counted) | consumed by periodicity reduction; landed, `unaudited` — flagged |
| dispersive realized tick | named | unchanged |
| 2-site periodicity scope | a scope choice | REPLACED by {Lattice translation + landed `{eta, eps}` pattern + homogeneity reading} |
| **single-tick normalization-placement reading** | (implicit, unrecognized) | **new, declared — the sharpest residual** |
| 3D simultaneous tick | named open | unchanged |

Exhaustively, what stands between this chain and an unconditional surface:
four readings (site-strictness, C-linear automorphism, homogeneity,
single-tick normalization placement), two named bridges (Berezin-Wick
free-sector bridge, Berezin-Wick interacting bridge), two landed-but-
unaudited dependencies (scheme-forcing, KS pattern), the nonflat-tick
premise, and the 3D simultaneous tick. No numeric, empirical, or selector
content remains anywhere in the chain.

## What this note does NOT claim

- **No registry action and no status claim.** Ratification grades belong to
  the independent audit lane; the primitive's classification belongs to the
  owner. This note reduces and names; it does not retire.
- **The single-tick normalization-placement reading is not derived.** It is a declared reading with a stated
  limited-circularity caveat (the primitive's own wording is its closest
  textual anchor). The landed
  [`PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09`](PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  does NOT supply it (that note's boundaries explicitly decline to supply an
  action), and the two
  kinetic-isotropy parent notes use a different locality reading. A skeptic
  placing the regulator
  normalization at the composite level keeps a tunable ratio — that is
  exactly what single-tick normalization-placement reading decides, and why it is flagged as the sharpest residual.
- **periodicity reduction's homogeneity reading is a reading.**
- **1D / per-axis; matter sector; free kinetic level.** The 3D simultaneous
  tick and the interacting loop surface remain the named opens.
- **No empirical input.** No comparator is cited.

## Falsifiers

- A framework derivation grounding the regulator normalization at a
  composite/n-tick kernel (kills the single-tick normalization-placement
  reading; the `k/(k+m)` dial becomes physical
  and the primitive's content returns as a genuine free parameter).
- A framework derivation of a fundamental antiunitary or non-automorphism
  tick (kills the automorphism reduction).
- A framework derivation of a tick spontaneously breaking the realized
  `(2Z)^3` translations (kills the periodicity reduction homogeneity reading).
- An interacting-loop computation requiring a `c_t != c_s` counterterm on
  this surface (kills the Berezin-Wick interacting bridge extension).

## No-Go Discipline Gate (for the negative leg)

The negative claim, correctly scoped after review: "no licensed SINGLE tick
provides a kinetic-form dial (the site-licensed tick dichotomy parent), and composite dials — which exist
(composite-dial witness) — are excluded from the regulator normalization
exactly by the single-tick normalization-placement reading."

- **N1 alternative routes:** (1) larger-cell fundamental single ticks —
  handled by periodicity reduction (landed pattern + homogeneity reading), with the reading
  named; (2) composite protocols — ATTEMPTED and EXHIBITED as genuine dials
  (composite-dial witness): excluded only by single-tick normalization-placement reading, declared; (3) non-automorphism ticks —
  premise-level, witnessed (anti-automorphism witness) and named (antilinear); (4) anisotropic
  free Euclidean kernels — excluded given Berezin-Wick free-sector bridge (free-sector bridge computation, computed); (5)
  interacting counterterms — NAMED OPEN.
- **N2 wall independence:** periodicity reduction, automorphism reduction, free-sector bridge computation consume different landed structure
  (KS pattern / Quantum-axiom algebra / the saturating cell's kernel); single-tick normalization-placement reading
  is independent of all three (it is a placement statement).
- **N3 hidden-wall scan:** the placement of the OS0 normalization was a
  HIDDEN WALL in the first draft of this very note — promoted by
  adversarial review to the explicit declared reading single-tick normalization-placement reading. No other
  unstated placement or identification survives the scan: Berezin-Wick free-sector bridge is the
  other promoted item.
- **N4 residual matching:** each table row matches one site-licensed tick dichotomy parent residual or
  declares itself new (single-tick normalization-placement reading).
- **N5 rhetoric audit:** "no dial" is scoped to licensed single ticks plus
  the single-tick normalization-placement reading-conditional regulator statement; composites have real tunable
  velocities (velocity-bound check, composite-dial witness) and the note says so.
- **N6 partial-closure scan:** no existing note performs the composition
  split, the `{eta, eps}` joint breaking computation, or the free-sector
  bridge computation.
- **N7 steelman:** "single-tick normalization-placement reading is doing all the work, and its closest textual
  anchor is the primitive itself — the derivation chain is a sophisticated
  restatement." Response, honestly: single-tick normalization-placement reading does carry the placement, and its
  circularity caveat is declared rather than hidden. What the chain adds
  beyond restatement: GIVEN the placement (wherever a reader grounds it),
  the value is forced — quantized, not tuned — by landed-or-proposed parent
  structure, with every alternative cell excluded by
  computation. The primitive asserted both the placement and the value; the
  chain reduces the assertion to the placement alone. That is this note's
  entire claim.
- **N8 cross-cycle echo:** the two kinetic-isotropy parent notes used the
  strict one-tick-map locality reading; the single-tick normalization-placement
  reading is a different reading (normalization placement)
  and is counted separately — the conflation of the two was a reviewed-out
  error of this note's first draft.

## Dependencies

- [STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md) — the site-licensed tick dichotomy parent (PR #3447).
- [KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md](KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md) — the strict-license chiral-quantization parent (landed).
- [STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md) — the landed `{eta, eps}` pattern (periodicity reduction; `unaudited`, conditionality inherited).
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the Quantum axiom's algebra (automorphism reduction) and the translation action (periodicity reduction).
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the target; also single-tick normalization-placement reading's closest textual anchor (limited-circularity caveat stated in composition reduction).
- [PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md](PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md) — retained-bounded one-tick form context only; it does not derive the single-tick normalization-placement reading.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or of the kinetic-isotropy primitive. The
independent audit lane is the only status authority.
