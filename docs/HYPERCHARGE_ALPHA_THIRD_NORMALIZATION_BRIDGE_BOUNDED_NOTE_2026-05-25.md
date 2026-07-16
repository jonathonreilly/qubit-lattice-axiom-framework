# Exact Formal Two-Equation Normalization Arithmetic

**Date:** 2026-05-25
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and effective
status are set by the independent audit lane.
**Primary runner:**
[`scripts/hypercharge_alpha_third_normalization_runner.py`](../scripts/hypercharge_alpha_third_normalization_runner.py)

## Claim

Let `n_sym`, `n_anti`, `q`, and `t` be supplied rational numbers, and let
`alpha` and `beta` be formal unknowns. Assume only

```text
n_sym * alpha + n_anti * beta = 0,
q = t + beta/2,
n_sym != 0.
```

Then the system has the unique exact solution

```text
beta  = 2(q - t),
alpha = -(n_anti/n_sym) * beta.
```

For the explicitly supplied formal packet

```text
(n_sym, n_anti, q, t) = (6, 2, -1, -1/2),
```

the solution is

```text
beta = -1,
alpha = 1/3.
```

This is the whole theorem. The variable names preserve the stable row's
notation, but they carry no physical semantics in this claim. In particular,
the theorem does not say that the packet occurs in the framework, that either
formal block is a particle multiplet, or that `alpha` is a physical
hypercharge normalization.

## Formal hypotheses

Every load-bearing item is an explicit theorem hypothesis:

1. `n_sym`, `n_anti`, `q`, and `t` are rational inputs.
2. `n_sym != 0`.
3. The first equation is supplied with the displayed plus sign.
4. The second equation is supplied in the displayed convention, equivalently
   `beta/2 = q - t`.
5. The specialization uses exactly the displayed packet `(6, 2, -1, -1/2)`.

No axiom, approved primitive, retained representation split, physical charge
assignment, weak-isospin assignment, or readout theorem is a hypothesis of
this formal result. The row therefore has no load-bearing scientific
dependency.

## Exact proof and uniqueness certificate

Write the equations as

```text
[ n_sym   n_anti ] [ alpha ]   [   0   ]
[   0       1/2  ] [ beta  ] = [ q - t ].
```

The determinant is

```text
det = n_sym/2.
```

Because `n_sym != 0`, the determinant is nonzero and the coefficient matrix
has rank two. Thus the system has exactly one solution. The second row gives
`beta = 2(q-t)`. Substitution into the first row gives
`alpha = -(n_anti/n_sym) beta`.

For the supplied formal packet,

```text
det   = 6/2 = 3,
beta  = 2(-1 - (-1/2)) = -1,
alpha = -(2/6)(-1) = 1/3.
```

Both equation residuals are exactly zero in rational arithmetic. No decimal
approximation, fit, empirical comparison, source-note phrase, audit status, or
pre-recorded answer is used as mathematical evidence.

## Hostile controls

The primary runner constructs the coefficient matrix and solves it with
`fractions.Fraction`. Normal execution also verifies that the certificate
fails closed under each of these mutations:

- `n_sym = 0`;
- a generic determinant-zero two-equation system;
- a minus sign in place of the displayed trace-equation plus sign;
- `t - q` in place of `q - t`;
- a changed multiplicity packet;
- a changed `q`/`t` packet; and
- an attempt to infer a physical Anti-squared-to-`L_L` readout from the
  formal certificate.

The runner's `--intentional-failure` mode presents a changed `q`/`t` packet as
the stated specialization and exits nonzero when that mutation is rejected.

## Open physical bridges

The following statements are explicitly outside this theorem and remain open
unless independently supplied by retained-grade authority:

- that a framework representation has the multiplicity split `6+2`;
- that a formal Anti-squared block is physically `L_L`;
- that `q=-1` and `t=-1/2` are framework-derived physical values;
- that `q=t+beta/2` is a derived physical readout equation rather than a
  supplied formal equation;
- that the sign and normalization conventions used here are selected by the
  framework;
- that the formal variable `alpha` is the framework's hypercharge
  normalization; and
- that a common abelian generator/coupling rescaling has been physically
  fixed.

Consequently, this row does not promote the parent physical hypercharge row.
`HYPERCHARGE_IDENTIFICATION_NOTE.md` remains context only and must supply or
derive its own physical interpretation and scale. The graph-first selector,
commutant, representation, matter-assignment, and charge-table notes are also
context only; none is consumed by this proof.

## Verification

Run the normal exact certificate:

```bash
PYTHONPATH=scripts python3 scripts/hypercharge_alpha_third_normalization_runner.py
```

Expected terminal lines:

```text
TOTAL: PASS=18 FAIL=0
VERDICT: exact formal implication verified; the supplied packet gives beta=-1 and alpha=1/3, with no physical readout inferred.
```

Run the fail-closed probe:

```bash
PYTHONPATH=scripts python3 scripts/hypercharge_alpha_third_normalization_runner.py --intentional-failure
```

That command must print `INTENTIONAL FAIL` and exit with status `1`.
