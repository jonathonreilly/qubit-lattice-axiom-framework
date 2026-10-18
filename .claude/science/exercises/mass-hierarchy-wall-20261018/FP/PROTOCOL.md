# First-principles protocol (from /first-principles)

## Allowed starting points (nothing else)

1. **The four axioms**: Lattice, Qubit, Admissibility, Record, as stated in docs/MINIMAL_AXIOMS_2026-06-29.md. Its exclusion lists and boundary sections are binding.
2. **Approved primitives**, only within what their source notes grant:
   - scale_reference_primitive: the Planck scale reference, as a units conversion only;
   - kinetic_isotropy_primitive: the structural OS0 kinetic-form isotropy c_t = c_s only;
   - realized_state_primitive: pointwise evaluation at the supplied realized state only.

   Read docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md.
3. **Retained-grade theorems.** Verify effective_status on origin/main through the ledger data in docs/audit/data. A note's own Status header is not evidence.
4. **Named open dependencies.** These carry zero premise weight.

**Never assume** a continuum, fields, Hamiltonians, Born weights, species identifications or gauge groups, except as named lanes.

## Protocol

1. **Target.** State it exactly, with quantitative characterization and source.
2. **Premise ledger.** List what you use, with effective_status for each retained dependency. Flag any import.
3. **Minimal mechanism.** Give the smallest configuration, checked exactly where feasible.
4. **Step chain.** Each step follows only from earlier steps. Mark every convention, normalization or readout choice.
5. **Novel prediction.** This is mandatory.
6. **Weakest link.** Name it, and the artifact that would test it.

## Further rules

- **If the derivation blocks**, name the exact wall.
- **No-go claims** need the N1–N8 gate (docs/ai_methodology/skills/no-go-gate if present). Do not reopen retired no-go routes without a new premise.

## Output

Write to .claude/science/derivations/{slug}-{date}.md format (in your folder), with these sections:

Date / Target / Premise Ledger / Minimal Mechanism / Derivation steps / Novel Prediction / Weakest Link / Status, where Status is one of PROPOSED, TESTED, CONFIRMED, REFUTED or BLOCKED (named wall).
