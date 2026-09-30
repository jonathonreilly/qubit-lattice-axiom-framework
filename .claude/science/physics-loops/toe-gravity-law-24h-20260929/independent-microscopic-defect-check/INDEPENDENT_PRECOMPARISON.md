# Independent reconstruction, before author-proof exposure

This derivation was written after the literal main definitions and before
opening DEFECT_LEMMA.md or the author's checker/results. It is an independent
argument to compare, not a formal review verdict. Constants below are finite
and deliberately not optimized. This uses the supplied microscopic quantum
law, not a primitive-derived dynamics. SOURCE_READS.json binds the actual
main definitions and exact read scopes.

## 1. Actual grades, norms and geometry

Let M=|A| and W=sum_a w_a, w_a=1-n_a. An unsigned outward F_a empties a,
so [W,F_a]=F_a and [W,F_a^*]=-F_a^*. The supplied T=-F-F^*, F=sum F_a,
and C commute with all Gauss operators. Each C_a preserves all A occupancies,
so [W,C]=0. A birth fills a vacant A and B, hence [W,j]=-j. These are
occupation-word facts independent of electric amplitudes. The normalized
integer-spin shifts have norm <=1, including the vanishing boundary shifts.
The two charge outputs of a fixed edge are orthogonal, so the unnormalized
coherent edge has j^*j equal to the sum of its resolved losses and norm <=sqrt2.
The full actual loss therefore obeys sum_j j^*j <=12 W on a cubic torus.
There is no lower bound by W asserted.

Use sites and links as elementary tensor factors. On even L>=6 tori the
radius-two A neighborhood has 18 other centers: six axial distance-two and
12 two-coordinate offsets. A C_a term involves at most 25 site factors and
six links, hence at most 31 factors. ||F_a||<=6, ||T_a||<=12, ||C_a||<=48
are sufficient main-source bounds, independent of S. Each factor belongs
to at most 19 compensation supports, giving an incident interaction norm
<=912. A hopping/generator star has at most 13 factors and incident norm
<=72. These are coarse sufficient bounds; periodic identifications cannot
increase them. There are eight elementary factors per A center (two sites
and six undirected links), so conversion of an incident interaction norm
to a global norm loses a fixed factor, not a second power of M.

## 2. A local finite-order Hamiltonian rotation

Write h=W+epsilon T+epsilon^2 C. Choose U as a product of five exponentials
exp(epsilon^r A_r), r=1,...,5, acting successively from the left. Every A_r
is anti-Hermitian and is a sum of bounded, finite-support terms. At step r,
if K_r is the still-present order-r coefficient, set

    A_r = sum_(g!=0) (K_r)_g/g,   [W,(K_r)_g]=g(K_r)_g.

Then [A_r,W]=-Off K_r, so conjugation removes that order's nonzero grades.
This fixes the sign. In particular A_1=F^*-F and [A_1,W]=-T. At order two
one obtains H_2=C+[A_1,T]/2, followed by any grade-zero extraction; no
unbounded electric norm is introduced because the literal C is bounded
uniformly in S. Parity Xi=(-1)^W gives h(-epsilon)=Xi h(epsilon) Xi.
The grade-removing recursion preserves this parity. The grade-zero odd
coefficients vanish. Therefore, on every finite torus,

    U h U^* = W+epsilon^2 H_2+epsilon^4 H_4+epsilon^6 R_epsilon,
    [W,H_2]=[W,H_4]=0.                                      (A)

The finite-order proof must use local bounds, not ||T||=O(M). Here is a
sufficient elementary majorant. For an interaction A of maximum support
size s and incident norm g, and O supported on n factors,

    ||ad_A^k(O)|| <= (2g)^k product_(l=0)^(k-1)[n+l(s-1)] ||O||.

Only connected overlap sequences contribute. Division by k! sums to
(1-2g(s-1)|u|)^(-n/(s-1)) for exp(u ad_A), when its argument is positive.
An extra exponential support weight or a factor of the support size is
absorbed by reducing the common u radius. This proves, for sufficiently
small epsilon independent of M,S, uniform local bounds for R_epsilon,
[W,R_epsilon], the rotated jumps and their Taylor remainders. A finite
number of recursively constructed A_r has fixed finite support and
incident norm, so applying this estimate five times suffices. In particular
||[w_a,U]||<=c epsilon uniformly in a,M,S. Although ||U-I|| need not be
small globally, that global bound is never used.

Grade extraction is averaging under alpha_theta(O)=exp(i theta W) O
exp(-i theta W); it preserves support and norm. Its zero-mean inverse is
bounded independently of the number of W sectors. With A0=i delta[W,.],

    I(X)=(1/(2pi delta)) integral_0^(2pi) (theta-pi) alpha_theta(X) dtheta,
    A0 I(X)=X-E(X),    ||I(X)||<=pi/(2delta)||X||.             (B)

This formula also preserves every support decomposition. Thus no global
cluster-isolation radius or sum over M spectral clusters enters (A).

## 3. Grade-averaged dissipation has only a small positive part

Put j_tilde=U j U^*. Since A_1 has only grades +/-1 and j has grade -1,

    j_tilde=j+epsilon[A_1,j]+r_j,
    ||r_j||+||[W,r_j]|| <= c epsilon^2.                      (C)

The first two terms have only grades -1,0,-2. All positive-grade components
of j_tilde are therefore components of r_j. These are statements about the
actual coherent or resolved jumps; the loss is not replaced by a proxy.
For any L=sum_g L_g of definite W grades,

    E(D_L^*(W))=sum_g g L_g^* L_g,
    D_L^*(W)=(L^*[W,L]+[L^*,W]L)/2.                        (D)

The non-averaged cross coefficient is (g+h)/2 in L_g^*L_h. In particular
both recycling and the anti-commutator loss are included. By vector-valued
Parseval and (C),

    sum_(g>0) g L_g^*L_g
       <= sum_g g^2 (r_j)_g^*(r_j)_g
       = E([W,r_j]^*[W,r_j]) <= c^2 epsilon^4 I.

There are 6 coherent or 12 resolved original marks per A center. Hence,
for D_epsilon^*=sum_j D_(j_tilde)^*,

    E(D_epsilon^* W) <= c epsilon^4 M I.                   (E)

This discards a negative part; it does not assume it is coercive in W.
The estimate is independent of spin dimension and the Fourier-grade count.

## 4. Two observable correctors cancel the large off-grade terms

In the rotated picture the exact Heisenberg generator is

    G^*=epsilon^-4 A0 + epsilon^-2 B0 + Q_epsilon,
    B0=i delta[H_2,.]+kappa D_0^*,
    Q_epsilon=i delta[H_4,.]+i delta epsilon^2[R_epsilon,.]
                         +kappa epsilon^-2(D_epsilon^*-D_0^*).

B0 preserves W grades: H_2 commutes with W and every original j has grade -1.
The local interaction-action norm of Q_epsilon is O(epsilon^-1).
Let Y=(1-E)D_epsilon^*(W)=O_loc(epsilon). Define Hermitian correctors

    V1=-kappa epsilon^2 I(Y)=O_loc(epsilon^3),
    V2=-epsilon^2 I(B0 V1)=O_loc(epsilon^5),
    Z=W+V1+V2.                                             (F)

Because B0 preserves grades and E(V1)=0, E(B0 V1)=0. Thus the two exact
cancellations are

    epsilon^-4 A0 V1=-kappa epsilon^-2 Y,
    epsilon^-4 A0 V2=-epsilon^-2 B0 V1.

Using (A), the exact residual is

    G^* Z = kappa epsilon^-2 E(D_epsilon^* W)
       +i delta epsilon^2[R_epsilon,W]
       +Q_epsilon V1+epsilon^-2 B0 V2+Q_epsilon V2.           (G)

Each remainder has global norm <=c epsilon^2 M: their local orders are
respectively epsilon^2, epsilon^2, epsilon^3, epsilon^4. The operator action
on an extensive interaction is bounded by overlapping local supports, not
by multiplying two extensive operator norms. Combined with (E), this gives

    G^* Z <= c epsilon^2 M I,
    ||Z-W|| <= c epsilon^3 M.                              (H)

The two small observable corrections are not positive; positivity of Z is
not used. W remains positive. There is no defect-gap, fast-mixing, or
excited-population inverse premise in (F)-(H).

## 5. Bare preparation, physical W and actual counts

For any initial P-supported density, and in particular the supplied bare
Omega, the rotated initial density sigma_0=U rho_0 U^* satisfies

    tr(W sigma_0)=sum_a ||w_a U rho_0^(1/2)||_2^2
                <=c epsilon^2 M,

because w_a rho_0^(1/2)=0 and ||[w_a,U]||<=c epsilon. Integrating (H) gives
tr(W sigma_t)<=c(1+t)epsilon^2 M on every fixed time interval. To return to
the actual, undressed W use the quadratic-form inequality

    U W U^* <= 2W+2 sum_a ||[w_a,U^*]||^2 I
             <=2W+c epsilon^2 M I.                        (I)

It follows from ||w_a U^* psi||^2 <=2||w_a psi||^2+
2||[w_a,U^*]psi||^2, not from the insufficient global operator comparison
||U W U^*-W||=O(epsilon M). Thus

    tr(W rho_t)/M <= c_T epsilon^2.                        (J)

Translation symmetry of the supplied Omega and law makes this also the
bound at any selected A center. For F selected A centers, the actual count
intensity is at most 12 kappa epsilon^-2 sum_(a in F) tr(w_a rho_t), so

    E N_F(T) <= 12 kappa |F| integral_0^T c_t dt.

This is finite uniformly in M,S; Markov gives a controlled finite-count
overflow. It preserves the original resolved or coherent instrument and
counts their actual events. With epsilon^2 S(S+1)=delta/K, (J) tends to zero
uniformly in volume. It does not give convergence of the field state,
original marked output maps, microscopic energy or unbounded field moments.

## 6. Limits and remaining checks

The needed local estimates in section 2 have been reconstructed analytically
by the connected-commutator bound, but constants have not been optimized or
numerically instantiated. A small independent grade-algebra control can test
(B), (D) and (G), but cannot replace those uniform estimates. The author proof
is still unread at this freeze; comparison must check whether its actual
normal-form order, orientation and corrector definitions supply this chain.

Dark defect states cannot be excluded. If every B neighbor of an A vacancy
is occupied, no birth on its star is available; spin boundaries can suppress
additional channels. Therefore an assumed uniform inequality sum_j j^*j>=cW
would be invalid. This reconstruction uses no such lower bound. Control of
small mean defect density does not control the accumulated fast motion of
those defects, and is not the target local microscopic-to-rotor convergence
lemma. The present scope is an upper defect/activity estimate only.
