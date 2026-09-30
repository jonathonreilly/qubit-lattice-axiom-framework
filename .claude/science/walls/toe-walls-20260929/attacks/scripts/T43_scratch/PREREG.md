# T43 pre-registration (written before any script was run)

Attacker: Claude Sonnet 5.5 (same vendor family as supervisor; same-family checks).

## Question the test decides
The lane closes the mass half on `M = M_S I + M_eps eps` with `M_eps = 0` (W4) and reports "no link between the two
halves" (W8). Prior art found in the repo before running anything:
- `THETA_ASSEMBLY_PAIRED_SHIFT_...2026-07-02` L2: `det(D + m e^{2 i a eps}) = e^{2 i a tr eps} det(D+m)`, so on a balanced
  surface the eps-direction mass phase is inert.
- `ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_2026-06-18`: eps is taste-dressed, not the taste-singlet gamma_5.
- `THETA_SUPPLIER_FLAVORED_GRADING_SPECTRAL_FLOW_..._2D_2026-07-02`: a taste-singlet grading Gamma_f whose spectral flow is
  `-2Q` on 2D U(1) flux `2 pi Q` (eps gives 0). No determinant-phase computation with Gamma_f is in that runner (grep `det`: none).
- `THE_TASTE_SINGLET_SECOND_MASS_...2026-09-03`: the Hamiltonian taste-singlet pseudoscalar mass M2 has body-diagonal support,
  algebra `(X, M2, eps) = (tau3, tau1, tau2)`; not cited by any theta note (grep).
So the untested step is the **assembly in the determinant channel**: does the mass phase carried by the taste-singlet grading
couple to the winding integer Q, and does the eps direction stay blind, on the lane's own staggered surface?

## Objects
- Surface: 2D even-L periodic staggered U(1), uniform flux `2 pi Q` (same construction as the 07-02 supplier note).
  Then 4D even-L periodic U(1) with flux `F12 = 2 pi Q1/L^2`, `F34 = 2 pi Q2/L^2`, `Q = Q1 Q2`; and SU(3) hot 4^4 configs.
- Masses: `Ms = m + i m5 eps` (eps direction), `Mg = m + i m5 Gamma` (Gamma = taste-singlet grading; 2D: the note's `Gamma_f`;
  4D: spin-taste gamma5 x 1, built by the Kluberg-Stern spin-taste map and validated in 2D against Gamma_f).
- Read-out: `arg det(D + M)` from `slogdet` (phase of the complex sign), `phi = arctan(m5/m)`.

## Pass and fail readings (fixed now)
- **P0 construction valid**: spin-taste `O(gamma5 x xi5)` equals `+-eps` to 1e-12; `O(1 x 1) = I`; 2D spin-taste singlet has the
  free-field spectrum of `Gamma_f` up to an overall sign (compare sorted spectra, tol 1e-9); singlet hops connect only
  x -> x + (+-1,...,+-1). Fail: I do not proceed to the 4D result and I report only 2D.
- **P1 eps direction inert**: `|arg det(D + m + i m5 eps)| < 1e-9` and `|det|` equals `det(D + sqrt(m^2+m5^2))` to 1e-9 relative,
  on every tested flux sector and on 10 SU(3) hot configs (4^4), for m5/m in {0.2, 1, 5}. Fail: any visible phase.
- **P2 singlet direction registers Q** (2D, L=8, 12, m=0.5, m5/m=0.2, Q in {-2..2}):
  `arg det(D + m + i m5 Gamma_f) = -s 2Q phi (1 +- 0.25)` with one common sign `s`, `|arg| < 1e-6` at Q=0,
  ratio(Q=2)/ratio(Q=1) in [1.8, 2.2], sign flips with Q -> -Q. Fail: phase not proportional to Q (then the taste-singlet mass
  phase is also inert and the mass half is not a topological-sector object on this surface).
- **P3 4D**: same on the 4D U(1) tori (L=4, 6): `arg det(Mg) = -s 4 Q phi (1 +- 0.3)` for `Q1=Q2=1` (Q=1), Q=2, Q=0 (Q2=0) gives ~0.
- **P4 flavour-class**: for random complex 2x2 flavour matrix `M_e` on the even sublattice and `M_o = M_e^dagger` on the odd
  (2^4 torus, SU(3)), `det > 0` to 1e-9 -- the whole "Hermitian-type" family is inert too. Fail: any negative or complex det.
- **P5 linearity in Gamma direction**: `arg det` vs `phi` for phi in {0.05..0.8}: linear to 15 per cent at Q=1 (2D).

## Reading, fixed now
- P0-P3 pass: the CP-odd mass phase couples to the same integer Q as theta_gauge, and the eps direction is a non-issue. Then
  W4's "M_eps = 0" leg carries no weight, W8's "no link" is answered in the determinant channel (link = the paired shift with
  the taste-singlet grading, existence on 2D/4D U(1)), and the wall reduces to one sum (theta_g + Sum arg) plus the protector of
  the taste-singlet mass direction (K-reality/achirality = T23, and POS = T42). Outcome then MISFRAMED or PRICED.
- P2 or P3 fail (phase not tied to Q): the mass phase is not registered by Q in the tested surface; outcome would be that the
  mass half is vacuous on this surface, a different misframing, reported as such.
- Nothing in this test derives any value of theta or any mass class from the axioms; it can only move the target.
