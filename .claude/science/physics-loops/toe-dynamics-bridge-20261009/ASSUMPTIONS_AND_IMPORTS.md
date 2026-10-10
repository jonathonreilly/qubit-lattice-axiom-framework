# Assumptions and imports

The foundation and approved primitive scopes are unchanged. New mathematics is
permitted; no Hamiltonian, carrier, clock or collision law is adopted as an axiom.

| Unit | Explicit supplied data | Provenance and open physical interface |
|---|---|---|
| Existing linear hydrodynamic theorem | D3Q27 velocities/energy, positive rates, Gibbs reference, torus streaming, regularity/preparation | The supplied collision parent and the branch's independently checked theorem; native identification is open |
| Existing graph quantum/mixing theorem | 27-level registers, connected mixing graph, local marks, ancillas, fast interchange and clock | Earlier theorem in this PR; its graph is a mixing-slot graph and has no spatial streaming interpretation |
| New spatial particle/kinetic theorem | Position/velocity particles, mass and multiple occupancy, directed local hops, co-located binary events, rates, clocks, initial law | Constructed explicitly here; fixed-amplitude PDE result has a stated classical lifetime and fixed prefactors |
| New spatial quantum theorem | Labelled position/velocity tensor factors, separately marked instruments, fresh ancillas, ordering and clock | Constructed explicitly here; addressable particle pairs and supplied spatial labels are not a native one-qubit-per-site encoding |
| New simultaneous fluid theorem | Tuned nine-reaction rate, Gibbs preparation, mean-zero density fluctuation, divergence-free momentum, H4 data, vanishing amplitude and joint scales | New stopped dissipative proof plus the prior H4 theorem and new quantum bound; the physical rate selection and autonomous carrier remain open |

The new spatial quantum generator gives exact local occupation dynamics with
no rapid global mixing assumption. The old mixing theorem remains a separate
mathematical model and is not silently assigned a spatial continuum limit.
The new near-equilibrium proof supplies that conditional composition for the
new spatial model. Its classical claim concerns a whole stochastic path;
its finite quantum schedule concerns a uniform choice of one measurement time.

Mathematical tools are finite operator/counting identities, jump martingale
energy estimates, local semilinear existence, Sobolev product bounds, and
contractive semigroup comparisons. Their uses and hypotheses are written in
the notes and selectively checked independently. No external persistence,
long-time kinetic or Lean theorem is needed by these new proofs. No empirical
observable, measured viscosity, global nonlinear PDE or nonlinear fluid limit
is inferred. Source hashes and review coverage are in the handoff and identity
record. Conditional use does not grant unaudited dependencies retained authority.
