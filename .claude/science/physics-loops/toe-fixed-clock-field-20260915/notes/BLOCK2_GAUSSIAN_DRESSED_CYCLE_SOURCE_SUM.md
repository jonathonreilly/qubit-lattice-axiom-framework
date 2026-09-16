# Gaussian dressing preserves signed loop bounds and their source remainder

Personal derivation candidate, 2026-09-15. This controls an explicitly
restricted family of unrestricted alternating loops at all lengths. The
same-species Gaussian interaction is retained in full. Hard-core pair
restrictions, residual mixed pair factors and branching graphs are not in
the functional defined here. Thus this is a partial resummation mechanism,
not the physical activity-one partition function or a field-limit theorem.

## 1. Reserve local activity and keep the Gaussian interaction

Use the marked infinite-cubic components and physical fillings from the
preceding notes. For a species with x=g^2 or b^2, use local weight

    w(current,mark)=2/384 exp[-x ||current||_2^2/64].       (1.1)

The factor two accounts for the two orientations when their signs are
averaged with probability one half. Marks have their previous normalized
384-fold cubic law. This is the local part of the exact stable self-weight
split, with c0=1/32. Its remaining Gaussian covariance on filling space is

    K_e=P-c0 DD*, K_m=Q-c0 B*B.                          (1.2)

Both are positive semidefinite contractions, as proved in the forest note.
For each species let s_ij be any fixed positive semidefinite correlation
matrix on the loop's vertex positions. It may be a forest matrix multiplied
entrywise by the earlier cut matrices. It must not be selected from the
component positions or labels during their summation. Define

    G_sigma=exp[-(1/2) sum_(same species i,j)
                   x s_ij sigma_i sigma_j <F_i,K_species F_j>].       (1.3)

The diagonal is included. Independent real Gaussian replica fields with
covariance s_ij K_species give the exact representation

    G_sigma=E_G product_i exp[i sigma_i sqrt(x_i)<F_i,eta_i>].         (1.4)

For each realization, every factor is a diagonal multiplication operator
of norm one on its own component space. The covariance can depend on the
loop length and interpolation parameters; positivity is all that is used.
Repeated and overlapping component labels are allowed by this extension.

## 2. Signed trace bound survives this dressing

In finite component restrictions put

    T_(m,e)=sqrt(w_m w_e) sin(c<F_m,P F_e>), c=2pi N,
    J = [[0,T*],[T,0]], A=|J|, rho=||J||=||T||.

These matrices act on counting l2 after moving the measure weights into
their kernels. Species projections are diagonal contractions. Every
length-l=2r alternating loop with prescribed vertex multipliers is a
trace of l factors M_i J, with those species projections included in M_i.
Two Hilbert-Schmidt factors and l-2 bounded factors give

    |Tr product_i M_i J| <= rho^(l-2) Tr(J*J).           (2.1)

For an alternating trace with a fixed starting species the sharper
Tr(T*T) is available, but the harmless factor two in (2.1) is sufficient.
Gaussian averaging in (1.4) preserves the bound. No entrywise absolute
spatial norm, Taylor expansion of the same-species Gaussian, or claim
that a signed trace is positive has entered this argument.

## 3. A four-source trace inequality includes coincident insertions

Let L be any diagonal complex source amplitude on the two component
spaces. If k_i are nonnegative integers with sum k_i=4 and ||M_i||<=1
are diagonal, then

    |Tr product_(i=1)^l M_i L^(k_i) J|
       <= rho^(l-1) S4,  S4=Tr(|L|^4 A).                (3.1)

This includes four insertions on a single vertex. Here is the proof,
including the noninteger Schatten exponent needed for a 3+1 distribution.
Write J=U A with U a partial isometry commuting with A, ||U||<=1.
Cyclically insert A^(1/2) between neighboring factors. For k>0, put p=4/k.
Factor a diagonal f=M_i L^k through |f|^(1/2) and its contraction-valued
phase, then use Schatten Holder and the Araki-Lieb-Thirring inequality:

    ||A^(1/2) f A^(1/2)||_p
       <= ||A^(1/2)|f|A^(1/2)||_p
       <= rho^(1-1/p) [Tr(|f|^p A)]^(1/p)
       <= rho^(1-k/4) S4^(k/4).                       (3.2)

For the middle step, ALT at p>=1 bounds the p-th power of the left
side by Tr(|f|^p A^p), and A^p<=rho^(p-1) A. For k=0 use the operator
norm bound rho. Apply Schatten Holder to the complete product, with
1/p_i=k_i/4; the partial isometries U do not increase these norms.
This proves (3.1), including singular J by continuity or its polar form.

The imported matrix inequality is Theorem 1 of Audenaert's primary paper,
arXiv:math/0701129v2, with its r>=1 direction. The matrices to which it is
applied are positive semidefinite, the exponent is p in {1,4/3,2,4}, and
the outer trace exponent is one. No complex matrix is treated as positive.
The complex diagonal phase is removed by Holder before that application.

## 4. Physical sources make S4 small without a volume factor

Take the same macroscopic h_a as earlier and

    L_e=-g<F_e,P h_a>, L_m=-i b<F_m,Q h_a>.

For a source disk |z|<=R, replace the measure weights in T by

    q_i=w_i exp(R |L_i|).                              (4.1)

The residual exp(z sigma_i L_i)/exp(R|L_i|) is a diagonal contraction.
For sufficiently small a, the earlier source estimate gives

    q_i <= (2/384) exp[-x_i m_i/128].                   (4.2)

All operator and moment bounds below use q. The full sine bound from the
previous operator note gives

    rho <= c sqrt(M_e(2) M_m(2))
                 +(c^3/6) sqrt(M_e(6) M_m(6)).         (4.3)

For example a sufficient uniform moment bound is

    M_species(k) <= 4 C_A 4^k exp(-x/128)
                   /[1-393*2^(2k+4) exp(-x/128)], k=2,6,
    C_A=1,562,500.                                    (4.4)

In particular rho<1 at sufficiently large fixed g^2,b^2. This is an
operator range, not a proof of a physical phase at those parameters.

To control S4, in the counting basis use

    A_ii <= sqrt((J^2)_ii)
          <= c sqrt(q_i M_other(2)) ||F_i||_1.         (4.5)

The first inequality is scalar Cauchy-Schwarz for the spectral measure
of A at coordinate i; the second is the filling frame bound on sin^2.
For u=P h_a or Q h_a,

    |<F,u>|^4 ||F||_1
        <= ||F||_1^4 sum_y |F(y)| |u(y)|^4.            (4.6)

The complete shape and anchor sum of sqrt(q_i)||F_i||_1^4|F_i(y)| is
uniformly finite when x/256>log393, by (4.2), the fill bound 4m^2 and
the earlier anchor count. The square root of the normalized mark weight
costs only a fixed factor; all 384 marks are included. Consequently

    S4 <= C_[fixed beta,N,R,f] (||P h_a||_4^4+||Q h_a||_4^4)
        <= C a^4.                                    (4.7)

The final bound follows from the earlier smooth-source l2 and Fourier
linfinity bounds: ||P h_a||_2,||Q h_a||_2=O(1) and their linfinity norms
are O(a^2). No finite-free-boundary projection estimate is imported here.

## 5. Every loop length can now be summed for this restricted functional

Define C_l(z), l=2r>=4, by the alternating loop integral of the product
of its l sine bonds, all local weights (1.1), G_sigma, and
exp(z sum_i sigma_i L_i), averaged over the orientation signs. The i^l
factor appropriate to odd mixed bonds may be included and has modulus one.
Global sign reversal makes C_l even. Subtract the constant and quadratic
terms inside the integral and apply the integral fourth-order Taylor
formula used in the cut-completion note.

For each of the l^4 ordered source choices, (1.4) and (3.1), with the
tilted weights (4.1), give

    sup_(|z|<=R) |C_l(z)-C_l(0)-z^2 C_l''(0)/2|
        <= (R^4/24) l^4 rho^(l-1) S4
        <= C l^4 rho^(l-1) a^4.                       (5.1)

The Gaussian expectation and normalized interpolation measures do not
increase the bound. Thus the sum of these remainders over l=2r>=4 with
coefficient 1/r is bounded by C a^4, since sum_r r^3 rho^(2r-1)<infinity.
That coefficient defines this restricted loop functional; it is not
asserted to be the physical cluster combinatorial factor.

For the infinite component spaces, use the operator cutoff prescription
of the sine note. Marked sandwich factors are in Schatten 4/k by (3.2)
and the finite diagonal trace (4.7). Diagonal component projections tend
strongly to one; their source-marked tails tend to zero in those Schatten
norms by (3.2) and the summable diagonal tail of (4.7). Unmarked factors
converge strongly with a uniform norm. Schatten Holder then passes the
subtracted traces to the limit. Dominated Gaussian integration and the
geometric sum over lengths are justified by (5.1). This specifies the
source remainder; it does not give arbitrary absolute spatial summability
of the unsubtracted loop or of its quadratic term.

## 6. What remains before this can control the physical law

The representation (1.4) shows that the full same-species stable Gaussian
does not by itself destroy the signed trace cancellation. This removes
one previously unresolved requirement for the unrestricted loop family.
The actual gas still has pairwise support exclusions, residual mixed
factors and branching networks. Those factors need their own compatible
operator representation or expansion. Their pointwise modulus bound is
insufficient to insert them into (3.1).

A simple finite diagnostic makes that last warning exact. For a normalized
4-by-4 Hadamard matrix T, ||T||=1 and Tr[(T*T)^2]=4. The sum of the absolute
four-cycle weights is 16. Multiplying each cycle by the indicator that
its weight is positive gives 10, violating the bound 4 even though that
multiplier lies in [0,1]. This is an abstract counterexample to arbitrary
bounded residual insertion, not a counterexample to the physical gas or
to the structured Gaussian dressing proved above.

No independent review, axiom change, selected-state identification or full
TOE conclusion is supplied by this personal derivation.
