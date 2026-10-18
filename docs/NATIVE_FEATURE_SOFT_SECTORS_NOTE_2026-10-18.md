# The large native feature has many soft symmetry sectors

Status: bounded-support. The extended-defect construction implies at least
2^(2m-1) heavy levels, counted with multiplicity, within an
O(Jlambda^(5/2)) window, with m proportional to lambda^-3/4.

The [proof](../.claude/science/physics-loops/neutral-composite-24h-20261018/native/FEATURE_SOFT_SECTORS_PROOF.md)
uses exact plane symmetries to generate orthogonal patch states. Local
native terms cannot connect their distinct internal patterns at the retained
order. Minmax in the exact odd-parity space counts actual heavy levels and
avoids accidentally counting the vacuum. The remainder is an operator-norm
bound, so the large state count does not amplify it.

This is also a constraint: the original neutral readout cannot connect the
different symmetry characters. The count is not a collection of visible
scalar oscillators or a derivation of fermion species. Dynamics within a
single character remain open.

[Replay](../scripts/native_feature_soft_sectors.py) verifies the finite
subgroup rank, flat patterns and minimum physical flip count. The result
remains conditional on the supplied one-qubit Hamiltonian and slab limit;
no empirical identification or new interaction is introduced.
