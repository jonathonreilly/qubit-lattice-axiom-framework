# Goal

Repair the kinetic isotropy paired runner so it verifies the current source
boundary on the B-W bridge-chain rows.

The branch must not:

- derive or assert B-W closure;
- retire the `kinetic_isotropy_primitive`;
- add a new axiom, primitive, or Tier-A admission;
- run or commit audit-loop results;
- edit audit ledger/effective-status files.

The useful output is narrow: latest `origin/main` had the source note already
fenced correctly, but the runner H5 predicate still expected the older
"bridge-chain dependencies" wording. The repair makes H5 check the actual
boundary: named inspection rows for re-audit, not proof inputs or status
authorities.
