# Manual finding after passing finite checks

The original side4 construction places enlarged boxes at lattice distance1.
They are disjoint as closed coordinate sets but can be Chebyshev adjacent.
The original program checked disjointness only, so it passed while missing
the stronger claim of uniformly finite enlarged lattice components.
The revised construction uses side6 blocks, central coordinates2/3 and
random origin in{0,...,5}^4. Enlarged boxes are separated by at least3,
which excludes even Chebyshev adjacency. The sign/noise limit and all
moment/probability formulas are unchanged. The previous passing source,
output and note are preserved, not relabeled as a program failure.
