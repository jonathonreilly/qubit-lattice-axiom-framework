# Handoff

This branch repairs the free-staggered SO(4) row without narrowing it.

The new runner Part 0 constructs the 16 hypercube components
`b in {0,1}^4`, applies the momentum-local rephasing
`chi_b(p)=exp(i a p.b) zeta_b(p)`, and verifies that the canonical
staggered difference is exactly
`i sin(p_mu a)/a alpha_mu`. It then verifies that the generated
`alpha_mu` algebra is 16-dimensional with a 16-dimensional commutant,
which is the finite taste spectator identity.

Pipeline result: the target row is reset to `unaudited`, queue-ready,
with `open_dependency_paths=[]`. Independent audit is still required
before any effective retained status.
