# First-birth energy spread on the seven-site path — review unit

This unit builds on PR #8865's exact physical seven-site path and actual
formation channels. Read `energy_spread_author/FIRST_BIRTH_ENERGY_SPREAD_ON_SEVEN_SITE_PATH.md`
and the adjacent exact runner/results. The root rotor-path implementation
reconstructs all first channel vectors and matches each one to the earlier
independently built PRE matrix in PR #8865. The post-result energy argument
has no separate independent reviewer yet.

The target's initial energy derivative is `128 kappa delta` in the stated
Hamiltonian convention. A uniform record-number energy offset changes its
mean by `24 kappa mu`; the conditional first-birth transition-energy
variance `56 delta^2/9` survives the offset. These are first-birth,
finite-path facts about the **supplied compensated target**. They neither
derive an autonomous energy source nor rule out a reservoir.

Run `verify_energy_spread_publication.py` here to authenticate this small
unit and its source dependencies. The exact runner uses only the Python
standard library. Set `ENERGY_SPREAD_OUTPUT_DIR` to a scratch directory to
rerun without rewriting the committed result. The complete result, stdout,
stderr and execution receipt are included. The review proposal requests no
merge, native-axiom adoption or formal audit verdict.
