# Assumptions And Imports

## Native Inputs

- Finite even periodic Z4 lattice with `L in {4,6}`.
- Staggered grading `epsilon(x)=(-1)^(x0+x1+x2+x3)`.
- Finite U(1) link phases supplied directly by the runner.
- Principal-branch plaquette angle sum is the finite invariant asserted for
  the displayed background.

## Imports

- No new literature theorem is used as a proof input.
- Fujikawa, Wess-Zumino, and index-theorem material remains motivation only.
- The branch does not import a nonzero lattice index theorem; the observed
  index stays zero on the tested small boxes.

## Retired Ambiguity

The source no longer describes the background as constant local plaquette data.
The runner proves:

```text
sum_{x0,x1} Arg P_01(x0,x1,x2,x3) / (2*pi) = 1
```

for each fixed `(x2,x3)`.
