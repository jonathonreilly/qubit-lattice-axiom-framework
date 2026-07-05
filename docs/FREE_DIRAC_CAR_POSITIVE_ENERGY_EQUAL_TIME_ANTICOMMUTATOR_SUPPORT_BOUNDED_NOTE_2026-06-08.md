# Free Dirac CAR Positive-Energy and Equal-Time Anticommutator Support (Bounded)

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived
after independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_free_dirac_car_positive_energy_equal_time_support.py`](../scripts/frontier_free_dirac_car_positive_energy_equal_time_support.py)
**Cached log:**
[`logs/runner-cache/frontier_free_dirac_car_positive_energy_equal_time_support.txt`](../logs/runner-cache/frontier_free_dirac_car_positive_energy_equal_time_support.txt)

## Result

On the supplied free massive Dirac mode algebra, the CAR quantization choice
gives a bounded-below one-mode Hamiltonian, while the corresponding Bose
commutator choice gives an unbounded-below antiparticle sector. The same finite
spinor calculation verifies the equal-time completeness identity in the normalized
projector convention, and records the equivalent `2E`-normalized convention with the
required `1/(2E)` field-expansion weight. The unweighted `2E`-normalized spinor sum is
not asserted to be `I_4`.

This is a support result. It does not choose CAR from the framework, prove a
spin-statistics theorem, construct the field on the reconstructed Hilbert
space, prove spacelike microcausality, or close any keystone residual.

## Inputs

Load-bearing input:

- [`FREE_DIRAC_ANTIPARTICLE_MODE_ALGEBRA_BOUNDED_NOTE_2026-05-30.md`](FREE_DIRAC_ANTIPARTICLE_MODE_ALGEBRA_BOUNDED_NOTE_2026-05-30.md)
  supplies the free massive Dirac `+E/-E` particle/antiparticle mode algebra
  and the `u/v` mode structure used here.

Scope context, not promoted here:

- the spin-statistics/CAR selection remains a separate gate or admitted input;
- the retained-bounded emergent-Lorentz surfaces remain the boost-covariance
  context;
- the partner-chirality and OS-to-Wightman field-delivery questions remain open
  unless closed by their own audited rows.

## Finite Algebra

For one free massive Dirac mode with energy `E > 0`, the normal-ordering
question is the antiparticle term in

```text
H_hat = E a^dag a - E b b^dag.
```

If the antiparticle operators obey CAR,

```text
b b^dag = 1 - b^dag b,
```

then, up to the usual vacuum constant,

```text
H_hat = E a^dag a + E b^dag b,
```

with one-mode Fock eigenvalues `{0, E, E, 2E}`.

If the same sign structure is combined with a Bose commutator,

```text
b b^dag = 1 + b^dag b,
```

then

```text
H_hat = E a^dag a - E b^dag b,
```

and the spectrum is unbounded below as the antiparticle occupation grows.

The runner also constructs an explicit `4 x 4` massive Dirac Hamiltonian and
checks:

- the single-particle spectrum is `{+E, +E, -E, -E}`;
- the Hamiltonian eigenspinor columns are orthonormal;
- in the orthonormal spectral-projector convention,
  `sum_s(u_s u_s^dag + v_s v_s^dag) = I_4`;
- the positive- and negative-energy projectors are orthogonal and idempotent;
- in the `2E`-normalized spinor convention, the unweighted sum is `2E I_4`,
  while the field-normalized sum `(1/(2E)) sum_s(u_s u_s^dag + v_s v_s^dag) = I_4`;
- the Bose-sign combination `sum_s(u_s u_s^dag - v_s v_s^dag)` is not `I_4`;
- the scalar mass matrix is invariant under the supplied spinor boost matrix.

The equal-time conclusion is therefore canonical CAR support, not a spacelike
field-commutator theorem.

## Guardrails

This note does **not** claim:

- the framework derives the CAR/spin-statistics selection;
- partner chirality is physically supplied;
- the massive Dirac field is constructed on the OS/Wightman Hilbert space;
- spacelike microcausality is proved;
- the keystone program is closed;
- `Q=2/3`, generation identification, or `r=1/2` is touched; or
- any audit status is changed.

The landed salvage intentionally removes the submitted PR's closure language.
What remains is the finite support theorem: given the supplied free Dirac mode
algebra, CAR is the positive-energy quantization and the equal-time CAR
anticommutator is canonical after the normalization convention is included.

## Command

```bash
python3 scripts/frontier_free_dirac_car_positive_energy_equal_time_support.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
