# Gravity Generator-Shift Eikonal Bridge — Honest Closure Note

**Date:** 2026-06-20
**Claim type:** bounded_theorem (NARROW: operator-shift sub-step only) with an
explicit named-premise residual on the WKB/Fermat reading.
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:** [`scripts/gravity_generator_shift_bridge_2026_06_20.py`](../scripts/gravity_generator_shift_bridge_2026_06_20.py)
**Runner cache:** [`logs/runner-cache/gravity_generator_shift_bridge_2026_06_20.txt`](../logs/runner-cache/gravity_generator_shift_bridge_2026_06_20.txt)
(`TOTAL: PASS=14 FAIL=0`)

## Target row located

- **claim_id:** `gravity_premise4_refractive_index_from_dispersion_bounded_theorem_note_2026-06-07`
- **current status (ledger snapshot):** `audited_conditional`, `chain_closes=false`,
  criticality `leaf`, deps `[self_consistency_forces_poisson_note,
  lensing_exponent_is_a_dipole_crossover_resolution_bounded_theorem_note_2026-06-07,
  gravity_clean_derivation_note]`.
- **exact open residual** (from `docs/audit/MISSING_DERIVATION_PROMPTS.md` line ~3502
  and `missing_derivation_difficulty.json`):
  > `missing_bridge_theorem: add a retained one-hop derivation of H->H+phi and the
  > WKB/Fermat identification n=k/k0; if T4 remains a lattice-lensing claim,
  > include the retained a/r source-potential or Green-kernel authority ...`

The residual has TWO halves. The orchestrator scopes the downstream phase-count
algebra `n = k_s/k0` as already closed in the premise4 note (the exact axis map
`k(phi)=arccos(1-(E-phi)/2)` and small-k limit `n=1-phi/(2E)` are runner-verified
there). This note targets the UPSTREAM half: the additive scalar generator shift

```text
H_s = H_0 + s * I          (sign +, normalization coefficient exactly 1)
```

i.e. the `H -> H + phi` step that the premise4 note currently labels "supplied by
`SELF_CONSISTENCY_FORCES_POISSON_NOTE.md`".

## What was already retained vs. what was stipulated

- `GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`
  (retained-bounded) proves the **action-level** static source coupling
  `Delta S_test = -m phi(x) Delta tau`, i.e. an on-site Euclidean weight
  `exp(-Delta tau * s)` with `s = phi` (for unit test mass).
- `SELF_CONSISTENCY_FORCES_POISSON_NOTE.md` **assumes** `S = L(1-phi)` and the
  field-in-Hamiltonian reading as a starting point; it derives Poisson *operator
  preference*, not the generator shift.
- The premise4 note then reads `lambda(k) + phi = E` — the operator shift at the
  dispersion level — as a **supplied** input. No retained note recomputes the
  operator-level shift, its sign, or its normalization coefficient.

So the operator-level `H_s = H_0 + s*I` was never recomputed in-tree.

## The bridge (recomputed in-tree)

Given the retained action surface, the operator shift follows by the **standard**
discrete-time path-integral <-> transfer-matrix (Lie-Trotter) correspondence:

1. **(A)** The retained generator is the graph Laplacian `H_0 = -Delta_lat`
   (symmetric, PSD, single constant zero mode). Recomputed: runner A1-A2.
2. **(B)** For a static on-site field `V = diag(s(x))`, the symmetric (Strang)
   transfer step
   `T = exp(-dtau V/2) exp(-dtau H_0) exp(-dtau V/2)`
   has one-step generator `-log(T)/dtau = H_0 + V + O(dtau^2)`. The shift is
   **additive** and the coefficient on `V` is **exactly 1** (not 1/2, not 2);
   the residual falls as `dtau^2`. Recomputed: runner B1 (||gen-(H0+V)||=8e-5),
   B2 (order ratio 3.97), B3 (coefficient c=1.00006).
3. **(C)** A **uniform** shift `V = s*I` commutes with `H_0` and moves the entire
   spectrum by exactly `+s` with NO Trotter error. This fixes both sign and
   normalization exactly at the operator level: the sign is `+` (higher field =
   higher generator energy), and a coefficient `c != 1` is rejected. Recomputed:
   runner C1 (max|shift-s|=1e-14), C2 (sign +), C3 (control c=2 rejected).
4. **(D)** The normalization is forced by the retained action coupling: the
   per-step weight `exp(-dtau s)` from `Delta S = -s dtau` matches the
   generator-side weight iff the coefficient is `c = 1`; `c = 1/2` fails.
   Recomputed: runner D1-D2.
5. **(E)** The shifted generator `(H_0 + s I)` evaluated on the axis plane wave
   reproduces the premise4 fixed-energy reading `lambda_axis(k) + s = E`, hence
   `k(s) = arccos(1-(E-s)/2)`, `n = k_s/k0 = 1 - phi/(2E) + ...` — closing the
   hand-off to the already-closed phase-count algebra. The linear slope
   `dn/dphi|_0 = -1/(2E)` is verified numerically (-25.04 at E=0.02 vs -25.0).
   Recomputed: runner E1-E4.

`TOTAL: PASS=14 FAIL=0`.

## Honest status (PROMOTION VALUE GATE)

This note does **not** claim a clean `bounded_theorem` closure of the parent
premise4 row, for two reasons:

1. **The operator-shift sub-step is standard-math completion of a retained
   coupling.** The Lie-Trotter / transfer-matrix correspondence between a static
   diagonal action coupling and an additive diagonal generator term is textbook
   mathematics. An independent audit lane could complete this step from the
   already-retained weak-field action coupling plus standard math. Per the
   promotion value gate, a result that the audit lane could already complete from
   retained primitives + standard math is **not** new derivational content and
   must NOT be promoted to a stand-alone bounded_theorem closure of the row.
   What this note legitimately supplies is the in-tree RECOMPUTATION proving the
   sign (`+`) and normalization (coefficient exactly `1`) of `H_s = H_0 + s*I`,
   which removes the "supplied without recomputation" character of the upstream
   half of the blocker.

2. **The second half of the blocker is unchanged.** The WKB/Fermat
   identification `n = k/k0` (reading a local wavenumber ratio as a Fermat
   refractive index, i.e. the eikonal/geometric-optics bridge) is still a
   **supplied** physical interpretation, not derived from the retained surface.
   That is a genuine admitted physical input (the geometric-optics limit of the
   lattice propagator), not closable by standard algebra over the retained
   primitives, and it remains the load-bearing open residual.

**Net effect on the row:** the upstream `H -> H + phi` half moves from
"supplied by self-consistency note" to "operator-level shift recomputed in-tree
from the retained action coupling by standard transfer-matrix math (sign +,
norm 1)"; the downstream WKB/Fermat half remains an admitted geometric-optics
premise. The parent row therefore stays `audited_conditional` /
`chain_closes=false`; this note narrows, but does not eliminate, its residual.

## Named premise (the remaining admitted input)

> **WKB/Fermat eikonal reading (admitted).** On the weak-field lattice
> propagator surface, the geometric-optics limit identifies the local-wavenumber
> ratio `k_s/k0` of the fixed-energy solution of `(H_0 + s I)psi = E psi` with
> the Fermat refractive index `n`. This is the standard eikonal/WKB bridge; it is
> not derived here from the retained Lattice+Quantum+Record primitives.

## Scope / does not claim

- No new axiom or primitive; the four approved primitives (`minimal_axioms`,
  `scale_reference_primitive`, `kinetic_isotropy_primitive`,
  `realized_state_primitive`) are unchanged and none is re-axiomatized.
- The `G_Newton` normalization remains registered/observed data, not derived.
- No nonlinear / tensorial / strong-field gravity; weak-field linear order only.
- No audit verdict; the independent audit lane is the sole status authority.

## Relation to retained inventory

| Packet | Ledger status | Role here |
| --- | --- | --- |
| `gravity_weak_field_source_response_bridge` | retained-bounded | Supplies the static action coupling `Delta S=-m phi dtau` that fixes the shift normalization. |
| `self_consistency_forces_poisson_note` | retained-bounded | Prior (weaker) supplier of `H->H+phi` as a stipulation. |
| `gravity_clean_derivation_note` | retained-bounded | Downstream consumer of premise (4). |
| `gravity_premise4_refractive_index_from_dispersion...` | audited_conditional | The parent row whose upstream half this note recomputes. |
