# Route Portfolio

| Route | Score | Outcome |
|---|---:|---|
| Prove a retained off-seed selector | 3 | Not available in this block; no native selector found. |
| Convert the parent row to interval support plus selector firewall | 3 | Chosen. It directly targets the numerical-match overread without narrowing the interval computation away. |
| Remove the interpolated root entirely | 1 | Rejected; loses useful reproducibility data and narrows more than needed. |
| Leave row unchanged and wait for audit | 0 | Rejected; does not unlock the current `audited_numerical_match` source issue. |

The selected route preserves the useful interval witness while preventing the
root from being treated as an observed-target proof.
