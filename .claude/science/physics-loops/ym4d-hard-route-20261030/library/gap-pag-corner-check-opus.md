# Check of gap-pag-corner-astra.md, Sections 1-3 and 6

- Checker: Claude Opus 5.5. Date: 2026-11-12.
- Author of the checked text: Codex gpt-6-astra. Every statement marked HOLDS is the author's result, and the credit is theirs.
- Read in full: `/Users/jonreilly/ym4d-lead/clone/.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-pag-corner-astra.md` lines 1-569. Sections 1, 2, 3.1-3.3 and 6 were checked line by line. Sections 4 and 5 were skimmed; I also checked the arithmetic of (7), the plaquette count in (8) and the derivative (9).
- Context read: `gap-crux-exercise-astra.md` lines 749-984 (8.1) and 1194-1389 (8.4, 8.5); `gap-gc-check-opus.md` (all).
- Method: by hand. One guide only, in this folder: `face_guide.py` with log `face_guide.log` (pure Python, `python3 -I`, own code; sparse CG on C^T C + D D^T). It reproduces the author's Section 5 face-test values exactly (L=1: 0.215885; L=2: 0.212202). It also gives t = 0.374 and 0.391 (at most 1/2), s = 1.025 and 1.060 (at least 2/3), and a = b = 0.350 and 0.363 (in [1/6, 1/2]). The guide uses the same formula as the author, so it checks the arithmetic only and is not an independent derivation. It decides nothing.
- Independence: one reader, the same source text. The derivations below are my own, done by hand.

## Verdict table

| Statement | Verdict |
|---|---|
| S1. Face-corner geometry; fully invariant pair; admissible in PA_g | HOLDS |
| S1. Present in every cover of the stated class | HOLDS AFTER CORRECTION (state the class as below; the two-site overlap is more than needed) |
| S2. (1) t <= 1/2 | HOLDS |
| S2. (2) s >= 2/3 | HOLDS |
| S2. (3) Corr >= 1/7, (4) trace Corr = c^2/(ab) >= 1/49, uniform | HOLDS |
| S3.1. Minima = interior-gauge orbit of I; no holonomy modes; forest slice; Hessian | HOLDS |
| S3.2. Laplace passage with moments; (5); positive-measure exteriors | HOLDS (notation clash S/S(A); the neighbourhood depends on beta) |
| S3.3. (6): beta_0(ell) for each fixed ell, uniform in torus and interval choices | HOLDS AFTER CORRECTION (quantifier order: the open set of exteriors depends on beta and on the cover) |
| S3.3. OPEN: beta_0 depends on ell, with no bound | HOLDS (correctly not claimed) |
| S4 (skim): (7) arithmetic, (8) count, (9) derivative | HOLDS |
| S6. Disposition | HOLDS AFTER CORRECTION (for the wider class of Section 1, "fixed block size" must mean bounded box sides; otherwise read it as the 8.1 covers) |

## 1. The face corner

Pair: B = I x J x K x L and C = I' x J' x K x L (indices (i,j,k,l) and (i+1,j-1,k,l), as in GC1). Coordinates are chosen so that min I' = 0 and min J = 0. Then v = (0, 0, a3, t), where a3 = min K and t-1 lies in L.

- v: 0 is in I and in I' (overlap); 0 is in J and in J'. So v is in B and in C.
- z = v - e1: -1 is in I and not in I' (since 0 = min I'). So z is in B only. w = v - e2: -1 is in J' and not in J. So w is in C only. u: not in C (coord 1), not in B (coord 2). Correct.
- Links at v. Outgoing (v, mu): base v, inside S. Incoming: U = (z,1) is in B\C; V = (w,2) is in C\B; (v - e4, 4) has base coordinate t-1, which is in L, so it is in S; e0 = (v - e3, 3) has base coordinate a3 - 1, which is not in K, so it is exterior. So e0 is the only exterior link at v, and v is a boundary vertex. Correct.
- (z - e3, 3) and (w - e3, 3) are exterior (third coordinate a3 - 1). So z and w are boundary vertices. Correct.
- p_U (1,3-plane, base z - e3) has links (z-e3,1), e0, (z-e3,3), U. All except U have third coordinate a3 - 1, so they are exterior. p_V is the same with V. p (base u) has links (u,1), V, U, (u,2). The two links with base u are exterior. Correct. U_p = A0 V U^-1 B0^-1, so at the identity exterior x(p) = x(U V^-1).
- In the fibre, ran E_C = functions of the links in S\C = B\C. x(p_U) = x(T U) with T exterior, so it lies in ran E_C; likewise x(p_V) lies in ran E_B. A plaquette trace is invariant under every gauge transformation, in particular at interior vertices. So both are admissible. For mean-zero f in ran E_C and g in ran E_B, <g, (E_B E_C - E_S) f> = <g, f>, so the PA_g norm is at least |Corr|. HOLDS.

Class. The author's class is sufficient but is stated loosely. Corrected statement: nonwrapping product-box covers (bounding box of the pair, plus its collar, a proper sub-box of the torus in every coordinate) with positive links assigned by base, containing an interacting pair B = I x J x K x L, C = I' x J' x K x L with these properties. Let a' = min I' and c = min J. Then a' - 1 and a' lie in I; c - 1 and c lie in J'; K is a proper interval (not the whole circle); L has at least two sites. The "two-site overlap" of the note is not needed: a one-site overlap with a' - 1 in I suffices. Every 8.1 cover has such a pair: the overlaps have at least 4 sites (earlier check), and the intervals have at least 17 sites, with N >= 12 ell. The author correctly excludes other link assignments and larger groups of blocks. HOLDS AFTER CORRECTION (wording only).

## 2. Quadratic model

- The covariance of CA is C (C*C)^+ C* = projection P_S onto ran C. Correct. X = A_U = +-(CA)_(p_U), so X is a function on the quotient; likewise Y. X - Y = -(CA)_p, since (CA)_p = A_V - A_U at zero exterior.
- (1): curls of patch cochains, extended by zero, lie in the exact 2-cochains of the N-torus, so P_S <= P_full. rank d1 = 4N^4 - dim Z^1 = 4N^4 - (N^4 - 1 + 4) = 3(N^4 - 1); this matches the Fourier count. The diagonal entries are equal by translation and axis permutation, so each equals 3(N^4-1)/(6N^4) <= 1/2. HOLDS.
- (2): h = d0 1_v restricted to S, which equals d0 1_v - 1_(e0) (e0 is incoming, value +1). So C h = -d1 1_(e0), and ||Ch||^2 = 6 because e0 lies in six plaquettes. All six touch S: each contains (v, mu) or (v - e_mu, mu) with mu in {1,2,4}, and these are free. Var(lA) = <l, (C*C)^+ l> = sup (lh)^2/||Ch||^2 for l vanishing on ker C. With l = 1_U + 1_V and lh = 2, s >= 2/3. HOLDS.
- (3): c = (s - t)/4 > 0. 4 sqrt(ab) <= 2(a + b) = s + t, so Corr >= (s-t)/(s+t) >= (1/6)/(7/6) = 1/7, because the ratio increases in s and decreases in t. a, b > 0 follows from c > 0 and Cauchy-Schwarz. HOLDS.
- (4): Cov(X^2, Y^2) = 2c^2 and Var X^2 = 2a^2 for a centred Gaussian pair; the three colours cancel. So Corr = c^2/(ab) >= 1/49. The bounds use only the local geometry at v, so they are uniform in the patch and in the torus. HOLDS.
- Guide agreement: see the header.

## 3. Wilson SU(2) at large beta

### 3.1
- Zero action: x(W) = 1 forces W = I, so every touching plaquette is I. The other plaquettes are exterior and equal I, so the field is flat on the torus.
- The bounding box of S is proper (extent at most about 14 ell/3 + 1, while N >= 12 ell), so each coordinate has an all-exterior cycle. These cycles connect to a common base point through the exterior shell, so the based holonomies are I and the field is pure gauge, g_x g_y^-1.
- Connectivity, checked: D = ((I x J) union (I' x J')) x K x L. A site that fails I x J and I' x J' moves in coordinate 3, keeping (x1, x2), to x3 outside K. A site that fails K or L is already outside the bounding box. The complement of a proper box in a torus of dimension at least 2 is connected: an interval's complement in a cycle is an arc, and two failing coordinates can be swapped. A boundary vertex in D carries an exterior link only as its target, and that link's base is outside D. A boundary vertex outside D has exterior outgoing links. So g is constant off the interior vertices, and a global constant removes it. Correct.
- Forest: every forest edge has an interior endpoint. U and V have two boundary endpoints, so they are not forest edges and are unchanged. Haar change of variables with no determinant: standard and correct. Unique minimum in the slice: correct.
- Hessian: a linear null vector has zero curl everywhere and zero exterior cycle sums. So it is d0 phi with phi = 0 off the interior vertices, and the forest forces phi = 0. The slice is a complement of ker C, so the laws of the quotient functionals X and Y agree with Section 2. HOLDS.

### 3.2
- x(exp(iA.sigma)) = cos|A|. The Haar density in exponential coordinates is J(A) = (sin|A|/|A|)^2 up to normalisation, with J(0) > 0. The action is (1/2)||CA||^2 + O(|A|^3), colour-diagonal at second order. Correct.
- Local lower bound k_S|A|^2, global gap m_S, Z_beta >= c beta^(-M/2), and tail at most C beta^(M/2+k) e^(-beta m_S): standard Laplace estimates, correct. Dominated convergence for beta(1 - cos|A_U|) <= |Y_U|^2/2 gives convergence of the first, second and joint second moments.
- Limits: |X|^2 = a chi^2_3, so Var(|X|^2/2) = 6a^2/4 = 3a^2/2 and Cov = (1/4)(3)(2c^2) = 3c^2/2. So the ratio is c^2/(ab) and (5) HOLDS. beta_0(S) exists by convergence.
- Positive measure: at finite beta the variances are positive (x(p_U) is non-constant under a positive density), and the correlation is continuous in the finitely many exterior links of the touching plaquettes. So the correlation exceeds 1/64 on a neighbourhood of I. That neighbourhood is obtained for each beta >= beta_0 separately; no uniformity in beta is claimed, and none is needed.
- Notation: S denotes both the patch and the action S(A). This is harmless but should be renamed. HOLDS.

### 3.3
- For fixed ell, the pair shape is determined by finitely many (s_(i-1), s_i, s_(i+1)) and offsets in coordinates 1 and 2, plus the K and L lengths. That is finitely many shapes up to translation; coordinate permutation is not needed. The conditional law at the identity exterior depends only on S and its touching plaquettes once S is nonwrapping, which holds for every admitted N >= 12 ell. Taking the maximum of finitely many beta_0(S) gives beta_0(ell), independent of N and of the interval choices. "Uniformly in the torus": PROVED.
- Correction to (6): read it as "for every beta >= beta_0(ell), every cover, and the chosen pair, there is an open set O(beta, cover) of exteriors on which ...". The open set is not uniform in beta. The pair's correlation is > 1/64; (6) writes >= 1/64, which is weaker and fine.
- Dependence on ell: beta_0(ell) is a maximum over the patches of size about ell. The proof's constants (M, epsilon_S, k_S, m_S) all depend on S, so beta_0 depends on ell and may grow without bound. The note states this, makes no bound claim, and keeps "exists beta_* for all ell", the cutoff trajectory and order-one beta OPEN. HOLDS.

## 4 (skim)
- 4.1: a, b >= 1/6 (same h, lh = 1) and a, b <= 1/2 (from (1)). For (7), sqrt((V_U+d)(V_V+d)) <= D(1 + 24d) and the numerator is >= D/49 - d. The result 8824/491176 = 1103/61397 > 1/64 is correct (1103 x 64 = 70592). The nonlinear premise is OPEN, as stated.
- 4.2: U and V lie in 6 plaquettes each and share p, giving 11; besides p, p_U and p_V, each other plaquette contains a further free link (checked for U: (z,2), (z,3), (z,4), (v-e4,4)). The counterexample R is legitimate as a refutation of the inference only. (9): integral x(V) x(UV^-1) dV = x(U)/4, so the derivative is 1/16 and the Corr slope is 1/4. Correct.
- 4.3: k = 1 - gap(a_B + a_C) <= 1 - exp(-2 beta n), and restricting to invariants does not increase it. Correct.

## 6. Disposition
- "At every fixed lattice block size of the stated product-box class, PA_g fails at sufficiently weak coupling, uniformly in the torus": proved for the 8.1 covers by 3.3. For the wider Section 1 class, the same finiteness argument works only if "fixed block size" means bounded box side lengths, and the tori are large enough to be nonwrapping. With that reading it HOLDS. It holds in both the every-exterior and the essential-supremum forms (3.2).
- "Merely removing the open-link functions of GC1 does not make this fixed-size criterion valid": HOLDS. This answers the risk named in `gap-gc-check-opus.md` Section 9, through a different, face pair (not the interior-transverse pair there, which remains GUIDE-only, as the note says).
- OPEN items (growing blocks with exists beta_*, the cutoff trajectory ell_h = ceil(R/h) with beta_h, order-one beta) match what is proved: nothing in 3.2 controls beta_0(ell) as ell grows. "No mass gap route refuted, no status": correct.
- Correction: the RESULT line of the note says "uniformly in the torus" correctly, but it should also say "for every fixed ell (beta_0 depends on ell, unbounded a priori)", which it does implicitly via beta_0(ell).

RESULT: Sections 1, 2, 3.1-3.3 and 6 of gap-pag-corner-astra.md HOLD (credit Codex gpt-6-astra), with wording corrections only: state the product-box class precisely (a one-site overlap with a'-1 in I and c-1 in J', proper K, |L| >= 2, nonwrapping); in (6) the open set of exteriors depends on beta; the Section 6 claim for the wider class needs bounded box sides. beta_0(ell) is proved uniform in the torus and in the interval choices but depends on ell with no bound, and the note correctly leaves the uniform-in-ell, cutoff-trajectory and order-one questions OPEN.
