# Primitive Chain Readout and Time-Coupling Update

**Status:** support - route-2 primitive-chain update
**Date:** 2026-04-19  
**Type:** open_gate
**Status authority:** independent audit lane only.
**Purpose:** restate the remaining Route-2 primitives after the exact bilinear
carrier and the new readout/time-coupling theorem block

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The status update follows algebraically from the cited no-go and bounded notes, but the full positive theorem does not close because the readout map P_R, specifically beta_E / alpha_E = 21/4, is explicitly left open."*

with repair: *"missing_bridge_theorem: derive beta_E / alpha_E = 21/4 from the restricted primitive-chain objects or prove an admissibility theorem showing it cannot be uniquely selected."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The algebraic reduction that collapses the primitive-chain readout problem to three exact endpoint ratios `(β_T/α_T, α_T/α_E, β_E/α_E)` and the exact derivation that the current stack (exact kinematic scaffold `PL S³ × R`, bilinear carrier `K_R`, and slice semigroup `T_R = exp(−Λ_R)`) already determines the `T`-side candidates, leaving only the `E`-channel ratio as the remaining obstruction; these structural reductions follow from the cited retained upstream authorities.
- **NON-load-bearing (split off / admitted):** The exact value `β_E/α_E = 21/4` — the specific E-channel readout entry needed to close the unique readout-to-slice time-coupling theorem — is not derived from the current Route-2 objects and is explicitly recorded as an open primitive; the positive theorem cannot close until this ratio is independently derived or an admissibility theorem rules out unique selection.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## Verdict

Route 2 no longer lacks an exact tensor carrier.

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

So the smallest missing primitive is no longer “some tensor observable.”
It is the **exact readout map from `K_R` to the Route-2 two-channel readout**.

## Exact stack already in hand

The current branch already retains:

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
- **Status:** exact and already retained

### Primitive P1: bilinear microscopic carrier

- `K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)`
- **Status:** exact and already derived

### Primitive P2: exact readout map

- `P_R : vec(K_R) -> Theta_R`
- restricted class:
  `gamma_E = alpha_E u_E + beta_E delta_A1 u_E`
  `gamma_T = alpha_T u_T + beta_T delta_A1 u_T`
- **Status:** exact reduction derived, exact theorem still open
- current obstruction:
  the exact endpoint target is equivalent to
  `(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E) = (-1, -2, 21/4)`

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

- exact carrier columns at the two `A1` endpoints
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

That is the current sharp open problem.

## Dependency ranking

The clean dependency order is now:

1. exact readout map `P_R`
2. exact readout-to-slice coupling theorem
3. final Einstein/Regge identification

The older “missing tensor primitive” framing is obsolete on this branch.

## Immediate next derivation target

The next theorem should be:

> derive the exact `E`-channel readout entry from current exact Route-2
> objects, or prove a stronger admissibility theorem that shows why the
> current readout class cannot select it uniquely.

That is the correct next route-2 primitive target after this block.

## Upstream authorities (Route-2 theorem notes)

- [QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) — exact bilinear carrier `K_R` and restricted bright readout class `P_R`.
- [QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md) — exact slice backbone `Lambda_R` and one-step transfer `T_R = exp(-Lambda_R)`.
