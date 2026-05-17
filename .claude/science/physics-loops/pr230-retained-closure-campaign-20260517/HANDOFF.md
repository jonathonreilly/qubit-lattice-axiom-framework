# Handoff

Current branch: `physics-loop/pr230-retained-closure-campaign-block131-20260517`.

Current base: `origin/claude/yt-direct-lattice-correlator-2026-04-30` at
`a7179acb5ce21f9fdf2e05af1139c8b6a6785699`.

Stacked review PR for Blocks120-121: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1439
Stacked review PR for Block122: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1445
Stacked review PR for Block123: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1450
Stacked review PR for Block124:
https://github.com/jonathonreilly/cl3-lattice-framework/pull/1456
Stacked review PR for Block125:
https://github.com/jonathonreilly/cl3-lattice-framework/pull/1458
Stacked review PR for Block126:
https://github.com/jonathonreilly/cl3-lattice-framework/pull/1461
Stacked review PR for Block127:
https://github.com/jonathonreilly/cl3-lattice-framework/pull/1463
Stacked review PR for Block128:
https://github.com/jonathonreilly/cl3-lattice-framework/pull/1468
Stacked review PR for Block129:
https://github.com/jonathonreilly/cl3-lattice-framework/pull/1476
Stacked review PR for Block130:
https://github.com/jonathonreilly/cl3-lattice-framework/pull/1479
Stacked review PR for Block131:
https://github.com/jonathonreilly/cl3-lattice-framework/pull/1481

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

Block125 refreshes the completed raw post-chunk surface across strict
source-Higgs, W/Z, Schur, and neutral contracts.  It finds 63/63 raw production
files, 693 finite source-Higgs rows, and 693 scalar LSZ support rows, but zero
source-Higgs time-kernel rows, zero pole-residue rows, zero accepted canonical
identity passes, zero W/Z response rows, zero Schur `K'`/pole hits, and zero
neutral transfer/primitive hits.  Reruns: Block125 `PASS=10`, campaign
`PASS=443`, assumption/import stress `PASS=126`.

Block126 constructs the matched top-side additive-subtraction packet from the
completed raw rows.  It checks 63/63 files and builds 1008 same-configuration
tau1 rows plus 23 complete tau slices for `T_total=dE_top/ds`,
`A_top=dE_top/dm_bare`, and `T-A`.  The tau1 means are
`T_total=1.245693776284446`, `A_top=1.2732143441892123`, and
`T-A=-0.02752056790476608`, with `corr(T,A)=0.9905564447030847`.  This is
bounded support only: no W/Z response rows, no matched top-W/Z covariance, no
strict non-observed `g2`, and no accepted same-source EW/Higgs action are
present.  Reruns: Block126 `PASS=10`, campaign `PASS=444`,
assumption/import stress `PASS=127`.

Block127 wires the Block126 top-side packet into the W/Z mass-fit response-row
builder.  The builder now recognizes the 1008-row top-side packet, but marks it
non-strict and writes no measurement rows because genuine W/Z rows, matched
top-W/Z covariance, strict non-observed `g2`, accepted same-source EW/Higgs
action, and canonical-Higgs/source-overlap authority remain absent.  Reruns:
W/Z builder current mode `PASS=10`, scout mode `PASS=9`, Block127 `PASS=10`,
campaign `PASS=445`, assumption/import stress `PASS=128`, retained route
`PASS=325`, full positive assembly `PASS=200`, completion audit `PASS=79`,
target-timeseries full set `PASS=9`, and chunk063 checkpoint `PASS=15`.

Block128 attempts the constructive next step after Block127.  The post-Block127
W/Z launch preflight records that the top-side root is satisfied, but
production W/Z mass-fit rows, accepted same-source EW/Higgs action, strict
non-observed `g2`, matched top-W/Z covariance, and a genuine production W/Z
harness remain absent.  The strict construction attempt then checks whether the
existing raw rows can supply strict same-source W/Z production rows matchable to
the 1008 Block126 top-side configuration keys, and then checks the accepted
`O_H`/action plus source-Higgs pole-row fallback.  The result is an exact
negative boundary: all 63 Block126 raw production files are present and carry
the scalar/top rows, but W/Z is only a disabled stub
(`wz_like_raw_file_count=0`, `disabled_wz_stub_file_count=63`).  The only
W/Z-shaped rows remain the scout smoke schema, which is not production,
synthetic, aggregate-only, not key-matchable to Block126, and lacks matched
covariance, strict `g2`, and identity certificates.  The source-Higgs fallback
also remains blocked: 252 lower-level raw finite `C_ss/C_sx/C_xx` rows and the
Block124 693-row assembled finite support packet are not pole residues;
`source_higgs_pole_residue_rows=0`; accepted canonical `O_H`/action authority
is still absent.  Reruns: Block128 py_compile passed, preflight `PASS=14`,
strict construction `PASS=12`, campaign status `PASS=447`, assumption/import
stress `PASS=130`, retained route `PASS=325`, full assembly `PASS=200`,
completion audit `PASS=79`, target-timeseries `PASS=9`, and chunk063
checkpoint `PASS=15`.

Active next work: pivot to strict Schur/Feshbach pole authority or neutral
H3/H4 physical-transfer/source-coupling authority.  Reopen W/Z only if a new
production W/Z mass-fit artifact appears; reopen source-Higgs only with
accepted canonical `O_H`/action plus nonempty numeric `C_ss/C_sH/C_HH`
pole-residue rows.

Block129 tests the Schur finite-proxy pivot and then the stricter row-authority
construction.  It uses the completed five-level higher-shell Schur packet to
check the prior two-point `C_x|s` one-pole scout and finite
Loewner/Stieltjes proxies.  Result: exact negative boundary.  The one-pole fit
through zero and first shell has `m^2=6.392091257441135` and
`R=1.7950481867558439`, but misses unused higher shells with max absolute
z-score `243.36741086003715`.  All eight finite candidate fields fail
necessary Stieltjes signs.  The construction attempt also finds no explicit
strict row sidecars, no strict pole keys in the 63 raw higher-shell files, no
finite-packet promotion past the Block121 nonidentifiability witness, and no
model/FV/IR/threshold or bridge authority.  Reruns: one-pole/Loewner
`PASS=13`, strict pole-authority construction `PASS=14`, campaign status
`PASS=449`, assumption/import stress `PASS=132`.

Block130 pivots to neutral H3/H4 physical-transfer/source-coupling authority.
It attempts to build H3/H4 from the completed 693-row finite
`C_ss/C_sx/C_xx` source/taste-radial packet, strict neutral sidecars, raw
higher-shell files, H1/H2 heat-kernel support, and the source-Higgs/Schur
fallbacks.  Result: exact negative boundary.  The runner finds no strict
neutral artifact paths, no strict raw neutral/primitive/source-coupling keys in
63/63 raw higher-shell files, and preserves the prior H1/H2-support-only,
finite-rows-not-transfer, Block128 source-Higgs, and Block129 Schur blockers.
It also constructs an explicit hidden-neutral two-completion witness: the
chunk001 `(0,0,0)` finite row is preserved while
`H(theta)=cos(theta)x+sin(theta)n` changes the normalized source coupling from
`-0.00022372749929547354` at `theta=0` to
`-0.0001118637496477368` at `theta=pi/3`, and positive transfer witnesses
`[[1,0],[0,1]]` versus `[[1,0.25],[0.25,1]]` change off-diagonal generator
content without changing current equal-time row data.  A complementary eta
counterfamily fixes the source self block and H1/H2 triplet block while
varying the source-triplet coupling from `0` to `0.12124355652982143`; the
eta scan checks 214 raw `ensemble_measurement.json` files and finds zero
strict neutral keys.  Reruns: Block130 transfer/coupling `PASS=12`, Block130
eta nonidentifiability `PASS=11`, campaign status `PASS=451`,
assumption/import stress `PASS=134`.

Active next work after Block130: neutral route reopens only with a new accepted
same-surface physical transfer/offdiagonal generator or
primitive/irreducibility certificate plus source/canonical-Higgs coupling
authority.  Without that artifact, pivot back to action-first source-Higgs pole
rows or strict W/Z production rows only if a new strict artifact appears.

Block131 pivots back to the action-first source-Higgs authority route and asks
whether the post-Block130 surface can supply accepted same-surface canonical
`O_H`/action authority plus nonempty numeric `C_ss/C_sH/C_HH` pole-residue
rows.  Result: exact negative boundary.  The runner preserves the Block123
formula and Block126 top-side response as support only, but finds no accepted
canonical `O_H`/action authority, no strict numeric pole residues, no nonempty
strict action/pole raw keys, and no strict packet sidecar.  The readout witness
holds `dE_top/ds=1.245693776284446` fixed while two Gram-pure non-authority
residue packets give `y_H=1.245693776284446` and
`y_H=2.491387552568892`.  Reruns: Block131 `PASS=14`, campaign status
`PASS=452`, assumption/import stress `PASS=135`.

Active next work after Block131: supply an accepted same-surface canonical
`O_H`/action/LSZ certificate plus nonempty numeric `C_ss/C_sH/C_HH`
pole-residue rows sharing source/action/`O_H` surface IDs.  Otherwise reopen
W/Z only with strict production W/Z rows plus non-observed `g2` and accepted
same-source action, or reopen Schur/neutral only with strict
pole/physical-transfer authorities.

Do not claim proposed_retained unless the closure/retained/audit/status gates
pass and the claim certificate explicitly allows a proposal.

Refresh the loop-local lock before expiry with:

```sh
python3 scripts/automation_lock.py \
  --lock-path .claude/science/physics-loops/pr230-retained-closure-campaign-20260517/campaign.lock.json \
  --meta-lock-path .claude/science/physics-loops/pr230-retained-closure-campaign-20260517/.campaign.lock.guard \
  refresh --owner physics-loop --holder-id 019de508-8c55-7850-b9a3-ef99e5ebf741 \
  --purpose pr230-retained-closure-campaign-20260517 --ttl-hours 1
```
