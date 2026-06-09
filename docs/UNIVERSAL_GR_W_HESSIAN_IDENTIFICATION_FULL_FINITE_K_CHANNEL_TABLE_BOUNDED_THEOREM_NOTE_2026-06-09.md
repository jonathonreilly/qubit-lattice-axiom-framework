# W Metric-Hessian Identification and Finite-k Channel Table

**Date:** 2026-06-09
**Claim type:** bounded_theorem (finite-Brillouin-zone source certificate)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note writes no
audit verdict and does not retag any ledger row.
**Primary runner:** [`scripts/frontier_universal_gr_w_hessian_identification_full_channel_table_2026_06_09.py`](../scripts/frontier_universal_gr_w_hessian_identification_full_channel_table_2026_06_09.py) (PASS=12 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_universal_gr_w_hessian_identification_full_channel_table_2026_06_09.txt`](../logs/runner-cache/frontier_universal_gr_w_hessian_identification_full_channel_table_2026_06_09.txt)

## Scope

[`UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md)
left open the full finite-`k` metric-source Hessian of `W` with contact
terms, the full symmetric vertex plus Ward check, `E_g/T_2g` spin-2
isotropy, magnitude, and chiral control.

[`UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md)
left open the identification of its runner-defined vertex/seagull with the
complete metric Hessian of `W`.

This note computes those objects for the native elliptic operator
`D(q) = i sigma.sin(q) + m` and tests whether the opposite-signed curvature
comparator supplied in
[`UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md)
(`V_trace = -k^2/2`, `V_TT = +k^2/2`) is induced by the tested native
one-loop `W` schemes at finite `k`.

## Finding 1 - Metric-Hessian Identification

A declared local vielbein link coupling,

`(sigma_nu + sum_alpha H_{alpha,nu} h(x_mid) sigma_alpha)/2`

on the forward hop, minus the corresponding backward hop, has an exact
second variation of `W = log|det D[h]|` equal to the momentum-space bubble
with midpoint vertex

`V_H = (i/2) sum_{alpha,nu} H_{alpha,nu} sigma_alpha sin(qbar_nu)`.

The runner verifies this two ways in position space: by explicit
`-Tr(G dD G dD)` and by an independent `log|det|` second difference. For the
checked `TT_yz`, `GAU_xy`, and `TT_E` channels, both agree with the
momentum-space prediction to the printed tolerance.

Thus the naive-type stress vertex is the exact `W` metric Hessian of this
declared local metric coupling. The Ward-selected conserved scheme differs
from it by an exhibited local improvement term plus the local diamagnetic
seagull. The runner also reproduces the landed Ward facts: the declared
metric scheme has residual `0.167`, while conserved plus seagull is cubic in
`k0` with `res/k0^3 = 0.0111, 0.0108, 0.0100`.

## Finding 2 - Finite-k Channel Table

Unit-Frobenius-norm channel slopes at `k = 2pi/16`, `m = 1`:

| channel | Ward-selected scheme | naive metric scheme |
|---|---:|---:|
| TT yz (`T_2g`) | +0.006469 | +0.009321 |
| TT (yy-zz)/sqrt2 (`E_g`) | +0.003091 | +0.010295 |
| gauge xy, xz | +0.005779 | +0.001495 |
| gauge xx | +0.001442 | -0.001152 |
| transverse trace (yy+zz)/sqrt2 | +0.003091 | +0.008361 |
| full trace delta/sqrt3 | +0.002541 | -0.001750 |

Both checked TT channels are positive in both schemes. In the Ward-selected
scheme the `E_g/T_2g` split is order one and stable over the accessible
`k` scan: `0.522, 0.523, 0.523`. It also persists in the accessible
light-mass scan: `0.522, 0.561, 0.605` for `m = 1, 0.5, 0.25`.

This is evidence for genuine cubic anisotropy in the tested finite-BZ
elastic constants. It is not a continuum theorem; the deep scaling regime
`k << m << 1` with `q_min << m` is out of scope.

## Finding 3 - Comparator Not Induced in the Tested Class

The Ward-selected trace stiffness is positive, the same sign as TT. The
transverse trace-vs-shear splitting is zero to machine precision at two
checked finite-grid points:

- `+1.4e-16` at `(N=16, m=1, k=2pi/16)`;
- `+8.7e-18` at `(N=12, m=0.7, k=4pi/12)`.

The checked cancellation is explained by the pi-shift mechanism: the
conserved vertex's per-component `cos(qbar) sin(qbar)` factor is pi-periodic,
so the compatible-grid `q_y -> q_y + pi` shift flips the cross-term integrand
and cancels `Pi_yy,zz`. The naive scheme's `sin(qbar)` factor is not
pi-periodic and shows a small nonzero splitting (`-1.9e-3`).

Pure-gauge channels are not suppressed at the slope level in either tested
scheme: `max|gauge|/TT = 0.89` for the Ward-selected scheme and `0.16` for
the naive metric scheme. The seagull fixes the longitudinal contact
structure; it does not give slope-level gauge decoupling in this finite-BZ
table.

Net: in the tested native one-loop `W` schemes at finite `k`, the induced
action is a positive but anisotropic, same-sign, gauge-unsuppressed elastic
stiffness. It does not reproduce the Einstein/Lichnerowicz opposite-sign
trace/TT comparator in this tested class. The comparator remains supplied
rather than induced here; a retirement would need another route, such as a
geometric/Regge route or a future improvement-classification theorem.

## What Is and Is Not Claimed

- **Is:** the metric-Hessian identification for the declared local coupling;
  the finite-BZ channel table; the accessible-scan anisotropy; the checked
  trace/shear degeneracy and pi-shift mechanism; the gauge-channel
  non-suppression; and the not-induced verdict for the supplied comparator in
  the tested native one-loop `W` schemes.
- **Is not:** a continuum dispersion law; a unique-coupling theorem; a
  classification of all local improvements; a derivation of GR channel signs;
  a no-go for the geometric/Regge route; or full GR closure.
- Adds no axiom, no primitive, and no fitted value.

## Boundaries

- 3D native elliptic operator only; time/lapse-shift channels and a 4D
  symmetric `Z^3 x Z_tau` extension are untested.
- Chiral-limit control remains bounded by 3D IR behavior. The light-mass trend
  is reported only at accessible sizes.
- The induced-stiffness magnitude is reported in lattice units (`c_TT/a^2`).
  With the registered [`scale_reference_primitive`](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
  (`a^-1 = M_Pl`), this is a units remark only; no dimensionless physics is
  granted.
- The `k=0` anchor facts are cited, not re-derived here:
  [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md).

## No-Go Discipline Gate

The negative sentence being shipped is narrow: the tested native one-loop `W`
schemes do not induce the Einstein/Lichnerowicz opposite-sign trace/TT
comparator on the finite-BZ grids checked by the runner.

- **N1 - alternative routes.** Declared midpoint metric coupling: attempted,
  gives the naive metric Hessian and does not supply the comparator.
  Ward-selected conserved scheme with local seagull: attempted, gives
  same-sign trace/TT and gauge slopes. Local improvement freedom: not closed;
  this note exhibits one improvement but does not classify all improvements.
  Deep continuum scaling `k << m << 1`: not attempted and out of scope.
  Geometric/Regge curvature route: not attempted and remains open.
- **N2 - wall independence.** The negative has one wall: this finite-BZ native
  one-loop `W` class. It is independent of the geometric route and of future
  improvement-classification work.
- **N3 - hidden-wall scan.** "Native elliptic operator", "declared local
  coupling", "Ward-selected scheme", "finite-BZ grids", and "scale primitive
  as units only" are explicit. No framework-wide GR no-go is assumed.
- **N4 - residual matching.** The degenerate-supermetric comparator residual is
  exactly the opposite-signed trace/TT pair. The runner tests that residual
  against the native one-loop `W` table only.
- **N5 - rhetoric audit.** The tested resolution is the finite-k channel table
  in the named schemes. The note does not claim failure of all matter actions,
  all couplings, all improvements, the continuum limit, or the geometric
  route.
- **N6 - partial-closure scan.** A future derivation of an improvement or
  geometric route that yields the opposite-sign comparator would retire this
  wall without a new axiom. That route remains available.
- **N7 - steelman.** A hostile reviewer can argue that the tested grids are not
  the deep continuum regime and that a different local improvement or Regge
  route could produce the Einstein/Lichnerowicz operator. This is valid
  against broad closure and is why the claim is finite-BZ and scheme-scoped.
- **N8 - cross-cycle echo.** Prior GR notes already separate matter-induced
  positivity from supplied geometric comparator structure. This note sharpens
  only the matter-`W` side and does not close the geometric side.

**Gate status:** PASS for the narrowed finite-BZ native one-loop `W` negative;
FAIL for any reading as a framework-wide no-go for GR emergence.

## Load-Bearing Inputs

- [`UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_INDUCED_GRAVITON_W_NATIVE_FINITE_K_BOUNDED_THEOREM_NOTE_2026-06-08.md) - finite-`k` yz diagnostic and named-open list.
- [`UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md) - conserved vertex plus seagull scheme.
- [`UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_DEGENERATE_SUPERMETRIC_GRAVITON_SIGN_NO_GO_BOUNDED_THEOREM_NOTE_2026-06-08.md) - supplied comparator tested here.
- [`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md`](UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md) - `k=0` scalar-kernel anchor.
- [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) - units remark only.

## Forbidden-Imports Check

No PDG, fitted, or literature value is consumed. Every number is computed from
the declared lattice objects in the runner. Sakharov induced gravity,
Adler-Zee, and Callan-Coleman-Jackiw improvement are context/comparators only;
no formula or value from them enters any check.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane is the only status
authority.
