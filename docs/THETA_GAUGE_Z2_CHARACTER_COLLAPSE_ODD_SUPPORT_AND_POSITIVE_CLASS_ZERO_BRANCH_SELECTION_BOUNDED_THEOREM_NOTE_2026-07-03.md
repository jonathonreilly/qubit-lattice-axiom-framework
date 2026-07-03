# The Gauge-Side Theta Dial Collapses to {0, pi} for Orientation-Even Character Weights on the Odd-Support Sector Lattice, and the Derived Positive Conjugation-Paired Weight Class Selects the Zero Branch — the Gauge Twin of the Mass-Side Pairing-Forced Zero Branch (Bounded Theorem)

**Date:** 2026-07-03
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact character-collapse and class-selection
statements on the landed carrier's sector lattice and inside the landed
positive weight class; not a terminal no-go, not a discharge of the theta
admission, and no claim that the physical action class lies in the positive
class — that adjudication remains open).
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, retire or
re-grade any Tier-A admission, or claim Strong-CP closure.
**Primary runner:**
[`scripts/theta_gauge_z2_collapse_positive_class_zero_branch_2026_07_03.py`](../scripts/theta_gauge_z2_collapse_positive_class_zero_branch_2026_07_03.py)
**Runner cache:**
[`logs/runner-cache/theta_gauge_z2_collapse_positive_class_zero_branch_2026_07_03.txt`](../logs/runner-cache/theta_gauge_z2_collapse_positive_class_zero_branch_2026_07_03.txt)

## Question

The mass side of the theta admission has a landed two-step structure: the
continuous determinant phase is erased down to the discrete set `{0, pi}`,
and the `+-i lambda` pairing then forces the zero branch on the K-real
Case-A surface for both signs of the mass
([`THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md`](THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md)).

The gauge side has the carrier: the theta slot is the character weight
`e^{i theta Q}` on the flux sectors, with odd support (`Q = 1` at unit
complementary fluxes)
([`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)),
and a derived weight class: the multi-plaquette gluing produces sector
weights that are strictly positive on every sector and conjugation-paired,
as members of the positive `2 pi`-periodic class-weight family
([`GAUGE_MULTIPLAQUETTE_CHARACTER_GLUING_EMERGENT_INTEGER_SECTOR_RECORD_CONTEXT_AND_ACTION_PAIRING_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](GAUGE_MULTIPLAQUETTE_CHARACTER_GLUING_EMERGENT_INTEGER_SECTOR_RECORD_CONTEXT_AND_ACTION_PAIRING_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)).
A companion analysis currently in review derives that the named axiom
surfaces supply no orientation datum, so supplied-structure constructions
are even under the sector inversion `Q -> -Q`; in this note that statement
enters only as a named hypothesis ("orientation-evenness"), re-earned in
miniature by the runner, and the note's theorems are unconditional given
their stated hypotheses.

Question answered here: does the gauge side have the same two-step
structure as the mass side — a discrete collapse followed by a forced
branch selection — and what exactly does each step?

## Answer

Yes, with the mechanisms precisely located:

1. **Collapse (Theorem 1).** An orientation-even weight in the theta slot
   — a multiplicative character `w(Q) = e^{i theta Q}` of the sector group
   with `w(Q) = w(-Q)` — must satisfy `e^{2 i theta Q} = 1` on the
   support; with odd support (`Q = 1` realized), this forces

   ```text
   theta in {0, pi} .
   ```

   The continuous theta dial dies without any orientation import; one bit
   survives. Both hypotheses are load-bearing (runner-witnessed): evenness
   alone does not collapse (a non-multiplicative even weight exists), and
   on an even-support sublattice the fixed set is strictly larger (the
   four fourth roots of unity).

2. **The surviving bit is not reachable by the collapse mechanism
   (two-mechanism honesty).** The `theta = pi` character `(-1)^Q` is
   orientation-blind — `(-1)^Q = (-1)^{-Q}`, and it is invariant under
   the spatial frame swap that flips `Q` itself. So orientation
   non-supply cannot distinguish the two branches, and a second, distinct
   mechanism must make the selection.

3. **Selection (Theorem 2).** Inside the derived weight class — per-sector
   weights induced by strictly positive, conjugation-paired dual
   coefficients (heat-kernel member `c_n = e^{-t n^2/2}`; Wilson members
   `c_n(beta) = I_n(beta)`; `SU(3)` Wilson duals at `beta = 6` positive
   and conjugation-paired, re-earned by quadrature) — every sector weight
   is strictly positive. The `theta = pi` branch multiplies odd-`Q`
   sectors by `-1`; odd-`Q` sectors exist (unit complementary fluxes);
   hence the `pi`-branch family attains negative values and is **not a
   member of the positive class**, while `theta = 0` reproduces the class
   identically. Within the derived class the zero branch is selected —
   the gauge twin of the mass side's `+-i lambda` pairing, with
   positivity of the derived coefficients playing the role the eigenvalue
   pairing plays for `det(M + m) >= 0`.

4. **Two-sided assembly (Corollary).** With the gauge branch selected to
   `0` within the derived positive class and the mass branch selected to
   `0` on the K-real Case-A surface (landed), the branch table
   `{0, pi} x {0, pi}` for `theta_bar = theta_gauge + arg det M` lands on
   the `theta_bar = 0` cell — within the stated surfaces and classes, and
   with the class-to-physical-action adjudication named below as the
   remaining item.

## Authorities and premises

- [`THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_4D_CARRIER_FLUX_COHOMOLOGY_INTERSECTION_PAIRING_CLOSED_BRANCH_AND_DEFECT_CLOSURE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  — the theta slot as the sector character `e^{i theta Q}`, the pairing
  `Q`, and its odd support (`Q = 1` at unit complementary fluxes).
- [`GAUGE_MULTIPLAQUETTE_CHARACTER_GLUING_EMERGENT_INTEGER_SECTOR_RECORD_CONTEXT_AND_ACTION_PAIRING_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](GAUGE_MULTIPLAQUETTE_CHARACTER_GLUING_EMERGENT_INTEGER_SECTOR_RECORD_CONTEXT_AND_ACTION_PAIRING_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  — the derived weight class: strictly positive sector weights,
  conjugation pairing, the positive `2 pi`-periodic class-weight family
  and its heat-kernel/Wilson members.
- [`THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md`](THETA_MASS_ORIENTATION_ZERO_BRANCH_PAIRING_FORCED_ON_K_REAL_SURFACE_NARROW_THEOREM_NOTE_2026-07-01.md)
  — the mass-side twin: erasure to `{0, pi}` (its cited chain) and the
  `+-i lambda` pairing-forced zero branch on the K-real Case-A surface.
- [`THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  — dagger/bar evenness of supplied pair reads (the evenness hypothesis's
  landed holonomy-level face).
- Orientation-evenness hypothesis: carried from the in-review native
  orientation non-supply analysis (referenced in prose only; not a
  dependency edge). Its use here is confined to the stated hypothesis of
  Theorem 1, re-earned in miniature by the runner's swap-closed check.

## Theorem statements and proofs

### Theorem 1 (Z2 collapse on odd support)

Let `w` be a sector weight in the theta slot: a multiplicative character
`w(Q) = z^Q` of the sector group `Z`, orientation-even (`w(Q) = w(-Q)`),
with `Q = 1` in the sector support. Then `z^2 = 1`, i.e.
`theta in {0, pi}`.

*Proof.* Evenness plus multiplicativity give `z^{2Q} = 1` for every
supported `Q`; `Q = 1` gives `z^2 = 1`, so `z in {+1, -1}` — the trivial
character (`theta = 0`) or the sign character (`theta = pi`). Runner: the
inversion-fixed character set on a 720-point unitary grid is exactly
`{+1, -1}` (A1). Both hypotheses are necessary: `w(Q) = cos(0.3 Q)` is
even but not multiplicative and lies outside `{0, pi}` (A2); on the even
sublattice `2Z` the fixed set is the four fourth roots of unity —
strictly larger — so the odd support delivered by the carrier is
load-bearing (A3). The evenness hypothesis itself is re-earned in
miniature: the alpha-odd holonomy insertion sums to zero exactly over
swap-closed pairs (A4a).

### Theorem 2 (positive-class zero-branch selection)

In the weight class with strictly positive, conjugation-paired dual
coefficients, every induced sector weight is strictly positive; the
`theta = pi` branch is not realizable in the class, and `theta = 0`
reproduces the class. Hence the derived class selects the zero branch of
Theorem 1's `Z2`.

*Proof.* Positivity of coefficients makes each sector weight a product /
positive combination of positive terms: on a matched-label closed surface
`Z_n = c_n^A > 0` with `Z_n = Z_{-n}` (runner earns this by two
independent code paths, B1); the `SU(3)` Wilson duals at `beta = 6` are
positive and conjugation-paired by direct antisymmetrized-Weyl quadrature
with an orthonormality gate (B2a-c); per-plane positive weights make
every carrier sector weight positive, including on the odd-support
witnesses where `Q = 1` (B3a). The `pi` branch multiplies odd-`Q` sectors
by `-1` and so attains negative values exactly there (B3b) — outside the
positive class. Two-mechanism honesty: the signed family satisfies every
Theorem-1 constraint (it is the `theta = pi` character and is
orientation-blind under the frame swap) yet exits the class (B4) — the
selection is done by the positivity of the derived coefficients, not by
orientation non-supply.

### Corollary (two-sided branch table)

The mass-side mirror is re-earned in miniature: real antisymmetric `M`
has spectrum in `+-i lambda` pairs and `det(M + m I) >= 0` for both signs
of `m`, and a real symmetric perturbation loses the guarantee (B5a-b,
consistency mirror of the landed theorem — no new mass-side claim). The
branch table over `{0, pi} x {0, pi}` with the gauge branch selected by
Theorem 2 and the mass branch selected by the landed pairing theorem
lands on `theta_bar = 0` (B6) — within the stated surfaces and classes.

## What this note does and does not claim

- **No physical-action claim.** Theorem 2 operates within the derived
  positive conjugation-paired weight class — the class the
  multi-plaquette gluing produced on its surface. Whether the physical
  action class lies in (or reduces to) this class on the full carrier is
  the standing action-level pairing adjudication; this note does not
  decide it, and nothing here asserts the physical value of `theta_bar`
  or anything about measured quantities.
- **The collapse is conditional on its named hypotheses**: the character
  form of the theta slot (the landed carrier's `e^{i theta Q}` shape),
  orientation-evenness (hypothesis; derivation in review), and odd
  support (landed). Each is exhibited as load-bearing.
- **The `pi` branch is not excluded by orientation non-supply** — it is
  orientation-blind, and this note says so explicitly; positivity of the
  derived class is the selecting mechanism. A future account that leaves
  the positive class (e.g. sign-carrying weight families) would reopen
  the branch selection, not the collapse.
- The mass-side content is cited, not re-graded; the runner's Case-A
  checks are consistency mirrors in miniature, not new mass-side claims.

## Residuals and next paths

1. **Class-to-action adjudication**: whether the physical action class on
   the carrier lies in the positive conjugation-paired class — the
   assembly item for the audit lane on the landed chain; together with
   the evenness grading (residual 3) it is what stands between the branch
   table and an unconditional gauge-side zero branch.
2. **Surface extension on the mass side**: beyond the staggered-only
   Case-A / K-real surface — the sister lane's account.
3. **Orientation non-supply derivation**: the in-review companion; when
   graded, Theorem 1's evenness hypothesis becomes a cited theorem and
   this note's collapse is premise-complete on the gauge side.
4. **The consolidation frontier this opens**: the admissibility rule's
   behavior under improper maps is unconstrained by the axiom text
   (proper covariance is required; improper behavior is an open
   property). Settling it would either make the framework achiral at rule
   level (pushing weak-sector chirality to an emergent mechanism) or
   supply a derived orientation source that must then appear in both the
   chirality gate and any theta-slot account — one datum, multiple
   shadows.
