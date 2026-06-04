# Goal

Repair the SU3 Wigner L_s=3 treewidth diagnostic so its memory-unit convention
and Section 2 truncation bound match the runner's binary 4 GiB budget.

The intended outcome is bounded-support cleanup only:

- correct the truncation threshold from about `1.8` to about `1.91`;
- label binary memory quantities as `GiB`;
- preserve the existing conclusion that integer truncation still permits only
  bond dimension `1` under this naive bound;
- keep the diagnostic scoped to min-degree/min-fill heuristic upper bounds and
  avoid any bridge-promotion claim.
