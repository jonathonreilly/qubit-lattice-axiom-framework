linear-kernel-3plus1, independent run 2 of 2
worker w-jonathonsmac4f50-jd97f (claude-opus-5), unit C-linear-kernel-3plus1-a2

phi(k) = (1 + e^{ik1} + e^{ik2} + e^{ik3})/4,  u = |phi|^2 = (4 + 2 sum_j cos k_j + 2 sum_{i<j} cos(k_i - k_j))/16.
Overlap disclosure: M and c also appear in my runs of C:two-pin-interaction-linear:a2 and C:event-lattice-geometry:a2;
the symmetry group and the quartic term are new here.

(1) THE SMALL-k FORM (exact)
  1 - u = k^T M k + O(k^4),  M = I/4 - J/16 = [[3/16, -1/16, -1/16], [-1/16, 3/16, -1/16], [-1/16, -1/16, 3/16]]
  eigenvalues: 1/16 once, with eigenvector (1,1,1); 1/4 twice, on the plane orthogonal to it.
  quartic term:
    -(3 k1^4 - 4 k1^3 k2 - 4 k1^3 k3 + 6 k1^2 k2^2 + 6 k1^2 k3^2 - 4 k1 k2^3 - 4 k1 k3^3
      + 3 k2^4 - 4 k2^3 k3 + 6 k2^2 k3^2 - 4 k2 k3^3 + 3 k3^4)/192

(2) THE SYMMETRY GROUP (exact, exhaustive)
  Over all 3^9 integer matrices with entries in {-1, 0, 1} and det = +-1, the maps with u(Ak) = u(k) number 48.
  The test is exact: u is determined by the six frequency vectors
      e_1, e_2, e_3, e_1 - e_2, e_1 - e_3, e_2 - e_3,
  and u(Ak) = u(k) for all k iff A^T permutes them up to sign.
  The group is the tetrahedral group S_4 of the four predecessors {0, e_1, e_2, e_3} times the inversion k -> -k.
  Solving A^T Q A = Q over the whole group leaves a ONE-dimensional space of quadratic forms: M is the unique invariant
  form up to scale, so "isotropic in the level plane's natural geometry" is exactly the statement that the geometry is M's.

(3) THE LARGE-DISTANCE FORM (exact)
  det M = 1/256, so
      C(x) -> c/sqrt(x^T M^-1 x),   c = sigma^2/(4 pi sqrt(det M)) = 4 sigma^2/pi = 1.273240 sigma^2.

(4) FFT CHECK (numerical)
  Columns: C(x); the raw product C sqrt(x^T M^-1 x); and C divided by the same Fourier sum carried out with the symbol
  k^T M k, which carries the torus images.
    L = 64
      (1,0,0)  r=2: 0.20507, 1.1600, 1.082 | r=3: 0.12787, 1.0850, 0.958 | r=4: 0.09000, 1.0182, 1.044 | r=6: 0.05245, 0.8900, 1.033
      (1,1,0)  r=2: 0.10736, 1.0519, 1.022 | r=3: 0.06401, 0.9408, 1.018 | r=4: 0.04243, 0.8315, 1.015 | r=6: 0.02107, 0.6193, 1.013
      (1,1,1)  r=2: 0.06935, 0.9610, 0.999 | r=3: 0.03878, 0.8059, 1.002 | r=4: 0.02365, 0.6554, 1.000 | r=6: 0.00894, 0.3717, 1.000
    L = 128
      (1,0,0)  r=2: 0.21645, 1.2244, 1.077 | r=3: 0.13923, 1.1814, 0.961 | r=4: 0.10133, 1.1464, 1.039 | r=6: 0.06369, 1.0808, 1.027
      (1,1,0)  r=2: 0.11871, 1.1631, 1.020 | r=3: 0.07530, 1.1066, 1.016 | r=4: 0.05362, 1.0508, 1.013 | r=6: 0.03199, 0.9403, 1.009
      (1,1,1)  r=2: 0.08065, 1.1175, 0.999 | r=3: 0.04994, 1.0379, 1.002 | r=4: 0.03462, 0.9595, 1.000 | r=6: 0.01937, 0.8052, 1.000

  Reading of the table: at fixed x the raw product rises toward c as L doubles (for example (1,0,0) at r = 2: 1.160 at
  L = 64, 1.224 at L = 128, against c = 1.273; (1,1,1) at r = 2: 0.961 then 1.118), because the periodic images subtract a
  constant of order 1/L. Against the image-carrying reference the ratio is 1 to within about 1 % on the two diagonals and
  within 8 % on (1,0,0), where the lattice's even-odd term sits. So the plateau at c is there in the infinite-volume sense
  that the task means; at finite L it is tilted by the images, not by any change of power.

No HIT: the expectations (eigenvalues 1/16 and 1/4 twice, isotropy in M's geometry, the plateau at c) all hold.
