# Additional literature falsification criteria

Declared after reading the indicated external theorem statements and before
executing the new exact checker. These are separate from the frozen Wilson-unit
diagnostics; they do not revise their tolerances or acceptance criteria.

1. An operator lower comparison does not imply an upper comparison on the vacuum
   complement. Test commuting, strictly positive, vacuum-normalized 2 by 2
   matrices, with zero remainder and identity compression. The claimed inference
   is falsified if its premise holds and its asserted upper bound fails.
2. The counterexample must fail a genuinely stronger, correctly oriented upper
   comparison. This control distinguishes an invalid inference from a sign error
   in the checker.
3. Summability alone must not be treated as a small total defect budget. Use an
   exact geometric series with sum exceeding the initial gap.
4. For vanishing lattice spacing, an unweighted summable error sequence need not
   remain summable after division by the spacing. Use rational powers of two.

Exact rational arithmetic is sufficient; there is no numerical tolerance or
parameter search. The targets are the main-paper equations (11.1), (11.5),
(11.7), (11.8) of Faizal–Shabir, arXiv:2606.19362v1. Only the first implication
is a direct counterexample to a displayed proof step. The other two checks
identify assumptions that such a transfer argument must establish separately.
