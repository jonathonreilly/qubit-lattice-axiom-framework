"""C5 s4d: pure unitarity minimization from the saved s4b penalty endpoint (r = 2, w = 3e6).
s4b itself was stopped (by me, to fit the session's background-time limit) during its slow LM stage;
its penalty-stage log is logs/s4b_defect_floor_penalty_stage_stopped_in_pure_stage.log. Here: trf with
bounded evaluations, 4 stages, tracking defect, min|det| and W3. Prediction (Theorem K + compactness):
no approach to defect 0 while W3 = -1 and min|det| stays near 1."""
import sys
import numpy as np
from scipy.optimize import least_squares
from w3lib import Checker
import s4_adversarial_fit_core as core
ck = Checker()
r, Nf, Nu = 2, 8, 9
H, nh, Cf, Vf, Cu = core.build(r, Nf, Nu)
p = np.load('../logs/s4b_params_penalty.npy')
uerr, sup, mind, ws = core.evaluate(p, H, nh, r)
print(f'start (s4b endpoint w=3e6): defect {uerr:.3e}  sup||U-V2|| {sup:.3f}  min|det| {mind:.4f}  W3 {ws[1].real:+.6f}', flush=True)
def pure(q):
    res, J = core.residual_and_jac(q, nh, Cf, Vf, Cu, 1.0)
    nf = 8 * len(Cf)
    return res[nf:], J[nf:]
hist = [(uerr, mind, ws[1].real)]
for it in range(4):
    sol = least_squares(lambda q: pure(q)[0], p, jac=lambda q: pure(q)[1], method='trf', max_nfev=60,
                        xtol=1e-15, ftol=1e-15, gtol=1e-15)
    p = sol.x
    uerr, sup, mind, ws = core.evaluate(p, H, nh, r)
    hist.append((uerr, mind, ws[1].real))
    print(f'pure-unitarity stage {it}: cost {sol.cost:.3e}  defect {uerr:.3e}  sup||U-V2|| {sup:.3f}  min|det| {mind:.4f}  '
          f'W3 {ws[0].real:+.6f} {ws[1].real:+.6f}', flush=True)
np.save('../logs/s4d_params_final.npy', p)
f = hist[-1]
ck.check(f'Theorem K consistency at r=2: no matrix with defect < 1e-10, W3 = -1, min|det| > 0.5 (final defect {f[0]:.2e}, W3 {f[2]:+.4f}, min|det| {f[1]:.3f})',
         not (f[0] < 1e-10 and abs(f[2] + 1) < 1e-3 and f[1] > 0.5))
ck.check('all W3 values integer to 1e-6', all(abs(h[2] - round(h[2])) < 1e-6 for h in hist))
sys.exit(ck.total())
