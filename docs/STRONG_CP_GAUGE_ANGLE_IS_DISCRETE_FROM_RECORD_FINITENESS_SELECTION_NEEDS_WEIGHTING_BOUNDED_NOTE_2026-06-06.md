# The Gauge Vacuum Angle Is Record-Discrete (Finiteness Dissolves the Continuous Strong-CP Problem); the θ=0 Selection Needs a Weighting the Record Axiom Disclaims

**Date:** 2026-06-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem with an explicit boundary. **Two parts, conditional on `θ_QCD` being a recorded
quantity** (framework-native: `θ_QCD` is *not* in the three axioms — it can only be a feature of the realized
recorded vacuum sector, never a Lagrangian input). **(Half 1, derivable, no new axiom):** the Record axiom's
*finite central-sector decomposition* makes a recorded vacuum angle **discrete**, dissolving the *continuous*
strong-CP naturalness problem. **(Half 2, does not close):** selecting **θ=0** out of the finite `K`/CPT-stable
set requires a **weighting/occupancy rule**, which the Record axiom **explicitly disclaims** — so it is a separate
principle, not a corollary.
**Claim scope:** **not a strong-CP solution and not a Tier-A retirement.** Half 1 dissolves the *continuity* of
the gauge angle (the gauge-side analog of the mass-side `{0,π}` of
[`STRONG_CP_THETA_BAR_MASS_SIDE_IS_RECORD_QUANTIZED_TO_Z2_BOUNDED_NOTE_2026-06-06.md`](./STRONG_CP_THETA_BAR_MASS_SIDE_IS_RECORD_QUANTIZED_TO_Z2_BOUNDED_NOTE_2026-06-06.md)).
Half 2 is the honest seam: the residual discrete **selection** is left open, and any minimum-information /
occupancy weighting that would close it is a **genuinely new principle** outside the current Record axiom.
**Status authority:** independent audit lane only. No effective-status change; **Independent audit required.**
**Runner:** [`scripts/audit_companion_strong_cp_gauge_angle_discrete_from_record_finiteness_exact.py`](./../scripts/audit_companion_strong_cp_gauge_angle_discrete_from_record_finiteness_exact.py)

## The premise: θ is a recorded quantity, not a law input

Strong-CP is usually posed as the naturalness puzzle of a *continuous* Lagrangian parameter `θ_QCD ∈ [0, 2π)`. In
this framework there is **no `θ_QCD` in the three axioms** (Lattice, Quantum, Record). A strong-sector vacuum angle
can only appear as a property of the **realized recorded vacuum sector** — i.e. as a *record*, observable through
the neutron EDM. This note's results hold under that reading (and are vacuous under the alternative reading that
`θ_QCD` is a law parameter outside the record principle — that alternative is the genuine escape, and it is named
in the steelman).

## Half 1 — finiteness ⟹ discrete (no new axiom): the continuous problem dissolves

The Record axiom, verbatim: *"Given a readout context with a **finite central-sector decomposition** and a fixed
`K`/CPT conjugation, the realized outcome is the `K`/CPT orbit of the realized central sector."*

A continuous vacuum angle `θ ∈ [0, 2π)` is an **uncountable** family of mutually-superselected `θ`-vacua
(`⟨θ|θ'⟩ = 0` for `θ ≠ θ'`). That is **not** a finite central-sector decomposition. So a **recorded** vacuum angle
cannot be continuous — it takes **finitely many** values (runner exhibits the `Z_N` model: a finite topological
charge `Q ∈ Z_N` has the discrete dual `θ ∈ {2πk/N}`, and a genuine finite decomposition — `N` orthogonal
clock-eigen projectors summing to `I` — exists, while `[0,2π)` cannot be so covered). (Runner (1),(1b).)

**Consequence.** `θ_QCD` is **discrete**, not a continuous knob. The *continuous-naturalness* statement of the
strong-CP problem — "why is the continuous `θ̄` tuned to `≲ 10⁻¹⁰`?" — **dissolves on the recorded gauge angle**,
exactly as it did on the mass side (`arg det ∈ {0, π}`, #2932). Both halves of `θ̄ = θ_QCD + arg det` are now
record-discrete: the mass half from self-adjointness, the gauge half from the finite decomposition. The
`K`/CPT-fixed (definite-record) values are `{0}` (`N` odd) or `{0, π}` (`N` even).

## Half 2 — the θ=0 selection is NOT forced by finiteness (the honest seam)

Finiteness leaves `θ` in a finite `K`/CPT-stable set, **recorded as `K`/CPT orbits**. A **2-element** orbit
`{k, N−k}` (`k ≠ 0, N/2`) is a perfectly valid *single* record (the "one letter" reading used for the flavor
doublet). So a **nonzero** `|θ|` is record-admissible: **finiteness does not select 0.** (Runner (2).)

To pick `θ = 0` out of the finite set you must **prefer the minimal-label sector** — i.e. supply a **weighting /
occupancy rule** over sectors. A minimum-information weighting (cost = the angle's description length) uniquely
selects `θ = 0` (cost `0 < π < generic`); **without** any weighting the orbits are on equal footing and the
selection is **undetermined**. (Runner (3),(4).)

But the Record axiom's own text **explicitly disclaims exactly this**: *"A record supplies no readout context,
decomposition, `K`/CPT structure, sector-generation rule, **weighting, normalization, probability**,
measurement/decoherence dynamics, time metric, within-sector data, or **occupancy rule**."* (Runner (5).)

**Consequence.** A minimum-information / occupancy weighting that would force `θ = 0` is a **genuinely separate
principle** — it is *not* a corollary of the Record axiom; the axiom carves it out by name. It would fill the
framework's standing **no-weighting gap** (the same gap behind the unresolved Koide block-weight). This note
**does not adopt** such a principle; it only locates the seam precisely.

## What closes, what does not

| | statement | status |
|---|---|---|
| `θ_QCD` is discrete, not continuous | from the Record axiom's *finite central-sector decomposition* (θ recorded) | **derivable — no new axiom** (runner 6/6) |
| continuous strong-CP naturalness | **dissolved** (gauge-side analog of the mass-side `{0,π}`) | **derived** |
| `K`/CPT-stable values | `{0}` (`N` odd) or `{0, π}` (`N` even) | **derived** |
| selection of `θ = 0` from that set | a 2-element orbit `{k,N−k}` is a valid record ⟹ not forced by finiteness | **open** |
| a weighting/occupancy rule (e.g. minimum-information) | would select `0`, but the Record axiom **disclaims** weighting/occupancy | **separate principle, not adopted here** |
| `θ` as a law parameter (not a record) | the record principle is then vacuous on `θ` | **the genuine escape (premise-level)** |

**Net.** The gauge angle's **continuity** — the thing that makes strong-CP a *naturalness* problem — is removed by
the Record axiom's finiteness alone, with no new postulate, completing the discrete picture begun on the mass side.
What remains is a **discrete selection** (`0` vs `π` vs a nonzero orbit), and closing it to `0` requires a
weighting/occupancy rule the Record axiom **explicitly does not supply**. That is the exact, minimal additional
ingredient — named honestly rather than smuggled.

## No-go discipline / steelman

**Strongest objection (θ is a law parameter, not a record).** If `θ_QCD` is a parameter of the action rather than
a recorded vacuum property, the Record principle has no jurisdiction and **both** halves are vacuous. The
framework-native rebuttal — there is no `θ` in the three axioms, so a strong-sector angle can only be a realized
(recorded) sector property — is a genuine structural commitment, stated as this note's premise, not a theorem.
**Second objection (which discrete set?).** The `Z_N` model is an illustration; the precise finite topological
structure of the framework's gauge sector is not pinned here, only that *some* finite decomposition replaces the
continuum. **Third objection (Half 2 is the whole problem).** Granted — selecting `0` is the residual, and this
note deliberately does **not** claim to close it; it proves only that finiteness removes the *continuity* and that
the selection needs a disclaimed weighting. Both halves are reproven in the runner; the discreteness (Half 1)
stands on the axiom text regardless of Half 2.

## Forbidden-import / reprove-and-cite

All algebra (`Z_N` duality and `K`-fixed points; the existence of a finite orthogonal clock-eigen decomposition;
2-element orbits as valid records; a description-length weighting selecting `0`; the axiom's disclaimer text) is
**reproven** from finite-group / projector primitives in the runner (sympy/numpy, 6/6). Superselection-sector and
`θ`-vacuum facts (`⟨θ|θ'⟩=0`) are textbook **comparators** only. No PDG values; `θ̄ ≈ 0` named only as the target
whose *continuity* this note removes.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`STRONG_CP_THETA_BAR_MASS_SIDE_IS_RECORD_QUANTIZED_TO_Z2_BOUNDED_NOTE_2026-06-06.md`](./STRONG_CP_THETA_BAR_MASS_SIDE_IS_RECORD_QUANTIZED_TO_Z2_BOUNDED_NOTE_2026-06-06.md)
- [`STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md`](./STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md)

**Independent audit required.** This note asserts no effective-status change and changes no Tier-A registry entry.
