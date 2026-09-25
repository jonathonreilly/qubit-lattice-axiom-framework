---
claim_id: ring_model_in_a_region_bounded_by_records_the_energy_only_photon_bound_matches_the_torus_and_the_records_reduce_only_the_response_amplitude_bounded_theorem_note_2026-09-25
claim_type: bounded_theorem
claim_scope: "Supplied link-qubit ice model with the exact vertex Gauss law and the ring clause -g (U + U^dag) at V = 0, g = 1, in the unrecorded interior {1..m}^3 of an (m+2)^3 cell whose other links carry records (the landed two-regulator construction), m = 8 with uniform-ice and canonical records and m = 12 with uniform-ice records; the compiled projector of open PR 9236 with per-plaquette ring couplings (480 walkers, projection 30, two to four seeds). Probe: the standing-wave triple W = sum_a sum_{a-links} sin(pi n x_b/(m+1)) sigma, b = a + 1 mod 3. Exact: E(h) = E_0 - h <W> - h^2 m_-1 + O(h^3), so the symmetric combinations of E(+-h), E(+-2h) give m_-1 = sum_n |<n|W|0>|^2/(E_n - E_0); the first moment m_1 = (1/2) <[W,[H,W]]> = (1/2) sum_p c_p <R_p>, c_p = 4 (sum_{l in p} w_l sign_l)^2, equals minus half the derivative of the ground energy in ring couplings 1 + eps c_p (Hellmann-Feynman); the moment chain gives omega_min <= (m_1/m_-1)^(1/2). On an exact 3646-state 3^3 region the first moment from Hellmann-Feynman equals the double commutator to 1e-8, the chain holds, and the projector reproduces m_-1 and m_1 within 1.3 standard errors. Finite estimates: at the smallest standing wave the energy-only bound on the lowest coupled excitation is 0.720 +- 0.010 (m = 8, uniform records), 0.710 +- 0.029 (m = 8, canonical), 0.729 +- 0.010 (m = 12) against the torus values 0.713, 0.713, 0.739 at the same momentum (ratios 1.010, 0.996, 0.986), while the normalized susceptibility 2 m_-1 / sum w^2 is 0.642 +- 0.013, 0.617 +- 0.049, 0.801 +- 0.020 against the torus 1.064; at the larger momentum (k = 1.40, 1.45) the region's bound is 0.888-0.955 of the torus value and its susceptibility 0.80-0.96 of it. No limit, boundary independence or photon law is claimed."
upstream_dependencies:
  - minimal_axioms
  - ring_model_two_regulators_a_region_bounded_by_records_matches_the_torus_at_size_eight_and_the_walker_population_is_the_larger_regulator_bounded_theorem_note_2026-09-25
runner: scripts/ring_model_energy_only_photon_bounds_in_a_region_bounded_by_records_against_the_torus_2026_09_25.py
---

# In a region bounded by records the energy-only photon bound matches the torus, and the records reduce only the response amplitude

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** exact identities of the supplied model with finite projector estimates; unaudited.

## Result

The Lattice axiom's sites are all of `Z³`; a region whose outside carries
records is the framework's own finite object, and the torus is a quotient
regulator. The landed two-regulator note compared the two through
correlations; open PR 9236 bounded the torus photon with energies alone.
This block measures the same energy-only bound inside a region bounded by
records.
- **The method carries over exactly.** The probe is a standing-wave triple
  that vanishes at the records. The records induce a mean field, so the
  energy in a probe field has odd terms; symmetric combinations remove
  them. The first moment needs the ring expectation plaquette by
  plaquette, and the Hellmann–Feynman derivative in per-plaquette ring
  couplings supplies it. On an exact 3646-state region the derivative
  equals the double commutator to `10⁻⁸` and the projector reproduces both
  moments.
- **The photon's energy scale matches the torus.** At the smallest standing
  wave the bound on the lowest coupled excitation is `0.720 ± 0.010`
  (size 8, records from uniform ice), `0.710 ± 0.029` (size 8, ordered
  records) and `0.729 ± 0.010` (size 12), against `0.713`, `0.713` and
  `0.739` on the torus at the same momentum: ratios `1.010`, `0.996`,
  `0.986`.
- **The records reduce the response, not its frequency.** The normalized
  susceptibility of that wave is `0.64` and `0.62` at size 8 and `0.80` at
  size 12, against `1.06` on the torus: `0.58–0.60` of the torus value at
  size 8 and `0.75` at size 12, moving toward it as the region grows. Since
  the bound, the square root of the ratio of the two moments, matches the
  torus, the first moment is reduced in the same proportion.
- **At the larger momentum the region sits below the torus.** For
  `k = 1.40` and `1.45` the bound is `0.888–0.955` of the torus value, and the
  two record frames differ by about two standard errors there.

Supplied model, finite estimates: no limit, boundary independence or
photon law is claimed. For the question whether the torus steers the
photon result, the answer on these sizes is: not its energy scale at long
wavelengths, which a region bounded by records reproduces to about one per
cent; the records act on the amplitude of the response near the boundary.

## Setting and decision points

- **D-gauss, D-roles, D-ring (landed).** The exact vertex Gauss law and the
  ring clause at `V = 0`, `g = 1`.
- **The region (method).** The unrecorded interior `{1, …, m}³` of an
  `(m+2)³` cell whose other links carry records, as in the landed
  two-regulator note; records from a uniform-ice sample of the cell's
  zero-winding sector or from its canonical ice state. A record on a link
  removes every ring term containing it (landed).
- **The probe and the projector (methods).** The standing-wave triple
  `W = Σ_a Σ_{a-links} sin(π n x_b/(m+1)) σ`, `b = a + 1 mod 3`, momentum
  `k = πn/(m+1)`; the compiled projector of open PR 9236 extended to
  per-plaquette ring couplings, guide `exp(0.2 N_flip + (h/2) W)`.

None is adopted.

## Theorem 1 — the energy-only bound in a region

Let `a_n = |⟨n|W|0⟩|²` for excited states `n` of the region's flip
component, `ω_n = E_n − E_0`, `m_j = Σ_n a_n ω_n^j`.

1. **The inverse moment from energies.** `E(h) = E_0 − h⟨W⟩ − h² m_{−1} +
   O(h³)`, with odd terms because the records give `⟨W⟩ ≠ 0`. The symmetric
   combinations `S(h) = [E(h) + E(−h)]/2 − E_0 = −h² m_{−1} − b h⁴ + …` at
   `h` and `2h` eliminate `b`: `m_{−1} = −(16 S(h) − S(2h))/(12 h²)`.
2. **The first moment from energies.** For diagonal `W`,
   `m_1 = ½⟨[W,[H,W]]⟩ = ½ Σ_p c_p ⟨R_p⟩` with `R_p = U_p + U_p†` and
   `c_p = 4 (Σ_{l∈p} w_l sign_l)²`, the squared change of `W` when a
   flippable `p` flips (independent of the configuration, since the links
   of a flippable plaquette follow its circulation). With ring couplings
   `1 + ε c_p`, the Hellmann–Feynman theorem gives `∂E_0/∂ε = −Σ_p c_p ⟨R_p⟩`,
   so `m_1 = −[E(ε) − E(−ε)]/(4ε) + O(ε²)`.
3. **The bound.** Log-convexity of the moments gives
   `ω_min ≤ (m_1/m_{−1})^{1/2}`, where `ω_min` is the lowest excitation with
   `⟨n|W|0⟩ ≠ 0`. The ratio is normalization-free, so it compares directly
   with the torus bound `2 s(k)(u/χ̄)^{1/2}` of open PR 9236.

On the exact 3³ region the Hellmann–Feynman `m_1` equals the double
commutator to `10⁻⁸` for both `n = 1, 2`, and the chain reads
`0.7805 ≤ 0.9925 ≤ 1.2622` and `0.7246 ≤ 0.8143 ≤ 0.9150`. ∎

## Diagnostic — regions against the torus

Two to four seeds per row; `h = 0.15`, `ε = 0.02`; the torus values
interpolate open PR 9236's 8³ and 12³ bounds per unit lattice momentum at
`k = π/4, π/3, π/2`. The normalized susceptibility is `2 m_{−1}/Σ w²`, which
equals the torus `χ̄` for plane waves.

| region | records | seeds | `k` | susceptibility | torus | bound on `ω_min` | torus | ratio | bound / `s(k)` |
|---|---|---|---|---|---|---|---|---|---|
| 8 | uniform ice | 4 | 0.698 | 0.642 ± 0.013 | 1.064 | 0.720 ± 0.010 | 0.713 | 1.010 | 1.05 |
| 8 | uniform ice | 4 | 1.396 | 1.096 ± 0.012 | 1.165 | 1.136 ± 0.007 | 1.279 | 0.888 | 0.884 |
| 8 | canonical | 2 | 0.698 | 0.617 ± 0.049 | 1.064 | 0.710 ± 0.029 | 0.713 | 0.996 | 1.037 |
| 8 | canonical | 2 | 1.396 | 0.930 ± 0.067 | 1.165 | 1.221 ± 0.044 | 1.279 | 0.955 | 0.950 |
| 12 | uniform ice | 3 | 0.725 | 0.801 ± 0.020 | 1.064 | 0.729 ± 0.010 | 0.739 | 0.986 | 1.028 |
| 12 | uniform ice | 3 | 1.450 | 1.119 ± 0.020 | 1.170 | 1.223 ± 0.011 | 1.317 | 0.929 | 0.922 |

- **Energy scale.** At the smallest standing wave the three regions agree
  with the torus within 1.4 % and within their errors, and with each other.
- **Amplitude.** The susceptibility of that wave is suppressed by the
  records (0.58–0.60 of the torus value at size 8, 0.75 at size 12). The
  bound matching the torus means the first moment is reduced in the same
  proportion; why the two fall together is not resolved here.
- **Larger momentum.** The region's bound lies below the torus by 4–11 %;
  the standing wave in a finite region mixes neighbouring momenta and
  weights the boundary layer more, and the two frames differ by about two
  standard errors in both the susceptibility and the bound. ∎

## What this means for the lanes

- **The regulator question.** The torus is a quotient of `Z³`; a region
  bounded by records is a subset. On these sizes the photon's energy scale
  at long wavelengths does not depend on which regulator is used, while
  the amplitude of its static response does, near the boundary, and less
  so as the region grows. The torus, the region and open PR 9236's
  energy-only bounds thus give one photon scale on these sizes.
- **What the framework supplied.** The Gauss law, the ring and the records
  at the boundary are decision points and supplied data; the probe, the
  projector and the Hellmann–Feynman step are methods.

## What stays open

- Larger regions, where the amplitude should approach the torus value,
  and the larger-momentum offset.
- Other record frames, and regions with a charge inside.
- Independent checks of every number here.

## Evidence limits

- **Domain:** two region sizes, two frames at size 8, the listed momenta,
  the flip components of the frame configurations.
- **Exact versus estimated:** Theorem 1 and the 3³ numbers are exact; the
  region and torus numbers are projector estimates with errors of no
  proved coverage; the torus column is an interpolation of open PR 9236.
- **Comparison:** agreement within errors is not an equivalence test.

## Prior art

Hellmann 1937 and Feynman 1939; the sum-rule and moment inequalities of
linear-response theory (for example Pitaevskii and Stringari, 2003);
Rokhsar and Kivelson 1988; Hermele, Fisher and Balents 2004. All cited as
prior art, not as premises.

## Checks

The runner has 2 checks and both pass in about 32 minutes, single-threaded.

| Check | Result |
|---|---|
| Exact 3³ control | Hellmann–Feynman first moment equals the double commutator; the chain; the projector's moments within 1.3 standard errors. |
| Regions against the torus | Reported: the table. |

## Independent check

None yet. The runner was run once through the cache tool; seeded Monte
Carlo reproduces its numbers.

## What this does not do

- It adopts no clause, Gauss law, record frame or method.
- It claims no limit, boundary independence or photon law; agreement within
  errors on two sizes is not an equivalence.
