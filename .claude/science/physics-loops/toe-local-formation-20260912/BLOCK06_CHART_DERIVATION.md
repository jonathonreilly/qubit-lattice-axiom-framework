# A sharper native Gaussian chart and uniform normalized-state compression

Author conditional theorem candidate, 2026-09-13. This is an analytical
extension of the pinned pair-chart, certified imaginary-time, mixed-Gaussian
and finite-excitation notes. It does not determine alpha. The sharper
rank-two metric is new in this packet; the Riccati and Gaussian identities
used after it are explicitly inherited and rederived where needed.

## 1. Domain and supplied objects

Use the actual infinite pi-flux cubic quadratic model, hopping units h>0,
and its original canonical pure Gaussian vacuum Omega. A is one of the
fifteen actual two-link impurities. In the common real reference polar
frame, the one-particle off-diagonal block is

    D=S-2u b^T,
    a=S^(-1/2)u, d=S^(-1/2)b, c=a^T d=1/3.

S is bounded, positive and injective; its inverse is not assumed bounded.
The weighted vectors exist in l2. The source supplies the actual Fock
representation and scalar energy, the trace-class polarization difference

    ||P_A-P_0||_1 < 87,

and positive reference overlap of the stationary impurity vacuum. These
remain conditional dependencies. No finite-L uniform threshold, axiom
selection of this Hamiltonian/state, or native numerical kernel is supplied
by this note. The relevant source pins are at the end.

The conclusions for the exact normalized state
psi_A(t)=exp(-t D_A)Omega/||exp(-t D_A)Omega||, every finite t>=0, are

    ||Z_A^ref(t)|| <= 7/9,
    ||Z_A^ref(t)||_1 < 111,
    ||Z_A^ref(t)||_HS^2 < 86.                         (1.1)

For any two such states, at independently chosen finite times, their
normalized overlap is strictly greater than exp(-152). Ordered transition
ratios of two unit real Majorana fields have absolute value at most8;
four fields have absolute value at most192. These bounds do not determine
the sign of an inserted Ward kernel.

If the stationary P_A-P_0 has a rank-k nuclear approximation with error
eta<1, then at each finite time there exists a normalized even Gaussian
state using at most k+1 complex reference modes and with Fock-vector error
at most eta/sqrt2. The mode subspace may depend on t. This is not a fixed
subspace, a numerically extracted basis, or an error guarantee for
normalizing a propagated approximate initial vector.

## 2. Sharpen the existing scalar metric without a physical oracle

The pair-chart source proves the positive expansion and tail bound

    h C0 <= (1000/2449) sum_(n=0)^32 c_(2n) p_(2n) + 1/192,
    c_(2n)=binom(4n,2n)/4^(2n),
    p_(2n)=binom(2n,n) sum_(j=0)^n binom(n,j)^2 binom(2j,j)/6^(2n).

The same thirty-three terms, with no changed cutoff, obey the sharper
exact rational comparison

    h C0 < 23/50.                                    (2.1)

The decimal value of the displayed rational upper bound is approximately
0.459482; that is a bound assembled from integer counts, not an acquired
physical value of C0. Its proof still uses the source's return-probability
tail and sqrt6>2449/1000. The exact comparison is checked separately.

For perpendicular pairs, p=||a||||d|| obeys p^2=2(h C0)^2<529/1250.
For opposite pairs, p^2=C0 mu/3, mu<=sqrt6 h<5h/2, so
p^2<23/60<529/1250. Thus both actual geometries satisfy

    c=1/3,  c^2<=p^2<529/1250<4/9.                  (2.2)

The source bound p<=33/50 alone would already give the joint metric
constant sqrt(7301/199), a substantial improvement on99. Equation(2.1)
lets us give the simpler final transition bound8.

## 3. Exact joint rank-two metric

Write the symmetric and skew parts in the Hamiltonian convention as

    H_s=(D+D^T)/2=S^(1/2) M S^(1/2),
    K_s=-(D-D^T)/2=S^(1/2) N S^(1/2),
    M=I-a d^T-d a^T, N=a d^T-d a^T.

The span of a,d is at most two dimensional. If p=c then N=0. Otherwise
the normalized sum and difference of a/||a|| and d/||d|| form an
orthonormal basis of that span. In this basis,

    M=diag(1-c-p,1-c+p),
    N=[[0, +/-sqrt(p^2-c^2)],[-/+sqrt(p^2-c^2),0]].

M is identity off this span and is strictly positive by(2.2). Hence

    ||M^(-1/2) N M^(-1/2)||^2
       = (p^2-c^2)/((1-c)^2-p^2)
       < 3511/239 < (31/8)^2.                       (3.1)

This is the exact relative skew norm, not separate bounds on M and N.
For real v,w, apply it to M^(1/2)S^(1/2)v and
M^(1/2)S^(1/2)w to obtain

    |v^T K_s w| <= (31/8)
           sqrt(v^T H_s v) sqrt(w^T H_s w).           (3.2)

Only the bounded inverse of M is used. No bounded inverse of S or H_s is
asserted. The factorization first holds on spectral cutoff vectors and
extends by bounded forms, since S^(1/2)a=u and S^(1/2)d=b.

The same argument covers the source interpolation D_lambda=S-2lambda u b^T.
Its squared relative norm is

    lambda^2(p^2-c^2)/[1-2lambda c-lambda^2(p^2-c^2)],

which increases on0<=lambda<=1: its derivative has the sign of
2lambda(1-lambda c). Thus(3.2) is uniform along that interpolation too.

For completeness, on a genuine relative-polar eigenvector with eigenvalue
exp(i theta), x^*D x=exp(i theta)x^*|D|x. The complex version of(3.2)
gives |tan theta|<=31/8 and Re(x^*D x)>0. Therefore the stationary graph
also lies inside the disk stated below. This does not infer an operator
ordering between |D| and S from a numerical-range inequality.

## 4. Uniform finite-time disk

The actual real Gaussian reference pairing solves the inherited ordered
CAR equation

    Z'=-K_s-H_s Z-Z H_s-Z K_s Z, Z(0)=0.

Set r=7/9, M_Z=r^2 I+Z^2, A_Z=H_s+ZK_s. Direct differentiation gives

    M_Z'=F-A_Z M_Z-M_Z A_Z^T,
    F=2r^2 H_s-2Z H_s Z-(1-r^2)(K_s Z+Z K_s).

For a0=v^T H_s v and b0=(Zv)^T H_s(Zv), equation(3.2) implies

    v^T Fv >=2r^2 a0+2b0-2(31/8)(1-r^2)sqrt(a0 b0)>=0,

because

    2r-(31/8)(1-r^2)=2/81>0.                       (4.1)

This estimate holds for every real skew Z; it does not assume the disk it
proves. Variation of constants represents M_Z as positive congruences of
r^2I and F. Consequently M_Z>=0 and ||Z||<=r. Bounded coefficients and
this norm bound preclude finite-time ODE blowup in the bounded-operator
space. Finite-rank K_s and the trace-ideal differential bound preserve
trace class at each finite time.

The source's real finite-rank compressions inherit(3.2). Their Riccati
solutions converge in trace norm on compact time intervals, using strong
convergence of the bounded H_s, trace convergence of K_s and Gronwall.
Quadratic Fock semigroup convergence identifies the resulting Gaussian
vector with the exact normalized evolution of the supplied D_A. The
relative-energy scalar cancels only on normalization. Thus this is a bound
on the actual quench, not merely a free-standing Riccati equation.

## 5. Uniform trace ideals by contraction in the stationary frame

Let P_t be the pure one-particle polarization of psi_A(t). In the stationary
impurity frame, the original state has skew graph Z_0^A. Its singular
values encode the principal angles between P_0 and P_A. Exact normalized
imaginary-time evolution has graph

    Z_t^A=U_t Z_0^A U_t^T, U_t=exp(-t omega_A), ||U_t||<=1.

The scalar ground-energy factor and vector normalization do not enter this
graph. For every j, s_j(Z_t^A)<=s_j(Z_0^A), by the min-max characterization
of compact singular values under left/right contractions. For a canonical
two-mode paired block of graph singular value z, the polarization
difference has four singular values sin(theta)=z/sqrt(1+z^2). That
function is increasing. Therefore, with multiplicities retained,

    s_j(P_t-P_A)<=s_j(P_0-P_A) for every j.           (5.1)

This is not a contraction assertion for normalizing arbitrary nearby
initial vectors. It compares the exact state on its specified Gaussian
orbit with its own stationary vacuum.

From(5.1) and the source trace bound,

    ||P_t-P_0||_1 <=||P_t-P_A||_1+||P_A-P_0||_1<174. (5.2)

For the graph in the original reference frame, the same canonical blocks
give the exact relation

    ||P_t-P_0||_1=2 Tr[|Z_ref|(I+|Z_ref|^2)^(-1/2)].

Combining this with ||Z_ref||<=7/9 gives

    ||Z_ref||_1 <87 sqrt(1+(7/9)^2)
                   =29 sqrt130/3 <111,
    ||Z_ref||_HS^2 <=||Z_ref|| ||Z_ref||_1
                   <203 sqrt130/27 <86.             (5.3)

This proves the all-time uniform bounds(1.1), beyond the source's
finite-time trace-ideal existence estimate. Square comparisons establish
both final rational inequalities; no spectrum is evaluated.

## 6. Uniform mixed overlap and fixed-degree transition ratios

Take two exact pair-quench states at any finite times in the same real
reference frame. Let their pairings be Z_A,Z_C. The existing exterior-
algebra/Fredholm formula with positive reference anchors is

    O_AC=a(Z_A)a(Z_C) exp[Tr log(I-Z_A Z_C)/2] >0,
    a(Z)=det(I+Z^*Z)^(-1/4).

The logarithm converges in trace norm since ||Z_A Z_C||<=49/81<1. With
T_A=||Z_A||_HS^2 and T_C similarly, its elementary series bound yields

    log O_AC >=-(T_A+T_C)/4
                -sqrt(T_A T_C)/(2(1-49/81))
              >-4859/32 >-152.                     (6.1)

The explicit floor concerns normalized states. The unnormalized
evolutions still have decaying scalar norms. The small value of this
conservative floor is not a claim of convenient numerical conditioning.

For the ordered transition contractions in the source convention,

    A=(I-Z_C Z_A)^(-1), F=-A Z_C,
    B=Z_A A, C=-Z_A A Z_C,

their respective operator bounds are81/32,63/32,63/32,49/32. A unit real
Majorana combination has annihilation and creation coefficient norms1.
Adding the four bilinear terms therefore gives8. The three terms of the
ordered four-field Wick formula give3*8^2=192. Index order, CAR contact
terms and explicit native factors of i must all remain in place. This
transition functional is not a positive state; no inserted sign follows.

## 7. Polylogarithmic normalized-state existence in the original frame

Suppose a stationary D_0=P_A-P_0 admits a rank-k approximation Q with
||D_0-Q||_1<=eta<1. The best-rank singular tail obeys
sum_(j>k)s_j(D_0)<=eta. Equation(5.1) transfers the same tail bound to
P_t-P_A. Adding respective rank-k best approximants gives a rank<=2k
approximation to P_t-P_0 with nuclear error<=2eta. Hence

    sum_(j>2k)s_j(P_t-P_0)<=2eta.                    (7.1)

Choose canonical paired principal-angle blocks before ordering accidental
degeneracies, and keep every block touching the first2k singular
directions. Completing the last block adds at most3 directions, so the
state uses at most floor((2k+3)/2)=k+1 complex reference modes. There are
no fully swapped modes: the reference graph norm is at most7/9. The
discarded angle trace satisfies

    tau=4 sum_tail sin(theta)<=2eta.

With both phases fixed by their positive reference amplitudes, the exact
paired Fock product gives

    ||psi_A(t)-psi_ret(t)||^2
      =2[1-product_tail cos(theta)]
      <=2 sum_tail sin^2(theta)
      <=2[sum_tail sin(theta)]^2 <=eta^2/2.           (7.2)

This proves the stated eta/sqrt2 normalized-state error. It does not
normalize a propagated approximate state, so it does not contradict the
source's two-level normalized-error counterexample. The exact principal
subspace generally depends on t; its construction may be expensive.

The source's stationary quadrature certificate supplies rank
k=4p(J_lo+J_hi) with nuclear error at most

    (357/25)2^(-J_lo)+2*2^(-J_hi)+429*(4/25)^p.

Thus at every time a common-original-reference finite-mode approximation
exists with k+1=O(log^2(1/eta)) modes. This is a uniform bound on required
mode count, not a fixed basis for all times, a computational complexity
bound, or a complete Ward integration method. Applying boundary sources,
constructing shared bases and propagators, relative scalar energies,
roundoff and signed integration remain separate obligations.

## 8. Proof status and provenance

All results are conditional on the supplied model and named source
theorems. They are new author derivations with43 same-agent check groups
recorded in BLOCK06_CHART_CHECKS.json, not independent review or formal audit. Alpha remains
open; a positive mixed overlap is not its missing sign theorem.

Source 4f0964492f54b5160b79ff39b60c4b8a4a77f09b:
NATIVE_PAIR_VACUUM_CHART_NOTE_2026-09-09.md,
NATIVE_CERTIFIED_IMAGINARY_TIME_NOTE_2026-09-09.md,
NATIVE_MIXED_GAUSSIAN_TRANSITION_NOTE_2026-09-09.md,
NATIVE_FINITE_EXCITATION_WARD_NOTE_2026-09-09.md.
Their canonical note text was read; their physical numerical certificates
were not replayed. The scalar metric check here repeats only the stated
fixed combinatorial upper bound at N32. Byte-identical copies and SHA256
bindings are in BLOCK06_SOURCE_MANIFEST.json and block06_sources/.

The checker verifies exact noncommuting rank-two congruences, the Lyapunov
identity and adverse signs, a literal16-dimensional Fock graph transform,
and a rational positive-contraction example where the projection-difference
rank grows from4 to8. An eight-mode one-particle fixture checks nontrivial
tail compression by small floating SVDs: actual paired-state error about
0.01927 versus the conservative bound0.51346. These are synthetic Gaussian
fixtures, not native propagation. All43 groups passed the first fixed run.
