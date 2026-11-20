lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T05:28Z

# gap-mini-solve-ba-opus (FINISH row 1313): plain brief "prove the SU(2) mass gap"

Row 1313, queued 2026-11-20T17:27Z. Worker: Claude Opus 5.5 (max) on the Mac mini, pinned at a084d7b24 on
`claude/ym4d-hard-route`. No commit, claim or push from this machine; a relay copies this file.

Labels used: PROVED (a complete argument written here or cited with anchor), ARGUED (an argument with a named gap),
GUIDE (numeric or heuristic, never a proof step), OPEN.

## 0. Status log

- 2026-11-20T17:28Z (date -u): file created; reading FINISH rules, GOAL.md, `parts/gap.md`, row 1218's digest.
- 2026-11-20T17:29Z (date -u): read GOAL.md in full; FINISH.md L1-84, L320-352 and this row (L1394); `parts/gap.md` L8-104;
  `library/prior/gap-onebound-read-sol.md` (row 1218) in full; RESULT lines of rows 1274-1307; Steps 0-1 of the
  sibling row 1309 (`gap-mini-solve-ay-opus.md`), which owns the account's `9.1:prop-blind-site-expansions`
  (CA-III L16559). So that item is taken; this row picks another.

## 1. Record read (pointers, not evidence)

1. The gap clause, modulo the ultraviolet carry, reads one lattice input at one physical size, uniformly in the cutoff:
   (N-phys) of row 1161 (`gap-solve9-astra62.md` L146-148; restated in row 1218's digest L38-44), equivalently a
   uniform cube gap plus the count (TR) of row 1259. Rows 1188-1300 (about 25 plain-brief rows) attacked it or its
   inputs; every route they name is on file with a first failing step.
2. Row 1218 (`prior/gap-onebound-read-sol.md`): the six-author paper A proves a conditional ascent from a one-scale
   thermal window (A-B*) / (A-B**) (L81-101) to a full transfer gap (Theorem F); row 1295 checked its lattice half
   (HOLDS). Paper B's weak-coupling Corollary 166 (L182-187) is BP(n, 1/2) for straight-path block variables on tori
   of side at most exp(2^k/(17k)); row 1220 (`gap-mini-solve-p-fable.md`) found it is the near-Haar property of long
   straight transports (an ultraviolet self-energy effect), and that B's Remark 155 says (H1) carries no gap
   information. Zeng's tunnelling package: row 1251 (`gap-mini-solve-ad-opus.md`).
3. The one-cutoff carry (rows 1256-1299) is reduced to named inputs; sibling rows own them (1309 the blind-site
   expansion).

## 2. How best to attack it (judgement, ARGUED; written 2026-11-20T17:38Z by date -u)

**Where the proof dies.** Modulo the ultraviolet carry and the continuum datum of the T0 chain, the Jaffe-Witten gap
clause reads one lattice estimate, (N-phys), at one physical size, uniformly in the cutoff (checked chain: row 1183,
`gap-neutral-chain-check-astra.md` L142). Its fixed-coupling forms (Theorem S's seed, (SL), (A-B*)) are statements
about finite but huge integrals at order-one coupling (lattice correlation length a few spacings, boxes of tens of
correlation lengths). Under the no-computation rule they need an analytic method valid at order-one coupling. None is
known: published hand gaps for SU(2) Wilson stop near beta_W = 0.36 (row 1218 digest L110-116, L175-180), and every
weak-coupling tool (Balaban's RG, B's Corollary 166) controls only ultraviolet content (row 1220). I re-derived three
quick forms of the seed before reading tables (the Renyi-2 form of (A-B**): 2 log Z(T) - log Z(2T) is the Renyi-2
entropy of the thermal state; the count (TR) as the low-temperature pressure of the confined phase; a small-volume
toron start, which fails because u E_1 <= g^(2/3)/K at small L). All three are on file (Renyi/purity in about 25
lane files; (TR) = row 1259 Lemma CD and row 1300; small-volume reduced models = rows 1285, 1287). Verdict: no route
to the seed off the record. I do not attack it, and nothing below counts as progress on it.

**What I do instead.** FINISH "Hardest first" lets a non-seed item go first only if it "could be hiding a real gap".
The one-cutoff carry's cut half now rests on Sussman and Alpoge's regular-gas chapter (row 1299 4.8, PROVED GIVEN
premises (P1)-(P5)). Two of those premises are decidable from texts on hand and could hide a real gap:
- (P4) the constant conditions (UM14), (UM19), (UM23), (UM26') "in one order of choice", together with q > p_0 of
  row 1299 4.7 (equivalently p_1 > p_0 in CA-I 4.3). If the conditions cannot be met in one order, the route through
  SA's chapter fails at that step.
- (P3) SA's structural identities (heredity, normalized functional, wall factorization, SA L14406-14412) and the
  completeness identity at complete physical pairs (SA L14262-14271), which SA states as hypotheses of its chapter.
  If no text proves them for the carry's step, the carry rests on an unproved hypothesis.
Rule 0a: `grep -n "(P4)\|(P3)" FINISH.md` and row 1299's own file name these only as open premises (row 1299 4.8);
`library/open-core.md` has no entry for them (checked in Step 3 below). Sibling rows: 1309 holds the blind-site
expansion; 1310 and 1314 had no item on the branch tip at 17:36Z.

Moves: the one-cutoff carry on the pin route (rows 1256-1299), premises (P3)-(P4) of row 1299 4.8. Success: (P4)
PROVED (an explicit order of choice) and (P3) located as proved text or reduced to a named statement; the cut half
then rests on (P1), (P2), (P5) only. Failure: the first constant condition that cannot be met, or the identity no
text proves. Neither outcome changes the seed.

**Plan, one step per response, each appended before the next.**
- Step 3: fetch SA's outline and CA-I by URL into a scratch folder; read CA-I 4.3 (p_0, p_1) and SA's chapter
  L13893-14811 for every constant condition; record each condition with its line.
- Step 4: the order of choice (P4), or the conflict.
- Step 5: (P3): read SA L14262-14271, L14406-14412 and search the library for proofs of the identities.
- Step 6: labels, what a checker should redo, RESULT.

## 3. The exponents p_0, p_1, q in the account (READ; written 2026-11-20T17:39Z by date -u)

Sources fetched by URL into a scratch folder outside the repository: Sussman and Alpoge, `YM4_sketch_500.tex`
(32,992 lines) and `theorem_0_complete_account_raw_I.tex` (CA-I, 166,711 lines) at commit 31a47c543775.

**3.1 What CA-I fixes (READ).** CA-I Notation 2.3:not-stages-first (L1332), Stage 0 (L1345-1390):
- p_0 in N, "free upward", with floors p_0 >= 5r (CMP 119) and p_0 >= (d+5) r_0 + 8r + 3 (L1352-1353);
- p_1 "a window": "We assume that 2p_1-(d+5)r_0>p_0" (CMP 122b), **p_1 < p_0** (CMP 122a), and finitely many lower
  bounds on p_0 - p_1 by numbers at most 4r+1 (L1353-1357); the account takes **p_1 := p_0 - 4r - 1** (L1359-1363);
- **q := q_0 = q_1, free upward, with floors such as q >= p_0 + 7r + 1 and q >= 3p_0 + 3r + 1** (L1364-1366).
The same window is restated at L1866-1876 (with r_1 for r_0) and L2017-2019; Proposition 2.4:prop-order-consistent
(L2271) asserts the order can be met. The degree function is p_0(g) := A_0 (log g^(-2))^(p_0) (L1014). In CA-I 4.3
(L4167-4178) the fluctuation domain of CMP 119 (3.43) has radius C_1 p_1(g), p_1(g) = (log g^(-2))^(p_1), and the
cutoff radius is (A_1/A_0) p_0(g).

**3.2 Consequence for row 1299 4.7 (READ, deduced).** Row 1299 4.7 (`gap-mini-solve-aw-opus.md` L352) closes (E0)
"provided q > p_0 (equivalently p_1 > p_0; not checked against the account's choice of p_1 here)". In the account the
two are NOT equivalent: q > p_0 HOLDS (q >= 3p_0 + 3r + 1), and p_1 > p_0 FAILS (p_1 = p_0 - 4r - 1 < p_0, and
p_1 < p_0 is one of the account's own conditions, from CMP 122a). So the cutoff radius (A_1/A_0) p_0(g) GROWS FASTER
as g -> 0 than the fluctuation-domain radius C_1 p_1(g): their ratio is (A_1/(A_0 C_1)) (log g^(-2))^(4r+1) -> infinity.
Which inequality (E0) needs depends on what "the box" of SA's condition (C2) is: if it is the ci-form box R = l^q, (E0)
holds; if the high threshold must lie inside the fluctuation domain of radius C_1 p_1(g), the reading of 4.7 fails as
written. Next: read `library/ci-form.md` and SA L14276-14340 to decide.

**3.3 What the box is: Balaban's own radii (READ; written 2026-11-20T17:43Z by date -u).** Balaban's papers are in the owner's paper
folder (OCR text plus PDF; formula (3.43) read from the page image, CMP 119 journal p. 276).
- CMP 119 (2.28) (OCR L832-838): the effective-action terms E^(j)(X, (U, J), z) are analytic on U_j(X, alpha_0j,
  alpha_1j) with **alpha_0j = g_j C_0 (log g_j^(-2))^(q_0), alpha_1j = g_j C_1 (log g_j^(-2))^(q_1)**, "where q_0, q_1 are
  integers greater than 1, C_0, C_1 are sufficiently large positive numbers". In units of the rescaled fluctuation
  (field / g) these radii are C_0 l^(q_0), C_1 l^(q_1), l = log g^(-2). The account takes q = q_0 = q_1 >= 3p_0 + 3r + 1.
- CMP 119 (3.3)-(3.4) (OCR L1150-1167): the small-field cut on approximate fluctuation fields is
  **delta_k = g_k (A_1/A_0) p_0(g_k)** = g_k A_1 l^(p_0); rescaled radius A_1 l^(p_0). This is CA-I 4.3's "cutoff radius
  (A_1/A_0) p_0(g) ... the quantity delta_k/g_k of CMP 119".
- CMP 119 (3.43) (page image): the space Ũ^c_(k+1)(Y, (1+beta) alpha~_0, (1+beta) alpha~_1) x {A : supp A in
  Y ∩ Λ^(k)*_(k+1), |A| < C_1 p_1(g_k)} is the analyticity space of the **remaining terms only**, those whose
  localization domain is not contained in the small-field region Λ_(k+1) ("These remaining terms will contribute to the
  boundary terms B^(k+1)"). The terms with Y inside Λ_(k+1) "satisfy exactly all the conditions" of Lemmas 5, 6 of
  CMP 116 with the analyticity space (I.6.34) of CMP 116 (not readable on this machine).
- CMP 122a (1.27) (OCR L404-410): near large-field regions the approximate fluctuation field is cut at
  **delta'_j = g_j A_1 p_1(g_j), p_1(g) = (log g^(-2))^(p_1), "and p_1 < p_0"**. CMP 122b (OCR L1431-1438) uses the same
  p_1 for its largest large-field factor and assumes 2p_1 - (d+5) r_0 > p_0.
So Balaban has two cuts and two domains: the p_0 cut with the q-radii in the small-field interior, and the tighter p_1
cut with the p_1 domain (3.43) for terms touching large-field regions. Each cut lies inside its own domain
(A_1 l^(p_0) < C l^q since q > p_0; A_1 l^(p_1) < C_1 l^(p_1) since C_1 > A_1 is among "C_1 sufficiently large").

**3.4 Verdict on (E0) of row 1299 4.7 (PROVED given the box hypothesis named below; correction of a reading).**
(a) The parenthesis "(equivalently p_1 > p_0)" of row 1299 L352 is FALSE in the account: p_1 < p_0 (CA-I L1356, from
CMP 122a). Row 1299 4.7 took "the fluctuation domain on which the step's potentials live has radius C_1 p_1(g)" from
CA-I 4.3 L4167-4178, i.e. the domain (3.43); with p_1 < p_0 that domain is NOT a box that contains the p_0 cut at small
coupling: (A_1 C_win l^(p_0)) / (C_1 l^(p_1)) = (A_1 C_win / C_1) l^(4r+1) -> infinity as g -> 0, and C_1, A_1 are
chosen before gamma (CA-I (H3) L1143-1149).
(b) (E0) itself HOLDS on the right box. Claim: if every potential type of the regular step is holomorphic on the
rescaled polydisc of radius R = c_R l^q with q > p_0 and c_R > 0 fixed before gamma (the ci-form box (1),
`library/ci-form.md` L12, which takes c_R = 1 and q > p_0 + 2r; the account's q >= 3p_0 + 3r + 1 meets it), then for
every pair of thresholds b_lo <= b_hi <= 2 C_win A_1 l^(p_0) the real cut ball of radius b_hi lies in the box once
l^(q - p_0) > 2 C_win A_1 / c_R, i.e. for g below a threshold fixed after A_1, C_win, c_R, q, p_0. Proof: the real ball
{|B(b)| < b_hi} lies in the scalar-coordinate polydisc of radius b_hi (`ci-form.md` L14: "A real bond ball of radius b
lies in its corresponding coordinate box"), and b_hi <= 2 C_win A_1 l^(p_0) < c_R l^q under the stated threshold. The
factor 2 covers row 1268 7.3's relative difference |c - 1| = O(theta^(-1/2) polylog) <= 1 between the two frames for
small g. The low threshold b_lo >= (1/2) C_win A_1 l^(p_0) -> infinity gives (UM23) above a floor, as row 1299 4.7
says. This is a threshold on g chosen last, not a cap (CA-I L1247-1250 forbids caps on p_0, q, not thresholds on g).
(c) What (b) needs that is not proved here: the box hypothesis itself, that every potential type that enters the
regular step (free, intrinsic, older formed, inserted) is holomorphic on c_R l^q. For the older formed terms it is
CMP 119 (2.28) as the inductive property; for the intrinsic terms (change of variables, gauge fixing, Jacobian) it
follows from analyticity on an unscaled radius alpha (CMP 109 L955-966: analytic for |H_k| < alpha_1, absolute),
i.e. rescaled alpha/g, which exceeds c_R l^q for small g; for inserted vertices it is row 1299 Lemma V-SA's (UM1)
input. This is premise (P1)/(P2) of row 1299 4.8 (the ci-form's H-D), not new.
(d) A remark on the account (ARGUED; CMP 116's space (I.6.34) not read): CA-I 4.3's variant (L4167-4178) states the
regular step with "the fluctuation domain of CMP 119 (3.43) ... strictly less than C_1 p_1(g)" together with "the
cutoff radius (A_1/A_0) p_0(g)". Read on one fluctuation variable this pairing is inconsistent at small coupling in the
account's own order (p_1 < p_0), by (a). In CMP 119 the p_1 domain belongs to the terms touching large-field regions
and the p_0 cut to the interior; the interior terms use (I.6.34). A consumer that reads the variant should take the
box from CMP 119 (2.28) (radii ~ l^q) or from (I.6.34), not from (3.43). Evidence for the owner of the account port
(T0 tree), no edit made.

## 4. (P4): SA's constant conditions and an order of choice (written 2026-11-20T17:45Z by date -u)

**4.1 Inventory (READ, SA L14276-14720).** Notation as in SA's chapter "The unmarked majorant for the actual regular
polymer gas" (L14276). Fine cubes of side M, coarse cubes of side LM.
- Geometric constants, fixed by d and the cube adjacency, independent of L >= 2, M, the torus and the cutoff:
  C_h (UM7)-(UM8) ("independent of L >= 2", L14432); kappa_f and S_xi for xi > kappa_f (UM9); c_f (UM10); c_m (UM5)
  and c_b (UM11) are pure numbers once the factor (LM)^4 is taken out; C_p (UM13) ("includes the finite tags and their
  rooted sums"); c_l (UM17); C_v, C_D, kappa_D, c_adj (L14668-14675, "bounded-degree cube covering walks").
- Gaussian comparison inputs (UM4)-(UM6): coarse disc radius R_s > 2; matrix perturbation at most eps on |s| < R_s; gap
  constant K; constants eps_0(K), rho_0(K), A_K of the proved comparison (UM6), valid when eps <= eps_0(K) and
  rho + gamma/2 <= rho_0(K).
- Potential inputs (UM1): amplitude a = sum over types of the type norms, decay rate lambda_V (fine-cube tree length).
- SA's free choices, in SA's own order: W_0 > 0 and lambda_0 > kappa_f (L14484-14488); W_0, gamma with
  **(UM14) C_p W_0 M^(-4) + gamma/2 <= rho_0(K)**; then
  C_0 = C_p W_0 L^4 + A_K c_m (LM)^4 (eps + C_p W_0 M^(-4) + gamma/2) (UM15), p = exp(-gamma b^2/2);
  Lambda > 0; K_* = 2 + c_l Lambda, Theta = C_h (C_0 + K_*) (UM18); sigma_0 > kappa_f and
  **(UM19) lambda_V - lambda_0 >= Theta/L + sigma_0, log(R_s - 1) >= Theta**;
  u_Y, q = p e^Theta, p_* = n_b p, tau = e^Theta [2 c_f L^4 S_(sigma_0) a / W_0 + p_*] (UM22);
  **(UM23) a <= W_0/2, tau <= 1**; mu > 0, g_* = Lambda - mu, B_* = C_D e^(2 C_v) e^(-5 g_*) sum_m e^(-(g_* - kappa_D - C_v) m)
  (UM25); **(UM26) g_* > kappa_D + C_v, c_adj B_* <= 1**, and row 1299's (UM26'): e c_adj B_* <= 1.

**4.2 Where a circularity could hide (ARGUED, to be decided in 4.3).** Theta contains C_0, and C_0 contains the two
volume factors C_p W_0 L^4 and A_K c_m (LM)^4 (eps + gamma/2 + C_p W_0 M^(-4)). (UM19) then asks lambda_V >= lambda_0 +
sigma_0 + Theta/L and R_s >= 1 + e^Theta. In the account's order (CA-I (H3), L1143-1149) Balaban's decay exponent kappa
(the source of lambda_V) is chosen FIRST, before M_1, M_2 = L^2 M_1 and M = L^(m'), and the coarse disc radius R_s and
the perturbation eps belong to the local Gaussian comparison of the actual step. So (P4) is consistent only if Theta
can be made bounded independently of M (and of L), which needs W_0 L^4, gamma (LM)^4 and eps (LM)^4 bounded by
constants chosen before kappa. W_0 and gamma are SA's free choices; eps is a property of the step's actual covariance.
