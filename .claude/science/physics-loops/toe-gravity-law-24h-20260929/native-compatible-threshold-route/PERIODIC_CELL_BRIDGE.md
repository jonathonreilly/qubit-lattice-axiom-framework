# Actual periodic-cell band and finite Schur operator

Author derivation during the compatible-route cold read, September30,2026.
This does not turn a large physical torus into independent periodic cells.
All prior files remain preserved. No new numerical calculation is required
or claimed. This statement uses the same full physical Hamiltonian, not an
auxiliary edge-particle Hamiltonian.

Fix an integer R>=14 and a physical torus of side L>=10(R+4). Work in its
actual N=2n occupation sector. Write V=L^3, a=min(tau,mu/12), and use the
source-bound C_B=28000322. Let

 C_R=4+15 C_B(R+4)^3,
 Delta=a/[C_B R^3+C_R L^2],
 delta=binom(n,2)(2R+9)^3/V,
 s_R=(2R+9)^3-(2R-7)^3=48(2R+1)^2+1024,
 A_R=60 max(mu,2tau) s_R.

Let W_n embed Sym^n C^5 into the auxiliary edge Fock space by the five
constant normalized U modes, with empty bad environment. The physical frame
is T_n=I_R^dagger W_n. It retains only mutually R-isolated edges. The union
bound from REPORT equation(23), now on a torus, gives

 (1-delta)I<=G_n=T_n^dagger T_n<=I.

Assume delta<1 and let V_n=T_n G_n^(-1/2) be its polar isometry. Its physical
range has dimension d_n=binom(n+4,4). Denote the range projection by P and
its orthogonal complement in the physical N-sector by Q.

## A. A genuine physical compression gap

The proof of REPORT equation(7), without radius averaging, gives

 J_guard(R)<=2J+15 B_(R+4)<=C_R H0/a.                    (A1)

Indeed an unequal guard forces the removed edge to be (R-4)-isolated and
not (R+4)-isolated. Weighted row incidence is at most15, and twice the number
of such edges is bounded by B_(R+4). The squared row split contributes the
factor two, canceled by that two-particle count. The actual all-state
isolation bound supplies the second inequality. This is an operator-form
statement at this fixed radius.

On the periodic nine-component one-body space, write f=m+q with mean q=0.
The first positive gradient eigenvalue is4 sin^2(pi/L)>=16/L^2. As in the
cell proof, S has norm at most2mu, and for constant m,
S(m)=2mu V||P_high m||^2. The squared triangle inequality gives

 V||P_high m||^2<=S(f)/mu+2||q||^2,
 dist(f,constant soft)^2<=3||q||^2+S(f)/mu<=L^2 J(f).

Thus in the embedded physical state the auxiliary nonsoft number obeys

 N_exc<=C_R L^2 H0/a                                  (A2)

in expectation. The environment particle number is B_R and obeys
B_R<=C_B R^3 H0/a. On the constrained auxiliary image of the fixed N-sector,
let P_aux select empty environment and all n pairs in the constant soft
space. Every vector in its complement has at least one environment particle
or one nonsoft pair. Hence

 I-P_aux<=B_R+N_exc

there. Pulling back gives

 H_N>=Delta[I-I_R^dagger P_aux I_R].                    (A3)

The positive contraction I_R^dagger P_aux I_R=T_n T_n^dagger has range P,
so it is at most P. Therefore the stronger full operator inequality holds:

 H_N>=Delta Q, and in particular Q H_N Q>=Delta Q.      (A4)

This is an actual physical finite-cell compression gap. No global defect
projection was assumed close to one. It is not a relative gap above an
extensive thermodynamic background; Delta tends to zero with cell size.
For odd N, empty environment is impossible and the simpler bound
H_N>=a/(C_B R^3) holds under the same torus conditions.

## B. Uniform trial energy on the complete internal n-pair frame

For all actual removal amplitudes, Cauchy on the collective definitions
gives W<=2tau Egrad9. Together with S this gives
S+W<=max(mu,2tau)J. The frame T_n is supported on separated dimers, so D=0
on every input occupation in its support.

For a normalized internal n-pair vector, fix a residual admissible set eta
of n-1 selected edges. The unguarded constant-soft annihilation amplitude is
V^(-1/2)(U v_eta)_d, independent of the removed bond anchor. This follows
from a_(x,d) W_n=V^(-1/2)sum_alpha U_dalpha a_alpha W_n.
The sum of ||v_eta||^2 over all auxiliary residual occupations is n; summing
only admissible residuals cannot increase it. A physical graph annihilator
cannot remove vertices from two different selected edges, since their
separation exceeds R>2. Thus these are all physical outputs of T_n.

The actual frame amplitude is q_R(e;eta) times that constant amplitude.
Every J row annihilates an unguarded constant U vector. Splitting at a
reference guard and applying Cauchy, without the extra factor two needed
when the unguarded row is nonzero, bounds the row by
||l||^2 sum_e |q_e-q_0| |(U v_eta)_d|^2/V.

An unequal guard requires a removed endpoint to lie in a Chebyshev shell
of radii R-4 and R+4 about some residual site. For a fixed bond orientation,
the number of anchors in this union is at most2|eta|s_R, where |eta| here
is the number of residual physical sites, namely2(n-1). Weighted row
incidence is at most15. Since U is isometric, summing all anchors, orientations
and rows therefore gives at most60(n-1)s_R||v_eta||^2/V. Summing the residuals
proves, as a matrix inequality on the full entangled internal space,

 T_n^dagger H_N T_n <= A_R n(n-1)/V I.                  (B1)

The torus shell count is valid under L>=10(R+4); there is no wrapping alias.
No coherent-vector restriction was used. Polar normalization consequently
satisfies

 V_n^dagger H_N V_n<=theta I,
 theta=A_R n(n-1)/[V(1-delta)].                         (B2)

For theta<Delta, min-max with(A4) and(B2) gives exactly d_n eigenvalues
(counting multiplicity) below Delta, all at most theta, and all remaining
eigenvalues at least Delta. For any normalized vector of this low band,
its Q probability is at most theta/Delta by(A4). This identifies the finite
cell's low-dimensional sector without an assumed many-particle dimer law.

At fixed R, mu,tau and n<=K from the dilute cell scales in REPORT(2), with
this cell side L=ell, delta=O(rho^(13/16)) and

 theta/Delta=O(n^2/ell)=O(rho^(1/16)).                   (B3)

The constants are large but fixed. The needed gap and band isolation are
therefore actual asymptotic statements for these periodic cells. This use
of a fixed R is distinct from the averaged growing radius used for the
large-system coarse-observable theorem.

## C. Exact finite many-pair Feshbach operator, not yet a T0 sum

Let C=QH_NQ, invertible with C>=Delta on Q, and define on Sym^n C^5

 S_(n,L)=V_n^dagger H_N V_n
       -V_n^dagger H_N Q C^(-1) Q H_N V_n.             (C1)

It is a well-defined finite Hermitian matrix with0<=S_(n,L)<=theta I. For
any physical vector V_n u+q, q in Q, exact completion of the square gives

 <V_n u+q,H_N(V_n u+q)>
 =<u,S_(n,L)u>
  +<q+C^(-1)QH_NV_nu, C[q+C^(-1)QH_NV_nu]>.           (C2)

No infinite zero-energy inverse or scattering limit has been assumed.
The whole constrained physical contact environment is included in C.

For0<=lambda<=theta<Delta, the energy-dependent Schur matrix differs from
S_(n,L) by a positive amount bounded by
lambda theta/(Delta-theta) times the identity. Indeed functional calculus
on C gives
0<=(C-lambda)^(-1)-C^(-1)
 <=[lambda/(Delta-lambda)] C^(-1),
and the zero-energy Schur subtraction is at most V_n^dagger H_N V_n<=theta.
Congruence of H_N-lambda with its positive Q block and its Schur block then
compares eigenvalue counts. If lambda_j are the d_n low eigenvalues and
s_j the ordered eigenvalues of S_(n,L), continuity at degeneracies gives

 lambda_j <= s_j <=[1+theta/(Delta-theta)] lambda_j.     (C3)

Thus the exact finite effective operator controls this actual low band up
to a relative error vanishing in(B3). This is not an evaluation of it.

## D. Two distinct remaining obligations

First, a controlled many-pair response expansion would have to prove,
uniformly through n<=K and retaining all internal entanglement, that this
exact operator equals the properly normalized sum of the actual full15
threshold pair form, up to o(n^2/L^3), with the appropriate finite-cell
identification. Even fixed-n convergence needs its own response/boundary
argument; it is not proved here from the fixed N4 threshold definition.

Second, an actual lower decomposition of the large physical torus into
such periodic cells is absent. Imposing periodic seams is a changed boundary
law and is not known to lower H0. A Neumann or positive-row alternative
must price the physical shared-center/boundary geometry. Neither the
finite compression gap nor(C2) supplies that gluing step.

These explicit missing obligations prevent an EOS inference. This bridge
is nevertheless stronger than positing a gap: it constructs the actual
periodic-cell low sector, a uniform compression gap and an exact finite
many-pair effective interaction, all from the checked carrier bounds.
