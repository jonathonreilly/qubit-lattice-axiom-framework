lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-16T10:56Z

# The conditional dichotomy of the gap lane (queue row 1024, `gap-dichotomy-write`)

Status: IN PROGRESS. Writing row, work item W4 of row 998. No new mathematics. This note does not land.
Pinned at commit 7dd0badbc. Started 2026-11-15T22:56Z.

## 0. Plan (save protocol; one step per response, result appended before the next)

1. Read the two forms: `library/gap-phys-seed.md` L296-330 (Theorem ZD-c, Corollary Z4) and
   `library/gap-compact-rigidity-max.md` 3.1-3.7, 5.1, 6.1 (Theorems CE, CR, Proposition OM, Corollary TRI).
2. Read the scope repairs: `library/gap-compact-rigidity-check-opus.md` 6.4, D1-D3.
3. Read the inputs and their checks: Theorem S, Proposition Delta, Theorem SH, Theorem ZD, Theorem EV-L.
4. Read the continuum leg: (DET), (HC-phys), (E0-tor); and the current marks in `parts/gap.md`.
5. Write Sections 1-3: setting, the statement in both forms, the proofs by citation.
6. Write Section 4: the table of inputs still PROVED GIVEN, ARGUED or unchecked, and what stays open for (I), (II), (III).
7. Write Sections 5-7: plain words, 'Lean', what the theorem does not claim.
8. Re-read every cited line once against the note, then the RESULT line.

## Working log

- Step 0 done: plan written.
- Step 1 done (read, no verdict changed). Form 1: `gap-phys-seed.md` L253-323 (Lemma Z L253, Corollary Z1 L259, Lemma Z' L268,
  Corollary Z1' L274, Lemma Z3 L283, Theorem ZD L296-304, Theorem ZD-c L311-320, Corollary Z4 L322-323). Form 2:
  `gap-compact-rigidity-max.md` 3.1 L131-158 (datum, rescaling, admissible sequence, critical element), Lemma UF L160-164,
  Theorem CE L168-196, Proposition OM L223-237, Theorem CR L241-243, Corollary TRI L350-352, Lemma LV L394-396.
  Source's own caveat at L129: "Nothing is checked by another model" (later checked by row 1019, same provider).
- Step 2 done. Check 1019 (`gap-compact-rigidity-check-opus.md`, Claude Opus 5.5 max, same provider as the author): first
  failing step none; verdict table L213-225. Repairs this note applies: D1 (L237: add "j >= n" to the diagonal of OM (a)),
  D2 (L233: Omega = Omega(D_0) with D_0 a bound of (BDD-Delta)), D3 (L235 and 6.4 L172: (III) reads "for some D_0,
  Omega(D_0) of this family has a uniformly recurrent element"), D7 (L241: the time l u_j/2 is an integer at least 3), D8
  (L241: a critical element presupposes the spectral form). Fact (F3) L63: (W) iff (PHYS-SEED) needs no extra hypothesis.
  Not covered by 1019 (L246-250): the inputs as a whole; Remark (3) of 3.3; the lattice realisations of log m.
- Step 3a finding (process, not mathematics): FINISH row 730 (`gap-zd-astra`, the cross-provider check of Theorems ZD, ZD-c,
  Corollary Z4) has a task text and NO RESULT. Its output `library/gap-zd-astra.md` does not exist at 7dd0badbc, nor on the
  remote head of this branch, nor on PR 10149 (file listing by a depth-1 blobless fetch into /tmp/gap-dichotomy-scratch,
  2026-11-15). So the only check of Theorem ZD-c and Corollary Z4 on record is row 727 (Claude Opus 5.5 high, same provider
  as the author). The queue row's phrase "checks rows 727 and 730" is right for 727 only.
- Step 3b done. Check 727 (`gap-phys-seed-check.md`, Claude Opus 5.5 high, same provider): Lemma Z L42, Corollary Z1 L44,
  Lemma Z' L48-52, Corollary Z1' L54, Lemma Z3 L56-60, Theorem ZD L62-69, Theorem ZD-c L73-78 (uniformity in j; the bound
  at L_1 is strict), Corollary Z4 L80 HOLDS AFTER CORRECTION (sides b multiples of 4, b >= max(4 a_0, 12)); table L111-132.
  Not covered there (L10, L137): the proofs of Lemma A, K, X, E', Theorem S, Corollary S3', Theorem SH, Proposition Delta.
- Step 3c/4 partial (read): Theorem EV-L = `gap-flux-exercise.md` C3 L135-145, proof 8.2 L420; cross-provider check row 732
  (gpt-6-astra max, `gap-flux-exercise-check.md`): HOLDS. Limit step = row 700 `gap-seed-limit.md` Theorem L3 L138,
  Propositions P L188, P' L200 ("the continuum datum is an OPEN input", L12). Corollary C = `gap-crux-fp.md` L449 (row 712).
  (DET): `gap-det-check-astra.md` L406 (HOLDS AFTER CORRECTION as a conditional matrix comparison; not (DET) for the
  account's physical normalizer). (E0-tor): `gap-idab-check-astra.md` L196-215, `parts/gap.md` L134. (TH): `gap-ladder-max.md`
  L150. (U1), (U2), (HC-phys): `gap-hcphys-max.md` L135-150. None of (DET), (HC-phys), (TH), (E0-tor) is read by the
  trichotomy; they sit on routes that would supply (I).
- Step 4 done (read). Theorem SH has a cross-provider check: row 722 (`gap-sh-astra.md`, gpt-6-astra max: HOLDS, domain
  1 <= p). Proposition Delta: same-provider check only (row 709); at integer ratios, the only ones this note reads, its
  two-line proof was re-derived in check 1019 L55. Corollary C: HOLDS in `gap-crux-fp-check.md` L126 (it is Proposition P (a)
  of row 700). Limit step: rows 703 (same provider) and 723 (`gap-limit-astra.md` L916-926, cross-provider): HOLDS with
  scope corrections; Proposition P' needs the continuum datum, positive-time convergence and totality, which nobody supplies.

---

# The note

**Provenance.** Written by Claude Fable 5.2, medium effort, Mac mini worker 1, at commit 7dd0badbc, 2026-11-15. A writing
row. It adds no mathematics. It assembles statements of rows 697-731 and 1017 and applies the repairs of check 1019.
Nobody has checked this note. It grants no status and it does not land (owner rule, Section 7).

**Credit.** The trajectory is that of the complete account of Ethan Sussman and Levent Alpoge (with Claude and Codex as
authors of their text; repository at commit 31a47c543775), which is built on the renormalisation group of Tadeusz Balaban
(CMP 95-122). The theorem below reads no line of either: it is a statement about partition functions of the Wilson
lattice theory. Their work enters only where Section 1.2 says so. The compactness architecture follows the roadmap of
Kenig and Merle (as recorded in row 1017, 2.4). The mixture method of Theorem EV-L is prior work of PR 10114
(`MIXGFF.md`, per check 732). Corollary S3' and Lemma E' are by Codex gpt-6-astra (row 699).

## 1. Setting

### 1.1 The lattice objects (definitions; `gap-crux-exercise3-max.md` L111-115; `gap-compact-rigidity-max.md` L133-143)

- **Model.** Wilson SU(2) on a periodic torus with integer sides n = (n_1, ..., n_4), all n_i >= 3. Action
  A(U) = sum over plaquettes of (1 - (1/2) tr U_p). Z(n; beta) = integral of exp(-beta A) over Haar measure.
- F = log Z; f = inf over n of F(n)/abs(n), with abs(n) = n_1 n_2 n_3 n_4; Delta(n) = F(n) - f abs(n) >= 0.
- **Casimir free energy** of the symmetric torus: D(a) = Delta(a, a, a, a).
- For a box B of three sides, T_B is the transfer operator: Z(k, B) = Tr T_B^k, with eigenvalues
  lambda_0 > lambda_1 >= ... >= 0. The **gap** is m(B) = log(lambda_0/lambda_1). The **thermal sum** at the time k is
  S(k; B) = sum over i >= 1 of (lambda_i/lambda_0)^k.
- Phi_4(n) = 256 F(n^4) - F((4n)^4) = 256 D(n) - D(4n) (the doubling defect; `gap-phys-seed.md` L247, L281).
- **Datum** (abstract class). A positive function Z on quadruples of integers at least 3, with (E1) symmetry in the four
  sides, (E2) Z(k, B) = sum over r of lambda_r(B)^k with lambda_0 > lambda_1 >= ... >= 0, (E3) f finite. Wilson SU(2)
  at one coupling is a datum (item A1 of row 1017: `gap-crux-restate.md` L33, L174-176; `gap-seed-check.md` Lemma 1.1
  for boxes with unequal sides).

### 1.2 The trajectory and the setting (S0)

A **family with units** is a sequence of data Z_j with integers u_j. For the theorem: Z_j is Wilson SU(2) at the
coupling beta_j, and u_j = l_1/a_j, where a_j > 0 is called the lattice spacing and l_1 is one physical size.

**(S0)** l_1/(4 a_j) is an integer at least 3 for all large j. (`gap-phys-seed.md` L311. So u_j is a multiple of 4 and
at least 12; this covers repair D7 of check 1019, L241: every time that occurs is an integer at least 3.)

P = {2^i l_1 : i >= 0} is the set of physical sizes. For L in P:

- D^+(L) := upper limit over j of D_j(L/a_j), in [0, +infinity];
- z^-(L) := lower limit over j of (L/a_j) m_j((L/a_j)^3) (the gap of the cube of side L, in units of 1/L).

**"The account's trajectory"** means: beta_j = the bare coupling that the Sussman-Alpoge construction assigns to the
spacing a_j ("first-passage data, dilated", `gap-crux-exercise3-max.md` L129). The theorem uses (S0) and nothing else
about the pairs (a_j, beta_j). Two facts about this, both from the record:

- The account's own tori have side 2 L^m with odd L (row 959, point 2; `gap-seed-limit.md` L206, item 5). They are not
  the tori of P. The theorem speaks about the bare Wilson measure on the tori of P at the couplings beta_j. That the
  account's couplings come with spacings that satisfy (S0) is **not verified** in the lane.
- Existence of the continuum limit is not proved (FINISH.md L11). The theorem does not need it.

### 1.3 The four statements of form 1 (`gap-phys-seed.md` L313-318; (W): `gap-crux-exercise3-max.md` L131)

- **(PHYS-SEED)**: there is l in P such that the upper limit over j of S_j(l/(2 a_j); (l/a_j)^3) is below 1/5041.
  (The form with 1/1650 is equivalent: proof of Theorem ZD-c, L320; check 727, L74.)
- **(BDD-Delta)**: there are L_0 in P and D_0 with D^+(L) <= D_0 for every L >= L_0 in P. I call (L_0, D_0) a
  **bound of (BDD-Delta)**.
- **(Z-UNB)**: for every number C and every size L' there is L >= L' in P with z^-(L) > C.
- **(W)**, the wall: there is L in P with z^-(L) > 256 D_0 + 30, where D_0 bounds D^+ on the sizes of P from L/4 on.

### 1.4 The objects of form 2 (`gap-compact-rigidity-max.md` 3.1, L145-158, 3.5 L225; repairs of check 1019)

- DD = {2^i : i in Z}. An **eternal datum** is a function Delta_* from DD^4 to [0, infinity).
- **Rescaling.** For k >= 0 and x in DD^4 with all x_i >= 2^(-k): Delta^(j,k)(x) := Delta_j(2^k u_j x). The rescaled
  levels, D^(j,k)(b), s^(j,k)(b) (the thermal sum of the cube of side 2^k u_j b at half its side) and z^(j,k)(b) are
  as at L149-151.
- **Admissible sequence with the bound D_0.** A sequence (j_i, k_i) with j_i -> infinity and k_i -> infinity such that
  for every m in Z there is i(m) with, for i >= i(m): (H1) D^(j_i,k_i)(2^m) <= D_0 + 1/i; (H2) s^(j_i,k_i)(2^m) >= 1/5041.
- **Omega(D_0)** := the set of all pointwise limits on DD^4 of admissible sequences with the bound D_0, for this
  family. sigma is the doubling: (sigma E)(x) = E(2x).
- **Critical element with the bound D_0** (repair D8, check 1019 L241): an eternal datum that has the spectral form
  exp Delta_*(T, B) = sum over r of exp(-T e_r^*(B)) in each of the four directions (its levels are then fixed by
  Lemma LV), with, for every b in DD: s_*(b) >= 1/5041; d_min <= D_*(b) <= D_0, d_min = (1/8) log(1 + 1/5041) > 2.47 x 10^(-5);
  z_*(b) <= 256 D_*(b/4) + 34.11.
- **Uniformly recurrent** element E of Omega(D_0): for every finite set of quadruples and every eps > 0, the integers t
  with abs(sigma^t E - E) < eps on that set have bounded gaps.

## 2. The theorem

Everything in Section 2 is for a family with units under (S0). Marks are in Section 4.

### 2.1 Form 1 (Theorem ZD-c with Corollary Z4)

**Theorem ZD-c** (`gap-phys-seed.md` L311-318, quoted in substance). These are equivalent:
(PHYS-SEED); (PHYS-SEED-Delta): there is l' in P with D^+(l') < 6.1 x 10^(-4); (Z-SEED): there is L in P with
z^-(L) > 2 psi^+(L) + 30, psi^+(L) the upper limit over j of Phi_4(L/(4 a_j); beta_j); and [(BDD-Delta) and (Z-UNB)].

**Trichotomy, form 1.** Exactly one of the following holds.

- **(I)** (PHYS-SEED).
- **(II)** (BDD-Delta) fails: for every L_0 in P, D^+ is unbounded on the sizes L >= L_0 of P (it may be +infinity at
  one size). In words: the Casimir free energy is unbounded on physical sizes.
- **(III)** (BDD-Delta) holds and (Z-UNB) fails. Then, for every bound (L_0, D_0) of (BDD-Delta):
  z^-(L) <= 256 D_0 + 30 for every L in P with L >= 4 L_0. This is branch G of Corollary Z4 at every size: for each
  such L, infinitely many lattices of the trajectory have a level of the periodic cube of side L within
  (256 D_0 + 30 + eps)/L of the ground state, in physical units, for every eps > 0.

Also: (I) holds if and only if (W) holds.

**Corollary Z4** (one coupling; `gap-phys-seed.md` L322, with the correction of check 727, L80). Let D(a) <= D_0 for
all a >= a_0. Then either (branch G) b m(b^3) < 256 D_0 + 29.64 for every multiple b of 4 with b >= max(4 a_0, 12), or
(branch M) there are N and c > 0 with m(L^3) >= c/N for every integer L >= 2N.

### 2.2 Form 2 (Theorems CE and CR, Proposition OM, Corollary TRI)

**Theorem CE** (`gap-compact-rigidity-max.md` L170-178). (i) If (BDD-Delta) holds with the bound (L_0, D_0) and
(PHYS-SEED) fails, there is an admissible sequence with the bound D_0. (ii) Every admissible sequence has a subsequence
along which Delta^(j_i,k_i) converges at every x in DD^4 and every rescaled level converges in (-infinity, +infinity].
The limit Delta_* is symmetric; it has the spectral form in each direction; every non-strict inequality of the engine
between finitely many values, with both sides continuous in those values (repair D9), holds for it; it is a critical
element with the bound D_0; and the centre flips give a sign +1 or -1 to each level, with the vacuum even.

**Proposition OM** (L225-231; repairs D1, D2). For each D_0: (a) Omega(D_0) is compact for pointwise convergence and
sigma is a homeomorphism of it onto itself. (b) If (PHYS-SEED) holds, Omega(D_0) is empty for every D_0. If (PHYS-SEED)
fails and (L_0, D_0) is a bound of (BDD-Delta), Omega(D_0) is not empty. (c) If Omega(D_0) is not empty, every continuous
Lambda on it has an element E with Lambda(sigma E) >= Lambda(E). (d) If Omega(D_0) is not empty, it contains a uniformly
recurrent element.

**Theorem CR** (L241; repair D2 and fact (F3) of check 1019). Let (BDD-Delta) hold, let (L_0, D_0) be any bound of it,
and Omega = Omega(D_0). These are equivalent: (1) (W); (2) (PHYS-SEED); (3) Omega is empty; (4) Omega has no uniformly
recurrent element; (5) there is a continuous Lambda on Omega such that no element E of Omega has
Lambda(sigma E) >= Lambda(E). The equivalence of (1) and (2) does not need (BDD-Delta).

**Corollary TRI** (L350; repair D3). At least one of these holds:

- **(I)** (PHYS-SEED);
- **(II)** (BDD-Delta) fails;
- **(III')** for some D_0, Omega(D_0) of this family has a uniformly recurrent element.

(I) excludes (II) and excludes (III'). The lane does not show that (II) excludes (III').

**Link of the two forms.** If (II) fails, then (III) of 2.1 holds if and only if (III') holds, and then Omega(D_0) has a
uniformly recurrent element for every bound (L_0, D_0) of (BDD-Delta). Each such element is a critical element with
the bound D_0.

### 2.3 What (I) gives (the gap leg)

- **(G1), on the lattice.** If (PHYS-SEED) holds at l, there is q' < 1 such that for all large j: every periodic cube
  of integer side L >= l/a_j has (l/(2 a_j)) m_j(L^3) >= log(1/q'). In physical units the gap of every cube of side
  at least l is at least 2 log(1/q')/l, uniformly in j. Also D_j <= 1024 q'^(2^k)/5041 at every size from 2^k l on.
- **(G2), limit states at one cutoff.** Every limit state of an admissible sequence of tori (sense of
  `gap-seed-limit.md` Section 4) at the cutoff j clusters at the rate M_* = 2 log(1/q')/l in physical units, and its
  transfer operator has norm at most exp(-M_* t a_j) on the complement of the vacuum (Proposition P).
- **(G3), the continuum, conditional.** Let D_inf be a continuum time-reflection datum with (P1)-(P4), a class of
  observables with positive-time convergence (H2) and totality (TOT) (Proposition P', `gap-seed-limit.md` L200). Then
  D_inf has a unique vacuum and spec(H) lies in {0} union [M_*, infinity).
- **The sector.** For the algebra of the tr(F^2) sector the limit step needs the even sector only: hypothesis (G_ev)
  of Theorem EV-L (`gap-flux-exercise.md` L143), which (PHYS-SEED) implies (L185).

So "(I) gives the mass gap of the continuum limit" is true **given** the datum D_inf with (H2) and (TOT). Nobody
supplies these: they are the existence chain T0, which is not proved.
