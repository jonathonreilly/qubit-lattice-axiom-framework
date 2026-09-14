# Source-level exclusions from the campaign assumptions

PR8122 inspected at head `a293aa3b67d64eda29ba959d43c209056c9ef7e4`.
This is a narrow author reading for safe reuse, not an applied audit or a
request to drain/repair another lane. Source note sections through Theorem 7
and selected runner definitions/checks were read. No independent reviewer was
used. The whole runner was not audited or executed here.

1. The note's Theorem 3 table labels its final two columns as lattice-vector
   output, but the runner's `VL` table uses `out='veclat'`, the tensor product
   of internal-vector and lattice-vector outputs. The scalar at degree zero
   on the soldered empty stratum is the invariant identity frame, not a fixed
   vector. A vector fixed by all proper cubic rotations must be zero (the
   pi rotations about x and y already suffice). The runner separately checks
   `out='lat' == out='vec'` in the soldered reading; that is consistent, but
   those are not the displayed `VL` columns. Do not reuse the table with its
   displayed labels.
2. The headline excluding every unsoldered linear covariant rule is broader
   than the scalar statement actually checked. The internal-vector map p->p
   is a degree-one equivariant map, and the note's own vector table contains
   it. Restrict the scalar claim before using it.
3. Theorem 6 describes a +x neighbour whose Bloch vector also points +x and
   says the unsoldered barycentre rule gives 1/2 on the x menu. Its displayed
   formula gives (1+1/3)/2=2/3, the same as the soldered rule for that input.
   The runner instead sets `TQ[4]=(1,0,0)`, with slot 4 equal to +z. That
   perpendicular orientation can give the intended separation; it is a
   different input from the prose witness. The existence of a corrected
   finite witness is not an audit of every axiom-satisfaction assertion.

These findings do not refute all invariant calculations or establish an axiom
inconsistency. They show why counts and PASS summaries must not be imported
without matching the object, output representation and witness input.
