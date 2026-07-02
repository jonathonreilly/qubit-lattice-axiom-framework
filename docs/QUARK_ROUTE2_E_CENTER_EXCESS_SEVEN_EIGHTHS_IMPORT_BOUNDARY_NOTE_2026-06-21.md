# Quark Route-2 E-Center Excess Seven-Eighths Import Boundary Note

**Date:** 2026-06-21
**Type:** exact-support / exact negative boundary
**Primary runner:** [scripts/frontier_quark_route2_e_center_excess_seven_eighths_import_boundary_2026_06_21.py](../scripts/frontier_quark_route2_e_center_excess_seven_eighths_import_boundary_2026_06_21.py)

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This packet identifies the exact Route-2 target as a seven-eighths E-center excess and proves that the visible seven-eighths anchors are not typed to that role."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Scope

The active S3/Route-2 readout gate asks for the endpoint triple

```text
(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E) = (-1, -2, 21/4).
```

After the two T-side entries are granted, the remaining E-side datum is

```text
rho_E := beta_E / alpha_E = 21/4.
```

This packet rewrites that datum as a Route-2 E-center excess target:

```text
e_E := q_E - 1 = rho_E / 6.
```

The exact target is therefore

```text
e_E = 7/8.
```

The result here is not a derivation of the E-side datum. It is a sharper
support and import-boundary statement: existing exact appearances of `7/8` in
the repo are useful candidate sources, but none is currently typed as the
Route-2 E-center excess `rho_E / 6`.

## Exact Route-2 Equivalence

The current Route-2 readout-map authorities use the support-side center step

```text
delta_A1(center) - delta_A1(shell) = 1/6.
```

Therefore

```text
q_E = gamma_E(center) / gamma_E(shell)
    = 1 + (beta_E / alpha_E) / 6
    = 1 + rho_E / 6.
```

Define

```text
e_E := q_E - 1 = rho_E / 6.
```

Then exact rational arithmetic gives the target chain

```text
rho_E = 21/4
<=> e_E = 7/8
<=> q_E = 15/8.
```

With the granted T-side values

```text
rho_T = -1,
alpha_T / alpha_E = -2,
q_T = 5/6,
```

the same target is equivalent to the signed center ratio

```text
c_TE := gamma_T(center) / gamma_E(center) = -8/9.
```

Thus a source theorem that proves `e_E = 7/8` on the Route-2 E-center readout
surface would supply the missing E-side entry. The current packet does not find
such a theorem.

## Visible Seven-Eighths Anchors

The repo has several exact or bounded contexts where the same rational appears.
They are not interchangeable with the Route-2 E-center excess unless a typed
role bridge is supplied.

| Anchor | Existing role | Boundary for this Route-2 target |
|---|---|---|
| `rho_E / 6 = 7/8` in the E-center lift attempt | Target arithmetic | It restates the missing value as an exact equivalent form; it does not source the value. |
| Hierarchy Riemann-Dirichlet dimensional anchor | Exact arithmetic coincidence at `d = 4` | It contains no Route-2 E-channel readout object, `rho_E`, `q_E`, or gamma-ratio role. |
| Thermal Stefan-Boltzmann ratio | Fermi/Bose thermal-integral weight | It supplies a thermal dof weight, not a Route-2 center-vs-shell readout coefficient. |
| APBC / radian inventory `7/8` | Contextual APBC fourth-power factor | It is a same-rational context without a typed E-center source/readout edge. |
| Color-adjoint complement candidate `(N_c^2 - 2)/(N_c^2 - 1)` at `N_c = 3` | New candidate arithmetic in this packet | It is exact, but it is not an existing authority edge and does not identify the Route-2 E-center excess. |

The last row is included only because it is a compact color-side candidate:

```text
(N_c^2 - 2)/(N_c^2 - 1) = 7/8  at  N_c = 3.
```

It is not the adjoint fraction `F_adj = (N_c^2 - 1)/N_c^2 = 8/9`, and it is
not currently typed as an E-center excess. A proof using this candidate would
need a new source-domain theorem that explains why the connected color-adjoint
denominator rather than the total color denominator supplies `e_E`.

## Import Boundary

The current typed bridge graph has exact Route-2 equivalence edges:

```text
route2_rho_E_21_4 <-> route2_e_E_7_8 <-> route2_q_E_15_8 <-> route2_cTE_minus_8_9
```

It also has independent exact seven-eighths anchors:

```text
hierarchy_d4_eta_zeta_7_8
thermal_fermi_bose_7_8
apbc_fourth_power_7_8
color_adj_complement_candidate_7_8
```

What it does not have is any edge of the form

```text
existing_7_8_anchor -> route2_e_E_7_8.
```

Adjoining such an edge would immediately reach the S3/Route-2 missing E-side
entry by exact algebra. Without it, importing an existing `7/8` value into
`rho_E / 6` is a role substitution rather than a derivation.

## Consequence For The Next Positive Route

The next positive theorem target can now be stated in its shortest form:

```text
derive e_E := q_E - 1 = rho_E / 6 = 7/8
```

from a typed Route-2 E-center source/readout primitive, or prove a typed bridge
from one of the existing seven-eighths anchors to that exact E-center excess.

This target is narrower than another search for `21/4`, because it separates
the support denominator `6` from the remaining dimensionless excess. The
support denominator is already present in the center-excess coordinate; the
open source question is why the numerator excess is exactly `7/8`.

## Boundary

This packet does not establish:

- `rho_E = 21/4` from current primitives;
- `q_E = 15/8` from current primitives;
- `gamma_T(center) / gamma_E(center) = -8/9` from current primitives;
- a typed bridge from hierarchy, thermal, APBC, or color-complement `7/8` to
  the Route-2 E-center excess;
- a physical `kappa_EW` weighting rule;
- quark-mass, CKM, or S3-time closure;
- any audit verdict.

It records the exact target equivalence and the import boundary for the
visible same-rational anchors.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_excess_seven_eighths_import_boundary_2026_06_21.py
```

Expected final line:

```text
TOTAL: PASS=53 FAIL=0
```
