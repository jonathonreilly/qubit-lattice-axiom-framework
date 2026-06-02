# Flavor — J-hunt round 5 (final): the residual is trace-vs-center-state, and it genuinely DODGES the C³=I wall (so it is NOT the U(1)_b obstruction) — but the center-symmetric state is admissible-not-forced. 5-round consolidation: r=1/2 is the single named, unobstructed, unforced input.

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** final round of the iterative J-hunt + the 5-round consolidation. A precise localization of the residual (now proven *unobstructed*), not a closure.
**Runner:** `scripts/flavor_find_J_round5_trace_vs_center_state_2026_06_02.py` (SCORECARD 5/5).
**Source:** `wf_9b01207c` (r5) + the 4 prior J-hunt rounds.

## Round 5 — operator-level superselection: the trace-vs-center-state question
`ℝ[C₃]=ℝ⊕ℂ` has two minimal central idempotents `e₀=(I+C+C²)/3` (rank 1, singlet) and `e₁=I−e₀` (rank 2,
doublet). A *state* weights them:
- **trace** (dimension weighting `Tr e₀ : Tr e₁ = 1:2`) → per-DOF → **r=1 → Q=1** (det_R, default);
- **center-symmetric** (equal weight `1:1`) → `3a²=6|b|²` → **r=1/2 → Q=2/3** (det_C, observed).

**The genuine advance (new vs rounds 1–4):** the center-symmetric state is reached by the *discrete*
conditional expectation onto the center (`E(·)=e₀·e₀+e₁·e₁`) — **C³=I-compatible, NOT the continuous
rephasing `C→e^{iα}C`**. So it **genuinely dodges the C³=I / U(1)_b obstruction** that killed every
continuous lever in rounds 1–4 (verified R5-4; cleared 2 of 3 lenses — *forced-not-U(1)b-form* ✓,
*dodges-C³* ✓). **This proves the residual is not the U(1)_b wall.**

**Why it still fails (the third lens, forced-not-chosen):** no framework baseline+emergent-dynamics principle forces
`1:1` over `1:2`. The framework's reference state is **derived to be the trace**
(retained `pre_record_reference_state_tracial_derivation` + `powers_uhf_tracial_uniqueness` +
`tomita_tensor_trace`), and the trace restricted to the center *is* dimension-weighting (1:2 → r=1). The
center-symmetric state is **non-tracial** and is a *different, equally-admissible-but-unforced* point —
literally the `β≠0` point of the retained_no_go `koide_frobenius_isotype_split_uniqueness` family
`B_{α,β}(A,A)=(α+3β)Tr(Aₛ²)+α Tr(A_t²)` (the trace is `β=0`); PD + Ad-invariance + isotype-orthogonality
force *neither*. (Round 4's K₀=ℤ² lesson, restated: having 2 discrete central idempotents is a *count*,
not a *weighting*; calling the choice "center-symmetric state" doesn't make it forced.)

(Caveat: the trace's *selection* as the physical reference rests partly on PRR / full-inner-unitary
invariance, which is `audited_conditional` — so the trace is the *over-determined default* — equipartition
+ Plancherel + decoherence + derived-reference-state all give it — but not itself an airtight forcing.)

## The 5-round J-hunt consolidation
**r=1/2 (det_C / Q=2/3) is not forcible from framework baseline+emergent-dynamics; it is admissible-but-unforced.** The
residual has *one* cleanest statement, with four identical framings:

> **trace ↔ center-state  =  det_R ↔ det_C  =  (1,2) ↔ (1,1) isotype weighting  =  β=0 ↔ β≠0** (Frobenius family)

The arc localized the gap precisely:
- **Rounds 1–4** retired every *continuous* lever (static `J_cs` measure-neutral; fermionic Berezin fixes
  the det *exponent* not the *count*; Dirac reality structure generation-blind; per-DOF over-determined by
  equipartition+Plancherel+trace; K-theory counts blocks but is metric-free) — each either cancels in `r`,
  *is* the C³=I-forbidden `U(1)_b`, or is the C₃-equivariance-breaking non-circulant.
- **Round 5** found the one *discrete* lever (the non-tracial center-symmetric state) that **genuinely
  dodges C³=I** — proving the residual is a **state-selection authority**, not a symmetry wall.

**The framework defaults to the trace → Q=1** (maximal hierarchy); the observed **Q=2/3 is the
center-symmetric state**. The single missing input is sharply named and — crucially — now **unobstructed**:
a *positive principle that selects the non-tracial center-symmetric (equal-per-central-block) state over
the canonical trace* — equivalently, that forces `β≠0` / the (1,1) ratio. This is the **same open gate the
framework already records**: the only landed theorem reaching Q=2/3
(`charged_lepton_brannen_bae_delta_tier_a_bounded`, retained_bounded) does so by *explicit Tier-A
admission* of the C₃-breaking `δ=2/9`, not derivation; `lepton_brannen_bae_delta_two_ninths` is `open_gate`.

## The next path (not a closing statement)
Round 5 changed the character of the gap: the path to r=1/2 is **open, not walled**. What's needed is a
positive *state-selection* principle distinguishing "block = one mode" (center-symmetric → r=1/2) from
"DOF = one mode" (trace → r=1) — candidates: a **record/persistence** argument (each superselected
central block = one classical record), or a **chiral-mass-generation** argument. These are now known to be
*unobstructed by C³=I*, which is where the discrete center-state route earns its keep over the (dead)
continuous routes.

## Provenance (verified 2026-06-02)
- Central idempotents, trace(1:2)/center-symmetric(1:1) weightings, the discrete conditional expectation dodging C³=I: verified directly (runner 5/5).
- Anchors: `koide_frobenius_isotype_split_uniqueness` (retained_no_go — the β-family), `pre_record_reference_state_tracial_derivation` / `powers_uhf_tracial_uniqueness` / `tomita_tensor_trace` (retained — trace is the derived reference), `koide_c3_generator_rephasing_obstruction` (retained — leaves discrete central structure untouched), `inner_automorphism_invariance` / `flavor_ba_ratio_bound_hs_equipartition` (audited_conditional). Matches Koide's free per-sector fit (arXiv:1301.4143).
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
