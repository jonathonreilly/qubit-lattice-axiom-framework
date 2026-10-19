<!-- Original PR9817 source SHA256 1e2f32e67724914409b5b0cc92f1ebac53fde7628a8d5d04844e73940cd5444d. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Order-ten pair coefficient: independent rational check

Disposition: PASS for every supplied graph/layer-assignment coefficient and their sum. Graph completeness is explicitly outside this check and remains the other reviewer's obligation. At L=10 interpret the result as a matched diagonal effective-H coefficient, not an isolated nondegenerate eigenenergy: winding also begins at order ten.

## Independent algorithm

I used a vacuum Feshbach self-energy calculation rather than the root Rayleigh wavefunction recurrence. For each labelled edge subset S I summed irreducible paths, terminating whenever they returned to the reference vacuum. Each nonvacuum resolvent was expanded as

 (E-cost)^-1=-sum_(j>=0) E^j/cost^(j+1).

Keeping j<=4 suffices for ten insertions because the lowest possible energy coefficient has degree two. This constructs Sigma(E) as a polynomial in E with coefficients in the squarefree edge-variable ring. I then solved E=Sigma(E) by finite fixed-point substitution in that ring, retaining all disjoint-mask products. This supplies the folded terms through a mechanism independent of the root's energy-times-wavefunction subtraction.

The only reused helper was the geometric decoding of the supplied graphs into their specified layer-labelled edge lists. The coefficient recurrence, denominators' energy expansion, fold generation and comparison were independently written. All 26 supplied graph/layer cases agree exactly as Fractions, not within a floating tolerance.

## Critical folded coefficients

For each touching four/six pair:
- Same layer: 7/2097152.
- Adjacent layers, either sign: -425/452984832.
- Separation two: zero.
- Layer-summed total: 331/226492416.

For the doubled-bridge four/four graph, with first square at z=0:
- Both squares and bridge at zero: -49/16777216.
- Cases with one square coplanar with the bridge and the other on an adjacent layer: 635/764411904 (four assignments in the supplied sum).
- Cases where both square layers are adjacent to the bridge layer, including equal or opposite sides: -157/536870912 (four assignments).
- Disconnected bridge-layer cases: zero.
- Layer-summed total: -75101/97844723712.

The six primitive cycle coefficients also agree: four are 55/33554432, one is -143/33554432, and one is -35/33554432.

Thus the total supplied connected graph coefficient is

 333355/97844723712,

and the connected two-column contrast is four times this:

 V_(0,0),(3,2) = JL lambda^10 *333355/24461180928.

## Repeated-bridge normalization

The two occurrences of the same physical bridge are temporarily distinguished as variables x1,x2 in the subset calculation. Replacing the physical coupling by x1+x2 makes a physical x^2 monomial contribute 2 x1 x2. Therefore the labelled squarefree coefficient must be divided by 2!, exactly as the root does. This is not an extra symmetry factor to be applied a second time after the layer sum. Both copies of that bridge must occur on the same physical layer in these supplied returning words; placing one copy at each of two layers leaves odd physical flip degree unless additional edges are supplied.

## Denominators and scope

For the small embedded supports, the exact longitudinal cost is 4 per flipped spin minus 4 for each adjacent simultaneously flipped vertical pair. The independent calculation uses that same physical H0, with all vertical exterior neighbors unflipped. The largest listed layer span is safely nonwrapping for L>=10; negative offsets represent the neighboring layers consistently. No denominator vanishes for a nonvacuum subset in these graphs.

At L=10, another aligned configuration can first be reached at ten transverse insertions. It is not a proper intermediate subset of these diagonal ten-word returns, so it does not invalidate the calculated diagonal coefficient. It does mean the full order-ten N0 effective Hamiltonian also has winding off-diagonal entries, and the displayed pair contrast alone must not be called a nondegenerate physical energy shift or a full potential/scattering result. For larger height, winding is later.

The factor-four contrast assumes the supplied graph's background monomial contains each of the two designated column signs once. It is then the exact finite difference E(both)-E(first)-E(second)+E(neither). Counting all geometrically possible graphs with that property is not proved by agreement of their individual coefficients; no completeness conclusion is claimed here.

Independent artifacts: /tmp/neutral_order10_reviewer.py and /tmp/neutral_order10_reviewer.json. Read root /tmp/neutral_order10_pair.py and /tmp/neutral_order10_pair.json. No repository edits or formal audit.
