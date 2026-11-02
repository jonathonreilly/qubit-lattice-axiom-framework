# Pre-run criteria: independent exact alignment checks

Prior exposure: saved ALIGN3_55 formulas and its recorded outputs; no saved checker is imported or executed. Standard-library Python Fractions/integers only. These checks support the proofs in RECOVERY_ALIGNMENT_ASTRA.md; finite tests are not uniform-norm proofs.

P: For L=3 and periodic coarse counts 3,5,9, solve cyclic cubic-spline collocation from scratch. Build merged shortest-path M. Define image M in dimension one through the proved harmonic correction M_merged(I-h), independently derive S1 from dS0=S1d and its row sum 1/L, and require Md=I-S0R, M1=0, dM=I-S1B entrywise. Control: merged M must fail harmonic cancellation and completion for each count. This does not test the infinite image sums directly; their equality to the corrected M is the one-dimensional Hodge argument in the note.

C: Enumerate centered order-paired S4 contours in dimension four, L=3 and L=5. For every output direction require zeroth moments L delta, edge-midpoint first moments L^2 delta/2, and vanishing total quadratic BCH signed area. Controls: lower-corner offsets and a single transverse-offset contour must violate the corresponding first-moment/area cancellation. This tests the exact moments used in the new direct AC proof. General L and d require the explicit contour formula in the note.

A: On the same four-dimensional L=3 contour average, use explicit noncommuting affine Lie-algebra fields and affine gauge functions, with the next-level background set to B y. The principal commutator residual must be nonzero, have no degree-two term, and scale exactly by 1/27 when the fine mesh shrinks by 1/3. Control: an uncentered family must retain a nonzero degree-two contribution for constant background and affine gauge function. This is a local polynomial check, not a global periodic gauge witness or an analytic remainder bound.

W: Recompute the G0 completion Y exponent theta+alpha-1 at alpha=1/4, theta=1/2 and verify nonpositive on depths 1..40; retain a control alpha=3/4, theta=7/8 with positive growth. Check positive-level G and s sums algebraically in the note. A positive control exponent only refutes extending this particular upper-bound argument; it does not refute P2 outside the window.

Higher-dimensional PER-3/4 are checked by a separate chain-contraction proof, not by a claimed exhaustive matrix calculation. No spline norm constant, full SU(N) analytic tail, infimum lower bound, weighted theorem, or physical Yang–Mills conclusion is numerically certified.
