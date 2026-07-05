# Zero-Import Hydrogen: Lepton `1/256` A3 Correction-Placement Discriminator

**Date:** 2026-07-04
**Type:** partial-narrowing discriminator note
**Claim type:** meta / precision-boundary support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `C_A3`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_a3_correction_placement_discriminator.py`

## Scope

The source-chain lane has now conditionally narrowed exact `S_l` to a
source-readout convention:

```text
y_scale = g_2 * (1/sqrt(2)) * S_l
S_l     = sigma([j])_c
sigma([j])_c = 1/256
```

That is still not a retained charged-lepton scale, because the physical
comparator is not exact `256`. The A3 firewall quantified the residual:

```text
N_A3   = 256.08243522600384
C_A3   = 256 / N_A3 = 0.9996780910571587
1/N_A3 = C_A3 * (1/256) = 0.003904992543192026
```

This note adds one discriminator: a future A3 theorem must say where that
small correction lives. Multiplying an end product by `C_A3` is not a
zero-import derivation unless the placement is licensed.

## Placement Algebra

Let

```text
F_0 = g_2 * (1/sqrt(2))
S_0 = 1/256
R_0 = any already-derived Koide/electron readout factor
```

The same numerical product can be written in multiple ways:

```text
(C_A3 F_0) * S_0       * R_0
F_0        * (C_A3 S_0) * R_0
F_0        * S_0       * (C_A3 R_0)
F_0        * (1/N_A3)  * R_0
```

Those are product-equivalent, but not dependency-equivalent. They assign the
missing theorem to different lanes.

## Placement Classes

| placement | theorem shape | hydrogen consequence |
|---|---|---|
| P1 source-readout correction | Derive `S_l = C_A3 * sigma([j])_c = 1/N_A3`, or derive a nonuniform source ray whose singleton L1 section is `1/N_A3`. | Changes the W6 source-readout convention or the A2 source-ray theorem. Exact `1/256` remains a bare scaffold, not the physical source readout. |
| P2 front-factor/threshold correction | Derive `F_phys = C_A3 * g_2 * (1/sqrt(2))` at the relevant charged-lepton comparator scale. | Leaves `S_l = 1/256` intact, but requires retained weak/lepton scale-running or threshold matching. |
| P3 Koide/electron-readout correction | Show the apparent `a_l^2` offset belongs to the Koide species, phase, pole-mass, or electron-branch readout rather than to `S_l`. | Keeps the scale source chain separate from K1-K3. It cannot be spent until the electron-readout firewall is retired. |
| P4 direct noninteger divisor | Derive `N_A3 = 256.082435...` directly from a retained determinant, volume, trace, or source-geometry theorem. | Replaces the exact finite-coordinate target with a physical noninteger divisor theorem and must explain why the uniform 256-coordinate source is only an approximation or intermediate object. |
| P5 empirical splice | Use observed `m_W`, observed charged-lepton masses, or fitted `a_l` to set the correction. | Not a zero-import lane. It is allowed as comparator bookkeeping only. |

The placement label matters because the algebra alone cannot distinguish P1
from P2 or P3. A future source theorem that only proves exact `1/256` cannot
also silently claim the empirical `256.082435...` precision. A future
threshold theorem cannot be counted as a source-measure theorem. A future
Koide/readout theorem cannot be counted as an A2 source-ray theorem.

The P2 weak-front follow-up
`ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P2_WEAK_FRONT_THRESHOLD_TARGET_DISCRIMINATOR_2026-07-04.md`
turns the front-factor/threshold branch into an auditable target: P2 requires
`F_phys = C_A3 * g_2 * (1/sqrt(2))`, equivalently a one-loop SU(2) bookkeeping
log `ell_A3 ~= 0.03768480771` at `b_2 = 19/6`, plus an explicit
charged-lepton front/matching theorem and no comparator proof input. It does
not derive that theorem.

The P1 source-readout correction current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P1_SOURCE_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records the source-side boundary for this placement class: current surfaces do
not supply `P1_SOURCE_READOUT_CORRECTION_RETAINED`, and the missing input is
`CORRECTED_SOURCE_READOUT_THEOREM_RETAINED`.

The P3 Koide/electron-readout correction current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P3_KOIDE_ELECTRON_READOUT_CORRECTION_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records the readout-side boundary for this placement class. OPEN. Current
Koide/electron surfaces do not supply
`P3_KOIDE_ELECTRON_READOUT_CORRECTION_RETAINED`, and the missing input is
`KOIDE_ELECTRON_A3_CORRECTION_THEOREM_RETAINED`.

The P4 direct noninteger-divisor current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_A3_P4_DIRECT_NONINTEGER_DIVISOR_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records the direct-divisor boundary for this placement class. OPEN. Current
direct-divisor surfaces do not supply
`P4_DIRECT_NONINTEGER_DIVISOR_RETAINED`, and the missing input is
`DIRECT_NONINTEGER_DIVISOR_THEOREM_RETAINED`.

## Relation To The Current Source Chain

The current A2 chain conditionally supports the exact source statement:

```text
source-family naturality
  -> uniform projective tensor-frame source ray
  -> sigma([j])_c = 1/256
  -> S_l = sigma([j])_c, if the source-readout convention is licensed
```

That chain is a strong scaffold for P1, but it does not by itself select
`C_A3`. To close P1, one of the following must be supplied:

1. a physical license that the charged-lepton source readout is not the exact
   singleton L1 section but the corrected section `C_A3 sigma([j])_c`;
2. a retained nonuniform source-ray theorem whose singleton section is
   `1/N_A3`;
3. a retained argument that the apparent correction is not source-side at all,
   routing A3 to P2, P3, or P4.

## Open PR Alignment

Open PRs were checked on 2026-07-04, including the Koide-search surface. They
move nearby science but do not identify the A3 placement:

| PR | current effect on A3 placement |
|---|---|
| `#5011` eta twisted walk family runner | `CLEAN` at latest refresh; runner stabilization, no A3 placement theorem. |
| `#4893` occupancy locked-record bridge | Bounded occupancy narrowing; it sharpens K1-style Koide occupancy bookkeeping but does not place `C_A3`. |
| `#4898` theta mass-side composition | Shares the occupancy bridge on theta mass-side context; no charged-lepton precision placement. |
| `#4902` occupancy individuation | Factors the occupancy bridge and leaves conjugate-sector phase registrability decisive; this keeps Koide/readout P3 open. |
| `#4905` slot-freedom classification | Leaves slot weighting under hypothetical conjugation reading as an open gate; no A3 source or threshold correction. |
| `#4906` phase registrability | Reports doublet-grade phase registrability no-go at enumerated-inventory grade while leaving defeat routes open; it sharpens P3 but does not place `C_A3`. |
| `#4938` K/CPT orbit-constancy supplied-context bridge | Merged into `main` at 2026-07-04T15:14:57Z; useful determinant-character/K-CPT hygiene, no A3 correction placement. |
| `#4940` rule achirality from minimality | Currently `CLEAN`; theta/admissibility licensing context, no `m_e`, `S_l`, `C_A3`, `alpha(0)`, or hydrogen closure. |
| `#4943` stale-green runner-cache repair sweep | Currently `DIRTY`; runner/cache hygiene and honest-red diagnostics, not a physics placement theorem. |
| `#4947` R-eta K-breaking transport no-go | Currently `CLEAN`; prunes minimal positive K-breaking / inhomogeneous C3 transport toward `Phi = Tr L_3^+ = 2/3`, but leaves R-eta and `AC_phi_lambda` live and does not derive `C_A3`. |
| `#4948` theta G1 exact-branch no-go | Currently `CLEAN` after earlier moving labels. It prunes the global exact-branch shortcut `n=dA` for theta G1 while leaving closed-nonexact sector, dynamical defect suppression, nonabelian registration, phase insertion, and mass-side determinant blockers open. It does not derive `C_A3`. |
| `#4949` theta closed-nonexact sector-record no-go | Currently `UNSTABLE` after earlier moving labels. It prunes the closed non-exact carrier witness to physical sector record/readout shortcut and does not derive `C_A3`. |
| `#4950` additive-even premise relocation onto K/CPT bridge | Currently `UNSTABLE`. It repairs a theta-chain premise edge and runner/cache surface without theorem-content changes; it does not place or derive `C_A3`. |

Thus the live A3 decision remains inside this packet: source-readout
correction, front-factor/threshold correction, Koide/electron-readout
correction, direct noninteger divisor, or empirical splice.

## Primitive Boundary

The primitive registry was checked. `scale_reference_primitive` supplies a
units conversion only; `kinetic_isotropy_primitive` supplies OS0 kinetic-form
isotropy only; `realized_state_primitive` supplies pointwise evaluation only.
None of these approved primitives supplies a mass ratio, correction factor,
readout bridge, normalization rule, weighting rule, state content, source
selector, or empirical match. They chain-satisfy their registered roles but do
not license any A3 placement.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the A3 correction cannot
be derived" is **not** shipped. The narrowed claim is: a zero-import A3
closure must declare and license its correction placement; the current packet
does not yet derive `C_A3` in any placement class.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| P1 source-readout correction | Put `C_A3` into `S_l = C_A3 sigma([j])_c`. | OPEN. The source chain currently supports exact `sigma([j])_c = 1/256` conditionally, but not the corrected source readout. |
| P2 front-factor/threshold correction | Put `C_A3` into `g_2 * (1/sqrt(2))` through running or threshold matching. | OPEN. Numerically plausible as a correction class, but no retained charged-lepton threshold theorem is supplied here. |
| P3 Koide/electron-readout correction | Put the offset into phase/species/pole-mass readout instead of source scale. | OPEN. The Koide PR stack sharpens K1-K3 but keeps electron readout open on current main. |
| P4 direct noninteger divisor | Derive `N_A3 = 256.082435...` directly. | OPEN. This would close A3, but must avoid observed `m_W`, observed lepton masses, or fitted `a_l` as proof inputs. |
| P5 empirical splice | Fit the correction from observed `m_W/a_l^2`. | RULED OUT AS ZERO-IMPORT ROUTE. It remains comparator bookkeeping only. |
| exact-only route | Treat exact `1/256` as the final physical precision. | ATTEMPTED BY PRIOR FIREWALL. It leaves the `0.032%` comparator offset unexplained. |

### N2 - Wall-independence audit

| pair | closes automatically? | conclusion |
|---|---|---|
| P1 source readout <-> P2 threshold/front factor | no in either direction | independent |
| P1 source readout <-> P3 Koide/electron readout | no in either direction | independent |
| P1 source readout <-> P4 direct divisor | P4 can bypass P1; P1 does not imply P4 | not double-counted |
| P2 threshold/front factor <-> P3 Koide/electron readout | no in either direction | independent |
| P2 threshold/front factor <-> P4 direct divisor | no in either direction | independent |
| P3 Koide/electron readout <-> P4 direct divisor | no in either direction | independent |

The collapsed wall is not "derive four corrections." It is "derive one
licensed placement, or prove that two placements compose without double
counting."

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `placement` / `correction` | explicit A3 target, not background. |
| `source-readout convention` | explicit W6 dependency; not assumed. |
| `threshold` / `running` | possible P2 route; not established premise. |
| `Koide` / `electron readout` | separate P3 route; not used to close A3. |
| `primitive` / `registered` | registry checked; approved primitives do not supply A3 placement. |
| `empirical` / `observed` | comparator role only; forbidden as zero-import proof input. |

No placement theorem is left hidden as "natural" or "standard" background.

### N4 - Residual matching

| cited surface | residual it attacks | match? |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_PRECISION_CORRECTION_FIREWALL_2026-07-04.md` | magnitude of the `256.082435...` versus exact `256` residual | yes |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md` | W6 identity between `S_l` and normalized source strength | partial: source identity only, not `C_A3` |
| `ZERO_IMPORT_HYDROGEN_KOIDE_ELECTRON_READOUT_FIREWALL_2026-07-04.md` | K1-K3 electron readout residuals | partial: P3 route only |
| `#4893`, `#4902`, `#4905`, `#4906` Koide/occupancy PRs | occupancy, slot, and phase registrability surfaces | partial: P3 route only |
| `#4947` R-eta K-breaking transport no-go | R-eta physical readout license route pruning | no: adjacent AC/Koide hygiene, not A3 placement |
| `axiom_premise_nodes.json` and primitive notes | approved primitive boundary | guard only |

No source-chain citation is counted as a precision-correction theorem.

### N5 - Rhetoric audit

The note avoids saying "`C_A3` is not derivable" or "no placement exists."
Tested resolutions:

| resolution | tested? | outcome |
|---|---|---|
| product algebra | yes | source, front-factor, and readout placements are numerically degenerate. |
| exact source scaffold | yes | conditional source chain gives exact `1/256`, not the physical correction. |
| empirical precision magnitude | yes | `C_A3 = 0.999678091...`. |
| all future running, threshold, determinant, or readout theorems | no | left open as placement routes. |

### N6 - Partial-closure path scan

Legitimate import-retirement paths remain:

| path | what it could close |
|---|---|
| ratify corrected source-readout semantics | P1 |
| derive charged-lepton weak/lepton threshold matching | P2 |
| retire Koide phase/species/pole readout gates | P3 |
| derive a retained noninteger divisor theorem | P4 |
| prove two placements compose with an independently derived product law | combined placement without double counting |

These are closure paths, not automatic new axioms. The discriminator exists
to keep them separate until one is actually supplied.

### N7 - Steelman

A hostile reviewer can argue that this discriminator is over-cautious: once
exact `1/256` is derived, a `0.032%` pole-scale correction is precisely what
ordinary threshold matching should do, so forcing the source theorem to solve
it is unnecessary. That steelman is strong. The response is that the note does
not force source-side placement; it explicitly leaves P2 open. It only forbids
using an unlabeled fitted multiplier as if placement had been derived.

### N8 - Cross-cycle echo

This mirrors prior framework lanes where a clean structural integer or
topological value arrived before the physical readout, scale, or pole
correction. The disciplined move is to preserve the structural scaffold while
keeping the final readout correction in a named lane. Convention or
ratification paths may retire such walls, but only after the placement is
visible enough for audit.

**Gate result:** broad no-go fails; narrowed correction-placement
discriminator passes.

## Explicit Non-Claims

- No derivation of `C_A3 = 0.999678091...`.
- No derivation of `N_A3 = 256.082435...`.
- No derivation of corrected `S_l = 1/N_A3`.
- No derivation of a weak/lepton threshold correction.
- No derivation of a Koide/electron readout correction.
- No derivation of a direct noninteger divisor theorem.
- No use of observed charged-lepton masses or `m_W` as proof inputs.
- No derivation of `m_e`, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_a3_correction_placement_discriminator.py
```

The verifier checks the A3 correction arithmetic, placement product
degeneracy, primitive boundary, open-PR alignment, no-go discipline section,
and explicit non-claims.
