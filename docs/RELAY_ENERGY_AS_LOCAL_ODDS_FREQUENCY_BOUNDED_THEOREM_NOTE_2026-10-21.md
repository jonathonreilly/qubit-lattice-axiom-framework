---
claim_id: relay_energy_as_local_odds_frequency_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Finite deterministic diagnostics on supplied lossless walks of a relay energy defined as the local odds-weighted phase advance per tick; no physical energy identification, field equation or derivation of the rules."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/relay_energy_as_local_odds_frequency_2026_10_21.py
---

# Relay energy as the local odds frequency

Claim type: bounded_theorem.
Primary runner: `scripts/relay_energy_as_local_odds_frequency_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Earlier source-tensor diagnostics weighted every relay by the packet's mean band frequency, an input set per packet. This note replaces that input with a local rule. A relay's energy is the odds-weighted mean, over the direction amplitudes at its site, of minus the argument of the amplitude after one tick times the conjugate of its value before. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the walks or rules used.

## Results

On a two-component walk on a line (coin angle .05, momentum .06), packets of width 30, 60 and 120 were followed for 160 ticks. The total relay energy (local energy times density, summed) varies over that time by 1.1e-4, 1.8e-5 and 1.2e-6. Its mean approaches the packet's spectral mean frequency: 0.079640 against 0.079721 at width 30, and equal to six digits at width 120.

The redraw and stress assignments are also weighted by the local energy. With them the smoothed momentum residual, relative to the divergence of the burn stress, is .114, .044 and .020 at the three widths. That is close to the values obtained with the packet-frequency input. On the six-direction walk on Z^3 with packets moving along (1,1,0), the residual is .277, .179 and .114 at widths 3, 5 and 8, again falling with width.

## Scope

The walks, coin angles, packets, phase-advance evaluation and smoothing are supplied. The residuals are finite diagnostics of a leading-gradient balance. No physical energy identification, field equation or derivation of the rules is established.
