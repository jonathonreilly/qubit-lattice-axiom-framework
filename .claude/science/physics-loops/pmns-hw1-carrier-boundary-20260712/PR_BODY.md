# [physics-loop] PMNS hw=1 carrier block01 — bounded theorem

## Summary

This science block repairs the missing derivation in
[`PMNS_SOLE_AXIOM_HW1_SOURCE_TRANSFER_BOUNDARY_NOTE.md`](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/physics-loop/pmns-hw1-source-transfer-block01-20260712/docs/PMNS_SOLE_AXIOM_HW1_SOURCE_TRANSFER_BOUNDARY_NOTE.md)
without presenting a definition as an axiom consequence.

The revised theorem proves:

- within the explicit translation/`C_3`-invariant `hw=1` candidate class, the
  complete joint commutant is `C I_3`;
- the current axiom signature does not create a carrier operator or select the
  unit-normalized pair `(I_3,I_3)`;
- under the displayed response and one-sided-minimal support interfaces, every
  nonsingular scalar active/passive pair produces only scalar basis-source
  columns and cycle-frame support and is rejected;
- the historical unit pack remains available only as a machine-labelled
  conditional compatibility alias.

## Direct blocker closure

Quoted blocker: the previous runner checked consequences after defining the
canonical pack with `active_block=I3` and `passive_block=I3`, so it did not
derive the advertised unit pair from the framework surface.

New derivation: complete joint-commutant classification, formal same-premise
expansion argument, analytic scalar-family resolvent/reconstruction theorem,
and corrected permutation-orbit/cyclic support classifier. The unit choice is
removed from the load-bearing rejection boundary.

## Artifacts

- [Source theorem](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/physics-loop/pmns-hw1-source-transfer-block01-20260712/docs/PMNS_SOLE_AXIOM_HW1_SOURCE_TRANSFER_BOUNDARY_NOTE.md)
- [Paired runner](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/physics-loop/pmns-hw1-source-transfer-block01-20260712/scripts/frontier_pmns_sole_axiom_hw1_source_transfer_boundary.py)
- [Handoff](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/physics-loop/pmns-hw1-source-transfer-block01-20260712/.claude/science/physics-loops/pmns-hw1-carrier-boundary-20260712/HANDOFF.md)
- [Trace gate](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/physics-loop/pmns-hw1-source-transfer-block01-20260712/.claude/science/physics-loops/pmns-hw1-carrier-boundary-20260712/TRACE_GATE.md)
- [Claim-status certificate](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/physics-loop/pmns-hw1-source-transfer-block01-20260712/.claude/science/physics-loops/pmns-hw1-carrier-boundary-20260712/CLAIM_STATUS_CERTIFICATE.md)
- [No-Go Discipline N1--N8](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/physics-loop/pmns-hw1-source-transfer-block01-20260712/.claude/science/physics-loops/pmns-hw1-carrier-boundary-20260712/NO_GO_DISCIPLINE_CHECKLIST.md)
- [Review history](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/physics-loop/pmns-hw1-source-transfer-block01-20260712/.claude/science/physics-loops/pmns-hw1-carrier-boundary-20260712/REVIEW_HISTORY.md)
- [Assumption/import audit](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/physics-loop/pmns-hw1-source-transfer-block01-20260712/.claude/science/physics-loops/pmns-hw1-carrier-boundary-20260712/ASSUMPTIONS_AND_IMPORTS.md)

## Verification

- paired runner: `PASS=31 FAIL=0`;
- independent SymPy commutant/resolvent/reconstruction derivation: exact;
- minimal-axiom/carrier/Burnside companions: `68/68`, `4/4`, `50/50`;
- direct downstream compatibility: five consumers execute; four pass and one
  shows an unrelated pre-existing note-text needle failure;
- review-loop: pass after three iterations;
- audit pipeline validation: row parsed as `bounded_theorem`, dependency only
  `minimal_axioms`, no helper runners, critical queue `ready: true`;
- strict audit lint: no errors;
- vocabulary, portable-link, and `git diff --check` gates: pass.

## Claim firewall

This PR does not claim that the axioms create a physical PMNS carrier, that
`I_3` is impossible, that every lattice operator is scalar, or that all PMNS
routes fail. The response/support interfaces are explicit theorem definitions.
The remaining positive target is a physical non-scalar carrier/source-action
law.

Independent audit is required after landing before the repository may treat
the bounded theorem as effective retained-grade. This PR does not apply or
predict an audit verdict and changes no audit-authority surface.
