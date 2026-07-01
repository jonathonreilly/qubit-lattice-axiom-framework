# Theta-Bar Assembly Interface Bridge

**Date:** 2026-07-01
**Claim type:** bounded theorem / operational assembly interface.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, or claim
Strong-CP closure.
**Primary runner:**
[`scripts/theta_bar_assembly_interface_bridge_2026_07_01.py`](../scripts/theta_bar_assembly_interface_bridge_2026_07_01.py)

## Claim

The latest theta stack has separated three jobs:

1. gauge-side sector selection;
2. mass-side determinant/orientation readout;
3. anomaly-invariant assembly.

This bridge supplies the finite assembly interface for job 3.

If:

- an emergent sharp integer `Q` sector context with odd support is supplied;
- Record/Born supplies pointwise nonnegative sector weights for that sharp
  context;
- the theta pointwise selector is used, so the gauge-side member of `{0, pi}`
  is `theta_gauge = 0`;
- the physical mass-side action-level datum reduces to a supplied determinant
  channel whose Record-registrable phase content is zero, with the physical
  orientation bit selected to the zero branch;
- anomaly bookkeeping pairs axial shifts as

```text
theta_gauge -> theta_gauge - n alpha
arg det M   -> arg det M   + n alpha,
```

then the invariant angle

```text
theta_bar = theta_gauge + arg det M     (mod 2 pi)
```

is exactly zero.

The finite algebra is not the remaining wall. What remains is the physical
derivation or approval of the supplied surfaces:

```text
W_theta_Q_context:
  emergent sharp integer Q with odd support and a pointwise record-facing
  sector measure.

W_mass_determinant_action:
  physical quark-sector action-level determinant-entry bridge, including
  W2/registrability, determinant-channel scope, orientation branch, and
  quark-sector transport.

W_anomaly_covariant_assembly:
  anomaly bookkeeping tying the gauge and mass shifts on the same physical
  quark/gauge surface.
```

This bridge does not derive those walls. It proves that once they are supplied
in the stated form, theta-bar assembly has no additional finite arithmetic
freedom.

## Source Surface

This bridge consumes current source surfaces only in their declared scope:

- the theta sector Born-measure bridge supplies pointwise sector weights once a
  sharp `Q` record context is supplied;
- the theta pointwise selector chooses `theta_gauge = 0` from `{0, pi}` under
  pointwise nonnegative sector weights and nonzero odd-sector support;
- the determinant-readout bridge erases mass determinant phase only inside a
  supplied Record-registrable determinant channel;
- the theta P2 determinant-readout exhaustion bridge keeps the W2 physical
  registrability and action-level determinant-entry premises explicit;
- the structured theta-bar admission identifies the invariant combination
  `theta_gauge + arg det M` and keeps the joint gauge/mass basis bridge open.

## Finite Theorem

Write all angles in units of `pi`, so equality is modulo `2`. Let

```text
theta_bar = theta_gauge + phi_mass  (mod 2),
```

where `phi_mass = arg det M / pi`.

For any flavor count `n` and axial parameter `alpha`, the paired anomaly shift

```text
theta_gauge' = theta_gauge - n alpha
phi_mass'    = phi_mass    + n alpha
```

leaves the sum invariant:

```text
theta_bar' = theta_bar  (mod 2).
```

Therefore only the paired gauge-plus-mass sum is the assembly target. Gauge
or mass values alone are not the invariant Strong-CP angle.

Under the supplied gauge selector,

```text
theta_gauge = 0.
```

Under the supplied mass determinant-channel readout with zero orientation
branch,

```text
phi_mass = 0.
```

Therefore

```text
theta_bar = 0 + 0 = 0  (mod 2).
```

The contrast cases are exact:

```text
theta_gauge = pi, phi_mass = 0  -> theta_bar = pi;
theta_gauge = 0,  phi_mass = pi -> theta_bar = pi.
```

So the gauge-side `0` selector and the mass-side zero-orientation branch are
both load-bearing if the target is `theta_bar = 0`.

## Explicit Finite Witness

Let the sharp sector weights be

```text
Z_-1 = 1/8,  Z_0 = 3/4,  Z_1 = 1/8.
```

They are pointwise nonnegative, conjugation-paired, normalized, and have odd
support. The pointwise selector rejects `theta = pi` because odd sectors would
receive negative weights:

```text
W_pi(1) = -1/8.
```

It therefore selects

```text
theta_gauge = 0.
```

For the mass side, a supplied determinant-channel readout whose phase character
is K/CPT-orbit constant has only the zero phase character in the registrable
channel. On the zero orientation branch this gives

```text
phi_mass = 0.
```

With three flavors and axial shift `alpha = 1/7`, the transformed values are

```text
theta_gauge' = -3/7,
phi_mass'    =  3/7,
theta_bar'   =  0.
```

The invariant sum is unchanged. This is the assembly algebra this bridge
packages.

## What Moves

| Prior residual | Effect of this bridge |
|---|---|
| theta-bar assembly as a broad phrase | narrowed to finite anomaly-invariant addition plus three physical surface suppliers |
| gauge-side 0-vs-pi selector | consumed conditionally from the pointwise sector-weight bridge |
| mass determinant phase | consumed only on a supplied Record-registrable determinant/action-entry channel |
| anomaly bookkeeping | stated as the paired shift relation needed for invariance |
| extra theta-bar arithmetic | closed: no additional finite arithmetic remains once the surfaces are supplied |

## What Remains

The remaining Strong-CP/theta wall is not the modular sum. It is physical
surface supply:

```text
W_theta_Q_context
W_mass_determinant_action
W_anomaly_covariant_assembly
```

The first wall is gauge-side: derive or supply sharp `Q`, odd support, and the
record-facing pointwise sector measure.

The second wall is mass/action-side: derive or supply the physical quark-sector
determinant-entry theorem, W2/registrability, determinant-channel scope,
zero-orientation branch, and quark-sector transport.

The third wall is joint: derive or supply the anomaly-covariant assembly that
places the gauge and mass shifts on the same physical quark/gauge surface.

## Audit Consequence If Retained

Rows that need `theta_bar = 0` should cite the stack as:

```text
sharp Q record context with odd support
  + Record/Born pointwise sector measure
  + theta pointwise sector selector
  + physical mass determinant/action-entry bridge with zero orientation branch
  + anomaly-covariant gauge/mass assembly
  -> theta_bar = 0.
```

Rows that have only total partition positivity, substrate no-carrier results,
mass determinant K-reality, or determinant-channel algebra must not cite this
bridge as Strong-CP closure. They still need the missing physical surfaces.

## Non-Claims

This note does not claim:

- Strong-CP closure or Tier-A retirement;
- derivation of emergent `Q`, odd-sector support, or pointwise sector measure;
- derivation of the physical gauge action or scaling-limit sector surface;
- derivation of W2 physical registrability or action-level determinant entry;
- derivation of the physical quark-sector determinant or zero orientation
  branch;
- derivation of anomaly-covariant gauge/mass assembly;
- exclusion of sign-problem formulations outside the record-facing
  probability-measure surface;
- use of PDG values, fitted constants, lattice-MC values, beta=6 values, or a
  new primitive.

## Minimum Foundation Update If Bridge Work Fails

No ontology axiom update follows from this bridge. If bridge-first routes fail,
the minimum foundation update would be narrower than a generic theta axiom.
It would need to register the physical theta-sector surfaces explicitly, for
example:

```text
P_theta_sector_surface:
  On a supplied physical gauge/quark action surface, a sharp integer Q sector
  record context, pointwise sector measure, mass determinant-entry map, and
  anomaly-covariant assembly relation are selected.
```

This note does not request or register that primitive. It records the minimum
operational shape that would be needed if derivations fail.

## No-Go Discipline Gate

**Status:** PASS for bounded wall localization inside a positive assembly
bridge. This is not a terminal no-go. It proves only the finite assembly step
after the named suppliers are present.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Gauge pointwise selector route | Use sharp `Q` plus pointwise nonnegative sector weights to choose `theta_gauge = 0`. | CONSUMED CONDITIONALLY: supplied by the theta sector/Born and pointwise selector bridges after `Q` and odd support are supplied. |
| Partition-positivity route | Use total positivity to choose `theta_gauge = 0`. | RULED OUT BY PRIOR: positive total partition sums can coexist with negative odd-sector point weights. |
| Mass determinant channel route | Use Record-registrable determinant readout to erase mass phase. | CONSUMED CONDITIONALLY: only inside the supplied determinant/action-entry channel. |
| Mass K-reality route | Use K-real determinant reality alone to set the invariant angle. | PARTIAL BY PRIOR: K-reality gives a mass-side discrete branch, not the full gauge/mass invariant angle. |
| Axial anomaly bookkeeping route | Assemble gauge and mass phases by paired shifts. | ATTEMPTED here: exact finite invariance, but the physical joint surface remains supplied. |
| Holomorphic/quark-sector route | Derive the physical quark-sector determinant and orientation branch from generation/chiral structure. | OPEN: possible downstream bridge, not supplied by this note. |
| New primitive route | Register theta-sector surface selection as an approved operational primitive. | OWNER-GOVERNANCE ROUTE: available only if bridge-first routes fail or are intentionally bypassed. |

### N2 - Wall-Independence Audit

The collapsed residuals are:

```text
W_theta_Q_context
W_mass_determinant_action
W_anomaly_covariant_assembly
```

Closing `W_theta_Q_context` selects the gauge member, but not the physical
mass determinant-entry map or joint anomaly assembly. Closing
`W_mass_determinant_action` supplies the mass side, but not the emergent gauge
sector or pointwise sector measure. Closing `W_anomaly_covariant_assembly`
supplies the invariant bookkeeping, but not either side's physical value.

### N3 - Hidden-Wall Scan

Terms used load-bearingly are classified as follows:

| Term | Classification |
|---|---|
| `sharp Q context` | Explicit bridge input from the theta sector lane, not derived here. |
| `pointwise sector measure` | Explicit bridge input supplied by Record/Born only after sharp `Q` interface. |
| `zero orientation branch` | Explicit mass-side physical branch input, not derived here. |
| `determinant-entry map` | Explicit action-level bridge input; the P2 note keeps it supplied. |
| `anomaly bookkeeping` | Explicit paired-shift relation tested finitely; physical joint surface remains a wall. |
| `physical quark-sector` | Future bridge target, not a premise supplied by this note. |

No hidden admission is promoted into a fourth independent wall.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `THETA_SECTOR_BORN_MEASURE_BRIDGE_2026-07-01` | sharp `Q` context and theta_bar remain open | `W_theta_Q_context` and assembly wall | yes |
| `THETA_POINTWISE_SECTOR_WEIGHT_SELECTOR_2026-07-01` | needs emergent `Q`, odd support, pointwise sector measure, theta_bar assembly | same gauge-side selector inputs | yes |
| `THETA_P2_DETERMINANT_READOUT_EXHAUSTION...` | W2 physical registrability and action-level determinant entry are supplied, not derived | `W_mass_determinant_action` | yes |
| `STRONG_CP_DETERMINANT_READOUT_BRIDGE...` | mass determinant-channel erasure is conditional on supplied channel | mass determinant subclaim | yes |
| `STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION...` | joint gauge/mass basis bridge remains open | `W_anomaly_covariant_assembly` | yes |
| `STRONG_CP_JOINT_BRIDGE_FAILS_HOLOMORPHIC_RESIDUAL...` | tested joint-basis route does not force theta_bar | preserves holomorphic/quark-sector route as open | yes |

### N5 - Rhetoric Audit

The negative boundary is scoped to this sentence:

```text
The assembly bridge does not derive the physical gauge sector, mass determinant
action-entry map, or anomaly-covariant joint surface.
```

It is tested at finite sector-weight, determinant-character, and modular-angle
bookkeeping resolution. It is not a claim that no future quark-sector,
holomorphic, anomaly, gauge-action, or measurement theorem can derive those
surfaces.

### N6 - Partial-Closure Path Scan

Live closure paths remain:

- derive sharp `Q`, odd support, and pointwise sector measure from the
  gauge-action/scaling bridge;
- derive W2 physical registrability and action-level determinant entry from a
  mass/quark action theorem;
- derive the zero orientation branch from quark-sector K-reality plus transport;
- derive anomaly-covariant assembly from a same-surface gauge/quark theorem;
- explicitly approve and register a theta-sector operational primitive if
  owner governance chooses that route after bridge-first work.

The primitive-registry check confirms that current approved primitives do not
already grant these theta-sector surfaces.

### N7 - Steelman

A hostile reviewer can argue that this bridge is mostly bookkeeping: once the
gauge sector, mass determinant channel, zero orientation branch, and anomaly
bookkeeping are supplied, `theta_bar = 0` is immediate. That objection is
accepted. The value of this bridge is audit hygiene: it prevents future rows
from treating substrate no-carrier, determinant K-reality, or gauge-side
pointwise positivity as Strong-CP closure until the missing physical surfaces
are explicitly supplied.

### N8 - Cross-Cycle Echo

Prior theta cycles overclaimed by turning reality, positivity, substrate
vacuity, or determinant reality into `theta_bar = 0`. This bridge keeps those
layers separate. It packages only the finite modular sum and paired-shift
invariance, while preserving the gauge `Q`, mass determinant action, and
joint anomaly surface as live bridge targets.

## Verification

Run:

```bash
python3 scripts/theta_bar_assembly_interface_bridge_2026_07_01.py
```

Expected close:

```text
TOTAL: PASS=130 FAIL=0
```
