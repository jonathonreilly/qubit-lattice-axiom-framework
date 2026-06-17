# Route Portfolio

| Route | Score | Result |
|---|---:|---|
| Patch source note to call B-W chain rows "dependencies" | 0 | Rejected. That would overstate the graph/proof role and contradict the note's "not proof inputs" boundary. |
| Patch runner H5 to check named inspection rows and not-proof-input firewall | 3 | Selected. It closes the live runner failure while preserving source honesty. |
| Attempt to derive B-W normalization in this PR | 1 | Rejected for this block. That is frontier physics and would not be a runner-hygiene repair. |
| Remove H5 entirely | 0 | Rejected. H5 is useful audit-unlock hygiene when it tests the correct boundary. |
