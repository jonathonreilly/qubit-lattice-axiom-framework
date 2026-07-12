# Newton Potential-Kernel Algebra Packet on Z^3

**Date:** 2026-04 (2026-05-29 scope repair).
**Claim type:** bounded_theorem.
**Status:** bounded-support potential-kernel algebra; not a retained Newton force-law derivation.
**Primary runner:** `scripts/newton_law_potential_kernel_scope_check.py`
**Status authority:** independent audit lane only.

## 2026-05-29 Scope Repair

The conditional audit accepted the algebra once three premises were granted,
but found that the test-mass force/source coupling

```text
F = -M_test grad(phi)
```

was neither retained nor registered as an approved admission. Rather than
pretend the physical response bridge is closed, this repair removes the force
law from the load-bearing claim.

The row now proves only the exact potential-kernel algebra:

```text
G(r) = 1/(4 pi r),
phi(r) = M G(r),
|grad phi| = M/(4 pi r^2).
```

This is an inverse-square gradient of a supplied `1/r` scalar kernel. It is
not yet a physical Newton force law.

No new axiom is introduced. No observed gravitational value, fitted coupling,
or test-mass response rule is load-bearing.

## 2026-07-12 Dependency-Edge Repair

The In-Scope Theorem previously took the radial kernel `G(r) = 1/(4 pi r)` and
its source-linearity `phi = M G` as bare "supplied" premises with no cited
provenance, so the packet carried both without attribution. This repair
attributes them to the framework's own nearest-neighbor `Z^3` graph-Laplacian
Green-kernel normalization row,
[`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md),
which establishes `G` as the Green kernel `(-Delta_lat)^{-1}` of the linear
lattice Laplacian — the lattice potential of a unit point source. Because the
kernel is the resolvent of a linear operator, the source-linearity `phi = M G`
is that kernel's response to a source of strength `M`, not an independent
assumption. No new axiom, literature import, or physical force-law claim is
added; the class-A algebra below is unchanged.

## In-Scope Theorem

Let `r > 0`, `M` be a formal source coefficient, and define the supplied
radial scalar kernel

```text
G(r) = 1/(4 pi r).
```

This kernel is not free-standing: it is the large-separation normalization of
the framework's own nearest-neighbor `Z^3` graph-Laplacian Green kernel,
supplied by
[`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md).
That row identifies `G` as the Green kernel `(-Delta_lat)^{-1}` of the linear
lattice Laplacian, so the linear response below is a property of the supplied
kernel rather than a separate premise.

By source-linearity, the formal scalar potential is

```text
phi(r) = M G(r) = M/(4 pi r).
```

The radial derivative is

```text
d phi / dr = -M/(4 pi r^2).
```

Therefore the scalar gradient magnitude is

```text
|grad phi| = M/(4 pi r^2).
```

This is class-A algebra/calculus on the supplied kernel and source-linearity.

## Non-Claims

This row does not prove:

- the lattice Poisson equation as a physical equation of motion;
- the `Z^3` Green-kernel asymptotic from first principles;
- the test-mass force/source response rule `F = -M_test grad(phi)`;
- the physical product law `M_source M_test`;
- the gravitational coupling normalization;
- Newton's law as an unconditional framework output;
- continuum/null-geodesic/general-relativistic gravity claims.

Those are separate bridge problems. The old finite-lattice distance-law runner
remains useful exploratory support, but it is not the primary authority for
this narrowed row.

## Verification

Run:

```bash
python3 scripts/newton_law_potential_kernel_scope_check.py
```

Expected closeout:

```text
NEWTON_POTENTIAL_KERNEL_ALGEBRA=TRUE
POTENTIAL_GRADIENT_INVERSE_SQUARE=TRUE
PHYSICAL_FORCE_LAW_CLAIMED=FALSE
BA3_TEST_MASS_COUPLING_DERIVED=FALSE
ACTUAL_CURRENT_SURFACE_STATUS=BOUNDED_SUPPORT
```
