# The Native Carrier Is 3d Space Plus Record Time: the Theta Pairing Splits Exactly as Electric x Magnetic, Is a Proper-Rotation Scalar Odd Under Each Unsupplied Orientation Factor, and the Conjugation-Odd Seed Direction Is the Orientation-Odd Direction — a Theta-Like Gauge Seed Requires an Orientation Import (Bounded Theorem + Route Localization)

**Date:** 2026-07-03
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact finite constructions on the landed
carrier template relabeled to the native footing, plus premise-surface
non-supply statements quoted from axiom text; not a terminal no-go, not a
discharge of the theta admission).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Current-main posture (2026-07-07):** theta's Tier-A admission is already
retired on main by the retained 2026-07-05 retirement decision. This note is
banked only as bounded historical/supporting science for the native
record-time orientation-import route; it does not reopen, modify, or supply
authority for that retirement record.
**Primary runner:**
[`scripts/theta_native_record_time_split_orientation_import_localization_2026_07_03.py`](../scripts/theta_native_record_time_split_orientation_import_localization_2026_07_03.py)
**Runner cache:**
[`logs/runner-cache/theta_native_record_time_split_orientation_import_localization_2026_07_03.txt`](../logs/runner-cache/theta_native_record_time_split_orientation_import_localization_2026_07_03.txt)

## Question

The landed carrier result derives the theta charge on the finite Euclidean
4-torus as the cross-plane intersection pairing of the six flux integers,
`Q = m01 m23 - m02 m13 + m03 m12`, and records that a coordinate reflection
flips `Q`
([`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)).
That computation lives on a Euclidean computational surface. The framework
itself is natively three-dimensional space plus record time: the Lattice
axiom supplies `Z^3` — "Physical sites are the points of the cubic lattice
`Z^3`, with nearest-neighbor adjacency, standard translations, and proper
cubic rotations about each site" — and time enters only through the Record
axiom's fixed, permanent records, with "arrow, record-production dynamics,
physical persistence dynamics, time metric, and local observability of
records" all explicitly outside axiom content
([`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)).

Questions answered here on the native footing:

1. What is the native (3d + record-time) content of the 4D carrier pairing?
2. Which supplied transformations act on it, and how?
3. Does the axiom-supplied premise surface determine the datum that fixes
   the sign of `Q` — and if not, what exactly must be imported for a
   theta-like gauge seed to exist?

## Answer

Four exact results (integer/finite linear algebra and finite-dimensional
real-algebra checks; all runner-verified), then the localization corollary.

1. **Native split (Theorem 1).** Labeling direction `0` as the record-step
   direction and `1..3` as the spatial directions, the six fluxes split
   `3 + 3` into electric windings `e_i = m_(0i)` (record-step x spatial
   planes) and magnetic fluxes `b_i = (1/2) eps_(ijk) m_(jk)` (spatial x
   spatial planes), and the carrier pairing is exactly the dot product

   ```text
   Q = e . b ,
   ```

   verified exhaustively (A1) and re-earned at cochain level against the
   landed cup-product construction, `sum F u F = 2 Q` (A2). Every monomial
   of `Q` pairs one electric with one magnetic component; there is no
   purely spatial-spatial and no purely record-record term (A3).

2. **Transformation law (Theorem 2).** Under the supplied proper cubic
   rotations (all 24, embedded with the record direction fixed) `e` is a
   vector, `b` is a vector, and `Q` is invariant. Under the two unsupplied
   flips, `Q` is odd in each factor separately and even in their product:

   ```text
   spatial inversion    P:  e -> -e,  b -> +b,  Q -> -Q
   record reversal      T:  e -> -e,  b -> +b,  Q -> -Q
   double flip        P T:                      Q -> +Q
   full spatial O_h  (S):  e -> S e, b -> det(S) S b, Q -> det(S) Q
   ```

   (B2-B5, exact; cochain-level cell maps agree with the flux-level action,
   B1). The sign of `Q` is exactly one bit: the product orientation
   (spatial orientation times record-order orientation). This sharpens the
   landed "a coordinate reflection flips `Q`" line to its native form.

3. **Orientation non-supply (Theorem 3).** The named premise surface
   carries no such bit. The Lattice axiom supplies nearest-neighbor
   adjacency (unoriented; inversion- and reflection-invariant as an edge
   set, C3), translations, and the **proper** cubic rotations — and naming
   the proper subgroup requires no orientation choice: `det` is
   basis-independent (C1) and the proper subset is closed under conjugation
   by every improper element (C2). Admissibility covariance is likewise
   named for "lattice translations and proper cubic rotations" only. On the
   time side, "A readout value is determined by record content alone", "A
   state is a configuration of records", and the arrow is explicitly
   outside axiom content — no record-order orientation is part of any
   record's content. So neither orientation factor, nor their product, is
   supplied.

4. **The conjugation = orientation-parity bridge (Theorem 4).** The Qubit
   axiom: "A `Cl(3,0)`-compatible real-algebra presentation may be used
   equivalently and adds no further primitive structure." In that
   presentation the complex unit of `M_2(C)` is the oriented volume
   element: `omega = e1 e2 e3 = i` (D1). Every improper generator map
   (inversion, single reflection, all 24 improper elements) extends to a
   **complex-antilinear** real-algebra automorphism — concretely
   `X -> sigma_2 conj(X) sigma_2^(-1)` for inversion — with
   `phi(omega) = det(S) omega`; every proper map extends complex-linearly
   (D2-D5, the linear/antilinear verdict measured, not assumed). Swapping
   the spatial orientation is complex conjugation on the one-site algebra.
   On holonomy reads this is the same flip as loop-orientation reversal:
   for the minimal theta-like insertion
   `w_alpha(U) = 1 + c (e^(i alpha) tr U + e^(-i alpha) tr U^dag)`, the
   alpha-odd direction is `-2 c sin(alpha) Im tr U` (E1), and conjugating
   the link and reversing the loop orientation flip it identically (E2) —
   consistent with the landed dagger/bar evenness of pair reads
   ([`THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)).

**Localization corollary (route statement).** Any construction assembled
from supplied structure alone — unoriented adjacency, translations, proper
rotations, the one-site algebra with its presentation-independent content,
and record contents — is invariant under both orientation swaps (Theorems
3 + 4), while the theta pairing and the seed's odd direction are odd under
exactly that product bit (Theorems 1 + 2 + 4). A swap-closed ensemble sums
the odd seed direction to zero exactly while the even sector survives
(E3); supplying the missing datum — an ordered spatial frame — makes the
odd pairing constructible and frame-odd, `D_(123) = -D_(213) != 0` (E4).
So on the native footing the gauge-side theta seed is **localized to a
single unsupplied datum: an orientation import** (one sign — the product
orientation bit). A theta-like gauge term cannot be sourced from the named
premise surfaces; it can only enter paired with an explicitly imported
orientation-odd datum, and the framework's conjugation-odd import surface
on the mass side is exactly where such a datum already lives in the
admission's decomposition `theta_bar = theta_gauge + arg det M`.

## Authorities and premises

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — quoted
  sentences: the Lattice
  axiom's "nearest-neighbor adjacency, standard translations, and proper
  cubic rotations about each site" and "Sites are distinguished by the
  supplied lattice structure alone"; the Admissibility covariance sentence
  ("covariant under lattice translations and proper cubic rotations"); the
  Qubit sentences ("The full one-site possibility domain has algebraic
  presentation `M_2(C)`", the `Cl(3,0)` equivalence clause, "Possibilities
  are distinguished by the supplied algebraic structure alone"); the Record
  readout sentence ("A readout value is determined by record content
  alone"); "A state is a configuration of records"; the open-gates line
  placing arrow/time-metric outside axiom content; and the Qualification
  ("Further physical structure requires derivation, bridge, explicit
  admission, or approved primitive registration before use as a premise").
- [`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  — the carrier pairing `Q`, its cup-product construction and
  normalization, and the reflection-flip mechanism this note splits
  natively.
- [`GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md`](GAUGE_CENTER_SECTOR_RECORD_CONTEXT_AND_THETA_Q_CHARACTER_GRADING_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-07-01.md)
  — the wall statement `W_theta_Q_context` this campaign addresses.
- [`THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  — dagger/bar evenness of supplied pair reads, which Theorem 4 identifies
  as orientation-blindness.

## Theorem statements and proofs

### Theorem 1 (native electric x magnetic split)

With direction `0` the record-step direction, `e_i = m_(0i)`,
`b_i = (1/2) eps_(ijk) m_(jk)`:

```text
Q(m) = m01 m23 - m02 m13 + m03 m12 = e . b .
```

*Proof.* Direct expansion: `b = (m23, -m13, m12)`, so
`e . b = m01 m23 - m02 m13 + m03 m12 = Q`. Runner: exhaustive over all
`5^6` flux vectors with entries in `[-2, 2]` (A1); cochain-level re-earn
of `sum F u F = 2 Q` with the landed corner representatives and shuffle
cup product at `N = 4` (A2); monomial support is exactly the three
electric x magnetic products, with all `e x e` and `b x b` coefficients
zero (A3). Interpretation: the native theta charge pairs record-step
windings with spatial fluxes — it is a record-time x space object, with
no purely spatial and no purely temporal part.

### Theorem 2 (proper-rotation scalar, odd in each orientation factor)

A coordinate map with signed-permutation matrix `L` acts on fluxes by
`m -> L m L^T`. For `L = diag(1, S)` with `S` in the full 48-element cubic
group: `e -> S e`, `b -> det(S) S b`, `Q -> det(S) Q`. For spatial
inversion `Q -> -Q`; for record reversal `diag(-1, 1, 1, 1)`:
`e -> -e`, `b -> b`, `Q -> -Q`; for the double flip `Q -> Q`.

*Proof.* `e` carries one spatial index (vector); `b` carries two spatial
indices contracted with `eps_(ijk)` (pseudovector); `Q = e . b` picks up
`det(S)`. Record reversal flips the single record index of `e` and leaves
`b` untouched. Runner: B2-B5 exact on integer draws, all 48 elements
swept, with the cell-map pullback on the cochain complex agreeing with
the flux-level action (B1). The sign of `Q` is therefore exactly the
product orientation bit, and no proper rotation reaches it.

### Theorem 3 (the named premise surface supplies no orientation)

Neither the spatial orientation, nor the record-order orientation, nor
their product is supplied by the axiom text.

*Proof.* Spatial side: the supplied data are nearest-neighbor adjacency,
translations, and the proper cubic rotations. The adjacency edge set is
invariant under inversion and every improper signed permutation (C3);
translations commute with them; and the proper subgroup is
orientation-blind as a *named* object — `det` needs no basis or
orientation choice (C1) and the proper subset is invariant under
conjugation by every improper element (C2), so "proper cubic rotations"
picks the same subgroup in either orientation class. Time side: readout
values are determined by record content alone; a state is a configuration
of records; and arrow/time-metric are explicitly outside axiom content —
record-order orientation is not record content. Nothing named
distinguishes the two orientation classes, in either factor.

### Theorem 4 (orientation swap = complex conjugation on the one-site algebra)

In the `Cl(3,0)` presentation of the one-site algebra, `omega = e1 e2 e3`
is central with `omega^2 = -1` and equals the complex unit of the
`M_2(C)` presentation. Any orthogonal generator map `e_i -> sum_j S_(ji) e_j`
extends to a real-algebra automorphism with `phi(omega) = det(S) omega`;
it is complex-linear iff `det(S) = +1` and complex-antilinear iff
`det(S) = -1`. Inversion extends to
`X -> sigma_2 conj(X) sigma_2^(-1)` — complex conjugation up to inner
equivalence.

*Proof.* Orthogonal maps preserve the Clifford relations, so the
extension exists; `omega` is grade 3, picking up `det(S)`. Since `omega`
implements `i`, `phi(omega) = -omega` is exactly antilinearity. Runner:
D1-D5, with the linear/antilinear verdict measured from the constructed
map on the 8-dimensional real basis and compared against the computed
determinant for all 48 elements. On holonomy reads the same flip is loop
orientation reversal: `tr(U^dag) = conj(tr U)`, so the alpha-odd seed
direction `-2 c sin(alpha) Im tr U` flips identically under link
conjugation and under orientation reversal (E1, E2). This identifies the
campaign's conjugation-odd/even split as the native orientation-odd/even
split: the landed dagger/bar evenness of supplied pair reads is
orientation-blindness, stated at the one-site presentation level and
checked on the holonomy reads this campaign actually uses.

### Localization corollary (the seed needs an orientation import)

Supplied-structure constructions are invariant under both orientation
swaps; the theta seed's odd direction is odd under them. A swap-closed
ensemble kills it exactly while the even sector survives (E3, with the
survival count reported); an explicitly imported ordered frame makes it
constructible and frame-odd (E4). Hence, on the native footing, the
gauge-side content of the theta admission is localized to one unsupplied
orientation-odd datum. Under the admission's decomposition
`theta_bar = theta_gauge + arg det M`, the admission already carries a
conjugation-odd import surface on the mass side — the determinant phase,
the natural home of that datum — while the gauge side has no supplied
source for it.

## What this note does and does not claim

- It does **not** claim "parity forbids theta". On the native footing that
  folk route is unavailable: the axioms name **proper** covariance only,
  so spatial parity is not a supplied symmetry, and no vanishing theorem
  is derived from it. The exclusion here runs through non-supply of the
  orientation datum, which is a different and sharper mechanism: it
  localizes what a theta-like term would need, rather than asserting a
  symmetry the axioms do not name.
- It does **not** claim the theta admission is discharged, that
  `theta_gauge = 0` as a physical measurement statement, or anything about
  the measured neutron EDM. The statements are about the supplied premise
  surfaces and exact finite constructions on the carrier template.
- Theorem 4's holonomy-level step is an identification at the presentation
  level plus the checked holonomy reads; a full from-axioms construction
  of the gauge register remains the standing wall, and this note does not
  build it.
- The record-step direction labeling in Theorem 1 relabels the landed
  Euclidean carrier template; deriving that template itself from record
  dynamics remains downstream (arrow and record-production dynamics are
  outside axiom content).

## Residuals and next paths

1. **Action-level pairing selection (ii')**: that the physical action
   class weights sectors by `e^(i theta Q)` for this carrier — the
   assembly adjudication belongs to the audit lane on the landed chain.
2. **Defect (monopole) closure (i-a)**: the carrier residual named in the
   landed 4D note; the linking-obstruction account remains the
   quantitative target.
3. **Mass side**: the orientation-odd import surface `arg det M` — the
   sister lane's account; this note's localization sharpens what any
   nonzero-theta proposal must now supply on the gauge side (an
   orientation import the named premises do not contain).
4. **Native carrier derivation**: replacing the relabeled Euclidean
   template by a record-dynamics-derived carrier once arrow/production
   dynamics enter as derived or admitted content — the next path this
   opens.
