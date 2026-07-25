# The composition countermodel does not survive Record determinacy — Cycle 691

Date: 2026-07-25

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. **No new axiom or primitive is proposed
or adopted. Deriving content is not adopting it.**

Runner:
`scripts/physical_composition_countermodel_record_determinacy_cycle691_2026_07_25.py`
(6 PASS / 0 FAIL, exit 0, ~1.2 s, exact integer arithmetic throughout).

## The question

The four-axiom completeness note
[Four-Axiom TOE Completeness And Final-Update Gate](work_history/repo/review_feedback/FOUR_AXIOM_TOE_COMPLETENESS_AND_FINAL_UPDATE_GATE_NOTE_2026-07-13.md)
lists multi-site composition as interface `C` — "physical finite-block joint
domain, canonical commuting embeddings, no extra global sectors, entangled
event domain" — with the disposition **"strong Qubit-level candidate unless
derived from the explicit rule"**, and supplies an exact finite countermodel:

```text
B      = M_4(C) (+) M_4(C)
A_x(a) = (a (x) I_2) (+) (a (x) I_2)
A_y(b) = (I_2 (x) b) (+) (I_2 (x) b)
```

Both local embeddings are faithful and commute; their products span only the
diagonal `M_4` copy, and the central observable `I_4 (+) (-I_4)` is invisible
to that span. The note concludes — correctly — that

```text
one M_2(C) at each site + locality
    does not entail
the ordinary generated finite tensor product or local tomography.
```

and then explicitly defers: *"Exact wording is deliberately deferred until the
rule/typing probe has decided whether this can instead be a theorem."*

**This cycle is that probe.** The framework is not Qubit plus locality. It also
has Record and Qualification. The question asked here is whether the
countermodel still defeats composition on the *full* axiom surface.

## Result

It does not. Three exact findings, all in integer arithmetic on declared finite
fixtures — no tolerance, no floating point, in any decisive row.

**1. The countermodel is reproduced exactly.** Both embeddings faithful,
commutator identically zero, local-product span of complex dimension 16 inside
an ambient of complex dimension 64, and the central observable provably outside
the span (rank 16 → 17 on adjoining it).

**2. Generation is forced.** For every declared pair of commuting faithful
unital \*-embeddings of `M_2(C)` — plain tensor product, the countermodel,
three identical summands, a signed-permutation twist, and a multiplicity
amplification — the generated \*-algebra has complex dimension **exactly 16**,
while the ambient dimension ranges over 16, 64 and 144. The full 16×16
multiplication table on matrix-unit words is identical to that of
`M_2(C) (x) M_2(C)` in every case, with every product resolving to a single
basis word or exactly zero.

> The ordinary tensor product is not an extra assumption. It is what two
> commuting faithful qubit copies **always** generate. The countermodel's
> excess is *ambient*, never *generated*.

**3. Record determinacy excludes the excess.** Over every declared
summand-swapped state pair, the two states agree **exactly** — difference
identically zero in integer arithmetic — on every element of the local-product
span, i.e. they carry identical record content at every site. Yet the central
observable separates them by exactly 2.

So the central observable's value is **not determined by record content**. The
Record clause *"readout value is determined by record content alone"* therefore
denies it lawful-readout status. The sector that defeats composition in the
countermodel is precisely the sector that carries no lawful readout.

A preregistered falsifier is run and does not fire: **no** element of the
local-product span separates any declared summand-swapped pair. Had one
existed, the excess would have been record-visible and this cycle's conclusion
would be false.

## What this settles, and what it does not

Settled, on the declared fixture family: the countermodel refutes composition
from **Qubit plus locality**, exactly as its source note says, and does **not**
refute it on the four-axiom surface. Interface `C`'s "no extra global sector"
content follows for *readable* structure without a new axiom.

**The one premise used beyond computation.** The step from "carries no lawful
readout" to "is not a distinct physical state" is performed by the
Qualification sentence *"a state is a configuration of records."* Two
configurations with identical record content are then the same state, and the
countermodel's two summand-states are not distinct states at all. That is a
declared framework-wording citation, recorded as such in the receipt — it is
not a computed row of this runner, and it is the single place where this cycle
leaves exact algebra for framework wording. A reader who rejects that reading
gets the weaker but still exact conclusion: the excess is unreadable.

**Not closed by this cycle**, and not claimed:

- local tomography;
- operational preparation / effect / channel typing (interface `Q`);
- frame measure, denominator, probability (interface `P`);
- which composite projectors are physically available or readable;
- identification of a prepared density operator;
- any statement about three or more sites — untested here;
- infinite dimensions, or ambient algebras outside the declared family.

The source note's own caution stands unchanged: tensor composition "would still
not make every composite projector physically available/readable, identify a
prepared density operator, supply a frame measure, or prove operational local
tomography. Those remain `Q`/`P` work."

## Why it matters

The completeness note's minimum candidate package lists **"Qubit: physical
finite-site composition, unless derived"** as one of four items. This cycle
supplies the "unless derived" branch for the composition content that the
countermodel was blocking, which is the difference between adding an axiom and
proving a theorem. Under the repository's no-new-axiom rule, that is the only
admissible direction of travel.

## Firewalls

- No new axiom or primitive is proposed or adopted here.
- A generated algebra is not a physical Hilbert space.
- Local tomography, preparation, effect typing, frame measure and probability
  are **not** claimed.
- No gravity, dynamics, time, matter, or probability content is asserted.
- This is not a promotion of any claim to retained status; only the independent
  audit lane ratifies retention.

## Dependency citations

The runner imports nothing from the repository; it is self-contained exact
finite algebra. It cites, and does not consume as computed evidence, the
countermodel and interface table of
[Four-Axiom TOE Completeness And Final-Update Gate](work_history/repo/review_feedback/FOUR_AXIOM_TOE_COMPLETENESS_AND_FINAL_UPDATE_GATE_NOTE_2026-07-13.md).
