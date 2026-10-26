# Finite axis-action covariance and particle–hole sector extension

**Date:** 2026-10-23
**Type:** bounded_theorem
**Status authority:** independent audit only; no retained status asserted.
**Primary runner:** `scripts/finite_axis_action_particle_hole_covariance_2026_10_23.py`
**Cached output:** `logs/runner-cache/finite_axis_action_particle_hole_covariance_2026_10_23.txt`

## Supplied finite setting

Let O be the 24 orientation-preserving signed permutation matrices in three
coordinates. Write P(R)=|R|, s(R)=det P(R) in {+1,-1}, T=ker s,
and supply the on-site Bloch action Q(R)=s(R)P(R). This is an explicit
chosen representation, not a selection of a physical soldering or dynamics.
Let S be any finite O-set of size V>=1, with site-permutation representation
Pi_R on H=(C^2)^{tensor S}. No spatial metric or locality is assumed.
For example the three unoriented coordinate axes form a three-element O-set.

Put n=(1,1,1)/sqrt(3). At each site choose the occupation basis
(|+n>,|-n>)=(occupied,vacant), and define N=sum_x (I+Z_x)/2 and
C=tensor_x X_x. Choose any SU(2) lifts D_R of Q(R), expressed in this
basis, and V_R=(tensor_x D_R) Pi_R. Lift signs/global phases do not affect
commutation or conjugation. Let U be a unitary on H satisfying [U,N]=0.
This number-conservation hypothesis is essential.

## Theorem: covariance reduction

For any fixed R0 with s(R0)=-1, the following are equivalent:

1. [U,V_R]=0 for every R in O.
2. [U,Pi_t]=0 for every t in T and [U,C Pi_R0]=0.

These statements concern finite tensor-product operators. They do not by
themselves construct a finite-range automorphism, a translation-invariant
lattice update, a glider or an infinite-volume dynamics.

**Proof.** Absolute values multiply for signed permutation matrices, so
P(RR')=P(R)P(R') and s is a homomorphism. Since det R=1, all Q(R)
have determinant s(R)^4=1; Q is a representation and Q(R)n=s(R)n.
The 12-element kernel T has index two. Every odd element lies in R0 T,
and R0^2 belongs to T.

For an even element D_R Z D_R^*=Z. A two-by-two unitary with this
property is diagonal, hence D_R=c_R exp(i theta_R (I+Z)/2) for some
unit-modulus c_R and real theta_R. For an odd element D_R Z D_R^*=-Z,
so it is antidiagonal. Multiplying on the right by X makes it diagonal,
hence D_R=c_R exp(i theta_R (I+Z)/2) X. Therefore

```
V_R = c_R^V exp(i theta_R N) H_R,
H_R = C^{epsilon(R)} Pi_R,  epsilon(R)=(1-s(R))/2.
```

Because [U,N]=0, the invertible phase factor commutes with U; thus
[U,V_R]=0 if and only if [U,H_R]=0, separately for every R.
The global C commutes with every site permutation and C^2=I, so H_R
is a representation of O. Consequently its commutant is determined by
T and any one odd coset representative. This proves both implications.
It does not assume that U commutes with C or with every odd Pi_R
separately; those are stronger conditions. ∎

## Positive paired-sector extension

Let H_k be the N=k eigenspace and Theta=C Pi_R0. Then Theta maps H_k
unitarily to H_{V-k}, because Pi preserves N and C N C=V I-N.
For k != V-k, any unitary A on H_k commuting with all Pi_t, t in T,
extends to a number-conserving, axis-O-covariant unitary on H by setting

```
U|H_k = A,
U|H_{V-k} = Theta A Theta^{-1},
U|other sectors = identity.
```

To check the assertion, conjugation by Theta sends Pi_t to
Pi_{R0 t R0^{-1}}, still in T. Thus the other block also commutes with T.
Moreover Theta^2=Pi_{R0^2}, which commutes with A. This makes the two
blocks consistent under Theta in both directions. Identity blocks are
preserved or exchanged by Theta. The covariance theorem now applies.
There is no statement that this arbitrary finite-sector extension is local.

**Half filling is different.** If V is even and k=V/2, Theta acts
inside H_k; the additional condition [A,Theta|H_k]=0 remains necessary.
For two sites with trivial O site action, T acts by number phases, but
Theta=X tensor X swaps |occupied,vacant> and |vacant,occupied>.
The diagonal A=diag(1,-1) on that sector commutes with T and fails to
commute with Theta. Thus the old unqualified assertion of no additional
in-sector condition is not used at finite half filling.

## Finite constructive witness and hypothesis controls

For S equal to the three unoriented axes, let p cycle the axis labels.
On the one-occupation sector let U=Pi_p, on the two-occupation sector
let U=Pi_p^{-1}, and fix the empty/full configurations. This is an
explicit eight-by-eight permutation unitary. Even permutations commute
with p, while odd ones conjugate p to p^{-1}; combining an odd
permutation with C exchanges the two number sectors. Hence U obeys all
24 supplied axis symmetries but does not commute separately with C or
an odd site permutation. This is a finite algebraic witness, not transport
on three lattice sites or a physical particle-identification claim.

Dropping number conservation fails: on a single fixed site take U=X.
It commutes with every reduced H_R (I for even R, X for odd R), but
not with an even nontrivial diagonal lift. This discriminates the phase
cancellation hypothesis from the reduced group identities themselves.

The primary checks integer group identities for all 24 matrices and all
576 products, all three Pauli-image identities for numerical SU(2) lifts,
the diagonal/antidiagonal pattern, exact permutation commutators for the
three-axis witness, and its full phase-sensitive covariance. The original
1e-12 lift-pattern tolerance is preserved; all numerical lift residuals
are explicitly reported. Finite checks support the written proof and do
not replace its arbitrary-finite-S argument. The half-filling and omitted
number-conservation examples test the actual finite operators.

## Source recovery and excluded campaign claims

This is the positive finite core of C4f Step 1, preserved at original
PR9831 commit `e294c1dc745dad0c95b4c8688efc6f3f0be03613` under
`.claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C4f/`.
The complete NOTE, REVIEW, scripts and logs remain in that recovery.
The original build_O, perm_sign and su2_lift functions are extracted
unchanged; the full two-layer CA is not imported to obtain these functions.
The historical reviewer independently derived the on-site action and checked
all 24 lifts (49/0); this is prior same-model-family evidence, not a new
independent review of this finite formulation or its half-filling boundary.

Pair-move enumeration, controlled-layer involution, arbitrary configurations,
CA/QCA radii, glider speed, interface behavior and all no-go conclusions
remain outside this unit. No C4e locality bound or physical primitive is
inherited. The lost author classification failure remains disclosed by its
explicitly reconstructed log; it is not relabelled as an original capture.
The original review also discloses its lost wrong-count run. Neither failure
is erased or repaired by selecting this separate positive symmetry lemma.
