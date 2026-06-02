# Flavor — J-hunt consolidation (4 rounds): det_C / r=1/2 / Q=2/3 is not forcible from A1+A2+emergent-dynamics; it is the single named block-count *measure* input. The framework defaults to det_R / Q=1.

**Date:** 2026-06-02
**Claim type:** consolidated bounded result of a 4-round iterative hunt — the residual sharply isolated to one named open object. Not a closure of r=1/2; not a no-go-with-closing-language.
**Status authority:** independent audit lane only.
**Runner:** `scripts/flavor_find_J_round4_consolidation_kappa_is_input_2026_06_02.py` (SCORECARD 4/4).
**Source:** J-hunt workflows `wf_719da018` (r1), `wf_d2438beb` (r2), `wf_2d355f65` (r3), `wf_702357cd` (r4, consolidating, 5/5 unanimous).

## The hunt
Find a complex structure / mechanism that forces the C₃ generation doublet to count as **one complex
mode** (det_C → r=1/2 → Q=2/3, the observed charged-lepton value), is not the C³=I-forbidden continuous
`U(1)_b`, and descends from A1. Four genuinely-distinct levers were attacked.

## The four rounds (all det_R-default)
1. **Static complex structure (`J_cs`).** `J_cs=(C−C²)/√3` is A1-native (Schur-forced, anti-Hermitian)
   but **measure-neutral**: `exp(θJ_cs)=SO(2)` preserves *both* det_R and det_C measures. A static J
   cannot select the count. (The "Γ_χ = J_cs" chiral bridge was a false identity.)
2. **Fermionic Berezin frame.** Fermionic-vs-bosonic fixes the determinant **exponent**
   (`det^{+1}` vs `det^{−1/2}`), **not** the doublet mode-**count**. Berezin gives `det(H)` (a
   determinant-product of 3 real factors), not the block-total; C₃ admits *both* the symmetric `I`
   (det_R) and antisymmetric `J=C−C²` (det_C) as invariant bilinears, so det_C's `J` is an unforced posit.
3. **Charged-lepton Dirac reality structure.** Charged leptons are Dirac (e⁻≠e⁺) — but this factorizes
   as `J_spin ⊗ I_generation`: charge conjugation acts as the **identity on the generation index**, so
   it is generation-blind and a spectator to the doublet. It does not supply the J.
4. **Block-count measure (the decisive, consolidating round).** Per-DOF / dimension / trace counting
   (→ r=1, det_R) is the **over-determined default**: three independent principles converge on it —
   the **equipartition theorem** (under `exp(−β‖H‖²)`, `⟨a²⟩=⟨|b|²⟩` → r=1; verified analytic + MC),
   the **Plancherel/character measure** (irreps weighted by dimension 1:2 → per-DOF → r=1), and the
   **trace energy functional** `‖H‖²=Tr(H†H)` → the (1,2) weighting. The strongest selector candidate,
   **K-theory/Wedderburn**, genuinely **fails**: `K₀(ℝ[C₃])=K₀(ℝ⊕ℂ)=ℤ²` counts the *two blocks* (fixing
   the generation **count** = 3) but is **dimensionless, metric-free, amplitude-constant** — it answers
   "how many blocks" (=2), not "how to weight block energies." Superselection doesn't rescue per-irrep
   either: the trace still counts each sector's full real dimension; collapsing the doublet's 2 states
   into 1 slot is the continuous `SO(2)/U(1)_b` angular quotient on `arg b` — the C³=I-forbidden lever
   already retired in rounds 1–3.

## Consolidated verdict
**det_C / r=1/2 / Q=2/3 is not forcible from A1+A2+emergent-dynamics by any of the four attacked
levers.** The common root: every *continuous* lever leaves `b` fixed and cancels in `r`, or is the
C³=I-forbidden `U(1)_b` rephasing, or is the C₃-equivariance-breaking non-circulant operator
(retained_bounded `koide_z3_equivariant_anticommuting_no_go`). The single residual is **not a symmetry
generator** but the **counting *measure*** on the C₃ isotype split `ℝ³ = trivial(1d) ⊕ standard(2d
real-irreducible)`:

> **det_C** = per-irreducible-**block** / equal-per-sector weighting `(1,1)` → **r=1/2 → Q=2/3** (observed)
> **det_R** = per-real-**dimension** / Plancherel / trace weighting `(1,2)` → **r=1 → Q=1** (the default)

This is **identical to the freedom** that `koide_frobenius_isotype_split_uniqueness` (retained_no_go —
the singlet:doublet ratio is free on the C₃-invariant cone) and `action_normalization` (retained_no_go —
declines to rank (1,1) vs (1,2)) explicitly leave open. The framework **defaults to det_R / Q=1**
(maximal hierarchy); the observed **Q=2/3 corresponds to det_C** (the equal-block weighting). This
**matches the literature**: Koide's Z₃ phenomenology (arXiv:1301.4143) likewise leaves the per-sector
ratio a **free fit** — nobody derives it.

So the honest standing of the whole charged-lepton value: the *structure* (3 chiral generations, the
exact `Q=1/3+(2/3)r`, the C₃ channels, the carrier) is derived; the *value* `r=1/2` is the **single
irreducible flavor input** — a per-irrep-vs-per-DOF **measure choice** (det_C vs det_R) — not forced by
the axioms, matching the field's frontier.

## The next path this opens (not a closing statement)
The residual is one precisely-named open object: the **block-vs-DOF counting measure** on the C₃ isotype
split. The one genuinely-distinct lever not yet exhausted is **operator-level superselection /
sector-factorization** on the framework's own `M₂(ℂ)`-per-site + `ℝ[C₃]` algebra — whether the trivial
and standard C₃ sectors can be made genuine *separate-power* sectors at the **operator** level (forcing a
per-sector power constraint = r=1/2), rather than the continuous angular quotient the retained surface
blocks. (Round 4's Routes 2–3 already found ordinary superselection insufficient; a stronger
operator-algebraic sector-factorization would be the next attempt.)

## Provenance (verified 2026-06-02)
- Equipartition→r=1 (analytic+MC), Plancherel→r=1, K₀=ℤ², det_C/det_R→r=1/2 / r=1: verified directly (runner 4/4).
- Anchors: `koide_frobenius_isotype_split_uniqueness` (retained_no_go), `action_normalization` (retained_no_go), `koide_z3_equivariant_anticommuting_no_go` (retained_bounded), `koide_kappa_two_orbit_dimension_factorization` (retained_bounded). Unaudited probe-notes (plancherel/maxent/block-total-measure) flagged, not load-bearing.
- Attribution: Koide & Nishiura Z₃ parametrization (arXiv:1301.4143) leaves the per-sector ratio a free fit.
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
