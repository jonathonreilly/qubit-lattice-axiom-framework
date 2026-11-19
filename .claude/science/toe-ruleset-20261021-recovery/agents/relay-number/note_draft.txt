---
claim_id: relay_number_change_by_switching_confined_to_tick_connected_configurations_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "In two supplied fermion-mode models (one block with a link mode, and a ring of three blocks with a pair pulse), odds on block-mode occupations with switching confined to configurations the tick connects keep Born statistics, conserve value in every jump and let relays begin and end in opposite-value pairs; no physical vacuum, particle creation, coupling or identification is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/relay_number_change_by_switching_confined_to_tick_connected_configurations_2026_10_21.py
---

# Relay number can change by switching confined to tick-connected configurations

Claim type: bounded_theorem.
Primary runner: `scripts/relay_number_change_by_switching_confined_to_tick_connected_configurations_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its relays follow the odds, but the register does not say whether the number of relays can change. This note puts odds on block-mode occupations and confines switching to configurations the block tick connects. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used.

## One block with a link mode

One block holds a fermion mode a of value +1, a mode b of value -1, and a link mode c, truncated exactly by the conserved n_c + n_a. The tick applies free phases and then a pair coupling a^+ b^+ c + h.c. It conserves the value Q = n_a - n_b exactly, while relay number N = n_a + n_b is not conserved (|[N,U]| = 0.41); with the coupling off, N commutes with the tick. The spectrum of the pair picture equals that of a filled lower mode to 1.1e-15. Class odds are conserved to 8.9e-16, and 20000 trajectories over 40 ticks follow the Born odds within 2.27 standard deviations, with 39971 creations and 20110 endings, each keeping Q.

Relay deposits plus link-quantum deposits are unchanged by every jump, while relay deposits alone jump by 2 eps (0.60). Confined switching gives no energy-violating jumps, against 4330 when switching is not confined. Tick energy is conserved only mod 2 pi: a drive at 2 eps + 2 pi converts as fully as resonance (pair odds 1.000), one at 2 eps + 1 does not (0.059). In the dressed state the joint phase advance is the same in every configuration (0.4800), while bare deposits are 0.6000, the difference being the binding share -0.1200.

## A ring of three blocks

A ring of three blocks with four fermion modes each (4096-dimensional Fock space) has a tick of a fermionic shift, which moves every relay one block, followed by block coins and a pulse that is later switched off. The tick commutes with ring translation. With the pulse off the empty state stays empty. Block-class odds are conserved to 8.9e-16, and 6000 trajectories reproduce the relay-number odds P(N = 1, 3, 5) = 0.844, 0.150, 0.006 as 0.839, 0.155, 0.006, within 1.64 standard deviations. The pulse creates relays (P(N > 1) = 0.156) with no block-value violations. Over 400 trajectories each site holds one record, none is read twice, an ended relay's last record is never read, and the recorded value per tick equals the total value. All 796 begun and 715 ended pairs are opposite-value pairs in one block.

Two controls fail as expected: joint switching over the whole configuration moves value between blocks (4931 violating trajectory-ticks), and a same-value pair coin breaks block value (2669).

## Scope

Supplied: one fermion mode per block mode, the value labels, the vacuum as empty modes equal to a filled lower band, the link mode and its deposit, the coin, pulse and coupling, relay-identity matching at switches and the site choice. No physical vacuum, particle creation, coupling or identification is established.
