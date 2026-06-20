# BBN eta_10 -> Omega_b h^2 Coefficient Admission Bridge

**Date:** 2026-05-28
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Source status:** source-note candidate for independent audit. This note does
not apply an audit verdict and does not promote any downstream cosmology row.
**Primary runner:** `scripts/bbn_eta10_to_omega_b_h2_coefficient_admission_bridge_runner.py`

proposal_allowed: false

**Type:** bounded_theorem
**Status authority:** independent audit lane only.

## 2026-05-28 Audit Repair (conditional arithmetic; premise packet admitted)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The arithmetic and source firewall close only as a conditional admission bridge. The imported P1-P4 packet, including the Cyburt convention/residual normalization, is not retained-grade or registry-accepted authority in this row."*

with repair: *"dependency_not_retained: derive, retire, or explicitly accepted-premise-register the P1-P4 coefficient premise packet, then re-audit whether the bridge can promote beyond conditional admission arithmetic."*.

Deriving or registering the named premise packet as retained authority is
substantive new work, out of scope. This revision narrows via the **admission
path**:

- **Load-bearing (in scope):** Given P1-P4 as supplied inputs, the deterministic unit-conversion arithmetic on the Planck-distribution photon number density (`2 zeta(3)/pi^2` factor) recovers the raw Cyburt+ 2016 coefficient baseline to within `0.107%`; exact equality to `3.6515e-3` uses the explicitly admitted P4 residual `S_Cyburt_exact = 0.9989276742641543`.
- **NON-load-bearing (admitted / not retained):** The P1-P4 premise packet — comprising proton rest mass `m_p` (P1), present-day CMB temperature `T_CMB` (P2), critical-density unit `rho_crit/h^2` from `H_100` and Newton's constant `G` (P3), and the Cyburt convention/residual normalization `S_raw` / `S_Cyburt_exact` (P4). It is recorded as an admitted, not-retained input; the physical higher-tier reading stays conditional on it reaching retained-grade authority.

No new axiom, import, or retained bridge is introduced. The conditional
arithmetic is the load-bearing content; the premise packet stays admitted
until a retained authority for it lands.

## 2026-06-12 P3 critical-density unit decomposition

This repair removes one black-box numerical constant from P3. The runner now
computes

```text
rho_crit / h^2 = 3 H_100^2 / (8 pi G)
```

with `H_100 = 100 km s^-1 Mpc^-1`, `G = 6.67430e-11 m^3 kg^-1 s^-2`, the
SI megaparsec conversion, and the final `kg m^-3 -> g cm^-3` unit conversion.
The calculation recovers `rho_crit/h^2 = 1.878e-29 g cm^-3`.

This is a unit-definition arithmetic repair, not a framework derivation of
`H_100`, `G`, or SI/CGS metrology. P3 remains a supplied physical-constant
premise, but no longer enters as an opaque critical-density unit.

## 2026-06-16 Post-Audit Prefactor And Residual Repair

The 2026-06-15 audit returned `audited_conditional` and identified two
source-side issues that can be repaired without changing the row's conditional
status:

- the displayed Planck-integral derivation skipped the `1/2` phase-space
  prefactor between `d^3p/(2 pi)^3` and the radial integral, even though the
  runner's final factor was the standard `2 zeta(3)/pi^2`;
- the text used `S_Cyburt` in an exact-looking equality without giving the
  numerical residual convention.

This revision repairs both. The radial phase-space reduction is now displayed
as `g * 4 pi / (2 pi)^3 = g / (2 pi^2)`, so
`n_gamma(T) = (g zeta(3) / pi^2) T^3`, and with photon polarization count
`g = 2`, `n_gamma(T) = (2 zeta(3) / pi^2) T^3`.

The runner also distinguishes two P4 readings:

- `S_raw = 1`, the raw unit-conversion baseline, gives
  `Omega_b h^2 / eta_10 = 0.00365541980072764`, which is within `0.107%`
  of the Cyburt+ 2016 comparator `0.0036515`;
- exact comparator equality requires the explicitly admitted residual
  `S_Cyburt_exact = 0.9989276742641543`, defined as
  `0.0036515 / 0.00365541980072764`.

The row still does not derive `S_Cyburt_exact`, `m_p`, `T_CMB`, `G`, `H_100`,
or the metrology constants from framework primitives. The repair removes a
derivation typo and makes the residual convention auditable; it does not
promote the bridge beyond conditional admission arithmetic.

## 2026-06-18 Analytic Factor Import Retirement

This revision removes the last avoidable textbook-math import from the
analytic part of the coefficient. The runner no longer merely names
`zeta(3)` as a supplied constant; it certifies the Planck integral by the
standard internal series proof

```text
1/(exp(x)-1) = sum_{n>=1} exp(-n x),
integral_0^infty x^2 exp(-n x) dx = 2/n^3,
integral_0^infty x^2/(exp(x)-1) dx = sum_{n>=1} 2/n^3 = 2 zeta(3).
```

The executable certificate computes the partial `zeta(3)` sum through
`N=20000` and uses the p-series tail bound

```text
0 <= zeta(3) - sum_{n=1}^N 1/n^3 <= 1/(2 N^2)
```

to bracket the reference `zeta(3)` value and therefore bracket
`2 zeta(3)`. This is an internal math certificate for the analytic
Planck-distribution factor only. It does not derive the Bose gas physical
setup, photon polarization count, proton mass, CMB temperature, Newton
constant, metrology constants, or `S_Cyburt_exact`; those remain exactly the
P1-P4 admitted physical/comparator premises listed below.

## 0. Scope and Boundary

This note formalizes a single textbook coefficient that currently enters the
live cosmology cascade as a quietly imported constant. The coefficient is:

```text
Omega_b * h^2 = 3.6515e-3 * eta_10,    eta_10 = eta * 1e10.
```

This is the standard Cyburt-Fields-Olive-Yeh 2016 conversion between the
baryon-to-photon ratio and the present-day baryon density parameter.

The current cosmology cascade `COSMOLOGY_FROM_MASS_SPECTRUM_NOTE.md`
consumes this coefficient as a single textbook number cited inline. This
admission bridge does **not** derive the coefficient. It decomposes the
coefficient into one analytic factor (the Riemann-zeta photon-density
ratio `2 zeta(3)/pi^2`) plus explicitly imported non-framework inputs, then
records the imports as a named premise packet so a later workstream can retire
them one at a time without re-opening the cascade row.

The decomposition is deterministic unit-conversion arithmetic. The
non-framework inputs (baryonic mass scale, present-day CMB temperature,
critical-density unit, and the small convention / normalization residual
needed to match the published Cyburt+ coefficient) remain imported on this
row.

## 1. Statement

Given the supplied premise packet P1-P4 below, the coefficient decomposes as

```text
C_raw
  = ( [2 zeta(3)/pi^2] * [T_CMB^3 / (rho_crit_per_h2 / m_p)] * S_raw ) * 1e-10,

3.6515e-3 = C_raw * S_Cyburt_exact,
```

where the bracketed factors carry the following imported / framework status:

| factor                          | role                            | framework status |
|---------------------------------|---------------------------------|------------------|
| `2 zeta(3) / pi^2`              | photon number density / T^3     | analytic Planck-distribution factor, not an empirical fit |
| `T_CMB`                         | present-day CMB temperature     | imported (P2) |
| `m_p`                           | proton rest mass                | imported (P1) |
| `rho_crit / h^2`                | computed unit conversion from admitted `H_100` and `G` | imported constants, arithmetic explicit (P3) |
| `S_raw = 1`                     | raw unit-conversion baseline | imported convention baseline (P4) |
| `S_Cyburt_exact = 0.9989276742641543` | exact Cyburt comparator residual | imported comparator convention (P4) |

The bridge proves: **if** P1-P4 are admitted as the non-framework premise
packet, **then** the raw unit-conversion baseline is recovered by
deterministic arithmetic within `0.107%` of the published Cyburt+ 2016
precision, and exact equality to the comparator is recovered only after
admitting `S_Cyburt_exact` as P4. The only analytic non-empirical factor is
the Riemann-zeta photon-density ratio.

This is a bounded admission-bridge that formally exposes the conditional chain
behind the previously-uncited single-number import. It does not eliminate the
admission; it names it.

## 2. Supplied premise packet (not axioms)

The following entries are the complete non-framework premise packet for this
bounded bridge. They are supplied only for this row's coefficient arithmetic;
they are not registry accepted premises and no new repo-wide axiom is
introduced.

- **P1 proton rest mass.** `m_p = 938.272 MeV` is admitted as the textbook
  proton rest mass, with `m_p = 1.6726219e-24 g` in cgs units. The framework
  does not derive `m_p` on this row.
- **P2 present-day CMB temperature.** `T_CMB = 2.725 K` is admitted as the
  textbook present-day CMB photon temperature (FIRAS / Planck). The framework
  does not derive `T_CMB` on this row.
- **P3 critical-density unit.** `rho_crit / h^2 = 1.878e-29 g cm^-3` is
  computed by the runner from the textbook critical-density formula
  `rho_crit/h^2 = 3 H_100^2/(8 pi G)`, the admitted convention
  `H_100 = 100 km s^-1 Mpc^-1`, the admitted Newton constant `G`, and the
  stated SI-to-cgs unit conversion. The framework does not derive `H_100`,
  `G`, or the metrology constants on this row.
- **P4 Cyburt conversion convention / residual normalization.** The raw
  unit-conversion baseline uses `S_raw = 1`. Exact equality to the Cyburt+
  2016 comparator requires the admitted residual
  `S_Cyburt_exact = 0.9989276742641543`, defined by
  `3.6515e-3 / 3.65541980072764e-3`. It carries the small convention
  difference between the raw `m_p * n_gamma0 / (rho_crit/h^2)` unit conversion
  and the published Cyburt+ 2016 coefficient. It may include mean baryonic
  mass convention, rounding/CODATA choices, and the convention by which the
  post-e+e- baryon-to-photon ratio is quoted. It is admitted as a combined
  textbook comparator normalization; the framework does not derive
  `S_Cyburt_exact` on this row.

This row proves: **if** P1-P4 are the non-framework premise packet and the
photon-density factor is read from the Planck blackbody distribution, **then**
the raw coefficient is recovered within `0.107%` of the textbook Cyburt+ 2016
coefficient, with exact equality only after the admitted P4 residual is
applied.

## 3. Decomposition arithmetic

### 3.1 Analytic factor: `2 zeta(3)/pi^2` photon-density ratio

The standard relativistic-boson number density at temperature `T` (in natural
units with `hbar = c = k_B = 1`) follows from the Planck distribution
`f(p) = 1/(exp(p/T) - 1)`:

```text
n_gamma(T)  =  g * integral d^3p / (2 pi)^3 * f(p)
            =  (g / (2 pi^2)) * T^3 * integral_0^inf x^2 dx / (e^x - 1)
            =  (g / (2 pi^2)) * T^3 * 2 * zeta(3)
            =  (g zeta(3) / pi^2) * T^3.
```

With photon polarization count `g_gamma = 2`,

```text
n_gamma(T)  =  (2 * zeta(3) / pi^2) * T^3.                              (I)
```

The bracketed prefactor `2 zeta(3) / pi^2` is pure transcendental arithmetic.
The runner certifies the identity
`integral_0^infty x^2/(exp(x)-1) dx = 2 zeta(3)` by expanding the Planck
kernel into its exponential series and bounding the p-series tail for
`zeta(3)`. `pi` is the framework's single allowed transcendental (consistent
with the `Q-bar(pi)` algebraic-closure convention recorded in
`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`). No fitted cosmological
number enters identity (I), but the Bose-Einstein distribution and the photon
polarization count `g_gamma = 2` are still part of the standard-physics
setup. This factor is analytic, not a framework derivation of the full BBN
coefficient.

### 3.2 Imported factors

Evaluating (I) at the present-day CMB temperature, converted to GeV via
`k_B = 8.617333e-14 GeV/K`:

```text
T_CMB_GeV  =  k_B * T_CMB  =  8.617333e-14 * 2.725  =  2.348e-13 GeV.    (II)
```

Converting to inverse-volume in `cm^-3` via `hbar c = 1.97327e-14 GeV cm`:

```text
n_gamma_today  =  (2 zeta(3) / pi^2) * (T_CMB_GeV / (hbar c))^3
              ~=  410.5 cm^-3.                                          (III)
```

Multiplying by the proton rest mass `m_p = 1.6726e-24 g` and a Cyburt
conversion convention factor `S` gives the present-day baryon mass density per
unit `eta`:

```text
rho_b(eta)  =  eta * n_gamma_today * m_p * S.                          (IV)
```

The `eta = n_b / n_gamma` convention used in the coefficient is the
post-e+e- baryon-to-photon ratio convention. This row does not derive that
convention; it records the residual Cyburt normalization as an admitted
input.

The runner computes the critical-density unit as

```text
H_100        = 100 km s^-1 Mpc^-1
             = 3.240779...e-18 s^-1,
rho_crit/h^2 = 3 H_100^2 / (8 pi G)
             = 1.878e-26 kg m^-3
             = 1.878e-29 g cm^-3.                                      (V)
```

Dividing by that computed P3 unit with the raw baseline `S_raw = 1`:

```text
Omega_b h^2 / eta  =  n_gamma_today * m_p * S_raw / (rho_crit / h^2)
                  =  410.5 * 1.6726e-24 / 1.878e-29
                  ~=  3.65541980072764e7.                                (VI)
```

With `S_raw = 1` as the raw unit-conversion baseline:

```text
Omega_b h^2 / eta  ~=  3.65541980072764e7,
Omega_b h^2 / eta_10  ~=  3.65541980072764e-3,                           (VII)
```

within `0.107%` of the published Cyburt+ 2016 value `3.6515e-3`. Exact
equality to that comparator is a separate admitted P4 residual:

```text
S_Cyburt_exact = 3.6515e-3 / 3.65541980072764e-3
               = 0.9989276742641543.                                  (VIII)
```

The residual sub-percent gap is the admitted P4 convention / normalization
residual, not a framework derivation.

### 3.3 Retention scorecard

| component | numerical content | framework status after this bridge |
|---|---|---|
| `2 zeta(3) / pi^2` | Riemann zeta arithmetic, photon polarization count | analytic, non-empirical factor inside the supplied setup |
| `T_CMB` | 2.725 K, set by CMB-FIRAS measurement | imported (P2) |
| `m_p` | 938.272 MeV, set by QCD spectroscopy | imported (P1) |
| `rho_crit / h^2` | `3 H_100^2/(8 pi G)` plus unit conversion | formula computed from admitted `H_100` and `G` (P3) |
| `S_raw` | raw conversion convention baseline | imported (P4) |
| `S_Cyburt_exact` | exact comparator residual `0.9989276742641543` | imported (P4) |

**The photon-density factor is analytic rather than empirical, and the
critical-density unit is formula-expanded instead of black-boxed.** The four
premise classes P1-P4 remain admitted because P1, P2, P3's physical constants,
and P4's comparator residual are still supplied. This is the canonical
import-name-it admission step, sharpened so the unit arithmetic is executable.

## 4. What this bridge does NOT close

This bridge intentionally does not close:

- derivation of the proton rest mass `m_p` (separate QCD spectroscopy
  workstream);
- derivation of the present-day CMB temperature `T_CMB` (separate cosmology
  / Planck-pin workstream);
- derivation of the Hubble unit `H_100`, Newton's constant `G`, or the SI/CGS
  metrology constants entering `rho_crit / h^2` (the formula and unit
  conversion are computed here; the physical constants are not);
- derivation of the photon entropy / e+e- annihilation / neutrino-decoupling
  convention used to quote the post-e+e- baryon-to-photon ratio;
- derivation of the Cyburt+ convention / normalization residual;
- any parent theorem/status promotion of the cosmology cascade row. The
  bridge records the decomposition as a separate bounded identity candidate;
  downstream status of the parent cosmology cascade is decided by the audit
  lane and remains gated on the four imports.

The Cyburt+ 2016 textbook coefficient stays imported on this row. The
bridge names the coefficient's premise packet so that future retirement of
any individual premise can be tracked mechanically without re-opening the
cosmology cascade.

## 5. Load-Bearing Dependencies

This bridge has no retained-grade load-bearing dependencies on framework
authorities. The analytic factor `2 zeta(3) / pi^2` is elementary
analysis of the supplied Planck distribution and is computed inline. P3's
critical-density arithmetic is also computed inline from its admitted
physical constants. The four admitted premise classes (P1-P4) are explicit
textbook imports recorded in section 2.

## 6. Non-Load-Bearing Context

- `COSMOLOGY_FROM_MASS_SPECTRUM_NOTE.md` is the conditional parent
  cascade row in which the textbook coefficient `3.6515e-3` was previously
  cited inline without a named premise packet. This bridge is meant to
  formally expose that coefficient's import status; it is not a dependency
  of this proof.
- `ETA_188_STRUCTURAL_ORIGIN_PARTIAL_NOTE_2026-05-03.md` and
  `DM_ETA_FREEZEOUT_BYPASS_QUANTITATIVE_THEOREM_NOTE_2026-04-25.md` are
  adjacent open / bounded work on `eta` itself; they consume the same
  coefficient downstream of the BBN link. Both are context, not
  load-bearing inputs for this row.
- `ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md` records the
  framework's central index of Tier-A admissions; this bridge supplies
  exactly the kind of named premise packet that future retirement work
  would mechanically reduce.

## 7. Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/bbn_eta10_to_omega_b_h2_coefficient_admission_bridge_runner.py
```

Expected:

```text
TOTAL: PASS=35 FAIL=0
VERDICT: bounded admission bridge passes; the textbook coefficient
3.6515e-3 is split into a raw unit-conversion baseline from one analytic
factor (2 zeta(3)/pi^2 from the Planck distribution) and admitted physical
premises (P1 m_p, P2 T_CMB, P3 H_100/G critical-density unit), plus explicit
admitted P4 residual S_Cyburt_exact = 0.9989276742641543. The raw baseline is
within 0.107% of the Cyburt+ 2016 published value; exact equality uses the
admitted residual comparator.
```

## 8. Audit Boundary

Audit status is set only by the independent audit lane. The intended
source-side claim type is `bounded_theorem`: assuming the supplied
P1-P4 premise packet, deterministic arithmetic on the Planck-distribution photon
number density gives the Cyburt+ 2016 coefficient to better than
0.2%. This row does not derive P1-P4, does not promote the cosmology
cascade row, and does not change the import status of `eta` on the
parent cascade.
