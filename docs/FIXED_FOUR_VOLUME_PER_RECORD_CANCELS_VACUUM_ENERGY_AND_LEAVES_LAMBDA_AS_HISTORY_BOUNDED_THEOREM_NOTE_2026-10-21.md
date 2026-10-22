---
claim_id: fixed_four_volume_per_record_cancels_vacuum_energy_and_leaves_lambda_as_history_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "On a supplied cubic-frustum Regge expansion carrier, varying edge lengths at fixed 4-volume per record cancels every vacuum term proportional to 4-volume and conserves a constant Lambda set only by initial data, lost matter energy and a kick rho^2/rho* per synchronous 2^3 split; supplied per-new-cell phase and split-trigger self-tuning rules either track the critical density, freeze the start or need the size by hand; no rule fixing the size of Lambda is established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/fixed_four_volume_per_record_cancels_vacuum_energy_and_leaves_lambda_as_history_2026_10_21.py
---

# Fixed 4-volume per record cancels vacuum energy and leaves Lambda as history

Claim type: bounded_theorem.
Primary runner: `scripts/fixed_four_volume_per_record_cancels_vacuum_energy_and_leaves_lambda_as_history_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. Its response law varies edge lengths with each record's 4-volume held fixed. This note tests what that rule, and three alternatives, do to the cosmological constant on a supplied expansion carrier. None fixes its size. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose none of the carriers, splits or rules used.

## Statement

1. On the supplied cubic-frustum Regge carrier, the fixed-4-volume rule cancels every vacuum term -rho_v V from the edge equation exactly.
2. Under that rule a constant Lambda is conserved with no secular drift, and the late expansion obeys Friedmann with it, so w = -1.
3. Its value is Lambda_0 plus the matter energy lost along the way plus rho^2/rho* for each synchronous 2^3 split of dust, with rho* = 3/(4 pi G a^2) the lattice's maximal density. Lambda_0 is set by the first slab, so the size is history, not a consequence of the rules.
4. A phase per new cell gives a constant of unfixed size plus a zero-mean term that tracks the critical density. Self-tuning through the split trigger tracks, freezes the starting value, or needs the measured size put in by hand.

## Derivation

Fixed 4-volume. At fixed V_n the variation of rho_v V vanishes, so a vacuum term proportional to 4-volume drops out of the edge equation. This removes the 4-volume parts of the vacuum sea and of any constant residual. It does not remove the sea's shear response. The integration constant of the remaining equations is a conserved Lambda, fixed by the first slab's mismatch. Matter non-conservation enters as Lambda = Lambda_0 + int Q dt. The split junction's one-slab residual of order (H l)^2 becomes a permanent kick rho^2/rho* per split. Fixing only the cell count is not enough: through the split trigger the record count follows the expansion, so on large scales a per-record phase still acts as a gravitating Lambda.

Per-new-cell phase. Write the phases as mean m plus fluctuation of size s. Then Lambda = m/v + s/(v sqrt N): a w = -1 constant of unfixed size m plus a zero-mean 1/sqrt N term proportional to H^2. "Constant because deterministic" and "size from sqrt N" are different terms.

Self-tuning. A steady split rate is a constant H at every epoch. New cells inheriting a fraction lam of the parent's phase plus k (H tau)^2 track for lam < 1/16 and freeze the first value at lam = 1. For F = alpha x^p, the de Sitter fixed points x^2 = 0.385 F(x) lie at x = H tau of order 1e-3 to 1e3 for alpha in [1e-2, 1e2].

Identity. rho_L/rho_P = 3/(8 S_dS) with S_dS = pi/(H_L l_P)^2, so a capacity rule restates the size rather than deriving it.

## Checks

The runner gives 19 PASS and 0 FAIL. These are finite diagnostics of supplied models.

- Vacuum cancellation to 3e-16 relative, for rho_v from 1e4 to 1e7 Lambda_0.
- No drift: |Lbar_n - Lambda_0| <= 4.2 c^2 rho_c(n) at every slab (3.92, 4.06, 4.13 at relative steps c = 0.02, 0.01, 0.005), though rho_c starts at 1e4 Lambda_0. Late (3H^2 - rho_r)/Lbar is 1.00008, 1.00001, 0.99999.
- Initial data: a 1e-7 change of the second edge length moves Lambda by 20% (1.2030 at the first slab, 1.2034 late).
- Lost energy: radiation losing 1% at one slab raises Lambda by the lost density (ratios 1.00078, 1.00017, 1.00004), with later drift at most 0.14 c^2.
- Split kick: ratio to rho^2/rho* from 0.9974 to 0.9991 in five setups, independent of step.
- Per-new-cell phases: slope -0.490 and mean 0.2980 against m = 0.3. Independent split phases have Fano factor 35.3 times the ticks per split (35.17 to 35.28 against 35.29 analytic).
- Self-tuning: lam = 0 gives Omega at BBN of 3.42; lam = 1 gives a ratio of 1.0667 between today's and the first value. Fixed points lie in [3.9e-3, 2.6e2]. Cancelling the junction residual with a vacuum term needs rho_v/rho_c of -1.014, -1.013, -1.027 at H l = 0.091, 0.046, 0.023, so no small positive constant.
- A corner-preserving split changes the energy of massless light states of the register's update by -c(eps) K^2 E per split, with c from 3.142e-2 at eps = 1.271 to 4.622e-5 at eps = 0.041 (c/eps^2 tending to about 0.0275).
- A supplied frozen sea has number variance 0.502 to 0.503 l^2 in sharp cubes and exponent 1.12 in smooth windows.

## Against measurement (estimates)

Measured inputs: rho_L = 1.13e-123 rho_P, w = -1.03 +- 0.03, Omega_L(BBN) < 0.05, early dark energy below 2% at recombination.

- Fixed 4-volume with splits: the measured value needs the first such split at T near 1.2 TeV. A supplied inflation by splits (539 ticks per split, 60 e-folds) overshoots by 3e110, and a Planck start gives about rho_P. The 1.2 TeV value sits at sqrt(M_L M_P), so reading it as the electroweak scale would be numerology.
- Fixed 4-volume with split losses in an empty vacuum and a thermal plasma: rho_L = 598 c g T_max^6/M_P^2, which needs T_max from 16 MeV (eps 1.27) to 48 MeV (eps 0.04), with w + 1 = -5e-66 today. This is a conditional relation only.
- Per-new-cell phase: Poisson counting lands within a factor of 2 but tracks, with the spread of Omega_L 3.59 at BBN, 2.74 at recombination and 1.25 today. Split noise is off by about 1e31 either way and correlated noise by about 1e116. Excluded.
- Self-tuning: a steady split rate makes the expansion at 1 MeV too slow by 3.7e17, and the measured H tau = 5.6e-61 needs alpha = 8.3e-121 by hand. Excluded.
- Sea number noise in a sharp Hubble window is 0.16 to 0.47 of the measured value, but it tracks, and the same noise on 1 m would be 5e25 kg/m^3 (sharp) or 4e7 kg/m^3 (smooth). Excluded.
- Capacity: 2^407.5 qubits per horizon would have to be supplied.

## Boundary

Supplied: the frustum carrier, its central tick, the matter phase -E T, kappa = 1, the split construction and threshold, the corner-preserving split map, the update at the chosen mu and b, the empty vacuum and thermal plasma for the split-loss estimate, independent split phases, the self-tuning families, the unit map, LambdaCDM and all measured numbers. The empty-vacuum input conflicts with the sea-induced running of alpha in the register. The result is negative for the size of Lambda: no tested rule fixes it, and the fixed-4-volume rule turns the vacuum-energy problem into a requirement that every refinement be adiabatic to about 1e-123 of rho_P. No rule fixing the size of Lambda is established.
