D4 spin cell: one fermion mode per D4 event does not give a protected spin-1/2 on any small W(F4) cell with root-hop phases, and no cell of 4 events can hold a spinor

Date: 2026-10-26
Claim type: bounded_theorem (exact F2 linear algebra and group/representation facts, plus finite node diagnostics on supplied free
nearest-neighbour kernels)
Status authority: independent audit lane only. This draft sets no audit outcome.
Runner: runner.py (this folder). AUDIT_TIMEOUT_SEC = 120. Seeded, 11/11, output 4.6 k characters, 480 MB peak.
  Run time 62 s, slightly above the probe's 60 s target. A re-run under a unique filename (scratchpad copy) gave identical output
  apart from the runtime line.
Pre-registration: criteria_pre_run.txt, written before any code.
Labels: [T] exact or theorem; [F] finite diagnostic; [S] reading. Axioms unchanged. No CL edit. Nothing adopted.

Sources used
- d4-sixteen-content (#10103): -1 in W(F4) makes every invariant one-component kernel even; KS lives on Z^4 = D4 + a hole class
  and keeps 384 elements; D4/2D4 orbits 1 + 12 + 3; D4/2D4* = 4 (OPEN there: "a 4-event sqrt2 cell"). This note closes that OPEN
  item in the scope below.
- d4-zoom-fixed-point-fermion (#10098) and d4-zoom-chirality (#10099): 4 supplied spinor components per event; W(F4) Molien counts.
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
   - [F, C4c] 4D4* (64 events): W(F4) admits 32 patterns, some non-uniform. Every one has degenerate zeros.

5. All uniform Z2 fluxes, any point symmetry or none [F, C6].
   - There are 2^14 patterns per class (14 = rank of the uniform-flux space; the 4D4* cell gives the same 14).
   - There are 40 W(F4)(+sign) orbits per class, 80 in all. 79 of them have degenerate zeros. One symmetric orbit (64 patterns) is GAPPED (min singular
     value 2.52).
   - Not one pattern has only isolated Dirac nodes.
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

VERDICT (pre-registered rule): NO-GO in the exact scope.
- Scope: Z2/uniform-U(1) phases on unit nearest-neighbour root hops; cells 2D4*, 2Z^4, 2D4, 4D4*; projective W(F4)/W(B4)/W(D4)
  covariance; plus all uniform fluxes with no symmetry.
- The representation no-go (6) covers every kernel range on the 4-event cell and untasted spin on the 16-event cell.
- Spin does not emerge, and protection is not even reached. The only remaining one-mode route is spin x taste on a 16-event (or
  larger) cell with a non-nearest-neighbour kernel.

Proposed CL text (UNTESTED, for review, NOT adopted)
  "Matter field content. Each matter species carries one 4-component spinor register per D4 event (four fermion modes)."
- This writes in the supply honestly. It is an AX-level bend of the Qubit axiom (one qubit per site becomes four).
Smuggling gate
- (1) No fitted number. PASS.
- (2) Names no gauge group or particle. But "spinor" is inserted structure, and is listed as SUPPLIED.
- (3) Prediction it was not built for: none new (inherits the D4 law's dim-8-only LIV). UNTESTED.
- (4) Bends the Qubit axiom.
- GATE: fails item (3) as a new rule. Report it as a supply, not a derivation.

Axiom-level implication (plain): with one qubit per event and nearest-neighbour root hops, the D4 event set cannot produce a light
spin-1/2. Keeping W(F4) protection means either four qubits per event, or an unproven 16-event spin x taste construction with long
hops.

Open (walls move)
- Spin x taste on the 16-event cell with the zoom kernel: does any W(F4) projective phase cocycle make the cell module equal to S x T?
- The gapped symmetric uniform-flux orbit: its second Chern number (class AI, d = 4) and boundary modes. Not computed.
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
