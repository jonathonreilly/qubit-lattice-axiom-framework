Reviewer model: claude-opus-5-5

# WARD55 — Ward-insertion bounds for rotation invariance on the sphere route (W1, W3, trace clause) via the frozen/top representation

Worker: Opus 5.5 (claude-opus-5-5), worker role under REVIEW_BRIEF_55 rules. Written append-only.
Start (UTC): 2026-10-29 06:33 (from `date -u` at session start: Thu Oct 29 06:33:46 UTC 2026).

## 0. PRE-STATED (written before any derivation)

### 0.1 Targets
- **T1 (W1).** A conditional theorem: for every n ≥ 1 and every separated / coarse-image family of local
  observables (the determining family of ALL finite products required by CODEX_REVIEW_SPHERE item 4 and
  ASSEMBLY55 F4), the bulk Ward insertion of each rotation-breaking density — including contact terms and
  including the traceless S^(3,6′) insertion — is bounded, with every norm and quantifier explicit; for the
  S^(3,6′) insertion the bound must be o(log(ℓ₀/a)) as a → 0 (SPHERE2_55's product condition), not merely
  O(g²·log).
- **T2 (W3).** A conditional theorem bounding the observable-side source terms (the Lie derivative / rotation
  generator acting on the observables) in the same norms and quantifiers.
- **T3 (trace clause, LCS-a).** A conditional theorem for the single SRC-M clause SPHERE2_55 reduced LCS-a to
  (Proposition M: −div Ξ_v = 2N·C_F·Σ_p (div v/4)(c_p) s(U_p)), with the fluctuation part B^fl taken from the
  quantum source RG (SRC2_55's frozen/top representation), not tree level.
- **T4.** H_Euc on the sphere route stated as an implication, every input named, with its status after this work.

Each of T1–T3 is to be derived only from SRC2_55's representation (Theorem II / Corollary II, Lemma MB, the
singleton cancellation) and its named inputs (Rep_m^𝒞), (Flow-pos), plus anything else I name explicitly as
an added input. Anything I cannot derive is reported NOT-VERIFIED / open, with the missing piece named.

### 0.2 What would count as a refutation (first-class results)
- **R1.** An explicit rotation-breaking insertion (in particular S^(3,6′), or a contact term of it) whose
  separated insertion into some finite product is ≥ c·log(ℓ₀/a) for a fixed c > 0 along a → 0 under the
  representation's own hypotheses — i.e. the o(log) budget fails. (Also: a power-counting argument that the
  generic bound is forced to be O(g²·log) with a non-vanishing coefficient, given only the inputs named.)
- **R2.** A contact term (coincident insertion with an observable support) not controlled by the
  separated/coarse-image bound — e.g. a δ-function-like contribution of size O(1) not cancelled by the
  observable-side source term W3.
- **R3.** A sign/normalisation error in Proposition M (the trace identity) that changes which component
  needs the quantum source RG, or that makes the trace clause not reducible to one SRC-M clause.
- **R4.** A gap in SRC2_55's Theorem II / Corollary II / Lemma MB / singleton cancellation that the Ward
  bounds would need (I will check only the steps I use; a Codex review is running on SRC2_55).
- **R5.** A quantifier mismatch: the bound needed is uniform in a (or in the observable family), while the
  representation gives it only at fixed a, fixed n, or fixed support — so the implication to H_Euc does not go
  through as stated.

### 0.3 Discipline
No git. Write only `$L/WARD55.md` and `$L/checks/wd55_*`. Criteria file before any script. Exact rational
arithmetic only. Every cited symbol located by file + string. Appended in small sections.
