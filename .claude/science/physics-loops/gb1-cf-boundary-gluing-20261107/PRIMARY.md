# Finite subdivision and boundary gluing: primary derivation

Status: exact conditional author derivation completed. No independent-check
or audit status.

Sources: raw model and question in this folder's `PRIMARY_SPEC.md` and
`GOAL.md`; prior finite-patch note
`docs/SU2_FIVE_STATE_TWO_PLAQUETTE_GAUGE_SECTOR_BOUNDED_THEOREM_NOTE_2026-11-07.md`
at parent head `ba7790560e50afe712a68d42f550493e980cb19c`; unchanged main
`f5af11cd0102cfd0b51aef0911f600130bf5beb1` for
`docs/MINIMAL_AXIOMS_2026-06-29.md` and
`docs/audit/data/axiom_premise_nodes.json`. Applicable workflow and workhorse
instructions were reused after verifying no change from the prior source.
The model and effort remain inherited. No new checker artifacts were read.

## Result and current checkpoint

The pullback `D f(g1,g2)=f(g2 g1)` maps the five-state space isometrically
onto the entire internal-Gauss singlet space of two five-state links. The
unprojected identities

```
(U2 U1)D = D U,      (U2 U1)^dagger D = D U^dagger
```

hold, including zero leakage out of the image. Subdivision is coassociative.
Each fine-edge `E^2` equals the coarse `E^2` on this image; their unweighted
sum equals twice the coarse operator, not once. A second subdivision gives
the corresponding three-link results. These statements are proved below,
not inferred from a projected agreement alone.

For edge-disjoint regions, retaining boundary group representations gives
an exact reconstruction by the diagonal boundary-group invariant space.
At a vertex still met by a third region, prematurely projecting the first
two regions to their singlet can discard valid global singlets. An exact
four-spin example below loses one of its two invariant channels under that
premature projection. Observable consistency does not make separately
ordered overlapping patch gates agree.

The standard-library certificate completed in 0.07446 seconds with peak RSS
25,083,904 bytes, after numeric preflight and under lease
`gb1cf-boundary-primary-20261107-run01`, which was released. It uses
`AUDIT_TIMEOUT_SEC=80`, a 290 MB RSS stop, and all four requested math-library
thread settings equal to one. No failed numeric execution occurred. Its
source hash was
`6a7bb048154dcd6e8dd9008bed574c53085f88ca9ff40037db18dd3e4d3625b3`.
The mathematical computation reads no mutable workflow, spec, goal, or other
runner. Only elapsed-time/resource diagnostics use floating-point values.

Completed author obligations: explicit cut and metric; complete internal
image; endpoint and multiplication intertwiners including adjoints;
coassociativity; electric accounting; normalized boundary reconstruction;
the three-region grouping witness; and mutation rejection. The supervisor
owns the next independent comparison and any integration. No checker output
has been consulted, and no four-plaquette sector count is claimed here.

## 1. Sources and route choice

The raw five-state Haar model is supplied construction data. The prior
two-square note supplies only the previously derived endpoint convention and
the already scoped noncommuting-patch example; every new cut/glue identity is
derived here from the raw model. No new physical premise is adopted.

A targeted primary-source literature search used the queries
`site:arxiv.org Donnelly entanglement entropy nonabelian gauge symmetry edge
subdivision Hilbert space 2014` and
`site:arxiv.org Donnelly decomposition entanglement entropy lattice gauge
theory boundary representations`. The relevant accessible sources were:

- William Donnelly, [Decomposition of entanglement entropy in lattice gauge
  theory](https://arxiv.org/pdf/1109.0036), v2 (26 April 2012), section II,
  equations (8)–(14) and (18)–(20): multiplication pullbacks, normalized
  boundary-index contraction, and boundary representation multiplicities.
- William Donnelly, [Entanglement entropy and nonabelian gauge
  symmetry](https://arxiv.org/pdf/1406.7304), v1 (27 June 2014), section 1.2,
  equations (10)–(13): normalized representation matrix elements and the
  `dim(R)^(-1/2)` subdivision coefficient.

Credit for this established boundary-representation construction belongs to
that literature and its predecessors; no novelty claim is made. The needed
special cases are re-derived below, and the compressed five-state operator
and electric-accounting identities receive explicit finite checks. No entropy,
continuum, or physical-identification claim from those papers is used. The
extracted 2012 equations (10) and (11) display opposite multiplication orders;
this apparent convention/typographical issue is not relied on. The raw task
fixes `g2 g1`, and both the derivation and certificate retain that order.

The chosen route is the multiplication pullback with the full boundary
representation retained. It directly tests finite closure and gives exact
local tensor coefficients. A nonzero leakage or failed metric would have
refuted it. The tested unweighted-electric and premature-singlet variants
instead give the explicit residuals recorded below.

## 2. The finite subdivision matrix and its metric

Let `e_4=I_2`, `e_j=i sigma_j`, and `g=sum_mu x_mu e_mu`. The orthonormal
link basis is `b_0(g)=1`, `b_mu(g)=2x_mu` for `mu=1,...,4` under normalized
SU(2) Haar measure. Orthogonality follows from
`int x_mu=0`, `int x_mu x_nu=delta_mu,nu/4`.
For a subdivision `x -> z -> y`, write the ordered fine tensor basis as
`|a,b>` with `a` on the first link `g1` and `b` on the second link `g2`.
Define `D f(g1,g2)=f(g2 g1)`.

The quaternion multiplication rule is
`e_i e_j=-delta_ij e_4-epsilon_ijk e_k` and `e_4 e_mu=e_mu e_4=e_mu`.
Expanding `2x_mu(g2 g1)` in the normalized tensor basis gives the complete
`25 × 5` matrix through its five sparse columns:

```
D|0> = |0,0>,
D|1> = (|1,4>+|4,1>+|2,3>-|3,2>)/2,
D|2> = (|2,4>+|4,2>+|3,1>-|1,3>)/2,
D|3> = (|3,4>+|4,3>+|1,2>-|2,1>)/2,
D|4> = (|4,4>-|1,1>-|2,2>-|3,3>)/2.
```

There are four unit-magnitude terms before the factor `1/2` in every
nonconstant column, and different columns have disjoint supports. Therefore
`D^dagger D=I_5`. Equivalently, Haar right invariance for each fixed `g1`
gives

```
int dg1 dg2 |f(g2 g1)|^2 = int dg |f(g)|^2.
```

The displayed finite closure is essential: the pullback of every member of
this `R` lies in `R tensor R`. The matrix is an isometry into a
25-dimensional space, not an isomorphism onto that whole space. Its image
projector is `Pi_D=D D^dagger`.

Writing `e_b e_a=sum_mu c^mu_ba e_mu`, the coefficients obey
`sum_ab c^mu_ba c^nu_ba=4 delta_mu,nu`. The nonconstant columns are
`D|mu>=(1/2)sum_ab c^mu_ba |a,b>`. This identity is also a convenient
finite certificate for the normalization.

## 3. Internal Gauss condition and exact image completeness

The link endpoint generators are fixed directly from the raw matrices:

```
L_mu,nu=-i(|mu><nu|-|nu><mu|),
J_1=L_23, J_2=L_31, J_3=L_12, K_a=L_a4,
N+_a=(J_a+K_a)/2,    N-_a=(J_a-K_a)/2.
```

The observable convention is
`[N+_a,U]=-sigma_a U/2`, `[N-_a,U]=U sigma_a/2`.
Thus the internal generator at `z` is
`G_z,a=N+_(first),a+N-_(second),a`.
At the level of group variables, the internal gauge transformation is
`(g1,g2) -> (h g1,g2 h^(-1))`, which leaves `g2 g1` unchanged. Its
pullback or inverse pullback therefore fixes `D f`. Explicitly,

```
G_z,a D = 0,
N-_(first),a D = D N-_a,
N+_(second),a D = D N+_a.
```

In particular, no endpoint singlet condition at `x` or `y` is imposed by
the subdivision. Nontrivial coarse boundary flux remains represented.

To show that the image is the *whole* internal invariant space, decompose
each link as `(0,0) + (1/2,1/2)` under its endpoints. Mixed occupancies
`(0,1/2)` and `(1/2,0)` carry one internal doublet and contain no singlet.
The empty/empty sector has one invariant. The occupied/occupied sector has
one singlet between the two internal doublets and leaves the two external
doublets free, giving dimension four. Hence

```
Inv_SU(2)_z(R_first tensor R_second) = image(D),    dimension 1+4=5.
```

This also follows by expanding the product of the two endpoint doublets
into its one-dimensional antisymmetric and three-dimensional symmetric
parts; a dual doublet at an oriented end is identified by the SU(2) invariant
epsilon tensor. The mixed incoming/outgoing contraction can equivalently be
written as a delta between a representation and its dual.

The runner applies all three internal generators to all five columns and
checks the two external endpoint identities on full sparse vectors. It also
forms the sparse stacked internal-generator map on all 25 fine basis states:
its exact rational rank is 20, so the nullity is five. Invariance and the
isometric five-dimensional image therefore establish full image completeness
without relying on a projected operator test.

## 4. Compressed link multiplication intertwines without leakage

Let `U_c` denote the coarse color/link matrix and let
`V=U2 U1` on the two fine links. The formula `P_mu=Q_mu/2`, with
`Q_mu=|mu><0|+|0><mu|`, gives the following color-matrix-valued actions:

```
V D|0> = (1/4)sum_ab (e_b e_a)|a,b>
        = (1/2)sum_mu e_mu D|mu> = D U_c|0>,

V D|mu> = (1/8)sum_ab c^mu_ba (e_b e_a)|0,0>
         = (e_mu/2)|0,0> = D U_c|mu>.
```

The second line uses the coefficient orthogonality from section 2. Replacing
`e_b e_a` by its adjoint `e_a^dagger e_b^dagger` proves the same identity
for `V^dagger` and `U_c^dagger`. Therefore, with the identity on color
understood,

```
V D = D U_c,             V^dagger D = D U_c^dagger,
(I-Pi_D) V D = 0,        (I-Pi_D) V^dagger D = 0.
```

These are unprojected identities. The image is reducing for each color
matrix entry and its adjoint. Compression `D^dagger V D=U_c` follows, but
is not being used as a substitute for invariance. The proof relies on the
specific finite representation and normalization; it does not assume `U`
itself is unitary or a classical group element.

The certificate evaluates both identities and both leakage residuals on all
ten color/coarse-link basis inputs, retaining every fine output component.
A wrong-order mutation replacing `U2 U1` by `U1 U2` is rejected: on color
zero and the coarse empty state, its full intertwining residual has squared
norm `3/2`, and its component outside `image(D)` has squared norm `3/4`.
This demonstrates that the image test can detect the relevant defect.

## 5. Second subdivision and finite-chain consistency

The two three-link pullbacks satisfy

```
(D tensor I)D = (I tensor D)D = D_3,
D_3 f(g1,g2,g3)=f(g3 g2 g1).
```

This follows from associativity of quaternion/matrix multiplication; it
also follows by expanding each column of section 2. Each occupied coarse
column has 16 nonzero coefficients `+/-1/4`, while the empty column is
`|0,0,0>`. Its metric is again the identity. The two internal Gauss
constraints require matching occupied representations along the chain.
There are only the all-empty and all-occupied sectors, with external
dimensions one and four. Thus `image(D_3)` is their full joint kernel.
The exact stacked-generator rank on the 125-state fine space is 120.

Repeated use of the unprojected two-link identity gives

```
(U3 U2 U1)D_3 = D_3 U_c,
(U3 U2 U1)^dagger D_3 = D_3 U_c^dagger.
```

The runner checks both compositions of `D`, all internal Gauss actions,
and both chain-operator identities. More generally the same induction
proves the finite-chain statement for every positive number `n` of
subedges: the map `D_n f=f(gn...g1)` is isometric and has the five-dimensional
joint internal-singlet image, and the chain and its adjoint intertwine `U_c`
without leakage. The all-`n` assertion is this induction proof; the runner
explicitly checks `n=2,3`, not an infinite enumeration.

Tensor products of these maps on different coarse edges give the analogous
finite graph refinement. Different-edge subdivisions commute, and repeated
subdivision of one edge is coassociative. The original vertex representations
are intertwined, and only the new subdivision vertices acquire internal
singlet constraints. Hence a fixed choice of original-vertex Gauss constraints
is preserved, including descriptions that retain original boundary flux.

## 6. Electric accounting is not an unweighted extensive identity

Write `E_c^2=(3/4)Q_c`, with `Q_c` the coarse occupied projector. Both
fine links are occupied on `D|mu>` and empty on `D|0>`. Consequently

```
E_1^2 D = D E_c^2,       E_2^2 D = D E_c^2,
(E_1^2-E_2^2)D=0,       (E_1^2+E_2^2)D=2 D E_c^2.
```

Each fine Casimir preserves the image. A weighted electric term
`a E_1^2+b E_2^2` intertwines `c E_c^2` precisely when `a+b=c`, apart
from the trivial restriction to the empty state alone. For the unit coarse
coefficient, the symmetric choice is `a=b=1/2`; the equality of weights
is a declared choice, not an additional consequence of the axioms.

For `n` subedges, every `E_i^2 D_n=D_n E_c^2`, and
`sum_i E_i^2 D_n=n D_n E_c^2`. The runner obtains the total diagonal
`(0,3/2,3/2,3/2,3/2)` for two links and
`(0,9/4,9/4,9/4,9/4)` for three links. In finite-angle form,

```
[product_i exp(-i tau_i E_i^2)] D_n
    = D_n exp[-i (sum_i tau_i) E_c^2].
```

Thus retaining a prescribed coarse electric angle requires that the fine
angles sum to it. Using that same angle on every fine subedge instead
multiplies it by `n`. The unweighted two-edge accounting mutation is
rejected with squared residual norm `9/16` on any unit occupied coarse
column. No physical length scaling, clock, or coupling selection is inferred.

## 7. Edge-disjoint regions and the exact boundary reconstruction

Let a finite oriented graph have edge partition `E=disjoint_union_r E_r`.
There is one five-state factor for each physical edge. Let `I_r` be the
vertices whose complete nonempty incident-edge set belongs to region `r`;
let `B` be the vertices incident to more than one region. Isolated vertices
act trivially and cause no exception. Define

```
H_r = tensor_(e in E_r) R_e,
K_r = Inv_(product_(v in I_r) SU(2)_v) H_r,
K_boundary = product_(v in B) SU(2)_v.
```

Each `K_r` retains the action of every boundary vertex that it meets.
The kinematical tensor-factor regrouping is a unitary identification
`H_graph = tensor_r H_r`, because edge sets are disjoint. Under that
identification, the exact global singlet space is

```
H_graph^singlet = Inv_(K_boundary)(tensor_r K_r).
```

This theorem concerns the declared all-vertex singlet space of the complete
graph. It does not set each regional boundary charge to zero before gluing.
If a larger construction still regards some graph vertices as external,
leave their group action unprojected as well; the same reasoning reconstructs
the corresponding boundary-carrying space rather than a closed singlet space.

**Proof.** At a boundary vertex `v`, the global gauge representation on the
regrouped space is `tensor_r T_r,v(h)`, with trivial factors for regions
not meeting `v`. Its invariant projector is

```
P_v = int_SU(2) dh tensor_r T_r,v(h).
```

Normalized Haar invariance makes `P_v` self-adjoint and idempotent, and its
range is exactly the invariant vectors: invariants are fixed by the average,
while left multiplication leaves the averaged vector fixed. Different-vertex
group actions commute, including at opposite ends of a shared edge. Interior
projectors act in the appropriate region and commute with every boundary
action. Therefore the full Gauss projector is

```
P_graph = [product_(v in B) P_v] [tensor_r P_(I_r)],
```

whose range is the displayed reconstruction. All factors are orthogonal
projectors; there is no quotient metric left unspecified. The statement is
valid for arbitrary finite region sizes and vertex valences in this model.

To make the retained data explicit, decompose each boundary representation
unitarily as

```
K_r = direct_sum_(lambda_r) M_(r,lambda_r) tensor V_(lambda_r).
```

Here `lambda_r` is a tuple of SU(2) spins at the boundary vertices, trivial
where the region is absent. `M` is the full multiplicity space. Since the
region is finite, only finitely many tuples occur. Finite-dimensional unitary
representations split orthogonally by taking invariant orthogonal complements,
so this step assumes no dynamics or state selection. The reconstruction is

```
H_graph^singlet = direct_sum_(lambda_1,...,lambda_m)
   [tensor_r M_(r,lambda_r)] tensor
   Inv_(K_boundary)[tensor_r V_(lambda_r)].
```

In particular, boundary spin labels alone are insufficient when either a
regional multiplicity or the final invariant tensor multiplicity exceeds
one. Those indices must not be collapsed.

For two regions, Schur's lemma identifies
`Inv(V_lambda tensor V_mu)` with `Hom(V_lambda^*,V_mu)`: it has dimension
one exactly for dual matching irreducibles and is otherwise zero. In dual
orthonormal bases its unit vector is

```
omega_lambda = (1/sqrt(d_lambda)) sum_a |a> tensor |a*>.
```

For a product boundary group, `d_lambda=product_v (2j_v+1)`.
Inserting `omega_lambda` in each matching sector gives an isometry from
`direct_sum_lambda M_(A,lambda) tensor M_(B,lambda^*)` onto the full
global invariant space. The factor `1/sqrt(d_lambda)` is forced by its
norm, because the unnormalized sum has norm squared `d_lambda`. In the
spin convention `V_j tensor V_j`, this is equivalently
`sum_m (-1)^(j-m)|j,m>|j,-m>/sqrt(2j+1)`.
For a fundamental pair, the runner uses `s=|01>-|10>` with metric two,
and the exact rational projector `s s^dagger/2`; omitting the denominator
fails idempotence. This avoids approximating square roots numerically.

## 8. Grouping when a third region still meets the vertex

Suppose a cluster of already joined regions has edge union `E_S`. A vertex
may be projected to its full Gauss singlet at this stage only if its entire
incident-edge set is in `E_S` and it is intended to be internal in the final
object. At every vertex with incident edges in a remaining region, retain the
cluster's *total boundary representation*, including all its spin channels
and multiplicities. These boundary channels need not be singlets.

The valid grouping rule follows from the projector proof: impose only those
commuting full-vertex constraints whose complete support has arrived. Tensor
product regrouping and full representation decomposition preserve the whole
space. Once all relevant regions have arrived, impose the single diagonal
Gauss projector at the vertex. Every grouping then imposes the same final
set of commuting projectors. This is the associativity statement; it does
not assert that projecting every pairwise boundary to a singlet is associative.

A local exact example exhibits the loss. Let regions `A` and `B` supply one
spin-half each at a common vertex and region `C` supply two spin-halves.
All are allowed occupied endpoint representations of the supplied link
model. With bits `0=up`, `1=down`, define

```
t = |0011>+|1100>
    - (|0101>+|0110>+|1001>+|1010>)/2.
```

The total `J_z`, `J_+`, and `J_-` annihilate `t`, whose norm squared is
three. It couples the first pair's triplet to the last pair's triplet into
a singlet. But the singlet projector of the first pair kills `t` exactly.
Thus an early singlet between regions `A` and `B` discards a valid global
state while region `C` is still unattached.

More explicitly, `u=(|01>-|10>) tensor (|01>-|10>)` is another invariant,
has norm squared four, and is orthogonal to `t`. The elementary decomposition
`(1/2 tensor 1/2)=(0+1)` shows that their channels `0 tensor 0` and
`1 tensor 1` are the two global singlets. A direct exact rank calculation
also gives total invariant dimension two, versus dimension one after the
premature first-pair singlet condition. This is a vertex-representation
example, not the separate four-plaquette graph calculation.

## 9. Common observable actions, overlap, and gate ordering

There are three distinct uses of “glue.”

**Subdivision of one physical link.** The map `D` is an isometric
representation of the same coarse link with a new internal singlet
constraint. It is not two independent copies of that link. Since the
unprojected identities hold for `U`, its adjoint, and correctly accounted
electric terms, they extend by multiplication and addition to any polynomial
in those generators. Hermitian combinations preserve the image and their
finite-dimensional exponentials intertwine as well. Substituting fine chain
products into a Wilson loop therefore gives the same coarse action under
the tensor cut map, in the prescribed traversal order. This statement
includes repeated occurrences of a coarse generator because the image is
preserved after every factor.

**Edge-disjoint regional partition.** There is one kinematical tensor factor
per edge and a canonical common space. A regional operator that preserves
`K_r` and commutes with its retained boundary group extends by identity on
the other factors and preserves the global invariant space. More generally,
boundary-covariant regional operators can be combined with the other
regions' operators by an invariant index contraction; it is the total
contracted operator that must preserve the diagonal singlet space. A charged
regional component alone need not do so. Its boundary indices must remain
available to specify that action.

**Two descriptions with overlapping physical edges.** They must refer to
the same edge factor in the common graph Hilbert space, or provide an actual
intertwiner into a common refinement with the required image condition.
Tensoring two independent copies of each overlapping edge is a different
model. In particular, an isometry `W` satisfying both
`(A tensor I)W=WA` and `(I tensor B)W=WB` for all operators of the same
single-link algebra would imply `W[A,B]=0`, because the two displayed fine
factors commute. Injectivity would force that link algebra to commute.
Here the raw coordinate witness is

```
[P_1,P_2]|2> = |1>/4 != 0.
```

The runner computes this witness. It rules out that particular independent-
copy definition of a common full operator action; it is not a physical
no-go theorem about other codes, constraints, or refinement maps. The valid
chain construction above does not satisfy that independent-copy definition:
the coarse `U` is represented by the ordered product `U2 U1` instead.

Algebraic agreement of observable descriptions does not make overlapping
gates commute or select their temporal ordering. The prior two-square note
already provides an exact witness on a shared physical-link model:
`[B_L,B_R]|L>=-3|R>`. Thus two separately ordered patch exponentials can
differ at second order even when both are well-defined on one consistent
global Hilbert space. A finite joint exponential of a sum of correctly
counted Hermitian patch terms is well-defined and gauge invariant; the
cut/glue theorem supplies neither a fixed-depth circuit for it nor an
ordering-independent product of its regional exponentials.

## 10. Relation to the unchanged framework axioms

The axiom memo fixes physical sites to `Z^3` with nearest-neighbor adjacency,
translations and proper cubic rotations, and fixes each site's full algebra
to `M_2(C)`. Its Admissibility axiom supplies one covariant nearest-neighbor
distribution rule, without selecting a Hamiltonian, update, clock, or
record-production process. Record requires one permanent admissible local
record when present and content-only readout. These requirements are not
replaced by the auxiliary SU(2) Haar model.

Mathematical link subdivision inserts new graph vertices. Inserting a
midpoint of a physical nearest-neighbor edge does not itself give another
site of the fixed `Z^3` lattice. Similarly, keeping boundary group indices
is an exact Hilbert-space construction, not a derivation of extra physical
site factors or allowed auxiliaries. A three-qubit code for a five-state
link and an isometric cut into two such codes establish finite dimensional
representability; they do not specify a homogeneous physical qubit allocation,
code initialization, or a translation- and proper-rotation-covariant fixed
nearest-neighbor schedule.

No native law satisfying the unchanged Admissibility and permanent Record
clauses has been constructed here. The approved primitive registry contains
the minimal axioms and the separate scale-reference, kinetic-isotropy and
realized-state primitives; none is used as a supplier of the five-state
link model or its gluing law. The result is conditional finite gauge-model
mathematics, not full GB1-CF, continuum physics, a physical vacuum or mass gap.

## 11. Exact certificate, mutations, and recovery identities

The runner is `scripts/gb1_cf_boundary_gluing_exact_2026_11_07.py`; its full
raw execution is this folder's `outputs/primary_raw.txt`. It uses only the
Python standard library and contains the mathematical model directly.
There are no imports of a prior primary, checker, mutable specification,
workflow document or claim-status file. The largest Gauss-domain dimension
is 125, handled by sparse exact row elimination; no dense lattice matrix
is formed. The largest cut column has 16 nonzero entries.

The certificate computes the cut columns and metric, complete two- and
three-link internal kernels, endpoint intertwiners, both full chain actions,
image leakage, electric totals, and the three-region grouping example.
Its intentional mutations are:

| Defect | Exact detected result |
|---|---|
| Remove `1/2` from the nonconstant cut columns | First occupied norm becomes `4` instead of `1` |
| Equate the unweighted two-edge electric sum to one coarse Casimir | Residual squared norm `9/16` on a unit occupied column |
| Replace `U2 U1` by `U1 U2` | Full residual squared norm `3/2`; image leakage squared norm `3/4` on the stated input |
| Omit the fundamental-singlet projector's metric denominator | Nonzero idempotence defect, squared norm `2` on `|01>` |

The first three are deliberate candidates passed to the same identity
verifiers as the unmutated construction and rejected by exceptions; the
projector defect is calculated directly. These are checks with detectable
defects, not a count of supporting assertions. All are still author-lineage
self-checks. A fresh-context or otherwise independent mathematical checker
must assess the load-bearing argument separately.

Reproduction requires a fresh `lab_ops.py preflight --numeric`, a unique
numeric lease, and all four recorded math-thread environment values set to
one. The script enforces an 80-second alarm and a 290 MB RSS stop. Release
the lease after the process exits. The host reports shell memory caps
unavailable; the recorded completed run stayed below 26 MB. The raw output
contains acquisition, all emitted exact certificates, resource diagnostics,
and release. No resource refusal was relaxed and no failed output was erased.

Source hashes at derivation time:

```
PRIMARY_SPEC.md
83f738a6017421668c63a5406470a05e4c40e9d56cd1591ea159ffea08f5b956
GOAL.md
3c9e97f4aed66965c6f0c35a76c5f0a36e725b79e9933a889a34b08ec373a715
prior two-plaquette note
6fe2122dbe905547319f9347e45fcc122ecc07ba6bc5e7c3ad7f626dd6d7b43f
MINIMAL_AXIOMS_2026-06-29.md
93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753
axiom_premise_nodes.json
615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37
```

Only the three assigned deliverables were authored. No axiom, registry,
editable prompt, shared workflow/status, GitHub object, or platform-supplied
instruction was changed. The next step is the supervisor's comparison with
the separate checker and its disposition of this bounded result.
