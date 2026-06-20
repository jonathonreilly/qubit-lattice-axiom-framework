# block01 section — CLUSTER 1: Record-Production-Dynamics Axiom (the B-AXIS sink)

**Gate:** arrow / measurement / decoherence / record-production dynamics
(`MINIMAL_AXIOMS_2026-06-05.md`'s largest open gate).
**hypothetical_axiom_status:** `"conditional on accepted new axiom; not retained
on the actual current surface."`
**Proposal note:**
[`docs/AXIOM_UPDATE_PROPOSAL_RECORD_PRODUCTION_DYNAMICS_2026-06-20.md`](../../../../docs/AXIOM_UPDATE_PROPOSAL_RECORD_PRODUCTION_DYNAMICS_2026-06-20.md)
**Runner:**
[`scripts/axiom_update_record_production_dynamics_cluster_2026_06_20.py`](../../../../scripts/axiom_update_record_production_dynamics_cluster_2026_06_20.py)
→ cache
[`logs/runner-cache/axiom_update_record_production_dynamics_cluster_2026_06_20.txt`](../../../../logs/runner-cache/axiom_update_record_production_dynamics_cluster_2026_06_20.txt)
— **TOTAL: PASS=34 FAIL=0**.
**Parent map:** [`WALL_TO_GATE_MAP.md`](WALL_TO_GATE_MAP.md) (CLUSTER 1).

---

## One line

The single-clock B-AXIS walls (N2b / N4 / N5) and the arrow share ONE sink: the
existence of record-producing dynamics; the weakest discharging primitive is one
CPTP record-production generator + a record-monotone + an orientation.

## Skeptical re-attack first (don't believe the no-gos)

- **N4 axis-LABEL is OVER-SPECIFIED for the fanout — partial crack, no axiom.**
  The ~959 B-AXIS fanout runs through `ANOMALY_FORCES_TIME_THEOREM` (~1049),
  which imports **only the count `d_t ≤ 1`** and is provably **axis-label-blind**
  (its own non-circularity text: "constrain only the count `d_t`, not which axis
  is temporal"). Runner confirms the only objects the anomaly chain reads —
  chirality `ε` and `{D_hop, ε}=0` — are EXACTLY `W`-invariant (residuals `0`).
  So the *axis label* is not in the axiom-bearing residual.
- **N5 / N2b genuinely wall (in the COUNT, not the label).** Runner recomputes:
  two commuting tensor-factor clocks survive Stone (`||H_prod−H_sum||=4.4e-16`,
  `[H_A,H_B]=0`) — N5 does not crack algebraically; `T` fixes only `τ·H` — N2b
  wall real. **N2b's dimensionful value is SK-1 (scale_reference × kinetic_isotropy),
  relocated, NOT proposed here.**
- **Genuine residual that does NOT crack:** the existence of record-producing
  dynamics at all. `H=0`/decoupled/eigenstate are exact no-record witnesses;
  Record verbatim excludes decoherence dynamics.

## Candidate primitive (UNADOPTED)

**(RP-DYN):** there exists ONE CPTP record-production generator `L` (semigroup
`e^{tL}`, `t≥0`) on system⊗environment, with a record-monotone `R` and an
orientation; for the realized state pointer coherence is monotonically suppressed
(einselection) and a durable record forms. The **registration direction** (which
lattice axis carries the produced event order) is this same object. Asserts
**existence + orientation only** — a slot, not content.

## Conditional discharges (each carries hypothetical_axiom_status)

| Wall | How it discharges given (RP-DYN) | Runner witness |
|---|---|---|
| **arrow** | `R` non-decreasing along `e^{tL}`; orientation = arrow direction; unitary step has no monotone | record proxy monotone up; reversibility contrast |
| **N5** (one clock) | one generator → one monotone record order even across two factors → single production clock | joint `|coh|` monotone under single `L` |
| **N4** (axis label) | the registration direction IS the produced event-order axis (= PIN-REG) | BC-asymmetry breaks `W` exactly (`8.0`); symmetric-BC restoration (`0`); relabeling-invariant kernel dim `0` vs `2` |
| **N2b-step** (rate) | `L` carries a rate → record half-life = the stream tick (dynamics side) | well-defined half-life for fixed `γ` |
| **record floor** | `|coh|→0` monotone in #env copies → durable broadcast record | `|coh|(N=1..64)→0` (einselection) |

## Fanout

Record-formation floor (transitively large) + ~959 (B-AXIS via the
registration-direction route) → gated path into the anomaly cap (~1049). After
the crack, the AXIOM-bearing part of the fanout is supplied by this ONE weak
existence primitive. Strength: **WEAK** (existence of einselecting dynamics;
weaker than a past hypothesis). Fanout-per-unit-strength: high (parent ranks
C2 ≈ C1 > C3).

## Minimality — does NOT grant

Past hypothesis (arrow *sign* stays open); kernel/Kraus/rate/weight; Born
weights/probability/normalization (→ CLUSTER 2); the dimensionful tick `2a_τ`
(SK-1); exclusion of commuting algebra in general (scope-boundary N6 stays open —
only a second *record-producing* stream is excluded); a fourth spatial dimension.

## Consistency with retained no-gos

Additive, contradicts none. Supplies the import named by the scope boundary (N4
construction + N5), the axis-selection no_go (PIN-REG), and the record-formation
no_go (the "separate record-production model" of its N6 partial-closure path).
Consistent with `realized_state_primitive` (supplies the dynamics slot evaluated
at the realized state; no state/measure/typicality). No boost/Lorentz/SO(4)
content.

## Skeptical re-attack outcome (one line)

The one genuine no-new-axiom re-attack (consumer-need decomposition: does the
fanout need the axis LABEL or only the count `d_t`?) **cracked** the axis-label
half of N4 for fanout purposes (anomaly chain is axis-label-blind), but the
**existence of record-producing dynamics still walls** (exact no-record
witnesses; Record excludes decoherence) — so (RP-DYN) is proposed for exactly
that residual and nothing more.
