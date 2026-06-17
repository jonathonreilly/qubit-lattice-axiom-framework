# Record-Intrinsic Readout Extensionality Bridge for P-dep

**Date:** 2026-06-17
**Claim type:** bounded_theorem
**Type:** exact-support / narrow bridge theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome and does not edit the audit-lane-owned ledger,
queue, registry, or publication-status surfaces.
**Primary runner:**
[`scripts/frontier_record_intrinsic_readout_extensionality_bridge_2026_06_17.py`](../scripts/frontier_record_intrinsic_readout_extensionality_bridge_2026_06_17.py)
**Cached runner output:**
[`logs/runner-cache/frontier_record_intrinsic_readout_extensionality_bridge_2026_06_17.txt`](../logs/runner-cache/frontier_record_intrinsic_readout_extensionality_bridge_2026_06_17.txt)

## Summary

This note supplies the missing P-dep interface in the narrow form needed by
the unordered-mass-multiset registrability bridge:

```text
record-intrinsic scalar readout
  => depends only on the registered atom supplied by the readout context
  => cannot depend on hidden label order, sign convention, ambient parameter,
     seed, construction history, or within-sector datum not registered
```

No new axiom is introduced. The input is exactly the approved Record wording in
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md):

- a record is the durable registration of the realized outcome;
- in a supplied finite central-sector readout context with fixed `K`/CPT, the
  realized outcome is the `K`/CPT orbit of the realized central sector;
- finite scalar readout is additive over finite pairwise-disjoint record
  collections;
- a record supplies no readout context, decomposition, `K`/CPT structure,
  weighting, normalization, probability, within-sector data, or occupancy rule.

The bridge does not derive the readout context. It says only: once a context
has supplied a finite registered atom alphabet, a scalar that is actually a
readout of the Record objects is a function on those registered atoms. A
hidden-context-dependent function may be a useful auxiliary diagnostic, but it
is not a record-intrinsic readout.

## Theorem

Fix a supplied finite readout context. Let `A` be the registered atom map:
each record object `r` has atom

```text
A(r) = (K/CPT orbit of the realized central sector, optional monitored
        central values explicitly supplied as registered atom data).
```

The optional monitored values clause is important: Record does not supply
those values. They may enter only when the supplied readout context explicitly
makes them part of the registered atom. If they are not registered, the
readout can depend only on the orbit component.

Let `I` be a scalar readout of finite collections of records. If `I` is
record-intrinsic, meaning it is a function of the Record objects and not of an
augmented pair `(record, hidden context data)`, then:

1. **Per-record extensionality.** If `A(r) = A(r')`, then
   `I({r}) = I({r'})`.
2. **P-dep factorization.** There is a function `f` on registered atoms such
   that, for every finite pairwise-disjoint collection `R`,
   ```text
   I(R) = sum_{r in R} f(A(r)).
   ```
3. **Hidden-context firewall.** Any scalar that changes when only an
   unregistered label, sign convention, ambient parameter, construction seed,
   or within-sector datum changes is not a readout on records. It is a readout
   on a larger supplied object.

This is the P-dep interface: per-record contributions depend only on the
registered datum and on nothing else. It is not an added primitive; it is the
ordinary extensionality of a function whose domain is the record object named
by the approved Record axiom.

## Proof

**E1 - Record object boundary.** By the approved axiom, the record object is a
durable registration of the realized outcome. In a supplied finite
central-sector context, that outcome is the `K`/CPT orbit of the realized
central sector. The same paragraph explicitly says the record supplies no
readout context, decomposition, `K`/CPT structure, weighting, normalization,
probability, within-sector data, or occupancy rule.

**E2 - Extensionality.** A scalar readout of records is a function on record
objects. Functions are extensional on their domain: if two domain elements are
the same record atom, a function on records cannot assign two values. A rule
that assigns different values after changing only hidden supplied-context data
is not a function on the record object; it is a function on an augmented
object.

**E3 - Additive sum.** Record finite additivity gives
`I(R1 union R2) = I(R1) + I(R2)` for pairwise-disjoint finite collections and
`I(empty) = 0`. Iterating over singletons gives
`I(R) = sum_{r in R} I({r})`. By E2, `I({r})` factors through the registered
atom `A(r)`, so `I(R) = sum f(A(r))`.

**E4 - Scope.** The theorem does not say that every context function is
record-intrinsic. It classifies hidden-context-dependent functions as outside
the Record readout class. Nor does it say which physical readout context is
realized; that remains a separate supplied-context or physical-bridge
question.

## Application Interface For The Unordered-Mass-Multiset Row

On the supplied AC_phi_lambda circulant context used by
[`UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md`](UNORDERED_MASS_MULTISET_REGISTRABILITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-11.md),
the context supplies:

- Fourier central-sector projectors `{P_k}`;
- fixed entrywise `K`/CPT conjugation, inducing the orbit `[k]`;
- monitored central values `lambda_k(delta)` as the registered spectral
  atom data for that theorem.

For that supplied context, the registered atom is

```text
A_k(delta) = ([k], lambda_k(delta)).
```

Therefore any record-intrinsic additive scalar readout has the form

```text
R(total) = sum_k f([k], lambda_k(delta)).
```

The hostile candidates rejected in the unordered-multiset runner split cleanly:

- label-order probes, signed doublet gaps, and `sin(3 delta)` are not scalar
  on the `K`/CPT orbit;
- cross terms are not additive;
- functions that depend on supplied-but-unregistered labels or ambient
  construction data are auxiliary context diagnostics, not record-intrinsic
  readouts.

This discharges P-dep only at the record-intrinsic-readout interface. It does
not prove that the physical species readout context is this supplied
AC_phi_lambda context, does not derive `|delta|`, and does not touch the
occupancy dial `r`.

## Boundaries

- Does not add an axiom, primitive, Tier-A admission, or audit status.
- Does not derive the readout context, central-sector decomposition,
  `K`/CPT structure, monitored central values, weighting, normalization,
  probability, measurement dynamics, or physical production.
- Does not forbid auxiliary hidden-context diagnostics. It only says those
  diagnostics are not scalar readouts of the Record objects.
- Does not claim that every downstream physical readout is
  record-intrinsic. A separate physical-readout bridge can still fail.
- Does not derive `|delta| = 2/9`, R-eta, R2, theta retirement, or any
  species/generation dial value.

## Runner Certificate

The runner mechanically checks:

- the required Record-axiom phrases are present in the current minimal-axiom
  memo;
- finite additivity iterates to a sum over singleton record contributions;
- extensional functions factor through the registered atom map;
- hidden-label, sign, ambient-parameter, seed, and within-sector probes fail
  record-intrinsic extensionality;
- in the supplied AC_phi_lambda toy interface, `([k], lambda_k)` is enough to
  express the P-dep form used by the unordered-multiset bridge;
- the note and runner do not claim a new axiom, audit verdict, registry edit,
  or physical readout-context derivation.

Run:

```text
python3 scripts/frontier_record_intrinsic_readout_extensionality_bridge_2026_06_17.py
```

Expected result:

```text
TOTAL: PASS=36 FAIL=0
```
