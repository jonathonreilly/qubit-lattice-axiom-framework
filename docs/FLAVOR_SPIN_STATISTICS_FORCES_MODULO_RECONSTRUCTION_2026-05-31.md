# Flavor Spin-Statistics Reconstruction Boundary Packet

**Date:** 2026-05-31; source-boundary repair 2026-06-07.
**Claim type:** bounded_theorem
**Actual current-surface status:** bounded-support.
**Trace class:** negative_route_pruning.
**Reachability to target:** prunes the route "the spin-statistics engine alone
forces the fermionic frame P1 from current baseline plus emergent spacetime."
**Bare retained allowed:** false.
**Audit required before effective status change:** true.
**Runner:** `scripts/flavor_spin_statistics_forces_modulo_reconstruction_2026_05_31.py`
(SCORECARD PASS=7 FAIL=0).

## Repaired Claim

This packet keeps the real bounded content and removes the current-surface
promotion that P1 is forced modulo a named reconstruction.

What closes:

1. For a **supplied relativistic spin-1/2 field with the usual particle /
   antiparticle sign structure**, the spin-statistics engine is genuine:
   wrong Bose quantization has an unbounded-below energy direction, while CAR
   occupation is bounded in the finite check.
2. A clean Dirac-block/taste decomposition can realize taste as spectator
   multiplicity rather than as spin-mixing; the Becher-Joos/Dirac-Kahler
   obstacle is therefore not a blocker for that supplied clean block.
3. The on-site qubit carries the spatial `SU(2)` spin-1/2 representation under
   `sigma_i/2`.
4. The tested UV-lattice data do **not** force cross-site CAR/Grassmann
   statistics: ordinary qubit ladders commute across sites, Jordan-Wigner
   dressed generators anticommute after a representation choice, and the free
   propagator kernel used in the check is statistics-blind.

Therefore the current framework packet supports a bounded route-pruning
statement:

```text
T1 spin-statistics engine + clean supplied relativistic spinor field
  -> excludes wrong Bose quantization for that field

current baseline + emergent spacetime alone
  -/-> non-circular P1/CAR forcing
```

In short: the repaired packet does not force P1 from current baseline.

The missing ingredient remains a non-circular reconstruction `R` that turns the
statistics-blind lattice kernel into a positive-energy, microcausal,
Poincare-covariant spinor field with the needed antiparticle sign structure,
plus a bare-qubit boost-spinor embedding that does not rely on an already
chosen Grassmann/staggered fermion construction.

## What The Runner Verifies

- CAR occupation has bounded finite spectrum for the supplied spinor field.
- Wrong Bose quantization on the same sign structure has an unbounded-below
  direction in the finite truncation.
- Taste can enter as four identical spectator copies of a clean spinor block.
- The free kernel matrix identity is statistics-blind.
- Ordinary two-site qubit ladders commute, while Jordan-Wigner dressed
  generators anticommute after a generator/string choice.
- `sigma_i/2` on a qubit has the `j=1/2` Casimir.
- The note boundary forbids promoting P1 as forced on the current surface.

These are finite algebra checks and hostile counterexamples. They are not a
replacement for a retained spin-statistics reconstruction theorem.

## What This Does Not Claim

This packet does not claim:

- P1 or cross-site CAR is forced from the current baseline axioms;
- the full Lorentz boost action on the bare qubit is derived;
- the free-field OS/Wightman reconstruction `R` is complete;
- the charged-lepton flavor sector closes from the current surface;
- any new axiom, owner admission, or audit status.

If a later retained theorem supplies `R` and a non-circular boost-spinor
embedding, the T1 engine recorded here can become a downstream forcing step.
Until then, the current retained content is the bounded engine plus the
negative UV back-propagation result.

## Provenance

- The runner checks the T1 finite spectrum, taste spectator multiplicity,
  statistics-blind kernel identity, statistics-agnostic lattice carrier, and
  spatial spin-1/2 Casimir.
- The packet is consistent with the existing FS/CAR admission fork: supplied
  Grassmann/CAR variables realize determinant amplitudes, but their selection
  is not derived here.
- No `docs/audit/**` status is updated by this repair.
- No new axiom is introduced.
