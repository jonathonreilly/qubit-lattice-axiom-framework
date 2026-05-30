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

## In-Scope Theorem

Let `r > 0`, `M` be a formal source coefficient, and define the supplied
radial scalar kernel

```text
G(r) = 1/(4 pi r).
```

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
