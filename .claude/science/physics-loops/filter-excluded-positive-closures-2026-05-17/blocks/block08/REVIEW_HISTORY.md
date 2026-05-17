# REVIEW HISTORY — Block 08 (yt vertex-power operator-counting lemma)

**Date:** 2026-05-17
**Block:** 08 — yt_vertex_power_derivation positive-closure attempt
**Branch:** `physics-loop/yt-vertex-power-derivation-block08-2026-05-17`
**Artifact:** `docs/YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md`
              + `scripts/frontier_yt_vertex_power_operator_counting_lemma.py`
**Honest tier:** conditional-bounded operator-counting structural lemma

## 1. Promotion Value Gate (V1-V5)

### V1: What SPECIFIC verdict-identified obstruction does this PR close?

**Answer:** The parent target `yt_vertex_power_derivation` (note
`docs/YT_VERTEX_POWER_DERIVATION.md`) is `unaudited` with
`transitive_descendants: 889` and `load_bearing_score: 11.298`. Its
companion narrow algebraic theorem
`alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10`
is `retained` but explicitly disclaims:

> Does NOT assert that the vertex-power exponent k = 2 is a prediction
> of the framework's axioms; it enters this note as the algebraic
> exponent in definition (2).

The companion is over abstract `R+`. This block supplies the missing
*operator-level* structural lemma that grounds `n_link = 2` in the
staggered Dirac operator structure (conditional on the staggered-Dirac
realization gate and the standard link-exponential convention).

**Disposition: PASS** — the operator-level gap is real and named.

### V2: What NEW derivation does this PR contain?

**Answer:** Three new explicitly-stated structural statements (S1, S2, S3)
with paired runner verification:

1. **S1 (single-link vertex):** Proof that `D' = dD/dA|_{A=0}` carries
   exactly one factor of the gauge link `U_mu(x)` per non-zero matrix
   element, from the staggered Dirac hopping form and the link-exponential
   convention. Runner verifies via `D'[lambda U] = lambda * D'[U]` to
   machine precision across five `lambda` values.

2. **S2 (bubble degree-2):** Proof that
   `Pi = -Tr[D^{-1} D' D^{-1} D']` is homogeneous of degree exactly 2 in
   `D'`. Runner verifies via log-log slope = 2.000000 (max rel.dev
   3.38e-16) and explicitly excludes degree 1 (would be `n_link=1`) and
   degree 4 (would be plaquette).

3. **S3 (relative count):** `n_link(vacuum polarization) = 2 = 2 ×
   n_link(hopping)`. Runner verifies relative count = 2.000000 to 2.22e-15.

   Companion: `Tr[D^{-1} D'']` is degree-1 in `D''` (slope = 1.000000),
   confirming the tadpole-vs-bubble structural distinction.

These statements are not in any existing note in `docs/` (verified by
case-insensitive substring search on `D' = dD/dA`, `degree-2 in D'`,
`n_link(VP) = 2`).

### V3: Could the audit lane already complete this?

**Answer:** No. The audit ledger row for `yt_vertex_power_derivation`
shows `runner_check_breakdown {A:0, B:0, C:0, D:0}` and
`effective_status: unaudited` with `effective_status_reason:
awaiting_audit`. The existing runner `scripts/frontier_vertex_power.py`
verifies the *consequences* (factorization, plaquette identity,
alpha_s(M_Z) match) but does not isolate the **structural** statements
S1/S2/S3 — it verifies them implicitly via composite arithmetic, not as
clean homogeneity-degree checks. This block packages the load-bearing
structural piece as a standalone verifiable lemma.

### V4: Is the marginal content non-trivial?

**Answer:** Yes:

- S1's machine-precision verification (max deviation 0.00e+00 across 5
  lambda values) is a sharp falsifier — any term in `D'` carrying two
  links would have produced quadratic deviation.

- S2's log-log slope = 2.000000 across `lambda ∈ {0.5, 0.7, 1.0, 1.3, 2.0}`
  cleanly distinguishes the bubble from the tadpole (degree-1) and the
  plaquette (degree-4) at machine precision.

- S3's relative count 2.000000 to 2.22e-15 is the load-bearing structural
  input that the companion algebraic theorem treats as a definition; this
  block converts it into a verifiable structural lemma.

### V5: Is this a one-step variant of an already-landed cycle?

**Answer:** No. Recent yt-cluster block work (2026-05-17) consists of
hostile-audit findings notes on the boundary / bridge-* notes (see
`docs/YT_BOUNDARY_THEOREM_HOSTILE_AUDIT_FINDINGS_NOTE_2026-05-17.md` and
siblings — these are dependency-classification artifacts, not new
derivations). The vertex-power operator-counting lemma is structurally
distinct from all of those: it is a new bounded-theorem statement on
the operator-level vertex insertion count, not a citation-graph
classification.

Recent campaigns reviewed: `plaquette-bootstrap-closure-20260503`,
`pmns-branch-selector-2026-05-03`, `industrial-sdp-bootstrap-20260503`,
`positive-only-retained-20260502`. None of these touched the vertex-power
operator-counting structure.

**Disposition: PASS** — structurally distinct from prior blocks.

## Value Gate disposition: PASS

All V1-V5 answers PASS. The PR is allowed.

## 2. Self-review findings

### Runner check

`python3 scripts/frontier_yt_vertex_power_operator_counting_lemma.py`:

```
PASS: 8  FAIL: 0
Time: 0.1s
```

Individual checks:
- S1_single_link_vertex: PASS (max dev 0.00e+00)
- S2_bubble_degree2: PASS (slope = 2.0000, rel.dev ≤ 3.38e-16)
- S2_bubble_not_degree1: PASS (excludes n_link=1)
- S2_bubble_not_degree4: PASS (excludes plaquette)
- S2_tadpole_degree1: PASS (rel.dev ≤ 1.81e-16)
- S3_hopping_n_link_eq_1: PASS (max dev 0.00e+00)
- S3_relative_count_2_to_1: PASS (rel.dev = 2.22e-15)
- S2_bubble_nontrivial: PASS (|Pi_base| = 4.7699e+03)

### Hard-rule compliance

- A_min only: YES. The runner uses `numpy`, `scipy.linalg.solve`. No
  observational targets (no PDG, no `alpha_s_MZ_obs`, no `m_t_obs`, no
  `M_Z`). No `canonical_plaquette_surface` import. No fitted constants.
  The only numerical constants are: `N_C = 3` (Cl(3) color from A1),
  `L = 4` (lattice size for verification), `M_REG = 0.05` (regulator
  mass to keep `D` invertible at the symmetric point; appears nowhere
  in any claim).
- No audit-data touches: YES. No edits to `docs/audit/data/`.
- No fitted/observational/literature: YES.
- No merge / no main push: YES (PR only).

### Scope vs claim discipline

- The note explicitly names three admissions and states what is NOT
  claimed (no closure of renormalized lane, no `alpha_s(M_Z)` derivation,
  no derivation of staggered-Dirac realization).
- The runner exclusion checks (`S2_bubble_not_degree1`,
  `S2_bubble_not_degree4`) are explicit falsifiability witnesses for
  the n_link = 2 count, not just consistency checks.
- The companion `alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10`
  status (retained, abstract algebra) is explicitly cited as the
  downstream-of-this-lemma boundary.

### Hostile review pre-mortem

- Could an auditor object that `n_link = 2` is "obvious from one-loop
  perturbation theory"? Yes, but the verification is non-trivial: the
  runner shows the count is *exactly* 2 (slope 2.000000), not
  approximately, and explicitly distinguishes from 1 and 4 at machine
  precision. The lemma is the *operator-level* support that the
  companion algebraic theorem disclaims; "obvious" is precisely what an
  audit-grade note is supposed to make machine-checkable.
- Could an auditor object that the lemma still depends on the
  staggered-Dirac gate? Yes — and the note states this in the admissions
  section. The claim type is `bounded_theorem`, not `positive_theorem`.
- Could an auditor object that the runner uses `scipy.linalg.solve`? It
  is standard linear-algebra infrastructure, not a fitted/observational
  import; the operation `D^{-1} D'` is purely structural.

## 3. PR body draft

(in CLAIM_STATUS_CERTIFICATE.md)

## 4. Next-block recommendation

The parent target `yt_vertex_power_derivation` itself can now be audited
with this lemma as the operator-level support; recommend the next block
work on a downstream `unaudited` yt-cluster note such as
`yt_zero_import_authority_note` (`unaudited`, td=869, lb=13.765) or
`alpha_s_derived_note` (`unaudited`, td=898, lb=37.812) — both have
massive descendant counts and now have stronger structural support from
this block's lemma.
