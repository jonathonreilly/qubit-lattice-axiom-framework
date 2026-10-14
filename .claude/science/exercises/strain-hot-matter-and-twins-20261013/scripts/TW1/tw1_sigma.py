"""TW-1 (c): one-loop self-energy Sigma(P = 0) of the REDUCED (Majorana) staggered field under SF strain, with controls.

One loop, a real-representation gauge field (e.g. SO(N) vector): the complex field in a real rep R_0 with real link matrices is
two decoupled Majorana copies (tw1_alg.out, item 2-3), so per copy Sigma_M = C_F(R_0) x [NF-1's U(1) one-loop 8x8 Sigma with e = 1]
(the group factor sum_A (iT^A)^2 = -C_F replaces i*i = -1). The evaluator below is NF-1's direct 8x8 evaluator
(scripts/C5/NF1/nf1_sigma8.py, function sigma8, copied unchanged): F1's Psym divided-difference vertices, Feynman gauge,
A_0 exchange, photon Gph(2.9435) with its own SF flow, full-BZ midpoint grid.

Reported per case: the Majorana-legal part of Sigma(0) (antisymmetric part; Sigma hermitian => i x real antisymmetric),
the Majorana-illegal symmetric part (must vanish for a Majorana-legal law: consistency check), and the components along
the 6 gap-opening Majorana masses i Geps J_a, i G5 J_a (G5 = Geps G1 G2 G3), J_a = Z_i Z_j (tw1_alg.py).
Cases:
  A  reduced law (staggered, r = 0), SF strain E_g t in {0, +-0.1, 0.2}: expect Sigma(0) = 0 (Theta_M + P_stag).
  B  control: Theta_M-breaking, P_stag-keeping, Majorana-legal local term  r_c cos(k1+k2) sum_l sin^2 k_l (i Geps J12)
     (zero at all corners; same-sublattice two-link x sin^2 operator), with the SF flow of its own band
     E^2 = sum s^2 + r_c^2 g^2 (non-separable; RK4, n = 4 as F1's flowF).
  C  control: Theta_M-keeping, P_stag-breaking, Majorana-legal local term  r_c cos(k3) sum_l sin^2 k_l (i G5 J12).
Folding covariance H(k + pi m) = P_m H(k) P_m is checked for every control term before use.
argv: N
"""
import numpy as np, sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'flat'))
from f1_lib import Phot, flowG1, CPH
from sublum import SymS

t00 = time.time()
N = int(sys.argv[1]) if len(sys.argv) > 1 else 24
BF = 0.909103708
A = SymS(BF); G = Phot(CPH)
G4 = np.load(os.path.join(HERE, 'nf1_gammas.npy'))
Gam, Geps = G4[:3], G4[3]
G5 = Geps @ Gam[0] @ Gam[1] @ Gam[2]

# J's from the shift symmetries at K = 0 (as in tw1_alg.py: Z_j[n, m] = <pi n| S_j |pi m>)
L = 2
def Zmat(j):
    bits = [((i >> 0) & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)]
    # S_j|pi m>: (S_j psi)(x) = zeta_j(x) psi(x + e_j), psi = (-1)^{m.x}  -> (-1)^{m_j} zeta_j(x) (-1)^{m.x}
    zeta = [(0, 1, 1), (0, 0, 1), (0, 0, 0)][j]
    Zm = np.zeros((8, 8))
    for a, m in enumerate(bits):
        n = tuple((mm + zz) % 2 for mm, zz in zip(m, zeta))
        Zm[bits.index(n), a] = (-1)**m[j]
    return Zm
Z = [Zmat(j) for j in range(3)]
J12, J23, J13 = Z[0] @ Z[1], Z[1] @ Z[2], Z[0] @ Z[2]
print('J check: J^2 = -1 %.1e ; commute with G4 %.1e ; (cf. tw1_alg.out: same Z_j from position space)'
      % (max(np.abs(J @ J + np.eye(8)).max() for J in (J12, J23, J13)), max(np.abs(J @ g - g @ J).max() for J in (J12, J23, J13) for g in G4)))
MASS = {'iGeJ23': 1j*Geps @ J23, 'iGeJ13': 1j*Geps @ J13, 'iGeJ12': 1j*Geps @ J12,
        'iG5J23': 1j*G5 @ J23, 'iG5J13': 1j*G5 @ J13, 'iG5J12': 1j*G5 @ J12}
bits = [((i >> 0) & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)]
def Pm(m):
    P = np.zeros((8, 8))
    for a, n in enumerate(bits):
        P[bits.index(tuple((x + y) % 2 for x, y in zip(n, m))), a] = 1
    return P

s, ds = A.s, A.ds
def wsum(kx, ky, kz): return np.sin(kx)**2 + np.sin(ky)**2 + np.sin(kz)**2
CTRL = {
    'B': dict(mat=MASS['iGeJ12'], g=lambda kx, ky, kz: np.cos(kx + ky)*wsum(kx, ky, kz),
              gx=lambda kx, ky, kz: -np.sin(kx + ky)*wsum(kx, ky, kz) + np.cos(kx + ky)*np.sin(2*kx),
              gy=lambda kx, ky, kz: -np.sin(kx + ky)*wsum(kx, ky, kz) + np.cos(kx + ky)*np.sin(2*ky)),
    'C': dict(mat=MASS['iG5J12'], g=lambda kx, ky, kz: np.cos(kz)*wsum(kx, ky, kz),
              gx=lambda kx, ky, kz: np.cos(kz)*np.sin(2*kx), gy=lambda kx, ky, kz: np.cos(kz)*np.sin(2*ky)),
}


def rk4(f, y, n):
    h = 1.0/n
    for _ in range(n):
        k1 = f(y); k2 = f(tuple(a + 0.5*h*b for a, b in zip(y, k1)))
        k3 = f(tuple(a + 0.5*h*b for a, b in zip(y, k2))); k4 = f(tuple(a + h*b for a, b in zip(y, k3)))
        y = tuple(a + h/6*(b + 2*c + 2*d + e) for a, b, c, d, e in zip(y, k1, k2, k3, k4))
    return y


def make_H(ctrl, rc, t, nrk=4):
    """H_t(k) = H_0(Phi_t(k)); H_0 = sum s(k_j) Gamma_j + rc g(k) M; SF E_g flow of E^2 = sum s^2 + rc^2 g^2."""
    c = CTRL.get(ctrl)
    def Hf(kx, ky, kz):
        kx, ky, kz = np.broadcast_arrays(np.asarray(kx, float), np.asarray(ky, float), np.asarray(kz, float))
        if t != 0.0:
            def f(y):
                x_, y_ = y
                px = s(x_)*ds(x_); py = s(y_)*ds(y_)
                if c is not None and rc != 0.0:
                    gg = c['g'](x_, y_, kz)
                    px = px + rc**2*gg*c['gx'](x_, y_, kz); py = py + rc**2*gg*c['gy'](x_, y_, kz)
                return 0.5*t*px, -0.5*t*py
            fx, fy = rk4(f, (kx.astype(float), ky.astype(float)), nrk)
        else:
            fx, fy = kx, ky
        H = (np.multiply.outer(s(fx), Gam[0]) + np.multiply.outer(s(fy), Gam[1]) + np.multiply.outer(s(kz), Gam[2])).astype(complex)
        if c is not None and rc != 0.0:
            H = H + rc*np.multiply.outer(c['g'](fx, fy, kz), c['mat'])
        return H
    return Hf


# folding + Majorana-legality checks of the control terms
rng = np.random.default_rng(1)
for nm, c in CTRL.items():
    Hf = make_H(nm, 0.3, 0.0)
    errF = errM = 0.0
    for _ in range(5):
        k = rng.uniform(-np.pi, np.pi, 3)
        H0 = Hf(*k)
        for m in bits:
            errF = max(errF, np.abs(Hf(*(k + np.pi*np.array(m))) - Pm(m) @ H0 @ Pm(m)).max())
        errM = max(errM, np.abs(Hf(*(-k)) + H0.T).max())
    Mm = c['mat']
    print('control %s: folding |H(k+pi m) - P_m H(k) P_m| %.1e ; Majorana-legal |H(-k) + H(k)^T| %.1e ; {M, Geps} %.1e ; [M, Geps] %.1e ; {M, G_j} %.1e'
          % (nm, errF, errM, np.abs(Mm @ Geps + Geps @ Mm).max(), np.abs(Mm @ Geps - Geps @ Mm).max(), max(np.abs(Mm @ g + g @ Mm).max() for g in Gam)))
Hf = make_H(None, 0.0, 0.3); errM = 0.0
for _ in range(5):
    k = rng.uniform(-np.pi, np.pi, 3); errM = max(errM, np.abs(Hf(*(-k)) + Hf(*k).T).max())
print('reduced law, strained t=0.3: Majorana-legal |H(-k) + H(k)^T| %.1e' % errM)


def sigma8(dx, dy, dz, x, Hf):
    """NF-1 nf1_sigma8.py sigma8 (Hf branch), unchanged in content."""
    n = len(x); w = 1.0/n
    z = 0*x
    H8_ = lambda a_, b_, d_: Hf(a_, b_, d_)
    H0 = H8_(0.0, 0.0, 0.0)
    Hx, Hy, Hz = H8_(x, z, z), H8_(z, x, z), H8_(z, z, x)
    Hxm, Hym, Hzm = H8_(-x, z, z), H8_(z, -x, z), H8_(z, z, -x)
    T = [(Hx + Hxm - 2*H0)/(2*dx[:, None, None]**2), (Hy + Hym - 2*H0)/(2*dy[:, None, None]**2), (Hz + Hzm - 2*H0)/(2*dz[:, None, None]**2)]
    Hxy = H8_(x[:, None], x[None, :], 0*x[:, None])
    tot = np.zeros((8, 8), complex)
    for iz in range(n):
        zz = x[iz]
        Hq = H8_(x[:, None], x[None, :], zz + 0*x[:, None])
        Hxz = H8_(x, z, zz + z)[:, None]; Hyz = H8_(z, x, zz + z)[None, :]
        Hz1 = H8_(0.0, 0.0, zz)
        Cx = Hx[:, None]; Cy = Hy[None, :]
        dX = dx[:, None, None, None]; dY = dy[None, :, None, None]; dZ = dz[iz]
        Vx = (2*(Cx - H0) + (Hxy - Cy) + (Hxz - Hz1) + 2*(Hq - Hyz))/6/dX
        Vy = (2*(Cy - H0) + (Hxy - Cx) + (Hyz - Hz1) + 2*(Hq - Hxz))/6/dY
        Vz = (2*(Hz1 - H0) + (Hxz - Cx) + (Hyz - Cy) + 2*(Hq - Hxy))/6/dZ
        Om = np.sqrt(dx[:, None]**2 + dy[None, :]**2 + dz[iz]**2)
        E, U = np.linalg.eigh(Hq)
        X = U @ ((np.sign(E)/(2*Om[..., None]*(np.abs(E) + Om[..., None])))[..., None]*U.conj().swapaxes(-1, -2))
        val = X - sum(V @ X @ V for V in (Vx, Vy, Vz))
        tad = (T[0][:, None] + T[1][None, :] + T[2][iz])/(2*Om[..., None, None])
        tot += (val + tad).sum(axis=(0, 1))*w**3
    return tot


x = -np.pi + (np.arange(N) + 0.5)*2*np.pi/N
def phot(t):
    if t == 0.0:
        d = G.d(x); return d, d, d
    return G.d(flowG1(G, np.abs(x), +1, t, 4)), G.d(flowG1(G, np.abs(x), -1, t, 4)), G.d(x)


def report(lab, S):
    asym = 0.5*(S - S.T); sym = 0.5*(S + S.T)
    comps = {k: np.real(np.trace(M.conj().T @ S))/8 for k, M in MASS.items()}
    big = sorted(comps.items(), key=lambda kv: -abs(kv[1]))[:2]
    print('  %-22s max|Sigma| %.2e | Majorana-legal (antisym) %.2e | illegal (sym) %.2e | top mass comps: %s'
          % (lab, np.abs(S).max(), np.abs(asym).max(), np.abs(sym).max(), ', '.join('%s %+.6e' % kv for kv in big)), flush=True)
    return comps


print('TW-1 one-loop Sigma(P = 0) of the reduced staggered field, full-BZ midpoint N = %d; per e^2 C_F' % N, flush=True)
print(' A: reduced law under SF strain (E_g)')
for t in (0.0, 0.1, -0.1, 0.2):
    report('A t=%+.2f' % t, sigma8(*phot(t), x, make_H(None, 0.0, t)))
for nm, key in (('B', 'iGeJ12'), ('C', 'iG5J12')):
    print(' %s: control (%s)' % (nm, 'Theta_M-breaking, P_stag-keeping' if nm == 'B' else 'Theta_M-keeping, P_stag-breaking'))
    for rc in (0.1, 0.3):
        out = {}
        for t in (0.0, 0.05, -0.05, 0.1, -0.1, 0.2):
            out[t] = report('%s rc=%.1f t=%+.2f' % (nm, rc, t), sigma8(*phot(t), x, make_H(nm, rc, t)))[key]
        h05 = (out[0.05] + out[-0.05] - 2*out[0.0])/0.05**2
        h1 = (out[0.1] + out[-0.1] - 2*out[0.0])/0.1**2
        hR = (4*h05 - h1)/3
        print('   %s rc=%.1f: dm(0) = %+.6e ; Hess_t central d=0.05 %+.4e, d=0.1 %+.4e, Richardson %+.4e ; odd part (t=+-0.1) %+.1e'
              % (nm, rc, out[0.0], h05, h1, hR, out[0.1] - out[-0.1]))
print('time %.0f s' % (time.time() - t00))
