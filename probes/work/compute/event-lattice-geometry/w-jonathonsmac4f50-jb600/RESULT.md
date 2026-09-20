event-lattice-geometry, independent run 2 of 2
worker w-jonathonsmac4f50-jb600 (claude-opus-5), unit C-event-lattice-geometry-a2

Setting: the level planes of Z^(d+1) in level order are the sets {x : x_1 + ... + x_(d+1) = t}, copies of the root lattice A_d.
Plane coordinates are the first d components: the site with coordinates x at level t is the lattice point (x, t - sum x).

(1) TWO BASES OF THE PLANE (exact)
  lattice displacement basis  b_j = e_j - e_(d+1)          Gram B^T B = I + J   (2 on the diagonal, 1 off it: the A_d Gram)
  projected basis             f_j = e_j - (1,...,1)/(d+1)  Gram G = I - J/(d+1)
  They are dual: f_i . b_j = delta_ij, and G = (I + J)^{-1}.
  This is the point that decides everything below: a position in the plane has components in the b-basis, a wavevector has
  components in the f-basis, and the coordinate wavevector k of e^{ik.x} IS the f-component vector of the physical wavevector.

(2) THE SMALL-k METRIC (exact)
  phi(k) = (1 + sum_j e^{i k_j})/(d+1), and 1 - |phi|^2 = k^T M k + O(k^4) with M = Cov of the uniform law on {0, e_1, ..., e_d}:
      M = (1/(d+1)) (I - J/(d+1)) = c G,   c = 1/(d+1)
      d = 2: c = 1/3     d = 3: c = 1/4     d = 4: c = 1/5
  and, with B the matrix of the b_j,
      B M B^T = c (I - J/(d+1)) = c P,   P the orthogonal projector on the plane.
  So in the plane's own Euclidean geometry the dispersion is c |kappa|^2: isotropic, with no direction singled out.

(3) THE EQUAL-LEVEL KERNEL IN 3+1 (exact, then numerical)
  d = 3: det M = 1/256 and r^T M^-1 r = 4 |X|^2, where |X|^2 = r^T (I + J) r is the squared Euclidean length on the
  face-centred cubic plane. The coordinate form sigma^2/(4 pi sqrt(det M) sqrt(r^T M^-1 r)) = (4/pi) sigma^2/sqrt(r^T M^-1 r)
  therefore becomes
      C(X) = c'/|X| ,   c' = 2 sigma^2/pi = 0.636620 sigma^2 .

  FFT at L = 64 (sigma^2 = 1). C|X|/c' is the plain law; C/periodic compares with the same Fourier sum carried out with the
  continuum symbol k^T M k, which carries the torus images:
    direction (1,0,0):  r=2 |X|=2.83: C=0.20507, C|X|/c'=0.911, C/periodic=1.082
                        r=3 |X|=4.24: C=0.12787, 0.852, 0.958
                        r=4 |X|=5.66: C=0.09000, 0.800, 1.044
                        r=6 |X|=8.49: C=0.05245, 0.699, 1.033
    direction (1,1,0):  r=2 |X|=4.90: C=0.10736, 0.826, 1.022
                        r=3 |X|=7.35: C=0.06401, 0.739, 1.018
                        r=4 |X|=9.80: C=0.04243, 0.653, 1.015
    direction (1,1,1):  r=2 |X|=6.93: C=0.06935, 0.755, 0.999
                        r=3 |X|=10.39: C=0.03878, 0.633, 1.002
                        r=4 |X|=13.86: C=0.02365, 0.515, 1.000
  Against the image-corrected law the three directions agree to 5 % or better for 3 <= |X| <= L/6, the (1,0,0) line carrying
  the familiar even-odd lattice term. The plain c'/|X| is low by the finite-size constant, which is why C|X|/c' falls with |X|.

(4) THE DRIFT (exact)
  A site's d+1 predecessors are y - e_j, j = 1..d+1. Projected orthogonally onto the plane their displacements are -f_j, and
      sum_{j=1}^{d+1} f_j = 0   exactly (d = 2, 3, 4),
  so the mean in-plane displacement per level is ZERO: there is no physical in-plane drift.
  The coordinate drift (1,...,1)/(d+1) that appears in Im phi is the motion of the chart. The site with fixed plane coordinates
  x sits at (x, t - sum x); its orthogonal projection onto the plane through the origin moves by
      f_(d+1) = e_(d+1) - (1,...,1)/(d+1)
  per level, and that displacement is exactly the coordinate drift. The chart slides; the physics does not.

READING
  Both expectations hold: the kernel is isotropic in the plane's Euclidean geometry, and the drift is a coordinate artefact.
  No HIT.
  The one thing to state carefully is which basis carries which object: G is the Gram of the projected (dual) basis, so
  M = c G means the dispersion is c times the Euclidean |kappa|^2, not c times a distance form. Reading G as the lattice's
  own Gram would turn the same equation into an anisotropy of ratio (d+1)^2 in the wrong direction.
