# Record formation: current premise boundary and finite unitary controls

**Date:** 2026-06-06; correction 2026-10-21
**Type:** bounded_theorem
**Claim scope:** finite-dimensional unitary identities and a current-premise
inventory. No general nonderivability theorem is asserted.
**Primary runner:** `scripts/frontier_record_formation_not_unconditionally_forced_by_minimal_axioms.py`
**Status authority:** independent audit lane only.

## Correction to the historical claim

The old argument treated all formation probabilities as absent from current
axioms and quoted scalar Record additivity as axiom content. Both statements
are obsolete. The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies a
nearest-neighbor conditional probability distribution through Admissibility.
Its form and numerical values, the site and rate of formation, and the realized
draw remain distinct questions. Record states that records form and fixes
one-record-per-site, permanence and content-determined readout. It does not
force formation at every site or every admissible opportunity.

The August 13 revision removed scalar collection additivity and `I(empty)=0`.
Neither is used as an axiom here. The July 4
[historical sweep](RECORD_FORMATION_APPEND_CONSISTENCY_SWEEP_2026-07-04.md)
records an earlier premise epoch, not authority to restore removed wording.
The original source is recoverable at
`f24d17d97d372df977476e4a69674577f31af575`. The filename remains for citations.

## What the finite controls establish

Supply a finite tensor-product Hilbert space, standard unitary evolution and
a selected system pointer basis. These are model inputs, not a construction of
the framework's full Admissibility law or its Record process.

1. If `H=0`, `exp(-itH)=I`; every state and its reduced pointer coherence stay
   fixed for all times.
2. For `H=H_S tensor I + I tensor H_E`, the two terms commute and evolution
   factorizes. A product state remains a product. In the runner's particular
   supplied `H_S=sigma_x` and system `|+>` eigenstate, pointer coherence is
   constant. This is not true of every pointer coordinate under every local
   Hamiltonian, and that universal claim is not needed.
3. An eigenstate of a time-independent Hermitian `H` changes only by a global
   phase, so its density matrix and every reduced coherence are stationary.
4. The supplied coupled, non-eigenstate control exhibits a reduced coherence
   smaller than its initial value at the tested time. This is a finite toy
   example; recurrence, irreversible measurement, physical formation and
   asymptotic decoherence are not established.

The first three statements have the elementary proofs just given. The runner
checks finite representatives and the contrast calculation. These unitary
examples alone are not full models of all four framework axioms, so they do
not prove that the current framework can never derive a formation mechanism.
In particular, coherence preservation is not defined as absence of a framework
Record event.

## Current premise inventory and open constructions

The current memo supplies occurrence and a local conditional distribution. It
does not specify that distribution's functional form or values, a dynamical
update, a production process, a formation site/rate or a physical realization
of the finite unitary model above. Those are open construction tasks or
explicit supplied conditions, not conclusions of the four numerical controls.
A future derivation can settle some of these questions without contradicting
this note. No extra premise is adopted here.

The two source-text checks in the runner verify quotation consistency only.
They cannot prove mathematical independence, physical selection or audit
status. The former blanket formation-rule/state/weight no-go is withdrawn;
there is no new N1–N8 exhaustion claim.

## Verification

```sh
python3 scripts/frontier_record_formation_not_unconditionally_forced_by_minimal_axioms.py
```

The six checks consist of four finite model calculations and two source-text
consistency checks. A successful exit certifies those checks only. It is not a
physical formation/no-formation or general nonderivability verdict.
