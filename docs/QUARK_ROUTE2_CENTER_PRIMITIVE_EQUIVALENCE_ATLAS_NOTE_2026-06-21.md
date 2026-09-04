# Quark Route-2 Center Primitive Equivalence Atlas

**Date:** 2026-06-21
**Claim type:** no_go
**Claim scope:** no_go
**Status authority:** independent audit lane only. This source note does not set, claim, or predict an audit outcome.
**Actual current-surface status:** no-go / exact residual atlas; no endpoint closure
**Trace class:** negative_route_pruning
**Reachability to target:** prunes a Route-2 endpoint escape route; does not derive the endpoint triple.
**Primary runner:** [`scripts/frontier_quark_route2_center_primitive_equivalence_atlas_2026_06_21.py`](../scripts/frontier_quark_route2_center_primitive_equivalence_atlas_2026_06_21.py)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_center_primitive_equivalence_atlas_2026_06_21.txt`](../logs/runner-cache/frontier_quark_route2_center_primitive_equivalence_atlas_2026_06_21.txt)
**Authority links:** [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md), [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md), [QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md), [QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md), [QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md), [QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md), [QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md), [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

## Scope

This block attacks the remaining S3/Route-2 readout endpoint residual by
putting the now-isolated center primitives on one exact rational surface.

Under the granted T-side values

```text
beta_T/alpha_T = -1,
alpha_T/alpha_E = -2,
```

the exact carrier/readout algebra gives

```text
q_T = 5/6,
s_TE = gamma_T(shell)/gamma_E(shell) = -2,
q_E = 1 + rho_E/6,
c_TE = gamma_T(center)/gamma_E(center) = s_TE q_T / q_E.
```

The remaining endpoint target may be written in several equivalent forms:

```text
rho_E = 21/4
q_E = 15/8
c_TE = -8/9
lambda := q_E/q_T = 9/4
```

Block94/95 also isolate a positive diagonal metric specialization

```text
b/a = 1449/704,
```

and the O_h covariance route isolates the inverse-square projector-weight form

```text
lambda = (w_E/w_T)^(-2) = 9/4,
w_E = 1/3,
w_T = 1/2.
```

This note verifies the exact equivalence web and then records that current
named surfaces do not supply any of these as a derived Route-2 source/readout
primitive.

## Authority Inputs

- [[QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  supplies the restricted readout map and endpoint algebra.
- [[QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)
  proves the E-channel parameter remains free under minimal naturality.
- [[QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md)](QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md)
  records the exact conditional center-bridge arithmetic and named missing
  computation.
- [[QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md)](QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md)
  records that the current source bank has no typed `R_conn -> c_TE` bridge.
- [[QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)](QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md)
  relocates the covariance route to `lambda = kappa^2` while keeping the bridge
  open.
- [[QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)](QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md)
  closes the quadratic O_h-invariant route as a selector for the covariance.
- [[QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md](QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md)](QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md)
  closes the bulk-limit promotion of the measured `N=15` coincidence.
- [[MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)](MINIMAL_AXIOMS_2026-06-05.md)
  withholds readout context, weighting, probability, dynamics, and physical
  observable bridges from the base Record/Quantum surface.

## Exact Equivalence Atlas

With the granted T-side values, the following entries are exact and mutually
convertible in the positive E-lift branch:

| Primitive slot | Value | Conversion to target |
|---|---:|---|
| E readout ratio | `rho_E = 21/4` | `q_E = 1 + rho_E/6 = 15/8` |
| E center lift | `q_E = 15/8` | `rho_E = 6(q_E - 1) = 21/4` |
| E/T center bridge | `c_TE = -8/9` | `q_E = (-2)(5/6)/c_TE = 15/8` |
| Cross-channel covariance | `lambda = q_E/q_T = 9/4` | `q_E = lambda q_T = 15/8` |
| Diagonal metric selector | `b/a = 1449/704` | `q_E^2 = 1 + (11/9)(b/a) = (15/8)^2` |
| O_h inverse-square lift | `(w_E/w_T)^(-2)=9/4` | same covariance slot `lambda=9/4` |
| SU(3) color route | `F_adj=8/9` | reaches target only if `c_TE=-F_adj` is supplied |

The important boundary is that these are equivalent discharge forms, not
independent derivations. Supplying any one as a typed Route-2 source/readout
primitive closes the arithmetic. Current surfaces do not supply that primitive.

## Current Route Firewall

The current named surfaces leave the following status:

- Minimal naturality and E-center-blind endpoint constraints leave `rho_E`
  free.
- The Rconn/color route supplies `F_adj=8/9`, but not the typed signed bridge
  from the color fraction to `c_TE`.
- The same-domain O_h route supplies `kappa=3/2` and the value
  `kappa^2=9/4`, but not the covariance bridge `lambda=kappa^2`.
- The quadratic O_h route leaves the E:T quadratic ratio free.
- The measured `N=15` stack calibration and box-size scan are comparator and
  falsifier surfaces, not a bulk-limit derivation.
- The metric selector can select the target only by supplying a metric tensor
  satisfying the exact target equation; current metric surfaces do not derive
  that tensor.

## Result

**Theorem (Route-2 center primitive equivalence atlas and firewall).** Under
the granted T-side values, the target endpoint forms

```text
rho_E=21/4, q_E=15/8, c_TE=-8/9, lambda=9/4,
b/a=1449/704
```

are exactly equivalent discharge forms in their respective primitive slots.
The current named Route-2, Rconn/color, O_h covariance, quadratic, measured
calibration, bulk-limit, and minimal-axiom surfaces do not derive any of those
slots as a typed Route-2 source/readout primitive. The residual is therefore
not many independent mysteries; it is one missing center primitive with several
equivalent exact faces.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_center_primitive_equivalence_atlas_2026_06_21.py
```

Expected result:

```text
TOTAL: PASS=49, FAIL=0
VERDICT: the Route-2 center primitive has equivalent exact faces, but no current surface derives it.
```

## Sign Discharge (2026-09-03 densify absorb-repair K1)

With the granted T-side values `q_T = 5/6` and `s_TE = -2`, the endpoint
algebra gives `c_TE = s_TE q_T / q_E = (-5/3)/q_E`. Positivity of the E-center
lift (`q_E > 0`, equivalently `rho_E > -6`) therefore **forces `c_TE < 0`**
for the entire admissible family. Consequently a magnitude-only bridge

```text
|c_TE| = R_conn = 8/9
```

suffices for the full endpoint: the `c_TE = +8/9` branch gives `q_E = -15/8`
and `rho_E = -69/4`, failing both `q_E > 0` and `rho_E > -6`. The open color
import is thereby reduced to the typed magnitude bridge plus the already-forced
sign. (Absorbed from
`QUARK_ROUTE2_RCONN_MAGNITUDE_SIGN_SPLIT_EXACT_SUPPORT_NOTE_2026-06-21.md`,
now a work-history record.)

## Admissibility Gate For Any Future E-Center Primitive (2026-09-03 densify absorb-repair K3)

A candidate primitive closes the endpoint only if it passes all six gates:

| gate | requirement |
|---|---|
| G1 nonblind | distinguishes `E-center` from `E-shell`, not merely shell normalization or a time-factor property |
| G2 selector | fixes one exact dimensionless value of `rho_E`, `q_E`, or `c_TE` — not only a sign, interval, norm, or scale |
| G3 target-free | no endpoint fitting, nearest-rational matching, observed masses, measured calibration, or target value as input |
| G4 typed Route-2 readout | maps into `gamma_E(center)/gamma_E(shell)` or `gamma_T(center)/gamma_E(center)` via a typed source/readout bridge |
| G5 current-surface | present on the current named source bank, not supplied as the missing premise |
| G6 target-compatible | under the granted T-side values gives `q_E=15/8` / `rho_E=21/4` / `c_TE=-8/9` |

Classification of the eight current candidate families by failing gate:
carrier/time factor-rigidity (G2); registration/positivity (G2); positive
projective `ell_E` family (G2/G6 — supplies the sign, not the magnitude);
step-free active-branch slopes (G2/G3/G4); measured E-center calibration
(G2/G3/G4); `F_adj`/`R_conn` color fraction (G1/G4 absent the typed bridge);
register-not-read color-trace shortcut (G1/G2/G4); explicit `q_E=15/8` premise
(G3/G5 — it *is* the missing premise). No named current-bank candidate passes
all six. (Absorbed from
`QUARK_ROUTE2_NONBLIND_SOURCE_READOUT_PRIMITIVE_GATE_NO_GO_NOTE_2026-06-21.md`,
now a work-history record.)

## Single-Adjoint-Line Wall (2026-09-03 densify absorb-repair K3-extension)

The color route's sharpest surviving structure, compactly:

- **Sufficiency.** A *supplied physical color ray* selects one adjoint line;
  the complementary fraction `7/8` of the adjoint then closes the full
  endpoint through the equivalence web above
  (`QUARK_ROUTE2_COLOR_RAY_ADJOINT_LINE_SELECTOR_BOUNDARY_NOTE_2026-06-21.md`).
- **Obstruction.** The adjoint commutant is scalar: no invariant adjoint line
  and no invariant rank-7 projector exists, so the selection cannot come from
  color symmetry alone
  (`QUARK_ROUTE2_COLOR_COMPLEMENT_SEVEN_EIGHTHS_BRIDGE_NO_GO_NOTE_2026-06-21.md`).
- **Uniqueness.** The `k = 7` uniqueness statement and its falsifiers stay in
  the standing conditional note
  `QUARK_ROUTE2_E_CENTER_SINGLE_ADJOINT_LINE_SELECTOR_CONDITIONAL_SUPPORT_NOTE_2026-06-21.md`.
- **Source-count identity** (stated nowhere else on the primary surface):
  `c_TE = -N_pair^3 / N_color^2` with `N_pair^3 = N_color^2 - 1` at
  `(N_pair, N_color) = (2, 3)`, i.e. `-8/9 = -F_adj` as a counting identity
  (from `QUARK_ROUTE2_SOURCE_COUNT_SELECTOR_BRIDGE_BOUNDARY_NOTE_2026-06-21.md`).
- **Connected-trace selector.** The physical family
  `R_phys(kappa_EW) = (8 + kappa_EW)/9` reaches the target only at the
  connected value `kappa_EW = 0`; that selector is not supplied by any current
  authority.
- **T-side minimality boundary.** The granted T-row `(1, -2, 2)` is *not*
  selected by primitivity/minimality rules (those pick `n = 1` or
  `beta_T in {0, 1}`); the named missing T-side premise is a physical
  multiplicity-two rule.

None of these lines changes the atlas verdict: the center primitive remains
underived, with one missing typed bridge carrying several equivalent faces.
