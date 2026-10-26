# G_bare Structural Normalization Boundary: Cl(3) -> End(V) -> su(3) -> Wilson Action Chain

**Date:** 2026-04-18 (bounded source hardening 2026-05-24;
source-boundary correction 2026-06-12)
**Type:** bounded_theorem (bounded support plus normalization-obstruction
boundary; not a positive derivation of a physical bare coupling)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_g_bare_structural_normalization.py`
**Status:** source proposal; independent audit required. The source scope is
            self-contained structural-normalization support plus an explicit
            residual action-coefficient boundary, conditional on the admitted
            Wilson plaquette action form and kinetic matching convention.
**Status authority:** independent audit lane. This source note does not assign
            an audit verdict and does not edit audit-owned registry, ledger,
            queue, or publication-status surfaces.

---

## Executive summary

This note records the corrected Path 1 boundary for the `g_bare = 1`
internal-fixation program. It supplies a representation and a triplet
generator basis. Fixing that basis excludes nontrivial positive scalar dilation preserving its Gram matrix.
The standard Wilson-surface calculation then gives the textbook coefficient
relation `beta = 2 N_c / g^2` once the Wilson action form and kinetic matching
convention are supplied.

The corrected boundary is that these facts **do not** derive the physical
bare coupling `g = 1`. They derive only:

```text
fixed canonical generators + supplied Wilson action surface
    -> beta = 2 N_c / g^2,
```

plus the statement that the generator rescaling route `T_a -> lambda T_a` is
not an allowed automorphism of the fixed trace-Gram basis. A separate
action/connection-normalization theorem is still required to set `g^2 = 1`
as a physical input rather than the unrescaled-coordinate convention.

**Verdict:**

- **Claim 1 (supplied representation and triplet):** the balanced chiral
  representation on C^8 is a choice of multiplicities (2,2). Faithfulness
  alone also permits (1,3) and (3,1). A specified triplet and Hermitian
  structure support the usual Gell-Mann construction; this does not select
  that triplet or its physical interpretation from the Clifford algebra.

- **Claim 2 (trace form):** for generators supported on one triplet block,
  `Tr_V(T_a T_b) = Tr_3(T_a T_b) = delta_ab/2`. The dimension of the zero
  spectator block adds no factor. The previously asserted Clifford
  pseudoscalar-adjoint form was not defined on general triplet endomorphisms;
  its identification with this trace form is withdrawn.

- **Claim 3 (Wilson coefficient relation and residual coupling multiplier)**:
  bounded conditional support. The following sub-claims close relative to
  the admitted Wilson action-form and kinetic-matching inputs:

  - (3a) Given canonical orthonormal generators `T_a` satisfying
    `Tr(T_a T_b) = delta_ab / 2`, and an operator-valued connection
    `A_op = sum_a A^a T_a` with *unrescaled* coefficients, the small-`a`
    expansion of `-beta Re Tr(U_plaq)/N_c` matches the continuum
    `(1/g^2) F^2` kinetic term only if `beta = 2 N_c / g^2`.
  - (3b) The positive-scalar-dilation route `T_a -> lambda T_a` is excluded by the
    fixed trace-Gram basis, but this does not exclude an independent action
    coefficient `g^2 = rho`.
  - (3c) Therefore the unrescaled-coordinate convention `g^2 = 1` gives
    `beta = 2 N_c = 6`; the present packet does **not** derive that
    convention as a physical bare-coupling theorem.

  What does NOT close: the Wilson action `S = -beta Re Tr(U_plaq)/N_c` is not
  itself *uniquely derived* from Cl(3) structure — it is the standard
  Euclidean lattice gauge action, and its *functional form* (quadratic in
  `F_munu`, summed over plaquettes) is imported as the standard kinetic
  ansatz. The theorem certifies only that, *given this standard action*,
  the coefficient relation follows from the fixed generator normalization.
  A reviewer who contests the choice of Wilson plaquette action per se (vs.
  improved actions, or non-kinetic corrections), or who asks why the physical
  action multiplier has `g^2 = 1`, is not answered by this theorem.

**Honest verdict**: Path 1 gives bounded support against hidden scalar
generator-normalization freedom, but it does NOT close the physical
action-coefficient objection. On the current admitted Wilson-evaluation
surface, `g_bare = 1 <=> beta = 6` is the unrescaled-coordinate convention
unless a separate theorem fixes the Wilson kinetic coefficient or physical
connection normalization.

---

## Materials and prior surface

This theorem builds on:

- [G_BARE_DERIVATION_NOTE.md](./G_BARE_DERIVATION_NOTE.md) -- bounded
  Cl(3) normalization argument, flagged as convention-vs-constraint.
- [NATIVE_GAUGE_CLOSURE_NOTE.md](./NATIVE_GAUGE_CLOSURE_NOTE.md) -- native
  cubic `Cl(3) / SU(2)` + graph-first `su(3)` structural closure.
- [GRAPH_FIRST_SU3_INTEGRATION_NOTE.md](./GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  -- su(3) closure on selected-axis fiber + complementary swap.
- [THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md](./THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
  -- upstream `hw=1` triplet + exact induced `C_3[111]` cycle.
- `scripts/frontier_native_gauge_family_uniqueness.py` -- runner-side check
  that `Lambda^2(R^n)` is the unique `O(n)`-covariant admissible bivector
  subspace on its stated finite test range.

The no-positive-scalar-dilation step is checked directly in this note and runner:
`T_a -> lambda T_a` changes the fixed trace Gram matrix by `lambda^2` and is
therefore not an automorphism of the canonical normalized generator basis.
The downstream plaquette-observable evaluation row is not load-bearing here;
it consumes `beta = 6` only after the separate unrescaled-coordinate
convention `g^2 = 1` is supplied, rather than supplying that convention.

---

## Claim 1 — Supplied representation and triplet

A complex representation of `Cl(3;C) = M_2(C) ⊕ M_2(C)` on C^8 has
multiplicities m_+,m_- with `2(m_+ + m_-)=8`. It is faithful exactly when
both multiplicities are positive, so the possibilities are (1,3), (2,2),
and (3,1). Their central-projector ranks are respectively (2,6), (4,4),
and (6,2), which distinguish them under unitary conjugation. Chirality
swap exchanges the first and last; it does not identify them with (2,2).
Within a fixed multiplicity pair, *-representations are unitarily equivalent.
An intertwiner between two embeddings need not lie in either one's commutant.

The runner chooses (2,2). It separately supplies a three-dimensional block
and the standard Gell-Mann generators on it. This constructs su(3) but does
not derive the physical color/triplet identification or show a canonical
embedding from Cl(3) alone. Minimizing the positive function
`F(p)=sum_{i<j} p_i p_j` yields simplex vertices; the choice of potential,
positive coefficient and minimization principle are supplied premises.
Neither the selector nor the numerical example establishes their dynamics.

## Claim 2 — Trace form on the supplied triplet

Use the real vector space of traceless Hermitian 3x3 matrices, with
`T_a=lambda_a/2` and bracket `(X,Y) -> -i[X,Y]`. Embed each generator as
`T_a ⊕ 0_5` in End(C^8). The positive real bilinear form is explicitly

```
B_HS(T,S) = Tr_8((T ⊕ 0_5)(S ⊕ 0_5)) = Tr_3(T S).
B_HS(T_a,T_b) = delta_ab/2.
```

Unitary conjugation preserves this form by trace cyclicity. Simplicity
implies that invariant symmetric forms are unique up to scale; it does not
choose the scale 1/2. That scale follows from the supplied Gell-Mann basis.
The runner checks the Gram matrix, its zero-extension and the invariant-form
space in this convention.

The old expression `B_Cl(T,S)=<omega T^bar,S>` did not define an extension
of Clifford conjugation or a pairing on all of End(V). Triplet generators
are not thereby elements of the Clifford image. Positivity and full su(3)
Ad-invariance were unproved, so no ratio to such a form is asserted here.
A future derivation must define the domain, involution and pairing and check
these hypotheses before invoking invariant-form uniqueness.

## Claim 3 — Wilson action coefficient rigidity

### Precise statement

**Claim 3 (Wilson coefficient relation and residual multiplier, narrow
version).** Assume:

- (P1) The continuum limit of the gauge action is `(1/(2 g^2)) Tr(F_munu F^munu)`,
  with `F_munu = partial_mu A_nu - partial_nu A_mu + i [A_mu, A_nu]`,
  `A_mu = A^a_mu T_a`, and `T_a` the canonical orthonormal generators
  with `Tr(T_a T_b) = delta_ab / 2`.
- (P2) The lattice action is the standard Wilson plaquette form
  `S_W = -beta sum_{p} (1/N_c) Re Tr(U_p)` (up to an additive constant).

Then `beta = 2 N_c / g^2` is the coefficient relation making the classical
Wilson surface match (P1). Claims 1 and 2 forbid absorbing `g` by scalar
dilation of the canonical generators (`T_a -> lambda T_a`), because that
changes the fixed trace-Gram basis. They do **not** fix the physical value
of the separate action coefficient `g^2`. Equivalently, for every positive
`rho`, the pair

```text
g^2 = rho,        beta = 2 N_c / rho
```

uses the same canonical generators and satisfies the same Wilson-surface
coefficient relation. The special value `rho = 1` gives `beta = 6` for
`SU(3)`, but this note does not derive `rho = 1` from retained framework
inputs.

### Proof sketch

**(3.a) Small-a expansion of the plaquette (classical lattice QFT).**
Using `U_p = exp(i a^2 F_{munu}^a T_a + O(a^3))`, expanding
`-beta (1/N_c) Re Tr(U_p)` to order a^4 and using
`Tr(T_a T_b) = delta_{ab}/2`, one obtains:

```
S_W = -beta · N_p + (beta / (4 N_c)) · a^4 sum_x sum_{mu<nu} F^a_{munu} F^a_{munu} + O(a^6)
```

(This is textbook: Creutz, Kogut, Montvay-Muenster. Checked numerically
in the runner.)

**(3.b) Matching to the supplied kinetic convention.** With
`Tr(T_a T_b) = delta_ab/2`, the trace/component conversion is
`Tr(F_munu F_munu) = (1/2) F^a_munu F^a_munu`. The coefficient matching is
therefore best stated at the trace level to avoid double-counting
convention drift in the `mu,nu` sums. On the standard Wilson convention
used here, the kinetic surface gives:

```
S_continuum^lattice-equiv = (1 / g^2) · a^4 · sum_x sum_{mu<nu} Tr(F_munu F_munu).
```

Matching this trace-level normalization to the Wilson plaquette expansion
in the textbook `beta = 2 N_c / g^2` convention yields the relation:

```
beta / (2 N_c) = 1 / g^2
<=>  beta = 2 N_c / g^2.
```

For SU(3) with the additional unrescaled-coordinate convention `g^2 = 1`,
`beta = 6`.

**(3.c) What the supplied basis fixes.** Claims 1 and 2
verify that the supplied generators `T_a` have fixed
normalization `Tr(T_a T_b) = delta_ab/2` with no residual scalar freedom.
Writing the operator connection as `A = sum_a A^a T_a` with no additional
factor is the unrescaled-coordinate description. Any attempt to absorb a
physical coefficient by `T_a -> lambda T_a` is forbidden:

- it rescales the generators (forbidden by the fixed trace form in Claim 2;
  the runner explicitly checks that nontrivial positive scalar dilation changes the canonical
  Gram matrix), or
- it rescales the coordinates of the same operator `A`, which is a coordinate
  convention unless a separate action/connection-normalization theorem says
  which coordinate normalization is physical.

Thus the canonical basis fixes the generator normalization but leaves a
residual positive action multiplier `rho = g^2` unless an independent
physical normalization input is supplied.

### What Claim 3 supplies

- Given the Wilson action form `-beta Re Tr(U_p)/N_c` and canonical generators,
  the relation `beta = 2 N_c / g^2` follows on the supplied Wilson surface.
- The direct positive-scalar-dilation exclusion proves that `g` cannot be hidden by
  changing the canonical generator basis.
- The present packet does not derive a physical value for `g^2`; it exposes
  that value as the remaining action/connection-normalization input.
- If the unrescaled-coordinate convention `g^2 = 1` is supplied, then
  `beta = 6`.

### What Claim 3 DOES NOT close

- **The choice of Wilson action itself.** The Wilson plaquette action is
  the *standard* lattice-QFT kinetic action, but it is not derived from
  Cl(3) first principles within this framework. Alternatives (Symanzik
  improved, fermion-induced, Cl(3)-native "volume form" actions) are
  not ruled out by the present chain.
- **The premise (P2).** The claim that the gauge kinetic action should
  be a function of plaquette holonomies at all (vs. arbitrary higher
  loops, or non-kinetic terms) is an external premise.
- **The physical value of `g^2`.** The source does not derive a theorem
  selecting `rho = g^2 = 1` rather than another positive action multiplier
  paired with `beta = 2 N_c / rho`.
- **Dynamical selection.** No dynamical fixed-point argument fixes `g = 1`;
  this is a normalization/rigidity claim, not a running-coupling claim.
- **Continuum-limit interpretation.** If one rejects the assumption
  (P1) that the Wilson action has a continuum limit matching `(1/g^2) F^2`
  (as the framework does, since there is no continuum limit in the
  Planck-lattice hypothesis), then (3.a)-(3.b) become an algebraic
  matching at the lattice scale rather than a continuum-limit matching.
  The algebraic relation `beta = 2 N_c / g^2` still holds by direct
  plaquette expansion at first nontrivial order, but the special value
  `beta = 6` additionally requires the unrescaled `g^2 = 1` convention.

**Circularity audit for Claim 3.**

- Step (3.a) uses only `Tr(T_a T_b) = delta_{ab}/2` (Claim 2 and the direct
  positive-scalar-dilation exclusion), no β or g input.
- Step (3.b) is the canonical QFT matching; uses no β or g input beyond
  the definitional identity being derived.
- Step (3.c) uses Claims 1 + 2 plus the direct trace-Gram positive-scalar-dilation
  check. It does NOT derive `g = 1`; it proves only that a generator scalar
  dilation is not an allowed way to hide `g`.

**Residual boundary**: the claim that `A` is the Cl(3)-native connection
with unit coefficient — vs. `A = g A_raw` for some `A_raw` identified by an
independent Cl(3) criterion — is a definitional choice until an independent
physical normalization theorem is supplied. The direct trace-Gram check
isolates the non-coordinate part: changing the generators themselves changes
the fixed canonical trace form.

### Verdict for Claim 3: **BOUNDED SUPPORT + RESIDUAL MULTIPLIER BOUNDARY**.
Supplies the coefficient relation and excludes generator nontrivial positive scalar dilation.
Does not close the physical action-coefficient normalization.

---

## Full rigidity chain

Combining Claims 1, 2, 3:

```
Cl(3) axioms                              (axiom: {G_mu, G_nu} = 2 delta_munu I)
   |
   | Wedderburn / Schur + supplied balanced 8-dim rep
   v
Cl(3) -> End(V=C^8)                       (supplied multiplicities (2,2))
   |
   | graph-first axis selector + hw=1 + C_3[111]
   v
su(3) ⊂ End(V)                            (supplied triplet embedding, Claim 1)
   |
   | Killing-form rigidity on simple Lie algebras
   v
Hilbert-Schmidt trace on the supplied triplet (Claim 2)
   |
   | direct trace-Gram check: no scalar T_a -> lambda T_a
   v
Canonical orthonormal basis {T_a}, Tr(T_a T_b) = delta_ab / 2
   |
   | Wilson plaquette expansion (standard lattice QFT)
   v
beta = 2 N_c / g^2
   |
   | if the unrescaled-coordinate convention g^2 = 1 is supplied
   v
beta = 6 for SU(3) (conditional on Wilson action form and rho = 1)
```

---

## Circularity audit (global)

The full chain was re-inspected for places where `g_bare = 1` or
`beta = 6` enters as input. Results:

| Step | Uses g as input? | Uses β as input? | Derives g or β? |
|------|------------------|-------------------|------------------|
| Claim 1 (Cl(3) -> End(V)) | No | No | Neither directly |
| Claim 2 (trace form) | No | No | Neither directly |
| Scalar-dilation exclusion | No | No | Derives "no nontrivial positive scalar dilation" |
| Claim 3a (plaquette expansion) | No (symbolic g) | No (symbolic β) | Relation β = 2N_c/g² |
| Claim 3b (matching) | No | No | β = 2N_c/g² |
| Claim 3c (residual multiplier) | Keeps g symbolic | No | no-generator-dilation boundary |

**No circular usage detected.** The final line "β = 6" follows only after
supplying the unrescaled-coordinate convention `g^2 = 1`; it is not derived
by this note as a physical bare-coupling theorem.

**Important caveat**: the downstream plaquette-observable evaluation row uses
`β = 6` as an evaluation input. This source supports the Wilson coefficient
relation and the no-generator-dilation boundary, but it does not upgrade
`g^2 = 1` from convention to retained physical theorem.

---

## Runner verification

Companion runner: `scripts/frontier_g_bare_structural_normalization.py`.

The runner performs explicit symbolic/numeric verification:

- **Section A (Claim 1):** Explicit construction of the Cl(3;C) = M_2(C) ⊕ M_2(C)
  chiral representation on C^8 = C^2 ⊗ C^4 with:
  - Cl(3) anticommutator `{G_mu, G_nu} = 2 delta_munu I_8` verified numerically.
  - Pseudoscalar `omega = G_1 G_2 G_3` squares to `-I` verified.
  - Chirality projectors commute with Cl(3)-even subalgebra.
  - Graph-first selector (trace invariant) minima at three axis vertices.
  - Canonical su(3) embedding on the triplet block by the inline Gell-Mann
    construction.

- **Section B (Claim 2):** Explicit computation of:
  - `Tr_V(T_a T_b)` for a, b ∈ {1,...,8} Gell-Mann indices.
  - `Tr_3(T_a T_b)` restricted to the triplet block.
  - Zero-extension of the triplet generators to C^8 leaves their trace unchanged.
  - Ad-invariance of the HS form under a sampled su(3) rotation.
  - One-dimensionality of the invariant symmetric-form space.

- **Section C (Claim 3):** Explicit plaquette small-a expansion:
  - Build small SU(3) links `U_mu(x) = exp(i a A^a_mu T_a)` with random A.
  - Compute `-beta Re Tr(U_p) / N_c` and extract `O(a^4)` coefficient.
  - Verify matching with `(1/(2 g^2)) F^2` continuum form.
  - Verify the family `beta = 2 N_c / rho` for several positive
    `rho = g^2` values using the same canonical generators.
  - Verify that rescaling generators `T_a -> lambda T_a` changes the
    trace Gram matrix and is therefore not an admissible automorphism of
    the canonical basis.

- **Section D (end-to-end):** Confirm that `Cl(3) axioms` + `graph-first
  selector input` + `Wilson action form` => `beta = 2 N_c / g^2` with no
  circular step; `beta = 6` appears only after supplying `g^2 = 1`.

**Runner results**: see final section.

---

## Premises table

| Premise | Scope | Current role in this bounded source |
|---|---|---|
| Cl(3) anticommutator axiom | framework axiom | current framework premise |
| Cubic `Z^3` taste substrate | framework axiom | current framework premise |
| Wedderburn / Schur for Cl(3;C) | pure math | standard math input |
| Graph-first axis selector | supplied positive potential/minimization | physical selection not derived here |
| `hw=1` triplet + C_3 cycle | upstream theorem row | dependency subject to audit status |
| `M_3(C)` generation on triplet | upstream theorem row | dependency subject to audit status |
| Killing-form rigidity on simple Lie algebras | pure math | standard math input |
| Standard Wilson plaquette action | lattice-QFT convention | admitted action-form input, not derived from Cl(3) |
| Standard small-a plaquette expansion | pure math | standard expansion input |
| Canonical kinetic-term convention `(1/g^2) F^2` | QFT convention | admitted matching convention |
| Physical value of `g^2` / Wilson action coefficient | open bridge | not derived here |

**Weak link**: the Wilson plaquette action form and the physical value of the
action coefficient remain admitted/open. The framework uses `beta = 6` for
downstream plaquette evaluation only after taking the unrescaled-coordinate
convention `g^2 = 1`; this note does not close the question of whether an
alternative action or a native action-normalization theorem would select the
same value.

**Bounded reading**: given that the community-standard Wilson plaquette action
is the admitted lattice kinetic term on the current Wilson-evaluation surface,
the supplied generator normalization supports
the Wilson coefficient relation, with no remaining continuous scalar freedom
in the generators. The physical action multiplier remains open.

---

## Paper-safe wording

> Given a supplied chiral representation, triplet embedding and Gell-Mann
> normalization, the triplet trace Gram is delta_ab/2. The supplied Wilson
> action and kinetic convention yield beta=2N_c/g^2. Neither faithfulness,
> invariant-form uniqueness nor these finite checks selects the chiral
> multiplicities, a physical triplet, or g^2=1. The physical
> action-coefficient normalization remains open.

---

## What this does and does not close

### What it closes

- The residual objection that `g_bare` might be hidden in a scalar
  rescaling of the fixed Cl(3) generator basis.
- Equivalence within a specified chiral multiplicity pair; the discrete
  multiplicities themselves remain supplied.
- The structural relationship `beta = 2 N_c / g^2` on the admitted SU(3)
  Wilson-evaluation surface, conditional on the admitted Wilson action form,
  with no circular input.

### What it does not close

- The question of whether the Wilson plaquette action itself is forced
  by Cl(3) structure (vs. any other standard lattice action).
- The physical normalization theorem selecting `g^2 = 1` rather than a
  residual positive action multiplier `rho`.
- Dynamical running of `g`: this is a bare-coupling / UV normalization
  statement, not a flow claim.
- The downstream phenomenology using `beta = 6` as an evaluation input
  (that belongs to the plaquette-observable evaluation lane, not this note).

---

## Commands

```bash
python3 scripts/frontier_g_bare_structural_normalization.py
```

Expected: all structural checks PASS; the bounded sections document the
action-choice and action-coefficient gaps honestly (they are status markers,
not failures).

---

## Next steps (outside scope of this note)

- Attempt to derive the Wilson plaquette action form and its physical
  coefficient normalization from Cl(3) first principles (e.g., as the minimal
  gauge-invariant curvature square in the Cl(3) volume-form induced measure).
  If that closes, Claim 3 could move beyond this bounded admitted-action-form
  scope after independent audit.
- Alternatively, demonstrate robustness of the `rho = 1` normalization
  across the natural family of lattice gauge actions (Wilson, Symanzik,
  fermion-induced), showing the normalization is action-choice-independent
  at leading order.
