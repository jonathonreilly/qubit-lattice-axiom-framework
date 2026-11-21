# gap-es1-opus: does a small even thermal sum bound the vacuum-energy defect? (ES-1)

- Author: Claude Opus 5.5 (one session, alone). Date: 2026-11-11.
- **Not checked by another model.** Research note, not a public claim. No mass gap is proved here.
- Sources read (read-only, folder `ym4d-lead/clone/.claude/science/physics-loops/ym4d-hard-route-20261030/library/`):
  - `gap-means-max.md` Sections 4.1 to 4.10 in full (Theorem R, Lemmas R1, R2, Proposition R3, Corollaries R4 to R8, the tests 4.8, the open list 4.9, the 2D Ising run 4.10). Author there: Claude Fable 5.2 max.
  - `gap-means-max-check.md` Section 1 (R1, R2, R3), and the headings of the rest. Checker there: Codex gpt-6-astra max.
  - `gap-crux-restate.md` Section 1 (setting, (TM), (TM-c), Lemma A) and Section 3.4 in full (Lemmas K, X, E, E', Theorem S, Corollaries S2, S3, S3').
  - `gap-seed-limit.md` Section 1 and Section 5 in full; the headings of Sections 2 to 4.
  - `gap-phys-seed.md` Part 3 in full (Lemmas Z, Z', Z3, Theorems ZD, ZD-c, Lemma DIL, Proposition MB, the tests).
  - `gap-skeleton-final.md` Sections 13.18 and 13.19.
  - Not opened, as instructed: `gap-es1-astra.md`, `gap-crux-exercise-astra.md`, `gap-crux-exercise-max.md`.
- Marks: **PROVED** (every step written), **ARGUED** (a step not closed; the gap is named), **GUIDE** (numeric or heuristic), **OPEN**.
- Credits. The setting, Lemma A, Lemma K, Lemma R1 (crossing), Proposition R3 and Corollary R7 are from the files above (authors named there). The idea that a massive phase has a self-dual set of light fluxes is 't Hooft's (1979). The low-temperature (surface) expansion of Z_2 lattice gauge theory used in Section 4 is standard (Wegner 1971; Balian, Drouffe and Itzykson 1975); I re-derive the few counts I use. The intuition that "two equal fluxes fuse into an even state" is stated in `gap-means-max.md` 4.9, item 2.

## 0. Answer in short

(ES-1) in its linear form is **false in the class of the lane's lemmas**. Z_2 lattice gauge theory (the SU(2) Wilson weight restricted to centre-valued links; the lane uses it as a test model of the same lemmas) at side a = 3 and large beta has, with u = e^(-2 beta),

delta = 216 u^9 + O(u^10), eps <= C u^12 (and, ARGUED, eps = 81 u^12 (1 + o(1))),

so delta/eps grows at least like u^(-3) and no constant C works; nor does any power eps^gamma with gamma > 3/4. The same holds with eps replaced by the even thermal sum at time a on any box, so "a comparable shape or a longer time" does not rescue it. The proof (Section 4) uses plaquette counts, Theorem V below and a min-max bound. The one step not re-checked is that Z_2 satisfies the class inputs; it is routine (ARGUED). The counterexample is at a = 3; it does not touch a statement restricted to large a, nor Wilson SU(2) itself.

What is true, and proved, is a sharp account of what delta *is*:

1. (Theorem V) the deficit of one doubling is the *flux variance* of the crossed sectors, up to sector thermal sums: -log(1 - Q/4) - 2 log(1 + eps) <= Delta <= -log(1 - H_L/2 - (1/2) sum_L s_z) + log(1 + S') - 2 log(1 + eps), where Q = sum p(1 - p), H_L is the weight of the twelve heavy sectors, s_z are sector thermal sums, and S' is the even sum of the doubled box.
2. (Theorem LB) the long-box form of 4.9 holds, with the factor 4 turned into an additive log 4 that disappears on long boxes: delta <= 2a (4 kappa_{a,a} + 2 kappa_{2a,a} + kappa_{2a,2a}), where kappa_{c,d} = lim over b of (1/b) log(1 + S_ev(a; (b, c, d))) is the growth rate of the even thermal sum on long boxes; and for every finite b > a, a(2e(a,c,d) - e(2a,c,d)) <= (2a/(b - a)) [log 4 + log(1 + S_ev(a; (b, c, d)))].
3. (Proposition FUSE-suff) a *fusion* input, "each heavy crossed flux weight is at most K times the square root of the even thermal sum, and the light sectors are no more excited than the even one", gives delta <= C(K) (sqrt(S_ev) + S_ev at doubled boxes). This is the weaker form delta <~ sqrt(eps). The Z_2 point satisfies it given the ARGUED lower bound on eps, and the 2D Ising run does not refute it (GUIDE). Fusion is OPEN in the class; it is where locality has to enter.

## 1. Setting and notation (from the sources; nothing new)

The class. Everything in Sections 2 and 3 uses only the inputs of `gap-means-max.md` 4.1, as written there: (TM-tw), (F1), (S3) (positive trace-class twisted transfer operators T_{B,m}, commuting with the flips; Z^{e+m}(t, B) = Tr(T_{B,m}^t C^e); permutation symmetry; sector sums Z_{chi,m}(t; B) = Tr(T_{B,m}^t P_chi) >= 0; every eigenvalue of T_{B,m} is at most lambda_0(B), the top eigenvalue of the periodic box, simple with an even eigenvector), Lemma A, Lemma K, Lemma R1 (crossing; it rests on CL1 and X16). I call "the class" every lattice model for which these hold. `gap-crux-restate.md` 3.4 says Lemma K and Theorem S hold "for every group and for every symmetric model with positive transfer operators", and `gap-means-max.md` 4.8 tests Theorem R on Z_2 gauge theory.

Notation (as in `gap-means-max.md` 4.2). Tori have sides at least 3; frame 1: direction 1 is time. e(B) = log lambda_0(B). S_ev(t; B) = Z_0(t; B)/lambda_0(B)^t - 1, with 0 = (chi; m) = (0; 0). X = Z_2^4 is the set of sixteen sectors with chi_2 = m_2 = 0; x = (x_1, x_2, x_3, x_4) stands for chi = (0, x_1, x_2), m = (0, x_3, x_4).

New shorthand for this file. Fix a >= 3 and c, d >= 3. Put

- A := (a, c, d) (the box), A' := (2a, c, d) (one side doubled);
- eps_{cd} := S_ev(a; A), S'_{cd} := S_ev(a; A');
- Delta(c, d) := a (2 e(a, c, d) - e(2a, c, d)) >= 0 (Lemma K (b));
- for z in X: S_z := T_{A, m_z} P_{chi_z} >= 0, mu_z its top eigenvalue, p_z := Z_z(a; A)/Z_0(a; A), and s_z := Z_z(a; A)/mu_z^a - 1 >= 0, the thermal sum of the sector z (s_z := 0 if S_z = 0);
- Q := sum over z in X of p_z (1 - p_z); for a set L of four sectors, H_L := sum over z not in L of p_z (the weight of the other twelve, "heavy" sectors).

By Lemma R1 (b) on the torus (a, a, c, d) and Lemma R2 (a): 0 <= p_z <= 1 and sum over X of p_z = 4.

The three deficits of Theorem R, Step 0 are Delta_1 = Delta(a, a), Delta_2 = Delta(2a, a), Delta_3 = Delta(2a, 2a) (e does not depend on the order of the sides, (S3)), and

delta = 4 Delta(a, a) + 2 Delta(2a, a) + Delta(2a, 2a), eps = eps_{aa}.

## 2. The deficit is the flux variance (Theorem V)

**Lemma 2.1 (exact identity; PROVED).** For c, d >= 3:

exp(-Delta(c, d)) (1 + S'_{cd}) = (1/4) sum over z in X of Z_z(2a; A) / lambda_0(A)^(2a).

Proof. Lemma R1 (a) with b = 2a: Z_0(a; A') = (1/4) sum_z Z_z(2a; A). The left side is lambda_0(A')^a (1 + S'_{cd}) by the definition of S_ev. Divide by lambda_0(A)^(2a); a e(A') - 2a e(A) = -Delta(c, d). QED

**Theorem V (PROVED).** Let c, d >= 3.

(a) Delta(c, d) >= -log(1 - Q/4) - 2 log(1 + eps_{cd}) + log(1 + S'_{cd}).

(b) For every set L of four sectors of X, with eta_L := H_L/2 + (1/2) sum over z in L of s_z < 1:

Delta(c, d) <= -log(1 - eta_L) + log(1 + S'_{cd}) - 2 log(1 + eps_{cd}).

(c) For every set L of four sectors: 2 H_L (1 - H_L) <= Q <= 2 H_L.

Proof. (a) Lemma A (a) for S_z: Z_z(2a; A) <= Z_z(a; A)^2 = p_z^2 lambda_0(A)^(2a) (1 + eps_{cd})^2. Sum over z; sum p_z^2 = sum p_z - Q = 4 - Q. Lemma 2.1 gives exp(-Delta)(1 + S') <= (1 + eps)^2 (1 - Q/4). Take -log. (This is the chain of Proposition R3, with the factor 1 + S' kept.)

(b) If S_z != 0: Z_z(2a; A) = Tr S_z^(2a) >= mu_z^(2a) = Z_z(a; A)^2 (1 + s_z)^(-2) >= Z_z(a; A)^2 (1 - 2 s_z), since (1 + s)^(-2) >= 1 - 2s for s >= 0. If S_z = 0 both ends are 0. Keep only z in L (the other terms are >= 0). With p_z <= 1: p_z^2 (1 - 2 s_z) >= p_z^2 - 2 s_z, and p_z^2 >= 2 p_z - 1. So sum over L of p_z^2 (1 - 2 s_z) >= 2 (4 - H_L) - 4 - 2 sum_L s_z = 4 (1 - eta_L). Lemma 2.1 gives exp(-Delta)(1 + S') >= (1 + eps)^2 (1 - eta_L). Take -log.

(c) sum over L of (1 - p_z) = 4 - (4 - H_L) = H_L. Each p in [0, 1]. Upper: for z in L, p(1 - p) <= 1 - p; for z not in L, p(1 - p) <= p; add. Lower: for z in L, 1 - p_z <= H_L, so p_z >= 1 - H_L and the sum over L of p(1 - p) is at least (1 - H_L) H_L; for z not in L, p_z <= H_L, so the sum over the others is at least H_L (1 - H_L). QED

**Corollary V1 (what delta is; PROVED from Theorem V).** Write h := H_L for the four sectors L of largest weight, and sigma_L := sum over L of s_z. If h <= 1/2 and eta_L <= 1/2, then

h/2 - h^2/2 - 2 eps_{cd} <= Delta(c, d) <= h + sigma_L + S'_{cd}.

Proof. Lower: (a), (c) and -log(1 - y) >= y: Delta >= Q/4 - 2 eps >= h(1 - h)/2 - 2 eps. Upper: (b) and -log(1 - y) <= 2y for y <= 1/2; log(1 + S') <= S'. QED

So, up to the sector thermal sums and the even sums of the doubled box, **the deficit of one doubling is half the weight of the twelve heavy crossed sectors at the time a**. A bound delta <= C (even thermal sums) is therefore equivalent, up to those terms, to a bound

(HEAVY) H_L(a; A_{cd}) <= C' (even thermal sums), at the three shapes (c, d) in {(a, a), (2a, a), (2a, 2a)}.

This is the precise content of (ES-1). Theorem R's Proposition R3 reads the same chain in the other direction (small Delta and eps give small Q); Theorem V says that the converse also holds, so (HEAVY) is not a side condition but the statement itself.

Check against the 2D Ising run of `gap-means-max.md` 4.10 (reading 4: "Delta is about Q/2"; in two dimensions sum p = 2 and the same proof gives Delta about Q/2 in place of Q/4). In Section 7 below a separate run checks the 2D forms of Lemma 2.1 and Theorem V (a), (b) at 21 points.

## 3. The long-box form (Theorem LB)

`gap-means-max.md` 4.9 sketches: kappa(a) is the growth rate of the even thermal sum on long boxes; the missing step is "from the box of length a to long boxes without the factor 4". The factor 4 does not have to be removed: on a long box it becomes an additive log 4 that disappears.

Fix c, d >= 3 and A = (a, c, d). For b >= 3 let B_b := (b, c, d). Lemma K applies to W(a, b) := Z(a, b, c, d) (the full partition function, symmetric in a and b by (S3)); its top eigenvalue for the box B_b is lambda_0(B_b) (the top eigenvector is even). Let ell := inf over b of e(B_b)/b and kappa(b) := e(B_b) - ell b >= 0; kappa is non-increasing (Lemma K (d)).

**Theorem LB (PROVED).**

(i) For every b >= 3: lambda_0(A)^b / 4 <= Z_0(a; B_b).

(ii) For every b >= a: Z_0(a; B_b) <= lambda_0(A)^b (1 + eps_{cd}).

(iii) For every b > a: (b - a) kappa(a) <= log 4 + log(1 + S_ev(a; B_b)), and so

Delta(c, d) <= 2a kappa(a) <= (2a/(b - a)) [log 4 + log(1 + S_ev(a; B_b))].

(iv) kappa(a) = lim over b of (1/b) log(1 + S_ev(a; B_b)), and

delta <= 2a [4 kappa_{a,a}(a) + 2 kappa_{2a,a}(a) + kappa_{2a,2a}(a)],

where kappa_{c,d} is kappa for the fixed sides (c, d).

Proof. (i) Lemma R1 (a): Z_0(a; B_b) = (1/4) sum_z Z_z(b; A) >= (1/4) Z_0(b; A) >= (1/4) lambda_0(A)^b.
(ii) Every eigenvalue of S_z is at most lambda_0(A) ((TM-tw)), so Z_z(b; A) = Tr S_z^b <= lambda_0(A)^(b - a) Z_z(a; A). Sum over z and use sum_z Z_z(a; A) = 4 Z_0(a; A) (Lemma R1 (b) on the torus (a, a, c, d)): Z_0(a; B_b) <= lambda_0(A)^(b - a) Z_0(a; A) = lambda_0(A)^b (1 + eps_{cd}).
(iii) a e(B_b) = log Z_0(a; B_b) - log(1 + S_ev(a; B_b)) >= b e(A) - log 4 - log(1 + S_ev(a; B_b)) by (i). So b e(A) - a e(B_b) <= log 4 + log(1 + S_ev(a; B_b)). The left side is b kappa(a) - a kappa(b) (the terms ell a b cancel), and it is at least (b - a) kappa(a) because kappa(b) <= kappa(a). Last, Delta(c, d) = a (2 kappa(a) - kappa(2a)) <= 2a kappa(a), since kappa(2a) >= 0.
(iv) By (i), (ii): log(1 + S_ev(a; B_b)) = b e(A) - a e(B_b) + r_b = b kappa(a) - a kappa(b) + r_b with -log 4 <= r_b <= log(1 + eps_{cd}). kappa(b) lies in [0, kappa(a)]. Divide by b. The bound on delta is (iii) at the three shapes with Delta <= 2a kappa(a). QED

**What Theorem LB gives.** The delta half of (ES) follows from one statement about the even sector alone: the even thermal sum at the time a, on boxes that are long in one direction (cross-sections a x a, 2a x a, 2a x 2a), grows at most like exp(b x 10^(-7)/(14a)) in the length b. With finite b: delta <= 10^(-7) if for some b, with r := 14a/(b - a), r [log 4 + log(1 + S_ev(a; (b, c, d)))] <= 10^(-7) at the three cross-sections (from (iii); 4 + 2 + 1 = 7 and the factor 2a). For example b = 2 x 10^9 a and S_ev(a; (b, c, d)) <= 1 would do.

**What it does not give.** It is not a bound by a *small* even sum at a comparable shape. On the long box the even sum is not small: in a dilute gas, log(1 + S_ev(a; B_b)) is about b kappa(a), and (iv) is an identity. Theorem LB moves the question from a deficit to a free-energy density of the even sector; it does not answer it. The growth rate kappa(a) is, by (iv) and Corollary V1, the heavy flux weight per unit length, and a short box with a small even sum does not see it (Section 4).

## 4. A counterexample in the class: Z_2 gauge theory at a = 3

### 4.1 The model, and what of the class it uses

G = Z_2 = {1, -1}, the centre of SU(2). Links carry sigma_l in Z_2; sigma_P is the product around a plaquette, equal to (1/2) tr U_P for the centre-valued SU(2) matrices. The weight is the Wilson weight of the lane, exp(-beta (1 - sigma_P)), and on a twisted stack exp(-beta (1 + sigma_P)) (`gap-crux-restate.md` (TM-c)). Put u := exp(-2 beta). A plaquette is *frustrated* if its weight is u.

What is used, and its status:
- (TM), (TM-c), (F1) for Z_2: Z^{e+m}(t, B) = Tr(T_{B,m}^t C^e) with T_{B,m} >= 0, and the sector sums as in 4.1 of `gap-means-max.md`. In temporal gauge T_B = D^(1/2) K D^(1/2) on gauge-invariant functions of the spatial links, with D(sigma) = u^(f(sigma)), f the number of frustrated spatial plaquettes, and K = tensor product over the N_B spatial links of k = [[1, u], [u, 1]] (the temporal plaquettes), up to a positive constant factor (the order of the gauge group of the slice), which cancels in every ratio used below. Standard; the proofs of `gap-transfer.md` for SU(2) use only reflection positivity of the Wilson weight, positivity of the temporal kernel and the centre flips, and all three hold for Z_2. **ARGUED (routine; not re-checked line by line for G = Z_2).**
- Lemma A, Lemma K, Lemmas R1 (a), (b) and R2 (a) for Z_2. Their proofs use (TM-tw), (F1), (S3) and the axis-exchange symmetry of the torus only. **ARGUED (routine), as above.** The lane already treats Z_2 as a model of these lemmas (`gap-means-max.md` 4.8; `gap-crux-restate.md` 3.4, the test list).

### 4.2 Lemma Z2-a (surface form; PROVED)

For a torus T and a twist class k, write F(sigma) for the set of frustrated plaquettes. As Z_2 cochains, F(sigma) = d sigma + khat, with khat the indicator of the stack. The map sigma -> d sigma + khat is onto the set of 2-cocycles in the cohomology class [khat] (every 3-cube has an even number of its plaquettes), and each fibre is a coset of ker d, of size N_fl := |ker d| (the flat configurations; N_fl does not depend on k). So

Z^k(T) = N_fl times the sum over the 2-cocycles F in the class [khat] of u^|F|.

Hence, with E_1 := the span of the classes of the stacks in the planes (1,2), (1,3), (1,4) (the eight electric twists of frame 1), and m a magnetic twist,

Z_{chi,m}(t; B) = (N_fl/8) sum over e in E_1 of (-1)^(chi.e) sum over F in [e + m] of u^|F|, and Z_0(t; B) = (N_fl/8) p_T(u), p_T(u) := sum over F with [F] in E_1 of u^|F|.

Since F = empty is the only cocycle of size 0, and there are at most 2^|P| cocycles: 1 <= p_T(u) <= 1 + 2^|P| u for 0 <= u <= 1.

The class of a cocycle is read on the coordinate 2-tori: for a pair mu < nu, [F]_{mu nu} is the parity of the number of plaquettes of F in any one coordinate (mu, nu)-plane (the set of points with the other two coordinates fixed). This parity does not depend on the plane, because two neighbouring planes bound a slab of 3-cubes, each with an even count. The stack of k_{mu nu} meets each (mu, nu)-plane once and no plane of another type.

### 4.3 Lemma Z2-b (minimal cocycles in a nonzero class; PROVED)

Let T have sides n_1, ..., n_4 >= 3, mu != nu, and N_{mu nu} := the product of the two sides other than n_mu, n_nu (the number of (mu, nu)-planes). Let F be a cocycle.

(a) If [F]_{mu nu} = 1, F contains at least one (mu, nu)-plaquette in each of the N_{mu nu} planes. So |F| >= the sum of N_{mu nu} over the pairs with [F]_{mu nu} = 1.

(b) If [F] = k_{mu nu} (one pair) and |F| = N_{mu nu}, then F is a *flat sheet*: the set of all (mu, nu)-plaquettes with one fixed value of (x_mu, x_nu). There are exactly n_mu n_nu flat sheets of this type, and each is a cocycle of class k_{mu nu}.

Proof. (a) Each plane has an odd, so positive, number. (b) By (a), F has exactly one plaquette in each (mu, nu)-plane and no plaquette of another type. For rho not in {mu, nu}, the 3-cube of directions (mu, nu, rho) at a base point y has exactly two (mu, nu)-faces, in the two planes through y and y + e_rho, at the same (x_mu, x_nu); its other faces are not in F. Evenness forces both or neither face in F. So the position (x_mu, x_nu) of the plaquette of F is the same in neighbouring planes, hence in all. Conversely, for a flat sheet each 3-cube of directions (mu, nu, rho) has zero or two faces in it, and a 3-cube without both directions mu, nu has none; its class is k_{mu nu} by the parity rule. QED

**Lemma Z2-b' (the least frustration of a non-flat spatial configuration; PROVED).** Let B be a box with sides >= 3 and sigma a configuration of its spatial links with d sigma != 0 (on the 3-torus). Then f(sigma) = |d sigma| >= 4.

Proof. In the dual lattice of the 3-torus, a plaquette is an edge and a 3-cube is a vertex; d sigma is a cocycle, so every dual vertex has even degree in it. A nonempty edge set with all degrees even contains a cycle. In this graph there are no loops or double edges (sides >= 3), and a cycle of odd length must wind around the torus (the steps are +-e_i), so a cycle of length 3 is three steps +e_rho around a side n_rho = 3. If |d sigma| <= 3, d sigma is one cycle (two disjoint cycles need at least 6 edges), so it is such a straight loop: three (mu, nu)-plaquettes with the same (x_mu, x_nu) and all x_rho. It meets each (mu, nu)-plane of the 3-torus once, so its class is nonzero, and it is not a coboundary. Contradiction. QED

### 4.4 Lemma Z2-c (thermal sums of the electric sectors of a periodic box; PROVED given 4.1)

Let B have sides >= 3, m = 0, N_B spatial links, and chi in Z_2^3. Let H_chi be the gauge-invariant functions psi with psi o C_nu = (-1)^(chi_nu) psi for nu = 2, 3, 4, d_chi its dimension, mu_0 >= mu_1 >= ... the eigenvalues of T_B on H_chi, and s_chi(t) := sum over i >= 1 of (mu_i/mu_0)^t. Put g(u) := (1 + u)^(N_B) - 1. If g(u) < 1/2, then

s_chi(t) <= d_chi (2 (1 + u)^(N_B) u^4)^t. In particular S_ev(t; B) = s_0(t) <= C_B u^(4t), and every sector thermal sum s_z with z = (chi; 0) is at most C_B u^(4t).

Proof. Flat configurations (f = 0) are the 1-cocycles of the 3-torus; their gauge orbits are the holonomy classes h in H^1 = Z_2^3, and C_nu maps the class h to h + e_nu. A gauge-invariant psi is constant on each orbit, and psi in H_chi then equals c (-1)^(chi.h) on the class h. So the restriction of H_chi to flat configurations is one-dimensional, spanned by Omega_chi := N^(-1/2) (-1)^(chi.h(sigma)) on flat sigma (N their number), 0 elsewhere; Omega_chi is in H_chi.
(i) D = 1 on flat configurations, K has entries in [0, 1], diagonal 1, and row sums (1 + u)^(N_B). So mu_0 >= <Omega_chi, K Omega_chi> >= 1 - g(u) > 1/2.
(ii) If psi in H_chi is orthogonal to Omega_chi, its flat restriction is c (-1)^(chi.h) with c = 0, so psi vanishes on flat configurations. Then <psi, T psi> = <D^(1/2) psi, K D^(1/2) psi> <= ||K|| sum over sigma of u^(f(sigma)) |psi(sigma)|^2 <= (1 + u)^(N_B) u^4 ||psi||^2, by Lemma Z2-b' and ||K|| = (1 + u)^(N_B). By min-max (T_B >= 0 self-adjoint on H_chi), mu_1 <= (1 + u)^(N_B) u^4.
(iii) s_chi(t) <= (d_chi - 1)(mu_1/mu_0)^t. QED

### 4.5 Theorem Z2 (PROVED given 4.1)

Let a = 3 and u = exp(-2 beta) -> 0. All constants below depend only on the fixed tori.

(a) For every box B with sides >= 3 and every t >= 3: S_ev(t; B) <= C_B u^12. In particular eps <= C u^12.

(b) delta = 216 u^9 + O(u^10).

(c) So delta/eps >= c u^(-3) -> infinity. For every gamma > 3/4, delta/eps^gamma -> infinity. And (ES) holds at a = 3 for all large beta.

Proof. (a) Lemma Z2-c with chi = 0, and S_ev non-increasing in t.

(b) Take L := the four electric sectors {x in X: x_3 = x_4 = 0} (m = 0) at each shape.

*Shape (3, 3)*, box A = (3, 3, 3), torus 3^4. Take z = (chi; m) with exactly one magnetic bit: m_3 = k_24 or m_4 = k_23 (eight sectors). In Lemma Z2-a, the term e = 0 is the class m = k_{mu nu}, a single spatial pair with N_{mu nu} = 9: by Lemma Z2-b its cocycles of size 9 are exactly the 9 flat sheets, and the others have size >= 10. A term e != 0 has a class with two components, size >= 18. So Z_z(3; A) = (N_fl/8)(9 u^9 + O(u^10)), and with Z_0(3; A) = (N_fl/8) p_T, 1 <= p_T <= 1 + O(u): p_z = 9 u^9 + O(u^10). The four sectors with m_3 = m_4 = 1 have classes with two spatial components: p_z = O(u^18). So H_L = 72 u^9 + O(u^10).
Lower bound: Theorem V (a) and (c), log(1 + S') >= 0, 2 log(1 + eps) <= 2 eps = O(u^12), -log(1 - y) >= y: Delta(3, 3) >= H_L (1 - H_L)/2 - O(u^12) = 36 u^9 + O(u^10).
Upper bound: Theorem V (b): eta_L = H_L/2 + (1/2) sum over L of s_z = 36 u^9 + O(u^10), since s_z = O(u^12) for z in L (Lemma Z2-c with t = 3). S'_{33} = S_ev(3; (6, 3, 3)) = O(u^12) by (a). -log(1 - eta) <= eta + eta^2 for eta <= 1/2. So Delta(3, 3) <= 36 u^9 + O(u^10).

*Shape (6, 3)*, box (3, 6, 3), torus (3, 3, 6, 3). The pair k_23 has its (2,3)-planes indexed by (x_1, x_4): N = 9; its flat sheets sit at (x_2, x_3): 3 x 6 = 18 of them. The pair k_24 has N = 3 x 6 = 18. So the four sectors with (m_3, m_4) = (0, 1) have p_z = 18 u^9 + O(u^10), the other eight heavy sectors O(u^18), H_L = 72 u^9 + O(u^10), and as above Delta(6, 3) = 36 u^9 + O(u^10).

*Shape (6, 6)*, box (3, 6, 6), torus (3, 3, 6, 6). Both magnetic pairs have N = 18: H_L = O(u^18), and Theorem V (b) gives 0 <= Delta(6, 6) <= O(u^12).

So delta = 4 Delta(3, 3) + 2 Delta(6, 3) + Delta(6, 6) = (144 + 72) u^9 + O(u^10).

(c) From (a), (b). For gamma > 3/4, eps^gamma <= C u^(12 gamma) = o(u^9). (ES): both numbers tend to 0. QED

**Agreement with Theorem R.** At this point the light group is the electric one (alpha = alpha_per), as `gap-means-max.md` 4.8 says for Z_2 at large beta. The heavy sectors are magnetic vortex lines that wrap one side of length 3 for the whole time 3 (9 plaquettes); the deficit is half their weight. In the frame where one of the two directions of the line is the time, the same 9 plaquettes are a sheet at one time that wraps two space directions: a tunnelling event between holonomy classes. That is why the vacuum energy feels it.

**What is not proved here (ARGUED).** (i) eps = 81 u^12 (1 + o(1)): the 81 configurations in which one spatial link is flipped at all three times (12 frustrated plaquettes) give the first even excitation, so eps is of the order u^12 and not smaller. With it, delta is about (8/3) u^(-3) eps and about C eps^(3/4). Not needed for (c). (ii) For Z_2 at a >= 5 the tube (4a plaquettes) is cheaper than the sheet (a^2), and both delta and eps are of the order u^(4a) times powers of a; Z_2 does not refute a linear (ES-1) at those sizes. At a = 4 the two costs are equal.

**Scope of the counterexample.** It refutes: "for every model of the class and every a >= 3, delta <= C eps", and the same with eps replaced by S_ev at any box and any time >= a, and with any power eps^gamma, gamma > 3/4. It does not refute a statement restricted to large a, nor any statement for Wilson SU(2) itself. The mechanism is general: in a phase with light electric flux, the heavy crossed sectors are flux objects of cost sigma* a^2 (sigma* the dual tension), and the lightest even excitation costs m a or 2 sigma* a^2; the linear form fails as long as sigma* a^2 < min(m a, 2 sigma* a^2), that is a < m/sigma*. The class lemmas carry no information on m/sigma*. A model of the class with m/sigma* large at a large a would give the same counterexample there; I did not construct one (OPEN).

## 5. The extra input that suffices: fusion (Proposition FUSE-suff)

The Z_2 point shows what the class is missing. There the heavy weight (u^9) is far above the even sum (u^12), but its *square* (u^18) is below it: two vortex lines in the same box make an even state of weight about the product. 4.9 of `gap-means-max.md` names this: "two equal fluxes should fuse to an even state of twice the energy, and that uses locality". Here is the input, stated so that Theorem V turns it into a bound on delta.

**(FUSE_K) at the shape (c, d).** There is a set L of four sectors of X such that, with S := eps_{cd} = S_ev(a; (a, c, d)):

- (F-h) p_z <= K S^(1/2) for every z not in L (a heavy flux weighs at most K times the square root of the even sum);
- (F-l) s_z <= K S for every z in L (the four light sectors are no more excited than the even one).

**Proposition FUSE-suff (PROVED).** If (FUSE_K) holds at the three shapes (c, d) in {(a, a), (2a, a), (2a, 2a)}, and at each 6 K S^(1/2) + 2 K S <= 1/2, then

Delta(c, d) <= 12 K eps_{cd}^(1/2) + 4 K eps_{cd} + S'_{cd} at each shape, and

delta <= 7 max over the three shapes of (12 K eps_{cd}^(1/2) + 4 K eps_{cd} + S'_{cd}).

So (ES) at a follows from one kind of number, even thermal sums at the time a on the six boxes (a, a, a), (a, 2a, a), (a, 2a, 2a), (2a, a, a), (2a, 2a, a), (2a, 2a, 2a): it suffices that each is at most 10^(-16)/(144 K^2) (then 7 (12 K x 10^(-8)/(12 K) + ...) < 10^(-7) with room; the constant is not optimized).

Proof. eta_L = H_L/2 + (1/2) sum over L of s_z <= (12/2) K S^(1/2) + (4/2) K S <= 1/2. Theorem V (b), -log(1 - y) <= 2y for y <= 1/2, log(1 + S') <= S', and -2 log(1 + eps) <= 0. Then delta = 4 Delta(a, a) + 2 Delta(2a, a) + Delta(2a, 2a). QED

**Where (FUSE) holds (marks).**
- Z_2 at a = 3, large beta: (F-l) is PROVED by Lemma Z2-c (s_z = O(u^12) for the electric sectors). (F-h) needs a lower bound eps >= c u^12, which is ARGUED in 4.5 (i); with it, K can be any number above 0 for small u.
- 2D Ising (GUIDE, Section 7): the largest heavy p^2/eps is 4.1 to 85 at the 21 points, largest at the critical coupling; Delta/eps^(1/2) stays between 3.9 and 8.3 while Delta/eps grows to 2.6 x 10^3.
- Wilson SU(2) in a confining phase (RECALLED physics, GUIDE): the heavy crossed sectors are electric, of weight about exp(-sigma a^2); two flux tubes along the same axis make a centre-even state of weight about exp(-2 sigma a^2), which is part of eps. So (F-h) is expected with K a power of a. Not proved.

**Why the class does not give (FUSE).** Every inequality in the class (Lemma A, the crossing, reflection positivity in the form of Cauchy-Schwarz) bounds a sum over sectors or a mixed product from *above* by pure ones. (F-h) is a *lower* bound on the even sum by the square of a heavy weight. A proof needs (1) an operator that creates the flux object of the sector z in a region of the box (a Polyakov line for an electric bit, a 't Hooft operator for a magnetic bit), and (2) a cluster estimate in the twisted sectors: two such objects at a distance of about a/2 cost at most the sum of their energies plus a controlled error. Item (2) is a locality statement at the scale of the box; at the size a of (ES), about 16 correlation lengths, this is itself a mass-gap-type estimate in the twisted sector. OPEN.

## 6. The exact point where the attempt fails

**Statement.** Theorem V reduces (ES-1) exactly to the bound (HEAVY): the total weight H_L of the twelve heavy crossed sectors on the box (a, c, d) at the time a, at the three shapes, by even thermal sums (with the light sector sums and S' as harmless additions). The class lemmas contain no inequality that bounds a heavy-sector weight from above by an even thermal sum, and none can exist: in Z_2 at a = 3, H_L is about 72 u^9 while every even thermal sum at the time 3 is O(u^12) (Theorem Z2). The step that would close a weaker form is the fusion inequality (F-h), p_z <= K S_ev^(1/2) for heavy z; it is a lower bound on an even sum by a product, and needs locality (Section 5).

Equivalently, on long boxes (Theorem LB): the growth rate kappa(a) of the even sum along a long box is exact and even-only, but no inequality of the class compares the rate on a box of length b >> a with the even sum on a box of length a; the comparison in both directions passes through the heavy weights.

**What was tried and why it does not close.**
1. A bootstrap through Proposition R3: Q <= 4 theta with theta about Delta + 2 eps, and Theorem V: Delta about Q/4. The two chains are inverse to each other up to second order; there is no contraction (Q -> Q). In 2D the same holds with Q/2 (the run of 4.10: "Q <= 2 theta is close to an equality").
2. The light sectors at the time 2a: Delta = -log((1/4) sum_z rho_z(2a)) + (even sums), rho_z(2a) := Z_z(2a; A)/Z_0(2a; A). From Lemma 2.1 directly, PROVED: |Delta(c, d) + log((1/4) sum_z rho_z(2a))| <= max(eps_{cd}, S'_{cd}), using (1 + eps(2a)) <= 1 + eps. The light weights at the time 2a are about 1 - 2 (1 - p_z), and by sum p = 4 the light defect at the time a equals the heavy weight. Circular.
3. Reflection positivity across planes perpendicular to a doubled side, to place two twisted half-boxes side by side: two equal twists cancel in Z_2, so Z^{k + k} on the doubled torus is the untwisted Z exactly, and RP gives only Z^k(2b)^2 <= Z^0(2b)^2, the wrong direction.
4. Monotony of the even sum in the box (S_ev(a; B') <= C S_ev(a; B) for B' a doubled box). Not available in the class without the flux sums (the doubling of Step 5 of Theorem R holds for the sums W_w over Sigma_w, not for the even sector alone, which in the crossed frame is the sum over all sixteen sectors with weight 1/4). Not needed for FUSE-suff, which uses the even sums of the six boxes directly.

## 7. A guide run in two dimensions (a run can refute or guide; it proves nothing)

**What was run.** The 2D Ising model, isotropic coupling K, exact transfer matrices on rings of a and 2a sites, a = 3, 4, 5, K = 0.2, 0.3, 0.38, K_c = 0.4407, 0.5, 0.6, 0.8 (21 points). Four sectors z = (chi, m): parity under the global flip, periodic or antiperiodic closing. Pure Python (no numpy on this machine), `python3 -I`, rings of at most 10 sites, memory under 20 MB. Scripts and outputs in the output folder: `ising2d_es1.py`, `ising2d_es1.out` (a = 3, 4), `ising2d_es1_a5.out` (a = 5). Not in git. This run is separate from the run of `gap-means-max.md` 4.10 (that script is on the Mini and was not used).

**Criteria, written in the script header before the run.** C1: the 2D form of Lemma 2.1, exp(-Delta) = (1/2) sum_z Z_z(2a; a)/lambda_0(a)^(2a)/(1 + S'), to relative error 10^(-8). C2, C3: the 2D forms of Theorem V (a) and (b) (sum p = 2, |L| = 2: Delta >= -log(1 - Q/2) - 2 log(1 + eps) + log(1 + S'); Delta <= -log(1 - H_L - sum_L s_z) + log(1 + S') - 2 log(1 + eps)). C4: the 2D form of Theorem LB (iii) with b = 2a. FAIL at any point would mean the algebra of Sections 2 and 3 is wrong in its 2D form.

**Result: PASS at all 21 points.** C1 holds to 7 x 10^(-15). Selected rows (light = the two sectors of largest weight):

| K | a | eps | Delta | Theorem V lower | Theorem V upper | Delta/eps | Delta/eps^(1/2) | max heavy p^2/eps |
|---|---|---|---|---|---|---|---|---|
| 0.2 | 5 | 2.24 x 10^(-6) | 5.80 x 10^(-3) | 5.79 x 10^(-3) | 5.82 x 10^(-3) | 2.6 x 10^3 | 3.87 | 4.10 |
| 0.3 | 5 | 1.98 x 10^(-4) | 7.08 x 10^(-2) | 7.00 x 10^(-2) | 7.45 x 10^(-2) | 3.6 x 10^2 | 5.03 | 9.32 |
| K_c | 5 | 2.41 x 10^(-3) | 0.406 | 0.395 | 0.868 | 1.7 x 10^2 | 8.27 | 84.8 |
| 0.6 | 5 | 2.83 x 10^(-4) | 8.82 x 10^(-2) | 8.71 x 10^(-2) | 9.41 x 10^(-2) | 3.1 x 10^2 | 5.24 | 10.6 |
| 0.8 | 5 | 2.91 x 10^(-6) | 6.67 x 10^(-3) | 6.66 x 10^(-3) | 6.70 x 10^(-3) | 2.3 x 10^3 | 3.91 | 4.21 |
| 0.2 | 3 | 1.78 x 10^(-4) | 5.63 x 10^(-2) | 5.56 x 10^(-2) | 5.85 x 10^(-2) | 3.2 x 10^2 | 4.22 | 5.36 |

**Readings (guides).**
1. Away from K_c the two sides of Theorem V agree with Delta to about 1 percent: Theorem V is nearly sharp, and Delta is the flux variance.
2. Delta/eps grows with a at fixed K (320, 870, 2590 at K = 0.2 for a = 3, 4, 5): the linear form fails in 2D at every size, not only at small a, because the heavy sector (the odd particle in the disordered phase) is a single particle, of weight about exp(-m a), while eps is about exp(-2 m a). This is the 2D form of the Z_2 mechanism.
3. Delta/eps^(1/2) stays between 3.9 and 8.3 at all 21 points, and the fusion ratio max p^2/eps between 4.1 and 85: the square-root form and (FUSE) are not refuted in 2D; their constants are largest at K_c.

## 8. Status of the statements

| Statement | Mark |
|---|---|
| Lemma 2.1: exp(-Delta)(1 + S') = (1/4) sum_z Z_z(2a; A)/lambda_0(A)^(2a) | PROVED (from R1 (a)) |
| Theorem V (a), (b), (c) and Corollary V1: Delta is the flux variance Q/4, up to sector thermal sums and S'; Delta is between about H_L/2 - 2 eps and H_L + sigma_L + S' | PROVED (from R1, R2 (a), Lemma A) |
| (ES-1) is equivalent, up to those terms, to (HEAVY): the heavy crossed weight is bounded by even sums | PROVED (Corollary V1) |
| Theorem LB: Delta <= (2a/(b - a))[log 4 + log(1 + S_ev(a; (b, c, d)))]; kappa(a) = lim (1/b) log(1 + S_ev(a; (b, c, d))); delta <= 2a(4 kappa_{aa} + 2 kappa_{2a,a} + kappa_{2a,2a}) | PROVED (from R1, (TM-tw), Lemma K) |
| Lemmas Z2-a, Z2-b, Z2-b', Z2-c (surface form, minimal cocycles, least frustration, electric-sector thermal sums) | PROVED (given 4.1) |
| Z_2 gauge theory satisfies the class inputs (TM), (TM-c), (F1), Lemma A, K, R1, R2 | ARGUED (routine; not re-checked for G = Z_2) |
| Theorem Z2: at a = 3, delta = 216 u^9 + O(u^10), every even thermal sum at time >= 3 is O(u^12); so delta <= C eps fails, and delta <= C eps^gamma fails for every gamma > 3/4, in the class; (ES) holds there | PROVED given 4.1 |
| eps = 81 u^12 (1 + o(1)) at that point; delta about C eps^(3/4) | ARGUED |
| Z_2 does not refute a linear (ES-1) at a >= 5 | ARGUED |
| A model of the class refuting linear (ES-1) at large a | OPEN (not constructed) |
| Proposition FUSE-suff: (FUSE_K) at three shapes gives delta <= 7 max(12 K eps^(1/2) + 4 K eps + S') | PROVED |
| (FUSE) in the class; (FUSE) for Wilson SU(2) | OPEN |
| (ES-1), linear or square-root, for Wilson SU(2) | OPEN |
| 2D Ising forms of Lemma 2.1, Theorem V, Theorem LB (iii) at 21 points; square-root form and (FUSE) not refuted in 2D | GUIDE |
| SU(2): heavy electric sectors fuse (two flux tubes make an even state), so (F-h) is expected with K a power of a | GUIDE (recalled physics) |

**The single most important open point.** The fusion inequality (F-h): for Wilson SU(2) on the box (a, c, d) at the time a, every heavy crossed sector has p_z <= K S_ev(a; (a, c, d))^(1/2), with K at most a power of a. With Proposition FUSE-suff it makes (ES) one kind of number (even thermal sums on six boxes). It is a lower bound on an even sum by a product of two flux weights, and it needs a locality (cluster) estimate in the twisted sectors that no lemma of the class supplies.

RESULT: (ES-1) in its linear form (delta <= C eps, or <= C S_ev at any shape and any time >= a) is FALSE in the class of the lane's lemmas: Z_2 gauge theory at a = 3 and large beta has delta = 216 u^9 + O(u^10) and every even thermal sum O(u^12) (proved given the routine membership of Z_2 in the class); what is proved in general is that delta is the heavy crossed flux weight up to even sums (Theorem V) and an exact long-box form (Theorem LB); a fusion input (F-h), open and needing locality, would give the weaker form delta <= C(K)(eps^(1/2) + even sums of doubled boxes).
