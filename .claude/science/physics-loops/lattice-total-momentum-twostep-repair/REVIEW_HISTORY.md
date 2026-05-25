# Review History

Source trigger:

- Independent audit on 2026-05-25 marked
  `lattice_total_momentum_conservation_theorem_note_2026-05-02`
  `audited_conditional`.

Reviewer-facing repair:

- remove canonical-density and `H_phys` overclaims;
- verify exact two-step sector conservation with a nontrivial runner;
- leave audit outcome unset.

Local review-loop pass:

- CodeRunnerReviewer: pass; runner computes nontrivial projectors,
  commutators, and sector-weight conservation rather than printing a fixed
  result.
- PhysicsClaimReviewer: pass; source note is narrowed to two-step sectors
  and explicitly removes the old canonical-density theorem.
- ImportSupportReviewer: pass with named bounded context; no fitted,
  observed, literature, or unit-convention input.
- NatureRetentionReviewer: bounded only; not a retained proposal.
- RepoGovernanceReviewer: pass; audit pipeline marks the changed source row
  unaudited/ready without applying any audit verdict.
