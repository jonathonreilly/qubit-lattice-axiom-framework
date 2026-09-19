# two-source-interaction, attempt 3 (worker w-macbookpro90c72-j165b, model grok-4.6)

Different route from a2 (linear AR Fourier on L=4,8,16,32). Here: the *nonlinear* 7-point synchronous automaton and its Gibbs measure `π ∝ ∏_x Z(S_x)`, `S_x = s_x + ∑_{±e_j} s_{x±e_j}`.

## (1) The statement attempted

**(a)** The 7-point level automaton `P(s→s')=∏_x K(s'_x | S_x(s))` is reversible w.r.t. `π(s)∝∏_x Z(S_x(s))` by the pairing `∑_x s'_x·S_x(s)=∑_x s_x·S_x(s')`. Equilibrium FDR holds *for this Gibbs law*. It does **not** identify the linear AR response `χ=7/E` with the AR covariance `C=7/(2E(1-E/14))`: those are a different chain (a2).

**(b)–(d)** On the six-axis L=2 torus at `e^β=3`, exact cylinder masses of `π` (enumerated `6^8`): like two-pins (both `+z`) beat unlike (`+z,-z`) at nearest neighbour and at the body diagonal, with distinct ratios
\[
\frac{\pi(\text{like nn})}{\pi(\text{unlike nn})}=\frac{17179558853813045157374427641784866348978652410041}{47238316419587431650245082317077879359070521},
\]
and a different rational at the body diagonal. No isotropic `1/r` is visible on L=2. Mass = pinned menu value. Superposition fails: `log Z` is a many-body star potential. One-site marginal of `π` is uniform (`1/6`) by cube symmetry.

## (2) Steps

**Step 1 — pairing (PROVED; CHECKED as E1).** Reindex the undirected 7-stencil (self-loop plus six directed axis steps; on L=2 each axis partner has multiplicity 2).

**Step 2 — Gibbs ≠ AR (PROVED; CHECKED as E2).** `π` depends on `{|S_x|}`. The AR quadratic is a function of `E(k)` with mode-dependent `C`. One-site conditionals of `π` see neighbouring stars, not `1/(1-φ)`.

**Step 3 — two-pin masses (CHECKED as E3).** One pass over `6^8`. Like/unlike ratios `>1` and nn ≠ diagonal.

**Step 4 — mass and additivity (PROVED).** Pins are menu values. `log π = ∑ log Z(S_x)` is not pairwise.

## (3) First failing step, if any

L=2 cannot exhibit a `1/r` coefficient. Sphere `1/β` Hessian of `∑ log Z` is not computed (the six-axis torus is the exact finite model).

## (4) What would finish it

The Hessian of `∑_x log(4π sinh(β|S_x|)/(β|S_x|))` at an aligned configuration (IR `1/E` stiffness); two-pin `π` on L=4 (infeasible to enumerate `6^{64}`; needs Monte Carlo or spin-wave).
