<!-- Original PR9817 source SHA256 77aa68399d832d139c81c523a428e095569844634c7f164036736d6b2c10eccc. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Independent check: plaquette-dependent winding detour

The subset DP, signs, source mark and classification support the proposed coefficient for even fixed height on a transverse grid without short wrap aliases. The plaquette-dependent order-L+2 correction must not be replaced by a scalar renormalization of winding.

## Independent enumeration

I wrote `/tmp/neutral_detour_winding_independent.py`, applying XX/YY directly to coordinate sets of down spins for every ordered word, with no subset-DP reuse. Exact permutation sums give:

L=4: per-layer -127/110592; all layers -127/27648; derivative ratio 5669/1016.
L=6: per-layer -14051/63700992; all layers -14051/10616832; derivative ratio 3882135/449632.

These independently reproduce the parent DP on all 720 and 40320 words, respectively. I also replayed the root DP through L=12. Its L=10 output is

d10=1076510135/10567230160896,
B10=1616665793187/110234637824.

The twelve distinct insertions at L=10 represent 479001600 ordered words, so subset summation rather than permutation replay is appropriate there. The small-height direct enumeration verifies its recurrence, including the marked denominator factors.

## Operator signs and intermediate states

On an initially aligned complementary layer, the two detour YY bonds give their initial column-sign product s0 s1 s2 s3. Their evolving spin signs are retained by the code. The final action flips complete columns 0 and 1, so the resulting background operator is P E_edge. P and E_edge commute because the plaquette contains both flipped columns. The all-positive-background calculation therefore fixes the displayed negative coefficient of P E for general backgrounds; it is not merely a calculation for P=+1.

No nonempty proper subset of these distinct detour/direct insertions returns to N0. A partial detour leaves an auxiliary column with an incomplete flip, and all other layers contain only the direct edge. A complete detour restores the auxiliary columns but leaves the target columns incomplete unless every other layer is also flipped. Thus the resolvent-only sum for this squarefree detour word has no missing model-space intermediate denominator.

## Exhaustion at order L+2

For a transition flipping exactly two neighboring whole columns, every layer must have odd incidence precisely at those two sites. A layer therefore contains an odd number of transverse insertions, at least one. With L+2 total insertions, exactly one layer has three and all others have one. At each ordinary layer its sole edge must be the original edge.

At the exceptional layer, the three-edge multigraph with this boundary is either a three-step simple path between the neighboring endpoints or the direct edge plus a doubled edge (including the direct edge repeated three times). On a nonaliased square lattice the simple paths are precisely the two detours around the two adjacent plaquettes. A direct edge plus repeated bond has only the direct edge in its modulo-two graph. Repetition can change the numerical amplitude or create disconnected cancellations, but supplies no new background Z monomial. It is therefore a scalar winding correction, not P-dependent.

At this order folds can combine leading order-L winding with order-two scalar returns. They remain background independent. A plaquette-dependent diagonal return starts at order four and cannot combine with an order-L-2 background-changing path, because such a path is forbidden by the physical flip count. Consequently folds do not change the P E coefficient. Summing the exceptional layer gives the factor L already included in d_L, and summing the two adjacent plaquettes supplies the stated edge/plaquette sum without an additional factor two in each individual coefficient.

## Source derivative

For the derivative device H+h sum ZZ_distance2, an intermediate configuration with N nearest vertical mismatches and D2 distance-two mismatches has excitation cost 2JN-2hD2. Differentiating its inverse negative energy denominator gives the logarithmic factor D2/(JN). Thus every word's derivative is its original amplitude times the sum of D2/(JN) over proper intermediate states. This is exactly the marked recurrence and the independent enumeration above.

Accordingly d'_L/d_L=B_L/J at h=0, with h having energy units and the source being the unnormalized uniform sum. A normalized source introduces its separate volume factor. This checks the coefficient derivative; identification with the matched observable in a parameter-dependent canonical frame also requires the connection commutator, which is not silently discarded here and remains part of root's source calculation.

The source parameter is a derivative device, not an adopted additional interaction. The result is a fixed-height perturbative coefficient with native signs. It neither supplies an all-height closed form nor establishes a new Q8 mode, transition rate or empirical coupling on its own.
