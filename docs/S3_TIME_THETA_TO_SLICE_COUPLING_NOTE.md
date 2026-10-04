# Route 2 Readout to Slice Coupling

**Status:** open_gate route survey — exact conditional readout-to-slice
coupling family obtained by composing cited upstream authorities, with the
unique-exact `Theta_R -> Lambda_R` coupling theorem **not** closed because
the underlying readout-map endpoint triple is not yet derived.
**Date:** 2026-04-19 (audit-narrowing refresh: 2026-05-10)
**Purpose:** state the current exact status of the Route-2 (s3-time)
`Theta_R -> Lambda_R` coupling problem after the exact bilinear carrier and
the audited Route-2 readout / time-coupling notes.
**Type:** open_gate
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/frontier_s3_time_theta_to_slice_coupling.py`](../scripts/frontier_s3_time_theta_to_slice_coupling.py)
**Authority role:** records, but does not close, the s3-time arm of the
Route-2 readout-to-slice coupling family. Names the missing readout-map
endpoint triple as the single open theorem target for this row.


## Quantifier boundary (2026-10-04)

The all-site identity holds for the stated seven-site stencil inside a
Dirichlet box containing all six neighbours. Equality of centre and shell
readouts follows **only when every interpolation stencil avoids the origin**,
the anchor ignores it, and the required denominators are nonzero. Locality
alone does not force this: the six-point control touches the origin and leaks
the spike. The four-point counterexample refutes interpolation-independent
interpretation of the size-15 rationals; it does not select a physical
interpolation. The finite sampled ladder fails a plateau test. Any statement
below that it “does not converge” means that finite diagnostic only; an
asymptotic nonconvergence theorem is not supplied.

## Corrigendum (2026-09-30)

**What was wrong.** This note names the readout-map endpoint triple
`(beta_T/alpha_T, alpha_T/alpha_E, beta_E/alpha_E) = (-1, -2, 21/4)` as the
single open theorem target, as if it were a property of the lattice gravity
metric waiting to be derived. Its two centre-minus-shell entries (`-1` and
`21/4`) are not. The centre and shell sources give the same lattice potential
at every site except the origin, where they differ by exactly `1/6`, and the
size-15 values come from the repo's global cubic-spline interpolation ringing on
that one-site spike. With a local interpolation the same readout gives
`beta_T/alpha_T = beta_E/alpha_E = 0` (`q_T = q_E = 1`, `rho_E = 0`) at every
box size, size 15 included.

**Corrected statement.** For those two entries there is no field value to
derive; the sentence naming the missing triple as the next theorem target is
withdrawn. The middle entry `alpha_T/alpha_E` is a shell-only quantity and is
not decided by this correction. This corrigendum does not change the row's type
or any status.

**What still stands.** The exact conditional coupling family, the restricted
readout class and its algebra, and the inherited non-uniqueness of `P_R`
(`rho_E = 0` and `rho_E = 21/4` are both admissible maps on the restricted
class). What is withdrawn is only the description of the triple as a
derivable property of the field.

**Evidence.** The note `QUARK_ROUTE2_ENDPOINT_TRIPLE_CENTER_MINUS_SHELL_READOUT_IS_A_GLOBAL_CUBIC_SPLINE_ARTEFACT_ON_A_ONE_SITE_SPIKE_BOUNDED_THEOREM_NOTE_2026-09-30.md` proves the identity `phi(e0) - phi(s_unit) = delta_origin / 6` at every site and replays the readout with the interpolation swapped (checker `scripts/frontier_quark_route2_endpoint_triple_center_minus_shell_readout_cubic_spline_artefact_check_2026_09_30.py`, `TOTAL: PASS=24 FAIL=0`). Same-family checks (Claude Sonnet 5.5), no independent referee yet.

## Audit boundary

This note assembles a conditional Route-2 coupling family on the s3-time
arm by importing four upstream authorities and combining them
algebraically. It is **not** a derivation of the underlying carrier,
slice backbone, or readout map.

**Cited authorities (one-hop deps; cited but not closed in this note):**

- [`QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md)
  (`claim_type: bounded_theorem`, `audit_status: audited_clean`) —
  canonical Route-2 slice backbone authority. Supplies the exact slice
  generator `Lambda_R` (SPD), the transfer matrix `T_R = exp(-Lambda_R)`,
  the seed law `V_R(t) = exp(-t Lambda_R) u_*`, and the conditional
  coupling family `Xi_P(t ; c) = (P_R c) ⊗ V_R(t)` once an admissible
  readout map `P_R` is supplied. Imported as the slice-backbone authority
  for this s3-time arm.
- [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
  (`claim_type: no_go`, `audit_status: audited_clean`) — canonical
  Route-2 readout-map authority. Establishes the exact bilinear carrier
  `K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)`, the restricted
  bright readout class
  `gamma_E = alpha_E u_E + beta_E delta_A1 u_E`,
  `gamma_T = alpha_T u_T + beta_T delta_A1 u_T`, and the
  **audited-clean no-go** that the endpoint dimensionless triple
  `(beta_T / alpha_T, alpha_T / alpha_E, beta_E / alpha_E) = (-1, -2, 21/4)`
  is not derived by the current exact stack. Imported as the readout-class
  authority and as the canonical statement of the open obstruction this
  row inherits.
- [`QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md)
  (`claim_type: no_go`, `audit_status: audited_conditional` as of the
  2026-05-10 fresh audit; previously `audited_clean`) — companion
  source-domain bridge no-go on the same Route-2 arm; cited for
  cross-confirmation that the readout-map blocker is not bypassed by a
  source-domain detour, with the source-domain typed-edge inventory now
  flagged as configured (hard-coded in the runner) rather than derived.
  This row inherits that conditional status; it does not bypass it.

**Admitted-context derivation gap (real, not import-redirect):**

The unique exact `Theta_R -> Lambda_R` coupling theorem on this s3-time
arm requires the readout-map endpoint triple to be derived. The cited
[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
records this as an **audited-clean no-go**: the exact endpoint triple is
not derived by the current exact stack on `main`. This row inherits that
no-go and does not bypass it.

## Verdict (scope-bounded)

Conditional on the cited upstream authorities, this row records:

- exact slice backbone `Lambda_R`, `T_R = exp(-Lambda_R)`,
  `V_R(t) = exp(-t Lambda_R) u_*` — imported from the Route-2 time-coupling
  authority;
- exact bilinear carrier `K_R(q)` and restricted bright readout class —
  imported from the Route-2 readout-map authority;
- exact conditional coupling family
  `Xi_P(t ; c) = (P_R c) ⊗ V_R(t)`
  obtained algebraically once an admissible readout map `P_R` is supplied;
- explicit absence, on `main`, of any retained-grade derivation of the
  readout-map endpoint triple, and therefore explicit absence of any
  unique exact `Theta_R -> Lambda_R` coupling theorem on this arm.

So the honest endpoint is:

> exact conditional coupling family obtained by composing cited Route-2
> authorities; exact induced obstruction to uniqueness inherited from the
> Route-2 readout-map no-go.

## Exact ingredients already available

### Carrier

- `K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)`

### Readout class

- restricted bright form
  `gamma_E = alpha_E u_E + beta_E delta_A1 u_E`
  `gamma_T = alpha_T u_T + beta_T delta_A1 u_T`

### Slice backbone

- exact `Lambda_R`
- exact `T_R = exp(-Lambda_R)`
- exact seed law `V_R(t) = exp(-t Lambda_R) u_*`

## Exact conditional coupling family

Once an admissible readout map `P_R` is chosen, the current branch supports
the exact family

```text
Xi_P(t ; c) = (P_R c) ⊗ V_R(t)
```

for every restricted carrier column `c`.

This is exact because:

1. `c` is exact,
2. `P_R` is algebraic once specified,
3. `V_R(t)` is exact.

So the route does not lack a carrier-to-slice construction anymore.

## Why the unique theorem is still blocked

The cited
[`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md)
records as an audited-clean no-go that the endpoint triple

```text
beta_T / alpha_T = -1
alpha_T / alpha_E = -2
beta_E / alpha_E = 21/4
```

is **not** derived by the current exact stack on `main`. Therefore the
readout map remains non-unique on the restricted class, and the unique
exact `Theta_R -> Lambda_R` coupling theorem is **not** closed on this
s3-time arm.

The cited Route-2 readout-map note documents the obstruction directly:

- distinct exact admissible maps agree at shell normalization,
- but produce different center `E` source factors,
- so they produce different exact spacetime tensors on the same slice
  backbone.

The ambiguity is therefore localized to the unresolved readout-map
endpoint triple — not to `Lambda_R` (audited_clean) and not to the
carrier `K_R` (audited_clean). This row imports that localization and
does **not** bypass it.

## Current blocker

The blocker is now very precise:

> unresolved readout exactness blocks a unique exact `Theta_R -> Lambda_R`
> coupling law on the current carrier.

This is sharper than the older “missing tensor observable” statement, because
the carrier and the slice semigroup are already exact.

## Bottom line

Conditional on the cited upstream authorities, this row records:

- exact carrier (imported from Route-2 readout-map authority),
- exact slice backbone (imported from Route-2 time-coupling authority),
- exact conditional readout-to-slice family obtained algebraically from
  the imports,
- no unique exact `Theta_R -> Lambda_R` coupling theorem on this arm,
  because the readout-map endpoint triple is not derived (no-go inherited
  from the cited Route-2 readout-map authority).

The next theorem target is the missing readout-map endpoint triple. That
target lives on the upstream readout-map row, not on this row. This row
remains `open_gate` until that target closes upstream.

## Primary runner

The primary verifier for this row is
[`scripts/frontier_s3_time_theta_to_slice_coupling.py`](../scripts/frontier_s3_time_theta_to_slice_coupling.py).
It checks the source-note boundary, rebuilds the exact conditional family
from the Route-2 slice backbone, and confirms that two admissible readout
maps agree at the shell while differing at the center. The runner therefore
supports only the stated open-gate endpoint: exact conditional family plus
inherited non-unique readout obstruction, not a unique closed coupling theorem.
