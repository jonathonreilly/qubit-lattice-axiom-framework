"""C5 s4c: range-1 version of s4b (cheap): penalty continuation to w = 3e6, then pure unitarity LM.
Same prediction as s4b: a positive defect floor eps_1 within W3 != 0 (Theorem K + compactness), or det collapse."""
import sys
import numpy as np
from scipy.optimize import least_squares
from w3lib import Checker
import s4_adversarial_fit_core as core
ck = Checker()
r, Nf, Nu = 1, 10, 5
H, nh, Cf, Vf, Cu = core.build(r, Nf, Nu)
kq, Vq = core.V2_on_grid(32, 0.0)
Ftr = np.einsum('kn,kij->nij', np.conj(np.exp(1j * kq @ H.T)), Vq) / len(kq)
p = np.concatenate([Ftr.real.ravel(), Ftr.imag.ravel()])
hist = []
for w in (0.3, 3.0, 30.0, 300.0, 3000.0, 3e4, 3e5, 3e6, 3e7):
    p = least_squares(lambda q: core.residual_and_jac(q, nh, Cf, Vf, Cu, w)[0], p,
                      jac=lambda q: core.residual_and_jac(q, nh, Cf, Vf, Cu, w)[1],
                      method='trf', max_nfev=1000, xtol=1e-15, ftol=1e-15, gtol=1e-15).x
    uerr, sup, mind, ws = core.evaluate(p, H, nh, r)
    hist.append((uerr, mind, ws[1].real))
    print(f'penalty w={w:9.1e}: defect {uerr:.3e}  sup||U-V2|| {sup:.3f}  min|det| {mind:.4f}  W3 {ws[0].real:+.6f} {ws[1].real:+.6f}', flush=True)
def pure(q):
    res, J = core.residual_and_jac(q, nh, Cf, Vf, Cu, 1.0)
    nf = 8 * len(Cf)
    return res[nf:], J[nf:]
for it in range(3):
    p = least_squares(lambda q: pure(q)[0], p, jac=lambda q: pure(q)[1], method='lm', max_nfev=5000,
                      xtol=1e-15, ftol=1e-15, gtol=1e-15).x
    uerr, sup, mind, ws = core.evaluate(p, H, nh, r)
    hist.append((uerr, mind, ws[1].real))
    print(f'pure-unitarity stage {it}: defect {uerr:.3e}  sup||U-V2|| {sup:.3f}  min|det| {mind:.4f}  W3 {ws[0].real:+.6f} {ws[1].real:+.6f}', flush=True)
np.save('../logs/s4c_params_final.npy', p)
f = hist[-1]
ck.check(f'Theorem K consistency at r=1: no matrix with defect < 1e-10, W3 = -1, min|det| > 0.5 (final defect {f[0]:.2e}, W3 {f[2]:+.4f}, min|det| {f[1]:.3f})',
         not (f[0] < 1e-10 and abs(f[2] + 1) < 1e-3 and f[1] > 0.5))
ck.check('all W3 values integer to 1e-6', all(abs(h[2] - round(h[2])) < 1e-6 for h in hist))
sys.exit(ck.total())
