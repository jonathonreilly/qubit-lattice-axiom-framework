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
3. Task (1): **done** (Section 3). Link (a) FAILS as a kept condition (counterexample TS, PROVED); for a value outside [d_min, D_0] it is equivalent to (W) given (BDD-Delta) (PROVED); CE cannot be strengthened to keep it (Proposition TWO, Lemma EXCL, PROVED).
4. Task (3): **done** (Section 4). PROVED: Lemma FV (on a fixed lattice torus D(n; beta) >= (3/2) log beta - 59 n^4 - 11 for SU(2), beta >= 16: the free value is infinite); Proposition FRZ (frozen values log 8, log 92, log 244); Proposition CONST (a constant c is a critical element iff c = log m).
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

## 3. Step 3 result (Task 1): link (a), stated exactly; the uniformity it needs; why no construction keeps it

Everything in 3.1-3.6 is proved by hand here from Section 2, Theorem CE, Proposition OM and Theorem S. Nothing is
checked by another model. No run was made.

### 3.1 The exact statement of (a)

Fix the family with units, a bound (L_0, D_0) of (BDD-Delta), and Omega = Omega(D_0). An **ultraviolet value** is a
number c_UV computed from the trajectory at bounded physical sizes. Two forms occur in the row:

- (fixed size) c_UV = D^+(L_1) for one size L_1 of P "just above first passage";
- (limit) c_UV = the limit of D^+(L) as L -> 0, in [0, +infinity]. This needs sizes below l_1, so a finer grid:
  **(S0-Z)** for every integer i <= 0, 2^i u_j/4 is an integer at least 3 for all large j (depending on i);
  P_Z := {2^i l_1 : i in Z}. (The account's tori have side 2 L^m with L odd, PS L63, so (S0-Z) is not the
  account's setting. It is used here only to give the limit form a meaning.)

**Link (a), exact form.** (UV-KEPT; c_UV): for every E in Omega, D_E(2^m) -> c_UV as m -> -infinity. In the notation
of 2.3 this is (ASY; Lambda_D, c_UV). For another continuous functional Lambda (a twist ratio, s_*(1), z_*(1), which
are continuous on Omega by Lemma LV) the form is (ASY; Lambda, c_UV), and every statement below holds for it with
Lambda(Omega) in place of [d_min, D_0].

**Proposition A1 (what (a) is; PROVED, a restatement of Corollary KEPT).**

- (1) (UV-KEPT; c) holds if and only if Lambda_D = c on the set A of 2.3.
- (2) If Omega is not empty and (UV-KEPT; c) holds, then d_min <= c <= D_0, and a critical element E' of the
  trajectory has D_E' = c at every scale. E' is a limit of an admissible sequence; so D_(j_i)(2^(k_i + m) u_(j_i)) -> c
  for every integer m along that sequence (a plateau at the value c along one admissible sequence).
- (3) If c lies outside [d_min, D_0], or the ultraviolet law is "D diverges", then (UV-KEPT) holds if and only if
  Omega is empty. Given (BDD-Delta) with this bound, that is (W) (Theorem CR, (1) iff (3)).

So link (a) has two cases. With a value outside the range that critical elements allow, it is the wall in other
words. With a value inside the range, it asserts a plateau of D on the infrared limit objects, and the ultraviolet
enters only through the claim that the plateau value equals c_UV.

### 3.2 The uniformity in the trajectory that gives (a)

**(PLATEAU; c).** For every eps > 0 there are L_eps in P, an integer R_eps >= 0 and j_eps such that: for every
j >= j_eps and every L in P with L >= L_eps, if the lattice j has no seed at the size 2^(R_eps) L (that is,
S_j(2^(R_eps) L/(2 a_j); (2^(R_eps) L/a_j)^3) >= 1/5041), then abs(D_j(L/a_j) - c) <= eps.

**Proposition A2 (PROVED).** (i) (PLATEAU; c) implies D_E(b) = c for every E in Omega and every dyadic b, hence
(UV-KEPT; c). (ii) (UV-KEPT; c) with Omega not empty implies the plateau along one admissible sequence (A1 (2)).

Proof of (i). Let E be the limit of the admissible sequence (j_i, k_i), b = 2^m, eps > 0. For large i: j_i >= j_eps;
the size L := 2^(k_i + m) l_1 is in P and at least L_eps (k_i -> infinity); and (H2) at the scale m + R_eps says that
the lattice j_i has no seed at the size 2^(R_eps) L. So abs(D_(j_i)(2^(k_i + m) u_(j_i)) - c) <= eps for large i, and
abs(D_E(2^m) - c) <= eps. QED

In words: (a) needs that, far below the first seed size and far above the unit, the Casimir free energy of the
trajectory sits at one value. This is a statement at physical sizes that tend to infinity. It is not a statement
about the ultraviolet, and no ultraviolet statement gives it (3.4). I know no reason to expect it for SU(2). For a
theory whose coupling runs it says that the running stops.

### 3.3 The object that keeps the ultraviolet data, and why it cannot be recurrent

Three kinds of sequences can be extracted from the family, by the behaviour of k_i:

- k_i -> +infinity: the blow-down limits, Omega (Theorem CE). Every scale of the limit is infrared (Lemma ALPHA).
- k_i bounded: the continuum datum at fixed physical sizes (below).
- k_i -> -infinity: a zoom into the ultraviolet. If D diverges at small sizes there is no finite limit.

**Proposition TWO (the two-ended object; PROVED given (S0-Z) and (TH-Z)).** Assume (S0-Z) and **(TH-Z)**: D^+(L) is
finite for every L in P_Z. Then:

- (i) Along a subsequence J' of the lattices, Delta_j(u_j x) converges for every x in DD^4, to an eternal datum E_c
  with the spectral form of CE (b) in each direction.
- (ii) liminf over j of D_j(L/a_j) <= D_(E_c)(L/l_1) <= D^+(L) for every L in P_Z. So the minus-infinity end of E_c
  is the ultraviolet behaviour of the trajectory.
- (iii) If (PHYS-SEED) fails, J' can be chosen so that s_(E_c)(b) >= 1/5041 at every dyadic b.
- (iv) If (PHYS-SEED) fails and (BDD-Delta) holds with the bound (L_0, D_0), then the set omega(E_c) of limits of
  sigma^(t_n) E_c, t_n -> +infinity, is not empty, closed, sigma-invariant, and contained in Omega(D_0).

Proof. (i) Fix x with least entry mu. By A2 (R L80; valid for every datum, CO fact (F1)),
Delta_j(u_j x) <= (x_1 x_2 x_3 x_4/mu^4) D_j(u_j mu) <= (x_1 x_2 x_3 x_4/mu^4)(D^+(mu l_1) + 1) for large j. The rest is
Steps 1-4 of the proof of Theorem CE (ii) with these bounds: a diagonal subsequence on the countable set of
quadruples and levels, and the tail bound at the time T/2. (ii) A limit along a subsequence lies between the lower
and the upper limit. (iii) Take J' inside the subsequence of Lemma UF: for every l in P, S_j at the size l is at
least 1/5041 for all large j in it. For a size 2^i l_1 with i < 0: a seed there gives a seed at each doubling
(Theorem S; R L164), so a seed at l_1; so for large j in the subsequence there is none. The thermal sums converge
(Step 4 of CE), and the closed inequality passes to the limit. (iv) For 2^t mu l_1 >= L_0 the values
E_c(2^t x) <= (x_1 x_2 x_3 x_4/mu^4) D_0 are bounded, so limit points exist. Let sigma^(t_n) E_c -> E' pointwise,
t_n -> +infinity; pass to a subsequence with 2^(t_n - n) l_1 >= L_0. Enumerate DD^4 as x_1, x_2, .... For each n choose
j_n in J', j_n >= n, j_n > j_(n-1), so large that: abs(Delta_(j_n)(2^(t_n) u_(j_n) x_p) - E_c(2^(t_n) x_p)) <= 1/n for
p <= n; D_(j_n)(2^(t_n + m) u_(j_n)) <= D_0 + 1/n for abs(m) <= n; and the lattice j_n has no seed at the sizes
2^(t_n + m) l_1, abs(m) <= n. Each condition holds for all large j in J' (convergence at finitely many quadruples;
the upper limit in (BDD-Delta) at finitely many sizes, all at least L_0; Lemma UF). Then (j_n, t_n) is an
admissible sequence with the bound D_0, and its limit at x_p is the limit of E_c(2^(t_n) x_p), which is E'(x_p).
Closed and invariant: as in Lemma ALPHA (i). QED

**Lemma EXCL (the two properties exclude each other; PROVED).** Let E be an eternal datum.

- (i) If E returns to each of its neighbourhoods at times that are unbounded below (in particular if E is
  uniformly recurrent) and D_E(2^m) has a limit c as m -> -infinity, then D_E = c at every scale.
- (ii) If D_E(2^m) -> +infinity as m -> -infinity, then E does not return to its neighbourhoods at times that are
  unbounded below.

Proof. (i) is the proof of Lemma REC (i) for the coordinate Lambda_D; it uses no property of Omega. (ii) A return
at the time t to the neighbourhood {abs(E''(1, 1, 1, 1) - E(1, 1, 1, 1)) < 1} gives D_E(2^t) < D_E(1) + 1, which fails
for all t below some bound. QED

**Corollary A3 (the answer to "can CE be strengthened to keep it").** No. The object that keeps the ultraviolet
data is E_c (k_i bounded). If the Casimir free energy of the trajectory is not the same at all sizes, E_c is not
recurrent, so link (b) does not apply to it. The objects to which link (b) applies lie in Omega, and by Lemma ALPHA
their minus-infinity end is infrared. The two ends are joined by E_c alone: its minus-infinity end is the
ultraviolet, and its plus-infinity end omega(E_c) lies in Omega (TWO (iv)). No object has both properties, unless D
is constant from the ultraviolet to the infrared.

**Corollary CR-1 (the one-orbit form of Theorem CR; PROVED given Theorem CR; (S0-Z) is not needed).** Given (S0)
and (BDD-Delta) with the bound (L_0, D_0), (PHYS-SEED) fails if and only if some subsequential continuum datum E_c on
the sizes of P has no seed at any size of P. Then omega(E_c) is a non-empty closed invariant subset of Omega(D_0),
and it contains a uniformly recurrent element (the proof of OM (d) applies to any non-empty compact invariant
set).

Proof. If (PHYS-SEED) fails: TWO (i), (iii), (iv) on the sizes of P, where (TH-Z) is (BDD-Delta) from L_0 on and
finiteness of D^+ on the finitely many sizes below L_0; if D^+ is infinite at one of these, start the grid at L_0.
If (PHYS-SEED) holds at l with the margin q' < 1, then S_j <= q'/5041 at l for all large j, and every subsequential
limit has s(l) <= q'/5041 < 1/5041. QED

This is the form (R2-two) of row 1017 (R L319), now with its limit set: the wall is the statement that the
continuum datum of the trajectory, which is asymptotically free at one end, has a seed at the other.

### 3.4 What joins the two ends: only the orbit E_c (Remark MON as a statement)

**Proposition MON+ (PROVED given Proposition TWO).** Let Lambda be continuous on the closure of the forward orbit of
E_c, with Lambda(sigma^(t+1) E_c) <= Lambda(sigma^t E_c) for t >= t_0. Then Lambda is constant on omega(E_c), with the value
Lambda_IR := lim of Lambda(sigma^t E_c) = inf over t >= t_0. In particular: if D_(E_c)(2b) <= D_(E_c)(b) for b >= b_0,
then every element of omega(E_c) has D = c_IR := the limit of D_(E_c)(b) as b -> infinity, at every scale.

Proof. A non-increasing sequence that is bounded below converges. For E' in omega(E_c) and an integer s,
sigma^s E' = lim of sigma^(t_n + s) E_c, so Lambda(sigma^s E') = Lambda_IR by continuity. QED

So a constant D on the limit objects comes from **monotony** of D along the trajectory, and the constant is the
**infrared** limit of D. The ultraviolet data enter as the inequality c_IR <= D_(E_c)(b) for each b, and in no other
way. This is Remark MON of R L284 for the functional D, proved for omega(E_c). Monotony of D along the doubling is
(MONO-Delta), held by earlier rows (`parts/gap.md` L75); I do not attack it.

### 3.5 Counterexample in the class: the family TS (PROVED; an argued counterexample in the skill's words)

Let m_0 >= 2, p >= 2, rho >= 1 be integers, u_j integers that satisfy (S0) and (S0-Z) (for example u_j = 12 x 2^j), and
eps_j > 0 with eps_j -> 0. Put

 Z_j(n) = (1 + (m_0 - 1) exp(- eps_j abs(n)/u_j^4)) (1 + (p - 1) exp(- abs(n)/(rho u_j)^4)).

- **It is a family of data.** Each factor is a datum A_(m,eps) of R L253. A product of two data is a datum: the
  transfer matrices multiply as a tensor product, the top eigenvalue 1 is simple, f = 0 (CO fact (F2)).
- **Its continuum datum.** Delta_j(u_j x) = log(1 + (m_0 - 1) exp(- eps_j abs(x))) + log(1 + (p - 1) exp(- abs(x)/rho^4)),
  with abs(x) = x_1 x_2 x_3 x_4. As j grows this tends to E_c(x) = log m_0 + log(1 + (p - 1) exp(- abs(x)/rho^4)). So, with
  L in units of l_1: D^+(L) = log m_0 + log(1 + (p - 1) exp(- (L/rho)^4)).
- **Its ultraviolet value** is log(m_0 p), and log(m_0 p) - (p - 1)(L/rho)^4 <= D^+(L) <= log(m_0 p) for every L.
  (With y = (L/rho)^4 and w = (p - 1)(1 - e^(-y))/p: log(1 + (p - 1) e^(-y)) = log p + log(1 - w), and
  log(1 - w) >= - w/(1 - w) = - (p - 1)(1 - e^(-y))/(1 + (p - 1) e^(-y)) >= - (p - 1) y.) So D is within eps of
  log(m_0 p) on all sizes up to rho (eps/(p - 1))^(1/4) l_1: on as many doublings above the unit as one likes, by
  the choice of rho.
- **(BDD-Delta)** holds: D^+(L) <= D_0 := log m_0 + log(1 + (p - 1)/e) for L >= L_0 := rho l_1.
- **(PHYS-SEED) fails.** For a product 1 + S = (1 + S_1)(1 + S_2), so S >= S_1 = (m_0 - 1) exp(- eps_j l^4/2), which
  tends to m_0 - 1 >= 1 at every size l.
- **Its limit set.** Omega(D_0) = {the constant log m_0}. Proof. Let (j_i, k_i) be admissible and
  gamma_i := eps_(j_i) 16^(k_i). At the scale 2^m: s = (1 + (m_0 - 1) exp(- gamma_i 16^m/2))(1 + (p - 1) exp(- 16^(k_i + m)/(2 rho^4))) - 1.
  The second bracket tends to 1. If gamma_i did not tend to 0, take gamma > 0 and a subsequence with
  gamma_i >= gamma, and m so large that (m_0 - 1) exp(- gamma 16^m/2) < 1/10082; then s < 1/5041 for large i of the
  subsequence, against (H2) at this m. So gamma_i -> 0, and Delta^(j_i,k_i)(x) = log(1 + (m_0 - 1) exp(- gamma_i abs(x))) +
  log(1 + (p - 1) exp(- 16^(k_i) abs(x)/rho^4)) -> log m_0 for every x. The set is not empty: k_i = i and j_i increasing with
  eps_(j_i) <= 16^(-3i) is admissible ((H1): D <= log m_0 + (p - 1) exp(- 16^(i + m)/rho^4) <= D_0 + 1/i for large i;
  (H2): s >= (m_0 - 1) exp(- 16^(m - 2i)/2) -> m_0 - 1).
- **Verdict on (a) for TS.** The only element of Omega is the fixed point log m_0. It is uniformly recurrent, and
  its limit at minus infinity is log m_0. The ultraviolet value of the trajectory is log(m_0 p), and its value at
  every size up to rho eps^(1/4) l_1 is within eps of that. So (UV-KEPT; c_UV) is false for TS in both forms of 3.1.

Remarks. (1) TS has every property that Theorem CE keeps. So no proof of (a) can rest on those properties and on
the existence of an ultraviolet value. (2) TS is Lemma PT-inf (ii) read at the ultraviolet end: a seeded factor
adds to the ultraviolet value and adds nothing to the limit. Proposition NP's model (K copies of strong-coupling
SU(2) times ordered Ising, `library/gap-crux-exercise4-max.md` L383) has the same shape; TS is its abstract form
and is not a new idea. (3) In TS link (b) holds (the element is constant) and the conclusion of (c) is false in
the sense that matters: the constant element with the limit value exists.

### 3.6 The blockers named in the row

- **Lemma PT-inf and the product with a massless factor.** "A product's limit also has a limit at minus infinity":
  yes, and it shows where (a) breaks. Let X be the SU(2) trajectory and Y the family A_(m,eps_j) (or the photon at
  one coupling, given its limit). If X has a seed, the limit set of X x Y is that of Y (PT-inf (ii)): its elements
  have D = log m at every scale, while the ultraviolet value of X x Y is that of X plus log m. So for X x Y link (a)
  is false exactly when X has a seed. If X has no seed, the limits are sums, and (a) for X x Y holds if and only if
  it holds for X with the X-part of the value. So a proof of (a) that also runs for X x Y would decide whether X
  has a seed. This is the lead rule W2 once more (`parts/gap.md` L93): the proof must read the whole state space.
  Mark: PT-inf blocks (a) as a class-wide principle (TS); it does not refute (a) for SU(2) alone, where (a) with an
  ultraviolet value outside [d_min, D_0] is true exactly when the wall holds (A1 (3)).
- **Theorem D2** (`library/gap-tiltproof-max.md` L240: every covariance bound that is uniform over tilts obeys
  kbar >= lam_* k00). (UV-KEPT) and (PLATEAU) speak of the periodic partition functions only; they hold no supremum
  over tilts, pins or coupling fields. So Theorem D2 and Lemma SHEET do not bind them. They bind one way to prove
  the uniformity: a bound for the block free energy that is uniform over boundary data.
- **Proposition NP.** It binds any proof of (PLATEAU) or of monotony that reads finitely many values of D: its model
  contracts on J doublings and then stalls at log 2.

### 3.7 Result of Task 1

| Statement | Mark |
|---|---|
| Link (a) as a principle for families of data with the kept properties of Theorem CE | FAILS (the family TS; PROVED counterexample) |
| (UV-KEPT; c) with c outside [d_min, D_0], or with a divergent ultraviolet law, is equivalent to "Omega is empty", hence to (W) given (BDD-Delta) | PROVED (A1 (3), Theorem CR): target-equivalent |
| (UV-KEPT; c) with c in [d_min, D_0]: equivalent to "D = c on A"; implied by (PLATEAU; c); implies a plateau along one admissible sequence | PROVED (A1, A2); the statement itself is OPEN for SU(2), and it is an infrared statement |
| CE's construction strengthened to keep the ultraviolet data | FAILS: the object that keeps them (E_c, Proposition TWO) is not recurrent unless D is constant (Lemma EXCL); PROVED |
| The ultraviolet data reach the limit objects only along the one orbit E_c: as an inequality through a monotone | PROVED for a monotone functional (MON+); the monotone itself is (MONO-Delta), OPEN, not attacked |
| Blockers: PT-inf (class-wide), D2 and SHEET (do not bind (a); bind boundary-uniform proofs of it), NP | as stated in 3.6 |

Point where this step stops: the value c_UV itself (finite or not, for SU(2), U(1), frozen groups) is Step 4.

## 4. Step 4 result (Task 3): the free value c

Everything marked PROVED in 4.1-4.4 is proved by hand here. A guard run (4.6) checked the counts and four elementary
inequalities; it proves nothing. Nothing is checked by another model.

### 4.1 Lemma FV (the free value of SU(2) on a fixed lattice torus is infinite; PROVED)

Setting: Wilson SU(2) on the periodic torus with all four sides n >= 3, N = n^4 sites, 4N links, 6N plaquettes,
Z(n; beta) = integral over Haar probability measures of exp(- beta A), A = sum over plaquettes of (1 - (1/2) tr U_p).
F = log Z, f(beta) = inf over all tori of F/abs(n), D(n; beta) = F(n; beta) - f(beta) N.

**Lemma FV.** For every n >= 3 and every beta >= 16: D(n; beta) >= (3/2) log beta - 59 n^4 - 11.

So for each fixed number of sites, D(n; beta) tends to infinity as beta grows. Along any trajectory with
beta_j -> infinity (the account's lattices are at weak bare coupling, I15), D_j(n) -> infinity for each fixed n.

The proof has two parts: an upper bound for f (all scales, by a shelling of plaquettes) and a lower bound for Z on
the fixed torus (a packing of small balls around the flat connections).

**Notation.** Sites x in {0, ..., n-1}^4; the link (x, mu) joins x to x + e_mu (mod n). It is **interior** if
x_mu <= n - 2 and **wrapping** if x_mu = n - 1. The **comb tree** T: the interior links (x, mu) with x_nu = 0 for all
nu < mu. T has (n - 1)(n^3 + n^2 + n + 1) = n^4 - 1 links and joins every site to the origin (lower x_1 to 0 by links
of direction 1; then x_2 by links of direction 2 at x_1 = 0; and so on). So T is a spanning tree. For U in SU(2),
norm(U - V) is the operator norm. With eigenvalues e^(i phi), e^(-i phi) of U: norm(U - 1) = 2 abs(sin(phi/2)) and

 1 - (1/2) tr U = 1 - cos phi = (1/2) norm(U - 1)^2.   (4.1)

The map U -> phi in [0, pi] carries Haar measure to (2/pi) sin^2 phi d phi. SU(2) is the unit sphere S^3 of the
quaternions, Haar measure is the normalised surface measure (total surface 2 pi^2), and norm(U - V) is the Euclidean
distance of the two unit quaternions (a quaternion q, as a 2 x 2 matrix, has q q* = abs(q)^2).

**Part A (f from above).** Put I(beta) := integral over SU(2) of exp(- beta (1 - (1/2) tr U)) dU.

(A1) I(beta) <= (pi/2)^(5/2) beta^(-3/2), and I(beta) <= 1. Proof: I = (2/pi) integral from 0 to pi of
sin^2 phi exp(- beta (1 - cos phi)) d phi. On [0, pi]: sin^2 phi <= phi^2, and 1 - cos phi = 2 sin^2(phi/2) >= 2 phi^2/pi^2
(sin is concave on [0, pi/2]). So I <= (2/pi) integral from 0 to infinity of phi^2 exp(- 2 beta phi^2/pi^2) d phi
= (2/pi)(sqrt(pi)/4)(pi^2/(2 beta))^(3/2) = (pi/2)^(5/2) beta^(-3/2).

(A2) **Shelling.** Let l = (x, mu) be an interior link that is not in T. Then mu >= 2 and some x_nu > 0 with nu < mu.
Let nu be the least such index, and p(l) the plaquette with the corners x - e_nu, x, x + e_mu, x - e_nu + e_mu. Its
links are (x - e_nu, nu), (x, mu), (x - e_nu + e_mu, nu), (x - e_nu, mu); all are interior. The two links of direction nu
start at sites whose coordinates below nu are those of x, namely zero; so both lie in T. Hence p(l) holds at most
two links outside T: l, and l' := (x - e_nu, mu). The map l -> p(l) is one-to-one: if p(l_2) = p(l_1) with l_2 not l_1,
then l_2 = l_1' = (x - e_nu, mu), and p(l_2) has its lower corner at x - e_nu - e_nu' for some nu', which is not the
lower corner x - e_nu of p(l_1). Put h(l) := x_1 + x_2 + x_3 + x_4; then h(l') = h(l) - 1. List the interior links
outside T as l_1, ..., l_M with h non-decreasing. Their number is M = 4 n^3 (n - 1) - (n^4 - 1) = 3 n^4 - 4 n^3 + 1.
For i < k the link l_k does not lie in p(l_i): otherwise l_k = l_i', so h(l_k) < h(l_i), against the order.

(A3) Z(n; beta) <= I(beta)^M. Proof: each plaquette weight w(U_p) = exp(- beta (1 - (1/2) tr U_p)) is at most 1. Drop
all weights except those of p(l_1), ..., p(l_M). Integrate over U_(l_M) first, the other links fixed. By (A2) it occurs
in the weight of p(l_M) only, as tr(U_(l_M) W) or tr(U_(l_M)^(-1) W) with W a product of other links. Haar measure is
invariant under translation and inversion, so this integral is I(beta), whatever the other links are. Repeat with
l_(M-1), ..., l_1. The remaining links integrate to 1.

(A4) f(beta) <= 3 log I(beta) <= 3.42 - (9/2) log beta. Proof: f <= F(n)/n^4 <= (3 - 4/n + n^(-4)) log I(beta) for every
n, by (A3) and log I <= 0. The right side decreases to 3 log I(beta) as n grows... more exactly it is at least
3 log I for each n and tends to 3 log I; f is at most each of its values, hence at most their limit. With (A1):
3 log I <= (15/2) log(pi/2) - (9/2) log beta, and (pi/2)^(5/2) < 3.1 (as 1.5708^5 < 9.57 < 3.1^2), log 3.1 < 1.14.

**Part B (Z on the fixed torus from below).**

(B1) **Tree gauge.** Z(n; beta) = integral over the 3N + 1 links outside T of exp(- beta A(V)), with V_l = 1 on T.
Proof: for a site x let g_x(U) be the product of the link variables along the path of T from the origin to x; it
depends on the links of T only. Put V_l = g_x U_l g_y^(-1) for a link l from x to y. Then V_l = 1 on T, and A(V) =
A(U) (A is gauge invariant). For fixed links of T, each V_l with l outside T is U_l multiplied on both sides by
fixed elements, which preserves Haar measure. Integrate over the links outside T first, then over T (total mass 1).

(B2) **Flat points of the slice.** Let H = (H_1, ..., H_4) be commuting elements of SU(2). Define U^H by: U^H_l = 1 on
every interior link, U^H_l = H_mu on every wrapping link of direction mu. Every plaquette of U^H is 1: in a
plaquette of the plane (mu, nu) the two links of direction mu are both interior or both wrapping, so both equal one
element a_mu in {1, H_mu}; the same for nu; and a_mu a_nu a_mu^(-1) a_nu^(-1) = 1. U^H is 1 on T (interior links).

(B3) **Balls.** For r > 0 let NN(H, r) be the set of slice configurations V with norm(V_l - U^H_l) < r on every link
outside T. On NN(H, r): for each plaquette, norm(V_p - 1) <= sum over its four links of norm(V_l - U^H_l) < 4r
(telescoping for products of unitaries; norm(A^(-1) - B^(-1)) = norm(A - B); the product of the U^H is 1). By (4.1),
1 - (1/2) tr V_p < 8 r^2, and A(V) < 48 N r^2.

(B4) **Volume of a ball.** NN(H, r) is a product over the 3N + 1 links of balls {U : norm(U - U_0) < r}, each of Haar
measure v(r) := Haar{norm(U - 1) < r}. For r <= 1: v(r) >= (8/(3 pi^3)) r^3 > r^3/12. Proof: the ball is the cap of S^3
of angular radius alpha, r = 2 sin(alpha/2), alpha <= pi/3. Its normalised measure is (2/pi) integral from 0 to alpha
of sin^2 t dt >= (2/pi)(4/pi^2)(alpha^3/3), by sin t >= 2t/pi on [0, pi/2]; and alpha >= r. Last, 3 pi^3/8 < 12.

(B5) **Packing.** Let 0 < r <= 1/4 and delta = 4r. For theta in Theta := {pi/4 + k delta : k = 0, ..., [pi/(2 delta)]} and
a unit vector e in DD_delta := {(a, b, sqrt(1 - a^2 - b^2)) : a, b in {0, delta, 2 delta, ...}, a, b <= 1/2} put
h(theta, e) := cos theta + sin theta (e_1 i + e_2 j + e_3 k). For one e these elements commute. Let HH_r be the set of
tuples H = (h(theta_1, e), ..., h(theta_4, e)). Then:

- its number is at least (pi/(2 delta))^4 (1/(2 delta))^2 = (pi^4/64) delta^(-6) >= delta^(-6) = (4r)^(-6);
- for two different tuples H, H' there is mu with norm(H_mu - H'_mu) >= delta/2 = 2r. Proof: if e = e', some
  theta_mu differs from theta'_mu by t in [delta, pi/2], and the distance is 2 sin(t/2) >= 2t/pi >= delta/2. If e is not
  e', then abs(e - e') >= delta, and for every mu, with s = sin theta_mu, s' = sin theta'_mu in [1/sqrt 2, 1]:
  distance^2 >= abs(s e - s' e')^2 = (s - s')^2 + s s' abs(e - e')^2 >= delta^2/2;
- so the sets NN(H, r), H in HH_r, are pairwise disjoint: the wrapping link ((n - 1) e_mu, mu) is outside T, and
  U^H has the value H_mu there; a common point V would give norm(H_mu - H'_mu) < 2r for every mu.

(B6) By (B1), (B3)-(B5), for 0 < r <= 1/4: Z(n; beta) >= (4r)^(-6) (r^3/12)^(3N + 1) exp(- 48 N beta r^2). Take
r = beta^(-1/2) (so beta >= 16): Z(n; beta) >= 4^(-6) 12^(-(3N + 1)) e^(-48N) beta^(-(9N - 3)/2). So

 F(n; beta) >= - ((9N - 3)/2) log beta - 48 N - 6 log 4 - (3N + 1) log 12.

**End of the proof.** D = F - f N >= - ((9N - 3)/2) log beta - 48N - 6 log 4 - (3N + 1) log 12 - 3.42 N + (9N/2) log beta
= (3/2) log beta - (48 + 3 log 12 + 3.42) N - 6 log 4 - log 12. With log 12 < 2.5 (e^2.5 > 7.38 x 1.64 > 12) and
log 4 < 1.39: the constant is at most 58.92 N + 10.84 < 59 N + 11. QED

Remarks.

1. **Where the 3/2 comes from.** The slice has dimension 3(3N + 1) = 9N + 3. Its flat points form a set of dimension
   6 (four angles and an axis). So 9N - 3 directions are stiff, against 9N stiff directions in the bulk count of f.
   The three directions that are missing are 4 flat moduli minus 1 for the stabiliser of an abelian flat point.
2. **The count of PS L109 (kappa = 3 in log(1/g), that is, (3/2) log beta) is now a lower bound with a proof.** A
   matching upper bound is not proved here. The count at the singular flat points (the twelve constant modes with a
   quartic action) suggests D(n; beta) = (3/2) log beta + log log beta + O(1) for SU(2) in four dimensions: the
   integral over the constant modes is at its threshold of convergence there (Krauth and Staudacher, recalled).
   GUIDE only.
3. **Other groups and dimensions (ARGUED: the same proof with other counts, not written out).** For a compact
   connected group of dimension g and rank rho in d dimensions the slice has dimension g((d - 1) N + 1), the flat
   set g + (d - 1) rho, and f is at most - (g (d - 1)/2) log beta + C. So D(n; beta) >= ((d - 1) rho/2) log beta - C(N).
   For U(1) in four dimensions: (3/2) log beta again. For SU(2) in five dimensions: 2 log beta.
4. The constant 59 n^4 + 11 is far from sharp. The lemma is a statement of divergence, not a usable number.

### 4.2 What Lemma FV says about the trajectory, and what it does not

- PROVED given beta_j -> infinity: at each fixed number of sites n, D_j(n) -> infinity. These tori have physical side
  n a_j -> 0. So at the lattice end of the scale axis the Casimir free energy of the trajectory is unbounded: the
  **free value is c = +infinity**, in the lattice sense.
- Not proved: the behaviour of D^+(L) at a fixed small physical size L (the number of sites grows with j). There the
  lane has I8 (GUIDE): D^+(L) grows like 3 log(1/g(L)). The account bounds D on its own tori above the floor ((TH), I6)
  and gives no asymptotics.
- By Corollary KEPT (4) and Proposition A1 (3): with a divergent ultraviolet law, link (a) is equivalent to (W),
  given (BDD-Delta). With the value at one fixed size just above first passage, c = D^+(L_1), link (a) is the
  plateau statement of 3.2 at that value; the same statement at the size 2 L_1 gives the value D^+(2 L_1), and Omega
  is the same set for both. So (a) in that form forces D^+(L_1) = D^+(2 L_1) = ...: the Casimir free energy does not
  run. This contradicts I8 at belief grade; no proof step uses it.

### 4.3 Proposition FRZ (frozen values; PROVED)

Let G be a finite subgroup of SU(2), with the Wilson action and normalised counting measure. Let c_k(G) be the
number of k-tuples of pairwise commuting elements of G.

- (i) For every torus n: Z(n; beta) -> c_4(G) abs(G)^(-3 abs(n) - 1) as beta -> infinity.
- (ii) f(beta) -> - 3 log abs(G).
- (iii) Delta(n; beta) -> log(c_4(G)/abs(G)) for every torus n: the same number at every size.
- (iv) m(G) := c_4(G)/abs(G) is the number of orbits of G, acting by conjugation, on commuting triples. It is an
  integer. m(Z_2) = 8, m(Q_8) = 92, m(2T) = 244.

Proof. (i) By (4.1), 1 - (1/2) tr U > 0 unless U = 1. So exp(- beta A(U)) tends to 1 if every plaquette of U is 1 and
to 0 otherwise, and the sum is finite. Count the flat configurations with the map of (B1): U -> (links of T, V) is
a bijection onto G^(N-1) x (slice), and U is flat exactly when V is. A flat V in the slice is 1 on every interior
link: by induction on h, the plaquette p(l) of (A2) has its other three links in T or of lower h. Then a plaquette
with one wrapping link (x, mu) and interior links of direction nu gives V_(x,mu) = V_(x + e_nu, mu); the sites with
x_mu = n - 1 are joined by such steps, so the wrapping links of direction mu carry one element H_mu. A plaquette with
two wrapping directions gives H_mu H_nu = H_nu H_mu. With (B2): the flat points of the slice are the U^H, H a
commuting 4-tuple. So there are abs(G)^(N-1) c_4(G) flat configurations among abs(G)^(4N). The same holds for a torus
with unequal sides. (ii) exp(- beta A) is at least the indicator of the flat configurations, so F(n; beta) >=
- (3 abs(n) + 1) log abs(G) + log c_4, and f(beta) >= - 3 log abs(G) (c_4 >= abs(G): the tuples (h, 1, 1, 1)). And
f(beta) <= F(n; beta)/abs(n), whose limit is - 3 log abs(G) + log(c_4/abs(G))/abs(n), for every n. (iii) From (i), (ii).
(iv) Burnside's lemma: the number of orbits is the mean number of fixed triples, and a triple fixed by g is a
commuting triple in the centraliser of g; the pairs (g, triple) are the commuting 4-tuples. The counts use
c_k(G) = sum over g of c_(k-1)(C_G(g)), c_k(A) = abs(A)^k for A abelian, c_0 = 1:

- Z_2: c_4 = 16, m = 8.
- Q_8: the centre {1, -1} has centraliser Q_8; the six elements of order 4 have a centraliser of order 4. So
  c_k = 2 c_(k-1) + 6 x 4^(k-1): c_1 = 8, c_2 = 40, c_3 = 176, c_4 = 736. m = 92.
- 2T (order 24): {1, -1} with centraliser 2T; six elements of order 4 with a centraliser of order 4; sixteen elements
  (+-1 +- i +- j +- k)/2 with a cyclic centraliser of order 6 (the elements of 2T on their axis). So
  c_k = 2 c_(k-1) + 6 x 4^(k-1) + 16 x 6^(k-1): c_1 = 24, c_2 = 168, c_3 = 1008, c_4 = 5856. m = 244. QED

Remarks. (1) At beta = infinity the torus function is the constant log m(G). It is not a datum in the sense (E2) (the
top eigenvalue is m-fold); at large finite beta it is one. (2) m(G) is the number of flat states of the periodic
cube (flat connections of the three-torus up to gauge). The number log 8 for Z_2 is on record (R L255); 92 and 244
were not found on record (search in Step 5). (3) That the blow-down limit at a large finite beta is the constant
log m(G) is a Peierls statement: THM in the lane for Z_2 (I11), BELIEF here for Q_8 and 2T.

### 4.4 Proposition CONST (is a constant D = c a critical element? PROVED)

- (i) The constant function c on DD^4 is a critical element with the bound D_0 if and only if c = log m for an
  integer m >= 2 with log m <= D_0.
- (ii) No critical element with any bound has D = +infinity at a scale; so "the constant element with the SU(2) free
  value" does not exist.
- (iii) The engine's axioms, the centre grading and the spectral clause of the definition (repair D8) exclude a
  constant c exactly when e^c is not an integer at least 2. They exclude no constant log m.

Proof. (i) "If": the data A_(m,eps) of R L253 (CA item 21). "Only if": a critical element has the spectral form
e^c = sum over r of exp(- T e_r(B)) for every dyadic T. If e_0 < 0 the right side is unbounded in T; if e_0 > 0 it tends
to 0; so e_0 = 0. Then e^c minus the multiplicity of the level 0 equals the sum over the levels above 0, which tends
to 0 as T grows and does not depend on T; so it is 0, there is no finite level above 0, and e^c is the multiplicity
m. s_* = m - 1 >= 1/5041 gives m >= 2. (This is the remark of CO 6.4, L172, written out.) (ii) D_* <= D_0 in the
definition. (iii) From (i); the centre grading asks only for sign triples on the m levels with the vacuum even and
twisted sums in [0, m], which exist for every m (all levels even). QED

Remark (D constant on the diagonal only). Link (b) gives D_E(b) = c at every b; it does not make the whole datum
constant. The elements with D = c on the diagonal form a family: the constants log m; by Lemma PT-inf (i), sums of
these with limits of constant D; the photon limit at one coupling (BELIEF as a limit, I10). So even with (a)
granted, (c) is not "one element" for a finite c. For c = +infinity it is no element at all.

### 4.5 Result of Task 3

| Statement | Mark |
|---|---|
| SU(2), fixed lattice torus: D(n; beta) >= (3/2) log beta - 59 n^4 - 11 for beta >= 16; the free value is +infinity | PROVED (Lemma FV) |
| The same at a fixed small physical size of the trajectory | OPEN (I8, GUIDE); not needed for any verdict here |
| D(n; beta) = (3/2) log beta + log log beta + O(1) | GUIDE (count; no upper bound proved) |
| U(1) and five dimensions: the same lower bound with (3/2) and 2 | ARGUED (same proof, not written out) |
| Frozen values: log 8 (Z_2), log 92 (Q_8), log 244 (2T), the same at every size | PROVED (Proposition FRZ) |
| A constant c is a critical element iff c = log m, m >= 2 an integer; the SU(2) free value gives no element | PROVED (Proposition CONST) |
| For a finite c, link (c) names a family (D = c on the diagonal), not one element | PROVED for the constants and sums; the photon member is BELIEF |

### 4.6 Guard run (guide only; pre-registered readings; under the numeric lock)

Script `/tmp/ym4d-w3-uvrig/scripts/guard_step4.py`, output `guard_step4.out` beside it (scratch, not in the
repository). Memory free before the run: 68 percent. Lock: `python3 scripts/lab_ops.py numeric-lock acquire`,
status "acquired" at 2026-11-16T00:42:59Z, released after the run. Pure Python, one process, exact arithmetic for the
counts. Readings written in the script before the first run; all PASS on the first run:

- G1: by enumeration, c_1..c_4 = (2, 4, 8, 16), (8, 40, 176, 736), (24, 168, 1008, 5856) for Z_2, Q_8, 2T, and 8, 92, 244
  conjugation orbits on commuting triples. Agrees with the hand count of 4.3.
- G2: the shelling of (A2) on the open box for n = 3, 4, 5: tree connected with n^4 - 1 links; the two nu-links of
  p(l) are tree links; l -> p(l) one-to-one; the order property; M = 136, 513, 1376 = 3 n^4 - 4 n^3 + 1.
- G3: I(beta)/((pi/2)^(5/2) beta^(-3/2)) <= 0.26 on a grid of twelve beta in [0.5, 2000]. G4: v(r)/((8/(3 pi^3)) r^3) >=
  2.27 on (0, 1]. G5: the packing set for delta = 1, 1/2, 1/4, 1/8: least distances at least delta/2, counts at least
  delta^(-6).

What the run can establish: that the hand counts and these inequalities are not false at the tested points. It
does not prove Lemma FV, and a pass is no proof of any inequality on its whole range.
