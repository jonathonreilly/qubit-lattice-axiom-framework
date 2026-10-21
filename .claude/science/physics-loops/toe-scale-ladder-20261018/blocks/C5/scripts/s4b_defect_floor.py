"""C5 s4b: does the range-2 near-unitary W3 = -1 fit of s4 approach exact unitarity?

s4 found range-2 Laurent matrices with W3 = -1 and unitarity defect 6.7e-5 (w = 3000), decreasing
with w. Theorem K + compactness (Corollary D(ii)) predict a strictly positive floor eps_2 for the
defect within W3 != 0, or else a collapse of min|det| (a change of W3) along any sequence whose
defect -> 0. A defect -> 0 with W3 = -1 and min|det| bounded below would be a COUNTEREXAMPLE to
Theorem K. Test: continue the penalty (w up to 3e6), then drop the fit term entirely and minimize the
pure unitarity residual from the last point. Track defect, min|det| and W3 at every stage.
Parameters are saved to logs/s4b_params.npy.
"""
import sys
import numpy as np
from scipy.optimize import least_squares
from w3lib import Checker
import s4_adversarial_fit_core as core

ck = Checker()
r, Nf, Nu = 2, 8, 9
H, nh, Cf, Vf, Cu = core.build(r, Nf, Nu)
kq, Vq = core.V2_on_grid(32, 0.0)
Ftr = np.einsum('kn,kij->nij', np.conj(np.exp(1j * kq @ H.T)), Vq) / len(kq)
p = np.concatenate([Ftr.real.ravel(), Ftr.imag.ravel()])
hist = []
for w in (0.3, 3.0, 30.0, 300.0, 3000.0, 3e4, 3e5, 3e6):
    sol = least_squares(lambda q: core.residual_and_jac(q, nh, Cf, Vf, Cu, w)[0], p,
                        jac=lambda q: core.residual_and_jac(q, nh, Cf, Vf, Cu, w)[1],
                        method='trf', max_nfev=300, xtol=1e-14, ftol=1e-14, gtol=1e-14)
    p = sol.x
    uerr, sup, mind, ws = core.evaluate(p, H, nh, r)
    hist.append(('penalty', w, uerr, sup, mind, ws[1].real))
    print(f'penalty w={w:9.1e}: defect {uerr:.3e}  sup||U-V2|| {sup:.3f}  min|det| {mind:.4f}  W3(N=40,56) {ws[0].real:+.6f} {ws[1].real:+.6f}', flush=True)
np.save('../logs/s4b_params_penalty.npy', p)
# pure unitarity minimization (fit weight 0): residual = U U^dag - 1 on the exact grid only
def pure(q):
    res, J = core.residual_and_jac(q, nh, Cf, Vf, Cu, 1.0)
    nf = 8 * len(Cf)
    return res[nf:], J[nf:]
for it in range(4):
    sol = least_squares(lambda q: pure(q)[0], p, jac=lambda q: pure(q)[1], method='lm', max_nfev=2000,
                        xtol=1e-15, ftol=1e-15, gtol=1e-15)
    p = sol.x
    uerr, sup, mind, ws = core.evaluate(p, H, nh, r)
    hist.append(('pure', it, uerr, sup, mind, ws[1].real))
    print(f'pure-unitarity stage {it}: defect {uerr:.3e}  sup||U-V2|| {sup:.3f}  min|det| {mind:.4f}  W3 {ws[0].real:+.6f} {ws[1].real:+.6f}', flush=True)
np.save('../logs/s4b_params_pure.npy', p)
final = hist[-1]
ck.check('Theorem K consistency: the run did NOT produce a range-2 matrix with defect < 1e-10, W3 = -1 and min|det| > 0.5 '
         f'(final: defect {final[2]:.2e}, W3 {final[5]:+.4f}, min|det| {final[4]:.3f})',
         not (final[2] < 1e-10 and abs(final[5] + 1) < 1e-3 and final[4] > 0.5))
w3_vals = [h[5] for h in hist]
ck.check('W3 values along the whole run are integers to 1e-6 (GL formula sanity)', all(abs(v - round(v)) < 1e-6 for v in w3_vals))
sys.exit(ck.total())
