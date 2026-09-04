# Named-Site Record-Faithful Equivalence Classification

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is an exploratory operator-algebra classification,
assumptions exercise, and finite counterprotocol packet. It is not an axiom
proposal, primitive, retained theorem, physical-equivalence declaration,
record-context selection, or audit verdict. It changes no axiom, primitive,
registry, audit surface, review queue, or retained claim.

**Outcome class:** exact finite classification with a live semantic fork. The
fixed named-site theorem is exact. The physical choice between a fixed site
net, a selected-record quotient, and a transported site net is not made here.

## Framework Refresher

The current supplied foundation was read directly:

- [`MINIMAL_AXIOMS_2026-06-29.md`](../../../MINIMAL_AXIOMS_2026-06-29.md);
- [`PRIMITIVE_REGISTRY_CHECK.md`](../../../ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md);
- [`axiom_premise_nodes.json`](../../../audit/data/axiom_premise_nodes.json);
- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](../../../SCALE_REFERENCE_PRIMITIVE_NOTE.md);
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](../../../KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md);
- [`REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`](../../../REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md);
- [`derivation_obligations.json`](../../../audit/data/derivation_obligations.json);
- [`CONTROLLED_VOCABULARY.md`](../../../repo/CONTROLLED_VOCABULARY.md);
- [`audit/README.md`](../../../audit/README.md);
- [`ACTIVE_REVIEW_QUEUE.md`](../../../repo/ACTIVE_REVIEW_QUEUE.md); and
- the current exercise, review, and no-go methodology instructions.

The approved primitives are scale conversion, structural kinetic-form
isotropy, and pointwise evaluation at a supplied realized state. None defines
physical equivalence, a record subalgebra, a boundary class, an update, or a
formation trigger.

The direct parent is the
[`Cycle 20 full-abstraction note`](ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md).
Cycle 20 proved exact multi-time protocol transport, then left one seam:
whether the transported operators still belong to the *physical* category
named by the foundation.

## Result In Plain Language

There are three different answers because there are three different meanings
of “the same local record.” They must not be blended.

1. **All one-site rank-one record PVMs are admitted, and the named one-site
   `M2` net is fixed.** Then preserving local records forces preservation of
   the whole one-site algebra. On a finite patch, every such unitary is only a
   product of one-site unitaries followed by a site permutation. No entangling
   phase is in this group. In projective notation the bare factor normalizer is
   `PU(2)^n semidirect product S_n`.
2. **A dynamically selected record subalgebra is the only fixed readable
   interface.** Then the group is much larger. A diagonal entangling phase can
   fix every selected `Z` record exactly while changing the unread off-diagonal
   possibilities. `C_phi` survives in the selected-record normalizer. This is
   record-faithful only after the full named `M2` site net has been dropped
   from the fixed-object requirement.
3. **A transported site net is allowed.** Set the new site algebra to
   `A'_x = C_phi A_x C_phi^dagger` and transport records, boundaries, rules,
   and readout with it. Every factor is still abstractly `M2`; distinct factors
   still commute and together generate the full algebra. `C_phi` is an exact
   transported-net morphism. The right object is then a groupoid rather than
   one fixed-object group.

That closes the Cycle 20 algebraic seam but not the physical one. The present
axioms name physical sites and a one-site possibility domain at each site.
They do not say whether physical equivalence must preserve those embedded
one-site algebras or may transport the entire embedding.

The strongest fixed-net result is close to the proposed intuition, but with
two qualifications:

- before homogeneity/readout requirements, independent onsite `PU(2)` maps
  are allowed, not only a common onsite `PU(2)`; and
- after the exact admissibility rule, scalar content functional, and boundary
  class are fixed, the physical group is their stabilizer and can be smaller.

Thus “proper cubic maps plus common onsite `PU(2)`” is a defensible structural
maximum only when a single site-independent content dictionary is required
and the fixed rule/boundary are invariant. It is not yet the derived physical
equivalence group of the unfinished law.

For the primitive phase family the conclusion is exact:

| Physical object held fixed | `C_phi` status |
|---|---|
| Full named one-site `M2` net; all local rank-one PVMs readable | Excluded for every entangling `phi` |
| Full named net plus one selected pointer PVM | Still excluded; selecting fewer records does not erase the Qubit net |
| Selected pointer-record algebra only | Allowed; diagonal `C_phi` fixes every pointer record |
| Entire site net and record interface transported | Allowed as a local groupoid morphism |
| Only update changed; decoder and records fixed | Operationally separable, as in Cycle 19 |

No universal finite-depth no-go is claimed. The fixed-net exclusion and the
transported-net equivalence are both exact on their different domains.

## 1. The Three Objects

Take a finite set of sites `S`, with

```text
H_S = tensor_(x in S) C^2,
A_S = B(H_S),
A_x = M2 acting at x and identity elsewhere.
```

The `A_x` are the named one-site factors. They commute for distinct sites,
intersect only in the scalars, and generate `A_S`.

The classification below is for complex-linear star automorphisms implemented
by unitary finite-depth/local frames or QCAs. A conjugate-linear antiunitary
equivalence would add a separate Wigner-type component. It is not a unitary
gate circuit and is not silently included in `PU(2)`.

At one site, let

```text
R_x(all) = {rank-one projectors in A_x}.
```

For a selected pointer PVM, choose two complementary rank-one projectors
`P_x^0,P_x^1` and write

```text
D_x = span{P_x^0,P_x^1} = span{1,Z_x}.
```

The three domains are then:

| Domain | Fixed object | What a frame must preserve |
|---|---|---|
| Full named net | `{A_x}` and all `R_x(all)` | Each local factor/record maps to one local factor/record |
| Selected-record quotient | `{D_x}` only | Each selected record coordinate maps to one selected record coordinate |
| Transported-net groupoid | Isomorphism class of `{A_x,R_x}` | The frame may replace each object by its conjugate image |

The distinction is physical. A projector can be rank one *inside a transported
factor* while having support on two old tensor factors. Calling it one-site is
then an assertion about which net is physical, not a matrix-rank fact.

## 2. All-PVM Locality Forces Factor Locality

### Theorem 1 — local-record rigidity

Let `alpha` be an automorphism of a finite qubit algebra. Suppose every
rank-one projector in each `A_x` is sent to a rank-one projector belonging to
some one-site factor. Then there is one site map `pi` such that

```text
alpha(A_x) = A_(pi(x)).
```

If `alpha` is onto, `pi` is a permutation.

### Proof

At one site, two distinct rank-one projectors commute only when they are
orthogonal complements. Pick two nonorthogonal projectors `P,Q` in `A_x`.
Their images do not commute, so their images cannot live at different sites;
different one-site factors commute.

For any third rank-one projector `R` in `A_x`, choose a rank-one projector
`T` nonorthogonal to both `P` and `R`. Such a `T` always exists on the Bloch
sphere. The same noncommutation argument connects `R` to the target site of
`P`. Therefore every rank-one projector from `A_x` lands at one common site.

Rank-one projectors linearly span `M2`, so the whole factor `A_x` lands in
that site's factor. Both have dimension four, hence the image equals it.

Two distinct source factors cannot land on the same target factor. Their
images would have to commute elementwise, but the commutant of a full `M2`
inside itself is only the scalars. Onto-ness gives a permutation. QED.

This proof uses record locality, commutation, and the one-site `M2` algebra.
It does not use probability, a decoder, a clock, or a formation rate.

## 3. Exact Fixed-Factor Normalizer

### Theorem 2 — finite factor normalizer

For `n` equal qubit factors, a unitary `U` satisfies

```text
U A_x U^dagger = A_(pi(x)) for every x
```

if and only if, up to an overall phase,

```text
U = Pi_pi (tensor_x u_x),
```

where each `u_x` is a one-qubit unitary and `Pi_pi` permutes tensor factors.
Projectively, the group is

```text
PU(2)^n semidirect product S_n.
```

### Proof

Compose `U` with the inverse factor permutation, so each `A_x` is fixed as a
set. Every automorphism of `M2(C)` is inner. Choose `u_x` implementing the
restriction on `A_x`. Remove the product `tensor_x u_x` from `U`. The
remainder commutes with every `A_x`. Since the one-site factors generate the
full matrix algebra, their common commutant is scalar. Restore the factor
permutation. QED.

This is the finite matrix-algebra form of the Skolem-Noether mechanism. The
companion runner independently checks the commutant step and explicit
factor-permuting examples.

### Infinite lattice form

For the quasi-local algebra, if an automorphism maps every named one-site
factor to a named one-site factor, the same argument applies on every finite
local subalgebra. Consistency gives a site permutation and onsite factor
automorphisms. One should state this as an algebra automorphism; an infinite
tensor product need not be represented by one global Hilbert-space unitary in
every representation.

Locality and the Lattice structure further restrict the site permutation.
The graph automorphism group of the nearest-neighbor cubic lattice is

```text
Z^3 semidirect product O_h,
```

where `O_h` is the 48-element signed-coordinate group. One direct proof is
short. Translate an automorphism so it fixes zero. Among the six neighbors of
zero, opposite directions are characterized by having only zero as a common
neighbor; nonopposite directions have a second common neighbor. The map must
therefore permute the three opposite pairs and may flip each pair. It is a
signed coordinate map on the unit directions. Each coordinate ray is the
unique-geodesic continuation of its first edge, so every point on all six axes
is fixed after removing that signed map. Finally, distances to `+N e_i` and
`-N e_i`, for `N` beyond a test point, recover its `i`th coordinate from their
difference. A map fixing all axes and all distances fixes every point.

If the supplied proper
orientation is part of what the equivalence must preserve, the point group is
the 24-element proper cubic subgroup. Merely preserving adjacency, or even the
set of proper rotations under conjugation, does not remove reflections; the
morphism itself must be required to preserve orientation or to belong to the
supplied proper symmetry action. Abstract global lattice symmetries must be
separated from finite-depth circuits: a geometric relabeling need not be a
bounded-displacement gate circuit in the old coordinates.

## 4. What Content-Only Readout Does

The bare fixed-factor normalizer permits an independent `u_x` at every site.
That is more than a common onsite `PU(2)`.

Now require a single content relabeling, independent of site. The image of a
one-site content `P` must be `f(P)` at every site. For an inner map this means

```text
Ad(u_x) = f for every x,
```

so all `u_x` are the same element of `PU(2)`. Site-dependent scalar phases do
not matter.

Why this condition matters: with `u_0=1` and `u_1=H`, the same target content
`P0` pulls back to `P0` at site zero and `P+` at site one. A scalar content
functional can distinguish those two projectors. Its transported value would
then depend on the site, contrary to one site-independent dictionary.

For one actual scalar readout `I`, the exact condition can be weaker:

```text
u_y^dagger u_x belongs to Stab(I)
```

for every pair of sites, where `Stab(I)` preserves all single-record values.
The axiom does not specify `I`, so its stabilizer cannot yet be computed.

Finite additivity adds no further group restriction after the single-record
dictionary is well-defined. If

```text
I'(f(P)) = I(P),
```

then a finite disjoint record collection keeps the same sum term by term.
The maximum-one-record-per-site clause is also preserved by a site
permutation. These clauses test consistency; they do not select `f`.

## 5. Selected-Record Normalizer

The selected pointer algebra gives a different exact theorem.

### Theorem 3 — coordinate-pointer normalizer

On `n` qubits, let each `D_x=span{1,Z_x}` be a selected record coordinate.
The unitaries that permute these coordinate algebras have the form

```text
U = D_theta X^c Pi_pi,
```

up to overall phase, where:

- `D_theta` is an arbitrary diagonal unitary in the joint pointer basis;
- `X^c` independently swaps the two pointer outcomes at selected sites; and
- `Pi_pi` permutes sites.

The basis-permutation part has size

```text
2^n n!.
```

### Proof

Any unitary normalizing the full diagonal algebra is monomial: it permutes
joint basis vectors and attaches phases. Requiring each *coordinate* algebra
`D_x`, rather than only the global diagonal algebra, to land on one coordinate
means each output bit is one input bit or its complement. Distinct output
coordinates must use distinct input bits. This gives a signed coordinate
permutation, followed by arbitrary diagonal phases. QED.

This is smaller than the normalizer of the global diagonal algebra. CNOT is a
useful counterexample: it permutes computational basis states and hence
normalizes the global diagonal algebra, but sends one local `Z` coordinate to
`Z tensor Z`. It does not preserve one-record-per-site coordinate identity.

It is also larger than the full-site-net normalizer. The arbitrary diagonal
phase `D_theta` may be entangling while fixing every selected record projector.

### Exact separability diagnostic

For two sites write the diagonal phases as

```text
q_00, q_01, q_10, q_11.
```

The diagonal unitary is an onsite product exactly when

```text
q_00 q_11 = q_01 q_10.
```

For the controlled phase,

```text
(q_00,q_01,q_10,q_11)=(1,1,1,exp(i phi)),
```

so the defect is `exp(i phi)-1`. It vanishes only when the gate is
non-entangling. The runner exhausts all 256 two-qubit diagonal gates with
fourth-root phases: all 256 fix pointer records, while exactly 64 are onsite
separable.

Therefore:

> A dynamically selected record subalgebra can hide an entangling phase from
> every selected record without making that phase an automorphism of the full
> named one-site possibility net.

The conclusion is basis independent. Conjugating the whole construction by
onsite unitaries gives the same result for any selected local PVM.

## 6. Controlled Phase As The Decisive Fixture

Let

```text
C_phi = diag(1,1,1,exp(i phi)).
```

For every `phi`, it fixes each local computational record projector. For
entangling `phi`, it does not preserve all one-site projectors. In particular,

```text
C_phi (P_X+ tensor 1) C_phi^dagger
```

has support in both old tensor factors and does not belong to either old
one-site factor. Its operator-Schmidt rank is two, while an onsite product has
rank one.

This gives an exact counterprotocol when all one-site PVMs are admitted:

1. prepare neighboring `X+` fixtures, with the first treated as the record
   being tested;
2. apply the candidate active phase frame; and
3. read the same named site in the same `X` context.

For `CZ`, the conditional textbook projector overlap for returning `X+` at
the first site is `1/2`, not one. An active update therefore does not preserve
that permanent local projector in the stated instrument. The conclusion is
scoped to a fixed all-PVM record category and supplied read instrument. It does
not show that an `X` record is admitted after a pointer rule has selected only
`Z` records, and it does not derive the framework's probability rule.

## 7. Boundary Classes

Boundary preservation also depends on what is fixed.

For a coherent two-site product boundary,

```text
|++> -> C_phi |++>,
```

the one-site reduced purity is

```text
Tr(rho_1^2) = (3+cos(phi))/4.
```

It is below one for every entangling `phi`, so the class of all product
boundaries is not preserved.

Every computational-basis record boundary is fixed as a density matrix,
because the phase changes only the ket's global phase. Every diagonal mixture
is fixed too. Thus a pointer-record boundary class permits `C_phi`, while an
all-product boundary class rejects it.

If the boundary is transported with the net, it is preserved tautologically
as an isomorphic object. If the boundary is fixed empirical data, the frame
must lie in its stabilizer. The realized-state primitive supplies neither
choice.

## 8. Tick And Capacity Cost

There are again two operations that must not be blended.

- A **passive relabeling** changes the algebraic description and writes no
  record. It has the same history labels, ticks, and scalar-additive record
  cost.
- An **active implementation** that writes a phase or schedule certificate has
  an extra permanent readable event. It has a larger record count, clock
  count, and capacity debit.

The algebraic normalizer theorem cannot prove that a physical substrate
executes a frame for free. Conversely, gate entanglement alone does not prove
an extra record was written. Zero extra tick/capacity cost is a morphism
condition on the physical category.

## 9. Transported Site-Net Groupoid

For any local unitary or locality-preserving automorphism `alpha`, define

```text
A'_x = alpha(A_x),
R'_x = alpha(R_x),
D'_x = alpha(D_x).
```

Then exactly:

1. each `A'_x` is isomorphic to `M2`;
2. `A'_x` and `A'_y` commute for `x != y`;
3. the transported factors generate the same total algebra;
4. orthogonality and complementarity of transported records are preserved;
5. maximum-one-record-per-transported-site is preserved;
6. scalar additivity is preserved by `I'(alpha(P))=I(P)`; and
7. morphisms compose because conjugations compose.

This is an exact groupoid rather than one fixed-object group. Objects are
embeddings of abstract site factors and record algebras into the quasi-local
algebra. Morphisms are local automorphisms carrying one full object to another.
The isotropy group of one fixed named net is the much smaller factor
normalizer of Theorem 2.

`C_phi` is allowed in this groupoid. Its transported `X` projector is
one-site relative to `A'_x` and two-site relative to the old net. Neither
description wins by algebra alone.

The exact physical questions are therefore:

- Are lattice sites the fixed tensor-factor embedding, or only labels on an
  isomorphic local net?
- Must the transported admissibility rule remain nearest-neighbor in the
  original embedding, or only in the transported net?
- Is record cost evaluated in old support, transported support, or solely by
  permanent history labels?

Those questions are the Cycle 20 seam stated at bare metal.

## 10. The Fixed Admissibility Rule Narrows The Group

The Qubit net alone gives a structural normalizer. A physical equivalence of
one finished law must also stabilize the one fixed admissibility rule.

A relative-overlap rule illustrates the difference. If admissibility depends
on `Tr(P_x P_y)`, a common onsite `PU(2)` leaves it unchanged, while unrelated
onsite rotations can change it. The runner checks this exactly.

A basis-sensitive function has a still smaller stabilizer. It is included in
the runner only as a mathematical control, not a framework rule; the current
foundation says no possibility is privileged by the supplied algebraic
structure. The control proves a logical point: without the exact fixed rule,
one cannot compute its stabilizer from the carrier algebra alone.

Thus the groups form a descending sequence:

```text
all factor-local maps
  -> homogeneous content maps
  -> fixed-rule stabilizer
  -> fixed-readout stabilizer
  -> fixed-boundary stabilizer.
```

The final physical equivalence group is the intersection. The current exact
law is not specified, so the intersection is not yet calculable.

## 11. Exact Classification

The maximal honest classifications are:

### Fixed full site net, all PVM records

On a finite patch:

```text
G_net = PU(2)^n semidirect product S_n.
```

After preserving cubic adjacency and proper orientation:

```text
G_lattice-net subset of PU(2)^(Z^3) semidirect product
                         (Z^3 semidirect product O),
```

with `O` the proper cubic group. Requiring a common content dictionary reduces
the internal part to common onsite `PU(2)`, modulo the stabilizer of the actual
scalar readout. The fixed rule and boundary may reduce it further.

Entangling `C_phi` is excluded from the fixed full-site-net automorphism group.

### Fixed selected record coordinates only

On a finite patch:

```text
G_pointer = {local diagonal phase circuits}
            semidirect product {outcome flips and site permutations},
```

with finite-depth diagonal phase circuits supplying the local lattice form.
The full finite-dimensional group allows arbitrary diagonal phases; locality
restricts those phases to bounded-range finite-depth realizations.

`C_phi` survives in the selected-record normalizer.

### Transported full net

The maximal object is the local-automorphism/QCA groupoid, with boundary,
rule, readout, and record-cost preservation included as morphism conditions.
`C_phi` is an exact transported-net morphism.

## 12. Consequence For The Axiom Question

No verbatim axiom addition follows from this classification.

The work identifies a prior semantic cut that must be settled before formation
language can be final:

```text
fixed-site reading:
  physical equivalence preserves each named one-site possibility algebra,
  up to a supplied lattice symmetry;

transported-net reading:
  physical equivalence may transport the site algebras, record algebras,
  rule, boundary, and readout together by a local autoequivalence.
```

The first reading is close to the literal wording “each site has a domain of
local possibilities.” If that literal reading is already intended, it may be
a clarification rather than a new axiom sentence. The second reading is a
larger equivalence convention and needs an exact account of what remains a
physical site and what record cost means.

Neither reading says when a record first forms, when a later possibility
locks, which member becomes actual, or what its weight is. First-record
nucleation remains separate.

---

# Assumptions Exercise

## Exercise Zero — State The Wall

**Target.** Determine the largest local equivalence that preserves the
foundation's physical site and record meaning, and decide whether an
entangling `C_phi` phase is gauge or physical.

**Current failure.** Cycle 20 proved exact adaptive protocol transport but did
not prove closure of the physical object category. The same conjugated
projector is local in a transported net and nonlocal in the old net.

**Progress criterion.** Classify the exact fixed-net and selected-record
normalizers, give decisive `C_phi` tests, and isolate the one semantic choice
that changes the answer.

**Decisive closure.** An exact law or explicit equivalence definition must say
whether the site net is fixed or transported and must preserve the fixed rule,
boundary, permanent history, and scalar record cost.

**Demotion criterion.** If a theorem covers only a selected pointer algebra or
only finite patches, say so and keep the larger category open.

## Exercise One — Assumptions From Axioms Up

### Assumption ledger

| ID | Layer | Assumption | Explicit/Implicit | Current source/evidence | Why it is needed | What if wrong? | Failure mode opened | New attack vector | Test/artifact to check | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| Foundation-Lattice | Axiom | Physical sites are `Z^3` points with nearest-neighbor adjacency and supplied cubic symmetries. | Explicit | Minimal axioms | Names the site carrier. | A transported algebra net might replace literal site support. | Fixed-support no-go becomes representation fixing. | Compare fixed and transported nets. | Theorem 4/groupoid runner block. | High |
| Foundation-Qubit | Axiom | Every named site carries a full `M2` possibility domain. | Explicit | Minimal axioms | Supplies the factor algebra used in the normalizer proof. | Only a selected commutative record algebra may be physical. | Diagonal entangling phases become invisible. | Quotient to `D_x`. | Selected-record normalizer. | High |
| Foundation-Admissibility | Axiom | One fixed nearest-neighbor rule determines available possibilities. | Explicit | Minimal axioms | A true physical symmetry must preserve the rule. | Carrier symmetries can exceed law symmetries. | `PU(2)` candidate overstates the physical group. | Compute the eventual rule stabilizer. | Relative-overlap control now; exact-law runner later. | High |
| Foundation-Record | Axiom | One permanent record per site; content-only scalar-additive readout. | Explicit | Minimal axioms | Defines record faithfulness. | Site-specific dictionaries or distributed encodings may be allowed. | Independent onsite maps or transported records expand the category. | Test dictionary consistency and encoded records. | Runner blocks D/F. | High |
| Primitive-Scale | Primitive | One dimensionful units reference. | Explicit | Approved registry | Included for complete ledger only. | No effect here. | None. | Delete from active proof. | Dependency scan. | High |
| Primitive-Kinetic | Primitive | Structural kinetic-form isotropy only. | Explicit | Approved registry | Included for complete ledger only. | No effect here. | None. | Delete from active proof. | Dependency scan. | High |
| Primitive-State | Primitive | Pointwise evaluation at one realized state. | Explicit | Approved registry | Could supply an actual boundary state, not a boundary class. | It cannot select the class or equivalence. | Boundary invariance remains open. | Separate realized member from class. | Boundary fixtures. | High |
| Equivalence-Fixed | Definition | Physical equivalence preserves the old embedded factors `A_x`. | Implicit fork | Cycle 20 seam | Needed for the strict factor normalizer. | The net may transport. | `C_phi` becomes a valid morphism. | Build the transported groupoid. | Runner block F. | High as conditional |
| Equivalence-All-PVM | Definition | Every rank-one local PVM can be a record context. | Implicit fork | Not supplied | Makes record locality span the whole `M2`. | Dynamics may select one pointer algebra. | Full-net rigidity cannot be inferred from records alone. | Classify selected `D_x`. | Theorem 3. | High as conditional |
| Equivalence-Selected | Definition | Only one dynamically selected local PVM is fixed as readable. | Implicit fork | Formation lane candidate | Permits a smaller operational object. | Other PVMs may remain legally recordable. | Pointer quotient is too small. | Search exact selection law. | Future exact-law probe. | Medium |
| Equivalence-Transport | Definition | Site factors and records may be conjugated together. | Implicit fork | Cycle 20 steelman | Creates full adaptive equivalence. | Physical sites may be literal old factors. | Groupoid equivalence misidentifies nonlocal records. | Test axiom language against embeddings. | This note's cut gate. | Medium |
| Dictionary-Global | Readout | One content relabeling applies at every site. | Implicit | “content alone” reading | Reduces independent onsite frames to common `PU(2)`. | Actual `I` may have a large stabilizer. | Common-rotation claim is too strong. | Compute `Stab(I)` once `I` is specified. | Pullback ambiguity fixture. | Medium-high |
| Boundary-Class | Boundary | A named class, not merely one realized state, must be preserved. | Implicit | Cycle 20 seam | Distinguishes pointer and coherent boundaries. | Boundary may transport or be unique. | Product-boundary counterexample loses force. | Test several boundary classes separately. | Purity formula. | High as conditional |
| Cost-Passive | Resource | A frame is a passive relabeling with no record event. | Implicit | Cycle 20 theorem | Needed for zero extra tick/capacity. | Substrate may execute and record it. | Extra certificate makes representatives physical. | Compare direct and wrapped histories. | Runner block E. | High as conditional |
| Locality-Uniform | Regularity | Infinite-time frames have a uniform locality/range bound. | Explicit condition | Cycle 20 | Prevents growing support from being called local. | Range can grow with time. | Finite equivalence does not extend indefinitely. | Track support radius under iteration. | Phase family already bounded; general QCA future test. | High |
| Frame-Linearity | Representation | Frames are complex-linear unitary/star automorphisms. | Explicit scope here | Finite-depth/QCA task | Gives `PU(2)` rather than a Wigner extension. | Antiunitary equivalences may be admitted. | Fixed-net group gains a conjugate-linear component. | Classify antiunitary physical meaning separately. | Wigner/transpose probe if requested. | High as scope |
| Rule-Stabilizer | Dynamics | Bare-net automorphisms also preserve the one fixed rule. | Required but unsupplied | Admissibility | Converts structural group into physical group. | Rule transforms as part of the object. | Fixed-rule and transported-rule categories differ. | Build rule naturality square. | Future exact-law runner. | High |
| Record-Formation | Dynamics | A record context is available when the probe uses it. | Implicit in counterprotocol | Formation gap | Needed to call an `X` projector an actual record. | Pointer selection forbids it. | All-PVM counterprotocol is outside the legal category. | Derive or condition on record context. | Formation theorem. | High |
| Actuality | Probability/ontology | One branch is actual and weights are defined. | Not used | Open | Included to prevent accidental import. | No effect on algebraic classification. | None. | Keep separate. | N2 residual table. | High |

### Routes opened by challenging assumptions

| Route | Assumptions challenged | Why this might open the wall | Expected artifact | Risk | First test |
|---|---|---|---|---|---|
| Fixed all-PVM net | Equivalence-Fixed, Equivalence-All-PVM | Gives a rigid exact group and excludes entanglers. | Factor-normalizer theorem | May exceed legal record contexts | Noncommutation/span proof |
| Selected pointer quotient | Equivalence-All-PVM | Lets diagonal phases be operationally inert. | Coordinate-MASA normalizer | Drops full Qubit net from fixed object | Exhaust monomial permutations |
| Transported net | Equivalence-Fixed | Makes Cycle 20 transport an exact physical candidate. | Local-net groupoid | Can turn locality into a relabeling choice | Verify factor relations after conjugation |
| Readout stabilizer | Dictionary-Global | May permit more than common rotations without site-dependent values. | `Stab(I)` theorem | `I` is not specified | Pullback ambiguity fixture |
| Fixed-rule naturality | Rule-Stabilizer | Could select the final subgroup scientifically. | Exact-law stabilizer theorem | Exact law still missing | Relative-overlap toy control |
| Boundary discrimination | Boundary-Class | Empirical boundary may select a representative. | Boundary stabilizer | One realized state is not a class | `|++>` and pointer controls |
| Active-cost discrimination | Cost-Passive | Record overhead may make frames physical. | Direct/wrapper counterprotocol | Active execution is not established | Transcript-length check |

## Exercise Two — Elon-Style First-Principles Reduction

The exact requirement was initially too broad: “preserve all science.” It
reduces to five concrete predicates:

```text
site factor,
record coordinate,
content dictionary,
boundary class,
record-event cost.
```

Delete probability, time rate, gravity, mass formulas, and first-record
nucleation from this classification. None is needed to decide whether a frame
maps one local algebra to another.

The smallest object retaining the issue is two qubits and one controlled
phase. The three answers already appear there:

- `P_X+ tensor 1` exposes full-net spreading;
- `P_Z+ tensor 1` exposes pointer preservation; and
- `C_phi A_1 C_phi^dagger` exposes transported-net locality.

The problem decomposes into two independent dials:

1. **object dial:** fixed net versus transported net;
2. **record dial:** all local PVMs versus one selected PVM.

The fastest falsifiers are a commutator/support test, a diagonal phase
rectangle defect, and one reduced-state purity. They replace broad simulation
prose with exact two-site checks.

The irreducible missing input is not another matrix identity. It is the
physical identity criterion for a site and record under representation change.

## Exercise Three — Literature Proof Search

External sources supply proof patterns only. The repo-native proofs above and
the runner remain the artifact support.

| Source | Problem it solves | Premises | Proof skeleton | What maps here | What does not map | Runner/proof translation | Import risk | Citation |
|---|---|---|---|---|---|---|---|---|
| Marcus and Moyls, *Transformations on tensor product spaces* (1959) | Linear maps preserving decomposable/rank-one tensors | Finite vector spaces, characteristic zero | Rank-one preservers factor, with factor swap when dimensions match | Product-plus-permutation shape | It concerns vector tensors, not permanent record algebras | Replace tensor-rank preservation by local-factor/projector preservation | Low as precedent; not framework authority | [Primary paper](https://msp.org/pjm/1959/9-4/pjm-v9-n4-p17-p.pdf) |
| Brešar, Hanselka, Klep, Volčič, *Skolem-Noether algebras* | Inner extension and tensor-product automorphisms | Central simple/finite-dimensional algebras | Restrict automorphism to a matrix factor, remove an inner map, use the commutant | Theorem 2 proof | Does not choose physical factors or record contexts | Explicit `M2` commutant calculation | Low | [Primary paper](https://arxiv.org/abs/1706.08976) |
| Liendo and Lucchini Arteche, *Automorphisms of products of toric varieties* | Automorphisms of product objects | Complete toric varieties | Product automorphisms plus permutations of isomorphic components | Independent confirmation of product-factor rigidity pattern | Projective/toric geometry is not the operator algebra | Use only as a cross-sector analogy | Medium if overread | [Primary paper](https://arxiv.org/abs/2101.03600) |
| Schumacher and Werner, *Reversible quantum cellular automata* | Strictly local translation-invariant automorphisms | Infinite quantum lattice, finite propagation | Define QCA as local algebra automorphisms and derive structure/reversibility | Transported-net/QCA object and uniform locality | Does not define this framework's physical record category | State the groupoid in quasi-local algebra language | Low | [Primary paper](https://arxiv.org/abs/quant-ph/0405174) |

No paper decides whether the framework's literal physical site is the old
tensor factor or an object transported by a QCA. That is the framework-local
semantic cut.

## Exercise Four — Mathematics Sector Search

| Sector | Reframe | Candidate theorem/tool | Minimal toy example | How it attacks the wall | What would falsify it | First artifact |
|---|---|---|---|---|---|---|
| Finite groups/representation theory | Equivalence as a normalizer group | Semidirect products and stabilizers | Two/three qubits | Classifies permutation, flips, and onsite rotations | An entangling unitary preserving every factor | Theorem 2 + enumeration |
| Operator algebras/C-star algebras | Sites as commuting matrix factors | Skolem-Noether and commutants | `M2 tensor M2` | Proves factor normalizer exactly | Non-inner one-factor automorphism in finite `M2` | Symbolic commutant solve |
| Category theory | Frames as morphisms between embedded nets | Groupoid, naturality, isotropy | Old and conjugated two-site nets | Separates fixed-object symmetry from object transport | Composition or inverse fails a physical structure | Runner block F |
| Algebraic topology/K-theory/index theory | Local automorphisms may have components not finite-depth | QCA index/component invariants | Shift versus onsite circuit | Warns that “local” and “finite-depth” differ | All relevant frames lie in one circuit component | Later QCA component probe |
| Spectral graph theory/combinatorics | Site maps as cubic graph automorphisms | Cartesian-product graph automorphisms | Six nearest neighbors of one point | Restricts `S_n` to lattice maps | A nonlinear adjacency-preserving bijection exists | Signed-coordinate enumeration |
| Convexity/optimization/SDP | Approximate record faithfulness | Distance to factor algebra/commutant | Noisy controlled phase | Extends exact theorem to robust errors | Small record error with large factor spreading | Future commutator-norm SDP |
| Probability/information theory | Difference as distinguishable transcript | Channel discrimination | Fixed Bell/X decoder | Turns category failure into a record statistic | All legal transcripts agree | Cycle 19 decoder reuse |
| Dynamical systems/stability | Uniform equivalence over time | Bounded support under iteration | Repeated `C_phi` | Distinguishes finite-horizon from indefinite equivalence | Frame range grows without bound | Support-radius recurrence |
| PDE/functional analysis | Infinite net as an inductive-limit algebra | Quasi-local automorphisms | Increasing finite boxes | Makes the finite proof consistent on `Z^3` | Finite restrictions do not glue | Local-algebra consistency proof |
| Number theory/arithmetic | Discrete phase grids as exact exhaustions | Root-of-unity phase tables | Fourth roots on two qubits | Gives finite sanity counts | Discrete count is mistaken for a phase selector | 256/64 runner check |
| Logic/model theory/proof theory | Fork as non-equivalent models of “local” | Relative interpretation/independence | Fixed net and transported net | Shows why algebra alone cannot pick semantics | Axiom wording entails one embedding uniquely | Language entailment review |
| Algebraic geometry | Product pure states as a Segre variety | Automorphisms of product/Segre objects | `P1 x P1` | Product-state preservation also forces local maps plus swaps | An entangler preserves the full product variety | Product-boundary test |

## Exercise Five — Reframing

| Reframe | What moves | What becomes simpler | What becomes harder | New route opened | First decisive test |
|---|---|---|---|---|---|
| Record locality to factor locality | Admit all rank-one PVMs | Full `M2` follows from projector span | Must justify all contexts are legal | Exact fixed-net group | Noncommutation graph |
| Full net to selected pointer algebra | Fix only `D_x` | Pointer permanence and cost are simple | Unread `M2` structure can change | Diagonal phase gauge | Rectangle defect |
| Symmetry group to groupoid | Transport objects | Cycle 20 functor becomes exact | Physical site identity must be redefined | QCA equivalence category | Conjugated factor relations |
| Common rotation to readout stabilizer | Fix actual `I` | Avoids unnecessarily strong homogeneity | `I` is presently unspecified | Larger honest fixed-net group | Compute `Stab(I)` |
| Boundary state to boundary class | Preserve a set, not one member | Clear invariant criterion | Realized-state primitive gives only one member | Boundary selection by science | Coherent vs pointer classes |
| Gate cost to record-event cost | Count only permanent writes | Matches Record axiom | Passive/active distinction must be physical | Zero-cost morphism criterion | Direct/wrapper histories |

## Route Portfolio

| Rank | Route | Source exercise(s) | Premise challenged | Expected status if successful | First artifact | Stop condition |
|---|---|---|---|---|---|---|
| 1 | Derive exact fixed-rule net stabilizer | One, Two, Four | Rule-Stabilizer | Physical equivalence subgroup | Rule naturality runner | Exact rule still absent |
| 2 | Decide fixed versus transported site ontology from axiom language | Zero, Five | Equivalence-Fixed/Transport | Semantic closure or exact ambiguity | Constitutional language review | Wording entails neither |
| 3 | Derive pointer selection before quotienting records | One, Four | Equivalence-All-PVM/Selected | Legal selected-record category | Formation/context theorem | Selection remains imported |
| 4 | Build robust approximate normalizer theorem | Four | Exact locality | Noise-stable experimental discriminator | Commutator-distance SDP | Exact lane is sufficient for axiom cut |
| 5 | Classify boundary/readout stabilizers | One, Five | Boundary-Class, Dictionary-Global | Smaller physical group | `Stab(B,I)` computation | `B` or `I` unspecified |
| 6 | Extend groupoid to nontrivial QCA components | Three, Four | Finite-depth restriction | Full local-equivalence category | Index/component note | No effect on current `C_phi` |

Assumptions most likely to be wrong: that all rank-one PVMs are legal records,
and that passive representation transport is physically free.

Assumptions most expensive to be wrong: fixed versus transported site identity,
because it flips the status of every entangling representative change.

Worth a later physics-loop: the exact fixed-rule stabilizer after the law is
specified, and a derived pointer-selection theorem if one exists.

Worth the opportunity ledger: robust approximate factor normalizers and the
transported-net QCA component classification.

What not to do next: write formation language that silently chooses one of
these categories; call all finite-depth circuits gauge; or use pointer-only
invisibility to erase the named full `M2` site net.

---

# Exact Clauses And Remaining Work

| ID | Exact clause | Scope |
|---|---|---|
| Derived-1 | All one-site rank-one record locality forces one-site factor locality. | Finite factors; quasi-local extension by compatible finite restrictions. |
| Derived-2 | The fixed factor normalizer is onsite projective unitaries semidirect site permutations. | Full named net. |
| Derived-3 | Cubic adjacency restricts site maps to translations and signed coordinate permutations; proper orientation leaves 24 point maps. | Lattice automorphisms. |
| Derived-4 | A universal site-independent content dictionary reduces onsite fields to a common projective map. | Stronger than additivity alone. |
| Derived-5 | The selected-coordinate record normalizer is diagonal phases times outcome flips and site permutations. | Pointer algebra only. |
| Derived-6 | Entangling controlled phases are selected-record faithful but not fixed-full-net faithful. | Exact two-site result. |
| Derived-7 | Transporting the entire factor/record net gives an exact local groupoid morphism. | Physical only if the category admits transported nets. |
| Derived-8 | Product and pointer boundary classes have different stabilizers. | Exact finite fixtures. |
| Derived-9 | Passive transport preserves record-event costs; an active readable wrapper does not. | History-defined cost. |

Collapsed remaining fields:

```text
E  = select and prove the full physical category, including fixed/transported
     site identity, legal records, rule, boundary, and cost preservation;
O0 = first-record nucleation/domain;
O1 = later formation-trigger domain;
A  = actual-member and weight semantics.
```

Record normalizer, boundary, and cost are subconditions of physical-category
closure, not independent axiom walls.

---

# No-Go Discipline Gate

The negative statement being shipped is narrow: an entangling `C_phi` is not
an automorphism of the *fixed full named one-site net*. No claim is made that
it cannot be a selected-record symmetry or transported-net equivalence.

### N1 — Alternative Route Enumeration

1. **ATTEMPTED — all-PVM route.** Use noncommutation and rank-one projector
   span to force a single target factor; this closes exactly and excludes an
   entangling phase from the fixed full net.
2. **ATTEMPTED — selected-record route.** Restrict records to one pointer PVM;
   the diagonal phase then survives, so a universal record-level exclusion
   fails.
3. **ATTEMPTED — transported-net route.** Conjugate factors and records
   together; all algebraic relations survive, so a universal local-net
   exclusion fails.
4. **ATTEMPTED — product-boundary route.** A coherent `|++>` boundary detects
   entanglement through reduced purity, but a pointer boundary is fixed.
5. **ATTEMPTED — additive-cost route.** Passive transport preserves history
   cost, while a readable active wrapper adds one record; cost depends on the
   morphism definition.
6. **ATTEMPTED — content-dictionary route.** Independent onsite maps are
   reduced to a common map only under a universal site-independent dictionary;
   a fixed readout stabilizer may permit more.
7. **ATTEMPTED — lattice route.** Cubic adjacency reduces arbitrary site
   permutations to affine signed-coordinate maps but does not by itself
   reject internal entangling net transport.
8. **ATTEMPTED — fixed-rule route.** A relative-overlap control rejects
   independent onsite frames while preserving common rotations; the unknown
   exact rule prevents a final physical stabilizer.
9. **ATTEMPTED — encoded-record route.** Treat the conjugated two-site
   projector as one record in a transported factor; this is algebraically
   consistent and keeps the semantic fork open.
10. **ATTEMPTED — antiunitary route.** Conjugate-linear Wigner symmetries can
    enlarge projector equivalence, but they are outside the stated
    complex-linear finite-depth/unitary-frame domain; the note does not claim
    to exclude them from a broader equivalence definition.

At least five distinct routes were tested. The broad no-go is rejected; only
the fixed-full-net statement is kept.

### N2 — Wall-Independence Audit

Use the collapsed fields `E,O0,O1,A` above.

| Pair | Does first close second? | Does second close first? | Independent? |
|---|---|---|---|
| `E,O0` | No | No | Yes |
| `E,O1` | No | No | Yes |
| `E,A` | No | No | Yes |
| `O0,O1` | No; first occurrence does not give later trigger truth | No | Yes |
| `O0,A` | No | No | Yes |
| `O1,A` | No | No | Yes |

Within `E`, record algebra, boundary preservation, fixed-rule naturality, and
zero-extra-record cost are subconditions of physical-category closure. They
are not counted as four independent walls.

### N3 — Hidden-Wall Scan

| Quoted search phrase | N3 scan classification |
|---|---|
| “we assume” | N3 scan: absent outside this quoted search phrase. |
| “by construction” | N3 scan: absent outside this quoted search phrase. |
| “as is standard” | N3 scan: absent outside this quoted search phrase. |
| “the framework provides” | N3 scan: absent outside this quoted search phrase. |
| “bridge context” | N3 scan: absent outside this quoted search phrase. |
| “background” | N3 scan: absent outside this quoted search phrase. |
| “naturally” | N3 scan: absent outside this quoted search phrase. |
| “obviously” | N3 scan: absent outside this quoted search phrase. |
| “standard QFT” | N3 scan: absent outside this quoted search phrase. |
| “registered” | N3 scan: registry descriptions are foundation provenance, not a scientific step. |
| “canonical” | N3 scan: absent outside this quoted search phrase. |

The load-bearing conditions are explicit in the three object definitions.

### N4 — Residual Matching

| Witness | Witness residual | Present residual | Match? |
|---|---|---|---|
| [Cycle 20 full-abstraction note](ADAPTIVE_RECORD_PROTOCOL_QCA_FULL_ABSTRACTION_THEOREM_NOTE_2026-07-14.md), lines 43-108 | Physical closure of transported records/boundaries/costs | `E`, the physical category | Yes |
| [Cycle 19 protocol-equivalence note](PRIMITIVE_QCA_RECORD_PROTOCOL_FULL_EQUIVALENCE_STEELMAN_NOTE_2026-07-14.md), lines 60-137 and 243-273 | Fixed protocol separates update-only representative changes | Fixed-net `C_phi` counterprotocol | Yes |
| [Minimal axioms](../../../MINIMAL_AXIOMS_2026-06-29.md), lines 63-71 and 163-168 | Formation trigger, weights, and rate are unsupplied | `O0/O1/A` | Yes, but not evidence for `E` |
| [Primitive registry](../../../audit/data/axiom_premise_nodes.json), lines 1-47 | Approved primitives do not select equivalence/boundary | Foundation inventory only | Yes as inventory, not a no-go proof |

No mass, gravity, or probability no-go is cited as evidence for the operator
normalizer result.

### N5 — Resolution And Rhetoric Audit

Tested resolutions:

- per projector: all rank-one PVM connectivity and selected `Z/X` fixtures;
- per site factor: exact `M2` span and commutant;
- per two-site block: controlled phase, CNOT, boundary purity, phase defect;
- finite patch: normalizer theorem and exhaustive two/three-bit coordinate
  permutations;
- lattice point group: all 48 signed coordinate maps and 24 proper maps;
- infinite quasi-local net: proof by consistent finite restrictions;
- conjugate-linear/antiunitary equivalence: named but outside the unitary-frame
  scope;
- all QCA components and approximate records: not classified.

Allowed wording is “fixed full named-net exclusion” and “selected/transported
routes remain.” Disallowed wording is “entangling frames are never gauge” or
“all local records force a common onsite rotation” without the content
dictionary condition.

### N6 — Partial-Closure Paths And Primitive Registry

1. If the literal axiom meaning fixes embedded site factors, Theorems 1-2
   close the entangling-frame question without a new axiom.
2. If physical equivalence is defined as transported-net isomorphism, Cycle 20
   and Theorem 4 close finite protocol equivalence without new physics, but the
   equivalence convention must be explicit.
3. If dynamics derives a pointer algebra, Theorem 3 supplies its exact
   record-only normalizer; an import can remain verbatim in a bounded theorem
   until a pointer-selection derivation retires it.
4. Once the exact rule and scalar readout exist, compute their stabilizer rather
   than adding a symmetry premise.
5. A boundary supplied as physical data can select a subgroup without becoming
   an axiom.
6. Approved scale, kinetic, and realized-state primitives do not close `E` and
   are not counted as walls.

The result does not say “new axiom required.” Clarification, definition, or a
later exact-law theorem may close the seam.

### N7 — Strongest Surviving Steelman

A hostile reviewer can reject the fixed-support criterion as a coordinate
artifact. The Qubit axiom may name an abstract `M2` fiber at every lattice
label, not one immutable tensor embedding. Under a local automorphism the
conjugated factors still form pairwise commuting `M2` fibers, have one record
slot each, generate the same quasi-local algebra, and preserve every
transported adaptive statistic. Demanding that `C_phi A_x C_phi^dagger` equal
the old `A_x` would then be like demanding a coordinate transformation leave
coordinate components unchanged. The proper physical object is the net plus
all structure, and Cycle 20 supplies its natural history transport.

This argument is convincing. The transported-net steelman remains live. To
win, it must also show that the transported nearest-neighbor rule, physical
site identity, fixed boundary data, and additive record cost satisfy the
literal foundation without redefining them after seeing the frame. Therefore
the broad no-go is premature and is not shipped.

### N8 — Cross-Cycle Echo

1. Cycle 19 showed that one fixed decoder distinguishes update-only phase
   representatives. This cycle identifies that result as a fixed-object test.
2. Cycle 20 transported every adaptive operation and exposed object-category
   closure. This cycle proves the exact fixed-object isotropy group and the
   larger transported-object groupoid.
3. Earlier readable-wrapper probes found extra certificate records. This cycle
   locates that as active implementation cost, not an automatic property of a
   passive frame.
4. Formation cycles separated global occurrence from first nucleation and
   later triggers. This equivalence classification leaves that separation
   unchanged.
5. Prior premise cleanups retired apparent walls by reclassification. The same
   possibility is preserved here: an explicit equivalence definition may
   close `E` without new physics.

**No-Go Discipline status:** PASS for the narrow fixed-full-net exclusion;
the universal claim is explicitly demoted and not made.

## Companion Runner

Run:

```bash
python3 scripts/named_site_record_faithful_equivalence_classification_probe_2026_07_14.py
```

It checks the cardinal-PVM span/noncommutation graph, the `M2` commutant,
product-permutation factor maps, controlled-phase support and operator-Schmidt
rank, exhaustive coordinate-pointer permutation counts, fourth-root phase
separability counts, cubic point groups, content-dictionary ambiguity,
additivity, boundary purity, active/passive record costs, transported-factor
relations and composition, rule-stabilizer controls, N1-N8 visibility, and
local links.
