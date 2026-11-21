lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-17T03:03Z

# gap-start-values (row 1058): (E0-tor) and the start values D^+ at first passage

Started 2026-11-16T15:03Z (date -u). Pinned commit 2f317758f. Status: DONE (one session, ended 2026-11-16T15:11Z by `date -u`; no numeric run; no subagent). Nothing below is checked by a second reader.

## 0. Plan (at most eight steps; one step per response, result appended before the next)

1. Read `parts/gap.md` and section 7.2 of `library/gap-direction3-max.md`; restate (SV1), (SV2) = (E0-tor), (SV3), the consumer, and the stop condition. Grep `library/open-core.md` and FINISH rows for overlap.
2. Locate in the Sussman-Alpoge complete account (after Balaban) the definition of the vacuum counterterm E_0^(j) and any localisation statement (CA labels); decide the stop condition.
3. Tests first: the Gaussian model of the check of row 993 (exact torus independence false, tail needed) and the free value of Lemma FV.
4. (SV2): statement and argument by locality (non-wrapping terms coincide, wrapping terms carry kernel decay), or the exact missing statement.
5. (SV1) and (SV3): statements, arguments, what fails.
6. Controls (compact U(1)), kill tests, five-dimensional sign test.
7. Verdict table with marks PROVED / ARGUED / OPEN / FAILS, credits, RESULT line.

## 1. Step 1: the statements, the consumer, the overlap grep (no new mathematics)

Read: `parts/gap.md` (L112-140, L254 in full; the rest by its first 330 characters per line), `gap-direction3-max.md`
7.2 in full, `gap-idab-check-astra.md` L140-215, `gap-ladder-max.md` L138-154, `gap-phys-seed.md` L60-96,
`gap-dichotomy.md` L340-356, `gap-afield-b-max.md` B15 and L290-300, `gap-uv-rigidity-max.md` 4.1 (statement), 4.2.

**Objects (RECALLED).** Wilson SU(2). F(n; beta) = log Z on the periodic torus with n sites on each side.
f(beta) = inf over tori of F/abs(n). D(n; beta) = F(n; beta) - f(beta) n^4 >= 0 (`gap-uv-rigidity-max.md` 4.1).
Along the account's trajectory (beta_j, a_j), D_j(n) is this number at beta_j, and D^+(L) is the upper limit
over j of D_j(L/a_j) at the physical side L. The account's tori have side l = 2 L^m (L odd; here L is the
account's block ratio, not a size) with l >= l_*(g) = 2 L^11 M R(g^(-2) + B_sharp) in the first-passage unit
(`gap-phys-seed.md` L62-66). "No step of the account integrates the scales between 1 and l" (same file L65).

**Statements of the row (from 7.2).**
- (SV1) D^+(L) is finite at each size L of the account, with a bound in the account's constants.
- (SV2) = (E0-tor): the account's whole vacuum counterterm E_0^(j) agrees on two tori up to a wrapping tail
  that is summable over the scales.
- (SV3) with (SV2): D^+(2L) - D^+(L) to an error o(1) as the coupling at the scale L tends to 0.

**Consumer.** (TH) of the (CAS) route (`gap-ladder-max.md` L150), (UV-Cas) of B15 (`gap-afield-b-max.md` L216),
and the two-torus step of (DET) and of the (HC-phys) reduction (`parts/gap.md` L137).

**Overlap grep (rule 0a).** `grep E0-tor`: no hit in `library/open-core.md` or `library/open-registry.md`. Hits in
`gap-afield-a-max.md`, `gap-afield-b-max.md`, `gap-dichotomy.md`, `gap-direction3-max.md`,
`gap-registry-after-checks-max.md`: each cites the open item; none attacks it. FINISH rows with the label: 1024,
1031, 1032, 1051 (citations) and this row. No other row covers (E0-tor), (SV1) or (SV3). I go on.

## 2. Step 2: where the account states the localisation of E_0^(j) (stop condition: does NOT fire)

Source: Ethan Sussman and Levent Alpoge, `theorem_0_complete_account_raw_{I,II,III}.tex` at commit 31a47c543775
(text authored with Claude and Codex), fetched by URL into a scratch folder; after Balaban CMP 109, 116, 119, 122.
Found by `library/sa-index/ca-full/index.tsv` rows 228, 229, 1137, 1423. All lines below were read in this run.

- **CA-I Theorem 4.38:thm-torus-independence (CA-I 58187-58410; index status PROVED).** Under its listed
  statements (1)-(7) and the level hypothesis (H_j): clause (i), a non-wrapping localized term E^(j)(X; ., z),
  read on a lift, "depends neither on s nor on the lift. No operator, minimiser, partition function or scalar of
  T_j(s) occurs in it" (CA-I 58275-58281). Its first lemma is 4.38:prf-proof-non-wrapping (CA-I 58416).
  Clause (ii)(a) adds: "No rate of convergence is part of the statement" for the limit of the torus tensors.
- **CA-II Lemma 8.22:lem-vacuum-energy-density (CA-II 141276-141386, proof to 141512; index status PROVED).**
  This is the account's statement of (E0-tor). For N = 2 and two tori T_m, T_m' above the floor, under
  hypotheses (a)-(c): abs(E_m/(2 L^m)^4 - E_m'/(2 L^m')^4) <= delta-bar_vac
  := 2 (E_0 + 1) K_* sum over u >= 0 of L^(4u) exp[-(kappa/2)((1/2) L^11 L^u - 2)].
  Hypothesis (a) defines E_m: "Balaban's normalisation constant of the bare density ... less the Gaussian
  normalisers of the K steps ... the Gaussian normalisers of the two tori are compared by the determinant lemma",
  and splits each level into (vac,1) explicit numbers times lattice counts, (vac,2) the sum of E^(j+1)(X, 1, z),
  (vac,3) the sum of R^(j+1)(X, 1). So the account's E_m is the reading the gpt-6-astra check of row 993 asked
  for (CMP 119 p. 279: the vacuum values of E^(k+1) and R^(k+1) are in it), not reading (i) of row 993.
  Hypothesis (c) is exactly "matching non-wrapping coefficients": a bijection of non-wrapping X on the two tori
  with equal numbers, taken from Theorem 4.38 (i), (iii)(b) and the lift lemma. The wrapping tail is the proof's
  (8.22:eq-vacuum-energy-density-4)-(6) (CA-II 141441-141507).

So the stop condition of the brief does not fire: the localisation of the whole E_0^(j) is stated, by label
8.22:lem-vacuum-energy-density, as an implication from (a)-(c). What the label leaves out is named in Step 4.

**Addendum to Step 2: what Lemma 8.22 leaves out, by label (read in this run).**

- (G) The Gaussian normalisers. Hypothesis (a) excludes them ("less the Gaussian normalisers of the K steps",
  CA-II 141288-141291), and the remark after the proof says "The determinant lemma, which compares the Gaussian
  normalisers of the steps excluded by hypothesis (a), contributes a further constant" (CA-II 141531-141534).
  `grep -i "determinant lemma"` over the three files finds only these two places and CA-I 103833 (a different
  lemma, "for the survivors, which forms det A_ss only"). So the two-torus determinant lemma is **named and
  not stated** in the account. It is the lane's (DET): rows 986 (`gap-detlemma-read-opus.md`), 987
  (`gap-det-fable.md`, Lemma A', Corollary B), 989, check `gap-det-check-astra.md` (HOLDS AFTER CORRECTION as a
  conditional matrix comparison; (ID) open). **Rule 0a: match named, not attacked here.**
- (G') A reading that may make (G) empty; not decided here. Balaban CMP 119 pp. 273-274, (3.33)-(3.38), and
  p. 276 put the determinant inside the localized terms: the number -(1/2) log lambda_0 "contributes to the
  vacuum energy renormalization, so we include it into the definition of E_0^(k)", and the resolvent term of
  (3.37) is "represented by the generalized random walk expansions ... a representation of the form (3.47)".
  CA-I 106163-106206 does the same (one density per bond, assigned to single-cube domains), and its Lemma
  4.38:prf-proof-non-wrapping takes "each of the three parts of (3.37)" (CA-I 58431). If the account's E^(j+1)(X, 1, z)
  of hypothesis (a) contain these determinant-born terms, the Gaussian normaliser at U = 1 is already in parts
  (vac,1) and (vac,2), and Lemma 8.22 covers it. The account's own consumer uses Z_m(0) = e^(E_m) Z~_m(0) with
  the lemma's delta_vac and no determinant constant (CA-II 141703-141727; Q_* of 8.22:thm-volume-transfer has
  only B + delta-bar_vac). So either reading (G') is meant there, or a constant is missing from Q_*. This is
  bookkeeping inside their text; I report it to the lead and post nothing.
- (Z) The residual normalised partition function Z~_m(0). The account bounds it per unit volume only:
  e^(-C_low (2 L^m)^4) <= Z~_m(0) <= e^(E_+^sharp (2 L^m)^4), B := E_+^sharp + C_low <= C_B (1 + log g^(-2))
  (CA-II Definition 8.22:not-partition-sources-cells (b), 140906-140934). Step 5 shows that all of D sits here.
- CA-III Lemma 9.10:lem-vacuum-localisation (CA-III 63431) compares two runs on one torus (sources and
  cutoffs), not two tori. It is not (E0-tor).
- The account's tori have sides 2 L^m with L odd. Two members differ by a factor L^(m - m'), never by 2. So
  "L and 2L" of the brief is not a pair of the account's family (`gap-dichotomy.md` row 23: match with P not
  verified). Below I state everything for the pair (m, m').

## 3. Step 3: tests first (hand; no numeric run)

**T1, the Gaussian model of the check of row 993.** T_n = m^2 + 2 - S - S^(-1) on the cycle of n sites. Put
2 cosh theta = m^2 + 2, theta > 0. The eigenvalues are 2 cosh theta - 2 cos(2 pi k/n), and
(e^theta - w)(e^theta - w^(-1)) e^(-theta) = 2 cosh theta - w - w^(-1) for a root of unity w. The product over the
n-th roots is e^(-n theta)(e^(n theta) - 1)^2. So

  log det T_n = n theta + 2 log(1 - e^(-n theta)).      (T1)

Check: n = 1 gives 2 cosh theta - 2 = m^2; n = 2 gives (m^2 + 2)^2 - 4 = m^2 (m^2 + 4). PROVED (identity).
What it says. (a) Exact torus independence of the density is false: the densities at n = 1, 2 differ. (b) The
whole difference is one wrapping term w(n) = 2 log(1 - e^(-n theta)), with abs(w(n)) <= 2 e^(-n theta)/(1 - e^(-n theta)):
the *total*, not only the density, is torus-free up to a tail that decays at the rate of the kernel times the
side. (c) At fixed n the tail is not small when theta -> 0: w(n) = 2 log(n theta) + O(1) -> minus infinity. A tail
statement holds only where the decay length is bounded by a fixed fraction of the side. The statement (SV2)
must carry this, and it does: the floor l >= 2 L^11 M R is that condition for each integrated step. (d) The
massless end is the model of D: -(1/2) w(n) = log(1/(n theta)) + O(1) is the free energy of the mode that
wraps, unbounded as theta -> 0 (compare Lemma FV).

**T2, the free value.** Lemma FV (row 1028, `gap-uv-rigidity-max.md` 4.1, its check is row 1030, whose verdict I did
not read; the proof was not re-read here): D(n; beta) >= (3/2) log beta - 59 n^4 - 11 on a fixed lattice
torus. So any bound of D by constants times a volume must let the constant grow like log beta at least on
that lattice. The account's bound has this form: B <= C_B (1 + log g^(-2)) (CA-II 140931-140933). The test
does not bind the account's tori (their residual lattice is not Wilson's); it fixes what (SV1) can look like:
a bound B V with B logarithmic in the coupling, and no bound free of g.

## 4. Step 4: (SV2) = (E0-tor)

Notation of CA-II Definition 8.22 and Lemma 8.22: N = 2, m >= m' >= m_T(g_-(g)), l' = 2 L^m' the smaller side,
V_m = (2 L^m)^4, E_m the constant of hypothesis (a) (so without the Gaussian normalisers).

**Lemma WT (the total form with its tail; PROVED as an implication from hypotheses (a)-(c) of CA-II Lemma
8.22; a port: the statement and every step are Sussman and Alpoge's, after Balaban; my part is to keep the
side l' in the exponent and to sum).** Put

  delta(l') := 2 (E_0 + 1) K_* sum over u >= 0 of L^(4u) exp[-(kappa/2)(l' L^u/(4M) - 2)].

Then (i) abs(E_m/V_m - E_m'/V_m') <= delta(l'); (ii) abs(E_m - L^(4(m - m')) E_m') <= V_m delta(l');
(iii) if t := kappa l'/(8M) >= 2 log L + 1/2, then delta(l') <= 4 e^kappa (E_0 + 1) K_* e^(-kappa l'/(8M));
(iv) at fixed K the limit e_inf := lim E_m/V_m exists and abs(E_m - e_inf V_m) <= V_m delta(2 L^m).

Proof. (i) is the account's (8.22:eq-vacuum-energy-density-6) (CA-II 141504-141507) with D_j of its
(8.22:eq-vacuum-energy-density-4), D_(K-1-u) = l' L^u/(4M) - 2, read before the proof replaces L^min(m, m') by
the floor value L^11 M. The steps, re-derived: part (vac,1) is a torus-free number times a lattice count, so
its density is the same on both tori; this uses that g_j, z_j are torus-free (hypothesis (c)). In part
(vac,2) the sum over X containing z does not depend on z (CMP 119 (2.29) at U = 1), so the density is
L^(4(K-j-1)) times that sum; every X containing z with d_(j+1)(X) < D_j is non-wrapping on both tori, the
non-wrapping sets correspond with equal values (hypothesis (c)), and the rest is at most
2 E_0 K_* e^(-kappa D_j/2) by abs(E(X, 1, z)) <= E_0 e^(-kappa d) and the count K_* at rate kappa/2. Part (vac,3)
is the same after averaging over one M-cube, with E_0 replaced by 1. There are L^(4u) sites of level j + 1
per unit volume, u = K - 1 - j. Sum over u. (ii) Multiply (i) by V_m; V_m/V_m' = L^(4(m - m')). (iii) The term
of index u is e^kappa L^(4u) e^(-t L^u). The ratio of term u + 1 to term u is L^4 e^(-t L^u (L - 1)) <= L^4 e^(-2t)
<= e^(-1) < 1/2, since L >= 3 and 2t >= 4 log L + 1. So the sum is at most 2 e^kappa e^(-t). (iv) delta is
decreasing in l' and tends to 0, so (i) makes E_m/V_m a Cauchy sequence; let m -> infinity in (i) with the
roles (m, m') -> (m'', m). QED

**Corollary WT1 ((SV2), the form the consumers read).** For a fixed ratio L^(m - m'), the total difference
abs(E_m - L^(4(m - m')) E_m') is at most 4 e^kappa (E_0 + 1) K_* L^(4(m - m')) l'^4 e^(-kappa l'/(8M)). It tends to 0
as l' grows. It is uniform in K, g_0 and g. The sum over the scales u is inside delta: "a wrapping tail
summable over the scales" holds, with the rate kappa/(8M) per unit of the first-passage length.

**What (SV2) is and is not.**
- It is the account's own statement, label 8.22:lem-vacuum-energy-density, with the smaller side kept. The
  gpt-6-astra check of row 993 asked for "matching nonwrapping coefficients and a summable wrapping tail":
  the first is hypothesis (c) (from CA-I Theorem 4.38 (i), (iii)(b) and the lift lemma), the second is (iii).
- Mark: **PROVED as an implication** from (a)-(c); checked by nobody. I did not check (a)-(c). The account
  declares Lemma 8.22 and Theorem 4.38 proved under their listed statements; Theorem 4.38 has seven assumed
  statements and the level hypothesis (H_j) (CA-I 58189-58268). Those are the hardening tally's, not this row's.
- It does not cover the Gaussian normalisers unless reading (G') holds; otherwise (DET) is needed (rows
  986-989, conditional).
- It is exact torus independence of nothing: by T1 the tail is really there.
- It needs the floor. At the floor t = kappa L^11 R/4 >= kappa L^11/4, so (iii) applies if
  kappa >= (8 log L + 2)/L^11 (6.1e-5 at L = 3). I did not read a lower bound for kappa in these units; without
  it use (i)-(ii) with delta(l') <= delta-bar_vac.

## 5. Step 5: (SV1) and (SV3)

Setting. Fix L, the parameters p, g <= gamma_J and m >= m_T(g_-(g)). Let K = K(g_0, g) run with g_0 -> 0: this
is the trajectory at first passage on the torus T_m of side l = 2 L^m in the first-passage unit. N_m =
V_m L^(4K) is the number of bare sites. F_m = log Z_m(0). By CA-II (8.22:eq-partition-sources-cells-4) and
hypothesis (a) of Lemma 8.22,

  F_m = E_m + G_m + log Z~_m(0),      (5.1)

with G_m the sum of the Gaussian normalisers of the K steps (G_m = 0 under reading (G') of Step 2).

Inputs, each named:
- (WT) Lemma WT of Step 4, given (a)-(c) of CA-II Lemma 8.22.
- (G-tor) abs(G_m/V_m - G_m'/V_m') <= c_G(l') with c_G decreasing to 0 in l', uniform in K, g_0, g. This is (DET)
  with its tail (row 987 Corollary B gives c_det proportional to L^(-5 min(m, m')), conditional on its inputs
  and on (ID); not re-read beyond its RESULT line). Under reading (G') it is empty, c_G = 0.
- (STAB) -C_low V_m <= log Z~_m(0) <= E_+^sharp V_m, B = E_+^sharp + C_low, uniform in K, g_0, m (CA-II Definition
  8.22 (b)).
- (TL) The thermodynamic limit: F(n)/abs(n) converges as all sides grow, and F(kn)/abs(kn) <= F(n)/abs(n) for
  multiples. RECALLED: the limit for bounded finite-range interactions is standard (Ruelle, Statistical
  Mechanics, Section 2.3); the monotony is the lane's Lemma A (a) and the account's trace sub-additivity
  (CA-II 8.22:lem-trace-subadditivity, Remark (iii), for even sides). Together: f = inf = lim. In the
  account's units (per unit volume, at fixed K): f_K := lim over m of F_m/V_m exists, and D(T_m) = F_m - f_K V_m.

**Proposition RED (all of D sits in the residual integral; PROVED given (WT), (G-tor), (STAB), (TL)).**
Put z_m := log Z~_m(0)/V_m. Then z_inf := lim z_m exists at each K, and with D~(m) := (z_m - z_inf) V_m:

  abs(D(T_m) - D~(m)) <= V_m (delta(l) + c_G(l)),   l = 2 L^m.      (RED)

Proof. Divide (5.1) by V_m. F_m/V_m converges by (TL), E_m/V_m by Lemma WT (iv), G_m/V_m by (G-tor) (a Cauchy
sequence). So z_m converges, and f_K = e_inf + g_inf + z_inf. Then D(T_m) = (E_m - e_inf V_m) + (G_m - g_inf V_m)
+ (z_m - z_inf) V_m. The first bracket is at most V_m delta(l) by Lemma WT (iv); the second at most V_m c_G(l)
by the limit m' -> infinity in (G-tor). QED

**Corollary SV1 ((SV1); PROVED given the same inputs).** 0 <= D(T_m) <= (B + delta(l) + c_G(l)) V_m <=
(C_B (1 + log g^(-2)) + delta-bar_vac + c_G) (2 L^m)^4, for every K. So D^+ at the size l = 2 L^m is finite,
with a bound in the account's constants, uniform along the trajectory.
Proof. z_m <= E_+^sharp and z_inf >= -C_low by (STAB), so D~(m) <= B V_m; add (RED). D >= 0 by (TL). QED

This is `gap-phys-seed.md` 1.1.5 (iii) (item A5 of row 1017) with its "density statement" now named: it is
Lemma 8.22 with (G-tor). Scope: the sizes are the account's (l = 2 L^m >= l_*(g), unit fixed by g up to the
first-passage window B_sharp); it is a bound at each size and grows like l^4, so it is not (BDD-Delta). By T2
no bound free of log g^(-2) can be expected.

**Corollary SV3-red (what (SV3) is; PROVED given the same inputs).** For m >= m' above the floor,

  abs([D(T_m) - D(T_m')] - [D~(m) - D~(m')]) <= 2 V_m (delta(l') + c_G(l')).

So, up to the wrapping tail of Step 4, (SV3) is a statement about the residual normalised partition function
alone: D~(m) - D~(m') = o(1). Locality of the counterterms contributes nothing else to it.

**Verdict on (SV3): OPEN. Not derivable from the account's statements; not refuted.**
- What the account gives for D~: only (STAB), so abs(D~(m)) <= B V_m + tail, an error of order one per unit
  cell, with V_m >= 16 L^44 M^4. The target is an absolute error o(1). This is Proposition 1.1 of
  `gap-phys-seed.md` once more, now with the counterterm side closed: the shortfall is in Z~ only.
- Why the mechanism of the brief stops here. Locality compares terms of steps whose kernels decay over the
  step's own length; their wrapping terms are small because the side is at least L^11 M step lengths (T1 (b)).
  Z~_m(0) is the integral that is left at the unit scale. "No step of the account integrates the scales
  between 1 and l" (`gap-phys-seed.md` L65). Its wrapping part is the case theta -> 0 of T1 (c): not small, and
  it is D.
- The prolonged run does not change this. CA-II 8.18:lem-horizon-cases (i) (CA-II 143297-143311, index status
  PROVED) runs the steps on until the torus has N_T^dagger <= 2 L^(c_gap) cells of side L^(m_T(g^dagger)), so
  (N^dagger)^4 <= 16 L^(4 c_gap + 44) M^4 R(g^dagger)^4 residual sites. The floor L^(m_T) stays. The error
  B(g^dagger)(N^dagger)^4 of its (8.18:eq-horizon-cases-c) is then still at least 16 L^44 M^4 B.
- The weak-coupling domain at the scale of the side has a name in the account: the first volume range
  K + m <= K_* - 1, implied by m <= m_V(g) (same lemma, (ii)). There the coupling at the end of the prolonged
  run is below gamma_*. So (SV3) can be stated inside the account: for members in the first volume range,
  D~(m + 1) - D~(m) -> 0 as g^dagger -> 0.
- **The exact missing statement, by label.** CA-II Definition 8.22:not-partition-sources-cells (b) (and its
  source, the lower and upper stability bounds of the correlation theorem, Balaban CMP 122b Theorem 1) bounds
  log Z~_m(0) by a constant times the volume. (SV3) needs instead: log Z~_m(0) = z V_m + c_m with
  c_(m+1) - c_m -> 0 as the coupling at the side tends to 0, on the first volume range. No statement of the
  account has this form; `grep` of the index for "Casimir", "finite-size", "zero mode" finds no statement on
  Z~ (the words "zero-mode factor" occur only in the proof of Lemma 8.22, CA-II 141424-141432, to say that
  no such number is among the counterterms).
- The pair. The account compares sides in the ratio L^(m - m'), L odd; (UV-Cas) asks for the ratio 2. Not
  available in the account's family without another statement (S0-type bookkeeping, `gap-dichotomy.md` row 23).
- Sign. (UV-Cas) asks for D(2n) <= D(n), the sign of a quantity that (SV3) says is o(1). So (UV-Cas) needs
  more than (SV3): the leading term of D~(m + 1) - D~(m), expected -(3/2) log(x(l)/x(L l)) < 0 with x the
  inverse squared coupling at the side (belief I8 of row 1028; GUIDE only).

## 6. Step 6: controls, kill tests, the five-dimensional sign

**Control, compact U(1) with the same blocking.** (SV2): Lemma WT uses of the model only hypotheses (a)-(c):
the itemisation, the decay bound, the count K_*, torus-free running constants, the non-wrapping bijection. No
step uses the size or the direction of the flow of g_j. With a constant coupling the same proof gives the same
tail. PASS (ARGUED: I did not read a U(1) version of (a)-(c); the claim is that the proof of Lemma WT is blind
to the group). (SV3): for any model whose trajectory has a constant coupling and spacings a_j = a_0 b^(-j),
D^+(b L) = D^+(L) exactly, because D_j(b L/a_j) = D_(j+1)(L/a_(j+1)) and the upper limit drops one term.
PROVED (one line). So the control gives 0, with no running, as required; and (RED) is consistent with it.

**Kill tests, line by line.**
- Lemma PT (row 998; D adds over a product with a massless factor). It binds statements claimed for the whole
  class. (SV1)-(SV3) read the account's itemised constants of Wilson SU(2) at first passage (kind (K-flow) of
  rule W2). A product model has no such itemisation. Does not bind. It does agree with (RED): a massless
  factor would enter through Z~, not through the counterterms.
- Proposition NP (row 1003; a model in which D contracts with no seed). It binds inductions on the history of
  D. (SV1) and (SV2) are bounds at one size; (SV3) is one comparison at the weak-coupling end. No induction.
  Does not bind.
- Theorem D2 (row 979; a hypothesis with a supremum over tilts is false). (SV1)-(SV3) are at zero source; the
  account says the same of its lemma ("concerns the zero-source constant E_m only", CA-II 141522-141524). No
  supremum over tilts or sources. Does not bind.
- Lemma SHEET (row 996; a form uniform over plaquette coupling fields is false). Hypothesis (c) uses site-free
  couplings g_j, z_j; no coupling field varies. Does not bind.
None of the four binds; none supports (SV3) either.

**Five dimensions (GUIDE; a count, not a proof).** One-loop count on a torus of n^d sites at weak coupling:
the tree-gauge slice has 3(d - 1) n^d + 3 dimensions, the flat set in it d + 2 (commuting d-tuples, modulo
nothing but with the 2-dimensional conjugation orbit kept). So F = -((3(d - 1) n^d + 1 - d)/2) log beta + O(1)
at fixed n, f = -(3(d - 1)/2) log beta, D = ((d - 1)/2) log beta + O(1). At d = 4 this is the (3/2) log beta of
Lemma FV. With beta read as the inverse squared coupling at the side: at d = 4 it falls with the side
(asymptotic freedom), D(2L) - D(L) < 0 and tends to 0; at d = 5 it is L/g^2, so D(2L) - D(L) -> 2 log 2 > 0. The
sign changes, as the brief requires. In five dimensions (SV3) in the form "o(1)" is then false; the o(1) is
a property of marginal running. Nothing here is proved for the trajectory.

## 7. Step 7: marks, scope, credits, texts for the lead, RESULT

### 7.1 Marks

| Item | Mark | Given | Where |
|---|---|---|---|
| Stop condition of the brief (the account does not localise E_0^(j)) | does not fire | CA-II 8.22:lem-vacuum-energy-density; CA-I 4.38:thm-torus-independence | Step 2 |
| The two-torus "determinant lemma" is named in the account and not stated | found (reading; two greps) | CA-II 141289-141291, 141531-141534 | Step 2 (G) |
| Identity (T1), log det T_n = n theta + 2 log(1 - e^(-n theta)) | PROVED | - | Step 3 |
| Lemma WT (i)-(iv), Corollary WT1 = (SV2) = (E0-tor) for the account's E_m | PROVED as an implication (port) | hypotheses (a)-(c) of CA-II Lemma 8.22, not checked here | Step 4 |
| (SV2) for the full normalisation constant | PROVED given also (G-tor) = (DET) with tail, or reading (G') | rows 986-989 own (DET); (G') not decided | Steps 2, 5 |
| Proposition RED, Corollary SV3-red | PROVED given (WT), (G-tor), (STAB), (TL) | (TL) recalled | Step 5 |
| Corollary SV1 = (SV1) | PROVED given the same | same | Step 5 |
| (SV3) | OPEN; reduced to Z~ alone; not derivable from the account's statements; not refuted | - | Step 5 |
| (UV-Cas) | OPEN; needs more than (SV3) (a sign) and the ratio 2 | - | Step 5 |
| U(1) control: (SV2) | ARGUED | proof of Lemma WT is group-blind | Step 6 |
| U(1) control: (SV3) gives 0 | PROVED | constant coupling, geometric spacings | Step 6 |
| Kill tests PT, NP, D2, SHEET | none binds (read from `parts/gap.md` L123-135, L226-227; the four proofs not re-read) | - | Step 6 |
| Five-dimensional sign | GUIDE (a count) | - | Step 6 |

Nothing FAILS. No statement of the lane is refuted.

### 7.2 Scope of each negative statement

- "(SV3) is not derivable from the account": from the statements I read (CA-II Definition 8.22 (b), Lemma 8.22
  and its remark, 8.18:lem-horizon-cases, and an index grep for Casimir, finite-size, zero mode). I did not read
  the 1,647 statements; a statement on Z~ under another name would change this.
- "The determinant lemma is not stated": two greps over the three files for the words "determinant lemma",
  `lem-determinant`, "log-determinant", "determinants of the two tori". A statement under another name is possible;
  row 986 (`gap-detlemma-read-opus.md`) is the lane's reading of the same point and I did not re-read it.
- "Locality cannot give D~": this is the reduction (RED) plus the model T1 (c). It is not a theorem that no
  local argument works; it says that every counterterm-side term is already accounted for.

### 7.3 What changes for the consumers

- (TH), the extensive base (`gap-ladder-max.md` L150): its hypothesis "two-sided stability with one bulk
  constant" is (STAB) + Lemma WT + (G-tor), with c_F = B + delta + c_G. So (TH) has its lower end as an
  implication from labelled statements of the account plus (DET). Theta is polynomial in the side, as stated
  there.
- (DET) and the (HC-phys) reduction (`parts/gap.md` L137): the two-torus step for the counterterm E_m is
  Lemma WT. What they still wait for is (G-tor)/(ID) of rows 987-989, or the decision on reading (G').
- (UV-Cas) of B15 and the (CAS) route's lower end beyond (TH): no supply. The account stops at B V. A band
  argument may assume at its lower end: D^+(l) <= (C_B (1 + log g^(-2)) + small) l^4 on the account's sizes, and
  nothing about D^+(L l) - D^+(l).

### 7.4 Texts for the lead (proposals; no other file was edited)

- `parts/gap.md` L137, replace "open ... (E0-tor)" by: "(E0-tor): for the account's E_m (Gaussian normalisers
  excluded) it is CA-II Lemma 8.22:lem-vacuum-energy-density; total form with tail = Lemma WT of row 1058
  (`library/gap-start-values.md` Step 4), PROVED as an implication from that lemma's hypotheses (a)-(c),
  unchecked. Open: the Gaussian normalisers ((DET), rows 986-989, or reading (G') of row 1058 Step 2)."
- New line: "(SV3)/(UV-Cas): reduced by Proposition RED of row 1058 to the Casimir part of the account's
  residual Z~_m(0), which the account bounds only by B V_m (CA-II Definition 8.22 (b)). OPEN; no row attacks
  it; it is the two-torus form of Proposition 1.1 of `gap-phys-seed.md`."
- A check row for Lemma WT, Proposition RED and the Step 2 reading (G)/(G') (cross-provider), before any use.
- For the hardening tally, not for a post: the account's 8.22:thm-volume-transfer uses Z_m(0) = e^(E_m) Z~_m(0)
  with the delta_vac of a lemma whose E_m excludes the Gaussian normalisers (CA-II 141703-141727 against
  141288-141291). Either reading (G') is meant or Q_* lacks the determinant constant. Rules 0g-0i and the five
  checks of rule 6 apply before anything goes out; this row checked none of them.

### 7.5 Credits and provenance

Every statement of Steps 2, 4 and 5 about counterterms, localisation, torus independence, stability constants
and prolonged runs is from Ethan Sussman and Levent Alpoge's complete account
(`theorem_0_complete_account_raw_{I,II,III}.tex`, commit 31a47c543775, text authored with Claude and Codex),
which builds on Tadeusz Balaban's renormalization group papers (CMP 109, 116, 119, 122; CMP 119 pp. 273-279
read here in the local OCR). The Gaussian test model is from the gpt-6-astra check of row 993. Lemma FV is
row 1028's; (DET) is rows 986-989's; Proposition 1.1 and 1.1.5 (iii) are row 720's (`gap-phys-seed.md`); the
brief is row 1051's Section 7.2. This file: Claude Fable 5.2, effort medium, Mac mini worker 1, one session at
2f317758f, checked by nobody, no numeric run, no commit, nothing posted.

RESULT: Row 1058 (Claude Fable 5.2 medium, one session at 2f317758f, checked by nobody, no numeric run). The stop condition does not fire: the account of Sussman and Alpoge (after Balaban) states the localisation of the whole vacuum counterterm as CA-II Lemma 8.22:lem-vacuum-energy-density, resting on CA-I Theorem 4.38. PROVED as implications from that lemma's hypotheses (a)-(c), which were not checked here: Lemma WT = (SV2) = (E0-tor) in total form, abs(E_m - L^(4(m-m')) E_m') <= V_m delta(l') with delta(l') <= 4 e^kappa (E_0+1) K_* e^(-kappa l'/(8M)), summed over the scales; Proposition RED, D on the account's torus equals the Casimir part of the residual Z~_m(0) up to that tail; Corollary SV1 = (SV1), 0 <= D <= (C_B(1 + log g^(-2)) + delta + c_G)(2 L^m)^4 uniformly along the trajectory. PROVED outright: the model identity (T1) and the U(1) control D^+(bL) = D^+(L). OPEN: (SV3) and (UV-Cas), reduced to Z~ alone, where the account has only the per-volume stability bounds of CA-II Definition 8.22 (b), so its error is B V_m and not o(1); the account's sizes differ by powers of odd L, not by 2; the Gaussian normalisers, excluded by hypothesis (a), need the two-torus determinant lemma, which the account names (CA-II 141289-141291, 141531-141534) and does not state: this is (DET) of rows 986-989, not attacked here (rule 0a), unless Balaban's itemisation (CMP 119 (3.33)-(3.38)) already places them among the localized terms (reading (G'), not decided).
