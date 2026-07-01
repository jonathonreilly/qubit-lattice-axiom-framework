# Record Occurrence First-Token Symmetry Boundary

**Date:** 2026-07-01
**Claim type:** bounded theorem / occurrence-law narrowing.
**Status authority:** independent audit lane only. This note does not set an
audit verdict, edit registries, register primitives, change axioms, or claim
that record occurrence is impossible.
**Primary runner:**
[`scripts/record_occurrence_first_token_symmetry_boundary_2026_07_01.py`](../scripts/record_occurrence_first_token_symmetry_boundary_2026_07_01.py)

## Claim

The record-occurrence wall has a sharper first-token boundary.

From a homogeneous no-record input, a deterministic rule that is covariant under
the lattice translations cannot produce a sparse first record set. The output
must be translation invariant. On a transitive finite periodic lattice, the only
translation-invariant record supports are:

```text
empty support;
full support.
```

With record values included, the translation-invariant partial record
configurations are:

```text
no records;
the same value recorded at every site.
```

Thus a deterministic translation-covariant occurrence rule cannot create "a
few first records" from no boundary, no trigger, and no prior record pattern. It
must either:

```text
write no records;
write an everywhere-symmetric record layer;
consume a symmetry-breaking boundary/trigger/realized state;
or use a stochastic/instrumental occurrence law whose individual outcomes need
not preserve the symmetry of the distribution.
```

This does not close occurrence. It narrows `W_occurrence`: if the framework
wants records to occur sometimes, and not everywhere, the occurrence bridge
must supply the symmetry-breaking, stochastic, instrumental, or boundary
content that selects the activated sites.

## Finite Theorem

Let `X` be a finite periodic lattice region on which the translation group `G`
acts transitively. Let the no-record input be invariant under `G`. Let `F` be a
deterministic record-extension rule with covariance

```text
F(g . input) = g . F(input)    for every g in G.
```

Since the input is invariant, `g . input = input`, so

```text
g . F(input) = F(input)       for every g in G.
```

The output is translation invariant.

For a partial record support `R subset X`, translation invariance means
`gR = R` for every translation `g`. Because the action is transitive, either
`R` is empty or every site lies in `R`. Therefore no nonempty proper support can
be the output of such a rule.

If record values are present and translations do not change the value labels,
then invariance also forces any full-support assignment to be constant: every
site is a translate of every other site, so all recorded values are equal.

The same argument applies to any homogeneous boundary on any transitive
periodic approximation. It does not assume probabilities, Hilbert-space
dynamics, Born weights, or a Hamiltonian.

## Explicit Witnesses

On a cyclic five-site lattice, the translation-invariant subsets are:

```text
empty;
{0,1,2,3,4}.
```

There is no invariant one-site support and no invariant two-site support.

On a `3 x 3` periodic square lattice, the translation-invariant subsets are:

```text
empty;
all 9 sites.
```

For binary record values on either transitive lattice, the invariant partial
record configurations are:

```text
no records;
all sites record 0;
all sites record 1.
```

So deterministic covariance allows the no-record outcome and the homogeneous
all-record outcomes, but not a sparse first-token event.

## Relation To The Current Occurrence Stack

The existing occurrence stack already shows:

```text
availability supplies support;
Born-form weights can supply conditional selection after an interface;
neither supplies activation.
```

This note adds the symmetry reason why activation cannot be a bare deterministic
"first record appears somewhere" rule on a homogeneous lattice. A local
deterministic rule with no symmetry-breaking input sees the same situation at
every site. If it writes one site, covariance writes every translate. If it does
not write every translate, then some extra input selected the site.

Therefore the clean occurrence target becomes:

```text
local record-extension kernel normal form
  + physical activation supplier
  + symmetry-breaking boundary/trigger, stochastic law, instrument, or realized
    state data
  -> sparse or local durable record production.
```

## What Moves

| Prior residual | Effect of this theorem |
|---|---|
| "derive record occurrence" | narrowed away from a bare deterministic homogeneous first-token rule |
| activation law | must include site/region activation data or stochastic/instrumental sampling |
| total-recording risk | exposed as the symmetric deterministic alternative to no-record |
| no-record witness | preserved as a symmetry-compatible output |
| sparse records | require boundary, prior records, trigger, stochastic realization, or instrument content |

## What Remains

The occurrence bridge still needs one of:

- a physical instrument/trigger that activates selected sites;
- a stochastic local record-extension law with declared outcome weights;
- a deterministic law acting on a non-homogeneous record boundary or realized
  state;
- a Markov/transfer generator plus clock or rate normalization;
- a pointer/decoherence supplier with its own boundary, coupling, and reset
  conditions.

This theorem only removes one tempting but invalid shortcut: deterministic
translation-covariant sparse first-token creation from a fully homogeneous
no-record input.

## Audit Consequence If Retained

Rows that need actual sparse record occurrence cannot cite only:

```text
Lattice + Admissibility + Record + deterministic covariance.
```

They must cite a retained bridge or approved primitive that supplies the
activation selector. Safe dependency shapes are:

```text
record boundary + local deterministic extension law -> possible local records;
instrument/trigger + extension kernel -> activated records;
stochastic extension law + realized draw -> sparse first records;
homogeneous deterministic law -> no records or homogeneous all-site records.
```

## Non-Claims

This note does not claim:

- records never occur;
- record production is impossible;
- a new ontology axiom is required;
- all sites must record;
- all sites must remain unrecorded;
- Born weights are excluded;
- stochastic laws, instruments, pointer dynamics, boundary-driven activation,
  or realized-state inputs fail;
- a clock, rate, Hamiltonian, transfer operator, metric, or physical observable
  selector is derived.

## Minimum Foundation Update If Bridge Work Fails

No ontology axiom update follows from this theorem.

If bridge-first routes fail and owner governance chooses an approved
operational primitive, this theorem sharpens the `P_record_extension` candidate:

```text
Given a record boundary and available local possibilities, a local composable
record-extension law may lock one available possibility at selected unrecorded
sites while preserving existing records. Sparse first-token production also
requires a symmetry-breaking boundary/trigger, stochastic realization,
instrument, or realized-state input; it is not forced by deterministic
translation covariance on a homogeneous no-record lattice.
```

## No-Go Discipline Gate

**Status:** PASS for the narrow first-token symmetry boundary. This is not a
terminal no-go against record occurrence. It is a bounded theorem about one
route: deterministic translation-covariant sparse first-record production from
a homogeneous no-record input.

### N1 - Alternative Route Enumeration

| Route | What it attempts | Standing |
|---|---|---|
| Bare deterministic covariance route | Produce a sparse first record from a homogeneous no-record state using only a deterministic translation-covariant rule. | ATTEMPTED here: fails because the output must be translation invariant. |
| Full-support deterministic route | Record every site with the same value. | ALLOWED SPECIAL CASE: symmetric but it is total homogeneous recording, not sparse occurrence. |
| Boundary route | Use supplied boundary records or inhomogeneous local conditions to select where activation occurs. | OPEN: not blocked by this theorem. |
| Stochastic route | Preserve covariance of the law while individual realized outcomes break translation symmetry. | OPEN: requires explicit probabilities/kernel and realized draw. |
| Instrument/trigger route | Use a physical record-writing instrument or trigger to activate selected sites. | OPEN/PARTIAL BY PRIOR: finite instrument normal form exists, physical supplier remains. |
| Pointer/decoherence route | Use controlled-copy or pointer dynamics with fresh fragments. | PARTIAL BY PRIOR: bounded finite supplier under explicit hypotheses, not axiom-level occurrence. |
| New primitive route | Register occurrence as an approved operational primitive. | OWNER-GOVERNANCE ROUTE: available only if bridge-first work fails or is intentionally bypassed. |

### N2 - Wall-Independence Audit

The collapsed wall is:

```text
W_sparse_activation_supplier.
```

For this theorem, the support-selection wall is not independent of activation:
the missing supplier must say where activation occurs, or provide stochastic
outcomes from which the activated support is realized. Conditional value
selection over available possibilities remains downstream of activation when
more than one value is available.

### N3 - Hidden-Wall Scan

| Term | Classification |
|---|---|
| `homogeneous no-record input` | Explicit theorem input: no prior records or boundary asymmetry. |
| `deterministic` | Explicit route being tested; stochastic routes are outside scope. |
| `translation-covariant` | Lattice-compatible covariance condition, not a physical dynamics assumption. |
| `transitive finite periodic lattice` | Finite approximation used to test the symmetry fact exactly. |
| `sparse first record` | Nonempty proper record support; not all-site recording. |
| `instrument` / `trigger` / `stochastic law` | Live closure paths, not assumed by the proof. |

No hidden admission is used to prove the negative boundary.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `RECORD_OCCURRENCE_GATE_FACTORIZATION_FROM_LOCAL_AVAILABILITY_2026-06-30` | activation and selection are not supplied by availability. | activation support still missing. | yes |
| `LOCAL_RECORD_EXTENSION_KERNEL_NORMAL_FORM_2026-06-30` | occurrence law needs activation, selection, and preservation. | activation support supplier narrowed by symmetry. | yes |
| `RECORD_OCCURRENCE_INSTRUMENT_SUPPLIER_BRIDGE_2026-07-01` | physical instrument/trigger remains. | instrument is an allowed supplier. | yes |
| `RECORD_OCCURRENCE_ACTIVATION_INDEPENDENCE_2026-07-01` | same available set admits different activation values. | deterministic homogeneous activation cannot pick a sparse site. | yes |
| `RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06` | baseline does not force record formation. | no-record output remains symmetry-compatible. | yes |
| `RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05` | pointer route is bounded under explicit hypotheses. | pointer route remains open/conditional. | yes |
| `MINIMAL_OPERATIONAL_PRIMITIVE_UPDATE_RECOMMENDATION_2026-07-01` | `P_record_extension` is a fallback candidate, not registered. | same candidate, now sharpened by symmetry. | yes |

### N5 - Rhetoric Audit

The proven sentence is only:

```text
A deterministic translation-covariant rule cannot output a nonempty proper
record support from a homogeneous no-record input on a transitive lattice.
```

It is tested at the support level and at the binary-valued partial-record level
on finite transitive periodic lattices. It is not a claim about stochastic laws,
boundary-driven laws, non-homogeneous histories, all-site recording, or
instrument dynamics.

### N6 - Partial-Closure Path Scan

Live closure paths remain:

- derive a physical trigger or instrument;
- derive a stochastic local record-extension law and realized outcome rule;
- derive a deterministic law acting on non-homogeneous supplied boundary
  records;
- derive occurrence from pointer/decoherence dynamics with fresh/reset
  conditions;
- approve and register `P_record_extension` if owner governance chooses a
  primitive production rule.

The primitive-registry check confirms that no current approved primitive grants
record-extension occurrence.

### N7 - Steelman

A hostile reviewer can argue that physical occurrence should be stochastic from
the start: the law can be translation covariant as a probability distribution
while each realized record history breaks the symmetry. That objection is
correct and is not blocked here. It is exactly why the theorem narrows the
deterministic shortcut rather than claiming occurrence cannot be derived. A
future stochastic or instrument theorem could close the occurrence wall without
changing the ontology axioms.

### N8 - Cross-Cycle Echo

Earlier record-production notes separated availability, Born weights, kernels,
instruments, and produced records. This theorem preserves that split. It adds
one recurring lesson: symmetry-compatible laws can describe allowed supports or
probability distributions, but sparse realized records require either a
realized draw or another symmetry-breaking input.

## Verification

Run:

```bash
python3 scripts/record_occurrence_first_token_symmetry_boundary_2026_07_01.py
```

Expected close:

```text
TOTAL: PASS=96 FAIL=0
```
