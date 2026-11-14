# LSC — value and novelty check

Codex; model variant and effort not independently exposed; checkout `3c3467adc33cbe363b134700c76625b62c29a179`; research text, not an audit. No status is granted. Nothing is posted.

**Verdicts per claim:** CORRECT-NO-ADVANCE for the ported stability and per-ball deductions. ADVANCE for the normalization repair and the bounded completion of the Chapter 6 assembly, at the stated inputs' standing. Most of the mathematics is already theirs. The substantive correction comes from the completed `gates/nrm-check.md`, not a second discovery in LSC. This value judgment does not reverse the round-2 proof check.

## Scope and source key

`library/prior/lsc-value.md` is absent. The registry's LSC row belongs to `lsc` and records the completed conditional proof. FINISH row 318 records the completed NRM correction; row 352 owns its proposed LSC write-up. This report does not restart either task or take over later-use repairs.

`I`, `II`, `III` denote the three complete-account TeX files; `SA` denotes `YM4_sketch_500.tex`, in `/Users/jonreilly/ym4d-lead/sa`. Their SHA-256 hashes match all four pinned-source records in `library/mu.md:17–20`, attributed to `31a47c543775`. References below are source lines. Credit Sussman and Alpoge, with Claude and Codex as authors of their text, and Balaban for the imported construction.

The outline index, neighbouring rows and obligations guided bounded source reads. Its status words are not proof evidence. Balaban's papers were not independently inspected; only this checkout's literature record and the account's quotations were available. The checkout lacks `docs/ai_methodology/SCIENCE_WORKFLOW.md`. No numerical calculation or machine verification discharges any step here.

## 1. Their label and exactly what is missing

At `6.3:lem-last-scale-constants`, II:63365–63367 says: “The statement of this lemma is not written out here; parts of its proof are printed below.” The missing statement is real. It does **not** mean the proof is wholly absent.

The source prints part (b), including lattice matching and the constant bound, at II:63369–63526; part (c) at 63568–63689; part (d) at 63691–63798; and part (e) at 63800–63833. Part (a), establishing the bounded offset, is referred to but not printed there. The hypotheses called (I1)–(I3) at II:63700–63702 are likewise not supplied as a labelled statement.

The local obligation is to match the two stopping indices and carry genuinely uniform last-scale constants into the per-ball estimate. A coherent normalization is essential. Chapter 1 defines the bare density without a vacuum scalar (I:477–481,924–933), whereas the energy used in 4.33(h4)(a) is initialized with that scalar (I:157039–157041;159153–159160). The missing factor affects the lower bound, not merely notation.

The source's status declarations conflict: III:110894–110899 calls last-scale uniformity incomplete, while II:64603 reports no incomplete chapter statements. Neither declaration overrides the arguments actually printed.

## 2. Exact match of LSC and its inputs to the need

**Match: a sufficient conditional reconstruction for Chapter 6, with an explicit correction to the density convention.** There is no complete original statement against which literal equality can be asserted.

With the account's constants fixed first, LSC fixes $g$, then $m_J=m^J_{\mathbb T}(g)$. It proves

\[
a=K_J-K\in\mathcal A,\qquad b=m_J-a\in\mathcal B(g)\subset[0,m_J],
\qquad K'=K-b,\qquad N=2L^{m_1+b}.
\]

Here $m_1$ is the physical torus exponent; $m_J$ counts omitted steps. Uniformity does not mean varying $m_J$ independently. Nor does LSC prove that $b$ is constant across bare couplings.

For $K_J\ge m_J$, its substantive bounds are

\[
\widehat Z=e^{-E_{\rm vac}}Z_{\rm bare},\qquad
\widetilde Z=e^{-\mathcal E}\widehat Z,\qquad
\widehat Z(0)\ge e^{-C^*_{\rm low}N^4},\qquad
|\widetilde Z(w)|\le e^{C^*_+N^4},\qquad C^*_++C^*_{\rm low}\le E_*.
\]

These constants are uniform in cutoff, bare coupling, physical torus size and placement, at fixed admitted data. The vacuum number itself need not be bounded. This is the convention already explicit at II:140916–140926 and SA:23405–23415,23515–23527.

The required inputs remain substantial: clause (0); the coefficient identification at II:63072–63081; positive source-free representation and mass preservation; the vacuum theorem's hypotheses; Balaban's real-background bound and the characteristic-function admission; and the correlation theorem's eight upper-bound hypotheses after removing its assumed floor. The latter are listed at II:59645–59680. LSC also retains the identification of the zero-source Chapter 5 energies with Chapter 4's energies. It does not derive that identity from equality of the numerical flow.

LSC's smaller bond radius respects both $a_1$ and the small-field threshold. The relevant supplier is I:154052–154058,155039–155096. Its explicit constants (17), (21)–(23) avoid inferring boundedness from an unspecified function of a bounded coupling. For $K_J<m_J$, part (d) gives a local bounded-observable estimate, not a partition-function floor. Section 6.4 supplies a finite-torus completion to the original floor of clause (iii-b), I:2610–2620.

The four original consumers match this corrected scope. II:63531–63565 reads the last-coupling dependence; II:63907–63946 reads the uniform sum and finite rescaling maximum; II:64157–64283 divides bounds on the same torus before taking a cell root; II:68362–68368 lists this input to the limit argument. In particular, the per-ball proof also names a bound for $C_{\rm low}$ separately. LSC supplies it separately in the normalized convention.

**No all-account replacement follows.** `gates/lsc-uses-check.md`, U6–U9, requires conversion from last-lattice volume to unit-lattice volume by $L^{4b}$. Cross-torus comparisons retain a vacuum-density difference, visibly present at II:141688–141725 and in hypothesis (e) at III:72762–72765. LSC does not bound that difference. The later report's Lemma M, face estimate and short-run transfer repair are additional, then-unchecked arguments. They are not part of the frozen LSC proof.

## 3. Already theirs?

**Most of the construction and deductions are theirs; the exact assembled note is not wholly duplicated.** Searches covered all four source files for the label, last-scale terminology, stopping-index expressions, the finite rescaling formulas, floor constants and stability-exponent label. These are the decisive matches:

| LSC material | Existing account or outline argument |
|---|---|
| Least admissible $m_J$, divergence and one-sided floors | II:62887–62983,63248–63364 prove these. |
| Lattice matching, transported norm, cumulant equality, bounded terminal coupling | II:63369–63507 proves these, assuming part (a). |
| Uniform $E_*$ at fixed $m_J(g)$ | II:63509–63526 already proves this from its explicitly stated correlation-theorem constant clause; II:63529–63565 explains that dependence. |
| Finite rescaling maximum, short-run local count, constant-offset subsequence | II:63568–63833 supplies the actual proofs, including the local rather than total-volume count. |
| Normalized vacuum remainder and density constants | I:159321–159336,159412–159443,159511–159593 proves the relevant implications. LSC ports them. |
| Small-field Haar integral and logarithmic floor | II:109859–110014, especially 109918–109975, gives the minimizing-background calculation under its stated inputs. SA:19791–19807 and 23481–23539 gives the normalized floor and Haar calculation. |
| Sourced upper bound and division by the floor | II:59645–59835 gives the conditional history calculation. SA:23385–23444 gives its normalized abstract form. |

The comparison with 8.8 is not literal identity: that lemma assumes $x_{K'}\le2X$ and reserve-weight estimates. LSC uses the whole interval $(X,x^*]$, a conservative radius and the ordinary sourced majorant. Nevertheless, the floor's mechanism is already theirs. Even choosing a common admissible radius on a coupling window has a detailed precedent at I:154866–154942,154947–154969.

SA:23570–23576 already explains how a supplied terminal window makes logarithmic constants cutoff-uniform, while expressly leaving admissibility of the run upstream. The outline's Theorems 4.1–4.2 at SA:22502–22550 do not supply the missing construction. Likewise, III:60586–60598 imports the floor for a hatted run, and III:72757–72765 assumes the lower bound and vacuum comparison. These are uses, not alternative proofs of the complete LSC reconstruction.

What remains additional is narrow: the short offset argument in LSC §4, explicit assembly of the two exponents on one window, the normalization reconciliation, and the finite-torus completion in §6.4. The normalization reconciliation's missing-term identity and corrected floor are already repository work in `gates/nrm-check.md` §5, equations (18)–(21). They must not be counted again as a distinct LSC discovery. I found no separate full proof of the exact reconstructed (a)–(e) in the sources inspected; that is different from finding a substantial new stability theorem.

## 4. Check record

Codex wrote LSC; its exact model variant is unrecorded. A fresh Claude session checked round 1 and rejected the bare-mass identification, while accepting the offset, matching, local count and subsequence arguments, and the per-ball deductions conditional on a valid exponent (`gates/lsc-gate.md`).

The independent Codex normalization check identified the missing vacuum term and corrected the referee's stronger claim that no normalization could work (`gates/nrm-check.md`). A fresh Claude session then checked the round-2 changes at `5129d8d4e`, retaining round 1's accepted parts: “First failing step: none” (`gates/lsc2-gate.md`). Its acceptance is explicitly conditional on the retained construction inputs and common energy identification.

The later-use report names Claude Opus 5.5, max effort, at `620e5d82f`. Its closing paragraph distinguishes checked uses from its own new, not-yet-independently-checked Lemma M and repairs. The use inventory is a direct-use inventory, not a full transitive closure. This report compares source content and value; it does not claim a new complete line-by-line referee check of every upstream hypothesis.

## 5. Value to the authors and decision

The target is on their main-theorem path. Its constants feed clause (iii-b), then the subsequential continuum argument; III:110894–110905 and II:68362–68368 explicitly say so. A consistent last-scale assembly is therefore useful.

But the note does not close a new key analytic gap at the level an outward gap-closing claim would suggest. Their Chapter 6 already proves the conditional constant transport. Their Chapter 4, Chapter 8 and outline supply the principal floor mechanism. The source-free construction, sourced majorants, real-background input and outstanding preparatory window statement remain inputs; the latter is explicit at II:2810–2812. No unconditional per-ball theorem, main theorem, factorial growth, clustering or rotation result follows from this contribution alone.

The contribution worth offering is the correction of the inconsistent bare-density application, together with its completed Chapter 6 use. It is already the completed NRM finding locally; that does not make the correction already present in the authors' pinned text. LSC supplies the explicit common constants and the original-floor completion needed to show that the repair preserves this part of their route. Thus it closes the named last-scale obligation conditionally, including a real normalization defect. It does not close their principal upstream analytic gaps. The offset and finite-maximum additions alone would not justify an outward contribution.

This is a content recommendation against the pinned sources. Current upstream revisions, issues, PRs and previous outward posts were not checked: the task restricts searches to disk. The normal pre-post comparison and approval of exact text remain outside this report.

**SEND, narrowly: the normalization correction with the conditional completion of `6.3:lem-last-scale-constants`.** The outward version must state first that Chapter 1's bare density is incompatible with the vacuum-energy substitution in 4.33(h4)(a), and that the repair uses the account's existing vacuum-normalized convention. Then state the reconstructed lemma and all retained inputs. Credit the printed proofs of (b)–(e), the floor calculation and NRM; isolate the actual additions. Restrict the claimed application to the checked Chapter 6 consumers and the original torus floor. Do not advertise a new stability theorem, an unconditional main-theorem gap closure, or coverage of every later use.
