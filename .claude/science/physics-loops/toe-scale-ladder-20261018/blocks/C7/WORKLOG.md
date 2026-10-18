# C7 worklog (massive continuum limit of the 3D two-qubit Dirac walk)

- 20:25Z start. Read SCIENCE_WORKFLOW §2, SCALE_LADDER_MAP C7, the full
  TWO_QUBIT_SITE_UNFREEZES note (2026-10-16) and its runner, and the first 250
  lines of GAPPED_CONTINUUM_LIMIT (2026-10-12) for its proof style.
- Fixed the definition: Clifford family U = f + i h.tau + i tau3 g.sigma with
  (f,h1,h2) = F phi(k), F^T F = G(b). Every member at fixed b is O F0 with O in O(3).
  So the mass is the angle of F(0) from e_f, and it is not a new parameter.
- Literature (web search, abstracts only): Arrighi-Forets-Nesme arXiv:1307.3524
  (convergence at fixed time, discrepancy O(eps^2) for their split walk);
  D'Ariano-Perinotti PRA 90 062106 (arXiv:1306.1934; bcc Weyl automata coupled
  into Dirac; Dirac recovered at small k and m; Lorentz distorted in the UR regime);
  Bisio-D'Ariano-Tosini Ann. Phys. 354 (2015) 244 (arXiv:1212.2839; 1D Dirac QCA;
  channel discrimination; dispersive wave-packet equation). I read no full texts.
- c7_exact.py run 1: 30/6. Five failures were sympy non-simplification: radsimp
  did not expand, and a chiral-rotation matrix was pre-simplified before the
  difference was taken. One was a real error in my own series:
  arccos(1-u)^2 = 2u + u^2/3 + 4u^3/45. I had copied 8/45 from the parent runner,
  where it is wrong. It enters only at O(k^6) and is irrelevant to my O(eps^4)
  claims. Fixed. Run 2: 36/0.
- Found while doing this: the parent runner's omega2_series uses 8u^3/45. This
  changes only the isotropic |k|^6 coefficient x of parent Theorem 7, from
  s^2(8s^4-5s^2+2)/360 to s^2(4s^4-5s^2+2)/360, and at b_iso from 1/243 to 1/1215.
  The anisotropic y = -s^2/360 and z are unaffected because u^3 is isotropic at
  leading order. c7_numeric checks this at 60 digits (independent path: direct arccos).
- c7_numeric run 1 (logs/c7_numeric_run1.log): 68/2. Both failures were my wrong
  expectation for the rotation defect at b_iso: the measured slope was 3.00, and I had
  expected 2. Explanation, proved and added to c7_exact: the O(k^3) anisotropy of g is
  ((b1 + 2 b2 - b0)/6) k_a^3, which vanishes on the k^4-isotropy plane. It is the only
  O(a^2) rotation breaking in H_a. I changed the expectation to 3 on the plane and kept
  2 elsewhere, and I record the revision in the script. c7_exact: 37/0.
- Wrote NOTE.md. Re-running c7_numeric (about 25 min at nice 10 on one core).
