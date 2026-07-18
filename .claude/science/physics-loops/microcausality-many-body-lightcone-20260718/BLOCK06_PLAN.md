# Block06 plan — directional-tilt refinement of the bond-class walk bound

Date: 2026-07-18. Sixth block, final one planned this session under the
standing lane directive. Takes the sharp-rate item PARTIALLY: a
certified rational-tilt refinement of the bond-class cone constant,
axis-aligned, explicitly not optimal.

## Inputs (worker b06, graded correct against independent supervisor derivations)

- Height function phi(b) = sum of the two x_1-coordinates. Neighbor
  height-change tables (enumerated, box-stable): parallel start
  {-2:1, -1:4, +1:4, +2:1}; transverse start {-1:2, 0:6, +1:2}.
- Tilt polynomials S_par(y) = y^2 + 4y + 4/y + 1/y^2,
  S_perp(y) = 2y + 6 + 2/y; S_par - S_perp =
  (y-1)^2 (y^2+4y+1) / y^2 >= 0, so S_par dominates for y >= 1
  (exact factorization). S_par(1) = S_perp(1) = 10 (sanity).
- Walk-tilt inequality (worker derivation verified line-by-line;
  standard tilted count): #\{k-bond walks from a start set with height
  gain >= m\} <= N_start * S_par(y)^{k-1} * y^{-m}, y >= 1.
- Offset: start bonds touching {x_1 = 0} have phi in {-1, 0, 1}; end
  bonds touching {x_1 = d} have phi >= 2d - 1; gain m >= 2d - 2.
- Velocity bookkeeping: series sum_k (2J)^k t^k/k! N S^{k-1} y^{-(2d-2)}
  = (N y^2 / S) y^{-2d} (e^{2 J S(y) t} - 1); decay once
  2d ln y > 2 J S_par(y) |t|, i.e. v(y) = J S_par(y) / ln y.
- Rational scan: best at y = 5/2: v = (1801/100) J / ln(5/2),
  advisory ~ 19.66 J, vs parent readout 20eJ ~ 54.37 J (exact ratio
  2000 e ln(5/2) / 1801, advisory ~ 2.77).

## Theorem to land

Axis-aligned refinement on the BOND class (qubit siblings' class):
for X, Y separated by m >= 1 along a coordinate axis (Y inside
{x_i >= a + m} with X inside {x_i <= a}), for every rational y > 1:

  ||[tau_t(A), B]|| <= 2||A|| ||B|| n_X (y^2 / S_par(y)) y^{-2m}
                        (e^{2 J S_par(y) |t|} - 1)

with the y = 5/2 instance certified: exponential decay in the axis
separation once m ln(5/2) > J (1801/100) |t| — velocity readout
(1801/100) J / ln(5/2) < 20 e J (gate with certified rational brackets
on ln(5/2) and e). HONEST SCOPE: per-axis statement only — for
diagonal separations the parent isotropic bound can be stronger; the
anisotropic multi-axis tilt is named open; optimality over y is NOT
claimed (scan certificate only).

## Key gates

Native re-enumeration of both Delta tables (box-stable); S polynomials
+ domination factorization symbolic; the tilt recursion F_{n+1} <= S^n
at a symbolic step + indicator inequality instance; offset arithmetic
(phi range at a hyperplane); series assembly identity symbolic; y=5/2
exact values; ln(5/2) rational brackets via atanh partial sums
(alternating/monotone tails); parent-comparison certificate
(1801/100)/ln(5/2) < 20e via the brackets; sanity S(1) = 10.

## Cluster discipline

PR #6: evaluator recorded before PR, referencing B05's forward
statement (this block IS the one further block B05's evaluation
planned).
