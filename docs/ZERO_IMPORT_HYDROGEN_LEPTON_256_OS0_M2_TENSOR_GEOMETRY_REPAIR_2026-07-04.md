# Zero-Import Hydrogen: Lepton `1/256` OS0 `M_2(C)^tensor4` Geometry Repair

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** meta / primitive-backed route refinement
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_os0_m2_tensor_geometry_repair.py`

## Scope

This note attacks Route A from
`ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md`: the
`M_2(C)^tensor4` reading of the charged-lepton suppression candidate

```text
S_l = 1 / dim_C(M_2(C)^tensor4) = 1/256.
```

The earlier `LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md` correctly
flagged the exponent `4` as unforced on the then-current surface. Since then,
the approved `kinetic_isotropy_primitive` has registered the OS0 kinetic-form
surface:

```text
Z^3 x Z_tau, c_t = c_s, one tick grained on the same footing as one edge.
```

That primitive changes the geometry accounting but not the charged-lepton
mass claim. It can source the **four regulator slots** for a bookkeeping
`M_2(C)^tensor4` count. It does not source the lepton-sector tensor lift,
the reciprocal readout, a mass value, a selector, or the empirical `256.08`
correction.

## Positive Narrow Repair

The finite algebra is exact:

```text
dim_C(M_2(C)) = 4
dim_C(M_2(C)^tensor4) = 4^4 = 256
1 / dim_C(M_2(C)^tensor4) = 1/256.
```

The geometry-only exponent question can now be split:

| sub-question | current answer |
|---|---|
| Why four regulator slots instead of three spatial slots? | The registered kinetic-isotropy primitive supplies the OS0 `Z^3 x Z_tau` regulator form. |
| Does the charged-lepton scalar block carry one `M_2(C)` factor per OS0 slot? | Not derived here. |
| Does reciprocal dimension become the charged-lepton suppression `S_l`? | Not derived here. |
| Does exact `256` explain the empirical `256.08` divisor? | Not derived here. |

So the route is no longer blocked at the vague phrase "where does the fourth
direction come from?" It is blocked at the sharper lepton-sector tensor-lift
and reciprocal-readout claims.

## Counterfactuals

Spatial-only counting gives the wrong bookkeeping value:

```text
dim_C(M_2(C)^tensor3) = 4^3 = 64.
```

The OS0 primitive is exactly the difference between a spatial-only count and
the four-slot regulator count:

```text
4^4 / 4^3 = 4.
```

This is not a mass prediction. It only says the geometry slot count is no
longer an unregistered assumption if the route is explicitly scoped to the
OS0 regulator surface.

## Residuals After The Repair

The `M_2(C)^tensor4` route now has three explicit residuals:

| wall | residual |
|---|---|
| A1 | Tensor lift: prove the charged-lepton scalar block carries one `M_2(C)` factor per OS0 regulator slot. |
| A2 | Reciprocal readout: prove `1/dim_C(M_2(C)^tensor4)` is the charged-lepton scale suppression `S_l`. |
| A3 | Precision correction: account for the empirical divisor `256.08` versus exact `256`. |

The older geometry wall is demoted to an approved primitive dependency:
`kinetic_isotropy_primitive` supplies the OS0 four-slot regulator form and
chain-satisfies that premise without making downstream claims
`retained_bounded`.

**Follow-up A2 firewall:**
`ZERO_IMPORT_HYDROGEN_LEPTON_256_RECIPROCAL_READOUT_FIREWALL_2026-07-04.md`
separates the finite count from the physical readout rule. The same
`N = 4^4 = 256` permits `1/sqrt(N) = 1/16` as a unit-amplitude
normalization and `1/N = 1/256` as a density/volume reciprocal; the latter is
the target but still requires a charged-lepton readout theorem.

**Follow-up A1 firewall:**
`ZERO_IMPORT_HYDROGEN_LEPTON_256_TENSOR_LIFT_FIREWALL_2026-07-04.md`
separates OS0 slot geometry from the charged-lepton carrier theorem. D17-prime
supplies the scalar singlet and `1/sqrt(2)` block normalization; the OS0 count
supplies `M_2(C)^tensor4` as regulator bookkeeping. Current retained surfaces
do not yet prove that the charged-lepton scalar coefficient carries one
`M_2(C)` factor per OS0 slot.

**Follow-up A3 firewall:**
`ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md`
quantifies the exact-`256` versus `256.082435...` residual. Even after the
geometry, tensor-lift, and reciprocal-readout questions close, exact `256`
still needs a precision correction or direct noninteger-divisor theorem.

## No-Go Discipline Gate

This section prevents overclaiming the repair. The broad claim "the
`M_2(C)^tensor4` route is now closed" is **not** shipped. The narrow claim is:
the OS0 primitive repairs the geometry-slot premise only; A1-A3 remain open.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| spatial-only `M_2(C)^tensor3` | Use only the `Z^3` spatial lattice slots. | ATTEMPTED. Gives `4^3 = 64`, not `256`. |
| OS0 `M_2(C)^tensor4` | Use the approved `Z^3 x Z_tau` regulator form. | PARTIAL POSITIVE. Gives the right finite count `4^4 = 256`, but not the lepton tensor lift or readout. |
| naive Euclidean taste `16^2` | Read `256 = 16^2` from naive 4D tastes. | RULED OUT AS PHYSICAL SELECTOR by the regulator-dependence boundary in the lepton structural probe; useful only as bookkeeping. |
| base-self exponent `4^4` | Say number of tensor copies equals `dim_C M_2 = 4`. | ATTEMPTED. Same arithmetic, but without OS0 it is a slogan; with OS0 it becomes geometry slots, not a selector. |
| Schur `/64` route | Use `g_2^2|_lattice/64 = 1/256`. | OPEN parallel route; addressed by the two-scale firewall, not this exponent repair. |
| empirical `m_W/256` | Use the observed relation directly. | RULED OUT AS ZERO-IMPORT ROUTE: comparator/open gate, not derivation. |

### N2 - Wall-independence audit

| pair | closes automatically? | conclusion |
|---|---|---|
| A1 <-> A2 | no in either direction | independent |
| A1 <-> A3 | no in either direction | independent |
| A2 <-> A3 | no in either direction | independent |

OS0 slot geometry does not close any of A1-A3 by itself.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `OS0` / `Z^3 x Z_tau` | approved primitive content from `kinetic_isotropy_primitive`; geometry only. |
| `tensor4` | finite bookkeeping count; lepton-sector lift is explicit A1. |
| `reciprocal` | explicit readout wall A2. |
| `primitive` | registry checked; primitive supplies no selector, weighting, mass value, or empirical match. |

No hidden admission is left as background.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` | OS0 kinetic-form graining `c_t = c_s`, `Z^3 x Z_tau` | yes for geometry slots only |
| `M2_TENSOR_D4_DIMENSION_256_BOUNDED_NOTE_2026-05-26.md` | finite algebra `4^4 = 256` with `d=4` input | yes, now with geometry source separated |
| `LEPTON_YUKAWA_256_STRUCTURAL_PROBE_2026-06-05.md` | charged-lepton `1/256` base/exponent/precision status | yes for target, but superseded only on geometry sub-wall |
| `p2_euclidean_vs_lorentzian_fork_2026_06_05.py` | Euclidean-regulator versus native real-time magnitude branch | partial: warns not to call regulator count physical by itself |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_ROUTE_TRIAGE_2026-07-04.md` | route-level target selection | yes |

No cited surface is counted as a charged-lepton mass closure.

### N5 - Rhetoric audit

The note avoids the broad phrase "`d=4` is derived" and uses the narrower
phrase "OS0 four regulator slots are approved primitive content." Tested
resolutions:

| resolution | tested? | outcome |
|---|---|---|
| finite vector-space count | yes | `dim_C(M_2(C)^tensor4) = 256`. |
| geometry slot source | yes | primitive grants `Z^3 x Z_tau`, `c_t = c_s`. |
| charged-lepton tensor lift | no closure | named A1. |
| reciprocal physical readout | no closure | named A2. |
| precision correction | no closure | named A3. |

### N6 - Partial-closure path scan

The primitive registry was checked. `kinetic_isotropy_primitive` is an approved
premise node and may chain-satisfy the OS0 geometry-slot premise. The same
registry explicitly says approved primitives do not supply selectors,
weighting rules, normalization rules, mass values, or empirical matches. Those
remain A1-A3.

### N7 - Steelman

A hostile reviewer can argue that once the framework accepts OS0 `Z^3 x Z_tau`,
the `M_2(C)^tensor4` expression is no longer a fit: the one-site algebra
`M_2(C)` tensored over the four regulator slots gives `256`, and the lepton
suppression is exactly the reciprocal. That is the strongest positive reading.
The rebuttal is scope: OS0 grants the four slots, not the instruction to tensor
the charged-lepton scalar block over those slots, and not the reciprocal
readout as a Yukawa suppression. Those are A1 and A2.

### N8 - Cross-cycle echo

This mirrors the kinetic-isotropy campaign itself: a previously hidden
time/space graining premise became an approved primitive, while downstream
dynamics and selectors remained separate theorem work. This note applies the
same split to `M_2(C)^tensor4`: geometry slot count improves; physical
charged-lepton closure remains open.

**Gate result:** broad closure fails; narrowed geometry repair passes.

## Explicit Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation that the charged-lepton scalar block carries
  `M_2(C)^tensor4`.
- No derivation that reciprocal dimension is a Yukawa suppression.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_os0_m2_tensor_geometry_repair.py
```

The verifier checks the finite dimension arithmetic, the OS0 primitive
boundary, the residual split, the no-go discipline section, and the explicit
non-claims.
