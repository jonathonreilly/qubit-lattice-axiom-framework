---
claim_id: candidate_law_cl2_a_records_qubit_leaves_the_flow_evidence_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Finite checks of stated toy rules supporting candidate law CL-2 (CANDIDATE_LAWS.md), conditional on CL-1 (lossless passing). (1) On a 400 x 240 slice with weights m = (1 + Phi)^-4, k = 1, a packet is shifted 12.5 sites further toward a pace well (Phi = -0.05) and 16.8 sites away from a pace hill (+0.05). (2) On a 96^3 torus the averaging response at r = 16 is 0.01654 for a unit drain on one site, on a 3 x 3 x 3 block, or on 6 neighbours, while at r = 3 the values are 0.15164, 0.14506, 0.15164. (3) Under the lean-away rule read with the chessboard at r = 12: one record +0.02639, two same-colour records +0.05620, two opposite-colour records -0.00360; under averaging two opposite-colour records give +0.05638. (4) On a 61^3 grid (q = 0.2): fixed shares at sparse records give 0.1200 and 0.1201 per record; a dense ball of radius 3.2 with pace held at zero below zero freezes a region of radius 10.0; multiplicative drains never reach zero and give 0.1006 and 0.0843 per record. (5) In 1D the group delay through Phi = -0.02 exp(-x^2/45000) over 2 sum |Phi| is 1.030, 1.056, 1.504 at wavelengths 41.9, 20.9, 6.3. (6) On a 41^3 grid: cutting a ball of radius 3.2 out of the averaging network changes the pace nowhere by more than 1e-8; held at zero, one site gives mass 0.399 and 33 sparse sites 0.194 per site; a fixed share gives the same mass per record for 1 and 33 records. (7) Twelve records each pinned at the pace current when they formed leave the far-field mass at 9e-9. (8) In the lean-away-in-time rule (s = 1/4), r d at r = 10 over ticks 56-68 varies by less than a quarter of its mean for a steady share (mean ~0.025) and for an absorber (~0.32), and by more than the steady mean after a one-time removal. (9) Removing 5% and 10% of the sites of a 100-site slab slows a crossing pulse by 6.8% and 14.2%. Not claimed: that these rules are the framework's law, nonlinear equations for frozen regions, a derivation from the axioms, or any physical identification."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/candidate_law_cl2_a_records_qubit_leaves_the_flow_evidence_2026_10_18.py
---

# Evidence for candidate law CL-2: a record's qubit leaves the flow

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Finite checks of stated toy rules, conditional on CL-1.
The clause itself is recorded in [CANDIDATE_LAWS.md](CANDIDATE_LAWS.md).

## Question

What should a record do to the influence around it, given that influence passes without loss
(CL-1)? The owner proposed that a record removes its qubit from the flow: "a drain in a way".
This note compares that with the alternatives.

## Result (stated toy rules)

| What the record does | Far-field pull | Additive mass |
|---|---|---|
| pure hole: influence detours (item 6) | none | — |
| perfect absorber (item 6) | yes | no (shielding) |
| holds its formation-time pace (item 7) | none | — |
| holds a fixed lower pace (item 4, PR #9825 L3) | yes | no (grows with size) |
| passes on a fraction, i.e. multiplicative (item 4) | yes | no |
| raises the pace (item 1) | repels | — |
| removes its share once (item 8) | passing ripple only | — |
| **permanently short one share** (items 4, 6, 8) | **lasting 1/r** | **yes** |

Under the adopted clause:

- **Attraction.** Slowing attracts (item 1).
- **Far field.** Only the total share matters far away (item 2).
- **Averaging.** The pace must average with its neighbours, because a lean-away pace makes
  mass sign follow the chessboard (item 3).
- **Freezing.** A region slowed to zero freezes, beyond the matter itself (item 4).
- **Equivalence.** Everything falls alike at long wavelength (item 5).
- **Local slowing.** Removed sites slow influence locally, by about 1.4 times the removed
  fraction in 2D (item 9).

## Premises

- **Candidate laws used.** CL-1 and CL-2.
- **Supplied.** The toy rules and their weights.
- **Standard facts used.**
  - Discrete Green functions.
  - The maximum principle.
  - Group delay.

## No-Go Discipline Gate

- **N1 — routes.**
  - Saturating or content-dependent shares.
  - Nonlinear pace rules.
- **N2/N3 — scope.**
  - Single grids and seeds.
  - The weak field except item 4.
- **N4 — inputs.** The thresholds are printed by the runner.
- **N5 — wording.** "Freezing" names the toy rule's zero-pace region.
- **N6/N7 — strongest objections.**
  - The floor rule is chosen.
  - Item 1 is a 2D slice.
- **N8 — earlier claims.** Builds on #9822 and #9825.

## Verification

```bash
python3 scripts/candidate_law_cl2_a_records_qubit_leaves_the_flow_evidence_2026_10_18.py
```

Expected: `TOTAL: PASS=9 FAIL=0` (about 30 seconds).

## Load-bearing sources

- [Candidate laws](CANDIDATE_LAWS.md)
- [Axioms](MINIMAL_AXIOMS_2026-06-29.md)
