lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T23:38Z

# gap-mini-solve-aj-opus: mass gap for 4D SU(2) Yang-Mills (FINISH row 1264)

Started 2026-11-20T11:38Z on the Mac mini Claude worker 3, at commit 6c33935f9 of
branch claude/ym4d-hard-route. Claude Opus 5.5, max effort. Not committed by this
worker; a relay copies the file.

Labels: PROVED (written argument, checkable by hand), ARGUED (argument with a named
gap), GUIDE (heuristic or numeric guide, never a proof step), OPEN.

Correction note (12:18Z by date -u): the step headings first carried clock times that I had guessed, not read; they
were later than the real time. They are replaced by "before 12:17Z by date -u". Times below come from date -u.

## Step 0. Orientation (written 2026-11-20, before 12:17Z by date -u)

**Read for this row.** GOAL.md; FINISH.md L1-84, L299-352 and row 1264; `library/prior/gap-onebound-read-sol.md`
(row 1218) in full; `parts/gap.md` L1-104; the RESULT lines of the gap-mini-solve rows a-ag (rows 1188-1258); row 1258
(`gap-mini-solve-ag-opus.md`) Sections 1, 4, 5; row 1233 (`gap-mini-solve-u-opus.md`) 3e-4; the opening of row 1260
(`gap-mini-solve-ai-opus.md`, worker 2, on (FI) at pins); `library/gap-bridge-exercise-check-opus.md` L250-300
(Proposition CA-FAIL as checked). Source fetched by URL into a scratch folder outside the repository: Sussman and
Alpoge's complete account, part III, at commit 31a47c543775 (`theorem_0_complete_account_raw_III.tex`; credit Ethan
Sussman and Levent Alpoge, with Claude and Codex as authors of their text, after Balaban). III:n below is its TeX line.

**What the record fixes (pointers to evidence, not evidence).**
- Beside the account's premises, the gap clause on the tr F^2 sector reads one infrared input, (N-phys) (rows 1161,
  1179, 1225; check 1232). On the one-cutoff carry it reads instead a seed at one base datum (rows 916-917, 1233, 1255,
  1256), and row 1258 (check 1265: holds after correction) states that base datum in its weakest proved-sufficient form:
  (SL), a bound tau_* on the total-variation dependence of a slab's middle slice on one boundary slice, uniform over all
  boundary slices, at ONE coupling in the window, slab thickness a few tens of correlation lengths.
- The one-cutoff carry also reads: (FI) at pins (row 1260 is on it now), (V9) at pins (row 1255; its check, row 1263, is
  running), the hypotheses (a)-(e) of the account's `9.1:thm-last-lattice-comparison` with (e) =
  `9.1:prop-blind-site-expansions` (III:16558, "Proof outstanding"), (DET)'s inputs (rows 987-994), clause (0)'s
  torus-independence lemma, and the account's premises. Row 1233 point 3: this route pays for clause (v) machinery,
  which `library/port-map.md` F3 puts off T0's chain.
- About eighty plain-brief rows found no engine that carries a selective input across the band (route registry RA-RG,
  methods 19-36 of `parts/gap.md`; the screening tables of rows 1189, 1194, 1199, 1237, 1256). Row 998 9.5 asks for no
  further fresh-framing exercise.

**Running beside this row (files not visible at this pin):** row 1259 (`gap-mini-solve-ah-opus`, worker 1; its file
holds only a header at this pin) and row 1260 (worker 2, (FI) at pins). Overlap with row 1259 cannot be checked here.

## Step 1. How to attack it, and the item chosen (written 2026-11-20, before 12:17Z by date -u)

**1.1 The crux (judgement, ARGUED; no new screen).** The open core is the base datum: (SL) of row 1258 at one coupling,
or (N-phys) at every cutoff. Either is a lattice gap of Wilson SU(2) with a volume-uniform count at order-one coupling,
with no small parameter. The worst-case forms are refuted at the window: suprema over pinnings (CA-FAIL, row 1072, check
L250-300 of `gap-bridge-exercise-check-opus.md`), over tilts (Theorem D2, row 977) and over coupling fields (Lemma SHEET,
row 996). The posted 2D O(N) mechanisms have no 4D carrier on gauge-invariant data (rows 1011-1016, 1228, 1229, 1241,
1243). I checked each idea I had against the record before working it: spectral independence and localisation schemes
(pinning or tilt suprema: CA-FAIL, D2), Polchinski-flow log-Sobolev (method 31), Birkhoff contraction of the slab kernel
(row 1258 Proposition RR), Durhuus-Frohlich slicing, Mack-Petkova and Tomboulis-Yaffe vortex inequalities,
Knabe-type local-gap criteria, Kogut-Susskind strong-coupling bounds (each term has 13 to 67 hits in `library/`), and the
newest literature (`library/prior/gap-lit-refresh-2026-11-20-luna.md`: no new unconditional 4D result to 2026-11-19).
I found no route off the map, so I do not attack the crux head-on in this row. This repeats the judgement of rows 1209,
1219, 1233 and 1258; it is recorded only so that the lead can see this row did not skip the crux.

**1.2 Items considered and set aside.**
- `9.1:prop-blind-site-expansions` (III:16558, "Proof outstanding"; on the one-cutoff carry; no owner, no FINISH row
  attacks it). Its route (III:16620-16760) is to repeat Balaban CMP 116 Section 2 with island-blind lengths. CMP 116 is
  not in the papers folder, and Project Euclid answered the PDF request with a bot check (Incapsula), so I stopped there
  as the rules require. Blocked for this worker; the account's five route points are not checked here.
- (FI) at pins: row 1260 works on it now. (V9) at pins: row 1255 with reading (R); its check (row 1263) is running.
  (DET)'s inputs: rows 990-994 with checks. (MON): only on the first-passage-top route (row 1256).

**1.3 Item chosen: H-C6a.** `8.6:lem-prefactor-monotone` (CA-II:102730-102830), the monotonicity of the common
prefactor under island removal, "Stated; proof incomplete at the step marked (*)". Registry row H-C6a
(`library/open-registry.md` L246): owner none, standing OPEN. Tree node: "R9 witness analytic inputs"
(`library/t0-tree.md` L213), on T0's chain through the finite-cutoff witness (non-triviality, which the Jaffe-Witten
statement needs: a gap of a trivial limit says nothing). Rule 0a: no FINISH row, no `library/open-core.md` entry and no
`library/l17c.md` entry names it (grep of `prefactor-monotone`, `H-C6a`, `Monotonicity of the common prefactor`).
The step (*) (CA-II:102804-102816) asks: on the cubes of side L M_2 R_k of a healed island X_a, wherever the
preparation's small-field characteristic function (CMP 122a (1.3)-(1.4)) equals 1, the step's own (CMP 119 (2.17),
(3.2)) also equals 1. The account gives two reasons that do not compare the thresholds and leaves the comparison open
("It remains to compare the thresholds ...", CA-II:102814-102816).

Moves: H-C6a (T0 tree, R9 witness analytic inputs). Success: (*) proved from the two papers' definitions, so the lemma
is an implication of its cited inputs. Failure: an explicit configuration on one cube where the preparation's
characteristic function is 1 and the step's is 0; then (8.6:eq-prefactor-monotone-a) fails as stated and the lemma
needs a different comparison. Either outcome changes the registry row.

## Step 2. The two characteristic functions, read (written 2026-11-20, before 12:17Z by date -u; READ unless marked)

Sources: Balaban CMP 119 (1988) 243-285 and CMP 122 (1989) 175-202 ("122a"), read from the page images of the legal
copies in the papers folder (the OCR layer is garbled in formulas). Credit: Tadeusz Balaban.

**2.1 The step's own function (CMP 119 p. 257, (2.16)-(2.17)).** Partition the lattice T_eta into cubes of side
L M_2 R_k. For each cube Q put U_(k,Q)(V_k) = U(B_k(Q^(~4)), M(Q_k^(s*) V_k)) (2.16), and
    chi_k(Omega_k) = prod over Q in Omega_k of chi( sup over p in Q^~ of |U_(k,Q)(V_k, dp) - 1| < eps_k eta^2 ).   (2.17)

**2.2 The functions CMP 122a writes out (p. 178, (1.2)-(1.9)).** On a class component Z (conditions (i), (ii) of
CMP 122a Section 1: inside a cube of side 100 M R_k, no new large field in the last N steps), Balaban writes
T_k(Z) exp A_k = chi_k(Omega_k^(~4)) prod over j = k-1, ..., h of T^(j)(Z_(j+1)) chi_h(Omega minus Omega_(h+1)^~) T_h(Z_h) exp A_k,
h = k - N, and lists the seven groups of characteristic functions of the one-step operations. The first two are
    (1.3) chi( sup over p in Q^~ of |U_(j,Q)(V_j, dp) - 1| < eps_j (L^(k-j) eta)^2 ),  Q in (Omega_j^(~4) minus Omega_(j+1)^~) cap Z,
    (1.4) chi( sup over p in Q'^~ of |U_(j+1,Q')(V_(j+1), dp) - 1| < eps_(j+1) (L^(k-j-1) eta)^2 ),  Q' in (Omega_(j+1)^(~4) minus Omega_(j+2)^~) cap Z,
with Q the L M_2 R_j cubes of T_(L^-j) and Q' the L M_2 R_(j+1) cubes of T_(L^-(j+1)). At j = k - 1, (1.4) is the factor
of (2.17) at level k on its own domain: the same function of V_k with the same threshold eps_k eta^2.

**2.3 What the preparation does (CMP 122a pp. 179-181, read in the OCR and to be checked on the images).** The
preparation integrates, for j = h, ..., k - 1, the variables localised in Z_(j+1) minus Z'_(j+1), with new background
fields U_k^((n)) built on new determining sets B_k^((n)) (1.14)-(1.21). Before each integration it inserts a decomposition
of unity 1 = chi_k^((n)) + (1 - chi_k^((n))) in each component of Z ((1.22), (1.23) for n = 0, 1). Components that take
1 - chi_k^((n)) get new large fields and leave Z. On the components that stay, the restrictions in chi_k^((n)) "imply"
that the old functions (1.3) (at j = h) and (1.4) (at j = h) equal 1, so these old functions are removed. After n
integrations "the only characteristic functions which remain ... are chi_k^((n)) chi_h(Z_h cap Omega_h)"; the definition
of chi_k^((n)) changes for j = h + n > k_0 = k - N_0, where "we change the regularity conditions by a factor".

So the preparation's function on a healed island is not literally (1.3)-(1.4): it includes the final chi_k^((N))
restricted to the island, written in the new background fields, with thresholds changed by a factor near the top levels.
(This first reading is superseded by 2.4 and Step 3: Balaban also keeps chi_k(Omega_k^(~4)) and, in CMP 122b, adds a
decomposition that puts the (2.17) factor on the rest of the component.)

**2.4 The preparation's final function and what it keeps (CMP 122a pp. 181-184, read on the page images).** After
n = j - h integrations the function is chi_k^((n)) of (1.24): conditions |U_(k,Z)^((n))(dp) - 1| < (threshold) on the
plaquettes p of each shell, in the new background field U_(k,Z)^((n)) (1.18)-(1.21). The last line of (1.24) reads
    |U_(k,Z)^((n))(dp) - 1| < c (1 - beta/2) eps_j (L^(k-j) eta)^2  for p in Omega_(j-1) minus Omega_(j+1),
"where c = 1 for j < k, and c = 3 for j = k", with 0 < beta <= 1/2 "not too small, e.g. beta = 1/2", and 2 <= L_0 < L/2.
So at the top level (n = N, j = k) the preparation's own threshold on the shell Omega_(k-1) minus Omega_(k+1) is
3 (1 - beta/2) eps_k eta^2, which is LARGER than the step's eps_k eta^2 of (2.17) (9/4 times larger at beta = 1/2).
Balaban's domination argument (1.29)-(1.31) shows that chi_k^((n+1)) and the other restrictions force the old
functions (1.3) and (1.4) to equal 1, using c = 1 in (1.24) and the bound (1.31)
|U_(j,Q)(dp) - 1| < (1 - beta/2 + 2 beta L^(-2)/10 + 4 beta/10) eps_j xi^2 < eps_j (L^(k-j) eta)^2. At the top level he
does not do this: "The same holds for the functions (1.4), because the argument above applies to an arbitrary j, hence
for j + 1, except when j + 1 = k. In this case we leave the functions (1.4) as chi_k(Omega_k^(~4)) on the right-hand side
of (1.29)" (p. 184); and (1.29) is stated "for j + 1 < k, and for j + 1 = k the right-hand side above is multiplied by
chi_k(Omega_k^(~4))" (p. 183).

Consequence for (*) (ARGUED from these two passages; the island representation of CMP 122b (1.70)-(1.72) is read in
Step 3). After the preparation, a class component Z carries at the top level BOTH the preparation's chi_k^((N))
(threshold 3 (1 - beta/2) eps_k eta^2 on its top shell, field U_(k,Z)^((N))) AND the step's own chi_k(Omega_k^(~4)) of
(2.17), kept on purpose. So:
- On the cubes of Omega_k^(~4) cap Z the prepared term carries the step's function itself, and the domination
  "prep = 1 implies step = 1" holds there trivially, as a product containing the step's factor.
- On a cube of Z outside Omega_k^(~4) (Balaban's ~n means n layers out, 3.10), the preparation alone leaves only
  chi_k^((N)), whose top threshold is weaker than eps_k eta^2. There the literal statement "wherever the
  preparation's function equals 1, so does the step's" cannot follow from the thresholds: a field with
  eps_k eta^2 <= |U(dp) - 1| < (9/4) eps_k eta^2 on one plaquette passes the first and fails the second, if the two
  background fields agree there.
Whether such cubes exist in a healed island, and which step function the term X' carries on them, is a question of
the geometry of the island representation. That is Step 3.

## Step 3. The island representation in Balaban's text, and the step (*) (written 2026-11-20, before 12:17Z by date -u)

**3.1 READ: what a healed island carries (CMP 122b pp. 377-379, page images).** Before the last decomposition the R
operation has the form (1.70): (1.1) = chi_k chi_(k,Lambda) delta_(G_0)(V'_k) chi exp A'_k(...) chi_(h,1/2) int dB ...
Then (p. 378): "Now we try to remove the characteristic functions chi_(k,Lambda) chi. We introduce the decompositions
of unity 1 = chi_k((Omega_k^(~4))^c) + chi_k^c((Omega_k^(~4))^c) in components of Z. ... For the components with the
first, small field function we can remove the characteristic functions chi_(k,Lambda) chi, because they are equal to 1
... Thus, the components of Z are divided into two classes. For components of the first class, denoted by
{X_1, ..., X_n}, there are only the characteristic functions chi_k(X_i^(~-6)), which are combined with the function
chi_k(Omega_k^(~4)), here Omega_k is the old k-th domain." The R operation is then (1.72):
    (R rho_k)(V_k) = sum over Z_k, {Y_1..Y_m} of chi_k((Omega_k cap (Y_1^c)^(~2) cap ... cap (Y_m^c)^(~2))^(~4)) (sum T''_k(Z_k)) exp A'_k
                     prod_i chi_k^c(Y_i^(~-6)) chi_(k,Lambda_i) chi_i delta_(G_i)(V'_k) T'_k(Y_i)
                     { sum over n >= 0 and {X_1..X_n} of prod_j T'_k(X_j) exp sum_Y V(Y, U_k) },
"where Omega_k is the new k-th domain defined by the determining set of the configuration U_k". The operation T'_k(X)
of (1.71) carries the island's own functions (chi'(X), chi_(h,1/2)(...), T_h(Z_h cap X)) inside it, on the island's
internal variables.

**3.2 Proposition TI (top-level threshold identity). PROVED (reading of two displays).** Let Q be a cube of side
L M_2 R_k of the partition of T_eta = T_(L^-k). The function of CMP 122a (1.4) at j = k - 1 on Q is
chi( sup over p in Q^~ of |U_(k,Q)(V_k, dp) - 1| < eps_k (L^0 eta)^2 ), which is the factor of CMP 119 (2.17) on Q: the
same field U_(k,Q)(V_k) of (2.16), the same plaquettes, the same threshold eps_k eta^2. So the threshold comparison
that CA-II:102814-102816 leaves open is an identity on every cube where both are defined, not an inequality.
Proof: (1.4) with j + 1 = k has eps_(j+1) (L^(k-j-1) eta)^2 = eps_k eta^2, and its cubes are "the L M_2 R_(j+1)-cubes of
the partition of the lattice T_(L^-(j+1))" (CMP 122a p. 178), i.e. the L M_2 R_k cubes of T_eta, which are the cubes
of (2.17) (CMP 119 p. 257). QED

**3.3 Remark P (the reading under which (*) fails). PROVED (threshold arithmetic), with its scope.** If "the
preparation's characteristic function" on X_a is read as the preparation's own final function chi_k^((N)) of CMP 122a
(1.24) on its top shell, then (*) is false as a threshold statement. The top line of (1.24) at j = k is
|U_(k,Z)^((N))(dp) - 1| < 3 (1 - beta/2) eps_k eta^2 on Omega_(k-1) minus Omega_(k+1) ("c = 3 for j = k"), and with
Balaban's beta = 1/2 this is (9/4) eps_k eta^2 > eps_k eta^2. A block field whose two background fields agree on one
cube Q and have one plaquette with eps_k eta^2 <= |U(dp) - 1| < (9/4) eps_k eta^2 passes chi_k^((N)) on Q and fails the
(2.17) factor on Q. This is exactly why Balaban does not leave chi_k^((N)) alone at the top level: he keeps
chi_k(Omega_k^(~4)) (CMP 122a p. 184) and adds chi_k((Omega_k^(~4))^c) on the components of Z (CMP 122b p. 378).
Scope: this remark shows that the account's (*) cannot be proved by comparing (1.24) with (2.17); it does not show
that the lemma is false, because the healed term carries more than chi_k^((N)) (3.1).

**3.4 Corollary H (the step (*) of 8.6:lem-prefactor-monotone). PROVED GIVEN 3.1 and premise (BG) below.**
In the term (O, X) every cube of the region of an island X_a carries a (2.17) factor: the old chi_k(Omega_k^(~4)) on
the cubes of Omega_k^(~4), and the factor chosen in the decomposition 1 = chi_k((Omega_k^(~4))^c) + chi_k^c(...) on the
other cubes of the component, since Balaban introduces that decomposition exactly on (Omega_k^(~4))^c "in components of
Z" (3.1) and a first-class component takes the small-field branch. Balaban writes the result as chi_k(X_i^(~-6))
"combined with the function chi_k(Omega_k^(~4))"; this description does not depend on the meaning of the layer index. In the term (O, X') the step's own function on the cubes of X_a
is the (2.17) factor on each cube. Under (BG) each (2.17) factor is the same function of V_k in both terms, so
    chi_a^prep = chi_a^step * (other characteristic functions) <= chi_a^step      pointwise,
which is (*). The rest of the account's proof (CA-II:102818-102830: products over islands, positivity of the other
three factors) then gives (8.6:eq-prefactor-monotone-a).
Premise (BG), proved in 3.6: on every cube Q of the region of X_a, the field U_(k,Q)(V_k) of (2.16) in the term (O, X) (built on
Balaban's new determining set after R, CMP 122b p. 377: "the new determining set B_k") equals the field of the term
(O, X') (built on the determining set of a region with no island at X_a). The account assumes the same thing off X_a
("the characteristic functions they carry coincide off the regions X_a", CA-II:102795-102797) and its companion lemma
8.6:lem-healed-islands-unread (registry H-C6b, its own step (*) open) is a statement of the same kind.

**3.5 What changes in the account's proof (ARGUED).** The account's reason "the preparation's characteristic function
of CMP 122a (1.3)-(1.4)" names the wrong object for the healed term: on a first-class component the functions of the
preparation are removed (122a p. 184 for (1.3), (1.4) below the top; 122b p. 378 for chi_(k,Lambda) and chi), and the
function that stands in the prefactor is chi_k(X_a^(~-6)), introduced by the last decomposition of unity of the R
operation. With that object the "threshold comparison" is Proposition TI (an identity), and what remains is (BG), a
statement about determining sets, not about thresholds. In Balaban's own (1.72) the prefactor does not depend on the
island family at all, so there (8.6:eq-prefactor-monotone-a) holds with equality, given that his regrouping is valid
(this is the account's representation lemma, cited in its Definition 8.6:def-island-representation).

**3.6 Premise (BG) is supplied by Balaban's new determining set. PROVED GIVEN CMP 122b (1.33)-(1.35) (read on the page
image, p. 365) and CMP 119 (2.16).** Balaban: "Now we introduce a new determining set B_k, and a new background field
U_k. We define B_k as equal to B''_k on Z^c, and to {Z^((k))} on Z. More precisely
    B_k = {Gamma_j}, where Gamma_j = Gamma''_j cap Z^c for j < k, Gamma_k = Gamma''_k cup Z^((k)).    (1.33)"
with new variables V = V'' on Z^c and V = V'_k V_Lambda = V_k on Z (1.34), "and V_Lambda ... equal to V_k outside Lambda",
and U_k = U_(B_k)(V) (1.35). So on the class region Z, which contains every island X_a, the determining set has only its
level-k piece: the history of the island is gone from it. In the term (O, X') the region of X_a lies in the small-field
region Lambda_k of a history with no large field there, where the determining set is also level k (Gamma_k = (Omega_k)^((k))
on Omega_k, CMP 119 (2.2)); and away from X_a the two terms have the same outer datum O, hence the same live
components with the same admissible subsequences (Definition 8.6:def-island-representation, outer data). The field
U_(k,Q)(V_k) = U(B_k(Q^(~4)), M(Q_k^(s*) V_k)) of (2.16) depends only on B_k near Q and on V_k. Hence on every cube Q of
the region of X_a it is the same function of V_k in the two terms. QED

**3.7 The cube inclusion (G). PROVED (from 3.1).** Write H_X for a history whose class component at X_a is healed
(term X) and H_X' for one with no large field at X_a (term X'), with the same outer datum and the same other islands.
Near X_a, Omega_k^c is contained in X_a in H_X (X_a is a connected component of Lambda_k^c, and Omega_k^c is contained
in Lambda_k^c because Lambda_k is contained in Omega_k, CMP 119 (2.1)). In the term X, every cube near X_a either lies in
Omega_k^(~4), where the old chi_k(Omega_k^(~4)) stands, or in (Omega_k^(~4))^c inside the component's region, where the
decomposition of 3.1 put the small-field factor. So the term X carries a (2.17) factor on every cube near X_a, and by
3.6 it is the same function as the factor that the term X' carries on any of those cubes. Cubes whose status is fixed
by another component (a live one, or another island) are treated alike in both terms, since the outer datum and the
other islands are the same. So the set of (2.17) factors of the term X' near X_a is a subset of those of the term X.
The argument uses only that the decomposition of unity is placed on the complement of Omega_k^(~4), not the meaning of
the layer indices ~4 and ~-6.

**3.8 Result for H-C6a, first form (superseded in part by 3.8a-3.8b). PROVED GIVEN the cited Balaban displays (TI, 3.1,
3.6, 3.7), except on the band cubes named in 3.8a.** For two admissible families
X containing X', the top-level small-field function of O_(O,X) on the cubes near the islands of X minus X' is the product
of the term X' function with further characteristic functions. So (*) holds, in the corrected form
    chi_a^prep (the product of all top-level functions of O_(O,X) on the cubes near X_a) <= chi_a^step,
and with it the account's (8.6:eq-prefactor-monotone-a), since its other steps (CA-II:102758-102800 and 102818-102830)
compare factors that are equal. Not checked here: those other steps of the account's proof (the completed action, the
coupling profile reset, the members that read an island); the account's representation lemma that puts the prepared
density in the form of Definition 8.6:def-island-representation; and Balaban's regrouping in (1.72), which holds up to
his "equivalence" after the reversed Faddeev-Popov step (CMP 122b p. 378: "equivalent, but not equal").
Standing: proved by Claude from Balaban's printed displays, read once on page images; not checked by another model.

**3.8a Correction to 3.6-3.8 found on re-reading (12:29Z by date -u).** Balaban's layer index means "n layers out"
(CMP 122b p. 384: S(Z) = Z'^(~10), "we add ten layers"; checked on a zoomed page image). Then Omega_k^(~4) is Omega_k with
four layers added, so the old factor chi_k(Omega_k^(~4)) has cubes up to four layers inside the island's core
Omega_k^c cap X_a. For such a cube Q the field U_(k,Q) of (2.16) reads B_k near Q, and in the old determining set (CMP 119
(2.2), before (1.33)) that neighbourhood can contain the island's history shells Gamma_j, j < k. So on those cubes 3.6
does not show that the old factor is the same function of V_k as the factor of the term X'. What 3.6 does show: the
factors placed by the decomposition of 3.1 on (Omega_k^(~4))^c, and every factor whose cube has its determining
neighbourhood inside Omega_k, are the same function in both terms. For the old factor on the band cubes, the
identification with a factor built on the new determining set is Balaban's own step "which are combined with the
function chi_k(Omega_k^(~4))" (CMP 122b p. 378), leading to the single front factor of (1.72) written for the new domain
and the new background field. I did not prove that step. (The meaning of the layer index is not used anywhere else in
this file; 3.10 holds under either meaning.)

**3.8b Corollary H0 (H-C6a from the account's own definition). PROVED GIVEN the representation lemma that the account's
Definition 8.6:def-island-representation already cites.** The Definition sets O_(O,X) := "the factor that stands
outside the bracket of [CMP 122b, (1.70)-(1.72)] for the term (O, X)". In (1.72) the only factor outside the bracket
{ sum over n >= 0 and {X_1, ..., X_n} of prod_j T'_k(X_j) exp sum_Y V(Y, U_k) } is
chi_k((Omega_k cap (Y_1^c)^(~2) cap ... cap (Y_m^c)^(~2))^(~4)) (sum T''_k(Z_k)) exp A'_k prod_i chi_k^c(Y_i^(~-6)) chi_(k,Lambda_i)
chi_i delta_(G_i)(V'_k) T'_k(Y_i), with Omega_k "the new k-th domain defined by the determining set of the configuration
U_k". It depends on the outer datum (Z_k, {Y_i}) and not on the island family. Hence O_(O,X) = O_(O,X') for any two
admissible families, and (8.6:eq-prefactor-monotone-a) holds with equality. QED
So the lemma is true as soon as the representation lemma is, and the step (*) is not needed. The analysis of 3.2-3.7 is
kept because it locates the content: the account's (*) names the wrong objects (3.10, Remark P), and the true content
is Balaban's "combined with" step, which sits inside the representation lemma.

**3.8c The layer convention, second source (12:32Z by date -u; READ on the CMP 119 p. 265 page image).** CMP 119
(3.5): "Omega_(k+1) = (Q'^(~2)_(k+1) cup (B^(k+1)(P^1_(k+1))^c)^(~3))^c, hence (Omega^(~2)_(k+1))^c = Q'_(k+1) cup
(B^(k+1)(P^1_(k+1))^c)^~". The complement of Omega^(~2) is two layers smaller than the complement of Omega, so
Omega^(~2) is Omega with two layers added: the same "n layers out" convention as S(Z) = Z'^(~10), now for a small-field
domain. So 3.8a stands as written: Omega_k^(~4) reaches four layers past Omega_k. (Balaban's domains carry built-in
margins, e.g. the two and three layers in (3.5), so the band cubes of 3.8a need not be large-field cubes; whether their
determining neighbourhoods meet the island's history shells is the question left open in 3.8a.)

**3.9 Two facts used above, now read (CMP 119 pp. 254-255, page images).** (2.1): Omega_1 contains Lambda_1 contains
Omega_2 contains ... contains Omega_k contains Lambda_k, so Lambda_k is contained in Omega_k and Omega_k^c in Lambda_k^c.
(2.2): Gamma_0 = Omega_1^c, Gamma_j = Omega_j^((j)) minus Omega_(j+1)^((j)) for j = 1, ..., k - 1, Gamma_k = Omega_k^((k)),
B = union of the Gamma_j; so on Omega_k the determining set is the level-k piece. Both are used in 3.6 and 3.7.

**3.10 Correction of the account's identification (a correction of their text, with the failing case). PROVED from the
cited displays.** The lemma says that for X the top-level functions on X_a "are those of the preparation, [CMP 122a,
(1.3)-(1.4)]", taken "on the same cubes" as the step's. Read literally this is false on part of X_a:
- (1.3) is a level-j function for each j; at the top level only (1.4) with j = k - 1 is present, and it is defined for
  cubes Q' in (Omega_k^(~4) minus Omega_(k+1)^~) cap Z (CMP 122a p. 178).
- X_a has cubes outside Omega_k^(~4). Balaban's layer index means "n layers out" (CMP 122b p. 384 defines
  S(Z) = Z'^(~10) as the cover Z' "and we add ten layers of such cubes"), so Omega_k^(~4) is Omega_k with four layers
  added. Its complement in the component is the set on which Balaban places the decomposition of 3.1 and which he writes
  X_i^(~-6), the component with six layers removed; it lies in the large-field core Omega_k^c cap X_a (not empty: by
  condition (ii) of CMP 122a Section 1 the component's large fields were created at levels at most h < k, so X_a meets
  Omega_j^c, contained in Omega_k^c by (2.1)). X_i^(~-6) is not empty because a class component spans about 42 cells or
  more (CMP 122a p. 177: "the minimal size is approximately equal to 42(L/(L-1)) M R_k"), more than the twelve layers
  removed.
- On such a cube Q the functions (1.3)-(1.4) carry no level-k factor, while the term X' (no large field at X_a) carries
  the (2.17) factor on Q. For a block field V_k with one plaquette of Q^~ where |U_(k,Q)(V_k, dp) - 1| >= eps_k eta^2,
  the first is 1 and the second is 0. So the sentence "wherever the preparation's characteristic function on such a
  cube equals 1, so does the step's" fails for the objects it names.
The displayed inequality (8.6:eq-prefactor-monotone-a) is not affected: Balaban's prefactor on a healed island also
carries the small-field factor of the decomposition of 3.1 on every cube of (Omega_k^(~4))^c in the component, so a
(2.17) factor stands on every cube of X_a, and with it 3.8 holds. Suggested replacement for the
sentence (unproved wording, for the lead): "For X these characteristic functions are chi_k(X_a^(~-6)) of [CMP 122b,
p. 378], combined with chi_k(Omega_k^(~4)) [CMP 122a, p. 184]; on X_a the determining set is level k by [CMP 122b,
(1.33)]; together they are the factors of [CMP 119, (2.17)] on every cube of X_a and of its neighbourhood, possibly
times further characteristic functions."

**3.11 Status of H-C6a after this row.**

| Statement | Label | Rests on |
|---|---|---|
| TI: (1.4) at j = k - 1 is the (2.17) factor (same field, cubes, threshold) | PROVED | CMP 122a p. 178, CMP 119 p. 257 |
| P: the preparation's own top function chi_k^((N)) has threshold 3(1 - beta/2) eps_k eta^2 > eps_k eta^2, so (*) cannot be proved from it | PROVED | CMP 122a (1.24) |
| 3.10: the account's named objects (1.3)-(1.4) leave the core cubes of X_a without a level-k factor, so its domination sentence fails as written | PROVED | CMP 122a p. 178, condition (ii); CMP 119 (2.1) |
| BG: the (2.16) field is the same function of V_k in the terms X and X', for the factors of the 3.1 decomposition and for cubes whose determining neighbourhood lies in Omega_k | PROVED GIVEN | CMP 122b (1.33)-(1.35), CMP 119 (2.1)-(2.2), (2.16) |
| BG on the old factor's band cubes inside the core (3.8a) | OPEN here; it is Balaban's "combined with" step inside the representation lemma | CMP 122b p. 378 |
| G: cube inclusion near X_a | PROVED GIVEN | 3.1 (the decomposition is placed on the complement of Omega_k^(~4)) |
| H0: O_(O,X) does not depend on X, so (8.6:eq-prefactor-monotone-a) holds with equality | PROVED GIVEN | the account's Definition 8.6:def-island-representation and its representation lemma; CMP 122b (1.72) |

All of it: Claude Opus 5.5 from Balaban's printed pages, read once; checked by no other model. A check should re-read
CMP 122b pp. 365, 377-379 and CMP 122a pp. 178-184 on the page images.

## Step 4. Second item: the step (*) of the age lemma (written 2026-11-20, before 12:17Z by date -u)

**4.0 Why this item.** `8.9:lem-age-lemma` (CA-II:112000-112100) is "Stated; proof incomplete at the step marked (*)",
and (*) is the join bound (8.9:eq-age-lemma-4) (CA-II:111979), "taken by statement from [CMP 122b, Section 1]". The
lemma is on two chains: registry row H-C7c (owner none, OPEN; T0 tree node "R9 witness analytic inputs"), and the gap
lane's one-cutoff carry, whose input `9.1:thm-last-lattice-comparison` lists "the age lemma" among its standing
hypotheses (a) (row 1233 Lemma 3.5, III:17940-17948). Rule 0a: no FINISH row, no `library/open-core.md` entry
(grep `age lemma`, `age-lemma`, `8.9:`). The rest of the account's proof (birth, quiet step, preparatory refresh, the
three groups after (*)) is complete given (*) and the clock rules it quotes.
Moves: H-C7c, and hypothesis (a) of the carry's 9.1 input (one of its named items). Success: (*) proved from stated
readings of Balaban's definitions. Failure: a join whose clock exceeds the bound.

**4.1 The bound to prove (CA-II:111967-111983).** A level-(n+1) component W' is the join of p >= 0 old pieces
S(W_1), ..., S(W_p) and q >= 0 new regions X_1, ..., X_q, with p + q >= 2 or p = 0. With E_(n+1) = n_1 + R_(n+1) + 2
(R = Balaban's number at that level, written R-check in the account),
    Phi_(n+1)(W') <= max{ max_i (Phi_n(W_i) - 1), max_l K_init(X_l) } + (p + q - 1) E_(n+1).          (8.9:eq-age-lemma-4)
Balaban's own two-domain step (CMP 122b pp. 386-387, read in the OCR): "The domain S^(K_1)(X) satisfies the conditions
(i), (ii) ... applying n_1 times the operation S to the last domain, where n_1 is a rather small number, e.g. n_1 < 10,
we obtain the domain S^(K_1+n_1)(Y) containing S^(K_1+n_1)(X) ... and that K <= K_2 + n_1 + R_(j+1)". The containment
claim is not proved there. The proof below does not use it; it uses only sizes.

**4.2 Hypotheses (readings of Balaban's definitions and the account's, stated so that a checker can test each).**
- (H1) S. For a level-m domain A, S(A) is the cover of A by level-(m+1) cells with ten layers of level-(m+1) cells
  added (account CA-II:111912-111913; READ in CMP 122b p. 384 (OCR): "If Z is a union of MR_j-cubes of the lattice
  T_xi, xi = L^(-j), then we take the cover Z' of Z by a smallest union of LMR_(j+1)-cubes, and we add ten layers of such
  cubes. We denote the obtained domain by S(Z), i.e. S(Z) = Z'^(~10)"; an LMR_(j+1)-cube of T_(L^-j) is a level-(j+1)
  cell). So
  S(A) contains A (as a point set), S(A cup B) = S(A) cup S(B), and S(A), S(B) meet when A and B touch.
- (H2) Size. Let s_m(A) be the side, in level-m cells (cubes of side M R_m), of the smallest cube containing A. Then
  s_(m+1)(S(A)) <= rho_m s_m(A) + 22, with rho_m = 1/L at a scaling step and rho_m = 1 at a step where Balaban's number
  R drops (the level-(m+1) cell is then no larger than the level-m cell). No two consecutive steps are drop steps.
  The size bound is the cover (one extra cell per side) plus ten layers per side. L >= 9 (the account's floors make
  L far larger). Isolation is Lemma ISO below.
- (H3) Condition (i) at level m: contained in a cube of side 100 level-m cells, i.e. s_m <= 100 (CMP 122a p. 177).
- (H4) Condition (ii) at level m with parameter N: at each of the N levels m' with m - N < m' <= m, the image of the
  component satisfies (i) at level m', and no new large-field region is created inside it at level m' (CMP 122a p. 177:
  "in the preceding N renormalization steps no new large field regions were created inside this component, and the
  previous regions contained in it satisfy the condition (i) on the corresponding scales").
- (H5) Clock. Phi_m(W) is the least K >= 0 such that S^K(W), at level m + K, satisfies (i) and (ii) with the clock's
  parameter, along the quiet continuation (no new large field inside). For a component formed at level n + 1 by a join
  the parameter is N = R_(n+1) (Balaban: "for a domain Z created at level j ... with N = R_j"; his join bound adds
  R_(j+1)); for a piece S(W_i) entering the join its index iota_i is its own clock at level n + 1 (Phi_n(W_i) - 1 by the
  quiet rule, or its event value). R_m >= 9 at every level of the run (the account's (9.1:eq-island-geometry-b)).

**4.3 Lemma ST (stable sizes). PROVED given (H2), L >= 9.** If a domain evolves by S and at some level m_0 that follows
a scaling step its size is at most 34, then its size is at most 56 at every later level. If its size is at most 100 at
three consecutive levels, then from the last of them on its size is at most 56.
Proof. After a scaling step from size s <= 56: s/9 + 22 <= 28.3 <= 34. After a drop step from size s <= 34:
s + 22 <= 56. By isolation a drop step is always preceded by a scaling step, so the level before a drop has size at
most 34; induction over the steps gives the first claim. For the second: of the two steps between three consecutive
levels at least one is a scaling step; the size after it is at most 100/9 + 22 <= 34, and the first claim applies. QED

**4.4 Theorem J (the join bound). PROVED given (H1)-(H5), L >= 9.** Put T := max{ max_i iota_i, max_l K_init(X_l) }
and m := p + q. Then
    Phi_(n+1)(W') <= T + R_(n+1) + 2 u_m + 2,     u_m := ceil( log_9 (1.57 m) ).                          (J)
Consequently (8.9:eq-age-lemma-4) holds for every n_1 >= 2.
Proof. (1) Pieces. For an old piece, its image at level n + 1 + iota_i satisfies (i) and (ii) with N >= 9, so by
(H4) its sizes were at most 100 at the last N >= 3 levels; by Lemma ST its size is at most 56 from then on along the
quiet continuation, in particular at level n + 1 + T (T >= iota_i). The same holds for S^T(X_l) since T >= K_init(X_l).
(2) The union. By (H1), S^T(W') is the union of the images S^(T+1)(W_i) and S^T(X_l), and it is connected because W' is
and S preserves touching. A connected union of m sets, each inside a cube of side 56, lies in a cube of side at most
57 m - 1 (chain the sets along a spanning tree). (3) Shrinking. Of any two consecutive steps at least one is a scaling
step (H2). Two steps map a size s to at most s/9 + 44 (scaling then drop) or s/9 + 24.5 (drop then
scaling). After 2u steps the size is at most (57 m)/9^u + 49.5. With u = u_m, 57 m / 9^u <= 36.4, so the size before
the next scaling step is at most 36.4 + 49.5 + 22 = 107.9, and after that scaling step at most 107.9/9 + 22 <= 34. So
within t <= 2 u_m + 2 steps after level n + 1 + T the union reaches size at most 34 just after a scaling step, and by
Lemma ST all its later sizes are at most 56 <= 100. (4) Window. Let K* = T + t + R_(n+1). At the R_(n+1) levels before
and including n + 1 + K* the union has size at most 56, so (i) holds there, and no new large field is created there:
the continuation is quiet, and these levels are after n + 1, the birth level of the X_l. So (i) and (ii) with
N = R_(n+1) hold at level n + 1 + K*, and Phi_(n+1)(W') <= K* <= T + R_(n+1) + 2 u_m + 2.
(5) Comparison with (8.9:eq-age-lemma-4). Its right side is T + (m - 1)(n_1 + R_(n+1) + 2). For m = 2, u_2 = 1 and (J)
gives T + R_(n+1) + 4 <= T + n_1 + R_(n+1) + 2 when n_1 >= 2. For m >= 3, (m - 1)(n_1 + R + 2) - R >= (m - 2) 9 + 4(m - 1)
= 13 m - 22 >= 17, while 2 u_m + 2 <= 2 log_9(1.57 m) + 4 <= 13 m - 22 for every m >= 3 (equality is far at m = 3,
5.4 against 17, and the left side grows like log m). For p = 0 (a birth from q >= 2 new regions) the same proof
applies with no old pieces. QED

**4.5 What this gives (ARGUED from the account's proof, CA-II:112023-112100+, read).** The account's proof of
`8.9:lem-age-lemma` uses (8.9:eq-age-lemma-4) only at the two places marked, with Balaban's n_1 as an unspecified
"rather small number". Fixing n_1 := 2 in the charge E(Z) = n_1 + R_(j(Z)) + 2 (so E(Z) = R_(j(Z)) + 4), Theorem J
supplies (*), and the age lemma becomes an implication of the clock rules the account quotes (birth (8.9:eq-age-lemma-1),
quiet (8.9:eq-age-lemma-2), preparatory (8.9:eq-age-lemma-3), healing) and of (H1)-(H5). Balaban's containment claim
("S^(K_1+n_1)(Y) containing S^(K_1+n_1)(X)") is not needed. Not done here: a check of the account's remaining proof
lines after (*) (CA-II:112100 on). The birth rule (8.9:eq-age-lemma-1), which the account takes from CMP 122b (1.81),
is proved in 4.9 with C_S = 4. Isolation in (H2) is Lemma ISO (4.6).

**4.6 Lemma ISO (drop steps are isolated). PROVED GIVEN CMP 119 (2.5)-(2.6) (read on the page image, p. 255) and the
account's Ř_k = R(min over i <= k of x_i) (CA-II:109689).** CMP 119 (2.5): "R_j is the smallest number of the form L^r
such that R_j >= (log g_j^(-2))^r" (r a fixed exponent). CMP 119 (2.6), first inequality: g_n <= (1 + g_n^2 beta'(n - m))^(1/2) g_m for n > m. With n = m + 1, squaring
and dividing by g_m^2 g_(m+1)^2 gives x_m <= x_(m+1) + beta' for x = g^(-2), that is x_(m+1) >= x_m - beta'. Hence the
running minimum X_m = min over i <= m of x_i obeys X_(m+2) >= X_m - 2 beta'. Two drops in a row would need
Ř_(m+2) = Ř_m / L^2, i.e. (log X_(m+2))^r <= L^(a-2) < L^(a-1) < (log X_m)^r for Ř_m = L^a, so
(log X_m / log X_(m+2))^r > L. But if X_m >= max(4 beta', 2e), then 2 beta'/X_m <= 1/2, so log(X_m/(X_m - 2 beta')) = -log(1 - 2 beta'/X_m) <= 4 beta'/X_m,
and log(X_m - 2 beta') >= log(X_m/2) >= 1; hence
    (log X_m / log(X_m - 2 beta'))^r <= (1 + 4 beta'/X_m)^r <= exp(4 r beta'/X_m),
which is below L when X_m > 4 r beta' / log L. So no two consecutive steps are drop steps as long as
X_m >= max(4 beta', 2e, 4 r beta'/log L + 1) along the run; the run has X_m >= g_U^(-2) with g_U small. QED

**4.7 Two robustness remarks on Theorem J (PROVED, same argument).** (a) If the join adds layers beyond the pieces
(Balaban: the pieces are "joined together into the one component ... in particular by adding layers"), and each piece
is enlarged by at most ten layers of level-(n+1) cells, then each enlarged piece lies in a cube of side 56 + 20 = 76
at level n + 1 + T, the union in a cube of side 76 m, and the proof runs with 57 replaced by 77: u_m = ceil(log_9(2.12 m)),
u_2 = 1, and the comparison in (5) is unchanged. (b) The index iota_i of an old piece is used only through "its image at
level n + 1 + iota_i satisfies (i) and (ii) with some N >= 9"; so the theorem covers both readings in the account
(quiet index Phi_n(W_i) - 1, or the piece's own event value).

**4.8 Readings re-checked on the page images (12:26Z by date -u).** CMP 122a p. 177: "(i) it is contained in a cube of
the size 100 M R_k, (ii) in the preceding N renormalization steps no new large field regions were created inside this
component, and the previous regions contained in it satisfy the condition (i) on the corresponding scales", and
"Passing to the next step it is usually rescaled by L^(-1), but in some steps the number R_k decreases by the factor
L^(-1), and adding ten new layers of M R_k-cubes we get a region with a size greater than 40 M R_k" (this is (H2)'s drop
step). CMP 122b p. 387: the two-domain step as quoted in 4.1, with "d'_n(S^(n-j-1)(Z)) <= d'_n(S^(n-j-1)(X)) +
d'_n(S^(n-j-1)(Y))" (the chain bound of step (2)) and "K <= K_2 + n_1 + R_(j+1)" (the join's parameter, (H5)). Support
for (H4)'s "last N levels" reading: Balaban's single-domain bound (CMP 122b p. 385) waits "at most R_j further steps"
after the domain first fits a cube of side 64 M R, which is the reading "(i) on each of the last N levels"; under a
reading in which every earlier region of the history must have fitted, a region created large would never heal,
against his finite K.

**4.9 Lemma B (the birth rule) and Lemma PR (the preparatory bound). PROVED GIVEN (H1)-(H5), L >= 9 (written 12:30Z by
date -u).** The account takes both from Balaban's sentences "as stated"; the size argument of Theorem J proves them.
(B) A region Z born at level j with s_j(Z) = D cells has K_init(Z) = Phi_j(Z) <= 2 log_L(D + 1) + R_j + 4, which is
(8.9:eq-age-lemma-1) with C_S = 4 (its d'_j(Z) is Balaban's linear size in the same cells).
Proof. Along the quiet continuation two steps map a size s to at most s/L + 44 (one of any two steps scales, (H2)), so
after 2u steps the size is at most D/L^u + 44 L/(L - 1) <= D/L^u + 49.5. With u = max(0, ceil(log_L(D/36.4))), which is at
most log_L(D + 1) + 1, the size is at most 85.9; as in step (3) of Theorem J, at most two more steps bring it to at most
34 just after a scaling step, and by Lemma ST it stays at most 56. So after t <= 2u + 2 <= 2 log_L(D + 1) + 4 steps, the
N = R_j levels that follow are levels where (i) holds and no new large field is created (they are after the birth level
j), and (i), (ii) hold at level j + t + R_j. QED
(PR) In the preparatory case (a component Z_0 that satisfies (i), (ii) at level n, with a new large field introduced in
the preparatory operations; account (8.9:eq-age-lemma-3), Balaban "hence K = R_(j+1) for Z"), Z = S(Z_0) has
Phi_(n+1)(Z) <= R_(n+1).
Proof. Z_0 satisfies (ii) with N >= 3, so its sizes were at most 100 at three consecutive levels and, by Lemma ST, the
sizes of Z and of all its quiet images are at most 56. The N = R_(n+1) levels after n + 1 then satisfy (i) with no new
large field, so (i) and (ii) hold at level n + 1 + R_(n+1). QED (Only the upper bound is proved; the account uses only
that.)
With B, PR, Theorem J and the quiet rule (which is the definition of Phi), the age lemma rests, beyond (H1)-(H5), only on
its healing rule (the class of components on which R acts is the class with Phi = 0), which is Balaban's definition of
that class (CMP 122a p. 177) read as the account reads it.

## Step 5. Third item: the step (*) of 8.8:lem-target-independence (written 2026-11-20, 12:21Z by date -u)

**5.0 Item.** `8.8:lem-target-independence` (CA-II:109661-109712), "Stated; proof incomplete at the step marked (*)";
registry row H-C7b (owner none, OPEN; tree node "R9 witness analytic inputs"). Rule 0a: no FINISH row and no
`library/open-core.md` entry names it. The proof treats g_k, Ř_k, eps_k, delta_k explicitly and says: "Fourth, by the
step marked (*), delta'_k and the per-scale integers N_0 are defined from (g_j)_(j<=k) and the partitions". So the open
content of (*), as the proof uses it, is two definitions.
Moves: H-C7b. Success: the two objects are shown to be functions of (x_i)_(i<=k), the fixed constants and the
partitions. Failure: one of them reads the target coupling or the stopping level.

**5.1 READ (CMP 122a, page images).** p. 183: "where delta'_j = g_j A_1 p_1(g_j), p_1(g_j) = (log g_j^(-2))^(p_1), and
p_1 < p_0". p. 179: "Take the smallest positive integer N_0 such that L^(-N_0+1) M R_(k-N_0+1) = M. It is easy to see that
either there is exactly one such integer, or there are two."

**5.2 Lemma TI8 (the (*) of 8.8, for the objects the proof reads). PROVED GIVEN 5.1, CMP 119 (2.5) and the account's
Ř_j = R(min over i <= j of x_i).**
(a) delta'_k = g_k A_1 (log g_k^(-2))^(p_1) is a function of x_k = g_k^(-2) and of the fixed constants A_1, p_1.
(b) Write R_j = L^(a_j) (R_j is a power of L by (2.5)). Then L^(-N_0+1) R_(k-N_0+1) = 1 (that is, = M/M) iff
a_(k-N_0+1) = N_0 - 1. Put f(n) := a_(k-n+1) - (n - 1) for 1 <= n <= k. Then f(1) = a_k >= 0, and
f(n+1) - f(n) = (a_(k-n) - a_(k-n+1)) - 1 lies in {-1, 0}, because R drops by at most one factor L per step
(CA-II, Definition 8.6:not-local-run: "Ř_(j+1) >= L^(-1) Ř_j") and does not increase (Ř is a running-minimum function).
So f is non-increasing with steps 0 or -1; if f(k) <= 0, that is a_1 <= k - 1, then f takes the value 0, and N_0, the
least n with f(n) = 0, exists and is a function of (a_j)_(j<=k), hence of (x_i)_(i<=k) and L. The value 0 is taken at
one n, or at two consecutive n when a drop step sits there; by Lemma ISO (4.6) drops are isolated, so never at three.
This is Balaban's "either there is exactly one such integer, or there are two".
(c) Neither definition reads the target coupling g, the stopping level K(x_0, g) - m, or the constant E of rho_0.
So, together with the account's own treatment of g_k, Ř_k, eps_k and delta_k (CA-II:109686-109692, read), every object
in the lemma's list is a function of (x_0, the bare count) and k, which is what the proof needs from (*). QED

**5.3 Scope.** The sentence marked (*) also says, more broadly, that "each object read by the k-th step" is so defined.
I checked only the objects the lemma lists and the proof uses. The condition a_1 <= k - 1 in (b) holds at every level
where Balaban's preparation is used (it needs N > N_0, CMP 122a p. 179); at earlier levels N_0 is not read. Standing:
proved by Claude, unchecked.

## Step 6. Summary, credits, check request (written 2026-11-20, 12:25Z by date -u)

**6.1 Verdict on the brief.** The Jaffe-Witten mass gap of four-dimensional SU(2) Yang-Mills is NOT proved here, and
nothing on the chain is disproved. Its open core, the infrared base datum ((N-phys) at every cutoff, or (SL) of row 1258
at one coupling), was not attacked head-on: every idea I had was on the record with a first failing step (Step 1.1,
ARGUED). The one unowned item of the ultraviolet carry, `9.1:prop-blind-site-expansions`, needs Balaban CMP 116, which
is not in the papers folder and which Project Euclid refused behind a bot check; it was set aside (Step 1.2).

**6.2 What was closed (three lemmas incomplete at a step (*) in Sussman and Alpoge's account, all owner none in the
registry).**

| Registry row, label | Result | Label | Rests on |
|---|---|---|---|
| H-C6a, `8.6:lem-prefactor-monotone` (CA-II:102730) | (8.6:eq-prefactor-monotone-a) holds with equality: by the account's own Definition, O_(O,X) is the factor outside the bracket of CMP 122b (1.72), which does not depend on the island family (Corollary H0); the step (*) is not needed. The finer comparison (3.4-3.7) is proved except on the old factor's band cubes inside the island core, which is Balaban's "combined with" step (3.8a) | PROVED GIVEN | the representation lemma the account's Definition cites; CMP 122b (1.72), read on the page image |
| H-C6a, same | Correction: the account names the wrong object ("CMP 122a (1.3)-(1.4)"); with that object the domination sentence fails on the island's core cubes (3.10); the preparation's own top function has the weaker threshold 3(1 - beta/2) eps_k eta^2 (Remark P); the threshold comparison it asks for is an identity (Proposition TI) | PROVED | CMP 122a pp. 178-184, CMP 119 p. 257 |
| H-C7c, `8.9:lem-age-lemma` (CA-II:112000) | (*) = the join bound (8.9:eq-age-lemma-4) holds for every n_1 >= 2, by a size argument (Theorem J with Lemmas ST, ISO), without Balaban's unproved containment claim; the birth rule (C_S = 4) and the preparatory bound also follow (Lemmas B, PR) | PROVED GIVEN | (H1)-(H5): S, sizes, conditions (i)-(ii), the clock, read from CMP 122a p. 177, CMP 122b pp. 384-387, CMP 119 (2.5)-(2.6), and the account's definitions |
| H-C7b, `8.8:lem-target-independence` (CA-II:109661) | (*) for the objects the proof reads: delta'_k and N_0 are functions of (x_i)_(i<=k), L, M and fixed constants (Lemma TI8) | PROVED GIVEN | CMP 122a pp. 179, 183; CMP 119 (2.5); the account's Ř |

The age lemma is also a standing hypothesis (a) of `9.1:thm-last-lattice-comparison`, which the gap lane's one-cutoff
carry reads (row 1233 Lemma 3.5). Its other hypotheses stay as recorded there, so the carry's input list loses one
"incomplete" item only.

**6.3 Not done, and why.** No cross-provider check. The account's proof lines outside the (*) steps were not
re-checked (they were read). For H-C6a the account's representation lemma and Balaban's regrouping in (1.72) ("equivalent,
but not equal" after the reversed Faddeev-Popov step, and his "combined with" step on the band cubes, 3.8a) are
inputs, not checked. For H-C7c the healing rule is used as the account states it. The broad sentence of the 8.8 (*) ("each object read by the k-th step") was checked
only for the objects listed. H-C6b (`8.6:lem-healed-islands-unread`) and H-C7a (`8.7:lem-translation-covariance`) were
read, not closed: their (*) steps are reviews of every rule of a step and of the account's history framework.

**6.4 Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (complete account
CA-II, CA-III at 31a47c543775): the lemmas, their proofs outside (*), the island representation, the clock and its
rules, and the routes they print. Tadeusz Balaban: CMP 119, CMP 122 (175-202 and 355-392), the objects and displays read
here. The lane's earlier rows cited in Step 0. The bot-check stop on CMP 116 follows FINISH Rules (Literature).

**6.5 Check request (for the lead).** One line-by-line check by gpt-6-astra of Steps 3, 4 and 5, re-reading on the page
images CMP 122a pp. 177-184, CMP 122b pp. 365, 377-379, 384-387, 390, and CMP 119 pp. 254-257. Points most likely to
fail: Corollary H0's reading of (1.72) (that the front factor is outside the island bracket) and 3.8a in Step 3; (H4)-(H5) in Step 4 (the reading of
condition (ii) as "the last N levels" and the join's parameter N = R_(n+1)); Lemma ISO's use of CMP 119 (2.6).

## Status log

- 11:38Z file created; 12:17Z first date -u read after Steps 0-4 (headings corrected, see the note at the top);
  12:21Z Step 5; 12:25Z Step 6; 12:29Z correction 3.8a and Corollary H0; 12:30Z Lemmas B and PR; 12:32Z note 3.8c (all by date -u).
- No numeric run. No subagent. Memory gate not needed. Scratch folders under /tmp only (account text, page images);
  nothing from them is committed.

RESULT: Row 1264 (Claude Opus 5.5 max, Mac mini worker 3, 11:38Z-12:33Z by date -u; author only, checked by no one; no numeric run, no subagent): the Jaffe-Witten mass gap of four-dimensional SU(2) Yang-Mills is NOT proved and nothing on the chain is disproved; the infrared base datum ((N-phys), or (SL) at one coupling) stays OPEN with no route off the record (ARGUED, Step 1), and the carry's unowned `9.1:prop-blind-site-expansions` is blocked here (CMP 116 behind a Project Euclid bot check). Closed instead, in Sussman and Alpoge's complete account (with Claude and Codex as authors of its text; after Balaban CMP 119, 122): H-C7c `8.9:lem-age-lemma`, whose (*) join bound (8.9:eq-age-lemma-4) is PROVED GIVEN stated readings (H1)-(H5) of Balaban's S, sizes, conditions (i)-(ii) and clock, for every n_1 >= 2, by a size argument (Theorem J, Lemmas ST, ISO) that avoids Balaban's unproved containment claim, together with the birth rule (C_S = 4) and the preparatory bound (Lemmas B, PR); the age lemma is also a standing hypothesis of the gap lane's one-cutoff carry input `9.1:thm-last-lattice-comparison`. H-C6a `8.6:lem-prefactor-monotone` holds with equality GIVEN the representation lemma its Definition already cites (Corollary H0: the factor outside the island bracket of CMP 122b (1.72) does not depend on the island family); the account's (*) names the wrong objects (PROVED: with CMP 122a (1.3)-(1.4) the domination fails on the island core, Proposition TI makes the threshold comparison an identity, and the preparation's own top threshold is 3(1 - beta/2) eps_k eta^2); the finer comparison leaves Balaban's "combined with" step on the old factor's band cubes OPEN (3.8a). H-C7b `8.8:lem-target-independence`: (*) PROVED GIVEN CMP 122a pp. 179, 183 for delta'_k and N_0 (Lemma TI8). OPEN: the mass gap and its infrared datum; the account's representation lemma; H-C6b and H-C7a (read, not closed); a cross-provider check of Steps 3-5. Output library/gap-mini-solve-aj-opus.md.
