# Handoff

Current branch: `physics-loop/pr230-retained-closure-campaign-block124-20260517`.

Current base: `origin/claude/yt-direct-lattice-correlator-2026-04-30` at
`a7179acb5ce21f9fdf2e05af1139c8b6a6785699`.

Stacked review PR for Blocks120-121: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1439
Stacked review PR for Block122: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1445
Stacked review PR for Block123: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1450
Stacked review PR for Block124:
https://github.com/jonathonreilly/cl3-lattice-framework/pull/1456

PR #230 is open and draft.  Latest current-surface block is base Block119.
Base Block117 records absence of strict Schur/scalar-LSZ pole authority.  Base
Block118 gives exact Hamming-Dirichlet support for the finite taste-radial
`O_H` axis, but keeps accepted EW/Higgs action, scalar LSZ/source-overlap, and
strict `C_ss/C_sH/C_HH` pole rows absent.
Base Block119 adds a native finite Dirichlet action/LSZ probe as support plus
boundary; it still does not supply accepted action, scalar LSZ/source-overlap,
or physical pole rows.

Block120 has landed locally as an exact negative boundary.  It narrows the
remaining blocker to one strict same-surface positive disjunct and rules out
source-only or finite-row promotion as invariant `y_t` data on the current head.

Block121 adds a Schur/Feshbach finite-packet boundary: complete finite A/B/C
rows at the current qhat^2 nodes do not determine `K'(pole)` or the residue.
The Schur route still requires strict pole derivative/residue rows or an
accepted analytic continuation/model-class plus FV/IR/contact bridge.

Block122 closes the finite-axis/native-Dirichlet promotion shortcut: the base
Block118 `O_H` axis and base Block119 finite action/LSZ support do not
determine accepted action, scalar LSZ/source-overlap normalization, contact
subtraction, or strict source-Higgs pole rows.

Block122 has been repaired after the interrupted rebase and rerun locally:
Block122 `PASS=11`, full positive `PASS=200`, retained route `PASS=325`,
completion audit `PASS=79`, campaign `PASS=440`, assumption/import stress
`PASS=123`, target-timeseries full set `PASS=9`, and chunk063 higher-shell
checkpoint `PASS=15`.

Block123 derives the exact source-Higgs LSZ readout formula
`y_H = (dE_top/ds) * sqrt(Res C_HH) / Res C_sH`.  It is exact support only:
current strict source-Higgs pole rows, canonical `O_H`/action authority,
Gram/leakage control, and retained-route gates are still absent.  Initial
reruns: Block123 `PASS=12`, campaign `PASS=441`, assumption/import stress
`PASS=124`.

Block124 consumes the now-completed higher-shell source-Higgs/taste-radial row
packet and verifies the tail chunk state.  It checks 63/63 chunk files and 693
finite `C_ss/C_sx/C_xx` rows.  The finite diagnostic is support-only:
`max |rho_sx| = 0.0015085138080374685` and the minimum finite Gram determinant
is `0.031674465976530355`, but these are not pole residues and `x` is not
certified canonical `O_H`.  `pole_residue_rows=[]` across the packet, no
canonical `O_H` identity is recorded, and the Block123 strict pole packet is
absent.  Reruns: Block124 `PASS=10`, campaign `PASS=442`,
assumption/import stress `PASS=125`.

Active next work: produce a strict same-surface row artifact with accepted
canonical `O_H`/action authority and numeric `C_ss/C_sH/C_HH` pole residues,
then rerun the Block123 readout/Gram/FV/IR/contact and retained-route gates.
If that cannot be supplied, pivot to genuine same-source W/Z response rows with
identity/covariance/`g2` authority.

Do not claim proposed_retained unless the closure/retained/audit/status gates
pass and the claim certificate explicitly allows a proposal.

Refresh the loop-local lock before expiry with:

```sh
python3 scripts/automation_lock.py \
  --lock-path .claude/science/physics-loops/pr230-retained-closure-campaign-20260517/campaign.lock.json \
  --meta-lock-path .claude/science/physics-loops/pr230-retained-closure-campaign-20260517/.campaign.lock.guard \
  refresh --owner physics-loop --purpose pr230-retained-closure-campaign-20260517 --ttl-hours 1
```
