lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T12:21Z

# gap-uv-rigidity-max: rigidity with kept ultraviolet data (queue row 1028)

Worker: Claude Fable 5.2, max effort, Mac mini worker 3, pinned at commit d8496276a.
Started 2026-11-16T00:21Z. Research-stage working state. Nothing here grants status.
No subagents. No commit, no push: the relay copies this file.

Marks used below: PROVED (every step written here, checkable by hand), ARGUED
(argument given, a named step not written out), OPEN, FAILS (with the failing step).

## Plan (at most eight steps; one step per response; each result is appended here)

Revised at the end of Step 1, after the exercise skill was read (the first plan listed the four tasks only; the
skill's steps are now folded in; still eight steps).

1. **Sources and scope** (skill steps 0 and 1): the read-first list, the duplicate check, the pinned definitions,
   the wall in plain and precise words, the open and closed lists.
2. **Inventory and reasoning up** (skill steps 2 and 3): what is known, with marks; what follows at once. The two
   structural lemmas are proved here: Lemma ALPHA (the minus-infinity end of a limit object is infrared) and
   Lemma REC (link (b)).
3. **Task (1), link (a)**: the exact statement, the uniformity it needs, the two-ended object, the blockers
   (Theorem D2, Lemma PT-inf, products), a counterexample in the class.
4. **Task (3), the free value**: Lemma FV (a hand bound for SU(2) and U(1) on a fixed lattice torus), the frozen
   values, and whether a constant D = c is a critical element.
5. **Task (4), controls**: compact U(1), frozen Q_8 and 2T, five dimensions; assumptions table and discard tests
   (skill steps 4 to 6).
6. **Routes and attempts** (skill steps 7 and 8): what survives, tried; the first lemma or the counterexample.
7. **Second pass** on every proof of this file (same session, so not a check), and corrections in place.
8. **Report** (skill step 9): plain words, verdict table, work items, credits, the RESULT line.

## Status block (one line per step; kept current)

1. Sources and scope: **done** (Section 1).
2. Inventory and reasoning up: **done** (Section 2). PROVED here: Lemma ALPHA, Corollary KEPT, Lemma REC (link (b)).
3. Task (1): not started.
4. Task (3): not started.
5. Task (4): not started.
6. Routes and attempts: not started.
7. Second pass: not started.
8. Report: not started.

**Nothing in this file is checked by another model.**

## 1. Step 1 result: sources, scope, the wall

### 1.1 How the exercise skill is applied

Skill text: `docs/ai_methodology/skills/exercise/SKILL.md` at main commit 8b11ae2bb9, fetched by URL into the new
folder `/tmp/ym4d-w3-uvrig/skill/` and read in full (703 lines). The files it names were fetched into
`/tmp/ym4d-w3-uvrig/skillref/`: `skills/physics-loop/references/proof-search-governance.md` (read in full),
`RULES.md` and `skills/SKILL_FRESHNESS_CHECK.md` (fetched, not needed beyond the skill's own quotations). This target
is a standalone proof target, so `GOAL.md` and the FINISH rules replace the framework refresher read (the skill allows
this and asks that it is said). No subagents: the passes of skill step 7 are passes of this one session and are not
independent. No blind check of the plain version can run.

The wall has had five exercises (rows 878, 998, 1003, 1011, 1017) and one invention row (1013). By skill step 0 ("do
not re-derive a mapped wall") their inventories and set-aside lists are reused. This row runs the skill on one
question only: the lead's reading (a)-(b)-(c) of the queue row, which starts from item 20 of the gpt-6-astra check
of row 1017.

### 1.2 What was read (at commit d8496276a)

Read in full: `GOAL.md`; `FINISH.md` L1-84 and L299-354 and the queue row L1109 (row 1028); `parts/gap.md`;
`library/gap-compact-rigidity-max.md` (row 1017, 499 lines); `library/gap-compact-rigidity-check-opus.md` (row 1019);
`library/gap-compact-rigidity-check-astra.md` (597 lines; item 20 is L387-404); `library/gap-zd-astra.md` item 18
(L403-420, the repaired (W)); `library/gap-dichotomy.md` L1-300 (the statements and the proofs by citation).
Read in part: `library/gap-phys-seed.md` L61-116 (the tori of the account, (UV-Z), 1.1.5, Section 1.2 "the small end");
`library/gap-ladder-max.md` L213-222; the head of FINISH rows 1024-1027. Row 1025 (`gap-cr-tomboulis-max`) has no
RESULT at this pin; it is not read and not redone.

### 1.3 The statements this note reads (file and line)

"R" = `library/gap-compact-rigidity-max.md`, "CO" = its Opus check, "CA" = its gpt-6-astra check, "Q" =
`library/gap-dichotomy.md`, "PS" = `library/gap-phys-seed.md`.

- **Datum** (R L133-143; Q L85-88): a positive function Z on quadruples of integers at least 3 with (E1) symmetry,
  (E2) Z(k, B) = sum over r of lambda_r(B)^k with lambda_0 > lambda_1 >= ... >= 0, (E3) f = inf log Z(n)/abs(n) finite.
  Delta(n) = log Z(n) - f abs(n) >= 0; D(a) = Delta(a, a, a, a); levels E_r(B) = - log lambda_r(B) + f abs(B).
- **Family with units, (S0)** (Q L92-101): data Z_j, integers u_j = l_1/a_j with l_1/(4 a_j) an integer at least 3 for
  large j; P = {2^i l_1 : i >= 0}; D^+(L) = limsup over j of D_j(L/a_j); z^-(L) = liminf of (L/a_j) m_j((L/a_j)^3).
- **(PHYS-SEED), (BDD-Delta), (Z-UNB)** (Q L114-118). **(W), repaired** (`gap-zd-astra.md` L413-414): there are a bound
  (L_0, D_0) of (BDD-Delta) and L in P with L >= 4 L_0 and z^-(L) > 256 D_0 + 30.
- **Rescaling, admissible sequence, Omega(D_0), sigma, critical element** (R L145-158; Q L123-134, with the repairs
  D1, D2, D8 of CO): Delta^(j,k)(x) = Delta_j(2^k u_j x); (j_i, k_i) with j_i, k_i -> infinity, (H1) D^(j_i,k_i)(2^m)
  <= D_0 + 1/i and (H2) s^(j_i,k_i)(2^m) >= 1/5041 for i >= i(m); Omega(D_0) = the pointwise limits on DD^4;
  (sigma E)(x) = E(2x).
- **Uniformly recurrent** (R L230, Proposition OM (d); Q L135-136): for every finite set of quadruples and every
  eps > 0, the integers t with abs(sigma^t E - E) < eps on that set have bounded gaps. By the proof (R L236; CA
  L262-271) every interval of 2N + 1 consecutive integers holds such a t; so the return times are unbounded in
  both directions.
- **Theorem CE, Proposition OM, Theorem CR, Corollary TRI, Lemma LV, Lemma PT-inf, Proposition SI** (R 3.3-3.7, 4.1,
  5.1, 6.1), with the verdicts of CO (first failing step none) and CA (HOLDS AFTER CORRECTION).
- **(LIOU)** (R L288, L380): Wilson SU(2) on the account's trajectory, with (BDD-Delta), has no uniformly recurrent
  element in Omega(D_0).
- **Item 20 of CA** (L387-404), the source of this row: Proposition SI HOLDS; the inference "no boundary condition at
  one end of the scale axis is a kept property" FAILS: "lim_(m -> -infinity) D(2^m) = c is already shift-invariant";
  "The bounds in CE do not establish preservation of the trajectory's ultraviolet normalization. If a specified UV
  law forces D to diverge at small scales, CE's uniform bound excludes that law; neither SI nor this check proves
  such a UV law for Wilson." CO has the same point (D14, L203, L240), with the reason: "the small scales of a
  blow-down limit are large physical sizes of the trajectory".
- **The trajectory and its unit** (PS L63-66; `gap-ladder-max.md` L215): the unit of length is the first-passage
  scale, where the running inverse coupling first enters the window [g^(-2), g^(-2) + B_sharp]; g is small and fixed;
  K_j -> infinity. The account's tori have side l = 2 L^m (L odd) above a floor l_*(g); (UV-Z): log Z of such a
  torus is known to an additive error C l^4. "No step of the account integrates the scales between 1 and l."
- **The small end, as the lane holds it** (PS 1.2, L98-113; RECALLED physics and GUIDE, "no proof step uses it"): on
  small physical tori S and Delta grow like a multiple of log(1/g(L)); "My count on a fixed lattice at large beta
  gives kappa = 3 ... This count is not a proof" (L109).

### 1.4 The lead's reading, as the row states it (to test, not a conclusion)

(a) The account's ultraviolet normalisation passes to the blow-down limits as an asymptotic condition at
m -> -infinity. (b) A uniformly recurrent element with a limit c at minus infinity has D constant, equal to c.
(c) So (LIOU) reduces to excluding one constant critical element with the free value c.

### 1.5 The wall, twice (skill step 1)

**Plain version.** We want to show that the four-dimensional SU(2) theory has no massless particle. The lane has
shown: if it had one, there would be a "limit picture" of the theory at very large sizes that looks almost the same
at all scales. To finish, one must show that SU(2) has no such picture. Every tool so far fails, because a photon is
such a picture. SU(2) differs from a photon at very small sizes: its force gets weak there in a known way. The
question of this row: does that small-size knowledge survive in the limit picture, as a condition on its small-scale
end? If it did, the limit picture would be pinned to one number, and one could hope to exclude it. Getting past the
wall here means: a proof that the small-size knowledge survives, or an exact reason why it does not.

**Precise version.** Target: (LIOU) of R L288, equivalent to (W) given (BDD-Delta) (Theorem CR; CO, CA). The
question: is there a condition of the form "lim as m -> -infinity of Lambda(sigma^m E) = c" (Lambda continuous on
Omega(D_0), c computed from the ultraviolet data of the trajectory) that holds for every E in Omega(D_0) of the
Wilson SU(2) trajectory? Allowed premises: the lane's checked statements; the account's statements as cited
(unchecked); published theorems, rebuilt or named. Forbidden: a computer-assisted step; a statement with a supremum
over tilts (Theorem D2) or uniform over coupling fields (Lemma SHEET). Comparison cases: compact U(1), frozen Q_8 and
2T, products with a massless factor, five dimensions. Completion: a proof of (LIOU), or a proof that link (a) is
equivalent to a named open statement, or a counterexample to a link. Not closure: a renamed crux.

### 1.6 Open and closed lists (skill step 0)

- **Open now:** the files of 1.2 (the row names them as "read first"; they hold the statement of the wall and the
  checked compactness chain).
- **Closed until the comparison in Step 5:** `library/gap-crux-fp.md` (the five-dimensional test), the bodies of rows
  988, 1002, 1003, `library/gap-brainstorm*-max.md`, `library/prior/gap-kflow-read-opus.md`,
  `library/gap-cr-tomboulis-max.md` (row 1025, running; never opened for attack).

### 1.7 Duplicate-attack check (rule 0a)

`grep -n -i -E "uniformly recurrent|critical element|LIOU|ultraviolet normali|asymptotic condition|free value|
blow-down|rigidity" library/open-core.md`: no hit. FINISH rows naming "uv-rigidity", "ultraviolet normali", "free
value", "LIOU" or "uniformly recurrent": 1017, 1019, 1021, 1023, 1024 and this row 1028. Rows 1021 and 1023 are
registry rows; 1024 is a writing row. No other row attacks links (a), (b), (c). Row 1025 uses Theorem CR with the
decimation line; I do not touch decimation, (K-RESP), (SER) or (SPR). (LIOU), (BDD-Delta), (CAS), (MONO-Delta) and
(W) are held by earlier rows; where a step below reduces to one of them, I name the match and stop there.

### 1.8 Working notes at the end of Step 1 (candidates, nothing proved yet; kept so that a lost response loses nothing)

- N1. For E in Omega the limit points of sigma^t E as t -> -infinity lie in Omega (Omega is compact and sigma-
  invariant). So the minus-infinity end of a limit object is made of infrared limit points of the trajectory. To
  prove in Step 2 (Lemma ALPHA).
- N2. Link (b) looks true and short: recurrence gives return times t -> -infinity, and D_(sigma^t E)(b) = D_E(2^t b).
  To prove in Step 2 (Lemma REC). Stronger: if sigma^t E converges as t -> -infinity, E is a fixed point.
- N3. Link (a) then reads: "the ultraviolet value c is attained by D on Omega". For SU(2) the free value looks
  infinite (the constant modes of the torus; PS L109 has the count kappa = 3), so (a) would be equivalent to
  "Omega is empty". To settle in Steps 3 and 4. A hand proof of D(n; beta) >= (3/2) log beta - C(n) on a fixed
  lattice torus looks feasible (a packing bound for Z near the flat connections; a bound of f by a shelling of
  plaquettes).
- N4. A counterexample to (a) in the class: a product of the data A_(m,eps) of R 3.7 with a seeded factor that has a
  non-zero Casimir free energy at small sizes. The trajectory's small-size value is log(m p), the limit is log m.
- N5. Frozen groups: at beta = infinity the datum is the constant log(abs(Hom(Z^4, G))/abs(G)): log 8 for Z_2;
  by a centraliser count 736/8 = 92 for Q_8 and 5856/24 = 244 for 2T (to re-derive in Step 4).
- N6. Controls: for U(1) with beta_j -> infinity and for five dimensions at weak coupling the same count makes D
  unbounded, so these families would sit in branch (II) of the trichotomy, not in (III). To examine in Step 5.

## 2. Step 2 result: inventory, and what follows from it (skill steps 2 and 3)

Written with the attack files of 1.6 closed. Everything in 2.2-2.4 is proved by hand here from Proposition OM (a)
(Omega(D_0) is compact and metrisable, sigma is a homeomorphism of it onto itself; R L227, L233, with repair D1) and
the definition of uniform recurrence. No run was made.

### 2.1 Inventory (items this question reads; marks as in the skill)

| # | Item | Mark | Source | Standing, reading state |
|---|---|---|---|---|
| I1 | Datum, family with units, (S0), Omega(D_0), sigma, critical element, uniformly recurrent | DEF | 1.3 above | - |
| I2 | Theorem CE, Proposition OM (a)-(e), Theorem CR, Corollary TRI, Lemma LV | THM, lane | R 3.3-3.6, 5.1, 6.1 | checked: CO (same provider, first failing step none), CA (cross-provider, HOLDS AFTER CORRECTION); read in full |
| I3 | Proposition SI holds; "no condition at one end of the scale axis is kept" does not follow from it | THM, lane | R L280-282; CA item 20; CO D14 | checked as stated; read in full |
| I4 | Lemma PT-inf: the limit of a product is the sum; a uniformly seeded factor contributes 0 | THM, lane | R L257-262 | CA item 19: HOLDS AFTER CORRECTION (both indices diverge; a uniform seed) |
| I5 | The data A_(m,eps); the constants log m (m an integer, m >= 2) are critical elements | THM, lane | R L253 | CA item 21, CO 7.1: HOLDS |
| I6 | (TH): on the account's tori (side 2 L^m, above the floor) D is bounded at each fixed physical size, given (UV-Z) and the density statement | THM given the account | PS L92; `gap-ladder-max.md` L150 | conditional; two assumptions unchecked (PS check, row 727) |
| I7 | (BDD-Delta) | OPEN; BELIEF for SU(2) | PS L316-318 | - |
| I8 | On small physical tori D grows like kappa log(1/g(L)), kappa = 3 | BELIEF (GUIDE) | PS L109 | "This count is not a proof"; Lemma FV of Step 4 proves the lattice form |
| I9 | Small-volume expansion: the low levels of the periodic torus are those of the nine constant modes, energies of order g^(2/3)/L | THM, published, recalled | Luscher; van Baal (as quoted at PS L100-105) | not re-read here |
| I10 | Compact U(1), Villain, beta >= 2^14: a massless phase | THM, published, recalled; lane row 786 for the Langevin form | `parts/gap.md` L207 | not re-read here |
| I11 | Frozen Z_2 at large beta: eight degenerate flux sectors on every periodic box | THM, lane (Peierls) | `parts/gap.md` L210 | recalled here |
| I12 | Frozen Q_8, 2T: at least two centre-even flat states at every box in the frozen limit; order-one couplings | frozen limit: check 884; order one: BELIEF | `parts/gap.md` L211 | Step 4 counts the flat states exactly |
| I13 | SU(2) Wilson in five dimensions at weak coupling has massless gluons | BELIEF (numerics) | R L95 (A17); `gap-crux-fp.md` F15 | closed until Step 5 |
| I14 | Theorem D2 (a hypothesis with a supremum over tilts is false); Lemma SHEET (uniform over coupling fields is false) | THM, lane | `parts/gap.md` L215-216 | D2: HOLDS AFTER CORRECTION (cross-provider); SHEET: same-provider check |
| I15 | The trajectory is one orbit: the unit is the first-passage scale at a fixed small g; the account controls log Z of its tori to an additive error C l^4; it integrates no scale between 1 and l | THM given the account, as quoted in the lane | PS L63-66, L74 | the account's TeX was not opened in this run |
| I16 | The lead's reading (a)-(b)-(c) | SUPPLIED (a reading to test) | queue row 1028 | - |
| I17 | "Ultraviolet normalisation" read as a value of D, and Lambda = D as the functional | SUPPLIED (a choice) | queue row 1028 | other functionals are covered by Corollary KEPT below |

### 2.2 Lemma ALPHA (the minus-infinity end of a limit object is infrared; PROVED given Proposition OM (a))

Fix a family with units and D_0, and write Omega = Omega(D_0). For E in Omega let alpha(E) be the set of all
pointwise limits on DD^4 of sequences sigma^(t_n) E with t_n -> -infinity.

- (i) alpha(E) is not empty, closed, and sigma(alpha(E)) = alpha(E). It lies in Omega.
- (ii) Let Lambda be a continuous real function on Omega. The limit points of the numbers Lambda(sigma^t E), as
  t -> -infinity, are exactly the values Lambda(E'), E' in alpha(E). So lim as t -> -infinity of Lambda(sigma^t E) = c
  if and only if Lambda = c on alpha(E).
- (iii) Every E' in alpha(E) is the limit of an admissible sequence (j'_i, k'_i) of the same family with the same
  bound D_0: E'(x) = lim over i of Delta_(j'_i)(2^(k'_i) u_(j'_i) x), with j'_i -> infinity and k'_i -> infinity.

Proof. (i) Omega is compact and metrisable and sigma^t E lies in Omega for every integer t (OM (a)). So the sequence
sigma^(-n) E has a convergent subsequence, and its limit lies in Omega because Omega is closed. alpha(E) is the
intersection over T of the closures of {sigma^t E : t <= -T}; so it is closed. If sigma^(t_n) E -> E', then
sigma^(t_n + 1) E -> sigma E' and sigma^(t_n - 1) E -> sigma^(-1) E', because sigma and its inverse are continuous;
and t_n + 1, t_n - 1 tend to -infinity. So sigma and sigma^(-1) map alpha(E) into itself.
(ii) Let c be a limit point: Lambda(sigma^(t_n) E) -> c with t_n -> -infinity. A subsequence of sigma^(t_n) E
converges, to some E' in alpha(E), and Lambda(E') = c by continuity. Conversely, for E' in alpha(E) the number
Lambda(E') is the limit of Lambda(sigma^(t_n) E) along the sequence that defines E'. Lambda is bounded on the compact
set Omega, and a bounded sequence converges to c exactly when c is its only limit point.
(iii) alpha(E) lies in Omega, and Omega is by definition the set of limits of admissible sequences. QED

**What (iii) says in units.** D_E(2^m) = (sigma^m E)(1, 1, 1, 1) = Lambda_D(sigma^m E), where Lambda_D(E) := E(1, 1, 1, 1)
is a coordinate, hence continuous. By (ii) and (iii), every limit point of D_E(2^m), as m -> -infinity, is a number
lim over i of D_(j'_i)(2^(k'_i) u_(j'_i)): a limit of Casimir free energies of lattice tori of the trajectory whose
physical side 2^(k'_i) l_1 tends to **infinity**, on lattices j'_i -> infinity. The ultraviolet sizes of the trajectory
(physical sizes that tend to 0) occur at no fixed scale of E and at no point of alpha(E).

### 2.3 Corollary KEPT (which asymptotic conditions at minus infinity are kept; PROVED)

Let Lambda be continuous on Omega and c a real number. Write (ASY; Lambda, c) for the statement "for every E in
Omega: lim as t -> -infinity of Lambda(sigma^t E) = c". Let A be the union of the sets alpha(E), E in Omega.

- (1) (ASY; Lambda, c) holds if and only if Lambda = c on A.
- (2) If (ASY; Lambda, c) holds and Omega is not empty, there is E' in Omega with Lambda(sigma^s E') = c for every
  integer s. So c is a value of Lambda on Omega.
- (3) For Lambda = Lambda_D: if (ASY; Lambda_D, c) holds and Omega is not empty, then d_min <= c <= D_0, and there is a
  critical element E' of the trajectory with D_E'(b) = c at every dyadic b.
- (4) So if c > D_0 or c < d_min, then (ASY; Lambda_D, c) holds if and only if Omega is empty. The same holds for the
  statement "D_E(2^m) -> +infinity as m -> -infinity, for every E in Omega": it holds if and only if Omega is empty.

Proof. (1) is Lemma ALPHA (ii). (2) Take E in Omega and E' in alpha(E) (not empty). By ALPHA (i), sigma^s E' lies in
alpha(E) for every s, and Lambda = c there. (3) By (2) with Lambda_D, and Theorem CE (ii)(d): every element of Omega is
a critical element, so d_min <= D_E'(b) <= D_0. (4) If Omega is empty the statement is vacuous; if not, (3) gives
d_min <= c <= D_0. For the divergent form: D_E(2^m) <= D_0 for every m by CE (ii)(d). QED

Remark. This is the exact form of item 20 of CA. An asymptotic condition at minus infinity can be a kept property
(CA's example: on a limit set of constants the limit of D exists). But what it constrains is the set A inside Omega,
that is, limit objects taken at large physical sizes. It is a kept **ultraviolet** condition only if the ultraviolet
value of the trajectory is also a value that D takes on critical elements of the trajectory.

### 2.4 Lemma REC (link (b) of the lead's reading; PROVED)

Let E in Omega be uniformly recurrent (definition of OM (d): for every finite set F of quadruples and every eps > 0
the integers t with abs(sigma^t E - E) < eps on F have bounded gaps). Let Lambda be continuous on Omega.

- (i) If lim as t -> -infinity of Lambda(sigma^t E) = c exists, then Lambda(sigma^s E) = c for every integer s. In
  particular: if D_E(2^m) -> c as m -> -infinity, then D_E(2^m) = c for every integer m.
- (ii) The same holds with t -> +infinity.
- (iii) If sigma^t E converges pointwise as t -> -infinity (or as t -> +infinity), then sigma E = E: E(2x) = E(x) for
  every x in DD^4.
- (iv) With no convergence assumed: inf over all integers s of Lambda(sigma^s E) = liminf as t -> -infinity of
  Lambda(sigma^t E) = liminf as t -> +infinity; the same for sup and limsup.

Proof. (i) Fix an integer s and eps > 0. The function Lambda o sigma^s is continuous on Omega, so the set
U = {E'' in Omega : abs(Lambda(sigma^s E'') - Lambda(sigma^s E)) < eps} is an open neighbourhood of E. The topology is
that of pointwise convergence on the countable set DD^4, so U contains a set {E'' : abs(E'' - E) < eps' on F} with F
finite and eps' > 0. By uniform recurrence the return times of E to this set have bounded gaps. A set of integers
with bounded gaps is unbounded below. So there are t_n -> -infinity with abs(Lambda(sigma^(s + t_n) E) -
Lambda(sigma^s E)) < eps. As n grows, s + t_n -> -infinity and Lambda(sigma^(s + t_n) E) -> c. So abs(c -
Lambda(sigma^s E)) <= eps. This holds for every eps. (ii) The same, with return times t_n -> +infinity.
(iii) Apply (i) to each coordinate Lambda_x(E) := E(x): the limit c_x exists by hypothesis, so E(2^s x) = c_x for every
s; with s = 0 and s = 1, E(2x) = E(x). (iv) For each s and eps the proof of (i) gives t_n -> -infinity with
Lambda(sigma^(s + t_n) E) < Lambda(sigma^s E) + eps. So the lower limit at -infinity is at most Lambda(sigma^s E) for
every s, hence at most the infimum; it is at least the infimum trivially. The other three cases are the same. QED

Remarks. (1) The proof of (i) uses only that E returns to each of its neighbourhoods at times that are unbounded
below. (2) By (iv), on a uniformly recurrent element D takes no value that it does not come back to near both ends:
the two ends of the scale axis carry the same information as the whole orbit. So for a uniformly recurrent element
a condition "at one end" is a condition at every scale. This is the true part of the sentence of R L282 that CA
struck: it holds for uniformly recurrent elements, by recurrence, and not for all elements of Omega by Proposition
SI. (3) Link (b) is therefore right as the lead states it, and more is true: (iii).

### 2.5 What follows at once (skill step 3; each conclusion names its inputs)

- **C1 (ALPHA, KEPT; I1, I2).** The minus-infinity end of an element of Omega is made of elements of Omega. An
  asymptotic condition there is kept only as a condition on critical elements of the trajectory. It carries
  ultraviolet data only if the ultraviolet value is attained on Omega.
- **C2 (REC; I1, I2).** Link (b) holds. A uniformly recurrent element with a limit at one end is constant along its
  orbit in the functional concerned; with a pointwise limit it is a fixed point of the doubling.
- **C3 (KEPT (4); I2, I8).** If the ultraviolet value of D is infinite, or only larger than D_0, then link (a) for
  that value is equivalent to "Omega is empty", which is (W) given (BDD-Delta) (Theorem CR). Whether the value is
  infinite is I8 (a belief on the trajectory); Step 4 proves it on a fixed lattice.
- **C4 (the least a proof of (a) must contain).** A statement about the trajectory at physical sizes that tend to
  infinity (ALPHA (iii)). No statement about the trajectory at small sizes can prove (a) by itself. The two ends
  are joined only by the trajectory itself, one orbit. So a proof of (a) must carry a quantity along that orbit
  across every scale: a conserved quantity, a monotone (Remark MON of R L284), or a law that holds at each scale.
- **C5 (the smallest object where the wall bites).** A product of the data A_(m,eps) with a seeded factor that has a
  non-zero Casimir free energy at small sizes (note N4). Step 3 builds it.
- **C6 (price, to be made exact in Step 3).** Link (a) is not a weaker statement than the wall. With an infrared
  value c it is a plateau statement about the trajectory at large sizes; with an ultraviolet value outside
  [d_min, D_0] it is the wall.

Point where this step stops: the exact trajectory form of (a), its uniformity, the two-ended object and the
counterexample are Step 3.
