# Assumptions And Imports

## Imported From Parent Blocks

- PR #2804 K-Z external-lift gate:
  - Do not land the K-Z package while `W_lift = 0.05` lacks explicit finite
    `SU(3)`, Wilson `beta=6` source/reproduction support.
- PR #2808 K-Z convention split:
  - The paper action coefficient and standard Wilson coefficient imply
    `lambda = N^2 / beta`.
  - For `N=3`, Wilson `beta=6` maps to source-paper `lambda=1.5`.
  - The old narrow `W_lift ~= 0.05` width matches the plotted `lambda=3.0`
    image slice, not the Wilson `beta=6` coordinate.

## Used In This Block

- Standard support for normalized finite `SU(3)` Wilson loops:
  `(1/N) Re tr U` lies in `[-1/3, 1]`.
- Support-only SDP ingredients considered here:
  - plaquette Hankel PSD;
  - shifted Hausdorff PSD on `[-1/3,1]`;
  - Wilson-loop Gram PSD on `{1,P,R,Q}`;
  - endpoint-compatible area-style inequalities such as `r1 <= p2` and
    `q1 <= p4`;
  - admitted lower-bound comparator `p1 >= 0.4225`.

## Not Imported

- No primary source-data bracket at `lambda=1.5`.
- No repo-owned beta-coupled Migdal-Makeenko / Schwinger-Dyson equation set.
- No observed plaquette value, fitted beta, or old `W_lift` shortcut as a proof
  input.
