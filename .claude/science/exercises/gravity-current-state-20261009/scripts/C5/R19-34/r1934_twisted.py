"""R19-34 (c) comparator: twisted-mass version of the root's Dirac edge, h(k) = sum_j s_j alpha_j + (m0 + sum_j W_j) beta + mu i beta gamma5
(R19-11's P-R19-11c / R19-21's 'twisted' E^2 = S^2 + (sum W)^2 + mu^2), at maximal twist (m0 = critical, O(e^2), enters E only at O(e^4)).
On-shell O(e^2) rest-energy shift from the referee-confirmed old-fashioned runner (r1610_core.dirac_pt / R13-7), rewritten for a
5-direction Clifford vector (alpha_x, alpha_y, alpha_z, beta, i beta gamma5); the vertex and seagull have no gamma5 part (mu is per site).
The rewrite with the twisted component switched off (mu -> Wilson-type m) reproduces r1934_onshell_check's Wilson-type values.
Claim tested: the twisted edge's physical-mass strain Hessian is O(mu) (-> 0 as mu -> 0), while the Wilson-type one tends to dm'' = -0.0405."""
import numpy as np, time
from r1934_lib import Grid, d1_law, photon, strain_l, hessian
t0 = time.time()

def rest_shift(Q, m_untw, mu, lam, Sf, Wf, df):
    qx, qy, qz = Q
    dd = [df[0](qx)**2, df[1](qy)**2, df[2](qz)**2]
    Wq = np.sqrt(dd[0] + dd[1] + dd[2] + lam**2)
    Ep = np.hypot(m_untw, mu)
    a = np.array([0.0, 0.0, 0.0, m_untw/Ep, mu/Ep])
    k = [-qx, qy, qz]                            # internal fermion; only squares/products enter (even integrand)
    hk = [Sf[0](k[0]), Sf[1](-qy), Sf[2](-qz), m_untw + Wf[0](k[0]) + Wf[1](-qy) + Wf[2](-qz), mu + 0*qx]
    Ek = np.sqrt(sum(c*c for c in hk)); b = [c/Ek for c in hk]
    ab = sum(a[i]*b[i] for i in range(5))
    # vertex difference vectors Delta_j = h_j(0) - h_j(k_j): components on alpha_j and beta only
    Dl = [(-Sf[0](k[0]), -Wf[0](k[0])), (-Sf[1](-qy), -Wf[1](-qy)), (-Sf[2](-qz), -Wf[2](-qz))]
    acc = 0.0
    for s in (+1, -1):
        X = -(1 + s*ab)/2
        for j in range(3):
            d2 = Dl[j][0]**2 + Dl[j][1]**2
            db = Dl[j][0]*b[j] + Dl[j][1]*b[3]; da = Dl[j][0]*a[j] + Dl[j][1]*a[3]
            X = X + (d2 + s*(2*db*da - d2*ab))/(2*dd[j])
        acc = acc + (-s*X/(2*Wq*(Wq + Ek - s*Ep)))
    tad = 0.5*a[3]*sum((Wf[j](Q[j]) + Wf[j](-Q[j]))/dd[j] for j in range(3))/(2*Wq)
    return acc + tad

def shift(s, W, d, g, l, m_untw, mu, lam):
    Sf = [lambda k, j=j: s(k)/l[j] for j in range(3)]; Wf = [lambda k, j=j: W(k)/l[j] for j in range(3)]
    df = [lambda q, j=j: d(q)/l[j] for j in range(3)]
    x, w = g.x, g.w; tot = 0.0
    for i0 in range(len(x)):
        Q = (np.full((len(x), len(x)), x[i0]), x[:, None] + 0*x[None, :], x[None, :] + 0*x[:, None])
        tot += float((w[i0]*w[:, None]*w[None, :]*rest_shift(Q, m_untw, mu, lam, Sf, Wf, df)).sum())
    return tot

s, W, L = d1_law(0.909103708, 0.555604226); d = photon('Gph', 2.9435)
g = Grid([0.909103708, np.pi - 0.909103708, 2.9435], 6, 0.25)
lam = 0.01
print('root Dirac edge D1(0.909103708, 0.555604226) + Gph(2.9435), lam = %.2f, H-cov E_g; on-shell O(e^2) rest-energy shift dE and d2dE/dh2' % lam)
for m in (1e-2, 3e-3, 1e-3):
    e0, _, _, _, hw = hessian(lambda h: shift(s, W, d, g, strain_l(h), m, 0.0, lam), 0.02)
    t0_, _, _, _, ht = hessian(lambda h: shift(s, W, d, g, strain_l(h), 0.0, m, lam), 0.02)
    print('  mass %.0e:  Wilson-type (untwisted m): dE %+.8f  Hess %+.6e   |  twisted (mu): dE %+.8f  Hess %+.6e  Hess/mu %+.4f' % (m, e0, hw, t0_, ht, ht/m), flush=True)
print('time %.0f s' % (time.time() - t0))
