# Two-seam forest gauge and Polyakov-holonomy preservation

**Date:** 2026-07-12
**Type:** bounded_theorem
**Status:** unaudited candidate; independent audit alone assigns retained status.
**Primary runner:** [`scripts/two_seam_forest_gauge_polyakov_holonomy_2026_07_12.py`](../scripts/two_seam_forest_gauge_polyakov_holonomy_2026_07_12.py)
**Cached output:** [`logs/runner-cache/two_seam_forest_gauge_polyakov_holonomy_2026_07_12.txt`](../logs/runner-cache/two_seam_forest_gauge_polyakov_holonomy_2026_07_12.txt)

## 0. Result and exact boundary

On an even periodic Euclidean-time circle, global temporal gauge
`U_0=I` erases the Polyakov holonomy and therefore does not represent the
full periodic gauge theory. This note replaces that invalid step with an
exact plane-adapted forest construction.

For either adjacent reflection plane `theta_j`, `j=0,1`, the two temporal-link
layers crossed by that reflection form a matching. They may be gauge-fixed to
identity with a constant Faddeev--Popov factor equal to one. The slice is
reflection invariant, the staggered Berezin Jacobian is one, and every
Polyakov conjugacy class remains realizable on the unfixed temporal links.
On the slice, both Wilson seam plaquettes reduce to the retained spatial-link
convolution form and both fermion seams reduce to the positive crossing matrix
of the twisted-antiperiodic circle repair.

The two adjacent planes require **separate plane-adapted charts**. A literal
identity-link condition that contains all four seam layers and is invariant
under both adjacent reflections closes to the entire temporal circle. It is
not a forest and forces trivial Polyakov holonomy. This is a narrow graph
statement about that common-chart proposal, not a no-go for compensated
reflections, holonomy-distributed gauges, or gauge-covariant proofs.

The proved output is the forest/Haar/holonomy bridge and the seam-local
Wilson-times-fermion positive kernel. A complete coupled finite-circle
reflection-positive Gram, adjacent-plane compressed-correlation identity,
infinite-time transfer semigroup, and continuum limit are not claimed here.
They are the next controlled target.

No axiom-update stop is established. The obstruction removed here was a
gauge-orbit and measure-coordinate problem, not a contradiction in the four
axioms.

## 1. Setting and supplied model conditions

Let

```text
Lambda = Z_(2N) x Lambda_s,       N>=2,                                (1.1)
```

where `Lambda_s` is a finite spatial lattice. Temporal links are
`U_0(t,x) in SU(3)` and spatial links are `U_k(t,x) in SU(3)`. Gauge
transformations act by

```text
U_mu(y) -> q(y) U_mu(y) q(y+mu)^dagger.                                (1.2)
```

The bounded theorem consumes, rather than derives from the axioms:

1. the finite periodic `SU(3)` Wilson-link model with normalized Haar measure;
2. the fundamental staggered-fermion link coupling with `m>0`;
3. antiperiodic temporal fermion wrap and the transported reflection phase;
4. a gauge-invariant positive-half cylinder algebra.

The phrase **gauge-invariant/dressed cylinder algebra** must be read with this
boundary: the theorem is immediate for gauge-invariant Wilson-loop, meson,
and baryon cylinder polynomials. A charged dressed extension requires an
explicit chart-dependent dressing and contraction of residual root charges;
arbitrary bare gauge-variant observables are not included.

The load-bearing prior results are:

- the [periodic staggered-circle repair](PERIODIC_STAGGERED_OS_CIRCLE_FAILURE_TWISTED_ANTIPERIODIC_FREE_REPAIR_BOUNDED_THEOREM_NOTE_2026-07-12.md), which supplies the two positive fermion seam matrices and adjacent reflection phases;
- the retained [temporal-gauge mixed-kernel factorization](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md), used only after the seam links have legitimately been fixed;
- the [coupled two-slice Wilson-times-staggered Gram](RP_COUPLED_TWO_SLICE_GAUGE_STAGGERED_BEREZIN_GRAM_NARROW_THEOREM_NOTE_2026-07-10.md), which supplies the local tensor-kernel composition pattern.

No full-circle claim inherits the June construction that sets every temporal
link to identity. That operation is valid only on the trivial-holonomy
restriction when time is periodic.

## 2. The plane-adapted seam forest

For the reflection plane between `j` and `j+1`, define

```text
r_j(t) = 2j+1-t mod 2N.                                                (2.1)
```

A forward temporal edge with base time `t` is reflected to the reversed edge
with base time

```text
sigma_j(t) = 2j-t mod 2N.                                              (2.2)
```

Define the seam edge set

```text
F_j = { ((t,x),(t+1,x)) : t in {j,j+N}, x in Lambda_s }.               (2.3)
```

### Theorem 2.1 -- forest and reflection invariance

For every `N>=2`, `F_j` is a matching and hence a forest. It is invariant
under `theta_j` with every forest edge mapped to itself with reversed
orientation.

**Proof.** The two base layers `j` and `j+N` have disjoint endpoint slices
when `N>=2`. Thus every vertex is incident to at most one edge of `F_j`, so
there is no cycle. Equation (2.2) gives

```text
sigma_j(j)=j,       sigma_j(j+N)=j-N=j+N mod 2N.                        (2.4)
```

Both edge layers are fixed setwise. Reversal sends `I` to `I`, so the slice
`U_e=I` for `e in F_j` is `theta_j` invariant. ∎

The runner checks the forest rank and computes the reduced incidence
determinant exactly by fraction-free Bareiss elimination. For
`2N=4,6,8,10` and `j=0,1`, it obtains `|det B_red|=1`.

## 3. Constructive gauge fixing and exact measure factor

Choose one root in every forest component. Put `q(root)=I`, and along an
oriented forest edge `e:s->t` define recursively

```text
q(t)=q(s) U_e.                                                         (3.1)
```

Then

```text
q(s) U_e q(t)^dagger=I.                                                (3.2)
```

Because `F_j` is a forest, the recursion is unambiguous and reaches every
nonroot exactly once. Conversely, the original links are reconstructed from
the fixed links, the transformed nonforest links, and the same vertex
matrices. Thus the map is a bijective triangular change of variables before
the residual root freedom is quotiented.

### Theorem 3.1 -- normalized Haar disintegration

For every integrable gauge-invariant link functional `A`, normalized Haar
bi-invariance gives

```text
int [product_(e in E) dU_e] A(U)
 = int [product_(e notin F_j) dV_e] A(V)|_(V_e=I, e in F_j).            (3.3)
```

The omitted forest-edge Haar volume is one. The normalized Haar bi-invariance
is the exact non-Abelian measure input. The reduced incidence matrix is also
unimodular, so the linearized/combinatorial Faddeev--Popov certificate is

```text
|det B_red|^dim(SU(3)) = 1^8 = 1.                                     (3.4)
```

**Proof.** Eliminate one leaf edge at a time. At a leaf, replace all links
incident on the leaf and the leaf matter fields by their translate under the
vertex group element that sends the unique forest link to identity. Left and
right Haar translations preserve every link measure. Gauge invariance removes
the group element from `A`, and normalized Haar integration of that element
is one. Repeat until every forest edge is eliminated. This is the compact-group
tree-gauge proof of (3.3); it does not infer the global non-Abelian measure
identity from the linearized determinant in (3.4). ∎

For staggered matter, transform `chi->q chi` and
`bar(chi)->bar(chi) q^dagger`. Since `det q=1`, the paired Berezin Jacobian is

```text
[det(q)]^(-1) [det(q^dagger)]^(-1)=1.                                  (3.5)
```

Residual transformations are constant on each forest component and preserve
the slice. They must still be contracted in a dressed charged algebra; they
do not affect gauge-invariant observables.

The runner's exact `Z_3` enumeration is only a **finite-group analogue** of
(3.3). It tests the orbit-counting shape and a gauge-variant negative control;
it does not prove SU(3) Haar invariance. The analytic normalized Haar
bi-invariance and leaf-elimination proof above carries that burden.

## 4. Residual temporal holonomy is not erased

At spatial base point `x`, define the Polyakov line

```text
P_x = U_0(0,x) U_0(1,x) ... U_0(2N-1,x).                               (4.1)
```

Under a periodic gauge transformation, intermediate vertex factors telescope:

```text
P_x -> q(0,x) P_x q(0,x)^dagger.                                      (4.2)
```

Hence its conjugacy class and trace are unchanged. On the forest slice,

```text
P_x = product_(t notin {j,j+N}) V_0(t,x),                              (4.3)
```

with the original cyclic order retained. At least two temporal links remain
unfixed for `N>=2`. For every supplied `H in SU(3)`, set one unfixed link to
`H` and all other temporal links to identity. Then both seam layers satisfy
the gauge condition and `P_x=H`. The residual temporal holonomy is therefore
arbitrary, not merely nontrivial in a numerical sample.

The runner checks the full matrix relation (4.2), not only `Tr P`, and also
constructs the arbitrary-`H` witness.

## 5. Exact seam reductions

### Lemma 5.1 -- Wilson plaquettes

For a temporal-spatial plaquette based at a seam time `t in {j,j+N}`,

```text
U_p = U_0(t,x) U_k(t+1,x)
      U_0(t,x+k)^dagger U_k(t,x)^dagger.                               (5.1)
```

Both temporal-link layers are in `F_j`, so on the slice

```text
U_p = U_k(t+1,x) U_k(t,x)^dagger.                                     (5.2)
```

Thus each seam Wilson weight is the spatial-link convolution kernel

```text
K_beta(V,W)=exp[(beta/3) Re Tr(V W^dagger)],       beta>=0.             (5.3)
```

used by the retained factorization theorem. It is a positive-type kernel.
Indeed, expanding the two exponentials in
`Re Tr=(Tr+overline(Tr))/2` writes (5.3) as a sum of tensor-power matrix
coefficient Grams with nonnegative coefficients.

The orientation dagger is load-bearing. On a fixed sampled `SU(3)` family,
the runner finds the correct kernel PSD and the dropped-dagger real kernel
has a strictly negative Gram eigenvalue.

### Lemma 5.2 -- staggered temporal crossings

On the same two seam layers, the temporal link in the staggered hop is also
identity. The antiperiodic wrap and plane-transported reflection phase from
the periodic-circle repair therefore reduce each site-color label to the
exact four-feature coefficient matrix

```text
C_r = diag(1,1/2,1/2,1/4).                                            (5.4)
```

For all seam labels,

```text
C_f = tensor_r C_r >= 0.                                               (5.5)
```

The seam-local joint crossing coefficient is consequently

```text
K_beta tensor C_f >= 0,                                                (5.6)
```

and the two circle seams tensor two such positive kernels. This removes the
specific Polyakov-holonomy obstruction that prevented legitimate use of the
open-time crossing suppliers on a circle.

Equation (5.6) is a seam-local theorem. The complete coupled circle Gram also
requires one written global side-action covariance and moment-vector
factorization for both seams, including the gauge-invariant observable
domain. That final composition is deliberately left to the next note rather
than inferred from a sampled kernel.

## 6. Why the adjacent planes use different charts

Translation by one temporal site maps `F_j` to `F_(j+1)`. Therefore the two
adjacent reflection classes have equivalent, but different, forest charts.
For gauge-invariant functionals, (3.3) computes the same original orbit
integral in either chart. No chart is assigned physical status.

### Theorem 6.1 -- no single common forest of the literal identity-link kind

Suppose an identity-link set contains all four crossing layers

```text
F_0 union F_1 = {0,N,1,N+1}                                           (6.1)
```

and is invariant under both edge reflections
`sigma_0(t)=-t` and `sigma_1(t)=2-t`. Their composition is translation by
two:

```text
sigma_1 sigma_0(t)=t+2 mod 2N.                                       (6.2)
```

Because (6.1) contains both base times `0` and `1`, closure under (6.2)
contains the entire even orbit and the entire odd orbit. It therefore
contains every temporal-link layer. At each spatial point the selected graph
is the full temporal cycle, has cycle rank one, is no longer a forest, and
the identity condition forces `P_x=I`.

Thus there is no single common forest that simultaneously fixes all four
adjacent-plane seam layers to identity, remains invariant under both
reflections, and preserves arbitrary holonomy. This does not exclude a
compensated reflection, a non-identity holonomy-distributed gauge, or a direct
gauge-covariant proof. None is needed for the separate-chart orbit integrals.

## 7. Runner certificate

The paired runner performs 37 gates when the source contract is present.
Its substantive checks include:

- exact reduced-incidence determinants for `2N=4,6,8,10`, both planes;
- the `1^8` Faddeev--Popov factor and residual-component count;
- constructive `SU(3)` gauge fixing and full-link reconstruction;
- unit staggered Berezin Jacobian;
- Wilson-action and reflection covariance;
- Polyakov matrix conjugacy, trace preservation, and arbitrary-holonomy
  realization;
- both seam plaquette reductions;
- the exact common-chart closure/cycle rejector;
- the exact `Z_3` finite-group analogue and a gauge-variant negative control;
- sampled Wilson-kernel PSD, its tensor with (5.4), and the dropped-dagger
  negative control;
- source-boundary and No-Go Discipline N1--N8 schema guards.

The numerical `SU(3)` checks are deterministic fixed-seed exercises. They
test the construction and falsifiers; the general Haar theorem is the
analytic proof in Section 3.

## 8. Honest boundary and next target

This note proves:

1. exact plane-by-plane forest gauge fixing at both circle seams;
2. unit normalized-Haar and Berezin measure factors;
3. preservation and arbitrary realizability of Polyakov holonomy;
4. exact Wilson and staggered seam reductions;
5. positivity of the seam-local Wilson-times-fermion crossing kernel;
6. the narrow common-literal-identity-forest impossibility theorem.

It does not prove:

- a full coupled finite-circle reflected Gram on the positive-half algebra;
- a chart-independent charged-field dressing;
- a finite-circle transfer semigroup or Hamiltonian;
- the interacting infinite-time, thermodynamic, or continuum limit;
- Lorentz invariance, unitarity, QFT/Standard-Model identification, or GR;
- selection of the Wilson-staggered action, `SU(3)`, coupling, mass, spin
  structure, reflection phase, or physical observable algebra from the four
  axioms.

The highest-leverage next step is now sharply isolated: write the two-seam
side-action decomposition and exact full coupled circle Gram in the separate
`F_0,F_1` charts, then derive the adjacent-plane compressed-correlation
identity without calling a finite-circle object a transfer semigroup.

## 9. No-Go Discipline N1--N8

The negative boundary under review is only Theorem 6.1. The broader claim
"periodic coupled reflection positivity is impossible" is rejected by the
successful separate-chart route.

### N1 — alternative-route enumeration

| Route | Marker | Attempt and result |
|---|---|---|
| Separate `F_0,F_1` charts | `ATTEMPTED` | This succeeds for gauge-invariant orbit integrals, so it defeats any broad gauge-fixing no-go but does not refute the literal one-common-forest graph theorem. |
| One global temporal gauge | `ATTEMPTED` | It sets every temporal link to identity and therefore lands exactly on the trivial-Polyakov restriction. |
| One common identity-link forest containing all four seams | `ATTEMPTED` | Exact closure under the two reflections gives every temporal edge and cycle rank one, so the requested set is not a forest. |
| A parity-matching common invariant forest | `ATTEMPTED` | Such matchings can exist, but they do not contain all four seam layers and therefore do not perform the requested simultaneous crossing reduction. |
| Compensated reflection | `ATTEMPTED` | It falls outside the literal identity-link/invariant-forest hypotheses; it remains an open alternative and is explicitly not excluded. |
| Holonomy-distributed non-identity gauge | `ATTEMPTED` | It also falls outside the narrow theorem and remains open; no universal gauge-fixing no-go is claimed. |
| Direct gauge-covariant proof without gauge fixing | `ATTEMPTED` | This bypasses the common chart rather than furnishing the forbidden common forest; it remains available for the full Gram. |
| Gauge-variant bare observables | `ATTEMPTED` | The exact finite-group negative control shows forest disintegration cannot simply erase forest variables for a noninvariant integrand. Dressed observables require residual-charge contraction. |

Eight distinct routes were separated. The successful and open routes force
the negative statement to remain the exact common-literal-forest theorem.

### N2 — wall-independence audit

The theorem closes the holonomy/gauge-coordinate residual. The remaining
conditions are:

| ID | Remaining condition |
|---|---|
| `C1` | Derive or select the coupled local action/admissibility law rather than supply Wilson-staggered dynamics. |
| `C2` | Derive or select the antiperiodic spin structure and transported reflection phase. |
| `C3` | Construct a chart-independent charged/dressed physical cylinder algebra beyond gauge-invariant composites. |
| `C4` | Prove the full coupled two-seam Gram, adjacent-plane compressed correlation, and infinite-time transfer semigroup. |
| `C5` | Control the interacting renormalized continuum and Standard-Model/QFT identification. |
| `C6` | Derive the gravitational/GR sector and its joint limit. |

| Pair | Does closing first close second? | Does closing second close first? | Independent? |
|---|---:|---:|---:|
| `C1,C2` | no | no | yes |
| `C1,C3` | no | no | yes |
| `C1,C4` | no | no | yes |
| `C1,C5` | no | no | yes |
| `C1,C6` | no | no | yes |
| `C2,C3` | no | no | yes |
| `C2,C4` | no | no | yes |
| `C2,C5` | no | no | yes |
| `C2,C6` | no | no | yes |
| `C3,C4` | no | no | yes |
| `C3,C5` | no | no | yes |
| `C3,C6` | no | no | yes |
| `C4,C5` | no | no | yes |
| `C4,C6` | no | no | yes |
| `C5,C6` | no | no | yes |

The rows are separate deliverables: even when one is useful upstream of
another, proving it does not automatically prove the other. No holonomy wall
is retained in this collapsed set because Sections 2--5 close it.

### N3 — hidden-condition phrase scan

| Phrase class | Hits and classification |
|---|---|
| `we assume` | none |
| `by construction` | none used as a proof substitute; the explicit recursion (3.1) and inverse reconstruction carry the claim |
| `as is standard` / `naturally` / `obviously` | none |
| `the framework provides` | none |
| `bridge context` / `background` | occurrences are descriptive and non-load-bearing; all model conditions are listed in Section 1 |
| `standard QFT` | none |
| `registered` / `canonical` | none used to grant a scientific premise |

The hidden-condition scan adds no wall. Normalized Haar measure, gauge
invariance, the coupled action, and the spin/reflection choice are explicit.

### N4 — citation/residual matching

| Cited witness | Witness residual | Present use | Match? |
|---|---|---|---:|
| [`PERIODIC_STAGGERED_OS_CIRCLE_FAILURE_TWISTED_ANTIPERIODIC_FREE_REPAIR_BOUNDED_THEOREM_NOTE_2026-07-12.md`](PERIODIC_STAGGERED_OS_CIRCLE_FAILURE_TWISTED_ANTIPERIODIC_FREE_REPAIR_BOUNDED_THEOREM_NOTE_2026-07-12.md), Sections 3 and 6 | both fermion seams and the residual gauge holonomy target | supplies exactly the seam phase/`C_f` and names the holonomy bridge closed here | yes |
| [`GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md`](GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md), Statement and T1 | mixed plaquette after legitimate identity temporal links | used only seam-by-seam after (3.2) | yes |
| [`RP_COUPLED_TWO_SLICE_GAUGE_STAGGERED_BEREZIN_GRAM_NARROW_THEOREM_NOTE_2026-07-10.md`](RP_COUPLED_TWO_SLICE_GAUGE_STAGGERED_BEREZIN_GRAM_NARROW_THEOREM_NOTE_2026-07-10.md), Sections 2--4 | local Wilson-times-fermion crossing composition | used for the same local tensor-kernel pattern, not for a circle theorem | yes |
| `GAUGE_OS_STEP1_WILSON_PLAQUETTE_DECOMPOSITION_THETA_INVARIANCE_REFLECTION_HERMITICITY_NARROW_THEOREM_NOTE_2026-06-02.md`, Section 1.4 | global temporal-gauge open/companion setup | not used as a full-circle authority because its periodic reading would erase holonomy | no; dropped as load-bearing |

No mismatched citation is used to claim closure.

### N5 — rhetoric and resolution audit

The phrase "no single common forest" is tested at the exact lattice-wide
edge-set resolution required by Theorem 6.1. At per-edge resolution, each
individual seam can be fixed; at per-plane resolution, `F_0` and `F_1` are
valid forests; at the two-plane/lattice-wide resolution, closure of the
all-four-seam set is the full temporal cycle. The negative statement is not
extended to compensated maps, non-identity gauges, gauge-covariant kernels,
or arbitrary gauge choices. No per-element failure is inflated into a
universal gauge-theory claim.

### N6 — partial-closure, convention, reframe, and primitive scan

The primitive registry contains the minimal axioms, scale-reference,
kinetic-isotropy, and realized-state primitives. None supplies gauge fixing,
Haar measure, a Wilson-staggered action, a spin structure, reflection phase,
or a probability/dynamics rule. None is misclassified as a wall here.

The successful partial-closure path is precisely the separate-chart reframe:
gauge-invariant orbit integrals do not require a common gauge slice. That
reframe closes the Polyakov-coordinate residual without a new axiom or new
primitive. Compensated-reflection and holonomy-distributed gauges remain
possible further refinements. Therefore this note does not say that any
remaining condition "requires a new axiom."

### N7 — hostile steelman

A hostile reviewer should reject any broad no-go immediately: the demand for
one literal identity-link forest is gratuitous. A compensated reflection can
move a residual Polyakov link, a holonomy-distributed gauge can leave crossing
links nontrivial while preserving a positive character kernel, and a direct
gauge-covariant OS proof may never choose a slice. The strongest existing
counterexample to the broad no-go is already Sections 2--5: separate
`F_0,F_1` charts preserve arbitrary holonomy and reduce the two seams exactly.
This steelman succeeds, so the broad no-go is not shipped. It does not touch
the narrow orbit-closure proof, whose hypotheses explicitly require one
common reflection-invariant identity-link forest containing all four seams.

### N8 — cross-cycle echo

Prior repo walls involving temporal gauge were often retired by narrowing an
overbroad global gauge statement to a local seam or open-time statement. The
May mixed-kernel theorem is retained at exactly that local temporal-gauge
scope. The July periodic-circle note then exposed the missing Polyakov
residual rather than declaring gauge coupling impossible. This cycle uses the
same successful mechanism: replace the global gauge with a plane-adapted
forest and preserve the residual variable. Similar convention/coordinate
walls elsewhere were retired by separating a derived algebraic core from a
choice of labels or chart. That mechanism has been applied here, so no
cross-cycle retirement path is ignored.

**No-Go Discipline result:** PASS for the narrow Theorem 6.1 boundary;
broader no-go language is rejected.

## 10. Axiom-stop decision

No contradiction, nonuniqueness theorem, or impossibility result has shown
that the four axioms must be changed. The present theorem uses supplied
Wilson-staggered model data and therefore does not derive the TOE dynamics,
but its remaining conditions are derivation/selection/continuum targets, not
an established demand for an axiom update.

**No axiom-update stop.**
