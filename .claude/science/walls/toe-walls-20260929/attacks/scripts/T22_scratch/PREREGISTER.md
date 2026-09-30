# T22 pre-registration (written before any script was run)

Attacker: Claude Sonnet 5.5. Date 2026-09-29.
Wall T22 = L05-W7 + L06-W15: chirality; free local walkers have mirror twins; the
chiral weak SU(2) and anomaly-complete hypercharge are added by premises.

Question the tests try to answer: what does each half of the wall actually rest on,
and can one cheap check price the routes (SMG, tails, extra dimension) or merge
the two halves?

## Test A  (test_A_equivariant_nn.py): "is L06-W15 a separate wall?"
Claim under test (A1): if a translation-invariant finite-range Hamiltonian (flowing) or
unitary (ticking) commutes with a compact internal group G acting unit-cell-locally
(or, more generally, by a representation that is continuous in k), then the node
chiralities inside each G-isotype sum to zero. So an SU(2) that acts only on the
left-handed nodes cannot be a symmetry of any free local walker.
Numerical test: random range-1 Hamiltonians on C^2 (spin) x (doublet + singlet) internal
spaces with SU(2)-invariant hopping; locate every node of each isotypic block by root
search plus sign(det) chirality.
- PASS (A1 supported): total chirality is 0 in each isotype (doublet block, singlet
  block) for every random draw; no draw has doublet chirality != 0.
- FAIL (A1 refuted): any draw with a nonzero net chirality in one isotype.
Side check (A2): eps(x) = (-1)^(x+y+z) satisfies eps H eps = -H for H = sum sin k_j sigma_j
and maps every node of chirality chi at k to a node of chirality -chi at k+(pi,pi,pi).
- PASS: exact. FAIL: eps commutes with node chirality (then eps could serve as gamma_5).

## Test B  (test_B_anomaly_ledger.py): "what content does any mirror-removal route need,
and how many lattice nodes does it cost?"
Exact rational arithmetic on the anomaly traces for
 (i) the framework's native left-handed 8-state surface, Q_L = (3,2)_{1/3}, L_L = (1,2)_{-1};
 (ii) plus the SU(2)-singlet completion with the SM values (P-COMP without nu_R, 15);
 (iii) plus nu_R (16).
Traces: SU(3)^3, SU(3)^2 Y, SU(2)^2 Y, Y^3, grav^2 Y, Witten count, and nu = number of
left-handed Weyl states mod 16 (Z_16 condition for the Z_4^X-preserving mirror gapping).
Also brute-force search: minimal SU(2)-singlet completions of (i) with colour reps in
{1, 3bar} and hypercharge on a rational grid.
- PASS (route price = P-COMP16): (i) fails at least Y^3 and SU(3)^3; (ii) passes the gauge
  traces and has nu = 15 (fails Z_16); (iii) passes with nu = 16; minimal completion has 7
  states; all minimal solutions reduce to the SM values.
- FAIL: (i) is anomaly free (then no completion premise is needed), or a smaller
  completion exists.
Node-count comparison (arithmetic): a symmetric-mirror route needs 2 x nu lattice nodes
(nu chiral, nu mirror). Compare with 8 (flowing walker), 16 (ordered tick), 4+4 (U_g).

## Test C  (test_C_tails_flux.py): "does the chiral (tails) tick buy chirality with a pump?"
Take the exponentially local covariant tick with W3 = 4 (probe 2, T4: normalised
range-2 Fourier truncation of q_g = (c_x c_y c_z, g s)). Put it on a 12 x 12 torus in the
(x, y) plane with flux 2 pi/12 per plaquette (Peierls, straight-line paths, polar factor of
the dressed truncation), keep k_z as a parameter.
Measure: the winding number of det V(k_z) around k_z in [0, 2 pi) (spectral flow of the
Floquet operator through the quasi-energy circle), per flux quantum.
- Prediction (dimensional reduction): winding / N_phi = W3 = +/-4 for the tails tick;
  0 for the strictly local ordered tick U_- (probe 2, T5) as a control.
- PASS (tails tick pumps): |winding| = 4 N_phi (up to the sign convention) and the control
  gives 0. Reading: the price of the tails route includes a per-cycle quasi-energy pump in
  E parallel B backgrounds (the pi-sector is the return path of the anomaly current).
- FAIL: winding 0 for the tails tick (then the tick is not chiral in the flux picture),
  or the control is nonzero (code bug).

Time box: about 45 minutes of computation for A, B, C together. If C does not run cleanly
inside its share, it is dropped and reported as not run.
