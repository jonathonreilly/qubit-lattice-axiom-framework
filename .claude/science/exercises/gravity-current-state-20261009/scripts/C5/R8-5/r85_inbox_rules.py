"""R8-5: check that BQ's Feynman rules are continuum QED inside the box (shape S3: b1=2,b2=3; photon c=(2,3)).
Spatial vertex coefficient (alpha_j part) V_j/(-e) = i[S(k)-S(k+q)]/Dhat(q), Dhat(q) = (e^{iq}-1) g(q), |Dhat| = d(q):
expected exactly e^{-iq/2} (link-midpoint phase); beta part i r[W(k)-W(k+q)]/Dhat = 0; seagull 2nd divided difference = 0;
photon d(q) = |q|; fermion E = sqrt(m^2+k^2)."""
import numpy as np, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r85_box_qed import Law, plateau
law = Law(2.0, 3.0, 1.0, 2.0, 3.0, 0.1)
rng = np.random.default_rng(1)
k = rng.uniform(-1.9, 1.9, 200000); q = rng.uniform(-1.9, 1.9, 200000)
ok = (np.abs(k + q) < 2.0) & (np.abs(k - q) < 2.0) & (np.abs(q) > 1e-6)
k, q = k[ok], q[ok]
rg = plateau(q, 2.0, 3.0); g = rg * (q / 2) / np.sin(q / 2) + (1 - rg) * 1.0
Dh = (np.exp(1j * q) - 1) * g
Va = 1j * (law.S(k) - law.S(k + q)) / Dh / (-1.0)      # coefficient of alpha_j, in units of -e... sign: V = ie[..]/Dh
Vb = 1j * (law.W(k) - law.W(k + q)) / Dh
sg = (law.S(k + q) + law.S(k - q) - 2 * law.S(k)) / law.d(q) ** 2
print(f"in-box samples: {k.size}")
print(f"max | alpha-vertex / e^(-iq/2) - 1 |      = {np.max(np.abs(Va / np.exp(-1j*q/2) - 1)):.2e}   (V_j = -e alpha_j e^(-iq_j/2))")
print(f"max | beta (Wilson) vertex part |          = {np.max(np.abs(Vb)):.2e}")
print(f"max | seagull (alpha part) |                = {np.max(np.abs(sg)):.2e}")
print(f"max | d(q) - |q| | on photon plateau        = {np.max(np.abs(law.d(q) - q)):.2e}")
E = np.sqrt(law.S(k)**2 + (0.1 + law.W(k))**2)
print(f"max | E(k) - sqrt(m^2+k^2) | (1D leg)       = {np.max(np.abs(E - np.sqrt(0.01 + k**2))):.2e}")
