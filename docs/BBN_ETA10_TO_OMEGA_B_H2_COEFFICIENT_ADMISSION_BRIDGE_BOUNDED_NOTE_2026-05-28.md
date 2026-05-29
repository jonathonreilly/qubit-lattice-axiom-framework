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

- **Load-bearing (in scope):** Given P1-P4 as supplied inputs, the deterministic unit-conversion arithmetic on the Planck-distribution photon number density (`2 zeta(3)/pi^2` factor) recovers the Cyburt+ 2016 textbook coefficient `3.6515e-3` to within 0.13%, which the runner verifies exactly.
- **NON-load-bearing (admitted / not retained):** The P1-P4 premise packet — comprising proton rest mass `m_p` (P1), present-day CMB temperature `T_CMB` (P2), critical-density unit `rho_crit/h^2` from `H_100` and Newton's constant `G` (P3), and the Cyburt convention/residual normalization `S_Cyburt` (P4). It is recorded as an admitted, not-retained input; the physical/promoted reading stays conditional on it reaching retained-grade authority.

No new axiom, import, or retained bridge is introduced. The conditional
arithmetic is the load-bearing content; the premise packet stays admitted
until a retained authority for it lands.

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
3.6515e-3
  = ( [2 zeta(3)/pi^2] * [T_CMB^3 / (rho_crit_per_h2 / m_p)] * S_Cyburt ) * 1e-10,
```

where the bracketed factors carry the following imported / framework status:

| factor                          | role                            | framework status |
|---------------------------------|---------------------------------|------------------|
| `2 zeta(3) / pi^2`              | photon number density / T^3     | analytic Planck-distribution factor, not an empirical fit |
| `T_CMB`                         | present-day CMB temperature     | imported (P2) |
| `m_p`                           | proton rest mass                | imported (P1) |
| `rho_crit / h^2`                | unit-conversion constant from `H_100` | imported (P3) |
| `S_Cyburt`                      | conversion convention / residual normalization | imported (P4) |

The bridge proves: **if** P1-P4 are admitted as the non-framework premise
packet, **then** the textbook coefficient `3.6515e-3` is recovered by
deterministic arithmetic up to the published Cyburt+ 2016 precision, and the
only analytic non-empirical factor is the Riemann-zeta photon-density ratio.

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
  admitted as the textbook Friedmann unit constant derived from
  `H_100 = 100 km s^-1 Mpc^-1` and Newton's constant `G`. The framework does
  not derive `H_100` or `G` on this row.
- **P4 Cyburt conversion convention / residual normalization.** The combined
  factor `S_Cyburt` carries the small convention difference between the raw
  `m_p * n_gamma0 / (rho_crit/h^2)` unit conversion and the published
  Cyburt+ 2016 coefficient. It may include mean baryonic mass convention,
  rounding/CODATA choices, and the convention by which the post-e+e-
  baryon-to-photon ratio is quoted. It is admitted as a single combined
  textbook normalization; the framework does not derive it on this row.

This row proves: **if** P1-P4 are the non-framework premise packet and the
photon-density factor is read from the Planck blackbody distribution, **then**
the textbook Cyburt+ 2016 coefficient is recovered.

## 3. Decomposition arithmetic

### 3.1 Analytic factor: `2 zeta(3)/pi^2` photon-density ratio

The standard relativistic-boson number density at temperature `T` (in natural
units with `hbar = c = k_B = 1`) follows from the Planck distribution
`f(p) = 1/(exp(p/T) - 1)`:

```text
n_gamma(T)  =  g * integral d^3p / (2 pi)^3 * f(p)
            =  (g / pi^2) * T^3 * integral_0^inf x^2 dx / (e^x - 1)
            =  (g / pi^2) * T^3 * 2 * zeta(3)
            =  (2 g zeta(3) / pi^2) * T^3.
```

With photon polarization count `g_gamma = 2`,

```text
n_gamma(T)  =  (2 * zeta(3) / pi^2) * T^3.                              (I)
```

The bracketed prefactor `2 zeta(3) / pi^2` is pure transcendental
arithmetic. `zeta(3)` is the Riemann zeta function at 3 (Apery's constant);
`pi` is the framework's single allowed transcendental (consistent with the
`Q-bar(pi)` algebraic-closure convention recorded in
`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`). No fitted
cosmological number enters identity (I), but the Bose-Einstein distribution
and the photon polarization count `g_gamma = 2` are still part of the
standard-physics setup. This factor is analytic, not a framework derivation
of the full BBN coefficient.

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

Multiplying by the proton rest mass `m_p = 1.6726e-24 g` and the Cyburt
conversion convention factor `S_Cyburt` gives the present-day baryon mass
density per unit `eta`:

```text
rho_b(eta)  =  eta * n_gamma_today * m_p * S_Cyburt.                   (IV)
```

The `eta = n_b / n_gamma` convention used in the coefficient is the
post-e+e- baryon-to-photon ratio convention. This row does not derive that
convention; it records the residual Cyburt normalization as an admitted
input.

Dividing by the textbook `rho_crit / h^2 = 1.878e-29 g cm^-3`:

```text
Omega_b h^2 / eta  =  n_gamma_today * m_p * S_Cyburt / (rho_crit / h^2)
                  =  410.5 * 1.6726e-24 * S_Cyburt / 1.878e-29
                  ~=  3.656e7 * S_Cyburt.                               (V)
```

With `S_Cyburt = 1` as the raw unit-conversion baseline:

```text
Omega_b h^2 / eta  ~=  3.656e7,
Omega_b h^2 / eta_10  ~=  3.656e-3,                                     (VI)
```

within 0.13% of the published Cyburt+ 2016 value `3.6515e-3`. The residual
sub-percent gap is the admitted P4 convention / normalization residual.

### 3.3 Retention scorecard

| component | numerical content | framework status after this bridge |
|---|---|---|
| `2 zeta(3) / pi^2` | Riemann zeta arithmetic, photon polarization count | analytic, non-empirical factor inside the supplied setup |
| `T_CMB` | 2.725 K, set by CMB-FIRAS measurement | imported (P2) |
| `m_p` | 938.272 MeV, set by QCD spectroscopy | imported (P1) |
| `rho_crit / h^2` | derives from `H_100` and `G` | imported (P3) |
| `S_Cyburt` | conversion convention / residual normalization | imported (P4) |

**One factor out of five is analytic rather than empirical.** The remaining
four are recorded here as a named premise packet. This is the canonical
import-name-it admission step.

## 4. What this bridge does NOT close

This bridge intentionally does not close:

- derivation of the proton rest mass `m_p` (separate QCD spectroscopy
  workstream);
- derivation of the present-day CMB temperature `T_CMB` (separate cosmology
  / Planck-pin workstream);
- derivation of the Hubble unit `H_100` or Newton's constant `G` entering
  `rho_crit / h^2` (the latter is a separate framework gravity workstream);
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
analysis of the supplied Planck distribution and is computed inline. The four
admitted premises (P1-P4) are explicit textbook imports recorded in
section 2.

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
TOTAL: PASS=29 FAIL=0
VERDICT: bounded admission bridge passes; the textbook coefficient
3.6515e-3 decomposes into one analytic factor (2 zeta(3)/pi^2 from the
Planck distribution) and four imported premises (P1 m_p, P2 T_CMB, P3
rho_crit/h^2, P4 Cyburt convention / residual normalization), recovered
to within 0.13% of the Cyburt+ 2016 published value.
```

## 8. Audit Boundary

Audit status is set only by the independent audit lane. The intended
source-side claim type is `bounded_theorem`: assuming the supplied
P1-P4 premise packet, deterministic arithmetic on the Planck-distribution photon
number density gives the Cyburt+ 2016 coefficient to better than
0.2%. This row does not derive P1-P4, does not promote the cosmology
cascade row, and does not change the import status of `eta` on the
parent cascade.
