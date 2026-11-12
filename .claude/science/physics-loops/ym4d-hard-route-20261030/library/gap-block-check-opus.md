# Check of library/gap-block-astra.md (FINISH row 808), by Claude Opus 5.5, line by line

- Clone: `/Users/jonreilly/ym4d-lead/clone` at commit `1bad6dfa3d3962673d61a692d5895cee2c1b0b9f`.
- Lane directory D = `.claude/science/physics-loops/ym4d-hard-route-20261030`.
- Target: `D/library/gap-block-astra.md`, 741 lines, by Codex gpt-6-astra max (FINISH row 807). Read in full.
- Context read: `D/library/gap-tree-astra.md` Sections 1-6 (lines 78-650) and its check `gap-tree-check-opus.md` (full);
  `D/library/gap-vmf-lip.md` lines 100-351 (Theorem V tail, Corollary V1, Lemma DC, Lemma INF) and its check
  `gap-vmf-lip-check-opus.md` (full); `D/library/gap-kappa-order.md` lines 31-74; `D/library/gap-ext-astra.md` lines 78-128.
- Sussman-Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, downloaded once into
  `.../scratchpad/sa-dl2.UKAgBC/`; only lines 2195-2393 read (GL3, GL4, GL5-GL7, GL8, GL9, GL10). Treated as data.
- Method: every verdict rests on a hand derivation written below. No numerical run decides anything. Two
  values marked GUIDE were estimated by hand arithmetic only. No repository file was edited.
- This is one reading by a model of a different provider from the author. It is not an audit.

Notation. x = half-trace, w = e^{beta x}, k = w/z, r_j = I_{2j+1}/I_1 for SU(2). Chord metric |g - h| on S^3.
Haar density of x on [-1, 1] is (2/pi) sqrt(1 - x^2).

## 1. (B1)-(B4): the slab kernel, sewing, the charge Theta, T preserves H_-

**(B2) to (B3).** z^b K is convolution by the product of w on each link. For f in L^2(G^E),
(K P_int f)(U) = int prod_e k(U_e W_e^{-1}) int f(h.W) dh dW. Substitute W' = h.W (Haar invariant) and then
h -> h^{-1}: the kernel is int prod_e k(U_e (h.V)_e^{-1}) dh. Multiply by A on both sides and by z^b: this is (B3).
Physical reading: a temporal plaquette over e = (x, y) is U_e(0) U_t(y) U_e(1)^{-1} U_t(x)^{-1}. Put h_x = U_t(x)^{-1}
at interior x and h_x = 1 at boundary x. Cyclicity and x(g) = x(g^{-1}) give w(U_e (h^{-1}.V)_e^{-1}); h -> h^{-1}
gives (B3). HOLDS.

**Symmetry and gauge structure.** T(U, V) = T(V, U): w(V_e (h.U)_e^{-1}) = w(U_e (h^{-1}.V)_e^{-1}) by cyclicity and
inversion, then h -> h^{-1}. K commutes with the vertex gauge action, since k is a class function and both arguments
move together. A is a product of plaquette traces, hence gauge invariant. So T maps H into H. HOLDS.

**Sewing.** T^2 = z^{2b} A K P_int A^2 K P_int A. The middle layer carries A^2 = full spatial action, once. The two
ends keep half action. Interior time links of each step are integrated (one P_int per step). HOLDS.
Scope remark (not an error). Fixing the side time links to the identity is a boundary condition of the slab. In a
larger lattice those links are integrated and shared with neighbours. The note says so in Section 6 (lines 640-641).

**Theta.** Theta is the gauge transformation by the central element -I at the boundary vertex v. Each plaquette
through v contains exactly two links at v, so U_p is unchanged and A is Theta-invariant. For the kernel,
(-U_e)(-V_e)^{-1} = U_e V_e^{-1}, and Theta(h.V) = h.(Theta V) because -I is central. So T(Theta U, Theta V) = T(U, V).
With the measure-preserving involution Theta this gives T Theta = Theta T. P_int commutes with Theta for the same
reason. So T preserves H_-. -I lies in SU(2), in the diagonal U(1) (angle pi) and in Gamma. HOLDS.

**Open Wilson line.** Take a simple path from v to a boundary vertex w != v and f(U) = (U_{e_1} ... U_{e_k})_{ab}.
At an interior vertex of the path h_x^{-1} h_x cancels; interior vertices off the path do not enter; v and w are not
gauged in H. So f is in H. The path has exactly one link at v, so f(Theta U) = -f(U). f is a nonzero function
(the matrix entry of the fundamental representation is nonzero on G, also on Gamma and on U(1)). So H_- is nonzero
and contains this line. HOLDS.

**Verdict, item 1: HOLDS.**

## 2. Resummation and T >= 0 for SU(2), U(1) and Gamma

**Resummation.** k = sum_j d_j r_j chi_j with r_0 = 1 (this matches SA (GL3) after dividing c_l by c_0).
|d_j r_j chi_j| <= d_j^2 r_j, and (GL4) gives r_j <= (beta/2)^{2j}/(2j+1)!, so the series converges absolutely and
uniformly. A finite product of such series may be integrated term by term. For U(1) the weights I_n(beta)/I_0(beta)
decay factorially; Gamma has finitely many irreducibles. HOLDS.

**Positivity.** exp(beta chi_V/2) = sum_n (beta/2)^n chi_V^n/n!. Each chi_V^n is the character of V^{tensor n},
a genuine representation of each of the three groups. A character is positive definite:
sum_{i,j} conj(c_i) c_j chi(g_i g_j^{-1}) = ||sum_i conj(c_i) rho(g_i)||_HS^2 >= 0 after expanding the trace.
A positive combination of positive-definite functions is positive definite. Convolution by a positive-definite
function is a positive operator, so C >= 0 and K >= 0. P_int is an orthogonal projection commuting with K, so
K P_int = P_int K P_int >= 0. A is a real multiplication operator, so <f, A X A f> = <Af, X Af> >= 0. Hence T >= 0.
No sign of an individual sewn spin-network amplitude is used. HOLDS for all three groups.

**Verdict, item 2: HOLDS.**

## 3. Proposition 1, (B5)-(B6)

**Kernel bounds, N = b + p.** For all three groups x lies in [-1, 1]. So A(U)A(V) lies in [e^{-beta p}, e^{beta p}]
and prod_e w lies in [e^{-beta b}, e^{beta b}]; the h-average keeps these bounds. So m = e^{-beta N} <= T <= M = e^{beta N}.
HOLDS.

**Perron eigenfunction.** A bounded kernel on a probability space is Hilbert-Schmidt, so T is compact. It is
self-adjoint (real symmetric kernel, item 1) and positive (item 2). The operator with kernel (B3) on all of
L^2(G^E) is T on H and 0 on H^perp, so the top eigenvalue lambda = ||T|| > 0 is attained in H.
<|f|, T|f|> >= |<f, Tf>|, with equality for a strictly positive kernel only if f = c|f| a.e. So a top eigenfunction can
be taken >= 0, and psi = T psi/lambda >= m (int psi)/lambda > 0. It is continuous because the kernel is uniformly
continuous on a compact product (trivial for Gamma). Simplicity: a second real top eigenfunction orthogonal to psi
would have fixed sign by the equality case, contradicting orthogonality to psi > 0. Theta psi is also a positive
normalized top eigenfunction, so Theta psi = psi. HOLDS.

**psi <= M I/lambda and lambda >= m I^2.** psi(U) = lambda^{-1} int T(U, V) psi(V) dV <= M I/lambda.
lambda = <psi, T psi> >= m I^2. HOLDS.

**Doob kernel and epsilon = m^2/M^2.** P1 = T psi/(lambda psi) = 1. Relative to pi = psi^2 dU the kernel density is
p(U, V) = T(U, V)/(lambda psi(U) psi(V)), symmetric, so P is reversible. Then
p >= m/(lambda (M I/lambda)^2) = m lambda/(M^2 I^2) >= m (m I^2)/(M^2 I^2) = m^2/M^2 = e^{-4 beta N}. With eps < 1,
R = (P - eps Pi_pi)/(1 - eps) has nonnegative symmetric density and R1 = 1, so ||R||_{L2(pi)} <= 1 (Jensen).
pi is Theta-invariant, so Theta-odd f has pi(f) = 0 and ||Pf|| = (1 - eps)||Rf|| <= (1 - eps)||f||.
f -> psi f is unitary L2(pi) -> L2(dU) (psi is bounded above and below), commutes with Theta, and conjugates P to
T/lambda. So ||T|_{H_-}/lambda|| <= 1 - e^{-4 beta N}. The n-fold slab has top eigenvalue lambda^n and charged norm
at most (1 - e^{-4 beta N})^n since T preserves H_-. HOLDS, for SU(2), U(1) and Gamma.

**Scope paragraph (lines 193-201).** Correct. The bound comes only from strict positivity of a finite-volume kernel,
so it cannot distinguish the groups. The note says this.

**Verdict, item 3: HOLDS.**

## 4. Proposition 2, (B7)-(B13)

**(B9).** For |g - 1| <= r <= 1: |g - 1|^2 = 2 - 2 g_0, so g_0 >= 1 - r^2/2 >= 1/2 and
|y|^2 = 1 - g_0^2 <= r^2 (1 - r^2/4). So the y-radius is r sqrt(1 - r^2/4), in [sqrt3 r/2, r]. The normalized
surface density in the chart is 1/(2 pi^2 g_0), in [1/(2 pi^2), 1/pi^2]. Lower: (4 pi/3)(sqrt3 r/2)^3/(2 pi^2)
= sqrt3 r^3/(4 pi) >= r^3/(4 pi). Upper: (4 pi/3) r^3/pi^2 = 4 r^3/(3 pi). HOLDS.

**(B10).** Lower: for beta >= 1 take r = beta^{-1/2} <= 1; on B_r, beta x >= beta - 1/2; so
z >= e^{beta - 1/2} beta^{-3/2}/(4 pi). c_z = e^{-1/2}/(4 pi). Upper: with y = 1 - x the density is
(2/pi) sqrt(y(2 - y)) <= (2 sqrt2/pi) sqrt y; extend to [0, inf); int y^{1/2} e^{-beta y} dy = Gamma(3/2) beta^{-3/2}
= sqrt(pi)/(2 beta^{3/2}). So z <= e^beta (2 sqrt2/pi)(sqrt pi/2) beta^{-3/2} = sqrt(2/pi) e^beta beta^{-3/2}. HOLDS.
Pointwise k: x = 1 - |g - 1|^2/2, so k = (e^beta/z) e^{-beta |g-1|^2/2}, between C_z^{-1} and c_z^{-1} times
beta^{3/2} e^{-beta|g-1|^2/2} for beta >= 1. HOLDS.

**f and its norm.** r = 1/(8 sqrt beta) <= 1/8. B_r and -B_r are disjoint (|1 - (-1)| = 2 > 2r), so Omega and
Theta Omega are disjoint. f(Theta U) = -f(U), P_int = 1, so f is in H_-, and ||f||^2 = 2|Omega|. HOLDS.

**(B11).** For U, V in Omega: |U_e V_e^{-1} - 1| = |U_e - V_e| <= 2r. Bi-invariance gives |gh - 1| <= |g - 1| + |h - 1|,
so every holonomy of four links within r of 1 is within 4r of 1, and x(U_p) >= 1 - 8r^2. Hence
prod_e k >= C_z^{-b} beta^{3b/2} e^{-2 beta b r^2} = C_z^{-b} beta^{3b/2} e^{-2b/64}, and
A(U)A(V) >= e^{beta p} e^{-8 beta p r^2} = e^{beta p} e^{-8p/64}. Product: c_1 = C_z^{-b} exp{-(8p + 2b)/64}. HOLDS.

**(B12), the count behind e^{-6 beta}.** For U in Omega, V in Theta Omega, write V = Theta V' with V' in Omega.
At the three corner links U_e V_e^{-1} = -U_e V'^{-1}_e lies within 2r of -I. |g + 1|^2 = 2 + 2 g_0 <= 4 r^2 gives
x <= -1 + 2 r^2. So each corner factor is k <= c_z^{-1} beta^{3/2} e^{-2 beta} e^{2 beta r^2} = c_z^{-1} beta^{3/2} e^{-2 beta} e^{2/64}.
Other links: k <= c_z^{-1} beta^{3/2}. Plaquettes: A(V) = A(V') since Theta is a gauge transformation; the bound
uses only x <= 1, so A(U)A(V) <= e^{beta p}. The factor e^{-6 beta} is three corner links times 2 beta each (half-trace
-1 instead of +1 in the temporal-plaquette weight). No spatial plaquette contributes, since spatial holonomies
are Theta-invariant. The constant is c_2 = c_z^{-b} e^{6/64}. HOLDS.

**Rayleigh quotient.** <f, T_0 f> = 2[int_Omega int_Omega T_0 - int_Omega int_{Theta Omega} T_0] by Theta invariance and
symmetry. Divided by 2|Omega|: at least |Omega| beta^{3b/2} e^{beta p}(c_1 - c_2 e^{-6 beta}). HOLDS.
|Omega| beta^{3b/2} = (|B_r| beta^{3/2})^b >= (r^3 beta^{3/2}/(4 pi))^b = (1/(512 * 4 pi))^b = (2048 pi)^{-b}. HOLDS.
beta_B >= 1 with c_2 e^{-6 beta_B} <= c_1/2 exists (c_2/c_1 is a fixed finite number). Then
||T_0|_{H_-}|| >= c_3 e^{beta p}, c_3 = (2048 pi)^{-b} c_1/2. HOLDS.

**(B13).** Z_B/z^b = <1, T_0 1> = <A, K A> <= ||A||^2 = int A^2, because 0 <= K <= 1. Keep one plaquette weight,
bound p - 1 by e^beta; the holonomy of four independent Haar links is Haar, so the remaining integral is z.
So Z_B/z^b <= e^{beta(p-1)} z <= C_z e^{beta p} beta^{-3/2}. HOLDS.

**(B8).** ||T|_{H_-}||/Z_B = ||T_0|_{H_-}||/(Z_B/z^b) >= (c_3/C_z) beta^{3/2} for beta >= beta_B. The bound int A^2 was
used in (B13), so normalization by z^b int A^2 is excluded too. HOLDS.
Consistency check: (B21) below gives ||T|_{H_-}||/Z <= e^{6 beta}; no conflict with c_B beta^{3/2}.

**Verdict, item 4: HOLDS.** The e^{-6 beta} count is three corner links times 2 beta, not a plaquette count.

## 5. (B14)-(B20) and the degree-twelve paragraph (SU(2) unless stated)

**XX* versus X*X.** X = A K^{1/2} P_int. K^{1/2} = tensor of C^{1/2} = sum r_j^{1/2} Pi_j commutes with the gauge action
and with Theta; so X maps H to H and H_- to H_-. XX* = A K^{1/2} P_int K^{1/2} A = A K P_int A = T/z^b on H.
X*X = P_int K^{1/2} A^2 K^{1/2} P_int = L_0. On H_-, ||XX*|| = ||X||^2 = ||X*X||. No inverse of K is used. This is
SA's L = P C^{1/2} e^{-V} C^{1/2} P of (GL8), up to the constant e^{-beta} per bond. HOLDS.

**(B15).** Spin-network functions are joint eigenvectors of K^{1/2} with eigenvalue sqrt(c_a) and are fixed by P_int.
The link-wise Peter-Weyl projections commute with the gauge action and with Theta, so P_J H_- has a finite
orthonormal spin-network basis. <phi_a, M phi_b> = sigma^{-1} sqrt(c_a c_b) int conj(phi_a) phi_b A^2, and
A^2 = exp(beta sum_p x(U_p)). HOLDS.

**(B16)-(B17).** (GL4) gives r_j <= (beta/2)^{2j}/(2j+1)! <= t^n/(n+1)! with n = 2j and t = beta_+/2 (the bound
increases in beta). For j > J, n >= 2J + 1, so each such r_j is a term of eta_J. A state in ran Q_J has at least
one link with j_e > J; the other factors r_j are at most 1. So ||Q_J K Q_J|| <= eta_J and ||K^{1/2} Q_J||^2 <= eta_J.
Then D_J = sigma^{-1} Q_J K^{1/2} A^2 K^{1/2} Q_J >= 0 and ||D_J|| <= eta_J e^{beta p}/sigma <= d_J. HOLDS.
B_J: M >= 0, so |<u, M v>|^2 <= <u, Mu><v, Mv> <= a_J ||u||^2 d_J ||v||^2. HOLDS.
Tail bound: m = 2J + 1, first term t^m/(m+1)!, successive ratios t/(n+2) <= t/(m+2). HOLDS.

**(B18)-(B19).** <u+v, M(u+v)> <= a||u||^2 + 2 sqrt(a d)||u|| ||v|| + d||v||^2 = (sqrt a ||u|| + sqrt d ||v||)^2
<= (a + d)(||u||^2 + ||v||^2). Since M >= 0, ||M|| <= a_J + d_J. d_J is uniform on I. So (B19) gives
||T|_{H_-}||/(z^b sigma) <= q. HOLDS.

**(B20).** With v' = v - (I - D)^{-1} B* u:
<(u,v), (I - M)(u,v)> = <u, S u> + <v', (I - D) v'>, S = I - A_J - B_J (I - D_J)^{-1} B_J*.
If S >= s > 0 then the form is >= min(s, 1 - d_J)(||u||^2 + ||v'||^2), and (u, v) -> (u, v') is bounded with bounded
inverse; so I - M >= eps. Conversely set v' = 0: <u, S u> >= eps ||u||^2. S acts on the finite-dimensional P_J H_-,
so S > 0 iff S >= s > 0. Since M >= 0, ||M|| < 1 iff I - M >= eps. The equivalence HOLDS.

**Degree-twelve and U(1) paragraph.** h^k is Gamma-invariant in Sym^{12k} V (checked in `gap-tree-check-opus.md`,
(G17a)). On Gamma its matrix coefficient is constant, so Gamma convolution fixes it, while the SU(2) eigenvalue r_{6k}
is factorially small. On V tensor span(h^k), a copy of V, the Gamma eigenvalue is r_V^Gamma >= beta/(4 e^beta)
>= beta_-/(4 e^{beta_+}) ((G16) without its e < 3 step). For U(1), Sym^{12k} V has a zero-weight vector, V tensor it has
weight one, and the eigenvalue I_1/I_0 >= beta/(2 e^beta) >= beta_-/(2 e^{beta_+}). So the bound
||Q_J K Q_J|| <= eta_J, transplanted by SU(2) parent label, fails for both controls. HOLDS.
Remark: for U(1) the failure is not tied to degree twelve; every even degree has a zero-weight vector. The note's
"first extra invariant is precisely degree twelve" refers to Gamma only, which is right.

**Lines 433-436.** "A compression is a lower bound on the full operator norm": ||P_J M P_J|| <= ||M||. HOLDS.
**Wording correction.** "Proposition 2 prevents this scalar choice from working uniformly at large beta": Section 4
fixes no scalar; sigma is generic. Proposition 2 concerns sigma = Z_B/z^b on the single cube. Suggested text:
"With sigma = Z_B/z^b on the cube, Proposition 2 gives ||M|| >= c_B beta^{3/2}, so this choice fails at large beta
even with J = infinity."

**Verdict, item 5: HOLDS** (one wording correction at lines 434-435).

## 6. (B21)-(B27)

**(B21).** D M D = (a/Z)^{1/2} a^{-1/2} T a^{-1/2} (a/Z)^{1/2} = T/Z. Qf = Tf/a has Q1 = 1; relative to
nu = (a/Z) dU its density T(U,V) Z/(a(U) a(V)) is symmetric, so Q is reversible. sqrt(a/Z) Q (sqrt(a/Z))^{-1} =
a^{-1/2} T a^{-1/2}. Top eigenvalue 1. a(Theta U) = a(U). ||T|_{H_-}||/Z <= ||D||^2 q = (max a/Z) q. HOLDS.

**(B22).** Pure algebra; each interior factor is D_i D_{i-1}. HOLDS.

**(B23).** For a finite block with exterior eta, the one-link kernel at a link depends on eta only if one of its
plaquettes contains an exterior link; those links form D. So mu_B^{eta'} has the kernels of mu_B^eta off D. The
influence bounds of Lemma INF hold inside the block (fewer neighbours, the same two geometric facts in Z^4), so
alpha <= 9 beta/2 < 1 for beta < 2/9. Lemma DC gives (B23). HOLDS as an application.

**(B24).** 2 alpha^l/(1 - alpha) <= eps iff l >= log(2/(eps(1 - alpha)))/|log alpha|. HOLDS.
**Majorant remark.** The bulk majorant has constant row sums: C1 = alpha 1, so C^n 1 = alpha^n 1. Iterating gains
nothing when alpha >= 1. HOLDS, as a statement about that majorant.

**(B25).** T(U,V)/a(U): A(U) cancels; the V-density is prod_e w(U_e V_e^{-1}) exp{(beta/2) sum_p x(V_p)}. HOLDS.

**Influence counts.** Each cube edge lies in exactly two faces; the two faces share only that edge; each has three
other edges. So six other V-links. As a function of V_e, x(U_e V_e^{-1}) = U_e . V_e and x(V_p) = V_e . W_p with
unit staple W_p, so the conditional law is mu_F with F = beta U_e + (beta/2)(W_1 + W_2). Changing V_k in face p moves
W_p by exactly |V_k - V_k'|, so F moves by (beta/2)|dV_k|; Corollary V1 (valid for all F, per the vmf-lip check)
gives beta/8. Changing U_e moves F by beta |dU_e|: beta/4. Row sum 6 * beta/8 = 3 beta/4. HOLDS.

**Modified DC step.** For U, U' differing only at link j, the V-kernels differ only at V-site j. In (11) replace the
oscillation bound 2 delta_j(g) by |int g dgamma_j - int g dgamma'_j| <= delta_j(g) d_Lip(gamma_j, gamma'_j)
<= delta_j(g)(beta/4)|U_j - U'_j|. The rest of the proof of Lemma DC is unchanged (alpha_V = 3 beta/4 < 1 needs
beta < 4/3). So delta_j(Qf) <= (beta/4) sum_i delta_i(f) ((I - C_V)^{-1})_{ij}. Summing over j and using row sums
of (I - C_V)^{-1} <= 1/(1 - 3beta/4): Delta(Qf) <= (beta/4)/(1 - 3beta/4) Delta(f) = beta/(4 - 3 beta) Delta(f).
It is < 1 iff beta < 1. (B26) HOLDS.

**Spectral transfer to (B27).** Q is compact and self-adjoint on L2(nu), with real smooth kernel. An eigenfunction
with t != 0 is f = Qf/t, smooth, with finite Delta. |t| Delta(f) <= beta/(4 - 3beta) Delta(f). Delta(f) = 0 forces f
constant, and a nonzero Theta-odd function is not constant. Real kernel: take real eigenfunctions. On the odd
subspace the norm of the compact self-adjoint Q is the largest |t| of its eigenvalues there. The unitary
sqrt(a/Z) is Theta-even. So ||M|_{H_-}|| <= beta/(4 - 3beta) < 1 for 0 < beta < 1. HOLDS.

**The factor e^{6 beta} beta/(4 - 3 beta).** a(U) <= z^b e^{beta p/2} e^{beta p/2} int prod k = z^b e^{beta p}.
K >= Pi_0 (constants have eigenvalue 1, all other eigenvalues >= 0), so <A, KA> >= (int A)^2; Jensen and
E x(U_p) = 0 give int A >= 1. So max a/Z <= e^{6 beta}, and ||T|_{H_-}||/Z_B <= e^{6 beta} beta/(4 - 3 beta). HOLDS.
**Correction (statement too weak, not wrong).** "It exceeds one near beta = 1" is true but incomplete.
Both factors increase in beta. At beta = 2/5 the factor is e^{12/5}/7 > 1, since e^2 > 7. So it exceeds one on all of
[2/5, 1). At beta = 1/4 it is e^{3/2}/13 < 4.49/13 < 1. So for 0 < beta <= 1/4 this route DOES prove
||T|_{H_-}||/Z_B < 1 on the cube with the original free-boundary scalar Z = Z_B. GUIDE (hand arithmetic): the
crossing is near beta = 0.35. The sentence "this attempt does not close the scalar estimate even where the
normalized conditional map contracts" holds only for beta above that crossing. This does not affect the
order-one conclusions; it does show that Proposition 2 (large beta) and (B27) (small beta) bracket a crossover.

**Verdict, item 6: HOLDS AFTER CORRECTION** (the e^{6 beta} sentence: exceeds one for beta >= 2/5, below one for
beta <= 1/4).

## 7. (B28)-(B31) and the passage to (V)

**(B29) from (GL10).** SA (GL10) reads |Tr(Xi_1 L ... Xi_s L)| <= prod ||Xi_j L||_{S_s} <= ||L||_{S_s}^s = Tr L^s, with
||Xi_j|| <= 1. The first step is generalized Schatten-Holder, valid for any bounded operators; the second is
||XL||_{S_t} <= ||X|| ||L||_{S_t}; the equality needs only L >= 0 trace class. Scaling X_j by ||X_j|| gives (B29) for
arbitrary bounded, signed, non-self-adjoint X_j. SA's pointwise positivity of k_Xi is used only to define phi_Xi
(a logarithm) and to make the modified integral positive (outline lines after (GL10)); the trace inequality does
not use it. L_m = P C^{1/2} e^{-V_m} C^{1/2} P is >= 0 for a spatial twist (e^{-V_m} is a positive multiplication)
and trace class (C^{1/2} is Hilbert-Schmidt by factorial decay). HOLDS, under the stated hypothesis (B28).
Tensor products: ||X tensor Y|| = ||X|| ||Y||. HOLDS. The caveat on overlapping exposures is correct.

**Count of connected sets.** A link of the 4D lattice lies in 6 plaquettes; a plaquette has 4 links; two distinct
plaquettes share at most one link. So a plaquette has at most 4 * 5 = 20 link-neighbours. A depth-first traversal
of a spanning tree of a connected set of A plaquettes, from a fixed root, makes 2(A - 1) moves, each to one of at
most 20 neighbours (a return to the parent is also such a move). The canonical walk determines the set. So at
most 20^{2(A-1)} sets per root, at most N_p 20^{2(A-1)} sets of area A. HOLDS.

**Area.** A connected gamma containing a closed S with h(S)_{mu nu} = 1 has A >= |S| >= n_mu n_nu >= a^2 by Lemma M
of `gap-kappa-order.md` (sides a, a, c, d >= a). HOLDS.

**(B30)-(B31).** sum_{A >= a^2} N_p 400^{A-1} h^A q^{A/D - 1} = (N_p/(400 q)) sum_{A >= a^2} (400 h q^{1/D})^A
= (N_p/(400 q)) rho^{a^2}/(1 - rho). HOLDS.

**Passage to (V).** For 0 <= u <= 1/2, -log(1 - u) <= u/(1 - u) <= 2u. N_p = 6 a^2 c d <= 24 a^4 since c, d <= 2a. So
F_m(v) <= (48 a^4/(400 q (1 - rho))) e^{-a^2 log(1/rho)} once the right side of (B31) is <= 1/2: this is (V) with
sigma = log(1/rho), p = 4. Finitely many small a: for fixed a there are finitely many (c, d, m, v), each F is finite
and continuous on compact I, so a prefactor absorbs them. (V) gives the large-a (FQ) because e^{-sigma a^2} beats
K(a) eta_*^{a/2}. HOLDS, as a conditional composition. Every hypothesis (B28), h, q, D is named as a hypothesis;
the OPEN paragraph (lines 637-648) states that none is constructed.

**Verdict, item 7: HOLDS** (conditional, as labelled).

## 8. (B32)-(B34)

**(B32).** r^{A_1} ... r^{A_s} = r^{A} when sum A_i = A. The per-patch reading uses Lemma T of `gap-kappa-order.md`
(each disc step gives 1/4; the torus closing gives 4^{-A} overall), checked in `gap-tree-check-opus.md` item 3.
HOLDS (the identity itself is trivial).

**r_* < 1 and the plane count.** r_{1/2} = I_2/I_1 < 1 termwise and continuous, so its maximum on compact I is < 1.
A flat (mu, nu)-plane is fixed by its two other coordinates: at most c d <= 4 a^2 choices. Each term is 2 r^A with
A >= a^2. Six orientations: 6 * 4a^2 * 2 r_*^{a^2} = 48 a^2 r_*^{a^2}. HOLDS. The caveat that this is not divided
by the full Z^m is correct.

**Patch area on fixed I.** r_*^A <= q_0 iff A >= log(1/q_0)/log(1/r_*). HOLDS.

**(B33).** r_{1/2} = (1/2) int k chi_{1/2} = int k x = E_beta x. Under k the law of y = 1 - x has density proportional
to e^{-beta y} y^{1/2} sqrt(2 - y) on [0, 2]: the Gamma(3/2, beta) density times h(y) = sqrt((2 - y)_+), which
decreases. E_beta y = E[Y h(Y)]/E[h(Y)]. With Y' an independent copy, 2 Cov(Y, h(Y)) = E[(Y - Y')(h(Y) - h(Y'))] <= 0,
since each product is <= 0. So E_beta y <= E Y = (3/2)/beta. HOLDS.

**(B34).** For beta >= 3, u = 3/(2 beta) <= 1/2, so -log r_{1/2} <= -log(1 - u) <= 2u = 3/beta. r^A <= q_0 gives
A >= log(1/q_0)/(-log r) >= (beta/3) log(1/q_0). Square patch: l >= sqrt(beta log(1/q_0)/3). HOLDS. The scope
(necessary only for this payment mechanism) is stated correctly.

**Verdict, item 8: HOLDS.**

## 9. Is the RESULT line fair?

Each clause matches a checked statement. "Exact resummed charged Wilson slab": (B2)-(B4), with side time links fixed
to the identity; the body says this boundary data must be restored (lines 640-641). "Shared Perron-normalized
contraction": (B5). "Conditional cube contraction for beta < 1": (B27), for the normalized map M, not for Z.
"Free-boundary-scalar obstruction growing as c_B beta^{3/2}": (B8). "Low-spin matrix plus controlled remainder":
(B15)-(B19). "Fails at degree twelve for Gamma and at weight one for U(1)": item 5. The OPEN items and the
disclaimers (no fixed-block no-go, no order-one (FQ) or (V)) are accurate.
It understates one thing: with (B21), (B27) gives ||T|_{H_-}||/Z_B <= e^{6 beta} beta/(4 - 3 beta) < 1 for
0 < beta <= 1/4 on the cube, with the original free-boundary scalar. This is a strong-coupling statement and does
not change the open order-one items. Verdict: FAIR, with that omission.

## 10. Verdict table

| Item | Statement | Verdict |
|---|---|---|
| 1 | (B2)-(B3) kernel from the Wilson integral, half action at ends, side time links = 1 | HOLDS |
| 1 | sewing (full action once per interior layer) | HOLDS |
| 1 | Theta, H_-, T preserves H_- | HOLDS |
| 1 | open Wilson line in H_- | HOLDS |
| 2 | absolute convergence of the resummation (SU(2), U(1), Gamma) | HOLDS |
| 2 | T >= 0 for all three groups | HOLDS |
| 3 | m = e^{-beta N}, M = e^{beta N}, N = b + p | HOLDS |
| 3 | Perron eigenfunction, simplicity, Theta-even | HOLDS |
| 3 | psi <= M I/lambda, lambda >= m I^2, eps = m^2/M^2 | HOLDS |
| 3 | (B5): 1 - e^{-4 beta N} | HOLDS |
| 4 | (B9), (B10) with c_z, C_z | HOLDS |
| 4 | (B11) c_1; (B12) c_2 and e^{-6 beta} (3 corner links x 2 beta) | HOLDS |
| 4 | Rayleigh bound, (2048 pi)^{-b}, (B13), (B8) | HOLDS |
| 5 | XX* versus X*X; (B15) | HOLDS |
| 5 | (B16)-(B18) with Cauchy-Schwarz for M >= 0; (B19) | HOLDS |
| 5 | (B20) Schur-complement equivalence | HOLDS |
| 5 | degree-twelve (Gamma) and weight-one (U(1)) failure | HOLDS |
| 5 | lines 434-435 "Proposition 2 prevents this scalar choice" | HOLDS AFTER CORRECTION (name sigma = Z_B/z^b on the cube) |
| 6 | (B21), (B22) | HOLDS |
| 6 | (B23), (B24), majorant remark | HOLDS |
| 6 | (B25), influences beta/8, beta/4, row sum 3 beta/4 | HOLDS |
| 6 | modified DC step, (B26) beta/(4 - 3 beta) | HOLDS |
| 6 | spectral transfer to (B27) | HOLDS |
| 6 | max a/Z <= e^{6 beta}; factor e^{6 beta} beta/(4 - 3 beta) | HOLDS AFTER CORRECTION (exceeds 1 for beta >= 2/5, below 1 for beta <= 1/4) |
| 7 | (B29) from (GL10) for signed X | HOLDS |
| 7 | 20^{2(A-1)} count; A >= a^2 | HOLDS |
| 7 | (B30)-(B31), passage to (V) and large-a (FQ) | HOLDS (conditional, as labelled) |
| 8 | (B32), 48 a^2 r_*^{a^2} | HOLDS |
| 8 | (B33) via gamma comparison and covariance sign; (B34) | HOLDS |
| 9 | RESULT line | FAIR (omits the beta <= 1/4 cube contraction with Z_B) |

Nothing FAILS.

Not checked: the repo-search and source-reading claims (lines 1-31, 41-52, 732-739); SA outline lines outside
2195-2393 (31860-31884, CA-I 2700-2716); the gap-ext consumer beyond lines 78-128.

RESULT: Every PROVED step of library/gap-block-astra.md holds by hand and nothing fails; two corrections: the cube multiplier e^{6 beta} beta/(4 - 3 beta) exceeds one for all beta >= 2/5 but is below one for beta <= 1/4 (so (B21)+(B27) do give a free-boundary-scalar cube contraction there, which the note and RESULT omit), and lines 434-435 should name the scalar sigma = Z_B/z^b to which Proposition 2 applies.
