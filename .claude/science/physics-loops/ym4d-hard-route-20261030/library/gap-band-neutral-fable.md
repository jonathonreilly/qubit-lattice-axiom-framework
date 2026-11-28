lead: anthropic/claude-fable-5-2/high laptop-subagent

# gap-band-neutral-fable (row 1574) — working file

## Plan (written before any reading; refined in step 0)

1. Read FINISH.md rule sections (lines 1-84, 299-360), GOAL.md, and the row 1574 brief.
2. Read check 1556 section (v), and checks 1570, 1571, 1572 in full.
3. Restate the row's target and tests in this file (step 0).
4. Work one candidate / one test / one lemma per step; append each result before thinking further.
5. Before calling a statement new: grep library/open-core.md, library/open-registry.md, FINISH rows.
6. End with one RESULT: line.

Constraints: no edits in the lane checkout, no commit/claim/push/post; do not read row 1573's output file;
labels PROVED / ARGUED / GUESSED / ON FILE with anchors; no numerics unless memory_pressure >= 50% free.

## Step 0. Sources read and the target restated

Read: FINISH.md lines 1-84 and 299-360 (rules; "Equivalent is not progress"; computation only as formal proof),
GOAL.md, row 1574 brief (same text as row 1573), check 1556 sections (iv)-(v)
(library/gap-mech-direction4-check-astra62.md lines 36-111), checks 1570, 1571, 1572 in full.

ON FILE (anchors as read):
- Cut rotation R_s (check 1556 (v), lines 60-80): axis a_x = Im Q_x/|Im Q_x| from the untouched 23-plaquette,
  (R_s U)_{x,1} = exp(s a_x) U_{x,1}; Haar-preserving, gauge-covariant, centre-commuting; R_pi = C_1 a.e.
  H_z(s;v) = int K_v(A, C_z R_s A) dA interpolates Z^z(v) -> Z^{z+e_1}(v).
- Four corners (1556 (v) line ~99; check 1570 "four corners"): int_0^pi int_0^pi d_s d_t log K_v(R_s X, R_t Y) = 2 log K_v(X,Y)/K_v(X,C_1 Y).
- BC => (N-flux) (check 1570): charged fraction f_v = 1 - Tr(P_0 T^{2v})/Tr(T^{2v}) = O(v^-eps).
- Blindness (check 1570 "BC can hold with arbitrarily poor neutral purity"; check 1572 Prop 1.2(1); check 1571 F (g4)):
  tensoring with a neutral factor leaves the cut row unchanged and multiplies purity by the spectator purity.
- Check 1570 two-period line: P_K / P_full = a_{2u}/a_u^2 with a_t = Z_+(t)/Z^0(t). So the object the cut rotation does NOT read is
  P_full = Z^0(2u)/Z^0(u)^2 (untwisted two-period ratio), "the common neutral normalization across the two periods".

Target of this row: a structure that reads the neutral two-period ratio
  P_K = Z_+(2u)/Z_+(u)^2  (or P_full = Tr T^{2u}/(Tr T^u)^2)
the way R_s reads Z^{z+e_1}/Z^z: a deterministic / circle-action interpolation whose endpoints are
"one period-2u torus" and "two period-u tori" (or a swap realized as a connected-group motion), OR a proof that
no map of a stated class exists. Then tests of row 1553 section 1.5 as corrected by check 1556 ((g4) in particular),
then the first lemma, or one precise lemma attacked three ways.

Refined plan:
 S1. Read row 1553 section 1.5 tests + check 1556 (iii) corrections; row 1529 section 3 + check 1539 (swap in Sp(2)); k2-tool-design 3.1.
 S2. Grep registry / open-core / FINISH rows for: swap, replica, two-period, TWO-PER, purity interpolation, Hellinger (row 1526).
 S3. Write the exact algebraic frame: Tr(T^{2u}) = Tr(SWAP . T^u (x) T^u). The swap is the "twist" for the neutral data.
 S4. Candidate A: connected path from 1 to SWAP in U(H(x)H) commuting with what? Test: class statement (no-go or construction).
 S5. Candidate B: geometric circle of link maps on the doubled system (two slices A, B) reaching the swap at half-turn.
 S6. Tests (g1)-(g6), then first lemma.

## Step 1. Prior structure on file for the neutral data (read; ON FILE)

- Tests: library/gap-mech-direction4-fable.md 1.3-1.5 ((g1)-(g6), Lemma ALG), corrected by check 1556 (iii)-(iv)
  (library/gap-mech-direction4-check-astra62.md lines 26-52): the spectator test lives on a class that admits the factor;
  "fires" means the specified failure mechanism repeats at the gapped twin.
- The swap as a twist: Tr T^{2u} = Tr(SWAP . T^u (x) T^u). ON FILE: rows 1115-1122; row 1131 (two sheets);
  route COVER / Lemma COV, library/gap-band-fresh-fable.md 2.1 and 4.2 (verdict: identity, rewriting of the seed);
  library/gap-laptop-solve3-fable.md item 5 ("the swap is the outer twist of Pin(4) ... not in the identity component,
  so the soft twist argument does not apply to it").
- Row 1529 (library/gap-mech-attack-fable.md section 3): swap made inner in Sp(2) with a unit 5-vector field; Lemma INN:
  R(beta,0)=1, R(beta,inf)=Pi=Z^0(2u)/Z^0(u)^2. Check 1539 (library/gap-mech-attack-fable-check-astra62.md line 17):
  "The global spin inversion is outside SO(5), while J realizes the exchange on the stabilizer." So the twist whose
  ratio is the purity is n -> -n, outside the identity component; the interpolation there is in a coupling kappa
  (a different model at each kappa), not a motion of boundary data.
- Registry: TWO-PER (library/open-registry.md line 1020) = relative transport of the purity along the coupling; R11, R12.
  No entry owns "a deterministic circle action on the doubled slice whose half-turn is the replica swap".
  (greps for swap/replica in library/open-registry.md and library/open-core.md: no hit other than these.)

Frame fixed for this row (all identities; ON FILE in substance, Lemma COV (a),(c)):
  Doubled slice space XX = X x X, X = SU(2)^{links of (Z/n)^3}; sigma(A,B) = (B,A).
  M = T^u or P_0 T^u (positive operators with positive kernels K_u, K^+_u = (1/8) sum_z K_u(., C_z .)).
  Tr(sigma . M (x) M) = Tr(M^2),   Tr(M (x) M) = (Tr M)^2.
  So P_full = Z^0(2u)/Z^0(u)^2 and P_K = Z_+(2u)/Z_+(u)^2 are the sigma-twist ratios of the doubled system.
  The swap is a 0-form Z_2 of the doubled system; the centre is a 1-form Z_2. The cut rotation connects 1 to the
  centre flip inside the Haar-preserving maps. The question of this row: does the same exist for sigma?

## Step 2. Candidate A: the literal analogue of the cut rotation (one link at a time). REFUTED (Proposition N1, PROVED)

Greps before calling it new: "orientation-reversing", "local degree", "circle action" with "swap" or "replica" in
library/gap-*.md, library/open-registry.md, library/open-core.md, FINISH.md: no match for a circle action that reaches
the replica swap, and none for this obstruction. Nearest on file: library/gap-laptop-solve3-fable.md item 5 (the swap is
outer in Pin(4)); that is a statement about the isometry group, not about Haar-preserving maps.

Class C1 (the class of check 1556 (v)). A flow phi_s on an open set U of full Haar measure in a doubled block space
B x B, B = G^j (j links, G = SU(2) or U(1)), continuous in (s, y) on R x U, with phi_0 = 1 and phi_{s+t} = phi_s phi_t.
The flow may depend on frozen parameters (links it does not move). The cut rotation R_s of check 1556 (v) is of this
kind with j = 1: it moves one link by exp(s a_x), a_x read from an untouched plaquette, and it is continuous off the
closed null set {Q_x = +-1}.

**Proposition N1 (PROVED).** Let N = dim B = j dim G be odd. Then no flow of class C1 has phi_{s_0} = sigma almost
everywhere on U, for any s_0, where sigma(p, q) = (q, p).

Proof. (1) Each phi_s is a homeomorphism of U, with inverse phi_{-s}. (2) If phi_{s_0} = sigma a.e. on U, then
everywhere on U, because both sides are continuous and Haar has full support. (3) The local degree of a homeomorphism
between open sets of an oriented manifold is +1 or -1 and is locally constant in the point. (4) It is constant in s:
fix y, a small closed coordinate ball D at y, and s. The compact set phi_s(boundary D) has positive distance from
z = phi_s(y). By uniform continuity on [s - d, s + d] x D, phi_{s'}(boundary D) avoids z for s' near s. So the degree
over z of phi_{s'} restricted to (D, boundary D) is constant for s' near s. It equals the local degree of phi_{s'} at
the one point of D over z, hence, by (3), at y. So s -> deg_y(phi_s) is locally constant, and it is +1 at s = 0.
(5) sigma is a diffeomorphism of B x B, and in product charts its differential exchanges two blocks of size N. That
is a product of N transpositions, so its local degree is (-1)^N = -1. Contradiction. QED

Corollaries (PROVED).
 (a) One link: N = 3 for SU(2), N = 1 for U(1). So no single-link rotation with frozen axes reaches the swap. The
     construction of check 1556 (v) has no swap analogue in its own form. A product over links of such maps does
     not exist either, since each factor would be such a flow for each value of its frozen parameters.
 (b) Any block with an odd number of links is excluded (for example the three links at one site).
 (c) Whole slice: N = 9 n^3 for (Z/n)^3. For n odd no flow of class C1 on X x X reaches sigma, local or not.
     For n even (the lane has n in 1024 N) the parity obstruction is absent.
 (d) Contrast: the centre flip a -> -a on S^3 has degree +1, so the cut rotation meets no such obstruction.
Remark (PROVED, one line). No flow continuous on all of X x X reaches sigma for any n: sigma exchanges the classes of
the two S^3 factors of a link in H_3(X x X; Z), so it is not homotopic to the identity. Every swap rotation has a
non-empty singular set.
Remark (scope). If continuity in y is dropped (Borel flows), existence is trivial and empty: sigma is a free
involution off the diagonal on a non-atomic space, so it sits in a measurable circle action. Such a flow has no local
generator and gives no covariance calculus. So C1 is the right class.

Result of step 2: the minimal block is two links. Next: build it.

## Step 3. Candidate B: a pair rotation. CONSTRUCTED (Lemmas CO, S2, Proposition ROT; PROVED by hand, unchecked)

Notation: unit quaternions for SU(2); normalized Haar; Rot(k, s) n = e^{sk/2} n e^{-sk/2} for unit imaginary k, n.

**Lemma CO (coordinates of one doubled link; PROVED).** For (a, b) in SU(2)^2 with b != +-a write
  c = a^{-1} b = e^{theta n},  theta in (0, pi),  n in S^2,   m = a e^{theta n / 2}.
Then a = m e^{-theta n/2}, b = m e^{theta n/2}. The map (a, b) -> (m, theta, n) is a homeomorphism from {b != +-a}
onto S^3 x (0, pi) x S^2. It carries Haar x Haar to  dm x (2/pi) sin^2(theta) dtheta x (uniform on S^2).
The swap acts by (m, theta, n) -> (m, theta, -n).
Proof. b = a c and left invariance give da db = da dc. For fixed c, a -> a c^{1/2} is a right translation, so
da dc = dm dc. Haar on S^3 in polar form is (2/pi) sin^2(theta) dtheta x dn/(4 pi). The swap sends c to c^{-1} = e^{theta(-n)}
and m to b e^{-theta n/2} = m. QED
Mirror form (tail-based): c' = b a^{-1} = e^{theta n'}, m' = e^{theta n'/2} a, a = e^{-theta n'/2} m', b = e^{theta n'/2} m'; same measure.

**Lemma S2 (PROVED).** On V = {(n_1, n_2) in S^2 x S^2 : n_1 x n_2 != 0} put k = n_1 x n_2 / |n_1 x n_2| and
  F_s(n_1, n_2) = (Rot(k, s) n_1, Rot(k, s) n_2).
Then F is a continuous circle action on V (F_0 = 1, F_s F_t = F_{s+t}, F_{2 pi} = 1), it preserves uniform x uniform,
and F_pi(n_1, n_2) = (-n_1, -n_2).
Proof. Rot(k, s) fixes k, so the pair (Rot n_1, Rot n_2) has the same k; this gives the group law. Both n_i are
orthogonal to k, so the half-turn negates them. Measure: g -> (g e_1, g(cos psi e_1 + sin psi e_2)) is a bijection
from SO(3) x (0, pi) onto V with g e_3 = k. The measure on V is invariant under the diagonal SO(3), so in these
coordinates it is Haar(g) x (1/2) sin psi dpsi. F_s is g -> g Rot(e_3, s), a right translation, and psi is fixed. QED
(N1 is consistent: the antipodal map of one S^2 reverses orientation; of S^2 x S^2 it does not.)

**Pairing.** n is even. Pair the link e_1 = (x, x + i^) with e_2 = (x + i^, x + 2 i^) for x_i even, i = 1, 2, 3.
The two links share the vertex y = x + i^: e_1 ends there, e_2 starts there. Each link is in exactly one pair.
N_p = 3 n^3 / 2 pairs.

**Definition (pair rotation).** For Y = (A, B) and a pair p = (e_1, e_2): a_i = A_{e_i}, b_i = B_{e_i}. Use Lemma CO for
e_1 (head-based: c_1 = a_1^{-1} b_1 = e^{theta_1 n_1}, m_1) and its mirror for e_2 (tail-based: c_2 = b_2 a_2^{-1} = e^{theta_2 n_2}, m_2).
Both n_1 and n_2 are adjoint vectors at y. With k_p = n_1 x n_2 / |n_1 x n_2|, the map R^p_s moves (n_1, n_2) by F_s and fixes
m_1, m_2, theta_1, theta_2 and every other link. In link variables, with r = e^{s k_p / 2}:
  a_1 -> w_1 a_1 r^{-1},  b_1 -> w_1 b_1 r^{-1},  w_1 = m_1 r m_1^{-1};
  a_2 -> r a_2 w_2^{-1},  b_2 -> r b_2 w_2^{-1},  w_2 = m_2^{-1} r m_2.
(Check: m_1 r e^{-theta_1 n_1/2} r^{-1} = (m_1 r m_1^{-1}) (m_1 e^{-theta_1 n_1/2}) r^{-1}.) So both replicas receive the same three group
elements: r at the middle vertex, and its transports w_1, w_2 through the midpoints at the outer ends, applied to the
two links of the pair only. R_s = product over pairs of R^p_s.

**Proposition ROT (PROVED).** Let U be the set where every c_e != +-1 and every pair has n_1 x n_2 != 0. Then:
 (i)  U is open, of full Haar measure, invariant; R_s is a circle action on U, continuous in (s, Y), with real-analytic orbits.
 (ii) R_s preserves product Haar on X x X.
 (iii) R_pi = sigma on U.
 (iv) R_s commutes with sigma, with the diagonal gauge group (g, g), and with the diagonal centre flips (C_z, C_z).
 (v)  Speed: |d/ds a_i| = |d/ds b_i| = sin(theta_i / 2) <= 1.
 (vi) R_s does not commute with the full gauge group G x G or with one-replica centre flips (C_z, 1).
Proof. (i) The factors act on disjoint link sets and read no other link, so they commute. Lemma S2 gives the rest.
(ii) Lemma CO turns Haar on the four links of a pair into a product in which (n_1, n_2) is uniform x uniform; Lemma S2.
(iii) F_pi negates n_1, n_2; by Lemma CO this is the swap on both links. (iv) sigma negates both n_i and fixes k_p, m_i, theta_i.
Under g: a_1 -> g_x a_1 g_y^{-1}, so c_1 -> g_y c_1 g_y^{-1}, m_1 -> g_x m_1 g_y^{-1}; a_2 -> g_y a_2 g_z^{-1}, so c_2 -> g_y c_2 g_y^{-1},
m_2 -> g_y m_2 g_z^{-1}; n_1, n_2, k_p turn by Ad(g_y), and the formulas above are covariant. Under a common sign on a link, c is
unchanged and m changes sign. (v) a_1(s) = m_1 e^{-theta_1 n_1(s)/2} and |d n_1/ds| = |k x n_1| = 1. (vi) Under b_1 -> -b_1:
(theta_1, n_1, m_1, k_p) -> (pi - theta_1, -n_1, -m_1 n_1, -k_p), and the new orbit is a_1'(s) = m_1 e^{s k_p} e^{-theta_1 nhat/2} with
nhat = Rot(k_p, -s) n_1. The flip does not touch a_1, so commutation would need a_1'(s) = a_1(s) = m_1 e^{-theta_1 n_1(s)/2}. The real parts
of m_1^{-1} times these are cos(s) cos(theta_1/2) and cos(theta_1/2) (nhat is orthogonal to k_p), so they differ unless cos s = 1. QED

U(1) version (PROVED, same proof). One doubled link: relative angle phi = b - a in (-pi, pi), midpoint a + phi/2; the swap
is phi -> -phi. For a pair, move (phi_1, phi_2) along the square contours max(|phi_1|, |phi_2|) = rho at constant arc speed
with period 2 pi. This preserves Lebesgue measure (the contours are at uniform normal distance) and its half-turn is
(phi_1, phi_2) -> (-phi_1, -phi_2). It is continuous off the origin.

**The interpolation.** Let M be T^u or P_0 T^u, with positive kernel k_M, and KK(Y', Y) = k_M(A', A) k_M(B', B). Put
  I_M(s) = integral of KK(Y, R_s Y) dY = Tr(U_s . M (x) M),   U_s the Koopman unitary of R_s on L^2(X x X).
Then I_M(0) = (Tr M)^2 and I_M(pi) = Tr(M^2). So for M = T^u: I(0) = Z^0(u)^2, I(pi) = Z^0(2u); for M = P_0 T^u:
I(0) = Z_+(u)^2, I(pi) = Z_+(2u). The endpoints are two period-u tori and one period-2u torus. (PROVED: (ii), (iii).)

**Lemma W (weights; PROVED).** U_s = sum over integers k of e^{iks} Pi_k (a unitary circle action). So
  I_M(s) = sum_k w_k e^{iks},  w_k = Tr(Pi_k (M (x) M) Pi_k) >= 0,   purity = I_M(pi)/I_M(0) = sum_k (-1)^k w_k / sum_k w_k.
The purity is the parity of an integer "replica charge" k in the doubled thermal state. R_s is not a symmetry of
T (x) T, so k is not conserved and its law is broad: the second moment of k is extensive (ARGUED: each pair generator
acts on the vacuum pair). Hence no moment bound in k gives the parity; a two-end argument is needed (step 4).

What is new against the file (greps in step 2): the obstruction N1, the pair rotation, and Lemma W.
What is not new: the swap twist identity (Lemma COV, rows 1115-1131, 1402, 1529).

## Step 4. The calculus of check 1556 (v) for the pair rotation (Theorem SW, Lemma CORNER; PROVED by hand, unchecked)

Setting. v >= 3, M_v = T^v (full form) or P_0 T^v (neutral form), k_v its kernel: K_v, or K^+_v = (1/8) sum_z K_v(., C_z .).
Both kernels are positive, symmetric and smooth. KK_v(Y', Y) = k_v(A', A) k_v(B', B). Sewing measure and masses:
  dmu(Y', Y) = KK_v(Y', Y)^2 dY' dY / Z_1,   Z_1 = (Tr M_v^2)^2,   Z_sigma = integral KK_v(Y', Y) KK_v(Y, sigma Y') = Tr M_v^4.
  Purity at period 2v:  P(2v) = Z_sigma / Z_1 = Tr(M_{2v}^2) / (Tr M_{2v})^2.   With 2v = u this is Pi (full) or P_K (neutral).
D_p = generator of R^p_s (a bounded vector field on U). Mixed terms, with (1), (2) the first and second argument:
  h_pq(Y', Y) = (D_p^(1) D_q^(2) log KK_v)(Y', Y).
  L_sigma(v) = sup over s, t in [0, pi] and over p of  sum_q E_mu | h_pq(R_s Y', R_t Y) |.

**Theorem SW (PROVED).**
 (a) Four corners. For Y', Y in U:  integral over [0, pi]^2 of sum_{p,q} h_pq(R_s Y', R_t Y) ds dt = 2 log [ KK_v(Y', Y) / KK_v(Y', sigma Y) ].
 (b) 0 <= -log P(2v) <= (1/2) integral over [0, pi]^2 of E_mu sum_{p,q} h_pq(R_s Y', R_t Y) ds dt <= (pi^2 / 2) N_p L_sigma(v),  N_p = 3 n^3 / 2.
 (c) At fixed ends, h_pq is a connected covariance of two local scores, one on each end, and |h_pq| <= 8 beta^2.
     Full form: h_pq = Cov_A(O^A_p, O^A_q) + Cov_B(O^B_p, O^B_q), each in the pinned Wilson cylinder of one replica, with
     O_p = beta sum over the two links e of p of d/ds Re(temporal plaquette on e), |O_p| <= beta (sin(theta_1/2) + sin(theta_2/2)) <= 2 beta.
 (d) Consumer. At n = 1024 v (so u = 2v = n/512):  -log P <= (3 pi^2 / 4) 1024^3 v^3 L_sigma(v). So
     L_sigma(v) <= C v^{-3-eps} gives 1 - P = O(v^{-eps}), and (3 pi^2/4) n^3 L_sigma(u/2) <= log(625/457) gives P >= 457/625.
     Full form with Lemma PER (row 1529, checked in 1539), or neutral form with Fact PUR (library/gap-k2-tool-design-fable.md 3.1),
     then gives the seed quantity s(u) <= 4/21 at that coupling and size.
Proof. (a) F(s, t) = log KK_v(R_s Y', R_t Y) is C^2 (smooth positive kernel, analytic orbits). sigma-invariance
KK(sigma Y', sigma Y) = KK(Y', Y) and R_pi = sigma give F(pi, pi) = F(0, 0) and F(pi, 0) = log KK(sigma Y', Y) = log KK(Y', sigma Y) = F(0, pi).
The fundamental theorem of calculus on the square gives the claim; d/ds = sum_p D_p because the pair flows commute.
(b) By symmetry and sigma-invariance, KK_v(Y, sigma Y') = KK_v(Y', sigma Y), so P = E_mu[rho], rho = KK_v(Y', sigma Y)/KK_v(Y', Y).
Jensen: log P >= E_mu log rho = -(1/2) E_mu of the integral in (a). Fubini holds since |h_pq| is bounded. P <= 1 because
Tr(M^2) <= (Tr M)^2 for a positive trace-class M. (c) log k_v(X, Y) is a sum of the two end terms beta W/2 and the log of
the interior integral, and X enters the interior only through the temporal plaquettes of the first slab (Lemma 1.1 of
row 1568, checked in 1572 Step 2; v >= 2 separates the ends). The velocity of each moved link is at most sin(theta/2)
(Proposition ROT (v)). For the neutral kernel the law also carries the twist label z, and the same formula is a
covariance in the joint law of (z, interior). (d) Arithmetic. QED
Remark. Only the signed mean in (b) is needed. L_sigma is the absolute form, as in lemma (B) of 1556 (v).

**Lemma CORNER (PROVED; the swap form of (3) of row 1565, checked in 1571 A1).** With MM = M_v (x) M_v and G = -i sum_p D_p
(self-adjoint, integer spectrum):
  E_mu sum_{p,q} h_pq(Y', Y) = 2 Tr(G MM G MM) / Tr(MM^2) = 2 sum_{j,k} j k |Pi_j MM Pi_k|_HS^2 / |MM|_HS^2 >= 0.
Proof. KK^2 D^(1) D^(2) log KK = KK D^(1) D^(2) KK - (D^(1) KK)(D^(2) KK). D = sum_p D_p is real and skew for Haar (the flow preserves
Haar). Integrate by parts in the first argument: the integral of the first term is minus that of the second. The kernel of
D MM is D^(1) KK and the kernel of MM D is -D^(2) KK, so the integral of (D^(1) KK)(D^(2) KK) is Tr((D MM)^2) = -Tr(G MM G MM).
Tr(G MM G MM) = |MM^{1/2} G MM^{1/2}|_HS^2. QED
Reading. Put weight |Pi_j MM Pi_k|^2/|MM|^2 on (j, k) in Z^2: the replica charges at the two ends. Then
P = E(-1)^j = E(-1)^k, j = k mod 2 almost surely, and the unrotated corner of (b) is 2 E[jk]. So (b) implies the
necessary test  E[jk] <= N_p L_sigma / 2.  For real eigenfunctions the diagonal matrix elements of G vanish, so in spectral
form E[jk] = sum over a != b of Lambda_a Lambda_b |<a|G|b>|^2 / sum Lambda_a^2, over eigenpairs of MM.

Count against the cut rotation (ARGUED). The centre is a 1-form Z_2: its defect is a cut of n^2 links, and (B) asks the
row power v^{-2-eps}. The swap is a 0-form Z_2: its defect is the whole slice, 3 n^3 / 2 pairs, and (SW) asks v^{-3-eps}.

## Step 5. Tests of row 1553 section 1.5, as corrected by check 1556 (verdicts with grades)

Candidate fact F = (SW), full form: there are C and eps > 0 with L_sigma(v) <= C v^{-3-eps} for every coupling in the stated
range, every n in 1024 N and v = n/1024 >= 3 (pair rotation of step 3, M_v = T^v). In d dimensions: N_p = (d-1) n^{d-1}/2 and
the power is (d-1) + eps. Consumer variable Q = Pi = Z^0(2u)/Z^0(u)^2 (or P_K for the neutral form), by Theorem SW (d).

- **(g1) 4D compact U(1), weak coupling: F is FALSE. PROVED GIVEN row 1565 (5)-(7) with check 1571 A2-A3.**
  Theorem SW holds for U(1) with the square-contour rotation (its proof uses only: Haar-preserving circle action, half-turn
  sigma, positive symmetric smooth kernel). F would give Pi -> 1. But Pi = (1 + Q)/(1 + S)^2 <= 1/(1 + S), and the odd-flux
  fraction at period u is p_- = S_odd/(1 + S) <= S/(1 + S). Row 1565 gives p_- >= eta > 0 uniformly at the two aspects
  (Villain beta >= 2000; Wilson beta_W >= beta_*, existential). So Pi <= 1 - eta, -log Pi >= eta, and by Theorem SW (d)
  L_sigma(v) >= (4 eta / (3 pi^2 1024^3)) v^{-3}. Failing line l_1: an order-one thermal weight outside the vacuum at period u.
  (The same line with the photon levels, which are neutral: ARGUED, not proved here.)
- **(g2) 5D SU(2), weak coupling: F is FALSE under the BELIEF that the model has no gap there.** F gives Pi -> 1 at fixed
  aspect, so S(u) -> 0. The construction does not read the dimension; only N_p and the power do.
- **(g3) gapped twins: l_1 does not fire. PROVED GIVEN (2.15) of row 1568 (Theorem E, checked in 1572 Step 7); the support
  count is redone here, unchecked.** The bound there is uniform in the pins, so it covers every rotated end. For one replica:
  O_p reads at most five free variables with total coefficient <= 6 beta; a far temporal link lies in six link plaquettes
  and each link is in one pair, so the far scores have summed coefficient <= 6 beta at each variable. Hence
    sum_q |Cov(O_p, O_q)| <= 36 beta^2 v q^{v-2}/(1 - q)^2,   L_sigma(v) <= 72 beta^2 v q^{v-2}/(1 - q)^2,   q = 6(d-1) beta/m.
  For 4D SU(2), q = 9 beta/2: F holds on beta <= beta_s < 2/9. For 4D U(1), q = 9 beta: F holds on beta <= beta_s < 1/9.
  So inside the 4D U(1) family F changes truth value between small and large beta. For 5D SU(2) the small-beta side is
  proved the same way (q = 6 beta) and the large-beta side is belief. 3D: not tested here.
- **(g4) gapless members with an SU(2) factor: F is FALSE on the product with a seedless neutral spectator. PROVED (given
  the product algebra of check 1556 (iii)).** In the product model the purity is P_W P_m. The swap of the product model
  exchanges both fields. A rotation of the Wilson fields alone has half-turn sigma_W (x) 1; its four corners give P_W only,
  and the consumer does not read P_W. A rotation that reaches the full swap moves the spectator, and then F gives
  P_W P_m -> 1, so P_m -> 1, which a seedless spectator refutes. Failing line: the spectator's own pair covariance.
  Witness: two copies of the neutral circle rotor of check 1570 (one rotor is excluded by N1; two carry the square-contour
  rotation). So, unlike (B), this candidate is not blind to neutral sectors: the swap moves every degree of freedom, the
  centre only the charged ones. K7 and the adjoint-Higgs Coulomb phase: F false at BELIEF grade, by the same purity line.
- **(g5) scale: PROVED GIVEN row 1143 (10).** N(beta) = any n in 1024 N at aspect u = n/512. At a fixed lattice with beta
  growing, the periodic seed fails when n^2 = o(beta) (row 1143 (10), as used in row 1529 section 3.3 (t4)), so Pi is not
  near 1 and F fails.
- **(g6) consumer, carry, method.** (Q, C) = (Pi, Lemma PER of row 1529) or (P_K, Fact PUR), then rows 1461, 1462, 1465.
  Step: none. On the band [2, 3] F gives a full seed at that coupling and needs the carry to beta_K (registry R12).
  Loss: Jensen and the absolute values only. Method at order-one coupling: none (step 7). Equivalence: step 8.

Summary of step 5: F passes (g1), (g3), (g4), (g5) at the stated grades and (g2) at belief grade. It fails (g6): no method, no carry.

## Step 6. What the pair rotation does to the ends, and why it cannot be made gentler by this route (PROVED items marked)

The cut rotation descends to gauge orbits. The pair rotation commutes with the diagonal gauge group only (Proposition ROT
(iv), (vi)). The kernels are invariant under G x G at each end, so I_M(s) and Theorem SW are unaffected. The cost is in
the ends:

**Lemma NOISE (PROVED).** Under mu, and under any law of (A, B) invariant under G x G, the relative variables c_e = a_e^{-1} b_e
on any forest of links are independent and Haar distributed. So theta_e has the law (2/pi) sin^2(theta) dtheta at every coupling,
and the mean speed of each link under R_s is E sin(theta/2) = 32/(15 pi), about 0.68.
Proof. Apply independent Haar gauge fields (g, g'). On e = (x, y): c_e -> g_y a_e^{-1} (g_x^{-1} g'_x) b_e g'_y^{-1}. Peel the
forest from its leaves: each leaf vertex brings a fresh Haar factor that enters one link only. The mean is
(2/pi) integral of sin^2(theta) sin(theta/2) = (2/pi)(16/15). QED
Reading (ARGUED). At s near pi/2 every link of both replicas has moved by an amount of order one in a direction set by
gauge noise. The rotated end R_s Y' is hot on the whole slice at every coupling. The cut rotation heats n^2 links; this
one heats 3 n^3 links in each replica. By the plaquette count the weight of an end changes by at most exp(36 beta n^3)
(nine plaquettes of the sewn torus per site and replica touch the slice, each changes by at most 2 beta).

Can a relative frame between the replicas remove the noise? Two exact limits:

**Lemma N3 (no relative frame in SU(2); PROVED).** There is no map h from link fields (of any number of slices of the two
replicas) to SU(2)-valued site fields with h(A^g, B^{g'}) = g h(A, B) g'^{-1} for all gauge fields g, g'.
Proof. The constant gauge field g = -1 fixes every link. With g' = 1 the rule gives h = -h. QED
So a covariant comparison of the two replicas exists only in SO(3), that is, modulo the centre. (Frames in SO(3) do
exist off null sets, for example from two plaquette axes of an adjacent untouched slice, carried by the temporal links.)

**Lemma N4 (the centre-blind pair rotation ends at the swap times centre signs; PROVED).** Define the pair rotation on
SO(3) data: for a doubled link let nu = n if theta < pi/2 and nu = -n if theta > pi/2 (the axis of the SO(3) class of c,
with angle min(2 theta, 2 pi - 2 theta)), keep the SO(3) midpoint, and rotate (nu_1, nu_2) by F_s. This flow commutes with all
four sign flips of a_i, b_i, and its lift to SU(2) is continuous. Its half-turn is
   (a_e, b_e) -> (eps_e b_e, eps_e a_e),   eps_e = sign Re(a_e^{-1} b_e).
Proof. For theta < pi/2 the lift is the orbit of Lemma CO. For theta > pi/2 put phi = pi - theta, m~ = a e^{phi nu/2}; then
a = m~ e^{-phi nu/2} and b = -m~ e^{phi nu/2} (since e^{-pi nu} = -1). The lifted orbit is a(s) = m~ e^{-phi nu_s/2}, b(s) = -m~ e^{phi nu_s/2},
and nu_pi = -nu gives a(pi) = -b, b(pi) = -a. QED
By Lemma NOISE the signs eps_e are fair coins, independent on forests. The field eps is not a pure gauge almost surely:
the map b_e -> -b_e preserves Haar, flips eps_e alone, and so flips the product of eps around each plaquette on e; hence
that product is -1 with positive probability. So the endpoint is the swap followed by thin centre vortices in both
replicas (dense: ARGUED from the fair coins), and its kernel is not KK(Y', sigma Y).
So the rotation that is covariant modulo the centre does not interpolate to the period-2u torus.

Consequence. Lemmas N1, N3, N4 bound the class from three sides: one link at a time is impossible (orientation); a
G x G-covariant version needs an SU(2) relative frame, which does not exist (centre); the SO(3) version reaches the
wrong endpoint (centre vortices). Not decided here: whether some other deterministic flow on pairs of gauge orbits, local
in a useful sense, reaches the swap. (On the orbit space of the slice the parity obstruction is absent: its generic
dimension is 6 n^3, even. So I have no proof that none exists, and no construction.)

Free-field guide (GUIDE only, not a proof step). For a free massless vector field there is an exact symmetry of the
doubled system through the swap: rotate the polarization of each transverse mode of the relative field A - B about its
momentum. Its half-turn is A - B -> -(A - B), the swap; its charge is the helicity of the relative field; then
P = E(-1)^k = product over modes of tanh(u omega/2), the number of row 1529 section 2 (log P about -5.5e7 at this aspect).
That generator is non-local (curl over |curl|) and needs a relative gauge. SU(2) Wilson has no such symmetry on file.

## Step 7. The first lemma, and three attacks on it (it stays OPEN)

**Lemma (SW), to prove or refute.** 4D Wilson SU(2). There are C < infinity and eps > 0 such that for every beta in [2, 3],
every n in 1024 N and v = n/1024 >= 3, with the pair rotation R_s of step 3 and the sewing measure mu of step 4 (M_v = T^v):
    sup over s, t in [0, pi] and over pairs p of   sum over pairs q of  E_mu | (D_p^(1) D_q^(2) log KK_v)(R_s Y', R_t Y) |   <=  C v^{-3-eps}.
Signed form (enough for the consumer): sup over s, t of E_mu sum_{p,q} h_pq(R_s Y', R_t Y) <= C v^{-eps}.
By Theorem SW it gives 1 - Pi(u; n, beta) = O(v^{-eps}), a full periodic seed at each band coupling for large n.

**Attack 1: one-link comparison, uniform in the pins. Closes for beta < 2/9 only.**
PROVED GIVEN (2.15) of row 1568: L_sigma(v) <= 72 beta^2 v q^{v-2}/(1-q)^2 with q = 9 beta/2 (step 5, (g3)). The pins are arbitrary
there, so hot ends cost nothing. Stop: q >= 9 on the band. The file already has the witness that no unweighted one-link
contraction holds at beta = 2: a bulk link whose eighteen maximized influence coefficients sum above 18/10 (row 1565
lines 84-90; checks 1570 A1 and 1571 C1). A finite-block criterion would need a verified box inequality that is uniform
over hot pins on a whole slice; none is on file. This attack reads neither the group nor the dimension.

**Attack 2: the transfer spectrum. Controls the unrotated corner given the full seed; fails at rotated ends.**
(a) Corner, PROVED: by Lemma CORNER, with Omega_2 = Omega (x) Omega, Lambda_0 the top eigenvalue of MM, r = (lambda_1/lambda_0)^v:
      E[jk] = Tr(G MM G MM)/Tr(MM^2)  <=  2 r |G Omega_2|^2 + r sum over b != Omega_2 of (Lambda_b/Lambda_0) |G b|^2.
    Proof: MM = Lambda_0 P + MM' with 0 <= MM' <= Lambda_0 r; <Omega_2, G Omega_2> = 0 (G = -iD, D real and skew, Omega_2 real);
    the cross term is 2 Lambda_0 <G Omega_2, MM' G Omega_2>; the last term is |MM'^{1/2} G MM'^{1/2}|_HS^2 <= |MM'| Tr(MM'^{1/2} G^2 MM'^{1/2}). QED
    So the corner needs: a gap uniform in the volume in every sector, a thermal sum of |G b|^2, and the static size of
    |G Omega_2|^2 (of order n^3, ARGUED). These inputs are at least the full periodic seed at that coupling. Same verdict as
    "Failure 1a" of row 1568 (check 1572 Step 8) and A2 of row 1566 (check 1570).
(b) Rotated ends: the weight mu sits at the unrotated ends and h_pq is read at R_s Y', R_t Y. The ratio does not cancel.
    The change of measure costs up to exp(36 beta n^3) (step 6), against exp(8 beta n^2) for the cut (check 1570, A2). By Lemma
    NOISE the loss is of volume order for typical ends (ARGUED). A fixed rate exp(-m v) with v = n/1024 cannot pay n^3.
    Stop: a spectral method needs ends inside the bulk of the vacuum; the rotation leaves it on the whole slice.

**Attack 3: a sign, or a one-end moment. Both are excluded (PROVED).**
(a) No fixed sign. For fixed Y and q the integral over Y' of h_pq(Y', Y) against Haar is zero (D_p is skew). If h_pq had one
    sign it would vanish almost everywhere for all p, q; then Theorem SW (a) gives KK_v(Y', Y) = KK_v(Y', sigma Y) almost
    everywhere, so Tr M^4 = (Tr M^2)^2 and M has rank one, which is false for beta > 0. (The argument of check 1570 A3, moved
    to the swap.) So absolute rows cannot be reduced to the signed mean, which the corners fix.
(b) No one-end moment. By Lemma W, 1 - P = 2 Pr(k odd) <= 2 E k^2 = 2 Tr(G^2 M (x) M)/(Tr M)^2. This is exact for a
    symmetry (it is the charge variance, as in (5) of row 1565 for U(1) flux). Here G does not commute with T (x) T, and
    E k^2 >= |G Omega_2|^2 (lambda_0^u)^2/(Tr M)^2, of order n^3 at any coupling (ARGUED). So the bound is empty.
    A usable one-end form would need a circle action through sigma that commutes with T (x) T. For free fields it exists
    (step 6, guide). For SU(2) Wilson none is on file; I did not prove that none exists (GUESSED: none).

Also tried, as a repair of the structure and not of the lemma: making the ends cold by a relative frame (step 6). It
stops at Lemmas N3 and N4.

Where the lemma stands. (SW) is true for beta < 2/9 and false for weak 4D U(1) (given row 1565). On the band it is OPEN.
It asks for mixing between the two ends of the cylinder that is uniform over ends heated on a whole slice. A gap alone
is not known to give that. This is one precise lemma, attacked three ways, with the stop of each written above.

Guess on the direct form (GUESSED, not used). Applied on the calibrated trajectory at fixed l, the absolute form pays
N_p = 3 n^3/2 against rows that need not decay across the slice (a zero-momentum level couples all pairs). I expect
the absolute form to fail there as K grows; only the band form with a separate carry is a candidate.

## Step 8. Equivalence test, relation to the cut lemma, verdict

**Relation to the cut lemma (PROVED, from check 1570's identity).** P_K = Pi a_{2u}/a_u^2 with a_t = Z_+(t)/Z^0(t). Lemma (B) of 1556 (v)
bounds the a's (relative twist weights). (SW) bounds Pi, the factor that (B) cannot see. The neutral form of (SW)
(M_v = P_0 T^v) bounds P_K directly and does not need (B). So the pair rotation reads the common neutral normalization
across the two periods, which is the input the band rows of 2026-11-26 named as missing. It reads it as the cut
rotation reads the twists: a Haar-preserving circle action whose half-turn is the Z_2, four corners, mixed boundary
covariances. The differences are exact: pairs of links in place of single links (N1), no descent to gauge orbits
(N3, N4), and a defect on the whole slice in place of a cut.

**Equivalent is not progress: the test.**
- (SW) implies a full periodic seed at each band coupling (Theorem SW (d), Lemma PER). PROVED.
- (SW) does not give (PUR-io): the seed lives at beta_K. The carry (registry R12) is not touched. So (SW) is not
  equivalent to the seed; it is not sufficient for it either.
- Against its own consequence, the full band seed, (SW) is strictly stronger on general transfer data (ARGUED, by the
  example of check 1570 moved to two rotors): on the 2-torus take the kernel 1 + 2q cos(m(x_1 - x_1')), q = 1/4, m^2 q^v = 1,
  with the square-contour rotation. The purity tends to 1, and the mixed derivative of log KK is of order m^2 q^v = 1 on a
  set of positive measure. This example has no Wilson locality. For the Wilson law I cannot show that the full band
  seed fails to imply (SW), and I cannot show that it implies it.
- Method: none at order-one coupling (step 7).
Verdict under the rule: (SW) is a selective, consumer-accepted, non-equivalent statement that passes (g4), and it is no
progress on the seed, because it has no method and no carry and is at least as strong as the full band seed. I do not
propose a proof row on (SW).

**What this row adds to the file (all by hand, unchecked; no numeric run; no Lean step).**
- PROVED: Proposition N1 with corollaries (a)-(d) (no single-link or odd-block rotation reaches the swap; none at all on an odd-n slice).
- PROVED: Lemmas CO, S2, Proposition ROT, the U(1) version, the interpolation I_M(s), Lemma W.
- PROVED: Theorem SW (a)-(d), Lemma CORNER, the corner bound of Attack 2 (a), the two exclusions of Attack 3.
- PROVED: Lemmas NOISE, N3, N4.
- PROVED GIVEN on-file results: (g1) (row 1565, check 1571), (g3) and Attack 1 (row 1568 (2.15), check 1572), (g5) (row 1143 (10)).
- ARGUED: extensive loss at rotated ends; E k^2 extensive; the abstract separation example; dense vortices in N4.
- GUESSED: no commuting circle action through sigma for SU(2) Wilson; failure of the direct absolute form on the trajectory.
- OPEN: Lemma (SW) on beta in [2, 3]; a deterministic local flow on pairs of gauge orbits reaching the swap; the carry; (PUR-io).

**What would change the verdict (triggers, in the form of check 1443).** (1) A circle action through sigma that commutes
with T (x) T up to a controlled error: then Lemma W gives the purity from a charge variance, a one-end quantity.
(2) A relative frame that keeps rotated ends typical (it must evade N3 and N4, so it cannot be a function of the link
fields alone, or it must treat the centre separately, for example on the SO(3) factor with (B) supplying the centre).
(3) A mixing theorem on the band that is uniform over hot pins on a slice.

Credits. Cut rotation, four corners, spectator test: gpt-6.2-astra, check 1556 (v). Tests (g1)-(g6), Lemma ALG: row 1553
(Claude Fable), corrected by check 1556. Swap twist identity: rows 1115-1131, 1402 (Lemma COV), 1529 (Lemma INN, PER;
check 1539 by gpt-6.2-astra). Pinned covariance lemma and Theorem E: gemini-4-neon, row 1568, checked by Claude Opus
(1572). U(1) flux bound and identity (3): gpt-6.2-astra, row 1565, checked by Claude Opus (1571). Two-period identity and
the A2, A3 stopping arguments: row 1566 (Claude Fable) and check 1570 (gpt-6.2-astra). Froehlich-Spencer and Guth for
the U(1) Coulomb phase, as cited in those rows. I did not read the output of rows 1573 or 1576.

RESULT: PROVED (by hand, unchecked): no rotation of single links, or of any block of odd dimension, reaches the replica swap (orientation, Proposition N1), so the cut rotation has no literal neutral analogue; a rotation of link pairs does (Proposition ROT): a Haar-preserving circle action on the doubled slice, continuous off a null set, with half-turn the swap, so it interpolates between two period-u tori and the period-2u torus, and the four-corner calculus carries over (Theorem SW: -log Pi <= (3 pi^2/4) n^3 L_sigma, also in neutral form for P_K; Lemma CORNER). It commutes with the diagonal gauge group only; a G x G-covariant version is excluded in SU(2) (Lemma N3) and the centre-blind version ends at the swap times centre vortices (Lemma N4), so rotated ends are hot on the whole slice (Lemma NOISE). Tests: the resulting lemma (SW) is FALSE for weak 4D U(1) (given row 1565), TRUE at strong coupling (beta < 2/9, given row 1568), FALSE on a product with a seedless neutral spectator, so it passes (g1), (g3), (g4), (g5) and reads the neutral normalization that lemma (B) cannot; (g2) at belief grade; it FAILS (g6). Not refuted and not proved: (SW) on beta in [2, 3], attacked three ways (one-link comparison stops at 2/9; the spectrum controls only the unrotated corner and loses exp(O(beta n^3)) at rotated ends; no sign and no one-end moment exist). (SW) is not equivalent to the seed and gives no progress on it: no method, no carry, at least the full band seed. Open: (SW), a local deterministic swap flow on gauge orbits, the carry to beta_K, and (PUR-io).
