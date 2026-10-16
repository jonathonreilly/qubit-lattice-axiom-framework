# Independent check: staggered block tick (B6 note)

A fresh agent context was given only the problem statement, not the note or
its runner.

- **Classes.** Signed corner actions give 4 diagonal gauge classes, matching
  H^2(S4, Z2) = Z2^2.
  - C0 is the permutation rep A1+A2+T1+T2; C1 is projectively equal to C0.
  - C2 (GL(2,3)) and C3 (2O) are spinorial. They are gauge-equivalent to each
    other and each is G3/2 + G3/2, i.e. two copies of spin 3/2.
  - This agrees with the note.
- **Propagation on {-1,0,1}^3 blocks: yes for every class.**
  - Construction: two-layer walks W = G(k) qB G(k)^dagger qA (block unitary,
    then shifted-block unitary, both in the commutant). Maximum displacement
    is 2 sites.
  - Spinorial example E1 has an exact spectrum
    cos w = (1/2)[1 +- sqrt((sum sin^2 k)/3)], with isotropic cones at
    w = +-pi/3 and identical nodes at all 8 TRIMs. Unlike the note's
    construction, it is not doubler-free.
- **Nearest-site.** Bosonic classes do have exact dispersive walks (N1), but
  an exact antipodal-symmetry argument shows they have no linear cones.
  Spinorial classes gave only flat, strictly localized solutions in 198 + 98
  converged runs. That is numerical, not proved.

Key scripts: `part1_classify.py`, `part1_decompose.py`, `part2_twolayer.py`,
`part2_cone.py`, `exact_spectra.py`, `part3_exact_eqs.py`, `part3_nn_search.py`.
Limit of independence: the checker is the same model family in a new context.
