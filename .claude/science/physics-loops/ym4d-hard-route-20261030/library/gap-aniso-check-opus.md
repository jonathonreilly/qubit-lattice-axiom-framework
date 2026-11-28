lead: anthropic/claude-opus-5-5/max laptop-subagent
row: 1069

# gap-aniso-check-opus: line-by-line check of row 1066's file

File under check: `library/gap-aniso-trajectory.md` (row 1066).
Reading it names: `library/prior/gap-aniso-read-luna.md`.

## Plan (at most eight steps; each step appends its result here)

1. Read row 1069 in `FINISH.md`. Record its exact instructions.
2. Read the file under check in full. List its claims and numbered lines.
3. Read the named reading. Record what it supports and what it does not.
4. Check the first block of claims line by line.
5. Check the second block of claims line by line.
6. Check the remaining claims line by line.
7. If a claim needs it, a small numeric guide (refute or guide only).
8. Verdicts per claim, the overall verdict, and the RESULT line.

## Step results

### Step 1. Row 1069 (read 2026-11-16 local; FINISH.md line 1150; checkout ddf283110, branch claude/ym4d-hard-route)

Row 1069 asks for a line-by-line check of `library/gap-aniso-trajectory.md`
(row 1066, by Claude Fable 5.2 medium; same provider as this checker). Items:

- I1. The definitions of step 4: the mixing length X and (MIX), the corrected
  region R_eps, l_par, l_perp, the renormalized anisotropy xi_R, the chain
  (S), (T), (B) and its consumer.
- I2. Lemma BARE and Corollary BARE-1.
- I3. Proposition PERP-BD, and the reading that an isotropic continuum limit
  needs l_perp to infinity.
- I4. The matching of 5.3: (a) the counting; (b) the sheet window with
  z(b) = (beta_M(b)/beta_M)^(3/4) and the cube in beta_T(b) (check the
  exponent against Brezin and Zinn-Justin for n = 4, open copies only);
  (c) Karsch-type coefficients grow like log xi in the 2+2 split, and no
  point of R_eps lies in their domain; (d) the cases; (e) the corrected
  formula; (f) the decision.
- I5. Proposition REN (1)-(3) and the four items of 5.4.
- I6. Lemma PERP and Claim S2 of step 6.
- I7. Proposition U1-BR and the layer-phase control of step 7.
- I8. The correction to row 1053: R must use X, not xi_2 (test K1).
- J1. Is (S-q) the right quantitative form of the seed, or does it assume
  what PERP-BD concludes?
- J2. Does Proposition REN prove that the bridge contains T_JW-lat at one
  coupling?
- J3. Is the verdict 'V2 FAILS as a route by S0' scoped to what is proved?

Use the reading `library/prior/gap-aniso-read-luna.md` (row 1067). Verdicts:
HOLDS, HOLDS AFTER CORRECTION (with the text), FAILS (with the first failing
line). No new attack. Lean-formalizable proofs only; no computer-assisted
proof. End with one RESULT line. Do not read `library/gap-aniso-check-astra.md`
(row 1070, run in parallel).

Sizes: file under check 289 lines, 47073 bytes (last commit 495d7314f);
reading 83 lines, 19477 bytes.

### Step 2. The file under check, read in full (289 lines; L = its line numbers)

Structure: steps 1-3 (L19-69) are orientation and sources; the checked
content is step 4 (L71-87), step 5 (L89-164), step 6 (L166-203), step 7
(L205-245), step 8 (L247-289, report, marks, RESULT).

Claims to check, mapped to row 1069's items:

- I1 (step 4): (MIX) and X >= xi_2 (L76); R_eps (L77); l_par, l_perp (L78);
  xi_R and the bare ratios (L79); the chain (S)/(S-q), (T), (B), consumer
  (L82-85).
- I2: Lemma BARE (L93-94); Corollary BARE-1 and the reconciliation of checks
  1061/1062 (L96-98).
- I3: Proposition PERP-BD (L102-106); the reading (L108); the answer box
  (L110); scope (L112); the transverse-lattice remark (L114).
- I4: 5.3 (a) L120; (b) L122-126, incl. the one-loop line at L126; (c) L128;
  (d) L130-132; (e) L134-138; (f) L140; mark L142.
- I5: (BR-iso), (BR-cont) (L148-150); Proposition REN (L152-156); the four
  mechanism items (L158-162); verdict (L164).
- I6: first failing line (L170-172); Lemma PERP (L174-184); Claim S2 and the
  try (L186-203).
- I7: 7.1 facts (F1)-(F3) (L213); the seed under U(1) (L215); U(1) in the
  corner (L217); layer-phase GUIDE (L219); Proposition U1-BR (L221-223).
- I8: K1 row of the table (L229) and L76.
- J1, J2, J3: L82, L102-112, L152-164, L253, L289.

Cross-references needed for the check (read in steps 4-6, as needed): row
1053 L138, L183, sections 3.2-3.3 ((FACE-SG), (BR-L), V2); `parts/gap.md`
L22-27 ((W), (PHYS-SEED), (SEED)), L139, L152-153; T_JW-lat at
`library/gap-wall-assumptions-opus.md` L485; the kill sheet
`library/gap-invent-selective-max.md` L52-63 (S0); checks 1061 and 1062 on
the items step 3 of the file summarizes.

First reading, to be confirmed line by line in steps 4-6 (not verdicts yet):
the one-loop line at L126 looks wrong in sign; PERP-BD's conclusion looks
like a restatement of the transverse clause of (S-q); Proposition REN (1)
holds only together with (S); the plain report L253 drops the condition
(S-q).

### Step 3. The reading of row 1067 (`library/prior/gap-aniso-read-luna.md`, 83 lines, read in full)

Row 1066 says row 1067 was absent when it ran (L35). It is present now. What
it gives for the items under check (gpt-6-luna high; reading only):

- Karsch 1982 (open scan read by row 1067): SU(2) derivatives 0.11403 and
  -0.06759 at xi = 1; SU(3) 0.20161 and -0.13195; sum b_0 = 11N/(48 pi^2);
  general finite asymmetry computed; the Hamiltonian limit xi -> infinity
  recovers Hasenfratz-Hasenfratz (finite Lambda ratio, about 0.84 for SU(2)).
  Karsch states that the universal anisotropy relations do not hold at strong
  coupling. So: the numbers that row 1066 marked RECALLED (L62) agree with the
  scan as row 1067 read it; the 3 + 1 boundedness as xi grows (L128) is
  supported; the domain statement (weak bare coupling, fixed xi) is
  supported.
- No 2 + 2 anisotropy coefficients were found. Carena et al. 2022 treat a
  temporal anisotropy (one fine direction) in any spatial dimension. This
  agrees with L128 ("I know no published 2 + 2 coefficients").
- Klassen 1998: SU(3), 3 + 1, Monte Carlo calibration; agrees with L63.
- Fu-Nielsen 1984 (metadata and abstract only): layer phase for D >= 5 with
  d = D - 1 Coulomb layers; agrees with L65 and L217 as recalled there.
  Dimopoulos-Farakos-Vrentzos 2006: agrees with L64.
- Five-dimensional SU(2) (Knechtli-Luz-Rago 2011; Del Debbio et al. 2013,
  Monte Carlo): a first-order bulk line, no layer phase seen in the explored
  range. Relevant only to the GUIDE entry K7 (L236).
- Orland 2006, 2007 are 2 + 1 dimensional; Orland 2008 is an effective
  high-energy model that Orland says is not established as QCD. Row 1067 does
  not report a "crossover" statement by Orland. Row 1066 L219 says "Orland
  posits a crossover"; row 1061 (as row 1066 L52 quotes it) says Orland
  proposes, and does not establish, a link to the isotropic theory. I treat
  "posits a crossover" as an unverified paraphrase (precision in step 7).
- Rigorous results: none for the 2 + 2 region (Osterwalder-Seiler 1978 is
  strong coupling, abstract only).
- Nothing in row 1067 on Brezin and Zinn-Justin. That check is done in step 5.

Net: row 1067 contradicts no statement of row 1066. It upgrades the Karsch
numbers and the 3 + 1 Hamiltonian-limit statement from "recalled" to "read
by row 1067 in an open scan".

### Step 4. I1 (step 4 of the file), I2 (Lemma BARE), I3 (PERP-BD), and J1

Sources read for this step: row 1053 L114-139, L181-184, L234-246, L281-286
(`library/gap-wall-vectors-max.md`); check 1061 L281-297, L335-374, L423-431
(`library/gap-wall-vectors-check-astra.md`); check 1062 L120, L171
(`library/gap-wall-vectors-check-opus.md`); `library/gap-wall-assumptions-opus.md`
L485 (T_JW-lat); `parts/gap.md` L21-26, L44-50, L93, L138, L152; row 998
L129-136 (`library/gap-crux-exercise3-max.md`); FINISH rows 978, 1009, 1010.

**I1. Definitions (L73-85).**

- (MIX) and X (L76). The form of (MIX) is fine. But "X(beta): a mixing
  length" does not fix X, and R_eps (L77) needs a function. The only mixing
  bound on file is the reading of rows 1009 and 1010 (OpenAI's pinned-cell
  iteration; uniform over boundary pins and strengths in [0, b]). For O(4),
  row 1009 reads the length as e^(pi b + o(b))
  (`library/prior/gap-o4-pinned-cell-read-opus.md` L359); for O(3), row 1010
  calls its length C e^((4 pi - eta) b) "lossy". So the reading gives X finite,
  with the same leading exponential as xi_2 (which grows like
  beta^(-1/2) e^(pi beta)) and an uncontrolled o(b) in the exponent. It does
  not give X/xi_2 bounded. Step 5.3 (b) of the file uses
  X(beta) = K_2 beta^(-1/2) e^(pi beta): that is the two-loop form of xi_2,
  so 5.3 assumes X/xi_2 bounded. **HOLDS AFTER CORRECTION.** Text for L76-77:
  "X(beta) is the infimum of the lengths for which (MIX) holds, with constants
  of the stated kind. X >= xi_2. The reading of rows 1009-1010 gives X finite,
  at most e^(pi beta + o(beta)); that X/xi_2 is bounded is not known and is
  assumed in 5.3 only. R_eps = { X(beta_M) < infinity, beta_T X(beta_M)^2 <=
  eps, beta_L >= X(beta_M)^2/eps }."
  Reasons for the clause X < infinity: L215 says R_eps for U(1) is empty at
  large beta_M "(it forces beta_T = 0)". With X = infinity the two inequalities
  leave the anchor point (infinity, beta_M, 0) under the convention
  0 . infinity = 0, and the U(1) anchor there has Kosterlitz-Thouless sheets,
  so (S) would claim a false clustering. The clause removes that point.
  X >= xi_2 HOLDS: (MIX) with F, H the components of s at two sites gives
  two-point decay at rate at least 1/X.
  Effect on the verdicts: none of the PROVED items uses the value of X (BARE,
  PERP-BD, PERP, the S2 bound given (MIX), K1). A larger X shrinks R_eps, so
  the negative conclusions of 5.2 and 5.3 hold a fortiori. Only formula (e)
  needs X comparable with xi_2.
- R_eps (L77): HOLDS AFTER the correction above. Remark, no verdict: R_eps has
  no lower bound on beta_M. Where X(beta_M) < 1 it allows beta_T > eps, far
  from the anchor. (S-q) there is a separate claim. No verdict of the file uses
  those points.
- l_par, l_perp (L78): HOLD as definitions (per limit state; l = 0 is possible,
  for example for transverse translates on the face at beta_T = 0).
- xi_R and the bare ratios (L79): HOLD. xi_R is undefined where l_perp = 0
  (the anchor). On (xi^2 beta, beta, beta/xi^2) both bare ratios equal xi. The
  classical factors (beta_L, beta_M, beta_T) proportional to (a_perp^2/a_long^2,
  1, a_long^2/a_perp^2) are row 1053 6.6 for d_perp = 2 as check 1061 L281-297
  corrects it (engineering factors, not a blocking flow).
- The chain (L82-85). (S) HOLDS as the statement of an OPEN target. (S-q): see
  J1. (T) HOLDS as a definition. (B) HOLDS as a description. Consumer (L85)
  HOLDS: "T_JW-lat at one coupling" is the single-cutoff instance of T_JW-lat
  (L485 there defines it for all large j); row 1053 L130 uses the phrase the
  same way for V1. Precision: the torus pointer "parts/gap.md L25-27" is
  L24-26 here, and the record there reads "(SEED) at each beta of the window
  2.3 to 2.6 with a carry to finer cutoffs" (row 998 L133-134). See I5.
- Pointers, no content: L31 cites `parts/gap.md` L139 for Theorem CR and
  L30-31 cite L153 for row 1053's record. Theorem CR is L138 (row 1017's
  record) and row 1053's record is L152, both before and after the lead's
  commit 495d7314f.

**I2. Lemma BARE (L93-94): HOLDS** (beta_M, beta_T > 0; at beta_T = 0,
xi_MT = infinity and both sides hold). Re-derived: beta_T X^2 <= eps iff
beta_M/beta_T >= beta_M X^2/eps iff xi_MT >= (beta_M/eps)^(1/2) X; and
beta_L >= X^2/eps iff xi_LM >= X/(eps beta_M)^(1/2).
**Corollary BARE-1 (L96): HOLDS.** On (xi_0^2 beta, beta, beta/xi_0^2) both
ratios equal xi_0, so membership is xi_0 >= X(beta) max((beta/eps)^(1/2),
(eps beta)^(-1/2)). Check 1061's example (its L355-358: xi^2 = (beta/eps)
e^(2 pi beta), beta >= 1) is this with X = e^(pi beta). Check 1062's
inequality (its L120: xi_2(beta_M) a_long <= sqrt(eps/beta_M) a_perp on the
classical trajectory) is the same inequality with a_perp/a_long read as the
bare ratio. **The reconciliation L98 HOLDS.**

**I3. Proposition PERP-BD (L102-106): HOLDS as an implication.** Given (S-q),
every gauge-invariant local observable has transverse rate log(1/(C eps))
with constants C_F C_H, so 1/l_perp >= log(1/(C eps)) by L78. (a)-(c) follow
from xi_R = l_par/l_perp. (S-q)'s first clause (l_par <= X/c) is not used.
- The reading (L108): HOLDS as the meaning of an isotropic continuum limit,
  with one precision: the limit must be non-trivial (a non-zero physical mass
  m in every direction); then l_par = 1/(m a_long) and l_perp = 1/(m a_perp)
  both diverge.
- Answer box (L110): HOLDS AFTER CORRECTION; the text is under J1.
- Scope (L112). The sentence "If (S-q) is false, V2 has no seed in R_eps and
  the question is empty" **FAILS** as written: (S-q) false does not make (S)
  false, and the next sentence of L112 treats exactly that case. Corrected:
  "If (S) is false, V2 has no seed in R_eps. If (S) holds and (S-q) fails, the
  proposition is not available, and 5.3 is the argument on file." The sentence
  "Support for the form (C eps)^t: Lemma PERP ..." HOLDS AFTER CORRECTION:
  "Lemma PERP gives the power of beta_T on each finite box, not the factor
  per step and not uniformity; Claim S2 with (MIX) gives the factor
  (beta_T X^2)^2 at transverse distance one."
- L114 (ARGUED): HOLDS as a remark. "Orland's weakly coupled regime" agrees
  with row 1067's reading of Orland 2006 (decoupled chiral models at
  e' -> 0, both couplings weak, 2 + 1 dimensions).

**J1. Is (S-q) the right quantitative form, or does it assume PERP-BD's
conclusion?** It assumes it. The second clause of (S-q) (L82) is, by the
definition L78, the bound l_perp <= 1/log(1/(C eps)), which is PERP-BD's
conclusion; PERP-BD restates it and adds no evidence. (S-q) is strictly
stronger than the seed of row 1053 L138, which states no rate. It is the
natural form for a convergent expansion about the anchor in the activity
beta_T X^2: it agrees with the order count of Lemma PERP and with Claim S2's
(beta_T X^2)^2 at transverse distance one (both checked in step 6). Nothing
shows that every proof of (S) must give it. So the mark "PROVED GIVEN (S-q)"
is correct as logic, but it is not support for the answer.
Corrected text for L110 (and the matching clause of L253 and L289): "Answer
to the row's first question: OPEN as a theorem, ARGUED. (S-q) states the
transverse rate, and Proposition PERP-BD reads it off through the definition
of l_perp. Given (S-q), R_eps contains no family ... [as written]. Without
(S-q), the evidence is the matching of 5.3 (ARGUED: R_eps lies in case (i));
Lemma BARE alone bounds only the bare ratio."

### Step 5. I4: the matching of 5.3 (L116-142), with the exponent check

**(a) Counting (L120): HOLDS** as a count of sites and plaquettes, with the
classical (smooth-field) factors b^2 beta_T, beta_L/b^2, beta_M. Re-derived:
a blocked T term sums b^2 sites; a blocked L plaquette has (1 - x) about b^4
times larger and there are b^2 times fewer; an M plaquette gains b^2 in
(1 - x) and loses b^2 in number. "Exact" applies to the count only; as check
1061 L281-297 says, these are engineering factors, not a blocking flow. The
file says so ("classical factors").

**(b) The sheet window (L122-126).**
- Running stiffness (L123): HOLDS (PERTURBATIVE, as marked). From
  X(beta_M(b)) = X(beta_M)/b and X = K_2 beta^(-1/2) e^(pi beta)(1 + o(1)),
  taking logarithms gives beta_M(b) = beta_M - (1/pi) log b - (1/(2 pi))
  log(beta_M/beta_M(b)) + o(1), valid while beta_M(b) is large. Precision
  from I1: this uses X comparable with xi_2.
- Field renormalization (L124): HOLDS. z(b) = (beta_M(b)/beta_M)^(3/4) and
  z = 1 - (3/(4 pi beta_M)) log b at first order.
  **Exponent check, open copies only.** Brezin and Zinn-Justin 1976 (Phys. Rev.
  B 14, 3110; Phys. Rev. D 14, 2615 with Le Guillou; Phys. Rev. Lett. 36, 691):
  NOT READ. INSPIRE lists no open document for any of them (queries saved in
  `/tmp/row1069-bzj-c/`), and they predate arXiv. Checked instead against the
  open TeX source of S. Caracciolo and A. Pelissetto, "Four-loop perturbative
  expansion for the lattice N-vector model", arXiv:hep-lat/9510015
  (`/tmp/row1069-bzj-b/`, read with `python3 -I`): the universal coefficients
  w_0 = (N-2)/(2 pi), w_1 = (N-2)/(2 pi)^2, gamma_0 = (N-1)/(2 pi) (their TeX
  L253-257, with citations to Brezin et al. among others); the correlation
  length xi = C_xi ((N-2)/(2 pi beta))^(1/(N-2)) e^(2 pi beta/(N-2)) (1 + ...)
  (L501-505); and chi_V/xi^2 = R_V (2 pi beta/(N-2))^(-(N-1)/(N-2)) (1 + ...)
  (L609-612). For N = 4: xi proportional to beta^(-1/2) e^(pi beta), the file's
  two-loop form; and chi/xi^2 proportional to beta^(-3/2), so the two-point
  function at the scale xi is suppressed by beta^(-(N-1)/(N-2)) = beta^(-3/2),
  that is G(r) proportional to (beta(r)/beta)^(gamma_0/w_0) with
  gamma_0/w_0 = 3/2. Second derivation (spin waves, mine): with action
  beta sum s.s', G(r) = 1 - (n-1)/(2 pi beta) log r + ..., and
  beta(r) = beta - ((n-2)/(2 pi)) log r, so (beta(r)/beta)^((n-1)/(n-2)) agrees
  at first order. Normalization: the sheet action of Lemma ANCH is
  beta_M sum s.s' (row 1053 L236), the same as in the source. **The exponent
  (n-1)/(n-2) = 3/2 for G, hence 3/4 for z, HOLDS.** (One more check of the
  convention: in d = 2 + eps these coefficients give eta = gamma_0 t* - eps =
  eps/(N-2), the standard result.)
- The cube (L125): HOLDS (ARGUED, first order in beta_T with independent
  sheets): the blocked T term is b^2 beta_T times E[product of four fields |
  blocks] = z^4 times the blocked plaquette, and z^4 = (beta_M(b)/beta_M)^3.
  So "the dropped factor is the fourth power of the sheet field
  renormalization" (L289) HOLDS.
- "This factor is what L183 dropped" (L126): HOLDS (row 1053 L183 sets the sheet
  coupling at a_perp with no field factor; check 1061 L337-374 names that line).
- **The one-loop line (L126): FAILS as written (sign).** From the file's own
  (b) and (d): K_T b_*^2 beta_T (beta_*/beta_M)^3 = beta_*, so
  xi_MT^2 = beta_M/beta_T = K_T b_*^2 (beta_*/beta_M)^2, that is
  xi_MT = K_T^(1/2) b_* beta_*/beta_M. With xi_R = K_R b_* and
  beta_*/beta_M = 1 - (1/(pi beta)) log b_* + ..., this is
  xi_MT = xi_R (1 - (1/(pi beta)) log xi_R + ...) for K_T = K_R^2 (classical
  normalization). The printed line has the opposite sign, and its size 3/2 is
  that of the factor z^(-2) alone; the running of beta_M(b) in the isotropy
  condition turns 3/2 into 1. Corrected text: "At one loop it reads
  xi_R = xi_MT (1 + (1/(pi beta)) log xi_R + ...): the bare ratio lies below
  the renormalized one (the factor z^(-2) gives +3/(2 pi beta), the running of
  beta_M(b) gives -1/(2 pi beta)). The coefficient grows like log xi_R." The
  next sentence and every later use (5.3 (c): growth like log xi; (e): the
  factor (beta_M/beta_*)^3 >= 1 makes beta_T X^2 larger) are unaffected; (e)
  is consistent with the corrected sign, not with the printed one. GUIDE run
  (`/tmp/row1069-scripts/sign_guide.py`, pure Python, no verdict rests on
  it): solving the file's relations exactly at beta_M = 200, b_* = 10^3 gives
  xi_MT/xi_R = 0.98900, against 0.98901 from the corrected line and 1.01649
  from the printed one.

**(c) Karsch's domain (L128): HOLDS (PERTURBATIVE/ARGUED, as marked).**
- 3 + 1 split: Karsch's coefficients are one-loop, weak bare coupling, fixed
  xi; the Hamiltonian limit xi -> infinity is finite (Hasenfratz and
  Hasenfratz). Row 1067 read both in Karsch's open scan, so these are no
  longer only recalled. Karsch also says the universal relations fail at
  strong coupling (row 1067 L23).
- 2 + 2 split: the growth like log xi follows from (b) (the stiffness runs by
  (1/pi) log b over the window), with expansion parameter (1/(pi beta)) log xi,
  which agrees with the corrected one-loop line above. ARGUED; no published
  2 + 2 coefficients are known to row 1067 either.
- "No point of R_eps lies in the domain": HOLDS (ARGUED). By Lemma BARE and
  X >= xi_2 = K_2 beta^(-1/2) e^(pi beta)(1 + o(1)): log xi_MT >= pi beta_M +
  (1/2) log(1/eps) + log K_2 + o(1), so (1/(pi beta)) log xi_MT >= 1 - o(1);
  the same holds for xi_LM up to a log beta term. This needs only X >= xi_2,
  not X comparable with xi_2.

**(d) The two cases (L130-132): HOLD (ARGUED).** Case (i): at b of order X,
beta_T(b) is of order K_T beta_T X^2 beta_M^(-3) <= K_T eps beta_M^(-3), and
beta_L(b) = beta_L/b^2 >= 1/eps, so R_eps lies in case (i); the remark that
the expected seed region is larger by beta_M^3 HOLDS as ARGUED. Case (ii):
xi_R = K_R b_*; the four-dimensional correlation length exp((3 pi^2/11)
beta_*) is non-perturbative. Check of 3 pi^2/11: for SU(2), b_0 = 11/(24 pi^2)
and beta = 4/g^2, so 1/(2 b_0 g^2) = (3 pi^2/11) beta. HOLDS.

**(e) The corrected formula (L134-138): HOLDS (ARGUED).** Re-derived:
beta_T X(beta_M)^2 = beta_T b_*^2 X(beta_*)^2 = (1/K_T) beta_* (beta_M/beta_*)^3
X(beta_*)^2 = (K_2^2/K_T) (beta_M/beta_*)^3 e^(2 pi beta_*) (1 + o(1)), so
K = K_2^2/K_T; and beta_M = beta_* + (1/pi) log b_* + (1/(2 pi))
log(beta_M/beta_*) + o(1). Precisions: "+ lower order" contains the O(1) term
-(1/pi) log K_R, which is not lower order when xi_R is fixed; write "+ O(1)".
The factor (beta_M/beta_*)^3 >= 1 needs b_* >= 1 and X increasing (true for
the asymptotic form). The comparison with row 1053 ((4/g^2) e^(8 pi/g^2) =
beta_* e^(2 pi beta_*) at g^2 = 4/beta_*) HOLDS.

**(f) The decision (L140): HOLDS AFTER CORRECTION.** On a fixed-xi_R family
with beta_* -> infinity, beta_T X(beta_M)^2 >= K e^(2 pi beta_*) (1 + o(1)) ->
infinity, so the family leaves R_eps; that part holds whatever the constants
are. The clause "that is at beta_* of order one or below, whatever the unknown
constants are" does not: the threshold (1/(2 pi)) log(eps/K) depends on the
unknown K, and (e) is an asymptotic formula, not valid at beta_* of order one.
Corrected text: "So it lies outside R_eps for every beta_* above a threshold
of the form (1/(2 pi)) log(eps/K) + o(1). Since beta_* -> infinity on the
family, it leaves R_eps, whatever the unknown constants are." The lists of
perturbative and non-perturbative steps HOLD.

**Mark for task 2 (L142): HOLDS**, read with J1 (the "PROVED GIVEN (S-q)"
half restates (S-q)). Its last sentence ("its conclusion that a trajectory
must leave R holds on these two grounds") HOLDS with the same reading.

### Step 6. I5 (the bridge, Proposition REN, 5.4), J2, and I6 (step 6 of the file)

**I5. The two bridge forms (L148-150).** (BR-iso)_beta: HOLDS as a statement.
Precision: "For one point P_0 in R_eps" is idle; the hypothesis is (S) on all
of R_eps, and P_0 plays no role. Drop it, or make the hypothesis "the limit
state at P_0 clusters". The window 2.3 to 2.6 agrees with `parts/gap.md`
L24-25. (BR-cont)_k: HOLDS as a statement.

**Proposition REN (L152-156).**
- (1), first two sentences: **HOLDS.** The conclusion of (BR-iso)_beta is
  clustering of every limit state at (beta, beta, beta) on gauge-invariant
  local observables. The single-cutoff instance of T_JW-lat (L485 of
  `library/gap-wall-assumptions-opus.md`) asks for clustering in the sense of
  A2 of every infinite-volume limit state (torus limits or DLR states), at some
  rate, on a total set of local observables, constants depending on the
  observable only; gauge-invariant local observables are such a set.
  Precision: "every limit state" at L148 should read "every infinite-volume
  limit state (torus limits and DLR states)", as at L485; step 4 L74 names
  only boxes and tori. Given (S), the implication (BR-iso)_beta is equivalent
  to its conclusion: elementary logic.
- (1), torus clause: **HOLDS AFTER CORRECTION.** "In torus form" can only mean
  a torus version of the bridge whose conclusion is (SEED) at beta; then the
  clause is a definition. But the record of the sufficient form is "(SEED) at
  each beta of the window 2.3 to 2.6 with a carry to finer cutoffs"
  (`parts/gap.md` L24-26; row 998 L133-134), and row 978 found no carrier
  from one coupling (its RESULT: the carry is (NOCRIT) plus an
  asymptotic-freedom climb, open). Corrected text: "In torus form with the
  flux sectors, the conclusion is the fixed-coupling (SEED) at beta. The
  torus form at each beta of the window 2.3 to 2.6, with a carry to finer
  cutoffs (open; row 978 found none), is the sufficient form of (PHYS-SEED)
  on record, hence of (W)."
- (2): **HOLDS** (definitions).
- (3): the implication **HOLDS**, and the path proof is right. Precision: (BR-L)
  of row 1053 L128 is "a lower bound for the clustering rate of (beta_L,
  beta, beta), uniform in beta_L in [beta, infinity]"; at beta_L = beta it
  already gives clustering at (beta, beta, beta). So (BR-L) alone gives
  (BR-iso)_beta, and (FACE-SG) is not needed. The last sentence, "V2 adds the
  seeded corner to V1 and removes none of V1's open statements", is **not
  proved** and is misleading: (3) shows that V1's pair implies V2's bridge,
  not the converse. Given (S), V2's bridge is clustering at one point, while
  (BR-L) asks for a rate uniform in beta_L. Corrected text: "(BR-L) alone
  gives (BR-iso)_beta. The converse is not shown: given (S), (BR-iso)_beta is
  clustering at one point, which is weaker than (BR-L)'s uniform rate. Both
  contain the target at one coupling." The S0 verdict does not change.

**The four mechanism items (L158-162).**
- Item 1 (soft bridge, U(1)): HOLDS, scoped to the statement B_soft of L221
  (checked in step 7).
- Item 2 (Ginibre): HOLDS as a remark, not used. Precision: Ginibre's
  inequality for U(1) makes Wilson-loop expectations non-decreasing in each
  coupling; the points of R_eps and (beta, beta, beta) are not ordered
  coordinatewise (beta_L goes down, beta_T goes up along the bridge), so the
  inequality compares them in neither direction. "It bounds the tension at the
  isotropic point from above" holds only against points with all couplings
  smaller, and none of those is in R_eps.
- Item 3 (blocking flow): HOLDS AFTER CORRECTION. Lead rule W2 (`parts/gap.md`
  L93) defines (K-flow) as "a statement that reads the first-passage data of
  Wilson SU(2)". The bridge starts from the seed (S) in R_eps, not from
  first-passage data. Also "to l_perp to infinity" fits (BR-cont), while
  (BR-iso)_beta ends at a fixed coupling with finite l_perp. Corrected text:
  "The bridge runs against it, from l_perp below 1 to the band (and, for
  (BR-cont), to l_perp to infinity), through the scales where the blocked
  couplings are of order one. It is a transport of the flow kind, but it
  starts from (S), not from first-passage data, so it is not (K-flow) in the
  sense of W2. V2 supplies no step for it." The direction claim ("inside R_eps
  it runs toward the anchor") is the classical transverse rescaling of row
  1053 6.6 as check 1061 L281-297 corrects it; ARGUED.
- Item 4: HOLDS.

**Verdict for task 3 (L164).** First sentence: HOLDS AFTER CORRECTION; insert
"given (S)" after "contains", and use the torus text above. "I did not show
that it contains (LIOU)": HOLDS. The S0 sentence: see J3 in step 8.

**J2. Does Proposition REN prove that the bridge contains T_JW-lat at one
coupling?** Yes, in this exact sense: given (S), (BR-iso)_beta is equivalent
to the single-cutoff instance of T_JW-lat at beta. Without (S) it is weaker
(it holds vacuously if (S) fails). Every use of V2 must prove (S), so the
chain (S) and (BR-iso)_beta is equivalent to (S) and T_JW-lat at beta; that is
the containment the S0 test needs. The proof is by definition. Its content is
the choice of consumer: V2's consumer is the target at one coupling (L85),
once no continuum limit is available inside R_eps. That last step rests on
5.2 (given (S-q)) or 5.3 (ARGUED); see J3. The RESULT line (L289) should say
"given the seed (S)" where it says the bridge contains T_JW-lat.

**I6. 6.1 (L170-172).** "There is none (5.2, 5.3)": HOLDS AFTER CORRECTION:
"There is none given (S-q) (5.2), and none by the matching of 5.3 (ARGUED)."
The pointer HOLDS: row 1053 L138 is V2's statement, and its consumer clause is
"a continuum limit taken inside R".

**Lemma PERP (L174-184): HOLDS.** Checked line by line.
- The tilt: on a finite box with free boundary, the face model is the anchor
  E_0 tilted by exp(beta_T X_T) (Lemmas FACE-LIM and ANCH of row 1053).
- Analyticity: E_0[F e^(t X_T)] is entire in t and the normalizer is positive.
- The cumulant identity: with Lambda(s, t) = log E_0[exp(sum s_i F_i + t X_T)],
  kappa_t(F_1, ..., F_n) = d_(s_1) ... d_(s_n) Lambda at s = 0, and d_t
  commutes with the d_(s_i), which adds the entry X_T. Correct.
- The closure: C = cl_P(A) is closed under P, so each p in P has its boundary
  inside C or disjoint from C; |P| <= k < d(A, B) gives C disjoint from B
  (repeated plaquettes make |P| smaller, which is fine). F is in the first
  group and H in the second, so both groups are non-empty, and the two groups
  are functions of disjoint sets of sheets, independent under E_0. A joint
  cumulant of two independent non-empty groups vanishes. QED holds.
- Remarks (1)-(3) HOLD. The Lean form named is plausible.

**Claim S2 (L188-196): HOLDS; the constant 1/16 HOLDS.**
- First order: x_p(u) is odd under Phi_3 -> -Phi_3 on the whole sheet, which
  preserves the sheet measure, and F, H do not depend on sheet 3; every term
  of kappa_0(F, H, x_p(u)) contains x_p(u) once, so it vanishes. For q not p:
  the term vanishes by the term-wise argument in Lemma PERP's proof with
  P = {q}, since no other plaquette contains both links 1 and 2.
- Second order: a pair (p, q), q not p, vanishes by flipping a sheet of a link
  of q outside the boundary of p (it exists: two plaquettes share at most one
  link; that link is not 1 or 2, so F, H, x_p do not depend on it). A pair
  (q, q') without p vanishes by the same term-wise argument: the only other
  plaquettes with link 1 or link 2 in their boundary are q_0 (across link 1)
  and q'_0 (across link 2); links 1 and 2 are consecutive in p, and q_0, q'_0
  share only a vertex, so cl_{q, q'}({1}) does not meet {2}. Precision: the
  file says "by Lemma PERP"; the statement of Lemma PERP with A = {1},
  B = {2} (d = 1) gives only order zero. It is the term-wise argument of its
  proof that applies. Cite it so.
- kappa_0(F, H, x, x') = E_0[F~ H~ x x']: all first moments of x vanish,
  Cov_0(F, H) = 0 (sheets 1, 2 independent), and E_0[F~ x] = 0 etc. by the
  sheet-3 flip; for centred variables the four-cumulant is E[ABCD] minus the
  three pair products, and all pair products vanish. Correct.
- E over sheets 3, 4: E_0[N(u) (x) N(u')] commutes with every L_g R_h, and
  these form SO(4), which is irreducible on R^4, so it is (c/4) I. c =
  (1/2) tr(G I . G I) = G^2 by Schur's lemma for each sheet. Then
  E_(3,4)[x x'] = (G^2/4) <M(u), M(u')>, and <M(u), M(u')> =
  (1/2) tr(A_1 A_2) with A_1 = Phi_1(u')^(-1) Phi_1(u), A_2 =
  Phi_2(u) Phi_2(u')^(-1) (cyclicity). Independence of sheets 1, 2 gives
  kappa_0 = (G^2/8) tr(<F; A_1>_0 <H; A_2>_0), and c_2 = (1/2) sum kappa_0, so
  1/16. Correct.

**The try (L198-201).**
- First bullet: the bound (1/2) sup|F| sup|H| sum G^2 HOLDS (operator norm of
  <F; A> at most 2 sup|F|; |tr(XY)| <= 2 ||X|| ||Y||; 1/16 . 2 . 2 . 2 = 1/2).
  "The best bound" and "two-point decay does not bound even the second order
  uniformly" overstate: this is the bound the estimate gives, not a proof that
  no better bound exists. Corrected text: "So this estimate, which uses
  two-point decay only, does not bound the second order uniformly in the
  box." HOLDS AFTER CORRECTION.
- Second bullet: HOLDS. (MIX) applied to F and each entry of A_1 (support
  {u, u'}, sup norm 1) gives |<F; A_1>| <= C_F e^(-d_F/X). Then
  sum_u e^(-d_F/X) <= 2 sum_v e^(-dist(supp F, v)/X) <= C |supp F| (1 + X)^2,
  and sum_r G(r)^2 <= C (1 + X)^2 by the two-point decay that (MIX) itself
  gives. So |c_2| <= C'_F C'_H (1 + X)^4: the second order is at most a
  constant times (beta_T X^2)^2 for X >= 1, uniformly in the box. The sums are
  elementary; **PROVED GIVEN (MIX)** is the right mark. The file marks it
  "ARGUED at that level" at L203 and "PROVED GIVEN (MIX)" at L268; use one
  mark.
- The parenthetical on sum_r G(r)^2 of order X^2 beta_M^(-3): HOLDS as
  ARGUED (G^2 is proportional to (beta(r)/beta)^3 by step 5, and the sum is
  dominated by r of order X). It accounts for the z^4 of sheets 3, 4 only;
  the estimate of <F; A_1> still uses C_F.
- Third bullet (first open line): HOLDS as a statement of what is open.
- Mark (L203): HOLDS, except the mark noted above.

### Step 7. I7 (compact U(1), the layer phase), I8 (test K1), the table, and steps 8.1-8.4 of the file

(Plan change: the small numeric guide of plan step 7 was run inside step 5,
for the one-loop sign. This step takes the remaining items.)

**I7. Facts (F1)-(F3) (L213).**
- (F1): HOLDS. The U(1) face model is a spin system of angles theta_l(u),
  compact single-spin space, finite-range bounded interactions (four M terms
  of strength beta_M and two T plaquettes of strength beta_T per variable).
  Dobrushin's interdependence sum is bounded by a constant times
  (beta_M + beta_T), below 1 for small couplings, which gives a unique Gibbs
  state with exponential decay of correlations. A correct use of a recalled
  standard theorem (Dobrushin).
- (F2): HOLDS as cited (Frohlich and Spencer 1981, through row 1007 B(3)).
- (F3): HOLDS AFTER CORRECTION (scope). The lane holds the Coulomb phase as
  "THM, published, recalled (Guth; Frohlich and Spencer); in the lane for
  Villain at beta >= 2^14" (`parts/gap.md` L223; kill sheet K5). For the
  Wilson form it is recalled only. A refutation at the lane's theorem grade
  should use the Villain form at both points: (F1) holds for the Villain
  weight at small couplings too, because its angle dependence is of order
  e^(-1/(2 beta)) there. Text: "(F3) ... theorem-grade in the lane for the
  Villain form at beta >= 2^14; for the Wilson form recalled. Proposition
  U1-BR is stated for the Villain form."

**The seed under U(1) (L215): HOLDS AFTER CORRECTION.** "R_eps for U(1) is
empty there (it forces beta_T = 0)" holds only with the clause X < infinity
of step 4 (I1); otherwise the U(1) anchor point (infinity, beta_M, 0) is left
in R_eps, and it does not cluster. "So no step of (S) gives U(1) a gap where
it has none": a pass on the face by (F1); at finite beta_L in R_eps(U(1)) no
theorem is cited (a pass is no support in any case). "A theorem-grade
difference (F2 against the posted O(4) theorems)": too strong. The U(1) side
(X infinite) is a theorem. The SU(2) side (X finite at every beta) is GIVEN as
a reading only (rows 1009, 1010; the posted O(n) text disclaims mixing, row
1053 L241). Text: "a difference that is a theorem on the U(1) side and a
reading on the SU(2) side." Lemma PERP and Claim S2 hold for U(1): HOLDS.

**U(1) in the SU(2) corner (L217): HOLDS (ARGUED).** Gaussian level, beta_T =
0: <e^(i theta(0)) e^(-i theta(r))> = r^(-1/(2 pi beta)), so e^(i theta) has
scaling dimension 1/(4 pi beta); four independent sheets give 1/(pi beta_M)
< 2, a relevant perturbation for beta_M > 1/(2 pi). This is consistent with
row 1053 6.6 (its exponent 1/(4 pi beta_M) is the power of the charged
correlation at beta_T > 0, where only the gradient half contributes; a
different quantity). The flow to four-dimensional Gaussian behaviour is
ARGUED. The agreement with Fu and Nielsen's criterion holds as far as row
1067 reads them (D >= 5, d = D - 1 Coulomb layers; abstract and metadata
only). The 4 + 1 numerics (Dimopoulos, Farakos and Vrentzos): row 1067 read
the full copy; consistent.

**The layer-phase GUIDE (L219): HOLDS AFTER CORRECTION.**
- "The bridge contains it" (the claim of no transition between the corner and
  the isotropic point) is wrong as logic. (BR-iso) does not exclude a
  transition between two clustering regimes. The converse direction would need
  a theorem that a path without non-analyticity carries clustering, and none
  is on file. Text: "A proof of the bridge along a path must deal with this
  region. The bridge does not imply the absence of a transition, and no
  theorem on file derives the bridge from it."
- "(Orland posits a crossover)": unverified paraphrase. Row 1061 (as L52
  quotes it) says Orland proposes, and does not establish, a link to the
  isotropic theory; row 1067 reports no crossover statement. Text: "(Orland
  proposes a link to the isotropic theory and does not establish it; check
  1061)."
- "It is false in an abelian relative": HOLDS as GUIDE (numerical, 4 + 1 U(1)).

**Proposition U1-BR (L221-223): HOLDS**, with the (F3) scope above (Villain
form at both points for the lane's theorem grade; Wilson form given the
recalled theorem). B_soft as written quantifies over compact groups, so one
group refutes it. The consequence ("a proof of (BR-iso) must use the group
between the two points; it cannot be continuity, analyticity on a
neighbourhood, or any property that U(1) shares") HOLDS as kill-test logic,
read as: no argument whose steps and hypotheses also hold for U(1). It
refutes B_soft, not (BR-iso) itself; the file says "its soft form" at L289,
which is the right scope.

**I8. The correction to row 1053 (L76, K1 row L229, mark L273): HOLDS
(ARGUED), with a precision on the reason.** For the product group SU(2) x
U(1) (product Wilson action, product model), a region defined by the SU(2)
sheet's two-point length contains points with large beta_M and small beta_T,
where the U(1) factor is expected gapless (ARGUED in 7.1; theorem-grade only
for the charged two-point function at beta_T = 0). So a hypothesis that reads
one factor fails the kill sheet's K1 condition (`library/gap-invent-
selective-max.md` L54: the conclusion step must read the whole state space).
With X of the whole sheet, X is infinite for the product, and the hypothesis
is void. Precision: K1 by itself asks for a length of the whole sheet; the
two-point length of the whole sheet (charged U(1) field included) would also
be infinite for the product. What asks for a mixing length rather than a
two-point length is the try of Claim S2 (L199-200: the second order needs
decay of <F; Phi(u')^(-1) Phi(u)>). Text for L76: "R must be written with a
mixing length of the whole sheet: test K1 asks for the whole sheet, and the
second-order try (6.3) asks for mixing, not two-point decay." For SU(2) alone
the change only rescales eps if X/xi_2 is bounded (expected, not known); with
the reading's length e^(pi beta + o(beta)) it rescales R by a factor
e^(o(beta)) in X^2.

**The table 7.2 (L227-241): HOLDS** row by row at the grade each row states
(K2, K8 not engaged; K3 pass in the stated form; K4 pass ARGUED, the class is
inside R_eps when X is monotone, as for the reading's uniform length; K6 void
given X < infinity; Pin(2) and K7 GUIDE, and K7 agrees with row 1067's
five-dimensional SU(2) numerics; CEN+, WN pass ARGUED; K9 rows as in J2, J3).
Precision on K1: as in I8. The "Numeric run" line (L243): HOLDS;
`scripts/lab_ops.py` is absent in this checkout (checked). The kill-pass
verdict (L245): HOLDS.

**Steps 8.1-8.4 of the file.**
- 8.1 plain report (L253): HOLDS AFTER CORRECTION. "Inside R the transverse
  correlation length stays below one transverse lattice unit" drops the
  condition. Text: "Given the quantitative seed (S-q), which states it, the
  transverse correlation length inside R stays below one transverse lattice
  unit; the matching argues the same without it." "That bridge contains the
  target at one coupling": add "given the seed". "Compact U(1) refutes every
  mechanism that does not use the group": add "(every mechanism whose steps
  and hypotheses also hold for U(1))". The rest HOLDS.
- 8.2 marks (L257-273): HOLD except: PERP-BD, read with J1; the matching row's
  "leaves R_eps at beta_* of order one" (correct as in 5.3 (f)); Proposition
  REN, "given (S)" for the containment and the torus text of I5; the uniform
  second-order bound, one mark (PROVED GIVEN (MIX)); V2's FAILS row, the scope
  of J3.
- 8.3 hand-over (L277-281): HOLDS. The four items it asks a checker to take
  first are done here (Lemma PERP, the constant 1/16, the exponent 3 and the
  two-loop form, Dobrushin for (F1)); all hold, with the source precision of
  step 5 (Brezin and Zinn-Justin not read; Caracciolo and Pelissetto read).
- 8.4 (L285): HOLDS.
- Credits (L287): HOLD.

### Step 8. J3, the verdicts, and the RESULT

**J3. Is "V2 FAILS as a route by S0" scoped to what is proved?** Partly. The
verdict has three parts:
1. Given (S), V2's bridge is the target at one coupling (Proposition REN (1),
   PROVED from the definitions; J2).
2. V2 needs a bridge, because R_eps holds no continuum limit: PROVED only
   GIVEN (S-q), which states it (J1), and ARGUED by the matching of 5.3.
3. No cheaper mechanism: ARGUED over four items; the soft form is refuted by
   compact U(1) given the cited theorems.
L164 names parts 1 and 3 but not part 2, and the RESULT (L289) puts "FAILS"
before its conditions. **HOLDS AFTER CORRECTION.** Text for L164: "So V2
FAILS as a route by S0, as V1 did at (BR-L), in this sense: given the seed
(S), its bridge is the target at one coupling (Proposition REN, PROVED from
the definitions); a bridge is needed because R_eps holds no continuum limit,
which is PROVED GIVEN (S-q) and ARGUED by 5.3; the absence of a cheaper
mechanism is ARGUED and scoped to the four items above. This is a verdict on
V2 as proposed. It is not a statement about every use of anisotropic
lattices." The last two sentences are the file's own and HOLD.

**Verdicts by item.**

| Item | Verdict | First failing line or correction (text in the step named) |
|---|---|---|
| I1 step-4 definitions | HOLDS AFTER CORRECTION | L76-77: X must be fixed (the infimal mixing length) and R_eps must require X < infinity; 5.3 assumes X/xi_2 bounded, while the reading gives only X <= e^(pi beta + o(beta)) (step 4) |
| I2 Lemma BARE, Corollary BARE-1, reconciliation L98 | HOLDS | none |
| I3 PERP-BD (implication), reading L108 | HOLDS | the reading needs a non-trivial limit (precision) |
| I3 scope paragraph L112 | HOLDS AFTER CORRECTION | first failing line L112, "If (S-q) is false, V2 has no seed in R_eps" (step 4) |
| I4 (a) counting | HOLDS | classical count; "exact" is about the count |
| I4 (b) window, z, the cube | HOLDS AFTER CORRECTION | exponents hold (checked against Caracciolo-Pelissetto; Brezin-Zinn-Justin not read); first failing line L126, the one-loop sign (step 5) |
| I4 (c) Karsch's domain | HOLDS (PERTURBATIVE/ARGUED) | none; Karsch's numbers and 3 + 1 statement now read by row 1067 |
| I4 (d) the two cases | HOLDS (ARGUED) | none |
| I4 (e) corrected formula | HOLDS (ARGUED) | "lower order" contains an O(1) term (step 5) |
| I4 (f) decision | HOLDS AFTER CORRECTION | L140, "at beta_* of order one or below, whatever the unknown constants are" (step 5) |
| I5 (BR-iso), (BR-cont) | HOLDS | "every limit state" to read as at L485; "one point P_0" idle |
| I5 REN (1) | HOLDS given (S); torus clause HOLDS AFTER CORRECTION | the record's sufficient form is (SEED) at each beta of the window with an open carry (step 6) |
| I5 REN (2) | HOLDS | none |
| I5 REN (3) | implication HOLDS; last sentence not proved | L155, "V2 ... removes none of V1's open statements"; (BR-L) alone gives the bridge (step 6) |
| I5 four items, L164 | HOLDS AFTER CORRECTION | item 3: not (K-flow) in W2's sense; L164: J3 text |
| I6 6.1 | HOLDS AFTER CORRECTION | L170, "There is none (5.2, 5.3)": scope |
| I6 Lemma PERP | HOLDS | none |
| I6 Claim S2, constant 1/16 | HOLDS | cite the term-wise argument of PERP's proof, not its statement |
| I6 the try | HOLDS AFTER CORRECTION | L199, "the best bound ... does not bound even the second order"; the uniform bound is PROVED GIVEN (MIX) (one mark, L203 vs L268) |
| I7 (F1), (F2) | HOLDS | none |
| I7 (F3), Proposition U1-BR | HOLDS, scoped | theorem grade in the lane: Villain form at beta >= 2^14 at both points |
| I7 seed under U(1) L215 | HOLDS AFTER CORRECTION | needs X < infinity in R_eps; "theorem-grade difference" is a reading on the SU(2) side |
| I7 layer-phase GUIDE L219 | HOLDS AFTER CORRECTION | first failing line L219, "The bridge contains it"; "Orland posits a crossover" unverified |
| I8 R with X, not xi_2 (K1) | HOLDS (ARGUED) | precision on the reason: K1 asks for the whole sheet, the S2 try asks for mixing |
| J1 | (S-q) assumes PERP-BD's conclusion | the answer is OPEN as a theorem, ARGUED (step 4 text) |
| J2 | yes, given (S), by definition | add "given the seed (S)" in L289 |
| J3 | HOLDS AFTER CORRECTION | text above |

Also corrected, no content: the pointers of L30-31 into `parts/gap.md` are off
by one; 8.1 (L253) and the marks table need the scope words of J1-J3.

**Overall.** No PROVED step of row 1066 FAILS. Its main conclusions hold at the
grade they state, after the corrections: the region R_eps (with X the
infimal mixing length, finite) holds no isotropic continuum limit GIVEN (S-q)
(a restatement) and by the ARGUED matching; given (S), the bridge is the target
at one coupling; the soft bridge is false for compact U(1). The corrected
formula of 5.3 (e) and the field exponent 3/4 hold. Two printed lines are
wrong and change no verdict: the sign of the one-loop line L126, and the
logic of L112's first sentence. One logical claim is wrong and is not used:
L219 "the bridge contains it". One claim is not proved and should go: the
last sentence of REN (3).

**Who checked what.** Checked line by line by Claude Opus 5.5 (max, laptop
subagent), same provider as the author (Claude Fable 5.2 medium); this is not
an independent-provider check (row 1070 is that, run in parallel and not read
here). Not covered: the step-3 source table beyond the Karsch, Klassen, Fu-
Nielsen, Dimopoulos-Farakos-Vrentzos and Hasenfratz entries; the claims of
check 1061 that L52 quotes about Orland's regime; rule 0a at L172. Sources
fetched (each in a new empty folder, read with `python3 -I`, nothing
committed): `/tmp/row1069-bzj-b/` (TeX of arXiv:hep-lat/9510015, read);
`/tmp/row1069-bzj-a/` (arXiv:hep-lat/9411009, PostScript with bitmap
formulas, not usable, not read); `/tmp/row1069-bzj-c/` (INSPIRE metadata for
the 1976 Brezin-Zinn-Justin papers: no open document). Scripts in
`/tmp/row1069-scripts/`; one GUIDE run (`sign_guide.py`, pure Python, BLAS not
used); no verdict rests on it. No computer-assisted step. (W) does not move.

**Credits.** E. Brezin and J. Zinn-Justin (the 2 + eps renormalization group;
not read here); S. Caracciolo and A. Pelissetto (the open source used for the
exponent check); F. Karsch; A. and P. Hasenfratz; T. Klassen; P. Orland; Y. Fu
and H. B. Nielsen; P. Dimopoulos, K. Farakos and S. Vrentzos; J. Frohlich and
T. Spencer; A. Guth; R. Dobrushin; J. Ginibre; OpenAI, and J. Ding, F. Huang
and P. Yang (posted two-dimensional O(n) theorems, unrefereed); T. Balaban,
and J. Sussman and L. Alpoge's account; rows 1053, 1061, 1062, 1066, 1067 of
this lane.

RESULT: Row 1069 (Claude Opus 5.5 max, laptop subagent; same provider as row 1066; not an independent check): row 1066 checked line by line; no PROVED step FAILS. HOLD: Lemma BARE, Corollary BARE-1 and the reconciliation of checks 1061 and 1062; Proposition PERP-BD as an implication; Lemma PERP; Claim S2 with the constant 1/16; the uniform second-order bound, PROVED GIVEN (MIX); Proposition REN (1)-(2) given (S); Proposition U1-BR (the lane's theorem grade needs the Villain form at both points); the matching of 5.3 as ARGUED, with z = (beta_M(b)/beta_M)^(3/4), the cube and the two-loop length checked against the open copy of Caracciolo and Pelissetto, arXiv:hep-lat/9510015 (Brezin and Zinn-Justin not read: no open copy). Corrected: the one-loop line L126 has the wrong sign (xi_R = xi_MT (1 + (1/(pi beta)) log xi_R + ...)); L112's first sentence; X must be the infimal mixing length and R_eps must require X finite, and 5.3 assumes X/xi_2 bounded (the O(4) mixing length on file is e^(pi beta + o(beta)), row 1009); REN (1) needs 'given (S)' and the record's torus form at each beta of the window with an open carry; REN (3)'s last sentence is not proved ((BR-L) alone gives the bridge); the bridge is not (K-flow) in W2's sense; the threshold in 5.3 (f) depends on the unknown K; 'the bridge contains it' at L219 is wrong as logic. Judged: (S-q) states PERP-BD's conclusion, so 'no continuum limit in R' is OPEN as a theorem and ARGUED by the matching; REN proves, by definition, that given (S) the bridge is T_JW-lat at one coupling; 'V2 FAILS as a route by S0' HOLDS AFTER CORRECTION of its scope (the need for a bridge rests on (S-q) or the ARGUED matching). (W) does not move.
