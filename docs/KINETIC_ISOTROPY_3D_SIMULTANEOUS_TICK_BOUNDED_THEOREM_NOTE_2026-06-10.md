# Kinetic Isotropy: the 3D Simultaneous Tick

**Date:** 2026-06-10
**Claim type:** bounded_theorem (the 3D structural results: covariant
flatness no-gos, the quantized-drift classification of every licensed
dispersive object exhibited or swept, and the honest competitor-class map
for the factorized-realization premise)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/kinetic_isotropy_3d_simultaneous_tick_2026_06_10.py`](../scripts/kinetic_isotropy_3d_simultaneous_tick_2026_06_10.py)
(SCORECARD: PASS=20, FAIL=0, PYTHONHASHSEED-pinned and ordering-canonical; cached:
[`logs/runner-cache/kinetic_isotropy_3d_simultaneous_tick_2026_06_10.txt`](../logs/runner-cache/kinetic_isotropy_3d_simultaneous_tick_2026_06_10.txt))

---

## What this establishes (relative to block03)

Blocks 01-03 (all landed) left ONE structural open: the full 3D simultaneous
tick — an 8-band object where multi-band mixing could hide either a tunable
cone slope or a quantized-but-nonunit one. The honest outcome of this cycle,
sharpened twice by adversarial review:

1. **No covariant single tick can transport** — flat in both analyzed
   covariance classes (Parts C, F; one exact, one sweep-grade).
2. **Quantized-but-nonunit dispersive ticks EXIST** — the mixed-cycle and
   staircase witnesses (Parts D3, D4, found in review) are licensed,
   dispersive, NOT per-axis, with slopes like (1/2, 1/2, 0) and
   (1/3, 1/3, 1/3) site/tick. The feared object is realized, not closed.
3. **But everywhere analyzed, slopes are QUANTIZED and bands exactly
   linear:** permutation-class ticks have monomial-rooted bands (slope =
   cycle winding / cycle length — rational, never tunable); the equivariant
   sweep finds no dispersive cell at all; hostile continuous-parameter coin
   families were forced flat by unitarity in the review round. **No
   curvature and no continuous dial was found anywhere.**
4. The per-axis saturating cells (Part E) are the |slope| = 1 extreme points
   of this quantized menagerie, equalized across axes up to the staggered
   gauge; **selecting them is the factorized-realization premise — graded
   honestly as load-bearing against an explicitly NONEMPTY competitor class
   of slower quantized drifts.**

## Setting

One Grassmann per site on `Z^3` (landed scheme-forcing, `unaudited` —
conditionality inherited); the joint landed `{eta_mu, epsilon}` pattern
leaves exactly `(2Z)^3` unbroken (block03, landed), so the covariant tick's
Bloch cell is the 2^3 = 8-site cube: `U(k)` is an 8x8 unitary, entries
Laurent in `z_i = e^{ik_i}`, constrained by the site license (radius 1).

## The structural collapse (runner Parts A-B)

- **A1 (the 3D degree table):** same-component hops are distance-2 moves, so
  ALL 8 diagonal Bloch entries are momentum-independent — `tr U(k)` is
  structurally CONSTANT in 3D exactly as in 1D. Couplings exist only between
  parity partners; each licensed entry has two offsets, both along the
  partner's own axis.
- **A2 (no axis blending):** each coupling entry lives in ONE variable
  (combinatorial), and unitarity kills the two-term blend — the cross terms
  `conj(c_i) d_i` sit at independent Fourier modes and must vanish
  separately (derived symbolically). No single-tick entry can mix axes.
- **B (the multivariable monomial lemma):** a finite Laurent polynomial in
  `(z_1, z_2, z_3)` unimodular on the torus is a monomial — the corner
  identities are illustrated at degree (1,1); the lemma is proved per
  variable from the 1D lemma plus analyticity (a Laurent coefficient
  vanishing on an open torus subset vanishes identically; the surviving
  power is locally constant on a connected torus). Hence
  `det U(k) = e^{iD} z^{w_1} z^{w_2} z^{w_3}`: an integer winding VECTOR —
  mixed-axis windings are permitted by the structure, and Part D shows they
  are realized.

## The covariant flatness no-gos (runner Parts C, F)

**C — the f(D) class.** Build the staggered NN Bloch operator `D(k)` on the
8-cell with the landed KS phases: Hermitian, spectrum
`+-sqrt(sum_i sin^2(k_i/2))` (the standard staggered dispersion in site
momentum; computed), sweeping a continuum. Any single tick `U = f(D(k))`
with `f` a polynomial — the natural construction covariant under the
staggered (projective) symmetry — must have `|f(lambda)| = 1` on that
continuum, which forces `f` CONSTANT (degree-1 system solved exactly;
degree-2 cascades via the leading coefficient `|c|^2`; and since
`D(k)^2 = sigma(k) I` is scalar, the degree-1 solve already covers the
ENTIRE licensed f(D) class). **The f(D) class is flat.** (Known-literature
comparator, non-derivation context, entered in the loop import ledger: the
no-nontrivial-isotropic-NN-walk obstruction on the primitive cubic lattice;
reproved here for the scalar carrier from the license.)

**F — the permutation-equivariant class.** The complementary covariance
class (the LINEAR axis-permutation representation; the staggered `D` itself
is only projectively covariant, so the two classes genuinely differ): orbit
reduction gives 4 component orbits (parity weight) and 6 hop orbits; the
licensed equivariant family has 4 + 12 complex orbit parameters; unitarity
on the torus reduces to 48 EXACT polynomial equations (derived symbolically
in the runner), containing the per-orbit kill `d conj(c) = 0` for ALL six
orbits and cross-orbit kills `d conj(d') = 0` for the two opposite-side-hop
pairs; the remaining cross-orbit coexistence is excluded at sweep grade
(F2b), not by the exact backbone. Branch-and-propagate over the single-term
bilinear kills collapses the exact system to 25 leaves (deterministic under
the runner's canonical equation ordering; the COVER's completeness is
ordering-independent: any exact solution zeroes a factor of every branched
equation and so descends to some leaf); dense seeded least-squares sweeps
within every leaf's reduced coordinates then find **no dispersive unitary
in any leaf** (F2b; the solution sets are continua — counts are optimizer
endpoints, not a canonical enumeration). Sweep-grade at leaf level with the
exact kill-structure backbone; an exact algebraic closure of the leaf
systems is a registered falsifier surface, not assumed.

**Together:** a 3D single tick covariant in either analyzed sense cannot
transport. 3D dispersion necessarily breaks single-tick axis covariance.

## The licensed dispersive menagerie: quantized drifts (runner Parts D, E)

- **D1:** the single-axis shift is licensed, unitary, dispersive along its
  own axis and flat transversely.
- **D2:** face-diagonal (distance 2) and body-diagonal (distance 3) hops —
  the geometries that the KNOWN nonunit-speed isotropic 3D automata use —
  are license-ILLEGAL at this carrier density (computed from the hop
  vectors). This closes the known comparator family only; D3/D4 show
  nonunit quantized slopes arise WITHOUT diagonal hops.
- **D3 (mixed-cycle witness):** a 4-cycle alternating axes 1 and 2 with two
  across-cell and two within-cell offsets accumulates net winding
  `z_1 z_2`: `U^4 = e^{i(k_1+k_2)} I` on its cycle (computed) — a licensed
  dispersive NON-per-axis tick with slopes (1/2, 1/2, 0) site/tick.
- **D4 (staircase witness, found in review):** hop `+e_1` on
  `x_1+x_2`-even sites and `+e_2` on odd sites: licensed, unitary,
  `W^4 = (unimodular k-scalar) I` exactly — same quantized-nonunit class;
  the 6-cycle variant gives (1/3, 1/3, 1/3).
- **The permutation-class fact:** every licensed permutation tick's bands
  are roots of its cycles' net monomials — EXACTLY linear, slope vector =
  (cycle winding)/(cycle length): rational-QUANTIZED, never tunable.
- **E1:** the eta-decorated per-axis shifts (all axes) satisfy
  `S_i^2 = e^{-ik_i} I` exactly: monomial bands, 1 edge/tick — the
  |slope| = 1 extreme of the menagerie.
- **E2:** the axis permutations (S3) conjugate the factors into each other —
  bare shifts exactly; decorated factors via the pinned diagonal gauge
  `V_p = (-1)^{p_0 p_1}` (computed): the per-axis factors are equal up to
  the staggered gauge.
- **E3:** bare axis shifts COMMUTE; decorated ones ANTI-commute, all pairs
  (computed).
- **E5:** every reordering of the 3-factor cycle is +-(the reference
  order): a central sign, physically equivalent — no ordering dial.
- **E4 (protocol weights):** because `S_i^2 = e^{-ik_i} I` is central,
  unequal-weight protocols factor into the symmetric cycle times quantized
  whole-cell translations (`S1^2 S2 S3 = e^{-ik_1} S2 S3` exactly). Unequal
  weights are therefore additional quantized drifts — REAL transport
  content, still quantized, never tunable. The SYMMETRIC cycle (one factor
  per axis) is part of the factorized-realization premise below, not a
  free lunch.
- **E6 (drift-only — no cone at this density):** every word of decorated
  shifts has `W^2 = (unimodular k-linear scalar) I` (the generators'
  squares are central and all pairs anticommute; verified on random words
  to length 6): EVERY band of EVERY factorized composite is exactly linear.
  **The staggered cone `+-sqrt(sum sin^2(k_i/2))` (Part C's continuum) is
  UNREACHABLE within the factorized class: curved 3D matter dispersion is
  larger-cell/larger-density content — a named open, stated explicitly, not
  implied away.**

## The 3D statement, assembled (honest form)

For the realized carrier density, in 3D:

1. covariant single ticks cannot transport (C, F);
2. the known diagonal-hop nonunit-slope geometries are license-illegal
   (D2), and the nonunit slopes that DO exist (D3, D4) are quantized
   rationals from cycle windings — exactly linear bands, no curvature, no
   continuous dial anywhere exhibited or swept;
3. the per-axis cells are the saturating (|slope| = 1) extreme of the
   quantized menagerie, equalized across axes up to the staggered gauge
   (E2), with no ordering dial (E5) and protocol weights contributing only
   further quantized drifts (E4);
4. **the FACTORIZED-REALIZATION premise** — the realized 3D protocol is the
   SYMMETRIC per-axis cycle — is named, not derived, and is load-bearing
   against an explicitly NONEMPTY competitor class: the slower quantized
   drifts (the D3/D4 class and weighted protocols). It selects among
   QUANTIZED cells; no continuous content hides in it (the block02
   "nonflat" pattern, one level up);
5. the dispersive symmetric composite drifts along its picked octant: it is
   permutation-covariant up to sign, and reflections are broken by the
   drift direction — "axis-permutation-equalized (cubic-equalized) with
   quantized speeds", NOT "fully isotropic".

Under {the block03 conditional set + the factorized-realization premise},
the 3D kinetic structure has every slope quantized, the axes equalized, and
no dial anywhere — with the cone/mass structure of 3D matter explicitly
deferred to larger-cell content (E6).

## The conditional set after this cycle

| entry | status |
|---|---|
| block03 set (P1' site-strictness reading, C-linear automorphism reading, homogeneity reading, R-P single-tick normalization-placement reading, B-W-free, B-W-interacting, scheme-forcing, KS pattern, nonflat tick) | unchanged |
| **factorized-realization premise (symmetric per-axis cycle)** | NEW, named — load-bearing against the NONEMPTY quantized-drift competitor class (D3/D4, weighted protocols); selection among quantized cells, zero continuous content |
| projective-representation enumeration | named refinement: Part F covers the LINEAR permutation representation; the f(D) class covers the projective natural construction; the general projective-equivariant family is the remaining variant |
| amplitude-mixing tunability (non-covariant, non-permutation licensed ticks) | named open: review-round probes were forced flat or inconclusive; no tunable dispersive cell was found, none is claimed impossible |
| the 3D matter cone | named open: provably ABSENT from the factorized class at this density (E6) — larger-cell content |
| 3D simultaneous tick | the structural results above; the previously vague "Weyl-block mixing" open is replaced by the two SHARP named opens in the rows above |

## What this note does NOT claim

- **No registry action, no status claim, no retirement.**
- **The factorized-realization premise is named, not derived** — and its
  competitor class is exhibited, not hidden.
- **No universal nonunit-slope closure:** D3/D4 realize quantized nonunit
  slopes; what is closed is TUNABILITY in everything analyzed.
- **No 3D cone is derived or implied** (E6 proves its absence from the
  factorized class at this density).
- **Free kinetic level; matter sector.** Interacting loops (B-W-interacting)
  unchanged from block03.
- **No empirical input.** The literature comparator is context, entered in
  the loop import ledger, reproved not imported.

## Falsifiers

- A licensed, dispersive, covariant single 3D tick in either analyzed class
  (contradicts C or F).
- A licensed single tick or factorized composite with a CURVED band or a
  continuously tunable slope (contradicts the quantized-drift
  classification; the amplitude-mixing named open is exactly where to
  look).
- A framework derivation selecting a non-symmetric or non-per-axis realized
  protocol (kills the factorized-realization premise).

## No-Go Discipline Gate (for the negative legs)

The negative claims, scoped: "no covariant dispersive single tick (two
analyzed classes)"; "the known diagonal-hop geometries are license-illegal";
"no curvature or continuous slope dial in anything exhibited or swept."

- **N1 alternative routes:** (1) tune f in the f(D) class — RULED OUT
  (continuum unimodularity, exact; `D^2` scalar closes all degrees);
  (2) equivariant coefficient tuning — RULED OUT at sweep grade (F2b) over
  the exact kill backbone; (3) diagonal hop geometries — RULED OUT
  combinatorially (D2; closes that family only); (4) mixed-cycle /
  staircase drifts — NOT ruled out: EXHIBITED (D3/D4), quantized; excluded
  from the realization only by the named premise; (5) amplitude-mixing
  non-covariant ticks — NAMED OPEN (probes forced flat or inconclusive);
  (6) projective-equivariant family — NAMED refinement; (7) larger Bloch
  cells — excluded by block03's periodicity-subgroup computation up to the
  same homogeneity reading.
- **N2 wall independence:** the license wall (A), the unitarity wall (A2,
  F), and the covariance classes (C vs F) are independent — witnessed by
  the staircase (licensed, dispersive, non-covariant), the bosonic family
  (block01), and the genuinely different orbit structures.
- **N3 hidden-wall scan:** "2^3 Bloch cell" — provenance: block03's
  periodicity-subgroup computation (landed KS pattern + homogeneity
  reading, flagged); "linear vs projective representation" — declared;
  "f polynomial" — all degrees covered via `D^2` scalar; "symmetric cycle"
  — promoted INTO the named premise by review (it was an implicit
  assumption of the first draft).
- **N4 residual matching:** the residual addressed is block01's named open
  ("the 3D strict Weyl enumeration ... the quantized 3D cone slope must be
  computed, not assumed") — answered: the licensed quantized slopes ARE
  computed (1, 1/2, 1/3, ... from cycle windings), and the selection of the
  saturating cell is a named premise, not an assumption.
- **N5 rhetoric audit:** "cannot transport" is scoped to the two analyzed
  covariance classes; "dispersive ticks are per-axis objects" was the
  FIRST DRAFT'S overclaim, removed in review — the current text states
  existence, not exhaustiveness; "fully isotropic" likewise replaced by
  "axis-permutation-equalized with quantized speeds".
- **N6 partial-closure scan:** no existing note analyzes 3D ticks.
- **N7 steelman:** "the factorized-realization premise now carries real
  selection content (saturating vs slower quantized cells), so the campaign
  has traded the primitive's dial for a cell-selection premise." Response:
  yes — and that is the entire honest claim. The primitive asserted a
  CONTINUOUS normalization choice; the chain replaces it, everywhere
  analyzed, by selection among QUANTIZED cells under named readings. A
  continuous dial was hunted in four classes across two review rounds and
  not found; its absence beyond the analyzed classes is registered as a
  falsifier, not asserted.
- **N8 cross-cycle echo:** block02's dichotomy {flat, saturating} acquires
  in 3D the intermediate quantized-drift cells — the same structure one
  dimension richer: quantization survives, uniqueness of the dispersive
  cell does not, and the selection moves into the realization premise
  exactly as the nonflat premise did in 1D.

## Dependencies

- [STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md) — block02 (landed): the 1D dichotomy and the monomial-lemma machinery.
- [KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md](KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md) — block01 (landed): the monomial lemma.
- [KINETIC_ISOTROPY_COMPOSITION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-09.md](KINETIC_ISOTROPY_COMPOSITION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-09.md) — block03 (landed): the (2Z)^3 cell and the conditional-set bookkeeping this extends.
- [STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md) — the landed KS phases (`unaudited`, conditionality inherited).
- [STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md](STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md) — one Grassmann per site (`unaudited`, conditionality inherited).
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the target.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or of the kinetic-isotropy primitive. The
independent audit lane is the only status authority.
