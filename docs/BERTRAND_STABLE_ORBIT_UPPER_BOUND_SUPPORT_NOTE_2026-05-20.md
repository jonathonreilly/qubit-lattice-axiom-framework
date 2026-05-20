# Bertrand Stable-Orbit Upper-Bound Support

**Date:** 2026-05-20
**Claim type:** bounded_theorem
**Status:** source-side proposal; independent audit lane only
**Related wrapper:** `DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`

## Claim Boundary

This note records a bounded support argument for the stable-orbit half of the
D=3 upper-bound route. It does not claim a repo-wide axiom change and it does
not claim a complete framework-internal proof of Bertrand's theorem.

The landable support claim is narrower:

> Given a continuum central potential of the form `V(r) = -k/r^(d-2)` with
> `k > 0`, the effective-potential stability calculation gives stable
> circular orbits only for integer `d = 3`; `d = 4` is marginal and `d >= 5`
> is unstable.

This supports the existing named-import wrapper by making the elementary
stability part explicit. The all-bounded-orbits-are-closed part of Bertrand's
theorem remains standard classical mechanics unless separately derived and
audited.

## Inputs

1. **Framework-connected potential form.** The source of the dimensional
   potential pattern is [`DIMENSIONAL_GRAVITY_TABLE.md`](DIMENSIONAL_GRAVITY_TABLE.md).
   Its audited binding scope is cache-backed `d = 3` and `d = 4` rows; use of
   a general `d` continuum law is therefore an explicit bounded extrapolation,
   not a retained universal theorem.
2. **Standard classical mechanics.** The effective-potential reduction for a
   central force is admitted background. This note writes out the stability
   algebra but does not re-derive Hamiltonian mechanics.
3. **Bertrand closure theorem.** The exact all-`L` closed-orbit theorem is a
   standard classical-mechanics import. It is not retired by this note.

## Effective-Potential Calculation

For a central potential

```text
V(r) = -k / r^(d-2),      k = GMm > 0,      d >= 3,
```

the radial effective potential is

```text
V_eff(r) = -k / r^(d-2) + L^2 / (2 m r^2).
```

A circular orbit at `r_c` requires

```text
dV_eff/dr = k(d-2)/r_c^(d-1) - L^2/(m r_c^3) = 0.        (1)
```

The second derivative is

```text
d^2V_eff/dr^2 = -k(d-2)(d-1)/r^d + 3L^2/(m r^4).         (2)
```

Using (1) to eliminate `L^2` gives

```text
d^2V_eff/dr^2 |_{r_c} = k(d-2)(4-d) / r_c^d.             (3)
```

So stable circular orbits require

```text
(d-2)(4-d) > 0.
```

For integer `d >= 3`, this holds only at `d = 3`. The `d = 4` case is
marginal and `d >= 5` is unstable.

## Relation To Dimension Selection

This note can support the upper-bound side of `DIMENSION_SELECTION_NOTE.md`
only in the bounded sense above. It does not by itself prove that the physical Cl(3) local
algebra on the `Z^3` spatial substrate should be replaced by a `Z^d` substrate,
and it does not close the D=3 chain.

The companion bounded support note
`COULOMB_STABILITY_UPPER_BOUND_SUPPORT_NOTE_2026-05-20.md` records the
atomic-stability route. The lower-bound bridge and single-clock uniqueness
gaps remain open as described in `D3_RETENTION_CLOSURE_PLAN_2026-05-20.md`.

## What This Does Not Close

- It does not retire the Bertrand theorem import completely.
- It does not establish a retained universal dimensional-gravity law for all
  integer `d`.
- It does not settle `d = 1` or `d = 2`; those belong to the separate
  lower-bound bridge.
- It does not promote any parent row or audit status.
