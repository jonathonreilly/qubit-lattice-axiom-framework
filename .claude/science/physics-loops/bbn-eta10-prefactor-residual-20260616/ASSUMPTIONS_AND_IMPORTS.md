# Assumptions And Imports

Still admitted:

- P1: proton rest mass `m_p`.
- P2: present-day CMB temperature `T_CMB`.
- P3: `H_100`, Newton constant `G`, and SI/CGS metrology constants.
- P4: exact comparator residual `S_Cyburt_exact = 0.9989276742641543`.

Repaired native arithmetic:

- radial phase-space factor `g * 4 pi / (2 pi)^3 = g / (2 pi^2)`;
- photon-density factor `n_gamma(T) = (2 zeta(3)/pi^2) T^3` for photon
  polarization count `g=2`;
- raw coefficient `0.00365541980072764`;
- exact comparator equality only after applying admitted P4 residual.
