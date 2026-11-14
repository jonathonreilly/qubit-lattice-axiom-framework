lead: anthropic/claude-opus-5-5/max laptop lane (FINISH row 844), AUTHOR
written: 2026-11-13 UTC
clone: /Users/jonreilly/ym4d-lead/clone at f1c86d81909cfef4bc95cfa244a7086b1f1599fb (2026-11-12 19:36 -0500), after `git pull --ff-only` ("Already up to date")

# gap-e17phys-opus: (E17-phys), Lemma W, the implication to (FQ), and the port (SD-cyl)

FINISH row 844, `gap-e17phys-opus`. Author: Claude Opus 5.5 at max effort, one session, by hand. **No mass gap is proved here.** No other model has checked this file. It is research text and grants no status.

**Marks.** PROVED = proved by hand in this file (not checked by another model), or proved in a named lane file with its check state. READ (path:line) = I read the statement at that line. ARGUED = a written argument with a named premise or a step I did not write in full. GUIDE = a number or belief from physics; no proof rests on it. OPEN = no proof exists.

**Paths.** D = `.claude/science/physics-loops/ym4d-hard-route-20261030` in the clone. Short names under D/library: AS = `gap-assume-opus.md` (row 838); FL = `gap-finishline-opus.md` (row 837); EX = `gap-expose-astra.md`; EXT = `gap-ext-astra.md`; SK = `gap-skeleton-final.md`; PS = `gap-phys-seed.md`; SS = `gap-seed-shape.md`; RS = `gap-crux-restate.md`; MM = `gap-means-max.md`; MB = `gap-skeleton-max-b.md`. SA L<n> = line n of the outline `YM4_sketch_500.tex` at commit `31a47c543775` (32,992 lines; sha256 starts d7f77d4da3eb2303, the same file that FL and `sa-index/` use).

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the outline, Theorem 0, Theorem 7.1, the transfer of the two-point law (their Section 7), and every statement marked READ about the account. Tadeusz Balaban: the renormalization method that the account follows. Lane authors: Codex gpt-6-astra (the consumer (FQ), (E16)-(E18)); Claude Opus 5.5 (Lemma W in AS 3.2 (b), Lemma FL in FL 2.2); Claude Fable 5.2 (Theorem SH, Lemma Z', Lemma A as used); the checks as named at each place.

**Downloads.** One file, fetched once with curl into the new empty directory `scratchpad/sa-e17/dl.yXZjcs/` (made with mktemp -d): `sa_ym4.tex` from `raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex`. Read with sed and awk by line range, never executed, never committed. The complete account (CA-I) was not fetched; the outline was enough for every READ below.

**What was read.** FINISH row 844 (D/FINISH.md L920). AS header and L405-L486 (3.2 whole). FL whole (L1-L266). EX L560-L658 (Section 7 and the end). EXT L1-L130 (contract, Section 1). SK L505-L595 (13.12 end to 13.17). PS L60-L100 (1.1.1-1.1.5) and L240-L273 (Part 3 notation, Lemmas Z, Z'). SS L87-L143 (Theorem SH, the table 1.5, the hand checks) and L8-L12 (the check note). RS L37 (Lemma A) and L129 ((TM')). MM L158, L193-L210, L254 (the sector notation and S_ev). MB L30-L31 (the measure and O(f)). `gap-transfer.md` L168-L176 (Statement (4)). FINISH rows 667, 671 (first 900 characters). In the outline: `sa-index/README.md`, the chunk-24 rows for SA L25976-L26066; SA L6905-L6977 (Theorem 0 (a)-(d)), L6848, L6885-L6888, L25970-L26066 (Theorem 7.1 and (7a)), L26765-L26866 ((ET5)-(ET7)), L26934-L27086 (the common normalizer and its transfer), L32535.

---

## 1. The objects, and (E17-phys) stated exactly

### 1.1 Units and the consumer

- **Units (READ SA L6856-L6861 via FL 1.1; SA L6911-L6915).** The unit of length is the first-passage scale of the account. A first-passage datum is a pair (K, beta) with beta in W_K(g). The spacing is a_K = L^(-K), L odd and large. The account's tori T_ell have four equal sides ell in L(g): ell = 2 L^m and ell >= ell_*(g) = 2 L^11 M R(g^-2 + B_sharp) (READ FL 1.5; SA L6913). Write ell_star for the smallest side in L(g).
- **Wilson weight and observable (READ SA L6848, L32535; MB:30-31).** a_p(U) = 1 - (1/2) Re tr U_p, and O(f) = sum_p f(x(p)) a_p(U), with x(p) the barycentre of the plaquette p. For each lattice isometry r, O(f) composed with r* equals O(r f) exactly (READ SA L6913).
- **The consumer tori (READ EXT:80-127).** n = (a, a, c, d) in lattice units, with a >= 3 and c, d in {a, 2a}. Direction 1 is time (READ MM:158). The spatial box is B = (a, c, d). The physical sides are A = a a_K, C = c a_K, D_ = d a_K.
- **Sectors and S_ev (READ MM:158).** A sector of a box B is (chi; m) in Z_2^3 x Z_2^3. Z_(chi,m)(t; B) is its sector sum at time t. e(B) := log lambda_0(B). The even sector is (0; 0), and S_ev(t; B) = Z_0(t; B)/lambda_0(B)^t - 1 >= 0. So S_ev(t; B) = sum over the eigenvalues lambda_j, j >= 1, of the untwisted transfer operator T_B on the centre-flip-invariant functions, other than one copy of lambda_0, of (lambda_j/lambda_0)^t.
- **The flux deficit (READ EX:578-583; EXT:96-122).** For a spatial twist m with m_2 = 0 and a temporal twist v_(1i), i = 3, 4: p_(m,i)(a) = Tr(P_(-,i) L_m^a)/Tr L_m^a = (1 - R_m(v_(1i)))/2, and Q_F = max over m_2 = 0, i = 3, 4 of p_(m,i)(a). Q_F depends on the consumer torus (a, a, c, d).
- **(FQ), the consumer (READ EXT:115-127).** 8 Q_F <= K(a) sqrt(S_ev(a; (a, c, d))), Q_F < 1/192, K(a) <= C_1 a^(p_1), at each of the three shapes. With (F-l) and FUSE-suff this is the input of the fusion chain (FL 2.6, (SEED-FQ); the chain is checked at rows 753 and 780).

### 1.2 The witness constants

Fix once:

- theta := 1/300 (a shape number of SA's class; any theta in (0, pi^2/2560] works below).
- g <= gamma_W(theta), the account's ceiling for this shape (READ SA L6911, L6953).
- A witness scale d with 0 < d <= d_0 = d_0(g, theta) (READ SA L6953, L25976: d_0 in (0, 1)).
- r := d/4, the radius of the bump.
- rho_* := (1/3) (2/7)^8 = 256/17294403, about 1.480e-5; log(1/rho_*) = 8 log(7/2) + log 3, about 11.121 (PROVED arithmetic).

The bump is the tent f(x) = (r - |x - x_0|)_+, centred at a point x_0 on a lattice time plane. Its properties (PROVED): f >= 0; ||f||_inf = r; Lip f = 1 = 4 ||f||_inf/d <= ||f||_inf/(theta d) since theta <= 1/4; supp f is the closed ball of radius r <= d; integral of f = 2 pi^2 integral_0^r (r - s) s^3 ds = pi^2 r^5/10 >= theta ||f||_inf d^4 = 256 theta r^5 because 256/300 < pi^2/10. The tent is invariant under the reflection of time through x_0.

### 1.3 (E17-phys)

**(E17-phys), stated exactly.** Fix theta, g, d, rho_* as in 1.2. Fix a physical side A in {2 L^m : m in N} with A >= ell_star, and a constant K_F >= 1. Fix K_0 such that, for every first-passage datum with K >= K_0: K - s(d) >= n_0 (READ SA L6953, L25976) and a_K <= d/8. Then (E17-phys) at (A, K_F) is the statement: for every first-passage datum (K, beta) at g with K >= K_0, with a = A/a_K, and at each of the three consumer tori (a, a, c, d), (c, d) in {(a, a), (2a, a), (2a, 2a)},

```math
\textbf{(E17-phys)}\qquad Q_F\;\le\;\frac{K_F}{8}\,\rho_*^{\,A/(3d)}\;=\;\frac{K_F}{8}\,e^{-\frac{\log(1/\rho_*)}{3}\,\frac{A}{d}},\qquad Q_F<\frac1{192}.
```

Every number in it is fixed before the cutoff: theta, d, rho_*, A, K_F. The rate log(1/rho_*)/(3d), about 3.707/d per unit of physical length, is a constant of the account's units.

**Corrections to AS 3.2 (c)-(d) (the form it had).** AS wrote Q_F <= (K/8) rho_*^(A/(2d)) with rho_* = ((1 - eps_0)/(1 + eps_0)) kappa_free gamma, for separations s in [d, 2d]. Four points change. (1) SA's class needs the distance between the two supports in [d, 6d] (READ SA L6953, L26007), so separations of the bump centres in [d, 2d] are not admissible for bumps of size comparable to d; I use bumps of radius d/4 and centre separations near 3d/2 and 3d. (2) With one class parameter d for both pairs, zeta_K(d) and g(d) are the same in both correlations, so gamma = 1. (3) Off the account's tori the account asserts only |eps| <= 1/2 (READ SA L6960, L25983, L26038), so eps_0 = 1/2 and the factor is 1/3. (4) The step in separation is 3d/2, so the exponent is A/(3d). The kind of statement is unchanged.

---

## 2. Lemma W (PROVED)

### 2.1 The setting

Let B be a periodic spatial box with sides at least 3. By (TM) (row 667, checked row 671; boxes with unequal sides, rows 698, 699; READ RS:129 for the weaker form (TM')) the Wilson weight has a transfer operator T = T_B in the time direction: a positive, self-adjoint, trace-class operator on the Hilbert space H_B of gauge-invariant functions of the spatial links of B. Its top eigenvalue lambda_0 is simple, and its eigenvector Omega has a continuous representative with e^(-12 beta N^3) <= Omega(u) <= e^(12 beta N^3) (READ `gap-transfer.md` L168-L176, Statement (4b)-(4c), for the cubic spatial torus of side N; the same Jentzsch argument for unequal sides is what rows 698, 699 extend; simplicity is also used in the checked Theorem SH (i), READ SS:107). The centre flips C_e, e = 2, 3, 4 (multiply every spatial link of direction e that crosses one fixed hyperplane by -1) are unitary on H_B and commute with T. Let P_ev project on the flip-invariant functions. The top eigenvector Omega is even: C_e Omega is again a top eigenvector, so C_e Omega = +-Omega by simplicity; both Omega and C_e Omega are strictly positive functions, so the sign is +. (This agrees with the lane's convention S_ev >= 0, READ MM:158.) Write mu_j = lambda_j/lambda_0 for the other eigenvalues of T on P_ev H_B, with orthonormal eigenvectors e_j; each mu_j lies in [0, 1). Then

S_ev(t; B) = sum over j >= 1 of mu_j^t (PROVED from the definition at MM:158).

**Slab objects.** Let F be a bounded real function of the links in a time slab [0, w] (the spatial links at the times 0, ..., w and the temporal links between them). Assume F is gauge invariant, centre-blind (invariant under each C_e applied at every time of the slab), and symmetric under the reflection t -> w - t. Its slab operator K_F has the kernel K_F(U, U') = the slab weight (with the half weights of the spatial plaquettes at the times 0 and w that make T symmetric) with F inserted, integrated over all links of the slab except the spatial links U at time 0 and U' at time w. So K_1 = T^w. K_F is self-adjoint, because its kernel is real and, by the reflection symmetry of F and of the slab weight, symmetric in (U, U'). K_F commutes with each C_e, because the slab weight and F are invariant under the flip applied at every time. As a kernel, |K_F| <= ||F||_inf K_1, so K_F is bounded.

**The cylinder.** The cylinder over B is the lattice B x Z. Its state is the limit n -> infinity of the Wilson states on the tori B x (Z/n). For bounded slab observables X on [0, w] and Y on [t, t + w] with t >= w, the torus mean is Tr(K_X T^(t-w) K_Y T^(n-t-w))/Tr T^n. Since T^m/lambda_0^m tends to the projection on Omega in trace norm (the distance is the sum, over all eigenvalues nu_i < 1 of T/lambda_0 other than the top one, in every sector, of nu_i^m; and nu_i^m <= nu_i nu_max^(m-1), with sum of nu_i finite because T is trace class and nu_max < 1 because lambda_0 is simple), the mean tends to <Omega, K_X T^(t-w) K_Y Omega>/lambda_0^(t+w). This limit is the cylinder mean (PROVED).

### 2.2 Statement and proof

Put c = <Omega, lambda_0^(-w) K_F Omega>, psi = lambda_0^(-w) K_F Omega - c Omega, and G(u) = <psi, (T/lambda_0)^u psi> for integers u >= 0.

**Lemma W.** (i) G(u) is the connected cylinder correlation of F and of its translate by t = u + w time steps. (ii) G is log-convex: G(u)^2 <= G(u - 1) G(u + 1) for u >= 1. If G(u) = 0 for one u >= 1, then G vanishes on [1, infinity). (iii) Let 0 <= u_1 < u_2 be integers with G(u_2) > 0. Then for every integer a >= u_2 - u_1,

```math
S_{\rm ev}(a;B)\;\ge\;\frac{G(u_1+a)}{G(u_1)}\;\ge\;\Big(\frac{G(u_2)}{G(u_1)}\Big)^{a/(u_2-u_1)} .
```

(iv) In particular G(u_2) <= G(u_1), and the even gap obeys m_ev(B) := -log mu_1 <= log(G(u_1)/G(u_2))/(u_2 - u_1).

*Proof.* (i) By 2.1 the cylinder mean of F times its translate is <Omega, K_F T^u K_F Omega>/lambda_0^(2w+u), and the mean of F is c (take Y = 1). K_F is self-adjoint, so the first mean is <phi_F, (T/lambda_0)^u phi_F> with phi_F = lambda_0^(-w) K_F Omega = psi + c Omega. Expand. (T/lambda_0)^u Omega = Omega, and <Omega, psi> = 0 by the choice of c, so both cross terms vanish and the mean is G(u) + c^2.

(ii) psi is even: K_F and Omega are even. psi is orthogonal to Omega. Put X = (T/lambda_0)^(1/2); it exists since T >= 0, and it fixes Omega. Then G(x) = ||X^x psi||^2, and for u >= 1, G(u) = <X^(u-1) psi, X^(u+1) psi> <= ||X^(u-1) psi|| ||X^(u+1) psi|| = (G(u - 1) G(u + 1))^(1/2) by the Cauchy-Schwarz inequality. In the eigenbasis, G(u) = sum over j >= 1 of mu_j^u |<e_j, psi>|^2. If G(u) = 0 for one u >= 1, every term with mu_j > 0 has <e_j, psi> = 0, so G = 0 on [1, infinity).

(iii) G(u_2) > 0 and (ii) give G(u) > 0 for every u >= 0: G(0) = ||psi||^2 > 0 since psi is not zero, and a zero at some u >= 1 would force a zero at u_2 >= 1. Let phi = X^(u_1) psi/||X^(u_1) psi||; the norm squared is G(u_1) > 0. phi is a unit vector; it is even, since X commutes with the flips; it is orthogonal to Omega, since <Omega, X^(u_1) psi> = <X^(u_1) Omega, psi> = 0. Then <phi, (T/lambda_0)^a phi> = <psi, (T/lambda_0)^(u_1 + a) psi>/G(u_1) = G(u_1 + a)/G(u_1). Write phi = sum over j >= 1 of c_j e_j with sum |c_j|^2 = 1. Then <phi, (T/lambda_0)^a phi> = sum |c_j|^2 mu_j^a <= max_j mu_j^a <= sum over j >= 1 of mu_j^a = S_ev(a; B), because a >= 1 and every term is non-negative. This is the first inequality. For the second: by (ii) the increments of log G over unit steps do not decrease, so the mean slope of log G on [u_2, u_1 + a] is at least sigma := (log G(u_2) - log G(u_1))/(u_2 - u_1). So log G(u_1 + a) >= log G(u_2) + (u_1 + a - u_2) sigma = log G(u_1) + a sigma. Exponentiate.

(iv) The eigenbasis formula shows G(u + 1) <= G(u). Let mu_1 be the largest mu_j, j >= 1. In (iii), G(u_1 + a)/G(u_1) = sum |c_j|^2 mu_j^a <= mu_1^a. With the second inequality of (iii) at a = u_2 - u_1: mu_1 >= (G(u_2)/G(u_1))^(1/(u_2-u_1)), which is the claim. QED

**Remarks.** (1) The lemma is AS 3.2 (b) with two additions: the hypothesis is G(u_2) > 0 (AS wrote G(u_1) > 0, which does not exclude G(u_2) = 0; then the bound is trivial anyway), and the proof of the cylinder limit (2.1) is written. No step of AS 3.2 (b) fails. (2) The lemma uses only (TM), the simple even top eigenvalue, and the centre-blindness and reflection symmetry of F. It holds for every symmetric model with positive transfer operators, like Theorem S (READ FL 2.1, RS:170-176). (3) Why the cylinder and not the torus: on a torus of time extent n the correlation also carries the terms lambda_i^(n-t) lambda_j^t |<e_i, K_F e_j>|^2 with i, j both excited, in all eight electric sectors. They do not give a lower bound on the even sector alone. AS 3.2 says the same (READ AS:459).

---

## 3. The physical witness and the implication to (FQ)

### 3.1 The interface input (SD-cyl), stated exactly

**(SD-cyl).** Let theta, g, d, r, K_0 be as in 1.2-1.3. Let B be a spatial box whose three physical sides are integer multiples of ell_star. Let (K, beta) be a first-passage datum with K >= K_0. Let (f, h) be a pair in SA's class T(d; theta) (READ SA L6953, L26002-L26010: f, h >= 0 Lipschitz, not zero, each supported in a ball of radius d, the distance of the supports in [d, 6d], the integral of each at least theta ||.||_inf d^4, the Lipschitz constant of each at most ||.||_inf/(theta d)), placed anywhere in the cylinder B x R (such a pair lies in one ball of radius 5d, which is what the transfer of Section 4 uses: READ SA L26807-L26808). Then the connected correlation in the cylinder state of 2.1 at (K, beta) is

```math
\langle\mathcal O(f);\mathcal O(h)\rangle_{B\times\mathbb Z}=\zeta_K(\mathsf d)^2\,\tfrac{3(N^2-1)}{\pi^4}\,g(\mathsf d)^4\,\mathcal K_{\rm free}(f,h)\,(1+\varepsilon),\qquad|\varepsilon|\le\tfrac12,
```

with the same zeta_K(d) and g(d) as on the account's tori (READ SA L6956-L6960), and K_free(f, h) = the double integral of f(x) h(y) |x - y|^(-8) (READ SA L6888, L25974).

Section 4 writes the port of (SD-cyl) from the account. This section uses it as a hypothesis.

### 3.2 Proposition W-phys (PROVED GIVEN (SD-cyl))

**Proposition W-phys.** Assume (SD-cyl). Let B = (a, c, d_) be a consumer box (lattice sides; c, d_ in {a, 2a}) whose physical sides are multiples of ell_star, at a first-passage datum with K >= K_0, and with A = a a_K >= 2d. Then

```math
S_{\rm ev}(a;B)\;\ge\;\rho_*^{\,2A/(3\mathsf d)},\qquad \rho_*=\tfrac13\big(\tfrac27\big)^8 .
```

*Proof.* (1) The witness. Take the tent f of 1.2 with centre x_0 on the time plane 0, inside the cylinder. F = O(f) depends on the plaquettes whose barycentre lies in the ball B(x_0, r). Their links lie in the time slab [-w', w'] with w' = ceil(r/a_K + 1/2), so F is a function of a slab of w = 2w' <= 2r/a_K + 3 steps. F is real and gauge invariant. F is centre-blind: each a_p is a function of U_p, and a flip changes no U_p (a plaquette contains two links of direction e or none, and both are flipped or neither). F is symmetric under the reflection of the slab, because the tent is symmetric under time reflection through x_0 and O(f) composed with r* is O(r f) (READ SA L6913). So Lemma W applies to F.

(2) The two separations. Let t_1 be the least integer with t_1 a_K >= 3d/2, and t_2 = 2 t_1. Put u_i = t_i - w. Then u_1 >= 0: t_1 a_K >= 3d/2 = 6r >= 2r + 3 a_K because a_K <= d/8 = r/2. For i = 1, 2 the pair (f, tau_(t_i) f), with tau_t the time translate by t steps, is in T(d; theta): both supports are balls of radius r <= d; the distance of the supports is t_i a_K - 2r, which lies in [d, d + a_K) for i = 1 and in [5d/2, 5d/2 + 2 a_K) for i = 2, so in [d, 6d]; the mass and Lipschitz conditions hold by 1.2 for f and for its translate. Both bumps lie in one ball of radius 2d. By Lemma W (i) and (SD-cyl), G(u_i) = Z (3(N^2 - 1)/pi^4) K_free(f, tau_(t_i) f)(1 + eps_i), with |eps_i| <= 1/2 and Z = zeta_K(d)^2 g(d)^4 the same number for i = 1, 2, because zeta_K(d) and g(d) depend only on (K, beta, d) (READ SA L6960). Z > 0: |zeta_K(d) - 1| <= eta-bar(d) <= 1/3 and g(d) > 0 (READ SA L6960).

(3) The free ratio. For x in supp f and y in supp tau_t f, |x - y| lies in [t a_K - 2r, t a_K + 2r]. So (integral of f)^2 (t a_K + 2r)^(-8) <= K_free(f, tau_t f) <= (integral of f)^2 (t a_K - 2r)^(-8). With s = t_1 a_K >= 3d/2 and r = d/4:

kappa := K_free(f, tau_(t_2) f)/K_free(f, tau_(t_1) f) >= ((s - d/2)/(2s + d/2))^8 >= (2/7)^8,

since (s - d/2)/(2s + d/2) increases in s (its derivative has the sign of 3d/2 > 0) and equals 2/7 at s = 3d/2.

(4) The ratio. G(u_2)/G(u_1) = kappa (1 + eps_2)/(1 + eps_1) >= (2/7)^8 (1/2)/(3/2) = rho_*. In particular G(u_2) > 0. By Lemma W (iv), G(u_2) <= G(u_1), so the ratio is at most 1.

(5) Lemma W (iii) with u_2 - u_1 = t_1 and the lattice time a: a >= t_1 because A >= 2d >= t_1 a_K (t_1 a_K < 3d/2 + a_K <= 2d). So S_ev(a; B) >= (G(u_2)/G(u_1))^(a/t_1). Here a/t_1 = A/(t_1 a_K) <= A/(3d/2) = 2A/(3d), and the base lies in [rho_*, 1]. So S_ev(a; B) >= rho_*^(a/t_1) >= rho_*^(2A/(3d)). QED

**Byproduct (PROVED GIVEN (SD-cyl)).** By Lemma W (iv), the even gap of every such box obeys m_ev(B) <= log(1/rho_*)/t_1 per lattice step, that is at most log(1/rho_*)/(3d/2), about 7.414/d, in physical units, uniformly in the cutoff. This is an upper bound on the even gap of the type of SK:66 (READ AS:439), now with a physical constant.

### 3.3 Corollary: (E17-phys) gives (FQ) with a constant bounded in physical units (PROVED GIVEN (SD-cyl))

**Corollary.** Assume (SD-cyl). Let A = 2 L^m >= max(ell_star, 2d), K_F >= 1, and suppose (E17-phys) holds at (A, K_F). Then for every first-passage datum with K >= K_0, at a = A/a_K and at each of the three shapes, (FQ) holds with the constant K(a) := K_F, which does not depend on the cutoff: 8 Q_F <= K_F sqrt(S_ev(a; (a, c, d_))) and Q_F < 1/192.

*Proof.* The three consumer boxes (a, c, d_) have physical sides A or 2A, multiples of ell_star (A = 2 L^m and ell_star = 2 L^(m_star) with m >= m_star; L is an integer). Proposition W-phys gives sqrt(S_ev(a; (a, c, d_))) >= rho_*^(A/(3d)). Then 8 Q_F <= K_F rho_*^(A/(3d)) <= K_F sqrt(S_ev). The strict bound is part of (E17-phys). (FQ) allows K(a) <= C_1 a^(p_1); K_F is the case p_1 = 0, C_1 = K_F. QED

**What the constants are (PROVED arithmetic).** theta = 1/300, rho_* = 1.4803e-5, rate log(1/rho_*)/3 = 3.7069 per unit of A/d. K_F is free. Downstream, FUSE-suff then asks the six even sums to be at most 1e-16/(144 K_F^2) (READ FL:170; row 751, checked row 753, holds with max(1, K)); with K_F fixed this is a fixed number. Nothing depends on beta, on K, or on a. So the beta-dependence of (E17), eta_*^(a/2) with eta_* = min over a beta interval, is gone.

**What (E17-phys) asks, in plain terms (GUIDE).** The rate is set by the account's short-distance scale d <= d_0 < 1, not by the correlation length xi. In the account's unit xi is large (FL 1.6: it grows like exp((3 pi^2/11) g^(-2)), recalled). So (E17-phys) asks Q_F <= (K_F/8) e^(-3.71 A/d) at a size A of many xi: a very small flux deficit. With an area law Q_F of order e^(-sigma A^2), and sqrt(sigma) xi about 0.28 (READ AS:455, from PS 1.4), it holds once A >= 3.71/(sigma d) + O(1/(sigma A)), that is A of about 47 xi^2/d. In units of xi this grows with xi. It is still one fixed physical size at the fixed reference coupling g, so it is cutoff-uniform, which is the point. The log-convexity of Lemma W cannot do better from short-distance data alone: the decay rate of G measured at d is an upper bound on its rate at every larger separation, and the free law 1/x^8 has a large rate at d.

**The arithmetic of AS 3.2 (a), re-checked.** For 0 < r <= 1, r^4/(4 + 16 r^4) increases in r and equals 1/20 at r = 1. And 40 x 0.3715 = 14.86. The formula for eta(beta) itself (READ there as e^(-80 beta) times that factor) I did not re-read in `gap-fusion-astra.md`; the statement that (E17) fails at fixed physical size along the sequence rests, as AS says, on one ARGUED premise (Q_F has a positive continuum limit). Not used here.

---

## 4. The port (SD-cyl): from the account's Theorem 0 (c)(3) to the consumer cylinders

Everything marked READ in 4.1 is the text of Sussman and Alpoge (with Claude and Codex). Their text states it as conditional on its packages A-H. A READ mark means "the text says this at that line", not "this is proved".

### 4.1 What the account states, and on which measures

- **Theorem 0 (c)(3) (READ SA L6953-L6960).** The class T_E(d; theta): pairs of Lipschitz f, h >= 0, not identically zero, each supported in a ball of radius d, with d <= dist(supp f, supp h) <= 6d, integral of f >= theta ||f||_inf d^4, Lip f <= ||f||_inf/(theta d), the same for h. Assume g <= gamma_W(theta), d <= d_0, the pair in T_(T_ell)(d; theta), and K - s(d) >= n_0. Then <O(f); O(h)>_(K,ell,beta) = zeta_K(d)^2 (3(N^2 - 1)/pi^4) g(d)^4 K_free(f, h)(1 + eps), with |eps| <= min{1/2, eps-bar_ell(d)}. Here g(d) = g_(K-s(d))(beta), zeta_K(d) = zeta'_(K-s(d)), |zeta_K(d) - 1| <= eta-bar(d), and eta-bar <= 1/3. The last sentence: "For periodic Gibbs states the identity remains true, but only with |eps| <= 1/2" (SA L6960).
- **The measures it covers.** The account's tori T_ell, ell in L(g) (four equal sides 2 L^m above the floor; READ SA L6911, L6913), and periodic Gibbs states at beta on the infinite lattice L_K (READ SA L25983: "every periodic Gibbs state at beta on L_K"; L26038). The limits obey the law with |eps| <= 1/2 on R^4 (READ SA L6962).
- **Theorem 7.1 (i) (READ SA L25976-L25983)** is the same statement, with d_0 = d_0(g, theta) and the bounds "uniform in (K, beta)". The index marks it "sketched" (READ `sa-index/chunk-24.md` row SA 25976-25983).
- **How the law reaches other measures (READ SA L26054).** "The local analysis is carried out on a single torus, the smallest one, T_(ell_star(g))." "Reflection positivity then carries it from this torus to the remaining volumes and to the Gibbs states." The tool is Lemma 7.6, "[outlined here; ...]" (READ SA L26062), which "transfers the law to every T_ell and every nu at a cost of C_2 d^2 ||f||_inf ||h||_inf". The threshold d_0 "is chosen at the point where these three errors combined give |eps| <= 1/2" (READ SA L26062): the reference error on T_star, the Riemann-sum error, and this transfer cost.
- **The transfer itself (READ SA L26765-L26866 and L26934-L27086).** (ET5)-(ET7) is an abstract lemma about two probability measures rho, tau, which "may be measures on different configuration spaces" (READ SA L26769). If the covariance difference D is invariant under joint lattice translations (L26774) and both measures have one common holomorphic cell normalizer E with |e^(-E) omega(e^(z_1 O(F_1) + z_2 O(F_2)))| <= Q on a source polydisc (ET5, L26782-L26787), then |D(f, h)| <= C(Q, r_0, c_M) theta^(-2) d^2 ||f||_inf ||h||_inf for pairs in one ball of radius 5d (ET7, L26807-L26827). The account supplies (ET5) for T_star and every larger T_ell by four ingredients: (a) the finite chessboard inequality on the target (L26981-L26985); (b) a pressure comparison Z_ell(W_z) <= Z_star(W_z)^((ell/ell_star)^4) by cutting in one direction at a time, "allowing rectangular tori at the intermediate stages" (L26987-L26999); (c) the floor Z_ell(0) >= exp(V_ell - C_- ell^4) on the target and the vacuum-density bound |ell^(-4) V_ell - ell_star^(-4) V_star| <= delta_vac (L26952-L26962); (d) the face series C_face, a property of the source energy on T_star alone (L27031-L27047). Then Q = exp{C_face + (C_+ + C_- + delta_vac) l_c^4} (L27051-L27053).

### 4.2 Why the clauses do not reach the consumer cylinder directly

The consumer cylinder is the lattice B x Z, B = (a, c, d_), c, d_ in {a, 2a}. It is not one of the account's tori: its sides are unequal (when c or d_ is 2a) and one side is infinite. It is not a periodic Gibbs state on L_K either: its configuration space is a different lattice, and the periodic extension of a cylinder or torus state to L_K is carried by periodic configurations, so it is not a DLR state of L_K (ARGUED; standard). So (SD-cyl) is not a clause of the account. AS 3.2 (c) says so (READ AS:441). It is, however, within reach of the account's own transfer, because (ET5)-(ET7) is stated for measures on different configuration spaces and its ingredients (a)-(d) are local or are about tori. The port below runs that transfer with the rectangular tori tau_n = B x (Z/n) as targets and then lets n grow.

### 4.3 The port in five steps

Fix theta, g, d, K_0 as in 1.2-1.3, and a first-passage datum (K, beta) with K >= K_0. Let B have physical sides that are multiples of ell_star, and let n run over the multiples of ell_star/a_K. Let tau_n be the Wilson measure at (K, beta) on the torus B x (Z/n). All its sides are multiples of ell_star.

**Step P1: the floor on rectangular tori. Lemma F (PROVED GIVEN the account's floor on its tori and its vacuum-density bound).** Let tau be a Wilson torus at (K, beta) with lattice sides n_1, ..., n_4 >= 3 and physical volume |tau| = a_K^4 n_1 n_2 n_3 n_4. Then

log Z_tau(0) >= |tau| (ell_star^(-4) V_star - delta_vac - C_-).

*Proof.* Pick ell' in L(g) with ell' >= a_K max n_i (L(g) is unbounded: the sides 2 L^m for all m beyond the floor; READ SA L6913 and FL 1.5). Put N' = ell'/a_K. Lemma A (a) (READ RS:37, from (TM)): k -> (Tr S^k)^(1/k) does not increase. In direction mu, Z(n) = Tr T_mu^(n_mu), with T_mu the transfer operator of the cross-section. So log Z(n)/n_mu does not increase when n_mu grows with the other sides fixed. Raise the four sides to N' one after the other: log Z_tau(0)/(n_1 n_2 n_3 n_4) >= log Z_(ell')(0)/N'^4. Multiply by a_K^(-4). The account's floor (READ SA L26954, the form of (ST5) used there) gives log Z_(ell')(0) >= V_(ell') - C_- ell'^4, and its vacuum-density bound (READ SA L26960-L26962) gives ell'^(-4) V_(ell') >= ell_star^(-4) V_star - delta_vac. QED

Lemma F needs the vacuum-density bound only on the account's own tori, where the account asserts it. It does not need a vacuum comparison for rectangular tori, so it does not need (ET9) for them (READ SA L26929-L26932 on when (ET9) is not proved).

**Step P2: (ET5) for tau_n with the account's normalizer (ARGUED: the account's chessboard route, line by line, with one new input, Lemma F).** Use the account's cell side l_c, with n_star = ell_star/l_c even, and its reflected source W_z (READ SA L26939-L26976). Each side of tau_n is a multiple of ell_star, so it carries an even number of cells, and W_z is defined on tau_n.

1. Chessboard on tau_n: |M_(tau_n)(z)| <= (Z_(tau_n)(W_z)/Z_(tau_n)(0))^(1/#cells), #cells = |tau_n|/l_c^4. The account uses this on T_ell (READ SA L26982-L26985). Its one-direction form (AM6) is proved for a split torus of any other sides (READ SA L2887-L2905). So the four-direction form on a rectangular torus with an even number of cells in each direction is the same argument (ARGUED; I did not read the account's complex-source version, which it uses without a separate statement).
2. Pressure comparison: 0 <= Z_(tau_n)(W_z) <= Z_star(W_z)^(|tau_n|/ell_star^4). This is the account's argument verbatim: cut in one direction at a time; the source vanishes near the cutting faces, so the crossing operator is the positive Wilson operator; Tr Y^q <= (Tr Y)^q; rectangular intermediate tori are allowed (READ SA L26987-L26999). It needs only that each side is a multiple of ell_star.
3. Upper bound on T_star: |Z_star(W_z)| <= exp{V_star + Re E_star(W_z) + C_+ ell_star^4} (READ SA L26952-L26953).
4. Floor: Lemma F.
5. Combine (PROVED arithmetic from 1-4): log |M_(tau_n)(z)| <= (l_c^4/|tau_n|) [ (|tau_n|/ell_star^4)(V_star + Re E_star(W_z) + C_+ ell_star^4) - |tau_n| (ell_star^(-4) V_star - delta_vac - C_-) ] = n_star^(-4) Re E_star(W_z) + (C_+ + C_- + delta_vac) l_c^4. This is the account's (eq:reference-cell-upper-bound) (READ SA L27006-L27010), with the same right side.
6. Face series: |n_star^(-4) Re E_star(W_z) - Re E°(z)| <= C_face, a statement about T_star only (READ SA L27045-L27047). So |e^(-E°(z)) M_(tau_n)(z)| <= Q, with the account's E° and Q (READ SA L27051-L27053), for every n.

**Step P3: the transfer (PROVED GIVEN (ET5) for the pair; the lemma (ET5)-(ET7) re-derived here).** Apply (ET5)-(ET7) to rho = mu_(T_star) and tau = tau_n. Both are torus measures, so D is invariant under joint lattice translations. The unit ball and its translates of (ET7) embed in both tori without wrapping, since all sides are at least ell_star, which is large (READ FL 1.5: ell_*(g) = 2 L^11 M R(g^-2 + B_sharp)). The bound of (ET5) is needed at every position of the ball (READ SA L26788); both measures are translation invariant, so the cell grid can be shifted to put the ball at the account's fixed place in its cell, on tau_n as on T_star. I re-derived the lemma from its text: h_omega := e^(-E) omega(e^(z.O)) is holomorphic with h_omega(0) = 1 and |h_omega| <= Q; Schwarz along rays gives |h_omega - 1| <= (Q + 1) sum c_i |z_i|, c_i = ||F_i||_sharp/r_0; on the bidisc of radii [4(Q + 1) c_i]^(-1), |h_omega - 1| <= 1/2 and |log h_omega| <= log 2; D(F_1, F_2) is the mixed derivative at 0 of log h_rho - log h_tau, because E cancels; Cauchy gives |D| <= 2 log 2 x 16 (Q + 1)^2 c_1 c_2 = 32 log 2 (Q + 1)^2 r_0^(-2) ||F_1||_sharp ||F_2||_sharp, which is (ET6) (READ SA L26798-L26801). The signed translates F^eps = sum_v eps_v tau_v f, H^eps likewise, have disjoint supports and do not increase the sup or Lipschitz norms (between two balls the segment crosses both boundaries, where the functions vanish); E_eps D(F^eps, H^eps) = N D(f, h) by bilinearity and translation invariance; with N >= c d^(-4) and ||f||_sharp <= (c_M/(theta d)) ||f||_inf for small d this gives (ET7): |S_2^T[tau_n](f, h) - S_2^T[T_star](f, h)| <= C(Q, r_0, c_M) theta^(-2) d^2 ||f||_inf ||h||_inf, uniformly in n.

**Step P4: the law on tau_n (ARGUED, conditional on the account's reference law and its choice of d_0).** On T_star the law holds with the reference error and the Riemann-sum error (READ SA L26054 (1)-(2), L26062: Proposition 7.3 and the free comparison). The main term is at least c theta^2 (ln(1/d))^(-2) ||f||_inf ||h||_inf (READ SA L26062; L26838-L26839 gives K_free >= 10^(-8) theta^2 ||f||_inf ||h||_inf in the class). The transfer cost of Step P3 has the same constant as the account's transfer to every T_ell, because Q, r_0 and c_M are the account's. The account's d_0(g, theta) makes reference error plus Riemann-sum error plus this transfer cost at most 1/2 in relative size (READ SA L26062). So, for d <= d_0 and every n: <O(f); O(h)>_(tau_n) = zeta_K(d)^2 (3(N^2 - 1)/pi^4) g(d)^4 K_free(f, h)(1 + eps_n), |eps_n| <= 1/2, with the same zeta_K(d) and g(d) as on T_star.

**Step P5: the cylinder (PROVED).** At fixed (K, beta, B, f, h), the torus covariance converges to the cylinder covariance as n -> infinity along multiples of ell_star/a_K. O(f) and O(h) are bounded local observables, and the torus mean of a bounded slab observable Z is Tr(K_Z T^(n - w_Z))/Tr T^n, which tends to <Omega, K_Z Omega>/lambda_0^(w_Z) by 2.1. The prefactor of the law does not depend on n, and |eps_n| <= 1/2 is a closed condition. So the cylinder covariance obeys the law with |eps| <= 1/2. This is (SD-cyl). QED (of the port, with the marks of P1-P5).

### 4.4 What is missing, named exactly

1. **The account's own status.** Theorem 7.1 (i) is "sketched" in the index; the argument of (7a) is "sketched"; Lemma 7.6 is "[outlined here ...]" (READ SA L26062). Its inputs (ST5) (Obligation D1, READ PS 1.1.2: "We must prove the precise torus conditions (ST5)-(ST6)", SA L4088-L4098), the vacuum-density bound from (ET8)-(ET10) (READ SA L26956-L26962), the reference law on T_star (Proposition 7.3, (7b)) and the face series are the account's. (SD-cyl) inherits exactly this conditionality, and no more.
2. **One standard fact not written in the account.** The four-direction chessboard inequality with the complex reflected source on a rectangular torus with an even number of cells in each direction (Step P2, item 1). The account proves the one-direction form for positive slab functions on split tori with arbitrary other sides (READ SA L2887-L2905) and uses the four-direction complex form on T_ell without a separate statement. ARGUED; it is the same proof.
3. **Geometric conditions.** The consumer box sides and the long time period must be multiples of ell_star. With A = 2 L^m, m >= m_star, all of A, 2A and the periods n a_K = q ell_star qualify. This is a restriction on the choice of the consumer size A, not a missing estimate.
4. **Precision.** Off the account's tori only |eps| <= 1/2 is available (as for the account's periodic Gibbs states). eps-bar_ell(d) -> 0 is not ported. Proposition W-phys needs only |eps| <= eps_0 < 1.
5. **Not missing.** No twisted run of the account is needed: the cylinder and tau_n are untwisted, and the even sector enters only through Lemma W. No uniqueness of the block law and no vacuum comparison for rectangular tori is needed (Lemma F replaces it).

So (SD-cyl) is not OPEN in the sense of AS 3.2 (c): it is a port with one new lemma (Lemma F, PROVED given the account), one standard fact (ARGUED), and the account's sketched Section 7 (READ). The marks of 3.2-3.3 are therefore: Proposition W-phys and the Corollary hold given the account's Theorem 7.1 (i) on T_star, its Lemma 7.6 route and its constants, and the four-direction chessboard on rectangular tori.

---

## 5. Check of Lemma FL (row 837; FL 2.2, L128-L134)

**Scope.** A line-by-line check of Lemma FL and of the paragraph after it, against the primary statements of Lemma Z' (READ PS:268-272) and Theorem SH with its table (READ SS:87-142). Same provider as the author of FL (Claude Opus 5.5); not an independent check in the sense of the working rules.

**Statement (READ FL:128-130).** rho >= 25 an integer, T_0 >= 3, b = rho T_0, Phi_rho(T_0) <= (rho/2) log(1 + s_0) with s_0 < 3/10; E = (6 rho/(rho - 1))^3; s_k = (3.03 s_0)^(6^k)/3.03. Claim: for every k >= 0 and every integer N with 2N >= 6^k b, S(N; (2N)^3) <= (1 + s_k)^E - 1.

**Step (1): holds.** Lemma Z' (PROVED GIVEN Lemma A, checked rows 698, 699 as PS states; row 727 per FL) needs integers T_0 >= 3, rho >= 2, b = rho T_0, and gives g(T_0; b^3) <= (2/rho) Phi_rho(T_0), with g = log(1 + S) (READ PS, proof of Lemma Z: "S = exp(g) - 1"). With the hypothesis, S(T_0; b^3) <= s_0.

**Step (2): holds.** Theorem SH with a = T_0, B = b^3, (j, p, q) = (6, 6, 12). Its hypotheses (READ SS:89): a >= 3; min b_i = rho T_0 > T_0; p divides j; p <= q; q a = 12 T_0 < rho T_0 because rho >= 25 > 12. The line r >= 24 (READ SS:126) gives K = 3.03 and x_0 = 3/10. I re-checked its hand check (READ SS:136): for rho >= 24, 2ja = 12 T_0 <= b/2, so Pi = (b/(b - 12 T_0))^3 <= 8 and C = (1/2)(Pi - 1) <= 3.5; phi(x) = e^u - 1 with u = 216 (log(1 + x^6) + C log(1 + x^12)) <= 216 x^6 (1 + 3.5 x^6); at x <= 0.3, 1 + 3.5 x^6 <= 1.00256 and u <= 0.15787 < 0.1579; e^0.1579 < 1.17105; so phi(x) <= u e^u <= 253.61 x^6 < 3.03^5 x^6 = 255.40 x^6; and K x_0 = 0.909 <= 1. The seed s = S(T_0; b^3) <= s_0 < 3/10 = x_0, and K s < 0.909 < 1. So SH (i) gives 3.03 S(6^k T_0; (6^k b)^3) <= (3.03 s)^(6^k) <= (3.03 s_0)^(6^k): the k-th sum is at most s_k. Since 3.03 s_0 < 1, s_k decreases in k. SH (ii) for the cube (r_min = r_max = rho) has E = (6 rho/(rho - 1))^3, as in FL; at L = 2N >= b and k(L) the largest k with 6^k b <= 2N it gives 1 + S(6^(k(L)) T_0; (2N)^3) <= (1 + s_(k(L)))^E. Since 6^k b <= 2N, k(L) >= k and s_(k(L)) <= s_k.

**Step (3): holds.** 2N >= 6^(k(L)) rho T_0 >= 2 x 6^(k(L)) T_0, so N >= 6^(k(L)) T_0. S(t; B) is the sum of (lambda_i/lambda_0)^t over i >= 1, each ratio in [0, 1] by (TM), so it does not increase in integer t. Hence S(N; (2N)^3) <= S(6^(k(L)) T_0; (2N)^3) <= (1 + s_k)^E - 1. **Lemma FL holds.** E <= 244.2: at rho = 25, E = 6.25^3 = 244.14, and E decreases in rho.

**The paragraph after the lemma (FL:134): holds after one correction.** (SEED-L) is a limsup: "limsup over first-passage data of Phi_L ... is at most phi_*" (READ FL:126). Lemma FL needs Phi_L(T_0) <= (L/2) log(1 + s_0) at every datum with K >= K_0. So take phi' strictly between phi_* and (L/2) log(13/10), choose K_0 with Phi_L <= phi' for K >= K_0, and put s_0 = e^(2 phi'/L) - 1 < 3/10 (FL wrote phi_* in place of phi'). The rest holds: T_0 = ell/a_K = 2 L^(m+K) >= 3; with rho = L odd, L >= 25; k_1 with E s_(k_1) <= 1/6000 exists because s_k -> 0, and depends only on (L, phi'); (1 + s)^E - 1 <= e^(E s) - 1 <= e^(1/6000) - 1 = 1.6668e-4 < 1/5041 = 1.9837e-4; with 2N = 6^(k_1) L T_0, N = 6^(k_1) L^(m+K+1) is an integer. The dilation reading Phi_L = L^4 F_(K,ell,beta) - F_(K+1,ell,beta) agrees with SA L6863-L6869 (READ: the dilation maps Lambda_(K,ell) onto Lambda_(K',L^b ell), plaquettes to plaquettes, with the same weight; so the torus T_(L ell) at cutoff K is the lattice of T_ell at cutoff K + 1 at the same beta). Note that (K + 1, beta) is then not a first-passage datum; FL says "one more block step", which is right.

**Verdict.** Lemma FL: holds, first failing step none. FL 2.2 application: holds after the correction phi_* -> phi' (no constant changes). Lemma FL can now be marked PROVED (composition of checked Lemma Z' and Theorem SH, checked here by Claude Opus 5.5, same provider as its author).

---

## 6. Status, scope, RESULT

### 6.1 The statements of this file

| Statement | Mark |
|---|---|
| (E17-phys): Q_F <= (K_F/8) rho_*^(A/(3d)), Q_F < 1/192, rho_* = (2/7)^8/3, at one physical size A = 2L^m >= ell_star, all three shapes, all first-passage data with K >= K_0 (1.3) | DEF (stated exactly) |
| Corrections to AS 3.2 (c)-(d): class distance [d, 6d]; one class parameter, so gamma = 1; eps_0 = 1/2 off the account's tori; exponent A/(3d) | PROVED (from READ SA L6953-L6960, L25983) |
| Lemma W (i)-(iv), including the cylinder limit and the even-gap bound (2.2) | PROVED (by hand; uses (TM), checked rows 671, 698, 699, and the simple even top eigenvalue) |
| Proposition W-phys: S_ev(a; B) >= rho_*^(2A/(3d)) on every consumer box with sides multiples of ell_star, uniformly in the cutoff (3.2) | PROVED GIVEN (SD-cyl) |
| Byproduct: m_ev(B) <= 7.42/d in physical units on the consumer boxes (3.2) | PROVED GIVEN (SD-cyl) |
| Corollary: (E17-phys) at (A, K_F) gives (FQ) with K(a) = K_F, a cutoff-independent constant, at the three shapes (3.3) | PROVED GIVEN (SD-cyl) |
| Theorem 0 (c)(3) and Theorem 7.1 (i) cover the account's tori and periodic Gibbs states on L_K; the transfer route of Lemma 7.6 and (ET5)-(ET7) (4.1) | READ (SA L6953-L6962, L25976-L25983, L26038, L26054-L26066, L26765-L26866, L26934-L27086); index status "sketched", Lemma 7.6 "outlined" |
| The cylinder is neither an account torus nor a periodic Gibbs state on L_K (4.2) | ARGUED (standard) |
| Lemma F: the floor log Z_tau(0) >= abs(tau)(ell_star^(-4) V_star - delta_vac - C_-) on every rectangular torus (4.3 P1) | PROVED GIVEN the account's floor on its tori and its vacuum-density bound (READ SA L26954, L26960-L26962) |
| (ET5) for tau_n = B x (Z/n) with the account's E° and Q (4.3 P2) | ARGUED (the account's chessboard route; the four-direction complex chessboard on rectangular tori is standard and not written in the account) |
| (ET6)-(ET7) re-derived; transfer to tau_n uniformly in n (4.3 P3) | PROVED GIVEN (ET5) |
| The law on tau_n with abs(eps) <= 1/2, same zeta_K(d), g(d) (4.3 P4) | ARGUED, conditional on the account's reference law on T_star (Proposition 7.3) and its choice of d_0 (READ SA L26062) |
| Passage n -> infinity to the cylinder (4.3 P5) | PROVED |
| (SD-cyl) as a whole | ported: conditional on the account's Section 7 exactly as Theorem 0 (c)(3) is, plus one standard chessboard fact; not OPEN |
| Lemma FL of row 837 | holds (checked here, same provider); FL 2.2 application holds after replacing phi_* by any phi' in (phi_*, 0.131 L) |
| (E17-phys) itself at any coupling; the flux deficit Q_F at a physical size; the glue half (six even sums at most 1e-16/(144 K_F^2)) | OPEN |
| The size at which an area law would give (E17-phys): A of about 47 xi^2/d | GUIDE |

### 6.2 What this file did not cover

1. No proof in the account was checked; only statements and the short arguments at the cited lines. CA-I, CA-II, CA-III were not fetched. The account's status for every input of the port is "sketched" or "outlined" (index chunk 24), and conditional on its packages (D1, F above all).
2. The four-direction chessboard inequality with a complex reflected source on rectangular tori is used, not proved (4.3 P2, item 1). The account's one-direction form (AM6) was read at its statement only (SA L2887-L2905).
3. The definition of eta(beta) and the claim that (E17) fails at fixed physical size (AS 3.2 (a)) were not re-derived; only the arithmetic was re-checked.
4. (TM) was read only at its Statement (4) (`gap-transfer.md` L168-L176: positivity improving, simple top eigenvalue, strictly positive ground state, for the cubic spatial torus), and its extension to unequal sides is taken from FINISH rows 698, 699 as FL cites them, not re-read.
5. No other model checked this file. The check of Lemma FL is by the same provider as its author.

### 6.3 Items the lead may queue (suggestions only)

1. A cross-provider check of Lemma W, Proposition W-phys and Lemma F (short; Sections 2, 3.2, 4.3 P1).
2. A check that the account's d_0(g, theta) and its transfer constant cover a target whose (ET5) is supplied as in 4.3 P2 (one reading of SA L26934-L27086 against L26062).
3. The four-direction complex chessboard on rectangular tori with even cell numbers, written once, so that P2 needs no ARGUED step.

RESULT: (E17-phys) is stated exactly as Q_F <= (K_F/8) rho_*^(A/(3d)) and Q_F < 1/192 at one physical size A = 2L^m >= ell_star and all three consumer shapes, with rho_* = (2/7)^8/3 (rate about 3.71/d per unit of A, d <= d_0 the account's short-distance scale); Lemma W is PROVED (cylinder limit, log-convexity, S_ev(a;B) >= G(u_1+a)/G(u_1) >= (G(u_2)/G(u_1))^(a/(u_2-u_1)), and the even-gap bound); given (SD-cyl), Proposition W-phys gives S_ev(a;B) >= rho_*^(2A/(3d)) uniformly in the cutoff and (E17-phys) gives (FQ) with a cutoff-independent constant K = K_F (PROVED GIVEN (SD-cyl)), after four corrections to AS 3.2 (class distance [d,6d], gamma = 1, eps_0 = 1/2, exponent A/(3d)); the port (SD-cyl) is written: the account's Theorem 0 (c)(3) and Theorem 7.1 (i) (SA L6953-L6960, L25976-L25983; "sketched") cover only its tori and periodic Gibbs states on L_K, but its own transfer, Lemma 7.6 with (ET5)-(ET7) (SA L26765-L26866, L26934-L27086; "outlined"), carries the law with |eps| <= 1/2 to the rectangular tori B x (Z/n) and then to the cylinder, given a new floor lemma for rectangular tori (Lemma F, PROVED from the account's floor and vacuum-density bound by Lemma A) and one standard fact not written in the account (the four-direction complex chessboard on rectangular tori with even cell numbers, ARGUED), with box sides multiples of ell_star; so (SD-cyl) is conditional on the account's Section 7 and no longer OPEN; Lemma FL of row 837 holds (first failing step none; its application needs phi' in (phi_*, 0.131L) in place of phi_*); (E17-phys) itself, the flux deficit at a physical size, and the glue half remain OPEN.
