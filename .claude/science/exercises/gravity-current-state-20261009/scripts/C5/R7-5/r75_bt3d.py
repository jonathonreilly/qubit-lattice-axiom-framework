"""R7-5 script 4: d = 3 lattice check of the BT mass-squared law with pair creation (s-wave,
rotationally invariant channel).  Sector at total lattice momentum P: {phi(P)} + {chi(k) chibar(P-k)}.
M^2 = diag(mu^2, M0^2(k)) + U,  U_{k,phi} = g F(|q(k)|) sqrt(|dq/dk1|_P * dk^3),  rank one =>
dressed z solves z - mu^2 - sum_k |U_k|^2/(z - M0^2(k)) = 0;  E_phi(P) = sqrt(z + P^2).
q(k) = rest-frame momentum of chi: q = k1 + [(gam-1)(k1.n) - gam*beta*E1] n, beta = P/W, gam = W/M0.
Jacobian at fixed P: |dq/dk1| = W E_q^2/(E1 E2 M0)  (E_q = M0/2)  [checked numerically below].
Leg cutoff chi(k) = prod_i plateau(k_i; 1.4, 1.8) removes zone-edge pairs; it is 1 on the support used."""
import numpy as np
from scipy.optimize import brentq
OUT = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)
def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def plateau(x, x1, x2): return 1.0 - sstep((np.abs(x)-x1)/(x2-x1))
def wrap(k): return -(((-k) + np.pi) % (2*np.pi) - np.pi)
B, B2, m, mu = 2.6, 3.0, 0.3, 0.5
KAP1, KAP2 = 0.25, 0.5
def s(k):
    k = wrap(k); r = plateau(k, B, B2); return r*k + (1-r)*np.sin(k)
def F(q): return plateau(q, KAP1, KAP2)
def legcut(k): return plateau(wrap(k), 1.4, 1.8)

def sector(L, nP):
    ks = wrap(2*np.pi*np.arange(L)/L)
    KX, KY, KZ = np.meshgrid(ks, ks, ks, indexing='ij')
    P = wrap(2*np.pi*np.array(nP)/L)
    k1 = np.stack([KX, KY, KZ]); k2 = np.stack([wrap(P[i] - k1[i]) for i in range(3)])
    s1 = np.stack([s(c) for c in k1]); s2 = np.stack([s(c) for c in k2])
    E1 = np.sqrt(m*m + (s1**2).sum(0)); E2 = np.sqrt(m*m + (s2**2).sum(0))
    W = E1 + E2; P2 = (P**2).sum(); M0 = np.sqrt(W*W - P2)
    if P2 > 0:
        n = P/np.sqrt(P2); beta = np.sqrt(P2)/W; gam = W/M0
        kn = (s1*n[:, None, None, None]).sum(0)
        q = s1 + (((gam - 1)*kn - gam*beta*E1)[None])*n[:, None, None, None]
    else:
        q = s1.copy()
    qa = np.sqrt((q**2).sum(0))
    Eq = M0/2
    jac = W*Eq**2/(E1*E2*M0)                      # |dq/dk1| at fixed P
    cut = legcut(k1[0])*legcut(k1[1])*legcut(k1[2])*legcut(k2[0])*legcut(k2[1])*legcut(k2[2])
    w8 = F(qa)*cut
    on = w8 > 0
    maxleg = max(np.abs(k1[:, on]).max(), np.abs(k2[:, on]).max())
    return P, M0**2, w8, jac, qa, maxleg

def dressed(L, nP, g):
    P, M02, w8, jac, qa, maxleg = sector(L, nP)
    dk3 = (2*np.pi/L)**3
    u2 = (g*w8)**2*jac*dk3
    on = u2 > 0
    u2, M2 = u2[on], M02[on]
    f = lambda z: z - mu*mu - np.sum(u2/(z - M2))
    z = brentq(f, -5.0, M2.min() - 1e-12)
    # Jacobian check: sum |dq/dk| dk^3 G(q) vs int d3q G(q), G = F(|q|)^2
    test = np.sum((w8**2*jac)[on])*dk3
    return np.sqrt(z + (P**2).sum()), z, test, maxleg, np.sqrt((P**2).sum())

if __name__ == '__main__':
    qq = np.linspace(0, KAP2, 200001)
    exact = np.trapezoid(4*np.pi*qq**2*F(qq)**2, qq)
    pr(f'int d3q F(|q|)^2 = {exact:.10f}')
    for g in (0.3,):
        for L in (64, 96, 128):
            rows = []
            for nP in ((0, 0, 0), (L//32, 0, 0), (L//16, 0, 0), (L//16, L//16, 0), (L//16, L//16, L//16), (L//10, L//20, 0)):
                E, z, test, maxleg, Pa = dressed(L, nP, g)
                rows.append((Pa, z, test, maxleg))
            zs = np.array([r[1] for r in rows]); ts = np.array([r[2] for r in rows])
            pr(f'g={g} L={L}: |P| = ' + ', '.join(f'{r[0]:.3f}' for r in rows))
            pr(f'   M_phys^2 = E^2 - P^2: ' + ', '.join(f'{r[1]:.10f}' for r in rows) + f'   spread {zs.max()-zs.min():.2e}')
            pr(f'   Jacobian test sum|dq/dk|F^2 dk^3 / int F^2 d3q - 1: ' + ', '.join(f'{r[2]/exact-1:+.1e}' for r in rows)
               + f'   max |k_i| of a leg on supp {max(r[3] for r in rows):.3f} (< 1.4: leg cutoff inactive)')
    with open('r75_bt3d.out', 'w') as fh:
        fh.write('\n'.join(OUT) + '\n')
