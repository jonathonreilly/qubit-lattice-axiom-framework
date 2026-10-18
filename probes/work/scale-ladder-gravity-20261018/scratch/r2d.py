import sys, numpy as np
sys.path.insert(0, '.')
import regge_generic as RG
from r2 import R2
from r2c import comp_inv, K, HC, itt, ixx
for lam in (0.0, -0.1, -0.3):
    row = []
    for kk in [np.array([0, 0.04, 0, 0.0]), np.array([0, 0.02, 0, 0.0]), np.array([0, 0.012, 0.009, 0.0])]:
        k2 = kk @ kk; Qk = K.Q(kk) + lam*R2(K, kk); M = K.line_map(kk)
        Ttt = np.zeros(10); Ttt[itt] = 1.0; Txx = np.zeros(10); Txx[ixx] = 1.0
        Jt, Jx = np.conj(M) @ Ttt, np.conj(M) @ Txx
        try:
            xt = comp_inv(Qk, K.gauge(kk), Jt)
            Ett = (Jt.conj() @ xt).real * k2; Ext = (Jx.conj() @ xt).real * k2
            row.append(f"|k|={np.sqrt(k2):.3f}: E_tt k^2 {Ett:+.4f}, E_xt/E_tt {Ext/Ett:+.4f}")
        except np.linalg.LinAlgError:
            row.append("singular")
    print(f"Kuhn lambda={lam:+.1f}: " + "; ".join(row))
