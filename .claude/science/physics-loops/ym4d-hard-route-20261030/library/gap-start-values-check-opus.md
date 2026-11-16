lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-17T03:18Z

# Check of row 1058 (`library/gap-start-values.md`): (E0-tor) and the start values

Row 1059 (`gap-start-values-check-opus`), same-provider check (Claude Opus 5.5 max, Mac mini worker 1) of
row 1058 (written by Claude Fable 5.2 medium). Pinned commit 631c8f5a6, branch `claude/ym4d-hard-route`.
Started 2026-11-16T15:18Z (date -u). Same provider as the author, so this is not an independent check in
the sense of the working rules; row 1060 (gpt-6-astra) is the cross-provider check.

Sources credited: the Sussman-Alpoge account (CA-I, CA-II, read through `library/sa-index/` and the pinned
raw files), Balaban's papers (CMP 119 (3.33)-(3.38) and the series it rests on), and the lane's own rows
named where used.

## Plan (at most eight steps; one per response; each appended before the next)

1. Read FINISH.md rules (L52-84, L299-351), GOAL.md, and row 1058's file in full; list every claim it makes
   with its line anchor (claim table).
2. Fetch CA-II and CA-I into a /tmp scratch folder; quote Lemma 8.22:lem-vacuum-energy-density, Definition
   8.22 (Z_m, Z~_m, E_m, stability constants), trace sub-additivity, CA-I Theorem 4.38 (clause (i)); compare
   with what row 1058 uses.
3. Hypotheses (a)-(c) of the account's lemma: state them from the text and test whether they hold along the
   trajectory the lane uses (where the lane fixes it: `parts/gap.md`, (E0-tor), start values).
4. Lemma WT ((SV2) in total form, the tail delta(l')), summed over scales; by-hand test of the tail bound on
   the Gaussian model of the check of row 993.
5. Proposition RED and Corollary SV1; the model identity (T1) and the U(1) control (by hand).
6. OPEN items: (SV3) and (UV-Cas) reduced to Z~ with error B V_m; sizes differing by powers of odd L;
   Balaban CMP 119 (3.33)-(3.38) and the reading (G') of the Gaussian normalisers.
7. Meaning: is (E0-tor) of `parts/gap.md` closed conditionally on the account's lemma; what remains.
8. Verdict table and RESULT line.

## Log

- 2026-11-16T15:18Z: file created; plan written.

## Step 1: claim table of row 1058 (anchors are lines of `library/gap-start-values.md` at 631c8f5a6)

Read in full: row 1058's file (363 lines), FINISH rows 1058-1059, FINISH rules L1-84, L299-351, GOAL.md.
Repo search for this check: the inputs row 1058 names are row 993's gpt-6-astra check (Gaussian model),
rows 986-989 ((DET)), row 1028 (Lemma FV) with check row 1030, row 720 (`gap-phys-seed.md`). A check row
attacks nothing, so rule 0a is satisfied by not attacking; the OPEN items are only re-read.

| # | Claim of row 1058 | Lines | To check against |
|---|---|---|---|
| C1 | Stop condition does not fire: CA-II Lemma 8.22:lem-vacuum-energy-density states the localisation of the whole E_0^(j) | 45-70 | CA-II text |
| C2 | CA-I Theorem 4.38 (i): non-wrapping localized term independent of s and lift; quote CA-I 58275-58281; (ii)(a) "No rate of convergence" | 51-55 | CA-I text |
| C3 | Lemma 8.22 bound abs(E_m/(2L^m)^4 - E_m'/(2L^m')^4) <= delta-bar_vac = 2(E_0+1)K_* sum_u L^(4u) exp[-(kappa/2)((1/2)L^11 L^u - 2)] | 56-59 | CA-II 141276-141386 |
| C4 | Hypothesis (a): E_m = Balaban's normalisation constant less the Gaussian normalisers; parts (vac,1)-(vac,3) | 60-64 | CA-II 141288-141291 |
| C5 | Hypothesis (c) = bijection of non-wrapping X with equal numbers, from Theorem 4.38 (i), (iii)(b) and the lift lemma | 65-67 | CA-II |
| C6 | (G) the two-torus determinant lemma is named (CA-II 141289-141291, 141531-141534) and not stated | 74-81 | grep of CA-I/II/III |
| C7 | (G') Balaban CMP 119 (3.33)-(3.38), p. 276 puts -(1/2) log lambda_0 into E_0^(k); CA-I 106163-106206, CA-I 58431; consumer CA-II 141703-141727 uses no determinant constant | 82-92 | CMP 119 OCR, CA-I, CA-II |
| C8 | (STAB) e^(-C_low V) <= Z~_m(0) <= e^(E_+^sharp V), B <= C_B(1 + log g^(-2)) (CA-II 140906-140934) | 93-95 | CA-II Def. 8.22 (b) |
| C9 | CA-III Lemma 9.10 compares two runs on one torus, not two tori | 96-97 | CA-III 63431 |
| C10 | Account's tori have sides 2L^m, L odd; ratios are powers of L, never 2 | 98-100 | CA-II Def. 8.22 |
| C11 | (T1) log det T_n = n theta + 2 log(1 - e^(-n theta)) and readings (a)-(d) | 104-119 | by hand |
| C12 | Lemma FV used only as a shape test | 121-126 | row 1028 statement |
| C13 | Lemma WT (i)-(iv) with delta(l') = 2(E_0+1)K_* sum_u L^(4u) exp[-(kappa/2)(l' L^u/(4M) - 2)]; (iii) bound 4 e^kappa (E_0+1) K_* e^(-kappa l'/(8M)) when kappa l'/(8M) >= 2 log L + 1/2 | 133-156 | CA-II proof 141386-141512; by hand |
| C14 | Corollary WT1 | 158-161 | by hand |
| C15 | Floor remark: (iii) applies if kappa >= (8 log L + 2)/L^11 | 173-175 | by hand |
| C16 | (5.1) F_m = E_m + G_m + log Z~_m(0) | 184 | CA-II (8.22:eq-partition-sources-cells-4) |
| C17 | (TL) thermodynamic limit, monotony for multiples; trace sub-additivity CA-II, Remark (iii) | 195-199 | CA-II 140996; by hand |
| C18 | Proposition RED | 201-209 | by hand |
| C19 | Corollary SV1 | 211-219 | by hand |
| C20 | Corollary SV3-red | 221-226 | by hand |
| C21 | (SV3) OPEN; horizon cases CA-II 143297-143311; first volume range | 228-256 | CA-II 8.18 |
| C22 | U(1) control: (SV2) ARGUED, (SV3) gives 0 PROVED | 260-266 | by hand |
| C23 | Kill tests PT, NP, D2, SHEET do not bind | 268-281 | `parts/gap.md` L123-135 |
| C24 | Five-dimensional count (GUIDE) | 283-290 | by hand |
| C25 | Texts for the lead | 337-350 | consequences of the above |

Log: step 1 done at 2026-11-16T15:19:34Z (date -u).

## Step 2: the account's text (CA-II Definition 8.22, Lemma 8.22, its proof and remark, the consumer)

Source: `theorem_0_complete_account_raw_{I,II,III}.tex` at 31a47c543775 (Ethan Sussman and Levent Alpoge,
text authored with Claude and Codex), fetched by URL into `/tmp/ym4d-chk1059-src/` (166,711 / 145,624 /
111,583 lines). Every line number below is from `grep -n -F` on that copy.

**2.1 Definition 8.22 (CA-II 140873-140945).** Quotes: "E_m=\sum_{j<K}E^{(j)}_{\mathrm{vac}}(\mathbb{T}_m,
\mathbb{T}_m)" (140919), "where E_m is Ba{\l}aban's normalisation constant of the bare density
\rho_0=\exp[-x_0A(U)-E_m]" (140921-140922), with \widetilde Z_m(v)=e^{-E_m-\mathcal E_m(v)}Z_m(v) (140918).
Clause (b): "|\widetilde{Z}_m(v)|\le e^{E_+^{\sharp}(2L^m)^4}, \widetilde{Z}_m(0)\ge e^{-C_{\mathrm{low}}(2L^m)^4}"
(140908-140910); B = E_+^sharp + C_low does not depend on K, g_0 or m (140926-140930); "by the logarithmic
degree bound for the stability constants ... B \le C_B(1+\log g^{-2})" (140932-140933).
Verdict on C8: HOLDS (row 1058's range 140906-140934 covers these lines). Note: Definition 8.22 writes the
*full* normalisation constant with the same formula sum_{j<K} E^(j)_vac(T_m,T_m) that Lemma 8.22 (a) uses for
the constant *less* the Gaussian normalisers (next item). Inside Lemma 8.22 the lemma's own meaning governs:
"In this lemma E_m has the meaning fixed in hypothesis (a)" (141278-141279).

**2.2 Lemma 8.22 statement (CA-II 141276-141387).** Hypothesis (a) (141286-141313): "E_{m''} denotes
Ba{\l}aban's normalisation constant of the bare density on \mathbb{T}_{m''}, as in the normalisation of
\widetilde{Z}_{m''} in Definition 8.22, less the Gaussian normalisers of the K steps, the Gaussian normaliser
of step j being the logarithm of the Gaussian integral of step j at the trivial background; the Gaussian
normalisers of the two tori are compared by the determinant lemma" (141286-141291); then the split into
(vac,1) normalisation numbers of step j [B-CMP109 (1.7)] built from log g_j, log z_j and SU(2) constants times
lattice counts, (vac,2) = sum_z sum_{X∋z} E^(j+1)(X,1,z), (vac,3) = sum_X R^(j+1)(X,1), "evaluated at the
trivial configuration U=1". Hypothesis (b) (141315-141335): (2.29) of CMP 119 at U=1 makes the unrestricted
sum E^(j+1)(1,z;T) independent of z; |E^(j+1)(X,1,z)| <= E_0 e^(-kappa d_(j+1)(X)); |R^(j+1)(X,1)| <=
e^(-kappa d_(j+1)(X)); sum_{X∋z} e^(-kappa d/2) <= K_* (CMP 116 (1.26) at rate kappa/2); E_0, K_* depend on L
and p only. Hypothesis (c) (141336-141374): clause (0) of Theorem 3.1:thm-main, torus-independence lemma parts
(i), (iii)(b) and the lift lemma; "It is assumed ... that the running constants g_j and z_j of the steps j<K
do not depend on the torus" (141347-141349); non-wrapping = image of a set in a closed cube of side at most a
quarter of 2L^(min(m,m')); assumed bijection of non-wrapping X ∋ z with equal numbers E and R; and "every
X ... with X ∋ z and d_(j+1)(X) < 2L^(min(m,m')) L^(K-j-1)/(4M) - 2 is non-wrapping" (141369-141372).
Conclusion (141375-141386): delta_vac := abs(E_m/(2L^m)^4 - E_m'/(2L^m')^4) <= delta-bar_vac :=
2(E_0+1)K_* sum_{u>=0} L^(4u) exp[-(kappa/2)((1/2)L^11 L^u - 2)], depending only on L and p.
Verdicts: C1 HOLDS (the lemma is the account's two-torus statement for the counterterm, as an implication
from (a)-(c); but "the whole E_0^(j)" in C1 is too strong, see 2.4); C3 HOLDS; C4 HOLDS (quote exact);
C5 HOLDS (hypothesis (c) is as row 1058 says, plus the clause-(0) and torus-free-constants assumptions).

**2.3 The proof (CA-II 141389-141519).** (eq-2) nu_(j+1)(T) = (2L^m'')^4 L^(4(K-j-1)) (141394-141396);
(eq-3) L^(min(m,m')) >= L^11 M (141405-141407); first part exactly extensive (141413-141423); second part:
(eq-4) "D_j := 2L^{min(m,m')}L^{K-j-1}/(4M) - 2" (141441-141443) and (eq-5) abs(E^(j+1)(1,z;T_m) -
E^(j+1)(1,z;T_m')) <= 2E_0K_* e^(-kappa D_j/2) (141465-141468); third part: the same with E_0 -> 1 after
averaging over one M-cube (141471-141499); (eq-6) "delta_vac <= sum_{u=0}^{K-1} L^{4u} 2(E_0+1)K_*
exp[-(kappa/2)D_{K-1-u}]" (141504-141507); then "D_{K-1-u} >= (1/2)L^11 L^u - 2" (141510) gives delta-bar.
So row 1058's delta(l') is exactly (eq-6) with D_(K-1-u) = l' L^u/(4M) - 2, l' = 2L^(min(m,m')), extended to
all u >= 0. Verdict on C13 (i): HOLDS as a port. I re-derived each of the three parts from (a)-(c) and agree.

**2.4 Two passages row 1058 did not weigh (they bear on (G) and (G')).**
- CA-II 141424-141431 (proof, after the first part): "no number of the first part is a global,
  non-extensive normalisation number, such as a zero-mode factor or a residual-gauge factor per torus. The
  averaging constraints, the gauge fixing and the normalisation integrals of Ba{\l}aban's step are per block,
  so no such number occurs among the three parts of hypothesis (a); the one torus-wide number per level, the
  Gaussian normaliser of the step, is excluded by hypothesis (a). Were hypothesis (a) to admit even a bounded
  number of torus-wide numbers per level, they would contribute to delta_vac a term of order
  K(2L^{min(m,m')})^{-4}, which is not uniform in K at fixed m'."
  So the account itself calls the Gaussian normaliser of a step "torus-wide" and keeps it out of parts
  (vac,1)-(vac,3). Reading (G') of row 1058 (the normaliser already sits in (vac,1)-(vac,2)) is therefore
  *not* the account's reading of its own hypothesis (a); whether it is the right reading of Balaban is Step 6.
- CA-II 141531-141535 (remark): "The determinant lemma, which compares the Gaussian normalisers of the steps
  excluded by hypothesis (a), contributes a further constant, depending on L and p only (in particular not on
  K, g_0, g, m or m'), to the zero-source comparison of the two tori." The account promises a *constant*
  c(L,p), not a quantity that decreases with the side. Row 1058's input (G-tor) asks for more: c_G(l')
  decreasing to 0 in l'. The constant form suffices for Corollary SV1; the decreasing form is needed for
  Proposition RED and Corollary SV3-red (Step 5 of this check).
- Consequence for C1: the account localises the counterterm *less* the Gaussian normalisers; "the whole
  vacuum counterterm" (row 1058 L69, RESULT) is right only together with the determinant lemma, which the
  account names and does not state. Row 1058 says this itself in its Addendum (G) and in its RESULT ("OPEN:
  ... the Gaussian normalisers ..."). Correction of wording only: C1 HOLDS AFTER CORRECTION, "localisation of
  the vacuum counterterm less the Gaussian normalisers of the K steps".

**2.5 The consumer (CA-II 141703-141727, in the proof of 8.22:thm-volume-transfer).** "At zero source on
\mathbb{T}_m the normalisation reads Z_m(0)=e^{E_m}\widetilde{Z}_m(0)" (141703), then "Let delta_vac = ... be the
vacuum-density difference of Lemma 8.22" (141720-141722) and Q_* := exp[(B + delta-bar_vac) ...] (141578).
Z_m(0)=e^{E_m}Z~_m(0) holds for Definition 8.22's E_m (full constant); delta_vac is Lemma 8.22's (constant
less the Gaussian normalisers). Row 1058's bookkeeping remark (C7, last sentence; its 7.4 last bullet) HOLDS:
the theorem's exponent needs the Gaussian-normaliser comparison too, and its stated Q_* does not show the
"further constant" of the remark at 141531-141534. Internal to their text; nothing to post (rule 6).

Log: step 2 (CA-II part) written at 2026-11-16T15:21:57Z (date -u).
