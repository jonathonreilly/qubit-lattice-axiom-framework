D4 root-sliced fermion: at k = 0 inside a window of w the transfer has exactly one complex-conjugate (Lee-Wick) pair; at the sampled momenta and parameters the real poles have one norm sign and keep the dimension-six protection

Date: 2026-10-26
Claim type: bounded_theorem (exact group, discriminant and Jordan-Wigner facts, plus finite diagnostics on supplied free models)
Status authority: independent audit lane only. This draft sets no audit outcome.
Runner: [`scripts/d4_root_slice_fermion_positive_real_sector_lee_wick_window_keeps_dimension_six_protection_2026_10_26.py`](../scripts/d4_root_slice_fermion_positive_real_sector_lee_wick_window_keeps_dimension_six_protection_2026_10_26.py). AUDIT_TIMEOUT_SEC = 120, seeded; it exits nonzero on any failed check.
  Its cache [`logs/runner-cache/d4_root_slice_fermion_positive_real_sector_lee_wick_window_keeps_dimension_six_protection_2026_10_26.txt`](../logs/runner-cache/d4_root_slice_fermion_positive_real_sector_lee_wick_window_keeps_dimension_six_protection_2026_10_26.txt) holds the current output and counts. The source run (2.5 s, 104 MB peak) had 10 checks;
  the 2026-11-14 repair added 4b.
Pre-registration: criteria_pre_run.txt, written before any computation.
Labels: [T] exact; [F] finite diagnostic on a supplied model; [A] argument that uses a supplied literature theorem; [S] reading.
Axioms unchanged. No CL edit. Nothing adopted.

Sources used
- d4-fermion-positivity (parent).
  - Its A3 finds complex slice energies for w < sqrt2 and its A5 finds ghosts for w >= sqrt2. Both are reproduced here.
  - This note NARROWS its verdict. For w- < w < w+, every complex energy belongs to ONE conjugate pair, and every
    real branch has positive norm. The parent did not separate the two.
- d4-interacting-check: the invariant counts, and its proposal (b).
- d4-time-blind-events ([#10094](D4_TIME_BLIND_EVENTS_KILL_DIMENSION_SIX_LIV_FOR_SCALAR_FERMION_PHOTON_BUT_THE_SLICING_DECIDES_LOCALITY_AND_SIGN_BOUNDED_THEOREM_NOTE_2026-10-26.md), in this PR): root slicing is the local one.
- bosonized-sites: the exact Z2 string-end algebra.
- On main, [ADMISSIBILITY_DIRAC_KAHLER_WICK_PHASE_FINE_SITE_STAGGERED_OS_LORENTZ_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14](ADMISSIBILITY_DIRAC_KAHLER_WICK_PHASE_FINE_SITE_STAGGERED_OS_LORENTZ_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md)
  lists "perfect/anisotropic action" as UNTESTED - LIVE. Section 1b below supplies the W(F4) version of that route as
  an existence argument.
- Lane names above that are not links (d4-fermion-positivity = #10096, d4-interacting-check = #10095, bosonized-sites)
  are recorded only in the source map of [the consolidation](D4_ROUTE_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md).

Model (supplied, as in the parent)
- Events D4 = {x in Z^4 : sum x even}.
- D = 2w + m + sum over the 24 roots of e^{i r.p}(g.r - w)/12.
- Pole test at fixed transverse k:
  - G(n) = sum_j lam_j^n P_j.
  - Site positivity on the open half needs every real lam_j to have P_j g_t of ONE sign.
  - A pseudo-Hermitian transfer additionally needs the non-real lam_j to come in conjugate pairs with
    P_jbar g_t = (P_j g_t)^dagger.

(1) Why D4 fails, exactly
- [T] Check 1. W(F4) has 1152 elements and exactly 24 reflections: 12 long-root lines and 12 short lines.
  - A pure time reflection exists only for two direction classes: roots, and short directions (e1, (1,1,1,1)).
  - It does NOT exist for 24-cell edge directions (2,1,1,0) or face directions (1,1,1,0).
  - The F4 = D4* lattice is D4 rotated by M/sqrt2, which maps the short vectors to the roots. So:
    - "D4* along an axis" is D4 along a root;
    - "D4* along a root" is D4 along e1;
    - the 24-cell's vertex, edge, face and cell-centre choices are root, none, none and short.
  - So the direction census is exhaustive for pure reflections. Twisted reflections fail, per the parent's A1.
- [F] Check 3.
  - Short time (e1): there are real negative-norm branches at every w (0.5, 1, 1.2, 2; wrong-sign 1.00).
  - Edge time (2,1,1,0): the poles are not closed under conjugation, so no reflection-compatible transfer exists.
- [T] Check 4. Root time, k = 0, m = 0: both g_t sectors have discriminant 27648 (144 w^4 - 213 w^2 + 2).
  - The pole pair is complex exactly for w- < w < w+, where w-+^2 = (71 -+ 17 sqrt17)/96. So w- = 0.09721 and
    w+ = 1.21232.
  - The edge moves with m: w+(m) = 1.2139, 1.2330 and 1.2660 at m = 0.02, 0.3 and 1 (scratch bisection).
- [T] Check 4b (repair 2026-11-14). Consequence, exact for m = 0 and every w with w- < w < w+: at k = 0 each g_t sector's
  quartic has negative discriminant, hence exactly two real roots and one non-real conjugate pair. So the k = 0 slice
  transfer has non-real eigenvalues and is not a positive operator. Instances: w = 0.15, 0.5, 1.0, 1.2 show the non-real
  poles; control: w = 0.05, 1.25, 1.5 (outside the window) show none.
- [F] Check 5. Root time, 43 transverse momenta (40 random plus three special), w in {0.3, 0.7, 1.0, 1.2},
  m in {0.02, 0.3, 1}:
  - every real pole has one norm sign, to < 1e-13 (observed <= 7e-16);
  - there is exactly one complex-conjugate pair, with conjugate residues to < 2e-15;
  - its Re E is >= 0.83 (w = 0.3) up to 3.45 (w = 1.2, m = 1), in units of a^-1, rising with w;
  - outside the window (w = 0.05 and w = 1.25) a real ghost appears (wrong-sign 0.49 and 0.67).
- [F] Check 6. The light branch at w = 0.5, 1 and 1.2 has E/k -> 1, and the k^2 coefficient of E/k - 1 (the phase
  velocity minus 1; hence also of dE/dk - 1) is below 1.1e-9 in the axis, face, body and generic directions. So dimension
  six is zero on the light branch at these w.
- [F] Check 7, at w = 1, m = 0.02.
  - At the 43 sampled real k the pair stays away from the real sector: min |lam_pair - lam_real| = 0.254.
  - Correction (2026-11-14). The source text concluded that the spectral projector onto the real sector is analytic on
    the real torus and that the projected H = -ln T is exponentially local. Those need a uniform gap over the whole real
    torus, which 43 sampled momenta do not give. They are OPEN obligations, not results.
  - Every branch has rank 2.
  - The real sector consists of the light Dirac branch plus a positive staggered branch with lam < 0. That is why the
    transfer is T^2 rather than T, as with the parent's scalar.
- [F] Check 8, zoom, at one transverse momentum. On coarse slices n -> b n, the indefinite weight of the Hankel form is
  4.5e-4, 7.4e-7 and 1.3e-13 at b = 1, 2 and 4 (b = 4 and 8 are at the float floor). It falls with the rung factor;
  whether it vanishes exactly at some finite b is not computed.
- Answer to (1). The no-go "no lattice fermion with W(F4) symmetry and RP" is contradicted only by the existence argument
  (ii), which rests on supplied theorems. Item (i) does not contradict it, because the pair remains.
  - (i) [F] At the sampled w in {0.3, 0.7, 1.0, 1.2}, m in {0.02, 0.3, 1} and 43 transverse momenta, the real poles of
    the nearest-neighbour family along a root have one norm sign and the rest is one Lee-Wick pair. That real part holds
    the light fermion. Positivity and T-invariance of a real sector for all k, and for all w in the window, are not shown.
  - (ii) [A] Existence of fully RP kernels. Smear a free continuum Dirac field over an O(4)-invariant compact ball of
    radius <= half the slice spacing, centred at each D4 site, and add alpha*delta.
    - That lattice two-point function is W(F4)-invariant.
    - It is RP on the open half, because the continuum OS positivity theorem is supplied and the smeared fields of
      slices n >= 1 are supported in t >= 0.
    - Its branches are exactly E = sqrt(m^2 + |k + K_perp|^2), with residues Pi(-m^2)^2 >= 0.
    - Its inverse is exponentially local for alpha > 0, by the perfect-action argument (Bietenholz-Wiese,
      Hasenfratz-Niedermayer, supplied). This is not computed here.
    - It imports a continuum field, so it FAILS the gate as a rule. It is an existence proof only.
  - What survives is a NARROW statement, in two parts.
    - Obstruction (exact, Check 4b): for m = 0 and every w with w- < w < w+, the root-time transfer of D(w, 0) is not
      positive (non-real eigenvalues at k = 0).
    - Failed search (finite): no other member of the family that was tried had a fully positive transfer: root time at
      w = 0.05, 1.25 (real ghost) and at the sampled (w, m) above (the pair); short time e1 at w = 0.5, 1, 1.2, 2;
      the parent's second-shell sample (B1) and w >= sqrt2 cases. This rules out nothing beyond the cases tried.
  - A general finite-range no-go is NOT proven. (Negative-claim packets: see the consolidation's note on the
    2026-11-13 "Negative-claim packet" setting; none is added here.)

(2) Bosonized fermions
- [T] Check 10. Exact bosonization (Jordan-Wigner, and BKSF in a fixed flux sector, as in bosonized-sites) is a
  unitary rewriting.
  - Test: a 6-site chain with a non-normal hop that has a complex single-particle pair (Im 0.17).
  - The spin-Hamiltonian spectrum equals the fermion Fock sums for all 64 levels, to 8e-15.
  - So bosonizing a fermion keeps its complex energies, its ghosts and its dimension-six term. Bosonizing the D4
    fermion gives a non-RP bosonic weight. Bosonizing CL-1's cube hop keeps CL-1's dimension six.
  - The transplant does NOT inherit protection by itself.
- [T] Check 9, plus [A]. Conversely, a Z2-charged excitation of ANY W(F4)-invariant RP bosonic weight is positive,
  by OS reconstruction in that superselection sector.
  - Its Euclidean kernel is W(F4)-covariant. W(F4) has 1 quartic scalar, 1 cubic vector covariant (p^2 p) and 2
    quintic covariants (p^4 p, grad J6), against B4's 2, 2 and 4.
  - So its on-shell dimension six vanishes, and anisotropy first enters at dimension 8.
  - Caveat: the string attachment (ordering/branching) may make W(F4) act projectively. It is still a symmetry of the
    gauge-invariant spectrum, as the flux-sector path independence in bosonized-sites shows.
  - Not built here: an RP, W(F4)-invariant bosonic qubit/link weight on D4 that has a fermionic Z2 charge (a 3+1D
    Levin-Wen-type twisted Gauss law). That is the open construction for route (2). Check 10 shows it cannot be obtained
    by bosonizing a finite-range fermion that already fails.

(3) H4 quasicrystal (feasibility only, [S])
- Cut-and-project sets have no translation group, so there is no Bloch transfer. RP needs a reflection that maps the
  point set to itself, and H4 contains reflections.
- It has not been tested whether a reflection hyperplane through a point of the E8 projection window preserves the set.
  Locality is not tested either. Not attempted, because route (1) gave a result.

Verdict (pre-registered rule): OPEN, with existence. Deviation, stated explicitly: the pre-registered 1a criterion
required all poles real, and that is NOT met, because of the pair.
Exact: at k = 0, m = 0 the D4 root-sliced fermion has exactly one complex-conjugate pair per g_t sector for
w- < w < w+ (a lattice Lee-Wick pair). Finite diagnostics at the sampled parameters and momenta:
- the real poles have one norm sign;
- they contain one light Dirac branch with dimension six = 0;
- the only other content is one complex-conjugate pair at Re E >= 0.8-3.5 /a.
Not shown (open): T-invariance and positivity of a real sector on the whole real torus, a uniform gap, an analytic
spectral projector, and exponential locality of the projected H.

Proposed CL text (UNTESTED; for review only; NOT adopted)
  "Fermions on the time-blind D4 events take time along a root with hop weight w inside the open window
  144 w^4 - 213 w^2 + 2 < 0 (no tuning; w = 1 included). Records and odds (CL-2) are defined on the real-spectrum
  sector of the slice transfer; the complex-conjugate pair at the cutoff is never a record and never an asymptotic
  state."
Gate:
- (1) No number is chosen. The window is open and derived at k = 0, m = 0, and w = 1 is the register's natural weight.
- (2) No observed structure is named.
- (3) Untested predictions:
  - zero dimension six for matter;
  - a fermion dimension-8 J6 pattern;
  - Lee-Wick-type acausal smearing at time scales ~ 1/Im E ~ a.
- (4) Bent clause: CL-2 (Born). It restricts records to a spectral subspace, and in an interacting theory it requires a
  Lee-Wick/CLOP-type prescription. That prescription's unitarity is disputed in the literature (Lee-Wick 1969-70 and
  Cutkosky et al. 1969 for it; Nakanishi 1971 and Kubo-Kugo 2023 against). It must be logged as an axiom-level working
  rule (AX-n) if pursued.
Gate result: PASS on (1)-(3); (4) names a real bend.

Open, walls move
- (a) Interacting check: does a W(F4) Yukawa or gauge loop produce the pair on shell below 2 Re E_pair?
  - Expected: no. The pair is complex and has no real threshold, but this is untested.
  - Testable at one loop with the parent d4-interacting-check machinery.
- (b) A finite-range kernel with NO pair, using more shells.
- (c) The bosonic RP fermionic-charge construction of route (2).

Smuggling review
- Forced or exact: W(F4) and its reflections; the direction census; the discriminant and window; the invariant counts;
  the JW identity.
- Supplied: the free D(w, m) family; m values; test momenta; the continuum-smeared existence model (an import, used
  only as an existence proof); the Lee-Wick literature.
- Fitted: none.
