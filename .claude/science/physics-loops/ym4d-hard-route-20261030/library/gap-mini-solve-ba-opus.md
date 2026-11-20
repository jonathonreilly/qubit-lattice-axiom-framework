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
follows from analyticity on an unscaled radius alpha (CMP 109 OCR L913-914: analytic in H_k "satisfying a boundedness condition of the form |H_k| < alpha_1, with an absolute, positive constant"),
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
  C_h (UM7)-(UM8) ("independent of L >= 2", L14431); kappa_f and S_xi for xi > kappa_f (UM9); c_f (UM10); c_m (UM5)
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

**4.3 The order of choice is on file (READ; written 2026-11-20T17:46Z by date -u).** Rule 0a search, done late (should have been
first): `library/in1.md` Lemma 3 (L336-372, "conditional UM budget and simultaneous choice") already carries out the
order of choice of SA's UM constants, with the circularity of 4.2 broken as follows (quoted in short):
- (22): W_0 = min{[3 P L^4 (1 + A c_m)]^(-1), rho_0/(2P)}, eps_* = min{eps_0, (3 D_0 M^4)^(-1)},
  gamma_tilt = min{2/(3 D_0 M^4), rho_0}, D_0 = A c_m L^4; "Only the first choice precedes M";
- (23): H_0 e^(b kappa-bar - dM) <= eps_*/2 (an M-floor) and a later radius/tube ceiling; hence (UM14) and
  C_0^UM <= 1, so Theta is bounded independently of M;
- (24): Theta = C_h^UM {3 + c_l [(1 + 4 beta_s) kappa + g_*]}, rate window lambda_0 + sigma_0 + Theta/L <= lambda <
  kappa/(2 C_h^WF) - eps_rate, "nonempty for large kappa" given a floor on L; then kappa-bar with
  log(e^(kappa-bar) - 1) >= Theta (this is (UM19)'s R_s-condition with R_s = e^(kappa-bar)), then M;
- the failed-bond floor b^2 >= (2/gamma_tilt){Theta + log(4 c_b (LM)^4)} ("the scaled box b grows proportionally to
  (log theta)^(p_0)"), which is (UM23)'s p_* part, and the insertion allowance a_* = min{W_0/2, (4 e^Theta A_a)^(-1)},
  (UM23)'s a part.
The gate `gates/in1-gate.md` (Claude, fresh session, first failing step none) records "Lemma 3. Holds" (L63-66) and
the verdict that the c4-order budget cycle is broken, conditionally on H-M (L161-164).

**4.4 Verdict on (P4) (PROVED, by citation plus two lines).**
(i) (UM14), (UM19), (UM23) in one order: in1 Lemma 3, checked (4.3), conditional on its hypothesis H-M (`in1.md` L99-108,
the actual matrix envelope on the discs |s| < e^(kappa-bar)), which is row 1299's premise (P2), not (P4).
(ii) (UM26'), row 1299's strengthening e c_adj B_* <= 1 of SA's (UM26): since B_* = C_D e^(2C_v) e^(-5 g_*) S(g_*) with
S(g_*) = sum_m e^(-(g_* - kappa_D - C_v) m) decreasing in g_*, (UM26') holds whenever SA's (UM26) holds with g_*
replaced by g_* - 1/5 and g_* - 1/5 > kappa_D + C_v: indeed e^(-5 g_*) = e^(-1) e^(-5(g_* - 1/5)) and S(g_*) <=
S(g_* - 1/5). So it is one more floor on g_*, which in1's order fixes before Theta (g_* enters (24) only through
Theta). No new cycle.
(iii) q > p_0 for (E0): holds in the account (q >= 3 p_0 + 3r + 1, CA-I L1364-1366) and in the ci-form (q > p_0 + 2r,
`ci-form.md` L12); the box is the q-box, by 3.3-3.4. The cut threshold is a threshold on g chosen last.
So (P4) is closed as a premise of row 1299 4.8, given H-M; row 1299's open list loses (P4). What it does not do:
supply H-M ((P2)), (UM1) ((P1)) or the structural identities ((P3)).

**4.5 Prior record of the exponent order (rule 0a, READ; written 2026-11-20T17:48Z by date -u).** The order p_1 < p_0 < q is already
on file: `library/b-in-r2.md` L251 ("Here p_1 < p_0 < q (I:1351-1364)"), `library/in1.md` L227 (IN1 order row 1:
"(p_0 + Cr)/2 < p_1 < p_0 - Cr, q > max(p_0 + 2r, C p_0)"), `library/lfi-ho.md` L261 (p_1 < p_0 - (5/2) r),
`library/ci.md` L335, and row 1268's file `gap-mini-solve-aj-opus.md` L470 (quoting CMP 122a "p_1 < p_0"). So 3.1 is a
re-reading, not new. What is new here is only the correction of row 1299 4.7's parenthesis and the identification of
(E0)'s box with the q-box (3.4), which in1's row-1 exponent order already makes consistent.

## 5. (P3): the structural identities (READ; written 2026-11-20T17:48Z by date -u)

SA states, as hypotheses of its chapter: "The remaining structural hypotheses are the actual heredity,
normalized-functional and wall-factorization identities. They identify (UM3) with the finite expansion on complete
physical pairs and define coherent local terms on every local complex core. These hypotheses concern the assigned
operators and supports. They are not consequences of a numerical Gaussian bound." (SA L14406-14412.) Its Gaussian
comparison chapter adds: "Completeness is separate. Equality of this local functional with a marginal of one
whole-torus Gaussian requires the actual completeness identity for its effective covariance. In the source
construction that identity is supplied on complete physical pairs and their physical-data continuation." (SA
L14262-14268.)

What the repository supplies:
- For the lane's adopted Y family D4, frozen `hma.md` Theorem 2 (L97-104) states that the local functional "is
  normalized, hereditary for these full reads, wall-factorizing, holomorphic at fixed real U, real at real parameters,
  pair-dependent and real-gauge covariant", via descent Theorem B. So the three identities hold for the D4 functional
  itself, conditional on hma's premises (library M = frozen hm and descent, FG, PIV).
- The link to the actual step is NOT supplied. Frozen hma's referee verdict (L598): "Not supplied: UM1 for the other
  potential types; SA's structural identities linking UM3 to the actual step's expansion", with the open list "carrier
  identification (D4 adopts hm's carriers rather than identifying them), stored-test/gauge-factor formation match,
  whole-domain admission, PH1-PH4 per step, the full vacuum interface, PIV" (L600). IN1's H-M carries the same clause
  ("agrees at physical parameters with the actual fluctuation law", `in1.md` L106) under "Outstanding - actual matrix
  envelope" (L108).

**Verdict on (P3) (READ).** (P3) is not a separate premise: its D4 half is hma Theorem 2, and its link half (that the
actual regular step's fluctuation integral equals the D4 gas (UM3) at complete physical pairs) is the carrier
identification that frozen hma lists as open, the same matching that row 1299 4.8 calls (P2) ("the carry's
presentation must be matched to D4 or supplied separately"). It is listed with an owner (the hard-core lanes of hm,
descent, hma), so by rule 0a I do not attack it. Row 1299's open list for the cut half shrinks from (P1)-(P5) to
(P1), (P2) (which now contains (P3)'s link half) and (P5).

## 6. State of this row after the first item (written 2026-11-20T17:48Z by date -u)

| Item | Before (row 1299 4.8) | After | Label | Where |
|---|---|---|---|---|
| (E0) both thresholds admissible | ARGUED, "provided q > p_0 (equivalently p_1 > p_0)" | holds on the q-box; the parenthesis is false (p_1 < p_0 in the account, CMP 122a); the p_1-domain of CMP 119 (3.43) is the boundary-term space, not the box | PROVED given the box hypothesis (the H-D/H-M domain clause) | 3.3-3.4 |
| (UM14), (UM19), (UM23) in one order | open premise (P4) | on file: in1 Lemma 3 (checked, gate in1 pass 3) | PROVED by citation, given H-M | 4.3-4.4 |
| (UM26') | open premise (P4) | one more floor on g_* (shift 1/5) | PROVED (two lines) | 4.4 (ii) |
| structural identities | open premise (P3) | D4 half: hma Theorem 2; link half: the open carrier identification (hma L598, L600) | READ | 5 |
| CA-I 4.3's variant (p_1 domain with p_0 cut) | not noted | inconsistent on one variable at small coupling in the account's own order | ARGUED (CMP 116 (I.6.34) unread) | 3.4 (d) |
| the seed (N-phys) | OPEN | OPEN, not attacked in this item | OPEN | 2 |

## 7. Second step: the margin reading (M) of rows 1294 and 1299 (written 2026-11-20T17:53Z by date -u)

**7.0 The statement.** Row 1294 4.2 (`gap-mini-solve-at-opus.md` L218-233) proves Proposition H2-cov (cross-admission
without connectedness of the core) GIVEN (M): "the supplier's requirement of EM L652-653 holds with a fixed relative
margin mu_m > 0, that is, for every frame and step, the earlier backgrounds produced by the real cut enlarged by the
factor 1 + mu_m still lie in the inherited members' covariance classes"; it calls (M) "ARGUED as a reading, not found
stated with that wording". Row 1299 5.1 keeps it open: "c_e is fixed by the domain margin, a supplier choice; not
decidable from EM". Rule 0a: `(M)` occurs in FINISH.md only in rows 1294 and 1299 as open; no row holds it.

**7.1 What the sources fix (READ).** Sussman and Alpoge's EM manuscript (`YM4/EM/YM4_EM.tex` at c7fef8b21b58, fetched
by URL; 2,001 lines):
- the profiles (EM L333-345): alpha_iota(y) = C_iota y^(-1/2) (log y)^q, delta(y) = A_1 y^(-1/2) (log y)^(p_0) with
  q > p_0 (so the box is the q-box, as in 3.4); EM L471-483: with eps(y) = A_0 y^(-1/2) (log y)^(p_0),
  R_m^2 eps(theta_m)/alpha_0(theta_m) <= (L^2 A_0/C_0) (log theta_m)^(p_0 + 2r - q), "the stronger choice q > p_0 + 2r
  makes this ratio uniformly small above a fixed floor";
- the requirement (EM L647-656): "There is an open real fluctuation ball on which all inherited backgrounds have their
  required covariance. The covariance radii e_j obey e_j' <= L^(2(j'-j)) e_j for j <= j'. ... The earlier backgrounds
  used by the actual step also have to lie in their own covariance classes throughout the retained real cut. The
  creation radius is c_e eps(theta_k) at step k -> k+1, where eps is the supplied real curvature threshold and c_e is
  fixed by the domain margin."
The outline defines the class (SA L5904-5911, (R15)): "The covariance class consists of the W for which these
backgrounds exist, every restriction lies in the required core, and L^(2j) max_p |d U_j(W)(p) - 1| < c min{eps(theta_(j-1)),
eps(theta_j)}", and the terminal covariance radius e_(k+1) = c eps(theta_k) (SA L20724). So the class is a condition
on W alone: it reads the background maps W -> U_j(W), the cores, the constant c and the threshold eps (that is, A_0); it
does not read the cut constant A_1 or the members formed in the run.
The account's order (CA-I Stage 7, L1590-1606; restated L2106-2136): "A_1 > 0, then A_0 upward, with A_0/A_1 >= max{c(d)(1+beta_0) B_3
L^(d+2), c'(d,L) M^2}" ("we assume that the constant A_0 is much larger than A_1", CMP 119), then C_0 upward with floors
by multiples of A_0 and A_1, then C_1 > 2 B_3^2 O(1) M C_0. Write F for that floor ratio; F is fixed before A_1 (it
reads d, beta_0, B_3, L, M only).

**7.2 Lemma MARGIN (PROVED, given the supplier hypothesis (S-unif) below).**
(S-unif): the supplier's requirement of EM L652-653 holds for every admissible choice of the account's letters, that
is, for every A_1 > 0 and A_0 with A_0/A_1 >= F, with the later letters (C_0, C_1, the radii, the floors on theta)
chosen admissibly for that pair. Claim: fix mu_m > 0 and choose A_0/A_1 >= (1 + mu_m) F, and each later letter inside its floors and
ceilings for both pairs (A_1, A_0) and ((1 + mu_m) A_1, A_0) (the maximum of the floors, the minimum of the ceilings). Then (M) holds with relative margin mu_m.
*Proof.* (1) The pair (A_1', A_0) with A_1' = (1 + mu_m) A_1 is admissible: A_0/A_1' >= F, and the later letters were
chosen inside the floors and ceilings of both pairs (finitely many, each a positive function of earlier letters; the
Stage-7 list CA-I L2106-2136 has only floors on C_0, C_1, ceilings on the radii and downward choices of eps^I_0,
eps^I_1, and Stage 8 only ceilings on gamma, L2139-2140; CA-I (H3) L1143-1160 allows this). (2) The cut radius is linear in A_1: delta'(y) = A_1' y^(-1/2) (log y)^(p_0) =
(1 + mu_m) delta(y) (EM L333-345). So the real cut of the A_1'-run is the actual cut enlarged by 1 + mu_m, at every
level. (3) Every history admissible for the actual run is admissible for the A_1'-run with the same A_0: its
fluctuations lie in the smaller cuts, and the curvature threshold eps (which reads A_0 only) is unchanged. (4) By
(S-unif) for the A_1'-run, the earlier backgrounds of every field of the enlarged cut, with that history, lie in the
covariance classes (R15). The class is the same set in both runs, since (R15) reads W, the cores, c and eps only
(7.1). That is (M). QED
(5) No cycle: the only new condition is the floor A_0/A_1 >= (1 + mu_m) F, attached to A_0, which the account's order
treats as free upward (CA-I L1592: "then A_0 upward"); the later letters take finitely many more floors. The domain
margin of EM L471-483 stays uniformly small above a theta-floor for any fixed A_0, since its exponent p_0 + 2r - q is
negative, and that floor is chosen last.

**7.2a Where the requirement itself lives (READ; written 2026-11-20T17:56Z by date -u).** `grep -i` of CA-I for "common covariance",
"covariance radi", "covariance ball", "Euclidean list" and "inherited backgrounds" returns nothing. The requirement is a
hypothesis of EM (EM L647-656, "They do not construct those inputs", abstract L120-122) and of the outline's statement
3.1 ("The substantive construction input says that, for an admitted box and frame prefix through k, E^(k+1) and its
coefficient are formed ...", SA L20718-20724, with the class at SA L20637-20646). So (S-unif) is a property of an input
that the carry already assumes (the supplier of statement 3.1), stated for every admitted box and frame prefix; it is
not proved in the repository or in CA-I.

**7.3 What this does and does not show.** It turns (M) from an ARGUED reading into a consequence of the uniformity
(S-unif) of the supplier's own requirement over the account's admissible letters, with one explicit floor
A_0/A_1 >= (1 + mu_m) F. Row 1294's Proposition H2-cov and row 1278's (H2) are then PROVED GIVEN the readings they
already list (row 1278 (R3)-(R5), row 1267's READ list) and (S-unif); mu_m = 1 is a valid choice. It does not prove the
supplier's requirement itself (that is the account's construction, a premise of the carry like (P1)-(P2)). A checker
should verify (a) that (R15) is the class EM L652-653 reads (EM cites the outline's class; the wording matches SA
L20637-20646, "The backgrounds of fluctuating fields must first lie in a common covariance class on an open real
fluctuation ball"), and (b) that no admissibility condition of the account caps A_1 from below in a way that excludes
A_1' = (1 + mu_m) A_1 (CA-I 4.3 has a floor on the cutoff radius (A_1/A_0) p_0(g), "exceeds the constant of CMP 116
(2.31)", which A_1' meets a fortiori, since the cut grows).

## 8. State of this row after the second step (written 2026-11-20T17:53Z by date -u)

| Item | Before | After | Label | Where |
|---|---|---|---|---|
| (M) margin reading (row 1294 4.2, row 1299 5.1) | ARGUED reading, "not decidable from EM" | follows from the uniformity (S-unif) of the supplier's own requirement over the account's admissible letters, with the one floor A_0/A_1 >= (1 + mu_m) F | PROVED given (S-unif) (Lemma MARGIN) | 7.2 |
| row 1294 Proposition H2-cov, row 1278 (H2) | PROVED GIVEN (M) and readings | PROVED GIVEN the same readings and (S-unif) | PROVED (by 7.2) | 7.3 |
| (E0), (P4), (P3) | see Section 6 | unchanged | | 3-5 |

**Carry inputs still open after this row (pointers):** (P1) (UM1) for the non-gauge potential types (frozen hma L598;
FINISH row 284); (P2) H-M and the carrier identification, which now also holds (P3)'s link half (hma L598-600, in1
L99-108); the supplier's requirement itself (EM L647-656, (S-unif)); row 1268's other hypotheses (P5); the blind-site
expansion (sibling row 1309); the seed.

## 9. A third small step: the unit caveat of (TH) (row 1268 3.5) (READ; written 2026-11-20T17:55Z by date -u)

Row 1268 3.5 (`gap-mini-solve-al-opus.md` L209-214) states (TH) (every threshold in the common chart is at least
a (log theta_k)^(p_0), a = A_1/3^(1/2)) and labels it ARGUED: "a = A_1/3^(1/2) works if the cut units are the
normalized field variables" (row 1268 L325: "the unit conversion between the two frames' normalized fields is my
reading"). The units are fixed by three texts read here:
- CA-I 4.3 L4172-4175: "the cutoff radius (A_1/A_0) p_0(g) ... When g = g_k, this radius is the quantity delta_k/g_k
  of [CMP 119]";
- CMP 119 (OCR L1167): "delta_k = g_k (A_1/A_0) p_0(g_k)", the bound on the approximate fluctuation field
  |V_k(b) (V_k^(0)(b))^(-1) - 1| in unscaled (group) units (OCR L1150-1166);
- the lane's frozen `hma.md` L112: "Fix b = sqrt(theta_j) u as the real integration coordinate ... The box is the
  product of bond balls |b(beta)| < b_j := sqrt(theta_j) delta_j", with g_j = theta_j^(-1/2).
So the cut radius A_1 (log theta)^(p_0) is delta/g, the cut in the field divided by the coupling, that is in the
normalized variables, in both the account's statement and the lane's chart. The caveat of (TH) is met; with row 1268's
own frame comparison ((psi_k/phi_k)^(1/2) >= 3^(-1/2) on |x_k/theta - 1| < 1/4) and the scalar-coordinate factor of
3.4 (b), (TH) moves from ARGUED to READ. Nothing else in row 1268 3.5 changes.

## 10. Labels, what a checker should redo, credits (written 2026-11-20T17:55Z by date -u)

**10.1 Labels.**

| Statement | Label | Where |
|---|---|---|
| The seed (N-phys) and its fixed-coupling forms: no route off the record | ARGUED (judgement), not attacked | 2 |
| Exponents in the account: p_1 = p_0 - 4r - 1 < p_0 (CMP 122a), q >= 3p_0 + 3r + 1 | READ (already on file: b-in-r2 L251, in1 L227) | 3.1, 4.5 |
| Balaban's two cuts and two domains (p_0 cut with the q-radii of CMP 119 (2.28) in the interior; p_1 cut of CMP 122a (1.27) with the domain (3.43) near large fields) | READ | 3.3 |
| Row 1299 4.7's "(equivalently p_1 > p_0)" is false; (E0) holds on the q-box above a threshold on g chosen last | PROVED given the box hypothesis (H-D / H-M domain clause) | 3.4 (a)-(c) |
| CA-I 4.3's variant pairs the p_1 domain (3.43) with the p_0 cut; inconsistent on one variable at small coupling | ARGUED (CMP 116 (I.6.34) not read) | 3.4 (d) |
| (UM14), (UM19), (UM23) in one order | PROVED by citation: in1 Lemma 3 (gate in1 pass 3: "Lemma 3. Holds"), given H-M | 4.3-4.4 |
| (UM26') is one more floor on g_* (shift 1/5) | PROVED | 4.4 (ii) |
| (P3): D4 half = hma Theorem 2; link half = the open carrier identification (hma L598-600) | READ | 5 |
| Lemma MARGIN: (M) with relative margin mu_m from the floor A_0/A_1 >= (1 + mu_m) F | PROVED given (S-unif) | 7.2 |
| Row 1294 Proposition H2-cov and row 1278 (H2) no longer read (M) | PROVED (by 7.2), given their other readings and (S-unif) | 7.3 |
| (TH)'s unit caveat | READ | 9 |

Every PROVED item is by Claude Opus 5.5 and is not yet checked by another model. No numeric run; no subagent.

**10.2 What a checker should redo first.** (1) 3.3: that CMP 119 (2.28)'s q_0, q_1 radii (OCR L832-838) are the radii
on which the regular step's integrand is analytic in the normalized fluctuation, and that (3.43) (page image, journal
p. 276) concerns only the terms with localization domain not inside Lambda_(k+1). (2) 3.4 (b): the factor 2 that
covers |c - 1| between the two frames (row 1268 7.3). (3) 4.4 (ii): monotonicity of S(g_*). (4) Lemma MARGIN 7.2: that
(R15) (SA L5904-5911) is the class EM L647-656 reads; that no condition of the account bounds A_1 from above or reads
A_1 in a way that the enlarged pair violates (I found only the ratio floor CA-I L1594, L2111, L142618 and the
cutoff-radius floor CA-I L4172-4174, which the enlarged cut meets); and step (3), that an all-small history of the
actual run is an admissible history of the enlarged run. (5) 3.4 (d), against CMP 116 (I.6.34) when a copy is available.

**10.3 Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the complete account
CA-I (`theorem_0_complete_account_raw_I.tex`) and the outline `YM4_sketch_500.tex` at 31a47c543775 (the order of
choice, the regular step, the regular-gas chapter (UM1)-(UM30), the covariance class (R15), (RF18)), and the EM
manuscript `YM4/EM/YM4_EM.tex` at c7fef8b21b58 (the running radii, the domain margin, the covariance requirement).
Tadeusz Balaban: CMP 109, 119, 122 (the cuts delta_k and delta'_j, the radii (2.28), the space (3.43), p_1 < p_0). The
lane's IN1 (Codex distillation of a Claude draft; gate by Claude), hma and ci-form notes; rows 1267, 1268, 1278, 1294,
1299 (Claude Opus 5.5, Mac mini workers 2 and 3) for the carry this row edits by evidence only.
