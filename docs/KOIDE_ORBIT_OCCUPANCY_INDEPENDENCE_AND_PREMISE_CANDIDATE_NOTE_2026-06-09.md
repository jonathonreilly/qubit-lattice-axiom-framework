# The Koide Occupancy Atom Is Independent of the Current Premise Surface; the Orbit-Occupancy Premise Candidate

**Date:** 2026-06-09
**Claim type:** bounded_theorem (independence by exhibition + the axiom's own boundary clause) + a premise-candidate proposal (NOT adopted)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.
**Primary runner:**
[`scripts/frontier_koide_orbit_occupancy_independence_2026_06_09.py`](../scripts/frontier_koide_orbit_occupancy_independence_2026_06_09.py)
**Cached runner output:**
[`logs/runner-cache/frontier_koide_orbit_occupancy_independence_2026_06_09.txt`](../logs/runner-cache/frontier_koide_orbit_occupancy_independence_2026_06_09.txt)
(SCORECARD: PASS=24, FAIL=0)

> **Not claimed:** a derivation of `r = 1/2`, adoption of any premise, or a mass
> prediction. **Claimed:** the one residual atom behind the Koide `r`-gate — the
> occupancy/weight class of the generation doublet — is **independent of the
> current premise surface** (shown by the Record axiom's own non-supply clause
> plus two exhibited consistent models), so the multi-attempt derivation loop is
> structurally closed; and the principled premise candidate (**orbit-occupancy**)
> is stated with computed support, for owner decision — the `ξ=1` playbook.

---

## Role

The orbit-quotient sharpening (`KOIDE_R_POLARIZATION_ORBIT_QUOTIENT_GATE_SHARPENING_NOTE_2026-06-09.md`,
plain-text context reference, in review as PR #3397) reduced the Koide `r`-gate
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
satisfying **every** constraint the axioms impose — `Z₃`-equivariance,
K-invariance/orbit-definedness of the weight (so outcomes-as-orbits is
respected), positivity, normalizability, and finite additivity of the induced
readout on the two-orbit outcome algebra:

```text
M_sector : one statistical slot per REAL component (a; x; y)
           doublet weight Z_d = 2π/g     (exact integral)
M_orbit  : one statistical slot per record-OUTCOME (a; b as one complex slot)
           doublet weight Z_d = π/g      (exact integral)
```

They differ **exactly** by the occupancy factor `2` — which is the fiber count
of the 2:1 sector→orbit covering (each outcome counted twice versus once).
Both consistent + the axiom's own non-supply clause ⟹ **the occupancy rule is
an irreducible input on the current premise surface.** This also mechanizes the
refuted-attempt history: every prior derivation route smuggled an occupancy rule
(the CW/fluctuation-modulus route is a sector-side occupancy choice — supplied,
never retained; refs #2624/#2688). Derivation attempts from the current surface
cannot settle `r`; only an explicit premise can.

## Consequence map — at the landed bookkeeping level only

No new microscopic bridge is invented (the #3138 lesson). The runner includes an
explicit **orientation guard**: of the two a-priori normalizations of the landed
`ρ`-map, the inverted one is computed and **rejected against the landed table**,
and the landed orientation (`ρ = (π/g)/Z_d`, `r = 1/(2ρ)`) is verified to
reproduce the landed cells exactly:

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

- **Granularity matching (unique):** the orbit model is the only choice whose
  statistical slot-groups biject with the record-outcomes (2 = 2); the sector
  model carries 3 slots against 2 outcomes. "Statistics grained at the
  granularity of outcomes" is the readout-side analogue of the approved
  `kinetic_isotropy_primitive`'s "tick grained like edge" — dimensionless,
  structural, binary, no fitted number.
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
`ξ=1` situation: the premise is provably not derivable, both horns are
consistent, and the honest resolution is an explicit structural choice rather
than an eighth derivation attempt.

## What this note does NOT claim

- **Not** a derivation of `r = 1/2`; **not** adoption of orbit-occupancy; **not**
  a charged-lepton mass prediction.
- **Not** a broad no-go ("no future route can derive the occupancy rule from a
  *larger* premise surface" is not claimed — the independence is relative to the
  **current** axioms + retained set, witnessed by the exhibited models and the
  axiom's own clause).
- **Not** a new microscopic moment-bridge: all cell assignments pass through the
  landed `ρ`-map with the orientation pinned by the landed table.
- **No** PDG/fitted input in any derivation step (PDG `Q` is a labeled
  comparator); **no** new axiom, primitive, vocabulary, or class tag is added by
  this note (the candidate is *proposed*, with approval routed through
  `AXIOM_MINIMALITY_POLICY.md` §6 exactly as for the kinetic-isotropy primitive).
- It does **not** set or change any audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner): the orbit partition (`K(e₁)=e₂`); the landed
  four-cell table cross-check; the `Q`-lever (100 draws); the exact weights
  `2π/g` and `π/g` and their factor-2 fiber interpretation; the two models'
  full constraint-consistency; the mechanical axiom-clause check; both `ρ`-map
  orientations with the landed-table arbitration; the convention-free cell
  ratio; the slot/outcome counting; the PDG comparator arithmetic.
- **Cited:** [`KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md`](KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md)
  (the landed cells + `ρ` bookkeeping);
  [`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
  (the lever); [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  (the non-supply clause and the orbit wording);
  [`AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md) §6 (the
  approval mechanism the proposal would route through); the refuted-route corpus
  (#2624, #2688, #3138) as non-re-walk boundaries.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. The independent audit lane is the only status authority.
