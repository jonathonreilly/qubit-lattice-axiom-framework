# Integrated source check

Date: 2026-11-08. Scope: narrow source-exposed continuation of INDEPENDENT.md,
not a second independent rediscovery, landing review or audit. Read the entire
gb1-cf-pair/Physics/.claude/science/physics-loops/gb1-cf-boundary-gluing-20261107/
local_implementation/RESULT.md at SHA256
235658471216f23f3ea1231cf475b369a5e4412cc6baa85684b25f9ac28d9ac2.
Compared its three repairs and added gate bounds with the prior proof check.
Neither the frozen independent file nor the source was changed. No numerical
run was performed; diagnostic execution claims in the source were not reaudited.

## Repairs checked

1. Simultaneous scratch is now disjoint. The herald uses 12n^3-1 sites with
   residues (i,j,0), 1<=i<=4, 1<=j<=3. Controller sites have residues
   (i,j,1), 1<=i<=4, 0<=j<=4; all have two nonzero residues and hence lie
   in F_p. The two banks are disjoint globally, not just within one cell.
   They offer 12n^3 and 20n^3 sites respectively. Controller demand is at
   most 3M+1, and total simultaneous demand is at most 12n^3+3M<112n^3
   under n>=2M+8. No qubit assumed clean is simultaneously holding a live
   controller copy or indicator. Routing uses returned carrier permutations
   and requires no additional clean qubits.
2. Failed-herald guarding now omits every k>=1 clause with h_1=0 and
   explicitly disables subsequent recipe AND registration ports. A failed
   stable first herald has f_1=1,y_1=0: k=0 fails its f_1=0 test, while
   every retained later clause requires y_1=1. No operation is enabled.
   The current macrostep still completes its stated value-then-completion
   append before this stable-boundary halt is applied. At N=1 both first
   outcomes are terminal after that completion. The guarded protocol therefore
   has the advertised absorbing failure, without resetting its permanent value.
3. Routing coordinates now explicitly use marker center a and its recovered
   oriented frame. Together with frame-ordered work allocation this removes
   the residue-representative ambiguity under coarse translations. The connected
   complement argument and D=30n+2 bound remain valid. Old record sites are
   never routing interiors or targets; reading uses them only as CX controls.

## Added gate bounds checked algebraically

One masked-copy pass uses d header CX gates, N flag CX gates, and per value
two temporary-bit CX gates plus one five-pair Toffoli: d+N+7N=d+8N pairs.
The inverse pass has the same cost. This includes masking future values and
returning its temporary bit, including when the new pointer is entangled.

A predicate has t<=M+1 nonconstant controls. Its AND chain requires t-1<=M
Toffolis, and compute plus reverse uses at most 2M Toffolis or 10M pairs.
Conjugating negative controls before and after costs at most 2(M+1) onsite X
gates. For k=0 the f_0=1 constant is omitted. At d=1 its remaining two
controls still fit this chain/count; no zero-control corner case is hidden.

For the declared X/H and CX/CV/CV-dagger/SWAP alphabet, adding one selector
costs one pair for an onsite gate, five pairs for CX or CV (using an exact
square root for CV), and seven pairs for SWAP via CX,CCX,CX. These reductions
need no additional clean work. Thus 7P_beta+S_beta is a valid loose bound for
the controlled branch word. It is not a bound for an arbitrary unspecified
two-qubit gate without its own controlled decomposition.

With P_herald=48m-9 and S_herald=8m, the bound is exactly
7(48m-9)+8m=344m-63 abstract pairs. This correctly counts the controlled
herald rather than reusing its uncontrolled count.

Summing predicate and controlled-word costs over at most
B=2^d sum_(k=0)^(N-1) 2^k=2^d(2^N-1) candidate clauses, then adding the two
copy passes, gives the displayed total
[2(d+8N)+sum_beta(10M+7P_beta+S_beta)](2D+1) adjacent pairs and at most
2(M+1)B onsite gates. A route of length l<=D uses 2l-1 adjacent pairs;
2D+1 is therefore safe also for record-control access. Omitting failure
clauses reduces counts. The sum may safely retain them as an upper bound.
Registration, flag flipping/registration and physical timing are explicitly
outside this unitary-cycle count, as they must be.

## Disposition and limits

No remaining correctness defect was found in this requested source scope.
The rank-one herald, passive-reference identity, old-record preservation and
masked-copy cleanup remain consistent with the earlier detailed check. The
integrated source now resolves all three previously reported repairs.

This confirms a conditional finite driven construction at stable macrostep
boundaries. It does not derive quantum gates, clean preparation, gated Record
formation, microstep scheduling, arbitrary magnetic evolution synthesis or
an autonomous record-only law. The six-edge mixture remains expressly outside
the all-work-clean recipe contract. Finite-run evidence and unrelated claims
were not independently inspected in this narrow follow-up.
