"""R16-1 (b) identification: L vs its first-order-in-W form  L1 = (1/4)<W''(q_x) w(q)> = (1/4)<W(q_x) w''(q)>,
w = (d_y^2 + d_z^2 + lam^2)/(d_x^2 Wg^3) (R13-7's heavy weight); and the tadpole piece kappa_T = <W''(q_x)/(4 d_x^2 Wg)>
(compare R13-7's 'tad' column slope, r137_mscan.out S1 gapped: (197.60 - 93.56)/25.6 = 4.064 at N = 64).
Also whole-zone v_max of the laws used (S17 rule)."""
import sys; sys.path.insert(0, '.')
import numpy as np
from r161_laws import D1Law, BQLaw
from r161_heavy import L_photon_slot, perp_grid, _gl, U
from r85_box_qed_copy import deriv
def moments(law, lam, Np=64, npan=40, nper=10):
    b = law.b1
    e = np.linspace(b, np.pi, npan + 1); xs = []; ws = []
    for a0, a1 in zip(e[:-1], e[1:]):
        x, w = _gl(a0, a1, nper); xs.append(x); ws.append(w)
    qx = np.concatenate(xs); wx = np.concatenate(ws)
    dy2, dz2, Wy, Wz = perp_grid(law, Np)
    L1 = 0.0; L1b = 0.0; kT = 0.0
    for i in range(len(qx)):
        q = qx[i]; t = law.d(q) ** 2; Wg = np.sqrt(t + dy2 + dz2 + lam ** 2)
        wgt = (dy2 + dz2 + lam ** 2) / (t * Wg ** 3)
        f = lambda s: (dy2 + dz2 + lam ** 2) / (law.d(q + s) ** 2 * (law.d(q + s) ** 2 + dy2 + dz2 + lam ** 2) ** 1.5)
        h = 1e-3; wpp = (-f(2 * h) + 16 * f(h) - 30 * f(0) + 16 * f(-h) - f(-2 * h)) / (12 * h * h)
        Wpp = deriv(law.W, np.array(q), 2)
        L1 += wx[i] * 0.25 * np.mean(Wpp * wgt); L1b += wx[i] * 0.25 * np.mean(law.W(np.array(q)) * wpp)
        kT += wx[i] * np.mean(Wpp / (4 * t * Wg))
    norm = 2 / (2 * np.pi)
    return L1 * norm, L1b * norm, kT * norm
lam = 0.05
for lab, law in (('D1(1.4, r=0.1)', D1Law(1.4, 0.1, 1.0)), ('D1(1.4, 1/sqrt3)', D1Law(1.4, 1 / np.sqrt(3), 1.0)),
                 ('D1(1.0, 1/sqrt3)', D1Law(1.0, 1 / np.sqrt(3), 1.0)), ('BQ S1 r=1 photon (1,2)', BQLaw(1.0, 2.0, 1.0, 1.0, (1.0, 2.0))),
                 ('BQ S3 r=1 photon (2,3)', BQLaw(2.0, 3.0, 1.0, 1.0, (2.0, 3.0))), ('BQ S3 r=1 naive', BQLaw(2.0, 3.0, 1.0, 1.0, 'naive'))):
    L = L_photon_slot(law, lam, Np=64) * U
    L1, L1b, kT = moments(law, lam)
    print('%-24s L*U = %+.5f | first order (1/4)<W\'\' w>*U = %+.5f, (1/4)<W w\'\'>*U = %+.5f | tadpole kappa_T*U = %+.4f' % (lab, L, L1 * U, L1b * U, kT * U), flush=True)
print('whole-zone v_max = max |grad E| over T^3 (grid 96^3 + axis lines 20001), m = 0.1, 0.3, 1:')
k = (np.arange(96) + 0.5) * 2 * np.pi / 96 - np.pi
for lab, mk in (('D1(1.4,1/sqrt3)', lambda m: D1Law(1.4, 1 / np.sqrt(3), m)), ('D1(1.2,1/sqrt3)', lambda m: D1Law(1.2, 1 / np.sqrt(3), m)),
                ('D1(1.0,1/sqrt3)', lambda m: D1Law(1.0, 1 / np.sqrt(3), m)), ('BQ S1 r=1', lambda m: BQLaw(1.0, 2.0, 1.0, m)),
                ('BQ S3 r=1', lambda m: BQLaw(2.0, 3.0, 1.0, m))):
    out = []
    for m in (0.1, 0.3, 1.0):
        law = mk(m)
        S, W = law.S(k), law.W(k); dS, dW = deriv(law.S, k), deriv(law.W, k)
        best = 0.0
        for a in range(96):
            M = m + W[a] + W[:, None] + W[None, :]
            E = np.sqrt(M ** 2 + S[a] ** 2 + S[:, None] ** 2 + S[None, :] ** 2)
            gx = (M * dW[a] + S[a] * dS[a]) / E; gy = (M * dW[:, None] + (S * dS)[:, None]) / E; gz = (M * dW[None, :] + (S * dS)[None, :]) / E
            best = max(best, np.sqrt(gx ** 2 + gy ** 2 + gz ** 2).max())
        k1 = np.linspace(-np.pi, np.pi, 20001)
        for n in (1, 2, 3):
            S1, W1, dS1, dW1 = law.S(k1), law.W(k1), deriv(law.S, k1), deriv(law.W, k1)
            M = m + n * W1; E = np.sqrt(M ** 2 + n * S1 ** 2)
            best = max(best, np.max(np.sqrt(n) * np.abs(M * dW1 + S1 * dS1) / E))
        out.append(best)
    print('  %-18s v_max(m=0.1, 0.3, 1) = %.4f %.4f %.4f' % (lab, *out), flush=True)
