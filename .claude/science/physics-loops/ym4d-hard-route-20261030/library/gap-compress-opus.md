lead: anthropic/claude-opus-5-5/max laptop lane (FINISH row 839)
written: 2026-11-13 UTC

# gap-compress-opus: does any compression or information theory give a handle on the crux?

FINISH row 839, `gap-compress-opus`. Owner: "spin up an opus 5.5 max lane on if any compression theory could matter here". Author: Claude Opus 5.5 at max effort, one session, on the lead's MacBook, no subagents. **No mass gap is proved here.** Nothing in this file is checked by another model.

**Pins.** Lane clone `/Users/jonreilly/ym4d-lead/clone` at commit `7f5a581faaf2a0607c6f315da65fd326a677e0b7` (2026-11-12 19:07 -0500, "docs(ym4d): add row 839, compression and information theory lane"), after `git pull --ff-only` ("Already up to date"). Lane directory D = `.claude/science/physics-loops/ym4d-hard-route-20261030`. Paths below are relative to D unless they start with `/`. No repository file was edited. The shared clone advanced during this session to `261ef7fb5c3e4d82ad6bcc332a9b8707f82ca1e9` (records of rows 833, 835, 836, 838, 844, checks 840, 841, new rows 842-848; eight files changed: FINISH.md and seven new lane outputs). None of the files cited here changed, and FINISH rows 818, 820, 832 are unchanged; the new lane outputs were not read (other lanes' work).

**Marks.** READ (path:line) = read by me at that line of a lane file. Statements about the account of Sussman and Alpoge are READ only through `library/gap-finishline-opus.md`, which quotes their text; I did not open their sources. PROVED = proved by hand in this file, not checked by another model. ARGUED = an argument with a step not written in full, or a composition not checked. GUIDE = a recalled literature statement or belief, or a numeric run; used in no proof. OPEN = no proof exists. Literature below is recalled from memory and was not opened in this session; every such statement is GUIDE unless a lane file READ it.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the account whose last scale fixes the finish line. Lane authors as named at each place: Claude Fable 5.2 (Theorem S, Theorem SH, Lemma Z', Identity L, Proposition TW, Theorem R, Identity FL, the two skeleton runs that first read the doubling defect as a Renyi-2 entropy); Codex gpt-6-astra (Lemma DC with (vMF-Lip) giving (AS-bg) below 2/3, (E16)-(E25), (TR-F), the seam costs, the periodic Villain theorem); Claude Opus 5.5 (the finish line of row 837, the area law, the Langevin gap, the guide runs of rows 820 and 832, checks). Outside authors are named where their ideas are used.

## 0. Repo search (rule 0a), reading state, scope

**Search before writing.** `grep -rli` over `library/` and `library/prior/` for: data processing, mutual information, contraction coefficient, strong data, SDPI, rate-distortion, Kolmogorov complexity, information bottleneck, tensor network, matrix product, relative entropy, Renyi, min-entropy, purity, entanglement, hypercontractivity, broadcast, OSSS, decision tree. Hits that bind this file:

- The doubling defect 2F(k, box) - F(2k, box) is already read as the Renyi-2 entropy of the state T^k/Tr T^k: READ `library/gap-skeleton-max.md:264-266` (run 1, Lemma 4) and `library/gap-skeleton-max-b.md:272` (run 2). `library/gap-skeleton-final.md:172` notes the two runs found it separately. Run 1 names the missing statement as an entropy change caused by a twist, "an upper bound for R(T_m, l) - R(T, l)" (READ `library/gap-skeleton-max.md:277, 281`). I use these and do not claim them.
- The lane already has a relative-entropy route to the twist deficit: the action-and-entropy identity (E21), the mixture cost (E22)-(E23) with the information term I_pi, and the polynomial lower bound (E25) (READ `library/gap-ext-astra.md:575-735`, Codex gpt-6-astra, row 789); the seam bound C >= c_R a^2 - log(32 a^2) with I(G; V) <= H(w) <= log(32 a^2) (READ `library/gap-seam-astra.md:473, 506`); the check notes I_pi <= H(pi) (READ `library/gap-ext-check-opus.md:124`).
- Log-Sobolev and hypercontractivity of the transfer Doob kernel are already surveyed as (M5-G), with the count (M5-H) named separately (READ `library/prior/gap-lit-geom.md:15, 38-75`). Birkhoff's projective-metric contraction is a lead the lane could not read (READ `library/prior/gap-math-lit.md:59`).
- Identity L (the twist ratio is the mean of a layer twist ratio), Proposition TW and the open form (AS-bg) with its flat-background ceiling: READ `library/gap-crux-fp.md:367-419`. (AS-bg) is proved for beta_W < 2/3 (READ `library/gap-vmf-lip.md:404-415`; checked by row 790). The ceiling near 0.94: READ `library/gap-arealaw-opus.md:485-488`.
- `library/open-registry.md` and FINISH rows 820-838 were searched for "information", "entropy", "compression": no row owns this question. Rows 833-838 run in parallel on other targets; nothing here does their work.

**Read for this file.** `library/gap-finishline-opus.md` whole; `library/gap-skeleton-final.md` Sections 0-3 and 13.15-13.20; `library/gap-expose-astra.md` header, Section 1 (E1)-(E5), Section 7; `library/gap-crux-fp.md` lines 1-120, 185-305, 367-420; `library/gap-means-max.md` lines 1-140, 280-363; `library/gap-tu-retry.md` lines 1-130 and the final status; `library/gap-transfer.md` lines 100-125, 144-196, 258-279; `library/gap-phys-seed.md` lines 240-282; `library/gap-ext-astra.md` lines 560-735; `library/gap-ds-gauge.md` lines 1-60; `library/prior/gap-math-lit.md` Section 3 and conclusion; `library/prior/gap-lit-geom.md` lines 36-75; `library/gap-arealaw-opus.md` lines 480-492; FINISH rows 783-839 (first lines), 818, 820, 821, 832 in full.

**The crux, as this file uses it.** READ `library/gap-finishline-opus.md:117-121`: (SEED-FP) asks for S(ell/2a_K; (ell/a_K)^3) <= s_* < 1/5041 at one physical size, uniformly over first-passage data. READ there, line 126: the same on the account's tori is (SEED-L), Phi_L = L^4 F(T_ell) - F(T_(L ell)) <= phi_* < (L/2) log(13/10). READ `library/gap-expose-astra.md:579-599`: the consumer's twist deficit p_(m,i)(a) = Tr(P_(-,i) L_m^a)/Tr(L_m^a) = (1 - R_m(v_(1i)))/2, Q_F its maximum, and (E17) Q_F <= C a^p eta_*^(a/2) as a sufficient fixed-coupling form. READ `library/gap-skeleton-final.md:644`: the crux is (ES) at one physical size at order-one coupling. The constraints of the brief: work at beta_W about 2.3-2.6 (READ `library/gap-finishline-opus.md:181`); fail for U(1) in its Coulomb phase (READ `library/gap-tu-retry.md:92-96`: the periodic Villain Langevin gap tends to 0 for beta >= 2^14); beat single-link methods, which miss by a factor 3 to 4 at beta 2 (FINISH rows 820, 832); keep the original normalization.

**Notation.** B is a spatial box with sides at least 3; T_P the gauge-invariant transfer operator with kernel A_T(u, v) = e^(-(V(u)+V(v))/2) I(u, v) (READ `library/gap-transfer.md:118-119`); lambda_0 > lambda_1 >= ... its eigenvalues with multiplicity, mu_i = lambda_i/lambda_0; Omega > 0 the continuous ground state (READ `library/gap-transfer.md:177-179`); S(t; B) = sum over i >= 1 of mu_i^t; F(t, B) = log Tr T_P^t = log Z. J = Z_nu, the centre flip of the links that cross one plane, which commutes with T_P and splits H_inv into flux sectors (READ `library/gap-transfer.md:262`). lambda_0^- is the top eigenvalue on the J-odd subspace and mu^- = lambda_0^-/lambda_0.

**The Doob chain.** pi(du) = Omega(u)^2 du and P(u, dv) = A_T(u, v) Omega(v) dv/(lambda_0 Omega(u)). P is a Markov kernel, reversible with respect to pi, and g -> Omega g is a unitary from L^2_inv(pi) onto H_inv that carries P to T_P/lambda_0 (PROVED: T_P Omega = lambda_0 Omega gives the row sums; pi(du)P(u,dv) = Omega(u)A_T(u,v)Omega(v) du dv/lambda_0 is symmetric). So P has eigenvalues mu_i, eigenfunctions g_i = psi_i/Omega, and the chain X_0, X_1, ... with X_0 ~ pi is the law of the time slices of the infinite cylinder Z x B.

## 1. The crux as an information quantity: an exact dictionary

Every candidate below must act on one of these objects. The identities are exact on every box at every coupling. They hold for every compact group, so by themselves they decide nothing; they fix what a tool would have to bound.

### 1.1 Identity I1: the thermal sum is a chi-square mutual information (PROVED)

Let n >= 1 and let (X_0, X_n) be two slices of the stationary Doob chain at distance n. The joint law has density p_n(u, v) = A^(n)(u, v)/(lambda_0^n Omega(u) Omega(v)) with respect to pi x pi, where A^(n) is the kernel of T_P^n. Then

I_chi2(X_0; X_n) := (integral of p_n^2 d(pi x pi)) - 1 = S(2n; B),
D_2(X_0; X_n) := log (integral of p_n^2 d(pi x pi)) = log(1 + S(2n; B)),
I(X_0; X_n) <= log(1 + S(2n; B))   (Shannon mutual information).

Proof. The integral of p_n^2 d(pi x pi) is the integral of A^(n)(u,v)^2 du dv divided by lambda_0^(2n). T_P^n is a self-adjoint Hilbert-Schmidt integral operator with kernel A^(n) (READ `library/gap-transfer.md:161`), so that integral is ||T_P^n||_HS^2 = Tr T_P^(2n) = lambda_0^(2n)(1 + S(2n; B)). The last line is Jensen's inequality: I = E log p_n <= log E p_n, and E p_n under the joint law is the integral of p_n^2 d(pi x pi). QED

So the seed S(n; (2n)^3) <= 1/5041 at even time says: across n layers of the infinite cylinder with cross-section (2n)^3, the chi-square (Renyi-2) information between two slices is below 1/5041. Theorem S's step, s_(k+1) <= K s_k^2 for s_k = S(2^k n; (2^(k+1) n)^3) once s_k < 1/K (READ `library/gap-crux-fp.md:94`), is a contraction of this information under doubling.

### 1.2 Identity I2: min-entropy, Renyi entropies and the free-energy defects (PROVED; the order-2 case is prior work)

Let rho_t = T_P^t/Tr T_P^t, with eigenvalues q_i = mu_i^t/(1 + S(t; B)). Then

H_inf(rho_t) = -log q_0 = log(1 + S(t; B)),   and for every integer alpha >= 2,   (alpha - 1) H_alpha(rho_t) = alpha F(t, B) - F(alpha t, B).

The case alpha = 2, H_2 = 2F(t) - F(2t), is in the lane already (READ `library/gap-skeleton-max.md:264`; `library/gap-skeleton-max-b.md:272`). The standard Renyi order H_inf <= H_alpha <= (alpha/(alpha - 1)) H_inf for alpha > 1 then gives

log(1 + S(t; B)) <= (alpha F(t, B) - F(alpha t, B))/(alpha - 1) <= (alpha/(alpha - 1)) log(1 + S(t; B)).

Proof. Tr rho_t^alpha = Tr T_P^(alpha t)/(Tr T_P^t)^alpha. For the order: sum q_i^alpha <= q_0^(alpha - 1), and sum q_i^alpha >= q_0^alpha. QED

So the seed is a **min-entropy** statement: the thermal state of the box at temperature 1/t is pure up to log(1 + s_*) < 1.98 x 10^(-4) nats. Section 4 uses the order-alpha form to sharpen Lemma Z' and the constant of (SEED-L).

### 1.3 Identity I3: the twist deficit is the chi-square distinguishability of a slice and its centre flip (PROVED)

Let P_- = (1 - J)/2 act by (P_- h)(u) = (h(u) - h(Ju))/2, and S_-(t) = sum over the J-odd eigenvalues of mu_i^t. Then

p(t) := Tr(P_- T_P^t)/Tr T_P^t = S_-(t)/(1 + S(t; B)),

which is the probability that the thermal state rho_t lies in the J-odd (electric-flux) sector, and for t = 2n

S_-(2n) = (1/4) integral of pi(du) ||f_u - f_(Ju)||^2_(L^2(pi)),   f_u = p_n(u, .) = dP^n(u, .)/dpi.

Proof. The first line is the spectral decomposition, since P_- commutes with T_P. For the second, Tr(P_- T_P^(2n)) = ||P_- T_P^n||_HS^2 because P_- is a projection commuting with T_P. The kernel of P_- T_P^n is (A^(n)(u, v) - A^(n)(Ju, v))/2. Write A^(n)(u, v) = lambda_0^n Omega(u) Omega(v) p_n(u, v) and use Omega(Ju) = Omega(u). QED

The same algebra holds for the consumer's twisted-background operators L_m with Theta_omega in place of J (READ `library/gap-expose-astra.md:106-111, 142-151`: L_m is positive, injective and trace class, Theta commutes with it, Z^(m+v) = Tr(Theta L_m^t)). Its kernel can be taken in the form e^(-V_m(u)/2) I(u, v) e^(-V_m(v)/2), which is pointwise positive and has the same nonzero spectrum (READ `library/gap-transfer.md:26`: the two orders XX* and X*X). So p_(m,i)(a) of (E16) is the probability of the odd sector in the thermal state of L_m, and (E17) asks that this probability fall like eta_*^(a/2).

A second exact form, the t-layer Identity L (PROVED; the case t = 1 is Identity L, READ `library/gap-crux-fp.md:377-386`). For 1 <= t <= a - 1, on the torus with time extent a,

1 - 2p(a) = Z^tw/Z = E_w [A^(t)(u, Jv)/A^(t)(u, v)],

where w is the joint law of the slices U(0) = u and U(t) = v of the torus measure (density proportional to A^(a-t)(v, u) A^(t)(u, v)). Proof: Tr(J T_P^a) is the integral of A^(a-t)(v, u) A^(t)(u, Jv) du dv; divide by Tr T_P^a. QED. Hence p(a) <= (1/2) E_w |1 - A^(t)(u, Jv)/A^(t)(u, v)| for every such t.

### 1.4 Which information measure the seed needs: Shannon information is not enough (PROVED)

**Proposition K.** There is no function Psi with Psi(x) -> 0 as x -> 0 such that S(2n) <= Psi(I(X_0; X_n)) for every reversible Markov chain with positive spectrum.

Proof. Two states a, b with pi = (1 - eps, eps), P(b, b) = 1 - delta, P(b, a) = delta, P(a, b) = delta eps/(1 - eps), P(a, a) = 1 - P(a, b). This is reversible, with eigenvalues 1 and mu = 1 - delta/(1 - eps) > 0. So S(2n) = mu^(2n), while I(X_0; X_n) <= H(X_0) = h(eps) -> 0 as eps -> 0 at fixed delta and n. QED (GUIDE numbers, Section 5: delta = 0.01, n = 10, eps = 10^(-6) gives S(20) = 0.818 and I <= 1.5 x 10^(-5).)

A rare slow mode carries almost no Shannon information but a full unit of thermal sum, because the thermal sum counts each level once, whatever its weight. So any entropy or KL statement (data processing, entropy decay, area laws, rate-distortion) reaches the seed only through a chi-square or Renyi-2 form, or together with a hypercontractive estimate that excludes rare slow modes. Theorem S needs the thermal sum.

### 1.5 The information term of the lane's transport route (PROVED; one line)

For the trial laws of (E22), nu = sum of pi_j (T_j)_* mu with M maps, the information term is I_pi = sum of pi_j D(nu_j || nu) = I(index; output) <= H(pi) <= log M (READ `library/gap-ext-astra.md:600-611, 641-646`; `library/gap-seam-astra.md:506`; `library/gap-ext-check-opus.md:124`). So a mixture of M deterministic Haar-preserving maps lowers the trial cost (E22) by at most log M. Against the lane's per-map lower bounds of order a^2 (READ `library/gap-seam-astra.md:473`; `library/gap-trf-astra.md:633`, for the classes those notes cover), passing (TR-F) needs about e^(c a^2) maps, or field-dependent randomness of the size of the twisted law itself (ARGUED). This is the information-theoretic reason the transport route needs "a trace-compatible joint resummation" (READ `library/gap-expose-astra.md:622-633`) and cannot be closed by mixing.

## 2. The candidates, one by one

Each entry gives (1) the exact statement the candidate gives here, (2) whether it is group-blind, (3) whether it restates the seed, (4) a proof attempt or a counterexample. The tests are those of the brief and of `library/gap-crux-fp.md` 3b.3 (READ L270-274: a tool is refuted by one model in its class where its hypothesis holds and the seed fails). Section 3 treats the twist-sector contraction coefficients separately.

| # | Candidate | What it gives here | Group-blind? | Restates? | Verdict |
|---|---|---|---|---|---|
| 2.1 | RG as lossy compression (data processing along the flow; chain rule; c-, F-, a-theorems) | coarse information <= fine information; monotony in time | yes | yes (crux-fp line 227) | no handle |
| 2.2 | Strict data processing: SDPI constants, contraction coefficients, entropy decay | chi2 constant = gap; TV constant not volume-uniform; KL route needs uniform LSI | the tools yes; the hypotheses fail for U(1) | chi2: yes; KL: stronger than the seed | no handle; Prop Q kills the "squared influence" hope |
| 2.3 | Mutual-information area laws | I(X_0; X_n) <= 6 beta_W abs(B) | yes | no decay at all | no handle |
| 2.4 | Tensor networks and matrix products; "approximability implies decay" | seed = rank-one approximability; Theorem S = its stability | rank one: no (it is the target); bounded rank: yes | yes | no handle; the converse is already Theorem S |
| 2.5 | Rate-distortion | per-site rates; defects cancel | yes | yes | no handle |
| 2.6 | Minimum description length, Kolmogorov complexity | complexity rate = entropy rate; excess = defects | yes | yes | no handle |
| 2.7 | Information bottleneck, RSMI coarse-graining | heuristic optimal blocks | yes | yes | no handle |
| 2.8 | OSSS and decision-tree inequalities (the information form of (M4)) | sharpness dichotomies for monotone measures | needs FKG, absent for SU(2) | dichotomy only | absent |
| 2.9 | Entropic uncertainty and duality | Theorem R = H_2 >= 0 per sector + self-duality | blind beyond the centre | flux half only | already present (M10) |
| 3 | Twist-sector contraction coefficients | chi2 = flux energy; one-layer TV = (AS-bg); thick-slab TV = boundary-uniform mixing | chi2 and slab forms fail for U(1); one-layer form is blind | chi2: yes; slab: (M1) | tested in Section 3: no proof lane |

### 2.1 The renormalization group as lossy compression

(1) **Exact statements.** (a) Data processing along time: for every f-divergence information, including chi-square, I_f(X_0; X_(n+1)) <= I_f(X_0; X_n). By Identity I1 this is S(2n + 2) <= S(2n), which is trivial. (b) Data processing under coarse-graining: for every slice-wise block kernel R (Balaban's block averaging, decimation, any learned map), I_f(R X_0; R X_n) <= I_f(X_0; X_n). The coarse information is a lower bound on the seed quantity, the wrong side for the seed. (c) The chain rule (Shannon only): I(X_0; X_n) = I(R X_0; R X_n) + I(R X_0; X_n | R X_n) + I(X_0; X_n | R X_0). The two conditional terms carry the short-distance information. In the account's regime Balaban's fluctuation fields have exponentially decaying covariance at the block scale, so these terms should be small at separations far above the block size (ARGUED, GUIDE level: the account makes no statement on the block law, READ `library/gap-finishline-opus.md:82, 139`). What remains is I(R^k X_0; R^k X_n) at the last scale, and at physical separation about 20 correlation lengths that is the crux itself, in Shannon form only (Proposition K). (d) The seed in partition-function form is exactly invariant under the account's change of variables (READ `library/gap-finishline-opus.md:123, 138`: the integral of rho_K equals Z). So the RG preserves the seed exactly as a statement about partition functions and loses it as a statement about block information. (e) Monotone functions of the flow (recalled, GUIDE: Zamolodchikov's c-theorem; the entropic c-, F- and a-theorems of Casini and Huerta (2004, 2012) and Casini, Teste and Torroba (2017) from strong subadditivity; the a-theorem of Komargodski and Schwimmer (2011)). They need continuum Lorentz invariance. They allow a massless infrared: a_IR of one free photon is below a_UV of three free gluons.

(2) **Group-blind:** yes. Data processing and the chain rule hold for every kernel and every group. (3) **Restates:** yes. This is line 227 of `library/gap-crux-fp.md` (READ: "It exists for every group; strictness restates the seed"), and route 6 of `library/gap-means-max.md` (READ L331: no route through a monotone quantity of the flow; test model (M9), L112). (4) **Counterexample (GUIDE level, recalled physics).** At the U(1) Coulomb fixed point the information between blocks at fixed aspect ratio is scale invariant: the photon's thermal sum S(n; (2n)^3) tends to a positive constant. Every information monotone of the flow is then constant along that flow, so strict decrease must use a property the photon fixed point violates. The adjoint Higgs model shares every symmetry of the Wilson theory and has a massless phase (READ `library/gap-means-max.md:70, 112`), so no symmetry-plus-information argument can supply that property. **Verdict: no handle.**

### 2.2 Strict data processing: SDPI constants, contraction coefficients, entropy decay

(1) **Exact statements for the Doob chain P on the box B.**
- chi-square constant: eta_chi2(P^n, pi) = mu_1^(2n), the squared maximal correlation of (X_0, X_n) (PROVED: P is self-adjoint on L^2(pi) with positive spectrum, and the maximal correlation is its norm on the constants' complement). The SDPI chain then reads S(2n; B) <= mu_1^(2(n-k)) S(2k; B) for k <= n. With k = 1 the count S(2; B) is of order e^(O(abs(B))), so this route needs n m(B) of order abs(B): useless without a separate count. Theorem S supplies the count from the seed at one size, which is the point of the lane's continuation.
- Dobrushin constant: eta_TV(P) = sup over (u, u') of TV(P(u, .), P(u', .)) >= eta_1 >= mu^- (eta_1 and Proposition TB of Section 3; the first inequality because eta_1 is the sup over the pairs (u, Ju) only). It is not volume-uniform: two slices that differ at a positive density of places give next-slice laws that separate by a law of large numbers (ARGUED; the GUIDE run of Section 5 shows the J-restricted part rising with the width in the disordered 2D Ising phase: 0.60, 0.69, 0.76, 0.81 for widths 4 to 10 at K = 0.3).
- Entropy (KL) route. With eta_KL(P^k, pi) <= theta < 1 uniformly in B, the data processing chain X_0 -> X_1 -> X_n and the area law of 2.3 give I(X_0; X_n) <= theta^(floor((n-1)/k)) 6 beta_W abs(B) (PROVED as a conditional: input-restricted SDPI and submultiplicativity under a stationary pi). That is a Shannon seed at n of order k log(abs(B))/log(1/theta). By Proposition K it is not the seed; one needs in addition a hypercontractive estimate for P that excludes rare slow modes. The hypothesis is a volume-uniform entropy contraction (log-Sobolev type) for the physical-time Doob kernel: the lane's (M5-G), surveyed with no supplier for 4D Wilson SU(2) (READ `library/prior/gap-lit-geom.md:15, 66-75`).
- Influence matrices. If a nonnegative matrix C on a torus has all row sums equal to r, its spectral radius is r (PROVED: C 1 = r 1 and the spectral radius is at most the largest row sum). The worst-case one-link influence matrix is translation invariant, so spectral (rather than row-sum) forms of Dobrushin's worst-case condition gain nothing over its row sums. The typical row sums that row 820 measures (medians 2.13 at beta_W = 0.5, 3.55 at 2.3, 3.31 at 3.0; FINISH row 820) belong to a matrix that is translation invariant in law, so the same holds for its mean (ARGUED). The typical (pinning) influence matrix of spectral-independence methods (Anari, Liu and Oveis Gharan 2020, recalled) has row sum of the order of the susceptibility: bounding it is a decay statement, that is, a restatement.

(2) **Group-blind:** the tools are. The hypotheses (a uniform chi2 or KL constant) are false for U(1) in the Coulomb phase (no gap), which is correct but leaves the hypothesis as the crux. (3) **Restates:** chi2 form, yes (it is the gap); KL form, it is stronger than the seed (an all-volume functional inequality).

(4) **The one hope with a number in it, and its counterexample.** On trees, information contracts with the square of the edge coefficient: broadcasting on a tree with branching b is impossible (the root is not reconstructible from far leaves) when b eta_KL < 1, and for the Ising edge channel eta_KL = lambda^2 with lambda = tanh beta (recalled, GUIDE: Kesten and Stigum 1966; Evans, Kenyon, Peres and Schulman 2000; Ahlswede and Gacs 1976; the Bayesian-network percolation bound of Polyanskiy and Wu 2017 is the DAG form). Squaring row 820's typical influence would turn a row sum of about 3.5 over about 18 neighbours into about 18 x (3.5/18)^2 = 0.68 < 1 (GUIDE arithmetic). That arithmetic is invalid on a lattice:

**Proposition Q (tree information thresholds are false on lattices; PROVED given the infrared bound of Frohlich, Simon and Spencer 1976, recalled).** For the nearest-neighbour Ising model on periodic cubes (Z/bZ)^3 at beta = 0.35, the tree criterion holds, 6 tanh^2(0.35) = 0.679 < 1 (with 5 non-backtracking neighbours, 0.566), but the periodic measure has long-range order: by Gaussian domination, <(sum over x of sigma_x)^2>/abs(Lambda)^2 >= 1 - G_Lambda/beta, which tends to m^2 = 1 - G_3/0.35 = 0.278 > 0, with G_3 = 0.252731 the simple-cubic lattice Green function at the origin (Watson's integral; computed in Section 5). By the argument of Proposition TB2 below with N = 1 (transfer along one axis, R the global flip), the flip-odd sector keeps weight w_o >= (m^2/2)^2 (1 - o(1)) = 0.0193 (1 - o(1)) in the thermal state of the cube b^3 at time b, so the thermal sum of every large cube stays above 0.019 > 1/5041, and the two-point function does not decay. QED. (At beta = 0.26 the same bound gives only 1.95 x 10^(-4), just below 1/5041, which is why 0.35 is used. Two dimensions, GUIDE: at beta = 0.5, 4 tanh^2 = 0.854 < 1 while beta > beta_c = 0.4407 of Onsager and Yang.)

So a criterion "sum over neighbours of eta_KL < 1 implies decay" is false on Z^d: on lattices, information along many paths adds coherently before it is squared, and the typical-measure thresholds are of uniqueness type, linear in the influence. **Verdict: no handle.** The factor 3 to 4 of rows 820 and 832 is not removed by passing from total variation to relative entropy.

### 2.3 Mutual-information area laws

(1) **Exact statement (PROVED).** For any cut of the torus or cylinder into link sets A and A^c, crossed by the plaquette set P_d (plaquettes with links on both sides), I(X_A; X_(A^c)) <= 2 beta_W abs(P_d). For two slices: I(X_0; X_n) <= I(X_0; X_1) <= 6 beta_W abs(B). Proof: the joint law of (X_0, X_1) has density a(u) a(v) I(u, v)/lambda_0 with a = Omega e^(-V/2); compare it with the product of the normalized a du; the relative entropy is E log I - log E_prod I <= osc(log I) <= 2 beta_W x (3 abs(B)) (one temporal plaquette per spatial link, each factor in [e^(-2 beta), 1]); and the mutual information is the least relative entropy to a product. QED. This is the classical form of the thermal-state area law of Wolf, Verstraete, Hastings and Cirac (2008, recalled).

(2) **Group-blind:** yes, for every compact group and every beta. (3) It gives no decay in distance, so it restates nothing and supplies nothing; with Pinsker it bounds correlations by the square root of an area. (4) Related results, recalled (GUIDE): in one dimension a gap implies an area law and so does exponential decay (Hastings 2007; Brandao and Horodecki 2013, 2015); clustering of conditional mutual information is proved above a threshold temperature (Kuwahara, Kato and Brandao 2020) and implies Davies gaps for commuting Hamiltonians (Brandao and Kastoryano 2019) — single-scale (M1) statements at high temperature. Topological entanglement entropy separates the deconfined Z_2 phase from a confined one but not U(1) from SU(2) (both have none), and for SU(2) its vanishing is the absence of electric topological order, which is the flux half again. The non-abelian edge entropy sum_j p_j log d_j of the electric-centre algebra (Donnelly 2012; Casini, Huerta and Rosabal 2014, recalled) is group-sensitive (zero for U(1)), but it concerns entanglement of subregions, not purity of the global thermal state, and no inequality ties it to the seed (ARGUED). **Verdict: no handle.**

### 2.4 Tensor networks and matrix products: does approximability imply decay?

(1) **Exact statement (PROVED).** For the positive operator rho = T_B^n/lambda_0^n, the trace-norm distance to its rank-one part is ||rho - |Omega><Omega| ||_1 = S(n; B). So "the partition tensor of the box at time n is within s of rank one" is the seed with threshold s. The converse question, approximability implies decay, is answered yes in rank one by Theorem S itself: s_(k+1) <= K s_k^2 once s_k < 1/K (READ `library/gap-crux-fp.md:94`) is the stability of the trivial fixed point under doubling. Kennedy and Rychkov proved the analogous stability for tensor renormalization of the 2D Ising model near its high-temperature fixed point (recalled, GUIDE).

(2) **Group-blind:** rank-one approximability is the target, not a tool; bounded rank r >= 2 is group-blind and admits ordered phases. (4) **Counterexamples (PROVED).** Bounded rank gives no rate: the 1D Ising transfer matrix has rank 2 and correlation length -1/log tanh(beta), unbounded as beta grows. Bounded rank allows no gap: the deconfined Z_2 gauge theory has light flux sectors (READ `library/gap-crux-fp.md:44`), so its block transfer approaches a projection of rank eight. (3) **Restates:** yes. Entering the basin of the trivial fixed point at order one is the seed. Doing it by a tensor computation with interval bounds would be a computer-assisted proof, which the lane's rules exclude (READ `library/gap-means-max.md:336`). **Verdict: no handle;** the "converse" is already proved as Theorem S.

### 2.5 Rate-distortion

(1) The exact statement I can give is the Gibbs variational principle, F = sup over nu of (E_nu(-S) + H(nu)): log Z is an entropy-minus-cost optimum, the dual of a description length. Rate-distortion functions of the Wilson field are per-site quantities; the defects Phi_L and the deficit are subextensive and cancel in every per-site rate. A tool must control the difference of two extensive optima to an absolute error of about 6 x 10^(-4) in the doubling form (READ `library/gap-crux-fp.md:250`), or below 0.262 (L - 1) on tori of L^4 cells in the dilation form (Section 4); no rate-distortion inequality does that. (2) Group-blind. (3) Restates. (4) No statement to attempt. **Verdict: no handle** (ARGUED).

### 2.6 Minimum description length, Kolmogorov complexity

(1) The algorithmic complexity rate of a typical configuration of an ergodic stationary field equals its entropy rate (Brudno's theorem and its Z^d forms, recalled, GUIDE). The finite-size part ("excess entropy" in the language of Crutchfield and Feldman) is the free-energy defect: scale-invariant and nonzero at the photon fixed point, exponentially small in a gapped phase (GUIDE). Its smallness at one size is (SEED-Delta) or (SEED-L) under another name (READ `library/gap-finishline-opus.md:125-126`). (2) Group-blind. (3) Restates. (4) Nothing to prove. **Verdict: no handle.**

### 2.7 Information bottleneck and RSMI coarse-graining

(1) Choose the coarse variable H of a block to maximize I(H; E), E the environment beyond a buffer (Koch-Janusz and Ringel 2018; Lenggenhager, Gokmen, Ringel, Huber and Koch-Janusz 2020; Gordon, Banerjee, Koch-Janusz and Ringel 2021; recalled, GUIDE). The claims are numerical or for Gaussian and one-dimensional examples. No theorem ties the optimal I(H; E) to a gap. In a gapped phase it tends to zero with the block size in units of the correlation length, at a fixed point to a constant: its decay is the seed in another form. (2) Group-blind. (3) Restates. **Verdict: no handle.**

### 2.8 OSSS and decision trees: the information form of (M4)

(1) The OSSS inequality Var f <= sum_i delta_i(T) Inf_i(f) for product measures, extended to monotonic (FKG) measures, gives sharpness: exponential decay below a threshold and a mean-field lower bound above it (O'Donnell, Saks, Schramm and Servedio 2005; Duminil-Copin, Raoufi and Tassion 2019; recalled, GUIDE). For lattice gauge theory it is known for Potts gauge models through a plaquette random-cluster model (READ `library/gap-crux-fp.md:244`). (2) It needs a monotone representation in a parameter. For 4D Wilson SU(2) a positive surface representation fails term by term (Corollary NS0, READ `library/gap-means-max.md:96`; checked by row 744). (3) It would give a dichotomy, not the selection: no soft theorem excludes the ordered branch in four dimensions (READ `library/gap-means-max.md:70`). **Verdict: absent.**

### 2.9 Entropic uncertainty and duality

Theorem R's inequality Tr S^(2t) <= (Tr S^t)^2 in each crossed sector (READ `library/gap-means-max.md:62`) is H_2 >= 0 for the sector thermal state; with the self-duality p = Hp it is an uncertainty principle between electric and magnetic flux weights. It is the means (M10), present for the flux half and blind beyond the centre (Z_2 at large beta passes it, READ `library/gap-means-max.md:284`); "For the even half I found no identity of this kind" (READ `library/gap-means-max.md:113`). An entropic (Maassen-Uffink type) version of the same duality adds no selection. **Verdict: already present; no new handle.**

## 3. The test asked for: strong data-processing coefficients of the Wilson transfer restricted to the twist sector

### 3.1 Three coefficients

Fix a box B (sides at least 3), a direction nu and its centre flip J (READ `library/gap-transfer.md:262`; c_nu of `library/gap-crux-fp.md:376-387`). Write A^(t) for the kernel of T_P^t (so A^(1) = A_T). The twist sector is the J-odd subspace. Define:

- **the chi-square coefficient** mu^- = lambda_0^-/lambda_0, the spectral radius of P on J-odd functions in L^2(pi) (the restriction of eta_chi2^(1/2) to the twist sector);
- **the Dobrushin twist coefficient** eta_t = sup over u of TV(P^t(u, .), P^t(Ju, .)), the worst-case total-variation contraction of the binary channel "flip or not" through t layers of the Doob chain (the KL form of this binary channel is equivalent to it up to Pinsker's inequality and Topsoe's bound, so it is not a separate object);
- **the slab coefficient** kappa_t = (1/2) sup over (u, v) of abs(1 - A^(t)(u, Jv)/A^(t)(u, v)), the worst-case twist response of a slab of t layers with both boundary slices fixed. For t = 1, A_T(u, Jv)/A_T(u, v) = I(u, c_nu v)/I(u, v), the layer twist ratio of (AS-bg) (V(Jv) = V(v)).

### 3.2 Proposition TB (PROVED)

For every integer t >= 1:

(a) (mu^-)^t <= eta_t <= kappa_t;
(b) for every a >= t + 1, the twist deficit obeys p(a) <= (1/2) E_w abs(1 - A^(t)(u, Jv)/A^(t)(u, v)) <= kappa_t, with w as in the t-layer Identity L (1.3);
(c) p(a) >= (mu^-)^a/(1 + S(a; B)).

The same holds for each twisted background L_m with Theta_omega in place of J, with its own ground state (its kernel e^(-V_m/2) I e^(-V_m/2) is pointwise positive, 1.3).

Proof. (a) J is a Haar-preserving involution that commutes with T_P, and Omega(Ju) = Omega(u); so P^t(Ju, .) is the image of P^t(u, .) under J. Let g be bounded and J-odd. Then (P^t g)(u) = integral of g dP^t(u, .) = -integral of g d(J_* P^t(u, .)), hence (P^t g)(u) = (1/2) integral of g d(P^t(u, .) - J_* P^t(u, .)) and abs(P^t g(u)) <= eta_t ||g||_inf. Take g = psi/Omega for an odd eigenfunction psi of T_P with eigenvalue lambda_0^-; it is continuous and bounded, since psi = (lambda_0^-)^(-1) T_P psi has a continuous kernel and Omega has a positive minimum (READ `library/gap-transfer.md:177-179`). Then P^t g = (mu^-)^t g, so (mu^-)^t <= eta_t. Next, P^t(u, .) has density A^(t)(u, v) Omega(v)/(lambda_0^t Omega(u)) and its J-image has density A^(t)(u, Jv) Omega(v)/(lambda_0^t Omega(u)), so TV(P^t(u, .), J_* P^t(u, .)) = (1/2) E_(v ~ P^t(u, .)) abs(1 - A^(t)(u, Jv)/A^(t)(u, v)) <= kappa_t. (b) is the t-layer Identity L of 1.3: 2p(a) = E_w (1 - ratio) <= E_w abs(1 - ratio). (c) is Identity I3: p(a) = S_-(a)/(1 + S(a)) and S_-(a) >= (mu^-)^a. QED

(GUIDE check of (a) and (b) on the 2D Ising transfer with the global flip: Section 5, criteria C5 and C6, all PASS.)

**Reading.** The chi-square twist coefficient mu^- is exactly e^(-E^-), E^- the energy of the lowest electric-flux state above the vacuum. A bound mu^- <= theta < 1, uniform in B, is electric confinement in Hamiltonian form; with (c) and Theorem R the flux information is already reduced to (ES) (READ `library/gap-skeleton-final.md:620`). So the chi-square form restates the flux half. The worst-case forms eta_t and kappa_t are new handles only if they can be bounded without that knowledge. 3.3 and 3.4 settle the one-layer case; 3.5 the rest.

### 3.3 Corollary TB1: the one-layer coefficient below beta_W = 2/3 (PROVED given (AS-bg), checked by row 790)

Let 0 <= beta_W <= beta_1 < 2/3, q_1 = 3 beta_1/2, m = (1/2) log(1/q_1), C = 4 beta_1 q_1^(-3/2)/(1 - q_1), and eps = C (abs(B)/b_nu) e^(-m b_nu). (AS-bg) gives abs(log(I(u, c_nu v)/I(u, v))) <= eps for every background and every box (READ `library/gap-vmf-lip.md:404-415`). So kappa_1 <= (e^eps - 1)/2, and by Proposition TB:

mu^- <= (e^eps - 1)/2,   and if eps <= 1:   E^- = -log mu^- >= m b_nu - log(C abs(B)/b_nu),

since e^eps - 1 <= (e - 1) eps < 2 eps for eps <= 1. On the cube b^3: **the lowest electric-flux level lies at least m b - log(C b^2) above the vacuum**, uniformly in the time extent, the background cocycle and the box. This is linear growth of the flux energy with the side, a Hamiltonian string tension of at least (1/2) log(2/(3 beta_1)), for every beta_W < 2/3. (Example: beta_1 = 1/2 gives m = 0.1438, C = 12.32, E^- > 2.66 at b = 100.) It is a strong-coupling corollary of a checked bound, new in the lane as a spectral statement as far as I found (the twist ratios themselves, (b) with t = 1, are Step 6 of Proposition TW, READ `library/gap-crux-fp.md:400`). It is off the path of (GAP) for the same reason as every fixed-beta result (READ `library/gap-finishline-opus.md:198`).

### 3.4 Proposition TB2: the one-layer coefficient is useless at order one (PROVED given the infrared bound of Frohlich, Simon and Spencer, recalled)

At the flat background u = v = 1 the layer model is the 3D O(4) model at coupling beta_W, and the flip is the antiperiodic boundary condition by -I in the direction nu (READ `library/gap-crux-fp.md:376, 387`). Write Z_per, Z_anti for its two partition functions on the periodic box Lambda with sides (b, c, d) (b in the direction nu), G_Lambda = (1/abs(Lambda)) sum over p != 0 of 1/E(p) with E(p) = sum over i of 2(1 - cos p_i), and m_Lambda^2 = 1 - (N/beta) G_Lambda with N = 4.

**Claim.** For even b, 1 - Z_anti/Z_per >= 2 [(m_Lambda^2/(2N) - b/(24 beta c d))_+]^2. On cubes b^3, as b -> infinity, 1 - Z_anti/Z_per >= m^4/(2N^2) (1 - o(1)) = m^4/32 (1 - o(1)), with m^2 = 1 - 4 G_3/beta_W and G_3 = 0.252731.

Proof. (i) Transfer in the direction nu: Z_per = Tr T^b and Z_anti = Tr(R T^b), where R is the global flip s -> -s of a slice (an element of SO(4)) and T >= 0 commutes with R. With w_o = Tr(P_odd T^b)/Tr T^b, Z_anti/Z_per = 1 - 2 w_o. (ii) Let M_t be the magnetization of the slice at nu-coordinate t, and g(t) = <M_0 . M_t> in the periodic state. Gaussian domination (Frohlich, Simon and Spencer) gives <abs(s-hat(p))^2> <= N abs(Lambda)/(beta E(p)) for p != 0; with Parseval, <abs(M_tot)^2> >= abs(Lambda)^2 m_Lambda^2. Write g(t) = (1/b) sum over p_nu of e^(i p_nu t) g-hat(p_nu), with g-hat(p_nu) = <abs(M-hat(p_nu))^2>/b >= 0 and M-hat(p_nu) = s-hat(p_nu, 0, 0). Then g(b/2) >= (1/b) g-hat(0) - (1/b) sum over p_nu != 0 of g-hat(p_nu) >= (cd)^2 m_Lambda^2 - N b c d/(12 beta), using sum over k = 1..b-1 of 1/(4 sin^2(pi k/b)) = (b^2 - 1)/12 (checked in Section 5). (iii) Each component M^a is R-odd, so it maps even to odd functions. Hence Tr(M^a T^(b/2) M^a T^(b/2)) = 2 Tr(A M^a B M^a) with A = P_even T^(b/2), B = P_odd T^(b/2), and by Holder's inequality for Schatten norms Tr(A M B M) <= ||M||^2 (Tr A^2)^(1/2) (Tr B^2)^(1/2). With ||M^a|| <= cd this gives g(b/2) <= 2N (cd)^2 (w_e w_o)^(1/2) <= 2N (cd)^2 w_o^(1/2). (iv) Combine (ii) and (iii) and square. On cubes, b/(24 beta b^2) -> 0 and G_Lambda -> G_3. QED

**Consequences.** (1) For every beta_W > 4 G_3 = 1.0109, the layer twist ratio at the flat background stays below 1 - m^4/32 + o(1) on large cubes, so kappa_1 >= m^4/64 (1 - o(1)) does not tend to zero: **(AS-bg) is false for every beta_1 > 1.0109.** This proves the step that `library/gap-crux-fp.md:416` marks "GUIDE for this second step", in the weak form needed, and puts a proved number on the ceiling that `library/gap-arealaw-opus.md:485-488` gives as about 0.94 (GUIDE; the gap between 0.936 and 1.011 is the gap between the believed critical coupling and the infrared bound). (2) At beta_W = 2.3 the bound reads 1 - Z_anti/Z_per >= 0.0098 (1 - o(1)); at 2.6, 0.0117 (Section 5). The one-layer worst-case twist contraction gives nothing in the window [2.3, 2.6]. (3) For U(1) the flat-background layer is the 3D XY model, and the same proof with N = 2 kills the one-layer form above 2 G_3 = 0.505. So the one-layer form is a high-temperature spin-model bound, blind to the group as a tool (READ `library/gap-crux-fp.md:404`), and it fails for both groups before order one.

### 3.5 The Doob and thick-slab forms (OPEN)

What is left is eta_t, or kappa_t, for thicknesses t of several correlation lengths. Proposition TB (b) shows that a bound kappa_t <= C a^p eta_*^(a/2) for some t <= a - 1 would give (E17) directly, with no count. Four observations, none of them a proof:

1. **The flat-background obstruction need not survive in a thick slab** (GUIDE, belief): with both boundary slices flat, the interior of a slab several correlation lengths thick is expected to disorder at beta_W in [2.3, 2.6], so the ordered-layer mechanism of 3.4 disappears. So the thick-slab form is not known to be false at order one.
2. **For a local symmetry sector the worst case is not volume-uniform in any phase** (GUIDE run, Section 5): for the 2D Ising global flip at K = 0.3, mu^- = 0.53 for every width, while eta_1 = 0.60, 0.69, 0.76, 0.81 and eta_4 = 0.082, 0.105, 0.121, 0.134 for widths 4, 6, 8, 10. The gauge centre flip is non-local (it is invisible on every region that does not wrap the cycle), so this mechanism does not transfer directly; but a worst-case boundary still forces overlaps psi_i(u)/Omega(u) that can be exponentially large in the cross-section, and then the thickness t needed for kappa_t < 1 grows at least like the logarithm of the cross-section (ARGUED from the spectral expansion A^(t)(u, v)/lambda_0^t = Omega(u) Omega(v) (1 + sum over i >= 1 of mu_i^t g_i(u) g_i(v))).
3. **It is a boundary-uniform mixing statement at the scale of the correlation length**: the same kind as (W) and (DS-tw) of row 691 (READ `library/gap-ds-gauge.md:36-50`) and as line 21 of the tool table (READ `library/gap-crux-fp.md:245`: "A hypothesis; no verification at order one"). In the lane's list of means it is (M1), which is absent at order one (READ `library/gap-means-max.md:38-42`). It is harder than the typical form (Identity L), which is the flux half itself.
4. **U(1) control.** In the Coulomb phase mu^- -> 1 as the box grows (GUIDE: the electric flux energy of one unit is of order 1/b), so by (c) p(a) does not decay, and every form fails, as the brief requires. So the chi-square and thick-slab forms are not group-blind in truth; but nothing in them says how a proof would use what separates SU(2).

### 3.6 Verdict on the twist-sector coefficients

The object is concrete and was tested. Its chi-square form is the electric-flux energy, so it restates the flux half (which Theorem R already folds into (ES)). Its one-layer worst-case form is (AS-bg): proved below 2/3 (row 790), now proved false above 1.0109 (Proposition TB2), so it cannot reach order one. Its thick-slab worst-case form may be true at order one, and would give (E17) directly, but it is a boundary-uniform mixing hypothesis at the correlation length with no means to verify it. **Not worth a dedicated proof lane.** Two usable by-products: Corollary TB1 (the flux energy grows linearly in the side for beta_W < 2/3) and Proposition TB2 (a proved ceiling 1.0109 for every background-uniform layer twist bound). The covariance form of the same ceiling, for the background-uniform slab routes to the area law (rows 825 and 834), follows from the same infrared bound directly, for any such route whose hypothesis includes the flat background on large periodic slabs, as `library/gap-arealaw-opus.md:485-486` says theirs does: long-range order at the flat background excludes a background-uniform exponential covariance bound above 1.0109 (ARGUED; the reduction of their exact hypothesis to the periodic flat slab is theirs, not re-read here). This puts a proved ceiling 1.0109 beside the believed one, about 0.94 (GUIDE); the interval between them is the gap between the believed critical coupling of the 3D O(4) model and its infrared bound.

## 4. What the information reading does give: a sharper count (Lemma Z'') and a wider margin for (SEED-L)

This section moves no number at order one. It sharpens a constant on the finish line.

**Lemma Z'' (Renyi telescoping; PROVED).** Let T_0 >= 3 and rho >= 2 be integers, b = rho T_0, and Phi_rho(T_0) = rho^4 F(T_0^4) - F(b^4) as in `library/gap-phys-seed.md:247` (READ; its ">= 0 (four uses of Lemma A (a))" is the same telescoping with each term only shown nonnegative). For k = 1, ..., 4 let B_k be the spatial box with k - 1 sides b and 4 - k sides T_0. Then

Phi_rho(T_0) = (rho - 1) sum over k = 1..4 of rho^(4-k) H_rho(rho^(k)) >= (rho - 1) sum over k = 1..4 of rho^(4-k) log(1 + S(T_0; B_k)),

where rho^(k) is the thermal state T_(B_k)^(T_0)/Tr T_(B_k)^(T_0). In particular, with B_4 = b^3,

log(1 + S(T_0; b^3)) <= Phi_rho(T_0)/(rho - 1).

Proof. Let Q_k be the torus whose first k sides are b and whose other sides are T_0, so Q_0 = T_0^4 and Q_4 = b^4. Telescoping, rho^4 F(Q_0) - F(Q_4) = sum over k = 1..4 of rho^(4-k) (rho F(Q_(k-1)) - F(Q_k)). Q_k differs from Q_(k-1) only in side k, from T_0 to rho T_0. Take direction k as time: by (TM) for boxes with unequal sides (READ `library/gap-finishline-opus.md:139`) and axis-permutation invariance of Z (READ `library/gap-crux-fp.md:38`), F(Q_(k-1)) = log Tr T_(B_k)^(T_0) and F(Q_k) = log Tr T_(B_k)^(rho T_0). By Identity I2 with alpha = rho, rho F(Q_(k-1)) - F(Q_k) = (rho - 1) H_rho(rho^(k)), and H_rho >= H_inf = log(1 + S(T_0; B_k)). QED

**Comparison with Lemma Z'.** Lemma Z' (Claude Fable 5.2, row 720; checked rows 698, 699 for its input, row 727 for the file) gives log(1 + S(T_0; b^3)) <= (2/rho) Phi_rho(T_0) (READ `library/gap-phys-seed.md:268-272`). Lemma Z'' replaces 2/rho by 1/(rho - 1): equal at rho = 2, smaller by the factor rho/(2(rho - 1)) for rho >= 3, close to 1/2 for large rho. Its proof uses only the positivity of Renyi entropies and does not use the monotonicity of F(n)/abs(n) in each side. The 2D form passes a GUIDE check on 12 cases (Section 5, C4).

**Consequence 1: the margin of (SEED-L) (ARGUED, as Lemma FL is).** In Lemma FL (READ `library/gap-finishline-opus.md:128-134`) only step (1) uses Lemma Z'. With Lemma Z'' its hypothesis becomes Phi_rho(T_0) <= (rho - 1) log(1 + s_0), and the rest of the proof is unchanged. So with rho = L, (SEED-L) gives (SEED-FP) as soon as

limsup over first-passage data of Phi_L <= phi_* with phi_* < (L - 1) log(13/10), about 0.262 (L - 1),

in place of phi_* < (L/2) log(13/10), about 0.131 L. For L = 25, the room grows from 3.28 to 6.30. Lemma FL itself is ARGUED in its source and not checked; this changes one of its steps.

**Consequence 2: Corollary Z1' (PROVED given Lemma Z'' and the proof of Lemma Z).** The seed S(b/2; b^3) <= 1/1650 follows from b m(b^3) >= (4/3) Phi_4(b/4) + 29.64, in place of 2 Phi_4(b/4) + 29.64 (READ `library/gap-phys-seed.md:274-279`): Lemma Z'' with rho = 4 gives log(1 + S(b/4; b^3)) <= Phi_4(b/4)/3, then S(b/2; b^3) <= e^(Phi_4(b/4)/3 - (b/4) m(b^3)) as in Lemma Z.

**What this is.** A constant, not a means. It shows the one place where the information reading was not already used to the end: the lane read the doubling defect as a Renyi-2 entropy (rows 669, 670) and then left the order free; the dilation by L is a Renyi-L entropy, and H_L is closer to H_inf than H_2 is.

## 5. GUIDE run (decides nothing)

**What was run.** `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/lane839/scripts/info_identities_guide.py` (sha256 c3caa7db...49981211), output `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/lane839/out/info_identities_guide.out` (sha256 b2f179d1...aa5ad787). Exact transfer matrices of the 2D Ising model (periodic width w = 4, 6, 8, 10; K = 0.3, K_c, 0.6), the global flip as J, spectra computed blockwise on the J-even and J-odd subspaces. numpy 2.4.4, scipy 1.17.1, one BLAS thread, 2.0 s, peak memory 140 MB (machine: 8 GB, low free memory, so the widths were capped at 10). Not in git. The criteria C1-C6 are in the script header, written before the run. The 2D Ising model is a control for the algebra only; its J is a local sector, unlike the gauge centre flip.

**Results: PASS on every criterion.**

| Criterion | Statement checked | Cases | Worst relative error or result |
|---|---|---|---|
| C1 | S(2n) = I_chi2(X_0; X_n) (Identity I1) | 12 (K, w) x n = 1, 2, 3 | 1.2 x 10^(-13) |
| C2 | S_-(2n) = (1/4) E_pi ||f_u - f_(Ju)||^2 (Identity I3) | same | 3.3 x 10^(-14) |
| C3 | 2F(n) - F(2n) = H_2, log(1 + S(n)) = H_inf (Identity I2) | same | 9.5 x 10^(-15) |
| C4 | 2D Lemma Z'': log(1 + S(T_0; rho T_0)) <= Phi/(rho - 1) | 12 | holds in all; equal to Lemma Z' at rho = 2; at rho = 3, K = 0.3: 1.04 against 1.39 (true value 0.32) |
| C5 | (mu^-)^t <= eta_t (Proposition TB (a)) | 12 x t = 1..4 | holds in all |
| C6 | p(a) = (1/2)(1 - E_w ratio_t) <= (1/2) E_w abs(1 - ratio_t) (t-layer Identity L, TB (b)) | 8 | holds in all |

**Numbers used in the text.** Proposition K: delta = 0.01, n = 10: S(20) = 0.8177 (eps = 10^(-3), H(X_0) = 7.9 x 10^(-3)) and 0.8179 (eps = 10^(-6), H(X_0) = 1.5 x 10^(-5)). Proposition Q: G_3 = 0.252731 (quadrature of the integral of (e^(-2t) I_0(2t))^3 over t > 0, error 3 x 10^(-10)); at beta = 0.35 the infrared bound gives m^2 >= 0.2779 and odd weight >= m^4/4 = 0.0193, while 6 tanh^2 = 0.679 and 5 tanh^2 = 0.566; at beta = 0.26 it gives m^2 >= 0.0280 and only 1.95 x 10^(-4) < 1/5041 (so 0.26 is not used); in 2D, beta_c = 0.44069 and at beta = 0.5, 4 tanh^2 = 0.854. The script was rerun once after adding the beta = 0.35 line; every criterion still passes and every number quoted in this file was read from the rerun output. Proposition TB2: 4 G_3 = 1.01092 (O(4), the SU(2) layer), 2 G_3 = 0.50546 (O(2), the U(1) layer); at beta_W = 1.5, 2.3, 2.6 the bound 1 - Z_anti/Z_per >= m^4/32 reads 0.0033, 0.0098, 0.0117. The identity sum of csc^2(pi k/b) = (b^2 - 1)/3 checked for b = 4, 6, 9, 16.

**Readings (GUIDE).** (1) The algebra of Identities I1-I3, Lemma Z'' and Proposition TB is right in a model with exact numbers. (2) For a local sector the worst-case coefficient eta_1 rises with the width in every phase (K = 0.3: 0.60 to 0.81), while mu^- does not move (0.514 to 0.531): worst-case contraction coefficients are not volume-uniform even where the typical one is. (3) The slab coefficient kappa_t is far above 1 for a local sector at t = 1 (17.8 at w = 6, 60 at w = 8, K = 0.3) and falls below 1 only for thick slabs (0.61 at t = 3, w = 6; 0.37 at t = 4, w = 8). Nothing here bears on 4D SU(2) at order one.

**Runs not made, and why.** A 4D Monte Carlo of eta_t or kappa_t at beta_W = 2.3 from a flat boundary slice would show whether the thick-slab form of 3.5 is plausible at order one. It would not change the decision of this file: that form is a boundary-uniform mixing hypothesis with no means to verify it, so no lane follows from either outcome (the lane's worth-doing test fails). A tensor-renormalization computation that enters the basin of the trivial fixed point would be a computer-assisted proof (2.4), excluded by the rules.

## 6. Verdict, status, scope

### 6.1 The answer to the owner's question, plainly

Compression theory gives the right words for the crux and no new inequality for it.

- The words are exact. The seed is a chi-square mutual information between slices (I1), the min-entropy of the box's thermal state (I2), and the statement that the partition tensor of one box is close to rank one (2.4). The twist deficit is the chi-square distinguishability of a slice and its centre flip (I3). Theorem S is a stability theorem for the trivial fixed point of this compression: the "approximability implies decay" converse, already proved in rank one.
- No candidate supplies a small number at the scale of the correlation length. Monotonicity statements (data processing along the flow, chain rules, entropic c-, F- and a-theorems, area laws, rate-distortion, MDL, RSMI) hold for every group and stay non-strict at the U(1) photon fixed point; their strictness is the seed (crux-fp line 227). Contraction-coefficient statements are single-scale criteria, (M1): their chi-square forms are the gap, their worst-case forms are not volume-uniform or are ceilinged by ordered backgrounds, their Shannon forms are too weak (Proposition K), and the tree-type square gain over Dobrushin is false on lattices (Proposition Q). The information form of a dichotomy (OSSS) needs an FKG structure that 4D SU(2) lacks.
- **None is worth a dedicated proof lane.** The concrete object the brief named, the twist-sector contraction coefficient, was tested: chi-square form = electric-flux energy (a restatement of the flux half); one-layer worst-case form = (AS-bg), proved below 2/3 and now proved false above 1.0109; thick-slab worst-case form = a boundary-uniform mixing hypothesis at the correlation length with no means.
- What is worth a short check: Lemma Z'' (a factor about 2 of room in (SEED-L)), Proposition TB with Corollary TB1, and Proposition TB2 (a proved ceiling 1.0109 for every background-uniform layer twist bound; in covariance form, ARGUED, the same ceiling for the background-uniform slab routes to the area law of rows 825 and 834).

### 6.2 Status of the statements of this file

| Statement | Mark |
|---|---|
| Identity I1: S(2n; B) = I_chi2(X_0; X_n), log(1 + S) = D_2, Shannon I <= log(1 + S) | PROVED (GUIDE check C1) |
| Identity I2: H_inf = log(1 + S(t)), (alpha - 1) H_alpha = alpha F(t) - F(alpha t), the Renyi order | PROVED; alpha = 2 is prior work (rows 669, 670) (C3) |
| Identity I3 and its twisted-background form; the t-layer Identity L | PROVED; t = 1 is Identity L of row 712 (C2, C6) |
| Proposition K: Shannon information does not control the thermal sum | PROVED |
| 1.5: a mixture of M maps gains at most log M in (E22) | PROVED; its consequence for (TR-F) ARGUED |
| 2.1: data processing and chain-rule statements; the RG preserves the seed only as a partition-function statement | PROVED (standard) and READ; verdict ARGUED; c-, F-, a-theorems GUIDE |
| 2.2: chi2 SDPI constant = mu_1^2; KL route conditional on uniform entropy contraction; spectral radius = row sum for translation-invariant influence matrices | PROVED; non-uniformity of the Dobrushin constant ARGUED (GUIDE run) |
| Proposition Q: tree-type squared SDPI criteria are false on Z^3 (Ising, beta = 0.35) | PROVED given the Frohlich-Simon-Spencer bound (recalled); 2D form GUIDE |
| 2.3: I(X_0; X_n) <= 6 beta_W abs(B) and the general cut bound | PROVED |
| 2.4: trace-norm distance to rank one = S(n; B); bounded rank gives no rate and allows no gap | PROVED; TRG literature GUIDE |
| 2.5 to 2.9 | ARGUED, literature GUIDE |
| Proposition TB: (mu^-)^t <= eta_t <= kappa_t; p(a) <= kappa_t; p(a) >= (mu^-)^a/(1 + S(a)) | PROVED (C5, C6) |
| Corollary TB1: E^- >= m b - log(C b^2) on cubes for beta_W < 2/3 | PROVED given (AS-bg) (checked, row 790) |
| Proposition TB2: 1 - Z_anti/Z_per >= m^4/32 (1 - o(1)) at the flat background; (AS-bg) false for beta_1 > 4 G_3 = 1.0109 | PROVED given the Frohlich-Simon-Spencer bound (recalled); G_3 from quadrature (GUIDE number, Watson's integral) |
| The covariance form of the same ceiling for background-uniform slab routes to the area law | ARGUED |
| 3.5: thick-slab and Doob forms at order one | OPEN; observations GUIDE and ARGUED |
| Lemma Z'' and Consequence 2 (Corollary Z1' with 4/3) | PROVED (C4) |
| Consequence 1: (SEED-L) with phi_* < (L - 1) log(13/10) | ARGUED, as Lemma FL is |
| (SEED-FP), (E17), (ES) at order-one coupling | OPEN |

### 6.3 What this file did not cover

1. No paper was opened. Every outside result is recalled (GUIDE). Two proofs rest on recalled theorems, named as such: the infrared bound of Frohlich, Simon and Spencer (Propositions Q and TB2) and, for the 2D remark only, the exact solution of Onsager and Yang.
2. The account of Sussman and Alpoge was not opened; every READ about it goes through `library/gap-finishline-opus.md`.
3. The quantum-information results named in 2.3 were not checked against the lattice gauge setting beyond the mismatch stated there.
4. SU(N) with N >= 3: the flat-background layer is then the SU(N) principal chiral model; Proposition TB2 was not written for it.
5. No 4D numerics. The thick-slab question of 3.5 has no guide run (5, "Runs not made").
6. Lemma FL's other steps, Theorem SH and Lemma Z were used as stated in their sources and not re-checked.
7. Nothing in this file is checked by another model.

### 6.4 Items the lead may queue (suggestions only)

1. One check, by a model that did not write this file, of Lemma Z'' with its two consequences, Proposition TB, Corollary TB1, Proposition TB2 (the infrared-bound step (ii) and the Holder step (iii)) and Proposition Q. All are short.
2. If they hold: the constant of (SEED-L) in `library/gap-finishline-opus.md` 2.2 becomes (L - 1) log(13/10); Corollary Z1' of `library/gap-phys-seed.md` takes (4/3) Phi_4; the "GUIDE for this second step" of `library/gap-crux-fp.md:416` becomes a proof, with the threshold 4 G_3 = 1.0109; and row 834 (area law beyond 2/3, toward the ceiling of background-uniform slab routes) can cite a proved ceiling of 1.0109 beside the believed 0.94.
3. Four filters for any later information-theoretic proposal: (F-chi2) state it in chi-square, Renyi-2 or min-entropy form, or add a hypercontractive estimate (Proposition K); (F-loop) no tree or DAG data-processing arithmetic on the lattice (Proposition Q); (F-mix) a mixture of M maps gains at most log M (1.5); (F-sym) an argument from symmetry and information structure alone must fail for the adjoint Higgs model and for U(1) (2.1).
4. Not suggested: a proof lane on any candidate of this file; the 4D guide run of 3.5; a tensor-renormalization computation.

RESULT: no compression or information theory gives a handle on (SEED-FP) or (E17) at order-one coupling, and none is worth a dedicated proof lane: the seed is exactly a chi-square mutual information between slices (S(2n;B) = I_chi2(X_0;X_n)), the min-entropy of the box's thermal state (log(1+S) = H_inf) and a rank-one approximability statement, and the twist deficit is exactly the chi-square distinguishability of a slice and its centre flip (PROVED; restatements, with Theorem S already the rank-one "approximability implies decay" converse); data processing along the RG, chain rules, entropic c/F/a-theorems, mutual-information area laws (I <= 6 beta_W |B|, PROVED), rate-distortion, MDL, RSMI and bounded-rank tensor networks are group-blind or restate the seed, Shannon forms are strictly weaker than the seed (Proposition K), tree-type squared SDPI gains over Dobrushin are false on lattices (Proposition Q: 3D Ising at beta = 0.35 orders, with flip-odd thermal weight at least 0.019, while 6 tanh^2 = 0.68 < 1), and OSSS needs an FKG structure 4D SU(2) lacks; the requested twist-sector contraction coefficients were tested: the chi-square one equals e^(-E^-), the electric-flux energy (restates the flux half), the worst-case one-layer one is (AS-bg), which gives E^- >= m b - log(C b^2) for beta_W < 2/3 (Corollary TB1, given AS-bg) and is PROVED false for every beta_W > 4 G_3 = 1.0109 at the flat background via the Frohlich-Simon-Spencer bound (Proposition TB2: a proved ceiling 1.0109 for every background-uniform layer twist bound, beside the believed 0.94), and the thick-slab one is a boundary-uniform mixing hypothesis at the correlation length with no means (OPEN); by-product on the finish line: Renyi-L telescoping (Lemma Z'', PROVED) improves Lemma Z' from 2/rho to 1/(rho - 1) and widens the (SEED-L) margin from 0.131 L to (L - 1) log(13/10), about 0.262 (L - 1) (ARGUED, as Lemma FL is); nothing here is checked by another model.
