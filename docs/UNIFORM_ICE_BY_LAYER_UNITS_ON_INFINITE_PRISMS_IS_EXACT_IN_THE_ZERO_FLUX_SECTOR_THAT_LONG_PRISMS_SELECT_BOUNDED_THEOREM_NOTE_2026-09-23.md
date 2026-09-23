---
claim_id: uniform_ice_by_layer_units_on_infinite_prisms_is_exact_in_the_zero_flux_sector_that_long_prisms_select_bounded_theorem_note_2026-09-23
claim_type: bounded_theorem
claim_scope: "Integer transfer T[v,w] counts in-plane ice completions between vertical layers, so trace(T^H) counts periodic-prism states. For2x2, traces at H=2,3,4 are9600,219776,23063296; the last agrees with transfer along another axis. On an even bipartite transverse torus, staggered flux flips sign at each layer.  For2x2, the positive zero-flux block has exact characteristic polynomial (x-6)(x+10)(x+14)^2(x^2-64x+188), top lambda=32+2sqrt(209), and next modulus14. Nonzero-flux blocks have dominant pairs \u00b146 and \u00b118. Their share vanishes for odd H and is asymptotic to2(46/lambda)^H for even H. Numerical kernel deviations are tested at H=4,8,12,16.  The limiting zero-flux chain has P(w|v)=T[v,w]phi(w)/(lambda phi(v)), initialized with stationary weights proportional to phi(v)^2. Conditional on v,w, choose uniformly among the T[v,w] in-plane completions to recover the full link measure. The2x4 zero block has a positive square; numerical eigenvalues show top2401.3316, next modulus668.3638 and nonzero-flux tops at most2059.36. The3x3 control has alternating vertical occupation parity and zero odd-height trace; it does not establish mixing of a two-step chain. Layer units here are a supplied coarse link-layer model. Adding deterministic coordinator records need not preserve schedulability on a finer neighbour graph. Staggered flux requires an even bipartite cross-section. Numerical spectral estimates are labelled separately from exact integer identities. Infinite height at fixed cross-section is not an infinite-cross-section Coulomb phase."
upstream_dependencies:
  - minimal_axioms
runner: scripts/uniform_ice_layer_units_on_infinite_prisms_zero_flux_transfer_chain_2026_09_23.py
---

# Transfer construction of stationary zero-flux ice measures on thin prisms

**Date:** 2026-09-23
**Type:** bounded_theorem

## Result and scope

Integer transfer T[v,w] counts in-plane ice completions between vertical layers, so trace(T^H) counts periodic-prism states. For 2x 2, traces at H=2, 3, 4 are 9600, 219776, 23063296; the last agrees with transfer along another axis. On an even bipartite transverse torus, staggered flux flips sign at each layer.

For 2x 2, the positive zero-flux block has exact characteristic polynomial (x-6)(x+10)(x+14)^2(x^2-64x+188), top lambda=32+2 sqrt(209), and next modulus 14. Nonzero-flux blocks have dominant pairs ±46 and ±18. Their share vanishes for odd H and is asymptotic to 2(46/lambda)^H for even H. Numerical kernel deviations are tested at H=4, 8, 12, 16.

The limiting zero-flux chain has P(w|v)=T[v,w]phi(w)/(lambda phi(v)), initialized with stationary weights proportional to phi(v)^2. Conditional on v,w, choose uniformly among the T[v,w] in-plane completions to recover the full link measure. The 2x 4 zero block has a positive square; numerical eigenvalues show top 2401.3316, next modulus 668.3638 and nonzero-flux tops at most 2059.36. The 3x 3 control has alternating vertical occupation parity and zero odd-height trace; it does not establish mixing of a two-step chain.

## Boundaries and non-claims

Layer units here are a supplied coarse link-layer model. Adding deterministic coordinator records need not preserve schedulability on a finer neighbour graph. Staggered flux requires an even bipartite cross-section. Numerical spectral estimates are labelled separately from exact integer identities. Infinite height at fixed cross-section is not an infinite-cross-section Coulomb phase.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Conditional finite ice measures, formation and supplied transfer models"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Preserve finite hypotheses and test extensions separately"
conditional_surface_status: "The declared model, order, records and numerical tolerances only"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
claim_type_reason: "Conditional mathematics and bounded computation; no retained grade asserted"
```

## Premises and declared objects

- **Measure.** The uniform ice measure: 3 of each vertex's 6 links are
  occupied. The tested even cross-sections are 2x 2 and 2x 4; 3x 3 is a parity control.
- **Layer unit.** The in-plane links of one layer and the vertical links
  above it. The kernel is for this coarse link-layer model; deterministic extra
  records do not by themselves establish finer-graph schedulability.
- **Locality.** In the coarse layer model, the completed past enters
  through the vertical boundary word v; the stated Markov kernel uses
  only that word. This is not a claim about single-site schedules.
- **Arithmetic.** Exact integer transfer matrices, traces and
  annihilating polynomial. Eigenvectors and convergence are in floating
  point at stated tolerances.


## Theorem 1 — Transfer and flux

The ice rule at a layer's vertices involves only the in-plane links of that
layer and the vertical links just below and just above it. Summing over
the in-plane links gives T[v, w], and the ice states of the n × n × H
torus number trace T^H.

In-plane degrees sum to 3 n² − |v| − |w|, and that sum is twice the number
of in-plane links, so it is even. For an even bipartite cross-section, with the staggered sign, conservation
sharpens to S(w) = −S(v) whenever T[v, w] > 0. The runner checks this for
all 256 pairs at n = 2.


## Theorem 2 — The zero-flux chain

For 2x 2 the zero-flux block is positive, so its top eigenvalue is simple with a
positive eigenvector φ (Perron). The torus conditional of a layer given
the layer below (v) and the far end (a) is
T[v, w] (T^(H−2))[w, a] / (T^(H−1))[v, a]. It converges to
T[v, w] φ(w) / (λ φ(v)) at the rate of the second eigenvalue, 14/60.91 per
layer. The chain with this kernel is a nearest-neighbour chain of layer
units, and it reproduces the limit measure.


Use stationary initial weights phi(v)^2/sum(phi^2) and, conditional on
v,w, a uniform in-plane completion. Symmetry of T proves detailed balance.
The same construction applies to the primitive 2x 4 zero block; its quoted
spectral ordering and deviations are numerical checks. For 2x 2 the exact
nonzero-sector characteristic polynomials are
(x^2-46^2)(x^2-10^2)^2(x^2-6^2) and x^2-18^2.
Their leading trace terms prove the stated even-height flux-share asymptotic.

## No-go discipline and falsifiers

Negative claims concern only the stated fixed models and completed searches.
Alternative records, hidden state, adaptive orders, larger units, different
rules and different boundary conditions require separate tests. Caps must
not bind for an exhaustive verdict. Finite spectral patterns do not prove
infinite-cross-section physics. A counterexample under the exact hypotheses,
a failed independent count, or a failed stated control falsifies its result.
No other claim is graded, unlocked or audited here.

## Dependencies and provenance

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)

Original context and author review history remain recoverable from the
originating PR. Historical mutation claims are not current review evidence.
The landing review preserves conditional proofs and narrows unsupported
extensions; no new axiom, primitive or audit grade is adopted.

## Verification

```bash
python3 scripts/uniform_ice_layer_units_on_infinite_prisms_zero_flux_transfer_chain_2026_09_23.py
```

The runner exits nonzero on failure. Its fresh captured cache is
`logs/runner-cache/uniform_ice_layer_units_on_infinite_prisms_zero_flux_transfer_chain_2026_09_23.txt`.
Analytic statements require the proofs above in addition to finite checks.
