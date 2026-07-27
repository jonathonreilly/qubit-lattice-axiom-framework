# Cycle 711 — V1–V5 Promotion Value Gate and N1–N8 No-Go Discipline Gate

Block: `physics-loop/poisson-beta-continuum-scaling-20260726`
Deliverable: `docs/POISSON_SELF_CONSISTENT_BETA_HAS_NO_FAR_FIELD_TO_EXTRAPOLATE_DEMOTION_NOTE_2026-07-26.md`
Runner: `scripts/physical_poisson_beta_has_no_continuum_limit_cycle711_2026_07_26.py` (8 PASS / 0 FAIL)

This is the **2nd PR** in the `self_consistency_forces_poisson_note` parent-row
family this campaign (after PR #5656). The judgment-based cluster-cap evaluator
triggers from the 3rd, so it does not gate this PR; the content-integrity criteria
are nonetheless answered under V5 and in the cluster-cap section below.

## V1–V5 Promotion Value Gate

**V1 — What specific verdict-identified obstruction does this PR close?**
The parent note's first caveat, verbatim, which is the sole defence of its Bounded
Claim 1 against a measured exponent of 1.28 rather than the Newtonian 1.0:

> "**Finite-size beta**: The measured beta ~ 1.28 exceeds the target 1.0 due to
> Dirichlet BC on small lattices (N=20). The distance-law closure script
> demonstrates beta -> 1.0 in the continuum limit via extrapolation from larger
> lattices (up to 96^3)."

PR #5656 emptied the note's two operator discriminators and named this
extrapolation, explicitly, as the highest-value open follow-up — because the note
ran its continuum argument for Poisson alone and never for the rivals. This is that
follow-up. It is a derivation-gap obstruction on the parent row itself. **PASS.**

**V2 — What new derivation does this PR contain that the audit lane doesn't
already have?**
The audit lane's verdict on this row notes the `r^(-2.805)` susceptibility
inconsistency but says nothing about the `beta` caveat, and nobody has run the
finite-size scaling for the rival operators. New content:

1. **Poisson's self-consistent `beta` does not extrapolate to 1.0.** `b_inf` is
   `1.2747 ± 0.0177` (`1/N` family) and `1.1578 ± 0.0012` (`1/N + 1/N^2` family),
   against the caveat's asserted 1.0. Over the doubling N=24 → 48 it moves
   `+0.0311` (S1).
2. **The continuum ranking is indeterminate**: the two families disagree on the
   sign of the Poisson-versus-biharmonic gap (S3). This independently confirms
   #5656's R16 — and had #5656 taken the stronger reading, this cycle would have
   refuted it.
3. **The mechanism**: the self-consistent source is scale-locked. Total mass is
   pinned to 1 and `RMS/N` is constant at ≈`0.30` across sizes 16–48, so the source
   never localizes and no point-source limit exists (S5).
4. **The diagnostic measures inside its own source**, and increasingly so: the
   fraction of source mass within the `beta` fit window rises from `0.5067` at
   N=16 to `0.8449` at N=48 (S6). **Enlarging the lattice moves the diagnostic
   further from a far-field measurement, inverting the caveat's premise.** This
   also explains why the power-law fit quality degrades monotonically for both
   operators (S4).
5. **The caveat cites a different observable.** The script it names measures ray
   deflection in a prescribed `f = s/r` field per its own docstring, and contains
   no occurrence of `self_consistent` (S7). **PASS.**

**V3 — Could the audit lane already complete this from existing retained
primitives plus standard math machinery?**
No. Finite-size extrapolation is standard machinery and is not the new part. The
new part is running the parent construction across seven lattice sizes for three
operators and measuring where its own diagnostic's fit window sits relative to its
own source. Those are outputs of this specific construction. Reaching N=48 for the
biharmonic rival required factorizing each operator once per size with `splu` and
reusing it across iterations rather than re-solving; the naive route is too slow to
run. No framework axiom or primitive is load-bearing — this is a
diagnostic-correctness result, which is why the artifact is a demotion packet.
**PASS.**

**V4 — Is the marginal content non-trivial?**
Yes. The strongest item is S6: the diagnostic's fit window contains most of its own
source, and the contained fraction *rises* with lattice size. That converts the
caveat from "unsupported" to "backwards" — the remedy it proposes makes the
measurement worse. Identifying that a finite-size defence points the wrong way is
not a restatement of anything in the ledger. **PASS.**

**V5 — Is this a one-step variant of an already-landed cycle in this campaign?**
No. Closest is PR #5656 on the same parent row. Structural distinctions:
- **Different claim object.** #5656 addressed the note's two *discriminators*
  (attractiveness, 0.93 correlation). This addresses its *caveat* — the finite-size
  defence of the exponent — a separate load-bearing sentence.
- **Different computation.** #5656 ran single-size diagnostics at N=10/20/24. This
  is a seven-size scaling study with two extrapolation families, reachable only via
  per-size factorization.
- **New load-bearing premise.** Source scale-locking (S5) and fit-window
  containment (S6) appear nowhere in #5656.
- **It could have refuted its predecessor.** S3 tests whether #5656's R16 was right
  to refuse naming a better operator. That is a genuine check on the prior cycle,
  not an application of it. **PASS.**

**Gate result: PASS on all five.**

## Cluster-cap content-integrity criteria (answered though not yet triggered)

1. **New load-bearing premise?** Yes — source scale-locking and fit-window
   containment (S5, S6), neither present in PR #5656.
2. **Distinct claim type?** Both are demotion packets, but on different sentences
   of the parent note: #5656 on Bounded Claims 1–3 via the discriminators, this on
   Caveat 1 via finite-size scaling. The artifact kind is shared; the target is not.
3. **Independently reviewable?** Yes. The runner imports the parent construction and
   stands alone; it cites #5656 for context (R7's per-layer result, R10's sign
   normalization) but re-derives nothing from it and does not depend on its files.
   Based on `main`, not stacked.
4. **Marginal review value?** A combined PR would have been better *if* both were
   known at once. They were not: this cycle exists because #5656's own handoff named
   it as the open follow-up, and its result changed #5656's standing (confirming
   R16). Splitting also keeps the confirmation independent rather than
   self-certifying.

## N1–N8 No-Go Discipline Gate

Applies because the deliverable asserts negative results. The negative claims are:
Poisson's `beta` does not extrapolate to 1.0 (S1); the continuum ranking is
indeterminate (S3); the diagnostic has no far field to measure (S5, S6); the
caveat's cited script is a different observable (S7).

**N1 — Alternative route enumeration.**

| # | Route | What it would attempt | Outcome |
|---|---|---|---|
| 1 | Larger lattices | N=48 is too small; go to 96³ as the caveat does | **PARTIALLY ATTEMPTED, and the trend answers it.** From N=24 to N=48 `beta` moves `+0.0311`; reaching 1.0 needs ~8 further doublings (N ≈ 6000). More decisively, S6 shows larger N makes the fit window *more* interior, so 96³ moves the wrong way. Declared: 96³ not run for the self-consistent loop (biharmonic at N=48 already dominates runtime). |
| 2 | A different extrapolation family | `1/N` and `1/N+1/N^2` are the wrong ansätze; another reaches 1.0 | **ATTEMPTED for two families (S1), which are the ones the repo's own distance-law script uses.** Not exhaustive, and S1's ledger row says so explicitly. This is the weakest point of the cycle and is declared, not hidden. |
| 3 | A different decay diagnostic | `check_field_physics`'s log-log fit is the problem | **ATTEMPTED indirectly (S4).** The fit quality degrades monotonically for both operators, so the diagnostic is deteriorating rather than merely noisy. A better diagnostic is exactly the constructive repair the note proposes. |
| 4 | Amplitude/coupling matching | The sizes are compared at unmatched field amplitude | **RULED OUT BY PRIOR (#5656 R15).** `beta` is amplitude-independent to within 0.023 across an 80-fold `G` sweep. |
| 5 | Source sign convention | The scaling is an artifact of the per-operator sign normalization | **RULED OUT BY PRIOR (#5656 R10).** The normalization fixes only a sign; `beta` is a log-log slope of `abs(phi)` and is invariant to it. |
| 6 | The caveat means the Green's function's `beta`, not the self-consistent field's | Read the caveat charitably as an operator statement | **ATTEMPTED.** For a point source Poisson gives `1/r` and `beta = 1` trivially in infinite volume — no 96³ study needed. So the charitable reading makes the caveat's citation vacuous rather than supportive, and it still does not defend the note's *measured* 1.28, which is a self-consistent-field number. |
| 7 | Fixed-source construction | Hold a localized source fixed while the box grows; then `beta` may reach 1.0 | **NOT ATTEMPTED — declared, and named as the successor.** This is the constructive repair in the note. It requires abandoning the parent propagator's per-layer normalization for the source step. It is the one route that could recover a far-field exponent, and this cycle does not claim it fails. |

**N2 — Wall-independence audit.** Named walls: (a) no extrapolation to 1.0;
(b) indeterminate ranking; (c) source scale-locking; (d) fit-window containment;
(e) wrong cited observable. (c) and (d) are **not independent** — (d) follows from
(c) plus the fixed `2..N//2-3` window, and the note presents (d) as the consequence
("And `check_field_physics` fits radii … which lies **inside** that source"). (a)
and (b) both rest on the same seven measurements and two families, so they are
**not independent** either; the note reports them as two readings of one dataset.
(e) is independent of all others — it is a string-level fact about a different file.
No wall is presented as independent where it follows from another.

**N3 — Hidden-wall scan.** Grepped for "we assume", "by construction",
"naturally", "standard", "registered", "canonical". Hits: "by construction" in the
note's §C describing the box-filling source — that is the finding, not a hidden
premise. Conditions promoted to explicit `[supplied]` tags: the parent parameters,
the parent `beta` diagnostic and its fit window, the two extrapolation families,
least squares as estimator, the flat-field probe for S5, fixed `sigma = 2.0` as N
grows, and the fact that only two families are tested. The last of these is the
cycle's real limitation and it is tagged in both S1 and S3.

**N4 — Residual matching.** Witnesses cited: the parent note's Caveat 1 (quoted
verbatim, matches exactly); the cited script's docstring (quoted verbatim, verified
programmatically in S7); PR #5656's R7, R10, R15, R16 (each used for a specific
prior result, and each matches). Nothing dropped.

**N5 — Rhetoric audit.** Checked at the resolutions actually tested:
- "does not extrapolate to 1.0" — two families, seven sizes, 16–48. Narrowed in S1
  to those families; the row says explicitly it is not a claim that no family could.
- "the ranking is indeterminate" — narrowed to "on this evidence", two families.
- "the source never localizes" — verified at six sizes with the flat-field probe;
  `RMS/N` reported per size, not asserted as a limit theorem.
- "the fit window lies inside the source" — per-size enclosed fractions reported;
  S6's row states it does not claim the *field* has no far field, only that this
  window does not sample one.
- "enlarging the lattice moves the diagnostic further from a far-field measurement"
  — verified as a monotone increase over the six tested sizes, not asserted for all N.

**N6 — Partial-closure path scan.** The caveat is repairable by convention in one
direction: restrict Bounded Claim 1 to the screened family, where #5656 R13 leaves
it intact. The note proposes exactly that rather than deletion, and lists Tests 1
and 4 as surviving. No "new axiom required" language appears; no axiom or primitive
is involved.

**N7 — Steelman.** Written in full in the note itself, not only here: *"there is no
reason the self-consistent `beta` should have a continuum limit at all, so
extrapolating it is meaningless, and citing a fixed-source script is the right
move."* This is **correct as physics**, and S5/S6 prove its first half. It does not
rescue the caveat: either `beta` has a limit and it is 1.16–1.27 (S1), or it has
none and there is no continuum value to appeal to (S5, S6) — and a fixed-source
deflection extrapolation cannot supply one for a different observable (S7). The
objection selects which reading is right; it does not yield a third in which Bounded
Claim 1 survives. It does identify the constructive repair, which the note records
as the successor. **Not demoted for N7**, and the steelman is carried into the
deliverable.

**N8 — Cross-cycle echo.** Structurally similar prior wall: PR #5656's R6, where my
own preferred repair (removing per-layer renormalization) was falsified by test
rather than argument. Same pattern here — my own expectation was that Poisson would
extrapolate cleanly to 1.0 and the interest would be whether biharmonic did too.
It does not, and the reason turned out to be the source construction rather than the
operator. Both cycles resolved by testing the repair rather than assuming it. No
structurally similar wall was found that has since been retired by a mechanism not
considered here.

**Gate result: no failure condition hit. Route 2 (other extrapolation families) is
declared as non-exhaustive and is the cycle's weakest point; route 7 (fixed-source
construction) is declared unattempted and named as the successor.**

## Open routes this cycle does not close

1. **The fixed-source repair (N1 route 7).** A localized source of fixed extent and
   fixed total mass, with the exponent fitted at radii outside it. This is the one
   route that could recover a far-field exponent from this construction, and this
   cycle makes no claim that it fails. It requires abandoning the per-layer
   normalization for the source step — and #5656 R6 showed that same removal does
   not by itself repair the response kernel, so the two repairs are independent and
   both would be needed.
2. **Extrapolation families beyond the two tested.** S1 and S3 are scoped to `1/N`
   and `1/N + 1/N^2`.
3. **96³ for the self-consistent loop.** Not run; the trend and S6 argue it would
   not help, but it is not measured.
