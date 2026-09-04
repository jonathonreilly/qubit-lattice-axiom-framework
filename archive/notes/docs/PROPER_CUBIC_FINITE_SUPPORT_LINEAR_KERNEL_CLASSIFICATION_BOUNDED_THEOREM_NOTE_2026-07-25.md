# Proper-cubic finite-support linear-kernel classification

**Date:** 2026-07-25

**Type:** bounded_theorem
**Authority:** none. **Audit:** unset.

**Primary runner:**
[`scripts/proper_cubic_finite_support_linear_kernel_classification_2026_07_25.py`](../scripts/proper_cubic_finite_support_linear_kernel_classification_2026_07_25.py)

## Question

What is the exact form of a rational scalar convolution kernel on `Z^3` when
its finite support is closed under the proper cubic rotation group and the
kernel is invariant under that group?

This is a classification inside an explicitly supplied linear operator class.
It does not derive that a physical law is linear, has finite range, is a
convolution, is rotation-covariant, or annihilates constants.

## Explicit hypotheses

Let `P` be a finite subset of `Z^3` closed under the proper cubic rotation
group `O`, and let

```text
k : P -> Q,
(L f)(x) = sum_{v in P} k(v) f(x+v).
```

The theorem assumes:

1. the rational scalar/module structure used by the displayed sum;
2. the linear convolution form of `L`, including translation covariance;
3. finite support `P`;
4. proper-cubic covariance, `k(Rv) = k(v)` for every `R in O`.

The [Lattice axiom](MINIMAL_AXIOMS_2026-06-29.md) supplies `Z^3`, its standard
translations, and the proper cubic rotations. It does not supply hypotheses
1–4 for a downstream physical law. Those are the named boundary of this
bounded theorem.

## Theorem: orbit indicators classify the invariant kernels

The vector space of `O`-invariant rational kernels on `P` has dimension equal
to the number of `O`-orbits in `P`. The indicator functions of the orbits form
a basis.

**Proof.** Invariance makes `k` constant on every orbit. Conversely, assigning
one rational value to each orbit defines an invariant kernel. The orbit
indicators have disjoint supports and span every such assignment. Therefore
they form a basis, with one basis vector per orbit. `[]`

The runner checks this by two exact routes at the six support balls
`|v|^2 <= 1,...,6`:

- Burnside counting, using the average number of fixed points of the 24 proper
  signed-permutation matrices;
- exact rational nullity of all equations `k(Rv)-k(v)=0`.

The resulting table is:

| `|v|^2 <=` | points | proper-cubic orbits | invariant nullity |
|---|---:|---:|---:|
| 1 | 7 | 2 | 2 |
| 2 | 19 | 3 | 3 |
| 3 | 27 | 4 | 4 |
| 4 | 33 | 5 | 5 |
| 5 | 57 | 6 | 6 |
| 6 | 81 | 7 | 7 |

The equality is proved above for every finite rotation-closed `P`; the six
balls are exact reproductions and controls, not an extrapolation.

## Nearest-neighbour corollary

For `P = {0, +/-e_1, +/-e_2, +/-e_3}`, the two orbits are the origin and the
six face displacements. Writing their kernel values as `a` and `b`,

```text
L = a I + b sum_{|v|=1} T_v
  = (a+6b) I + b Delta,

Delta = sum_{|v|=1} T_v - 6 I.
```

Thus the supplied class is exactly `span_Q{I, Delta}`. The anisotropic forward
difference `T_{e_1}-I` is a local translation-covariant control outside this
proper-cubic invariant span. With the rotation group removed, the range-1
kernel space has dimension seven.

If one additionally assumes

```text
L(1) = 0,
```

then `a+6b=0`, so `L` lies on the Laplacian line. This
constant-annihilation condition is an extra hypothesis, not axiom content.
At the next support ball `|v|^2 <= 2`, the invariant space has dimension
three and the same one linear condition leaves dimension two. The collapse to
one line is therefore specific to the nearest-neighbour support.

## Prior-art boundary

`CUBIC_ORBIT_REYNOLDS_PROJECTOR_NARROW_THEOREM_NOTE_2026-05-10.md` already
proves the orbit-indicator basis and orbit-count dimension statement for a
`D_4` action on a forward-cone support. The general finite-group mechanism is
therefore not new here. The new reusable content is the exact proper-cubic
`O` application on centered `Z^3` balls and its range-1
`span{I, Delta}` / constant-annihilation corollary.

## Claim boundary

- This note classifies a supplied rational linear convolution class. It does
  not derive a propagation law from Record additivity.
- It does not derive range-1 locality, constant-annihilation, an overall
  normalization, a source, a field/readout bridge, a dynamics, or an action.
- It does not repair, promote, or change any gravity row or any other audit
  row.
- It contains no claim about dimensionless or intensive readouts.
- It proposes or adopts no axiom or primitive. Independent audit remains
  required before any retained-grade use.

## Reproduction

```bash
python3 scripts/proper_cubic_finite_support_linear_kernel_classification_2026_07_25.py
```

Expected final lines:

```text
RESULT 5 0
RESULT PROPER_CUBIC_FINITE_SUPPORT_LINEAR_KERNEL_CLASSIFICATION_PASSES
```

## Dependency

The sole load-bearing framework authority is the
[Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) note for the supplied lattice
and proper cubic rotation group. The operator-class hypotheses and the proof
are stated in full above.
