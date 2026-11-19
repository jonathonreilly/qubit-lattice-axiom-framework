---
claim_id: graviton_mass_and_floor_margins_bound_the_edge_register_step_count_below_and_exclude_the_edge_dimension_lambda_rule_bounded_theorem_note_2026-10-22
claim_type: bounded_theorem
claim_scope: "For the update law's edge registers (length = flat length x 2^(n/s - 3), n = 0 .. (4 + Delta)s, window [L/8, 2^(1+Delta) L], children born at the flat length, split at twice it), with a block edge's absolute zero-point spread s1 L independent of its length and block size: (pinning, exact numerics) integer register values give E0(f) = E - A cos 2 pi f with k_pin/k ~ sigma_n^3 exp(-16 sigma_n^2) (tridiagonal ground states, fitted slope 15.96, WKB 16); (wall, exact) a hard wall t zero-point spreads away shifts the ground energy by t e^(-t^2/2)/sqrt(2 pi) (D_nu(-t) = 0, ratio 0.97 at t = 6); (region) requiring both the pinning mass and the wall mass below the LIGO graviton-mass bound, with the floor at 1/8 of the flat length, gives s >= 2 ln2 sigma_pin t_wall / d, d the floor distance in flat units, in which s1 and the block size b_e cancel: s >= 135 in weak fields, 278 to 363 in a J0740+6620 core, 1027 in the causal maximum-mass core; the moving bound 0.85/sin eps0 (>= 32.7 at the heating cap) is weaker; the top-wall margin is Delta >= log2(1 + d/2) < 1, so s cancels from it and Delta >= 1 satisfies it; nothing bounds s above except the site budget at a free b_e, so s is bounded below, not fixed. The edge-dimension rule Lambda L^2 = 2^-(4+Delta)s needs s = 398.9/(4+Delta) <= 80 for Delta >= 1, outside the region; at the smallest allowed s it gives Lambda L^2 <= 1e-203 (Delta = 1), 83 decades below the measured 7.15e-121. Under the response law's vacuum standard a vacuum-share 1/dimension term cancels exactly. Supplied model, estimates against measurement: m_g < 1.3e-23 eV, hbar c/L in two unit readings, the floor 1/8, alpha_c for J0740+6620 and the causal limit, the eps0 cap, Delta >= 1, the harmonic register and wall models; Lambda is used only in the rule test."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/graviton_mass_and_floor_margins_bound_the_edge_register_step_count_below_and_exclude_the_edge_dimension_lambda_rule_2026_10_22.py
---

# Graviton-mass and floor margins bound the edge register's step count below and exclude the edge-dimension Lambda rule

Claim type: bounded_theorem.
Primary runner: `scripts/graviton_mass_and_floor_margins_bound_the_edge_register_step_count_below_and_exclude_the_edge_dimension_lambda_rule_2026_10_22.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its update law (CL-1) places a quantum edge register on each edge of the block triangulation (b_e cells to an edge), with (4 + Delta)s fermion-mode sites at each end; the edge length is the flat length times 2^(n/s - 3), so each step changes the log-length by ln2/s. The register lists s and Delta as supplied. A sibling note (PR #9962) found that the rule "Lambda per proper 4-volume = 2^-(4+Delta)s in rung units" hits the measured Lambda L^2 = 7.15e-121 at s = 99.8, 79.8, 66.5 or 57.0 for Delta = 0 to 3, but only as a fit of s. This note asks whether other measured constraints fix s and Delta without Lambda, and then tests the rule against the result. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) fix none of the inputs used here.

Units: rung units, L the flat cell rung, 8 pi G hbar = L^2, c = 1. Measured inputs: the LIGO graviton-mass bound m_g < 1.3e-23 eV, so m_g L < 5.3e-51 (L the rung) or 2.7e-51 (L the site spacing; both unit readings are carried); the heaviest measured neutron star J0740+6620, with central lapse ratio alpha_c = 0.45 to 0.55.

## Statement

A. Pinning by the value lattice.

1. A register with a quadratic phase (k/2)(n - f)^2 on integer values n has ground energy E0(f) = E - A cos 2 pi f. In the edge-momentum picture A is the tunnelling amplitude around the theta circle (Mathieu q = 8t/k, sigma_n^2 = sqrt(t/(2k))), so k_pin/k ~ sigma_n^3 exp(-16 sigma_n^2). Exact tridiagonal ground states give a slope of 15.96.
2. The pinning stiffness gives the long-wavelength edge field a mass m a = sqrt(k_pin/k). The graviton-mass bound then needs every register's zero-point spread to be at least sigma_pin = 3.88 steps (3.90 under the other unit reading). This reproduces hop-recheck D3 (3.79 without the prefactor).

B. Wall margin.

3. A hard wall t zero-point spreads from an oscillator mode shifts its ground energy by nu(t) = t e^(-t^2/2)/sqrt(2 pi) for large t. This is exact through D_nu(-t) = 0: the ratio is 0.87, 0.93, 0.96 and 0.97 at t = 3 to 6.
4. The wall is an edge-local potential whose curvature over the mode stiffness is 2 nu''(t). Its mass stays below the graviton-mass bound only if t >= t_wall = 21.9 (22.0). This reproduces edge-block B2's 22 spreads from a simpler model.

C. The allowed (s, Delta) region.

5. A block edge's absolute zero-point spread is s1 L at every length and block size (edge-block B0; s1 = 0.2 or 0.4 depending on the unit reading). At length l a step is l ln2/s, so sigma_n = s1 s L/(l ln2). The sparsest values of the cosmic cycle are at the split (l = 2 b_e L), so pinning needs s >= 2 ln2 sigma_pin b_e/s1. The floor margin needs d b_e >= t_wall s1, where d is the floor distance in flat units: 7/8 for a child born at the flat length, and alpha_c - 1/8 for a static core at the worst far phase. Together:

   s >= 2 ln2 sigma_pin t_wall / d.

   The unknown s1 and the block size cancel. This is a theorem given items 2 and 4, and it holds in either unit reading.
6. Values: s >= 135 in weak fields, 278 to 363 in a J0740+6620 core, and 1027 in the core of the causal maximum-mass star (alpha_c = 0.240), whose floor margin the register's floor placement intends to keep. The moving bound s >= 0.85/sin eps0 (32.7 at the heating cap eps0 < 0.026) is weaker. The split trigger (mean value 4s) and the birth value 3s are integers for every s, so they add no constraint.
7. Top margin (gap H5). The margin "Delta s steps >= 22 spreads" reads Delta >= log2(1 + t_wall s1/(2 b_e)). At the floor-limited b_e this is log2(1 + d/2): 0.52 in weak fields and 0.22 in a J0740+6620 core. s cancels, and Delta >= 1 (needed for the post-crunch exterior), or Delta >= 2 with the trapped-shift cure, already satisfies it.
8. Strong-field variant (estimate). Radially stretched exterior edges reach 2^(1+Delta) b_e L. Keeping them unpinned there too multiplies the bound by 2^Delta: s >= 270, 540 and 1080 for Delta = 1, 2 and 3.
9. No upper bound. The site budget 12(4 + Delta)s/b_e^3 <= 0.8 per cell (block-hierarchy) bounds s above only at a given b_e, and b_e is free above. At the pinning-limited s this gives b_e >= 45 and s >= 1210 for s1 = 0.2, or b_e >= 32 and s >= 428 for s1 = 0.4 (Delta = 1). So s is bounded below, not fixed.
10. Gravitational-wave dispersion and Lorentz-violation smoothness give no further bound. With dressed weights and sigma_n >= sigma_pin, the value lattice reaches dispersion only through the pinning mass of item 2 and through lattice terms (k b_e L)^2, which are 5e-77 at LIGO frequencies. Uniform dilations are exact whole shifts. Collinear-shift deficits (sigma_n ln2/s)^2 = (s1/(2 b_e))^2 do not depend on s.

D. The edge-dimension rule.

11. Lambda L^2 = 2^-(4+Delta)s needs s = 398.9/(4 + Delta): 79.8, 66.5 and 57.0 for Delta = 1, 2 and 3. All lie below the weak-field bound of item 6, so the hits of PR #9962 sit outside the allowed region.
12. At the smallest allowed s the rule gives Lambda L^2 <= 1e-203 (Delta = 1, weak fields), 83 decades below the measured value; with J0740+6620 (s >= 278) it gives <= 1e-418. This is a miss, not a prediction.
13. Look-elsewhere. A rule 2^-cs with another bit count c fits at s = 398.9/c whenever c <= 398.9/s_min, with chance 1, because s is only bounded below. c = 3 (the states between the floor and the birth value) lands at 133, at the weak-field bound. This is a logarithmic coincidence: to leading order s_min = sqrt2 ln2 ln(1/(m_g L))/d, and the graviton-mass bound and Lambda are both near-Hubble scales. J0740+6620 excludes c = 3. c = 1 (one octave, s = 399) survives J0740+6620 but not the causal maximum-mass core. None of these is a derivation.

E. Law-level justification of a 1/dimension phase.

14. Uniform odds give every configuration of an end the weight 2^-N. But the response law answers only departures from the vacuum of the same edges, so a vacuum-share term of that size cancels exactly: it is zero in the vacuum and nonzero only on departures (N = 8 check). Any Lambda equal to a vacuum expectation of register operators is subtracted; Lambda can enter only as the supplied constant CL-3 already carries.
15. The length reads only n, which takes N + 1 values (with C(N, n) configurations each, summing to 2^N), so a normalisation over readable values would give 1/(N + 1), about 1e-3. The CL text fixes none of these choices: per end (N bits), per register (2N) or per block site (12N); per cell 4-volume or per block 4-volume (b_e^4, 21 bits at b_e = 40). So "one end per cell 4-volume" is a choice, not a law.

## Candidate law tested (not adopted)

> "Edge-register dimension. Lambda per proper 4-volume is 2^-(4+Delta)s in rung units."

Result: excluded. The graviton-mass bound and the floor margin put s >= 135 independently of the spread normalisation and block size, and the rule needs s <= 80 for Delta >= 1.

## Rule proposal (from item 5; offered for the register, not adopted)

Replace "the edge register size s" in the supplied list by the derived bound: s >= 2 ln2 sigma_pin t_wall / d_min, with sigma_pin and t_wall read from the graviton-mass bound and d_min the smallest floor distance the register must hold (7/8 for the vacuum, alpha_c - 1/8 for the stars it must support). The supplied list then holds a lower bound tied to measurement, not a free number, and the "23 to 113" range quoted for s (the moving bound alone) should be read as superseded: block edges need s in the hundreds or more.

## Derivation

Item 1: tridiagonal H = -t sum(|n><n+1| + h.c.) + (1/2)(n - f)^2 on n in [-70, 70]; A = (E0(1/2) - E0(0))/2, k_pin = (2 pi)^2 A, fitted as ln(k_pin) - 1.5 ln(sigma_n^2) against sigma_n^2 over sigma_n = 0.69 to 1.10. The WKB slope comes from the Mathieu bandwidth e^(-4 sqrt q) with q = 8t/k. Item 3: brentq root of scipy's pbdv. Items 2 and 4: brentq on m a against m_g L. Items 5 to 9: closed forms. Item 14: an exact 8-mode vector check.

## Finite checks

The runner gives 15 PASS and 0 FAIL. Exact or theorem checks: A1, B1, C1, C3, D1, E1. Estimates: A2, B2, C2, C4 to C6, D2, D3, E2. Two runs gave identical output.

## Boundary

Not claimed: a value of s; any upper bound on s; that no Lambda rule built on edge registers exists. The pinning and wall masses are single-mode harmonic estimates. The prefactors move sigma_pin and t_wall by a few percent, and the conclusion needs sigma_pin t_wall to be about 40% lower than computed, which would mean a graviton-mass bound weaker by about 1e21 in mass. If the phase minimum could always sit on the value lattice (no pinning), only the moving bound would remain and the rule's s = 66 to 80 would be allowed again; no law places it there. The zero-point spread's independence of length (edge-block B0) is a finite diagnostic. The causal maximum-mass bound applies only if the register must support such stars.

## Supplied vs forced

Supplied: m_g < 1.3e-23 eV, hbar c/L (two readings), the floor 1/8, alpha_c (J0740+6620, causal limit), the eps0 cap 0.026, Delta >= 1 (>= 2 with the cure), the harmonic register and wall models, the budget 0.8 per cell, and Lambda (part D only). Forced, given those: the s1- and b_e-free lower bound on s, the s-independence of the top margin, the absence of an upper bound, and the exact cancellation of any vacuum-share 1/dimension term.

## Dependencies

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md).
- [Candidate-law register](CANDIDATE_LAWS.md): the Edges clause (window, log spacing, (4 + Delta)s sites per end), the response law's vacuum standard, and the window and floor-placement items. Zero premise weight.
- Builds on campaign probes edge-block (B0, B2, D1), hop-recheck (B2, D3) and unit-map (readings A and B); PR #9953 (block-hierarchy budget); PR #9936 (window-fix, alpha_c); the post-crunch probe (Delta >= 1, >= 2 with the cure); PR #9962 (lambda-size-rule, the rule tested); PR #9947 (lambda-quantum). It narrows the register's "s exceeds ~0.85/sin eps0 (23 to 113)" to a lower bound for block edges.

## How to run

```
python3 scripts/graviton_mass_and_floor_margins_bound_the_edge_register_step_count_below_and_exclude_the_edge_dimension_lambda_rule_2026_10_22.py
```

Needs numpy and scipy. Self-contained, declares `AUDIT_TIMEOUT_SEC = 120`, runs in about 1 s at about 80 MB resident, prints about 5.5 kB and ends with `TOTAL: PASS=15 FAIL=0`.
