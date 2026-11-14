D4 spin cell, one fermion mode per D4 event: exact obstructions (no Kogut-Susskind phases, no onsite chirality, no W(F4) spinor on the 4-event cell) and a failed numerical search for isolated Dirac nodes among root-hop phase patterns on small cells

Date: 2026-10-26
Claim type: bounded_theorem (exact F2 linear algebra and group/representation facts, plus finite node diagnostics on supplied free
nearest-neighbour kernels)
Status authority: independent audit lane only. This draft sets no audit outcome.
Runner: [`scripts/d4_event_one_mode_per_event_spin_cell_no_go_root_hop_phases_and_cell_spinor_obstruction_2026_10_26.py`](../scripts/d4_event_one_mode_per_event_spin_cell_no_go_root_hop_phases_and_cell_spinor_obstruction_2026_10_26.py). AUDIT_TIMEOUT_SEC = 120, seeded; it exits nonzero on any failed check.
  Its cache [`logs/runner-cache/d4_event_one_mode_per_event_spin_cell_no_go_root_hop_phases_and_cell_spinor_obstruction_2026_10_26.txt`](../logs/runner-cache/d4_event_one_mode_per_event_spin_cell_no_go_root_hop_phases_and_cell_spinor_obstruction_2026_10_26.txt) holds the current output (the source run: 11 checks, 62 s, 480 MB peak). A re-run under a unique
  filename (scratchpad copy) gave identical output apart from the runtime line.
Pre-registration: criteria_pre_run.txt, written before any code.
Labels: [T] exact or theorem; [F] finite diagnostic; [S] reading. Axioms unchanged. No CL edit. Nothing adopted.

Sources used
- d4-sixteen-content (#10103): -1 in W(F4) makes every invariant one-component kernel even; KS lives on Z^4 = D4 + a hole class
  and keeps 384 elements; D4/2D4 orbits 1 + 12 + 3; D4/2D4* = 4 (OPEN there: "a 4-event sqrt2 cell"). This note closes that OPEN
  item in the scope below.
- d4-zoom-fixed-point-fermion ([#10098](D4_ZOOM_FIXED_POINT_FERMION_HAS_ONLY_REAL_POSITIVE_POLES_BUT_SITE_POSITIVITY_NEEDS_A_ONE_SLICE_BUFFER_BOUNDED_THEOREM_NOTE_2026-10-26.md)) and d4-zoom-chirality ([#10099](D4_ZOOM_FIXED_POINT_CHIRALITY_OVERLAP_INDEX_AND_DOMAIN_WALL_SLAB_BOUNDED_THEOREM_NOTE_2026-10-26.md)): 4 supplied spinor components per event; W(F4) Molien counts.
- d4-sixteen-content (#10103) is not carried in this PR; it is recorded only in the source map of [the consolidation](D4_ROUTE_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md).
- git grep on origin/main and the open PRs: no D4/W(F4) staggered or spin-cell note. Nothing contradicted.

Scope of the search
- One complex Grassmann pair per D4 event.
- A bilinear nearest-neighbour kernel D with |D_x,x+r| = 1 on all 24 roots (all directions alike), carrying Z2 phases.
- Two classes: antisymmetric (KS class) and symmetric. Translation-uniform U(1) flux reduces to these two (see 3).
- Phases are periodic on a cell. A symmetry is realised projectively: a signed permutation with D -> chi D.
- A pattern counts as "spin emerges" only if EVERY zero of D(k) is an isolated Dirac node: the zero space has dimension 0 mod 4 and
  the linearised map is a nondegenerate Clifford map (D^dag D = g_ab p_a p_b 1, with g positive definite).

1. Cells [T, C1]. The W(F4)-invariant sublattices between 4D4 and D4 have indices 1, 4, 16, 64, 256. None has index 2 or 8.
   So the small cells are 2D4* (4 events, the sqrt2 cell, itself a D4 lattice with point group W(F4)), 2D4 (16) and 4D4* (64).
   For the subgroups we also used 2Z^4 (8 events).

2. No D4 eta phases [T, C2]. The KS property (all hops pairwise anticommuting) is impossible on D4 for ANY U(1) phases and ANY
   period.
   - Proof: Delta = (A_u A_v)(A_w A_z)^-1, with u, v, w, z = e1 +- e2, e1 +- e3, is diagonal and obeys Delta(x+r) = s_r Delta(x),
     where s = -1 exactly on +-u, +-v, +-w, +-z.
   - s would have to be a character of D4. It is not: (e2+e4) + (e1-e4) = e1+e2 (96 violations).
   - Check: the F2 system on the 2D4 cell is inconsistent.
   - The naive spinor kernel sum (r.gamma) T_r cannot be spin-diagonalised: a triangle product of r.gamma/sqrt2 is unitary but is not
     a multiple of 1.

3. No onsite chirality [T, C3].
   - Roots form triangles, so no sign eps(x) anticommutes with any kernel whose hops contain a triangle. There is no remnant U(1)_eps
     (KS's eps is constant on D4).
   - The sign characters of D4/2D4 fall into W(F4) orbits 1 + 3 + 12, so a character eps keeps at most 384 elements.
   - [T] W(F4), and even W(D4), acts transitively on the 64 oriented triangle classes. So a translation-uniform U(1) flux on an
     (anti)Hermitian D is forced to triangle holonomy +-1 or +-i: the two Z2 classes.

4. Projective-covariance search [T + F, C4].
   - For W(F4), W(B4) and W(D4) on the 2D4*, 2Z^4 and 2D4 cells, the covariance systems are consistent ONLY for:
     - (antisymmetric, chi = -1 on long reflections);
     - (symmetric, trivial chi).
   - Each has exactly 2 flux patterns (D and -D). The uniform flux is forced, even by W(D4).
   - [T, C4b] The antisymmetric uniform pattern is a WEAK D4 eta.
     - D^dag D = f(k) 1 exactly: the 60- and 120-degree cross terms cancel.
     - f = 24 + 6 sum_{24 norm-4 v} cos(v.k) + sum_r cos(2r.k). This is a scalar operator on the coarse 2D4* lattice: the D4 analogue
       of KS's D^2 = Laplacian on 2Z^4.
     - But f vanishes on whole lines, e.g. (0,0,0,pi) + t(1,1,1,1). That gives lines of zero modes, not Dirac points.
   - The symmetric pattern is the plain even hop (Fermi surfaces).
   - [F, C4c] 4D4* (64 events): W(F4) admits 32 patterns, some non-uniform. The numerical node search finds a degenerate
     zero in every one.
   - [F, C4] Likewise, on the 2D4*, 2Z^4 and 2D4 cells the numerical node search finds a degenerate zero in each of the
     forced patterns. A "degenerate zero" here is a Nelder-Mead minimum with singular value below 1e-6 whose linearised map
     fails the Clifford test; it is a numerical witness, not an exact one.

5. All uniform Z2 fluxes, any point symmetry or none [F, C6].
   - There are 2^14 patterns per class (14 = rank of the uniform-flux space; the 4D4* cell gives the same 14).
   - There are 40 W(F4)(+sign) orbits per class, 80 in all. In 79 of them the numerical search finds a degenerate zero.
     In one symmetric orbit (64 patterns) it finds no zero: the minimum singular value over 1500 random momenta and three
     refined grid minima is 2.52.
   - Correction (2026-11-14). The source text called that orbit GAPPED and said no pattern has only isolated Dirac nodes.
     Both rest on numerical root searches and 1500 random momenta. That is not an all-torus gap certificate, so the
     statement is narrowed: no pattern was FOUND with only isolated Dirac nodes. This is a failed search over the
     enumerated patterns, not an obstruction. (A certificate is within reach: for the 2D4 cell, |D(k) - D(k')| <=
     sqrt(24 x 12) |k - k'| by the Schur test, so a grid of (pi/N) D4* with N >= 16, covering radius 2.22/N, and a grid
     minimum near 2.5 would certify the gap. Not run here.)
   - With translations acting with a sign character (staggered flux), a scratch sweep of ALL 2 x (1156 + 2240) orbit
     representatives (the lambda orbits of sizes 3 and 12) found every one degenerate. The runner rechecks a seeded sample of 16
     (C6b).

6. Representation obstruction, ANY kernel range and ANY U(1) phases [T, C7].
   - At a W(F4)-invariant node, the cell mode space is a sum of modules induced from the coset stabilisers H (orders 1152, 384, 96).
   - Each H's spinor lift spans all of M_4(C), so S|_H is irreducible. By Frobenius the 4-dim spinor S is never a constituent.
   - Hence the 4-event sqrt2 cell (dim 4) cannot hold one Dirac spinor with W(F4) acting by the cell symmetries, whatever the kernel
     (zoom fixed point included).
   - The 16-event cell cannot hold an untasted spinor either.
   - Spin x taste is NOT excluded by this argument, for non-NN kernels on the 16-event cell. Its "Dirac-Kahler" form End(S) x lambda
     = 1 + 4 + 6 + 4 + 1 is excluded there by the cell's 3-dim frame block. That last step is argued in the text, not run.

7. Protection count [T, C8]. Quartic invariants: W(F4) 1, W(B4) 2, W(D4) 3, root-class stabiliser (96) 4. Any staggered escape
   that keeps only a frame or root stabiliser re-admits dim-6 LIV.

8. Supply [T, C9]. One Dirac spinor per event is 4 fermion modes = Fock dimension 16 = FOUR qubits per event (M_2(C)^(x)4), not two.
   The Qubit axiom gives one mode, M_2(C).

VERDICT (pre-registered rule, narrowed 2026-11-14): exact obstructions plus a failed search.
- Obstructions (exact, each about an explicit family):
  - (2) for every U(1) phase assignment of any period on the 24 unit root hops, the hops do not pairwise anticommute (no D4 eta);
  - (3) for every kernel whose hops contain a root triangle, no onsite sign eps(x) anticommutes with it;
  - (4) for W(F4), W(B4), W(D4) realised projectively on 2D4*, 2Z^4, 2D4, the only consistent covariance classes are the two
    listed, each with 2 uniform patterns (exact F2 solve);
  - (6) for any kernel range and any U(1) phases, the 4-event cell does not contain the 4-dim spinor with W(F4) acting by the
    cell symmetries, and the 16-event cell does not contain an untasted spinor.
- Failed search (numerical): among the patterns enumerated in (4), (4c), (5) and the staggered sample, the node search found
  no pattern whose zeros are all isolated Dirac nodes. This rules out nothing beyond those patterns and that search.
- Not excluded: spin x taste on a 16-event (or larger) cell with a non-nearest-neighbour kernel; non-uniform phases on larger
  cells; unequal hop magnitudes. Negative-claim packets are not added (see the consolidation's note on the 2026-11-13
  "Negative-claim packet" setting).

Proposed CL text (UNTESTED, for review, NOT adopted)
  "Matter field content. Each matter species carries one 4-component spinor register per D4 event (four fermion modes)."
- This writes in the supply honestly. It is an AX-level bend of the Qubit axiom (one qubit per site becomes four).
Smuggling gate
- (1) No fitted number. PASS.
- (2) Names no gauge group or particle. But "spinor" is inserted structure, and is listed as SUPPLIED.
- (3) Prediction it was not built for: none new (inherits the D4 law's dim-8-only LIV). UNTESTED.
- (4) Bends the Qubit axiom.
- GATE: fails item (3) as a new rule. Report it as a supply, not a derivation.

Axiom-level implication (plain, narrowed): with one mode per event, the 4-event cell cannot carry a W(F4) spinor (exact), and no
tested nearest-neighbour root-hop pattern on the small cells gave isolated Dirac nodes (failed search). Keeping W(F4) protection
with one mode per event needs a route outside those: for example a 16-event spin x taste construction with long hops, not built.
Four supplied components per event remain a supply, not a derivation. Reading one mode per event off the Qubit axiom with a
Grassmann realisation is itself an assumption (printed as SUPPLIED by the runner).

Open (walls move)
- Spin x taste on the 16-event cell with the zoom kernel: does any W(F4) projective phase cocycle make the cell module equal to S x T?
- The symmetric uniform-flux orbit with no zero found: an all-torus gap certificate (see 5), its second Chern number (class AI,
  d = 4) and boundary modes. Not computed.
- Non-uniform U(1) phases on 4D4* and larger cells; unequal hop magnitudes.

Smuggling review
- Forced or exact: cells, eta no-go, non-bipartite, triangle transitivity, covariance consistency, weak-eta identity, Frobenius
  obstruction, invariant counts.
- Supplied: nearest-neighbour unit root hops, Z2 phase classes, the node classifier thresholds (1e-6, rank tolerance 1e-4), grid sizes.
- Fitted: none.
Deviations from pre-registration
- P6 wording ("2 qubits?") is answered as four.
- The full staggered-character sweep is scratch-only (the runner samples it).
- The run takes 62 s, above the 60 s target.
