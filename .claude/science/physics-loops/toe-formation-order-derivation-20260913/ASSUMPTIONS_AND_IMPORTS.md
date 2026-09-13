# Assumptions and imports

Baseline: `origin/main` `b8c9d9d819`. Axiom memo
`docs/MINIMAL_AXIOMS_2026-06-29.md` last changed `f1d08841be`.
Approved primitives: `scale_reference_primitive`,
`kinetic_isotropy_primitive`, `realized_state_primitive`.

## Load-bearing premises

- Lattice, Qubit, Admissibility, Record as written.
- `realized_state_primitive` for the registered-data reading of
  order-dependent statistics. Not used in Lemma C, the exchange
  characterization, or the path3 polynomial.

## Declared scaffolding (not imports)

- proper cubic group as signed permutations of determinant `+1`;
- records-only reading of partial neighbourhoods;
- isotropic binary kernels `f(m,k)`;
- one witness kernel, Ising-type with `e^J = 2`.

## Explicitly not used

Hamiltonian, action, carrier, clock, formation unit, rate, Born weights,
Gauss kernel, readout instrument, uniform mixture over orders, any
unapproved primitive.

## Counterfactual pass

| Assumption | What if wrong | Alternative | Direction |
|---|---|---|---|
| sequential single-site formation | records form jointly on covariant sets | joint formation | clause 2 |
| records-only partial neighbourhoods | absence is a condition | absence-as-condition kernels | later block |
| isotropic count kernel | cubic orbits of direction pairs are used | still forced constant on each orbit by path3 and L | Theorem 3 |
| interior `(0,1)` conditionals | deterministic 0/1 kernels | unclassified boundary | named residual |
| binary alphabet | Bloch / six-projector menu | later alphabet blocks | campaign queue |
