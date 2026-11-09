# Monotone routing in a finite Z3 box

2026-11-08: checked the specified algorithm mathematically; no numerical run
or source-diff inspection. This amends only the previous routing argument.
Let L=5n and B={a+sum_i x_i e_i: 0<=x_i<L} in the recovered marker frame.
V consists of sites whose three coordinates are multiples of five.
For u outside V, if y,z are multiples of five, x is not. Increasing y by
one stays in B since y<=L-5 and avoids V because x is unchanged.
Now y or z is not a multiple of five, so moving x monotonically to 1
avoids V. With x=1, move y and z monotonically to 1. All steps remain in B;
none uses modular wrap. This gives a path to the common hub (1,1,1).
Each path costs at most 1+3(L-2), since L>=3 and every coordinate distance
to 1 is at most L-2. A V endpoint first takes +e1, which stays in B since
its x<=L-5 and reaches a nonvertex. Thus connecting two endpoints via the
hub costs at most 2[1+3(L-2)]+2=30n-8<30n+2. Deleting loops preserves
the bound and the exclusion of V from path interiors.
Returned-SWAP conjugation therefore implements each abstract pair exactly
using literal nearest-neighbor Z3 edges, with the prior record protections.
This includes seam-spanning logical reader pairs: they must use the box route,
not a separate shortcut based on toroidal adjacency. Frame-anchored choices
transport with the prepared apparatus, and all earlier gate bounds remain safe.
Conclusion: the specified finite circuit embeds in this literal Z3 box.
Periodic gauge labels can still be used, but this proves neither that their
wrapped Hamiltonian is physically finite-range nor an infinite/continuum limit.
