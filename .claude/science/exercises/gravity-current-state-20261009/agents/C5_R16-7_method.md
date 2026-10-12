# R16-7 method statement (written 23:08Z, before any run)

Method M (controlled, non-perturbative): exact operator inequalities, valid in every ground
(or thermal) state of the stated class, at every coupling (U ~ J ~ g included), no small-field
expansion, no Schrieffer-Wolff convergence, no finite-size extrapolation.
 (M1) f-sum rule: m1(k) = <[C^dag,[H,C]]> with C = E_TT(k) = sum_x e^{ikx} eps_TT(k).E(x).
 (M2) Bogoliubov inequality: chi_AA >= |<[C,A]>|^2 / m1(k) for any A (static susceptibility chi).
 (M3) Diamagnetic inequality for stoquastic H: twisting off-diagonal phases cannot lower E0.
 (M4) Moment/softness bound: omega_min(k)^2 <= m1(C)/chi_CC.
Definition fixed before running: metric susceptibility chi_TT(k) := chi_AA / |<[E_TT(k),A]>|^2
for a gauge-invariant TT probe A (equals chi_hh^TT for CCR fields with A = h_TT; EH gives 1/(g k^2),
compact-h |R|^2 gives 1/(g k^4)). Scalar-source response: W(k) = d^2 E0(rho)/d rho_k d rho_-k
in the conserved scalar-charge sector rho (EH: -g/(4 qhat^2), attractive inverse Laplacian).

Classes: rotors (E integer, h in U(1)) and quantum-link truncations (E integer in a finite
window, h-operators = raising/lowering, [E,U]=U exactly; spin-1/2 = qubits). Exact integer vector
Gauss law G E commuting with H. Z_N mod-N clocks: only above a k-floor (wrap/aliasing), labelled.

Control parameter: none for rotors/QLM (exact inequalities). For Z_N clocks: the aliasing ratio
(2 pi M/N) and the k-floor k* ~ (M/N)^(1/2). For numerics: the exact lattice symbols are evaluated
at k = 1e-3..0.3 along 5 directions; k-power = log-log slope; subtraction: none (invariant
patterns have zero 0th and 1st moments, so m1 has no constant or k^2 term to subtract in the
tensor case; checked).

Control (c), same method: cubic-lattice U(1) quantum-link / spin-ice-type ring-exchange model
(plaquette characters, exact Gauss law div E = 0). Pass = the method's bound has exponent 2
(chi >= c/k^2, i.e. it admits and is saturated by the emergent photon's 1/k^2) and does not
exclude the photon. ED check of M1-M4 algebra on a 2D U(1) QLM 4x4 torus (sanity of factors).
