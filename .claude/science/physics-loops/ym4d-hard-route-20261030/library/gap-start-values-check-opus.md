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

**2.6 CA-I Theorem 4.38:thm-torus-independence (CA-I 58187-58411; proof from 58413).** Assumes the book's
statements (1)-(7) (58188-58217) and the level hypothesis (H_j) (58219-58268): site-free numbers
(g_i, Ř_i, beta_i) (a); steps 1..j-1 performed at every site (b); clauses (i), (ii)(a), (iii) at lower levels
(c+); (d) "the whole-lattice step j converges ... This step is the last logarithm in [CMP 119 (3.28)], taken
in the case in which the localization domains Omega_j and Lambda_j are both the whole lattice torus, pointed
as in [(3.37)-(3.42)] and expanded as in [(3.44)-(3.47)]" (58242-58246), with
abs(E^(j)(X;.,z)) <= E_0 e^(-kappa d_j(X)) on a polydisc (58262-58264). Clause (i) (58272-58285): for
non-wrapping X, "it depends neither on s nor on the lift. No operator, minimiser, partition function or scalar
of T_j(s) occurs in it" (58280-58281). Clause (ii)(a) ends "No rate of convergence is part of the statement"
(58322-58323). Clause (ii)(b) (58336-58343): beta_j "is a function of (g_0,...,g_(j-1)) and of the fixed
parameters ... alone. Hence x_j is site-free", and g_j, Ř_j, epsilon_j, delta_j, k_1(j) "are the same at
every site, and free of m and K'". Clause (iii)(b) (58363-58391): the R-terms of [CMP 119 (2.30)] on
non-wrapping X equal one family r^(j)(X^;.), independent of the site, the lift and the label.
Definition 4.38:def-non-wrapping (CA-I 57291-57330): non-wrapping = in a closed cube of side at most s_j/4 of
the torus's own side (a); "(f) Every wrapping X in D_j(s) satisfies d_j(X) > s_j/(4M) - 2" (eq-non-wrapping-a);
(g) the lift bijection with D_j^infinity.
Verdict on C2: HOLDS (quotes and anchors exact). Two remarks for later steps: (1) hypothesis (d) places in
E^(j) exactly the terms that Balaban's (3.37)-(3.47) produce; this is the textual hook of reading (G')
(Step 6). (2) Lemma 8.22's "non-wrapping (for the pair m,m')" uses the *smaller* torus's quarter side on
both tori, and its last clause (every X ∋ z with d_(j+1)(X) < D_j is non-wrapping for the pair) is assumed in
hypothesis (c), not quoted from 4.38 (f), which is stated for each torus's own side. The step from (f) to the
pair form is short (a connected union of M-cubes with tree length d has sup-diameter at most M(d+1), so
d < s'/(4M) - 2 puts it in a cube of side below s'/4), but the account does not write it; it is a hypothesis
of the lemma, as row 1058 says.

Log: step 2 (CA-I part) written at 2026-11-16T15:22:45Z (date -u).

## Step 3: do hypotheses (a)-(c) of CA-II Lemma 8.22 hold along the lane's trajectory?

The lane's trajectory is the account's (`gap-phys-seed.md` 1.1.1, L60-66; row 1058 Step 5): Wilson SU(2),
N = 2, (H1)-(H7) of Theorem 3.1:thm-main, g <= gamma_J, 0 < g_0 <= g_-(g), K = K(g_0, g) the first-passage
level, tori T_m of side 2L^m with m >= m_T(g_-(g)), g_0 -> 0 (so K -> infinity). For j < K the running
inverse coupling is still above the window (x_j > g^(-2) + B_sharp), so every integrated step is at
coupling g_j < g.

**(c), torus-independence: HOLDS along the trajectory as an implication from the account's package, with
one assumed clause.** CA-I Definition 4.38:def-admissible-sites (ii) (CA-I 57079-57083): "Let K=K(g_0,g) be
the first-passage level ..., and let m >= m_T(g_-(g)). The sites (m,K) of Theorem~0 lie in
\bigcap_{j\le K}\mathcal{S}_j." So both tori of every pair the lane uses are admissible at every level, and
Theorem 4.38 (i), (iii)(b) (Step 2.6) apply to both, given its statements (1)-(7) and (H_j). The
site-freeness of g_j is 4.38 (ii)(b) ("Hence x_j is site-free ... free of m and K'", CA-I 58339-58343).
The second running constant z_j is *not* in the site-free list of 4.38 (ii)(b) (g_j, Ř_j, epsilon_j, delta_j,
k_1(j)); Lemma 8.22 (c) assumes it ("It is assumed, as part of clause (0) and of its torus-independence
lemma, that the running constants g_j and z_j ... do not depend on the torus", CA-II 141347-141349). The
pair form of the wrapping bound (every X ∋ z with d_(j+1)(X) < D_j is non-wrapping for the *smaller*
side) is assumed in (c); it follows from the argument behind CA-I 4.38 (f) (a connected union of M-cubes of
tree length d has sup-diameter at most M(d+1) or so), which the account writes for each torus's own side
only. Neither point is a failure; both are assumed clauses the account does not derive at this place.

**(b), Balaban's format at zero source: HOLDS along the trajectory as a cited input.** The bounds
abs(E^(j+1)(X,1,z)) <= E_0 e^(-kappa d), abs(R^(j+1)(X,1)) <= e^(-kappa d) and the count K_* at rate
kappa/2 are Balaban's inductive bounds (CMP 119 (2.27), (2.29), (2.31)-(2.33); CMP 116 (1.26)), which the
account carries as (H_j)(d) of Theorem 4.38 with "E_0^natural > 0, a^natural > 0 and kappa >= 2 kappa(d)
independent of s, X and z" (CA-I 58262-58265). Every step j < K is at coupling below g <= gamma_J, inside
the small-coupling regime of those bounds. Uniformity of E_0, K_*, kappa in j and K is part of the cited
format. Status in the T0 chain: theirs-cited (Balaban), not rebuilt here.

**(a), the itemisation: NOT established along the trajectory; it is an itemisation hypothesis whose
content is exactly the (G)/(G') question.** The account calls it so: "Hypothesis (a) is a hypothesis on how
E_m is itemised" (CA-II 141529-141530). Two findings from the cited source (CMP 109 OCR,
`~/ym4d-papers/cmp109.txt` L630-670, journal pp. 260-261; page images read in Step 6):
- The account cites "[B-CMP109 (1.7)]" for the *normalisation numbers built from log g_j, log z_j and
  constants of SU(2)* of part (vac,1). In the OCR, (1.7) is the localized representation of the step-j
  term, E^(j)(g_(j-1), U_j) = sum over X in D_j of E^(j)(X, U_j) (L659-668: "We assume that it has the
  representation ... we can represent this term in the form (1.7)"). If the page image confirms this, the
  citation of part (vac,1) points at the wrong equation, and the meaning of z_j is not fixed by the cited
  source. The first part's argument (per-block numbers times lattice counts are exactly extensive) does not
  depend on which numbers they are, so this is a citation defect, not a failure of the lemma.
- CMP 109 p. 260 (OCR L652-668): "the factor Z^(j)(U_k) is given by the Gaussian integral normalizing the
  Gaussian measure for a fluctuation field in j-th step integration (1.4)", and "the expansion of the
  log Z^(j-1)(U_j) constructed in [16], implies, that we can represent this term in the form (1.7)". So in
  Balaban's effective action the step's Gaussian normaliser is a configuration-dependent term with a
  localized expansion of the same form as the E-terms. This is evidence for reading (G') of row 1058 and
  against the account's description of the normaliser as "the one torus-wide number per level"
  (CA-II 141428). Which of the two itemisations holds decides whether Lemma 8.22 covers the whole constant;
  Step 6 reads Balaban's (1.3)-(1.4) of CMP 109 and (3.33)-(3.38), p. 276, p. 279 of CMP 119 on page images.

Verdict for the row's claim "PROVED as an implication from (a)-(c), which were not checked here": the
implication HOLDS (Step 2.3). Along the lane's trajectory (b) and (c) hold as the account's package
supplies them (with the two assumed clauses above); (a) is the open point, and it is the same point as
(G)/(G').

Log: step 3 written at 2026-11-16T15:25:54Z (date -u).

## Step 4: Lemma WT, Corollary WT1, the floor remark, and the Gaussian-model test (by hand)

**Lemma WT (i)-(iv) (row 1058 L133-156): HOLDS as an implication from (a)-(c).**
- (i) is CA-II (eq-6) (141504-141507) with D_(K-1-u) = l' L^u/(4M) - 2, l' = 2L^(min(m,m')) (from (eq-4),
  141441-141443), and the finite sum over u <= K-1 extended to all u >= 0 (positive terms). Re-derived.
- (ii): V_m abs(E_m/V_m - E_m'/V_m') = abs(E_m - (V_m/V_m') E_m') and V_m/V_m' = L^(4(m-m')). Correct for m >= m'.
- (iii): with t = kappa l'/(8M), (kappa/2)(l' L^u/(4M) - 2) = t L^u - kappa, so term u = 2(E_0+1)K_* e^kappa
  L^(4u) e^(-t L^u). Ratio of terms u+1 to u: L^4 e^(-t L^u (L-1)) <= L^4 e^(-2t) for L >= 3, and
  2t >= 4 log L + 1 gives ratio <= e^(-1) < 1/2; the geometric sum is at most twice term 0, so
  delta(l') <= 4 e^kappa (E_0+1) K_* e^(-t). Correct (uses L >= 3, which the account's odd large L meets).
- (iv): delta is decreasing in l' and tends to 0 (dominated convergence over u against the floor value), so
  E_m/V_m is Cauchy at fixed (g_0, g, K); letting m'' -> infinity in (i) for the pair (m'', m) gives
  abs(E_m - e_inf V_m) <= V_m delta(2L^m). Correct; it needs Lemma 8.22 for every pair (m'', m) above the
  floor at the same K, which the lemma gives (both exponents only need m'' >= m_T(g_-(g))).
**Corollary WT1 (L158-161): HOLDS.** V_m delta(l') <= L^(4(m-m')) l'^4 * 4 e^kappa (E_0+1) K_* e^(-kappa l'/(8M))
once t >= 2 log L + 1/2; constants depend on (L, p) only, so the bound is uniform in K, g_0, g.
**Floor remark (C15, L173-175): HOLDS.** At l' >= 2L^11 M R: t >= kappa L^11 R/4 >= kappa L^11/4, so (iii)
applies when kappa >= (8 log L + 2)/L^11 = 6.09e-5 at L = 3 (8 log 3 + 2 = 10.79; 3^11 = 177147).

**Identity (T1) (L104-119): HOLDS.** With 2 cosh theta = mu^2 + 2 (I write mu for the model's mass, to keep
m for the torus exponent): (e^theta - w)(e^theta - w^-1) e^-theta = 2 cosh theta - w - w^-1; the n-th roots
are closed under inversion and prod_k (x - w_k) = x^n - 1, so det T_n = e^(-n theta)(e^(n theta) - 1)^2 and
log det T_n = n theta + 2 log(1 - e^(-n theta)). n = 1 gives mu^2, n = 2 gives mu^2(mu^2 + 4). Readings (a)-(d)
are correct: abs(log(1 - x)) <= x/(1 - x) gives (b); 1 - e^(-n theta) ~ n theta gives (c) and (d).

**Test: the tail bound of Lemma 8.22's mechanism on the Gaussian model (by hand). PASSES.** Write
T_n = 2cosh(theta)(1 - P/(2 cosh theta)), P = S + S^-1. Then (1/n) log det T_n = log(2 cosh theta)
- sum_{r>=1} (1/r)(2 cosh theta)^(-r) N_n(r), with N_n(r) the number of sign strings in {+1,-1}^r whose sum
lies in nZ. Split N_n(r) = C(r, r/2) + W_n(r): the first count (closed walks of Z, the "non-wrapping
terms") is the same on every cycle, which is hypothesis (c) for this model; W_n(r) counts walks of
displacement in nZ \ {0} (the "wrapping terms"), vanishes for r < n and is at most 2^r. Hence, with
kappa_G := log cosh theta (the decay rate of the term of length r, (1/r)(cosh theta)^(-r)),
abs((1/n) log det T_n - theta) <= sum_{r>=n} (1/r)(cosh theta)^(-r) <= e^(-kappa_G n) / (n (1 - e^(-kappa_G))),
using that the n-independent part equals theta (the n -> infinity limit of (T1)/n). So two cycles n >= n'
have densities within 2 e^(-kappa_G n')/(n'(1 - e^(-kappa_G))): the Lemma 8.22 form, a summable wrapping tail
at the decay rate of the terms. Exact value from (T1): 2 abs(log(1 - e^(-n theta)))/n ~ 2 e^(-n theta)/n.
Since kappa_G < theta, the bound is valid and loose in the rate, as a walk count must be. At theta = 1,
n = 1: bound 1/(cosh 1 - 1) = 1.84 against exact 2 abs(log(1 - e^-1)) = 0.92. As theta -> 0 the bound
degenerates (kappa_G ~ theta^2/2, prefactor ~ 2/theta^2), matching the exact w(n) -> -infinity of (T1)(c):
the mechanism needs a decay rate fixed against the side, which in the account is the fixed kappa of each
step (unit decay in that step's lattice) and the floor l' >= 2 L^11 M R. Consistent with row 1058 Step 3.
What the test does not show: anything about the four-dimensional step normaliser; it only confirms the
shape of (SV2) and that exact torus independence is false.

Log: step 4 written at 2026-11-16T15:27:43Z (date -u).

## Step 5: (5.1), (TL), Proposition RED, Corollaries SV1 and SV3-red, the (SV3) verdict, the controls

**(5.1) F_m = E_m + G_m + log Z~_m(0) (row 1058 L184): HOLDS.** Definition 8.22 (eq-4) gives
Z~_m(0) = e^(-E_m^Def) Z_m(0) with E_m^Def the full constant (140918-140922); hypothesis (a) of Lemma 8.22
makes the lemma's E_m equal to E_m^Def less G_m (141286-141291). So F_m = E_m^Def + log Z~_m(0)
= E_m + G_m + log Z~_m(0). The sign convention of G_m does not matter below (only abs values are used).

**(TL) (L195-199): HOLDS as a recalled input, with one scope remark.** Along the account's family the
monotone part is CA-II Lemma 8.22:lem-trace-subadditivity: "0 <= Z_{n^(mu,k)}(W) <= Z_n(W)^k" for tori with
every n_mu even and *every integer k >= 1* (141024-141029; the inequality is 141028); at W = 0 and k = L^(m-m') (odd) in each
direction it gives F_m/V_m <= F_m'/V_m', so f_K = lim_m F_m/V_m = inf_m F_m/V_m exists at fixed K
(F_m/V_m is bounded below at fixed K). Identifying f_K L^(-4K) with the lane's f(beta) = inf over *all* tori
uses the standard thermodynamic limit (Ruelle) and F(n)/n^4 >= f_infinity for every torus; row 1058 recalls
this and does not prove it, and the account's lemma covers only even sides. It is an input of the lane's
definition of D (row 1028), not a new claim of row 1058.

**Proposition RED (L201-209): HOLDS as an implication from (WT), (G-tor), (STAB), (TL).** Dividing (5.1) by V_m:
F_m/V_m -> f_K by (TL), E_m/V_m -> e_inf by WT (iv), G_m/V_m -> g_inf by (G-tor) (Cauchy, since c_G decreases
to 0), so z_m -> z_inf = f_K - e_inf - g_inf. Then D(T_m) - D~(m) = (E_m - e_inf V_m) + (G_m - g_inf V_m), and
the two brackets are at most V_m delta(l) and V_m c_G(l) (WT (iv); the limit m'' -> infinity in (G-tor)).
Re-derived line by line; correct.
Scope remark: (G-tor) is the *decreasing* form. The account's remark (CA-II 141531-141535) promises only a
constant c(L, p) for the Gaussian-normaliser comparison (Step 2.4). Row 987's Corollary B (conditional on (ID)
and its imports) gives c_det proportional to L^(-5 min(m,m')) (`gap-det-fable.md` RESULT, L556), which is the
decreasing form; then V_m c_G(l) ~ l^4 l^(-5) -> 0, so the polynomial rate is enough for RED and SV3-red.

**Corollary SV1 (L211-219): HOLDS as an implication from the same inputs.** z_m <= E_+^sharp and z_m >= -C_low
by (STAB), so z_inf >= -C_low and D~(m) <= B V_m; add RED; D >= 0 by (TL). The final form uses
B <= C_B(1 + log g^(-2)) (140932-140933), delta(l) <= delta-bar_vac at the floor, c_G(l) <= c_G. Uniform in K
and g_0. For SV1 alone the account's constant form of the determinant comparison would suffice (it only needs
abs(G_m - g_inf V_m) <= c V_m), but the existence of g_inf still needs G_m/V_m to converge, which the constant
form does not give. So SV1 also rests on (G-tor) in a form that makes G_m/V_m converge (or on (G')).
Row 1058 states the inputs; its claim is correct as stated.

**Corollary SV3-red (L221-226): HOLDS.** Apply RED at m and at m' and use V_m >= V_m', l >= l' and the
monotony of delta and c_G: the error is at most V_m(delta(l) + c_G(l)) + V_m'(delta(l') + c_G(l'))
<= 2 V_m (delta(l') + c_G(l')).

**(SV3) OPEN; the reasons given (L228-256): HOLD.** Quotes checked: CA-II 8.18:lem-horizon-cases (statement
143297-143338): (i) "Suppose K+m <= K_*-1 ... N_T^dagger <= 2L^{c_gap}" with
(N^dagger)^4 <= 16 L^(4c_gap) L^(4m_T(g^dagger)) = 16 L^(4c_gap+44) M^4 R(g^dagger)^4 (eq-horizon-cases-a);
(ii) "m <= m_V(g) ==> K+m <= K_*-1" (eq-horizon-cases-b); (iii) beyond the horizon,
B(g^dagger)(N^dagger)^4 <= V-bar(g,m) (eq-horizon-cases-c). Row 1058's reading is right: the prolonged run
still ends on a residual torus of at least the floor size (2 L^(m_T(g^dagger)) per side, so at least
16 L^44 M^4 sites), and the account bounds the residual integral only by B times that volume. Wording: the
row writes "the error B(g^dagger)(N^dagger)^4 of its (8.18:eq-horizon-cases-c)"; (eq-c) is stated in part
(iii), beyond the horizon; in the first volume range the same product is bounded through (eq-a). No effect.
The grep claim (L246-251) HOLDS and extends: over the full text of CA-I/II/III (not only the index) every
"Casimir" is a group Casimir (CA-I 3885, 164664; CA-II 26800, 27495, 27504, 60532; CA-III 76764, 76882,
95233); "zero mode" occurs once, for the free massless scalar (CA-III 106149); "zero-mode factor" once
(CA-II 141425); "finite-size"/"finite size" never. No statement of the account bounds the Casimir part of
log Z~_m(0). The "exact missing statement" (log Z~_m(0) = z V_m + c_m with c_(m+1) - c_m -> 0 on the first
volume range) is a correct name for what (SV3) needs, given RED.

**U(1) control (L260-266).** (SV2) ARGUED: correct as stated (the proof of Lemma 8.22 reads only (a)-(c); the
group enters through E_0, K_*, kappa). (SV3) "D^+(bL) = D^+(L)": HOLDS AFTER CORRECTION (scope). The shift
D_j(bL/a_j) = D_(j+1)(L/a_(j+1)) is right, so the identity holds in [0, infinity]; "the control gives 0" needs
D^+(L) < infinity, which row 1058 does not show for compact U(1). Plausibility (GUIDE, not proved): for a
compact massless *scalar* in d = 4 the zero mode makes D(n; beta) grow like (d/2 - 1) log n = log n at fixed
beta, so its D^+ would be infinite; for the Maxwell field on the 4-torus the zero-mode and determinant
scalings cancel (ghost det' +2, gauge det' -4, flat connections +4, constant gauge volume -2, in units of
log of the side), so D^+ finite is plausible for compact U(1) in the Coulomb phase. Corrected text: "for
constant coupling and spacings a_0 b^(-j), D^+(bL) = D^+(L) in [0, infinity]; the control gives 0 where D^+
is finite."

**Kill tests (L268-281): HOLD as appraisals.** The four descriptions match `parts/gap.md` L123-135 (PT: product
with a massless factor; D2/SUB: supremum over tilts; SHEET: uniform over coupling fields; NP: no-seed model,
no induction on the history of D). None of SV1, SV2, SV3-red is a class statement, an induction on the
history of D, a supremum over tilts, or a form uniform over coupling fields.
**Five-dimensional count (L283-290): HOLDS as GUIDE.** Tree gauge: 3(d n^d - (n^d - 1)) = 3(d-1)n^d + 3
coordinates; commuting d-tuples in SU(2) have dimension d + 2 (a maximal torus, 2 parameters, and d
angles); so D = ((d-1)/2) log beta + O(1) at fixed n, (3/2) log beta at d = 4 (Lemma FV's coefficient).
The d = 5 sign (+2 log 2) and the d = 4 sign (negative, tending to 0) follow from beta ~ L^(d-4)/g^2 and
asymptotic freedom. Nothing is claimed for the trajectory; correct.

Log: step 5 written at 2026-11-16T15:31:39Z (date -u).
