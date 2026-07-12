# CKM Down-Type Five-Sixths Algebra And Scale-Covariance Boundary

**Date:** 2026-04-22; first-principles covariance repair 2026-07-12
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded support theorem with an exact algebraic core and an exact
scale-rescue obstruction. Independent audit owns any effective status.
**Primary runner:**
[`scripts/frontier_ckm_down_type_scale_convention_support.py`](../scripts/frontier_ckm_down_type_scale_convention_support.py)

## 1. Question and repaired scope

The earlier version compared one fixed prediction,

```text
R_pred = [alpha_s(v)/sqrt(6)]^(6/5),
```

to two observational surfaces:

```text
R_common = m_s(m_b)/m_b(m_b),
R_mixed  = m_s(2 GeV)/m_b(m_b).
```

It reported a roughly `+15.5%` common-scale deviation and a `+0.2%`
mixed/reference-scale deviation. That comparison did not transport the theory
prediction when it transported the observation. It was therefore not an
RG-covariant comparison.

This repair proves two narrower results:

1. a rank-`1+5` normalized determinant realizes a `5/6` power exactly and
   singles out `N_c=3` within its `2N_c` generalization;
2. any shared multiplicative transport preserves the relative deviation
   between theory and observation, so a scale-convention change alone cannot
   turn the common-scale mismatch into a sub-percent agreement.

The first result is an abstract algebraic lemma, not evidence for its physical
typing. The second closes the scale-convention-rescue route on the stated
multiplicative-transport domain.

## 2. Minimal premise set

The exact proof uses only these explicit conditions:

1. a six-dimensional vector space with complementary projectors `Q` and `P`,
   where `rank(Q)=1`, `P=I-Q`, and `rank(P)=5`;
2. a positive scalar `R` and the operator `X_R = Q + R P`;
3. positive common-scale theory and observation ratios `R_pred` and
   `R_common`;
4. a positive shared multiplicative transport `T` from the common surface to
   the mixed/reference surface.
5. for the Casimir comparison only, the standard fundamental-generator
   normalization `tr_F(T^a T^b)=T_F delta^(ab)` with `T_F=1/2`.

No observed mass, fitted exponent, quoted coupling, or selected scale is a
proof input. The numerical values in Section 6 are a post-theorem illustration.

The [current framework axioms](MINIMAL_AXIOMS_2026-06-29.md) and approved
primitives do not supply a quark-mass operator, a CKM normalized-determinant
readout, or a `2 GeV` selector. In particular, the approved
[scale-reference primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md) is a units
conversion and carries no mass ratio or dimensionless selector.

## 3. Exact normalized-determinant core

Let `Q` have rank one on a six-dimensional space and let `P=I-Q`. For `R>0`,

```text
X_R = Q + R P.
```

The spectrum is

```text
spec(X_R) = {1, R, R, R, R, R}.
```

Therefore

```text
det(X_R) = R^5,
Delta_6(X_R) := det(X_R)^(1/6) = R^(5/6).             (3.1)
```

This is an exact abstract realization of a `5/6` power. Because the eigenvalue
multiplicity was built into `X_R`, it is not evidence for the physical bridge.
It does not identify `R` with `m_s/m_b` or `Delta_6(X_R)` with `|V_cb|`.

The color-rank generalization has dimension `2N_c`, a rank-one channel, and a
rank-`2N_c-1` complement. Its normalized-determinant exponent is

```text
p_det(N_c) = (2N_c-1)/(2N_c).
```

For fundamental `SU(N_c)` in the stated `T_F=1/2` normalization,

```text
C_F-T_F = (N_c^2-N_c-1)/(2N_c).
```

Equality requires

```text
2N_c-1 = N_c^2-N_c-1
<=> N_c(N_c-3)=0.
```

Among integer color ranks `N_c>=2`, the equality is unique at `N_c=3`:

```text
p_det(3) = C_F-T_F = 5/6.                              (3.2)
```

## 4. Why the algebraic core is not yet the physical bridge

Two interfaces of one composite physical bridge remain absent:

```text
down-quark mass data  --->  X_R = Q + (m_s/m_b) P,       (4.1)
X_R                   --->  |V_cb| = Delta_6(X_R).       (4.2)
```

The rank split alone cannot supply those maps. A direct counterexample fixes
all up- and down-mass eigenvalues and varies only their relative eigenbasis:

```text
M_u = diag(m_u,m_c,m_t),
M_d(theta) = R_23(theta) diag(m_d,m_s,m_b) R_23(theta)^dagger.
```

Every spectral mass invariant is independent of `theta`, while

```text
|V_cb| = |sin(theta)|
```

varies continuously. Thus mass spectra, Casimir arithmetic, and a rank count do
not entail a CKM mixing entry. Equations (4.1) and (4.2) form one genuine
physical bridge obligation, not an algebraic consequence of (3.1).

This is a current-packet boundary only. A future source/action theorem may
derive both maps.

## 5. Exact scale-covariance theorem

Let `R_pred` and `R_common` be positive theory and observation ratios on one
common renormalization surface. Let `T>0` be the shared transport to a mixed
surface. Covariance gives

```text
R_pred,mixed = T R_pred,
R_obs,mixed  = T R_common.                               (5.1)
```

The relative deviation is invariant:

```text
R_pred,mixed/R_obs,mixed - 1
  = (T R_pred)/(T R_common) - 1
  = R_pred/R_common - 1.                                 (5.2)
```

This identity is independent of the numerical value or perturbative order of
`T`. Threshold matching factors may be included in `T`; if they act on the
same numerator transport, they cancel in (5.2) as well.

The crossed comparison used previously was instead

```text
D_cross(T) = R_pred/(T R_common) - 1.                    (5.3)
```

It holds the theory result on the common surface while moving only the
observation. It is not invariant:

```text
d D_cross/dT = -R_pred/(T^2 R_common) != 0.              (5.4)
```

Indeed, `T=R_pred/R_common` makes (5.3) vanish identically. A small crossed
deviation can therefore be created by the selected transport and cannot serve
as a scale-selection theorem.

For flavor-universal multiplicative QCD mass running on a fixed-flavor
surface,

```text
d ln(m_q)/d ln(mu) = -gamma_m,
d ln[m_s(mu)/m_b(mu)]/d ln(mu) = -gamma_m + gamma_m = 0. (5.5)
```

A mixed ratio with only the strange numerator moved has a nonzero scale
derivative. Consequently, a bridge stated directly on that mixed ratio already
contains an additional scale/readout prescription. QCD transport does not
select `2 GeV`.

## 6. Comparator-only numerical illustration

The current central values give

```text
R_pred   = 0.0223897316159,
R_common = 81.0/4180.0 = 0.0193779904306,
T        = 93.4/81.0   = 1.1530864197531,
R_mixed  = T R_common  = 0.0223444976077.
```

The old crossed comparison is

```text
R_pred/R_mixed - 1 = +0.202439%.                         (6.1)
```

The covariantly transported prediction is

```text
T R_pred = 0.0258172954682,
(T R_pred)/R_mixed - 1 = +15.542072%,                    (6.2)
```

exactly equal, up to rounding, to

```text
R_pred/R_common - 1 = +15.542072%.                       (6.3)
```

The `+0.20%` value is therefore a cross-surface coincidence. It is not a
transport explanation of the common-scale discrepancy.

The earlier runner also stored `alpha_s(2 GeV)=0.3026` and
`alpha_s(m_b)=0.2211`. Those values give the one-loop-truncated factor

```text
[0.3026/0.2211]^(12/25) = 1.1625576,
```

not the observed-mass ratio `93.4/81.0 = 1.1530864` and not the historical
literal `1.14747`. Only the one-loop coefficient arithmetic leading to
`12/25` is exact; a finite-order transport factor is not an exact all-orders
QCD statement.

## 7. Theorem and boundary

**Theorem (five-sixths algebra and scale-covariance boundary).** On the
explicit domain of Sections 2-5:

1. the normalized determinant of a rank-`1+5` operator gives `R^(5/6)`
   exactly, and, in the standard `T_F=1/2` generator normalization, `N_c=3`
   uniquely equates this exponent with `C_F-T_F` in the `2N_c` family;
2. fixed mass spectra do not determine a mixing angle, so the composite
   mass-operator/CKM-readout bridge (4.1)-(4.2) remains a separate physical
   obligation;
3. shared multiplicative RG transport preserves relative theory/observation
   deviation, so scale convention alone cannot convert the common-scale
   mismatch into the reported sub-percent agreement.

The scale-convention-rescue route is closed on this domain. The constructive
remaining target is sharp: derive the composite typed bridge (4.1)-(4.2), and state the
result on a common or explicitly RG-covariant mass surface. If a future bridge
is instead defined directly on `m_s(2 GeV)/m_b(m_b)`, its `2 GeV` prescription
must be supplied or derived as part of that bridge.

## 8. Does not claim

- no observed quark mass or CKM value is derived;
- no absolute bottom or strange mass is closed;
- the physical maps (4.1)-(4.2) are not supplied by the determinant identity;
- no global impossibility is claimed for future source/action, RGI-mass, or
  explicitly conditional convention routes;
- the old `+0.20%` central-value coincidence is not retained as derivation
  evidence.

## 9. Verification

Run:

```bash
python3 scripts/frontier_ckm_down_type_scale_convention_support.py
```

Expected final line:

```text
SUMMARY: EXACT_PASS=26 COMPARATOR_PASS=6 FAIL=0
```
