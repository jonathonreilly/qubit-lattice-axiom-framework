lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T13:01Z

# Check of row 1192 (`library/gap-solve20-astra62.md`), queue row 1203

Started 2026-11-20T01:01Z (date -u) on the Mac mini, checkout pinned at f59595fbf. Checker: Claude Opus 5.5, max
reasoning (cross-provider check of an OpenAI-lane row). No numeric run is used as proof; any run guides only.

## Plan (at most eight steps; one step per response, result appended after each)

1. Read the FINISH rules that bind this item, GOAL.md, and the structure of the checked file; list every numbered
   statement of the checked file with its line, in the order the row asks (positive claims first).
2. Positive finite-link approximation of the Wilson heat trace: statement, proof, every constant, line by line.
3. Rare-event criterion (37) with its length and resolution bounds.
4. Obstruction (45)-(50).
5. Remaining statements, first half (with the cited earlier rows read where a step depends on them).
6. Remaining statements, second half.
7. Optional numeric guide (only at >= 50 percent memory free and under the numeric lock), or by hand.
8. Verdict table (HOLDS / HOLDS AFTER CORRECTION / FAILS, with lines) and the RESULT line.

## Status log

- 01:01Z: file created; step 1 starting.

## Step 1. Scope, rules and inventory (done 01:02Z, date -u)

Provenance: Claude Opus 5.5, max reasoning, Mac mini worker; checkout `f59595fbf`; checked file
`library/gap-solve20-astra62.md` (754 lines, 151,893 bytes; written by gpt-6-astra, row 1192, its source pin
`ec52ef469`). This is a line-by-line check, not an audit. Verdicts: HOLDS, HOLDS AFTER CORRECTION, FAILS.

Binding rules read: FINISH.md "Working efficiently" and "Rules" (L320-350), GOAL.md "No computer-assisted steps"
(a run may refute or guide, never discharge). Queue row 1203 (FINISH.md L1284) fixes the order: (A) positive
finite-link approximation of the Wilson heat trace; (B) rare-event criterion (37) with its length and resolution
bounds; (C) obstruction (45)-(50); (D) the rest.

The checked file labels about 110 paragraphs PROVED, 2 OPEN (L5, L748, L750), the rest GUIDE. Map to the row's order:

| Block | Lines | Content |
|---|---|---|
| A | 13-102 | (1) one-plaquette Poisson-tail bound; (2) relative trace error; Gauss-product rule eta_d, nu_d; positivity of the finite transfer; equality of polynomial-model spectra; (3) exponential finite-link trace error; (4) equivalence with the seed; local channel (5); low levels (6); subspace (7) |
| B | 424-543 | (28)-(34) conditioning the gapped comparison model; (35)-(37) finite-resolution smooth test, the criterion (37); length bounds L466-505; resolution L541-566 |
| C | 659-745 | (44) two stiffnesses; (45)-(48) counting stiff faces, mixed-tile cost, one-link threshold; (49)-(50) the slow reading in Wilson |
| D | 107-423, 544-658 | alphabet lower bound (8); Haar restoration (9)-(10); neutral gap on the centre side (11)-(12); interpolation (13)-(16); Haar endpoint (17); smooth link measures (18)-(19); orbit estimates (20)-(23); adaptive gauge (24); first response (25)-(27); slab, volume, analytic continuation (38)-(43) |

Plan adjustment: block A is checked in Step 2, B in Step 3, C in Step 4, D in Steps 5-6.

## Step 2. Block A: positive finite-link approximation of the Wilson heat trace (L13-102)

Read in full: checked file L1-106; row 1161 `gap-solve9-astra62.md` L140-152 and L379-400 (consumer, necessity,
(26), equivalence); its check row 1162 `gap-solve9-check-opus.md` verdicts S11 (L150) and S18-S19 (L247-267), both
HOLDS. GL8 (SA outline 2313-2335) is used only as the positivity of the Haar-averaged electric kernel, which L58 also
proves directly; I did not re-read GL8.

**A1. (1), L17-25. HOLDS.** With b = beta(1+x) in [0, 2 beta], w_m/w = e^{-b} sum_{k<=m} b^k/k! = P(Poisson(b) <= m),
so w_m <= w. Chernoff with t = h/b >= 1 gives P(N >= h) <= e^{-b}(eb/h)^h; h >= 4 e beta gives eb/h <= 1/2, so the
tail is <= 2^{-h} = delta. Holds for every g in SU(2), so also at -g. 1 + x = chi_0 + chi_{1/2}/2 and Clebsch-Gordan
give nonnegative character coefficients of every power; values are >= 0 since 1 + x >= 0; x(U_1 U_2 U_3^{-1} U_4^{-1})
is real linear in each link's quaternion coordinates (inversion = conjugation is linear on S^3). Remark (no defect):
the twisted weight w_m(-g) has signed character coefficients; nothing uses positive definiteness of a twisted weight,
since a seam enters the transfer as a centre-flip operator (L58 last sentence).

**A2. (2), L27-37. HOLDS.** Bv = 6n^3 v plaquettes, positive integrands, so (1 - delta)^{Bv} Z_g <= Z_{m,g} <= Z_g.
(Tr T^v)^{1/v} -> top eigenvalue for a positive trace-class T (the normalized sum is between 1 and its value at a
fixed earlier power). T_m is finite rank (spins <= m/2). w_m >= e^{-beta} > 0 and w > 0, so both kernels are strictly
positive; the |f| argument gives a one-signed top vector, two orthogonal nonnegative top vectors would have
<psi_1, F psi_2> = 0 against a strictly positive kernel, so the top eigenvalue is simple, and a positive vector
fixed up to sign by each flip has flip eigenvalue +1: neutral. Then D_{0,m}/D_0 = [sum_g Z_{m,g}/sum_g Z_g](lambda/lambda_m)^v,
each factor in [(1-delta)^{Bv}, 1] resp. [1, (1-delta)^{-Bv}]. The single-seam version is the same computation.

**A3. Degree choice, L39. HOLDS.** delta <= (2n)^{-(p+5)} and -log(1-delta) <= 2 delta (delta <= 1/2) give
Bv[-log(1-delta)] <= 12 c n^4 (2n)^{-p-5} = O_c(n^{-p-1}) for v <= cn.

**A4. eta_d, L44-50. HOLDS.** Hopf coordinates: s = cos^2 alpha is uniform and independent of the two angles. A q-point
uniform circle rule is exact for frequencies |k| < q, and |k| <= d < q. Surviving monomials are s^a(1-s)^b with
a + b <= floor(d/2) <= 2r - 1. Gauss nodes: r sign changes, distinct, interior; weights int l_i^2 > 0; exactness to
degree 2r - 1 by division by p_r. Atom count q^2 r <= (d+6)^2 (d+3)/2 <= C(d+1)^3. q even makes eta_d antipodally
invariant (theta_i -> theta_i + pi permutes the roots), which L52 uses.

**A5. nu_d, L52. HOLDS.** Exactness: for fixed B, U -> P(U B^{-1}) has the same degree, and Haar is right invariant.
Inversion swaps (A, B). E R(AB^{-1}) = M M^* with M = E R(A). Antipodal invariance from A4.

**A6. Positive finite transfer, L54-58. HOLDS.** Electric plaquette at link e: tr(x_e V_{s+i} y_e^{-1} V_s^{-1}) =
tr(x_e (gy)_e^{-1}) with g_s = V_s, so the temporal integrand is k(x, gy). k is a product of positive definite kernels
w(x_e y_e^{-1}) (nonnegative character coefficients), gauge invariant because w is a class function. With g = ab^{-1}
per site (a, b iid eta_d, or Haar), k(x, ab^{-1}y) = k(a^{-1}x, b^{-1}y), and E_{a,b} of a Gram kernel is the Gram
kernel of the averaged vectors, defined on the whole continuous slice, then restricted to the finite support.
Sandwiching by A^{1/2} keeps PSD; strictly positive entries and the finite Perron-Frobenius argument give a simple
neutral top eigenvalue (the flips permute the antipodally invariant support). Trace identity and seam = flip insertion
are standard.

**A7. Equal polynomial spectra, L60. HOLDS.** Each link lies in 6 plaquettes, degree <= m each, so <= 6m = d per
link (twists keep the degree); link-by-link Fubini with nu_d exact to degree d gives equality of every seam integral.
Sector traces Tr(T^v P_chi), v >= 3, agree; both transfers are PSD; the measures sum_i lambda_i^3 delta_{lambda_i}
on a common bounded interval have equal moments, so equal atoms: nonzero spectra agree with multiplicities.

**A8. (3), L62-66. HOLDS.** hat Z_{m,g} = Z_{m,g} (A7), and each exponential model is within (1-delta)^{+-Bv} of the
common polynomial model in seam integrals and (1-delta)^{+-B} in top eigenvalue; the two ratios give 2 b_n(v). The
unnormalized bound b_n(v) and the per-step vacuum bound b_n(1) follow by the same trapping.

**A9. (4), L68-72. HOLDS (conditional exactly as labelled).** (4) => seed: |log hat D_0(u) - log D_0(u)| <= 2b_n(u) -> 0
since u <= n/512 (and u >= 3 once n >= 1536). Seed => (4): row 1161 L148 turns the seed into the Pfaffian seed, and
L150/L400 (Theorem S-w plus Proposition B3 enlargement and monotonicity in time) make the neutral excited sum at
floor(n/K), K = 512, arbitrarily small on larger dyadic sides with the cutoff limit first; this is checked HOLDS in
row 1162 (S11, S19). Then (3) gives a strict margin. The citation "after (26)" points at L400, which states the
propagation at time n/2; the step to time floor(n/512) is the B3 enlargement of L150. Precision note only.

**A10. Smaller alphabet, L77. HOLDS.** A temporal link lies in 6 electric plaquettes of one time step, so its degree is
<= 6m and the eta_d average equals the Haar average at fixed spatial ends; the kernel is the restriction of the Haar
polynomial transfer kernel (PSD), and full periodic integrals agree link by link, so positive spectra agree. (4) then
holds with D_{0,m} on eta_d, since |log D_{0,m} - log D_0| <= b_n(u).

**A11. Local resampling channel, L79. HOLDS.** For a set of links no two on a common plaquette, the exterior marginal
is a product of one-link integrals of polynomials of degree <= 6m, equal for Haar and eta_d; so exterior marginal times
new conditional is exactly the switched Gibbs law. w_m >= e^{-beta} keeps every conditional normalizer positive.
6 x 3 = 18 neighbours, greedy colouring with 19 colours.

**A12. (5), L81-85. HOLDS.** J_m <= J_H, J_Q <= (1-delta)^{-6} J_m (six incident weights); exterior Radon-Nikodym
derivative J_Q/J_H over its old mean lies in [(1-delta)^{12}, (1-delta)^{-12}]; resampled law and exact law share the
new conditional, so the same bound holds for the joint law; Markov kernels preserve two-sided bounds between positive
measures, so the factors multiply over |S| links.

**A13. (6), L90-96. HOLDS.** 3n^3 electric factors plus 2 x 3n^3 half spatial factors = 6n^3, so c_n F <= F_m <= F as
kernels. |(F - F_m)f| <= (1-c_n)F|f| gives ||F - F_m|| <= (1-c_n) lambda; c_n lambda <= lambda_m <= lambda by testing
the nonnegative top vectors; ||F/lambda - F_m/lambda_m|| <= (1-c_n) + (1 - lambda_m/lambda) <= 2(1-c_n). Weyl per centre
character, zero padding, A7 for the polynomial lists, so 4(1-c_n) between the two exponential models. Energies:
|log r - log r'| <= 2|r - r'| on [1/2, 1], so errors <= 8(1-c_n)/a = O(n^4 delta/L) -> 0.

**A14. (7), L98-102. HOLDS.** F_m(., y) = A_m(x) x (polynomial of degree <= m in each x_e: each spatial link meets one
electric plaquette per step), and the gauge average keeps the degree. |A_m f|^2 has degree <= 4m + 2m (a spatial link
lies in 4 spatial plaquettes in 3D), so eta_d evaluation is isometric on A_m V (finite dimensional). For phi in the
spectral subspace of U = F/lambda on [r,1], phi = U psi, ||psi|| <= ||phi||/r, and (1-Pi)phi = (1-Pi)(F - F_m)psi/lambda.

**Step 2 verdict.** Block A: 14 statements, all HOLD; no correction needed. What block A proves is a relative
(multiplicative) approximation of every seam integral, of the neutral trace at time <= cn, and of every normalized
level, by a strictly positive finite-alphabet model with degree O(log n); it moves no physical input: (4) is exactly
as hard as the seed.

## Step 3. Block B: rare-event criterion (37), its length and resolution bounds (L424-541), with dependencies

Read in full: checked file L107-566. Dependencies of (37) checked here first (they are also block D items):

**B0a. (9), L152-163. HOLDS.** z_beta <= C(1+beta)^{-3/2} from density (2/pi) sin^2 theta and 1 - cos theta >= 2 theta^2/pi^2
(sin y >= 2y/pi). Column argument: a direction mu with <= |A|/4 links of A is held fixed; in each nu-column (a cycle
of length >= ell along mu) each non-root A-link is assigned the mu-nu face to its predecessor; assigned faces are
distinct; discarded weights are <= 1 (normalized action); integrating from the far end, each link meets only its own
retained face, giving exactly z_beta (Haar absorbs translation, inversion, sign). At most one link per all-A column is
lost, so the exponent is >= (3/4)(1 - 1/ell)|A|, and z_beta <= 1. All exterior links fixed throughout.

**B0b. (10), L165-170. HOLDS.** Upper: average (9) over labels and signs. Lower: all +I gives (s/2)^E; all Haar with
a spanning tree gauged to I and the 3V+1 chords in the (1+beta)^{-1/2} cap gives (3/2)(3V+1) log(1+beta) + CE with
bounded face action (angle <= 4(1+beta)^{-1/2}). Label concentration: the k-term bound
binom(E,k) s^{E-k} z^{(3/4)(1-1/ell)k} against the matching lower bound gives a cost c E log beta away from the minimizing
endpoint; binom <= 2^E is o(E log beta).

**B0c. (12), L182-191. HOLDS.** D = supp(d sigma + t_g) is closed in the seam class; |Z^1(T^4; F_2)| = 2^{V-1} 2^4;
H^2 = F_2^6 detected by the six coordinate 2-tori; a temporal seam for g pairs only with the tori T_{0i}, so the
average over the 8 seams keeps exactly the D with zero pairing on the three spatial tori T_{ij}. Prefactor:
s^E 2^{-E} 2^{V+3} (1/8) = s^{4V} 2^{-3V}. Faces off St(A) have weight 1 or e^{-2 beta}. Transfer positivity for mu_s:
mu_s = nu * nu^{-1} with nu = (1 - sqrt s) sigma + sqrt s (delta_I + delta_{-I})/2 (checked: (1-sqrt s)^2 + 2(1-sqrt s) sqrt s = 1 - s).

**B0d. Local expansion and (11), L175-180, L193-209. HOLDS.** Faces of one 3-cube have base vertices at sup distance
<= 1, so cube equations hold per component; a face of St(A_1) cannot meet D_2 or St(A_2) at separation > 2; so the
gas factorizes, positive and hard-core. j <= 7k + r (6 faces per Haar link). Activity <= (kappa z^{(3/4)(1-1/ell_0)})^k e^{-2 beta r}
with kappa <= beta^alpha, base <= C beta^{alpha - (9/8)(1-1/ell_0)}, so <= beta^{-c(7k+r)} <= e^{-c j log beta} for beta >= beta_0.
J = 10 x 5^4, J^{2(j-1)} connected sets, KP sum <= |gamma|, rooted-tree recursion T^{(k)} <= e^{|gamma|} correct. Short
clusters (j < v/16) lift uniquely; a component with nonzero spatial pairing has the same pairing on every time slice,
so >= v faces; P(polymer) <= activity. Then D_{0,s}(v) = Xi^restr_v / e^{v p_n} <= Xi_v / e^{v p_n} <= exp(C n^3 v e^{-mu v/16})
for all n, v >= ell_0, and D >= 1 since the top eigenvalue is neutral. Energy bound by v-th roots. (KP itself is
cited to the Sussman-Alpoge outline 1223-1356; I did not re-read it; the two-line recursion given is correct.)

**B0e. (17), L283-294. HOLDS.** Z_s/Z_0 = E_T[Z(T)/Z_0]; forest pins have ratio exactly 1 (transitive site rotations);
each further pin multiplies by a conditional one-link density <= C(1+6 beta)^{3/2} <= K, also after mixing over unfixed
links and for any pin law; lower bound via FKG on <= V 8^l simple cycles of length l >= 4; upper bound
E K^{b(T)} = sum over Z/K currents of s^{|supp|}, leafless connected supports have b <= l - 3, and
K^{l-3} s^l = K s^4 (Ks)^{l-4}. The neutral seam average only takes a ratio of positive averages.

**B0f. Smooth (11), L317-331. HOLDS** at the precision (37) needs. All-cap positive faces: |r_p| <= beta (4 eps)^2/2;
negative: <= e^{-2 beta + C beta eps^2}; components of A, D, P (joining distance 4) read disjoint cap noises; signed
activities obey the stated absolute bound; at s_hi the base is <= C - sqrt(log beta) + (9/8) log beta/ell <= -c sqrt(log beta)
for ell >= 5 sqrt(log beta). The spatial restriction as 2^{-3} sum_chi chi([D]_spatial): small polymers have chi = 1, each
Xi_chi = exp(convergent series) > 0, so the average keeps two-sided bounds.

**B0g. (26), L401-411. HOLDS.** Upper: conditional face density e^{w y.U}/Z(w), w <= 6 beta. Lower: log Z(beta/2) - log Z(beta)
<= C V + C(1 + V/ell) log(2+beta) <= C'V for ell >= log(2+beta); convexity of log Z (also for the seam-averaged sum,
a single log-Laplace transform) gives E S <= 2C'V/beta; 1 - |x| is seam-invariant and translation invariant, so <= 2C'/beta
per face; Markov puts the centre caps of radius M/sqrt(beta) at probability >= 7/8; on a 3/4 exterior set the caps have
conditional probability >= 1/2, forcing 1 + w >= c_M beta; the two events intersect, so a central element lies within
M/sqrt(beta) + D/sqrt(1+w) of y, where the conditional density is >= c_M (1+w)^{3/2}.

Block B proper:

**B1. (28), L426-430. HOLDS.** For a forest T the pinned seam integral equals Z^g_0 for every seam (root each tree,
solve child frames); summing iid weights over forests gives Z_{neut,s} P_s = Z_{neut,0} B_s. The same transitivity, with a
bounded gauge-invariant insertion, gives the product law of (T, orbit) on F.

**B2. (29), L432-437. HOLDS.** A Haar-labelled link has a conditional density, so a cycle through it is central with
probability 0; finitely many simple cycles; F = {no simple cycle has central holonomy} a.s., gauge- and flip-invariant,
probability one under Haar Wilson. P_s^orb = P_s(F) P_0^orb + (1 - P_s(F)) Q gives <=, the event gives =.

**B3. (30), L439-444. HOLDS.** Forest plus an isolated square with all 28 incident edges unmarked (the text's 32 is a
harmless overcount); injective; weight ratio (s/(1-s))^4; pinned ratio (rho_p(I) + rho_p(-I))/2 = a_p + 1 (three pins
plus the forest form a forest, the fourth pin reads the face density, pins' product is +-I with probability 1/2);
FKG gives (1-s)^{32} given F; (26) gives a_p + 1 >= c beta^{3/2}. So P_s <= 1/(1 + c V beta^{3/2} s^4). Reverse: (17) and
B_s >= e^{-C V s^4}. The V >> beta^{9/2} clause makes Ks -> 0 when V beta^{3/2} s^4 -> 0.

**B4. (31), L446-456. HOLDS.** log Z_{neut,0} = log Z_{neut,s} + log P_s - log B_s; (11) at s = beta^{-alpha}; forest gas
(vertex-disjoint trees, activity (s/(1-s))^j <= (2s)^j, decay alpha log beta) gives log B_s(v) = v b_s(n) + O(n^3 v e^{-c v log beta});
D_{0,0}(w)^{1/w} -> 1 since D_{0,0} is nonincreasing and >= 1, so gamma_s = log lambda_0 - log lambda_s + b_s exists, and both
identities follow. Purity inequalities (L392: (max p_i)^2 <= e^{-J} <= max p_i, vacuum p_0 = 1/D_0) give
log D_0 <= J_0 <= 2 log D_0, hence the sufficiency and the converse via row 1161.

**B5. (32), L458-463. HOLDS.** -log P_s = -log Z_{neut,0} - log B_s + log Z_{neut,s}; neutral (10) at s = 0 and at
s = beta^{-alpha} (upper bound per seam from (9), lower bound Z_neut >= Z_ord/8); 0 <= -log B_s <= 4V s.

**B6. (33), L468-480. HOLDS.** b(S) <= |S|/k for girth > R >= (2k)^4: a uniformly translated partition into boxes of
side in [k, 2k] cuts each edge with probability <= 1/k and leaves an acyclic remainder. FKG gives P(S occupied | F_R) <= s^{|S|}
and P(no long cycle | F_R) >= P(no long cycle). Every component of a current support inside a girth > R graph has
>= R+1 edges. P^R/P = E[Z(T)/Z_0; F_R]/P(F) <= E[K^{b(T)} | F_R]/P(F | F_R). The exact TV identity follows from (29).

**B7. (34), L482-489. HOLDS.** Perimeter 2(floor(R/2) + 1) > R, width < ell. Sign: site reflection through the middle
time slice, conditioning on the two mirror slices (v even); ordinary: sum of |half-integral|^2; neutral: seam on the
far mirror slice gives <h, P_0 h> = ||P_0 h||^2 >= 0 (flips preserve the slice reference); integer spin ignores seams.
Then (1+x)^m + (1-x)^m has nonnegative integer-spin coefficients, trivial coefficient 1 after normalization, so
(rho_C(I) + rho_C(-I))/2 >= 1 by continuity of rho_C. Injective forest-plus-rectangle markings with <= 8q empty edges.

**B8. Sharp length, L491-496. HOLDS.** k = floor(R^{1/4}/2) gives log(C s K^{1/k}) = -(alpha - o(1)) log beta since
log K = O(log beta) and k -> infinity; with log V = alpha H log beta the bound (33) is exp(-(zeta alpha - o(1)) H log beta) -> 0.
Below: (34) gives V[s(1-s)^7]^q >= exp((zeta alpha - o(1)) H log beta - O(log beta)) -> infinity, so the conditional TV -> 1.

**B9. Criterion at physical size, L498-503. HOLDS (conditional exactly as labelled).** (33) at V = n^3 u and 2 n^3 u
with the stated R; H ~ 4 log n/(alpha log beta) = o(u) on the logarithmic trajectory.

**B10. (35), L508-521. HOLDS.** Union bound with sup density C(1+beta)^{3/2}. Pivots on faces at sup distance >= 4
are conditionally independent tilts; 6 - w_i/beta <= sum_{p ni e_i}(1 - eps_p x(U_p)) since U.(RY) <= R; Markov on the
total deficit (26) and on sum Delta(y_i)^2; density >= c(1+beta)^{3/2} e^{-C M^2} within (M+1)/sqrt(beta) of y_i;
M^2 = (2C)^{-1} log Lambda.

**B11. (36)-(37), L523-539. HOLDS.** Cap links are within eps of +-I, so a label cycle of length <= R has
Delta <= R eps <= r/4: readout G subset F_R. On F the orbit law is exactly Haar Wilson, so
P(F \ G) <= P(F) C V_* 8^{R+1} (1+beta)^{3/2} r^3 = P(F) C 8^{R+1} V_*^{-3 eta} = o(P(F)) (8^R = V_*^{O(1/log beta)});
P(G \ F) <= P(F_R) - P(F) = o(P(F)) by (33) (pins at arbitrary cap values keep the bound K). Conditioning on G
instead of F moves every event by <= 2 delta/(1 - delta). log p(u)^2/p(2u) = J_0(u) - J_{s,eps}(u) + O(n^3 u e^{-c u log beta}),
and 0 <= J_{s,eps}(u) <= 2 log D_{0,s,eps}(u) <= C n^3 u e^{-c u log log(2+beta)} by B0f, valid for every eps <= (1+beta)^{-1/2}/b.

**B12. Resolution, L541. HOLDS.** Link errors <= r/(4R) give cycle errors <= r/4 (bi-invariant metric); the read event
lies between the exact events at 5r/4 and 3r/4, both of which obey B11's two bounds (3r/4 > r/4 for the inclusion
in F_R; (5r/4)^3 only changes C). Necessity: any law supported on {min_p Delta(U_p) > r'} has TV >= P_0(min Delta <= r') -> 1
by (35) and monotonicity.

**Step 3 verdict.** Block B: 12 statements and 7 dependencies, all HOLD; no correction needed. The criterion is an
exact reformulation: (37) moves the seed to the order-one ratio p(u)^2/p(2u) of an exponentially rare event (32) in the
gapped comparison model; nothing in block B bounds that ratio.

## Step 4. Block C: the obstruction (44)-(50) (L659-743), with dependencies

Read in full: checked file L567-745. Dependencies checked first (block D items used by C):

**C0a. Spectral inequality after (16), L272-278. HOLDS.** Cov <= <B(0)B(t)>_th; with U^t = Pi + R, R >= 0:
Tr(B Pi B Pi) = <Omega, B Omega>^2 = 0, Tr(B Pi B R) <= ||R|| <= Tr R, Tr(BRBR) = ||R^{1/2} B R^{1/2}||_HS^2 <= (Tr R)^2, and
Tr U^{2t} >= 1; so Cov -> 1/4 forces 2 Tr R + (Tr R)^2 >= 1/4 - o(1), Tr R >= 0.118 > 1/20. lambda >= e^{-12 beta n^3},
D(3) <= e^{36 beta n^3} (weights in [e^{-2 beta}, 1], 6n^3 faces per step), Tr R <= rho^{t-3} D(3).

**C0b. (40) and its slab machinery, L569-592. HOLDS.** Loomis-Whitney by Shearer (sum_i H(X_{!=i}) >= 3 H(X)),
prod p_i >= (|W|/D)^3, partial lines carry two boundary edges each, AM-GM, min_i D/N_i = M^3: |dW| >= c|W|^{3/4}. On each
elementary square the crossings of dH have bad endpoints at sup distance <= 1, hence one component, even count: closed
cochain per component; |c_B| <= 8|B| < M^3 forces zero periods (every parallel line carries the period); primitives sum
to H or H^c. Moment bound: (14) with one factor 8 for any collection, e^x - 1 <= x e^x, theta j^{4/3} <= (j/2) log(1/q) for
j <= M^3/16 and c_0 small. Union over ~ e^{c_1 n^3 log beta} slabs; overlapping slabs agree for large M.

Block C proper:

**C1. (44)-(45), L663-672 with proof L674-694. HOLDS.** w_c has nonnegative character coefficients, so W_y is of positive
type, analytic, strictly increasing. Counting: some direction carries >= k/2 stiff faces (each face counts in two
directions); retained axial faces give exactly z_b or z_B each (seam signs absorbed by Haar); 3V axial faces, <= 3V/ell lost
roots; with ell >= log B and b = (log B)^2: b^{(9/2)V/ell} = e^{o(V)} and (B/b)^{(9/2)V/ell} <= e^{(9/2)V}. Pattern bound
e^{CV} b^{-(9/2)V} (B/b)^{-3k/4} against the pure lower bounds e^{-CV} b^{-(9/2)V} and y^{6V} e^{-CV} B^{-(9/2)V}: at
y = delta (B/b)^{3/4} the ratio for k >= (3/2)V is <= 2^{6V} e^{2CV} delta^{(3/2)V}; at y = D (B/b)^{3/4} the ratio for
6V - k >= (3/2)V is <= 2^{6V} e^{2CV} D^{-(3/2)V}. Labels are conditionally independent given the field with posterior
h_y(U_p); covariance of two labels = covariance of the two readings; h_y depends on x(U_p), which spatial flips preserve
(a spatial face holds 0 or 2 flipped links). Normalized minimum weight e^{-2b}/(1+y_*) and log(1+y_*) <= log B = sqrt b give
D(3) <= e^{C b n^3}; C0a with t ~ e^{c_1 n^3 log B} gives (45); u m_+ -> 0 gives D_0(u) >= 2 - o(1).

**C2. (46), L680-688. HOLDS.** Unequal directional counts on a period-four pattern differ by multiples of V/4^4, so the
maximum exceeds the mean k/2 by >= V/(4 x 4^4). Equal counts: if no stiff face met a broad face across an edge in a
distinct plane, the six faces through every edge would share a label (coplanar pairs via a third plane), and the
edge-adjacency graph of faces is connected, so the pattern would be pure. Period four puts a broad axial face at least
every four steps in the common column, so the chain has <= 4 links. Chain variables (root, plaquette increments) are a
product-Haar change of variables; the short root X enters the selected nonaxial stiff face once (the opposite nu-edge
and the two rho-links lie in other columns) and no other retained face (increments do not contain X; separation > 12);
integrating X gives one extra z_B per selected strip, >= cV strips. Geometric mean of the pure bounds: y^k cancels and
the ratio is <= exp(CV + 9V log log B - (3/2) eta V log B). The face-label chessboard step (labels in a mirror plane are
shared boundary variables with positive weight) is the cited AM6 argument as used for (14); I accept it as cited.
Opposite pure tiles cannot touch (shared faces). y_* location: mean stiff fraction is monotone in log y (derivative =
variance / 6V), equals 1/2 + O(q) at y_*, and is < 1/4 + o(1) resp. > 3/4 - o(1) at the two binomial endpoints.

**C3. (47), L699-704. HOLDS.** log(1 + y_*)/b = O(1/log B). Upper: Haar density of U_p <= C b^{3/2} and
int e^{-p(B-b)(1-x)} d sigma ~ C_p B^{-3/2}. Lower: in the ordinary ensemble E(1 - x(U_p)) <= C/b, so the (26) cap argument
around +I alone gives density >= c b^{3/2} on the B^{-1/2} cap. With y_* ~ L_B^{3/4}: ||h||_p ~ L_B^{3/4 - 3/(2p)}, -> 0 iff p < 2.

**C4. (48), L706-722. HOLDS.** G - 1 = sum_S A_S >= 0. sup A_S <= y_*^{j-1} sup E[h(U_{p_1}) | xi] <= C y_*^j L_B^{-3/2}. The six
opposite parallel edges lie in pairwise disjoint plaquette sets (displacements +-nu differ by graph distance two), so
successive integration gives E A_S <= (C y_* L_B^{-3/2})^j and E A_S^p <= C_p L_B^{(3/4)[(j-2)(p-2) - 2]}; all exponents with
j <= 6 are negative iff p < 5/2, and the maximum for p >= 5/2 is j = 6: 3p - 15/2. Lower: P(all six faces within B^{-1/2} of +I)
>= c L_B^{-9} (six conditionally independent tilts, each good with probability near one by the (35) first-moment bounds in the
ordinary ensemble); given xi this event has probability <= C L_B^{-3/2}, so P(alignment) >= c L_B^{-15/2}; on alignment the
tilt strength is >= 5b, the density is >= c b^{3/2} on the B^{-1/2} cap about S_1 where all six stiff factors are O(1) times
y_*, so A_all >= c y_*^6 L_B^{-3/2} ~ L_B^3. Kernel TV: q_new >= q_old/G gives TV <= 1 - 1/G <= G - 1.

**C5. (49), L727-732. HOLDS.** g >= 1/2 iff (B-b)(1-x) <= log y_*; the ball radius ~ sqrt(log y_*/B) is o(b^{-1/2}) because
log y_* <= log B = sqrt b and b^{3/2} = (log B)^3 << B; inside/outside split with 1 - cos theta >= 2 theta^2/pi^2 gives the upper
bound C_p L_B^{-3/2} ((log y_*)^{3/2} + 1); |Cov| <= E g^2 -> 0.

**C6. (50), L734-739. HOLDS.** W_y >= w_b gives >= 0. Broad-dominant slabs: pure-stiff and mixed volume <= C sum |B'|^{4/3}
(C0b), expected O(q) per slab volume, exceptional events e^{-c n^3 log B} = o(q) since n >= log B; Markov at level C sqrt q leaves
>= 1/3 of the neutral raw integral with stiff fraction <= C sqrt q; a fixed set of j stiff faces weighs <= y_*^j Z_b
(w_B <= w_b, also at signed faces); binomial sum gives H_2(C sqrt q) + C sqrt q log y_* = o(1) per face since
sqrt q log y_* ~ B^{-c_0/2} log B. Ordinary vs neutral within factor 8: Tr(G F^v) <= Tr F^v for F >= 0, G unitary.

**C7. Physical time and relative entropies, L741-743. HOLDS.** log D(w) in [0, C b n^3] for w >= 3 (D nonincreasing in w),
so the per-plaquette pressure gap moves by O(b/u + b/v_*) = o(1) for b = o(n). D(P_b || P_W) = log(Z_W/Z_b) - E_b sum log(1+h)
<= log(Z_W/Z_b). Reverse: convexity in the stiff coupling (log-Laplace in B') between B/2 (bounded since
y_*(B/2b)^{-3/4} = O(1)) and B gives B E sum_stiff (1 - eps x) <= CV; log(1+h) = H_2(g) + g log h (verified); E sum g_p = E j;
so D(P_W || P_b)/(6V) = (1/2) log y_* + O(1). d_x log W_y = b + (B-b) g verified.

**Step 4 verdict.** Block C: 7 statements and 2 dependencies, all HOLD; no correction needed. Scope as the file states:
(45) is an eigenvalue of a deformed isotropic analytic action whose single-face, one-link, pressure and
relative-entropy distances to Wilson at coupling b all vanish (47)-(50), while its detector is rejected by Wilson (49).
It refutes transferring a spectral bound between actions by those closeness measures; it says nothing about Wilson's
own neutral levels.

## Step 5. Block D, first half (L107-315; items not already checked in Steps 3-4)

**D1. (8), L109-133. HOLDS.** e^{b y.x} = e^{b chi_{1/2}(y x^{-1})/2} is a class kernel; r_l = I_{l+1}/I_1 (GL3, standard). Poisson
integral for I_j; d/du[e^{bu}(1-u^2)^{j+1/2}] integrates to 0 and gives I_{j+1}/I_j = mean of u < 1; with
I_j - I_{j+2} = 2(j+1) I_{j+1}/b and I_{j+2} <= I_{j+1}: I_{j+1}/I_j >= (1 + 2(j+1)/b)^{-1}; product over j = 1..l gives
r_l >= e^{-(l^2+3l)/b}. dim V_k = D_k (Peter-Weyl), V_k V_k-bar in V_{2k} (Clebsch-Gordan), constant diagonal kernel D_k gives
||f||_inf <= sqrt(D_k). With f in V_k vanishing on the N < D_k nodes, h = T_b^{-1}|f|^2 in V_{2k}: ||h||_2 <= e^{(4k^2+6k)/b} sqrt(D_k);
int h G dsigma = int T_b h dQ = int |f|^2 dQ = 0 and int h dsigma = int |f|^2 dsigma = 1 (T_b symmetric, mass-preserving).

**D2. Physical exterior, L135-139. HOLDS.** A gauge rotation at the initial endpoint applied to the exterior only preserves
the exterior marginal (Haar invariance of U_e) and right-translates Y, so Y | R is Haar on R > 0. Small-ball bound
Z >= (c(1+beta)^{-3/2})^{4V} e^{-48V}; convexity with Z(0) = 1 gives E S <= -log Z/beta; 6 - R <= sum_{p ni e}(1 - x_p).

**D3. Alphabet lower bound, L141. HOLDS.** On R >= 3, Y is Haar given R, so (8) at b = beta R >= 3 beta applies;
k = floor(c log n) gives exponent (4c^2/(3c_1)) log n + O(1) and D_k^{-1/2} = n^{-o(1)}; so N >= D_k >= (k+1)^3/3. The
matching order for eta_d (one-link normalizer error <= 12 delta) is correct. The outline line reference 19957-19996 for the
logarithmic coupling is a citation I did not re-read; nothing here depends on it.

**D4. Why the limit cannot transfer, L211. HOLDS.** ||mu_s - sigma||_TV = s (c singular to sigma). P(face central) -> 1 from (10)
by translation invariance and four links. f_beta > 0 only on caps of radius ~1/beta (volume O(beta^{-3})), conditional density
<= C(1+beta)^{3/2}, so E_0 f_beta = O(beta^{-3/2}) while E_s f_beta -> 1.

**D5. (13), L218-226. HOLDS.** Unequal directional Haar fractions (multiples of 4^{-4}): the least is <= mean - 4^{-4}/4, so
(9) gains V/(4 x 4^4). Equal: a Haar mu-edge meets a centre nu-edge at a vertex (else the pattern is constant by
connectivity); translating along +mu reaches the next centre nu-edge within h <= 4 steps; with the column order in that
sign the last strip face f_{h-1} is unassigned in (9) (its forward link is centre); after all other column eliminations
(which give z_beta whatever the side links), integrating the Haar mu-edge in f_0 and the h-1 Haar nu-edges in f_1..f_{h-1}
gives z_beta^h, one extra factor per strip; >= gV separated strips; root loss <= 3V/ell.

**D6. (14), L228-239. HOLDS.** Disseminated numerator s^{E-k}(1-s)^k z^{3k/4+eta V}; denominator >= geometric mean of
(s/2)^E and (1-s)^E e^{-CE}(1+beta)^{-(3/2)(3V+1)}; label factors cancel; (1+beta) exponent -(3/2) eta V + (3/2) k/E;
so (C beta^{-c})^V uniformly in s. Chessboard with link labels as shared mirror variables (cited AM6-AM7 argument, not
re-read); 216 links in a closed side-two tile, V/16 tiles, power 16/V. Neutral: Cauchy-Schwarz on K_+(x,y)K_-(y,gx), the
flip preserves the slice reference, then Z_neut >= Z_ord/8.

**D7. (15)-(16), L244-278. HOLDS.** s_* by continuity and endpoint swap; P(H), P(C) = 1/2 + O(q) by (14); tile-independence
via seam moves by flips; Haar fraction 1/2 + O(q); exponential-family monotonicity in log((1-s)/s) and neutral (10) at
beta^{-(9/8 +- eps)} locate s_*. Contours: opposite pure tiles cannot touch; boundary edges of a good component face bad
tiles; curves shorter than M/2 are contractible and some curve separates the two points; >= l/4 bad tiles per contour,
probability <= 8 q^{l/4}; long contours cost C M T (4q^{1/4})^{M/2} -> 0 since c_1 < c_0/100 and -log(4q^{1/4}) >= (c_0/5) log beta.
f_beta is flip-invariant and L^1-close to the pure-centre indicator (error O(q + beta^{-3/2})), so Cov -> 1/2 - 1/4. Spectral
step as in C0a; m_+ <= (36 beta n^3 + log 20)/(t-3).

**D8. Typical conditional accuracy, L298. HOLDS.** Centre normalizer cosh(b Re y); ||G_b||_p^p ~ e^{pb} b^{-3/2}/(e^{pb} b^{-3p/2});
R in [3,6] with probability -> 1 and monotonicity in b for R < 3; s_* beta^{(3/2)(1-1/p)} -> 0 iff p < 4.

**D9. (18) and the smooth slow mode, L303-315. HOLDS.** nu * nu-check = mu-type mixture with Q_eps (centre commutes);
faces with four cap links lie within 4 eps of +-I, so all-positive caps cost <= 8 beta eps^2 <= 8/b^2 per face and
1 - f_beta <= 16/b on all-cap faces; Haar faces give f_beta > 0 with probability <= C b^{-3/2}; ||q_eps - 1||_p <=
C eps^{-3(1-1/p)} + 1 with eps^{-3} = beta^{3/2 + o(1)}; exponent -9/8 + (3/2)(1-1/p) < 0 iff p < 4.

**Step 5 verdict.** 9 statements, all HOLD; no correction needed. (Statements (9)-(12), (17), smooth (11), (26), (40) and
the spectral step were checked in Steps 3-4.)

## Step 6. Block D, second half (L334-423, L544-658) and the cited earlier rows

Cited rows read where a step depends on them: row 1161 consumer (L148), necessity (L150), (26) and the equivalence
(L379-400); all checked HOLDS in row 1162 (`gap-solve9-check-opus.md` table: S10, S11, S18, S19; (19) is S25, used only
in the remark at L211). Row 1186's small-ball comparison (L139) and row 1153's purity test (L392) are re-proved in the
checked text itself, so nothing depends on those rows. Outline citations (GL3 eigenvalue formula, KP L1223-1356,
AM6-AM7 chessboard L2885-2942) are standard results used as cited; I did not re-read the outline lines.

**D10. (20)-(21), L338-351. HOLDS.** Gauge change of variables gives the factor W exactly. Every proper nonempty vertex set
has >= 2j 5^{4-j} >= 8 boundary edges (periods >= 5; translate a partial line along invariant directions), so induced edges
<= 4(|B|-1) and |S| <= p_V r(S) per component (spanning case: 4V = p_V (V-1)). Edmonds' spanning-tree polytope via greedy and
summation by parts (w.1_{T*} - w.x = sum (w_i - w_{i+1})(r(S_i) - |S_i|/p_V) >= 0) gives a tree law with P(e in T) = 1/p_V;
generalized Hoelder with exponents P(T); the rotated links of a tree are iid Haar.

**D11. (22), L353-357. HOLDS.** A leaf vertex integrates h to 0; surviving components are leafless, >= 4 edges, activity
<= delta^{|S|} by (21); KP as in (11). At s <= beta^{-9/8-eta}: ||h||_{p_V} <= C s eps^{-3(1 - 1/p_V)} = beta^{-eta + 3/(8V) + o(1)} -> 0
as V, beta -> infinity (1 - 1/p_V = 3/4 + 1/(4V)).

**D12. (23), L359-365. HOLDS.** The convolution of two half-caps has density >= c eps^{-3} within c' eps of I; frames within
c' eps/3 of the root give W(I) >= (c eps^3)^{V-1}(c s eps^{-3})^E, and (V-1)/E = 1/p_V. s = eps^gamma with
3(1-1/p) < gamma < 3(1-1/p_V). At s_hi: -(9/8) log beta + sqrt(log beta) + (9/8) log beta + (9/4) log b + O(log beta/V) -> infinity.

**D13. (24), L372-387. HOLDS.** Upper: <= 4V/K crossing links, >= (eta - 4/K)V internal chords, each closes a cycle of length
<= B whose holonomy is within Br of the centre in any gauge; the constraint for chord i reads only the forest, so conditional
densities <= C(1+beta)^{3/2} give (C B^3 t^3)^d; 2^{4V} candidate sets. Lower: tree gauged to I, k chords in the r-cap and
q - k in the thermal cap, bounded face cost; denominator from (9); the leftover (1+beta)^{-3/2 - (9/2)V/ell} is
o(V log(1/t)) when ell >= log(2+beta).

**D14. (25), L394-399. HOLDS.** A one-edge vertex makes the marginal constant in that edge, so its (Q - sigma) integral
vanishes. Periods >= 6: odd cycles wrap (length >= 6), so leafless supports with <= 5 edges are single squares. Square
coefficient: pinned ratio (rho(I) + rho(-I))/2 = a_p + 1 for the full square, 1 for each of the 15 proper subsets (forests),
alternating sum a_p. Then J_s(v) = J_0(v) + s^4[2 sum_v a_p - sum_{2v} a_p] + O(s^6) = J_0 + 2V[abar(v) - abar(2v)] s^4 + O(s^6).

**D15. (27), L413-421. HOLDS.** |c_S| <= 2^{|S|} K^{b(S)} from the pin expansion and (17); s^l K^{l-3} = K s^4 (Ks)^{l-4}; connected
non-square leafless supports have >= 6 edges; multi-component sum <= e^{C lambda} - 1 - C lambda; |s^4 sum a_p| <= C lambda since
|a_p| <= CK. Onset: Ks = (lambda K^3/V)^{1/4} -> 0 for V >> K^3, and (26) traps s^4 sum a_p between c lambda and C lambda.

**D16. (38), L546-554. HOLDS.** P(S > C_0 V/beta) <= (Z(beta/2)/Z(beta)) e^{-C_0 V/2} <= e^{-c_0 V}; conditionally independent
pivot deviations have bounded e^{c beta d^2} moments; the two exterior conditions (few weak tilts, sum Delta(y_i)^2 = O(V/beta))
then fail with probability <= 2e^{-cV}; no-hit <= e^{-c Lambda} + P_bad(1 - e^{-c Lambda}), giving e^{-c''' Lambda} for
Lambda <= c''V (the bounded range 1 <= Lambda <= Lambda_0 is covered by the same 1 - c bound; wording only). Upper: one-edge
conditional bound b_0 given avoidance of faces not containing p's edges, local-lemma induction with x = 2 b_0,
(1-x)^{d_0} >= 1/2, product over 6V faces.

**D17. (39), L556-564. HOLDS.** Three-edge paths of separated squares extend to a spanning tree; in that gauge the fourth
edge is a conjugate of U_p^{+-1}; favorable exteriors from D16; hit probability >= c t^3 e^{-CM^2}. Upper: a face with
Delta > 4r needs a failed edge in every gauge (triangle inequality); per face the tilt puts mass >= c_t outside the 4r caps
in both regimes of w. Large radius: tree-gauge link = product of <= 8k conjugated faces, Delta subadditive for products
modulo the centre, E Delta^2 <= C k^2/beta; failed fraction <= 4/k + C k^2/(beta r^2).

**D18. (41) and the DLR corollary, L597-616. HOLDS.** Under G, the one-link conditional density is <= K/(1 - C 8^{R+1} K r^3)
<= 2K; the all-Haar integral with G is positive (sequential avoidance). Label girth > R since R eps < r. Removing a cyclic
component Gamma: the rest is gauge invariant at Gamma's vertices (components are vertex-disjoint), forest pins cost 1,
b(Gamma) further pins <= 2K each, label ratio t_s^j, injective; b(Gamma) <= j/k. Tree components unpin exactly after the
final site-gauge average. On good markings the law in Omega is Wilson restricted to G, whose rejection probability under the
Wilson conditional is <= C|Omega| 8^{R+1} K r^3. Cutoff relation: a^{-4} a^{(4+xi)(1-o(1))} = a^{xi - o(1)} and
8^{R+1} a^{3 eta} = a^{3 eta - o(1)}; at fixed large beta, R -> infinity and the Feller continuity of the Wilson kernel give DLR.

**D19. (42), L621-634. HOLDS.** Z_s = s^E L(w); L(w_* e^{z/E})/L(w_*) = E[e^{zj/E}]; for |arg w - arg w_*| < pi/E the nonzero
summands have arguments in an arc of length < pi, so no zeros. Location: z_beta^{(3/4)(1-1/ell)} <= C/B with B = (1+beta)^{9/8}
when ell >= log(2+beta); at s = D/B the ratio of j >= E/4 terms to (cs)^E is <= (2/c)^E (C/D)^{E/4}; at s = d/B the ratio of
E - j >= E/4 terms to [c(1-s)/B]^E is <= 2^E (2d)^{E/4} (C/c)^E. Whole-torus boundary argument gives a 1 - delta pure majority;
j/E tends to the majority bit, mean -> 1/2; Rouche at z = i pi; ds = -s(1-s) dw/w.

**D20. (43) and the reflection failure, L639-656. HOLDS.** Under F_R (R >= 6) the two reflected three-edge centre paths
close a 6-cycle: M_11 = 0 < M_01, determinant -M_01^2 < 0. Bit model: p = s^4 + (1 - s^4)/2; one-link density <= 2 (each bit
value has Haar mass 1/2 for any exterior); constant configurations dominate with error 2[(1 + e^{-2J})^{4N} - 1] -> 0 at
J = 10 log n, N ~ n^4; t^N ~ e^{-2 s^4 N} -> 0. Transfer A K A with ||K - I|| <= (1 + e^{-2J})^m - 1, A^2 = diag(1, t^m, <= e^{-2J}),
Weyl gives a second eigenvalue <= n^{-16}; all nonzero levels neutral (kernel depends only on flip-invariant bits), so
Z_neut = Z; (28) holds since the action is gauge invariant; P_s(u)^2/P_s(2u) = [Z_0(u)^2/Z_0(2u)][B_s(u)^2/B_s(2u)][Z_s(2u)/Z_s(u)^2]
-> 2 x 1 x 1. Smoothing step: e^{J f(x) f(y)} positive definite by its power series; continuity at fixed cutoff.

**D21. OPEN paragraphs and RESULT, L748-754. HOLD as scope statements.** p(u)^2/p(2u) < 3/2 iff p(2u)/p(u)^2 > 2/3; the
listed o(1) corrections are exactly those checked in B4, B6, B11; the RESULT line matches the body.

**Step 6 verdict.** 12 items, all HOLD; no correction needed.

## Step 7. Numeric guide (guides only; no verdict above rests on it)

memory_pressure at 01:28Z: 61 percent free. Tests and pass criteria, written before the run:

- T1, (1): for beta in {0.1, 1, 5, 20, 60}, h in {ceil(4 e beta), ceil(4 e beta) + 3} (h >= 1), m = h - 1, x on a 401-point
  grid of [-1, 1]: (1 - 2^{-h}) w <= w_m <= w. Pass: no violation beyond relative 1e-12.
- T2, Bessel bound in (8): r_l(b) = I_{l+1}(b)/I_1(b) >= exp(-(l^2 + 3l)/b) for l = 0..60, b in {0.5, 1, 3, 10, 30, 100, 300}.
  Pass: no violation beyond relative 1e-12.
- T3, eta_d and nu_d (A4, A5): for d in {6, 12, 18}, every monomial z1^a1 conj(z1)^b1 z2^a2 conj(z2)^b2 of total degree <= d has
  eta_d average equal to the Haar value (a1! a2!/(a1 + a2 + 1)! if a1 = b1, a2 = b2, else 0); and nu_d gives E chi_j = delta_{j0}
  for 2j <= d. Pass: max error < 1e-10.
- T4, approximate identity in (34) (B7): f_m = (1+x)^m + (1-x)^m, m in {10, 20}: half-integer character coefficients vanish and
  integer ones are >= 0. Pass: |half-integer| < 1e-10 (relative to c_0), integer >= -1e-10.

Run at 01:29Z (date -u) under `lab_ops.py numeric-lock` (holder solve20-check-opus, acquired and released), `nice`, BLAS threads 1,
python3 -I, scratch scripts and log in a /tmp scratch folder (not committed). Results:

- T1 first pass: no violation within relative 1e-12, but for beta >= 5 delta = 2^{-h} is below double precision, so that pass
  tested nothing there. Rerun in log space (log P(Pois(b) >= h) by the leading term times the convergent ratio series, beta up
  to 200): no violation; the smallest margin log delta - log tail over the grid is 2.66. PASS.
- T2: no violation; min r_l/bound = 1.000000 (equality at l = 0). PASS.
- T3: eta_d with 576, 2268, 5760 atoms (d = 6, 12, 18): max monomial error 3.1e-16; nu_d characters E chi_j = delta_{j0} for 2j <= d
  with max error 2.6e-11 (pairwise sums of up to 3.3e7 terms). PASS.
- T4: half-integer coefficients <= 1.6e-16 c_0, integer coefficients >= -1.5e-17 c_0 (rounding). PASS.

What this establishes: nothing beyond guidance. It is consistent with A1, D1 (the Bessel lower bound), A4-A5 and B7, by a
different data path (floating-point evaluation instead of the hand arguments). It does not touch any statement whose
proof is asymptotic (blocks B, C, most of D).
