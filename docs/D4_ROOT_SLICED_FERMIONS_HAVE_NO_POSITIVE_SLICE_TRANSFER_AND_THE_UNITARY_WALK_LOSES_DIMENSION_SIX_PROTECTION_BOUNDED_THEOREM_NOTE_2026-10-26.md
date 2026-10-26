D4 root-sliced fermions have no positive slice transfer, and the unitary walk on the same events loses the dimension-six protection

Date: 2026-10-26
Claim type: bounded_theorem (exact group and isometry counts, plus finite diagnostics on supplied free models)
Status authority: independent audit lane only. This draft sets no audit outcome.
Runner: runner.py (this folder), AUDIT_TIMEOUT_SEC = 120, 0.6 s, 61 MB peak, seeded. Output in out.txt (10/10). A re-run
under a unique filename gave identical output.
Pre-registration: criteria_pre_run.txt, written before any computation.

Labels: [T] exact, [F] finite diagnostic on a supplied model, [S] reading.
The axioms are unchanged, CL is not edited, and nothing is adopted.

Context
- Open item from d4-interacting-check (PR #10095): fermion reflection positivity (RP) along a root. The natural site
  reflection gave an indefinite form (wrong-sign fractions 4.4e-2, 4.6e-3 and 8.9e-4 for w = sqrt2, w = 1 and the overlap).
- Main, SCALE_LADDER_GRAVITY_D4_CONE_FERMION_CONE_REFLECTION_POSITIVITY_CURVATURE_SQUARED_BOUNDED_THEOREM_NOTE_2026-10-18:
  - Its "reflection positivity" is a finite PSD check of reflected COVARIANCE matrices for supplied SCALAR (P1/NN)
    operators, at Nt = 6 and two momenta.
  - Its fermion is a 16-component Whitney/Dirac-Kahler complex, checked only for cones and soft-eigenvalue counts. No
    fermion RP is shown on main.
  - It is consistent with this note. The Dirac-Kahler carrier is NOT tested here (see Open).

Setup (supplied, as in the parent runners)
- Events: D4 = {x in Z^4 : sum x even}. Time runs along the root r_t = (1,1,0,0), with slice n = x.r_t.
- Each slice is a cubic lattice of spacing sqrt2. Alternate slices are body-centre shifted, so they are CL-1's two tilings.
  - A slice event reaches the 8 cube corners of the next slice (16 roots), plus the r_t hop to n +- 2 and 6 in-slice roots.
- Fermion: D = 2w + m + sum_r e^{i r.p}(g.r - w)/12, the W(F4)-covariant nearest-neighbour family.
- Method: at fixed transverse momentum k, D(z; k) is a Laurent polynomial in z (z^n per slice, powers -2..2).
  - For n >= 1, the slice propagator is G(n) = sum_j lam_j^n P_j, a sum over the poles (exact block-companion
    eigenvalues; residues by contour integral).
  - Any Hilbert space with Hermitian slice transfer T (so T^2 >= 0) whose adjoint is slice-local needs two things:
    - every lam_j real;
    - every P_j Gamma Hermitian and of ONE sign, for a pairing psi^dag ~ psibar Gamma(k).
  - This necessary condition does not depend on which reflection is chosen. The adjoint must keep k, because the
    translations are unitary.

Route A: twisted / any slice-local reflection. FAIL
- [T] A1. Isometries x -> A x + c, with A in W(F4), A^2 = 1 and A r_t = -r_t, map slice n to K - n.
  - A pure reflection needs c = lambda r_t in D4, so K = 2 lambda is even: it is site-type. This is exact.
  - Link-type maps (K odd) exist only twisted: 7 found, 0 pure.
  - A twisted map pairs transverse momentum k with A k != k (min |A k - k| = 1.11 at the test k). The Gram form on
    {f_k, f_Ak} is then [[0, X], [X*, 0]], with eigenvalues +-|X|. It is indefinite whenever X != 0. Even the scalar
    fails: |X| = 0.015.
  - Charge-conjugation twists pair psi with psi. By U(1) that Gram form vanishes identically, so it gives no Hilbert space.
- [F] A2. Calibration on Z^4 (time axis):
  - Wilson r = 1: one real pole, definite (T >= 0), to 3e-16.
  - Naive: real poles at +-lam. lam P_j is definite (link RP, 1e-16), but P_j is not (T indefinite, 1.00).
  - These are the known results, so the test discriminates.
- [F] A3. D4 family, root time:
  - The slice energies are COMPLEX for every w < sqrt2: Im/|z| = 0.99-1.0 at w = 0, 0.5, 1 and 1.40. At those w, no
    Hermitian transfer exists for ANY reflection.
  - They are real for w >= sqrt2 (< 5e-15 at 1.42-3). The threshold is at w = |r| = sqrt2, the projector point, to 1e-5.
- [F] A4. For w >= sqrt2:
  - The per-k space of Hermitian pairings Gamma(k) is 2-dimensional: g_t and a spatial spin generator.
  - Minimising over that whole circle, the wrong-sign fraction stays 0.96 / 0.995 / 0.999 (w = 1.5 / 2 / 3).
- [F] A5. Where the extra norms come from: the r_t hop (n +- 2) is forced by W(F4), since r_t is a root. It doubles the time
  branches. With the light branch normalised positive, these heavy branches carry negative norm:
  - w = sqrt2: one ghost, at E = 1.85;
  - w = 1.5, 2, 3: two ghosts each, at E = (1.67, 6.16), (1.12, 4.29), (0.71, 3.74).
  - Units are the D4 coordinate unit^-1, where a root has length sqrt2.
- Overlap: its kernel is not polynomial in z (it has a cut), so A3-A5 do not apply to it. Only the parent's natural-Theta
  result stands (indefinite, 8.9e-4). It is not re-tested here.

Route B: modified D4 fermion. FAIL
- [F] B1. Adding the second W(F4) shell (24 norm-4 vectors, independent w2 and b2) keeps the time range at +-2.
  - Random search over 50 points (w1, w2, b2): 42 have complex energies, 8 are real but indefinite, 0 are positive.
- [F] B2. Time-projector variant: crossing hops -K(q) P_-/+ with K = prod cos(q_j/sqrt2), r_t hop removed, in-slice
  Wilson-Dirac. It breaks W(F4) down to the 48-element root stabiliser.
  - T >= 0 holds: one pole, definite to 1e-16 (Luscher structure). But:
    - (i) the speed equals 2 b_s, so the cone has to be tuned (b_s = 1/2);
    - (ii) dim-6 returns: v - 1 = c k^2 with c = (1.5 ws - 1/4) - (sum n^4)/3. The anisotropic part, body - axis = 2/9, is
      the same for every ws;
    - (iii) K(q) = 0 on the real surface q_j = pi/sqrt2. There T(k) = 0 (no poles), so H = -ln T is infinite on real
      momenta and the step is not exponentially local. This is the parent's axis-slicing failure, moved into the fermion.
  - It fails the gate: the tuned cone is a chosen number.

Route C: unitary real-time walk on the D4 events. Works as a real-time definition; NO protection
- [T] C0. In real time, the only symmetry that survives is the stabiliser of r_t in W(F4): 48 elements, the slice's cube
  group.
  - Its quartic invariants number 2 on the slice ((k^2)^2 and sum k^4). On R^4 the stabiliser of +-r_t has 4 against
    W(F4)'s 1.
  - So nothing forbids dim-6 in real time. Even the isotropic k^4 term in omega(k) is boost-violating, and only W(F4)
    acting on the full Euclidean 4-momentum kills it on shell.
- [F] C1. Walk: each half-tick is the 8-corner hop prod_j exp(-i alpha_j q_j/sqrt2), which goes from one D4 slice to the next.
  Two half-ticks are applied in palindromic order (the two tilings).
  - It is unitary to 1e-15, with speed 1.
  - v - 1 = -(1 - sum n^4)/6 (k a_D4)^2: axis 0, face -1/12, body -1/9, generic -0.0825. It is subluminal and zero only
    along the slice axes.
  - It has the same O_h shape as CL-1's c_q = -S/6 + 1/24 (other units).
- [F] C2. Control: the Euclidean W(F4) kernel's light branch (w = 1) has a k^2 coefficient below 7.4e-10 in every direction.
  So the protection is real in the Euclidean weight and is lost in the unitary step.

Verdict (pre-registered rule): NONE
- A fails: no slice-local reflection, twisted or not, works.
- The W(F4) family of B fails.
- C gives a unitary, strictly local fermion, but with dim-6 nonzero.
- So the D4 law does NOT survive for fermions as written. Its dim-6 protection is a theorem for the Euclidean weight, and
  that weight's fermion sector has no positive slice Hilbert space:
  - complex energies for w < sqrt2;
  - 1-2 negative-norm time branches at E ~ 0.7-6 in lattice units for w >= sqrt2.
- Every positive or unitary fermion found keeps only the stabiliser's O_h, and dim-6 comes back.

Proposed amendment to the CL register entry (text only; UNTESTED; owner/review decides):
  "Time-blind D4 event law, fermions: the W(F4) Euclidean weight has no positive slice transfer along a root. For hop weight
  w < sqrt2 the slice energies are complex; for w >= sqrt2 there are 1-2 negative-norm time branches at the cutoff. Its
  dimension-six protection therefore holds for bosons only (scalar site-RP holds). Matter keeps CL-1's unitary half-tick,
  whose dimension-six term the root-slice symmetry does not remove."
Gate for the amendment: it is a narrowing, not a new rule. Nothing is fitted, no observed structure is named, and no clause
bends. The projector variant FAILS the gate (tuned cone b_s).

Readings and routes still open [S] (walls move)
- (a) Cutoff-ghost reading. The light branch is positive, and the ghosts sit at E >~ 0.7/a.
  - This is the lattice-QCD Symanzik situation, but the lattice here is physical.
  - Accepting it would bend CL-2 (Born) above about 0.7 E*, so it needs an axiom-level working rule.
- (b) The 16-component Dirac-Kahler/Whitney D4 fermion on main (a different carrier). Its transfer is untested; the same
  pole test applies.
- (c) Hop weights that make the r_t coupling a pure time projector. These cannot be W(F4)-covariant, because r_t's hop is
  (g.r_t - w)/12. The open question is a mixed weight that still kills the extra branches.
- (d) A walk rule forcing both O_h quartic coefficients to vanish. That needs a reason, not a tuning.

Smuggling review
- Forced or exact: W(F4) and its stabiliser; the invariant counts; the isometry census; the Z^4 calibrations; the pole
  structure.
- Supplied: the free Wilson family and its second shell; the projector variant; the palindromic walk; m = 0.3 and 0.02; the
  test momenta.
- Nothing is fitted. No observed structure is named.

Deviations from the pre-registration
- The A2 plan ("Gram form for each twisted map times 16 Clifford Gammas") was replaced by two things:
  - the exact pairing argument plus the scalar |X| check;
  - the stronger, reflection-independent per-k Gamma(k) test (A4), which covers every slice-local pairing, Clifford or not.
- Route B's GW/overlap and doubler checks were not run, because no positive W(F4) point exists to check.
- Route C's "step angle theta scan": on the D4 event set a half-tick must hop to the corners, so a "stay" amplitude is not
  an event move. The walk has no angle parameter, and only the palindromic full step was tested.
