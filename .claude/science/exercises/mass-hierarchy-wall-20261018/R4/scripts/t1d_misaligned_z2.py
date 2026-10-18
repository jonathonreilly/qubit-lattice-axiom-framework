"""T1d: up placements Z2(y<->z)-invariant, down placements Z2(x<->z)-invariant (misaligned residual symmetry)."""
import numpy as np
from common import MZ, LOW, CKM, LN3, obs_logs, null_N1
import t1c_symmetric_placements as T

rng = np.random.default_rng(13)
cfu, LSu, ULu = T.build(lambda h, t: h[1] == h[2] and t[1] == t[2])
cfd, LSd, ULd = T.build(lambda h, t: h[0] == h[2] and t[0] == t[2])


def ckm2(yu, yd, target=CKM):
    best, arg = np.inf, None
    for a in range(len(T.SIG)):
        iu = np.where(0.5 * np.ptp(yu - LSu[a], -1) <= LN3)[0]
        idd = np.where(0.5 * np.ptp(yd - LSd[a], -1) <= LN3)[0]
        if len(iu) and len(idd):
            V = np.einsum("aki,bkj->abij", ULu[a, iu], ULd[a, idd])
            v = np.abs(np.stack([V[..., 0, 1], V[..., 1, 2], V[..., 0, 2]], -1))
            f = np.abs(np.log(np.maximum(v, 1e-300) / target)).max(-1)
            k = np.unravel_index(np.argmin(f), f.shape)
            if f[k] < best:
                best, arg = f[k], (T.SIG[a], v[k])
    return best, arg


for label, data in (("MZ", MZ), ("LOW", LOW)):
    Yo = obs_logs(data)
    f, arg = ckm2(Yo[0], Yo[1])
    print(f"{label}: misaligned Z2, u,d masses x3 and best CKM factor x{np.exp(f):.2f}; sigma, |V| = {arg}")
Y = null_N1(rng, 100)
ok = sum(ckm2(Y[i, 0], Y[i, 1], np.exp(rng.uniform(np.log(1e-4), 0, 3)))[0] <= LN3 for i in range(100))
print(f"random (N1 masses, random CKM): pass {ok}/100")
