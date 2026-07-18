# Worker task: exact adjacency/reach data for the finite-range (plaquette-inclusive) walk class on Z^3

You are a bounded computation worker. Do NOT read any repository files.
All context you need is in this spec. Write your deliverable
INCREMENTALLY (append section by section as you compute) to:

  .claude/science/physics-loops/microcausality-many-body-lightcone-20260718/worker_b05_analysis.md

Also write your enumeration script to:

  .claude/science/physics-loops/microcausality-many-body-lightcone-20260718/worker_b05_enum.py

Run the script yourself and paste its printed output into the analysis
file. Do not synthesize verdicts, do not claim audit status, do not
commit/push anything.

## Mathematical setup (self-contained)

On the lattice Z^3 define two families of "terms":
- BONDS: unordered nearest-neighbor site pairs {x, x+e_i}.
- FACES (plaquettes): unit-square site quadruples
  {x, x+e_i, x+e_j, x+e_i+e_j} for i < j.

Two terms are ADJACENT iff their site supports share at least one site
and they are not the same term. All enumerations must be done on a
centered box large enough that counts are boundary-free, and CHECKED at
two box sizes (e.g. radius 4 and radius 6) for stability.

## Required exact counts (deliverable table 1)

1. Number of bonds incident to one fixed site. (Sanity: known = 6.)
2. Number of faces containing one fixed site.
3. Number of bonds adjacent to one fixed bond. (Sanity: known = 10.)
4. Number of faces adjacent to one fixed bond (sharing >= 1 site).
5. Number of bonds adjacent to one fixed face.
6. Number of faces adjacent to one fixed face (sharing >= 1 site),
   EXCLUDING itself.
7. Therefore: the maximum total term-adjacency degree
   D = max over term type of (#adjacent bonds + #adjacent faces),
   stated separately for a bond start and a face start.

## Required diameter/reach data (deliverable table 2)

8. The l1 (graph) diameter of a bond support (max graph distance
   between its sites) and of a face support.
9. For walks (T_1, ..., T_k) with T_1 containing a fixed site X = {0}
   and each T_{j+1} adjacent to T_j (mixed types allowed), compute by
   brute force, for k = 1, 2, 3: the maximum graph distance from X of
   any site of T_k over all such walks. Compare with the a priori
   bound sum of diameters: report whether max distance = k * 2, less,
   or more (it cannot be more if the bound argument is right — if you
   find more, FLAG IT LOUDLY).
10. The count of length-2 mixed walks from a single-site start
    (T_1 ranges over all terms containing X), exactly, and the check
    that it equals (#terms containing X) * D-ish bounds — report the
    exact count and the product bound, and whether count <= bound.

## Honesty requirements

- Every number must come from the enumeration script output, not from
  by-hand reasoning alone. Where you also derive a count by hand
  (encouraged as a cross-check), show the derivation and mark
  agreement/disagreement.
- If any count fails box-stability, report both values and FLAG.
- End the analysis file with a section "LIMITS" listing anything you
  did not verify.
