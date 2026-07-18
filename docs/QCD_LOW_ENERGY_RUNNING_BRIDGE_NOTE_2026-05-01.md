# QCD `v -> M_Z` Supplied-Input Transfer-Map Theorem

**Date:** 2026-05-01; two-loop EFT repair 2026-07-18
**Type:** bounded_theorem
**Claim scope:** the exact piecewise one-loop transfer formula on
`D = [0.085, 0.130]`, plus finite numerical observations for an explicitly
defined piecewise two-loop QCD EFT map on the ten-point grid
`G = {0.085, 0.090, ..., 0.130}` and at the separate center point `0.1075`.
**Status authority:** the independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:** `scripts/frontier_qcd_low_energy_running_bridge.py`

## 1. Repair and narrow boundary

The previous two-loop implementation was not the system named by the note. It
changed the one-loop `n_f` coefficient below `m_t` while retaining the
six-flavor Standard Model two-loop `g_3` term and continuing to evolve an
active top Yukawa. That hybrid is neither the full un-decoupled Standard Model
nor a five-flavor QCD EFT. The previous note also inferred a threshold bracket
for that coupled flow from `beta_0(5) > beta_0(6)` alone and called
`T_2 - T_1` a truncation envelope without a higher-order remainder argument.

This repair keeps the exact one-loop theorem and replaces the hybrid with the
narrow scalar QCD EFT map defined below. It makes only finite-grid claims for
the two-loop ordering and expansivity observations, and it reports
`T_2 - T_1` only as an observed order-to-order shift.

No PDG target value, preferred `alpha_s(v)` boundary value, or target-matching
boolean is part of this packet. Comparator uses remain the responsibility of
downstream notes and are not evidence for this theorem.

## 2. Supplied data and external infrastructure

The theorem is about the transfer map defined by these supplied inputs; it is
not a derivation of QCD, `alpha_s(v)`, or any physical scale from the framework
axioms.

1. The external continuum input is the massless `MSbar` QCD beta function
   through two loops for `n_f` active fundamental quark flavors.
2. The supplied scales are

   ```text
   v   = 246.282818290129 GeV,
   m_t = 172.69 GeV  (supplied pole-mass threshold),
   M_Z = 91.1876 GeV.
   ```

   Only the supplied top marker lies between `v` and `M_Z`; bottom and charm
   thresholds are not crossed.
3. At `mu = m_t`, the map uses the supplied identity matching prescription

   ```text
   alpha_s^(5)(m_t) := alpha_s^(6)(m_t).
   ```

   This is the one-loop matching prescription at the chosen pole-mass
   threshold, not an all-orders no-jump theorem. In the standard decoupling
   relation at `mu = m_h`, the one-loop constant is zero; for a pole mass the
   first nonzero constant shown by the official QCD review is the coefficient
   multiplying `alpha_s^2` in the matching bracket. Thus the first omitted
   nonzero change in `alpha_s` is absolute order `alpha_s^3`. This packet sets
   that and all higher matching corrections to zero by definition and supplies
   no bound on them.
4. The domain and finite grid are

   ```text
   D = [0.085, 0.130],
   G = {0.085, 0.090, 0.095, 0.100, 0.105,
        0.110, 0.115, 0.120, 0.125, 0.130}.
   ```

No electroweak auxiliary tuple is supplied or evolved. In particular, no
un-decoupled `y_t`, `g_1`, `g_2`, or Higgs coupling is carried into the
five-flavor segment.

## 3. Coefficients and convention conversion

Let `T^a = lambda^a/2` be the fundamental Gell-Mann generators. The runner
reconstructs

```text
Tr(T^a T^b) = T_F delta^(ab),     T_F = 1/2,
f^(acd) f^(bcd) = C_A delta^(ab), C_A = 3,
sum_a T^a T^a = C_F I,            C_F = 4/3.
```

In the convention

```text
dg/d ln(mu)
  = -beta_0 g^3/(16 pi^2) - beta_1 g^5/(16 pi^2)^2,
```

the standard two coefficients are

```text
beta_0 = (11/3) C_A - (4/3) T_F n_f,

beta_1 = (34/3) C_A^2
         - [(20/3) C_A + 4 C_F] T_F n_f.
```

Substitution gives

```text
(beta_0, beta_1) at n_f=6 = (7, 26),
(beta_0, beta_1) at n_f=5 = (23/3, 116/3).
```

For `alpha_s = g^2/(4 pi)`, the chain rule

```text
d alpha_s/d ln(mu) = [g/(2 pi)] dg/d ln(mu)
```

gives the scalar equation used by the runner:

```text
d alpha_s/d ln(mu)
  = -beta_0 alpha_s^2/(2 pi)
    -beta_1 alpha_s^3/(8 pi^2).
```

The factor `1/(8 pi^2)` is therefore fixed by the displayed `g` convention;
it is not a fitted normalization.

## 4. Transfer-map definitions

Write `a = alpha_s(v)`.

### `T_1`: exact piecewise one-loop map

Run with `n_f=6` from `v` to `m_t`, apply the supplied identity matching map,
then run with `n_f=5` from `m_t` to `M_Z`. Direct integration gives

```text
1/T_1(a) = 1/a - L,

L = [7/(2 pi)] ln(v/m_t) + [(23/3)/(2 pi)] ln(m_t/M_Z)
  = 1.1746670550677...
```

This is the preserved exact result. Since `1 - L a > 0` throughout `D`, it is
finite and positive there. Its exact derivative is

```text
dT_1/da = 1/(1 - L a)^2 = [T_1(a)/a]^2 > 1 on D.
```

### `T_2`: supplied piecewise two-loop QCD EFT map

`T_2(a)` is defined by solving the scalar two-loop equation with `n_f=6` on
`[m_t,v]`, carrying `alpha_s` identically at `m_t`, and solving it with
`n_f=5` on `[M_Z,m_t]`. It is a two-loop-running/one-loop-matching map. It is
not a full coupled Standard Model flow and is not a complete decoupled
electroweak EFT.

For an independent constant-`n_f` check, set

```text
c_f = beta_1/(4 pi beta_0),
Phi_f(alpha) = 1/alpha + c_f ln[alpha/(1 + c_f alpha)].
```

Each segment obeys the implicit analytic relation

```text
Phi_f(alpha_out) - Phi_f(alpha_in)
  = [beta_0/(2 pi)] ln(mu_out/mu_in).
```

The runner solves this relation independently on each segment and compares it
with direct numerical integration.

## 5. Narrow kernel theorem (K1-K5)

### K1. Coefficient and conversion certificate

The matrix reconstruction gives `T_F=1/2`, `C_A=3`, and `C_F=4/3`; the
displayed group formulas then give `(7,26)` for `n_f=6` and
`(23/3,116/3)` for `n_f=5`. Direct chain-rule evaluation of the `g` equation
agrees with the implemented `alpha_s` equation at every point of `G` for both
flavor counts, with maximum residual `1.1e-17`.

### K2. Exact one-loop theorem on the whole domain

The formula `1/T_1(a)=1/a-L` and its derivative identity hold analytically for
every `a` in `D`. The pole `1/L = 0.851305...` lies a factor `6.5485` above
the upper domain edge. Independent one-loop integration agrees with the
closed form at every grid point with maximum residual `7.3e-16`.

### K3. Finite two-loop grid certificate

At every point of the declared ten-point grid `G`, `T_2` is finite and
positive. Its grid image is

```text
[T_2(0.085), T_2(0.130)]
  = [0.094774427..., 0.154884028...].
```

RK45 and DOP853 agree across the full grid to at most `8.2e-15`; RK45 and the
independent implicit segment solution agree to at most `7.7e-15`. The sampled
values are strictly increasing, every adjacent grid secant is greater than
one (minimum `1.256627`), and the separate center-point inverse round-trip
recovers `0.1075` to `9.1e-16`.

These are finite observations on `G` plus one center check. They are not an
analytic continuum theorem for `T_2` between grid points and do not establish
a global two-loop bijection on `D`.

### K4. Threshold ordering is a finite observation

The runner separately computes the `n_f=6`-only, matched, and `n_f=5`-only
maps using the same scalar two-loop equation. At all ten points of `G` it
observes

```text
T_2[n_f=6 only] < T_2[matched] < T_2[n_f=5 only].
```

The smallest matched-minus-`n_f=6` gap is `6.882e-4`; the smallest
`n_f=5`-minus-matched gap is `3.854e-4`. The theorem claims only this tested
finite ordering. It does not infer a continuum comparison theorem from the
coefficient inequalities alone.

### K5. Observed order-to-order shift, not a remainder bound

Across `G`, the observed difference `T_2-T_1` is positive and ranges from
`3.461e-4` to `1.454e-3`. At the separate center point,

```text
T_1(0.1075) = 0.123036665...,
T_2(0.1075) = 0.123794102...,
T_2 - T_1   = 7.574e-4.
```

This difference is only the observed change between the two defined
truncations. It is not a conservative estimate, envelope, error bar,
higher-order remainder, or bound on omitted running or threshold terms. The
runner supplies a computed counterexample family with an unconstrained
`alpha_s^4` beta-function term for which the next change exceeds
`|T_2-T_1|`; that family is a logic counterexample, not a physical `beta_2`
input.

## 6. Independent reconstruction and hostile mutations

The primary runner provides three modes:

```bash
python3 scripts/frontier_qcd_low_energy_running_bridge.py
python3 scripts/frontier_qcd_low_energy_running_bridge.py --independent
python3 scripts/frontier_qcd_low_energy_running_bridge.py --hostile
```

The normal mode reports `PASS=15 FAIL=0`. The independent mode reconstructs
`beta_0`, `beta_1`, and all ten outputs using separate exact-rational
coefficient substitution and fixed-step RK4, without reading a primary result
table; it reports `PASS=5 FAIL=0`. The hostile mode reports `PASS=7 FAIL=0`
and detects:

- omitted/wrong `beta_1`;
- the wrong factor of two in the two-loop term;
- a beta-function sign flip;
- a missing top threshold;
- `n_f=5` above and `n_f=6` below the threshold;
- reversed scale direction;
- false remainder/envelope semantics.

## 7. What this map does and does not establish

Downstream rows may use this note only as a supplied-input map. They must own
the provenance and scheme identification of any boundary value they feed into
it, and they must label target comparisons separately.

This note does not establish:

- a framework-native value of `alpha_s(v)` or `alpha_s(M_Z)`;
- a PDG match or prediction;
- a full coupled Standard Model RGE below `m_t`;
- finite-mass top effects, a decoupled electroweak EFT, or matching beyond the
  supplied identity prescription;
- a continuum two-loop monotonicity, expansivity, or ordering theorem between
  grid points;
- a higher-order running or matching uncertainty;
- any statement below `M_Z`.

The adjacent
`ALPHA_S_HEAVY_THRESHOLD_MATCHING_KERNEL_THEOREM_NOTE_2026-06-18.md`
proves exact algebra only for defined rational piecewise-affine maps and
identity carries. It supplies no physical QCD coefficient, threshold
placement, or decoupling rule and is not load-bearing for the physics inputs
here. In particular, it supplies no QCD beta coefficient and cannot substitute for threshold physics.

## 8. Sources for the declared continuum infrastructure

- W. E. Caswell, “Asymptotic Behavior of Non-Abelian Gauge Theories to
  Two-Loop Order,” *Phys. Rev. Lett.* **33**, 244 (1974),
  [doi:10.1103/PhysRevLett.33.244](https://doi.org/10.1103/PhysRevLett.33.244).
- D. R. T. Jones, “Two Loop Diagrams in Yang-Mills Theory,” *Nucl. Phys. B*
  **75**, 531 (1974),
  [doi:10.1016/0550-3213(74)90093-5](https://doi.org/10.1016/0550-3213(74)90093-5).
- Particle Data Group, “Quantum Chromodynamics,” 2025 update, Sec. 9.1.1,
  Eqs. (9.3)-(9.4),
  [official review](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-qcd.pdf).

These references support the declared standard continuum formulas and
matching convention; they are not new framework premises or registry entries.

## 9. Frozen-baseline and audit boundary

This repair adds no axiom, admission, primitive, carrier, physical input,
premise-registry entry, or publication-governance change. It edits no audit
verdict, ledger, queue, dispatch, effective-publication, or front-door output.
A fresh independent review and audit remain separate later steps.
