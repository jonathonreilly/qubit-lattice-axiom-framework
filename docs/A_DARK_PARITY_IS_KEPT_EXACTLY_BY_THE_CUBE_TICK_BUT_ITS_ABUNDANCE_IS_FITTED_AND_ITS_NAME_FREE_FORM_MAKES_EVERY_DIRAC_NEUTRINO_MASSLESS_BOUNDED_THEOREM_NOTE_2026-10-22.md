---
claim_id: a_dark_parity_is_kept_exactly_by_the_cube_tick_but_its_abundance_is_fitted_and_its_name_free_form_makes_every_dirac_neutrino_massless_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "Tests the candidate rule AX-5 (dark parity): one link-free species D is odd, and every term of the update other than the tick holds an even number of D modes. Exact checks on CL-1's tick (anticommuting face-phase -1 hops, copy sign, copy mass, both tilings): the copy sign s commutes with the tick at K = 0 only (5e-16; 0.235 at a random K), and the one-cube traceless strain vertex takes the heavy copy at rest to the light copy at recoil 0.87 M with amplitude 0.30 (M = 0.5) and 0.36 (M = 0.05), so no copy parity that equals s at rest survives CL-1's edge reading. On a real-space 4^3 torus with a random metric per cube and random links on a second species E, the update commutes exactly with the D projector, and D's block does not depend on E's links. In Fock space (4 + 4 modes, dim 256) the tick keeps (-1)^N_D, a one-D-mode term breaks it, and a pair term keeps it. The lightest D-odd state is D's light copy at rest (phase mu_D, 8^3 grid). With D taken as one family's nu^c, the Dirac neutrino matrix has rank 2. In the name-free form, where every zero-charge mode enters only in pairs, it has rank 0. The anti-smuggling gate FAILS: the abundance is fitted, the one-family form names nu^c, and the name-free form makes every neutrino massless under Z4, which the measured splittings contradict. Supplied model, finite diagnostic: (b, mu, M), the metric weights, the link phases, the charge table, the unit map, the graviton-exchange rate coefficient, g*, A_s, r, the measured Omega h^2 and the neutrino splittings."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/a_dark_parity_is_kept_exactly_by_the_cube_tick_but_its_abundance_is_fitted_and_its_name_free_form_makes_every_dirac_neutrino_massless_2026_10_22.py
---

# A dark parity is kept exactly by the cube tick, but its abundance is fitted and its name-free form makes every Dirac neutrino massless

Claim type: bounded_theorem.
Primary runner: `scripts/a_dark_parity_is_kept_exactly_by_the_cube_tick_but_its_abundance_is_fitted_and_its_name_free_form_makes_every_dirac_neutrino_massless_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight.

The register says what a dark-matter law must give: a stable, cold, link-free species whose abundance the rules set. Three earlier probes found no such species in CL-1 to CL-3:
- the copy-sign note (PR #9963): the copy sign is exact only at rest;
- the mirror note (PR #9988): a gapped mirror keeps only a number it shares with light matter;
- the fold-defect note (PR #9991): fold defects are not topological.

All three end the same way: a stable species would need a conserved number that the laws do not contain. This note writes the smallest rule that supplies one and tests it against CL-1 and against measurement. It also runs the owner's anti-smuggling gate (2026-10-22), and the rule fails that gate.

## Candidate rule (AX-5, tested and NOT adopted)

> "Dark parity. One species, D, has zero charge in every link factor and is odd; every other mode is even. Every term of the update other than the tick, which moves each species' odds only within that species, holds an even number of D modes."

- Bends: Admissibility. The rule narrows the admissible local terms: an admissible nearest-neighbour term that is odd in D is excluded. It also uses AX-2's role layout for D's sites.
- Owner decision 2, "a hand-added parity for dark matter", is exactly this rule.

## Why not the copy parity or the label parity

Option (i), the copy parity, fails on CL-1's own terms:
- A1: the copy sign s commutes with the tick at K = 0 (5e-16), where the s = -1 copy has rest phase mu + M. At a random K it does not (0.235).
- A2: CL-1's edge reading is the strain vertex. It takes the heavy copy at rest to the light copy at recoil 0.87 M with amplitude 0.30 at M = 0.5 and 0.36 at M = 0.05. It is zero at q = 0.
- Consequence: any parity that equals s at rest and follows the bands by continuity is broken at O(1) by gravity itself. To make (i) exact, one species would have to read its edges through a band-projected tick, which is a non-local reading.

Option (ii), the label parity N', is not kept by the fine tick. This is cited from dm-revisit, PR #9946, and not recomputed.

Option (iii) is AX-5, a parity on species number. Every CL-1 term acts within one species, so the tick keeps this parity exactly.

## Statement

B. Consistency with the update.

1. B1. Take a real-space 4^3 torus with both tilings, the copy mass, an independent random diagonal metric on every cube (edges that vary in space) and random link phases on E's odd hops. The update is unitary (9e-16) and commutes with the D projector exactly. D's block does not depend on E's links.
2. B2. In Fock space with 4 D modes and 4 E modes (dimension 256):
   - the second-quantised tick keeps (-1)^N_D exactly;
   - a term with one D mode, such as L H nu^c_D, breaks it (norm 2.0);
   - a D pair term keeps the parity while changing N_D.
3. Further structural facts:
   - the copy mass, the dressing V^q (q = 0 for D) and the edge control are one-body operators within each species;
   - the split's passing sends each corner mode to that corner of the children, within the same species;
   - CL-2's records never condition the odds;
   - CL-3 moves only edges and links.
   So, as the rule text stands, P_D is exact under the update. The full passing was not simulated.

C. Consequences.

1. C1. On an 8^3 grid, D's lowest positive quasienergy is mu_D, at K = 0. The lightest D-odd state is therefore D's light copy at rest, with mass m_D = mu_D/N, and it is absolutely stable. The s = -1 copy of D sits at mu_D + M and may decay to the light copy through gravitons (vertex A2), since both copies are odd.
2. C2. D has Gauss charge zero, so it carries no dressing and no link coupling. Its rest phase is exactly mu_D.
3. C3. In one family, nu^c is the only link-free Weyl state. Its Majorana term is odd under Z4 = i^(B-L). L H nu^c is Z4-even but odd under the dark parity.
4. C4 (one-family form, D = nu^c_1). The Dirac neutrino matrix y_ij L_i H nu^c_j loses a column and has rank 2, so the lightest neutrino is exactly massless. Then:
   - sum m_nu = 58.7 meV (normal ordering) or 99.2 meV (inverted);
   - DESI DR2 + CMB (< ~64 meV) keeps only the normal ordering;
   - m_bb = 0.
5. C5 (name-free form, the gate's requirement). "Every mode with zero charge in every link factor enters non-tick terms only in pairs" removes all three nu^c columns, and L L H H is Z4-odd. Every neutrino is then massless, which the measured Delta m^2_21 = 7.4e-5 eV^2 contradicts.

## Estimates against measurement

Supplied inputs:
- alpha_1/2 = 1.1e-3, the graviton-exchange rate coefficient (literature, approximate);
- g* = 106.75;
- A_s = 2.1e-9;
- r;
- Omega_c h^2 = 0.12.

Results:
- E1, abundance. Gravitational freeze-in from the bath gives Omega h^2 = 0.12 on the line m_D T_RH^3 = const. It needs T_RH >= 9.5e12 GeV. At instant reheating:
  - m_D = 1.4e4 GeV at T_RH = 5.8e15 GeV (r = 0.036);
  - m_D = 2.1e8 GeV at T_RH = 2.4e14 GeV (r = 1e-7, the fold-plateau range).
- E2, sensitivity. On the light branch d ln Omega/d ln m_D = 1.00 and d ln Omega/d ln T_RH = 3.00. A heavy branch at m_D ~ 7 T_RH has d ln Omega/d ln T_RH = 17.
  - The fitted number is the combination m_D T_RH^3: m_D is supplied, and T_RH is supplied by the reheating sector.
  - At a cell-scale m_D, or for D's s = -1 copy at M ~ 1e18 GeV, production is Boltzmann-absent.
- E3, coldness. v0 ~ 2e-17 c at m_D = 1e4 GeV, far below what Lyman-alpha requires.
- E4, self-interaction. It is gravitational only: sigma/m ~ 1e-60 to 1e-46 cm^2/g, against a bound of about 1 cm^2/g.
- E5, direct detection. Gravity only: alpha_G ~ 9e-35, about 5e-45 events per tonne-year. Indirect detection is likewise negligible.
- Delta N_eff ~ 0.
- Misalignment does not apply to a fermion. The exact split passing carries vacuum to vacuum; the reheating-into-misfolds route is supplied.

## Anti-smuggling gate (owner 2026-10-22): FAIL

1. Measured numbers chosen: the abundance is FITTED (m_D T_RH^3 is tuned to 0.12), and m_D itself is supplied.
2. Observed structure inserted by name: the one-family form names nu^c and one family, a lopsided choice whose only reason is the data. The name-free form, stated purely in charge and term terms, is falsified by neutrino oscillations under Z4 (C5).
3. Prediction it was not built for: only in the one-family form, m_lightest = 0 and sum m_nu = 58.7 meV. That form fails item 2. Darkness, zero direct-detection signal and stability are built in.
4. Axiom bent: Admissibility (term selection).

Result: FAIL. The rule is not adopted and not logged as AX-5. Owner decision 2 stays open.

## Boundary

Not claimed:
- a dark-matter law;
- that the passing, with a heating kernel, conserves N_D (argued by species-wise structure, not simulated);
- inflaton-scattering or end-of-inflation gravitational production, which add to the same fitted line;
- the Z4-broken reading, in which Majorana nu^c and L L H H are allowed, the name-free form survives with all three nu^c dark, and m_D and the abundance are still supplied (not tested).

Option (i) would need a non-local, band-projected edge reading; it was not built.

## Supplied vs forced

Supplied: (b, mu, M), the metric weights, the link phases, the charge table, the choice of D, m_D, T_RH, alpha_1/2, g*, A_s, r, Omega h^2 and the neutrino splittings.

Forced, given these:
- s is exact only at rest, and the edge reading mixes copies at O(1);
- P_D is exact under every CL-1 term;
- the lightest odd state is D's light copy at rest, and the heavy copy decays to it;
- zero link couplings;
- the rank of the neutrino Dirac matrix in each form;
- the scaling law Omega ~ m_D T_RH^3.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md): unchanged.
- [Candidate-law register](CANDIDATE_LAWS.md): CL-1's tick, copy sign, copy mass, links, edges and passing. Zero premise weight; results that use it are conditional on it.
- Companion results:
  - PR #9963, copy sign (vertex recomputed);
  - PR #9946, label parity (cited);
  - PR #9988, mirror;
  - PR #9991, fold defects;
  - PR #9877, the link-free slot.

## How to run

```
python3 scripts/a_dark_parity_is_kept_exactly_by_the_cube_tick_but_its_abundance_is_fitted_and_its_name_free_form_makes_every_dirac_neutrino_massless_2026_10_22.py
```

Needs numpy and scipy. The runner is self-contained, seeded and declares `AUDIT_TIMEOUT_SEC = 120`. It runs in about 1 s with about 100 MB resident and prints about 4.5 kB. It ends with `TOTAL: PASS=14 FAIL=0`.
