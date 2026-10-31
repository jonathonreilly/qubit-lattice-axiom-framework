# Independent exact checks: source-local return

Pre-stated in REVIEW_SOURCE_LOCAL_RETURN_ASTRA.md before new calculations.
This adds concrete implementation choices before running review_source_return_01.py.

1. A nine-vertex cycle with three boxes, one deleted integrated vertex, and
   diagonal coefficients reading the next vertex. Construct local inverses by
   characteristic-polynomial/adjugate methods, not the author's elimination.
   Check the signed right parametrix, all walks through three corrections,
   exact remainder, row and column bounds, marked incidence and connected full
   collars. Wrong sign/order must be detected. Change a source in the collar
   but outside the compression; the atom must change. A source outside the
   complete collar must have no effect.
2. A star-shaped matrix pair with a marked vertex in only the right factor
   must detect replacing the left column bound by its row bound.
3. Derive the derivative of -logdet/2 from the characteristic polynomial of
   [[2+z,1/3],[1/3,3-2z]] and compare with the trace formula. At z=0 the exact
   answer is 9/106. Missing half-factor or wrong sign must fail.
4. Exact projection Pi=[[1,-1],[-1,1]]/2, O=17I: one-coordinate compression of
   K=Pi O Pi+I-Pi is [9]. Subtracting compressed I-Pi from its inverse square
   root gives -1/6, contradicting a positive physical-square-root reading.
5. Use exact 2x2 complex rational SU(2) matrices on a graph with two anchors,
   rooted forest and a fixed collar edge. All tree edges, anchored transports,
   closed-loop traces and collar data must transform as required. Moving one
   anchor must preserve loop traces but fail anchored-transport/collar checks.
   Independently integrate a triangle trace square with normalized S^3 moments
   before and after tree gauge, and verify the SU(2) HS-chart Haar constant.
6. Enumerate scalar Taylor multi-indices and marked-factor counts for multiple
   a/source coordinate counts. Verify the degree+one and difference bounds;
   omitting the source linear term or the scalar-coordinate multiplicity must
   be detected. A local two-site cubic action's Picard Taylor coefficients
   through degree five must solve its stationary equation to that degree;
   suppressing remote dependence must fail.
7. For a polynomial holomorphic two-form and a complex affine source-dependent
   map, compute the two domain integrals and all four oriented swept faces by
   independent pullbacks. Correct Jacobian minors/orientations must agree;
   side omission and reversed side orientation must fail.
8. F(a;B,epsilon)=(a-B)^2/2 at epsilon=0 witnesses that comparison against a
   reference at B=0 has nonzero W displacement. The same-B reference removes
   this false O(rho p) inference. All examples are finite algebra diagnostics;
   none proves actual Yang-Mills operator uniformity or the return estimates.
