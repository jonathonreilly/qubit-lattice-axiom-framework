lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-16T10:56Z

# The conditional dichotomy of the gap lane (queue row 1024, `gap-dichotomy-write`)

Status: DONE 2026-11-15 (all eight steps). Writing row, work item W4 of row 998. No new mathematics. Unchecked. This note does not land.
The note starts at the heading "The note"; the plan and the working log above it are the run record.
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
  at L_1 is strict), Corollary Z4 L80 HOLDS AFTER CORRECTION (sides b multiples of 4, b >= max(4 a_0, 12)); table L124-127.
  Not covered there (L12, L137): the proofs of Lemma A, K, X, E', Theorem S, Corollary S3', Theorem SH, Proposition Delta.
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

- The account's own tori have side 2 L^m with odd L (row 959, point 2; `gap-seed-limit.md` L204, item 5). They are not
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

## 3. Proofs by citation

Each line names the statement used, the file and line of its proof, and the line of its check. "727" =
`gap-phys-seed-check.md` (Claude Opus 5.5 high). "1019" = `gap-compact-rigidity-check-opus.md` (Claude Opus 5.5 max).
Both are of the author's provider. "PS" = `gap-phys-seed.md`; "CRm" = `gap-compact-rigidity-max.md`; "CR0" =
`gap-crux-restate.md`.

### 3.1 Theorem ZD-c

Proof at PS L320; check 727 L73-78 (HOLDS; every constant is fixed before j is taken large). The steps:

1. (PHYS-SEED) gives (BDD-Delta) and (Z-UNB). Fix q' < 1 with 5041 S_j <= q' for all large j. Lemma Z3 (PS L283-294;
   727 L56-60) gives D_j <= 1024 q'^(2^k)/5041 at every size from 2^k l on. Corollary S3' (CR0 L217-219; row 699) gives
   (L/a_j) m_j >= 2 (L/l) log(1/q').
2. (BDD-Delta) and (Z-UNB) give (PHYS-SEED). Choose L_1 >= 4 L_0 in P with z^-(L_1) > 256 D_0 + 30. For all large j,
   (C_b) of Corollary Z1 (PS L259-264; 727 L44) holds at b = L_1/a_j, so S_j(L_1/(2 a_j); (L_1/a_j)^3) <= exp(-7.436)
   < 1/1650 (727 L75). The two-stage line of Theorem SH (`gap-seed-shape.md` 1.5, L138) turns this into the 1/5041 form at a
   larger size of P (PS L304, "(C) gives (A)"; 727 L67, L74).
3. (PHYS-SEED) and (PHYS-SEED-Delta): Proposition Delta at the ratio 4 and Theorem SH (i) at the line r = 4 one way
   (PS L304 "(B) gives (A)"; 727 L64, L76), Lemma Z3 the other way.
4. (PHYS-SEED) and (Z-SEED): Corollary Z1' (PS L274-279; 727 L54) and psi^+(L) <= 256 D^+(L/4) (727 L77).

Inputs read: Theorem S and Corollary S3', Lemma E' (CR0 3.4), Theorem SH, Proposition Delta at the integer ratio 4,
Lemma A and the exchange of axes (items A1, A2 of row 1017).

### 3.2 The trichotomy, form 1 (assembled in this note; propositional steps only; unchecked)

- "Exactly one". (II) is the negation of (BDD-Delta). If (BDD-Delta) holds, exactly one of "(Z-UNB)" and "not (Z-UNB)"
  holds. By Theorem ZD-c, (I) is "(BDD-Delta) and (Z-UNB)". So the three cases are (I), "not (BDD-Delta)", and
  "(BDD-Delta) and not (Z-UNB)": a partition.
- The bound in (III). Let (L_0, D_0) be a bound of (BDD-Delta) and suppose z^-(L_1) > 256 D_0 + 30 for one L_1 >= 4 L_0
  in P. Step 2 of 3.1 uses this one size only and gives (PHYS-SEED) (PS L320; 727 L75; fact (F3) of 1019, L63). Then
  (Z-UNB) holds by Theorem ZD-c, against (III).
- (I) if and only if (W): fact (F3) of 1019, L63, and 1019 L151. If (W) holds, Step 2 of 3.1 gives (I). If (I) holds,
  Theorem ZD-c gives a bound (L_0, D_0) and, by (Z-UNB), a size L >= 4 L_0 with z^-(L) > 256 D_0 + 30.

### 3.3 Corollary Z4

Proof at PS L323: if (C_b) holds for one multiple b of 4 with b >= max(4 a_0, 12), Theorem ZD ((C) gives (A), PS L304;
727 L62-69) gives a seed, and Corollary S3' gives branch M. Check: 727 L80, HOLDS AFTER CORRECTION (the range of b).

### 3.4 Theorem CE

Statement CRm L170-178; proof L180-196; check 1019 L99-125 (CORRECT, first failing step none).

- (i)(b): Lemma UF (CRm L162-164; 1019 L91-97) gives a subsequence with no seed at any size of P for large j; the
  choice k_i = 2i + i_0 (CRm L180; 1019 L103).
- (ii): bounds from A2 (CRm L182); a diagonal subsequence on a countable set (L184); the tail bound at the time T/2
  (L186-190; 1019 L69); the thermal sums (L192); the constants d_min and 34.11 from Proposition Delta at the ratio 2
  and Lemma Z at T_0 = b/4, T = b/2 (L194; 1019 L72, L119); the centre signs (L196; 1019 L121, which adds that the
  three flips commute).

### 3.5 Proposition OM, Lemma LV

Statement CRm L225-231; proof L233-237; check 1019 L129-143 (CORRECT with D1, D2, D11). Repairs applied here: D1 (add
"j >= n" in the diagonal choice of (a), 1019 L73, L237); D2 (the second half of (b) needs D_0 to be a bound of
(BDD-Delta), 1019 L133, L233). (d) uses Zorn's lemma once (CRm L236; 1019 L137). Lemma LV: CRm L394-396; 1019 L141.

### 3.6 Theorem CR

Proof CRm L243; check 1019 L147-160 (CORRECT given Theorem ZD-c, with D2). (1) and (2): fact (F3) and Theorem ZD-c.
(2) gives (3): OM (b), first half, for every D_0. (3) gives (2): Theorem CE (i)(b) and (ii), with D_0 a bound of
(BDD-Delta). (3) gives (4), (5): trivial. (4) gives (3): OM (d). (5) gives (3): OM (c).

### 3.7 Corollary TRI and the link

- TRI: proof CRm L352; check 1019 L172 (CORRECT after D3). If (I) and (II) fail, (BDD-Delta) holds with some bound
  (L_0, D_0); Theorem CE (i)(b), (ii) and OM (d) give (III'). (I) excludes (II): Lemma Z3 gives D_j <= 1024/5041 from
  the seeded size on, for all large j. (I) excludes (III'): OM (b), first half.
- The link (assembled here from the same lines; unchecked). Let (II) fail. If (III) holds, (I) fails (3.2), so TRI's
  proof gives a uniformly recurrent element in Omega(D_0) for every bound (L_0, D_0). If (III') holds, (I) fails
  (OM (b), first half), so (III) holds by 3.2. Every element of Omega(D_0) is a critical element: Theorem CE (ii)(d).

### 3.8 The gap leg

- (G1): Corollary C (`gap-crux-fp.md` L449; check `gap-crux-fp-check.md` L126) is Corollary S3' at each j. The bound
  on D_j is Lemma Z3.
- (G2): Proposition P (`gap-seed-limit.md` L188-196), with (SEED-phys) supplied by (PHYS-SEED): n_j = l/(2 a_j),
  ell_* = l/2, s_* = q'/5041. It reads Theorem L3 (L138). Checks: row 703 (Claude Opus 5.5, same provider; every
  integer side) and row 723 (gpt-6-astra max, `gap-limit-astra.md` L916-926: HOLDS with scope corrections; P (a) needs a
  uniform seed margin and control of the physical size, which (PHYS-SEED) gives).
- (G3): Proposition P' (`gap-seed-limit.md` L200-202), given `gap-os-equiv.md` (5a)-(5c). Check 723: "P' additionally
  needs the continuum datum, positive-time convergence and totality". These are OPEN (`gap-seed-limit.md` L204, item 4).
- The sector: Theorem EV-L, `gap-flux-exercise.md` L135-145, proof 8.2 (L420); cross-provider check row 732 (gpt-6-astra
  max, `gap-flux-exercise-check.md`): HOLDS. Its passage to the transfer operator of the limit and to the continuum "was
  not rewritten" (`gap-flux-exercise.md` L18). It reads the twisted transfer operator (TM-tw) (Theorem TW-T,
  `gap-transfer-twisted.md`, row 1004; check 1008, same provider).

## 4. Inputs, marks, and what is open

Marks: PROVED = a written hand proof exists. "Same provider" = one line-by-line reading by Claude Opus 5.5 of a text by
Claude Fable 5.2. "Cross-provider" = one reading by gpt-6-astra. No file under `gates/` names this lane
(`parts/gap.md` L100-102), so no input carries `implication` or `discharged`. A check is one reading, not an audit.

### 4.1 Inputs that the trichotomy reads (Sections 2.1, 2.2)

| # | Input | Where | Mark in the lane | Checked by | Standing for this note |
|---|---|---|---|---|---|
| 1 | (TM): Z(n) = Tr T_B^k, T_B positive, trace class, simple top eigenvalue; symmetry of Z in the four sides; Lemma A; f finite (A1, A2) | `gap-crux-restate.md` L29-45, L174-176; `gap-transfer.md` (row 667); boxes with unequal sides: `gap-seed-check.md` Lemma 1.1 | PROVED | rows 671, 698 (same provider), 699 (cross-provider; Sections 1, 3.1, 3.4) | checked; the unequal-sides lemma is same provider only (row 703: "not re-checked") |
| 2 | Centre flips commute with T; twisted traces (A4, (TM-c)) | `gap-crux-restate.md` L35, L98, L105 | PROVED | rows 698, 699 | checked; read only by Theorem CE (ii)(e) |
| 3 | Theorem S, Lemmas K, X, E | `gap-crux-restate.md` L170-203 | PROVED from (TM) | rows 698, 699 | checked, cross-provider |
| 4 | Lemma E', Corollary S3' | same file L213-219 | PROVED (written by gpt-6-astra, row 699) | re-derived by the lead (Claude) | checked, cross-provider in the other direction |
| 5 | Theorem SH, the lines r = 4 and "r = 2, two stages" | `gap-seed-shape.md` 1.4-1.5, L89, L138 | PROVED | row 707 (same provider), row 722 (cross-provider, `gap-sh-astra.md`: HOLDS, domain 1 <= p) | checked, cross-provider |
| 6 | Proposition Delta | `gap-mid-max.md` 4.3, L63 | **PROVED GIVEN** Theorem SH | row 709 (same provider) | same provider only. This note reads it at the integer ratios 2 and 4, where a two-line proof from E_0 <= 0 and A2 was re-derived in check 1019, L55 |
| 7 | Lemma Z, Corollary Z1 | `gap-phys-seed.md` L253-264 | **PROVED GIVEN** Proposition Delta | check 727 L42-44 (same provider) | same provider only |
| 8 | Lemma Z', Corollary Z1' | same file L268-279 | **PROVED GIVEN** Lemma A | check 727 L48-54 | same provider only |
| 9 | Lemma Z3 | same file L283-294 | **PROVED GIVEN** Theorem S, Lemma E', Corollary S3' | check 727 L56-60 | same provider only |
| 10 | Theorem ZD | same file L296-304 | **PROVED GIVEN** Theorem SH, Proposition Delta, Lemmas Z, Z', Z3 | check 727 L62-69 | same provider only |
| 11 | Theorem ZD-c | same file L311-320 | **PROVED GIVEN** Theorem ZD and its inputs | check 727 L73-78: HOLDS | same provider only. **The cross-provider check, row 730, was queued and never run**: no RESULT in FINISH L807, no file `gap-zd-astra.md` |
| 12 | Corollary Z4 | same file L322-323 | **PROVED GIVEN** Theorem ZD | check 727 L80: HOLDS AFTER CORRECTION | same provider only; row 730 not run |
| 13 | Lemma UF, Theorem CE, Proposition OM, Lemma LV | `gap-compact-rigidity-max.md` L160-237, L394-396 | PROVED given items 1-3, 6, 7 | check 1019 L91-143: CORRECT, with D1, D2, D7-D11 | same provider only; no cross-provider check queued |
| 14 | Theorem CR | same file L241-243 | **PROVED GIVEN** Theorem ZD-c and item 13 | check 1019 L147-160: CORRECT with D2 | same provider only |
| 15 | Corollary TRI | same file L350-352 | PROVED given item 13 and Lemma Z3 | check 1019 L172: CORRECT after D3 | same provider only |
| 16 | The assembly of this note: "exactly one" and the bound in (III) (3.2), the link (3.7), the supply of (SEED-phys) by (PHYS-SEED) (3.8) | here | assembled from the lines cited | nobody | **unchecked** |
| 17 | The repairs D1, D2, D3, D7, D8, D9 of check 1019 | check 1019 L231-242 | the check's own text | nobody (a check is not checked) | applied in this note. At 7dd0badbc the text of row 1017 still has the unrepaired wording (critical element L158, TRI (III) L350); `parts/gap.md` L135 records the scope |

Every statement in items 6-12 and 14 is still **PROVED GIVEN** in the lane's own marking. The chain below them (items
1-5) is checked by two providers. So the first form rests, above the engine, on one reading by one model of the
author's provider.

### 4.2 Inputs that only the gap leg reads (Section 2.3)

| # | Input | Where | Mark | Checked by | Standing |
|---|---|---|---|---|---|
| 18 | Corollary C | `gap-crux-fp.md` L449 | PROVED from Corollary S3' | `gap-crux-fp-check.md` L126: HOLDS | checked (same provider; it is Proposition P (a)) |
| 19 | Theorem L3, Proposition P | `gap-seed-limit.md` L138, L188 | **PROVED GIVEN** (TR), (G), Theorem S | row 703 (same provider); row 723 (cross-provider): HOLDS with scope corrections | checked, cross-provider |
| 20 | Proposition P' | same file L200 | **PROVED GIVEN** Proposition P and `gap-os-equiv.md` (5a)-(5c) | row 723: holds as an implication | conditional on item 22 |
| 21 | Theorem EV-L | `gap-flux-exercise.md` L135-145, 8.2 | PROVED given (TM-tw) | row 732 (cross-provider): HOLDS | checked; its passage to the continuum is **not written** (L18); (TM-tw) is same provider only (check 1008) |
| 22 | The continuum datum D_inf with (P1)-(P4), positive-time convergence (H2), totality (TOT) | the existence chain T0 (the account of Sussman and Alpoge, after Balaban) | **OPEN** | - | not proved; FINISH.md L11: "Existence is not proved" |
| 23 | (S0) for the account's spacings; match of the account's tori (side 2 L^m, odd L) with the sizes of P | `gap-seed-limit.md` L204 item 5; row 959 point 2 | **not verified** | - | open bookkeeping; without it the theorem is about the bare tori of P only |

### 4.3 The continuum leg on the supply side (not read by any statement of Section 2)

These would help to prove (I) or to exclude (II) from the account's data. The trichotomy does not use them.

| Input | Where | Standing |
|---|---|---|
| A5: for each fixed physical size of the account, D is bounded along the trajectory, given (UV-Z) and the density statement | `gap-phys-seed.md` L92, 1.1.5 (iii); `gap-ladder-max.md` L150 (as cited by item A5 of row 1017; L92 not re-read here) | conditional; check 727 Section 1: two assumptions unchecked. It is a bound at each size, not (BDD-Delta), which is uniform in the size |
| (TH), the extensive base, given two-sided stability with one bulk constant | `gap-ladder-max.md` L150 | **PROVED implication**; cross-provider check: HOLDS AFTER CORRECTION (`parts/gap.md` L115); its hypothesis is an interface statement of the existence chain |
| (DET), the comparison of the step normalisers on two tori | rows 987, 989; `gap-det-check-astra.md` L406 | HOLDS AFTER CORRECTION as a conditional matrix comparison from (I-loc), R and W. **Not** (DET) for the account's physical normaliser. "Elimination factors disappear at U = 1" FAILS. R, W not discharged; (I-loc) ARGUED |
| The (HC-phys) reduction: (U1), (U2) with (TH) give (W) | `gap-hcphys-max.md` L135-150; `parts/gap.md` L112 | (U1) implies (U2) HOLDS (cross-provider). (U1), (U2), (HC-phys) are **OPEN** and stronger than the target |
| (E0-tor): torus independence of the account's whole vacuum counterterm E_0^(j), up to a summable wrapping tail | `gap-idab-check-astra.md` L196-215; `parts/gap.md` L134 | **OPEN** (the justification failed; no counterexample). Needed wherever (DET) or the (HC-phys) reduction compares two tori |

### 4.4 What stays open for each case

| Case | What the lane has | What is open | Mark |
|---|---|---|---|
| (I) holds | (I) is equivalent to (W), to (PHYS-SEED-Delta), to (Z-SEED), and to "(BDD-Delta) and (Z-UNB)". Sufficient: (CAS) with theta < 1 and an extensive base (row 708); (U1) or (U2) with (TH) (row 982). | **(W)**. No route is near closure (`parts/gap.md` L166). No mechanism for the selective step is on record (L86). | OPEN |
| (I) gives the continuum gap | (G1) checked; (G2) checked cross-provider | items 22, 23; the continuum form of Theorem EV-L | OPEN |
| (II) is false | (BDD-Delta) holds in every comparison model on record (`gap-phys-seed.md` L336). A5 bounds D at each fixed size, conditionally. | **(BDD-Delta)** for SU(2): item A6 of row 1017, "OPEN; BELIEF for SU(2)". Named open by row 720; rows 982 and 1017 name it as a match and do not attack it; `library/open-core.md` has no entry; no FINISH row has it as its target (grep of the row names, 2026-11-15). | OPEN |
| (III) is false | Given (BDD-Delta) it is (LIOU): no uniformly recurrent element in Omega(D_0) (`gap-compact-rigidity-max.md` L380). Equivalent to (Z-UNB), so to (W). No rate is needed (Theorem CR (5)). | **(LIOU)**. It is target-equivalent. Every soft form of rigidity FAILS: the constants log m, m >= 2, are critical elements of the abstract class (Proposition NR, CRm L264; check 1019 L185, L199), and products absorb (Lemma PT-inf). | OPEN |
| (II) and (III') together | - | not excluded by the lane | not shown |

Comparison cases on record (recalled or lane theorems; `gap-phys-seed.md` L336; `gap-compact-rigidity-max.md` L253-255):
the record places compact U(1) at weak coupling, frozen Z_2 and a point with two phases in case (III) (for U(1) the
bounded half is GUIDE only). A broken continuous symmetry
is the one kind of model on record where (BDD-Delta) fails; it is not a gauge model of the class (recalled, not proved
here).

## 5. In plain words

Take the SU(2) lattice gauge theory in four dimensions with the Wilson action. Follow it along the sequence of
couplings that the construction of Sussman and Alpoge selects; that construction uses Balaban's renormalisation group.
Put the theory in a periodic box of a fixed physical size. Two numbers describe the box. The first number is the
Casimir free energy: it is the free energy of the box minus the bulk part. The second number is the lowest energy
gap of the box, multiplied by the side of the box. The lane proved that one of three cases occurs, and only one.
In case (I), one box is "good": the excited states have a small total weight at a time of half the side. Then every
larger box has a gap, and the gap has a lower bound in physical units that does not depend on the lattice spacing.
In case (II), the Casimir free energy has no bound when the box grows. In case (III), the Casimir free energy has a
bound, but the gap multiplied by the side also has a bound, for every box. Thus the lowest excitation of a box of
side L has an energy of the order of 1/L, as for a massless particle or for degenerate vacua. Case (III) has a second
form. Shrink the picture again and again by a factor of two. A limit object exists, and one such object returns
close to itself again and again, after waiting times that have a bound. Case (I) is the mass gap on the lattice, uniformly in the spacing. It
becomes a mass gap of the continuum theory only if the continuum theory exists, and that is not proved. The theorem
does not tell which case occurs. To prove the mass gap, a proof must exclude case (II) and case (III). Nobody knows
how to exclude them. Every tool that the lane has is true also for models with a massless particle, so no such tool
can exclude case (III).

## 6. Lean

Owner rule: a written proof needs a compute check or a Lean check before it lands. This note does not land. Nothing
here is formalized, and no Lean file exists for this lane. The table says what a Lean check would cover if it is made.
GOAL.md asks that every step can be formalized. A compute check can cover only the numeric constants: the statements
are for all sizes and all data.

**The natural layers.** Layer A is abstract: a "datum" is a function Z with (E1)-(E3). Every statement of Section 2.1
and 2.2 is a theorem about data and families of data. It uses real analysis of sums of exponentials, upper and lower
limits, a diagonal argument on a countable set, compactness of a countable product of intervals, and Zorn's lemma
once. Layer B is the model: Wilson SU(2) on a torus is a datum. Layer C is the continuum.

| Statement | Lean-formalizable as written? | What a Lean check would cover | What it would not cover |
|---|---|---|---|
| Lemma A, Lemmas K, X, E, E', Theorem S, Corollary S3' (layer A) | Yes. The setting "W(a, b) = Tr T_b^a, symmetric" can be replaced by (E1)-(E2): sums of powers of a non-negative sequence. No operator theory is needed. | every inequality and the constants 64, 71, 5041 | that Wilson SU(2) is a datum |
| Theorem SH, the lines r = 4 and "r = 2, two stages" | Yes, after the hypotheses are stated as in check 722 (integers j >= 2, 1 <= p <= q, p dividing j, q a < min b_i). The table of thresholds is finite real arithmetic (K = 22.2, x_0 = 1/25). | the recursion and the two numeric lines used here | the other lines of the table, not read here |
| Proposition Delta at integer ratios; Lemmas Z, Z', Z3; Corollaries Z1, Z1' | Yes. Finite chains of inequalities; explicit numbers (29.64, log 1650 < 7.409, 15360/15 = 1024). | all of it | - |
| Theorem ZD, Corollary Z4 | Yes, with the range of b of check 727 (multiples of 4, b >= max(4 a_0, 12)). | the five equivalences | - |
| Theorem ZD-c and the trichotomy, form 1 | Yes. The statement needs (S0) and the definitions of D^+ and z^- as limits in the extended reals. Not as written in one respect: "for all large j" must be made a quantifier in each line, and the two thresholds of (PHYS-SEED) must be one definition with a lemma. | the equivalences, uniformly in j; "exactly one"; the bound in (III) | any property of the account's trajectory |
| Lemma UF, Theorem CE | Yes, after the repairs D7-D10 are written into the statement (domain of the times; the spectral form inside the definition of a critical element; the commuting flips; the exact class of inequalities that pass to the limit). CE (ii)(c) is a schema: Lean needs it as separate lemmas, one for each inequality used. | extraction, the spectral form of the limit, the constants 2.47 x 10^(-5) and 34.11 | CE (ii)(e) needs the signs as extra data of a datum (layer A with a Z_2^3 grading) |
| Proposition OM, Lemma LV | Yes, with D1 and D2. OM (d) is the existence of a minimal set of a homeomorphism of a compact space and uniform recurrence of its points; Mathlib has compactness, Zorn's lemma and minimal actions, and the statement here is elementary. | (a)-(e) | - |
| Theorem CR, Corollary TRI, the link | Yes, with D2 and D3 (Omega(D_0) of this family; D_0 a bound of (BDD-Delta)). | the five equivalences; TRI; the link of 3.7 | - |
| Layer B: Wilson SU(2) is a datum ((TM), symmetry, simple top eigenvalue, f finite; centre flips) | Yes in principle, and it is the large part of the work: Haar measure on SU(2)^links, the transfer operator as a positive trace-class integral operator, Perron-Frobenius (Jentzsch) for the simple top eigenvalue, the trace formula on boxes with unequal sides. I do not know which of these Mathlib has today; check before any planning. | the hypothesis of every statement above, for the model | - |
| (G1), Corollary C | Yes (layer A, one line from Corollary S3'). | the uniform lattice gap | - |
| (G2), Theorem L3, Proposition P; Theorem EV-L | Yes in principle (states on local algebras, limits of states, the mixture argument). Much more text than layers A and B. | clustering of limit states at one cutoff | - |
| (G3), Proposition P' | As an implication from an abstract continuum datum: yes. As a statement about Yang-Mills: **no**, because the datum is not constructed. | the implication only | existence |

A Lean check of layer A alone would certify the trichotomy for every family of data. It would remove the dependence
on single readings in items 6-17 of Section 4.1. It would say nothing about which case occurs. The smallest useful
target is: (E1)-(E3) as a structure; Theorem S; Lemma Z3; Theorem ZD-c; the trichotomy of form 1. Form 2 is a second
target, independent of layer B.

## 7. What the theorem does not claim

- **No mass gap.** The theorem does not prove (I). (W) is open, and no route to it is near closure (`parts/gap.md` L166).
- **No claim that (II) is false, and no claim that (III) is false.** (BDD-Delta) and (LIOU) are open. That SU(2) is in
  case (I) is a belief of physics, not a result of the lane.
- **No continuum theory.** Existence is not proved. In case (I) the continuum gap follows only given the datum of
  Proposition P', with positive-time convergence and totality.
- **No statement about the account's own tori** (side 2 L^m, odd L), and no check that the account's spacings satisfy (S0).
- **No new mathematics.** Form 2 is an equivalent form of form 1 (`gap-compact-rigidity-max.md` L249: "What is not
  new. The content. Theorem CR is an equivalence"). The trichotomy is a theorem of logic above Theorem ZD-c: its content
  is the equivalence of (I) with "(BDD-Delta) and (Z-UNB)", the engine behind it, and compactness.
- **No selectivity.** Every proved statement here holds for every datum: for compact U(1), frozen groups, and
  products with a massless factor (F1 of row 998, `gap-crux-exercise3-max.md` L236-238). So the theorem is equally true
  for models in case (III).
- **No independent check.** Above the engine, every input has one reading by a model of the author's provider. The
  cross-provider check of Theorem ZD-c (row 730) was never run. This note itself is unchecked.
- **No status.** No gate file names this lane. The note is research-stage working state and does not land.
- **Not that (II) and (III') exclude each other** in form 2. Form 1 is a partition; form 2 is "at least one".

## 8. For the lead

1. Row 730 (`gap-zd-astra`, the cross-provider check of Theorems ZD, ZD-c and Corollary Z4) has no result and no
   output file. The milestone rests on it. Row 998's W4 asks for "one cross-provider check" of this note; one check
   can cover both: `gap-phys-seed.md` L253-323 and Sections 2-3 here (items 7-12, 16 of 4.1).
2. Check 1019 is of the author's provider. Items 13-15 have no cross-provider check queued.
3. The repairs D1-D3, D7-D9 are not yet in the text of row 1017's file (seen at L158, L350).
4. (S0) against the account's spacings (item 23) is bookkeeping that nobody did.
5. `parts/gap.md` L118 can cite this note for Theorem ZD-c and Corollary Z4. Its mark stays "unchecked (lane: PROVED
   GIVEN; same-provider check 727; no gate)". I did not edit `parts/gap.md`.

## 9. Run record and RESULT

- Read in full: `gap-phys-seed.md` L225-349; `gap-compact-rigidity-max.md` L127-272, L342-399;
  `gap-compact-rigidity-check-opus.md` (all); `gap-phys-seed-check.md` (all); `parts/gap.md` (all); `gap-crux-restate.md`
  L170-222; `gap-seed-limit.md` L182-206; GOAL.md; FINISH.md L1-84 and the rows 697-709, 720-734, 959, 987-993, 1017, 1019,
  1024 (head and RESULT of each).
- Read in part (statement or RESULT only): `gap-flux-exercise.md` C2-C3 and its "not covered" list; `gap-limit-astra.md`
  result section; `gap-det-check-astra.md` L1-30, L406; `gap-idab-check-astra.md` L196-215; `gap-ladder-max.md` L146-152;
  `gap-hcphys-max.md` L135-150; `gap-crux-fp.md` L447-458; `gap-crux-exercise3-max.md` L105-136, L236-250, L925-945.
- Not read: the proofs of the engine (taken as checked); `gap-seed-shape.md` beyond the anchors; `gap-os-equiv.md`;
  `gap-transfer.md`; the account's TeX and Balaban's papers (no statement here cites a line of them); rows 722 and 723
  beyond their RESULT; `gap-sh-astra.md`.
- One cross-branch look: a depth-1 blobless fetch of this branch's head and of PR 10149 into /tmp/gap-dichotomy-scratch,
  file listing only, to look for `gap-zd-astra.md`. Not found. Main and PR 10114 were not searched (this row derives
  nothing).
- No numeric run; the numeric lock was not taken; memory was not measured. No subagents. No file other than this one was
  written. No commit, no push.
- Last step (Step 8): the cited line numbers were compared once with the sources where the source was read with line
  numbers; three were corrected (two lines of check 727, one of `gap-seed-limit.md`).

RESULT: Row 1024 (Claude Fable 5.2 medium, Mac mini worker 1; writing row, no new mathematics, unchecked, does not land). Written once and exactly, for a family of Wilson SU(2) lattices with units under (S0) (the couplings of the Sussman-Alpoge account, built on Balaban's renormalisation group; credited): form 1, exactly one of (I) (PHYS-SEED), (II) not (BDD-Delta), (III) (BDD-Delta) with z^-(L) <= 256 D_0 + 30 at every size L >= 4 L_0 of P (Theorem ZD-c, Corollary Z4); form 2, with the repairs D1-D3, D7-D9 of check 1019, at least one of (I), (II), (III') a uniformly recurrent element in Omega(D_0) of the trajectory (Theorems CE, CR, Proposition OM, Corollary TRI); given not (II), (III) iff (III'); (I) iff (W). Each proof is by citation of file and line, with a table of 23 inputs and marks, a plain-words paragraph, a Lean section and a list of non-claims. Found: the cross-provider check of Theorems ZD, ZD-c and Corollary Z4 (row 730) was never run, so everything above the engine (Proposition Delta, Lemmas Z, Z', Z3, Theorems ZD, ZD-c, CE, CR, Proposition OM, Corollaries Z4, TRI: all still PROVED GIVEN or same-provider only) rests on one reading by a model of the author's provider; the assembly steps of this note (the partition, the bound in (III), the link) are unchecked. Open, not moved: (W), (BDD-Delta), (LIOU); the continuum gap from (I) needs the continuum datum with positive-time convergence and totality (existence, not proved) and the unverified match (S0) with the account's tori; (DET), (HC-phys), (TH), (E0-tor) are on the supply side and are not read by the theorem. No mass gap is claimed, and no claim that (II) or (III) is false.
