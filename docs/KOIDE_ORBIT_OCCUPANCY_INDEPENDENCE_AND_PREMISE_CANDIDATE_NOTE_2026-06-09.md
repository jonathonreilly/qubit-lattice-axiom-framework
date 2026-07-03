# The Koide Occupancy Atom Is Independent of the Current Checked Premise Surface; the Orbit-Occupancy Premise Candidate

**Date:** 2026-06-09
**Review-loop update:** 2026-06-12 — the four fork cells and the `rho`-map
orientation are now derived in this note's runner from explicit per-cell
integrals. The landed table remains a consistency cross-check; the fork and
sharpening citations are context accordingly.
**Claim type:** bounded_theorem
**Type:** bounded_theorem + premise-candidate proposal (proposal NOT adopted)
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_koide_orbit_occupancy_independence_2026_06_09.py`](../scripts/frontier_koide_orbit_occupancy_independence_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_koide_orbit_occupancy_independence_2026_06_09.txt`](../logs/runner-cache/frontier_koide_orbit_occupancy_independence_2026_06_09.txt)
(SCORECARD: PASS=32, FAIL=0)

> **Not claimed:** a derivation of `r = 1/2`, adoption of any premise, or a mass
> prediction. **Claimed:** the one residual atom behind the Koide `r`-gate — the
> occupancy/weight class of the generation doublet — is **independent of the
> current checked premise surface** (shown by the Record axiom's own non-supply
> clause plus two exhibited consistent models), so the present derivation loop is
> closed at this atom without adding or deriving an occupancy rule; and the
> principled premise candidate (**orbit-occupancy**) is stated with computed
> support, for owner decision — the `ξ=1` playbook.

---

## Role

The orbit-quotient sharpening
`KOIDE_R_POLARIZATION_ORBIT_QUOTIENT_GATE_SHARPENING_NOTE_2026-06-09.md`
reduced the Koide `r`-gate
to one residual atom: the slot **degree** — equivalently, at the landed fork's
bookkeeping level, the per-doublet measure-weight class
`Z_d ∈ {2π/g, π/g} ⟺ r ∈ {1, 1/2} ⟺ Q ∈ {1, 2/3}`. This note settles the
**status** of that atom.

## Result 1: the atom is not suppliable by Record — by the axiom's own clause

The landed Record axiom
([`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)) states that a
record *"supplies no readout context, decomposition, K/CPT structure,
sector-generation rule, **weighting, normalization, probability**,
measurement/decoherence dynamics, time metric, within-sector data, **or
occupancy rule**."* The doublet measure-weight class is precisely a
weighting/occupancy rule. The runner checks the clause mechanically on the live
axiom file. So Record — the axiom whose 2026-06-05 orbit refinement powers the
quotient sharpening — **declines, in its own text, to supply this atom**.

## Result 2: independence by exhibition

Two explicit models on the generation configuration `(a, b) ∈ R × C`, both
satisfying the checked constraints supplied by the current Record/Koide
bookkeeping surface — `Z₃`-equivariance, K-invariance/orbit-definedness of the
weight (so outcomes-as-orbits is respected), positivity, normalizability, and
finite additivity of the induced readout on the two-orbit outcome algebra:

```text
M_sector : one statistical slot per REAL component (a; x; y)
           doublet weight Z_d = 2π/g     (exact integral)
M_orbit  : one statistical slot per record-OUTCOME (a; b as one complex slot)
           doublet weight Z_d = π/g      (exact integral)
```

They differ **exactly** by the occupancy factor `2` — which is the fiber count
of the 2:1 sector→orbit covering (each outcome counted twice versus once).
Both consistent + the axiom's own non-supply clause ⟹ **the occupancy rule is
not supplied by the current checked premise surface.** This also mechanizes the
refuted-attempt history: every prior derivation route in this loop smuggled an
occupancy rule (the CW/fluctuation-modulus route is a sector-side occupancy
choice — supplied, never retained; refs #2624/#2688). Derivation attempts from
this surface cannot settle `r` without adding or deriving an occupancy rule; an
explicit owner-approved premise is one possible resolution.

## Consequence map — at the landed bookkeeping level only

No new microscopic bridge is invented (the #3138 lesson). The runner includes an
explicit **orientation guard**: of the two a-priori normalizations of the
`ρ`-map, the inverted one is computed and **rejected against the derived
per-model `r` values**, and the orientation (`ρ = (π/g)/Z_d`,
`r = 1/(2ρ)`) is verified from the explicit per-cell integrals. The landed
table remains only a consistency cross-check:

```text
M_sector  →  ρ = 1/2  →  r = 1    →  Q = 1      (the real/2-slot cell)
M_orbit   →  ρ = 1    →  r = 1/2  →  Q = 2/3    (the holomorphic/1-slot cell)
```

Convention-free core fact: `r_sector / r_orbit = Z_sector / Z_orbit = 2`
exactly — the cell ratio *is* the occupancy factor, independent of any
normalization choice.

## The premise candidate: orbit-occupancy (proposal; NOT adopted)

> **Orbit-occupancy:** record statistics assigns one statistical slot per
> record-**outcome** (K/CPT orbit), not per central sector.

Computed support:

- **Granularity matching (unique among the two exhibited slot choices):** the
  orbit model is the only exhibited choice whose statistical slot-groups biject
  with the record-outcomes (2 = 2); the sector model carries 3 slots against 2
  outcomes. "Statistics grained at the granularity of outcomes" is the
  readout-side analogue of the approved `kinetic_isotropy_primitive`'s "tick
  grained like edge" — dimensionless, structural, binary, no fitted number.
- **Comparator (labeled, never an input):** the empirical charged-lepton Koide
  ratio `Q_PDG = 0.666661` sits on the orbit-occupancy cell (`2/3`) to
  `6×10⁻⁶`; the sector-occupancy cell (`Q = 1`) is excluded empirically by
  ~50%.
- **Payoff if approved (stated as the proposal's consequence, not a result):**
  with orbit-occupancy, `r = 1/2` and `Q = 2/3` follow from the landed
  `Q = (1+2r)/3` lever — the Koide relation becomes the statement that nature's
  record statistics counts outcomes, not sectors. The phase `δ` remains a
  separate admission (the radian-period note).

Per the independence result, this is **owner-decision territory** — exactly the
`ξ=1` situation: the premise is not supplied by the current checked premise
surface, both horns are consistent, and one honest resolution is an explicit
structural choice rather than an eighth derivation attempt.

## No-go discipline gate

- **N1 Route enumeration:** Record non-supply is ATTEMPTED and stops at the
  axiom's explicit "no occupancy rule" clause; sector occupancy is ATTEMPTED
  and gives a consistent `r = 1` horn; orbit occupancy is ATTEMPTED and gives a
  consistent `r = 1/2` horn but remains proposed, not adopted; the prior
  CW/fluctuation-modulus route is RULED OUT BY PRIOR as supplied sector-side
  occupancy context; the derived `rho`-orientation check is ATTEMPTED and
  orients the map but selects no horn; the PDG comparator is ATTEMPTED only as
  labeled non-input support; the future-larger-premise route is left OPEN.
- **N2 Wall independence:** the common wall is the missing occupancy/weighting
  rule; the two exhibited models agree on the checked constraints and differ
  only at that wall.
- **N3 Hidden-wall scan:** no readout context, weighting, probability,
  normalization, dynamics, phase, mass input, or empirical value is introduced as
  a premise.
- **N4 Residual matching:** the residual atom is exactly the sector-versus-orbit
  slot count, with ratio `2`.
- **N5 Rhetoric audit:** the claim is current-surface independence, not a
  universal future no-go and not a derivation of `r = 1/2`.
- **N6 Partial closure:** the live continuation is either an owner-approved
  orbit-occupancy premise or a later derivation from additional theory.
- **N7 Steelman:** a larger retained premise surface could still derive the
  orbit-occupancy rule; this note does not block that route.
- **N8 Cross-cycle echo:** prior failed Koide `r` routes are treated only as
  refuted-route context, not as evidence that the proposed premise is adopted.

## What this note does NOT claim

- **Not** a derivation of `r = 1/2`; **not** adoption of orbit-occupancy; **not**
  a charged-lepton mass prediction.
- **Not** a universal route-closure claim: no claim is made that a future
  larger premise surface cannot derive the occupancy rule. The independence is
  relative to the **current checked** Record/Koide bookkeeping surface,
  witnessed by the exhibited models and the axiom's own clause.
- **Not** a new microscopic moment-bridge: all cell assignments pass through the
  explicit per-cell integrals and derived `ρ`-map identity; the landed table is
  kept only as a consistency cross-check.
- **No** PDG/fitted input in any derivation step (PDG `Q` is a labeled
  comparator); **no** new axiom, primitive, vocabulary, or class tag is added by
  this note (the candidate is *proposed*, with approval routed through
  `AXIOM_MINIMALITY_POLICY.md` §6 exactly as for the kinetic-isotropy primitive).
- It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner): the orbit partition (`K(e₁)=e₂`); the four fork
  cells (partition weights AND equipartition `r` per model) derived from
  explicit integrals; the `ρ`-map `r = 1/(2ρ)` verified as a derived identity;
  the landed table kept as a consistency cross-check; the `Q`-lever (100 draws);
  the exact weights `2π/g` and `π/g` and their factor-2 fiber interpretation;
  the two models' checked constraint-consistency; the mechanical axiom-clause
  check; the convention-free cell ratio; the slot/outcome counting; the PDG
  comparator arithmetic.
- **Cited:** [`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
  (the `E_s = 3a^2`, `E_d = 6|b|^2` lever used by the equipartition
  derivation); [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  (the non-supply clause and the orbit wording);
  [`AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md) §6 (the
  approval mechanism the proposal would route through); the refuted-route corpus
  (#2624, #2688, #3138) as non-re-walk boundaries.

**Context (not load-bearing: backticked names are context, not dependency
edges):**

- `KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md` — where the
  four-cell mechanism landed (open-gate row); the cells are recomputed from
  explicit per-cell actions in this note's runner, and the landed table is
  consumed only as a consistency cross-check.
- `KOIDE_R_POLARIZATION_ORBIT_QUOTIENT_GATE_SHARPENING_NOTE_2026-06-09.md` —
  the reduction history (how the r-gate narrowed to this atom); framing only, no
  content consumed.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
