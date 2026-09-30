# T20 pre-registration (written before any script was run)

Attacker: Claude Sonnet 5.5 (same family as supervisor; same-family checks).
Wall: T20 = L05-W4 (spin-1/2 lift is a choice) + L05-W5 (Dirac law supplied).

Conjecture under test (route R1, "one premise, not five"): once the cubic
rotations act on the qubit's Bloch vector as the lattice vector rep T1
("full soldering", one of the four actions of the landed soldering menu),
(i) the spinor double cover is forced on the finite lattice group (no separate
"faithful lift" premise), and (ii) the nearest-neighbour, translation-invariant,
Hermitian one-particle law on l2(Z^3) x C^2 is fixed up to three real numbers
and is the Weyl/naive-Dirac law H = e0 + e1 sum cos k_mu + a sigma.sin k, with
eight isolated linear nodes; the other three actions give none.

## Test A (cover lemma), script test_A_cover.py
Objects: O = 24 proper cubic rotations; four homomorphisms rho: O -> SO(3)
(trivial, sign twist diag(1,s,s), axis s|g|, full g). For each, the double cover
pull-back: does a LINEAR 2-dim unitary rep U of O exist with Ad(U(g)) = rho(g)?
Method 1: presentation S4 = <s,t | s^2, t^3, (st)^4>; enumerate the phase
freedom of U_s, U_t (2 x 3 choices) and test (U_s U_t)^4 = 1.
Method 2: the lifted group G^ in SU(2); is -1 in the commutator subgroup?
PASS (R1 part i survives): trivial, sign twist, axis: linear lift exists;
full soldering: NO linear lift (both methods agree) => cover forced.
FAIL: full soldering has a linear lift (then the faithful-lift premise is
independent of the soldering choice and W4 stays a pair).

## Test B (covariant NN law), script test_B_covariant.py
Solve, for each action, the real-linear system A_{gv} = U_g A_v U_g^dagger,
C = U_g C U_g^dagger, A_{-v} = A_v^dagger over hop sets V = 6 nearest
neighbours, then |v|_inf <= 1 (26), for one-particle H(k) = C + sum A_v e^{ikv}.
Report covariant-space dimension, d(0) and Jacobian at Gamma, and the node set
of the traceless part d(k) (multi-start Newton on the torus).
PASS: full soldering NN: dim 3 (e0, e1, a); d(k) = a sin k; 8 nodes at {0,pi}^3,
each rank-3 Jacobian, chirality prod cos k, 4 plus and 4 minus, |charge| 1;
range 26: d(0)=0 and J(0)=a*Identity for every member. Other three actions NN:
no isolated rank-3 node for any member (nodal lines, surfaces, or gapped), and
J(0)=0 for all ranges.
FAIL: any other action gives isolated linear nodes at Gamma or in NN; or full
soldering NN has more than 3 parameters or nodes elsewhere.
Also: intersection of full-soldering-covariant with invariance under ALL internal
rotations (the strong reading of "no possibility is privileged") -> expect only
scalars (a = 0): Dirac law excluded by the strong reading.

## Test C (discrete-time NN unitary), script test_C_unitary.py
Under full soldering with NN support, is any non-trivial U(k) = c + sum A_v e^{ikv}
unitary for all k? PASS (consistent with Dirac-lane prior art on the cubic
lattice): none. FAIL: a non-trivial unitary NN covariant walk is found.

## Test D (Route R2, drop covariance), script test_D_generic.py
Random NN translation-invariant 2-band H(k) with no symmetry: does an open set
of parameters give isolated Weyl nodes of charge +-1, total charge 0, with
anisotropic velocity matrices (condition number >> 1)? PASS: yes. FAIL: no
nodes or isotropic by accident.

## Reading rules
- R1 survives (as a REDUCTION, not a pass) if A and B pass.
- Outcome PRICED needs both directions of the equivalence at NN range:
  full soldering => Weyl law (B) and Weyl-type isolated nodes => full soldering (B, other actions).
- If B fails for other actions (they also give isolated linear nodes), the price
  argument fails and the outcome downgrades to STANDS.
