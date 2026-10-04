# A50 notes (retry): non-Pauli dressings and lemma F

Conventions. theta(i,j,k) defined by t_i t_j^dag t_k = theta * t_k t_j^dag t_i on H_{ik}
(charges at ends i,k; vertex 0 and end j empty).  Equivalently theta = holonomy
W = t_i^dag t_j t_k^dag t_i t_j^dag t_k restricted to H_{ik}.

## Task 1 (single half-turn, arbitrary unitary hops)

Step 1 (configuration hexagon).  Two charges among {0,1,2,3}; hop t_j joins {j,k}<->{0,k}.
The six configurations form ONE 6-cycle:
 01 -t2- 12 -t1- 02 -t3- 23 -t2- 03 -t1- 13 -t3- 01.
theta(1,2,3) is the holonomy of this hexagon based at 13 in one direction.
If it is scalar at one base point it is the same scalar at every base point
(conjugate by a path of hop isometries).  The opposite direction gives the inverse.

Step 2 (intrinsic identities, EXACT).  theta(2,3,1) and theta(3,1,2) traverse the hexagon
in the same direction as theta(1,2,3): equal.  theta(2,1,3), theta(1,3,2), theta(3,2,1)
traverse it backwards: equal to theta(1,2,3)^{-1}.

Step 3 (covariance under C = half-turn about eps through v).  U_C t_d U_C^dag = p1 t_{-d} G^{c1},
U_C t_{-d} U_C^dag = p2 t_d G^{c2}, U_C t_e U_C^dag = p3 t_e G^{c3}, with G any Gauss-type
operator diagonal on charge configurations (B_v for Z2, exp(i a Q_v) for U(1)).
Apply Ad(U_C) to W(d,-d,e) on H_{d e}.  Each hop and its adjoint appear once, so the
phases p cancel.  Each G^{c} acts on a configuration where v is EMPTY (checked step by
step along the transformed word), and each c appears once from t and once from t^dag,
so the Gauss factors cancel whatever their value on the empty vertex.
The image word is the holonomy of the hexagon traversed BACKWARDS (based at H_{-d,e}).
Hence theta(d,-d,e) = theta(-d,d,e) = theta(d,-d,e)^{-1}, so theta^2 = 1.  (EXACT)

Step 4 (nothing more from one half-turn).  Both signs occur: theta = +1 for trivial
dressings; theta = -1 for the {1,C2z} control (A48's escape, frame-changed to the exact
action, see Task 2 control).  Without C, theta is unconstrained: U(1) field-phase link
dressings give theta = (r13 r32 r21)/(r31 r23 r12) (r_jk = phase ratio of t_j's dressing
on leg-link k), any phase.  C forces r13=r23, r31=r32, r12=r21 so this equals 1.

## Task 2 (a): per-site conditions (EXACT)

Product hops t_i = O_i (x) prod_x u_i(x).  Non-link places carry a full qubit, so the
Levin-Wen product is scalar iff every per-site word is scalar:
 W_x = u_i^dag u_j u_k^dag u_i u_j^dag u_k = lambda_x.
Equivalent form: with X = u_i u_j^dag and Y = u_k u_j^dag, the condition is XY = lambda YX.
For 2x2 matrices det forces lambda^2 = 1, so lambda_x = +-1 always (no symmetry needed).
In SO(3): the relative rotations R_i R_j^-1 and R_k R_j^-1 commute; lambda = -1 exactly
when they are half-turns about perpendicular axes.
All triples at one site scalar <=> the six rotations lie in one coset A.R0 of an abelian
subgroup A: either SO(2)_n (coaxial; every lambda = +1) or a Klein group K
(u_i = q_i g, q_i Paulis in a rotated frame, g a common right factor; lambda = Pauli signs).
Links: Gauss preservation forces field-diagonal factors exp(i phi sigma^a) off the hop's own
link (no closed flip loops inside the window).  Their total is the phase
 Phi = (r_ik r_kj r_ji)/(r_ki r_jk r_ij),  r_jk = e^{2 i phi_jk s_k}.
Swapped pair (x, Cx): lambda_Cx = lambda_x^{-1} (the word at Cx is a cyclic rotation of the
inverse word at x).  Fixed site: lambda_x = +-1.
CHECKED: factorized theta = state-vector theta on 298 scalar junctions (13 qubits), 6.7e-15.

## Task 2 (b): Lemma F'' (claim, EXACT within class)

Class: any finite window; arbitrary single-qubit unitaries on non-link places; field-diagonal
factors on links other than the own link; covariant under the 24 turns up to phases and
Gauss factors; one T-junction product scalar (then all 12 are, they form one O-orbit).
Claim: theta(d,-d,e) = +1.
Proof.
1. theta = Phi_links * prod_x lambda_x.  Phi_links = 1 under C = C2e (r13=r23 etc.;
   Gauss factors flip both r's of one hop, cancel).  Swapped pairs cancel.  Remaining:
   C2e-fixed non-link places = corners v + 2k e.
2. Corner v: Stab(d) contains C4d, so R_d(v) = rotation about d by angle f, R_-d(v) =
   rotation by -f, R_e(v) = rotation about e by f.  X = R_d(2f), Y = R_e(f) R_d(f).
   Commuting forces f in {0, pi}, so lambda_v = +1 (90-degree f gives X = C2d but Y a
   120-degree turn).
3. Pair x = v+2ke, x' = v-2ke.  C4e fixes x, so R_{+e}(x) = R_e(a), R_{-e}(x) = R_e(b).
   C2d swaps x,x' and +-e, fixes +-d: lambda_x'(d,-d,e) = lambda_x(d,-d,-e).
   The T-junction (e,-e,d) at x must be scalar: X = R_e(a-b), Y = A R_e(-b), A = R_d(x).
   (i) a = b: third-leg factors equal, the two lambdas are equal, product +1.
   (ii) A about e: R_-d(x) = C2e A C2e = A, so X_I = 1, lambda = +1.
   (iii) a-b = pi and Y a half-turn perpendicular to e: A e = -e, A commutes with C2e,
   again lambda = +1.  Every pair contributes +1.
Hence theta_T = +1.  Load-bearing turns: C2e, C2d, C4e (stabiliser of axis places), C4d at v.

## Task 2 (c),(d): numerics so far (CHECKED)

t0_sanity: own-link transport 2.9e-16; covariance residual <= 1.1e-15 (all seed modes);
factorized theta = state-vector theta (298 junctions); no-symmetry U(1) link control gives a
generic phase -0.6056+0.7957i, matching the r-formula.
t2_census O (60/mode, quick): Clifford-sparse 15 T-scalar, all +1; axis-only 21, all +1;
continuous seeds never scalar.  Corners: 'all -1' in 7 samples while T = +1 (geometry-dependent
sign, not a statistic).
t2_search (Levenberg-Marquardt, continuous seeds, axis places):
 O far none 30: 30/30 scalar, all 12 T = +1.
 O far T 30: 0/30 reach target; best residual 6.928 = sqrt(48) = all 12 T stuck at +1.
 O v T, O vlinks T: 0 reach target (5.581).  T vlinks T, D2 vlinks T: 0 (5.581, 5.251).
 CONTROL C2z vlinks T 25: 12 scalar optima, 11 with all 12 T = -1.
 CONTROL C2z vlinks all 25: 6 optima with ALL 20 junctions = -1 (non-Clifford vertex
   factor, e.g. half-turn about an in-plane axis at -46.8 deg; continuous link angles).

## Sharper pair identity (EXACT) and what is load-bearing

At any place x where both (d,-d,+e) and (d,-d,-e) words are scalar:
 lambda_x(d,-d,+e) * lambda_x(d,-d,-e) = s(P_d, P_e),  P_d = u_d u_-d^dag, P_e = u_e u_-e^dag
(s = commutation sign; proof: X P = s+ P X and X Q = s- Q X give X P Q^-1 = s+ s- P Q^-1 X
with X = P_d, P = u_e u_-d^dag, Q = u_-e u_-d^dag, so P Q^-1 = P_e).
Far-corner pair (x = v+2ke, partner via C2d): product = s(P_d(x), P_e(x)).
Only C2e is needed at x: P_e in O(2)_e and P_d = C2_{Ae} C2_e.  -1 needs Ae perpendicular to e and
P_e = C2e or C2_{Ae}; type-III scalarity (P_e commutes with A u_-e^dag) then forces Ae = +-e or
Ye perpendicular to Ae: contradiction either way.  So far-corner pairs cancel already under
D2 = {1, C2x, C2y, C2z}.  CHECKED: T far T, D2 far T reach no -1 (best 5.477);
T far none 24/24 and D2 far none 7/7 scalar optima all +1.
Corner v: my proof uses C4d (lambda_v = +1); A48's Pauli argument uses D2 faithfulness.

## Task 3 (non-product), t3_composite.py (CHECKED, dense 7 qubits)

(a) SWAP-type t_j = O_j (x) SWAP(v, v+2d_j): automatically covariant (SWAP commutes with U(x)U).
Holonomy = SWAP(v,e-x) SWAP(e+x,e+z) on its support exactly (residual 0, rank 16, eigenvalues
+1 x10, -1 x6).  Not a scalar: the exchange moves the internal qubits.  ARGUED: bosons
carrying an internal qubit (exchange = +SWAP); a fermion would need -SWAP.
(b) CZ-type, O-covariant: t_i = O_i (x) exp(i sum_m k(i,m) P_m (x) s_m sigma^{a_m}_v) (x) CZ-phases on
link pairs.  First attempt failed covariance (0.87, non-commuting ordered product); fixed with a
single exponential (7.2e-15).  18 sets: 14 not scalar; 3 with T = +1 (corners +-1 uniform);
ONE with all 12 T-junctions = -1: k_opp = pi/2 (controlled-i sigma on v by the opposite link),
k_perp = 0, CZ(pi) on perpendicular link pairs.  24-turn covariance 2.7e-15, T residual 3.6e-15,
but every corner junction is non-scalar (residual 1.000): no consistent statistic.
