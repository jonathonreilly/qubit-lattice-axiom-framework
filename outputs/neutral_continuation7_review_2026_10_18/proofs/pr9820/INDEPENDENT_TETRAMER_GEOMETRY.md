<!-- Original PR9820 source SHA256 01556ffcbe2b8917ad1ec344ee3bdbad39cf0a57b0df31164bc737f1693f4474. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Q8 perimeter-24 tetramer geometry check

Disposition: PASS for exhaustive finite-support geometry and the supplied D8 energy functional; conditional for its identification with the complete native D8 Hamiltonian. No repository edits or formal audit.

## Why the finite gap-type enumeration is exhaustive

Every occupied row and column of a finite plaquette syndrome has positive even cardinality. With eight plaquettes, there are between two and four occupied rows and between two and four occupied columns. Listing all even row/column incidence matrices in these dimensions is therefore exhaustive, irrespective of geometric diameter or inverse-column support size. The perimeter is 4*8-2*adjacency, so perimeter 24 is exactly adjacency four, as tested.

The finite inverse column configuration exists uniquely for an even-row/even-column syndrome. Its total parity equals sum_(x,y in syndrome) x*y modulo two: discrete double differentiation and summation by parts turn that moment into the sum of inverse bits. Translation changes the moment only by terms proportional to even row/column sums, so this criterion is origin independent. It does not restrict the inverse to four columns; long rods and other extended inverse configurations are included.

For the specified invariant patterns, the coordinate span is at most two along either axis. Their translated intersections, hence the odd-overlap counts, depend only on coordinate differences of magnitude at most two. Thus a gap >=3 has no further energetic distinction. Perimeter distinguishes only gap one. Inverse parity can distinguish odd and even large gaps, requiring the four categories 1, 2, odd >=3, even >=4. Representatives 1,2,3,4 are sufficient. This is a finite reduction of an unbounded geometric problem, not a finite bounding-box assumption. Periodic configurations wrapping around a small torus are not covered by this finite-support classification.

## Independent exact enumeration

I used a different enumeration of even row bitmasks and alternate far-gap representatives 5 and 6. I evaluated each odd-overlap count using inclusion-exclusion of translated-set intersections, rather than the root's symmetric-difference accumulation. Scratch code and output: /tmp/neutral_per24_reviewer.py and /tmp/neutral_per24_reviewer.json.

All 4912 accepted gap types and the entire energy histogram agree exactly. Reference energy is -23216 in the stated integer units. The minimum relative value is -5832, attained by precisely four oriented gap types. Up to translation and square symmetry these are two geometries of inverse columns:

- {(0,0),(1,0),(4,0),(5,0)}: two parallel collinear dimers;
- {(0,0),(1,0),(0,3),(1,3)}: two parallel dimers displaced transversely by three.

Rotating gives the other two oriented representatives. All minimum gaps are 1 or 2 at syndrome level, so none is an infinite far-gap family hidden by representative compression. The next relative energy is -2916, with 24 representatives; the separation from the minimum is 2916/21233664. The minimum -5832/21233664 simplifies to -9/32768. These are JL lambda^8 coefficient energies relative to the stated pair of distant neutral dimers, not yet exact eigenband gaps.

## Native-invariant caveat

The calculation takes the coefficients 729, -405, -464 over 21233664 and their pattern list as supplied input. Terms proportional to a constant, sum P, or nearest-neighbor sum P P do not distinguish this manifold: Q and nearest-neighbor syndrome adjacency are fixed. Their omission is therefore legitimate for relative energies if these are the only omitted terms.

However, an earlier perimeter-16 minimum classification alone is not a proof that every other native D8 invariant is either present here or constant on perimeter 24. A term constant on one restricted manifold need not be constant on another. To promote the minimum to a native conclusion, cite or supply the complete connected D8 graph classification and coefficient reduction, with its validity for all finite-support Q8 configurations. The present exhaustive geometry does not replace that source completeness argument. It establishes the stated minimum and separation for the supplied functional and does not by itself establish an isolated tetramer eigenband, dynamics, or scattering statement.

## SHA-256

- `/tmp/neutral_pair_q8_per24.py`: `544bb90c09c05d6f1255260fe0ea6199be9e6a12efab45707a50a9aef5176fbd`
- `/tmp/neutral_pair_q8_per24.json`: `228a6ca9ca2cd12013c1ac96d8e72355fa339e5f36d2147b2387e0fc2287780c`
- `/tmp/neutral_per24_reviewer.py`: `f90245de5e7f0d2c3b1994ac4cf494f5aab762a01f1b79a7a542ff1f212c53c9`
- `/tmp/neutral_per24_reviewer.json`: `2ae3deaa2edfe0d318dfa53cf89fca532bb0408f39be722190be32a107ae8bd0`
