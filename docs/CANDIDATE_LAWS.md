---
claim_id: candidate_laws
claim_type: meta
claim_scope: "Register of owner-adopted candidate law clauses: working clauses below the axioms, recorded with the owner's approval, date, exact wording and evidence. They carry no premise weight: results that use one are conditional on it until it is derived from the axioms or promoted through AXIOM_MINIMALITY_POLICY section 6."
---

# Candidate laws

**Type:** meta (register).

**Status:** living register. Entries are owner-adopted *working* law clauses, not axioms or
primitives.

## What belongs here

The four axioms (`MINIMAL_AXIOMS_2026-06-29.md`) leave the law's form and values open. For
example, Admissibility says each site's odds depend on its neighbours, but not how.

A **candidate law** is a clause the owner has adopted as a working answer to such an open
question, so that work can build on it. An entry is added only after the owner decides, and it
records:
- the exact wording;
- the date and the owner's words of approval;
- the evidence (PRs with runners);
- what remains open.

## What it does not do

- **No premise weight.** A candidate law is not registered in
  `docs/audit/data/axiom_premise_nodes.json` and does not chain-satisfy anything. A result that
  uses one is conditional on it and must say so.
- **Not an axiom edit.** Promotion to axiom or primitive goes only through
  `docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6, with the owner's explicit approval there.
- **Revisable.** An entry is retired when it is derived from the axioms (it then becomes a
  theorem) or is replaced by the owner.

## Entries

### CL-1 — Influence passes without loss (adopted 2026-10-18)

> "Influence passes from site to site without loss."

- **Owner approval.** "If you are confident decision 1 is correct (that there is no loss in
  influence) then lets go with it and build on it."
- **Reading.** It specifies the form left open by Admissibility: whatever rule turns
  neighbours' odds into a site's odds loses nothing as it passes influence on. The rule may
  lean with or away from its neighbours.
- **Why.**
  - Any loss ε per step screens a record's 1/r influence to a range of about 1/√ε sites.
  - Long-range gravity therefore needs ε = 0.
  - A lossless rule's effect is also exactly what survives zooming out.
- **Evidence.** PR #9825, items L1 and L2.
- **Open.**
  - Whether the clause follows from the axioms.
  - How it applies to the continuous-time form (PR #9825, L8).

### CL-2 — A record's qubit leaves the flow (adopted 2026-10-18)

> "When a record forms, its qubit leaves the flow: the network is permanently short that
> site's share."

- **Owner approval.** "I am good with decision 2."
- **Reading.**
  - A recorded site stops carrying its share of the influence, permanently.
  - Every site has the same possibilities (Qubit), so every record takes the same share.
  - The idea is the owner's: "the record removes the qubit which is a drain in a way".
- **Why.** In the toy rules:
  - A record that is permanently short one share gives a lasting, additive 1/r pull, and
    packets bend toward it.
  - The alternatives fail:
    - a pure hole, where influence detours, gives no far pull;
    - a perfect absorber, or a site that holds a fixed pace, pulls, but its mass grows with
      size rather than count;
    - holding the pace it had when it formed gives nothing;
    - a one-time removal at formation only radiates.
  - Under CL-2:
    - the pace must average with its neighbours (a lean-away pace would make mass sign follow
      the chessboard);
    - only the total share matters far away;
    - a region slowed to zero freezes;
    - everything falls alike at long wavelength.
- **Evidence.** The companion note
  `CANDIDATE_LAW_CL2_A_RECORDS_QUBIT_LEAVES_THE_FLOW_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md`
  and PR #9825 (item L3).
- **Open.**
  - The floor at zero pace.
  - Where the share goes (CL-3, pending).
  - The pace deficit is a standing gap in a field, not a flow of content into the record.

## Pending (not adopted)

- **Decision 3: formation moves content rather than creating it.**
  - **Candidate wording.** "When a record forms, the share its qubit takes out of the flow is
    held by the record, not destroyed; the total is unchanged."
  - **Evidence.** PR #9825, L4: a conserved source satisfies the Ward identity, while a source
    that appears without a current fails.
  - **Open.** What the conserved total is.
