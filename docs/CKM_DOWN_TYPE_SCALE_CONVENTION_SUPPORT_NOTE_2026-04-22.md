# CKM Down-Type Five-Sixths Algebra And Shared-Transport Covariance

**Date:** 2026-04-22; first-principles covariance repair 2026-07-12;
exact-scope repair 2026-07-27
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded support theorem with an exact algebraic core and an exact
shared-positive-scalar-transport identity. Independent audit owns any
effective status.
**Primary runner:**
[`scripts/frontier_ckm_down_type_scale_convention_support.py`](../scripts/frontier_ckm_down_type_scale_convention_support.py)

## Corrigendum (2026-09-30)

**What was wrong.** The down-type bridge `|V_cb| = (m_s/m_b)^(5/6)` was reported
as matching the observed strange/bottom mass ratio to `+0.20%`. That figure
compares the prediction with `m_s(2 GeV)/m_b(m_b)`: the strange mass at 2 GeV
against the bottom mass at its own mass. The ratio of two MS-bar masses taken at
one energy does not depend on that energy (Section 5, eq. (5.6)), so a bridge
stated on `m_s/m_b` has one scale-consistent test, at one common scale. Sections
1 and 6 below already record that the `+0.20%` is a cross-surface coincidence
and give `+15.5%` at the common scale. That `+15.5%` used the ratio `93.4/81.0`
for the transport from 2 GeV to `m_b`, which four-loop running does not
reproduce. The common-scale miss is larger.

**Corrected statement.** With four-loop QCD running (`n_f = 4` from 2 GeV to
`m_b`, `n_f = 5` from `M_Z` to `m_b`, two-loop decoupling at `m_b`) and PDG 2024
inputs `m_s(2 GeV) = 93.5(8) MeV`, `m_b(m_b) = 4.183(7) GeV`,
`alpha_s(M_Z) = 0.1180(9)`:

```text
alpha_s(2 GeV) = 0.3014,  alpha_s(m_b) = 0.2247      (n_f = 4)
m_s(2 GeV)/m_s(m_b) = 1.184                          (Section 6 used 1.153)
m_s(m_b) = 78.97 MeV                                 (Section 6 used 81.0)
R_common = m_s(m_b)/m_b(m_b) = 0.018878
R_pred/R_common - 1 = +18.6% +- 1.2%                 (about 16 sigma)
p = ln|V_cb| / ln R_common = 0.7975                  (5/6 = 0.8333)
c = |V_cb| / R_common^(5/6) = 1.153                  (prefactor needed at 5/6)
```

The sigma count takes the atlas `|V_cb| = alpha_s(v)/sqrt(6)` as exact and uses
the PDG errors. By loop order (1 to 4) the miss is `+12.0%`, `+17.1%`, `+18.3%`,
`+18.6%`. Across standard input sets (PDG 2024, PDG lattice-only `m_s`, FLAG 2024
`N_f = 2+1+1` and `2+1`, and one-sigma corner choices) it is `+16.9%` to
`+20.4%`; from lattice mass ratios with no running at all (FLAG 2024
`m_b/m_s = 53.86`) it is `+20.6%`. Against measured `|V_cb|` instead of the atlas
value `0.04217` the miss is `+8.6%` (`0.0392`), `+14.7%` (`0.0410`), `+18.7%`
(`0.0422`), with fitted exponent `0.816`, `0.805`, `0.797`; an exact `5/6` on the
common surface needs `|V_cb| = 0.0366`. The exponent that fits stays at `0.79` to
`0.80` at every scale up to the Planck scale in one-loop Standard-Model running
of the Yukawa matrices: `|V_cb|` and `m_s/m_b` rise together (by `13.9%`), so
`p` moves from `0.7975` to `0.7906`, not toward `5/6`.

The `+0.20%` needs the strange mass quoted at `mu_s = 1.99 GeV` against the
bottom mass at `m_b`. The same mixed ratio fits the exponent `4/5` at
`mu_s = 3.9 GeV`, `6/7` at `1.43 GeV` and `8/9` at `1.05 GeV`, and moves by 1%
per 3.6% in `mu_s`. It is a convention coincidence, not support for `5/6`.

**What still stands.** `C_F - T_F = 5/6` (exact group theory); the atlas value
`|V_cb| = alpha_s(v)/sqrt(6)` as a supplied model; the value
`R_pred = 0.0223897`; the rank-`1+5` determinant algebra (Section 3); the fixed
spectra / mixing-angle countermodel (Section 4); the shared-transport covariance
theorem (Section 5), which also shows that no shared transport can change the
common-scale miss; and every non-claim in Section 8. Nothing here was ever a
retained claim. This corrigendum changes no status field: audit status remains
with the independent audit lane.

**Consequence for the lane.** On the RG-invariant ratio the bridge as written
(exponent `5/6`, prefactor `1`) is not supported; it would need a prefactor `1.15`
or an exponent `0.80`, and the alignment law would have to supply one. A bridge
stated directly on `m_s(2 GeV)/m_b(m_b)` is a different, mixed-scale statement
that owes its 2 GeV selector (Section 7).

Check: `python3 scripts/frontier_ckm_five_sixths_common_scale_four_loop_correction_2026_09_30.py`
(comparator content only; own four-loop implementation with a second, independent
integration path; `TOTAL: PASS=47, FAIL=0`). The same correction is recorded in
`CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md`,
`QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md`,
`DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md`,
`QUARK_MASS_RATIOS_TASTE_STAIRCASE_SUPPORT_NOTE_2026-04-25.md`,
`UP_TYPE_MASS_RATIO_CKM_INVERSION_NOTE.md`, `MASS_SPECTRUM_DERIVED_NOTE.md`,
`COMPLETE_PREDICTION_CHAIN_2026_04_15.md`,
`YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md` and
`lanes/open_science/03_QUARK_MASS_RETENTION_OPEN_LANE_2026-04-26.md`.

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
   between theory and observation. More generally, separate positive
   transports change the deviation only through their ratio.

The first result is an abstract algebraic lemma, not evidence for its physical
typing. The second is an exact covariance identity on the explicitly stated
scalar-transport domain. It does not classify nonmultiplicative evolution,
observable-specific matching, or a future typed CKM/mass readout.

## 2. Minimal premise set

The exact proof uses only these explicit conditions:

1. a six-dimensional vector space with complementary projectors `Q` and `P`,
   where `rank(Q)=1`, `P=I-Q`, and `rank(P)=5`;
2. a positive scalar `R` and the operator `X_R = Q + R P`;
3. positive common-scale theory and observation ratios `R_pred` and
   `R_common`;
4. a positive shared multiplicative transport `T` from the common surface to
   the mixed/reference surface;
5. for the fixed-spectrum countermodel only, supplied left-handed positive
   Hermitian `3 x 3` mass-squared representatives `H_u` and `H_d` with simple
   spectra, unitary diagonalizers `U_u` and `U_d`, and the standard textbook
   CKM definition `V=U_u^dagger U_d`;
6. for the Casimir comparison only, the standard fundamental-generator
   normalization `tr_F(T^a T^b)=T_F delta^(ab)` with `T_F=1/2`.

No observed mass, fitted exponent, quoted coupling, or selected scale is a
proof input. The numerical values in Section 6 are a post-theorem illustration.
Condition 5 supplies only the textbook meaning of an admissible quark
mass-pair counterexample; it is not a new framework axiom or a derivation of
the physical mass operators.

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

The rank split alone cannot supply those maps. Choose strictly positive,
pairwise-distinct eigenvalues in each sector and define the admissible
left-handed positive Hermitian representatives

```text
H_u = diag(h_u,h_c,h_t),
H_d(theta) = R_23(theta) diag(h_d,h_s,h_b) R_23(theta)^dagger.
```

They are diagonalized by `U_u=I` and `U_d=R_23(theta)`. Under the standard
textbook definition

```text
V = U_u^dagger U_d = R_23(theta),
```

every spectral mass invariant is independent of `theta`, while

```text
|V_cb| = |sin(theta)|
```

varies continuously. Thus mass spectra, Casimir arithmetic, and a rank count do
not entail a CKM mixing entry. Equations (4.1) and (4.2) form one genuine
physical bridge obligation, not an algebraic consequence of (3.1).

This is a current-packet boundary only. A future source/action theorem may
derive both maps.

## 5. Exact shared-transport covariance theorem

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

The exact two-sided law makes the hypothesis in (5.1) explicit. For positive
theory and observation transports `T_pred` and `T_obs`, define

```text
D(T_pred,T_obs)
  = (T_pred R_pred)/(T_obs R_common) - 1.
```

Then

```text
1 + D(T_pred,T_obs)
  = (T_pred/T_obs) [1 + D(1,1)].                         (5.3)
```

Since all factors are positive, `D(T_pred,T_obs)=D(1,1)` if and only if
`T_pred=T_obs`. Thus (5.2) is neither a claim about every possible RG map nor
an assumption that theory and observation must always have the same
transport; it is the exact result conditional on a shared scalar transport.

The crossed comparison used previously is the special case
`T_pred=1`, `T_obs=T`:

```text
D_cross(T) = R_pred/(T R_common) - 1.                    (5.4)
```

It holds the theory result on the common surface while moving only the
observation. It is not invariant:

```text
d D_cross/dT = -R_pred/(T^2 R_common) != 0.              (5.5)
```

Indeed, `T=R_pred/R_common` makes (5.4) vanish identically. Consequently, a
small crossed deviation does not by itself determine or derive a scale
selector; an independent physical prescription for the unequal transport
ratio would be additional input.

For flavor-universal multiplicative QCD mass running on a fixed-flavor
surface,

```text
d ln(m_q)/d ln(mu) = -gamma_m,
d ln[m_s(mu)/m_b(mu)]/d ln(mu) = -gamma_m + gamma_m = 0. (5.6)
```

A mixed ratio with only the strange numerator moved has a nonzero scale
derivative. Consequently, a bridge stated directly on that mixed ratio already
contains an additional scale/readout prescription. QCD transport does not
select `2 GeV`.

## 6. Comparator-only numerical illustration

Every number in this section is a comparator, not a proof input, and each
carries an explicit conditional provenance. The prediction
`R_pred = [alpha_s(v)/sqrt(6)]^(6/5)` is a historical conditional comparator:
`alpha_s(v)` is the reused strong coupling that rides on the supplied plaquette
`<P>=0.5934` (comparator-only license; see the comparator note
`ALPHA_S_DERIVED_NOTE.md`, cited here by name only so it stays a comparator and
not a load-bearing dependency), and the `alpha_s(v)/sqrt(6)` combination rests
on the supplied CKM-atlas
identifications `|V_us|^2 = alpha_s(v)/2`, `A^2 = N_pair/N_color = 2/3`, and
`|V_cb| = A|V_us|^2`, together with the still-open physical five-sixths bridge
`|V_cb| = (m_s/m_b)^(5/6)`. None of those identifications is derived here. The
mass values `81.0`, `93.4`, and `4180.0` (MeV: strange at `m_b`, strange at
`2 GeV`, and bottom at `m_b`) and the couplings `alpha_s(2 GeV)=0.3026`,
`alpha_s(m_b)=0.2211` are observational/PDG-style literature comparators.

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

## 7. Theorem and exact scope

**Theorem (five-sixths algebra and shared-transport covariance).** On the
explicit domain of Sections 2-5:

1. the normalized determinant of a rank-`1+5` operator gives `R^(5/6)`
   exactly, and, in the standard `T_F=1/2` generator normalization, `N_c=3`
   uniquely equates this exponent with `C_F-T_F` in the `2N_c` family;
2. fixed mass spectra do not determine a mixing angle, so the composite
   mass-operator/CKM-readout bridge (4.1)-(4.2) remains a separate physical
   obligation;
3. separate positive scalar transports obey the exact ratio law (5.3), and a
   shared positive scalar transport preserves relative theory/observation
   deviation exactly.

The transport theorem quantifies only over the positive scalar factors in
(5.3). It does not assert closure of every scale-convention route. In
particular, non-shared or observable-specific transport, nonmultiplicative
evolution, and a future source/action-derived CKM/mass readout remain outside
the theorem. The constructive remaining target is the composite typed bridge
(4.1)-(4.2), stated on a common or explicitly RG-covariant mass surface. If a
future bridge is instead defined directly on `m_s(2 GeV)/m_b(m_b)`, its
`2 GeV` prescription must be supplied or derived as part of that bridge.

## 8. Does not claim

- no observed quark mass or CKM value is derived;
- no absolute bottom or strange mass is closed;
- the physical maps (4.1)-(4.2) are not supplied by the determinant identity;
- no global impossibility is claimed, nor is exhaustive route closure, for
  future source/action, RGI-mass, non-shared-transport, or explicitly
  conditional convention routes;
- the old `+0.20%` central-value coincidence is not retained as derivation
  evidence.

## 9. Verification

Run:

```bash
python3 scripts/frontier_ckm_down_type_scale_convention_support.py
```

Expected final line:

```text
SUMMARY: EXACT_PASS=34 COMPARATOR_PASS=6 FAIL=0
```
