# Block 14 V1-V5 Grounding

## V1 — Soundness (does it prove what it says?)

Claim: every admissible bare-action contact 4-fermion operator
coefficient on Q_L is zero, by direct enumeration of the bare action's
operator content from `MINIMAL_AXIOMS_2026-05-03:32-43`. The action
specification lists exactly two operators:

1. Wilson plaquette (gauge-only, no fermion factor).
2. Staggered Dirac kinetic (fermion bilinear with one gauge-link insertion).

No four-fermion contact operator is present. By the standard rule that
bare-Lagrangian coefficients are read directly off the operator
decomposition, the contact-4-fermion coefficient is identically zero
for every admissible (Clifford × Clifford × color × iso) choice on Q_L.

The D9 composite-Higgs structural fact rules out the "integrate out a
fundamental scalar to produce a contact" loophole: D9 forbids any
independent fundamental scalar field, so the only scalar bilinear is
the composite `phi = (1/N_c) psibar psi`, which is itself made of
fermions and cannot be integrated out as an external field.

With the contact coefficient identically zero on the scalar-singlet
channel, the tree-level decomposition `Γ_tree = Γ_OGE + Γ_contact +
Γ_higher` reduces to `Γ_tree = Γ_OGE + Γ_higher`, with `Γ_higher`
suppressed by `O(g_bare^2 / q^2)` per Feynman-rule power counting.
Therefore the OGE diagram is the complete tree-level `Γ_S^(4)` at
leading order in `g_bare^2 / q^2`.

This is the positive Lagrangian-completeness fact behind the
parent's D16 ("Feynman-rule completeness of the bare action at tree
order"), now stated as an independent narrow theorem rather than as a
parenthetical inside the parent's input table.

## V2 — Independence

This block is distinct from prior yt blocks (08, 10, 11, 13). None of
those touched the matter-sector Lagrangian-completeness / contact-4-fermion
question. The closest prior work was the 2026-05-10 open-gate diagnostic
`YT_WARD_STEP3_SAME_1PI_CONSTRUCTION_NARROW_THEOREM_NOTE`, which
documented the open Step 3 gap but explicitly did not close it. Block 14
closes the specific contact-vanishing step positively.

Block 14's content:

- not subsumed by the 2026-04-19 same-1PI pinning theorem (that note
  invoked "uniqueness of the scalar-singlet coefficient" as the bridge;
  block 14 supplies the orthogonal operator-counting fact);
- not subsumed by the 2026-05-10 abstract polynomial-algebra forcing
  theorem (that note is pure algebra `F^2 = c0` + `F^2 = g^2/(2N) =>
  g^2 = 2Nc0`; block 14 supplies the physical operator-content
  premise that justifies one of those equations);
- not subsumed by the 2026-05-17 g_bare-forced-via-Ward-substitution
  narrow theorem (that note is the algebraic-substitution closure;
  block 14 supplies the operator-content premise that legitimates the
  same-1PI equation it substitutes).

## V3 — A_min purity

- A1 (Cl(3)) + A2 (Z^3): used directly via the bare-action specification.
- No PDG observed values consumed.
- No fitted constants consumed (`g_bare` left symbolic).
- No literature numerical comparators consumed.
- No admitted unit conventions load-bearing on the claim.
- No canonical-plaquette-surface import in the runner.
- Sympy only; no numpy-based fitting.

Admitted-context inputs (open gates, explicitly listed):

- (A) staggered-Dirac realization derivation target
- (B) g_bare derivation target (referenced for context only; statement
  is g_bare-arbitrary)

Retained one-hop dependency inputs (cited as authorities):

- D9 (composite-Higgs structural fact) from `YUKAWA_COLOR_PROJECTION_THEOREM`
- D12 (SU(N_c) color-singlet Fierz coefficient) from `YT_EW_COLOR_PROJECTION_THEOREM`
- S2 (Clifford scalar projection c_S = +1) standard Clifford algebra
- D17 (composite-Higgs scalar-singlet uniqueness on Q_L) from
  `YUKAWA_COLOR_PROJECTION_THEOREM` Block 5
- `UNIT_SINGLET_OVERLAP_NARROW_THEOREM_NOTE_2026-05-02` for the
  retained H_unit form-factor identity

## V4 — Honest scope

What this narrow theorem CLAIMS (positive):

- (T1) every bare-action contact-4-fermion coefficient on Q_L = 0
- (T1a) scalar-singlet projection contact coefficient = 0
- (T2) OGE-only tree-level completeness of `Γ_S^(4)` at leading order
- (T2a) OGE coefficient = `-g_bare^2 / (2 N_c q^2)`
- (T3) same-1PI bridge reduces to (R) without a separate matching axiom

What this narrow theorem does NOT claim:

- Does NOT derive `g_bare = 1`. (`g_bare` is left arbitrary throughout.)
- Does NOT prove the Standard Model top-Yukawa observable.
- Does NOT close the parent `yt_ward_identity_derivation_theorem` row.
- Does NOT derive the H_unit operator's normalization `Z^2 = 6`.
- Does NOT introduce any new axiom beyond `A1 + A2 + admitted-context`.
- Does NOT consume any PDG / fitted / literature value.
- Does NOT touch any control-plane file or publication-matrix file.

## V5 — Failure modes

| Risk | Status |
|---|---|
| Wilson plaquette contributes a tree-level four-fermion piece | NO: Wilson plaquette is gauge-only, no fermion factor. |
| Staggered Dirac contains a contact 4-fermion term hidden in compact link | NO: staggered Dirac is fermion bilinear; gauge links act on fermion bilinears, not four-fermion contacts. |
| Multi-gluon exchange gives a leading correction | NO: Feynman-rule power counting (each trilinear vertex = O(g_bare); each propagator = O(1/q^2)) puts TGE at O(g_bare^4 / q^4), sub-leading. Verified in Block 4 of runner. |
| D9 composite-Higgs argument circular | NO: D9 is a retained structural axiom of the framework's operator content; not derived from the same-1PI bridge. |
| Substituting Rep B's form-factor into (R) is circular | NO: Rep B's form-factor is the retained UNIT_SINGLET_OVERLAP narrow theorem, an independent algebraic identity (1/sqrt(6)). The (R) identity follows from Rep A == Rep B at leading order, which itself follows from contact-vanishing (T1a); the substitution is the corollary, not the load-bearing claim. |
| Control-plane / publication-matrix touch | NO: this PR adds only the source note, runner, cache, and block artifacts. Verified by file list. |
| Audit-data touches | NO: no audit-state YAMLs, no audit-lane authority changes. |
| Fitted / PDG values consumed | NO: `g_bare` is symbolic; integer counts (N_c, N_iso, DIM_Q_L) only. |
| Block PR opens with merge / main push | NO: PR only; merge defers to independent audit lane. |

Block content is bounded; closure is conditional on the explicit
admitted-context inputs listed above. The runner is deterministic, A_min
compliant, and self-contained (no external dependencies beyond sympy).
