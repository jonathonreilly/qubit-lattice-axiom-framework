# Opportunity Queue

1. Audit-ready FSB-K after U4 dependency removal
   - Impact: high.
   - Why: retaining FSB-K would activate the P-FLUX composer using already
     retained Z geometry.
   - Missing imports: none identified in this block.
   - Runner availability: strong, `frontier_axiom_first_fermionic_stefan_boltzmann_narrow.py`.

2. Kinetic-class forcing surface audit
   - Impact: high.
   - Why: needed to move from selection within the two-class surface to broader
     P-KIN closure.
   - Missing imports: audit/review of the kinetic-class row.
   - Runner availability: existing row/runners need separate review.

3. FSB-K finite-L constants
   - Impact: medium.
   - Why: would reduce a declared numerical finite-grid residual, but is not
     required for the current conditional composition.
   - Missing imports: analytic finite-size estimates.
   - Runner availability: current mode-sum runner.
