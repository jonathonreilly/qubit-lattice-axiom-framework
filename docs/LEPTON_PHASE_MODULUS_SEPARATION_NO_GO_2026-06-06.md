# Charged-Lepton Phase/Modulus Separation Narrow No-Go

**Date:** 2026-06-06
**Type:** no_go
**Claim type:** no_go
**Claim scope:** the standalone structural fact that, for the Brannen/circulant
charged-lepton sqrt-mass spectrum `sqrt(m_k) = a(1 + 2 sqrt(r) cos(delta + 2 pi
k/3))`, the Koide modulus `r = |b|^2/a^2` and the Brannen phase `delta = arg(b)`
live on **separate `C3`-invariants** — so a real `C3`-invariant **scalar action**
can fix `r` (the modulus, `r=1/2 <=> Q=2/3`) but **provably cannot stationarize
`delta` at `2/9`** (its stationary phases are forced to the `C3`-rational
directions `delta in {0, pi/3, 2pi/3, ...}`). This **prunes** the
scalar/variational/partition route to `delta`; it does **not** close `delta = 2/9`
(the `C3`-covariant `eta`/holonomy = chirality route is untouched and open).
**Status authority:** independent audit lane only. Source note; later status is
set by the audit pipeline.
**Runner:** [`scripts/lepton_phase_modulus_separation_no_go_2026_06_06.py`](../scripts/lepton_phase_modulus_separation_no_go_2026_06_06.py)
(`TOTAL: PASS=13 FAIL=0`, exact `sympy`).

```yaml
actual_current_surface_status: no-go
target_claim_type: no_go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: null
proposal_allowed: false
proposal_allowed_reason: "Prunes the scalar/variational/partition class of delta=2/9 derivations; closes no positive theorem, retires no axiom, leaves delta=2/9 open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Provenance

From the `delta = 2/9` fresh-angle hunt (workflow `wa0o7fje5`, Lens 1), run with an
explicit AVOID-list of the worked routes (the six `(N-1)/N^2` mechanisms, APS-`eta`,
Fisher-Rao, `L(N;1)` holonomy, the two logged `koide_delta_*` no-gos). The hunt
found **no fresh derivation** of `delta=2/9`; its genuinely-new, framework-native,
off-AVOID-list content is the separation no-go recorded here.

## Statement

For the circulant generation mass operator `Y = a I + b C + conj(b) C^2` with
`z := b/a = sqrt(r) e^{i delta}` (so `|z|^2 = r`, `Re z^3 = r^{3/2} cos 3delta`):

**(N1) The elementary symmetric functions of the sqrt-mass spectrum separate
`r` from `delta`** (exact, runner Section S):
```text
e1 = 3 a                                         (scale)
e2 = 3 a^2 (1 - r)            -- delta-BLIND; e2 = (3/2) a^2 <=> r=1/2 <=> Q=2/3 (the entire Koide content)
e3 = a^3 (1 - 3r + 2 r^{3/2} cos 3delta)         -- the ONLY carrier of delta, solely via cos 3delta
```

**(N2) Scalar-action phase-blindness** (exact, runner Section W). Any real
`C3`-invariant scalar action is a function `W(|z|^2, Re z^3) = W(r, r^{3/2}
cos 3delta)`. Its `delta`-stationarity factorizes as
`dW/ddelta = W_X * (-3 r^{3/2} sin 3delta)`, so a stationary point with `W_X != 0`
requires `sin 3delta = 0`, i.e. `delta in {0, pi/3, 2pi/3, ...}` — the
`C3`-rational directions. `delta = 2/9` is **not** among them (`2/9 = n pi/3`
needs `n = 2/(3 pi)`, non-integer). Hence such an action **can fix the modulus `r`
(→ `r=1/2`) but can never stationarize the phase `delta` at `2/9`.**

**(N3) Convergence with the register-not-read partition map.** The genuine
register-not-read license (the central-sector partition map `D = sum_k P_k M P_k`)
delivers the **weight ratio `r`** (the `e2`-content), never the **within-block
phase `delta`** (the `e3` `cos 3delta` content). So the variational route (N2) and
the partition route land on the **same object — the modulus `r`** — from opposite
directions; **neither touches the phase.** The `(r, delta)` plane has exactly two
native classes: `r` is a **modulus** (scalar/variational/partition → `r=1/2`);
`delta` is a **phase** that only a `C3`-**covariant** `eta`/holonomy object can
carry off the rational directions. There is no third native option.

**Consequence.** `delta = 2/9` is **not an independent target.** A `C3`-covariant
`eta`/holonomy object is exactly the chirality/orbit-splitting structure — the
**same gate as Koide-`Q` and generation-ID.** So the lepton-phase gate and the
chirality gate are one gate, not two.

## Tested fresh candidates (all collapse; recorded for the no-go boundary)

| candidate (fresh-hunt) | exactly 2/9? | native? | verdict |
|---|---|---|---|
| single scalar `C3`-action fixing `(r,delta)` jointly | no (forced to `C3`-rational) | yes | **(N2) forbids** |
| native `C3`-orbit Berry phase on the circulant | 0 (eigenvector rigidity, retained) | yes | gives 0, not 2/9 |
| native `Z^3` plaquette / staggered-`eta` holonomy | roots of unity / `Z2` | yes | quantized, not 2/9 |
| Hirzebruch `G`-signature defect of `L(3;1)` | **exactly `-2/9`** (`(N-1)(N-2)/3N`, distinct family) | **no** (curved imported `S^3/Z_3`) | APS-`eta` (AVOID-list); already on main (`Z_N_ASYMMETRY_RESIDUAL_1`); + radian-bridge no-go |

The combinatorial space of future mechanisms is not exhaustive in principle; within
the native scalar/variational/partition class, (N2) is a complete obstruction.

## No-Go Discipline Gate

**Status: PASS for the narrow scalar-class no-go only.** The claim closed is *not*
"`delta=2/9` is underivable" — it is "no real `C3`-invariant **scalar** action
stationarizes `delta` at `2/9`; `delta` is a covariant phase, not a modulus."

- **N1 — alternative routes:** scalar/variational action (forbidden, N2);
  partition map (delivers `r` not `delta`, N3); native Berry/holonomy (0 or roots
  of unity); `C3`-covariant `eta`/holonomy (**NOT closed** — this is where `delta`
  lives, the chirality gate, left open).
- **N2 — wall independence:** the symmetric-function separation (N1) and the
  Wirtinger stationarity (N2) are exact algebra; the partition convergence (N3) is
  an independent route landing on the same modulus. They reinforce, not restate.
- **N3 — hidden-wall scan:** load-bearing inputs are the circulant structure
  (A1+A2) and the exact symmetric-function/Wirtinger algebra (runner). No "standard"
  phrase is a hidden input; "scalar `C3`-invariant" is defined explicitly as
  `W(|z|^2, Re z^3)`.
- **N4 — residual matching:** matches the `delta=2/9` open gate
  (`LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE`) and the session's partition-map
  result; the `G`-signature `-2/9` is cited (already on main), not re-derived.
- **N5 — rhetoric audit:** "provably cannot" is scoped to real `C3`-invariant
  scalar actions; the covariant `eta`/holonomy route is explicitly left open.
- **N6 — partial-closure:** the open path is the `C3`-covariant `eta`/holonomy =
  chirality gate (= Koide-`Q`/generation-ID); not called an axiom; left for that gate.
- **N7 — steelman:** the strongest objection — "a cleverly-chosen scalar functional
  might still hit `2/9`" — is refuted exactly: *any* `W(|z|^2, Re z^3)` has
  `delta`-dependence solely through `cos 3delta`, so its `delta`-derivative is
  `proportional to sin 3delta` regardless of `W`'s form; `2/9` is not a zero of
  `sin 3delta`. No scalar choice evades it.
- **N8 — cross-cycle echo:** consistent with the chirality-gate convergence already
  recorded for Koide-`Q` and generation-ID (`delta` joins that one gate); does not
  re-open the worked `(N-1)/N^2`/APS-`eta` routes.

## What this note does NOT claim

- Does **not** close `delta = 2/9` (it stays `open_gate` / Tier-A admission).
- Does **not** foreclose the `C3`-covariant `eta`/holonomy route — that is where
  `delta` lives (the chirality gate), and it is left open.
- Does **not** derive `r=1/2` (it states `r` is the modulus a scalar action *can*
  reach; the lepton occupancy of `r=1/2` is matched, per the dial discipline).
- Does **not** re-derive the `G`-signature `-2/9`, the six `(N-1)/N^2` routes,
  APS-`eta`, Fisher-Rao, or `L(N;1)` holonomy (all on main / the AVOID-list).
- Sets no audit status.

## Load-bearing references

- `LEPTON_BRANNEN_BAE_DELTA_TWO_NINTHS_OPEN_GATE_NOTE_2026-05-26` (open_gate) — the
  `delta=2/9` gate this prunes one route of.
- `KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE_2026-05-31` (retained_bounded) — the
  native `C3`-orbit Berry phase is 0 (eigenvector rigidity).
- `Z_N_ASYMMETRY_RESIDUAL_1_FINITE_VS_CONTINUUM_NOTE_2026-05-31` (retained_bounded)
  — the `G`-signature defect `-2/9` (cited, not re-derived).
- `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24` (retained_no_go) —
  the dimensionless→radian bridge wall (why a rational `-2/9` is not yet a radian).
- This session's register-not-read partition-map scope correction
  (`REGISTER_NOT_READ_SCOPE_CORRECTION_PANEL_VERDICT_2026-06-06`) — the partition
  map delivers `r` not `delta` (N3 convergence).

## Forbidden imports check

- No PDG values consumed; the masses do not enter (the no-go is structural algebra
  on the circulant). No literature comparators; no fitted selectors; no new axiom.
- The `G`-signature `-2/9` is cited as the existing on-main object, not introduced.

## Validation

`scripts/lepton_phase_modulus_separation_no_go_2026_06_06.py` (`PASS=13 FAIL=0`,
exact sympy): Section S (the `e1/e2/e3` separation; `e2` delta-blind, `e3` via
`cos 3delta`), Section W (`dW/ddelta proportional to sin 3delta`; stationary
`delta = n pi/3`; `2/9` excluded), Section C (partition-map convergence; two native
classes), Section B (scope: prunes scalar route, leaves `delta=2/9` open).

## Reading rule

This note is the claim boundary for: charged-lepton `r` (modulus) and `delta`
(phase) live on separate `C3`-invariants, and no real `C3`-invariant scalar action
(nor the register-not-read partition map) can stationarize/deliver `delta` at `2/9`
— `delta` is a covariant phase whose only native home is the `C3`-covariant
`eta`/holonomy = chirality gate (the same gate as Koide-`Q`). It does **not** close
`delta = 2/9`; it relocates it onto that one gate.
