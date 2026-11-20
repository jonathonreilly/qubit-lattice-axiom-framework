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
