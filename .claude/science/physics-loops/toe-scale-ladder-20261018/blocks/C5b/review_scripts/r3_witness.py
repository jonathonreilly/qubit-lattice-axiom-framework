"""r3: independent spot-check of the witness T2 = e^{ik_x} Q_211 and T3 = T2 (+) e^{-0.5i} e^{-2ik_x}.
Q_211 = S_x(2k_x) S_y(k_y) S_z(k_z), S_a(q) = cos q + i sin q sigma_a = exp(i q sigma_a).
Own construction (no import of lib5b/walks5b)."""
import numpy as np
from scipy.optimize import minimize
import rlib as R

T = R.Tally()
ex = lambda q, s: np.cos(q)[..., None, None] * np.eye(2) + 1j * np.sin(q)[..., None, None] * s

def Q(K):
    return ex(2 * K[..., 0], R.SX) @ ex(K[..., 1], R.SY) @ ex(K[..., 2], R.SZ)

def T2(K):
    return np.exp(1j * K[..., 0])[..., None, None] * Q(K)

def T3(K):
    U = np.zeros(K.shape[:-1] + (3, 3), complex)
    U[..., :2, :2] = T2(K); U[..., 2, 2] = np.exp(-0.5j - 2j * K[..., 0])
    return U

# finite range: Fourier support on a 16^3 grid
g = np.arange(16) * 2 * np.pi / 16
K = np.stack(np.meshgrid(g, g, g, indexing='ij'), -1)
F = np.fft.fftn(T2(K), axes=(0, 1, 2)) / 16 ** 3
m = np.fft.fftfreq(16, 1 / 16).astype(int)
supp = [(m[i], m[j], m[k]) for i, j, k in zip(*np.nonzero(np.abs(F).max((-1, -2)) > 1e-12))]
rx = max(abs(s[0]) for s in supp); ry = max(abs(s[1]) for s in supp); rz = max(abs(s[2]) for s in supp)
print(f'T2 Fourier support: |m_x|<={rx}, |m_y|<={ry}, |m_z|<={rz}, {len(supp)} hops')
uni = np.abs(T2(K.reshape(-1, 3)) @ np.conj(np.swapaxes(T2(K.reshape(-1, 3)), -1, -2)) - np.eye(2)).max()
T.check(f'T2 is a finite-range (r_x={rx}) unitary Laurent walk (unitarity err {uni:.1e})', rx == 3 and ry == 1 and rz == 1 and uni < 1e-13)

for W, nm in ((T2, 'T2'), (T3, 'T3')):
    ws = [R.w3_grid_fd(W, N, 0, 2 * np.pi, h=1e-5) for N in (20, 23)]
    print(f'{nm}: W3 grid sums N=20,23: {ws[0].real:+.2e}, {ws[1].real:+.2e}')
    T.check(f'{nm}: W3 = 0 (degree <= 6r=18 per axis integrand, N >= 19 grid exact up to FD error)', all(abs(w) < 1e-6 for w in ws))

# --- analytic inventory of Q nodes (Q = +-1): (A) sin2kx=sin ky=sin kz=0, (B) cos2kx=cos ky=cos kz=0
qn = [np.array([a, b, c]) for a in (0, np.pi/2, np.pi, 3*np.pi/2) for b in (0, np.pi) for c in (0, np.pi)]
qn += [np.array([a, b, c]) for a in (np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4) for b in (np.pi/2, 3*np.pi/2) for c in (np.pi/2, 3*np.pi/2)]
okq = all(min(np.abs(Q(p[None])[0] - np.eye(2)).max(), np.abs(Q(p[None])[0] + np.eye(2)).max()) < 1e-14 for p in qn)
T.check('the 32 analytic points all have Q = +-1 (16 of family A, 16 of family B)', okq and len(qn) == 32)
# numeric completeness of Q = +-1: minimise ||Q -+ 1|| from 400 random starts
rng = np.random.default_rng(11)
found = []
for x0 in rng.uniform(0, 2 * np.pi, (400, 3)):
    for sgn in (1, -1):
        f = lambda k: np.abs(Q(k[None])[0] - sgn * np.eye(2)).sum()
        r = minimize(f, x0, method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-12, maxiter=4000))
        if r.fun < 1e-7:
            kk = np.mod(r.x, 2 * np.pi)
            if not any(np.abs(np.mod(kk - q + np.pi, 2*np.pi) - np.pi).max() < 1e-4 for q in found):
                found.append(kk)
extra = [k for k in found if not any(np.abs(np.mod(k - q + np.pi, 2*np.pi) - np.pi).max() < 1e-4 for q in qn)]
print(f'numeric search: {len(found)} distinct Q = +-1 points found, {len(extra)} outside the analytic list')
T.check('no Q = +-1 point outside the analytic 32 (sampled minimisation)', len(extra) == 0)

# level-0 degeneracies of T2 = Q-nodes with e^{i p_x} Q(p) = 1
lev0 = [p for p in qn if np.abs(T2(p[None])[0] - np.eye(2)).max() < 1e-13]
print('level-0 degenerate points of T2:', [tuple(np.round(p / np.pi, 3)) for p in lev0], '(units of pi)')
T.check('T2 has exactly 4 degenerate points at level 0: (0,0,0),(0,pi,pi),(pi,0,pi),(pi,pi,0)', len(lev0) == 4)
for W, nm in ((T2, 'T2'), (T3, 'T3')):
    chis = []
    for p in lev0:
        chi, v, t, tv, tvT, D = R.weyl_data(W, p, 0.0)
        # basis dependence of the author's |v^-T t|: redo with a rotated degenerate basis
        ch, rk = R.chern_surface_faces(W, R.cube_faces(p, 0.1), 0.0, np.pi, 20)
        sv = np.linalg.svd(v, compute_uv=False)
        print(f'  {nm} node {tuple(np.round(p / np.pi, 2))}pi: chi={chi:+d} t={np.round(t, 6)} sv(v)={np.round(sv, 6)} '
              f'|v^-1 t|={tv:.6f} (author quantity |v^-T t| in this basis {tvT:.3f}); box(0.1) Ch={ch:+.6f} ranks {rk}')
        chis.append((chi, ch, tv))
    T.check(f'{nm}: all 4 level-0 nodes chi = -1, box Ch = -1, |v^-1 t| = 1/2 exactly (type I)',
            all(c == -1 and abs(h + 1) < 1e-6 and abs(tv - 0.5) < 1e-6 for c, h, tv in chis))

# analytic linearisation at the 4 nodes: T2 ~ 1 + i(dk_x + 2dk_x sx + dk_y sy + dk_z sz) => t = (-1,0,0), v = -diag(2,1,1)
# basis dependence of |v^-T t|: v -> v R for R in SO(3)
v0 = -np.diag([2.0, 1, 1]); t0 = np.array([-1.0, 0, 0])
vals = []
for _ in range(200):
    A = rng.normal(size=(3, 3)); Rm, _ = np.linalg.qr(A); Rm *= np.sign(np.linalg.det(Rm))
    v1 = v0 @ Rm
    vals.append((np.linalg.norm(np.linalg.solve(v1.T, t0)), np.linalg.norm(np.linalg.solve(v1, t0))))
vals = np.array(vals)
print(f'|v^-T t| over random degenerate bases: min {vals[:,0].min():.3f} max {vals[:,0].max():.3f};  |v^-1 t|: {vals[:,1].min():.6f}..{vals[:,1].max():.6f}')
T.check('author type-I parameter |v^-T t| is basis dependent (spread > 0.3), invariant |v^-1 t| = 0.5', np.ptp(vals[:, 0]) > 0.3 and np.ptp(vals[:, 1]) < 1e-9)

# --- Fermi sheets at level 0: f(k) = e^{-ik_x} det(T2 - 1) = 2(cos k_x - Re tr Q / 2 * 2/2) is real
def fsheet(K):
    U = T2(K)
    return (np.exp(-1j * K[..., 0]) * np.linalg.det(U - np.eye(2)))
Kr = rng.uniform(0, 2 * np.pi, (2000, 3))
fv = fsheet(Kr)
T.check(f'f = e^(-ikx) det(T2-1) is real (max |Im| = {np.abs(fv.imag).max():.1e}) and = 2cos kx - tr Q', np.abs(fv.imag).max() < 1e-12
        and np.abs(fv.real - (2 * np.cos(Kr[:, 0]) - np.trace(Q(Kr), axis1=-2, axis2=-1).real)).max() < 1e-12)
p0 = np.array([2 * np.pi / 3, 0, 0])
lam = np.linalg.eigvals(T2(p0[None])[0]); dd = np.sort(np.abs(lam - 1))
h = 1e-6; grad = np.array([(fsheet((p0 + h * e)[None]) - fsheet((p0 - h * e)[None]))[0].real / (2 * h) for e in np.eye(3)])
print(f'sheet point (2pi/3,0,0): eigenvalue distances to 1 = {dd}, grad f = {np.round(grad, 6)}')
T.check('(2pi/3,0,0) is a non-degenerate level-0 point with grad f != 0 (implicit fn thm => a 2D sheet through it)',
        dd[0] < 1e-12 and dd[1] > 0.5 and np.linalg.norm(grad) > 1)
# sign changes of f along 300 random k_x-lines, away from the 4 nodes
nsc = 0; nlines = 0
xs = np.linspace(0, 2 * np.pi, 2001)
for (ky, kz) in rng.uniform(0, 2 * np.pi, (300, 2)):
    L = np.stack([xs, np.full_like(xs, ky), np.full_like(xs, kz)], -1)
    s = np.sign(fsheet(L).real)
    c = int((s[1:] * s[:-1] < 0).sum()); nsc += c; nlines += c > 0
print(f'sign changes of f on 300 random k_x lines: total {nsc}, lines with >=1: {nlines}')
T.check('level 0 of T2 is 2-dimensional (f changes sign on a positive fraction of generic lines)', nlines > 100)
# T3: det constant
d3 = np.linalg.det(T3(Kr)); 
T.check(f'T3: det constant (spread {np.abs(d3 - d3[0]).max():.1e}) and T2 det = e^(2ikx) non-constant',
        np.abs(d3 - d3[0]).max() < 1e-12 and np.abs(np.linalg.det(T2(Kr)) - np.exp(2j * Kr[:, 0])).max() < 1e-12)
print('Implied sheet flux at level 0 (identity W3 = -sum chi + sum Phi, W3 = 0, sum chi = -4): sum Phi = -4 '
      '(equivalently sum of sheet-tube Ch(P_<) = +4).')
T.total()
