# Handoff

Block242 closes the remaining static, row-reduced O10 q=4 problem. After four
declared trace-normalized `I/3` column pairings, the complete rational `3^8`
row tensor is `K10=C^dagger/243`, with 81 nonzeros and 0/6561 mismatches. The
raw cup obeys `C^dagger C=3I`; hence `K10 C=I/81`, the cup-complement leakage is
zero, and the operator has rank 27. This fixes the entire 91-coordinate
equivariant O10 obligation at once and recovers Block240's `2/27` determinant
overlap as a consequence.

No axioms or primitives changed. This is not the unrestricted sixteen-index
endpoint or a full q=4 response. Different column closures, the nested temporal
multipliers, physical Q, four Gram histories, reachability/observability, and
minimal memory remain open. Next: assemble the supplied pair/triple/quadruple
operators on the exact Block241 O01 cycle and Block242 O10 cup maps, then apply
physical Q. Block241 is open as review PR #7795 and Block242 is open as stacked
review PR #7796; do not merge either PR in this campaign.

Block243 isolates the first exact dynamical obstruction. With
`Chat=C/sqrt(3)` and `P_C=Chat Chat^dagger`, the complementary one-leg
four-strand operators have the cup-complement bridge

```text
Delta4 = Chat^dagger R_(pDEF) (I-P_C) R_(ADEF) Chat.
```

It is scalar on total spins `J=0,1,2,3` but generically nonzero for
`J=1,2,3`; at `(t,u,v,w)=(3/10,2/5,1/2,3/5)` its exact sector values are
`(0,49/1800,-29/5000,-1097/176400)`. Therefore the static cup map is a
control, not a license to multiply independently compressed temporal weights.
This local bridge is an exact warning against inserting an intermediate static
cup projector, but it is not the mechanism of the full eight-axis Haar network.
The apparent O10 post/pre mismatch was instead a bookkeeping error: the first
comparison used the O01 selected-power census `Counter({1:16,2:8,3:10,4:8})`.
The exact O10 census is `Counter({1:17,2:8,3:11,4:7})`. Haar-projector sliding
to the Block242 cup cut, followed by orthogonality in the nested Block241
`EF subset DEF subset V^4` chain, proves that only the 19 globally coherent
paths survive and fixes their coefficients to `(2K+1)/243`. The full network
checker passes 90/90 projector-resolved checks. The same transport proof,
including `Pi_J^(pADEF) C = C Pi_J^(DEF)` for the power-five insertions, gives
the other three O10 histories. All four formulas match the direct network at
eight rational samples over three primes; the expanded certificate passes
138/138 checks, while an independent all-history projector checker passes
182/182. The four formulas are the exact O10 contribution, not yet the combined
physical response: Block239's quadratic Gram expression also requires all four
O01 histories. Next: derive those through Block241's non-diagonal `P/243`
kernel, combine both orientations, then apply physical conditional-Haar `Q`
without identifying it with the static cup projector.

The O01 proof gate is now closed. At the extra `h2` degree-two cut,
`H2=(1/3)|cup><cup|` and the `p1,A` cup lies in even spin zero, so this cut
contributes one rather than a ninth `x_L`. The two degree-five cuts reduce to
`DEF` and add `y_J^2`. Block241's physical cyclic permutation intertwines the
right and left nested path projectors; mixed labels vanish and `P^dagger P`
cancels in the closed Gram. The four O01 formulas and four O10 formulas are
therefore exact, and the expanded direct all-link checker passes `247/247`.

With one-side factors `T_Y=t^7 x_L^4 y_J^9`,
`T_Z=t^8 x_L^4 y_J^4 z_K^5`, `T_01=t^8 x_L^4 y_J^6 z_K^3`, and
`T_10=t^9 x_L^4 y_J^7 z_K^2`, the stripped combined response is

```text
sum_P4 (2K+1)/972 [
  (T_Y+T_01)(T_Z+T_01) + (T_Y+T_10)(T_Z+T_10)
].
```

At fixed `delta0`, normalized Haar means of the vector endpoints vanish, so
all first-order histories lie in `ker Q`; the supplied `[C,Q]=0` preserves
this through the crossing. Thus `(I-Q)` acts as the identity on this history
span. This is physical conditional-Haar `Q`, not the static cup projector.
The stripped identity control is exactly `2/3`. Fresh independent review and
the focused review loop both pass. The full repository pipeline still stops at
the inherited dependency-policy epoch-manifest mismatch on the parent stack;
strict audit lint has no errors and no audit verdict was applied. The next
science gate is Gram positivity/minimal history memory, then comparison with
the arbitrary-r scalar-fused transfer route. No axiom or approved primitive
changed.

Block243 is open as stacked review PR #7797 on Block242 PR #7796. Do not merge
either PR in this campaign.
