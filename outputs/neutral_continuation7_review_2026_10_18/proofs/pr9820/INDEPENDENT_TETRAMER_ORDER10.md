<!-- Original PR9820 source SHA256 c4aa0eccd960b18f6f11c1ffebd71c86fc615aa00f5c2e500bc4e6054e0b92f3. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Tetramer D10 geometry and one-edge selection

Disposition: PASS for the combinatorics and supplied primitive coefficients. The complete native D10 coefficients/invariant list remain the separate domain review's input. No repository edits or formal audit.

I independently evaluated translated plaquette-product signs directly, using signed coordinate permutations for square orbits, rather than the root's symmetric-difference count. Code/output: /tmp/neutral_tetramer_d10_reviewer.py and .json.

Let A be columns {(0,0),(1,0),(4,0),(5,0)}, B={(0,0),(1,0),(0,3),(1,3)}. Primitive polygon orbit counts and contributions to B-A are:

| Polygon | A count | B count | contribution |
|---|---:|---:|---:|
| straight tetromino |16|24|143/2097152|
| L tetromino |136|128|55/2097152|
| P pentomino |136|128|55/2097152|
| 2x3 rectangle |28|24|-143/4194304|
| T tetromino |56|56|0|
| skew tetromino |68|72|35/4194304|

Their exact sum is 199/2097152. The sign uses -2*c*(countB-countA) for a Hamiltonian product coefficient c: an odd syndrome overlap changes the plaquette product from +1 to -1. Thus no sign or factor-two discrepancy was found.

The six simple length-ten square-lattice polygon families are complete. Their enclosed connected cells have bounding dimensions w+h<=5 and area at most floor(25/4)=6. Up to rotation, the nontrivial boxes are 1x4 and 2x3 (smaller boxes cannot add another perimeter-ten family). Direct connected-subset classification gives the four perimeter-ten tetrominoes I,L,T,S, the corner-missing 2x3 P pentomino, and the full 2x3 rectangle. No hole is possible at this perimeter. The code's growth through six cells consequently suffices for this primitive class; it does not enumerate all repeated-edge native diagrams.

The additional orbit counts independently agree:

- PP displacement (2,0): 20 versus 20;
- PP displacement (2,1): 52 versus 56;
- skew triple {(0,0),(1,0),(2,1)}: 136 versus 144.

All cited older invariant counts agree between A and B: straight-three sum 20, box 16, L-triple sum 64, diagonal-pair sum 32. Renormalizations of these square-summed invariant orbits therefore do not split A and B. This does not license omitting an unclassified new D10 invariant.

For the one-edge test, I enumerated all four translation-normalized oriented minimum column sets. Any adjacent-edge XOR mapping a four-column minimum to another four-column set must intersect the initial set in exactly one endpoint. Thus the finite list of edges incident to its four columns is exhaustive, including all translated targets. None of those outputs is a translated or rotated minimum. This is an analytic finite reduction, not a cutoff on target translations.

Therefore the inherited order-ten native winding term, which flips one adjacent column pair at fixed height ten, has no off-diagonal matrix element within this minimum manifold. More generally a different nonadjacent two-column flip needs more than ten microscopic transverse edges, and a four-column change needs at least twenty; no additional order-ten off-diagonal term is supplied by those possibilities. Diagonal D10 splitting is allowed. Virtual excursions can produce later-order effective hopping and are not excluded by this result.

## SHA-256

- `/tmp/neutral_tetramer_d10_shapes.py`: `54e84389874e40a9baef3700360503eac3f8811aac7cfbc6574983a05bfd3524`
- `/tmp/neutral_tetramer_d10_reviewer.py`: `feb3a8befe416213f183904a46407382063a846b5fe8e7ef0e811ea5962b7cf8`
- `/tmp/neutral_tetramer_d10_reviewer.json`: `8b1df5136a70be1319953e95b66b59e2cb83883cb318aba51d7cabd93ac893f7`
