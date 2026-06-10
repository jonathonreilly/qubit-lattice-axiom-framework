# Hydrogen/Helium Atomic Companion -- Lattice-Kinetic Dependency Repair

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Review boundary:** source-note candidate. Later independent review sets the
ledger state; this note does not set or predict it.
**Primary runner:** [`scripts/frontier_hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_verifier.py`](../scripts/frontier_hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_verifier.py)

## Purpose

This companion repairs a narrow dependency and scope problem in
`work_history/atomic/HYDROGEN_HELIUM_ATOMIC_COMPANION_NOTE_2026-04-18.md`.
The parent atomic note uses the scalar lattice Hamiltonian

```text
H_g = -Delta_lat - g/|r|
```

on finite `Z^3` boxes. The repair has three parts:

- route the scalar graph-Laplacian stencil through the lattice Green-function
  source note rather than through broad gravity prose;
- record the four-line Coulomb-kernel arithmetic that turns the lattice
  Green-function asymptote into `V(r) = -g/|r|`;
- remove two unsupported framings from the load-bearing chain: that Quantum plus
  Lattice uniquely produce this scalar `-Delta_lat`, and that the finite-box
  readout proves a finite Rydberg series.

This is a companion repair only. It does not edit the parent note, does not add
an axiom or primitive, does not add a Tier-A input, and does not change any
consumer row's generated status. The Lattice/Quantum/Record baseline is kept
separate from the atomic dependency: Lattice supplies the `Z^3` graph, Quantum
supplies the one-qubit operator algebra, and Record is not used to derive the
scalar atomic Hamiltonian.

## Source Dependencies

Load-bearing links:

- [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md) fixes the
  current named baseline: Lattice, Quantum, and Record.
- [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md)
  supplies the nearest-neighbor `Z^3` graph-Laplacian stencil and the
  `G(r) -> 1/(4 pi |r|)` asymptote used below.
- [`STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md)
  supplies the staggered Hermitian-lift comparison surface used only for the
  scope disambiguation in section 3.

Target row label, not a source-graph dependency:

- `work_history/atomic/HYDROGEN_HELIUM_ATOMIC_COMPANION_NOTE_2026-04-18.md`
  is the parent note whose dependency chain this companion narrows.

## 1. Scalar Lattice-Kinetic Stencil

The scalar kinetic operator used by the parent runners is the nearest-neighbor
graph Laplacian on `Z^3` finite boxes:

```text
(-Delta_lat f)(x) = 6 f(x) - sum_{|y-x|=1} f(y).
```

The verifier checks that the parent-style Kronecker construction of
`build_graph_laplacian(N)` matches this site-by-site stencil at `N = 4`,
including diagonal value `6` and nearest-neighbor entry `-1`.

This routing is deliberately weaker than a derivation of `-Delta_lat` from the
framework baseline. No such derivation is claimed here. The scalar graph
Laplacian is the named lattice-kinetic source dependency used by the atomic
finite-box computation.

## 2. Coulomb-Kernel Arithmetic

Let `G(r)` denote the lattice Green function for `-Delta_lat`, with asymptote

```text
G(r) -> 1/(4 pi |r|)
```

at large separation. For a unit negative point source of strength `g`, define

```text
(-Delta_lat) V_lat = -4 pi g delta_{x,x0}.
```

Then by the Green-function definition,

```text
V_lat(r) = -4 pi g G(r).
```

Substituting the asymptote gives

```text
V_lat(r) -> -4 pi g * 1/(4 pi |r|) = -g/|r|.
```

This is exactly the parent potential term. The same arithmetic gives the helium
kernel forms by charge substitution and translation invariance of the stencil:
`V_nuc(r) = -Z g_EM/|r|` and
`V_ee(r1,r2) = +g_EM/|r1-r2|`.

## 3. Scope Disambiguation

The scalar `-Delta_lat` in the parent is not the square of the staggered Dirac
Hamiltonian used in the staggered surface.

The verifier builds the Kogut-Susskind phased real anti-Hermitian hopping
operator `D` on a `4^3` periodic torus and compares
`H_Dirac^2 = -D^2` with the scalar graph Laplacian. The matrices differ:

- the diagonal entries are `1.5` for `H_Dirac^2` and `6` for `-Delta_lat`;
- nearest-neighbor entries cancel in `H_Dirac^2` but are `-1` in `-Delta_lat`;
- distance-2 axis entries appear in `H_Dirac^2` and are absent from
  `-Delta_lat`.

So the parent atomic computation should be read as a scalar finite-box
Hamiltonian sourced by the graph-Laplacian dependency above, not as a unique
consequence of the staggered Dirac square.

The parent runner's finite-Rydberg wording is also narrowed. The finite-box
readout checks low-level ratios against an `n^-2` pattern on a finite grid; it
does not prove a finite continuum Rydberg series. In the continuum Coulomb
problem the attractive `1/r` potential has infinitely many bound states, so
"finite" refers only to finite-grid truncation.

## 4. Residuals

This companion does not supply helium Hartree or Jastrow cached runs, does not
edit the parent note, does not claim continuum-limit closure, and does not make
absolute-eV predictions. Those remain separate source tasks.

The intended repair is narrow: the atomic parent now has a clean source path for
the scalar `-Delta_lat` and Coulomb kernel used by its finite-box runners, plus a
recorded counterexample showing why that scalar operator should not be described
as the staggered Dirac square.
