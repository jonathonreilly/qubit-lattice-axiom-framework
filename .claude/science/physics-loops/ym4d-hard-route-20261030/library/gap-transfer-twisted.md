lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T03:55Z

# The transfer operator of a twisted box: (TM-tw) as a lemma of its own

Written in queue row 1004 (`gap-outside-box-max`, Section 7 there) by Claude Fable 5.2, max effort, Mac mini worker 2, at commit 95fecd964, 2026-11-15. Research text, not an audit; it grants no status. No numeric run was made; every step is by hand.

**Status.** Theorem TW-T below is PROVED by hand, given Statements (1) to (4) and Lemmas A0 to A3 of `library/gap-transfer.md` (row 667; checked line by line by Codex gpt-6-astra, row 671). **This file is checked by no one.** No mass gap is proved here and nothing here bears on the size of any gap.

## 0. Why this file, repo search, credits

**Why.** Every statement of the gap lane that reads a twisted partition function uses one input, called (TM-tw): the transfer operator of a box whose spatial plaquettes carry a twist is again positive, trace class, with a simple top eigenvalue, and the twisted partition functions are its traces with centre flips. Theorem R, the full and kappa seeds and the fusion consumer rest on it (`gap-assume-opus.md` rows 58 and L265). It was stated as an input in `gap-flux-exercise.md` 3.0, with the work item "Write `library/gap-transfer-twisted.md` ... each step written from `gap-transfer.md` Sections 1 to 4 and 9.3 (not 'word for word')" (L660, item 2 of row 731), and again in the ledger of row 838 ("proposed in row 731, never queued. Cheap."). Until now it lived in two check files.

**Repo search (rule 0a), before writing.** `library/open-core.md`: no entry. FINISH: "TM-tw" occurs once (`grep -c -F "TM-tw" FINISH.md` = 1), in the result of row 838 itself, which lists "write (TM-tw) as a lemma" among its ideas; no row was queued for it; "transfer-twisted" has no hit. (My search before writing used a pattern with fixed context lengths and missed that one line; the count above was made after writing. It changes nothing: the line is a proposal, not a claim on the item.) `ls library | grep -i twist`: `gap-twist-chart.md`, `gap-twist-port.md`, `twisted-order-calculus.md` (other subjects); no `gap-transfer-twisted.md`. Places where the content already stands, all used and credited here:
- `gap-transfer.md` Sections 1 to 4 and 9.3 (Claude Opus 5.5; the untwisted cube, and the flips).
- `gap-seed-check.md` Lemma 1.1 (L30-34) and Remark F3 (L177) (Claude Opus 5.5, check row 698): every box with sides at least 3; one electric plane; the remark that a twisted spatial potential keeps the proof.
- `gap-crux-fp-check.md` L30-38 (not re-read here; named by the work item as a second source).
- `gap-flux-exercise.md` 3.0 and 3.1, C2 (Claude Fable 5.2, row 731; checked by Codex gpt-6-astra, row 732: "The input (TM-tw), including Pf(k)=1: HOLDS"): the statement, the sector sums (F1), the inequalities (S1) to (S3).
- `gap-assume-opus.md` L494 (Claude Opus 5.5, row 838): the frame proof of Z^k <= Z^0.

So nothing below is new mathematics. What is new is that the statement and its proof are in one place, with every step that differs from `gap-transfer.md` written out.

**Credits.** Osterwalder and Seiler, and Luescher, for the lattice transfer operator (not read; rebuilt in `gap-transfer.md`). 't Hooft for twists and flux sectors (not read). Sussman and Alpoge, with Claude and Codex as authors of their text, for the layer operator ported in `gap-transfer.md`. The rows named above.

## 1. Setting

1.1 (The box; from `gap-transfer.md` N.1 to N.8.) G = SU(2) with normalized Haar measure. N_1, N_2, N_3 >= 3. Lambda = Z/N_1 x Z/N_2 x Z/N_3, |Lambda| = N_1 N_2 N_3. Spatial links E = {(x, i) : x in Lambda, i in {1,2,3}}, |E| = 3 |Lambda|. X = G^E with product Haar measure du, H = L^2(X, du). Spatial plaquettes: for x in Lambda and 1 <= i < j <= 3, u_p = u_(x,i) u_(x+e_i,j) u_(x+e_j,i)^(-1) u_(x,j)^(-1); x is the base point of p and (i, j) its plane. Gauge group 𝒢 = G^Lambda, (h.u)_(x,i) = h(x) u_(x,i) h(x+e_i)^(-1). One-bond kernel c(g) = exp(-beta (1 - (1/2) tr g)), and K_0(u, v) = product over links l of c(u_l v_l^(-1)). (Pf)(u) = integral over 𝒢 of f(h.u) dh. C_E is the integral operator with kernel K_0.

1.2 (Magnetic twist.) m = (m_12, m_13, m_23) in Z_2^3. The **stack** of the spatial plane (i, j) is the set of spatial plaquettes in that plane with base point x, x_i = x_j = 0 (one for each value of the third coordinate). eps^m_p = -1 if p lies in the stack of a plane with m_ij = 1, and +1 otherwise. (Stacks of different planes are disjoint.)

  V_m(u) = beta sum over spatial plaquettes p of (1 - (1/2) eps^m_p tr u_p).

M_m is the multiplication by exp(-V_m/2). T_m = M_m C_E M_m, with kernel T_0,m(u, v) = exp(-V_m(u)/2) K_0(u, v) exp(-V_m(v)/2). T_(P,m) = P T_m P. For m = 0 these are V, M, T, T_P of `gap-transfer.md` on the box Lambda.

1.3 (Flips.) For k in {1,2,3}, Z_k is the map of X that changes the sign of u_(x,k) for every x with x_k = 0. (C_k f)(u) = f(Z_k u). For e in Z_2^3, Z^e is the composition of the Z_k with e_k = 1, and C^e the product of the C_k with e_k = 1. For chi in {+1,-1}^3 put chi(e) = product of the chi_k with e_k = 1, and P_chi = product over k of (1/2)(1 + chi_k C_k).

1.4 (The four-dimensional lattice and its twists.) Directions 0 (time), 1, 2, 3. The lattice is Lambda x Z/T, T >= 2. A configuration is (U(t), g_t), t in Z/T, with U(t) in X the spatial links of slice t and g_t in 𝒢 the time-like links from slice t to slice t+1. A **twist** is a pair (e, m) in Z_2^3 x Z_2^3: e_k for the plane (0, k), m_ij for the plane (i, j). The sign field s = s^(e,m) on the plaquettes of the lattice is -1 on
- the spatial plaquettes of every slice that lie in the stack of a plane (i, j) with m_ij = 1, and
- the time-like plaquettes in a plane (0, k) with e_k = 1 that are based at (x, T-1) with x_k = 0,
and +1 on all others. The twisted action and partition function are

  S^(e,m)(U) = beta sum over plaquettes P of (1 - (1/2) s_P tr U_P),  Z^(e,m)_T(Lambda) = integral of exp(-S^(e,m)) over all links (normalized Haar measure).

Every Z^(e,m) is strictly positive (the integrand is). On a stack the weight exp(-beta (1 - (1/2) tr U_P)) is replaced by exp(-beta (1 + (1/2) tr U_P)); this is the corrected wording of row 698. Section 3.5 shows that Z does not depend on where the stacks sit, so this is the Z^k of `gap-flux-exercise.md` 3.0 (stacks at base points x_mu = x_nu = 0).

## 2. Statement

**Theorem TW-T ((TM-tw); PROVED by hand, given `gap-transfer.md` Statements (1) to (4) and Lemmas A0 to A3).** Let beta > 0, N_1, N_2, N_3 >= 3, m in Z_2^3, T >= 2.

- **(T1) The operator.** T_(P,m) = T_m P = P T_m is the integral operator on H with the kernel A_m(u, v) = integral over 𝒢 of T_0,m(u, h.v) dh. A_m is real, symmetric, continuous, invariant under gauge transformations of each argument, and exp(-12 beta |Lambda|) <= A_m <= 1.
- **(T2) Positive, trace class.** T_m and T_(P,m) are bounded, self-adjoint and positive (as operators), Hilbert-Schmidt with norm at most 1, and trace class with Tr T_(P,m) <= Tr T_m = integral of exp(-V_m) du <= 1.
- **(T3) Top eigenvalue.** T_(P,m) improves positivity. lambda_m := ||T_(P,m)|| is a simple eigenvalue, exp(-12 beta |Lambda|) <= lambda_m <= 1. Its unit eigenvector Omega_m has a continuous representative with exp(-12 beta |Lambda|) <= Omega_m <= exp(12 beta |Lambda|); Omega_m is gauge invariant; and lambda_m is also the simple top eigenvalue of T_m on all of H.
- **(T4) Flips.** Each C_k is a unitary self-adjoint involution of H that maps almost-everywhere positive functions to such functions. The C_k commute with each other, with M_m, C_E, P, T_m and T_(P,m). Omega_m is even: C_k Omega_m = Omega_m for k = 1, 2, 3.
- **(T5) Traces.** For every e in Z_2^3: Tr(T_(P,m)^T C^e) = Z^(e,m)_T(Lambda).
- **(T6) Sectors.** Z_(chi,m)(T) := Tr(T_(P,m)^T P_chi) >= 0, and
  (F1) Z^(e,m) = sum over chi of chi(e) Z_(chi,m),  Z_(chi,m) = (1/8) sum over e of chi(e) Z^(e,m).
- **(T7) Positions and frames.** On a four-dimensional torus with all sides at least 3, the twisted partition function does not depend on the positions of the stacks, and it is carried into itself by every permutation of the four axes, the twist being carried along. So (T1) to (T6) hold with any of the four directions as time; the planes through the time direction are the electric ones.
- **(T8) Inequalities.** (S1) Z_(chi,m) <= Z_(0,m), where 0 is the sector chi = (+,+,+). (S2) 0 < Z^(e,m) <= Z^(0,m), and Z^k <= Z^0 for every twist k on a torus with all sides at least 3. (S3) lambda_m <= lambda_0 for every box with sides at least 3, lambda_0 the top eigenvalue of the untwisted box.

## 3. Proof

### 3.1 What the proof of `gap-transfer.md` uses of the cube and of V

I went through Sections 1 to 4 of `gap-transfer.md` (read in full for this file) and list every use.

(i) The cube enters through the numbers |V| = N^3, |E| = 3 N^3, the number 3 N^3 of spatial plaquettes, the constants exp(-c beta N^3), and step 1.1 (each plaquette of the space-time lattice is a spatial plaquette of one slice or the time-like plaquette of one (x, i, t); for T >= 2 the time-like ones are distinct). None of these uses equal sides. With N^3 replaced by |Lambda| they hold for the box of 1.1 (this is Lemma 1.1 of `gap-seed-check.md`).

(ii) The potential V enters through three properties only:
- (v1) V is real and continuous on X (N.4; used in 1.3, 1.4 for continuity of the kernels);
- (v2) 0 <= V <= 6 beta N^3 (N.4; used in 1.4 for exp(-12 beta N^3) <= T_0 <= 1, in 2.1 for the bound 1, in 3.3 for Tr T = integral of exp(-V) <= 1);
- (v3) V(h.u) = V(u) (N.5; used in 1.2, 1.4, 4.2, 4.3);
and through the identity of step 1.2: the part of the action S carried by the spatial plaquettes of slice t is V(U(t)).

(iii) V_m has (v1) to (v3), with 6 beta |Lambda|: (v1) tr u_p is a polynomial in the entries; (v2) tr u_p lies in [-2, 2], so each of the 3 |Lambda| terms 1 - (1/2) eps tr u_p lies in [0, 2]; (v3) (h.u)_p = h(x) u_p h(x)^(-1) has the same trace, and eps^m_p does not depend on u. And the part of S^(0,m) carried by the spatial plaquettes of slice t is V_m(U(t)), by the definition of s^(0,m) in 1.4; the time-like plaquettes of S^(0,m) are untwisted.

### 3.2 (T1), (T2), (T3), and (T5) for e = 0

By 3.1, the proofs of Statements (1), (2), (3), (4) of `gap-transfer.md` run with (Lambda, V_m, S^(0,m)) in place of (the cube, V, S). I name the steps, so that nothing is taken "word for word":
- Step 1.2 gives exp(-S^(0,m)(U)) = product over t of T_0,m(U(t), g_t.U(t+1)). Steps 1.3 to 1.6 give (T1): the integral over the g_t, the continuity, the bounds (exp(-V_m/2) >= exp(-3 beta |Lambda|) twice and K_0 >= exp(-6 beta |Lambda|)), the invariances, the symmetry, and T_m P = S_(A_m) = P T_m. Step 1.7 gives Z^(0,m)_T = Tr(T_(P,m)^T): (T5) for e = 0.
- Steps 2.1 to 2.4 give boundedness, self-adjointness and positivity: <f, T_m f> = <M_m f, C_E M_m f> >= 0 because C_E >= 0 (2.3 there; K_0 is not changed by the twist) and M_m is a real bounded multiplication. Steps 3.1 to 3.3 give Hilbert-Schmidt, compact, trace class and the trace integral of exp(-V_m). This is (T2).
- Step 4.1 applies Lemma A3 (Jentzsch, rebuilt there) to the kernel A_m with kappa_1 = exp(-12 beta |Lambda|), kappa_2 = 1: positivity improving, simple top eigenvalue, continuous positive eigenvector with the two bounds. Step 4.2 gives gauge invariance of Omega_m from A_m(h.u, v) = A_m(u, v). Step 4.3 gives the statement for T_m on all of H. This is (T3).

### 3.3 (T4): the flips

This is 9.3 of `gap-transfer.md`, with the one new point that V_m is flip-invariant for every m.

(a) u_p(Z_k u) = u_p(u) for every spatial plaquette p. Let p be based at x in the plane (i, j). If k is neither i nor j, p contains no link of direction k. If k = i, the links of direction k in p are (x, i) and (x + e_j, i); they have the same k-coordinate x_i, so Z_k changes the sign of both or of neither, and -1 is central: u_p is multiplied by (-1)^2 or by 1. If k = j, the links are (x + e_i, j) and (x, j), with the same k-coordinate x_j; the same holds. Hence V_m(Z_k u) = V_m(u) for every m.
(b) K_0(Z_k u, Z_k v) = K_0(u, v), because (-u_l)(-v_l)^(-1) = u_l v_l^(-1). Z_k(h.u) = h.(Z_k u), because -1 is central. Z_k preserves du (multiplication of some coordinates by the fixed element -1), and Z_k Z_k = identity. The Z_k commute with each other.
(c) So C_k is unitary, C_k^2 = 1, C_k^* = C_k^(-1) = C_k. By (a) it commutes with M_m; by (b) and the substitution v -> Z_k v with C_E; by (b) with P; hence with T_m and T_(P,m). It maps a.e.-positive functions to a.e.-positive functions.
(d) C_k Omega_m is a positive unit eigenvector of T_(P,m) for lambda_m. By simplicity it is z Omega_m with |z| = 1, and z = 1 because both are positive.

### 3.4 (T5): the trace with flips

Let e in Z_2^3. By the substitution w = Z^e v (a measure-preserving involution), (T_(P,m) C^e f)(u) = integral of A_m(u, v) f(Z^e v) dv = integral of A_m(u, Z^e w) f(w) dw. So T_(P,m) C^e is the integral operator with the bounded continuous kernel A_m(u, Z^e w). T_(P,m)^(T-1) is the integral operator with the (T-1)-fold composed kernel (Lemma A0 (e)). By Lemma A0 (e) for the product of these two Hilbert-Schmidt operators,

  Tr(T_(P,m)^T C^e) = integral over u(0), ..., u(T-1) of [ product over t = 0, ..., T-2 of A_m(u(t), u(t+1)) ] A_m(u(T-1), Z^e u(0)).

Write each A_m as its integral over the gauge group (step 1.3 of `gap-transfer.md`), with g_t the integration variable of the t-th factor and U(t) = u(t). The integrand becomes

  [ product over t <= T-2 of T_0,m(U(t), g_t.U(t+1)) ] T_0,m(U(T-1), g_(T-1).Z^e U(0)).

All factors are bounded and continuous on a compact space, so Fubini applies. In the last factor: V_m(g_(T-1).Z^e U(0)) = V_m(U(0)) by (v3) and 3.3 (a), so the potentials are those of S^(0,m). And K_0(U(T-1), g.Z^e U(0)) is the product over the links (x, i) of c applied to

  U(T-1)_(x,i) ( sigma g(x) U(0)_(x,i) g(x+e_i)^(-1) )^(-1),  sigma = -1 if e_i = 1 and x_i = 0, sigma = +1 otherwise.

By tr a = tr a^(-1) this has the trace sigma tr( g(x) U(0)_(x,i) g(x+e_i)^(-1) U(T-1)_(x,i)^(-1) ), and by step 1.1 of `gap-transfer.md` the argument of this trace is the holonomy of the time-like plaquette in the plane (0, i) based at (x, T-1). With c(-g) = exp(-beta (1 + (1/2) tr g)), the last factor carries exactly the signs of s^(e,m) on the time-like plaquettes of the step from slice T-1 to slice 0. The other factors are those of 3.2. So the integrand is exp(-S^(e,m)(U)), and the integral is Z^(e,m)_T(Lambda).

### 3.5 (T7): positions of the stacks, and exchange of axes

Now a four-dimensional torus with sides n_mu >= 3 (mu = 0, 1, 2, 3) and a general sign field: for each plane (mu, nu) with k_(mu nu) = 1 the sign is -1 on the stack Sigma_(mu nu)(b, c) = {plaquettes in the plane (mu, nu) with base point x, x_mu = b, x_nu = c}, for some positions (b, c) chosen for that plane.

**Lemma P (a stack can be moved).** The twisted partition function does not change when the position b of one stack is replaced by b + 1 (or c by c + 1).
Proof. Change the sign of every link (y, nu) with y_mu = b + 1 and y_nu = c. This is a measure-preserving involution of the link variables. Its effect on a plaquette P based at x: (1) P in a plane without nu holds no link of direction nu: no change. (2) P in a plane (nu, rho), rho different from mu and nu: its two links of direction nu are (x, nu) and (x + e_rho, nu), with the same mu- and nu-coordinates; both change or neither: no change. (3) P in the plane (mu, nu): its links of direction nu are (x, nu) and (x + e_mu, nu), with mu-coordinates x_mu and x_mu + 1 and the same nu-coordinate. Exactly one of them changes if and only if x_nu = c and x_mu is b or b + 1 (the two cannot both change, because that would need x_mu = b + 1 and x_mu + 1 = b + 1). So tr U_P changes sign exactly on Sigma_(mu nu)(b, c) and on Sigma_(mu nu)(b+1, c). The sign field of the plane (mu, nu) is multiplied by -1 on both stacks: the stack moves from b to b + 1. The other planes are untouched. The roles of mu and nu are symmetric. QED

**Exchange of axes.** Let sigma be a permutation of the four directions. The relabelling x -> sigma x of the sites carries links to links, plaquettes of the plane (mu, nu) to plaquettes of the plane (sigma mu, sigma nu), stacks to stacks, and the product Haar measure to itself. So Z^(sigma k)(sigma n) = Z^k(n), with any positions by Lemma P. (For k = 0 and one plane this is (v) of Lemma 1.1 in `gap-seed-check.md`.)

So for any direction mu taken as time, relabel mu as 0 and move the stacks to the positions of 1.4: the planes through mu give e, the three others give m, and (T1) to (T6) hold for the box of the three other sides. In particular the definition of 1.4 (time-like stacks at the step from T-1 to 0) agrees with the convention of `gap-flux-exercise.md` 3.0 (base points x_mu = x_nu = 0).

### 3.6 (T6) and (T8)

(T6). By (T2) and Lemma A2 of `gap-transfer.md`, T_(P,m) has an orthonormal system of eigenvectors with positive eigenvalues lambda_i, each eigenspace of finite dimension, and it vanishes on the orthogonal complement. Each C_k commutes with T_(P,m), so it maps each eigenspace into itself; the three commuting self-adjoint involutions can be diagonalized together there. In such a basis, completed by a basis of the kernel, C^e has the eigenvalue chi_i(e) on the i-th vector, with chi_i in {+1,-1}^3. The trace of a product of two Hilbert-Schmidt operators does not depend on the basis (Lemma A0 (b)). So

  Z^(e,m) = Tr(T_(P,m)^T C^e) = sum over i of chi_i(e) lambda_i^T,  Z_(chi,m) = Tr(T_(P,m)^T P_chi) = sum over i with chi_i = chi of lambda_i^T >= 0.

P_chi is the projection on the joint eigenspace, and the sum over chi of chi(e) P_chi is C^e; this gives the first identity of (F1). The second is the inversion: (1/8) sum over e of chi(e) chi'(e) is 1 if chi = chi' and 0 otherwise.

(T8). (S1): by (F1), Z_(0,m) - Z_(chi,m) = (1/8) sum over e of (1 - chi(e)) Z^(e,m) >= 0, because every Z^(e,m) > 0. (S2), first part: Z^(e,m) > 0 because the integrand is positive, and Z^(e,m) = sum of chi_i(e) lambda_i^T <= sum of lambda_i^T = Z^(0,m). Second part, on a torus with all sides at least 3 (`gap-flux-exercise.md` C2, `gap-assume-opus.md` L494): with direction 0 as time the first part removes the planes through 0; with direction 1 as time (by (T7)) it removes the planes (1, 2) and (1, 3) from what is left; the remaining plane (2, 3) is electric with direction 2 as time and is removed in a third step. So Z^k <= Z^0. (S3): for a fixed box, Z^(0,m)_T = sum over i of lambda_i^T lies between lambda_m^T and lambda_m^(T-1) Tr T_(P,m), so its T-th root tends to lambda_m as T grows; the same for m = 0. For T >= 3 all four sides are at least 3 and Z^(0,m)_T <= Z^(0,0)_T by (S2). Hence lambda_m <= lambda_0. QED

## 4. What this does not give

- No bound on a gap, a flux energy or a thermal sum. The constants exp(-12 beta |Lambda|) degenerate with the volume and the coupling, as in `gap-transfer.md` 9.1.
- Nothing on the account's effective actions on twisted tori (`gap-finishline-opus.md` 2.4, item 4: "The twisted forms are outside the account's present scope").
- Statement (5) of `gap-transfer.md` (a positive gap of the finite box) was not needed and is not ported. It holds for T_(P,m) by the same proof (compactness, positivity, positivity improvement), but I did not go through its steps 5.3 to 5.7 for V_m.
- The remark "including Pf(k) = 1" of the check of row 732 is not used: no statement above depends on the parity of e.m.

## 5. For the checker

Points to test first. (1) 3.1 (ii): is the list of uses of V in `gap-transfer.md` Sections 1 to 4 complete? (2) 3.3 (a): the two links of direction k in a plaquette have the same k-coordinate. (3) 3.4: the sign sigma and the identification of the flipped plaquettes with the stack of 1.4. (4) Lemma P, case (3): exactly the two stacks change. (5) (S3): the limit of the T-th root, and the use of T >= 3.

RESULT: (TM-tw) is written as one lemma with its proof (Theorem TW-T, PROVED by hand given `gap-transfer.md` Statements (1) to (4) and Lemmas A0 to A3; checked by no one): for every box with sides at least 3 and every magnetic twist m, the operator T_(P,m) is positive and trace class with a simple top eigenvalue and an even, positive, gauge-invariant ground state; it commutes with the centre flips; Tr(T_(P,m)^T C^e) equals the twisted partition function for T >= 2; the partition function does not depend on the stack positions and is carried along by permutations of the axes; the sector sums are non-negative with (F1); and Z^k <= Z^0, lambda_m <= lambda_0. The content was on file in `gap-seed-check.md` (Lemma 1.1, Remark F3) and `gap-flux-exercise.md` (3.0, C2); nothing new is claimed beyond the single written proof. Open: a check by another model.
