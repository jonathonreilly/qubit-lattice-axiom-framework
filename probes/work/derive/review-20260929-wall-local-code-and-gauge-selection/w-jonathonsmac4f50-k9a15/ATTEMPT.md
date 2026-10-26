# Attempt: review-20260929-wall-local-code-and-gauge-selection (a1)

Worker: Claude Sonnet 5.5, same family as the sources, unrefereed. Nothing here is audited.
I read in full `docs/MINIMAL_AXIOMS_2026-06-29.md` and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (main checkout `a77a3449c9`) before any premise judgment. The registry lists three primitives (scale reference, kinetic isotropy, realized state). None supplies dynamics, a conserved quantity, a constraint-preservation principle, or a payload clause.

## Plain-language summary

Source wall T79 (in `WALLS.md` and `SUMMARY.md`, which are in this task's source list) says: the Maxwell dynamics class is supplied; a search on a small coefficient grid found "exactly 2" Maxwell-type laws with both Gauss rows, a kill check found "8" and called "one speed" a grid artifact, and said the magnetic Gauss row is circular. I rebuilt the class and settled it without a grid.

Result (scoped, same-family): in the supplied class of linear, covariant, nearest-neighbour flows on one real number per vertex, edge, face and cube of the cubic torus, a law keeps every orbit bounded in both time directions exactly when the four on-site rates vanish and each of three coupling pairs is either absent or has opposite signs. That is also exactly when a positive diagonal energy is conserved. The speed is a free positive number. Given bounded orbits, "the electric Gauss row is kept" is the same statement as "the vertex payload is frozen and unread", and "the magnetic Gauss row is kept" is the same statement as "the cube payload is frozen and unread". So the magnetic row is not extra evidence that the cube payload is absent. It is that statement in other words.

This is a classification inside a supplied class. It does not derive the class, boundedness, or any Gauss row from the four axioms, and it says nothing about the other five walls in this task's list (T18, T19, T20, T25, T26, T27) beyond verifying their source hashes.

## Setting and premises (every one is an assumption)

- P1 (ASSUMED, supplied) Payload: one real number per vertex (phi), edge (E), face (B), cube (psi) of the cubic torus Z_L^3, L >= 2. Source: `U1_GAUSS_SUPPORT_FORCING_EXTENDED_PAYLOAD_CLASS_BOUNDED_NOTE_2026-09-05.md` (the "extended payload"), not the axioms.
- P2 (ASSUMED, supplied) The evolution is a real linear first-order continuous-time generator G. The axioms name no time (memo, "Relation To Dynamics").
- P3 (ASSUMED, supplied) A derivative reads only its own cell and incident cells (vertex-edge, edge-face, face-cube). Covariance under translations and the 24 proper rotations about a vertex acting on oriented cells.
- P4 (READING) The source's role-compiled doubled lattice is this cubical cochain complex with its standard orientations. I rebuilt it from cell data and did not import the source runners.
- P5 (ASSUMED) Stability notion: every orbit bounded for all t in R. Forward-time boundedness would admit damped members and is not what is classified.
- P6 (ASSUMED) The Gauss rows are supplied surfaces {d0^T E = rho_V}, {d2 B = rho_C}. They are a static constraint code. Keeping them is a property of the generator.

## Numbered steps

1. (CHECKED, check.py A1-A2) The torus complex has C d0 = 0, d2 C = 0 exactly (L = 2, 3, 4) and exact Betti numbers (1,3,3,1).
2. (CHECKED, B1-B6, L = 3 and 4) Rotation actions on oriented cells are signed permutations and chain maps. The space of translation-invariant nearest-neighbour matrices commuting with them has dimension exactly 10, spanned by: four on-site rates w, u, v, wc; vertex-edge pair (gve: phi' from d0^T E, gev: E' from d0 phi); edge-face pair (r: E' from C^T B, q: B' from C E); face-cube pair (gbc: B' from d2^T psi, gcb: psi' from d2 B). This reproduces the source's "ten coefficients" with my own construction (source: block 03 note, claim scope line 4). Retrieval of a known count, not new.
3. (PROVED from step 1, verified C1-C4 for L = 2, 3, 4, 6 with exact rational vectors) Constants are exact eigenvectors: the constant phi has eigenvalue w, the constant x-field E has u, the constant x-normal B has v, the constant psi has wc. Hence boundedness for t in R forces w = u = v = wc = 0.
4. (PROVED and CHECKED, C2-C4) Let l = 2 - 2cos(2 pi/L) > 0 and f(x) = cos(2 pi x/L). Three 2-dimensional subspaces are exactly invariant under all ten generators: (phi = f, d0 phi) with block [[w, gve l],[gev, u]]; (E on y-edges = f, C E) with [[u, r l],[q, v]]; (d2^T psi, psi = f) with [[v, gbc],[gcb l, wc]]. Identities used: d0^T d0 phi = l phi, C^T C E = l E, d0^T E = 0, d2 d2^T psi = l psi, C^T d2^T psi = 0.
5. (PROVED, C5-C6) For M = [[0,b],[c,0]], M^2 = bc I. If bc < 0, e^{tM} = cos(wt) I + sin(wt)/w M with w^2 = -bc (bounded). If bc > 0 it grows like cosh. If bc = 0 and M != 0, e^{tM} = I + tM (linear growth). If M = 0 it is bounded.
6. (PROVED from 3-5) Necessity: a member bounded for all t has w = u = v = wc = 0, and each pair (gve,gev), (q,r), (gbc,gcb) is (0,0) or has product < 0. A violation gives an explicit unbounded orbit inside one of the invariant subspaces of step 4.
7. (PROVED, CHECKED D1-D2 exactly at L = 3, 4) Sufficiency: for such a member choose weights W_V = 1, then W_E, W_B, W_C > 0 solving gev W_E + gve W_V = 0, r W_E + q W_B = 0, gcb W_C + gbc W_B = 0 (free where a pair is zero). Then G^T W + W G = 0, so |x|_W is conserved and every orbit is bounded. Verified exactly with Fractions for three members off every integer grid (for example q = 2, r = -1/3).
   **Theorem 1 (L = 2, 3, 4, 6 by finite exact checks; every L >= 2 by the same algebra).** Bounded for all t <=> w = u = v = wc = 0 and each of the three pairs is (0,0) or has negative product <=> a positive diagonal conserved form exists. The bounded set has nonempty interior in every active pair.
8. (CHECKED, D3-D7, E1-E2) Counts on integer grids follow: 26 on {-1,0,1}^10; 2 with g_ev = g_bc = 0; 8 and 8 with only one row; 8 on {-2..2}^2 for (q,r); in general 2n^2 on {-n..n}^2. I also scanned all 59,048 nonzero grid members at L = 2 (the source's "side 4") numerically (eigenvalues, then matrix-exponential growth) and it agrees with the rule on every member. So the earlier counts are right as counts, and "exactly 2 / one speed" is a statement about the grid. The speed c = sqrt(-q r) is free (G3).
9. (CHECKED F1-F3 exactly, L = 3; PROVED by the identities in F3) d/dt(d0^T E) = gev (d0^T d0) phi + u d0^T E and d/dt(d2 B) = v d2 B + gbc (d2 d2^T) psi, because d0^T C^T = 0 and C^T d2^T = 0. The zero-charge electric surface is invariant iff gev = 0. The zero-charge magnetic surface is invariant iff gbc = 0 (exact nullspaces of dimension 9, each fixing exactly that coefficient). Charged surfaces add u = 0 and v = 0.
10. (PROVED from 6 and 9, CHECKED G1-G3) **Theorem 2.** Within the bounded class: gev = 0 <=> (gev = gve = 0) <=> phi is a constant of motion that nothing reads; gbc = 0 <=> (gbc = gcb = 0) <=> psi is a constant of motion that nothing reads. A one-sided coupling is a nilpotent block (step 5) and is unbounded. Consequences: (a) keeping the ice rule alone (electric row) removes only the vertex payload. (b) With the electric row only, the bounded set is Maxwell plus an independent cube/longitudinal-magnetic oscillator: at L = 3 with (gbc,gcb) = (3,-1) the spectrum carries Maxwell frequencies and a second family sqrt(3) sqrt(spec d2 d2^T) (G2). (c) The magnetic row removes that second family, but only by being equivalent to "no cube payload dynamics". The source's step "the Gauss rows remove the vertex and cube extras" is therefore sound for the vertex half and circular for the cube half, now by an exact argument rather than a grid count.
11. (ASSUMED; FIRST UNRESOLVED STEP) Boundedness in both time directions (P5), the payload clause (P1) and the Gauss rows (P6) are not derived. Theorem 1 shows boundedness is exactly the conservation premise inside the class, so it removes no supply, it relocates it.
12. (READING) Code versus ensemble versus formation law. The Gauss rows are a supplied static code (constraint surfaces). The Gaussian ensemble with precision W is stationary under every bounded member (D2: G W^-1 + W^-1 G^T = 0 follows from step 7), and so is its conditioning on any invariant surface. The ensemble is therefore a property of the supplied W and rows, and carries no information about the flow. The flow is linear and reversible, so it is not an irreversible formation law, and T77's question (a covariant nearest-neighbour formation process whose terminal law is the uniform ice ensemble) is untouched here.

## What is new, and what is not

Not new (background): the ten-coefficient class and its CONS-based reduction (block 02 and block 03 notes); the unsupported "exactly 2" count and the "8" and circularity corrections (kill T79, `known_review_boundaries`); retrieval of source hashes and scripts.
New to my search (searched `docs/`, `scripts/u1_*`, 231 open PR titles; none states it): the grid-free exact classification (Theorem 1) including the equivalence of boundedness with a positive diagonal invariant inside the class, and the exact payload-inertness form of the row conditions (Theorem 2). I did not find a landed note stating either; `docs/` has no "bounded orbit" statement for this class. Same-family, unrefereed.

## Limits

- Theorem 1 is checked for L in {2,3,4,6} with exact rational mode vectors; the proof for general L uses the same Fourier mode with l = 2 - 2cos(2 pi/L). The infinite-volume statement follows by the symbol (blocks with s^2 -> 0 force the on-site rates to zero) but I did not execute it (SUGGESTED).
- Forward-time-only boundedness admits damped members; not classified.
- The class excludes complex or doubled payloads, longer reach, nonlinear terms and finite ticks. No impossibility is claimed for them, and the linear class is at most a weak-field statement for bounded qubit domains (source point, not rechecked).
- The covariant class was derived for vertex-rotation plus translation symmetry. Larger symmetry can only shrink it, and the ten named generators are cell-complex-invariant, so the dimension stays 10.

## Remaining obligations (and the unadvanced walls)

1. Derive or exclude "no runaway in either time direction" from the axioms (step 11).
2. Execute the infinite-volume symbol argument; connect the class to a finite-spin link model's Hessian (belongs to the photon-mode task, T78).
3. T77 uniform-measure half and role covariance: untouched.
4. T18/T19: the 2026-09-14 local-reference note proves growth of range only under a hypothesis that a local representative of an occupation-bit flip exists. Whether that hypothesis can be dropped, and the T19 SAT quantifier (r* for L <= 10), is not rechecked. Do not read the Pauli search as showing that every encoding needs extra local content.
5. T20, T25, T26, T27: sources hash-verified (`RECOVERY_STATUS.json`) and read; no new computation.
