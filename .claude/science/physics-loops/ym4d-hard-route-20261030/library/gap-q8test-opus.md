author: anthropic/claude-opus-5-5 (max effort), AUTHOR of FINISH row 843 (`gap-q8test-opus`), run 2026-11-13 on the lead's MacBook
clone: /Users/jonreilly/ym4d-lead/clone at f1c86d81909cfef4bc95cfa244a7086b1f1599fb ("docs(ym4d): add rows 843-846, four more Opus max lanes"); pull --ff-only: already up to date

# gap-q8test-opus: the SU(2)-specific inputs against Q_8 and 2T, and a low-spin charged filter

**No mass gap is proved here.** Nothing in this file is checked by another model. It is research text and grants no status.

**Marks.** READ = I read the statement at the cited path and line. PROVED = proved by hand in this file, not checked by another model. ARGUED = a written argument with a named gap or a physical premise. GUIDE = numerics or recalled physics; no proof step rests on it. OPEN = no proof exists.

**Paths.** D = `.claude/science/physics-loops/ym4d-hard-route-20261030` in the clone. Short names, all under D/library: AS = `gap-assume-opus.md` (row 838); TR = `gap-tree-astra.md` (row 804); TRC = `gap-tree-check-opus.md` (row 805); EXT = `gap-ext-astra.md` (row 799 era; (LC) at 4.2); SX = `gap-shape-exercise-astra.md` (row 814); SXC = `gap-shape-check-opus.md` (row 824); JO = `gap-joint-astra.md` (row 811); VO = `gap-vortex-astra.md` (row 778); FL = `gap-flat-astra.md` (row 817); RT = `gap-rtail-astra.md` (row 823); EX = `gap-expose-astra.md`; FIN = D/FINISH.md (row n at line n + 76).

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the account and the Bessel convolution facts (GL3)-(GL4) as read by TR:156-169. Codex gpt-6-astra max: (LC) (EXT), the two-filter and degree-12 filter (G5)-(G21) (TR), Lemma D1 and Route C (SX), the joint representation (J1)-(J23) (JO), the commutator contraction (5)-(10) (VO), the class bounds (FL, RT). Claude Opus 5.5: the checks TRC, SXC, and AS (row 838), whose Lemmas F1-F6 this file extends. Hartung, Jakobs, Jansen, Ostmeyer and Urbach (arXiv:2201.09625, Table IV), as read by AS: the finite-group freezing couplings (GUIDE). Felix Klein: the invariants of the binary polyhedral groups (classical).

**What was read.** FIN row 843 (L919) and rows 844-846; the RESULT entries of rows 778, 780, 783, 785, 800, 804, 817-830. AS L1-L20, L131-L150, L295-L315, L345-L411 (Section 3.1 in full). TR in full (L1-L650). TRC in full. EXT 4.2-4.3 (L474-L574). SX Route D and Route C (L241-L358, L475-L620). SXC in full. JO L40-L723 (Sections 1-6). VO Sections 4-5 (L256-L443). FL L190-L280. RT L315-L324. EX L100-L170 (the transfer L_m).

**Method.** Every new statement below is derived by hand. Decimal values are marked GUIDE unless a hand bound is written. No repository file was edited; this is the only file written.

---

## 1. The comparison groups and their one-plaquette data

Notation. V = C^2 with the defining action. V_j = Sym^(2j) V is the spin-j module, d_j = 2j + 1. x(g) = tr(g)/2, chi = chi_V = 2x. For a closed subgroup G of SU(2) with normalized Haar measure, the Wilson one-plaquette density is k_beta^G(g) = e^(beta x(g))/z_G(beta), z_G = E_G e^(beta x). For a finite-dimensional G-module W put

```math
C^G_{\beta,W}=\int_G k^G_\beta(g)\,D_W(g)\,dg .
```

This is the operator of (G6) and (G14)-(G16) (READ TR:196-205, TR:383-420), now for any G.

**Lemma 1.1 (class data; PROVED, standard).** Use unit quaternions, 1 <-> I.
(a) Q_8 = {+-1, +-i, +-j, +-k}. x = 1 at 1, x = -1 at -1, x = 0 at the six others. Classes: {1}, {-1}, {+-i}, {+-j}, {+-k}.
(b) 2T = Q_8 together with the sixteen elements (+-1 +-i +-j +-k)/2. These have x = 1/2 (eight, order 6) or x = -1/2 (eight, order 3). Classes: {1}, {-1}, the six of order 4 (one class), and four classes of four elements: order 6 splits into two classes, order 3 into two classes.
(c) Q_8 is normal in 2T, [Q_8, Q_8] = {+-1}, [2T, 2T] = Q_8 (READ AS:378, Lemma F4).

*Proof.* (a), (b): direct; the 24 elements of 2T are the vertices of the 24-cell, and conjugation by (1+i+j+k)/2 permutes i -> j -> k cyclically, so the six order-4 elements form one class; an element of order 6 and its inverse are not conjugate in 2T because 2T/Q_8 = Z_3 sends them to different cosets. QED

**Lemma 1.2 (centre-odd irreducibles and their convolution eigenvalues; PROVED).** For G in {Q_8, 2T} every centre-odd irreducible G-module has dimension 2. For Q_8 there is one, V. For 2T there are three, V, V' = V (x) omega, V'' = V (x) omega-bar, where omega is a nontrivial character of 2T/Q_8 = Z_3. On any copy of an irreducible rho inside a G-module W, the operator C^G_{beta,W} acts by the scalar

```math
r^G_\rho(\beta)=\frac{\mathbb E_G[\chi_\rho\,e^{\beta x}]}{d_\rho\,\mathbb E_G[e^{\beta x}]},
```

and, explicitly, with s = beta/2,

```math
r^{Q_8}_V=\frac{\sinh\beta}{\cosh\beta+3},\qquad
r^{2T}_V=\frac{\sinh\beta+4\sinh s}{\cosh\beta+3+8\cosh s},\qquad
r^{2T}_{V'}=r^{2T}_{V''}=\frac{\sinh\beta-2\sinh s}{\cosh\beta+3+8\cosh s}.
```

For SU(2) the same formula gives r_j(beta) = I_(2j+1)(beta)/I_1(beta) on V_j (READ (G3), TR:160-166; checked TRC:104-110). For U(1) = {diag(e^(i theta), e^(-i theta))} with density proportional to e^(beta cos theta), a weight vector with eigenvalue e^(i n theta) has eigenvalue I_n(beta)/I_0(beta).

*Proof.* Dimensions: |Q_8| = 8 = 4 x 1 + 2^2 and |2T| = 24 = 3 x 1 + 3^2 + 3 x 2^2; the centre-even irreducibles are those of the quotients by {+-1} (Z_2 x Z_2, resp. A_4: 1, 1, 1, 3), and the remaining ones (V; V, V', V'') are centre-odd of dimension 2. omega is trivial on Q_8 and takes the values omega^(+-1) on the two cosets; V' and V'' are irreducible because tensoring by a one-dimensional character keeps irreducibility, and they are not isomorphic to V because their characters differ on the order-6 elements. The scalar form is Schur's lemma, since k^G is a class function, so C^G_{beta,W} commutes with D_W(G) and acts on each copy of rho by (1/d_rho) E_G[k chi_rho]. Explicit values: chi_V = 2x. For Q_8, E[chi_V e^(beta x)] = (2e^beta - 2e^(-beta))/8 = (1/2) sinh beta and E[e^(beta x)] = (e^beta + e^(-beta) + 6)/8; divide by 2 E[e^(beta x)]. For 2T, chi_V is 2, -2, 0, 1, -1 on x = 1, -1, 0, 1/2, -1/2 (multiplicities 1, 1, 6, 8, 8); the sums give E[chi_V e^(beta x)] = (4 sinh beta + 16 sinh s)/24 and E[e^(beta x)] = (2 cosh beta + 6 + 16 cosh s)/24. chi_V' equals chi_V times omega^(+-1) on the sixteen elements and chi_V on Q_8; summed over each set of eight elements of equal x, omega + omega-bar = -1 replaces 8 by -4, which gives the third formula. U(1): the n-th Fourier coefficient of e^(beta cos theta) is I_n(beta). QED

**Lemma 1.3 (the tilted mean; PROVED).** For every closed G containing -1, r^G_V(beta) = E^beta_G[x], the mean of x under k^G_beta, and r^G_V is nondecreasing in beta, with derivative Var^beta_G(x). For SU(2), r_(1/2) = E^beta[x] in the same sense.

*Proof.* chi_V = 2x and d_V = 2, so r^G_V = E[x e^(beta x)]/E[e^(beta x)] = psi'(beta) with psi = log E_G e^(beta x); psi'' is the tilted variance. For SU(2) V = V_(1/2). QED

**Lemma 1.4 (r^{2T}_V <= r^{Q_8}_V; PROVED).** For every beta >= 0, r^{2T}_V(beta) <= r^{Q_8}_V(beta), with equality only at beta = 0.

*Proof.* Split 2T into Q_8 and the sixteen elements R. The tilted law on 2T is a mixture, with positive weights, of the tilted law on Q_8 and the tilted law on R. On R, x = +-1/2 with weights e^(+-s) on eight elements each, so E^beta_R[x] = (1/2) tanh s. On Q_8, E^beta[x] = sinh(2s)/(cosh(2s) + 3) = sinh s cosh s/(cosh^2 s + 1). Its quotient by (1/2) tanh s is 2 cosh^2 s/(cosh^2 s + 1) >= 1, with equality only at s = 0. A mixture mean lies between the two means. QED

**Lemma 1.5 (restriction of the centre-odd SU(2) spins; PROVED).** Let n_G(j) = dim Hom_G(V, V_j) for half-integer j. Then n_G(j) = dim (V (x) V_j)^G = m_G(j - 1/2) + m_G(j + 1/2), where m_G(l) = dim V_l^G for integer l. The values for l <= 6 are

| l | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| m_{Q_8}(l) | 1 | 0 | 2 | 1 | 3 | 2 | 4 |
| m_{2T}(l) | 1 | 0 | 0 | 1 | 1 | 0 | 2 |

so n_{Q_8}(j) = 2, 3, 4, 5, 6 for j = 3/2, 5/2, 7/2, 9/2, 11/2 and n_{2T}(j) = 0, 1, 2, 1, 2 for the same j. In particular V_(3/2) restricted to Q_8 is 2V and V_(5/2) restricted to Q_8 is 3V (all of V_j is V-isotypic for Q_8), while V_(3/2) restricted to 2T is V' + V'' and V_(5/2) restricted to 2T is V + V' + V''.

*Proof.* V (x) V_j = V_(j-1/2) + V_(j+1/2) (Clebsch-Gordan), and Hom_G(V, W) = (V* (x) W)^G with V* = V (the invariant alternating form). For integer l, chi_l(theta) = sin((2l+1) theta)/sin theta with x = cos theta. Q_8: theta = 0 (one element, value 2l+1), theta = pi (one, value 2l+1), theta = pi/2 (six, value (-1)^l); so m_{Q_8}(l) = (2(2l+1) + 6(-1)^l)/8, which gives the row. 2T: add theta = pi/3 and 2pi/3 (eight each). For integer l, chi_l(pi/3) = chi_l(2pi/3) = 1, 0, -1 as l = 0, 1, 2 mod 3 (the three-periodic sequence b_l of (G13), READ TR:313-320); so m_{2T}(l) = (2(2l+1) + 6(-1)^l + 16 b_l)/24, which gives the row (for example l = 3: (14 - 6 + 16)/24 = 1; l = 2: (10 + 6 - 16)/24 = 0). Since every centre-odd Q_8-irreducible is V, V_j restricted to Q_8 is n_{Q_8}(j) V, and dimensions match (4 = 2 x 2, 6 = 3 x 2). For 2T: chi_(3/2) is 4, -4, 0, -1, 1 on x = 1, -1, 0, 1/2, -1/2, so <chi_(3/2), chi_V> = (8 + 8 - 8 - 8)/24 = 0, and the remaining four dimensions are V' + V'' (each pairs to 1 by the same count with omega + omega-bar = -1). chi_(5/2) vanishes off +-1, so it pairs to 1 with each of V, V', V''. QED

The pattern is general: for j >= 3/2, n_G(j) > 0 exactly when G has a nonzero invariant of degree 2j - 1 or 2j + 1. So the least centre-odd spin above 1/2 that contains a G-copy of V is j_G = (d_G - 1)/2: 3/2 for Q_8, 5/2 for 2T, 7/2 for 2O, 11/2 for 2I (degrees d_G = 4, 6, 8, 12 of AS Lemma F1, READ AS:363). For 2I this is (G15)'s spin 11/2 (READ TR:394-402).

## 2. Each SU(2)-specific input of the lane, tested against Q_8 and 2T

**The rule used (READ AS:385-391, Proposition F6; ARGUED there).** A flux-half tool claimed on I = [beta_-, beta_+] must fail for a comparison group G only if beta_+ is above the freezing coupling of G: about 1.15 for Q_8 and 2.15 for 2T (GUIDE, READ AS:383). Below it G is a positive control. So "holds for G" below means the input is true as a statement about G; whether that matters depends on the coupling range of the tool that uses it. I test the inputs as statements, at every beta, and then say where the range matters.

### 2.1 (LC), the small commutators (READ EXT:476-513)

For a closed subgroup G, write (LC_N)[G] for: there are A, B in G with x([A, B]) = cos(pi/N) (so [A, B] is conjugate in SU(2) to C_N and its N-th power is -I), 1 - x(A) <= pi/(2N), 1 - x(B) <= pi/(2N) and N(1 - x([A, B])) <= pi^2/(2N).

**Proposition 2.1 (PROVED).** (a) (LC_N)[Q_8] fails for every N >= 2. (b) (LC_N)[2T] fails for every N >= 3 and holds for N = 2. (c) (LC_N)[U(1)] fails for every N (READ EXT:510-513).

*Proof.* Let Delta_G = min over g != 1 of (1 - x(g)); by Lemma 1.1, Delta = 1 for Q_8 and 1/2 for 2T. If pi/(2N) < Delta_G, the generator bounds force A = B = 1, and x(1) = 1 != cos(pi/N). For Q_8 this covers every N >= 2 (pi/4 < 1). For 2T it covers N >= 4 (pi/(2N) < 1/2 iff N > pi). At N = 3 the commutator lies in [2T, 2T] = Q_8, whose x-values are 1, 0, -1, and cos(pi/3) = 1/2 is not one of them. At N = 2 take a = (1+i+j+k)/2 and b = (1+i-j-k)/2. Quaternion multiplication gives ab = (1+i+j-k)/2 and ba = (1+i-j+k)/2, so [a, b] = ab (ba)^(-1) = (1+i+j-k)(1-i+j-k)/4 = j. Then 1 - x(a) = 1 - x(b) = 1/2 <= pi/4, x(j) = 0 = cos(pi/2), and 2(1 - 0) = 2 <= pi^2/4. QED

**Consequence.** (LC) separates SU(2) from Q_8 and 2T only as N grows (N >= 3 suffices for both). No proved estimate of the lane uses (LC) quantitatively: its one attempted use, independent conjugacy averaging, is refuted by (J22)-(J23) (READ JO:601-651), and the coherent product is a sign change, not damping. So the test changes no conclusion.

### 2.2 The commutator contraction (READ VO:256-443, rows 778 and 780)

**Proposition 2.2 (PROVED).** Let G be Q_8 or 2T, with uniform (Haar) measure, and let K be right convolution by the law mu_G of [A, B], A and B independent and uniform on G.
(i) For every irreducible rho of G, E[rho([A, B])] = I/d_rho^2. This is (6) of VO.
(ii) On the centre-odd subspace of L^2(G), ||K|| = 1/4 exactly. This is (5).
(iii) For Q_8, mu = (5/8) delta_1 + (3/8) delta_(-1), so K = (1/4) I on centre-odd functions, in L^2 and in sup norm.
(iv) The density bound (7), mu >= (1/2) Haar, fails: mu is supported on [G, G], which is {+-1} for Q_8 and Q_8 for 2T.
(v) (8), (9) and (10) hold verbatim. In particular, for a >= 8, every twisted G-Wilson measure at every beta has |<W_a>_k| <= rho_beta^(floor(a/4)^2) with rho_beta = 1 - (3/4) e^(-24 beta), for the word W_a of VO (11).

*Proof.* (i) is the argument of VO (6) and of AS Lemma F2 (READ AS:367-371), which uses only Schur's lemma and the orthogonality of matrix coefficients; both hold for finite groups. (ii): by Lemma 1.2 every centre-odd irreducible of G has dimension 2, and the centre-odd part of L^2(G) is the sum of their matrix-coefficient spaces, on which K is the scalar 1/4 by (i). (iii): A and B commute iff A is central (probability 1/4) or A is not central and B is in {+-1, +-A} (probability (3/4)(1/2)); so P(commute) = 5/8, and every noncommuting pair in Q_8 has commutator -1. Then (Kf)(g) = (5/8) f(g) + (3/8) f(-g) = (1/4) f(g) for odd f. (iv): direct. (v): the proof of (8) uses only |x| <= 1 (oscillation at most 24 beta of the two selected links' exponent) and that left and right translations preserve the measure on the selected links; both hold for G. (9) uses (5) and the mixture decomposition. (10) uses (6) for the defining representation (which is irreducible for G), the mixture, conditional independence of the selected pairs, and submultiplicativity (READ VO:378-433); none of these depends on G being SU(2). QED

**Consequence (PROVED part, GUIDE part marked).** Row 780 argued that Q_8 shares (5), (6), (8)-(10) (READ FIN:856). This is now proved for Q_8 and 2T, and (7) is the one statement that fails. The bound (10) on W_a holds at every beta for Q_8 and 2T, including above their freezing couplings, where (V) fails (GUIDE). So the W_a bound is not an order parameter: it is a product of conditionally independent commutator signs, and it decays like a volume for any non-abelian finite gauge group whose commutator subgroup contains -1. This confirms, as a theorem, the reading of rows 780 and 783 that all content must sit in the comparison (CF).

### 2.3 The gauge reserve (C4) and (C5)-(C7) (READ SX:475-618; checked SXC:21-49)

**Proposition 2.3 (PROVED, by inspection).** (C1)-(C5) are not defined for a finite G: they need link tangent spaces, the infinitesimal gauge action J_ve and the bracket [a, b] = 2 a x b (READ SX:487-497). The source of the reserve is the Lie bracket; it vanishes for U(1) (READ SXC:73-75). The conclusion (C6)-(C7) is a theorem for beta < 11/48, below every finite-group freezing coupling (GUIDE). So no comparison group binds it at its coupling.

ARGUED: an order-one extension of Route C would pass the Q_8 and 2T tests by inapplicability, as TRC:225-226 already says for route B with 2I. That is a pass, but it does not locate the SU(2) mechanism; it only says the mechanism, if any, lies in the tangent structure.

### 2.4 Lemma D1 and the one-link covariance (READ SX:249-356; checked SXC:9-20)

**Proposition 2.4 (PROVED).** (D1) is a Poincare inequality for the gradient on S^3; it is not defined on a finite G. Its formulable shadow is the covariance of the coordinate vector q under exp(F . q): for SU(2) the supremum over F of the largest covariance eigenvalue is 1/4 (Theorem V, READ FIN:861), for Q_8 it is 1/2 (AS Lemma F5, READ AS:380-383). For 2T, the covariance agrees with the SU(2) value to third order in F at F = 0: Cov_F(q) - Cov^SU(2)_F(q) = O(|F|^4).

*Proof of the last sentence.* The k-th Taylor coefficient of Cov_F(q) at F = 0 is a polynomial in the moments of q of degree at most k + 2. The coordinates of q are linear in the matrix entries, and the 2T moments of degree at most 5 equal the SU(2) moments (AS Lemma F1, READ AS:361-365). So the coefficients of order k <= 3 agree. QED

For Q_8 the degree-4 moments differ, and the second-order term changes sign: along u perpendicular to F = f(1,1,0,0)/sqrt 2 with u = (1,-1,0,0)/sqrt 2, E_Q8[(u.q)^2 (F.q)^2] = f^2/8 against f^2/24 for SU(2), so Cov_F(u.q) = 1/4 + f^2/32 + O(f^4) for Q_8 and 1/4 - f^2/96 + O(f^4) for SU(2) (PROVED by the same expansion, Cov_F(u.q) = 1/4 + (1/2)(E[(u.q)^2(F.q)^2] - |F|^2/16) - (u.F)^2/16 + O(|F|^3), with E_SU(2)[q_a q_b q_c q_d] = (delta_ab delta_cd + delta_ac delta_bd + delta_ad delta_bc)/24 on the unit S^3). This is the local form of F5. Every R1 range built on Theorem V (beta below 2/9, 2/3, 1/4, 8/27, 11/48) is below 1.15, so the comparison groups do not bind them.

### 2.5 The two-filter contraction and the degree-12 filter (READ TR:180-461; checked TRC:62-140)

**Proposition 2.5 (PROVED).** (a) The pair filters (G5)-(G11) are shared by Q_8 and 2T with t replaced by t_G (AS Lemma F3, READ AS:373-378; t_Q8 = (cosh beta - 1)/(cosh beta + 3)). (b) The degree-12 filter (G15)-(G17a) separates SU(2) from Q_8 and from 2T as well: m_Q8(6) = 4 and m_2T(6) = 2 (Lemma 1.5), so Sym^12 V contains a G-invariant h, V (x) h is a G-copy of V, and on it the G-convolution is r^G_V >= beta/(4 e^beta).

*Proof of (b).* The lower bound is the argument of (G16) (READ TR:405-420; range caveat of TRC:118-121), which uses only E_G[chi_V^2] = 1 (V irreducible for G) and E_G[chi_V^n] >= 0 (an invariant dimension). Both hold for every G that acts irreducibly on V. For h^k in (G17a) use h^k != 0 in the domain of binary forms. QED

So the degree-12 filter is not wrong for the binding groups; it is wasteful. At beta = 2 its SU(2) eigenvalue is r_(11/2)(2) = I_12(2)/I_1(2), about 1.4 x 10^(-9) (GUIDE, READ AS:394), where spin 5/2 suffices (Section 3).

### 2.6 The joint surface weights (READ JO:70-500, FL:206-276, RT:315-324)

**Proposition 2.6 (PROVED).** (a) The joint representation (J1)-(J4), the strong-coupling bounds (J6)-(J9) and the leading plane term (J10) hold for Q_8 and 2T with their own Haar measures: they use only -1 in G, x(-g) = -x(g), |x| <= 1 and degree-2 moments (READ JO:653-666, which records the same for 2I). (b) The Haar moments that the class bounds use are

| moment | SU(2) | 2T | Q_8 |
|---|---|---|---|
| E x^2 | 1/4 | 1/4 | 1/4 |
| E x^4 | 1/8 | 1/8 | 1/4 |
| E x^6 | 5/64 | 3/32 | 1/4 |

(c) The numerical step (5/64)^(1/6) < 2/3 of (F11) fails for both groups: (3/32)^(1/6) > 2/3 because 3 x 729 = 2187 > 2048 = 32 x 64, and (1/4)^(1/6) > 2/3 because 729 > 256. (d) The fourth-moment payment of (R13) is shared by 2T and not by Q_8.

*Proof.* (b): E_G x^(2l) = 4^(-l) E_G chi^(2l), and the class sums of AS Lemma F1 give E chi^(2l) = 1, 2, 6 for 2T and 1, 4, 16 for Q_8 at l = 1, 2, 3 (READ AS:365; I re-derived them from Lemma 1.1: for 2T, E x^(2l) = (2 + 16 (1/4)^l)/24). (c), (d): arithmetic and (b). QED

**Consequence.** The class theorems of rows 817, 823, 827 are proved at beta <= 1/2 (resp. 5/11), where Q_8 and 2T are positive controls (GUIDE). Their proofs use moments that differ for the comparison groups ((c), (d)), so the proofs, not the conclusions, are group-selective there. This is not a pass of a binding test, since nothing binds at beta <= 1/2. GUIDE (decimals): at beta = 1/2 the branching factor q_6 = m6^(1/6) sinh(beta) cosh(beta)^8 is about 0.89 (SU(2)), 0.92 (2T) and 1.08 (Q_8), so the q_6 < 1 conclusion of (F14) would survive for 2T and fail for Q_8 at beta = 1/2; I did not re-derive the 2T constants by hand.

### 2.7 Summary of the tests

| Input | Q_8 | 2T | Coupling range of its use | Changes a conclusion? |
|---|---|---|---|---|
| (LC) | fails, every N >= 2 | fails N >= 3, holds N = 2 | no quantitative use | no |
| commutator contraction (5), (6), (8)-(10) | holds verbatim, every beta | holds verbatim, every beta | every beta | yes: W_a is not an order parameter (2.2) |
| density bound (7) | fails | fails | not used in (10) | no |
| (C4)-(C7) | not defined | not defined | beta < 11/48 | no |
| D1, Theorem V | D1 not defined; covariance 1/2 | D1 not defined; covariance = SU(2) to O(F^4) | beta < 2/3 | no |
| pair filters (G7) | shared (t_Q8) | shared | every beta | no (AS F3) |
| degree-12 filter (G15) | separates | separates | every compact interval | wasteful: spin 11/2 |
| (J2)-(J10) | holds | holds | all / beta <= 1/2400 | no |
| moments in (F11), (R13) | differ at degrees 4, 6 | differ at degree 6 | beta <= 1/2 | proofs selective, conclusions not binding |

## 3. A charged filter at spin 5/2 that separates SU(2) from Q_8, 2T and U(1) at every beta

### 3.1 Bessel facts, by hand

**Lemma 3.1 (PROVED).** For nu > -1/2 and x > 0 let w = w_(nu,x) be the probability density proportional to e^(xt) (1 - t^2)^(nu - 1/2) on (-1, 1). Then:
(a) I_(nu+1)(x)/I_nu(x) = E_w[t], and 0 < E_w[t] < 1;
(b) I_(nu+1)(x)/I_nu(x) is strictly increasing in x;
(c) E_w[1 - t^2] = ((2 nu + 1)/x) E_w[t];
(d) I_(nu+1)(x)/I_nu(x) <= U_nu(x) := x/(a + sqrt(a^2 + x^2)), a = nu + 1/2; U_nu is increasing in x, and 1 - U_nu(x) >= a/(2a + x).

*Proof.* Poisson's formula I_nu(x) = (x/2)^nu/(sqrt(pi) Gamma(nu + 1/2)) Int_(-1)^1 e^(xt)(1 - t^2)^(nu - 1/2) dt follows by expanding e^(xt), integrating termwise with Int t^(2k)(1 - t^2)^(nu - 1/2) dt = Gamma(k + 1/2) Gamma(nu + 1/2)/Gamma(k + nu + 1), and Gamma(k + 1/2) = sqrt(pi) (2k)!/(4^k k!); the result is the series Sum_k (x/2)^(2k+nu)/(k! Gamma(k + nu + 1)). (c): write e^(xt) = (1/x) d/dt e^(xt) in Int e^(xt)(1 - t^2)^(nu + 1/2) dt and integrate by parts; the boundary term vanishes because nu + 1/2 > 0, and d/dt (1 - t^2)^(nu+1/2) = -(2nu + 1) t (1 - t^2)^(nu - 1/2). (a): by Poisson's formula, I_(nu+1)/I_nu = (x/(2nu + 1)) E_w[1 - t^2], which is E_w[t] by (c). E_w[t] < 1 since t < 1 almost surely; E_w[t] > 0 since the numerator is Int_0^1 t (e^(xt) - e^(-xt))(1 - t^2)^(nu - 1/2) dt > 0. (b): d/dx E_w[t] = Var_w(t) > 0. (d): with m = E_w[t], Jensen gives E_w[t^2] >= m^2, so (c) gives ((2nu + 1)/x) m <= 1 - m^2; m is at most the positive root of m^2 + ((2nu + 1)/x) m - 1, which is U_nu(x). U_nu(x) = 1/(a/x + sqrt(a^2/x^2 + 1)) is increasing. Finally 1 - U_nu = (a + sqrt(a^2 + x^2) - x)/(a + sqrt(a^2 + x^2)) >= a/(a + sqrt(a^2 + x^2)) >= a/(2a + x). QED

For nu = 1 the density w is the tilted semicircle, which is the law of x = tr(g)/2 under k_beta on SU(2); for nu = 0 it is the tilted arcsine law, the law of cos(theta) under the U(1) density. Part (d) is the classical Amos-type bound; the proof above is self-contained.

**Lemma 3.2 (SU(2) side; PROVED).** For beta > 0, r_(5/2)(beta) = I_6(beta)/I_1(beta) = Prod_(n=1)^5 I_(n+1)(beta)/I_n(beta). It is strictly increasing in beta, and

```math
r_{5/2}(\beta)\le M(\beta):=\min\Big\{\frac{(\beta/2)^5}{6!},\ P(\beta),\ 1-\frac{11}{22+2\beta}\Big\},
\qquad P(\beta)=\prod_{n=1}^{5}U_n(\beta).
```

Each of the three majorants is increasing in beta. Also r_(5/2) < r_(3/2) < r_(1/2) < 1.

*Proof.* Monotonicity: a product of five positive increasing functions (Lemma 3.1(b)). The first majorant is the product of the five inequalities I_(n+1)/I_n <= beta/(2(n + 1)) of (G3) (READ TR:160-166; checked TRC:12-15). The second is Lemma 3.1(d). The third: r_(5/2) <= I_6/I_5 <= U_5 <= 1 - 5.5/(11 + beta), since the other four factors are below 1. The chain r_(5/2) < r_(3/2) < r_(1/2) < 1 is Lemma 3.1(a). QED

**Lemma 3.3 (comparison side; PROVED).** (a) For every closed G acting irreducibly on V (Q_8, 2T, 2O, 2I, SU(2)), r^G_V(beta) >= beta/(4 e^beta). For U(1), I_1(beta)/I_0(beta) >= beta/(2 e^beta).
(b) r^(2T)_V(beta) >= 1/2 for beta >= 7/2, and r^(Q_8)_V(beta) >= 1/2 for beta >= log(3 + sqrt 12) (about 1.87).
(c) With s = beta/2, 1 - r^(2T)_V(beta) <= g(s) := 4e^(-s) + 6e^(-2s) + 12e^(-3s) + 2e^(-4s), and 1 - r^(Q_8)_V(beta) <= 6e^(-beta) + 2e^(-2beta).
(d) For U(1), 1 - I_1(beta)/I_0(beta) <= 1/beta + 1/I_0(beta), and I_0(beta) >= beta^4/64.

*Proof.* (a) is the argument of (G16) (READ TR:405-420): the numerator E_G[chi_V e^(beta chi_V/2)] has nonnegative Taylor coefficients E_G[chi_V^(n+1)]/n! (invariant dimensions) and linear term (beta/2) E_G[chi_V^2] = beta/2; the denominator 2 E_G[e^(beta chi_V/2)] is at most 2 e^beta. For U(1) the same argument with E[cos^2] = 1/2. (b) With y = e^s, Lemma 1.2 gives 2N - D = y^2/2 - (3/2) y^(-2) - 8/y - 3 for 2T, where r = N/D. This is increasing for y >= 1 and equals 7.84 > 0 at y = 5. And e^(7/4) >= 1 + 7/4 + (7/4)^2/2 + (7/4)^3/6 + (7/4)^4/24 > 5.56. For Q_8, r >= 1/2 iff 2 sinh beta - cosh beta >= 3 iff e^(2beta) - 6 e^beta - 3 >= 0 iff e^beta >= 3 + sqrt 12. (c) D - N = e^(-2s) + 3 + 2e^s + 6e^(-s) and D >= e^(2s)/2 for 2T; for Q_8, 1 - r = (3 + e^(-beta))/(cosh beta + 3) <= 2e^(-beta)(3 + e^(-beta)). (d) I_1/I_0 = E_w[t] for nu = 0 (Lemma 3.1(a)), and E_w[1 - t^2] = E_w[t]/beta <= 1/beta (Lemma 3.1(c)). Since 1 - t <= 1 - t^2 on [0, 1] and 1 - t <= 2 on [-1, 0), E_w[1 - t] <= 1/beta + 2 P_w(t < 0). Poisson's formula with nu = 0 gives Int_(-1)^1 e^(beta t)(1 - t^2)^(-1/2) dt = pi I_0(beta), and Int_(-1)^0 e^(beta t)(1 - t^2)^(-1/2) dt <= pi/2, so P_w(t < 0) <= 1/(2 I_0). The last bound keeps one term of I_0 = Sum (beta/2)^(2k)/(k!)^2. QED

### 3.2 The filter theorem

Let H = V_(5/2) = Sym^5 V: centre-odd (-I acts by -1), SU(2)-irreducible, dimension 6. Let H' = V (x) Sym^6 V = V_(5/2) + V_(7/2), the (G15)-shaped version, and h_6 = xy(x^4 - y^4) in Sym^6 V (binary forms in the coordinates of V).

**Theorem 3.4 (spin-5/2 charged filter; PROVED).** For every beta > 0:
(i) SU(2): C^(SU(2))_(beta,H) = r_(5/2)(beta) I_H, and ||C^(SU(2))_(beta,H')|| = r_(5/2)(beta) <= M(beta).
(ii) Q_8: C^(Q_8)_(beta,H) = r^(Q_8)_V(beta) I_H: all of H is V-isotypic for Q_8.
(iii) 2T: H = V + V' + V'' as a 2T-module, and C^(2T)_(beta,H) acts by r^(2T)_V(beta) on the copy of V. In H', the line V (x) h_6 is a copy of V for both Q_8 and 2T, with eigenvalues r^(Q_8)_V and r^(2T)_V.
(iv) U(1): the weight vectors x^3 y^2 and x^2 y^3 of H (eigenvalues e^(+-i theta)) have eigenvalue I_1(beta)/I_0(beta); in H', e_+ (x) x^3 y^3 likewise.
(v) Separation at every coupling:

```math
r_{5/2}(\beta)\ \le\ M(\beta)\ <\ r^{2T}_V(\beta)\ \le\ r^{Q_8}_V(\beta),\qquad M(\beta)<\frac{I_1(\beta)}{I_0(\beta)} .
```

(vi) On every compact I = [beta_-, beta_+] in (0, infinity), the ratio of the SU(2) operator norm to each comparison eigenvalue in (ii)-(iv) has supremum below 1 on I; it is at most M(beta_+)/lambda_G(beta_-) whenever that number is below 1, where lambda_G is the comparison eigenvalue.

*Proof.* (i) Schur's lemma on the irreducible V_(5/2), with the eigenvalue of Lemma 1.2; on H' the two eigenvalues are r_(5/2) > r_(7/2) (Lemma 3.1(a)), both positive, so the norm is r_(5/2); the bound is Lemma 3.2. (ii) Lemma 1.5 (V_(5/2) restricted to Q_8 is 3V) and Lemma 1.2. (iii) Lemma 1.5 and Lemma 1.2. For H': h_6 is invariant under diag(i, -i) (x -> ix, y -> -iy) and under (x, y) -> (y, -x), the generators of Q_8; m_Q8(3) = 1 = m_2T(3) (Lemma 1.5), so h_6 spans the Q_8-invariant sextics, and the 2T-invariant sextic line, being Q_8-invariant for the 2T that contains this Q_8, is the same line (Klein's tetrahedral form). V (x) h_6 is then a G-copy of V. (iv) The weights of V_(5/2) are e^(i n theta), n in {+-1, +-3, +-5}; x^3 y^2 has n = 1; Lemma 1.2.

(v) for 2T, in three ranges.
- 0 < beta <= 7/2: (beta/2)^5/720 < beta/(4 e^beta) iff beta^4 e^beta < 5760. The left side is increasing; at 7/2 it is (2401/16) e^(7/2) < 150.07 x 33.12 < 4971, using e < 2.71829 and e^(1/2) < 1.6488 (1.6488^2 > 2.71829), so e^(7/2) < 20.086 x 1.6488 < 33.12. With Lemma 3.3(a), M < r^(2T)_V.
- 7/2 <= beta <= 6: M(beta) <= P(6) <= Prod_(n=1)^5 6/(n + 1/2 + 6) = 7776/73129.2... < 0.107 (each sqrt((n + 1/2)^2 + 36) >= 6), and r^(2T)_V(beta) >= r^(2T)_V(7/2) >= 1/2 (Lemma 1.3, Lemma 3.3(b)).
- beta >= 6: M(beta) <= 1 - 5.5/(11 + beta), so it suffices that g(s)(11 + 2s) < 5.5 for s >= 3 (Lemma 3.3(c)). Each term c e^(-ks)(11 + 2s) has derivative c e^(-ks)(2 - k(11 + 2s)) < 0, so the product decreases; at s = 3, g(3) < 4(0.04980) + 6(0.00248) + 12(0.000124) + 2(0.0000062) < 0.2157 (from e^3 > 20.08), and 17 x 0.2157 < 3.67 < 5.5.
For Q_8, Lemma 1.4. For U(1): for beta <= 7/2 the first majorant is below beta/(2 e^beta) (beta^4 e^beta < 11520); on [7/2, 7], M <= P(7) <= Prod 7/(n + 1/2 + 7) = 16807/121882.4... < 0.138, while I_1/I_0 >= I_1/I_0 (7/2) >= 1 - 2/7 - 1/7.35 > 0.57 (Lemma 3.1(b), Lemma 3.3(d), and I_0(7/2) >= 1 + 3.0625 + 2.3447 + 0.7979 + 0.1527 > 7.35 from the first five series terms); for beta >= 7, (1/beta + 64/beta^4)(11 + beta) is decreasing and below 18/7 + 1152/2401 < 3.06 < 5.5 at beta = 7.
(vi) The ratio is continuous and below 1 on (0, infinity) by (v), so its maximum on a compact I is below 1; the explicit bound uses that M is increasing (Lemma 3.2) and each lambda_G is nondecreasing (Lemma 1.3 for Q_8 and 2T, Lemma 3.1(b) for U(1)). QED

**Corollary 3.5 (spin 3/2, Q_8 and U(1) only; PROVED).** On V_(3/2) = Sym^3 V, C^(SU(2)) = r_(3/2) I and C^(Q_8) = r^(Q_8)_V I (V_(3/2) restricted to Q_8 is 2V), and r_(3/2)(beta) < r^(Q_8)_V(beta) for every beta > 0. For 2T, V_(3/2) = V' + V'' contains no copy of V, and C^(2T) = r^(2T)_(V') I there; this is no fixed-vector separation.

*Proof.* Three ranges, as above. beta <= 2.2: (beta/2)^3/24 < beta/(4 e^beta) iff beta^2 e^beta < 48, and (2.2)^2 e^(2.2) < 4.84 x 9.03 < 43.8 (e^2 < 7.3891, e^(0.2) < 1.2215). 2.2 <= beta <= 6: r_(3/2) <= U_1 U_2 U_3 (6) <= (6/7.5)(6/8.5)(6/9.5) < 0.357, and r^(Q_8)_V >= 1/2 since e^(2.2) > 3 + sqrt 12 (Lemma 3.3(b)). beta >= 6: 1 - r_(3/2) >= 1 - U_3 >= 3.5/(7 + beta) and (6 e^(-beta) + 2 e^(-2 beta))(7 + beta) is decreasing and below 0.2 at beta = 6. The 2T statements are Lemma 1.5. QED

**Remark 3.6 (the power family, (G17a) form; PROVED).** h_6^k is a nonzero Q_8- and 2T-invariant in Sym^(6k) V. On V (x) Sym^(6k) V the SU(2) norm is r_(3k - 1/2) <= (beta/2)^(6k-1)/(6k)!, while V (x) h_6^k carries the comparison eigenvalue r^G_V >= beta/(4e^beta). So for any compact I and any epsilon > 0, some k gives an SU(2) norm below epsilon times the comparison eigenvalue on all of I. Theorem 3.4 shows that k = 1 already separates at every beta; the powers are needed only to make the ratio small, not to make it below 1.

**Corollary 3.7 (the spin-2 charged space already separates all three; PROVED).** On H_2 = V (x) Sym^4 V = V_(3/2) + V_(5/2) (centre-odd, the (G15) shape at degree 4), the SU(2) norm is r_(3/2)(beta). Q_8 has the copies V (x) x^2 y^2 and V (x) (x^4 + y^4) of V; 2T has the copy of V inside the summand V_(5/2) (Lemma 1.5); U(1) has e_+ (x) x^2 y^2. For every beta > 0, r_(3/2)(beta) < r^(2T)_V(beta) <= r^(Q_8)_V(beta) and r_(3/2)(beta) < I_1(beta)/I_0(beta).

*Proof.* 2T, in four ranges. beta <= 2.2: (beta/2)^3/24 < beta/(4 e^beta) (Corollary 3.5) and Lemma 3.3(a). [2.2, 3.5]: r_(3/2)(beta) <= U_1 U_2 U_3 (3.5) <= (3.5/5)(3.5/6)(3.5/7) < 0.205, and r^(2T)_V(beta) >= r^(2T)_V(2.2) >= 1/4, because with y = e^(1.1) >= 3 (series: 1 + 1.1 + 0.605 + 0.2218 + 0.061 + 0.0134 > 3.001) one has 4N - D = 1.5 y^2 - 2.5 y^(-2) + 4y - 12/y - 3 >= 13.5 - 0.28 + 12 - 4 - 3 > 0, increasing in y. [3.5, 6]: r_(3/2) <= U_1 U_2 U_3 (6) < 0.357 < 1/2 <= r^(2T)_V (Lemma 3.3(b)). beta >= 6: 1 - r_(3/2) >= 1 - U_3 >= 3.5/(7 + beta), and g(s)(7 + 2s) is decreasing with g(3) x 13 < 2.81 < 3.5. Q_8: Lemma 1.4. U(1): beta <= 2.6: (beta/2)^3/24 < beta/(2e^beta) iff beta^2 e^beta < 96, and 6.76 e^(2.6) < 6.76 x 13.47 < 91.1; [2.6, 4]: r_(3/2) <= (4/5.5)(4/6.5)(4/7.5) < 0.239 and I_1/I_0 (2.6) >= 1 - 1/2.6 - 1/I_0(2.6) > 0.33 (I_0(2.6) > 1 + 1.69 + 0.714 + 0.134 > 3.53); [4, 7]: r_(3/2) <= (7/8.5)(7/9.5)(7/10.5) < 0.405 and I_1/I_0 (4) >= 1 - 1/4 - 1/11.2 > 0.66 (I_0(4) > 1 + 4 + 4 + 1.777 + 0.444 > 11.2); beta >= 7: (1/beta + 64/beta^4)(7 + beta) <= 2 + 0.38 < 3.5. QED

So the row's "spin 2 or 3" has two answers. The degree-4 space H_2 separates SU(2) from Q_8, 2T and U(1) at every beta, with SU(2) norm r_(3/2) (0.032 at beta = 2, factor about 14 below 2T and 17 below Q_8; GUIDE). The irreducible V_(5/2), sensitive at degree 6, does the same with SU(2) norm r_(5/2) (0.0010 at beta = 2, factor about 430 below 2T). The irreducible V_(3/2) separates Q_8 and U(1) only.

**What is new against TR.** (G15) separates at spin 11/2 and needed (G17a) to cover a compact interval. Theorem 3.4 separates at spin 5/2, for every beta > 0 at once, from the groups that bind at the crossover (Q_8, 2T) and from U(1). It does not separate from 2O or 2I (n_2O(5/2) = n_2I(5/2) = 0 by the same character count; GUIDE that they bind only above about 3.2 and 5.7). Corollary 3.5 is the spin-2-sensitive filter for Q_8 alone.

### 3.3 Sizes at the crossover (GUIDE decimals; the inequalities are Theorem 3.4)

Exact formulas of Lemma 1.2, evaluated by the GUIDE script `scratchpad/lane843/scripts/guide843.py` (16 MB; output `guide843.out` beside it). No proof step rests on these numbers.

| beta | r_(1/2) | r_(3/2) | r_(5/2) | r^Q8_V | r^2T_V | r^2T_(V') | I_1/I_0 | r_(5/2)/r^2T_V | r_(3/2)/r^Q8_V |
|---|---|---|---|---|---|---|---|---|---|
| 1.15 | 0.2729 | 0.00720 | 7.8e-5 | 0.2999 | 0.2731 | 0.0146 | 0.497 | 2.9e-4 | 0.024 |
| 1.5 | 0.3441 | 0.0150 | 2.7e-4 | 0.3978 | 0.3449 | 0.0309 | 0.596 | 7.9e-4 | 0.038 |
| 2.0 | 0.4331 | 0.0319 | 1.0e-3 | 0.5363 | 0.4358 | 0.0668 | 0.698 | 2.3e-3 | 0.060 |
| 2.15 | 0.4569 | 0.0382 | 1.4e-3 | 0.5760 | 0.4605 | 0.0805 | 0.721 | 3.0e-3 | 0.066 |
| 2.5 | 0.5072 | 0.0548 | 2.6e-3 | 0.6625 | 0.5139 | 0.1174 | 0.765 | 5.1e-3 | 0.083 |
| 3.2 | 0.5890 | 0.0943 | 7.0e-3 | 0.8011 | 0.6057 | 0.2087 | 0.824 | 1.2e-2 | 0.118 |
| 5.7 | 0.7511 | 0.2534 | 4.8e-2 | 0.9803 | 0.8290 | 0.5960 | 0.907 | 5.7e-2 | 0.258 |

Readings. (1) The spin-5/2 filter separates SU(2) from 2T by a factor of about 330 at beta = 2.15 and 190 at 2.5; the degree-12 filter of TR does it at the cost of an SU(2) eigenvalue near 10^(-9) (READ AS:394). (2) On the fundamental itself, 2T and SU(2) nearly agree: r^2T_V - r_(1/2) = beta^5/7680 + O(beta^7) (PROVED: r = psi'(beta) = Sum_n kappa_(n+1) beta^n/n!, the cumulants of x agree through order 5, and kappa_6 differs by E_2T x^6 - E x^6 = 3/32 - 5/64 = 1/64; the series is 1/64 x beta^5/5!), and the GUIDE difference is 0.0027 at beta = 2. For Q_8 the difference starts at order beta^3 (kappa_4 differs by 1/8) and is 0.10 at beta = 2. (3) On spin 3/2, 2T has no fixed copy and its eigenvalue r^2T_(V') is about twice r_(3/2): the ratio tends to 2 as beta -> 0 (PROVED: both numerators start with (beta/2)^3/6, since V' occurs once in V^(x)3 restricted to 2T and V_(3/2) once in V^(x)3, while d_V' = 2 and d_(3/2) = 4), and it is about 2.1 at beta = 2 (GUIDE).

**GUIDE, for Section 2.4.** A random search over 20 000 fields F gives sup_F lambda_max Cov_F(q) = 0.49997 for Q_8 (consistent with AS Lemma F5's 1/2) and 0.25 for 2T, attained at F = 0. So Theorem V's quarter appears to hold for 2T (OPEN as a proof); if so, Lemma INF and the Dobrushin ranges are 2T-blind, and only Q_8 fails them.

## 4. Wilson exposure of the filter, and the first missing step

### 4.1 The filter is an exact factor of the actual transfer (PROVED, with the transfer READ)

The full transfer of EX (E1) is L_m = z^|E| K^(1/2) B_m K^(1/2) on the gauge-invariant space H = L^2(SU(2)^E)^(SU(2)^V), with K = (x)_e C_beta and C_beta = Sum_j r_j Pi_j, Z^m = Tr L_m^t, and Z^m - Z^(m+v) = 2 Tr(P_- L_m^t), P_- = (1 - Theta_omega)/2 (READ EX:95-152). Here Pi_j projects one edge's function space onto its spin-j Peter-Weyl block, on which left and right translations act as V_j (x) V_j*. So on an edge whose state lies in a centre-odd block of spin j >= 5/2, the kinetic factor C_beta is the scalar r_j <= r_(5/2) <= M(beta), which is the SU(2) side of Theorem 3.4 (i) (as a left or right module the block is a sum of copies of V_j). Three consequences, all PROVED from these definitions:

(a) No insertion is needed. The filter is a factor of L_m at the original normalization, in every time step and on every spatial edge. The cost argument (G19) (READ TR:483-511; TRC:184-187), which charges 1/||K|| for writing a Haar projection through a contraction, does not arise: nothing is written through a Haar tensor.

(b) The same structure holds for G. The G-transfer is L^G_m = z_G^|E| K_G^(1/2) B_m K_G^(1/2) on L^2(G^E)^(G^V) with K_G = (x)_e Sum_rho r^G_rho Pi_rho (the derivation of EX (E1) uses only Peter-Weyl and the class-function kernel, both valid for finite G). Restriction of functions R: L^2(SU(2)) -> L^2(G) maps the spin-j block into the sum of the rho-blocks with rho in V_j restricted to G, and

```math
R\,C_\beta-C^G_\beta\,R=\sum_j\sum_{\rho\subset V_j|_G}(r_j-r^G_\rho)\,\Pi_\rho R\,\Pi_j .
```

By Lemma 1.5 the term (j, rho) = (5/2, V) is present for Q_8 and 2T, and by Theorem 3.4 (v) its coefficient satisfies |r_(5/2) - r^G_V| >= (1 - M/r^G_V) r^G_V > 0 at every beta. So the SU(2) statement "an odd edge in spin >= 5/2 is damped by at most M(beta) per kinetic step" has, for G, the restriction of that edge landing in the V-block, where the damping is r^G_V. The intertwining defect is large exactly there: at beta = 2 it is about 0.43 at (5/2, V) for 2T, against about 0.003 at (1/2, V) (GUIDE, Section 3.3).

(c) One time slice carries a positive spin law. Let Pi = (x)_e Pi_(S_e) for sets S_e of spins. Pi commutes with K, with the gauge projection and with Theta_omega (J_e acts on the spin-j block by (-1)^(2j)), so for the projection Q = P_- Pi,

```math
0\le \operatorname{Tr}(Q\,L_m^t)=\|L_m^{t/2}Q\|_{\rm HS}^2,\qquad \sum_{\text{partition}}\operatorname{Tr}(P_-\Pi\,L_m^t)=\operatorname{Tr}(P_-L_m^t),
```

since L_m is positive (READ EX:108-110). So the odd-sector weight splits, at any one time slice, into nonnegative parts labelled by the edge spins. The same holds in the even sector and for G with its irreducibles.

### 4.2 Where the odd sector meets the filter (PROVED identities, ARGUED reading)

(a) **Branching links.** In the surface form (J2)-(J4) the moments of Section 2.6 are traces of Haar projections: E_G x^(2l) = 4^(-l) dim Inv_G(V^(x)2l) (PROVED: E_G chi^n is the invariant dimension of V^(x)n). With V^(x)4 = 2V_0 + 3V_1 + V_2 and V^(x)6 = 5V_0 + 9V_1 + 5V_2 + V_3, Lemma 1.5 gives dim Inv = 2 + m_G(2) for n = 4 (2, 2, 4 for SU(2), 2T, Q_8) and 5 + 5 m_G(2) + m_G(3) for n = 6 (5, 6, 16). So the extra G-channel at a 4-valent odd link is the Q_8-invariant plane in the totally symmetric fusion V_2 = Sym^4 V of the four spin-1/2 strands; for 2T, at a 6-valent link it is the line h_6 in V_3 = Sym^6 V (for Q_8 the six-valent extra space has dimension 11: ten from the five copies of V_2, one from V_3). These are the uncharged forms of the filters of Section 3: on V_2 (Q_8) and V_3 (2T) the G-convolution fixes the invariant (eigenvalue 1), while SU(2) has r_2 (0.0062) and r_3 (1.4 x 10^(-4)) at beta = 2 (GUIDE). The moment selectivity of rows 817 and 823 found in Section 2.6 is this exposure at beta = 0.

(b) **Fusion with the vacuum.** The charged filter is the uncharged one tensored with the flux: V (x) V_3 = V_(5/2) + V_(7/2), and the G-copy V (x) h_6 has eigenvalue 1 x r^G_V. In the transfer picture an odd edge reaches spin 5/2 when the winding spin-1/2 line shares the edge with an integer-spin excitation of spin 2 or 3 of the vacuum (Clebsch-Gordan). ARGUED reading: in a frozen finite-group phase the vacuum edge states carry the invariant channels at no kinetic cost (eigenvalue 1), and a flux line through them pays only r^G_V, as a bare line does. In SU(2) at the same beta those vacuum channels are damped by r_2 or r_3 per step, and the dressed line by r_(5/2)/r_(1/2) (about 0.0023 at beta = 2) relative to a bare line. This is the mechanism the filter can see. It is a reading, not a theorem.

(c) **Exposure density (PROVED identity, GUIDE values).** The character law of one plaquette, w_j(beta) = (2/beta) d_j^2 I_(2j+1)(beta) e^(-beta), is a probability law on spins (PROVED: k_beta(1) = e^beta/z = Sum_j d_j^2 r_j, and Sum_(n in Z) n^2 I_n(beta) = beta e^beta from (t d/dt)^2 of the generating function e^((beta/2)(t + 1/t)) at t = 1). Its weight on half-integer spins >= 5/2 is 0.29%, 0.80%, 1.6%, 2.8% at beta = 1.5, 2, 2.5, 3; on all spins >= 11/2 it is 3 x 10^(-9), 5 x 10^(-8), 4 x 10^(-7), 2 x 10^(-6) (GUIDE). So spin-5/2 channels occur at a small positive density at the crossover; spin-6 channels do not. This is a single-plaquette count, not the law of 4.1 (c).

### 4.3 What the filter cannot do (READ TR:522-585; PROVED transfer)

Proposition 4 of TR applies verbatim at spin 5/2: J_k v = s^(x)k (x) v keeps spin 1/2 with any number of strands (G20), and the single flat wrapping plane of spin-1/2 plaquettes contributes 2 r_(1/2)^A to Z^m - Z^(m+v) without any edge of spin above 1/2 (G21) (READ TR:524-570; checked TRC:192-208). In the transfer picture this is the odd sector whose winding odd cycle is in spin 1/2 at every time slice. So exposure of the spin-5/2 (or 3/2) channel is not mandatory term by term, at any period. On that leading part, 2T and SU(2) differ only through r^2T_V - r_(1/2) = beta^5/7680 + O(beta^7) (Section 3.3) and through the vacuum around the line.

### 4.4 The first missing step (OPEN)

The proof tree, after this file: spin-5/2 filter (Theorem 3.4, PROVED) -> exact location in L_m (4.1, PROVED) -> **(HS) high-spin rarity in the even sector** -> **(LS) low-spin odd-sector bound** -> original-normalization twist bound. The first missing arrow is (HS):

**(HS), OPEN.** There are an order-one interval I reaching above 2.15 (for example [2.15, 2.5]), a density eta(beta) < 1 and c > 0 such that, uniformly in the admissible tori (a, a, c, d), the twists m and beta in I, under the nonnegative one-slice law of 4.1 (c) in the even sector,

```math
\frac{\operatorname{Tr}\big(P_+\,\Pi_{\{N_{\ge2}(0)\ \ge\ \eta|E|\}}\,L_m^t\big)}{\operatorname{Tr}(P_+L_m^t)}\ \le\ e^{-c|E|},
```

where N_(>=2)(0) counts the spatial edges at time 0 whose spin is at least 2 (this is the place where Q_8's invariants live; for 2T use spin at least 3).

Why this is the first step. (i) It is the only statement in the tree that uses the filter directly: a large-deviation bound on high-spin edges is exactly what r_j <= M(beta) for j >= 5/2 (and r_2, r_3) should give through the kinetic factor, if the spatial multiplier B_m can be controlled (ARGUED). (ii) It is SU(2)-selective in the way the binding test requires: its G-analogue (the density of edges whose restricted state lies in the alias of the spin-2 or spin-3 invariant, which is the trivial G-block) is of order one in any G-vacuum, frozen or not, so it is not a statement G satisfies (ARGUED). (iii) It is not a rewrite of the twist deficit: it concerns the even sector only. A natural tool is reflection positivity in the time direction with chessboard estimates on the one-slice projections of 4.1 (c); I have not checked that the projections Pi are reflection-compatible (OPEN). The naive one-edge bound fails: Tr(Pi_e K X) <= r_(5/2) Tr((Pi_e (x) K_rest) X) with X = (B K)^(t-1) B >= 0 (PROVED by Pi_e K Pi_e <= r_(5/2) Pi_e (x) K_rest on odd spin >= 5/2), but the right side carries no kinetic factor at e, so the ratio to Tr(K X) is not bounded by this argument.

**(LS), OPEN, the remaining content.** On the low-spin part (fewer than eta|E| high-spin edges at time 0) the odd-sector fraction must satisfy the consumer bound (E17), Tr(P_- Pi_low L_m^t) <= C a^p eta_*^(a/2) Tr(L_m^t). (LS) is where the spin-1/2 flux line of 4.3 lives, so it is as hard as the original problem unless the low-spin restriction gives a usable finite-spin structure. I do not claim it does.

## 5. Which earlier conclusions change

Each entry gives the earlier statement (READ at the FIN line), then the change. "Unchanged" means the statement stands as written; the reason is given.

| Row | Earlier statement (READ) | After this file |
|---|---|---|
| 778, 780 | The commutator mechanism (5)-(10) fails for U(1); row 780 argued that Q_8 shares (5), (6), (8)-(10) (FIN:854, FIN:856). | **Changed (proved).** Q_8 and 2T share (5), (6), (8), (9), (10) at every beta, and (7) fails for them (Prop. 2.2). The W_a area bound holds in their frozen phases, so W_a is not an order parameter; all content sits in (CF), as row 780 read. |
| 783 | (iv): 2I has full density flattening, so contraction plus flattening do not separate SU(2) from finite subgroups; next: "a use of SU(2) beyond contraction and flattening" (FIN:859). | **Changed in scope.** The statement is true for 2I, which binds only above about 5.7 (GUIDE). For the groups that bind at the crossover, flattening already fails (AS F4) and (7) fails (Prop. 2.2 (iv)); but flattening's constant e^(-24 beta) is useless at order one (AS:403). The guide becomes: a quantitative use of SU(2) that Q_8 and 2T lack at order-one cost. Theorem 3.4 and Corollary 3.7 supply one, with no exponential loss. (iii) on Q_8 is unchanged: no fixed-beta Q_8 counterexample is certified. |
| 800 | (K25): 2I has the same centre-odd commutator norm 1/4 (FIN:876). | **Extended, conclusion unchanged.** Q_8 and 2T have it too (Prop. 2.2 (ii)). The missing (K-RESP) is unchanged. |
| 804 | Route A's pair filters are shared by 2I; Haar tensors first differ at degree 12; the charged filter (G15) at spin 11/2 separates 2I and U(1); free insertion (G18)-(G19) and mandatory exposure (G20)-(G21) are refuted; missing (G22) (FIN:880). | **Partly changed.** (1) The pair filters are shared by Q_8 and 2T too (AS F3); the discard stands. (2) For the binding groups the first moment difference is at degree 4 (Q_8) and 6 (2T), and a charged filter at spin 3/2-5/2 separates them and U(1) at every beta (Theorem 3.4, Corollary 3.7); (G15) also separates them (Prop. 2.5) but at an SU(2) eigenvalue near 10^(-9) at beta = 2. (3) The cost objection (G19) does not reach the kinetic factor: the filter is an exact factor of L_m (4.1 (a)). (4) (G20)-(G21) stand unchanged at spin 5/2 (4.3). (5) (G22) is still missing; its first concrete sub-step is (HS) (4.4). |
| 817 | The class theorems at beta <= 1/2 are group-blind for 2I (moments agree through degree 6) (FIN:893). | **Unchanged for 2I; not group-blind for 2T or Q_8.** The proofs use E x^6 = 5/64 and the step (5/64)^(1/6) < 2/3, which fails for both (Prop. 2.6 (c)). This is not a binding issue: no comparison group binds at beta <= 1/2 (GUIDE). |
| 818, 829 | Langevin gap for beta < 1/4 (and 8/27 on special tori) via Theorem V (FIN:894, FIN:905). | **Unchanged.** Theorem V fails for Q_8 (1/2) and appears to hold for 2T (GUIDE, 3.3); the range is below 1.15. |
| 819, 821 | Novelty and literature readings (FIN:895, FIN:897). | **Unchanged.** |
| 820 | Typical single-link influence is far above 1 at order one; routes must be collective (FIN:896). | **Unchanged.** |
| 822, 826, 830 | Checks of rows 817, 823, 827 (FIN:898, FIN:902, FIN:906). | **Unchanged.** Their remarks "finite-group moments agree through degree 11" concern 2I. |
| 823 | All class bounds group-blind for 2I (moments 1/4, 1/8, 5/64 agree) (FIN:899). | **Unchanged for 2I.** 2T shares 1/4 and 1/8 and not 5/64; Q_8 shares only 1/4 (Prop. 2.6). Not binding at beta <= 1/2. |
| 824 | Route C, (C4)-(C7), checked (FIN:900). | **Unchanged.** Not formulable for finite groups; range below 11/48 (Prop. 2.3). |
| 825, 828 | Area law for beta_W < 2/3 from Lemma INF and Lemma DC (FIN:901, FIN:904). | **Unchanged.** Its inputs use Theorem V, which fails for Q_8 (so the Q_8 version of the same proof would stop at about half the range; ARGUED, not derived); 2/3 is below 1.15. |
| 827 | SOS class bound at beta <= 5/11, group-blind for 2I (FIN:903). | **Unchanged.** Row 830 records that no link has degree above four (READ FIN:906); if only moments of degree at most 4 enter, the proof is also 2T-blind and Q_8-selective (ARGUED from that reading; I did not read (S8)-(S10)). |
| 838 (AS 3.1) | The separation sits at spin 2 for Q_8 (factor about 17 at beta = 2) and at spin 3 for 2T (factor about 430) (AS:393-395). | **Confirmed and sharpened.** The factors agree with Section 3.3. New: the degree-4 charged space already separates 2T (through its V_(5/2) summand, Corollary 3.7, factor about 14), and every separation holds at every beta > 0, not only at beta = 2. |

**Net effect.** No proved result of rows 783-830 is refuted. Three readings move: the commutator word W_a is now proved blind to Q_8 and 2T; "beyond contraction and flattening" binds only above about 5.7; and the missing filter of route A is no longer a spin-6 object with a 10^(-9) cost but a spin-3/2 or spin-5/2 kinetic factor that is already present in the transfer at the original normalization. The missing Wilson estimate itself, (G22), is unchanged in kind; this file names its first sub-step (HS).

## 6. What is proved, what is open, and what a checker should read first

**PROVED here (by hand, not checked by another model).**
1. Class data, the centre-odd irreducibles of Q_8 and 2T, and closed forms of their one-plaquette convolution eigenvalues (Lemmas 1.1-1.2); r^2T_V <= r^Q8_V (Lemma 1.4); the restriction table of V_j for j <= 11/2 (Lemma 1.5).
2. (LC) fails for Q_8 at every N >= 2 and for 2T at every N >= 3, and holds for 2T at N = 2 with [a, b] = j (Prop. 2.1).
3. The commutator contraction (5), (6), (8)-(10) of row 778 holds verbatim for Q_8 and 2T at every beta, and the density bound (7) fails (Prop. 2.2). Hence the W_a area bound holds in their frozen phases.
4. (C4)-(C7) and D1 are not formulable for finite groups; the covariance shadow of D1 agrees for 2T with SU(2) to order F^3 and differs for Q_8 at order F^2 (Props. 2.3-2.4). (G15)-(G17a) separate Q_8 and 2T too (Prop. 2.5). The moment steps of rows 817 and 823 are selective for Q_8 and 2T at degrees 4 and 6 (Prop. 2.6).
5. Bessel facts: I_(nu+1)/I_nu is the tilted mean E_w[t], increasing in x, with the Amos-type upper bound U_nu (Lemma 3.1).
6. **Theorem 3.4:** on the centre-odd irreducible V_(5/2) (and on V (x) Sym^6 V), the SU(2) Wilson convolution is r_(5/2) <= M(beta), while Q_8 is r^Q8_V on all of it, 2T has r^2T_V on a copy of V, and U(1) has I_1/I_0 on a weight vector; and M(beta) < r^2T_V <= r^Q8_V, M(beta) < I_1/I_0 for every beta > 0, so the ratio is below 1 uniformly on every compact interval. **Corollary 3.7:** the degree-4 charged space V (x) Sym^4 V separates all three as well, with SU(2) norm r_(3/2). Corollary 3.5: V_(3/2) separates Q_8 and U(1).
7. The small-beta differences r^2T_V - r_(1/2) = beta^5/7680 + O(beta^7) and r^Q8_V - r_(1/2) = beta^3/48 + O(beta^5) (Section 3.3).
8. The filter is an exact factor of the full transfer L_m of EX (E1) at the original normalization; the one-slice decomposition of the odd sector by edge spins is nonnegative; the SU(2)-to-G intertwining defect of the kinetic factor is largest at (5/2, V) (Section 4.1). The plaquette spin law w_j and its normalization (4.2 (c)).

**ARGUED.** The aliasing reading of 4.2 (b): a frozen finite-group vacuum carries the invariant channels at no kinetic cost, and the filter sees the flux line meeting them. The claims in 4.4 that (HS) is the first missing arrow and that its G-analogue fails. The Q_8 version of the row-825 proof would stop at about half its range.

**GUIDE.** All decimals in Section 3.3 and 4.2 (c); the freezing couplings 1.15 (Q_8) and 2.15 (2T) (READ AS:383, from Hartung et al.); sup_F Cov_F(q) = 1/4 for 2T.

**OPEN.** (HS), a volume-uniform large-deviation bound on high-spin edges in the even one-slice law at an order-one beta above 2.15; (LS), the low-spin odd-sector bound, which carries the remaining content of (E17); a proof that Theorem V's quarter holds for 2T; whether the one-slice projections are reflection-compatible (needed for a chessboard proof of (HS)). (G22), (E17), (FQ), (V) and the mass gap remain unproved. Note on (HS): its G-analogue fails at every beta, also where G confines, so (HS) passes the binding test cheaply and does not by itself locate the confining mechanism; that is left to (LS).

**For a checker, in order.** (i) Lemma 1.5's two rows and the 2T restrictions of V_(3/2) and V_(5/2). (ii) Lemma 3.1 (c)-(d) and the three ranges in the proof of Theorem 3.4 (v), with the hand bounds e^(7/2) < 33.12, P(6) < 0.107, g(3) < 0.2157. (iii) Lemma 1.4's mixture argument. (iv) Corollary 3.7's four ranges, in particular r^2T_V(2.2) >= 1/4. (v) Prop. 2.2 (v): that nothing in VO (8)-(10) uses SU(2) beyond irreducibility of V. (vi) 4.1 (c): positivity Tr(Q L^t) = ||L^(t/2) Q||^2 for Q = P_- Pi.

**Delivery.** Only this file was written (plus the GUIDE script and its output in `scratchpad/lane843/scripts/`, 16 MB peak). No repository file, registry, PR or post was touched.

**GUIDE re-check (decides nothing).** A second script, `scratchpad/lane843/scripts/guide843b.py` (output `guide843b.out`), recomputed the rows of Lemma 1.5 from the class sums (they agree), evaluated the inequalities of Theorem 3.4 (v) and Corollary 3.7 on the grid beta = 0.01, 0.02, ..., 60 with series Bessel functions (all hold, strictly), and checked numerically that h_6 = xy(x^4 - y^4) is fixed by the 2T generator (1+i+j+k)/2 under the embedding a + bi + cj + dk -> [[a+bi, c+di], [-c+di, a-bi]] (error below 10^(-15) in both substitution conventions).

RESULT: PARTIAL, by Claude Opus 5.5 (max effort), not checked — tested every SU(2)-specific input against Q_8 and 2T (the commutator contraction (5), (6), (8)-(10) and the W_a area bound hold verbatim for both at every beta, (7) fails; (LC) fails for Q_8 at N >= 2 and for 2T at N >= 3 but holds for 2T at N = 2; (C4)-(C7) and D1 are not formulable; the moment steps of rows 817/823 are Q_8/2T-selective at couplings where nothing binds) and proved a low-spin charged filter (Theorem 3.4: on V_(5/2), and by Corollary 3.7 already on V (x) Sym^4 V, the SU(2) Wilson convolution r_(5/2) (resp. r_(3/2)) lies strictly below the Q_8, 2T and U(1) eigenvalues at every beta > 0, hence uniformly on every compact interval; at beta = 2 about 0.0010 against 0.44 for 2T); its Wilson exposure is exact, as the kinetic factor of the actual transfer L_m at the original normalization (no (G19) insertion cost; exposure density about 1% per plaquette at the crossover against 10^(-8) for spin 6), but (G20)-(G21) still let spin-1/2 flux lines avoid it; the first missing step is (HS), a volume-uniform high-spin rarity bound in the even one-slice law at an order-one beta above 2.15, followed by (LS) which carries the content of (E17); rows 778/780, 783, 804 change in scope, no proved result of rows 783-830 is refuted.
