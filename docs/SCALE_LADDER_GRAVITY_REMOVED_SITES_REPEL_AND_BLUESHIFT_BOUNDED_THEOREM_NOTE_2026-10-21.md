---
claim_id: scale_ladder_gravity_removed_sites_repel_and_blueshift_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Rayleigh minimum monotonicity under principal restriction of a fixed finite symmetric stiffness matrix, plus fixed seeded Dirichlet-grounding numerical diagnostics of transmitted squared-amplitude centroids and confined-mode frequencies. No physical force, clock or density identification."
runner: scripts/scale_ladder_gravity_removed_sites_repel_and_blueshift_2026_10_21.py
---

# Dirichlet grounding: finite centroid diagnostics and a spectral restriction lemma

Claim type: bounded_theorem.
Primary runner: `scripts/scale_ladder_gravity_removed_sites_repel_and_blueshift_2026_10_21.py`.

The filename and claim identifier are historical handles. The results below concern a supplied scalar lattice model, not generic repulsion or a physical frequency shift. All dynamics, grounding rules, geometry, initial data and readouts are supplied model choices; no candidate-law clause or framework axiom determines them.

## Fixed model and readout

On a periodic 360 by 200 grid, X=i-180 and Y=j-100, evolve d2u/dt2 = Lap u - m^2 u. The four-neighbor Laplacian retains diagonal -4, including at live sites adjacent to grounded sites. Grounded sites have amplitude and velocity zero. This is Dirichlet grounding (principal restriction of the stiffness), not induced-graph edge deletion: the latter also reduces neighboring diagonal entries. On a three-vertex path, grounding the middle leaves stiffness diag(1,1) on the endpoints; deleting the middle and its incident edges leaves the zero matrix. Their eigenvalues differ.

Packet grounding masks use NumPy default_rng seed 5 inside the disk hypot(X-60,Y)<20, with Bernoulli probabilities f=.005,.01,.02; these are not exact realized grounded percentages. Reusing the same random draws makes the masks nested. The packet envelope is exp(-(X+100)^2/(2*14^2)-(Y-26)^2/(2*10^2)); initial fields are u=envelope*cos(kX), v=omega*envelope*sin(kX), both restricted to live sites. The supplied (m,k) pairs are (0,.5) and (.5,.95). Here omega=sqrt(m^2+4 sin^2(k/2)) and vg=sin(k)/omega are the semidiscrete dispersion frequency and group speed. They are not exact numerical packet speeds.

The velocity-first symplectic Euler update uses dt=.25 for floor((260/vg)/dt) steps, ending at that step count times dt. The runner reports these times. The supplied stability bound dt*sqrt(8+.5^2)<2 holds, but no time-step or continuum convergence study is provided. At the final time the detected region is X>120. The readout is C=sum_detected(Y*u^2)/sum_detected(u^2), and the detected fraction is sum_detected(u^2)/sum_all(u^2). This is instantaneous squared field amplitude, not energy, flux, a trajectory, or a force.

For the fixed masks, the centroid changes C(f)-C(0), in sites, are approximately:

| Mass | f=.005 | f=.01 | f=.02 |
|---|---:|---:|---:|
| 0 | +3.96 | +9.98 | +14.50 |
| .5 | +3.86 | +5.63 | +9.01 |

The runner reports all corresponding detected fractions and actual mask counts. Positive changes are numerical properties of these six readouts only. They establish no sign for arbitrary seeds, momenta, impact parameters or forces.

The separate spectral experiment uses a 61 by 61 box centered at zero and a fixed outer Dirichlet disk hypot(X,Y)<28. Interior grounding uses radius 20, the same three probabilities, and seed 9. The stiffness has diagonal 4 and off-diagonal -1 for adjacent live sites; outside-disk values are zero. For supplied mass .1, the scalar confined-mode frequency is sqrt(.1^2+lambda_min). Relative to the ungrounded disk the three relative frequency changes are approximately .05903, .23219 and .49803. This is not a physical body or clock model.

## Spectral restriction lemma

Let L be a fixed finite real symmetric matrix, and let nonempty coordinate sets S' be a subset of S. Then lambda_min(L[S',S']) >= lambda_min(L[S,S]). For any nonzero vector on S', extend it by zero on S minus S'. Its Rayleigh quotient for L[S,S] equals its quotient for L[S',S']. Minimizing over these extended vectors restricts the minimization domain, proving the inequality. Disconnected sets are allowed; empty sets are excluded. If a fixed m^2 is added and both resulting lowest eigenvalues are nonnegative, taking square roots preserves the inequality. Strict increase is not asserted.

Applied to the nested seed-9 masks with the same parent stiffness and outer boundary, this proves nondecrease of the lowest frequency. The numerical strict increases above are observations for those masks. The lemma does not concern the induced-edge-deletion operator, which changes the parent diagonal, and says nothing about packet-shift signs.

## Evidence boundary

The independent saved computation used a sparse incidence Gram matrix and a second-order displacement recurrence for the packet, and a smallest-algebraic eigenvalue solve for the disk. The runner compares with those independently computed values at their stated decimal precision; these are regression checks, not proofs or convergence estimates. Source/input hashes bind the exact configuration and cache. The three-path grounding counterexample is also checked directly. Independent source review of this corrected packet remains required; no audit status is assigned.

There is no density-to-record bridge, physical-clock map, gravitational response or proof that an additional long-range field is necessary. Such physical identifications remain outside this diagnostic. Original broader claims are preserved in the original PR history and are not conclusions of this note.
