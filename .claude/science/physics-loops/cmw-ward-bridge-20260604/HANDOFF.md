# Handoff

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/2623

This branch repairs the CMW low-dimensional sublattice row by supplying a
finite-volume Ward-normalized Bogoliubov bridge:

- `SUMMARY: CMW WARD BRIDGE PASS=17 FAIL=0`
- updated CMW runner cache: `OVERALL: PASS`
- `WARD_NORMALIZED_BRIDGE_HYPOTHESES_EXPLICIT=TRUE`
- `WATSON_LIMIT_COMMENT_REPAIRED=TRUE`

What remains open:

- W1-W4 are explicit hypotheses. This branch does not prove that every
  abstract continuous-symmetry Hamiltonian automatically supplies those
  operators and volume-independent constants.
- Independent audit owns any status movement.

Reviewer action:

Check whether the revised CMW sublattice note's W1-W4 scope is acceptable for
clean re-audit. If not, the remaining work is a broader operator-construction
theorem, not a cache/source exposure problem.
