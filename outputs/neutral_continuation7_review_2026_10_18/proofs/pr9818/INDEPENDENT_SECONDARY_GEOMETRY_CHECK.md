<!-- Original PR9818 source SHA256 b2fb3ee7a7e4bb16fbf2967e5e78d9c1a08935ed614c249fd032910ba68b6222. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Exhaustive finite-support Q8 / perimeter-16 classification

Disposition: classification completed; the bounded enumeration is correct within its box but misses an infinite family with arbitrarily many flipped columns. It must not be promoted to 'two columns plus eight four-column shapes' globally.

For a finite column set C define its bad-plaquette syndrome by XOR of the four plaquettes incident to each column. Finite-support inversion is unique. Up to translations and D4, all even-parity inverse sets with Q=8 and plaquette perimeter 16 are exactly:

1. **Two separated columns:** C={(0,0),(a,b)}, with a>=b>=0, and either a>=3 or (a,b)=(2,2).
2. **An odd rod plus a separated singleton:** C={(x,0):0<=x<=d-1} union {(d+1,0)}, for any odd d>=3. There is one missing site between the rod and the singleton. Its column count is d+1, unbounded.
3. **The T tetromino:** C={(-1,0),(0,0),(1,0),(0,1)}.

Reflections/rotations and translations generate all orientations. The d=3 member of family 2 and the T tetromino account for the eight oriented four-column examples in the supplied W=7 output. At d=5, six columns already occur and their bad-plaquette bounding box has width eight, just outside that enumeration.

## Incidence classification independent of a bounding cutoff

Let r,c be the numbers of occupied rows and columns of the bad set S, and let H,V be the numbers of horizontal and vertical adjacent occupied pairs. Since |S|=8 and perimeter is 16,

 H+V=8.

Every occupied row and column has positive even cardinality, so r,c<=4. Their binary incidence matrix contains eight ones and has even row and column degrees. Up to transposition the only possible dimensions are (r,c)=(2,4),(3,4),(4,4). A 3-by-3 matrix would have each row degree at most two, hence at most six ones; smaller alternatives similarly fail. This leaves only the cases below, with coordinate gaps unrestricted.

### Two occupied rows, four columns

Both rows contain all four columns. Write their ordered x coordinates x1<x2<x3<x4, and let a be the number of unit successive x gaps. Then H=2a. V is four if the rows are adjacent and zero otherwise. H+V=8 forces adjacent rows and exactly two unit x gaps: precisely one successive gap d is nonunit, d>=2.

If the nonunit gap is the middle one, finite inversion gives two isolated columns separated by d+1>=3 along an axis: family 1. If it is either outer gap, inversion gives a rod of length d plus a singleton one vacant site away. Even inverse parity requires d+1 even, hence odd d>=3: family 2. This is the source of the unbounded family. Transposition gives no new D4 class.

### Three occupied rows, four columns

The row degrees are (4,2,2), while every column has degree two. The two short rows partition the four columns into two pairs. Each pair's vertical adjacency contribution to the full row is either zero or two, so V is 0,2,4. Horizontal adjacency is at most five. Thus H+V=8 forces V=4 and H=4: the full row lies between the two other rows and all three are consecutive.

Let a be the number of unit gaps among the four columns, and b1,b2 indicate whether each short-row pair is adjacent. Then H=a+b1+b2=4.

- If a=2, both short-row pairs must be adjacent. They are two separated adjacent-column blocks, with the intervening gap nonunit. Inversion yields two columns separated by at least three in one direction and by one in the other, covered by family 1.
- If a=3, exactly one short-row pair is adjacent. Among partitions of four consecutive columns, only the outer pair {1,4} and inner pair {2,3} have this property. Inversion yields the T tetromino, family 3.

There are no other values because a<=3 and b1+b2<=2. Transposition adds only D4 images.

### Four occupied rows, four columns

Every row and column has degree two. Hence H<=4 and V<=4, so both must equal four. Every row's occupied pair is adjacent, and every column's occupied pair is adjacent.

View each occupied row as an edge between its two adjacent ordered columns. Every column has degree two in this multigraph, and edges can only join consecutive physical columns. Starting from the leftmost occupied column forces two copies of its edge to the second; this saturates the second column and forbids an edge to the third. The remaining two columns likewise form a repeated adjacent pair. Applying the same argument to rows shows S is two full 2-by-2 bad blocks on disjoint row pairs and disjoint column pairs. Their inverse is two columns with both coordinate separations at least two, exactly the remainder of family 1.

This argument uses no upper bound on empty gaps and therefore covers arbitrary separation and every disconnected bad-set geometry.

## Explicit missing-family check

For the odd-rod family,

 S={-1,d-1,d,d+1} times {-1,0}.

It has eight plaquettes. Its horizontal adjacent-pair count is four, vertical count four, so perimeter is sixteen for every d>=2. Every row contains four points and every column two; inverse parity is even exactly when d is odd. Direct XOR checks at d=3,5,7,11 give respectively 4,6,8,12 flipped columns, always Q8 and perimeter16.

## Boundaries

This classifies allowed finite-support geometry only. It does not assign eighth-order energies to the rod family or T shape, prove closure under hopping, or isolate an energetic band. In particular the unbounded rod family must be considered before treating the perimeter-sixteen manifold as a finite set of two-particle geometries. On a torus flat-background identifications and wrapping require a separate quotient; the classification here is the requested finite-support infinite-lattice result.

Read /tmp/neutral_q8_perimeter16.py and its JSON. No shared files edited and no formal audit.
