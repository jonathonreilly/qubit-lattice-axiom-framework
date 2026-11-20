lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T13:37Z

# Check of row 1204 (`library/gap-solve21-astra62.md`), queue row 1210

Cross-provider check: the author is gpt-6.2-astra max (row 1204), the checker is Claude Opus 5.5 max on the Mac mini
Claude worker. Pinned at commit 5e5082e7c. Started 2026-11-20T01:37Z (date -u).

Scope (row 1210): check line by line, by hand, positive claims first: the relativistic mass test (1), the strip bound
(8), the Wilson contact and infrared estimates (21), (26), (32)-(35), the axial-packet exclusion (36); then everything
else. For each cited earlier row, read the cited statement and its proof where the step depends on it. Verdicts:
HOLDS, HOLDS AFTER CORRECTION, FAILS, with the line. Numerics guide only.

## Plan (at most eight steps; one step per response, appended as done)

1. Read the checked file in full; inventory its labelled statements with line numbers; list cited earlier rows.
2. Check (1), the sharp relativistic mass test, and what it rests on.
3. Check (8), the strict strip bound.
4. Check (21) and (26), the Wilson contact and infrared estimates.
5. Check (32)-(35).
6. Check (36), the exclusion of axial plaquette packets.
7. Check everything else, and the cited statements of earlier rows where a step depends on them.
8. Verdict table and RESULT line.

## Status log

- 2026-11-20T01:37Z: file created; step 1 next.

## Step 1. Inventory of the checked file (done 2026-11-20T01:38Z, date -u)

`library/gap-solve21-astra62.md` at the pinned commit: 437 lines, 75,012 bytes, read in full. Labels: 6 GUIDE paragraphs
(L3, L5, L7, L13, L46, L109), 5 OPEN paragraphs (L9, L42, L140, L386, L435), and 61 PROVED paragraphs, which I group into
60 statements S1-S60 in file order (S1 = the two paragraphs L15 and L30; every other S is one paragraph). Each verdict
below gives the S-number, the line and the equation.

| S | lines | content |
|---|---|---|
| S1 | L15-30 | (1) norm of B_h = Q(hM) in a relativistic vacuum representation |
| S2 | L32-40 | q_0 = e^{-pi/2}/2, strict threshold, (2) |
| S3 | L48-61 | PL5 dispersion E >= g(abs eta); (3) B^(k) <= b_k; (4) b_k asymptotics |
| S4 | L63-71 | (5) concentration near x_0 = pi/2 |
| S5 | L75-92 | two perpendicular reflections, (6) |
| S6 | L94-99 | (7) quantitative deficit |
| S7 | L101-107 | (8) strict strip bound (same-time spatial sources, R(F) <= 1) |
| S8 | L113 | strip functions are a proper subspace (one-link variance, row 1173 (8)) |
| S9 | L115-126 | (9) lower bound on the transverse numerator for alternating plaquette sums |
| S10 | L128-138 | (10), (11) R(F) unbounded at the mirror through the source |
| S11 | L144-154 | (12) three reflected correlations give the continuum ratio |
| S12-S13 | L156, L158 | totality of box vectors under the Wightman hypotheses |
| S14 | L160 | abelian time-zero strip algebras are not cyclic |
| S15 | L162 | shell (conditional-integral) representation |
| S16-S17 | L166-172 | free Maxwell singlet approaches q_0 with deficit O(A^-2) |
| S18 | L174-179 | (13) spectral representation of A_0/abs(x)^8 |
| S19 | L181-186 | (14) l^{-9/2} power law for the free action density |
| S20-S21 | L190-197 | (15) momentum projection of strip subspaces |
| S22 | L199-205 | (16) delocalization |
| S23 | L209-214 | (17) |
| S24-S25 | L216-223 | (18) full-space test and its finite Wilson form |
| S26 | L225-229 | (19) small-h expansion of Q |
| S27 | L231-235 | (20) |
| S28-S29 | L239-246 | (21) contact identity for the cube transfer and its proof |
| S30 | L248-253 | (22) |
| S31 | L255-260 | (23) |
| S32-S34 | L264-277 | (24) free lattice singlet comparison, lower edge g(abs eta) |
| S35 | L281 | padding gives R = 1 |
| S36-S37 | L283-289 | (25), no common reflection-norm bound |
| S38-S39 | L293-300 | (26) second-moment contact identity |
| S40-S41 | L302-308 | (27) and its compatibility with (24) |
| S42-S45 | L312-326 | (28), (29) all-momentum neutral weight on a cube |
| S46-S48 | L330-348 | (30) thermal transition measure, first exponential moment |
| S49 | L350-358 | (31) |
| S50 | L362-366 | (32) infrared domination in the four-cube limit |
| S51 | L368-376 | (33) |
| S52 | L378-384 | (34) |
| S53-S55 | L390-399 | (35) and the exact contact in the limit state |
| S56-S58 | L403-422 | (36) axial plaquette packets and its consequence |
| S59 | L426 | Euclidean Gram lower bound in four directions |
| S60 | L428-433 | bounded real-frequency density of the massless singlet |

Cited sources a step depends on (to be read where needed): row 1161 `gap-solve9-astra62.md` (18)-(20), the one-link
conditional variance c_0 and the inverse estimate, with its check `gap-solve9-check-opus.md` (S21-S24); row 1173
`gap-solve15-astra62.md` (8); the outline's PL4-PL7 (lines 3260-3427) and GL3-GL7 (lines 2224-2311) by Sussman and
Alpoge, via `sa-index/chunk-02.md`, `chunk-03.md`; PH1 Lemma 2 `ph1.md`; outline lines 1601-1624 (free curvature);
outline F2/F3 lines 4289-4314, 4360-4374; `gap-neutral-chain-check-astra.md`; row 977 `gap-tiltproof-max.md` 5.3.

## Step 2. The relativistic mass test (1), (2) and its expansion (19), (20) (done 2026-11-20T01:39Z, date -u)

**S1, L15-30, (1): HOLDS.** Checked by hand.
- Multiplier: (1/4)|1 - e^{i h p_1}|^2 e^{-hE} = (1/2)(1 - cos(h p_1)) e^{-hE} = sin^2(h p_1/2) e^{-hE}, as written.
- Norm: for a bounded continuous function b of the commuting generators, the norm of b(H, P) is the essential supremum
  of b under the joint spectral measure, which equals sup over the closed support Sigma because b is continuous. Correct.
- Orbits: covariance U(L) e^{i a.P} U(L)^* = e^{i (L a).P} gives E(L Delta) = U(L) E(Delta) U(L)^*, so Sigma is
  Lorentz invariant. In the closed forward cone E = 0 forces p = 0, so every point of Sigma minus 0 lies on a mass
  hyperboloid (mu > 0) or on the null cone minus 0, and contains (sqrt(mu^2 + (x/h)^2), (x/h, 0, 0)) for every x >= 0
  (x > 0 on the null cone). At fixed p_1 the transverse momentum only raises E; folding h|p_1| into [0, pi] keeps
  sin^2 and lowers E. So the supremum on the orbit of mass mu is Q(h mu); on the null cone the maximiser x = pi/2 > 0
  is admissible, so the value is Q(0).
- Q is the maximum over a compact x-interval of a jointly continuous function, so it is continuous; it is
  non-increasing in y because sqrt(x^2 + y^2) is. Hence sup over the masses in Sigma of Q(h mu) = Q(h M). The origin
  contributes 0. No step uses a discrete mass shell.

**S2, L32-40, q_0 and (2): HOLDS.** d/dx log(e^{-x} sin^2(x/2)) = cot(x/2) - 1, which is strictly decreasing and
vanishes only at x = pi/2; value e^{-pi/2} sin^2(pi/4) = e^{-pi/2}/2. For y > 0, at the maximiser x_y of Q(y) the
value is positive, so sin^2(x_y/2) > 0 and Q(y) = e^{-sqrt(x_y^2+y^2)} sin^2(x_y/2) < e^{-x_y} sin^2(x_y/2) <= q_0.
For (2): Q(y) >= (1/2) e^{-sqrt(pi^2/4 + y^2)} (value at x = pi/2), so Q(hM) <= q_0 e^{-delta} gives
pi/2 + delta <= sqrt(pi^2/4 + (hM)^2), i.e. (hM)^2 >= pi delta + delta^2. Correct. The edge statements: every point of
Sigma minus 0 has E >= sqrt(E^2 - |p|^2) >= M, and each orbit contains its rest point, so inf spec(H) on the complement
of the zero four-momentum space is exactly M. B_h annihilates that zero space, so (1) says nothing about vacuum
multiplicity; the file says so (L40). The empty case (Sigma = {0}) is excluded by the hypothesis on L15.

**S26, L225-229, (19): HOLDS.** With log f(x, y) = log sin^2(x/2) - sqrt(x^2 + y^2) and
sqrt(x^2 + y^2) = x + y^2/(2x) + O(y^4) uniformly for x in a neighbourhood of pi/2: the lower bound
log(Q(y)/q_0) >= -y^2/pi + O(y^4) is the value at x = pi/2. The critical equation cot(x/2) = x/sqrt(x^2+y^2) and the
non-degenerate maximum of log f(., 0) (second derivative -1/2 at pi/2) give x_y = pi/2 + O(y^2); then
log f(x_y, y) <= log q_0 - y^2/(2 x_y) + O(y^4) = log q_0 - y^2/pi + O(y^4). Uniform convergence keeps the maximiser
near pi/2 for small y (the maximiser of f(., 0) is strict and unique on [0, pi]). The remark about a running coupling is
labelled as a hypothesis, which is correct.

**S27, L231-235, (20): HOLDS as a conditional corollary of (7)** (verdict on (7) in Step 3). If the Wilson ratio is
within C_1 (hM)^2 of q_0 and k^{-2} = o((hM)^2), then with b_k = q_0(1 + O(k^{-2})) from (4) the left side of (7) is
at most C_2 (hM)^2, and (7) gives [1 + D/k + log(2 + R(F))]^2 >= c/(C_2 (hM)^2). Note that by (1) and (19) a normalised
continuum state can come no closer than q_0 (hM)^2/pi + O((hM)^4) to q_0, so the hypothesis needs C_1 >= 1/pi; the
file's "c depends on the constant in the approximation" covers this. The sentence "Boosting to weak coupling changes
momentum and energy together" (L235) is commentary, not a step.
