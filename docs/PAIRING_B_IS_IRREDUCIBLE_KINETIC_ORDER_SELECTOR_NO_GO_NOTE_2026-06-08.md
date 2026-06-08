---
claim_id: pairing_b_is_irreducible_kinetic_order_selector_no_go_note_2026-06-08
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# The γ↔Lattice-Edge Pairing B Is an Irreducible Admission; the Residual Is the Kinetic-Order Selector (No-Go) — Completing the su(2) Double-Use Resolution

**Date:** 2026-06-08
**Type:** no_go (+ a conditional-theorem sharpening of the turn-1 companion)
**Primary runner:**
[`scripts/frontier_pairing_B_irreducible_kinetic_order_selector_2026_06_08.py`](../scripts/frontier_pairing_B_irreducible_kinetic_order_selector_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_pairing_B_irreducible_kinetic_order_selector_2026_06_08.txt`](../logs/runner-cache/frontier_pairing_B_irreducible_kinetic_order_selector_2026_06_08.txt)

## Role

This is turn 2 of the su(2)-double-use resolution. Turn 1 (companion
`SU2_DOUBLE_USE_REDUCES_TO_ONE_INDEX_PAIRING_ADMISSION_FORCED_GIVEN_B_BOUNDED_NOTE_2026-06-08`)
reduced the internal↔external su(2) double-use to a single atom

```text
B = "the Clifford/derivative index μ of the (Kähler-/staggered-)Dirac operator
     D = Σ_μ γ_μ ∂_μ  equals the spatial lattice edge-direction μ acted on by O_h"
```

and proved *forced-given-B* (the spin lift is the qubit's own su(2), Skolem–Noether + no
dim-2 spectator). This note settles the **status of B**: it is **NOT** derivable from
{Lattice=Z³, Quantum=Cl(3,0)=M₂(ℂ)/site, Record} together with the dynamics the axioms permit
(locality, O_h-covariance, Hermiticity, Record-formation, the Hodge/Kähler structure). **B is
an irreducible admission — the staggered/Kähler-Dirac realization gate.** Runner **11/11**;
established by a 16-agent map→attack→adversarial-verify→synthesize workflow on which all five
attack angles converged to `B_irreducible` (conf 0.83–0.90).

This is the **rotation-level twin** of the landed boost-faith no-go
[`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md):
local-algebra faithfulness ≠ a faithful physical (rotation) action; covariance *presupposes*
the attachment B, it does not deliver it.

## Conditional-theorem sharpening (closes the turn-1 "wrong-rep hatch")

**GIVEN** a first-order-in-space kinetic operator, B is forced *and unique* among the 2-dim
internal O_h lifts. The T₁(vector) multiplicity in the conjugation rep of `M₂(ℂ)` is (runner
D2, via the O character formula `mult = (1/24)Σ_R |χ_ρ(R)|² Tr R`):

```text
spin/2O lift : 1      trivial lift : 0      E-irrep lift : 0
```

so **only the spin lift hosts a first-order O_h-covariant vector vertex** — and there
`M₂(ℂ)=span{I,σ_i}=A₁⊕T₁` with `U_R σ_i U_R† = Σ_j R_{ji} σ_j` (runner D1), uniquely fixing
`A_μ ∝ σ_μ = B`. This is rep-theoretic, independent of the matched-3=3 count and of the
merger/cubic-lift reading (the turn-1 forbidden inversions). It strengthens turn-1: not only
does GIVEN-B force the qubit su(2), but GIVEN-first-order the spin lift is the *only* 2-dim
lift that can carry the vertex.

## The no-go core: first-order-in-space is the unsupplied antecedent

The antecedent — *"the kinetic operator is first-order Dirac, not second-order scalar
Laplacian"* — is a **dynamics selector absent from the three axioms** (which supply no
dynamics; the staggered-Dirac realization is an open gate *outside* axiom content). A genuine
all-constraints-satisfying **non-B realization survives**: the second-order scalar Laplacian

```text
H(p) = (Σ_μ cos p_μ) · I₂
```

is local (nearest-neighbour), **full-O_h-covariant including spatial inversion** (`cos` is
parity-even), Hermitian, has a valid dispersion, and `[H, σ_i] = 0` exactly (runner B1) — the
**qubit genuinely spectates**. (Turn-1 correction carried: the cleanest spectator witness is
this *parity-even second-order* Laplacian; a *first-order scalar* hop does not exist — its
symbol `Σ_{n∈O-orbit} sin(p·n)` vanishes on every orbit and is parity-excluded under full O_h,
runner A1/A2. This sharpens the turn-1 spectator statement; the turn-1 verdict is unchanged,
since its symmetric hop is itself parity-even.) The first-order γ-vertex
`D=Σ_μ σ_μ sin p_μ` is by contrast qubit-active (`[D,σ_i]≠0`, runner C1).

**No axiom-permitted selector picks first-order over second-order non-circularly** (runner E):

- **Record** is timeless and order-silent (it supplies no dynamics, no kinetic order);
- **Stability/positivity disfavours** first-order — the Dirac symbol `±|sin p|` is unbounded
  below (no ground state), while the Laplacian is bounded;
- **Nielsen–Ninomiya** doubler-control bites *within* the first-order class, it does not force
  the class;
- the only thing that forces first-order is the **isotropic linear Lorentz cone** `|E|=|p|` —
  i.e. the Dirac form itself = B (circular) — and isotropic `SO(3)` is **not** supplied by the
  cubic `O_h` (corroborated by the landed
  [`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
  and the boost-faith no-go).

So the residual is exactly a **kinetic-order selector**, which the axioms do not supply ⇒ **B
is irreducible**.

## Completes the double-use resolution

| turn | result |
|---|---|
| 1 (#3255) | the double-use reduces to the single atom B; **forced-given-B** (spin lift = qubit su(2)); no-go refuted (matched pair `2O→O` consistent) |
| 2 (this) | **B is not forced** by {L,Q,R}+permitted dynamics — an **irreducible admission**; GIVEN-first-order the spin lift is the *unique* 2-dim O_h lift carrying the vertex |

**Net:** the internal↔external su(2) double-use is *forced-given-B + B-is-an-irreducible-
admission* ⇒ net an **irreducible admission, sharpened to a single atom** whose residual is the
**kinetic-order selector**. No open sub-question of the double-use remains.

## Residual and downstream

- **Minimal missing principle:** a lattice-native `O_h`-Wigner-covariance lemma deriving the
  `γ_μ↔e_μ` edge-pairing *and* the first-order kinetic order from {L,Q,R}+retained bridges
  *without* presupposing the γ-edge hopping form — none exists in the repo.
- B additionally gates three further named-open admissions
  ([`STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md`](STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md)):
  FS fermionic statistics, the Euclidean signature/time import, and the chirality selector
  `ε(x)`.
- **Downstream:** this is exactly the dirac-weyl physical-spin-label admission; emergent
  Lorentz's boost-spinor link remains a separate conditional; the Finkelstein–Rubinstein
  rotation→exchange bridge fails on discrete `Z³`, so spin-statistics stays forced-modulo
  {emergent Lorentz + Record}; **d=3 is unchanged** (a `Z³` lattice primitive; the
  `M₂(ℂ)=Cl(3,0)=GA(3)` match is a consistency, not a derivation — #2559/#2586 protected).

## No-Go Discipline Gate (N1–N8)

**N1 — routes:** (a) locality+covariance forcing — *fails* (first-order scalar excluded but
the second-order Laplacian spectates); (b) action axiom-supplied — *no* (axioms supply no
dynamics); (c) Record supplies B — *no* (order-silent); (d) boost-faith no-go extension —
*yes, B not forced* (rotation twin); (e) two-realizations no-go — *constructed* (B vs
Laplacian both axiom-consistent). All → B irreducible. **N2 — wall independence:** the
first-order-scalar exclusion (A), the second-order spectator (B), and the no-selector catalog
(E) are independent. **N3 — hidden-wall scan:** "first-order", "covariance", "isotropy" are
tested, not imported; isotropy is shown *not* supplied by O_h. **N5 — rhetoric audit:**
"irreducible admission" means *not forced by {L,Q,R}+permitted dynamics*, with the precise
unsupplied datum named (the kinetic-order selector); it is **not** a claim that B is false or
physically wrong. **N7 — steelman:** the strongest pro-B case (first-order forces B uniquely)
is *accepted as a conditional theorem* — the gap is solely the first-order antecedent. **N6 —
partial-closure:** a future O_h-Wigner-covariance lemma could promote to
"forced-modulo-covariance" without a new axiom. **N8 — cross-cycle echo:** same pattern as the
boost-faith and cubic-anisotropy no-gos (local structure ≠ forced physical action).

## Reprove-and-cite / guards

Reproven from primitives (numpy, 11/11): the T₁-multiplicity {spin 1, trivial 0, E 0}; the
spin-lift `M₂=A₁⊕T₁` action; the first-order-scalar orbit-vanishing + parity exclusion; the
second-order Laplacian spectator (`[H,σ_i]=0`); the γ-vertex activity; the
Dirac-unbounded-below stability point. **Comparators / landed cites only** (never used to
*supply* B): O character theory, Skolem–Noether, Nielsen–Ninomiya, the boost-faith and
cubic-anisotropy no-gos. No PDG. **Turn-1 inversion guards respected:** B is *not* forced from
the matched-3=3 count, and the merger-273 / Cl(3) cubic-lift are *not* cited to supply B.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- `SU2_DOUBLE_USE_REDUCES_TO_ONE_INDEX_PAIRING_ADMISSION_FORCED_GIVEN_B_BOUNDED_NOTE_2026-06-08.md` (turn-1 companion; PR in flight)
- [`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md)
- [`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
- [`STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md`](STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md)

## What this note does NOT claim

- It does **not** claim B is false/unphysical — only that it is **not forced** by
  {L,Q,R}+permitted dynamics (an admission), with the unsupplied datum = the kinetic-order
  selector.
- It does **not** force B from the matched-3=3 count, nor cite the merger-273 / Cl(3)
  cubic-lift to supply B (turn-1 inversions).
- It does **not** relocate d=3 onto the matter/Dirac dynamics (the #2586-closed move).
- **No** new axiom, primitive, or repo vocabulary; no PDG input; sets no audit status.

**Independent audit required.** This note asserts no effective-status change.
