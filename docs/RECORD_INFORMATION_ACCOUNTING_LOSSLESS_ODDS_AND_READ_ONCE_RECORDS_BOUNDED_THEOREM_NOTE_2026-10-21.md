---
claim_id: record_information_accounting_lossless_odds_and_read_once_records_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "Standard identities (unitarity, the conditioning chain rule, Schmidt decomposition) checked on a supplied lossless walk with one site record, plus bookkeeping consequences of the read-once and record clauses; no physical information law, thermodynamic reading or derivation of the clauses."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/record_information_accounting_lossless_odds_and_read_once_records_2026_10_21.py
---

# Information accounting with lossless odds and read-once records

Claim type: bounded_theorem.
Primary runner: `scripts/record_information_accounting_lossless_odds_and_read_once_records_2026_10_21.py`.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) give records that are permanent, one per site, readable and holding exactly one outcome. The [candidate-law register](CANDIDATE_LAWS.md), which has zero premise weight, records the lossless-influence clause. It also records the read-once clause: "A record can be read once. A burn's one read is taken by the next site of its relay." Results using these clauses are conditional on them. The identities checked here are standard; what the note adds is how they combine with the clauses.

## Between records

A lossless tick is unitary, so the norm and purity of the odds are unchanged. The runner checks both to rounding over sixty ticks of a two-component walk. Over the same ticks the position Shannon entropy of the packet rises from 4.55 to 5.20 bits. The quantity lossless evolution keeps fixed is therefore the purity of the odds, not the spread of their position distribution.

## At a record

Let a record form at site j and register whether the walker is there, with Born probabilities p and 1-p. Conditioning the odds on the outcome gives

    H(X) = sum_r p(r) H(X | r) + H(R).

On average the odds lose exactly the record's entropy, and the record's information comes out of the odds' uncertainty about the recorded variable. The runner checks the identity at three sites. In a purified description a controlled flip writes the outcome onto a record qubit. The joint state stays pure, and the record qubit's entanglement entropy equals H(R), which the runner also checks. In that description nothing is created or lost. In the description where the realised outcome is a fact, the selection of one outcome is new; the two descriptions differ exactly by that selection.

## Read-once bookkeeping

Under the read-once clause a relay step spends a record's single read at the next site and forms a record of the same value there. Reading never increases the number of readable records of a fact. The number of readers a fact can have is at most the number of records formed of it, so a fact many readers share needs many records at formation. By the record axioms, each formation and each relay step uses a site that can never record again. The number of used sites is therefore nondecreasing, while lossless ticks are reversible. In this bookkeeping the used-site count is the only quantity that only grows. It counts how many records formed, not what they hold.

## Scope

The walk, packet, record sites and the controlled-flip purification are supplied choices. No physical information law, thermodynamic entropy identification, arrow-of-time theorem or derivation of the clauses is established.
