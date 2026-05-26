# Valley-Linear Continuum Synthesis Note

**Date:** 2026-04-04 (2026-05-26: continuum derivation packet and runner
added for audit requeue)
**Claim type:** bounded_theorem
**Status:** bounded synthesis of the valley-linear continuum bridge and
retained-bounded lattice evidence; not a theorem promotion
**Runner:** `scripts/frontier_valley_linear_continuum_synthesis.py`

## Purpose

This note is the current bridge between the analytic valley-linear derivation
and the frozen lattice artifacts on `main`.

It intentionally keeps three categories separate:

- what is derived
- what is retained-bounded numerically
- what is still open

That separation matters because the valley-linear lane is now stronger, but it
is still an architecture-aware branch rather than a settled universal claim.

## What is derived

The analytic derivation originally lived in
`.claude/science/derivations/valley-linear-distance-law-2026-04-04.md`.
For audit, the load-bearing continuum bridge is included here directly and
checked by `scripts/frontier_valley_linear_continuum_synthesis.py`.

It shows the following continuum statement for the valley-linear action
`S = L(1-f)` on the `1/L^(d-1)` lattice family:

- the field perturbation is linear in `f`
- the continuum phase shift integrates to a `1/b` deflection law in 3D
- the resulting distance law is Newtonian in the 3D continuum limit, up to
  the finite-size corrections of the discrete lattice

The derivation is the cleanest part of the current story:

- `S = L(1-f)` is the source of the linear-in-`f` behavior
- linear-in-`f` gives the right continuum scaling
- the lattice measurement then becomes a finite-resolution approximation to
  that continuum result

This is a derivation of the distance law in the continuum approximation. It is
not a proof that the full discrete model has no finite-size or architecture
dependence.

### Self-contained continuum bridge

Let the mass field be `f(r) = s/r` and let a path pass the source at transverse
impact parameter `b`. Along a straight continuum ray with longitudinal
coordinate `x`, `r(x,b) = sqrt((x - x_m)^2 + b^2)`.

For the valley-linear action,

```text
S = L(1 - f)
delta S = -L f
delta phi = -k L f
```

After absorbing the step-length normalization into the continuum integral, the
field-dependent phase along a path of length `L_phys` is

```text
delta Phi(b) = -k s integral_0^L_phys dx / sqrt((x - x_m)^2 + b^2)
             = -k s [asinh((L_phys - x_m)/b) + asinh(x_m/b)].
```

Differentiating with respect to `b` gives

```text
d(delta Phi)/db
  = k s [
      (L_phys - x_m) / (b sqrt((L_phys - x_m)^2 + b^2))
      + x_m / (b sqrt(x_m^2 + b^2))
    ].
```

In the wide-ray continuum regime `x_m >> b` and `L_phys - x_m >> b`, each
bracketed term tends to `1/b`, so

```text
d(delta Phi)/db -> 2 k s / b.
```

Thus the continuum deflection scale of the valley-linear action is `1/b` in
the 3D straight-ray approximation. The retained-bounded lattice notes below
remain finite-resolution evidence for this behavior, not a proof of universal
architecture independence.

## What is retained-bounded numerically

The retained-bounded lattice evidence comes from the already-frozen artifact
chains:

- [VALLEY_LINEAR_ACTION_NOTE.md](VALLEY_LINEAR_ACTION_NOTE.md)
- [VALLEY_LINEAR_ROBUSTNESS_NOTE.md](VALLEY_LINEAR_ROBUSTNESS_NOTE.md)
- [VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md](VALLEY_LINEAR_ASYMPTOTIC_BRIDGE_NOTE.md)
- [DIMENSIONAL_GRAVITY_TABLE.md](DIMENSIONAL_GRAVITY_TABLE.md)
- [DECOHERENCE_ACTION_INDEPENDENCE_NOTE.md](DECOHERENCE_ACTION_INDEPENDENCE_NOTE.md)

The strongest retained-bounded reads are:

| Result | Bounded read |
|---|---|
| 3D same-family action comparison | Valley-linear improves the tested mass-law exponent from `0.50` to `1.00`, and steepens the retained-bounded post-peak tail from `-0.52` to `-0.93` on the `h = 0.25` family |
| Robustness sweep | On the tested 3D ordered-lattice slices, Born stays machine-clean, `F~M = 1.00` stays fixed, and gravity stays TOWARD across the tested width/connectivity/length rows |
| Dimensional table | `F~M = 1.00` is the recurring result in 2D/3D/4D, with the 3D distance tail at `b^(-0.93)` on the retained-bounded `h = 0.25` slice |
| Decoherence identity | On the 3D `1/L^2` lattice, decoherence observables are exactly identical for valley-linear and spent-delay at the tested `h` values |

The safe interpretation is:

- valley-linear is a real bounded action fork on the ordered-lattice family
- the best retained-bounded 3D distance-law read is now a near-Newtonian finite-
  lattice replay with slice-dependent tail fits
- the action does not alter the decoherence observables on the tested zero-field
  family

## What remains open

The main open questions are still:

- the 4D tail law, because the current 4D lattice is still too narrow for a
  clean far-tail fit
- the 3D asymptotic bridge, because the finite-lattice tail is now close to
  Newtonian but still slice-dependent enough that it should not be promoted as
  an exact universal `-1.00`
- the transfer-norm / marginality story, because the kernel-selection claims
  are still being reconciled against frozen scripts and notes
- Gate B, because the generated-geometry signal is real but the imposed
  comparator still loses detector purity
- whether the valley-linear continuum derivation should be read as a genuine UV
  completion or as a continuum effective description of the ordered-lattice
  lane

## Best bounded synthesis

The most honest summary is:

- the valley-linear action has a clean continuum distance-law derivation
- the ordered 3D lattice carries retained-bounded matching near-Newtonian behavior at the
  frozen `h = 0.25` resolution, and the new asymptotic bridge note shows the
  finite-size correction is still slice-dependent
- decoherence is action-independent on the tested 3D `1/L^2` family
- robustness is good on the tested ordered-lattice slices
- the 4D and Gate B questions remain open

That means the current state is stronger than “exploratory only,” but still not
strong enough to promote a universal theorem or a final closure claim.

## Practical reading

If you are entering the valley-linear lane quickly, read in this order:

1. the continuum derivation
2. the 3D same-family action comparison
3. the robustness sweep
4. the dimensional gravity table
5. the decoherence-independence note

That sequence gives the cleanest separation between:

- analytic statement
- retained-bounded lattice numerics
- remaining open tensions
