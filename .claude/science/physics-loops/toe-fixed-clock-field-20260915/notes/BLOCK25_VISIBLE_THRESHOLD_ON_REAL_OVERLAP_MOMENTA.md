# A local source reaches the polarized threshold on a different momentum slice

Personal derivation, 2026-09-16 UTC. PROVISIONAL, no independent audit.
Same supplied native Hamiltonian and polarized boundary representation as
Blocks9--10. This does not select a physical vacuum or prove a particle pole.

## 1. The remaining source question

Block9 gives the full fiber floor E_pol=2U-4sqrt(3)|t| at every momentum,
with no eigenvector at that floor. Block10 shows that at diagonal momentum
k=(theta,theta,theta), theta!=0, every bounded-word source misses a
support-dependent interval above that floor when J>0.

The source used here is the SAME local Hermitian operator

    C_m=epsilon_m/sqrt(3) sum_i X_(m,i),

whose fiber vector is the one-letter u=(1,1,1)/sqrt(3) in the exact signed
native translation frame. It is not a newly chosen nonlocal preparation.

Put a=sqrt(3)|t|>0 and v(k)=(exp(ik1),exp(ik2),exp(ik3))/sqrt(3). Consider
momenta satisfying

    c=<u,v(k)> is REAL and 0<=c<1.                              (1)

A concrete nontrivial curve is

    k=(theta,-theta,0),   0<|theta|<=2pi/3,
    c=(1+2cos theta)/3.                                         (2)

For every fixed J>0, the spectral measure of C_m at each such momentum
has infimum of support EXACTLY E_pol. It gives positive weight to
(E_pol,E_pol+delta) for every delta>0, and has no atom at E_pol.
No edge-density exponent or uniform lower weight is claimed.

## 2. A reducing two-letter carrier with nonpositive off-diagonal entries

Let s=sqrt(1-c^2)>0 and w=(v-cu)/s. Then u,w are orthonormal and

    v=c u+s w.                                                  (3)

The space of all nonempty words in {u,w} reduces the exact fiber operator

    H(k)=2U+J sum_j(I-Swap_(j,j+1))
                     -a(R_u+R_u^*+L_v+L_v^*).                  (4)

Indeed all creations and annihilations use vectors in this two-dimensional
space and swaps preserve it. Its orthogonal complement also stays invariant
by self-adjointness. The local source is the one-letter basis vector u.

In this orthonormal binary-word basis, every off-diagonal coefficient of H
is real and nonpositive: unequal adjacent letters swap with coefficient
-J, left u/w creation has coefficient -ac/-as, and right u creation has
coefficient -a. Coincident edges add their nonpositive coefficients. This
is a momentum-dependent mathematical frame, not a claim that the native
Pauli Hamiltonian is stoquastic in one common frame for all momenta.

The graph of nonzero off-diagonal entries is connected for J>0. Starting
from u, left-create any desired number m of w letters and right-create
the remaining u letters, then use adjacent swaps to order them. An all-w
word is reached by prepending its w letters to the initial u and removing
that final u on the right. The intermediate word remains nonempty.
This also works at c=0; left u creation is unnecessary.

## 3. The threshold already occurs in this smaller carrier

Set alpha=arccos c in (0,pi/2] and choose the real unit curve

    z(r)=cos((1-r)alpha)u+sin((1-r)alpha)w,   0<=r<=1.          (5)

It joins v to u inside the binary carrier, has nonnegative coefficients,
and obeys <z,z'>=0 and ||z'||=alpha. The same explicit tensor argument
as Block9 now uses

    xi_n=tensor_(j=1)^n z(j/(n+1)),
    <xi_n,K_n xi_n>=(n-1) sin^2(alpha/(n+1))<=alpha^2/n.        (6)

Both endpoint creation overlaps are real and positive and are exactly

    <xi_(n+1),L_v xi_n>=<xi_(n+1),R_u xi_n>
       =product_(r=1)^(n+1) cos(alpha*r/[(n+1)(n+2)])
       >=1-alpha^2/[2(n+1)].                                  (7)

The inequality follows from 1-cos x<=x^2/2 and telescoping products in
[0,1]. Take normalized nonnegative sine coefficients b_n on N,...,2N,
with sum_n b_n b_(n+1)=cos(pi/(N+2)). Then the finite-word positive vector
Xi_N=sum b_n xi_n satisfies

    <Xi_N,(H-E_pol)Xi_N>
       <=J alpha^2/N
        +4a{1-[1-alpha^2/(2(N+1))]cos(pi/(N+2))}->0.            (8)

The global lower bound H>=E_pol still applies to this reducing carrier.
Thus its floor is exactly E_pol. The pure-length-raising isometry argument
from Block9 excludes a normalizable vector at that floor here as well.

## 4. Positivity transfers the floor to the fixed local source

This step does not assume that the source is an algebraically cyclic vector.
The positive heat semigroup is enough. Write H=2U+JK-B with B the bounded
nonnegative-entry endpoint matrix, ||B||<=4a. At each word length K is a
finite graph Laplacian, so exp(-tau JK) is positivity preserving. The norm
convergent Dyson series in the bounded B proves that exp(-tau H) has
nonnegative entries. Connectivity from section2, with positive time spent
in each required swap block and endpoint insertion, makes every matrix
element between two binary words strictly positive for tau>0.

Shift H by E_pol so it is nonnegative. For the source e_u and any fixed
tau>0 the vector psi_tau=exp[-tau(H-E_pol)]e_u has strictly positive
coordinates. Every nonnegative finite-word vector f therefore obeys
0<=f<=C_f psi_tau coordinatewise for some finite C_f. Positivity gives

    <f,exp[-T(H-E_pol)]f>
      <=C_f^2 <psi_tau,exp[-T(H-E_pol)]psi_tau>.                 (9)

Suppose the source spectral measure were supported above E_pol+delta for
some delta>0. The right side would be at most C_f^2 exp(-T delta), since
||psi_tau||<=1. Choose f=Xi_N with its normalized Rayleigh excess below
delta, possible by (8). Spectral Jensen gives the lower bound

    <f,exp[-T(H-E_pol)]f>
        >=exp[-T <f,(H-E_pol)f>].                               (10)

Equations (9)--(10) contradict each other as T->infinity. Therefore the
source has spectral support arbitrarily close to E_pol. Since that energy
is not an eigenvalue, the source measure has no atom there and the nearby
weight lies in the open interval claimed in section1.

All infinite statements follow from these form and semigroup arguments.
There is no limiting inference from small finite matrices, and no claim
that C_f or the spectral weight is bounded uniformly as the threshold
is approached.

## 5. Scope and significance

The local symmetric source cannot see the full threshold on the nonzero
diagonal momentum line of Block10, yet it DOES reach that threshold on
the distinct real-overlap momenta (1). A flat spectral floor is therefore
neither universally invisible nor an isolated particle band. The exact
source and the boundary representation matter.

The real nonnegative overlap is the hypothesis that removes interfering
endpoint phases. A generic complex <u,v> does not satisfy the positivity
argument. The result is not extended to generic momentum by continuity,
nor is the earlier near-diagonal leakage upper bound treated as a lower
bound. J=0 has separate exact channels in Blocks9--10 and is not needed
for the connected-swap proof here.

E_pol is a charged-pair threshold relative to the supplied polarized
neutral reference. For U>2sqrt(3)|t| it is strictly positive. The theorem
does not imply a massless physical particle, identify the periodic vacuum,
or resolve the fixed-g charged photon/Weyl phase of the different rotor
model in Blocks16--24. No axiom wall follows.

The finite checker independently builds full three-letter and binary-word
matrices, checks their exact embedding and the local source, tests graph
connectivity and off-diagonal signs, and evaluates the texture bounds.
It does not assign a numerical threshold exponent or photon interpretation.
