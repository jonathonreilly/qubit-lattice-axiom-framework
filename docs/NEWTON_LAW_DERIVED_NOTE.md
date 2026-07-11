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

## Premise wiring (2026-07-11)

The two granted premises now carry explicit authorities:

- **Kernel form.** The supplied radial scalar kernel `G(r) = 1/(4 pi r)` is
  the continuum-limit asymptotic normalization of the `Z^3` graph-Laplacian
  Green function carried by the retained-bounded import authority
  [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md),
  cited at its bounded scope: this note consumes only the functional form
  `1/(4 pi r)` of the leading asymptotic, not any first-principles
  derivation claim (which that authority explicitly does not make).
- **Source-linearity.** Registered as an explicit accepted premise:

```text
(P-LIN)  Source-linearity accepted-premise entry (2026-07-11).
         The formal scalar potential responds linearly to the formal
         source coefficient: phi(r) = M G(r). This is a modeling premise
         of the potential-kernel algebra packet; it is registered, not
         derived, and no superposition dynamics is claimed.
```

**Status:** accepted-premise packet entry. Deriving source-linearity from a
lattice field equation (and the physical response bridge listed under
Non-Claims) remains outside this row.

## In-Scope Theorem

Let `r > 0`, `M` be a formal source coefficient, and define the supplied
radial scalar kernel

```text
G(r) = 1/(4 pi r).
```

(kernel form per the wired import authority above). By source-linearity
(P-LIN), the formal scalar potential is

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

This is class-A algebra/calculus on the wired kernel authority and the
registered source-linearity premise (P-LIN).

## Repair Note

**2026-07-11 premise wiring.** The audit of this row returned
`audited_conditional` with, verbatim:

> missing_dependency_edge: cite a retained-grade or explicitly accepted
> premise establishing the supplied kernel and source-linearity, then
> re-audit the updated note.

Both granted premises are now carried explicitly: the kernel form is wired
(markdown link = dependency edge) to the retained-bounded `Z^3`
Green-asymptotic import authority at its bounded scope, and source-linearity
is registered as the explicit accepted premise (P-LIN). No claim content
changed; the narrowed potential-kernel algebra and every Non-Claims item are
exactly as before. This dated line moves the note hash so the row re-enters
for re-audit.

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
