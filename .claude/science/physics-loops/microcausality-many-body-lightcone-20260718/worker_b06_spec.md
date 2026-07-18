# Worker task: directional tilt data for the bond-adjacency walk on Z^3 (sharp-rate refinement)

You are a bounded computation worker. Do NOT read any repository files.
All context is in this spec. Write your deliverable INCREMENTALLY to:

  .claude/science/physics-loops/microcausality-many-body-lightcone-20260718/worker_b06_analysis.md

and your script to:

  .claude/science/physics-loops/microcausality-many-body-lightcone-20260718/worker_b06_enum.py

Run the script yourself and paste its output into the analysis file.
Use EXACT rational/symbolic arithmetic (fractions/sympy), never floats,
except where a float is explicitly marked as advisory-only. Do not
commit/push; do not claim audit status.

## Setup (self-contained)

Bonds of Z^3 = unordered NN pairs {x, x+e_i}. Two bonds are adjacent
iff they share exactly one site (a bond is not adjacent to itself).
Each bond has exactly 10 adjacent bonds.

Fix the direction e = e_1 (the x-axis). For a bond b = {p, q} define
the integer height phi(b) = p_1 + q_1 (sum of the two x-coordinates).
A bond parallel to e_1 at base x has phi = 2x + 1; a transverse bond
at level x has phi = 2x.

## Required data

1. For a PARALLEL start bond: enumerate its 10 neighbors and tabulate
   the multiset of height changes Delta = phi(neighbor) - phi(start).
   Report the counts per Delta value.
2. Same for a TRANSVERSE start bond.
3. Verify by brute-force enumeration on a box (two box sizes for
   stability).
4. Define the tilt polynomials in a formal variable y (= e^{lambda/2}):
     S_par(y)  = sum over the 10 neighbors of a parallel start of
                 y^{Delta},
     S_perp(y) = same for a transverse start,
     S(y)      = max-coefficient-wise honest bound: report BOTH
                 polynomials exactly and also S_max(y) = the pointwise
                 max for y >= 1 (state which dominates for y >= 1 and
                 prove the domination by comparing coefficients or by
                 an exact factorization).
5. WALK-TILT INEQUALITY (derive carefully, show every step): for walks
   (b_1, ..., b_k) with b_1 in a fixed finite start set and each step
   adjacent, and any y >= 1:
     #{walks with phi(b_k) - phi(b_1) >= m} <= S_*(y)^{k-1} * y^{-m}
   where S_* is the appropriate per-step bound. Prove it by the
   standard tilted-count argument: each walk contributes
   y^{sum of Deltas} >= y^m when the total height gain is >= m, and
   the sum over all walks of y^{sum Deltas} factorizes step by step
   into at most S_*(y) per step. State the inequality with exact
   hypotheses (y >= 1, integer m).
6. VELOCITY BOOKKEEPING: in the parent bound the walk length k enters
   through (2J)^k t^k / k! and reach requires the walk to gain height
   of order 2d (phi doubles distances: crossing site-distance d in the
   e_1 direction means height gain >= 2d - 2 or so — derive the exact
   offset from the definitions: start bonds touch X = {x_1 = 0} say,
   end bonds touch {x_1 = d}). Assemble:
     sum_{k >= 1} (2J)^k (t^k / k!) N_start S_*(y)^{k-1} y^{-(2d - c0)}
       = (N_start / S_*(y)) * y^{-(2d - c0)} * (e^{2 J S_*(y) t} - 1)
   with the exact constant c0 you derive. Conclude a decay statement:
   the bound decays exponentially in d once
     2 d ln y > 2 J S_*(y) t + O(1),
   i.e. a velocity bound v(y) = J * S_*(y) / ln y in site units
   (CHECK the factor 2 bookkeeping between phi-units and site units
   carefully — phi gains 2 per site of distance; 
   show the bookkeeping cleanly and state v(y) exactly).
7. RATIONAL TILT SCAN (exact): evaluate S_par(y), S_perp(y), and
   v(y) = J * S_max(y) / (2 * ln y) or the correctly-derived formula,
   at exact rational y in {5/4, 3/2, 2, 5/2, 3, 4}. ln y is
   transcendental — keep v(y) as an exact expression J * S/ln(y) and
   ALSO give advisory floats. Identify the best y in the scan and
   compare against the parent readout 20 e J ~ 54.37 J (advisory
   float). Report the best certified v as an exact expression.
8. SANITY: S_*(1) must equal 10; the m = large behavior must recover
   the reach lemma qualitatively.

## Honesty requirements

- Show the full derivation of every inequality; mark anything assumed.
- Exact arithmetic only for load-bearing numbers.
- End with a "LIMITS" section: what remains unproven (e.g. optimality
  of the scan point, non-integer offsets, the O(1) constant's exact
  value if you did not pin it).
