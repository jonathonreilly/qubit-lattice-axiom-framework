# Block 01 — Review History

**Loop:** filter-excluded-positive-closures-2026-05-17
**Block:** 01 (staggered-Dirac realization gate closure synthesis)
**Date:** 2026-05-17

## V1-V5 Promotion-Value Gate

Full V1-V5 record (verbatim from `/tmp/physics-loop-2026-05-17/block01-prompt/VALUE_GATE.md`):

### V1 — What SPECIFIC obstruction does this close?

The parent gate note (`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`)
records that "pieces of an 'A1+A2 forces the staggered-Dirac realization'
chain exist across the in-flight supporting notes... [but] have not been
packaged as a single end-to-end canonical proof."

The four explicit named obstructions:
1. Forcing the Grassmann partition from A1+A2
2. Staggered taste structure (Kawamoto-Smit forcing argument from A1+A2)
3. Substrate-fundamentality bridge (delegated to one-axiom chain — out of scope)
4. Physical-species bridge (open identification residual)

This synthesis closes obstructions (1) and (2) as a single packaged
end-to-end forcing chain on the named upstream stack, and packages
obstruction (3)'s algebraic content (BZ-corner 1+1+3+3 + hw=1 M_3(C))
as the BZ-corner derivation step. Obstruction (4) remains explicitly
open per the May-10 positive ratchet attempt and the substep-4 AC
narrowing — this synthesis honestly carries that residual as a named
admitted-context atom (`AC_residual = AC_φ ∧ AC_φλ`) rather than
silently dropping it.

**V1 outcome: PASS**

### V2 — NEW derivation content?

Yes:

1. Cross-substep dependency graph (lemma chain T2 → T3 → T4 → T5
   with explicit input/output matching at each step).
2. Joint dependency chain audit (full hypothesis set across all
   substeps named — 20 cited authorities; A1, A2 + 18 retained/
   support/admissible. This enumeration was not on record before).
3. Honest residual statement (synthesis enumerates that gate closes for
   kinetic + algebraic-structure surface but species-label residual
   remains open admitted context requiring external input).
4. Counterexample probes (A1-violation probe with Cl(4) carrier;
   A2-violation probe with non-bipartite substrate; chain-consistency
   end-to-end probe). New content not present in any substep runner.

**V2 outcome: PASS**

### V3 — Could the audit lane alone do this?

No. The audit lane evaluates individual notes and runners; it does not
synthesize multi-note derivation chains into a single end-to-end
forcing claim. The structural insight — that substeps 1-3 chain together
into a closure of the staggered-Dirac kinetic-and-algebra surface, while
substep 4 remains a separate residual — is new content that the audit
lane cannot manufacture from the existing four notes.

The synthesis also makes the classification choice (positive_theorem
vs bounded_theorem with named residual). Audit verifies the choice
but cannot construct it.

**V3 outcome: PASS**

### V4 — Marginal content non-trivial?

Yes. The substep notes are each bounded_theorem; their combined synthesis
is also bounded (because the S2 spin-statistics support input is still
re-audit-dependent, and substep 4's AC_φλ remains an open residual).
But the bounded synthesis is a higher-utility object than four separate
bounded substeps:

- Single citeable bounded source for downstream lanes (retires parent
  gate's "no single packaged proof" weakness).
- Explicit residual enumeration (what hostile reviewers and the audit
  lane need to know whether to depend on the chain).
- Identifies which residual atoms (AC_φ, AC_φλ) are genuinely open
  vs candidate-derivable.

This is non-trivial because before this synthesis, downstream lanes had
to read 5+ substep notes and the May-10 ratchet attempt to figure out
"is this gate effectively closed for my surface?". After this synthesis,
the answer is recorded as: "kinetic + algebra surface is closed (bounded);
species-label surface is open (named residual)".

**V4 outcome: PASS**

### V5 — Not a one-step variant of a landed cycle?

No. The synthesis is the FIRST note that:

1. Explicitly chains T2 → T3 → T4 → T5
2. Enumerates the FULL hypothesis set across all substeps
3. Records the gate's honest tier classification (bounded_theorem
   with named residual) at the synthesis level
4. Provides counterexample probes that test the chain end-to-end

It is NOT a relabel of any landed cycle (substep 1 / 2 / 3 / 4 partial
/ substep-4 AC narrowing / substep-4 positive ratchet stretch).

**V5 outcome: PASS**

## Overall outcome

**ALL V1-V5 PASS.** Synthesis built as `bounded_theorem` with named
carried residuals (AC_φ, AC_φλ, S2 inherited). NOT `proposed_retained`
positive_theorem — substep 4's species-label residual prevents that
tier per the 2026-05-10 positive ratchet attempt.

## Self-review disposition

**Disposition:** PASS — proceed to commit + push + open PR.

**Self-review checks performed:**

1. **Source-only policy compliance** — only 3 source artifacts (note,
   runner, cache) + block artifacts under `.claude/science/physics-loops/`.
   No output-packets, no lane promotions, no synthesis "Block" notes.

2. **Honesty checks:**
   - Note proposes `bounded_theorem`, not retained / promoted bare.
   - Authority disclaimer present: "Effective `effective_status` is
     generated by the audit pipeline only after the independent audit
     lane reviews..."
   - Residuals explicitly enumerated (3: AC_φ, AC_φλ, S2_re_audit).
   - Substep 4 species-label residual carried forward as named
     admitted-context, not silently dropped.
   - Runner enumerates exactly 20 authorities matching the note's
     premise + retained/support tables.

3. **Forbidden-imports check:**
   - No PDG observed values
   - No lattice MC empirical measurements
   - No fitted matching coefficients
   - No new axioms beyond A1+A2
   - No HK + DHR appeal
   - No re-opening of retired no-go routes (substrate-to-pa,
     first-order coframe, physical-lattice necessity)

4. **Runner-verification:**
   - 17 PASS / 0 FAIL on live execution
   - Cache fresh per `precompute_audit_runners.py --check-only`
   - Independent algebraic verification (Hamming-weight 1+3+3+1=8;
     KS phases via T^dag sigma_mu T on all 24 (site, direction) pairs;
     Pauli chirality sigma_1 sigma_2 sigma_3 = i*I; orthogonality from
     distinct joint eigenvalues; C_3[111] 3-cycle on hw=1 corners).

5. **Memory-feedback rules respected:**
   - `feedback_consistency_vs_derivation_below_w2.md`: residuals
     honestly enumerated; not consistency-equality dressed as derivation.
   - `feedback_hostile_review_semantics.md`: stress-tests action-level
     "closure" semantics — closes kinetic-and-algebra surface, NOT
     species-label identification.
   - `feedback_retained_tier_purity_and_package_wiring.md`: synthesis
     is bounded_theorem (not retained); standard 1-theorem + 1-runner
     + 1-cache packaging.
   - `feedback_physics_loop_corollary_churn.md`: synthesis is genuine
     cross-substep chaining + new residual enumeration + new
     counterexample probes, not a one-step relabel.
   - `feedback_primitives_means_derivations.md`: no new axioms; only
     "new" content is chaining structure + residual enumeration +
     counterexample probes, all from A1+A2 + retained authorities +
     admissible standard math.
   - `feedback_review_loop_source_only_policy.md`: only source theorem
     note + paired runner + cached output committed. Block artifacts
     under `.claude/science/physics-loops/` (allowed planning surface).

**Disposition rationale:** All V1-V5 pass for bounded_theorem audit
seeding (the honest tier). Synthesis closes substeps 1-3 chain as a
named-residual bounded forcing, retires parent gate's "no single
packaged proof" weakness, and explicitly carries substep 4's
species-label residual forward as named admitted-context. No bare
retained / promoted claims. Independent audit required before any
effective_status change.
