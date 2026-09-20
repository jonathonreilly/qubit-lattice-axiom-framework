two-pin-interaction-linear, independent run 2 of 2
worker w-jonathonsmac4f50-j4dda (claude-opus-5), unit C-two-pin-interaction-linear-a2

Field: the stationary equal-time law of the linear formation model on the periodic L^3 lattice, a centred Gaussian with
C(k) = sigma^2/(1 - |phi(k)|^2) and the zero mode removed. sigma^2 = 1 throughout; every C and every interaction scales with sigma^2.
Light-cone past: phi = 1 - E(k)/7, E(k) = sum_i 2(1 - cos k_i). Backward past: phi = (1 + sum_j e^{i k_j})/4.

(1) THE PAIR OF PINS (exact)
  Conditioning the Gaussian field on theta(x1) = a and theta(x2) = b:
    the pair (theta(x1), theta(x2)) has covariance K = [[C0, Cr], [Cr, C0]], C0 = C(0), Cr = C(r),
    log density = -(1/2) v^T K^-1 v - (1/2) log det(2 pi K), v = (a, b),
    the cross term of -(1/2) v^T K^-1 v is + a b Cr/(C0^2 - Cr^2).
  So the interaction energy is
    U(r) = - a b C(r) / (C0^2 - C(r)^2) = - a b C(r)/C0^2 - a b C(r)^3/C0^4 - ...
  Like pins (a b > 0) attract wherever C(r) > 0.

(2) THE LIGHT-CONE PAST: 1/r
  1 - phi^2 = E (14 - E)/49 exactly, and E = |k|^2 + O(|k|^4), so C(k) = (7/2)/|k|^2 + O(1) and
    C(r) -> c/r  with  c = 7 sigma^2/(8 pi) = 0.278521 sigma^2   (exact)
  On the torus the zero-mode removal turns this into c(1/r - xi/L); the measured constant xi is 2.70, 2.91, 3.04 at
  L = 32, 64, 128 from the same Fourier sum with the continuum symbol (the textbook cubic Wigner constant is 2.8373).

  C(r) by FFT, as rC/c (the plain law) and as C/periodic (against c/r with the torus images):
  L = 32,  C(0) = 1.35312
    (1,0,0)  r=1: 0.726/0.754  r=2: 0.989/1.284  r=3: 0.750/0.971  r=4: 0.675/1.088  r=5: 0.575/0.976  r=6: 0.491/1.062
    (1,1,0)  r=1.41: 0.969/1.073  r=2.83: 0.766/1.019  r=4.24: 0.629/1.000  r=5.66: 0.509/0.997  r=7.07: 0.394/0.997
    (1,1,1)  r=1.73: 0.736/0.856  r=3.46: 0.687/0.989  r=5.20: 0.541/0.987  r=6.93: 0.402/0.991  r=8.66: 0.268/0.991
  L = 64,  C(0) = 1.36547
    (1,0,0)  r=1: 0.770/0.765  r=2: 1.078/1.254  r=3: 0.882/0.976  r=4: 0.849/1.068  r=5: 0.789/0.984  r=6: 0.744/1.038
    (1,1,0)  r=1.41: 1.031/1.069  r=2.83: 0.890/1.016  r=4.24: 0.813/1.000  r=5.66: 0.749/0.998  r=7.07: 0.688/0.998
    (1,1,1)  r=1.73: 0.813/0.868  r=3.46: 0.839/0.991  r=5.20: 0.764/0.991  r=6.93: 0.692/0.995  r=8.66: 0.619/0.996
  L = 128, C(0) = 1.37164
    (1,0,0)  r=1: 0.792/0.770  r=2: 1.122/1.241  r=3: 0.948/0.978  r=4: 0.937/1.060  r=5: 0.899/0.987  r=6: 0.875/1.031
    (1,1,0)  r=1.41: 1.063/1.066  r=2.83: 0.952/1.015  r=4.24: 0.906/1.000  r=5.66: 0.874/0.998  r=7.07: 0.843/0.999
    (1,1,1)  r=1.73: 0.851/0.873  r=3.46: 0.915/0.991  r=5.20: 0.878/0.992  r=6.93: 0.843/0.996  r=8.66: 0.806/0.997

  Over 3 <= r <= L/6 the largest |C/periodic - 1| is
    (1,1,0): 0.000, 0.002, 0.002 and (1,1,1): 0.013, 0.009, 0.009 at L = 32, 64, 128,
    (1,0,0): 0.088, 0.068, 0.060 - an even-odd term, high at even r and low at odd r.
  That oscillation is the lattice's staggered piece: 49/(E(14 - E)) has a second factor 1/(14 - E) peaking at the zone
  corner, which contributes (-1)^(x1+x2+x3) times a short-range profile. It cancels on the (1,1,0) line, where the parity
  is constant, and averaging neighbouring r on the axis brings the deviation under 5 %.
  Without the image term the plain c/r is low by about 2.8 r/L, which is 47 % at r = L/6.

  The interaction itself, L = 64, along the axis:
    U(r)/(a b) = -C(r)/(C0^2 - C(r)^2)  against  the periodic -C_(1/r)(r)/C0^2:
      r=1: -0.117973 vs -0.150488;  r=2: -0.081465 vs -0.064175;  r=3: -0.044066 vs -0.044972
      r=9: -0.010130 vs -0.010295;  r=10: -0.008479 vs -0.008258
    largest deviation over 3 <= r <= L/6, after averaging neighbouring r: 0.0304.

(3) THE BACKWARD PAST: the same law with an anisotropic metric
  M = Cov{0, e1, e2, e3} = (1/4) I - (1/16) J = [[3/16, -1/16, -1/16], [-1/16, 3/16, -1/16], [-1/16, -1/16, 3/16]]
  eigenvalues 1/16 along (1,1,1) and 1/4 twice across; det M = 1/256.
  1 - |phi|^2 = k^T M k + O(|k|^4), so
    C(r) = sigma^2 / (4 pi sqrt(det M) sqrt(r^T M^-1 r)) = (4/pi) sigma^2 / sqrt(r^T M^-1 r)
  EQUIPOTENTIAL SURFACES: the ellipsoids r^T M^-1 r = const, with semi-axes proportional to sqrt(eigenvalue of M):
    1/4 along (1,1,1) against 1/2 across it, so at fixed |r| the potential is twice as strong across the cone axis as along it.
    Per unit distance: sqrt(u^T M^-1 u) = 2.828 along (1,0,0), 3.464 along (1,1,0), 4.000 along (1,1,1).
  FFT at L = 64 against the anisotropic continuum kernel on the same grid:
    (1,0,0)  r=3: C=0.12787, ratio 0.958;  r=4: 0.09000, 1.044;  r=6: 0.05245, 1.033;  r=8: 0.03381, 1.028
    (1,1,0)  r=4.24: C=0.06401, ratio 1.018;  r=5.66: 0.04243, 1.015;  r=8.49: 0.02107, 1.013;  r=11.31: 0.01067, 1.012
    (1,1,1)  r=5.20: C=0.03878, ratio 1.002;  r=6.93: 0.02365, 1.000
    infinite-volume values for comparison: 0.15005 at r = 3 along the axis, 0.08663 at r = 4.24, 0.06126 at r = 5.20.

READING
  The task's expectation holds: the 1/r law appears within about 1 % along the two diagonals for 3 <= r <= L/6, once the
  torus images are included. Along the axis the even-odd lattice term reaches 6 to 9 %, which is the only deviation above
  a few percent; it is a short-range artefact of the stencil, not a change in the power.
  Two like pins attract with a Newtonian potential of strength a b c/C0^2 per unit 1/r; the backward past gives the same
  law through the metric M, with ellipsoidal equipotentials flattened by a factor 2 along the cone's axis.
