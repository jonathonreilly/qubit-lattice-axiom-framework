# Flavor — stipulated records map: `r=1/2` is the unstable separatrix of `r→2r²`.

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** bounded map theorem. The source verifies the supplied Lüders/records sharpening map
`r→2r²`, its fixed-point structure, and the 2-sector vs 3-real-DOF entropy comparison. It does **not**
derive that this map is the physical emergent charged-lepton records flow.
**Runner:** `scripts/flavor_r_half_is_the_records_flow_separatrix_2026_06_02.py` (SCORECARD 4/4).
**Source:** workflow `wf_f433eb9d` — 5 routes + verification + synthesis.

## The question
Under the lane reframe (`r=1/2` is the *balanced extremum*, not a forced value), does the supplied
records/Lüders sharpening map make the balanced lane a dynamical **attractor**?

## Verdict: no — r=1/2 is the unstable separatrix of the supplied map
The stipulated records/Lüders sharpening update on the C₃ generation sector has a clean, verified form:

- **The Lüders/records sharpening map is exactly `r → 2r²`** (verified): sharpening
  `p→p²/Z` on the 2-sector power distribution `p_singlet=1/(1+2r)`, `p_doublet=2r/(1+2r)` reduces
  precisely to `r↦2r²` (grounded in the retained_bounded `luders_rule_from_composition_consistency`).
- **Fixed-point structure:** `r=0` (`f'=0`, **stable** — singlet-collapse, **Q=1/3 degenerate**) and
  `r=1/2` (`f'=2`, **unstable separatrix**, **Q=2/3**). For `r>1/2`, the coordinate runs away
  (`r_n→∞`), which is the projective doublet-collapse end (`p_doublet→1`). Finite `r=1` is **not** a
  fixed point of this map; it is a separate hierarchy/Plancherel comparator.
- **Entropy functionals:** the **2-sector** Shannon entropy `S2(r)` peaks at `r=1/2` (a stable max);
  the **3-real-DOF** entropy `S3(r)` peaks at `r=1`. Only a 2-sector entropy functional selects
  `r=1/2`, and the 2-sector partition *is* the unforced det_C/(1,1) block-count (the C³=I-forbidden U(1)_b/SO(2)
  doublet quotient would be needed to make it an emergent partition).
- **Contextual route notes, not load-bearing here:** mass-generation energetics heuristics such as
  NJL → `r=4` or Coleman-Weinberg over the 3 eigenvalue DOF → dimension `(1,2)` do not provide a
  verified attraction to `r=1/2` in this packet.

So `r=1/2` is a stable max only of the unforced 2-sector entropy functional, and an unstable
separatrix of the supplied Lüders map. The map theorem alone does **not** drop charged leptons onto
`r=1/2` as a vacuum; a physical use would still need a stabilizer or a derivation of the relevant
2-sector partition/record basis.

**Ledger correction (honesty):** the only measures landing on r=1/2 (`bae_max_entropy`, `bae_f1_f3`,
`koide_real_rep_block_count`) are **unaudited** on origin/main; the *retained* pieces all point away —
`luders_rule_from_composition_consistency` (retained_bounded, the `r→2r²` flow), `frobenius_isotype_split`
(retained_no_go, declines to rank (1,1) vs (1,2)), the primitive trace-degeneracy (retained_no_go).

## The conditional physical reframe this buys
The famous **Koide precision** — `Q=2/3` to ~10⁻⁵ — now has a sharp dynamical interpretation: the
charged-lepton sector, if modeled by this records map, lies on its separatrix. A system on that
separatrix to 10⁻⁵ is a knife-edge: it is either **stabilized** (some mechanism pins the 2-sector
partition as the physical record basis), or **durably stationary** (a durability principle requiring
only fixedness under re-registration — no attraction needed; the separatrix instability then makes the
*exact* value the only persistent one — alternative added 2026-06-11, examined in
`KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`), or a
**tuned/transient** initial condition. This reframes the
open problem without closing the physical records-flow identification.

## Net standing & the next path (not closing)
- For the supplied map, the finite fixed points are `r=0` and `r=1/2`; `r=1/2` is the unstable
  separatrix, and `r>1/2` runs toward the projective doublet-collapse end (`r→∞` in this coordinate).
- The charged-lepton value, if governed by this map, would therefore be a **separatrix occupancy** that requires a **stabilizer** — and
  that stabilizer is exactly the "select the 2-sector (isotype) partition" pin the J-hunt isolated
  (the det_C / center-state choice), now in dynamical language. *(Scope correction 2026-06-11: a
  stabilizer is one sufficient mechanism, not a necessary one — fixedness under a durability
  principle also yields persistence of the exact separatrix value without any attraction; the
  original wording over-demanded attraction.)*
- **Next:** does **einselection** — a pointer basis from the *commutant of the C₃-invariant interaction
  Hamiltonian* (predictability sieve) — single out the **2 isotype sectors** as the stable record basis
  non-circularly? If an actual emergent coupling decoheres into the singlet/doublet split (rather than
  the 3 eigenmodes), the 2-sector partition could become the physical coarse-graining and the separatrix
  could be stabilized. This is the sharply-posed open object.

## Provenance (verified 2026-06-02)
- `r→2r²` Lüders map, fixed-point stability (r=0 stable, r=1/2 unstable separatrix), S2 peak at 1/2 / S3 peak at 1: verified directly (runner 4/4).
- Anchors: `luders_rule_from_composition_consistency` (retained_bounded), `frobenius_isotype_split_uniqueness` (retained_no_go), `primitive_p_bae_m1` trace-degeneracy (retained_no_go). The r=1/2 measures (`bae_max_entropy` etc.) are **unaudited** — flagged, not load-bearing.
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
