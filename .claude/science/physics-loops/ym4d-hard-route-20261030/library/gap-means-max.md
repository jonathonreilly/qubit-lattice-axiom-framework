lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-12T11:09Z

# gap-means-max: which means could verify a seed or (G_ev) for SU(2) at the scale of the correlation length

Queue row 737 of `FINISH.md`. Pinned commit e6c83cc9a. Author document, research-stage working state. It grants no status and is not a public claim. One model wrote it; nothing here is checked by another model.

Labels used: **proved** (full argument written here or in the cited note), **argued** (argument written, a step is not closed), **reading** (what a source says, with its place), **belief** (no argument), **guide** (numeric or heuristic, cannot discharge a step), **open**.

Status of this file: in progress. Sections are appended as they are finished. Section 4 (the proof attempt) was written first, so that it survives an error.

## 0. Repo search, rule 0a, sources read

**Read in full for this item.** `GOAL.md`. `FINISH.md` lines 1 to 84, 299 to 349, row 737. `library/gap-skeleton-final.md` Sections 0 to 5, 8 to 11, 13.14 to 13.17. `library/gap-flux-exercise.md` Steps 0 to 3, 8.1 to 8.5, 8.7, 9. `library/gap-flux-exercise-check.md` Sections 7, 8. `library/gap-form-exercise.md` 2.D, Step 3, Steps 6, 7, 9. `library/prior/gap-precedent-lit.md`. `library/gap-kappa-order.md`. `library/gap-crux-restate.md` Section 3.4 (Lemmas K, X, E, E', Theorem S, Corollaries S2, S3').

**Rule 0a (before the attack of Section 4).** The statement attacked is a form of (EV-STEP) (`gap-flux-exercise.md` 8.5). `library/open-core.md`: no line for "EV-STEP", "even step", "rigid", "light sector", "group of four". FINISH rows that name (EV-STEP): 731 (its source; it states the statement open, "no mechanism", and does not queue it) and 732 (the check; "(EV-STEP) stays open"). `gap-skeleton-final.md` 13.16 lists it as open and not queued. No row owns it or attacks it. Section 4 attacks it with a mechanism that those files do not hold (4.9 says what is new and what is theirs).

**Other branches.** A scratch fetch of main and of the pull requests 10114, 10133, 10141, 10144, 10149 was searched for flux-sector work; the result is in Section 6.

**The account.** `gap-flux-exercise-check.md` Section 8 (Codex gpt-6-astra) searched the index of the complete account of Sussman and Alpoge (with Claude and Codex) and found no centre-flux, dyonic or Pfaffian-sector theorem; CA-I 2702-2712 excludes a mass-gap assertion. I did not repeat that search. Nothing of the account is ported in this file. Its Wilson convolution and transfer construction is the base of `gap-transfer.md`, which every statement below reads through (TM-tw).

**Credit.** The twist and flux frame, and the argument that in a massive phase the light fluxes form a self-dual set: G. 't Hooft, Nucl. Phys. B 153 (1979) 141 (recalled, not re-read; no step below rests on it). The sector sums, the crossing identity (*), the sum rule (SR), Lemma CL1, Proposition CL and Theorem S-w: `gap-flux-exercise.md` (Claude Fable 5.2; checked by Codex gpt-6-astra, row 732). Lemmas A, K, X, E, E' and Theorem S: `gap-crux-restate.md` and `gap-seed-check-astra.md` (rows 697 to 699). The four means (M1) to (M4): `gap-form-exercise.md` (row 735).

## 4. Route 1, first statement: an even seed at one size gives two of the three seeds (Theorem R)

All of Section 4 is **proved** by Claude Fable 5.2 (max) in this file, given the inputs of 4.1. It is not checked by another model. Sections 1 to 3 (the means and the plan) follow this section in the file's numbering and were written after it.

**In words.** The lane has three seeds, and each one counts seven flux sectors. Theorem R below needs no flux sector in its hypothesis. It reads two numbers of the centre-even sector of one symmetric torus: its thermal sum, and the defect of additivity of the vacuum energy. If both are small, the flux sectors have no choice: four of every sixteen crossed sectors weigh as much as the vacuum sector and twelve weigh nothing, the four form a self-dual group, and two of the three seeds hold. This is 't Hooft's dichotomy for a massive phase, as a finite inequality with constants.

### 4.1 Inputs

Each input is a statement of the lane that another model checked. I use them as written.

- **(TM-tw), (F1), (S3)**: `gap-flux-exercise.md` 3.0 and 3.1; checked by Codex gpt-6-astra (row 732, "The input (TM-tw), including Pf(k)=1: HOLDS"). For every box B with sides at least 3 and every magnetic twist m: T_{B,m} is a positive trace-class operator that commutes with the flips; Z^{e+m}(t, B) = Tr(T_{B,m}^t C^e) for t >= 3; a permutation of the axes maps the twist to its image and keeps Z^k; the sector sums are Z_{chi,m}(t; B) = Tr(T_{B,m}^t P_chi) = (1/8) sum_e (-1)^{chi.e} Z^{e+m} >= 0; every eigenvalue of T_{B,m} is at most lambda_0(B), the top eigenvalue of the periodic box, which is simple with an even eigenvector.
- **Lemma A (a)**: for S >= 0 trace class, (Tr S^k)^(1/k) is non-increasing in k (`gap-crux-restate.md` L37; rows 698, 699).
- **Lemma K (b)**: e(jb) <= j e(b), where e(b) = log lambda_0(b, c, d) and c, d are fixed (`gap-crux-restate.md` 3.4).
- **Lemma CL1 and Proposition X16**: `gap-flux-exercise.md` 8.3, 8.5; checked (row 732).
- **Lemma W, Theorem S-w, Corollary EV, Theorem EV-L**: `gap-flux-exercise.md` 8.2, 8.4; checked (row 732). Lemmas X and E' for W_w: by Theorem S-w.

### 4.2 Notation

Tori have sides (n_1, n_2, n_3, n_4), all at least 3. Frame 1: direction 1 is time. A sector of a box B is (chi; m) in Z_2^3 x Z_2^3, with indices 2, 3, 4. Z_{chi,m}(t; B) is its sector sum at time t. e(B) := log lambda_0(B). The even sector is 0 := (0; 0), and S_ev(t; B) = Z_0(t; B)/lambda_0(B)^t - 1 >= 0.

X := Z_2^4. A point x = (x_1, x_2, x_3, x_4) of X stands for the sector chi = (0, x_1, x_2), m = (0, x_3, x_4). So x_1, x_2 are the parities under the flips of the directions 3, 4, and x_3, x_4 are the twists m_3 = k_24, m_4 = k_23. On X: B(x, y) := x_1 y_4 + x_2 y_3 + x_3 y_2 + x_4 y_1 (mod 2), and for a function f on X, (Hf)(x) := (1/4) sum over y of (-1)^{B(x,y)} f(y). B is bilinear, symmetric, B(x, x) = 0, and B(u, .) = 0 only for u = 0. So H H = 1. A subgroup L of X is *isotropic* if B = 0 on L x L.

The three sector sets of Proposition CL (b), written by one element alpha of Z_2^2 each: Sigma_w = {(chi; m): (chi_nu, m_nu) is (0,0) or alpha_w, for nu = 2, 3, 4}, with alpha_per = (1,0), alpha_full = (0,1), alpha_kappa = (1,1).

### 4.3 Lemma R1 (the crossed slices)

Let a, b, c, d >= 3.

(a) Z_0(a; (b, c, d)) = (1/4) sum over z in X of Z_z(b; (a, c, d)).

(b) On a torus with n_1 = n_2 = a: for each (chi_2, m_2) in Z_2^2 the function G(x) := Z_{(chi_2, x_1, x_2), (m_2, x_3, x_4)}(a; (a, c, d)) on X satisfies G = HG. So G(x) <= G(0) for every x, and the sum of G over X is 4 G(0).

Proof. (a) is (*) of Proposition X16. (b) Put w(k) := Z^k(a, a, c, d) for k in K. The exchange tau of the axes 1 and 2 maps the torus (a, a, c, d) to itself, so w o tau = w by (TM-tw). In the notation of 8.3, what(chi; m) = sum_e w(e; m) (-1)^{chi.e} = 8 Z_{chi,m}(a; (a, c, d)) by (F1). Lemma CL1 gives G = HG for every slice. G >= 0, so G(x) = (1/4) sum_y (-1)^{B(x,y)} G(y) <= (1/4) sum_y G(y) = G(0). QED

### 4.4 Lemma R2 (finite algebra: weights that are almost 0 or 1)

Let p be a function on X with p >= 0, Hp = p, p(0) = 1. Put Q := sum over x of p(x)(1 - p(x)).

(a) p <= 1 and the sum of p over X is 4. So Q >= 0.

(b) If Q <= 4 theta with theta < 1/20, then L := {x: p(x) > 1/2} is an isotropic subgroup of X with exactly four elements, and

eta := sum over x in L of (1 - p(x)) + sum over x not in L of p(x) <= 2Q <= 8 theta.

Proof. (a) As in Lemma R1 (b). (b) For x in L: 1 - p(x) <= 2 p(x)(1 - p(x)). For x not in L: p(x) <= 2 p(x)(1 - p(x)). So eta <= 2Q <= 8 theta < 2/5.
*Count.* 4 = sum p = |L| - sum_{L} (1 - p) + sum_{not L} p, so | |L| - 4 | <= eta < 1, and |L| = 4.
*Isotropic.* Let x be in L, and let n be the number of y in L with B(x, y) = 1. Then 4 p(x) = sum_y (-1)^{B(x,y)} p(y) <= (4 - n) - (n - sum_{L}(1 - p)) + sum_{not L} p = 4 - 2n + eta. Also p(x) >= 1 - eta. So 2n <= 5 eta < 2, and n = 0.
*Subgroup.* 0 is in L. Let x, x' be in L. Then B(x + x', y) = 0 for y in L, so 4 p(x + x') >= sum_{L} p - sum_{not L} p >= 4 - eta > 2. So x + x' is in L. QED

### 4.5 Proposition R3 (rigidity for one pair of axes)

Let a, c, d >= 3, A := (a, c, d), and

eps := S_ev(a; A), Delta := a (2 e(a, c, d) - e(2a, c, d)), theta := 1 - exp(-Delta) (1 + eps)^(-2), p(x) := Z_x(a; A)/Z_0(a; A) for x in X.

Then: (a) Delta >= 0, p >= 0, Hp = p, p(0) = 1, and sum over x of p(x)(1 - p(x)) <= 4 theta. (b) If theta < 1/20, the conclusion of Lemma R2 (b) holds for p.

So the sixteen sectors of the box A at the time a split into four that carry the weight of the even sector, up to eta, and twelve that carry at most eta in total.

Proof. Delta >= 0 by Lemma K (b) with j = 2. Hp = p by Lemma R1 (b) for the slice (chi_2, m_2) = (0, 0) of the torus (a, a, c, d).
*The lower bound.* Lemma R1 (a) on the torus (a, 2a, c, d): Z_0(a; (2a, c, d)) = (1/4) sum_z Z_z(2a; A). The left side is at least lambda_0(2a, c, d)^a, because S_ev >= 0.
*The upper bound.* For each z = (chi; m), the operator S := T_{A,m} P_chi is positive and trace class, and Z_z(t; A) = Tr S^t. By Lemma A (a), Z_z(2a; A) <= Z_z(a; A)^2.
*Together.* 4 lambda_0(2a, c, d)^a <= sum_z Z_z(a; A)^2 = Z_0(a; A)^2 sum_z p(z)^2, and Z_0(a; A) = lambda_0(A)^a (1 + eps). So sum p^2 >= 4 exp(-Delta)(1 + eps)^(-2) = 4 (1 - theta). With sum p = 4 this is sum p(1 - p) <= 4 theta. QED

**Where the information comes from.** The lane used the same two facts in Proposition EVL to bound the even sum of the doubled box from above, and lost a factor Theta. Here they are used the other way: the even sum of the doubled box is at least 1 for free, and this bounds sum p^2 from below. The weights lie in [0, 1] and sum to 4, so sum p^2 = 4 forces them to be 0 or 1.

### 4.6 Theorem R

**Definition (ES), the even seed at the size a.** Let a >= 3 and

eps := S_ev(a; (a, a, a)), delta := a (8 e(a, a, a) - e(2a, 2a, 2a)).

(ES) at a is: eps <= 10^(-7) and delta <= 10^(-7).

eps is the thermal sum of the centre-even sector of the cube of side a at the time a (the symmetric torus a^4). delta/a is E_0((2a)^3) - 8 E_0(a^3), with E_0 = -e the ground energy of the periodic cube: the defect of additivity of the vacuum energy. Both read the even sector only: lambda_0(B) is the limit of Z_0(t; B)^(1/t).

**Theorem R.** delta >= 0. If (ES) holds at a, then there is exactly one alpha in {(1,0), (0,1), (1,1)} such that:

(a) for each of the two w in {per, full, kappa} with alpha_w != alpha: S_w(a; (a, a, a)) <= 1.27 x 10^(-5), and

S_w(a; (2a, 2a, 2a)) <= 1.02 x 10^(-4) < 1/5041;

(b) for the w with alpha_w = alpha: S_w(a; (a, a, a)) > 2.

So an even seed gives two of the three seeds of Corollary EV at the size N = a, and it says which one fails.

Proof. *Step 0 (the three deficits).* Put Delta_1 := a (2 e(a, a, a) - e(2a, a, a)), Delta_2 := a (2 e(2a, a, a) - e(2a, 2a, a)), Delta_3 := a (2 e(2a, 2a, a) - e(2a, 2a, 2a)). Each is >= 0 by Lemma K (b), applied to one side of the box with the other two fixed (e(B) does not depend on the order of the sides, by (TM-tw)). 4 Delta_1 + 2 Delta_2 + Delta_3 = delta. So delta >= 0 and Delta_1 <= delta/4.

*Step 1 (rigidity on a^4).* Proposition R3 with c = d = a. theta = 1 - exp(-Delta_1)(1 + eps)^(-2) <= Delta_1 + 2 eps <= 2.25 x 10^(-7) < 1/20, because exp(-u) >= 1 - u and (1 + eps)^(-2) >= 1 - 2 eps. So L := {x in X: p(x) > 1/2} is an isotropic subgroup with four elements and eta <= 8 theta <= 1.8 x 10^(-6).

*Step 2 (symmetry and dominance).* For each of the 64 sectors sigma = (chi; m) of the cube put rho(sigma) := Z_sigma(a; (a, a, a))/Z_0(a; (a, a, a)). So rho = p on X. A permutation pi of {2, 3, 4} acts on sectors by permuting the indices of chi and of m alike, and rho(pi sigma) = rho(sigma): by (TM-tw) Z^{pi k} = Z^k on the torus a^4, and pi permutes the indices of e and of m alike (8.3), so (F1) gives the claim. For nu in {2, 3, 4} let sigma|nu be the sector that keeps (chi_nu, m_nu) and has the other four entries 0. **Dominance: rho(sigma) <= rho(sigma|nu).** For nu = 2 this is Lemma R1 (b) for the slice (chi_2, m_2) of sigma. For nu = 3, 4 apply the permutation that exchanges 2 and nu.

*Step 3 (the group L is one of three).* For (c, n) in Z_2^2 let t(c, n) be the sector chi = (0, 0, c), m = (0, 0, n), that is the point (0, c, 0, n) of X. Put A_0 := {(c, n): (0, c, 0, n) in L}. A_0 is a subgroup of Z_2^2, because L is a subgroup. Let x be in L and sigma its sector. sigma|3 has chi = (0, x_1, 0), m = (0, x_3, 0); the exchange of 3 and 4 maps it to t(x_1, x_3). By dominance and symmetry, p((0, x_1, 0, x_3)) = rho(sigma|3) >= rho(sigma) > 1/2, so (x_1, x_3) is in A_0. In the same way sigma|4 = t(x_2, x_4) gives (x_2, x_4) in A_0. So L lies in {x: (x_1, x_3) in A_0 and (x_2, x_4) in A_0}, a set with |A_0|^2 elements. Hence |A_0| >= 2. If |A_0| = 4, then L contains the four points (0, c, 0, n), so L is that set; the exchange of 3 and 4 maps L to itself (Step 2) and maps that set to {(c, 0, n, 0)}, a different set. So |A_0| = 2: A_0 = {(0,0), alpha} for one alpha != (0,0), and L = {x: (x_1, x_3) in A_0 and (x_2, x_4) in A_0}.

*Step 4 (two sector sets are small on a^4).* Let alpha_w != alpha and sigma in Sigma_w, sigma != 0. Some nu has (chi_nu, m_nu) = alpha_w. By dominance and symmetry rho(sigma) <= rho(sigma|nu) = p(x*), with x* := (0, alpha_w1, 0, alpha_w2). x* is not in L, because alpha_w is not in A_0. So rho(sigma) <= eta. Now 1 + S_w(a; (a,a,a)) = (1 + eps) sum over sigma in Sigma_w of rho(sigma), so

S_w(a; (a, a, a)) <= eps + 7 eta (1 + eps) <= 10^(-7) + 7 (1.8 x 10^(-6))(1 + 10^(-7)) < 1.27 x 10^(-5).

*Step 5 (three doublings of the box at the fixed time a).* Let B be a box and B' the box with one side doubled, from a to 2a, the other two sides fixed. W_w is invariant under permutations of the sides, and W_w(t, B) = Tr (T^w_B)^t with top eigenvalue lambda_0(B) (Lemma W). Cross the doubled side with the time: W_w(a, B') = Tr (T^w_{B_a})^(2a) <= (Tr (T^w_{B_a})^a)^2 = W_w(a, B)^2, where B_a is the box with the sides a (the old time) and the two fixed sides; Lemma A (a). So

1 + S_w(a; B') <= (1 + S_w(a; B))^2 exp(a (2 e(B) - e(B'))).

Apply this along (a, a, a), (2a, a, a), (2a, 2a, a), (2a, 2a, 2a):

1 + S_w(a; (2a)^3) <= (1 + S_w(a; a^3))^8 exp(4 Delta_1 + 2 Delta_2 + Delta_3) = (1 + S_w(a; a^3))^8 exp(delta).

With Step 4: S_w(a; (2a)^3) <= exp(8 x 1.27 x 10^(-5) + 10^(-7)) - 1 = exp(1.017 x 10^(-4)) - 1 < 1.02 x 10^(-4), and 1/5041 > 1.98 x 10^(-4).

*Step 6 (the third set).* For alpha_w = alpha the three points of L other than 0 are sectors of Sigma_w. So S_w(a; a^3) >= (1 + eps)(3 - eta) > 2. alpha is unique because A_0 is defined by the weights. QED

### 4.7 Corollaries

**Corollary R4 ((ES) at one size gives (G_ev) at all sizes, and the gap of the periodic limit on the centre-blind functions).** Let (ES) hold at a. Then for every integer L >= 2a, with k >= 0 such that D := 2^(k+1) a <= L < 2D:

S_ev(D/2; L^3) <= q^(2^k)/71 with q <= 5041 x 1.02 x 10^(-4) < 0.515, and m_ev(L^3) >= log(1/q)/a > 0.66/a.

Every limit point of the periodic symmetric tori clusters exponentially at the rate 0.66/a on the functions with (i) of 8.2, in the four directions.

Proof. Theorem R (a) is the hypothesis of Corollary EV with N = a. QED

This is (EV-STEP) of `gap-flux-exercise.md` 8.5 with the hypothesis (ES) in place of "S_ev(N; (2N)^3) <= t_0". The hypothesis is on the even sector alone, at one size.

**Corollary R5 (the converse: a seed gives (ES) at a larger size).** Let S_w(N; (2N)^3) < 1/5041 for one w and one N >= 3, q := 5041 S_w(N; (2N)^3). Then (ES) holds at a = 2^(k+1) N for every k with q^(2^k) <= 4.5 x 10^(-6).

Proof. Put s_k := S_w(a/2; a^3) <= q^(2^k)/5041 (Theorem S-w). *eps.* The even sector is in Sigma_w and thermal sums do not increase with the time: eps <= S_w(a; a^3) <= s_k. *delta.* Lemma X for W_w: (b - a') kappa(b) <= g(a', b) for a' < b, with kappa >= 0 the deficit in the side b. For a doubling of one side from a to 2a: a (2 e(B) - e(B')) = a (2 kappa(a) - kappa(2a)) <= 2a kappa(a) <= 4 g_w(a/2; B). So Delta_1 <= 4 log(1 + s_k). By Lemma E' with (a', b, h) = (a/2, a, 2a) the exponent is 4: g_w(a/2; (2a, a, a)) <= 4 log(1 + s_k) and g_w(a/2; (2a, 2a, a)) <= 16 log(1 + s_k). So Delta_2 <= 16 log(1 + s_k), Delta_3 <= 64 log(1 + s_k), and delta <= (16 + 32 + 64) log(1 + s_k) <= 112 s_k. Both are at most 10^(-7) if 112 q^(2^k)/5041 <= 10^(-7). QED

**So the crux has an equivalent form with no flux sector in it:**

(there are w and N with S_w(N; (2N)^3) < 1/5041) if and only if (there is a with (ES) at a).

**Corollary R6 (the flux phase cannot change while an even seed exists; argued, the continuity step is not written with constants).** At a fixed coupling, alpha is the same at every size a at which (ES) holds. (If (ES) holds at a_1 with alpha_1 and at a_2 >= 2 a_1 with alpha_2 != alpha_1, then the w with alpha_w = alpha_2 has a seed at a_1 by Theorem R (a), so S_w is small on the cube of side a_2 by Corollary S3' and the monotony in the time; this contradicts Theorem R (b) at a_2.) All the quantities of a fixed torus are continuous in beta. So on an interval of couplings on which (ES) holds at some size for every coupling, alpha is constant. At small beta the periodic seed is proved (`gap-seed-sc.md`, row 701: beta below 1/12800; row 711: below 1/18, as `gap-skeleton-final.md` 13.10 and 13.12 report; I did not re-read those proofs). By Theorem R (b) alpha is then not alpha_per. Consequence: **if an even seed exists at every coupling of an interval (0, beta_1], then the periodic seed holds on all of it.** In words: with a gap of the centre-blind sector at every coupling, heavy electric flux at strong coupling stays heavy. Confinement cannot be lost without the even seed failing first. (Whether alpha is alpha_full or alpha_kappa at small beta decides the kappa seed in the same way. I expect alpha_full, because all twists are free at strong coupling; that is recalled, and I did not find it written in the lane.)

### 4.8 Tests of Theorem R against known cases

- **Z_2 gauge theory at large beta** (Proposition Z2 of `gap-form-exercise.md`: the full and the kappa seed hold at N = 3 for beta >= 91). Theorem R allows this: alpha = alpha_per, the electric sectors are the four light ones. Pass.
- **A scale-invariant model.** Theorem R must not apply. In the two-dimensional critical Ising model (recalled conformal data, as in 8.6 of row 731; the two-dimensional form of R3 has four sectors, sum p = 2) the weights at a = b are about (1, 0.456, 0.456, 0.086): not 0 or 1. The hypothesis fails there through Delta: a (2 kappa(a) - kappa(2a)) = pi c/4 = 0.39 with c = 1/2, so theta is about 0.33. The even sum alone is small there (about exp(-2 pi) = 0.002). So **the deficit hypothesis cannot be dropped from Proposition R3**, and eps <= 10^(-7) alone is not shown to suffice (open; see 4.9). *recalled data; a guide.*
- **U(1) at weak coupling.** No gap. (ES) fails: the photon gives eps of order exp(-2 pi) and delta of order one (recalled; Casimir energy -c/L). Pass.
- **A guide run in two dimensions** is in 4.10.

### 4.9 What is new, what is not shown, what is open

**New against the lane's record.** Proposition EVL has the two facts (the crossing identity (*) and Lemma A in each sector) and reads them as a loss Theta in [1/4, 4]. Its text says "(EV-STEP) follows from: an even seed at N forces one of the three seeds at a comparable size ... In a massive phase 't Hooft's argument says that they are (recalled; not proved)". Section 4 proves that statement, with the deficit as the second hypothesis. The three steps that the record does not hold: the weights are at most the even weight at a = b (Lemma R1 (b)); the doubled even sum is used as a lower bound (R3); dominance and the symmetry of the cube select one of three groups (Steps 2, 3). The idea that a massive phase has a self-dual set of light fluxes is 't Hooft's.

**Not shown.**
1. (ES) for SU(2) at any size at any coupling above the strong-coupling range. At small beta it holds by Corollary R5 and the proved periodic seed.
2. That eps small implies delta small. In the class of the lemmas I know no proof and no counterexample. A hypothetical table with eps = 0 and all fifteen flux weights 1/5 satisfies p = Hp and the bounds used here, and has exp(-Delta) <= 0.4. It is not shown to come from a model: two equal fluxes should fuse to an even state of twice the energy, and that uses locality, which the class does not hold.
3. Anything for the functions that see the centre.
4. The constants 10^(-7) are not optimized.

**Open (named).** (ES-1) Is there, for Wilson SU(2), a bound delta <= C eps or delta <= C S_ev at a comparable shape? It would make the even seed one number. A route: the deficit kappa(a) is the growth rate of the even thermal sum on long boxes, kappa(a) = lim over b of (1/b) log(1 + S_ev(a; (b, c, d))) (from Lemma R1 (a): only the sectors of the crossed box with top eigenvalue lambda_0 survive as b grows); what is missing is the step from the box of length a to long boxes without the factor 4.

### 4.10 A guide run in two dimensions

(to be appended)
