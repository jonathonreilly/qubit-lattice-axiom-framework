# T68 pre-registration (written before running t68_test.py)

Wall: the curvature member (light bending x2) is declared, not forced.
Hypothesis H (from reading b59/b60/b64/b112/b144/P4): at LINEAR order, the
static bending factor is 1+gamma with gamma = (length stiffness ratio) = b59's
free "beta". In any linearised-relabelling-invariant (group G) member built on a
symmetric 4-tensor h_{mu nu} with only the SPATIAL cubic symmetry S3 (+ time reversal),
I predict:
  (P1) the S3+G family is 2-dimensional (reproduce P4 T1: 26 -> 2).
  (P2) in that family the lapse-multiplier coefficient K_m (coefficient of h_00 * R^(3)_lin)
       is tied to the kinetic coefficient alpha by K_m = 4 alpha (ADM value), for EVERY member;
       the pure-length gradient stiffness K_s and hence the TT speed^2 = K_s/K_m are free.
  (P3) static gamma_PPN (spatial potential / Newtonian potential, from solving the static
       equations with a rest-mass source T^00 = rho and the matter metric eta + h) equals
       K_m/K_s = 1/(TT speed^2) for every member.
  (P4) b60's scalar-model exponent a/(2(ap-b)) (mapped from the tensor's isotropic sector)
       equals the same ratio.
  (P5) kinetic sign of the isotropic stretch c_k = 12 alpha + 36 beta_kin = -24 alpha < 0
       for every member with alpha > 0 (beta_kin = -alpha forced).
PASS (wall priced at ONE number): P1-P5 all hold. Reading: bending x2 <=> one light cone
   (c_grav = c_matter) given G; exponent p, sign of c_k, linearity are forced at linear order by G;
   only the cone ratio s = K_m/K_s stays open.
FAIL: gamma independent of K_m/K_s, or K_m/alpha not fixed, or the family is not 2-dim.
   Then the bending factor is a separate free number and the wall stays as stated (b59/b60).
Also pre-registered control: the B4 (hypercubic) Fierz-Pauli member must give s=1, gamma=1.
