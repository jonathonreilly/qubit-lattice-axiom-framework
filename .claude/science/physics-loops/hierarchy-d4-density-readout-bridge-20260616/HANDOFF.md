# Handoff

Branch: `physics-loop/hierarchy-d4-density-readout-bridge-20260616`
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4133

This block adds a source-side D=4 fixed-density coefficient-to-scale bridge for
the hierarchy dimensional-compression lane.

What moved:

- Proves `rho_* = A(L) v(L)^4` forces
  `v(L)/v(L_ref) = (A_ref/A(L))^(1/4)`.
- Applies it to `A_2/A_4 = 7/8` and `A_inf/A_2 = 2/sqrt(3)`.
- Wires the parent `HIERARCHY_DIMENSIONAL_COMPRESSION_NOTE.md` to the new
  bridge for re-audit.
- Leaves physical electroweak VEV/order-parameter identification open.

Verification completed before PR:

- New bridge runner: `TOTAL: PASS=13 FAIL=0`.
- Taste-authority parent runner: `SCORECARD: 8 pass, 0 fail out of 8`.
- Legacy parent runner: `SCORECARD: 7 pass, 0 fail out of 7`.
- Caches refreshed for all touched runners.

Next exact action:

- Reviewer/auditor should evaluate whether this source bridge closes the
  coefficient-to-scale part of the audit blocker. If yes, the remaining hard
  science lane is the physical electroweak order-parameter/readout theorem.
