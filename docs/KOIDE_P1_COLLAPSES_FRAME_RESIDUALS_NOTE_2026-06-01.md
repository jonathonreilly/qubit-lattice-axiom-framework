# Koide Finite Carrier-Frame Residual Boundary

**Date:** 2026-06-01 (finite-boundary repair 2026-06-15)
**Claim type:** bounded_theorem
**Claim boundary:** finite carrier-frame diagnostics only. The repaired row
checks four finite statements:

1. supplied faithful spin-1/2 one-mode input gives a soft-Bose-vs-CAR
   positive-energy discriminator;
2. the retained cardinality obstruction
   [`SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md`](SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md)
   is blind to a hard-core boson realized by the same single-site `sigma_+`
   matrix;
3. a finite scalar/RP-kernel witness is positive-energy and positive
   semidefinite in the runner's toy surface;
4. the nearest-neighbour bilinear spectra agree between the JW-fermion and
   hard-core-boson frames.

This note does not supply or import a retained continuum spin-statistics
theorem, OS/Wightman reconstruction theorem, GL(F) supplier, or scalar
microcausality theorem. It does not force faithfulness and it does not reduce
the retained carrier-frame residual count to zero.

**Primary runner:**
[`scripts/frontier_koide_p1_collapses_frame_residuals.py`](../scripts/frontier_koide_p1_collapses_frame_residuals.py)
with cache
[`logs/runner-cache/frontier_koide_p1_collapses_frame_residuals.txt`](../logs/runner-cache/frontier_koide_p1_collapses_frame_residuals.txt)
(14/14 checks).

## Source-Scope Repair

The prior packet was conditionally useful but still read like a bridge through
continuum spin-statistics and OS/RP reconstruction authorities. The current
audit finding was:

```text
missing_bridge_theorem: cheapest repair is to provide retained one-hop scalar
OS/microcausality and spin-statistics/GL(F) supplier notes, or narrow this row
to the finite soft-Bose/CAR and hard-core-blindness computations only.
```

This repair chooses the second path. It keeps the finite diagnostics and removes
the field-theoretic bridge claim from the load-bearing surface. The named
spin-statistics, OS/Wightman, GL(F), and scalar microcausality rows remain
future audit targets, not dependencies of this repaired bounded row.

## Finite Diagnostics

### A. Supplied Faithful Spin-1/2 Input Discriminates Soft Bose From CAR

Given a supplied faithful spin-1/2 one-mode spectrum with a negative-energy
branch, soft Bose occupation is unbounded below as the occupation cap grows,
while CAR occupation is bounded by construction in the runner's normal-ordered
finite check. This is a finite algebraic discriminator under the supplied
faithful-spin input. It is not a derivation of that input and not a continuum
spin-statistics theorem.

### B. Hard-Core Boson Blindness

The single-site hard-core boson `b = sigma_+` and the single-site fermion
ladder `c = sigma_+` use the same 2x2 matrix and both square to zero. The
soft-CCR cardinality obstruction checks `[a,a^dagger] = I`; the hard-core
matrix has traceless commutator and therefore evades that obstruction. This
runner-checked fact is the bounded retained-tier caution: cardinality alone
does not select the cross-site exchange sign.

### C. Scalar Toy Witness

The runner checks a finite scalar witness: `omega_k = sqrt(k^2 + m^2) > 0` on
the sampled grid and an OS-reflected rank-one Kallen-Lehmann-style kernel is
positive semidefinite on the sampled Euclidean times. This is a toy witness
that the present finite packet has not excluded the scalar alternative. It is
not a retained continuum scalar field theorem and not a microcausality theorem.

### D. Nearest-Neighbour Spectrum Relabel

For the two-site nearest-neighbour bilinear, the hard-core-boson frame and the
JW-fermion frame have identical spectra. This is a finite spectrum/unitary
relabel statement. It is not a claim that all bounded-local commutators or
dynamics are byte-identical across the two frames.

## Result

The repaired row supports only this bounded boundary map:

```text
finite faithful-spin input -> soft-Bose/CAR positive-energy discriminator
cardinality obstruction -> hard-core boson remains unexcluded
finite scalar toy witness -> this packet does not force faithfulness
NN spectrum check -> bounded-local spectrum is exchange-sign blind
```

The row no longer claims that microcausality/reflection positivity or
spin-statistics has been supplied as a retained one-hop bridge. Therefore the
current retained-tier conclusion is conservative: the finite packet identifies
where the residuals sit, but it does not close them.

## Non-Claims

This note does not:

- prove continuum spin-statistics;
- prove continuum OS/Wightman reconstruction;
- prove GL(F) reconstruction;
- prove scalar microcausality;
- derive the faithful spin-1/2 matter representation;
- derive the physical charged-lepton readout;
- apply an audit verdict or edit `docs/audit/**`.

## Runner Certificate

The runner verifies:

- the source-scope firewall above is present;
- the faithful-spin input is explicit and supplied;
- the row is narrowed to finite diagnostics only;
- soft Bose is unbounded under increasing occupation cap;
- CAR is bounded in the finite normal-ordered check;
- hard-core boson `sigma_+` evades the soft-CCR cardinality obstruction;
- the scalar toy witness is positive-energy / PSD on the sampled surface;
- the nearest-neighbour bilinear spectra match across the two finite frames.

Expected output:

```text
14/14 checks passed.
```

## Future Work

To use this lane for a retained carrier-frame closure, a later source packet
would still need retained one-hop suppliers for the physical matter carrier,
continuum spin-statistics or an approved lattice replacement, and any
OS/Wightman/GL(F) bridge meant to be load-bearing. This note intentionally does
not provide those bridges.
