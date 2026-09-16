# A random-partition hard-core interpolation and its derivative geometry

Personal derivation candidate, 2026-09-15. This is a new interpolation, not
an identity equating the old pairwise-affine hard core with a partition
mixture. The finite three-component challenge passes. The change preserves
the protected loop mechanism but creates new spatial cancellations in the
general tree expansion; those are explicitly unresolved below.

For each species separately, take a random graph on its component vertex
indices with independent edge probabilities s_ij in [0,1]. For its connected
partition pi, let h_pi be the product of full hard-core indicators within
each block. Define H(s)=E_graph h_pi, multiplying the two species' factors.

H is a multi-affine polynomial, 0<=H<=1, H(0)=1, and H(1) is the exact full
hard core. If all s across a prescribed partition are zero, its random graph
and H factorize across those blocks. Thus replacing the old softened hard
core by H in the stable Gaussian/mixed-phase interpolation preserves both
the physical full-coupling endpoint and finite BKAR factorization. The
same-species Gram matrix is unchanged and stays PSD at forest matrices;
the phase-preserving mixed factors retain modulus at most one. Stability
of the undifferentiated residual is unchanged.

Each h_pi has the exact lowering-operator representation from the hard-core
note, with one separate resource copy per block. Every vertex occupies only
one block copy. Its activity cost remains 2^|footprint|<=2^(3m), independently
of the number of vertices or blocks. All entries still commute and have norm
at most one. The partition probabilities depend only on vertex indices and
s, not on the component labels. Consequently the protected cycle/source
trace bound applies to H(s) after its positive partition average.

For a set A of distinct same-species edge parameters, finite differentiation
is the exact Bernoulli difference identity

    partial_A H(s)=sum_(B subset A) (-1)^(|A|-|B|)
             E_(edges outside A) h_(pi(E union B)).

To prove the formula, differentiate the independent Bernoulli product for
each edge in A. A present edge contributes +1 and an absent edge -1;
the other Bernoulli probabilities retain total mass one. This also proves
the derivative formula at boundary values of the remaining parameters.
It represents every derivative as a signed sum of partition hard cores
with total variation at most 2^|A|. A loop whose explicit sine edges already
cover its vertices therefore retains its source bound with this additional
factor. No activity cost proportional to vertex count is required.
For a specified derivative set with k elements, the hard-core loop theorem
therefore gives the four-source bound

    2^k (R^4/24) l^4 rho^(l-2) S4_2, S4_2=O(a^4).

The two-source bound acquires the same factor. If k<=l-1, this is still
geometric in length whenever 2rho<1, for one specified derivative set per
length or a normalized average of such sets. A sum over all derivative sets
and trees requires its own combinatorial bound; it is not included here.

The derivative geometry DOES change. With three same-species vertices and
only the pair (1,3) incompatible,

    H(s)=(1-s_13)(1-s_12 s_23),
    partial_12 H=-(1-s_13)s_23,

although chi_12=0. This derivative enforces the contact (1,3) through a
random connecting path. It is not proportional to the old local factor
chi_12. Thus the former spatial tree majorants cannot be copied over.
Pure hard-core differentiated tree edges still need contact routing or a
new expansion; a signed partition bound without a spatial edge does not
make a general vertex sum finite. Branching and residual mixed interactions
remain distinct obligations.

The changed geometry has an exact three-vertex diagnostic. For pure hard
core with only (1,3) incompatible, vertex 2 is independent and the connected
three-vertex coefficient is zero. Nevertheless the new BKAR tree integrals
are individually nonzero:

    tree {(1,2),(2,3)}: -integral_[0,1]^2 (1-min(u,v)) du dv = -2/3,
    tree {(1,2),(1,3)}:  integral_[0,1]^2 min(u,v) du dv = 1/3,
    tree {(1,3),(2,3)}:  integral_[0,1]^2 min(u,v) du dv = 1/3.

Their sum is zero. If these terms were bounded separately before the
component-position sum, the location of vertex 2 would be unanchored. This
shows exactly why the earlier local hard-core tree majorant cannot be
transferred. It is a method diagnostic, not an impossibility theorem for
this interpolation, the full gas or the axioms.

For clarity, the complete finite interpolation is the earlier product of
local self-reserves, the same-species Gaussian with its original diagonal
and s-weighted modified off-diagonal Gram entries, all affine mixed phase
factors Phi_ij(s), and the source, with H(s) replacing the old hard core.
It is smooth on the finite parameter cube. At all s=1, H enforces the
physical compatibility, where modified and physical Gaussian couplings
agree. At a partition matrix s, every factor splits across its blocks.
These are exactly the finite BKAR identity's smoothness and factorization
hypotheses. At a forest correlation matrix, positivity of the same-species
Schur Gram matrix, |Phi|<=1 and H<=1 retain the earlier local mass reserve.
No convergence theorem has been imported with that finite identity.

The checker realizes the incompatibility pattern on actual electric face
fillings [0,6,1] of the four-cube chain. Original connected partition
inversion and the new analytically differentiated BKAR quadrature agree
within 6.62e-24 at order 28 for a nonzero complex physical cochain source.
Orders 12 and 20 are retained too. Incorrectly forcing every hard-core
derivative to contain the matching local chi gives an error 9.28e-9 against
a reference of magnitude 2.42e-8. The finite checker uses shared floating
cochains and is a personal check, not an independent audit or interval
quadrature proof. The identities and checked finite BKAR hypotheses carry
the derivation; general spatial routing and the physical law remain open.
