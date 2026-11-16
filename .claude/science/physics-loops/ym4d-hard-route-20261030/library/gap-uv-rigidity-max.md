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
5. Task (4): **done** (Section 5). The chain is a sound tool in the valid form and passes every control; it proves nothing for SU(2), because its hypothesis (a) is the wall there. U(1) with beta_j -> infinity and five dimensions sit in branch (II) (GUIDE), a correction to row 1017's table.
6. Routes and attempts: **done** (Section 6). The surviving link is (b); its lemma is proved (REC, REC+). Five routes from the corrected picture; none survives as a route to (LIOU); the family is blocked-equivalent.
7. Second pass: **done** (Section 7). Eight repairs applied in place; no statement failed.
8. Report: **done** (Section 8 and the last line).

**Nothing in this file is checked by another model.** The list "what this run did not cover" is in 8.8. The
exercise skill at main commit 8b11ae2bb9 was followed as 1.1 says; `GOAL.md` and the FINISH rules replace the framework
refresher read, because this is a standalone proof target.

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

**What the account's normalisation is (from the lane's index of the account, `library/sa-index/chunk-06.md` rows
6854-6895; the TeX was not opened).** The first-passage datum is a definition, the dilation identity is proved in
detail there, and Theorem 0 lists a "nontrivial short-distance normalization" of correlations. That clause speaks
of correlations at small separations. The objects of Omega hold no observables (R L219), and the account "defines no
running coupling at the scale of the torus side itself" (PS L66). So the account's normalisation is not a statement
about D at all; a form in terms of D or of a twist ratio would need a new ultraviolet estimate at the scale of the
torus. Lemma FV (Step 4) is such an estimate on a fixed lattice. By Lemma ALPHA the answer below does not depend
on which ultraviolet functional is taken.

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
- (iv) If (PHYS-SEED) fails and (BDD-Delta) holds with the bound (L_0, D_0), and J' is chosen as in (iii), then the
  set omega(E_c) of limits of sigma^(t_n) E_c, t_n -> +infinity, is not empty, closed, sigma-invariant, and contained
  in Omega(D_0).

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

**Corollary CR-1 (the one-orbit form of Theorem CR; PROVED given Theorem CR; (S0-Z) is not needed).** Assume (S0) and
(BDD-Delta) with the bound (L_0, D_0). Let G_0 be the set of dyadic b with b l_1 >= L_0. A **continuum datum on G_0**
is a pointwise limit E_c of Delta_j(u_j x), x in G_0^4, along a subsequence of the lattices on which the lowest level
of every box converges too (so s_(E_c)(b), the limit of the thermal sums, is defined for b/2 in G_0). Then:
(PHYS-SEED) fails if and only if some continuum datum on G_0 has s_(E_c)(b) >= 1/5041 at every b with b/2 in G_0. In
that case omega(E_c) is a non-empty closed invariant subset of Omega(D_0), and it contains a uniformly recurrent
element (the proof of OM (d) applies to every non-empty compact invariant set).

Proof. If (PHYS-SEED) fails: the proof of TWO (i), (iii), (iv) on the grid G_0. There D^+ <= D_0, which replaces
(TH-Z); the sizes are in P, so Lemma UF applies as it stands; for each x and all large t the point 2^t x lies in
G_0^4, so omega(E_c) is defined on all of DD^4. If (PHYS-SEED) holds at l with the margin q' < 1, then by Theorem S,
S_j <= q'/5041 at every size 2^k l for all large j, so every continuum datum has s <= q'/5041 < 1/5041 at each such
size with half of it in G_0. QED

This is the form (R2-two) of row 1017 (R L319), now with its limit set: the wall is the statement that the
continuum datum of the trajectory, which is asymptotically free at one end, has a seed at the other.

### 3.4 What joins the two ends: only the orbit E_c (Remark MON as a statement)

**Proposition MON+ (PROVED given Proposition TWO).** Let Lambda be continuous on the closure of the forward orbit of
E_c, with Lambda(sigma^(t+1) E_c) <= Lambda(sigma^t E_c) for t >= t_0. Then Lambda is constant on omega(E_c), with the value
Lambda_IR := lim of Lambda(sigma^t E_c) = inf over t >= t_0. In particular: if D_(E_c)(2b) <= D_(E_c)(b) for b >= b_0,
then every element of omega(E_c) has D = c_IR := the limit of D_(E_c)(b) as b -> infinity, at every scale.

Proof. Each coordinate of sigma^t E_c is bounded for t >= t_0 (TWO (iv)), so the closure of the forward orbit is
compact and Lambda is bounded on it. A non-increasing sequence that is bounded below converges. For E' in
omega(E_c) and an integer s,
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
  every size up to rho (eps/(p - 1))^(1/4) l_1 is within eps of that. So (UV-KEPT; c_UV) is false for TS in both forms
  of 3.1.

Remarks. (1) TS has every property that Theorem CE keeps (with the trivial centre grading: all levels even). So no proof of (a) can rest on those properties and on
the existence of an ultraviolet value. (2) TS is Lemma PT-inf (ii) read at the ultraviolet end: a seeded factor
adds to the ultraviolet value and adds nothing to the limit. Proposition NP's model (K copies of strong-coupling
SU(2) times ordered Ising, `library/gap-crux-exercise4-max.md` L383) has the same shape; TS is its abstract form
and is not a new idea. (3) In TS link (b) holds (the element is constant) and the conclusion of (c) is false in
the sense that matters: the constant element with the limit value exists.

### 3.6 The blockers named in the row

- **Lemma PT-inf and the product with a massless factor.** Let X be the SU(2) trajectory and Y the family
  A_(m,eps_j) with eps_j u_j^4 -> 0 (or the photon at one coupling, given its limit). On every torus D = D_X + D_Y (Lemma PT),
  and 0 <= D_Y <= log m. So X x Y has the ultraviolet law of X: Lemma FV holds for it with the same right side. X x Y
  has no seed, because S >= S_Y, which tends to m - 1 at every physical size. If (BDD-Delta) holds for X it holds for
  X x Y, and then the limit set of X x Y is not empty (Theorem CE (i)(b)), whether X has a seed or not. By Corollary
  KEPT (4), link (a) with the divergent ultraviolet law is then **false for X x Y**. "A product's limit also has a
  limit at minus infinity": yes; if X has a seed the limits of X x Y are limits of Y alone (PT-inf (ii)), for example
  the constant log m. But that limit is not the ultraviolet value. So a proof of (a) for X must fail for X x Y, which
  has the same ultraviolet law and every kept property: it must read the whole state space. This is the lead rule
  W2 once more (`parts/gap.md` L93). Mark: PT-inf blocks (a) as a class-wide principle (the family TS is the bare
  form); it does not refute (a) for SU(2) alone, where (a) with an ultraviolet value outside [d_min, D_0] is true
  exactly when the wall holds (A1 (3)).
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
all weights except those of p(l_1), ..., p(l_M). Integrate over U_(l_M) first, the other links fixed. By (A2), among the
weights kept it occurs in that of p(l_M) only, as tr(U_(l_M) W) or tr(U_(l_M)^(-1) W) with W a product of other links. Haar measure is
invariant under translation and inversion, so this integral is I(beta), whatever the other links are. Repeat with
l_(M-1), ..., l_1. The remaining links integrate to 1.

(A4) f(beta) <= 3 log I(beta) <= 3.42 - (9/2) log beta. Proof: f <= F(n)/n^4 <= (3 - 4/n + n^(-4)) log I(beta) for every
n, by (A3) and log I <= 0 (f is the infimum over all tori). The right side tends to 3 log I(beta) as n grows, and f
is at most each of its values; so f <= 3 log I(beta). With (A1):
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
5. **The dependence on the size, in the Gaussian abelian model (ARGUED; a count, one recalled fact).** Take the
   lattice Gaussian U(1) model with compact constant modes (the spin-wave part of the Villain model) on the
   symmetric torus with N = n^d sites. Split the link field into gauge directions, stiff directions and the d
   constant modes. The gauge orbit has the volume (2 pi)^(N-1) N^(-1/2) (det' Lap)^(1/2), with Lap the lattice
   Laplacian on functions and det' the product of its non-zero eigenvalues. The stiff directions are d - 1 copies
   of the non-zero spectrum of Lap and give (2 pi/beta)^(((d-1)N - d + 1)/2) (det' Lap)^(-(d-1)/2). A constant mode with
   holonomy angle theta has the normalised amplitude theta n^(d/2 - 1), so the d constant modes give
   (2 pi)^d n^(d(d/2 - 1)). Recalled fact: log det' Lap = c N + 2 log n + O(1) (one eigenvalue of size n^(-2) is missing
   from the bulk count). The powers of n add to - d/2 + 1 - (d - 1) + d(d/2 - 1) = (d - 1)(d - 4)/2. So

    D(n; beta) = ((d - 1)/2) log(beta n^(d-4)) + O(1).

   In four dimensions D does not depend on the size: the scale invariance of the photon. In five dimensions D grows
   like 2 log n. In words: the coupling of the constant modes at the size n is 1/(beta n^(d-4)). For SU(2) in five
   dimensions at weak coupling the same count gives 2 log(beta n) (GUIDE: the theory is free in the infrared, so
   the count improves with the size). The same count for a scalar with a broken continuous symmetry gives
   (1/2) log(beta n^(d-2)), the power of L that `gap-phys-seed.md` L336 recalls.

### 4.2 What Lemma FV says about the trajectory, and what it does not

- PROVED given beta_j -> infinity: at each fixed number of sites n, D_j(n) -> infinity. These tori have physical side
  n a_j -> 0. So at the lattice end of the scale axis the Casimir free energy of the trajectory is unbounded: the
  **free value is c = +infinity**, in the lattice sense.
- Not proved: the behaviour of D^+(L) at a fixed small physical size L (the number of sites grows with j). There the
  lane has I8 (GUIDE): D^+(L) grows like 3 log(1/g(L)). The account bounds D on its own tori above the floor ((TH), I6)
  and gives no asymptotics.
- By Corollary KEPT (4) and Proposition A1 (3): with a divergent ultraviolet law, link (a) is equivalent to (W),
  given (BDD-Delta). With the value at one fixed size, c = D^+(L_1), link (a) is a plateau statement at that value
  (3.2). The row's phrase "just above first passage" does not single out one size: L_1 and 2 L_1 both qualify, and
  by the dilation identity (PS L66) another admissible g' gives another unit. Omega does not depend on this choice.
  If (a) holds with the value at L_1 and with the value at 2 L_1, and Omega is not empty, then D^+(L_1) = D^+(2 L_1):
  the Casimir free energy does not run there. This contradicts I8 at belief grade; no proof step uses it.

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

## 5. Step 5 result (Task 4): the controls; assumptions; the discard tests in their valid form; comparison

### 5.1 The chain as a tool (skill step 6c)

In the skill's words a tool is a hypothesis H with a written proof of "H(M) implies T(M)" on a class K. For the
lead's chain: K = families of data with units and a bound D_0. H_a(M; c) = (UV-KEPT; c) of 3.1. T(M; c) = "every
uniformly recurrent element of Omega(M) has D = c at every scale; so (LIOU) for M holds if and only if Omega(M) has
no uniformly recurrent element with D = c". The proof of "H_a implies T" is Lemma REC with Corollary KEPT (PROVED).
So the chain is a sound tool. A control refutes it only if H_a is true and T is false there. A control where
(LIOU) is false and H_a is true tells what the last step (the exclusion of the D = c elements) must use.

### 5.2 The controls

| Control M' | Its ultraviolet (free) value | Its limit set | H_a(M'; c) | T(M'; c) | Verdict |
|---|---|---|---|---|---|
| **Compact U(1) at one coupling** (Villain, beta >= 2^14; the constant family) | finite: about (3/2) log beta + O(1) at every size (ARGUED: Lemma FV's count for U(1); the Gaussian part of the Villain model has exactly this power of beta; not written out) | the photon limit, D = c_inf(beta) := lim of D(n; beta), if D is bounded and converges (BELIEF, I10) | true with c = c_inf(beta), because the model is scale-invariant in the infrared; the lattice value D(3; beta) differs from c_inf by lattice terms | true: the uniformly recurrent element has D = c_inf; (LIOU) is false and the element with D = c exists | The chain does not fail and does not prove too much. It ends at an element that exists. For U(1) the last step is false. |
| **Compact U(1) along beta_j -> infinity** (the T_W form of the test table) | +infinity (Lemma FV for U(1), ARGUED, at fixed n) | empty for every D_0, if D_j(L/a_j) is about (3/2) log beta_j at every size (GUIDE) | vacuous | vacuous | Not a test of the chain or of (LIOU). The family has no seed because (BDD-Delta) fails: branch (II) of Corollary TRI. |
| **Frozen Q_8, 2T at large beta** (constant family) | log 92, log 244 at every size as beta -> infinity (PROVED, Proposition FRZ) | the constant log m(G) (BELIEF: a Peierls statement; THM in the lane for Z_2 with log 8) | true with c = log m(G): here the free value is literally kept | true: the constant log m(G) is the recurrent element; (LIOU) is false | The chain ends at the constant log m(G), which is a critical element (Proposition CONST). The engine, the centre grading and the spectral clause do not exclude it. |
| **Product SU(2) x (massless factor)** (the family A_(m,eps), or the photon at one coupling) | that of SU(2) plus a constant; +infinity on a fixed lattice (Lemma FV) | not empty: the factor's limit if SU(2) has a seed; sums otherwise (Lemma PT-inf) | false with the ultraviolet value (Corollary KEPT (4)) | not tested | It binds every proof of (a): the product has the same ultraviolet law as SU(2) and (a) is false for it. So a proof of (a) must read the whole state space (rule W2). |
| **The family TS** (3.5) | log(m_0 p), on any number of doublings above the unit | {log m_0} | false | not tested | (a) is not a consequence of the kept properties and an ultraviolet value. PROVED. |
| **SU(2) in five dimensions, weak coupling** (`gap-crux-fp.md` F15, L50, L76: GUIDE; one coupling) | +infinity: D(n; beta) >= 2 log beta - C(N) (ARGUED, remark 3 of 4.1) | empty for every D_0, if D(n; beta) is about 2 log(beta n) (GUIDE: the coupling of the constant modes at the size n is 4/(beta n)) | vacuous | vacuous | Not a test of the chain or of (LIOU). It tests (BDD-Delta): the weak-coupling phase has an unbounded Casimir free energy, branch (II). A proof of (BDD-Delta) must use the dimension. |

**What separates SU(2) inside the chain.** Only the free value: finite for U(1) at one coupling and for the frozen
groups (and then realised by a critical element), infinite for SU(2) (Lemma FV). No proof can use this, because for
an infinite value link (a) is the wall (A1 (3)).

**Correction to row 1017's table (R L294, L300), at GUIDE grade.** R lists "Compact U(1), Villain, beta_j -> infinity"
and "SU(2) Wilson in five dimensions, weak coupling" as families with a non-empty limit set "if D is bounded". By
the count of Lemma FV, D is not bounded there: both sit in branch (II). The family with a photon limit is U(1) at
one coupling. This changes no theorem of R. It changes what these two controls test: the hypothesis (BDD-Delta),
not (LIOU). The same correction applies to row 720: `gap-phys-seed.md` L336 says of the comparison models, five
dimensions included, "in every comparison model the failing half is (Z-UNB), and (BDD-Delta) holds", and names a
broken continuous symmetry as the one known kind of model where (BDD-Delta) fails; item A6 of R (L84) repeats it.
By remark 5 of 4.1 the gauge models that are free in the infrared are of that kind too: five dimensions at weak
coupling (D about 2 log(beta n)), and U(1) along beta_j -> infinity. So (BDD-Delta) is not automatic in the class, and
a proof of it for SU(2) must use that the dimension is four. All of this is GUIDE or ARGUED on both sides; neither
statement is proved.

**A reading that the controls suggest (reading; on record as Observation SCH of row 1004,
`library/gap-outside-box-max.md` L127).** At weak coupling D is (3/2) log of the inverse coupling of the constant
modes at the size of the torus. In this reading the three branches of Corollary TRI are: (I) the coupling grows
without bound and D falls to 0; (III) the coupling stalls and D stays in [d_min, D_0]; (II) the coupling returns to
weak at large sizes. Five dimensions and U(1) with beta_j -> infinity are of kind (II), U(1) at one coupling of kind
(III).

### 5.3 Assumptions of the lead's reading (skill step 4)

| ID | Assumption, in plain words | Where | Needed or habit | If it is wrong | Check |
|---|---|---|---|---|---|
| R1 | The small-scale end of a limit object shows the small-size behaviour of the theory | link (a) | needed by the chain | the chain has no ultraviolet input | **wrong**: Lemma ALPHA (PROVED) |
| R2 | The free value c is a finite number | links (a), (c) | needed by (c) as "one element to exclude" | with c infinite, (a) is the wall and (c) is empty | **wrong for SU(2)** on a fixed lattice: Lemma FV (PROVED); I8 at fixed physical size (GUIDE) |
| R3 | A recurrent element with a limit at one end is constant | link (b) | needed | - | right: Lemma REC (PROVED) |
| R4 | After (b), one element is left to exclude | link (c) | needed by the plan | a family is left | wrong for finite c (4.4, remark); empty for infinite c |
| R5 | The engine's axioms, the centre grading or the spectral clause might exclude a constant | link (c) | hope | nothing excludes it | they exclude a constant c iff e^c is not an integer >= 2: Proposition CONST (PROVED) |
| F1 | "Ultraviolet normalisation" can be read off D on symmetric tori | 3.1 | a choice | another functional Lambda | Corollary KEPT holds for every continuous Lambda |
| F2 | The trajectory's unit (first passage at one g) marks a size that is "ultraviolet" | row text | habit | by the dilation identity (PS L66) every admissible g' gives another unit; (a) with the value at L_1 and at 2 L_1 forces D^+(L_1) = D^+(2 L_1) | 4.2 |
| F3 | Dyadic sizes are enough | R | needed by the method (Theorem S doubles) | a finer grid changes no statement here | none needed |
| B1 | (BDD-Delta) holds for SU(2) | everywhere | belief; needed by Theorem CR | branch (II) | open (I7) |
| B2 | Asymptotic freedom separates SU(2) from the photon | the lane | belief with a proved fragment (Lemma FV) | - | it separates them at the ultraviolet end only; ALPHA shows that end is not in Omega |
| W1 | No computer-assisted step; rule 0a; rule W2 | GOAL.md, FINISH | owner rules | not questioned beyond paper | obeyed |

**Ranking** (by how much the question changes if the assumption is dropped): R1, R2, R4, F2, B1. With R1 dropped the
lane would stop looking for ultraviolet conditions on limit objects. With R2 dropped (a) is read as the wall. R4:
the last step is a family, so "exclude one element" is not a plan. F2: no size is singled out. B1 is the other open
half of the wall and is not touched by this row. None of these changes an owner decision.

### 5.4 Set-aside statements that this question touches, re-judged (skill steps 6a, 6d)

| # | Statement (author) | Reason given there | Where | Re-judged here |
|---|---|---|---|---|
| 1 | "No boundary condition at one end of the scale axis is a kept property" (row 1017) | Proposition SI and CE (d) | R L282 | **wrong as a blanket sentence** (CA item 20, CO D14). Corrected form, PROVED here: an asymptotic condition at minus infinity is kept if and only if it holds on the set A inside Omega (Corollary KEPT); for uniformly recurrent elements a condition at one end is a condition on the whole orbit (Lemma REC (iv)). The conclusion that the ultraviolet normalisation is not kept stands, by Lemma ALPHA, for every ultraviolet value that D does not take on Omega. |
| 2 | (R2-blow) "no critical element is asymptotically free at small scales: PROVED, and useless" (row 1017) | SI and CE (d) | R L318 | valid in the corrected form: it is Corollary KEPT (4) with CE (d). |
| 3 | (R2-two), first form: "this is (W) word for word" (row 1017) | reading | R L319 | valid; now a proved equivalence with its limit set (Corollary CR-1). |
| 4 | (R2-two), third form: "an o(1) quantity must be carried across all scales ... by a monotone"; Remark MON, ARGUED (row 1017) | - | R L284, L319 | valid; PROVED for omega(E_c) and a monotone functional (Proposition MON+). The monotone itself stays open. |
| 5 | Row 1017's test rows for U(1) with beta_j -> infinity and for five dimensions | "if D is bounded" | R L294, L300 | valid as conditionals; the condition is believed false (5.2). They test (BDD-Delta). |
| 6 | Soft exclusion of branch G, "no contradiction follows from the two ends alone" (row 988 Route 3; re-judged "too strong" by row 998) | w_p, U(1) | `parts/gap.md` L64, L68 | valid as reported for class-wide statements; not re-derived. The family TS is one more example with both ends prescribed. |
| 7 | The lead's reading (a)-(b)-(c) (row 1028) | to test | FINISH L1109 | (b) valid (PROVED); (a) target-equivalent for SU(2) and false in the class; (c) a family for finite c, empty for infinite c. |

**The blockage in one sentence (6b).** A limit object of the trajectory is made of infrared scales only, and the one
object that has both ends, the continuum datum itself, is not recurrent; so ultraviolet knowledge can reach the
limit objects only by being carried along the trajectory across every scale, which is the selective step the lane
does not have.

### 5.5 Comparison with the earlier work (skill step 5)

Search scope for every mark: `grep -l -i -E` over `library/gap-*.md`, `library/prior/gap-*.md`, `parts/gap.md` for the
patterns "alpha-limit|omega-limit|heteroclinic|two-ended", "toron|constant mode|zero mode", "commuting
(triple|4-tuple|tuple|quadruple)|Hom\(Z", "log 92|log 244| 736|5856", "(3/2) log beta|kappa = 3|3 log(1/g|log log
beta", "plateau", "free value|ultraviolet value|UV value"; the hit lines of the files named below were read. Not
searched: `origin/main` and the open PR branches (not refs of this checkout); files outside this folder.

| Item of this run | In the earlier work? | Where | Note |
|---|---|---|---|
| Lemma ALPHA, Corollary KEPT | partly | CO D14 (L203): "the small scales of a blow-down limit are large physical sizes of the trajectory"; CA item 20 | The reason is CO's sentence. The statement with alpha(E), the equivalence (1), and (4) were not found. |
| Lemma REC (link (b)) | new in the files searched | the row states it as a guess | - |
| Proposition A1 (3): (a) with a value outside [d_min, D_0] is the wall | partly | CA L401-403: "If a specified UV law forces D to diverge at small scales, CE's uniform bound excludes that law" | CA has the exclusion; the equivalence with (W) is the addition. |
| Proposition TWO, Lemma EXCL, Corollary CR-1 | partly | R L221 ("that object is the theory itself"), R L319 (R2-two) | Row 1017 named the object; the statements and proofs are here. |
| Proposition MON+ | yes, as ARGUED | Remark MON, R L284 | found again; now with a proof for omega(E_c). |
| The family TS | yes in substance | Lemma PT-inf (ii), R L260; Proposition NP (row 1003) | an abstract form of a known device; credit rows 1003, 1017. |
| The count (3/2) log beta, kappa = 3 | yes, as GUIDE or ARGUED | PS L109, L192 (row 720); `gap-outside-box-max.md` L127, L408 (row 1004), its check L422, L447: "neither count is checked" | **Lemma FV is the proof of the lower half.** A proof was not found in the files searched. |
| Proposition FRZ (i)-(iii), the formula log(abs(Hom(Z^4, G))/abs(G)) and Burnside | yes | gpt-6-astra, `gap-crux-skeleton-check-astra.md` L305 | found again; credit that check. |
| The numbers 92 and 244 | not found in the files searched | - | new within the search scope; guard run G1 agrees. |
| Proposition CONST | yes | CO 6.4 (L172) | found again, written out. |
| "D is a coupling"; the three branches as three behaviours of it | yes | Observation SCH, row 1004 | found again. |
| U(1) with beta_j -> infinity and five dimensions sit in branch (II) | not found; the record says the opposite | R L294, L300 (conditionals); `gap-phys-seed.md` L336 ("in every comparison model ... (BDD-Delta) holds", GUIDE) | new reading, GUIDE or ARGUED grade; the scalar case of the same count is recalled at L336. |

**What the fresh pass added:** Lemma ALPHA and Corollary KEPT (the exact form of CA's item 20); Lemma REC;
Proposition TWO with Lemma EXCL and Corollary CR-1; Lemma FV; the numbers 92 and 244; the place of two controls in
branch (II). **What it only found again:** the count kappa = 3, the frozen formula, the constants log m, Remark MON,
the device behind TS, the reading of D as a coupling.

## 6. Step 6 result: routes and attempts (skill steps 7 and 8)

### 6.1 Target contract (governance format)

Target: (LIOU) (R L288), equivalent to (W) given (BDD-Delta). Quantifiers: one trajectory of the account; every
uniformly recurrent element of Omega(D_0), D_0 a (BDD-Delta) bound. Allowed premises: the lane's checked statements,
the account as cited, published theorems rebuilt or named. Forbidden weakenings: a statement for one factor of the
state space; a hypothesis with a supremum over tilts or coupling fields; a computed number. Required cases: U(1),
frozen Q_8 and 2T, products, five dimensions. Completion: a proof of (LIOU), or an exact equivalent of a link, or a
counterexample to a link. Not closure: a renamed crux.

### 6.2 The link that survives, and its lemma

Link (b) survives. Its lemma is Lemma REC (2.4), proved by hand. One sharpening follows at once.

**Lemma REC+ (PROVED).** Let E be a uniformly recurrent element of Omega and Lambda continuous on Omega. If
Lambda(sigma^(t+1) E) <= Lambda(sigma^t E) for all t <= t_0, or for all t >= t_0, then Lambda(sigma^t E) is the same for
every integer t.

Proof. Lambda is bounded on Omega, so the monotone sequence has a limit at that end. Lemma REC (i) or (ii). QED

This is Proposition OM (e) with a weaker hypothesis: monotony along one orbit near one end, in place of monotony on
all of Omega. It is on the path only if a monotone is found; none is on record for the doubling of all sides.

Links (a) and (c) do not survive: 3.7, 4.5. The counterexample to (a) is the family TS (3.5).

### 6.3 Routes that the corrected picture suggests, each tried against the lane's tests

Passes of this one session; they are not independent. One pass used a lens from outside the lane (topological
dynamics: alpha and omega limit sets, Lyapunov functions); one pass argued that the question is misframed.

| Route | Object and mechanism | What you would have to believe | Kill pass | Verdict |
|---|---|---|---|---|
| U1, a conserved functional | a continuous Lambda with Lambda(sigma E_c) = Lambda(E_c) along the continuum datum; then Lambda = Lambda_UV on omega(E_c) (MON+ with equality) | that the torus datum of SU(2) has an exactly scale-independent number whose ultraviolet value no critical element has | The known scale-independent data of a field theory are anomaly-type data; they add over decoupled factors, and they prove masslessness, not a gap. No candidate. The product with a massless factor has the same ultraviolet law and a non-empty limit set, so the functional must not be additive (rule W2). | dead: no candidate |
| U2, a monotone | MON+ with a non-increasing Lambda; needs Lambda_UV below Lambda on every critical element | a monotone for the doubling of all four sides | For Lambda = D the ultraviolet value is +infinity (Lemma FV), so the inequality c_IR <= D_UV says nothing: in the functional D, asymptotic freedom gives the worst ultraviolet bound. For the a-function the photon lies below (row 1002). (MONO-Delta) is held by earlier rows. | blocked-equivalent; not attacked (rule 0a) |
| U3, a law at every scale | a closed condition on the datum at one scale that every SU(2) lattice satisfies at every size (so it is kept, Proposition SI) and that critical elements violate | a selective inequality at order-one coupling | Tried one candidate: "the twisted torus has a Casimir free energy bounded below", log Z^(1 nu)(n) >= f abs(n) - C. By the counts of Lemma FV it separates SU(2) (twisted flat connections exist, the ratio falls like beta^(-3/2)) from U(1) (the Z_2 twist costs an action of order beta) at weak coupling: GUIDE. But it reads the SU(2) factor only: SU(2) x photon satisfies it whenever SU(2) does. By rule W2 it cannot give (LIOU). Not proved, not pursued. | dead by rule W2 (the candidate); the family is the wall ((K-one) or (K-flow) of `parts/gap.md` L47-50) |
| U4, pin the limit by recurrence alone | Lemma REC (iv): the two ends of a recurrent orbit carry the same information as the whole orbit | that recurrence with the engine forces a contradiction | The constants log m are recurrent and satisfy everything (R, Proposition NR). | dead (found again) |
| U5, misframing pass | "The ultraviolet end is not part of any limit object. The question that replaces (a): which statement at finite sizes above first passage forces a seed after boundedly many doublings?" | - | This is (CAS) of row 708 and the (K-flow) input of `parts/gap.md` L47-50. Proposition NP binds every form that reads finitely many values of D. | found again; nothing new |

**Outside lens, one remark (recalled, not used in a proof).** For a homeomorphism of a compact metric space Conley's
theorem gives a continuous function that falls strictly along every orbit outside the chain-recurrent set and is
constant on each chain component. So on Omega a Lyapunov function always exists, and it is constant on every
uniformly recurrent orbit. A monotone can order the critical elements; it cannot exclude one. This agrees with
Theorem CR (5) and with Way 3 of row 1017.

### 6.4 Attempts made in this run (skill step 8)

| Attempt | Result | On the path of the target? |
|---|---|---|
| Prove link (b) | PROVED: Lemma REC, REC+ | on the path only with a monotone or a kept limit |
| Prove or refute link (a) | refuted in the class (TS); for SU(2) reduced to an exact statement: equivalent to (W) for an ultraviolet value outside [d_min, D_0] (A1 (3)); an infrared plateau statement otherwise (A1, A2) | this prices the route: target-equivalent |
| Strengthen CE to keep the ultraviolet data | impossible in the sense of Corollary A3: Proposition TWO, Lemma EXCL | - |
| Compute the free value | Lemma FV (lower bound, PROVED); frozen values (PROVED) | off the path (the ultraviolet end is not in Omega) |
| Decide whether the constant element is excluded | Proposition CONST: not excluded for c = log m; no element for c infinite | - |
| One candidate kept law (U3) | not selective against products; dropped | - |

No route was left untested for lack of budget. No numeric test bears on a verdict; the guard run of 4.6 is the only
run.

### 6.5 Registry entry for this family (governance words; for the lead; I do not edit `parts/gap.md`)

| Route | Object | Mechanism | Terminal obligation | Strength | Status | Evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| RH-uv, a kept ultraviolet condition on blow-down limits (sub-family of RH of row 1017) | elements of Omega(D_0) and their minus-infinity end | asymptotic freedom as a boundary condition, then recurrence (Lemma REC) | (UV-KEPT; c) | target-equivalent for c outside [d_min, D_0] (Proposition A1 (3)); an infrared plateau statement for c inside | blocked-equivalent | Lemmas ALPHA, REC, EXCL; Corollary KEPT; Propositions A1, A2, TWO, MON+; the family TS; Lemma FV (this file, unchecked) | a functional of the torus datum that is conserved or monotone along the continuum datum of the trajectory, whose ultraviolet value lies outside its range on critical elements, and which is not additive over decoupled factors |

## 7. Step 7 result: second pass on the proofs (same session, so not a check)

I re-read Sections 2 to 4 from the file and re-derived each step once more. No statement failed. Eight repairs
were made in place:

1. Proposition TWO (iv) now says that the subsequence J' is the one of (iii) (inside the subsequence of Lemma UF);
   the proof used it.
2. Corollary CR-1 was restated on the grid G_0 of sizes from L_0 on, with the definition of a continuum datum on
   G_0. The first wording spoke of "the sizes of P" and left open what happens at a size below L_0 with D^+ infinite.
3. Proposition MON+ now says why Lambda is bounded (the closure of the forward orbit is compact).
4. The family TS: the lower bound for D^+ had the inequality log(1 - w) >= - w the wrong way round; corrected to
   D^+(L) >= log(m_0 p) - (p - 1)(L/rho)^4, and the range of the plateau to rho (eps/(p - 1))^(1/4) l_1.
5. Section 3.6, the product: the first wording said that link (a) for X x Y "is false exactly when X has a seed".
   That was wrong for the divergent ultraviolet law: the limit set of X x Y is never empty, so (a) is false for
   X x Y in both cases. Rewritten; the conclusion (a proof of (a) must read the whole state space) is the same.
6. Lemma FV (A3): "among the weights kept" added. (A4): a broken sentence replaced.
7. Section 4.2: the remark on the value "just above first passage" now states its hypothesis (that (a) holds with
   the value at L_1 and with the value at 2 L_1).
8. Section 3.1: a paragraph on what the account's normalisation is, from the lane's index.

Points a checker should test first (the places where I would expect an error, if there is one):

- Lemma REC (i): that the set U contains a basic neighbourhood, and that "bounded gaps" in the sense of OM (d)
  gives return times that are unbounded **below** (CA L262-271: every interval of 2N + 1 integers holds one).
- Corollary KEPT (2): that sigma^s E' lies in alpha(E) for every s (ALPHA (i)), so that Lambda is c along the whole
  orbit of E'.
- Proposition TWO (iv): the diagonal choice of j_n (three conditions, each on finitely many quantities), and that
  (H1), (H2) then hold with i(m) = max(1, abs(m)).
- The family TS: that every admissible sequence has gamma_i -> 0 (the use of (H2) at one large scale m).
- Lemma FV (A2): the two nu-links of p(l) are tree links; the map is one-to-one; the order property. (B5): the two
  separation bounds and the count. (B6): the powers of beta. The constants 3.42, 58.92, 10.84.
- Proposition FRZ: the three centraliser recursions.

## 8. Step 8: report (skill step 9)

### 8.1 The wall, in plain words

The lane must show that the four-dimensional SU(2) theory has no massless particle. It has shown this much: if the
theory had one, and a certain free energy stayed bounded, there would be a "limit picture" of the theory at very
large sizes that keeps coming back to itself as the scale is doubled. To finish, one must show that SU(2) has no
such picture. A photon is such a picture, so every general tool fails. This row asked: SU(2) differs from a photon
at very small sizes; does that difference survive in the limit picture, as a condition on its small-scale end, so
that the picture is pinned to one number and can be excluded?

### 8.2 What the exercise found

1. No. Every scale of a limit picture, its small-scale end included, is made of very large physical sizes of the
   theory. The small physical sizes never appear in it. This is now a short theorem (Lemma ALPHA, proved by Claude
   Fable 5.2 by hand, not yet checked).
2. The second step of the lead's reading is right: a picture that keeps coming back to itself and has a limit at
   one end is constant there (Lemma REC, proved, not yet checked).
3. So the first step carries all the weight, and it is not a weaker statement than the wall. If the small-size
   value is a number that limit pictures cannot have, the first step says "there is no limit picture", which is the
   wall itself. If it is a number they can have, the first step says that the free energy stops changing at large
   sizes, and nothing about small sizes gives that.
4. For SU(2) the small-size value is infinite: on a fixed lattice the free energy in question grows at least like
   (3/2) log beta (Lemma FV, proved by hand with explicit constants, not yet checked). So for SU(2) the first step is
   the wall. For the frozen groups the value is finite and exact: log 8, log 92, log 244. Limit pictures with these
   values exist, and nothing in the lane's axioms excludes them.
5. The one object that does remember the small sizes is the theory itself at fixed sizes. It is not a picture that
   comes back to itself. The two kinds of object are joined only by following the theory through every scale, and
   that is the step the lane does not have.
6. This run did not pass the wall. It priced one more route exactly, corrected one sentence of row 1017 into a
   theorem, and proved a fact about small sizes that the lane held as a count.

### 8.3 Filters corrected

- **Row 1017's sentence "no boundary condition at one end of the scale axis is a kept property"** (struck by the
  gpt-6-astra check, item 20). Valid form, proved here: an asymptotic condition at minus infinity is kept exactly
  when it holds on the alpha-limit sets inside the limit set (Corollary KEPT); on a uniformly recurrent element a
  condition at one end is a condition on the whole orbit (Lemma REC). The trajectory's ultraviolet normalisation is
  kept only if its value is taken by critical elements. What comes back: nothing for SU(2); for a model whose free
  value is finite and realised (frozen groups, U(1) at one coupling) the condition is kept and excludes nothing.
- **Row 1017's test rows for U(1) with beta_j -> infinity and for five dimensions** ("limit set not empty, if D is
  bounded"), **and row 720's sentence "in every comparison model ... (BDD-Delta) holds"** (`gap-phys-seed.md` L336).
  By the count of remark 5 in 4.1, D is believed unbounded in gauge models that are free in the infrared: five
  dimensions at weak coupling, U(1) along beta_j -> infinity. These families test (BDD-Delta), not (LIOU), and
  (BDD-Delta) is not automatic in the class. ARGUED for the Gaussian abelian model, GUIDE otherwise; the earlier
  statements are GUIDE too.
- No discard test of `parts/gap.md` changed. Rule W2 binds this route as written there (3.6).

### 8.4 Routes worth doing

None on this family. The reopen condition is in 6.5: a functional of the torus datum that is conserved or monotone
along the continuum datum, whose ultraviolet value lies outside its range on critical elements, and which is not
additive over decoupled factors. I know no candidate.

### 8.5 What not to do next

- A row that looks for an ultraviolet boundary condition on blow-down limits, in any functional. Lemma ALPHA covers
  every continuous functional.
- A row that tries to "exclude the constant element". For a finite value the constants log m are critical elements
  and the element is a family; for the SU(2) value there is no element.
- A row that proves the ultraviolet law of D at a fixed small physical size (the small-volume expansion on the
  account's lattices). It has no consumer: that end of the scale axis is not in any limit object.
- Using U(1) with beta_j -> infinity, or five dimensions, as tests of a Liouville statement. They are tests of
  (BDD-Delta).

### 8.6 The exact price

Link (a) of the lead's reading, with the free value of SU(2), is equivalent to (W), given (BDD-Delta) (Proposition
A1 (3) with Theorem CR; proved here given the lane's inputs; unchecked). With a value in [d_min, D_0] it is
equivalent to "D takes that value on every alpha-limit point of the limit set", an infrared plateau statement
(Proposition A1 (1), A2). In neither form is it weaker than the wall.

### 8.7 Work items

**W1, check (a model that did not write this file; high effort).** Check line by line, in
`library/gap-uv-rigidity-max.md` at the commit that holds it: Lemma ALPHA (2.2), Corollary KEPT (2.3), Lemma REC (2.4),
Propositions A1 and A2 (3.1, 3.2), Proposition TWO, Lemma EXCL, Corollary CR-1 (3.3), Proposition MON+ (3.4), the
family TS (3.5), Lemma FV with Parts A and B (4.1), Proposition FRZ (4.3), Proposition CONST (4.4), Lemma REC+ (6.2).
Read first: `library/gap-compact-rigidity-max.md` L131-158 (definitions), L223-243 (Proposition OM, Theorem CR), L253
(the data A_(m,eps)), L257-262 (Lemma PT-inf); its checks `gap-compact-rigidity-check-opus.md` L129-141 and
`gap-compact-rigidity-check-astra.md` items 11, 14, 19, 20; `library/gap-dichotomy.md` L92-136 (the setting). Test first
the six points listed at the end of Section 7. Then judge: (i) is Proposition A1 (3) right as stated, with
(BDD-Delta) as the only extra hypothesis beyond Theorem CR; (ii) does the proof of Lemma FV hold with its constants,
and is its f the infimum the lane uses (`gap-crux-restate.md` L29-45); (iii) is the family TS a family of data with
units in the sense of `gap-dichotomy.md` L85-101, and is its limit set as stated; (iv) is the correction of 5.2 to
rows L294 and L300 of `gap-compact-rigidity-max.md` fair as a GUIDE-grade statement. Report the first failing step,
or none. Stop rule: no new attack. Output: `library/gap-uv-rigidity-check-<model>.md`.

**W2, bookkeeping (the lead).** If W1 passes, in `parts/gap.md`: (1) in the obligation line of row 1017, replace "the
limit keeps no condition at one end of the scale axis (Proposition SI)" by: "an asymptotic condition at minus
infinity is kept exactly when it holds on the limit set itself (Corollary KEPT, row 1028); the trajectory's
ultraviolet normalisation is not kept unless critical elements take its value; with the SU(2) free value the
statement is (W)". (2) Test table: add the frozen values log 8, log 92, log 244 (Proposition FRZ) to the row
"Frozen Q_8, 2T"; add to the U(1) row that the family with beta_j -> infinity sits in branch (II) (GUIDE); the same
for five dimensions where it is used. (3) Route registry: add the row RH-uv of 6.5. (4) At `gap-phys-seed.md` L109
and L192 the count kappa = 3 has a proved lower half on a fixed lattice: Lemma FV. (5) At `gap-phys-seed.md` L336 and
at item A6 of row 1017, mark that five dimensions at weak coupling and U(1) along beta_j -> infinity are believed to
violate (BDD-Delta) (remark 5 of 4.1, ARGUED); the sentence "in every comparison model (BDD-Delta) holds" then needs
the words "at one coupling, in four dimensions".

**Not proposed.** (1) A proof row on (UV-KEPT) or (PLATEAU): the first is the wall; the second has no mechanism and
says that the running stops. (2) A row on the upper half of Lemma FV, or on D^+(L) at a fixed small physical size:
no consumer (Lemma ALPHA). (3) Rows on the routes U1 to U5 of 6.3: no candidate, or held by earlier rows. (4) A
numeric study of D(n; beta) at weak coupling: it would decide nothing.

### 8.8 Appendix

**Marks.**

| Statement | Where | Mark | Rests on |
|---|---|---|---|
| Lemma ALPHA | 2.2 | PROVED by hand, unchecked | Proposition OM (a) (checked: CO, CA) |
| Corollary KEPT | 2.3 | PROVED, unchecked | ALPHA; Theorem CE (ii)(d) |
| Lemma REC (link (b)), Lemma REC+ | 2.4, 6.2 | PROVED, unchecked | the definition of OM (d) |
| Proposition A1; (a) with a value outside [d_min, D_0] is equivalent to (W) | 3.1 | PROVED GIVEN Theorem CR and (BDD-Delta), unchecked | KEPT |
| Proposition A2, (PLATEAU; c) gives (a) | 3.2 | PROVED, unchecked | the definition of admissible sequences |
| (PLATEAU; c), (UV-KEPT; c) with c in [d_min, D_0], for SU(2) | 3.2 | OPEN; no mechanism; an infrared statement | - |
| Proposition TWO, Lemma EXCL, Corollary A3, Corollary CR-1 | 3.3 | PROVED, unchecked (TWO given (S0-Z), (TH-Z); CR-1 given Theorem CR) | Theorem CE's proof, Lemma UF, Theorem S |
| Proposition MON+ | 3.4 | PROVED, unchecked; its hypothesis (a monotone) is OPEN | TWO |
| The family TS; link (a) FAILS as a class-wide principle | 3.5 | PROVED (an argued counterexample in the skill's words), unchecked | the data A_(m,eps) (R L253) |
| Blockers of 3.6 | 3.6 | PT-inf: PROVED given Lemma PT, Lemma FV; D2, SHEET: do not bind (reading of their statements); NP: as cited | - |
| Lemma FV | 4.1 | PROVED by hand, unchecked; guard run agrees at the tested points | definitions only |
| D(n; beta) = (3/2) log beta + log log beta + O(1); I8 at a fixed physical size | 4.1, 4.2 | GUIDE | counts; recalled literature |
| Lemma FV for U(1) and in five dimensions | 4.1 remark 3 | ARGUED (same proof, not written out) | - |
| The Gaussian count D = ((d - 1)/2) log(beta n^(d-4)) + O(1); five dimensions and U(1) with beta_j -> infinity violate (BDD-Delta) | 4.1 remark 5, 5.2 | ARGUED for the Gaussian abelian model (one recalled fact); GUIDE for SU(2) in five dimensions | - |
| Proposition FRZ; the values log 8, log 92, log 244 | 4.3 | PROVED, unchecked; guard run agrees | Burnside; the shelling of 4.1 |
| Proposition CONST | 4.4 | PROVED, unchecked (found again from CO 6.4) | Lemma LV's argument |
| Controls of 5.2 | 5.2 | U(1) at one coupling, frozen Q_8 and 2T at large finite beta: BELIEF for their limit sets; TS: PROVED; five dimensions and U(1) with beta_j -> infinity in branch (II): GUIDE | - |
| Routes U1 to U5 | 6.3 | dead, blocked-equivalent or found again, as stated there | - |
| (LIOU), (BDD-Delta), (W) | - | OPEN, not moved | - |

**Assumptions most likely to be wrong** (of the reading tested): R1 (shown wrong), R2 (shown wrong on a fixed
lattice), R4. **Most expensive to be wrong:** B1, (BDD-Delta): every statement about Omega is empty without it.
**Literature proofs worth translating:** none for this question. The small-volume expansion (Luscher; van Baal)
would raise I8 from GUIDE, and has no consumer here.

**What this run did not cover.** The account's TeX was not opened; its statements are taken from `gap-phys-seed.md`
L61-116 and from the lane's index (`library/sa-index/chunk-04.md`, `chunk-06.md`, a few rows). No primary paper was
read; Luscher, van Baal, Krauth and Staudacher, Conley, Birkhoff, Guth, Frohlich and Spencer are recalled or taken
through the lane's quotations. `library/gap-dichotomy.md` was read to L300 only. `library/gap-crux-fp.md` was read at
L50, L66-80, L258-268, L279-285 only. The bodies of rows 988, 1002, 1003, 1004 were read only at the lines cited. Row
1025 was not read (no RESULT at the pin). The inputs Theorem S, Lemma UF, Theorem CE, Proposition OM, Theorem CR,
Lemma PT and Lemma PT-inf were used as checked by CO and CA and were not re-derived, except the steps of CE's proof
that Proposition TWO reuses. The U(1) and five-dimensional forms of Lemma FV were not written out. No upper bound
for D on a fixed lattice was proved. The limit sets of U(1) at one coupling and of frozen Q_8 and 2T at large finite
beta are beliefs here. `origin/main` and the open PR branches were not searched (not refs of this checkout); the
repo search covered this folder at the pin. No blind check of the plain version ran (no subagents). The passes of
6.3 are passes of one session and are not independent.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (the account: the
trajectory, the first-passage datum, the dilation identity, (UV-Z); no proof of theirs is used). Tadeusz Balaban
(the stability theorem behind (UV-Z)). Claude Fable 5.2, row 1017 (Theorems CE and CR, Proposition OM, Lemma PT-inf,
the data A_(m,eps), Remark MON, the form (R2-two)). The gpt-6-astra check of row 1017 (item 20, the source of this
row; the exclusion of a divergent ultraviolet law by CE's bound). Claude Opus 5.5, check 1019 (D14: "the small
scales of a blow-down limit are large physical sizes of the trajectory", which is the idea of Lemma ALPHA; 6.4, the
constants log m). The target lead (the reading (a)-(b)-(c); link (b) is the lead's). Row 720 (the count kappa = 3,
Section 1.2 of `gap-phys-seed.md`). Row 1004 and its check 1008 (the count (3/2) log beta for the twist ratio;
Observation SCH). The gpt-6-astra check `gap-crux-skeleton-check-astra.md` L305 (the frozen formula and its Burnside
form). Row 1003 (Proposition NP, the device behind TS). Row 998 (Lemma PT, rule W2). Row 712 (`gap-crux-fp.md`, the
dimension test). Martin Luscher and Pierre van Baal (the small-volume expansion, through row 720). Werner Krauth and
Matthias Staudacher (the convergence threshold of Yang-Mills integrals, recalled). George Birkhoff (recurrence and
minimal sets), Charles Conley (Lyapunov functions and chain recurrence), recalled. Carlos Kenig and Frank Merle
(the roadmap, through row 1017).

**Strong words, read against what the run did.** "PROVED": by hand, by one model, unchecked, given the inputs named
in the table. "Equivalent" (A1 (3), 8.6): given Theorem CR and (BDD-Delta). "The free value is infinite": on a fixed
lattice torus as beta grows (Lemma FV); at a fixed small physical size of the trajectory it is a belief. "No
construction keeps it" (Corollary A3): in the sense of Lemmas ALPHA and EXCL, for extraction by sequences (j_i, k_i)
from the torus data; not a statement about objects with more structure. "New", "not found": within the search
scope of 5.5. "Sound tool" (5.1): the implication is proved here and is unchecked. "No candidate", "no mechanism":
none found in this run and none on record in the files read; not a proof that none exists. "Branch (II)" for U(1)
with beta_j -> infinity and for five dimensions: GUIDE.

**Run record.** Started 2026-11-16T00:21Z; report written 2026-11-16T00:56Z; last edit (remark 5 of 4.1 and the pointers
to row 720) 2026-11-16T00:59Z (all from `date -u`). One guard run under
the numeric lock (4.6), memory free 68 percent before it; no other run. No subagents. Files written: this one only;
scratch under `/tmp/ym4d-w3-uvrig/` (the skill text, two reference files, one script and its output). No commit, no
push.

RESULT: Row 1028 (Claude Fable 5.2 max, Mac mini worker 3; author, checked by no one; one guard run, no subagents). The lead's chain does not pass the wall: link (a) is false as a class-wide principle and, for SU(2), is the wall itself (target-equivalent given (BDD-Delta)); link (b) holds; link (c) is empty for the SU(2) value. PROVED by hand (unchecked): Lemma ALPHA and Corollary KEPT (every scale of a blow-down limit, its minus-infinity end included, is infrared: the alpha-limit set of an element of Omega lies in Omega; an asymptotic condition at minus infinity is kept exactly when it holds there, which is the valid form of the sentence struck by item 20 of the gpt-6-astra check); Lemma REC and REC+ (link (b): a uniformly recurrent element with a limit at one end has D constant, and with a pointwise limit it is a fixed point of the doubling); Proposition A1 (link (a) with an ultraviolet value outside [d_min, D_0], or a divergent law, is equivalent to (W) given (BDD-Delta); with a value inside it is an infrared plateau statement, (PLATEAU), OPEN with no mechanism); Proposition TWO, Lemma EXCL, Corollary CR-1 (the object that keeps the ultraviolet data is the continuum datum at fixed sizes; it is not recurrent; its forward limit set lies in Omega; so CE cannot be strengthened to keep (a)); Proposition MON+ (ultraviolet data reach the limit set only as an inequality through a monotone, which stays OPEN); the family TS (a counterexample to (a) in the class with every kept property: ultraviolet value log(m_0 p) on any number of doublings, limit log m_0); Lemma FV (task 3: on a fixed lattice torus D(n; beta) >= (3/2) log beta - 59 n^4 - 11 for SU(2), beta >= 16, so the free value is +infinity; the count kappa = 3 of row 720 now has a proved lower half); Proposition FRZ (frozen values log 8, log 92, log 244 for Z_2, Q_8, 2T, the same at every size); Proposition CONST (a constant c is a critical element iff c = log m, m >= 2 an integer: the engine, the centre grading and the spectral clause exclude no such constant; for the SU(2) value there is no element, and for a finite value link (c) names a family). Controls (task 4): the chain is a sound tool and passes them all (U(1) at one coupling and frozen Q_8, 2T end at elements that exist; products and TS make (a) false, so a proof of (a) must read the whole state space, rule W2; Theorem D2 and Lemma SHEET do not bind (a)); GUIDE-grade correction to rows 1017 and 720 (`gap-phys-seed.md` L336): U(1) with beta_j -> infinity and five dimensions have unbounded D (Gaussian count D = ((d - 1)/2) log(beta n^(d-4)) + O(1), ARGUED) and sit in branch (II), so they test (BDD-Delta), not (LIOU), and (BDD-Delta) is not automatic in the class. OPEN, not moved: (LIOU), (BDD-Delta), (W); the route "kept ultraviolet condition" is blocked-equivalent, with the reopen condition of 6.5.
