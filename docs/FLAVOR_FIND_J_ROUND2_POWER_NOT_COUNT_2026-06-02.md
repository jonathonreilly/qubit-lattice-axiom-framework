# Flavor — J-hunt round 2: the fermionic frame does NOT force det_C (power ≠ count; the symplectic pairing J is unforced). det_R/Q=1 stands; the wall moves to Dirac-vs-Majorana reality structure.

**Date:** 2026-06-02
**Claim type:** bounded negative (round 2 of the iterative J-hunt) + the power-vs-count clarification.
**Status authority:** independent audit lane only.
**Runner:** `scripts/flavor_find_J_round2_power_not_count_2026_06_02.py` (SCORECARD 4/4).
**Source:** workflow `wf_d2438beb` — 5 hunt routes + 3-lens verification + synthesis (12 agents).

## The test
Round 1 showed a *static* complex structure is measure-neutral; the lever became a **first-order
(Dirac/Berezin) action** — i.e. the matter being **fermionic** (P1, the sector's one import). Round 2
tested the bridge **[fermionic] → [Berezin det_C] → [r=1/2 → Q=2/3]**, which would *unify* r=1/2 with
the chirality gate.

## Round-2 verdict: det_R/Q=1 stands — the bridge does not close
Guard (i) **passes** (P1 is independently motivated by spin-statistics/the carrier, not posited to reach
r=1/2). Guards (ii),(iii) **fail**, for three verified reasons:
1. **Power ≠ count.** Fermionic-vs-bosonic fixes the determinant *exponent* (Grassmann `det^{+1}` vs boson
   `det^{−1/2}`), **never** the doublet mode-*count* (det_C vs det_R). P1 is silent on the count. The
   "fermion = 1 factor, boson = 2 factors" asymmetry is a Pfaffian-vs-unrooted-det normalization artifact
   (`Pf(aJ)=a` vs un-rooted `det(sI)=s²`); on equal footing `log|Z|` both are single-power (verified R2-3).
2. **Berezin gives a determinant-product, not a block-total.** Integrating the matter field gives
   `Z=det(H)` = three **real** eigenvalue factors `(a+2Re b)(a−Re b ± √3 Im b)` = (1 singlet)(2 doublet),
   a *function* of `(a,b)` — it never integrates *over* `b` to set `r` (verified R2-1). This
   determinant-PRODUCT functional is structurally distinct from the Frobenius **block-total** functional
   (`E_singlet=3a²`, `E_doublet=6|b|²`) whose equal-block point gives `r=1/2`.
3. **C₃ admits both invariant bilinears** (verified R2-2): the symmetric `I` (det_R) *and* the
   antisymmetric `J=C−C²` (det_C) both satisfy `CᵀXC=X`. So pairing the two real doublet modes into one
   complex mode (choosing `A∝J` = det_C) is an **unforced extra posit** — and that `J` is exactly the
   `U(1)_b` complex structure round 1 proved **measure-neutral** and `C³=I` forbids as a continuous
   rephasing. **The fermionic frame is the same static J in a Berezin costume — it does not move the wall.**

(Index equivocation also noted: the retained Berezin/forcing notes are *site*-indexed — per-site Fock
occupation dim 2 — and silent on the *generation* reality structure; the 2=2 match is coincidental.)

## The wall now — Dirac vs Majorana (round 3)
Three rounds converge cleanly: **det_C/r=1/2/Q=2/3 ⟺ a DIRAC (complex / antisymmetric-J-paired) reality
structure on the generation doublet; det_R/r=1/Q=1 ⟺ MAJORANA (real).** The question is now sharp and
clean: *can A1+A2+emergent-spacetime force a Dirac over a Majorana reality structure on the
generation-doublet field?* — separated cleanly from the per-site Fock index (silent on it). A physically
suggestive lever for round 3: **charged leptons ARE Dirac** (e⁻ ≠ e⁺, tied to electric charge), while
neutrinos may be Majorana — so the Dirac-vs-Majorana split may also *predict the lane assignment*
(charged → Dirac → Q=2/3; neutral → Majorana → other r), which had been open.

## Provenance (verified 2026-06-02)
- Power-vs-count, Berezin determinant-product, C₃ both-bilinears: verified directly (runner 4/4).
- Anchors: `spin_statistics_berezin_determinant` (retained_bounded), `staggered_dirac_substep1_grassmann_forcing_bridge` (retained_bounded), `koide_kappa_block_total_frobenius` (retained). Round-1 U(1)_b measure-neutrality carried forward.
- Established det_C→r=1/2 / det_R→r=1 mapping kept (a synth label-slip on "one-complex-mode" not propagated).
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
