---
claim_id: records_never_condition_the_odds_formation_law_diagnostics_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Finite diagnostics on supplied lossless 1D walks and few-qubit couplings of the candidate formation law that records never condition the odds, with relays following the joint odds by minimal switching: Born statistics, kept drift, agreeing pointer readings, no signalling of outcome marginals, CHSH above 2, kept interference and undisturbed free crossing, against four conditioning alternatives, plus one failure of the turn deposit under a remote basis choice; no physical identification, measurement theory or adoption of the law is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/records_never_condition_the_odds_formation_law_diagnostics_2026_10_21.py
---

# Formation law diagnostics: records never condition the odds

Claim type: bounded_theorem.
Primary runner: `scripts/records_never_condition_the_odds_formation_law_diagnostics_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight, and no law there says when a new fact forms from the odds. This note tests the candidate that records never condition the odds: the odds evolve losslessly and relays follow them by minimal switching on the joint configuration. Four conditioning alternatives serve as controls. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the models used.

## One walker

The flow image of the odds equals the odds after 100 ticks to 4.3e-16, and sampled relays match the Born histogram with chi2/dof 1.412 over 76 bins. The Born spread is 54.1 sites, ballistic, against about 10 for a classical walk. The unconditioned odds keep the drift (shift over v T = 0.9845 at v = 0.8926), and relays carry it (351.79 against 351.52 sites). Conditioning on the record every tick keeps a drift ratio of only 0.111, and conditioning at a rate twice the energy (0.447 per tick) keeps 0.466 by T = 400.

## Pointers, singlets and interference

With an ideal pointer coupling, the reading frequency is the Born weight (0.3024 against 0.3), and joint switching gives zero disagreement between two readers, while marginal-only switching gives 0.4188 against 2p(1-p) = 0.42. For a singlet the exact odds give CHSH 2 sqrt 2 = 2.828427 and relay readings give 2.841; B's outcome odds are independent of A's setting to 5.6e-17, and sampled B frequencies are 0.5060 and 0.5006. In an interferometer the law keeps full fringe visibility for both odds and relays, while conditioning on branches of disjoint support gives 1/2 at every phase. Two free walkers crossing leave walker 1's momentum odds unchanged (8.9e-17), while conditioning when relays meet disturbs them (total variation 0.303 at met fraction 0.42).

## A failure of the turn deposit

B's position and direction odds are independent of A's basis at every tick, to 5.6e-17, so the burn density is unchanged. But B's expected turn count at its coupling tick depends on A's basis: 0 with no measurement, 0.3536 in z, 0 in x. The z value equals the sum over A branches of the change in B's odds, sin(pi/4)/2 = 0.353553. Since each 1D turn deposits -1 in the record source, the turn part of that source depends on a remote basis choice under this law.

## Scope

Supplied: the walks, coins, couplings, protocols and the four conditioning alternatives. No physical identification, measurement theory or adoption of the law is established, and the turn-deposit failure is recorded, not repaired.
