"""Physical sizes of the box-QED one-loop split (arithmetic only)."""
import numpy as np
alpha = 1 / 137.035999; u = alpha / (4 * np.pi)        # e^2/16pi^2
bound = 2.66e-19                                      # c_gamma - c_e < 2 m_e^2/E^2 at E = 1.4 PeV (F2 referee arithmetic)
me = 0.51099895e-3                                    # GeV
for lab, D in [("S7 (b1=1,b2=3) smallest |Delta|", -11.03), ("S3 (b1=2,b2=3) m->0", -21.8),
               ("near-SLAC S8 (2.5,3.1)", -71.2), ("S3, r=32 heavy edge", -712.6), ("no box, Wilson r=1", -22.1)]:
    dc = D * u
    Eth = 2 * me / np.sqrt(2 * abs(dc))              # photon-decay threshold (c_gamma > c_e): E^2 * 2|dc| = 4 m_e^2
    print(f"{lab:34s} Delta={D:+8.2f} e^2/16pi^2 -> c_e - c_gamma = {dc:+.3e};  ratio to 2.66e-19 bound = {abs(dc)/bound:.1e};"
          f"  gamma->ee open above {Eth*1e3:.1f} MeV")
print(f"e^2/16pi^2 = alpha/4pi = {u:.4e}")
