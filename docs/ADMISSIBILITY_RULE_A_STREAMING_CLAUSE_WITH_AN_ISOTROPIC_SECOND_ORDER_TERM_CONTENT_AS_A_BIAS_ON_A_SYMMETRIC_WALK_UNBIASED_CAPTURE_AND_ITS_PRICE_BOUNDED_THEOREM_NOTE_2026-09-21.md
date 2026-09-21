---
claim_id: admissibility_rule_a_streaming_clause_with_an_isotropic_second_order_term_content_as_a_bias_on_a_symmetric_walk_unbiased_capture_and_its_price_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN a supplied variant of the inertial clause of block 44 (PR #8550), sphere menu: the BIASED WALK, in which a record of content s hops to x + e, for each of the six lattice directions e, at the rate (alpha + c s.e)/2 with alpha >= c > 0 (block 44's clause is c max(0, s.e): forward hops only); nothing adopted. (T1) The biased walk has first moment c s and second moment alpha delta_kl whatever the content; any non-negative axis-hop law with first moment c s has a second moment along axis k of at least c |s_k|, with equality only for forward hops, so a second moment that does not depend on the content is at least c: the biased walk with alpha = c is the least diffusive such clause. (T2) On fields of degree two its streaming operator is exactly -c s.grad + (alpha/2) Laplacian: the second-order term is the same for every content and isotropic; in local equilibrium the momentum equation gets (alpha/2) Laplacian g_i and no part of cubic symmetry, so the potential inflow of blocks 45 and 46 meets no viscous stress at this order and the defect found in block 51 (PR #8563) is absent; the lattice returns at fourth order in gradients. (T3) A site captures every content at the rate 3 alpha, and a body of any shape at alpha/2 per exposed face: captured records are a fair sample of the gas whatever its content law, which is what block 45's T5 had wrongly assumed of the forward clause (block 48, PR #8558). (T4) With exchange of contents on occupied targets every hop has a predecessor of the same rate, the uniform measure is stationary, and number and momentum are conserved event by event (checked for two and three records on the 3x3x3 torus); not so if a blocked hop does nothing. (T5, the price) a record hops against its content the share (3 alpha - c |s|_1)/(6 alpha) of the time when no component vanishes, between (3 - sqrt 3)/6 and 1/3 at alpha = c, and a record along an axis makes two hops in three sideways: the content is a bias on a walk, not a direction of travel. EXECUTED, NOT CLAIMED (one capturing body of about 22 sites, side 64, density 0.1, gamma 2, eight seeds, r from 6 to 10; inward momentum density times r^2 over the capture rate within 15 degrees of the axes / face diagonals / body diagonals): under the biased walk 0.2563 +- 0.0035, 0.2531 +- 0.0034, 0.2548 +- 0.0034 (ratio of axes to body diagonals 1.006 +- 0.019; isotropic closure 3/(4 pi (1 - rho)) = 0.2653), where block 51's forward clause gave 0.1754, 0.1485, 0.1304 (ratio 1.35 +- 0.03) at the same density and scattering rate. NOT claimed: isotropy beyond second order in gradients, a hydrodynamic limit, forces between bodies under this clause, that the clause is the framework's, any gravitational statement, any adoption."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_a_streaming_clause_with_an_isotropic_second_order_term_content_as_a_bias_on_a_symmetric_walk_2026_09_21.py
---

# A streaming clause with an isotropic second-order term: content as a bias on a symmetric walk, unbiased capture, and its price

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements about a supplied variant of a supplied clause; one wind by direction executed, not claimed; nothing adopted or registered; unaudited)

This note works within a supplied variant of the inertial clause of block 44; it reports a streaming clause whose second-order term is isotropic, what it restores and what it costs; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 51 (PR #8563) found that the wind of a capturing body is not the same in every direction of the lattice, and traced it to block 44's streaming rule: a record hops *forward only*, along the lattice axes on which its content has a positive component, and the second-order term of that rule depends on the content. Block 51 named, as a route it had not worked, a rule with an isotropic second-order term. This note works it.

1. **The clause.** Let a record of content `s` hop to each of its six neighbours `x + e` at the rate `(α + c s·e)/2`, `α ≥ c`: a symmetric walk biased by the content. Its mean displacement is `c s` and its second moment is `α δ_kl`, *whatever the content* (T1).
2. **It is the least one can do.** Any rule that hops along axes with mean displacement `c s` has a second moment of at least `c|s_k|` along axis `k`, and only forward hops reach it; so block 44's rule is the least diffusive of all, and a second moment that does not depend on the content costs at least `α = c` (T1).
3. **What it restores.** The streaming operator is exactly `−c s·∇ + (α/2)∇²` on fields of degree two: the second-order term is isotropic, the viscous term has no part of cubic symmetry, and a potential inflow meets no viscous stress at this order (T2). A site, and a body of *any* shape, captures every content at the same rate: captured records are a fair sample of the gas (T3) — what block 45 had assumed and block 48 found false for forward hops. The uniform measure stays stationary and number and momentum stay conserved (T4).
4. **What it costs.** A record no longer travels along its content. At `α = c` a record whose content lies along an axis makes one hop in three forwards and two in three sideways; one along a body diagonal makes a fifth of its hops backwards (T5). The content is a bias on a walk.
5. **Executed.** The wind of one capturing body by direction, at the density and scattering rate at which block 51 found the ratio of axes to body diagonals `1.35 ± 0.03` for forward hops: under the biased walk the three classes are `0.2563, 0.2531, 0.2548` (each `± 0.0035`), ratio `1.006 ± 0.019`.

So the defect of block 51 is a property of forward-only hopping and not of inertia as such; it can be removed at second order in gradients, at the price of a record that mostly does not move the way it points. The defects found in blocks 48 and 49 (a capturing body is carried, not accelerated; the pull is the body's growth) do not depend on the streaming rule and remain.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 51 (PR #8563), N1 route 2: 'a clause with isotropic second-order streaming ... Not worked'"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "an isotropic second-order streaming term exists at the price alpha >= c; next: the force between capturing bodies by direction under this clause, the fourth-order terms, and the owner's judgement on whether a content that only biases a walk is still a record's direction of travel"
conditional_surface_status: "T1, T2, T3, T5 exact for the clause; T4 checked for two and three records on the 3x3x3 torus and argued in general; the wind by direction (floating point; side 64; eight seeds) is in the control and not claimed"
hypothetical_axiom_status: "the biased-walk variant of block 44's inertial clause (scattering re-draws contents as there) and the capture of records by bodies; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full) is used through "A site never carries more than one record; records are permanent." Block 01 (on `main`, proposed and unaudited) supplies the menus. Blocks 44, 45, 48 and 51 (open PRs #8550, #8553, #8558, #8563) supply the forward clause, the wind law's closure, the capture law of forward hops and the viscous term of cubic symmetry. They are restated; the runner re-derives what it uses.

- **Forward clause (block 44).** Rate `c·max(0, s·e)` to the neighbour `x + e`, `c = 1/√3`.
- **Biased walk (supplied here).** Rate `(α + c s·e)/2` to each of the six neighbours, `α ≥ c > 0`. An empty target is entered; an occupied target exchanges contents with the record; a capturing site keeps the record; bonds re-draw their two contents on the momentum class as in block 44. The control uses `α = c = 1/3` (probability `(1 + s·e)/6` per attempt).
- **Moments of a hop law.** First moment `Σ_e a(s, e) e`; second moment `Σ_e a(s, e) e_k e_l`.

Replacing forward differences by symmetric ones plus a diffusion is the oldest device for removing the directional error of a transport scheme on a grid (Courant, Friedrichs, Lax); the isotropy of fourth-rank moments is the classical requirement on lattice gases (Frisch, Hasslacher and Pomeau). None is used as authority.

## Prior art and what is new

The device is classical in numerical transport. What is new is its statement inside the campaign's clause: the lower bound `c|s_k|` that makes block 44's forward rule the least diffusive, the price `α ≥ c` of a content-independent second moment, the unbiased capture by a body of any shape, the stationarity of the uniform measure under exchange, and the shares of hops that no longer follow the content.

## Exact target and obligation graph

Target: a streaming clause with mean displacement along the content whose second-order term is isotropic; what it restores and what it costs. Obligations: (O1) the clause and its minimality; (O2) the streaming operator; (O3) the capture law; (O4) stationarity and conservation; (O5) the price. T1–T5 discharge them; the control executes the wind by direction.

## Theorem T1 — moments, and the least diffusion

For the biased walk, `Σ_e a(s, e) = 3α`, `Σ_e a(s, e) e = c s`, and `Σ_e a(s, e) e_k e_l = α δ_kl`, because the two hops along an axis have the rates `(α ± c s_k)/2`, whose difference is `c s_k` and whose sum is `α`. The rates are non-negative for every unit content exactly when `α ≥ c`.

Let `a` be any non-negative law of hops along the axes with first moment `c s`. Along axis `k`, `a₊ − a₋ = c s_k` and `a₊, a₋ ≥ 0` give `a₊ + a₋ ≥ c|s_k|`, with equality exactly when the hop against `s_k` has rate zero. So the second moment along axis `k` is at least `c|s_k|`, and only forward hops reach it. A second moment that is the same for every content must dominate `c|s_k|` for the contents along the axes, so it is at least `c`. ∎

## Theorem T2 — the streaming operator is isotropic at second order

For a field of degree two, `f(x − e) − f(x) = −e·∇f + ½(e·∇)²f` exactly. Summing with the rates of T1 gives `−c s·∇f + (α/2)∇²f`. The second-order term carries no content. In local equilibrium it gives the number equation `(α/2)∇²n` and the momentum equation `(α/2)∇²g_i`; there is no term `∂_i²g_i`. For a potential flow `g = ∇χ`, `∇²χ = 0`, the viscous term vanishes identically, so the potential inflow solves the creeping equations with uniform pressure: block 51's T3 has no counterpart here. ∎

The expansion continues: at fourth order the hops of one lattice step bring `∂_k⁴`, which has cubic symmetry only. Its effect on a flow of scale `r` is smaller than the second-order term by the square of the lattice step over `r`; it is a near-field effect, unlike the defect of block 51, which has no scale.

## Theorem T3 — capture is unbiased, for a body of any shape

A record at the neighbour `x − e` of a capturing site hops onto it at the rate `a(s, e)`. Summed over the six neighbours the site captures the content `s` at the rate `3α`, the same for every content. For a body, a face with outward normal `n` is entered by hops along `−n`, at the rate `(α − c s·n)/2`; a finite body has as many faces with normal `n` as with `−n`, so the parts that depend on the content cancel and the body captures every content at `α/2` per exposed face. Captured records are therefore a fair sample of the gas, whatever its content law and whatever the body's shape, and a body takes up the mean momentum of the gas times its capture rate. For the two contents `(1,0,0)` and `(−3/5,−4/5,0)` of block 48's witness the captured mean is the gas mean `(1/5, −2/5, 0)`, where forward hops gave `(1/15, −7/15, 0)`. ∎

## Theorem T4 — the uniform measure is stationary; number and momentum are conserved

Let a hop onto an occupied target exchange the two contents. Then for every configuration, every record at `x` with content `s` and every direction `e`, there is exactly one predecessor event that produces it, and its rate is `a(s, e)`: if `x − e` is empty, the same record one site back hopping along `e`; if it is occupied, the configuration with the two contents exchanged, in which the record at `x − e` carries `s` and hops along `e` onto an occupied target. The flow into a configuration is therefore `3α` per record, which is the flow out of it, and the uniform measure is stationary. Hops move contents or exchange them, so the number of records and the sum of their contents are conserved event by event. If a blocked hop did nothing instead, the flow out would lack `a(s, e)` and the flow in would lack `a(s, −e)`, which differ. ∎

## Theorem T5 — the price

For a content with no vanishing component the hops against it have the total rate `Σ_k(α − c|s_k|)/2 = (3α − c|s|₁)/2`, a share `(3α − c|s|₁)/(6α)` of all its hops: at `α = c`, from `(3 − √3)/6 ≈ 0.21` on a body diagonal towards `1/3` near an axis. For a content along an axis no hop is against it, but the four sideways hops have the rate `α/2` each: two hops in three are across the content. In every case the record's mean velocity is `c s` and its position spreads as `√(αt)` about it: over a time `t` the travel along the content exceeds the spread only when `t` is large against `α/c²`. ∎

## Executed: the wind of one capturing body by direction, under the biased walk (not proved)

Control `specs/supervisor_control_block52_wind_by_direction.py` (the control of block 51 with the streaming rule replaced by the biased walk at `α = c = 1/3`, that is, probability `(1 + s·e)/6` per attempt for each neighbour; one capturing body, a ball of radius 3 filled to `0.18`, about 22 sites; open box of side 64 with a reservoir at the walls; `ρ = 0.1`, `γ = 2`; eight seeds of 20000 ticks; `r` from 6 to 10).

| clause | axes | face diagonals | body diagonals | axes over body diagonals | isotropic closure |
|---|---|---|---|---|---|
| biased walk | `0.2563 ± 0.0035` | `0.2531 ± 0.0034` | `0.2548 ± 0.0034` | `1.006 ± 0.019` | `3/(4π(1 − ρ)) = 0.2653` |
| forward hops (block 51) | `0.1754 ± 0.0017` | `0.1485 ± 0.0017` | `0.1304 ± 0.0021` | `1.35 ± 0.03` | `√3/(4π(1 − ρ)) = 0.1531` |

Under the biased walk the three classes agree within their errors and lie at `0.95` to `0.97` of the isotropic closure. The capture rate is `0.57` of the kinetic value `ρ` per site: a gas that diffuses this strongly is depleted next to a body more than block 44's gas is.

## No-Go Discipline Gate

The note's negative sentences: no axis-hop clause with mean displacement `c s` has a content-independent second moment below `c`; under the biased walk a record does not travel along its content; isotropy is restored at second order in gradients only.

### N1 — Routes by which the sentences could fail
1. *Hops to more neighbours* — with face- and body-diagonal neighbours the bound of T1 changes (a hop along a diagonal has components along several axes); a clause with less diffusion and an isotropic fourth-rank moment may exist there. Not worked.
2. *A second moment that depends on the content isotropically* — `αδ_kl + β s_k s_l` has an isotropic fourth-rank moment too, but axis hops give a diagonal second moment, so `β = 0` is forced with six neighbours.
3. *Fourth order* — the terms `∂_k⁴` have cubic symmetry; they fall off with distance and are not computed.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
T2's statement about the momentum equation is in local equilibrium at small density, as in block 51. T4 is checked in the two- and three-record sectors; the pairing argument is general.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | one record per site; permanence | yes (premise) |
| block 01 (`main`) | the menus | yes (premise, proposed) |
| block 44 (open PR #8550) | the forward clause, the exchange rule, the scattering | yes (restated; varied) |
| block 51 (open PR #8563) | the defect this clause removes | yes (restated) |
| blocks 45, 48 (open PRs #8553, #8558) | the unbiased-sample argument and its failure for forward hops | placement |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "moments `c s` and `αδ`; the bound `c|s_k|`; operator `−c s·∇ + (α/2)∇²`; capture `3α` per site and `α/2` per face; uniform measure stationary; shares of hops against and across" | executed: rates and moments for 150 rational unit contents; the bound and its attainment | executed: capture by a site, a cube, a plate and a ball; the two-content witness | not applicable | executed: the operator on fields of degree two; the balance of flows at 1755 two-record configurations; the shares of hops | T1–T3, T5 exact for the clause; T4 checked at two and three records and argued in general; fourth-order terms not computed; the wind executed only |

### N6 — Partial-closure paths and primitive scan
The registered `kinetic_isotropy_primitive` grants only a structural isotropy of a kinetic form and supplies no streaming rule; it is not used. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "You have repaired the isotropy by turning inertia into diffusion." Reply: that is the content of T1 and T5, stated as a price: with hops along axes, a content-independent second moment cannot cost less than `α = c`, and then between a fifth and two thirds of a record's hops do not follow its content. Whether such a record still "travels along its content" is the owner's question. Second objection: "Then block 51's defect was an artefact of a bad discretisation." Reply: block 44's rule is not a discretisation of anything; it is the clause in which a record moves only the way it points, and T1 shows it is the least diffusive rule there is. The defect is what that strictness costs on a cubic lattice.

### N8 — Cross-cycle echo
Block 45 left the six-axis menu for the sphere menu to gain isotropy of contents; block 51 found the lattice again in the hops; this block removes it from the hops at second order and finds it again at fourth. Each step has bought isotropy at one order by giving up some of what made the carrier ballistic, which block 43 had found it needs.

## Falsifiers

- A unit content for which the biased walk's first moment is not `c s` or its second moment not `αδ`; a non-negative axis-hop law with first moment `c s` and a second moment below `c|s_k|` along some axis.
- A body whose capture rate under the biased walk depends on the content.
- A two- or three-record configuration at which the flows of the uniform measure do not balance.
- For the executed part: a wind by direction under the biased walk whose three classes differ by more than their errors at distances where the walls do not matter.

## Boundaries and non-claims

One value of `α` (`α = c`), one density and one scattering rate executed. Isotropy is claimed at second order in gradients only. Forces between bodies under this clause are not executed. The clause is a variant of a supplied clause and is not proposed for adoption; whether a content that only biases a walk is a record's direction of travel is left to the owner. Blocks 48 and 49's findings (a capturing body is carried; the pull is tied to growth) do not depend on the streaming rule. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the sentence quoted under Premises. Block 01 (on `main`): the menus; proposed, unaudited. Blocks 44, 45, 48, 51 (PRs #8550, #8553, #8558, #8563, open): restated, varied or placed.
- Named standard imports at definition level: the expansion of a difference to second order, exact on polynomials of degree two; stationarity as the balance of flows.
- Reference only: Courant, Friedrichs and Lax for symmetric differences with added diffusion; Frisch, Hasslacher and Pomeau for the isotropy of fourth-rank moments.

## Review record
Supervisor-run block of the 12-hour campaign, the last one. Lens: block 51's N1 named a rule with isotropic second-order streaming as an unworked route; the second moment of a hop law is a sum of two rates and its first moment their difference, so the whole question is one inequality per axis. The theorems were written and the prediction made (equal winds in the three direction classes) while the control ran; the control agrees (`1.006 ± 0.019`). Refuting pass (`specs/supervisor_control_block52_refuter.py`, machinery disjoint from the runner's): W1 the moments with a symbolic content; W2 the streaming operator expanded symbolically; W3 a Monte Carlo of the captures of one site in a gas of two contents (biased walk: the gas mean; forward hops: block 48's biased mean); W4 three records of distinct rational contents on the `3×3×3` torus, all 17550 ordered configurations, flows balanced; W5 the share of hops against the content. All pass. Two findings folded, both the campaign's standing one: an empty `sum()` and a quotient of two Python integers each produced a floating-point number inside an exact check (runner E2, refuter W5); both now start from exact numbers. One mutation did not bite as first written (it restored the right value by construction) and was rewritten. Mutation census: 8 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_a_streaming_clause_with_an_isotropic_second_order_term_content_as_a_bias_on_a_symmetric_walk_2026_09_21.py
```

Expected: `TOTAL: PASS=13 FAIL=0`.
