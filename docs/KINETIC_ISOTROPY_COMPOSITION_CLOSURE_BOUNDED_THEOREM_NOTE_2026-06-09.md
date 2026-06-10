# Kinetic Isotropy: the Composition Closure

**Date:** 2026-06-09
**Claim type:** bounded_theorem (premise reductions on the block02 conditional
set + the computed free-sector bridge + one NEW declared reading, R-P)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/kinetic_isotropy_composition_closure_2026_06_09.py`](../scripts/kinetic_isotropy_composition_closure_2026_06_09.py)
(SCORECARD: PASS=14, FAIL=0; cached:
[`logs/runner-cache/kinetic_isotropy_composition_closure_2026_06_09.txt`](../logs/runner-cache/kinetic_isotropy_composition_closure_2026_06_09.txt))

---

## What this cycle does (relative to block02)

The site-licensed tick dichotomy
([`STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md`](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md),
PR #3447) left the conditional set {P1' site-strict reading + P2 unitary
reading + B-W Wick bridge + scheme-forcing + a dispersive realized tick +
the 2-site periodicity scope}. This cycle REDUCES three entries, COMPUTES
the free-sector bridge, and — the load-bearing honesty of the cycle —
exhibits that the periodicity residual cannot be dissolved, only RELOCATED
into one sharply named new reading (R-P below), which is now the campaign's
sharpest surviving residual.

### L1 — the periodicity scope wall becomes landed structure + one reading

The joint landed pattern {Kawamoto-Smit phases `eta_1 = 1`,
`eta_2 = (-1)^{x_1}`, `eta_3 = (-1)^{x_1+x_2}`; sublattice parity
`epsilon(x) = (-1)^{x_1+x_2+x_3}` — both from
[`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md),
itself `unaudited` on the live ledger — conditionality inherited} breaks
EVERY odd translation (single-site along all three axes AND the mixed odd
shifts) and is invariant under exactly `(2Z)^3` — computed on a 4^3 block
(L1a). A tick covariant under the realized structure's unbroken translations
has the uniform 2-site Bloch cell per axis — precisely the block02 setting
(L1b). The scope wall is replaced by: {the Lattice axiom's translation
action + the landed `{eta, eps}` pattern (unaudited) + a HOMOGENEITY READING
(the tick respects the realized structure's own unbroken symmetry; a
spontaneously symmetry-breaking tick is not excluded by computation)}.

### L2 — composition: curvature is dynamics, and the honest dial finding

The two-tick composite of two LICENSED single ticks — the flat exchange
cell `U_flat(theta)` and the saturating shift — has the reduced band
equation (derived, L2c)

```text
mu^2 - 2 i sin(theta) cos(K/2) mu - 1 = 0,   lambda = e^{-iK/2} mu :
```

genuinely CURVED massive bands (nonzero curvature, L2d), `|v| <= 1` proved
symbolically (the `cos^2(theta) >= 0` identity, L2e), while every licensed
SINGLE tick is flat-or-saturating (block02; both factors cross-checked,
L2f). Curvature requires composition.

**The honest finding (L2g, hostile witness):** composite-level KINETIC
dials exist. `U_shift^2 = e^{-iK} * I` exactly, so shift/identity protocols
give MASSLESS composites with tunable cone slope `k/(k+m)` (e.g. 2/3 for
{shift, shift, identity}) — a marginal velocity fully decoupled from mass
and gap. An OS0 normalization placed at the n-tick kernel would read a
tunable ratio. **What excludes composite dials from the regulator
normalization is a PLACEMENT READING, declared by this cycle as the new
residual:**

> **(R-P) the OS0 kinetic normalization is the SINGLE-TICK kernel's.**

R-P is motivated by — NOT derived from — the primitive's own self-locating
wording ("one tick is one edge in form") and the landed per-plaquette note's
one-tick form context; citing the primitive's own wording carries a
LIMITED-CIRCULARITY CAVEAT, stated here explicitly: R-P localizes where the
normalization lives, while the chain (blocks 01-02) derives what its value
must then be. Under R-P, block02's dichotomy leaves no dial; without R-P,
the dial returns at the composite level. R-P is the campaign's sharpest
surviving residual.

### L3 — P2 reduced to the C-linear-automorphism reading

If the one-tick map is a C-LINEAR AUTOMORPHISM of the site algebra (the
Quantum axiom's `M_2(C)` structure preserved), it is inner, hence unitary —
Skolem-Noether, consumed as ADMISSIBLE STANDARD MATH (cited; the
`automorphism => inner` direction is NOT machine-proved here; L3a is a
consistency exhibit of the converse direction only). The premise has
content on two sides, both named: the transpose map preserves trace but
REVERSES products (an anti-automorphism, computed, L3b), and ANTILINEAR
(antiunitary, Wigner-allowed) ticks are excluded by the C-linearity clause,
not by computation. P2's residual content becomes: "the tick is a C-linear
automorphism of the site algebra" — a reversibility/structure reading
adjacent to the Quantum axiom's own wording.

### L4 — the B-W bridge: free sector computed GIVEN a named sub-bridge

The identification of the tick's EUCLIDEAN one-tick kernel with the same
shift structure (the standard Berezin transfer representation) is itself
the free-sector instance of B-W — a named standard-math sub-bridge
(**B-W-free**), assumed not derived. GIVEN B-W-free: the kinetic operator
`1 - e^{-omega_E} e^{iK}` expands to `partial_tau - i partial_x`, the
conjugate cell to `partial_tau + i partial_x` (both coefficients computed,
L4a/L4b), the pair kernel's degree-2 part is exactly `omega_E^2 + K^2`
(L4b), and the exact zero locus is `omega_E = iK` identically — zero
artifact corrections at the free kinetic level (L4c). **B-W-interacting**
(the loop surface) remains named.

## The conditional set after this cycle (complete)

| entry | before (block02) | after (this cycle) |
|---|---|---|
| P1' site-strict reading | named reading | unchanged |
| P2 unitary-tick reading | named reading | REDUCED to the C-linear-automorphism reading (Skolem-Noether as admissible standard math) |
| P3 / P4 | discharged / reduced (block02) | unchanged |
| B-W bridge | named for everything | split: B-W-free (named sub-bridge) + free-sector computation DONE given it; B-W-interacting still named |
| scheme-forcing | landed, unaudited | unchanged |
| KS `{eta, eps}` pattern | (not previously counted) | consumed by L1; landed, `unaudited` — flagged |
| dispersive realized tick | named | unchanged |
| 2-site periodicity scope | a scope choice | REPLACED by {Lattice translation + landed `{eta, eps}` pattern + homogeneity reading} |
| **R-P placement reading** | (implicit, unrecognized) | **NEW, DECLARED — the sharpest residual** |
| 3D simultaneous tick | named open | unchanged |

Exhaustively, what stands between this chain and an unconditional surface:
four readings (site-strictness, C-linear automorphism, homogeneity, R-P
placement), two named bridges (B-W-free, B-W-interacting), two landed-but-
unaudited dependencies (scheme-forcing, KS pattern), the nonflat-tick
premise, and the 3D simultaneous tick. No numeric, empirical, or selector
content remains anywhere in the chain.

## What this note does NOT claim

- **No registry action and no status claim.** Ratification grades belong to
  the independent audit lane; the primitive's classification belongs to the
  owner. This note reduces and names; it does not retire.
- **R-P is not derived.** It is a declared reading with a stated
  limited-circularity caveat (the primitive's own wording is its closest
  textual anchor). The landed per-plaquette note does NOT supply it (that
  note's boundaries explicitly decline to supply an action), and blocks
  01-02 use a different (locality) reading. A skeptic placing the regulator
  normalization at the composite level keeps a tunable ratio — that is
  exactly what R-P decides, and why it is flagged as the sharpest residual.
- **L1's homogeneity reading is a reading.**
- **1D / per-axis; matter sector; free kinetic level.** The 3D simultaneous
  tick and the interacting loop surface remain the named opens.
- **No empirical input.** No comparator is cited.

## Falsifiers

- A framework derivation grounding the regulator normalization at a
  composite/n-tick kernel (kills R-P; the `k/(k+m)` dial becomes physical
  and the primitive's content returns as a genuine free parameter).
- A framework derivation of a fundamental antiunitary or non-automorphism
  tick (kills the L3 reduction).
- A framework derivation of a tick spontaneously breaking the realized
  `(2Z)^3` translations (kills the L1 homogeneity reading).
- An interacting-loop computation requiring a `c_t != c_s` counterterm on
  this surface (kills the B-W-interacting extension).

## No-Go Discipline Gate (for the negative leg)

The negative claim, correctly scoped after review: "no licensed SINGLE tick
provides a kinetic-form dial (block02), and composite dials — which exist
(L2g) — are excluded from the regulator normalization exactly by R-P."

- **N1 alternative routes:** (1) larger-cell fundamental single ticks —
  handled by L1 (landed pattern + homogeneity reading), with the reading
  named; (2) composite protocols — ATTEMPTED and EXHIBITED as genuine dials
  (L2g): excluded only by R-P, declared; (3) non-automorphism ticks —
  premise-level, witnessed (L3b) and named (antilinear); (4) anisotropic
  free Euclidean kernels — excluded given B-W-free (L4, computed); (5)
  interacting counterterms — NAMED OPEN.
- **N2 wall independence:** L1, L3, L4 consume different landed structure
  (KS pattern / Quantum-axiom algebra / the saturating cell's kernel); R-P
  is independent of all three (it is a placement statement).
- **N3 hidden-wall scan:** the placement of the OS0 normalization was a
  HIDDEN WALL in the first draft of this very note — promoted by
  adversarial review to the explicit declared reading R-P. No other
  unstated placement or identification survives the scan: B-W-free is the
  other promoted item.
- **N4 residual matching:** each table row matches one block02 residual or
  declares itself new (R-P).
- **N5 rhetoric audit:** "no dial" is scoped to licensed single ticks plus
  the R-P-conditional regulator statement; composites have real tunable
  velocities (L2e, L2g) and the note says so.
- **N6 partial-closure scan:** no existing note performs the composition
  split, the `{eta, eps}` joint breaking computation, or the free-sector
  bridge computation.
- **N7 steelman:** "R-P is doing all the work, and its closest textual
  anchor is the primitive itself — the derivation chain is a sophisticated
  restatement." Response, honestly: R-P does carry the placement, and its
  circularity caveat is declared rather than hidden. What the chain adds
  beyond restatement: GIVEN the placement (wherever a reader grounds it),
  the VALUE is forced — quantized, not tuned — by retained-or-landed
  structure (blocks 01-02), with every alternative cell excluded by
  computation. The primitive asserted both the placement and the value; the
  chain reduces the assertion to the placement alone. That is the cycle's
  entire claim.
- **N8 cross-cycle echo:** blocks 01/02 used the strict one-tick-MAP
  (locality) reading; R-P is a DIFFERENT reading (normalization placement)
  and is counted separately — the conflation of the two was a reviewed-out
  error of this note's first draft.

## Dependencies

- [STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md) — block02 (PR #3447).
- [KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md](KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md) — block01 (landed).
- [STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md) — the landed `{eta, eps}` pattern (L1; `unaudited`, conditionality inherited).
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — the Quantum axiom's algebra (L3) and the translation action (L1).
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the target; also R-P's closest textual anchor (limited-circularity caveat stated in L2).

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or of the kinetic-isotropy primitive. The
independent audit lane is the only status authority.
