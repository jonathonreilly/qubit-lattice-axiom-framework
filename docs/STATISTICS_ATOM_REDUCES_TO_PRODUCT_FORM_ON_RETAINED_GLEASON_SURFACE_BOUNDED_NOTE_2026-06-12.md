# W8a Statistics Atom Reduces To Outcome Factorization Under A Supplied Quotient Instance

**Date:** 2026-06-12
**Claim type:** bounded_theorem / bounded support under a supplied outcome-factorization instance
**Status:** source proposal under supplied outcome-factorization instance; independent audit required.
**Status authority:** independent audit lane. This source note does not set,
predict, promote, or demote any audit outcome and does not edit audit-owned
registry, ledger, queue, or publication-status surfaces. The
`bounded_theorem` label is a source-side claim-boundary declaration, not an
audit verdict.
**Primary runner:** `scripts/frontier_statistics_atom_reduces_to_product_form_2026_06_12.py`
**Runner cache:** `logs/runner-cache/frontier_statistics_atom_reduces_to_product_form_2026_06_12.txt`

## 2026-06-16 audit-boundary repair: product-form is not load-bearing

The earlier source row used the product object `sigma tensor sigma` as the
row-local supplied premise. That was stronger than the chain needs. The
retained-bounded sibling
`PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md`
proves that agreement-conditioned flow consumes only the registered
two-outcome weights

```text
m(j,k) = p_j p_k,   j,k in {s,d},
```

and does not require a full joint-state product representation. This note
therefore removes `sigma tensor sigma` as a load-bearing premise. A product
joint state remains a sufficient witness for factorization, but it is not the
premise that this row asks future work to discharge.

The retained Gleason/Busch surface supplies the one-copy Born form. It still
does **not** supply physical independence, iid repetition, or the
outcome-level factorization law. The remaining non-retained input is therefore
the quotient registered-weight statement `m(j,k)=p_j p_k`, not a state-level
product theorem and not an axiom.

The source claim is correspondingly narrow:

- K1 restates the retained Born form on the supplied two-outcome partition.
- K2 imports the retained-bounded weakening theorem and uses the supplied
  outcome-level factorization premise `m(j,k)=p_j p_k`; the old
  `sigma tensor sigma` product instance is retained only as an overstrong
  sufficient example.
- K3 rederives the agreement-conditioned sharpening flow under that supplied
  outcome-factorized quotient instance.
- K4 reduces the wave-8a statistics atom to one named premise: repeated
  registrations factor on the registered two-outcome quotient.

This note does **not** discharge the outcome-factorization premise, does not
assert iid/product composition as a physical fact, does not adopt R-D, does not
select an occupancy cell, does not fix `r`, and does not import probability
beyond the retained Gleason/Busch surface. The Born form here is the cited
retained authority, not a new rule. For firewall clarity: the
outcome-factorization premise is the supplied bounded premise for this row; it
is named, not derived or retained. R-D stays proposed; no occupancy cell is
selected; `r` is never fixed; the occupancy binary stays open.

## 2026-06-18 companion no-go: one-copy Born marginals are insufficient

The companion source-side no-go
`STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS_NARROW_NO_GO_NOTE_2026-06-18.md`
proves that the retained one-copy Born/Gleason surface plus finite scalar
additivity does not force the quotient-level law `m(j,k)=p_j p_k`.

That result does not refute future record-stack independence. It only prunes
the false repair route in which this row's remaining premise is treated as a
mere corollary of one-copy Born authority. A positive unbounded repair still
needs a record-stack independence, stationarity, reset/preparation, or other
framework-native theorem that supplies the registered two-copy quotient
weights.

## 2026-06-17 source-edge bridge: exact product-instance criterion

The paired source bridge
`STATISTICS_PRODUCT_INSTANCE_CRITERION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-17.md` proves the
finite product-instance recognition theorem that the earlier wording lacked:
on the `M_2(C)` effect surface, a same-marginal two-registration density matrix
is forced to be `sigma tensor sigma` when its shifted-Pauli product-effect
connected cumulants vanish. It also records the weaker registered quotient
criterion `m(j,k)=p_j p_k` as the exact outcome-factorization premise consumed
here, and checks a same-marginal correlated witness that fails the criterion.

This bridge does not derive physical independence, iid repetition,
record-stack stationarity, or an instrument law. It is a source-edge repair:
the product-state witness and the weaker quotient premise are now executable
finite criteria rather than vague prose imports. The physical
outcome-factorization premise itself remains open outside this bounded row.

## Boundary

This note proves K1-K4 only in the bounded setting above: retained one-copy
Born authority plus the retained-bounded product-to-outcome weakening plus a
supplied outcome-factorized two-registration quotient. The 2026-06-17 bridge
supplies an exact product-instance criterion for the overstrong
`sigma tensor sigma` witness and an exact quotient-cumulant criterion for the
weaker premise; it does not supply the physical repeated-registration law.

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

**K2 — outcome factorization, not state-product composition.** The retained
product-to-outcome weakening theorem proves that the later flow consumes only
the four registered weights `m(j,k)`. Supply the quotient-level premise
`m(j,k)=p_j p_k` for `j,k in {s,d}`. Then the agreement cells are

```text
m(s,s) = p_s^2,   m(s,d) = p_s p_d,
m(d,s) = p_d p_s, m(d,d) = p_d^2.
```

If a full product state `sigma tensor sigma` is separately supplied, the Born
trace-tensor identity gives the same four weights; that is a sufficient
witness, not a load-bearing necessity. The 2026-06-17 product-instance bridge
gives the finite product-effect criterion that forces that overstrong witness
when its same-marginal cumulants vanish. The runner verifies the
outcome-factorized algebra, the product-state witness, and the bridge link so
the boundary is executable. **[check K2]**

**K3 — the flow follows.** Agreement-conditioning the joint weights keeps the
`(s,s)` and `(d,d)` cells and renormalizes:

```text
p_i' = p_i^2 / (p_s^2 + p_d^2).
```

On the finite odds chart `p_s > 0`, the outcome ratio `x = p_d / p_s` sends
`x` to `x^2`. With `x = 2r`, the bounded wave-8a records-flow coordinate
obeys, under the supplied outcome-factorized quotient instance,
`r -> 2r^2`; its inverse direction is `r -> sqrt(r/2)`, the thermalizing map.
The endpoint `p_d=0` is included as `x=0`; the endpoint `p_s=0` is outside this
finite chart and is handled directly as the all-`d` fixed boundary. The wave-8a
G2 identification is reproven inline here as this ratio calculation. **[check K3]**

**K4 — the atom reduced.** The wave-8a statistics atom, "repeated registration
composes independently on the weight bookkeeping," therefore reduces to the
single outcome-factorization premise:

```text
repeated registrations factor on the registered two-outcome quotient:
m(j,k)=p_j p_k for j,k in {s,d}.
```

That premise is named, not discharged. Its framework home is the record-stack
stationarity/independence residual of the unraveling lane, especially
`UNRAVELED_RECORD_TRAJECTORIES_SUPPLY_NONDEGENERATE_STEP_DISTRIBUTION_BOUNDED_THEOREM_NOTE_2026-06-10.md`
and
`UNRAVELED_STEP_LAW_BI_INVARIANT_QUASI_STATIONARITY_SPLIT_BOUNDED_THEOREM_NOTE_2026-06-10.md`.
Everything else in this row's R-D algebraic reduction is derived from retained
Born authority and the retained-bounded product-to-outcome weakening once that
premise is supplied. The product-instance criterion bridge makes the
state-level sufficient witness checkable, but the physical
outcome-factorization premise itself remains open outside this bounded row.
**[check K4]**

The runner also checks a correlated joint-state witness:
`rho_corr = p_s P_s tensor P_s + p_d P_d tensor P_d`. It has the same one-copy
weights but `m(P_s tensor P_d) = 0 != p_s p_d` generically, and
agreement-conditioning gives the identity update `p_i' = p_i`. This witness is
the control showing that the outcome-factorization premise does real work.

## Consequence

After this note, the occupancy lane's open content is:

- the outcome-factorization premise, named as a supplied bounded premise with
  the record-stack stationarity/independence home above;
- the outcome dictionary, the wave-9 tri-guise binary;
- the durability-to-weight coupling.

Each item is named; none is selected here. The route remains live.

## Does Not

- This does not assert iid/product composition as a physical fact.
- This does not discharge, retain, or physically select the
  outcome-factorization premise.
- This does not require repeated registrations to be represented by
  `sigma tensor sigma`; state-level product form is an overstrong sufficient
  witness only.
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
`KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`,
and
`STATISTICS_OUTCOME_FACTORIZATION_NOT_FORCED_BY_BORN_MARGINALS_NARROW_NO_GO_NOTE_2026-06-18.md`.

## Dependencies

- [`GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md`](GLEASON_ON_QUBIT_LATTICE_PROJECTION_LATTICE_NARROW_THEOREM_NOTE_2026-05-20.md)
- [`BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](BUSCH_POVM_EFFECT_GLEASON_QUBIT_AUTHORITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
- [`PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md`](PRODUCT_FORM_PREMISE_WEAKENS_TO_OUTCOME_FACTORIZATION_BOUNDED_NOTE_2026-06-12.md)
  — retained-bounded theorem proving that agreement-conditioned flow needs only
  outcome-level factorization, not state-level product form.
- [`STATISTICS_PRODUCT_INSTANCE_CRITERION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-17.md`](STATISTICS_PRODUCT_INSTANCE_CRITERION_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-17.md)
  — exact finite criterion for recognizing the overstrong product-state
  witness and the weaker quotient-cumulant premise; it does not derive the
  physical repeated-registration law.
- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency, context note, premise, or bridge. The
independent audit lane is the only status authority. References to retained
or retained-bounded dependency surfaces are descriptive references to existing
audit-ledger status, not a status action by this note.
