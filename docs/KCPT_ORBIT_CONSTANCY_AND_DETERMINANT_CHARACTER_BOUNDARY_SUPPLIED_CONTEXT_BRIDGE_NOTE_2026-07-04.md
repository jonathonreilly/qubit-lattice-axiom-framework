# K/CPT Orbit Constancy And Determinant-Character Boundary Supplied-Context Bridge

**Date:** 2026-07-04
**Claim type:** bounded_theorem
**Status:** exact supplied-context bridge; audit_required_before_effective_retained=true; bare_retained_allowed=false
**Status authority:** independent audit lane only. This note does not set or predict an audit outcome and does not edit audit ledgers, queues, Tier-A registries, publication-status surfaces, active review queues, lane registries, or front-door status files.
**Primary runner:** [`scripts/frontier_kcpt_orbit_constancy_determinant_character_boundary_bridge_2026_07_04.py`](../scripts/frontier_kcpt_orbit_constancy_determinant_character_boundary_bridge_2026_07_04.py)
**Cached log:** [`logs/runner-cache/frontier_kcpt_orbit_constancy_determinant_character_boundary_bridge_2026_07_04.txt`](../logs/runner-cache/frontier_kcpt_orbit_constancy_determinant_character_boundary_bridge_2026_07_04.txt)

## Purpose

The 2026-06-29 foundation reset moved K/CPT-orbit and readout-context content
out of the Record axiom. The 2026-06-05 Record wording carried an
orbit-constancy clause; the current Record axiom supplies only: records form;
one-record-per-site; permanence; "only records are readable"; "a readout value
is determined by record content alone"; finite scalar additivity over
pairwise-disjoint records with `I(empty)=0`.

From [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md), the current
Record axiom is:

```text
### Record / Fixed Reality

Records form.

When present, a record locks exactly one admissible local possibility. A
site never carries more than one record; records are permanent.

Only records are readable. A readout value is determined by record content
alone. For any finite collection of pairwise-disjoint records, scalar readout
`I` is additive, with `I(empty)=0`.
```

Notes that previously cited the axiom for orbit constancy now need a retained
bridge. This note is that bridge: it registers, on a supplied readout context,
(T1) K/CPT orbit constancy as a theorem from the current Record axiom plus one
named supplied-context property, and (T2) the determinant-character/log-character
homomorphism boundary as named supplied-context structure, with the even+odd
zero-phase algebra restated on premises that are now correctly located.

The relevant context handles are
`REGISTRABLE_READOUT_DETERMINANT_CHARACTER_ALGEBRAIC_CORE_SPLIT_NOTE_2026-06-18.md`
(context handle, not a citation-graph dependency),
`TIER_A_KORBIT_DETERMINANT_AND_ORIENTATION_INVARIANCE_BOUNDED_NOTE_2026-06-09.md`
(context handle, not a citation-graph dependency),
`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`
(context handle, not a citation-graph dependency), and
`C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md`
(context handle, not a citation-graph dependency).

## The Supplied Context

The bridge is stated only for a supplied finite readout context with these
components:

- finite orthogonal central idempotents `{e_j}` used as sector record labels;
- a fixed K/CPT conjugation `K`;
- **ORBIT-INDEXING:** the context's record contents are indexed by `K`-orbits,
  so `K`-conjugate outcomes carry the same record content;
- registrable scalar readouts that are functions of record content and obey the
  Record axiom's finite scalar additivity over pairwise-disjoint records;
- a sector-factored determinant datum `z = prod_j z_j`;
- the supplied action of `K` on phase data, `arg z_j -> -arg z_j`;
- the determinant-character/log-character boundary: the phase-bearing
  contribution is an `R`-valued group homomorphism of the per-sector phase
  group.

ORBIT-INDEXING and the determinant-character/log-character homomorphism
boundary are supplied context structure. They are not derived from Record.

## T1 Statement And Proof

**Theorem T1.** In a supplied finite readout context satisfying
ORBIT-INDEXING, every registrable scalar readout is constant on K/CPT orbits.

**Proof.**

1. ORBIT-INDEXING supplies equality of record content on each K/CPT orbit:
   if `y = Kx`, then `content(y) = content(x)`.
2. The Record axiom sentence "A readout value is determined by record content
   alone" transfers that supplied content equality to readout equality:
   `I(y) = I(x)`.

Thus constancy transfers from the supplied orbit-indexing through the
content-determination sentence. It is not axiom content on its own.

## T2 Statement And Proof

**Theorem T2.** In a supplied determinant-character/log-character context with
sector-factored determinant datum `z = prod_j z_j`, with the phase-bearing
contribution an `R`-valued group homomorphism of the per-sector phase group,
and with T1 orbit constancy for `K: arg z_j -> -arg z_j`, the homomorphic phase
functional is identically zero. The additive K-even modulus/log-modulus datum
survives this boundary.

**Proof.**

1. The idempotents `{e_j}` are pairwise-disjoint sector record labels in the
   supplied context. Current Record finite additivity makes the scalar readout
   additive across those sectors.
2. Sector factorization writes the determinant datum as `z = prod_j z_j`, so
   the phase datum is the sum of per-sector phase data in the supplied phase
   group.
3. The determinant-character/log-character boundary says the phase-bearing
   contribution is an `R`-valued group homomorphism on that phase group. This
   boundary is supplied structure, not derived from Record finite additivity.
4. Any additive `R`-valued functional `g` on an abelian phase group is odd:
   `g(0)=0`, and `0 = g(x + (-x)) = g(x) + g(-x)`, so `g(-x) = -g(x)`.
5. T1 orbit constancy, with `K` acting by `arg z_j -> -arg z_j`, makes the same
   scalar K-even: `g(-x) = g(x)`.
6. Even and odd together force `g(x) = 0` for every phase datum.
7. The modulus datum is different: `log|prod_j z_j| = sum_j log|z_j|`, and
   `log|z_j|` is K-even under complex conjugation. Thus modulus/log-modulus
   data survives while the homomorphic phase functional vanishes.

## Negative Controls

An otherwise-identical context can register K-conjugate outcomes as distinct
record contents. For example, if `x` and `Kx` carry contents `left` and `right`,
then the scalar readout with `I(left)=0` and `I(right)=1` is still determined by
record content, but it is not orbit-constant. Orbit constancy is exactly
supplied ORBIT-INDEXING plus Record content-determination, no more.

K-even non-homomorphic functionals such as `cos(theta)` and
`sum_j cos(theta_j)` remain phase-dependent and nonzero. They are outside this
homomorphism boundary. The determinant-character/log-character boundary does
that work, not Record.

## What This Bridge Does Not Claim

- no context selection;
- no K/CPT structure from axioms;
- no Born weights, probability rule, or measurement update rule;
- no physical mass, species, or strong-CP readout identification;
- no Tier-A change;
- no derivation or special role for `|delta| = 2/9`;
- no new axiom, primitive, admission, normalization, comparator, fitted value,
  or measured input.

## Status Certificate

```yaml
actual_current_surface_status: exact-supplied-context-bridge
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
target_claim_id: registrable_readout_determinant_character_algebraic_core_split_note_2026-06-18
target_blocker_text: "the 2026-06-18 core split cited older Record orbit-constancy content; under the 2026-06-29 foundation reset, orbit constancy and determinant-character/log-character homomorphism structure must be registered as supplied-context premises"
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This bridge relocates context-specific orbit indexing and determinant-character/log-character structure without changing admissions or audit status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner Certificate

The runner verifies:

- T1 positive: a 3-idempotent orbit-indexed context makes 200 random
  registrable readouts orbit-constant;
- T1 negative control: a conjugate-distinguishing context admits a registrable
  readout that is not orbit-constant;
- T2 symbolic: additivity gives oddness, and even plus odd gives zero;
- T2 concrete: the supplied circulant family obeys
  `conj(H(delta)) = H(-delta)`, determinant phase conjugation, and log-modulus
  invariance on a small grid including `delta=2/9` as an ordinary point; the
  Hermitian family's determinant is real (phase index already in `{0, pi}`,
  consistent with only modulus data surviving), so the nonzero-phase witness
  that forces the homomorphic coefficient to zero is constructed on generic
  supplied sector data `z_j = r_j e^{i theta_j}`, not on that family;
- hostile guard: `cos(theta)` and `sum_j cos(theta_j)` are K-even,
  phase-dependent, nonzero, and non-homomorphic;
- text guards: required supplied-context phrases are present, forbidden
  completion phrases are absent, and the only markdown citation target for a
  doc note is the current minimal axiom memo.
