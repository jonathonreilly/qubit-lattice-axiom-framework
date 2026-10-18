# F3 pre-registrations (written before any script was run), 2026-10-14 ~13:40Z

## Test R1 (time-doubler duality), script scripts/r1_duality_check.py
Objects: two-band free ticks U(k) = a(k) - i b(k).sigma in SU(2) on Z^3:
 (i) U_g of LATTICE_HANDEDNESS T4 (exact formula), (ii) its range-2 Fourier truncation V = q_tr/|q_tr|,
 (iii) normalized Wilson-type maps U_M = (m - i s.sigma)/|.|, m = M - sum cos k_j, M in {2, -2, 0.5}.
Quantities: W3 (grid); nodes = zeros of b; tick chirality chi (T2 convention, sign det(+-J));
E = (i/2)(U - U^dag) = b.sigma and its zero chiralities chi_E = sign det(db/dk).
PASS if, for every tick: sum chi at eps=0 == sum chi at eps=pi == round(W3); chi_E = chi at eps=0 nodes and
chi_E = -chi at eps=pi nodes, so sum chi_E == 0; for U_g additionally b == g * (sin kx, sin ky, sin kz)
(i.e. E = g * H_walker) and a == +1 / -1 on even / odd corners. Fock-vacuum check: particle-hole pairs at
eps=0 nodes have quasi-energy in (0, small), at eps=pi nodes in (-small, 0) mod 2pi (inverted).
FAIL if any equality fails beyond 1e-6 (W3 within 0.05).

## Test R2 (seam-path gauging), script scripts/r2_seam_gauging.py
Object: L x L torus in (x,y), Landau gauge A_y = phi x, phi = t * 2pi/L (t in [0,1]; t = 1 is a uniform field
with N_phi = L flux quanta), k_y and k_z good quantum numbers; Peierls substitution of each Fourier hop
(y-move at the starting x, then x-move).
 Control: ordered strictly local tick S_x S_y S_z, gauged factor by factor (unitary for every t).
 Test: range-2 truncation q_tr of U_g, gauged as a polynomial Q(t), unitarized U(t) = Q (Q^dag Q)^{-1/2}.
Measured: total det-winding in k_z (summed over k_y) of U(t) = net spectral flow through any quasi-energy;
sigma_min(Q(t)) over (k_y, k_z).
Pre-registered readings:
 PASS (lemma mechanism confirmed): control winding constant (0) for all t with sigma_min = 1; test winding
 = 0 at t = 0 and = 4 N_phi (+-10%) at t = 1, and every change of the winding happens at a t where
 sigma_min(Q) < 1e-3 (i.e. the natural gauging of the chiral tick is NOT a continuous unitary family).
 FAIL-A: test winding at t = 1 is 0 (the T22 '4 N_phi pump' would then not be a property of the gauged tick).
 FAIL-B: a winding change with sigma_min bounded away from 0 (would contradict continuity: a bug or a wrong lemma).
 INCONCLUSIVE: winding at t = 1 not within 10% of 4 N_phi but nonzero.

## Follow-up R1-F1 (dated 2026-10-14 ~13:48Z, added AFTER seeing R1's result; R1's verdict is unchanged)
R1 was recorded as FAIL solely because the N=40 finite-difference W3 estimate missed the integer by more than 0.05
for three ticks (3.937, 3.943, 1.944) while every node identity passed. New test, script scripts/r1f1_w3_richardson.py:
W3 at N = 32, 48, 64 and Richardson extrapolation assuming error c/N^2 (fit on the three).
PASS if the extrapolated W3 is within 0.05 of the integer sum chi(eps=0) for all five ticks; FAIL otherwise.

## Test R1-F2 (dated 2026-10-14 13:49Z, before running): no selection rule on the pi-sector's soft-photon vertex
Script scripts/r1f2_vertex.py. For U_g, the q->0 photon vertex of a Peierls-coupled tick is dU/dk_j. Interband
element M_j(k) = <u_+(k)| dU/dk_j |u_-(k)> (u_+: eigenvalue e^{-i eps}, empty band; u_-: e^{+i eps}, filled band),
evaluated on shells |k-K| = r = 1e-2, 1e-3, 1e-4 (200 random directions) around the eps=0 node K=0 and the eps=pi
node K=(pi,0,0). PASS (no selection rule; vacuum -> photon + pi-pair allowed at first order) if the shell average of
sum_j |M_j|^2 at the pi-node tends to a nonzero limit (ratio between r=1e-3 and 1e-4 within 10%, value > 1e-3),
like at the 0-node. FAIL if it tends to 0 (a selection rule would protect the inverted sector at linear order).
