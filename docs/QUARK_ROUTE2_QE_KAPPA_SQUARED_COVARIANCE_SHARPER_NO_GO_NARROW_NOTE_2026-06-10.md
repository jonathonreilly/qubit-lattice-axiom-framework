# The Route-2 q_E Pin, Sharper No-Go: 9/4 = κ² Is the Same-Domain O_h Shell-Leverage Squared (κ=3/2 Derived); the Remaining Open Datum Is the Covariance Bridge λ = q_E/q_T = κ², Which Equivariance Does Not Supply

**Date:** 2026-06-10
**Claim type:** no_go (sharpening of the Route-2 E-channel readout naturality no-go; relocates the missing datum)
**Status authority:** independent audit lane only. This source note does not set, predict, or estimate an audit outcome.
**Primary runner:** [`scripts/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.py`](../scripts/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.py) (PASS=7 FAIL=0)
**Runner cache:** [`logs/runner-cache/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.txt`](../logs/runner-cache/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.txt)

## The pin and the attempt

The `s3_time_primitive_chain` open gate's single missing Route-2 up-sector readout datum is
`c_TE = γ_T(center)/γ_E(center) = −8/9` (equivalently `ρ_E = β_E/α_E = 21/4`; `q_E = 1 + ρ_E/6 = 15/8`;
with the granted T-side `q_T = 5/6`, the covariance `λ := q_E/q_T = 9/4`). The
[naturality no-go](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) proved the
restricted channelwise carrier class does not select it. This note reports a genuine attempt to derive
it from the exact finite Route-2 star/`O_h` objects, **without empirical input** (no observed masses, no
fitted target, no nearest-rational selection, no live-endpoint selector — the no-go's forbidden inputs).
**Result: no derivation; a sharper no-go that relocates the missing datum.**

## Exact content (every load-bearing fact independently re-verified by the runner)

1. **A derived same-domain leverage `κ = 3/2` (K1).** The 7-site octahedral star is 1 center + 6 arms;
   the 6-arm `O_h` permutation rep decomposes multiplicity-free as `A1g ⊕ Eg ⊕ T1u`. Via the antipodal
   involution `A` (the action of `−I`, swapping each arm with its opposite): `P_A1` = Reynolds average
   (all entries `1/6`), `P_T1 = (I−A)/2` (antipodal-odd, 3-dim), `P_E = (I+A)/2 − P_A1` (2-dim). The
   exact per-arm projector weights are `P_A1 = 1/6`, `P_E = 1/3`, `P_T1 = 1/2` (= dim/6). Hence the
   **same-domain shell leverage on the readout's own E/T channels**
   `κ := P_T1(arm,arm)/P_E(arm,arm) = (1/2)/(1/3) = 3/2`, and `κ² = 9/4`.
2. **Commutant independence (K3).** `E` and `T1` are inequivalent `O_h` irreps, so `Hom_Oh(E,T1) = 0`
   (the Reynolds intertwiner `⟨P_T1 · g · P_E⟩ = 0`). Every `O_h`-equivariant star operator carries
   **independent** scalars `λ_E, λ_T` — equivariance ties nothing between the channels, and the A1
   center-excess gives the **same** center increment `1/6` to E and T (the carrier does not distinguish
   them, K5).
3. **Endpoint algebra (K4).** With shell normalization + the granted T-side (`β_T/α_T = −1 → q_T = 5/6`;
   `α_T/α_E = −2`): `q_E = 1 + ρ_E/6`, `c_TE = −2·q_T/q_E`. The target chain `ρ_E=21/4 ↔ q_E=15/8 ↔
   c_TE=−8/9` holds exactly, and `λ = q_E/q_T = 9/4`.
4. **The pinning (K5).** `9/4 = κ²` **exactly** — the derived same-domain leverage squared. **But the
   bridge `λ = q_E/q_T = κ²` is not a consequence** of (1)–(2): equivariance leaves `λ_E, λ_T`
   independent, the carrier gives equal E/T center increments, and the `−8/9` sign enters only through
   the granted `α_T/α_E = −2` (not the projectors). So the remaining open datum is precisely the
   covariance rule `λ = κ²` (equivalently the E-center datum / `ρ_E`). This note does not adopt that
   datum as an approved input.
5. **Admissibility continuum (K6).** Positivity of the E-center lift gives only `q_E > 0 ⇔ ρ_E > −6`;
   idempotency/norm fixes the E-row norm, not its direction. So `ρ_E ∈ {−1, 0, 1, 21/4, 6, …}` are all
   exact admissible reduced maps — `λ = 9/4` is one special value in a continuum.

## The relocation (the genuinely new result, K7)

The *other* candidate origin of the same datum — `c_TE = −R_conn = −(N_c²−1)/N_c² = −8/9`, an `SU(3)`
**fiber-space** color fraction — was already adjudged a **cross-domain coincidence** no-go
([`CTE_RCONN_..._CROSS_DOMAIN_COINCIDENCE`](CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md)):
a position-space tensor ratio identified with a fiber-space color fraction, with no typed link.

By contrast, **`κ = 3/2` is a *same-domain* `O_h` leverage on the readout's own E/T channels** — not a
cross-domain object. So this note **relocates** the missing datum from the cross-domain color
coincidence to a **same-domain covariance rule** `λ = κ²` — a sharper, more attackable target. The two
candidate structural numbers are *distinct* (`9/4 ≠ 8/9`) and feed *distinct* slots (the covariance
`q_E/q_T` vs `c_TE` directly), yet both yield the same final `ρ_E = 21/4`; **neither is derived.**

## Verdict

No derivation of `ρ_E = 21/4` was found. The pin remains an open supplied datum, now sharpened: `9/4 = κ²` with
`κ = 3/2` the derived same-domain `O_h` shell leverage, and the **single remaining free datum is the
covariance bridge `λ = q_E/q_T = κ²`**, which `O_h` equivariance provably does not supply. The next
positive route would have to derive that covariance rule (or an equivalent E-center primitive) from
named tensor/source-domain structure — *not* from any limit of the bright-tensor functional (the
box-size scan note linked below closes that), nor from the cross-domain color identification
(already a coincidence no-go).

## No-go discipline gate (N1–N8)

- **N1 (alternative routes).** Six routes are separated: (a) exact star/`O_h` scalars — yields `κ=3/2`
  but not the covariance squaring; (b) cross-channel equivariance — `Hom(E,T1)=0`, ties nothing;
  (c) A1 carrier center-excess — gives the same `1/6` increment to E and T; (d) positivity/norm/closure —
  leaves the `ρ_E>−6` continuum; (e) the source-domain color fraction — closed as a cross-domain
  coincidence by the linked `c_TE=-R_conn` note; (f) the bulk-limit route — closed by the linked box-size
  scan note. None derives `λ=κ²`.
- **N2 (wall independence).** The walls are independent: equivariance independence (K3), carrier equal-
  increment (K5), positivity non-uniqueness (K6), the cross-domain color-route mismatch, and the
  bulk-limit miss each separately fail to fix `ρ_E`; closing one does not close the others.
- **N3 (hidden-wall scan).** `κ=3/2`, `κ²=9/4`, the projector weights, and `Hom(E,T1)=0` are derived in
  exact arithmetic in the runner; no value is asserted by name or imported.
- **N4 (residual matching).** The residual is exactly the E-center datum / covariance `λ`, the same
  residual the April naturality no-go named; this note sharpens its *location* (same-domain `λ=κ²`), not
  its logical force.
- **N5 (rhetoric).** "Sharper no-go" means a sharper *location* of the same open datum; it is **not** a
  claim that `ρ_E` is underivable by any future construction (N7), nor that `9/4=κ²` is a derivation.
- **N6 (partial-closure).** Real partial content: `κ=3/2` is derived same-domain; the missing step is the
  single covariance rule `λ=κ²` — a well-posed future derivation or owner-approved input target. No
  input is adopted here.
- **N7 (steelman).** A future nonlinear tensor observable, or a derived readout-covariance primitive,
  could still supply `λ=κ²`; this note does **not** prove impossibility over such constructions — it
  closes the finite-star/equivariant/carrier-linear/positivity/simple-covariance routes.
- **N8 (cross-cycle echo).** Consistent with the naturality no-go (`ρ_E` free in the restricted class),
  the box-size scan (no bulk limit gives `15/8`), and the `c_TE=−R_conn` cross-domain coincidence; this
  note adds the same-domain `κ²` relocation without adopting a new premise.

## What is / is not claimed

- **Is:** `κ=3/2` and `κ²=9/4` are derived exactly from the `O_h` per-arm projectors (same-domain);
  `Hom(E,T1)=0` and the equivariant-scale independence are exact; the endpoint algebra and the
  `ρ_E=21/4 ↔ q_E=15/8 ↔ c_TE=−8/9 ↔ λ=9/4` chain are exact; the admissibility continuum (`ρ_E>−6`) is
  exact; the missing datum is relocated to the same-domain covariance rule `λ=κ²`.
- **Is not:** does **not** derive `ρ_E=21/4`/`c_TE=−8/9`; does **not** prove impossibility over arbitrary
  future nonlinear observables; does **not** identify `c_TE` with the color fraction `−R_conn` (that is
  the cross-domain coincidence no-go); does **not** use the bright-tensor `N=15` proximity as a
  derivation (the box-scan closed the limit route); adds no axiom, primitive, or fitted value.

## Load-bearing inputs

- [`QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`](QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md) — the P_R reduction + endpoint algebra (K4).
- [`QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`](QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md) — the no-go this note sharpens; its forbidden-inputs discipline binds here.
- [`TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md`](TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md) — the 7-site star + the A1 center-excess `1/6` (K5).
- [`CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md`](CTE_RCONN_SPATIAL_TENSOR_COLOR_BRIDGE_IS_A_CROSS_DOMAIN_COINCIDENCE_NARROW_NO_GO_NOTE_2026-06-08.md) — the cross-domain color route this note relocates away from (K7).
- [`QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md`](QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md) — the bulk-limit route closure used in the no-go discipline gate.
- [`S3_TIME_PRIMITIVE_CHAIN_NOTE.md`](S3_TIME_PRIMITIVE_CHAIN_NOTE.md) — the open gate the datum belongs to.

## Forbidden-imports check

No PDG / observed / fitted value is consumed. The star geometry, the `O_h` projectors, `κ=3/2`,
`Hom(E,T1)=0`, the endpoint rationals, the continuum, and `R_conn = (N_c²−1)/N_c²` (computed from
`N_c=3`) are all derived in exact arithmetic in the runner; `5/6, 15/8, −2, −8/9, 9/4, 21/4` appear only
as comparison targets, per the naturality no-go's comparator discipline.
