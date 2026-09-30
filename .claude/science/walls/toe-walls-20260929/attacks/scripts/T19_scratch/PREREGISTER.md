# T19 pre-registration (written before any script was run)

Wall: a local fermion on one qubit per site (string / extra-qubit trilemma).

## Test A: exact one-qubit-per-mode Pauli embedding (Lemma S)
Setup: L x L open grid (and 1D chain, and 2x2x2 / 3x3x3 for d=3), one qubit and one complex
fermion mode (two Majoranas) per site. An exact Pauli encoding is a set of pairwise
anticommuting Paulis P_a (one per Majorana); the bilinear g_a g_b maps to P_a P_b.
"r-local" = for every nearest-neighbour Majorana pair (same site, or adjacent sites), P_a+P_b
(mod phase) is supported in the Chebyshev box of radius r around the two sites.
Script: sat_lemmaS.py (PySAT, CaDiCaL).
Prediction from the by-hand lemma (two disjoint paths => a(v) supported at both ends => the
far-away c_u are pairwise anticommuting Paulis in a bounded box, at most 2m+1 of them):
 - 1D control, r=1: SAT (Jordan-Wigner).
 - 2D: r*(L) grows with L; SAT at r=1 for small L only; UNSAT at r=1 for L large enough.
   Lemma bound: r=1 impossible once (L-4)^2 > 2*(r+2)^2+1, i.e. L >= 9.
PASS (wall's exact corner is a theorem at Pauli level): r*(L) strictly non-decreasing and
   increases at least once between L=2 and L=5 in 2D, with 1D control SAT.
FAIL (wall broken at this level): r*(L) constant (<=2) for L=3,4,5 in 2D, i.e. a bounded-range
   exact one-qubit-per-mode Pauli encoding exists in these windows. Then look for a general
   construction and re-read the wall.

## Test B: what the "extra qubit" escape leaves behind (vacuum order)
Setup: Bravyi-Kitaev superfast (BKSF) code on an L x L torus, qubits on edges. Vacuum stabilizer
group = <B_v, plaquette loop words>. Compute the Kitaev-Preskill topological entropy
gamma = S_A+S_B+S_C-S_AB-S_BC-S_AC+S_ABC on a disc from GF(2) stabilizer rank (S_R = |R| - dim G_R).
Script: bksf_tee.py.
PASS (extra-qubit escape has a topologically ordered fermion vacuum, so state preparation from a
   product state is depth >= ~L by Bravyi-Hastings-Verstraete 2006): gamma = 1 bit (ln 2).
FAIL (preparation obligation is not intrinsic): gamma = 0 for the BKSF vacuum.
   Control: JW encoding vacuum (a product state) must give gamma = 0; toric code must give 1.

## Test C: bookkeeping on Z^3 (counts, not physics)
Script: cell_complex.py. Z^3 nearest-neighbour graph restricted to roles by parity of coordinates
(vertex 000, edge 100.., face 110.., cube 111 mod 2). Checks: NN adjacency equals cubic-complex
incidence; each edge site has 2 vertex + 4 face neighbours; each face site 4 edge + 2 cube neighbours;
mode density (vertices) = 1/8; edge qubits = 3/8; per mode 3 edge qubits.
PASS: all counts hold. FAIL: any count differs (then the "one qubit per site" reading of BKSF changes).
