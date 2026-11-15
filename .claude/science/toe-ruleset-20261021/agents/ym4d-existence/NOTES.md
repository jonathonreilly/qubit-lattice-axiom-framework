# Literature notes: YM4D existence lane (session 1, 2026-10-27)

**Provenance.** arXiv PDFs fetched from arxiv.org/pdf/<id> into the session scratchpad (`exlit_dl/`), text extracted
with pypdf (`pdfenv/bin/python -I`, script in `exlit_scripts/`), read in the extracted text. The MRS preprint is the
authors' own TeX source on the mp_arc preprint archive (web.ma.utexas.edu/mp_arc/e/92-38.tex). No paywall, sign-in or
bot check was crossed. Quotes are short and exact; everything else is paraphrase.

**Tags.** [read]: passage read in the primary text. [read-skim]: located and statement read, not the proof.
[read-abs]: abstract only. [not-read]: bibliographic only. [via P]: read by the sister lane (P/literature/NOTES.md),
not re-read here.

---

## 1. Balaban's programme (all via P)
- **CMP 109 (1987) 249-301** [via P, read in full there]: small-field effective actions, Theorems 1-3, (0.22)-(0.31),
  (1.18). Used for H-Bal-1 (Theorem 2, (0.31); proof deferred by Balaban) and the small-field half of H-Bal-3. P's
  transcription notes: (1.18) carries no positive power of the coupling; the coarse regularity condition
  |∂V - 1| < ε_0 is an alternative domain definition (p.259); the inductive step is completed in CMP 116.
- **CMP 116, 119, 122 I-II, 102** [not-read; P has Crossref/OSTI abstracts]: localisation/cluster expansion, convergent
  expansions, the large-field R-operation, the background field. H-Bal-2 and the large-field half of H-Bal-3 rest on
  these. **Their exact statements are the main unverified inputs of this lane.**
- **Dimock I-III, QED3 series** [via P]: scalar/abelian templates; Dimock III: "The analysis can be adapted to treat
  correlation functions as well" (p.33) — correlations are not proven there.

## 2. J. Magnen, V. Rivasseau, R. Sénéor, "Construction of YM4 with an infrared cutoff", CMP 155 (1993) 325-383; preprint mp_arc 92-38 (Feb 1992) [read: abstract, introduction l.16-200, statement of the Theorem in §VIII]
- Abstract: Schwinger functions of pure SU(2) YM4 "(in the trivial topological sector) with a fixed infrared cutoff but
  no ultraviolet cutoff, in a regularized axial gauge"; validity checked by Slavnov identities holding
  non-perturbatively.
- Their description of Balaban's result (intro): the effective action on the unit lattice "remains bounded"; from this
  the UV limit for gauge-invariant observables such as "smoothed Wilson loops" should follow "at least through a
  compactness argument using a subsequence of approximations; but the limit is not necessarily unique". This is
  exactly the soft layer X-ALG/X-MONTEL of EXISTENCE.md.
- They also say Balaban's programme does not construct the gauge-fixed Schwinger functions, and they "do not claim to
  provide here the proofs of convergence of our expansion in all detail".
- OS axioms: not studied (IR cutoff kept). They think OS positivity could be obtained by starting from a lattice cutoff
  (lattice RP for lattice hyperplanes) and slicing below the lattice scale. Not done.
- Theorem (§VIII): the UV limit of the Schwinger functions (moments of their measure (II.77)) exists and satisfies the
  Slavnov identities. These are **gauge-fixed** objects; gauge-invariant observables are not constructed there.
- Use here: framing of (a) and of the observable question. IMPORTED-NOT-YET-REVERIFIED for any technical content (none
  used).

## 3. S. Chatterjee, "Yang-Mills for probabilists", arXiv:1803.01950 [read: §5 pp.9-10, §6 pp.10-13]
- Problem 5.2 (continuum limit of raw rectangular Wilson loops): log⟨W⟩ = -c(R + T) - dRT + o(1) with c = c(β) → ∞, i.e.
  a divergent perimeter subtraction. He adds that it is not clear the renormalisation term is needed. Used in X-RAW.
- §6 on phase-cell renormalisation: the goal is convergence of the macroscopic effective theory; "Usually, convergence
  is hard to prove, so one settles for subsequential convergence by a compactness argument", and he calls the existence
  of a convergent subsequence ultraviolet stability. Consistent with EXISTENCE.md §0.
- No construction of a continuum limit with non-trivial Wilson loops is known in any dimension above two (as of that
  survey).
- Heat-flow regularisation (Charalambous-Gross, Lüscher) is mentioned as a new route in 3D.

## 4. Gradient flow
- **M. Lüscher, "Properties and uses of the Wilson flow in lattice QCD", arXiv:1006.4518, JHEP 08 (2010) 071**
  [read: abstract, §1, §4.1].
  - Lattice flow (1.4): V̇_t = -g_0²{∂_{x,μ}S_w(V_t)}V_t, V_0 = U. On a finite lattice existence, uniqueness and
    smoothness for all t are rigorously guaranteed (citing his earlier trivializing-maps paper); S_w decreases.
  - Abstract: the field at positive flow time "is a smooth renormalized field" (supported by theory and numerics, not
    a theorem).
  - §4.1: on a finite lattice U → V_{t_0} is a diffeomorphism of field space. Used for X-FLOW.
- **M. Lüscher, P. Weisz, "Perturbative analysis of the gradient flow in non-abelian gauge theories", arXiv:1101.0963,
  JHEP 02 (2011) 051** [read: abstract and §1].
  - To all orders in perturbation theory, correlation functions of the flowed field at positive flow time are finite
    once the 4D theory is renormalised in the usual way. Perturbative only. Used in X-SRC-GAP (plausibility of
    H-src-flow).
- **R. Narayanan, H. Neuberger, "Infinite N phase transitions in continuum Wilson loop operators", arXiv:hep-th/0601210,
  JHEP 03 (2006) 064** [read: abstract, contents].
  - Smoothed lattice Wilson loops have a finite non-trivial continuum limit — checked numerically, not proven; they stay
    unitary matrices. Numerical support for O^flow being the right observable class.
- **S. Cao, S. Chatterjee, "A state space for 3D Euclidean Yang-Mills theories", arXiv:2111.12813, CMP 405 (2024) art. 3**
  [read: abstract, §1.1-1.7 to Theorem 1.6 and Conjecture 1.8].
  - Theorem 1.6 (3D): if S_YM(X_n(t)) is tight for every t > 0, a subsequence of the laws converges on their
    distributional-gauge-orbit space. Conjecture 1.8: the tightness holds for suitable approximations.
  - It is 3D. In 4D the YM action is scale invariant, Uhlenbeck compactness is critical, and the analogue is not
    available as stated [ARGUED, not checked]. EXISTENCE.md uses only the lattice-flowed analogue (X-FLOW), whose
    compactness is trivial because flowed lattice loops are bounded.

## 5. Reflection positivity
- **K. Osterwalder, E. Seiler, Ann. Phys. 110 (1978) 440** [not-read; not open]. The lattice RP proof is re-derived in
  P, L9a/L9a-m (check c4), and re-read here: X-LRP, IMPORTED-AND-REVERIFIED.
- **E. Seiler, Gauge theories as a problem of constructive QFT and statistical mechanics, LNP 159 (1982)** [not-read;
  not open]. Chatterjee (§5) says his Wilson-loop approach to the continuum limit follows Seiler's Chapter 8.

## 6. Clay problem description (Jaffe-Witten) [via P, read pp.11-13 there]
- Balaban's 4D extension includes asymptotic freedom and large-field estimates; the citation given is CMP 109 alone.
  Not re-read here.

## 7. Not found / not read
- No open-access statement of Balaban's CMP 122 large-field theorem or of the exact form of his normalised Z bound.
- No open-access paper constructing gauge-invariant Schwinger functions of 4D YM in any volume.
- The OpenAI announcement (2026-10-26) is still known only through secondary summaries (P/../openai-balaban-review);
  nothing about its OS-axiom content could be read.

---

## Session 2 (2026-10-27)
No new primary sources were read. Used, via P (P/literature/NOTES.md, not re-read in the primary text here):
- Dimock II (arXiv:1212.5562) large-field split, thresholds p_k = (-log λ_k)^p and the factor e^{-O(1)p_0²} per cube
  [via P, P read-skim]: the template for H-Bal-3T (EXISTENCE §10.1). Its YM transposition is [unverified].
- Dimock III (arXiv:1304.0705) p.33, correlation functions "can be adapted", not proven [via P]: cited for W-AF2/H-corr.
- Balaban CMP 109 Theorem 2 / (0.31) and (2.13), and the deferral of the flow proof [via P §9.4-9.5]: cited for W-AF1 and
  for why the small-field two-grid step needs the fluctuation covariance (CMP 99 [not-read]).
- Balaban CMP 102 Proposition 9, (190) (exponential decay of δH/δB) [via P §9.7, P read only CMP 109's citation of it]:
  cited as the expected source of volume-uniform one-link increments in H-Bal-3L. [not-read]

## Session 3 (2026-10-27): X-WIL prior-art search (open access only; no barrier crossed)
- Chatterjee, "The leading term of the Yang-Mills free energy", arXiv:1602.01222 (JFA 2016) [read-skim: abstract page
  and the ar5iv HTML through a page summariser, §1-16; not read line by line]. Theorem 2.1: leading term of the U(N)
  lattice free energy on boxes, n → ∞, g_0 → 0 jointly. Theorem 8.1 (per the summary): action tail bound
  P(βS > Cn^d log β + t) ≤ e^{-t}, β ≥ 2. No mean-plaquette lower bound found.
- Brennecke, arXiv:2511.07297 [read-abs]: explicit characterisation of Chatterjee's K_d.
- Kazakov-Zheng arXiv:2203.11360, Li-Zhou arXiv:2404.17071, Guo et al. arXiv:2502.14421 [read-abs via search
  summaries]: numerical rigorous bootstrap bounds on the plaquette; no analytic c/β lower bound.
- Seiler (1982 lecture notes), chessboard/Peierls literature for lattice gauge theory [not-read].

## Session 4 (2026-10-27): chessboard estimates, log-concavity (open access only; no barrier crossed)
- Biskup, "Reflection positivity and phase transitions in lattice spin models", arXiv:math-ph/0610025 (Lecture Notes in
  Math. 1970, 2009) [read-abs: the arXiv abstract page only; the PDF was downloaded (open access) but its text could not
  be extracted in this environment, so no theorem in it was read]. Cited as the standard modern account of chessboard
  estimates; the proof of Lemma CBE in EXISTENCE §13.4 is written out independently.
- Fröhlich, Israel, Lieb, Simon, CMP 62 (1978) 1-34 (chessboard estimates) [not-read]; Shlosman, Russian Math. Surveys
  41 (1986) [not-read]. Cited for provenance of Lemma CBE only.
- Caffarelli contraction theorem / Hargé's convex-correlation inequality for log-concave perturbations of Gaussians
  [not-read; cited as STANDARD in §13.6, used by no counted item].
- Layer-1 sources used (read in P this session, by offset): RLARGE.md §0-§13 (RLF, Proposition CL, Lemma RS, (I_k),
  (PLD), RLF-step), LINEAR_PACKAGE.md §1-§11 (D4-norm (2) only as quoted in RLARGE §5-§6; PROOF.md L5 not re-read; A1, N2-E/N2-lin/N2-exp, Prop. 6.2-6.4, Prop. 7.1 = A2).
