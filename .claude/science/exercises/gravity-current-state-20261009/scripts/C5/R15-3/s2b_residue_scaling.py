"""R15-3 s2b: M1 h-weight (quantum-normalised 2*omega*|h|^2) of the two gapless branches vs |k| along z: expect k^2 (a1) and k^4 (a2)."""
import numpy as np
from s2_models import modes, tt_projector
prm = dict(m2=1.0, c1=1.0, c2=0.7, g1=0.3, g2=0.3)
for t in (1e-3, 1e-2, 1e-1):
    om, vec, H, n = modes(t * np.array([0, 0, 1.]), "M1", prm)
    sel = np.where((om > 1e-12) & (om < 0.5))[0]
    out = []
    for j in sel:
        v = vec[:, j]; v = v * np.sqrt(om[j] / np.real(v.conj() @ H @ v)); h = v[:6]
        out.append((round(om[j] / t, 5), 2 * om[j] * np.real(h.conj() @ tt_projector([0, 0, 1]) @ h)))
    print(f"|k|={t:g}: (omega/|k|, h-TT weight) = {sorted(out)}")
