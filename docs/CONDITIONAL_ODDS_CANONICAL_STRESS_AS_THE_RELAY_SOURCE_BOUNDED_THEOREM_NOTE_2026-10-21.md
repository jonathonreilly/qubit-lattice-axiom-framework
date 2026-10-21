---
claim_id: conditional_odds_canonical_stress_as_the_relay_source_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Finite diagnostics on supplied lossless 1D coin-shift walks and few-relay toys of a proposed source reading: each relay sources the canonical conserved stress of its conditional odds, with relays following the joint odds by minimal switching only; its Born mean equals the reduced-state value, its per-tick jumps average to zero, and remote settings change only its distribution, with finite size estimates under a supplied coupling; no physical identification, field equation or adoption of the reading is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/conditional_odds_canonical_stress_as_the_relay_source_2026_10_21.py
---

# The canonical stress of the conditional odds as the relay source

Claim type: bounded_theorem.
Primary runner: `scripts/conditional_odds_canonical_stress_as_the_relay_source_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its record source counts burns and turns, which gives a standing wave the wrong stress and lets a remote setting change a relay's turns. This note tests a replacement: each relay sources the canonical conserved stress of its conditional odds, the joint odds with every other relay fixed at its actual block and direction, and relays follow the joint odds by minimal switching only. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used.

## One relay

On a walk with coin theta = 0.1 on 154 blocks, a plane wave has stress (eps, k, eps v, k v) = (0.2269, 0.2040, 0.2033, 0.1828). A standing wave of the same modes has energy eps, zero momentum and flux, and T_xx = k v = 0.1828, the plane-wave sign and size; the burns-and-turns reading gave -0.0563. The stress is linear, so a six-mode packet gets the odds-weighted mode value (0.1517), and a moving packet keeps it for 60 ticks to 2.2e-16. Flux over momentum density tends to theta/tan theta = 0.996664 at low k. The generator H = i log U is quasi-local, with |H| falling about 0.129 per block.

## Two relays

For the entangled pair (0,2k)+(2k,0) with theta = 0.2, the Born mean of relay 1's conditional source is the branch-mixture value in all four components, (0.3192, 0.1963, 0.1937, 0.1735). Per configuration it spreads between the branch values (energy 0.2826 to 0.4135, branches 0.2000 and 0.4383). It is not conserved per tick: it jumps when the other relay switches (fraction 0.056 per tick, rms 0.1308). The jumps average to zero, the exact Born mean is constant to 1.2e-15, and the variance of E1(t) - E1(0) saturates at 0.0043, below the squared branch gap 0.0568. A free per-relay stress misses the binding energy of a bound pair (<V> = -1.8 of E = -5.0), and splitting V half to each relay restores conservation of the Born-mean source in scattering to 4.9e-16.

Minimal switching alone keeps the joint Born odds exactly (3.6e-16; chi2/dof 1.016 over 978 bins), gives coined-pointer disagreement 0.1002 against 0.1012 for the odds, and CHSH 2.567 against 2.5710. A plane-wave relay never switches; a standing wave switches with mass 0.0883 per tick.

## Remote settings and branches

With B entangled with two blocks at A, A's choice of basis leaves the Born means of B's momentum and mass dipole unchanged, but changes their distribution (variance 0.1542 against 4.8e-33, and 255.9 against 5.6e-17). In a two-branch ball toy the conditional source follows the actual branch: with n imperfect pointer relays of overlap 0.801 the torque is 0.3211, 0.7342 and 0.9889 at n = 1, 4 and 16, within the rederived bound 1 - torque <= overlap^n. A single elementary relay sources half in each arm, while a bound pair sources fully in the actual arm.

Taking G = a^2/(8 pi) as a supplied conversion, the setting-dependent field of a rubidium pair split by 0.54 m differs at 1 m by about 5.2e-36 m/s^2 per run, at least 20 orders below any measured gravitational source.

## Scope

Supplied: the walks, coins, packets, toys, the binding split and the coupling conversion. Dropping the relay energy and the burn and turn deposits is part of the proposal tested, not a derived result. No physical identification, field equation or adoption of the reading is established.
