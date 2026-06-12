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
spinor calculation verifies the equal-time completeness identity that makes the
CAR anticommutator canonical.

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
- the positive- and negative-energy eigenspinors are orthonormal Hamiltonian
  eigenvectors;
- `sum_s(u_s u_s^dag + v_s v_s^dag) = I_4` as an orthonormal projector
  resolution of identity;
- the Bose-sign combination `sum_s(u_s u_s^dag - v_s v_s^dag)` is not `I_4`;
- the scalar mass matrix is invariant under the supplied spinor boost matrix.

The equal-time conclusion is therefore canonical CAR support, not a spacelike
field-commutator theorem.

## 2026-06-12 normalization bridge

The conditional audit asked for an explicit bridge from textbook
`2E`-normalized Dirac spinors to the orthonormal eigenspinor projector
identity, or for the required `1/(2E)` field-expansion factor to be included
before claiming an `I_4` equal-time matrix.

This note takes the orthonormal-eigenspinor route. The runner diagonalizes the
finite `4 x 4` Hermitian Dirac Hamiltonian with `numpy.linalg.eigh`, so the
columns `u_s` and `v_s` are orthonormal in the finite Hilbert-space inner
product. The identity checked is the spectral resolution

```text
U_+ U_+^dag + U_- U_-^dag = I_4,
```

not the covariant textbook spin-sum normalization. If one rewrites the same
calculation using covariant `2E`-normalized spinors, the corresponding field
expansion must carry the standard compensating `1/(2E)` weight.
No such covariant-spinor normalization is imported or claimed here.

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
anticommutator is canonical.

## Command

```bash
python3 scripts/frontier_free_dirac_car_positive_energy_equal_time_support.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
