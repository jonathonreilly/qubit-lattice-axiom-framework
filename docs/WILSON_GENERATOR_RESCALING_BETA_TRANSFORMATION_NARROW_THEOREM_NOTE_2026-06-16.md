# Formal Generator/Coupling Label Rescaling and Coefficient Transformation

**Date:** 2026-06-16. Dependency-free scope repair: 2026-07-16.
**Claim type:** positive_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/wilson_generator_rescaling_beta_transformation_2026_06_16.py`](../scripts/wilson_generator_rescaling_beta_transformation_2026_06_16.py)

## Purpose

This note proves an exact transformation law for defined algebraic symbols.
Its stable filename is historical. No Wilson action or physical coupling is
part of the theorem.

The formal coefficient theorem
[`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md)
defines `C_left=beta*g^2/(4n)` and `C_right=1/2` and proves

```text
C_left=C_right  <=>  beta*g^2=2n.
```

## Theorem

Let `n >= 2` and let `beta,g,c > 0`. Suppose the formal coefficient equality

```text
beta*g^2 = 2n
```

holds. Define

```text
T'_a = c T_a,
g'   = g/c,
beta' = c^2 beta.
```

Then:

```text
g'T'_a = gT_a,
g'^2 = g^2/c^2,
beta'/beta = c^2,
beta' g'^2 = beta g^2 = 2n.
```

If additionally `Tr(T_a T_b)=delta_ab/2`, then

```text
Tr(T'_a T'_b)=c^2 delta_ab/2.
```

Thus a nontrivial `c^2 != 1` changes the supplied half-trace Gram convention,
even though the defined products `gT_a` and `beta*g^2` remain invariant under
the paired label transformation.

## Proof

Every identity follows by direct substitution:

```text
g'T'_a = (g/c)(cT_a)=gT_a,
beta'g'^2=(c^2 beta)(g^2/c^2)=beta g^2=2n.
```

Bilinearity of trace gives the Gram transformation. Positivity ensures the
divisions are defined; no other input is used.

## Boundary

This note does not claim:

- that `T_a`, `g`, or `beta` are physical gauge variables;
- that the paired label transformation is induced on any Wilson or other
  action;
- action-surface selection, a continuum dictionary, or a coupling value;
- that a noncanonical generator scale is physically forbidden;
- an audit verdict or status promotion.

A downstream physical use must separately prove the dictionary from these
formal symbols to its action and observables. This note supplies only the
displayed algebra.

## Verification

```text
python3 scripts/wilson_generator_rescaling_beta_transformation_2026_06_16.py
```

Expected:

```text
TOTAL: PASS=79 FAIL=0
```
