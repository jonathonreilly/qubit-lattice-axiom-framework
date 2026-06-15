# W8a Statistics Atom Reduces To Product Form Under A Supplied Product Instance

**Date:** 2026-06-12
**Claim type:** bounded_theorem / bounded support under a supplied product-form joint instance
**Status:** source proposal under supplied product-form joint instance; independent audit required.
**Status authority:** independent audit lane. This source note does not set,
predict, promote, or demote any audit outcome and does not edit audit-owned
registry, ledger, queue, or publication-status surfaces. The
`bounded_theorem` label is a source-side claim-boundary declaration, not an
audit verdict.
**Primary runner:** `scripts/frontier_statistics_atom_reduces_to_product_form_2026_06_12.py`
**Runner cache:** `logs/runner-cache/frontier_statistics_atom_reduces_to_product_form_2026_06_12.txt`

## 2026-06-15 audit-boundary repair: product-form is a supplied bounded premise

This repair makes the non-retained input explicit. The retained
Gleason/Busch surface supplies the one-copy Born form. It does **not** supply
physical independence, iid repetition, or a product-form joint registration
law. The product object `sigma tensor sigma` is therefore a row-local supplied
bounded premise, not a retained theorem and not an axiom.

The source claim is correspondingly narrow:

- K1 restates the retained Born form on the supplied two-outcome partition.
- K2 derives product weights after the registered pair is **supplied** as the
  product instance `sigma tensor sigma`.
- K3 rederives the agreement-conditioned sharpening flow under that supplied
  product instance.
- K4 reduces the wave-8a statistics atom to one named premise: repeated
  registrations are carried by product-form instances of the registered
  surface.

This note does **not** discharge the product-form premise, does not assert
iid/product composition as a physical fact, does not adopt R-D, does not select
an occupancy cell, does not fix `r`, and does not import probability beyond the
retained Gleason/Busch surface. The Born form here is the cited retained
authority, not a new rule. For firewall clarity: the product-form premise is
the supplied bounded premise for this row; it is named, not derived or
retained. R-D stays proposed; no occupancy cell is selected; `r` is never
fixed; the occupancy binary stays open.

## Boundary

This note proves K1-K4 only in the bounded setting above: retained one-copy
Born authority plus a supplied product-form joint instance.

## The Retained Surface

The Gleason note supplies the retained projection-lattice surface:

> "It applies the standard Gleason theorem (1957, refined by various authors)
> to the framework's specific Hilbert space `H_Λ = ⊗_{x ∈ Λ} ℂ²` for finite
> `Λ ⊂ Z^3` with `|Λ| ≥ 2`."

It also records the Born-form readout on that lattice:

> "Reading off Born form `p(P) = Tr(σ P)` as the unique probability measure on
> the qubit-lattice projection lattice."

The Busch/CFMR bridge supplies the retained qubit-effect surface:

> "Then there is a **unique density matrix** `σ ∈ M_2(C)` (`σ = σ†`, `σ ≥ 0`,
> `Tr σ = 1`) with `m(E) = Tr(σ · E)` for every `E ∈ E(M_2)`."

The minimal axiom memo keeps this from being smuggled in as an axiom-level
probability rule:

> "This axiom supplies the one-site algebraic carrier. It does not supply a
> dynamics, composition theorem beyond the named lattice placement, measurement
> instrument, Born rule, species identification, gauge group, particle content,
> or physical observable bridge."

## Theorem

**K1 — retained Born form.** On the retained Gleason/Busch surface, Gleason's
theorem applied to the framework's `H_Lambda = tensor C^2` projection lattice
and the Busch/CFMR effect-valued result `m(E) = Tr(sigma E)` force every
finitely additive weight assignment on the supplied two-outcome partition into
Born form. This is consumed as cited retained authority; the form is restated,
not re-proven. **[check K1]**

For a partition `{P_s, P_d}` with `P_s + P_d = I`, the retained form gives
`p_s = Tr(sigma P_s)`, `p_d = Tr(sigma P_d)`, and
`p_s + p_d = Tr(sigma) = 1`. Positivity of `sigma` and of the projectors gives
`p_s, p_d in [0,1]`.

**K2 — product composition from the supplied joint instance.** For two
registrations carried by a supplied product instance `sigma tensor sigma` on
the joint lattice, with the product partition `{P_j tensor P_k}`, the same
Born form on the joint algebra gives

```text
m(P_j tensor P_k)
  = Tr((sigma tensor sigma)(P_j tensor P_k))
  = Tr(sigma P_j) Tr(sigma P_k)
  = p_j p_k.
```

Thus multiplicative weights are no longer an additional algebraic premise
*after* the product-form joint instance has been supplied: they are the retained
Born form evaluated on that supplied product object.
The runner verifies the trace-tensor lemma symbolically on the supplied
two-sector surface with generic `sigma`. **[check K2]**

**K3 — the flow follows.** Agreement-conditioning the joint weights keeps the
`(s,s)` and `(d,d)` cells and renormalizes:

```text
p_i' = p_i^2 / (p_s^2 + p_d^2).
```

For the outcome ratio `x = p_d / p_s`, this sends `x` to `x^2`. With
`x = 2r`, the bounded wave-8a records-flow coordinate obeys, under the
supplied product-form joint instance,
`r -> 2r^2`; its inverse direction is `r -> sqrt(r/2)`, the thermalizing map.
The wave-8a G2 identification is reproven inline here as this ratio
calculation. **[check K3]**

**K4 — the atom reduced.** The wave-8a statistics atom, "repeated registration
composes independently on the weight bookkeeping," therefore reduces to the
single product-form premise:

```text
repeated registrations are carried by product-form instances
(sigma tensor sigma) of the registered surface.
```

That premise is named, not discharged. Its framework home is the record-stack
stationarity/independence residual of the unraveling lane, especially
`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`
and
`UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md`.
Everything else in this row's R-D algebraic reduction is derived from retained
Born authority once that premise is supplied. The physical product-form premise
itself remains open outside this bounded row. **[check K4]**

The runner also checks a correlated joint-state witness:
`rho_corr = p_s P_s tensor P_s + p_d P_d tensor P_d`. It has the same one-copy
weights but `m(P_s tensor P_d) = 0 != p_s p_d` generically, and
agreement-conditioning gives the identity update `p_i' = p_i`. This witness is
the control showing that the product-form premise does real work.

## Consequence

After this note, the occupancy lane's open content is:

- the product-form premise, named as a supplied bounded premise with the record-stack
  stationarity/independence home above;
- the outcome dictionary, the wave-9 tri-guise binary;
- the durability-to-weight coupling.

Each item is named; none is selected here. The route remains live.

## Does Not

- This does not assert iid/product composition as a physical fact.
- This does not discharge, retain, or physically select the product-form premise.
- This does not adopt R-D or any R-D bridge premise.
- This does not select the wave-9 tri-guise outcome dictionary.
- This does not select any occupancy cell and does not fix `r`.
- This does not promote the wave-8a anatomy note, the separatrix note, the
  thermalizing note, the unraveling notes, or the R-D chain note.
- This does not add a new probability axiom beyond the retained
  Gleason/Busch authority.

## Context

Context only, backticked and not link-bearing: `wave-8a anatomy note` (in
review; its G2 identification is reproven inline above),
`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`,
`FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md`,
`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`,
`UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md`,
and `KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`.

## Dependencies

- [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- [`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency, context note, premise, or bridge. The
independent audit lane is the only status authority. References to retained
or retained-bounded dependency surfaces are descriptive references to existing
audit-ledger status, not a status action by this note.
