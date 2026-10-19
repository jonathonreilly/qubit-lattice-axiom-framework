---
claim_id: scale_ladder_gravity_records_to_geometry_lossless_passing_and_the_tick_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "Conditional finite lattice calculations for explicitly supplied response, segment-reading and update rules: neutralized periodic Green equations and checkerboard conjugacy; finite block means and converged Dirichlet cluster proxies; the exact segment identity M(k)C(k)=G(k) and its full-column-rank left-inverse consequence; specified leapfrog, variable-step, pulse-delay, Pauli-sine, heat and seeded periodic growth fixtures. Boundary contact, amplification and equation residuals are reported explicitly. Physical gravity/source identification, a framework update law, universal asynchronous or real-system exclusions, asymptotic growth isotropy and owner adoption are not established."
upstream_dependencies:
  - minimal_axioms
  - kinetic_isotropy_primitive
runner: scripts/scale_ladder_gravity_records_to_geometry_lossless_passing_and_the_tick_2026_10_18.py
---

# Finite lattice response, segment reading and supplied update rules

**Date:** 2026-10-18
**Claim type:** bounded_theorem.
**Primary runner:** `scripts/scale_ladder_gravity_records_to_geometry_lossless_passing_and_the_tick_2026_10_18.py`.

The models below are supplied mathematical hypotheses. In particular, lossless neighbor averaging is a chosen rule. No trusted owner adoption of that rule is established by this source. The original proposal, its exploratory physical interpretation, submitted cache and generated graph are preserved exactly in `archive/records_geometry_review_2026_10_18/`, with original identities in its manifest. That history supplies no current premise or fresh execution evidence.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) provide the stated lattice and local algebra, while the [kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) supplies only structural kinetic-form isotropy. The dynamics, Green-function source, metric reading, scalar pulse equation and growth probabilities used here remain separate supplied choices. The conditional scope comes from those choices, not from the registered foundations.

## Periodic response and block reading

Let A be the six-neighbor average on the even L³ periodic grid, and χ(x)=(-1)^(x₁+x₂+x₃). Its Fourier symbol is a(k)=(cos k₁+cos k₂+cos k₃)/3. Define the inverse of I−s q A by Fourier division away from singular modes, setting every singular component to zero. Here s=±1 and 0<q≤1.

At q=1 this definition gives the exact equations

    (I−A)d₊ = δ₀−1/L³,       sum_x d₊(x)=0,
    (I+A)d₋ = δ₀−χ/L³,       sum_x χ(x)d₋(x)=0.

These follow directly because the omitted eigenvector is constant for I−A and χ for I+A. In particular, summing the first equation gives zero on both sides; replacing its source by δ₀ would give an inconsistent equation. The second condition fixes the analogous checkerboard gauge. Since Aχf=−χAf and χδ₀=δ₀, uniqueness on the respective orthogonal complements gives d₋=χd₊. The runner checks the full finite arrays, both source residuals and both gauge conditions, and detects omission of the neutralizing source.

For 0<q<1, all denominators 1−s q a(k) are positive and the source is δ₀ without neutralization. At q=1−ε near k=0,

    1−(1−ε)a(k)=ε+(1−ε)|k|²/6+O(|k|⁴).

The quadratic continuum approximation therefore has screening length sqrt((1−ε)/(6ε)). At ε=0 its continuum Green kernel scales as 1/r. This is an approximation mechanism, not a proof that finite torus data have a universal 1/r tail or that two measured decay lengths certify an infinite-volume asymptotic. The runner's L=96 samples at ε=.03,.01 estimate a decay length from r=6,12 and compare their ratio with sqrt(3), using the stated finite tolerance.

The plain 2³ block average and the χ-weighted block average exchange d₊ and d₋ exactly by conjugacy. Their additional suppression ratio is measured at one declared block separation and reference block. These are explicit readout functionals, not a derivation of a physical observation channel.

## Finite Dirichlet source clusters

On a 41³ cube, boundary values are pinned to one. The interior equation uses the positive Dirichlet operator D=6I−neighbor-sum. A fixed drain of .01 per selected site corresponds to the source −.06 per selected site. Linearity gives exact superposition of source responses; equal far-field coefficients per source at different sites require a far-field approximation and are not an exact finite-box consequence of linearity.

The runner compares two sampled 1/r-shaped proxies for clusters of 1,19,33 sites. It separately solves the different boundary-value problem in which the cluster is pinned to .5. The latter's response depends on the full cluster geometry. Every conjugate-gradient solve must return status zero, finite entries and relative equation residual at most 2e−11 before any proxy comparison is accepted. These scalar responses are not identified with physical mass.

## Exact segment gauge-reading identity

The supplied four-dimensional path complex has the fifteen nonzero vectors v∈{0,1}⁴ as edge directions and ten independent symmetric tensor coordinates. Only those two constant inventories are taken from `scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py`; its Regge action, Hessian conclusions and main routine are not invoked.

For symmetric h and displacement ξ, define

    (M(k)h)_v = [(exp(i k·v)−1)/(i k·v)] vᵀ h v /(2|v|),
    (C(k)ξ)_ab = i(k_a ξ_b+k_b ξ_a),
    (G(k)ξ)_v = (exp(i k·v)−1)(v·ξ)/|v|.

The removable ratio has value one at k·v=0. Substitution gives M(k)C(k)=G(k), including at the removable points by continuity. This identity is valid for complex k with the stated bilinear coordinate convention; no complex conjugation is inserted into k·v. If M has full column rank ten, its Moore–Penrose left inverse L obeys LM=I and hence LG=C. Rank failure removes this last inference, not the original identity.

For a supplied symmetric tensor T, use weights one on diagonal and two off diagonal in its ten-coordinate pairing t. Then

    t C(k) ξ = 2i (kᵀT) ξ.

Thus a transverse T with kᵀT=0 gives zero pairing. At the runner's two complex momenta, kᵀk≠0, so Π=I−kkᵀ/(kᵀk) and T=Π e₄e₄ᵀ Πᵀ supply an explicit transverse example. The unprojected e₄e₄ᵀ is the finite comparison. Singular values, MC−G and LG−C are checked before the source pairings. This is a conditional algebraic identity; identifying a record-formation process with T or deriving its conservation remains a separate scientific task.

## Supplied time and propagation fixtures

For the leapfrog equation u_(j+1)=2u_j−u_(j−1)+Δu_j/n², a Fourier mode has

    z²−(2−λ/n²)z+1=0,      λ=4 sum_a sin²(k_a/2)∈[0,12].

Unit-modulus characteristic roots occur for 0≤λ/n²≤4. Consequently n=2 lies within the stability interval for every spatial Fourier mode, while n=1 contains growing modes. Repeated roots at endpoints require the usual initial-data care; the finite pulse test starts with equal consecutive fields. This criterion belongs to this discretization and sets no compulsory framework tick or physical light speed.

The seeded partially updated scheme and the coherent variable-step scheme are distinct supplied algorithms. For the former, the runner reports final peak radius and amplitude amplification separately. A large amplitude does not establish nonpropagation; a growing remote pulse explicitly defeats the original OR-based diagnostic. The coherent scheme is tested only for three finite pulse speeds with its chosen random steps in [.15,.55]. No exclusion of asynchronous integrators is inferred.

In one dimension, m u_tt=(k u_x)_x has local continuum speed sqrt(k/m). For the supplied weak well Φ<0, N=1+Φ and a=1−Φ, the lapse-only weights m=1/N,k=N give inverse speed 1/N=1−Φ+O(Φ²). The weights m=a³/N,k=Na give inverse speed a/N=1−2Φ+O(Φ²). Integrating the leading excess travel time gives ∫|Φ| and 2∫|Φ| respectively. The runner compares finite discrete pulse arrival times with those leading formulas. This calculation is a one-dimensional delay, not a bending-angle calculation.

The Pauli-sine propagator has H(k)=Σσ_a sin k_a and H²=Σsin²k_a I. Its exact exponential is cos(|s|t)I−i sin(|s|t)H/|s|, with its continuous limit at |s|=0. Finite t=30 shell probabilities on a 96³ torus are compared with the particular real scalar heat kernel exp(tΔ). This comparison establishes no general complex-versus-real propagation distinction: writing ψ=x+iy converts any complex linear first-order equation into a real first-order system for (x,y). The selected heat generator and Pauli generator simply differ.

## Finite periodic growth

The supplied rule occupies an empty neighbor of the existing cluster with probability p per tick, with a fixed seed. For p=1 and T=30 on the centered 81³ box, induction gives exactly the Manhattan ball |x|₁≤T, which does not meet the boundary. The runner verifies the whole occupied set against that formula.

The original p=.05, T=300 fixture is retained as a periodic-box diagnostic. The runner records the first occupied boundary site and counts cross-face neighbor proposals before reporting axis/body extent ratios and extent divided by elapsed ticks. Once contact occurs, periodic interactions can affect these quantities. The coordinate-derived extent is then not an unbounded front radius. One seeded periodic ratio establishes neither an asymptotic shape theorem nor isotropy across all directions.

## Verification and remaining scientific scope

Run the primary above once after source confirmation. It declares a 1200-second actual timer, literal input closure, fail-closed solver checks, named finite diagnostics and five resolution statements. Its final total is the actual check count; no new result is inferred from the historical nine-check cache.

The current constructive content consists of the explicit equations, segment identity and specified finite model tests. Physical action/source selection, physical record readout, clock dynamics, nonlinear gravity, continuum/unbounded limits and alternative integrators remain untested here. The original broad exclusions and exploratory records-to-gravity chain are preserved as deferred history, not active conclusions. Their old three-route checklist is not a complete negative-claim packet, and no replacement route families are invented.
