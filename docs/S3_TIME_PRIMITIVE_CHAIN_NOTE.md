# Primitive Chain Readout and Time-Coupling Update

**Type:** open_gate
**Date:** 2026-04-19
**Primary runner:** [`scripts/frontier_s3_time_primitive_chain_reaudit.py`](../scripts/frontier_s3_time_primitive_chain_reaudit.py)
**Purpose:** restate the remaining Route-2 primitives after the exact bilinear
carrier, the readout/time-coupling theorem block, and the upstream
E-channel readout naturality no-go.

## 2026-05-28 Repair Boundary

Earlier review found that the full positive theorem still does not close because
the readout map `P_R`, specifically `beta_E / alpha_E = 21/4`, is explicitly left
open. The narrow repair target is therefore either to derive
`beta_E / alpha_E = 21/4` from the restricted primitive-chain objects or to prove
an admissibility boundary showing why the current restricted class cannot select
it uniquely. This revision takes the **split path**:

- **Load-bearing (in scope):** The algebraic reduction that collapses the primitive-chain readout problem to three exact endpoint ratios `(β_T/α_T, α_T/α_E, β_E/α_E)` and the exact derivation that the current stack (exact kinematic scaffold `PL S³ × R`, bilinear carrier `K_R`, and slice semigroup `T_R = exp(−Λ_R)`) already determines the `T`-side candidates, leaving only the `E`-channel ratio as the remaining obstruction; these structural reductions follow from the cited upstream authorities.
- **NON-load-bearing (split off / admitted):** The exact value `β_E/α_E = 21/4` — the specific E-channel readout entry needed to close the unique readout-to-slice time-coupling theorem — is not derived from the current Route-2 objects and is explicitly recorded as an open primitive; the positive theorem cannot close until this ratio is independently derived or an admissibility theorem rules out unique selection.

No new axiom, import, or bridge is introduced. The runner-verified core is the
load-bearing content; the named `21/4` bridge remains open.

## Verdict

Route 2 no longer lacks an exact tensor carrier, and the prior open blocker for
this row has a direct upstream no-go answer.

The current exact stack already gives:

- exact background `PL S^3 x R`
- exact slice generator `Lambda_R`
- exact one-step transfer backbone `T_R = exp(-Lambda_R)`
- exact bilinear microscopic carrier
  `K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)`

The new theorem block then sharpens the remaining problem:

- the restricted bright readout reduces exactly to one channelwise map `P_R`
- the endpoint ratio chain does **not** derive exactly on the current stack
- the exact missing readout entry collapses to the `E`-channel ratio
  `beta_E / alpha_E`
- and the unresolved readout map induces the current exact obstruction to a
  unique readout-to-slice time-coupling theorem

The upstream no-go
[`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md)
then proves the admissibility boundary requested by audit: within the current
restricted Route-2 carrier/readout class, even after granting the two T-side
candidates, `beta_E / alpha_E` remains a free parameter unless an additional
E-center endpoint ratio, source-domain rule, or stronger readout primitive is
supplied. In particular, the current objects do not uniquely select
`beta_E / alpha_E = 21/4`.

So the smallest missing primitive is no longer “some tensor observable.”
It is the **exact readout map from `K_R` to the Route-2 two-channel readout**.
The exact next target is sharper: derive a new E-center/source/readout
primitive, or accept this route as blocked at the current restricted surface.

## Exact stack already in hand

The current branch already has:

1. exact `S^3` spatial compactification
2. exact anomaly-forced single-clock time
3. exact background `PL S^3 x R`
4. exact Schur boundary generator `Lambda_R`
5. exact bilinear support carrier `K_R`
6. exact slice semigroup backbone `T_R = exp(-Lambda_R)`

Those are not speculative staging objects anymore. They are the live exact
Route-2 backbone.

## Revised primitive chain

### Primitive P0: kinematic scaffold

- `PL S^3 x R`
- **Status:** exact upstream scaffold

### Primitive P1: bilinear microscopic carrier

- `K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)`
- **Status:** exact reduction exists

### Primitive P2: exact readout map

- `P_R : vec(K_R) -> Theta_R`
- restricted class:
  `gamma_E = alpha_E u_E + beta_E delta_A1 u_E`
  `gamma_T = alpha_T u_T + beta_T delta_A1 u_T`
- **Status:** exact reduction derived, exact theorem still open
- current obstruction:
  the exact endpoint target is equivalent to
  `(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E) = (-1, -2, 21/4)`
- admissibility boundary:
  after granting the two T-side entries, the current restricted carrier leaves
  `beta_E / alpha_E` free; selecting `21/4` requires additional structure.

### Primitive P3: exact readout-to-slice coupling law

- `Xi_R(t ; c) = (P_R c) ⊗ exp(-t Lambda_R) u_*`
- **Status:** exact conditional family exists; unique theorem still open
- induced obstruction:
  unresolved `P_R` means the source factor is still non-unique

### Primitive P4: final Einstein/Regge identification

- identify the exact carrier/readout/coupling package with the final
  Einstein/Regge tensor law on the current restricted class
- **Status:** still open

## Current theorem endpoint

The new endpoint is now very specific.

The current branch already proves:

- exact carrier columns at the two endpoint-shift columns
- exact reduction of the readout problem to one `E` map and one `T` map
- exact endpoint algebra for the ratio chain
- exact slice semigroup on the Route-2 side

What it does **not** yet prove is the exact readout triple

```text
beta_T / alpha_T = -1
alpha_T / alpha_E = -2
beta_E / alpha_E = 21/4.
```

Granting the two `T`-side candidates collapses the remaining missing step to
the single `E`-channel entry `beta_E / alpha_E = 21/4`.

That is the current sharp open problem. The naturality no-go proves
that this entry is not selected by carrier linearity, shell normalization,
T-side transfer data, or low-rational naturality alone.

## Dependency ranking

The clean dependency order is now:

1. exact readout map `P_R`
2. exact readout-to-slice coupling theorem
3. final Einstein/Regge identification

The older “missing tensor primitive” framing is obsolete on this branch.
The older “maybe the current restricted class already selects `21/4`”
framing is also obsolete: the naturality no-go shows the current class does not
uniquely select it.

## Immediate next derivation target

The next theorem should be:

> derive the exact `E`-channel readout entry from current exact Route-2
> objects, or prove a stronger admissibility theorem that shows why the
> current readout class cannot select it uniquely.

The second branch of that repair request is now supplied by the
naturality no-go. The remaining positive-science target is therefore a new
primitive beyond the current restricted carrier/readout surface: derive the
E-center endpoint ratio, a source-domain rule, or a stronger readout-map
theorem.

## Downstream source-boundary firewall

Allowed downstream uses of this packet are limited to:

- cite the exact Route-2 carrier/readout/time authority chain;
- cite the reduced-family algebra showing that `rho_E = 21/4` gives
  `q_E = 15/8` and, under the granted T-side data, center `T/E = -8/9`;
- cite the admissibility boundary that the current restricted
  carrier/readout class leaves `beta_E / alpha_E` free;
- cite the open positive target: derive an E-center endpoint ratio,
  source-domain rule, or stronger readout-map theorem.

Forbidden downstream uses without a new retained bridge:

- do not cite this packet as a derivation of `beta_E / alpha_E = 21/4`;
- do not cite it as a unique readout-to-slice time-coupling theorem;
- do not cite it as final Einstein/Regge identification;
- do not cite the granted T-side candidates as selecting the E-channel ratio;
- do not use the Route-2 no-go as an exhaustive no-go against all possible
  readout primitives;
- do not promote the primitive chain from open gate to positive theorem unless
  a new E-center/source/readout primitive is supplied.

Re-audit should be triggered if a downstream row uses this packet as a
positive readout theorem, as a derivation of the `21/4` E-channel entry, or
as closure of the Route-2 readout-to-slice time-coupling theorem.

## Upstream authorities (Route-2 theorem notes)

- [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) — exact bilinear carrier `K_R` and restricted bright readout class `P_R`.
- [QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md) — exact slice backbone `Lambda_R` and one-step transfer `T_R = exp(-Lambda_R)`.
- [QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) — no-go proving the current restricted Route-2 carrier/readout class does not uniquely select `beta_E / alpha_E = 21/4`.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_primitive_chain_reaudit.py
```

Expected result:

```text
TOTAL: PASS=22, FAIL=0
VERDICT: S3 primitive chain is an open gate backed by Route-2
non-selection.
```
