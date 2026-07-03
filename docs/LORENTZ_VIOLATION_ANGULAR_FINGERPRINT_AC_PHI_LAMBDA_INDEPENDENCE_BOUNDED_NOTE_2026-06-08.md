# Lorentz-Violation Angular Fingerprint Is Independent of the AC Phi Lambda Carrier (Bounded)

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived
after independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_lorentz_fingerprint_ac_phi_lambda_independence.py`](../scripts/frontier_lorentz_fingerprint_ac_phi_lambda_independence.py)
**Cached log:**
[`logs/runner-cache/frontier_lorentz_fingerprint_ac_phi_lambda_independence.txt`](../logs/runner-cache/frontier_lorentz_fingerprint_ac_phi_lambda_independence.txt)

## Result

Within the two nearest-neighbor dispersion surfaces already present in the
Lorentz package, the leading Lorentz-violation angular operator is the same:

```text
sum_i p_i^4.
```

The bosonic graph-Laplacian carrier gives coefficient `-1/12`; the staggered
Dirac carrier associated with `AC_phi_lambda` gives coefficient `-1/3`. The
coefficient changes the magnitude, but after dividing out that scalar coefficient
the angular operator is identical. Consequently the `[100]/[111]` anisotropy
ratio is `3` on both carriers.

This is the narrow claim: the angular fingerprint is independent of the
`AC_phi_lambda` carrier coefficient. The theorem does not derive either
dispersion surface from the axioms, does not remove the parent dependencies,
and does not make a magnitude or experimental-reach claim.

## Inputs

Load-bearing dependencies:

- [`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
  supplies the retained-bounded staggered-dispersion surface and records the
  corresponding `-1/3` quartic coefficient.
- [`LORENTZ_VIOLATION_DERIVED_NOTE.md`](LORENTZ_VIOLATION_DERIVED_NOTE.md)
  supplies the retained-bounded graph-Laplacian Lorentz-violation surface and
  records the cubic-harmonic angular fingerprint.

The `scale_reference_primitive` is not a Tier-A admission and not a bounded
status source. This note does not use it: scale conversion and any numerical
magnitude estimate are outside the claim.

## Computation

Using the physical nearest-neighbor dispersion normalizations,

```text
bosonic:   sum_i 2(1 - cos(p_i a)) / a^2
staggered: sum_i sin^2(p_i a) / a^2
```

the Taylor expansions have the form

```text
p^2 + a^2 c_4 sum_i p_i^4 + O(a^4 p^6),
```

with no odd powers in `a`, hence no dimension-5 term from these even
nearest-neighbor carriers. The runner solves the quartic term against

```text
A (p^2)^2 + B sum_i p_i^4
```

and gets `A = 0`, `B = -1/12` for the bosonic carrier and `B = -1/3` for the
staggered carrier. Normalizing by `B` gives the same operator `sum_i p_i^4`.

On unit directions `n`,

```text
sum_i n_i^4 = 1        on [100],
sum_i n_i^4 = 1/3      on [111],
```

so the angular ratio is exactly `3`, independent of the carrier coefficient.
The runner also cross-checks the parent cubic-harmonic decomposition by verifying
the isotropic average `3/5` and zero `ell=2` projection.

## Guardrails

This note does **not** claim:

- the staggered carrier admission is retired;
- the graph-Laplacian or staggered dispersion is newly derived from axioms here;
- the magnitude coefficient is carrier-independent;
- the approved scale-reference primitive supplies a dimensionless prediction;
- any experimental number is a derivation input;
- any parent effective status changes; or
- any audit verdict is set.

The landed claim is only coefficient-independence of the angular shape within
the two supplied nearest-neighbor dispersion surfaces.

## Command

```bash
python3 scripts/frontier_lorentz_fingerprint_ac_phi_lambda_independence.py
```

Expected: `TOTAL: PASS=8 FAIL=0`.
