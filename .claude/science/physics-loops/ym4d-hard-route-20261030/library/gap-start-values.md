lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-17T03:03Z

# gap-start-values (row 1058): (E0-tor) and the start values D^+ at first passage

Started 2026-11-16T15:03Z (date -u). Pinned commit 2f317758f. Status: IN PROGRESS. Nothing below is checked by a second reader.

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
  (8.22:eq-vacuum-energy-density-4)-(6) (CA-II 141441-141497).

So the stop condition of the brief does not fire: the localisation of the whole E_0^(j) is stated, by label
8.22:lem-vacuum-energy-density, as an implication from (a)-(c). What the label leaves out is named in Step 4.
