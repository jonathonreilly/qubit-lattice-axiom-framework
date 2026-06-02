# Flavor — which-vacuum dynamics: r=1/2 (Q=2/3) is the UNSTABLE SEPARATRIX of the emergent records flow `r→2r²`. The balanced lane is a saddle between the Q=1/3 (degenerate) and Q=1 (hierarchy) collapse basins — it needs a stabilizer.

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** positive dynamical characterization (a verified flow + its fixed-point structure) + an honest "not-an-attractor" verdict.
**Runner:** `scripts/flavor_r_half_is_the_records_flow_separatrix_2026_06_02.py` (SCORECARD 4/4).
**Source:** workflow `wf_f433eb9d` — 5 routes + verification + synthesis.

## The question
Under the lane reframe (r=1/2 is the *balanced extremum*, not a forced value), does an emergent
records/persistence or mass-generation **dynamics drop the charged-lepton sector onto r=1/2** as a
*vacuum*? I.e. is the balanced lane a dynamical **attractor**?

## Verdict: no — r=1/2 is the unstable SEPARATRIX of the emergent flow (a saddle, not an attractor)
The records/decoherence dynamics on the C₃ generation sector has a clean, verified form:

- **The emergent Lüders/records sharpening flow is exactly `r → 2r²`** (verified): sharpening
  `p→p²/Z` on the 2-sector power distribution `p_singlet=1/(1+2r)`, `p_doublet=2r/(1+2r)` reduces
  precisely to `r↦2r²` (grounded in the retained_bounded `luders_rule_from_composition_consistency`).
- **Fixed-point structure:** `r=0` (`f'=0`, **stable** — singlet-collapse, **Q=1/3 degenerate**) and
  `r=1/2` (`f'=2`, **unstable separatrix**, **Q=2/3**); `r>1/2` runs away to doublet-collapse
  (**Q→1 hierarchy**). So **r=1/2 is the repelling watershed** between the degenerate basin and the
  hierarchy basin.
- **Entropy functionals:** the **2-sector** Shannon entropy `S2(r)` peaks at `r=1/2` (a stable max);
  the **3-real-DOF** entropy `S3(r)` peaks at `r=1`. Only **2-sector** thermalization lands on r=1/2 —
  and the 2-sector partition *is* the unforced det_C/(1,1) block-count (the C³=I-forbidden U(1)_b/SO(2)
  doublet quotient would be needed to make it an emergent partition).
- **Mass-generation** energetics (NJL → r=4; Coleman–Weinberg over the 3 eigenvalue DOF → dimension
  (1,2) → r=1) flow to endpoints, not r=1/2.

So **r=1/2 is a stable max only of the (unforced) 2-sector functional, and an unstable
saddle/separatrix of every genuinely emergent flow.** The natural attractors are `r=0` (degenerate)
and `r=1` (hierarchy) — *the other two lanes*. The lane-assignment dynamics does **not** drop charged
leptons on r=1/2 as a vacuum; the balanced lane needs a **stabilizer**.

**Ledger correction (honesty):** the only measures landing on r=1/2 (`bae_max_entropy`, `bae_f1_f3`,
`koide_real_rep_block_count`) are **unaudited** on origin/main; the *retained* pieces all point away —
`luders_rule_from_composition_consistency` (retained_bounded, the `r→2r²` flow), `frobenius_isotype_split`
(retained_no_go, declines to rank (1,1) vs (1,2)), the primitive trace-degeneracy (retained_no_go).

## The physical reframe this buys (genuinely new)
The famous **Koide precision** — `Q=2/3` to ~10⁻⁵ — now has a sharp dynamical interpretation: the
charged-lepton sector sits **exactly on the decoherence-flow separatrix**. A system on a separatrix to
10⁻⁵ is a knife-edge: it is either **stabilized** (some mechanism pins the 2-sector partition as the
physical decoherence basis) or a **tuned/transient** initial condition. This is a falsifiable physical
statement and reframes the open problem precisely.

## Net standing & the next path (not closing)
- The three lanes are: two **stable collapse basins** (`r=0` Q=1/3 degenerate; `r=1` Q=1 hierarchy) +
  the **unstable separatrix** between them (`r=1/2` Q=2/3, the charged-lepton balanced lane).
- The charged-lepton value is therefore a **separatrix occupancy** that requires a **stabilizer** — and
  that stabilizer is exactly the "select the 2-sector (isotype) partition" pin the J-hunt isolated
  (the det_C / center-state choice), now in dynamical language.
- **Next:** does **einselection** — a pointer basis from the *commutant of the C₃-invariant interaction
  Hamiltonian* (predictability sieve) — single out the **2 isotype sectors** as the stable record basis
  non-circularly? If the actual emergent coupling decoheres into the singlet/doublet split (rather than
  the 3 eigenmodes), the 2-sector partition becomes the physical coarse-graining and the separatrix is
  stabilized. This is the sharply-posed open object.

## Provenance (verified 2026-06-02)
- `r→2r²` Lüders map, fixed-point stability (r=0 stable, r=1/2 unstable separatrix), S2 peak at 1/2 / S3 peak at 1: verified directly (runner 4/4).
- Anchors: `luders_rule_from_composition_consistency` (retained_bounded), `frobenius_isotype_split_uniqueness` (retained_no_go), `primitive_p_bae_m1` trace-degeneracy (retained_no_go). The r=1/2 measures (`bae_max_entropy` etc.) are **unaudited** — flagged, not load-bearing.
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
