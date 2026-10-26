---
claim_id: record_information_accounting_lossless_odds_and_read_once_records_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Standard identities (unitarity, the conditioning chain rule, Schmidt decomposition) checked on a supplied unitary walk with one site record, plus bookkeeping consequences of supplied read-once and same-value relay rules and the Record axiom; no physical information law, thermodynamic reading or derivation of the clauses."
upstream_dependencies:
  - minimal_axioms
runner: scripts/record_information_accounting_lossless_odds_and_read_once_records_2026_10_21.py
---

# Information accounting with lossless odds and read-once records

Claim type: bounded_theorem.
Primary runner: `scripts/record_information_accounting_lossless_odds_and_read_once_records_2026_10_21.py`.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) give records that are permanent, one per site, readable and holding exactly one outcome. This note separately supplies a read-once assumption: each record permits at most one read. It also supplies a one-for-one relay rule: a relay consumes one unread record's read and forms one new, unread record of the same value at a previously unused site. Neither rule is asserted to follow from the axioms or to have owner-approved premise status. The identities checked here are standard and conditional on the explicit model choices below.

## Between records

For the supplied unitary walk, norm and purity are unchanged. Complex amplitudes, position Born weights and a normalized pure input are supplied choices. The coin is C = cos(theta) I - i sin(theta) sigma_x, which is unitary; the periodic shift permutes an orthonormal basis. Their product therefore preserves norm and density-matrix purity. The runner checks this to rounding over sixty ticks. Over those ticks the position Shannon entropy rises from 4.55 to 5.20 bits. This model preserves purity while allowing its position distribution to spread; a verbal losslessness clause alone does not determine this quantum structure or its evolution operator.

## At a record

Let a record form at site j and register whether the walker is there, with Born probabilities p and 1-p. Conditioning the odds on the outcome gives

    H(X) = sum_r p(r) H(X | r) + H(R).

Here X is the position variable and R = 1{X=j}, a deterministic function of X. Thus H(X,R)=H(X), and the chain rule gives the displayed identity. On average, conditioning reduces position Shannon uncertainty by H(R); this is not a statement about all quantum information. Zero-probability branches contribute zero, including p=0 or p=1; the runner checks three nondegenerate sites.

In the supplied purification, a controlled flip maps psi|0> to Q psi|0> + P_j psi|1>, with Q = I-P_j. The orthogonal system components have squared norms 1-p and p. The constructed joint vector has unit norm and is pure; the record's reduced entropy equals H(R). The runner checks these properties. Describing a realized outcome additionally requires a supplied outcome-conditioning operation. Neither joint-state purity nor this entropy identity derives outcome-selection dynamics or establishes equivalence of full physical descriptions.

## Read-once bookkeeping

Count each read event once and allow no record to supply two reads. Cumulative reads of a given value are then at most cumulative formations of records of that value (including any initial records). A serial relay can form these records successively; they need not all exist initially. Simultaneous independently available reads require that many unread records at that time.

Reading alone decreases the unread-record count by one. The supplied one-for-one, same-value relay consumes one unread record and forms one unread record, leaving this count unchanged. Independent formation may increase it. Permanence and one-record-per-site uniqueness prohibit reusing an already recorded site for fresh formation. Consequently the used-site count is a nondecreasing bookkeeping count, equal to cumulative formations when initial records are included; it counts records, not their values. It is not the only nondecreasing count: cumulative reads are another. Reversibility of the supplied walk does not undo record formation.

## Scope

The 240-site periodic two-component walk (theta=0.3, sixty ticks), Gaussian packet of width 8 with phase 0.5x and component ratio 0.4i, position Born weights, record sites, controlled-flip purification, outcome conditioning, read-once assumption and same-value relay rule are supplied choices. The finite walk is not identified with physical Z^3. No physical information law, thermodynamic entropy identification, arrow-of-time theorem or derivation of the clauses is established.
