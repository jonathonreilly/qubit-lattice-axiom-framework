#!/usr/bin/env python3
"""Reviewer's numerical checks for C7, independent implementation.
Walk built from G(b) by SVD factorisation + Householder alignment (author: eigh + QR).
Matrix log by eigh of the Hermitian generator built from eigenphases of U (author: Schur).
[numerical] labels everything that is floating point.
"""
import sys, itertools
import numpy as np
import mpmath as mp

P = F = 0
def chk(name, ok):
    global P, F
    ok = bool(ok); P += ok; F += (not ok)
    print(("PASS " if ok else "FAIL ") + "[numerical] " + name, flush=True)

I2 = np.eye(2); s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]).astype(complex)
T1, T2 = np.kron(s1, I2), np.kron(s2, I2); SS = [np.kron(s3, x) for x in (s1, s2, s3)]

def Gm(b0, b1, b2):
    return np.array([[1 - 3*b0**2, -2*b0*b1, b1**2 - b0**2 - b0*b2, -3*b1*(b0 - b2)],
                     [-2*b0*b1, b0**2 - 2*b1**2, b1*(b0 - b2), b0*b2 - b1**2 + b2**2],
                     [b1**2 - b0**2 - b0*b2, b1*(b0 - b2), 2*b1**2 - b2**2, 2*b1*b2],
                     [-3*b1*(b0 - b2), b0*b2 - b1**2 + b2**2, 2*b1*b2, 3*b2**2]])
phi0 = np.array([1., 3, 3, 1]); w = np.array([0., 1, 2, 1])
def phi(k):
    c = np.cos(k); return np.array([1, c.sum(), c[0]*c[1]+c[0]*c[2]+c[1]*c[2], c.prod()])
def gv(b, k):
    c, s = np.cos(k), np.sin(k)
    return np.array([s[i]*(b[0] + b[1]*(c[(i+1)%3] + c[(i+2)%3]) + b[2]*c[(i+1)%3]*c[(i+2)%3]) for i in range(3)])

class Walk:
    def __init__(s, b):
        s.b = np.array(b); G = Gm(*b)
        Uu, sv, Vt = np.linalg.svd(G)            # G PSD: G = Uu diag(sv) Uu^T
        Fm = (np.sqrt(np.clip(sv[:3], 0, None))[:, None]*Uu[:, :3].T)   # 3x4, F^T F = G (rank<=3)
        e = Fm @ phi0                              # unit vector
        v = e - np.array([1., 0, 0]); 
        Hh = np.eye(3) - 2*np.outer(v, v)/(v @ v) if np.linalg.norm(v) > 1e-14 else np.eye(3)
        s.F = Hh @ Fm                              # F phi0 = e_f
        s.W = s.F[1:] @ w; s.s = b[0] + 2*b[1] + b[2]
        s.svmin = sv[3]
    def U(s, k, th=0.0, chi=0.0):
        """massive member; chi measured from W (chi=0: mass along W)."""
        f, h1, h2 = s.F @ phi(k); g = gv(s.b, k)
        U0 = f*np.eye(4) + 1j*(h1*T1 + h2*T2 + sum(g[i]*SS[i] for i in range(3)))
        ang = (np.arctan2(s.W[1], s.W[0]) if np.linalg.norm(s.W) > 1e-12 else 0.0) + chi
        hh = np.cos(ang)*T1 + np.sin(ang)*T2
        M = np.cos(th/2)*np.eye(4) + 1j*np.sin(th/2)*hh
        return M @ U0 @ M, hh

def Hlog(U, a):
    lam, V = np.linalg.eig(U)
    # U normal, nondegenerate pairs may be degenerate: re-orthonormalise via QR per eigenvalue cluster
    Q, _ = np.linalg.qr(V)
    D = Q.conj().T @ U @ Q                        # (near-)diagonal
    om = -np.angle(np.diag(D))
    return (Q @ np.diag(om) @ Q.conj().T)/a

co = [259200000000, -453744000000, 12644840000, 1185396800, -39225499]
ust = min(r.real for r in np.roots(co) if abs(r.imag) < 1e-10 and r.real > 0)
r5, r6, r15 = np.sqrt(5), np.sqrt(6), np.sqrt(15)
pts = {'bstar': (11/30, np.sqrt(ust), 3/20),
       'iso': ((r6 + 2*r15)/27, (5*r6 - 2*r15)/27, (2*r15 - 2*r6)/27),
       'gold': ((9*r5 - 5)/38, (5*r5 - 7)/19, (71 - 29*r5)/38)}
W_ = {n: Walk(b) for n, b in pts.items()}
TR = [np.array(K)*np.pi for K in itertools.product((0, 1), repeat=3)]
rng = np.random.default_rng(2026)
table = {'bstar': (2.308, 2.196, 2.198), 'iso': (1.911, 2.462, 2.715), 'gold': (np.pi, 2.665, 2.455)}
c0tab = {'bstar': 0.2644, 'iso': 0.3184, 'gold': 0.2956}
spd = {'bstar': 0.914, 'iso': 0.816, 'gold': 1.0}
for n, Wk in W_.items():
    ks = rng.uniform(-np.pi, np.pi, (200, 3))
    uerr = max(np.linalg.norm(Wk.U(k, 0.3, 0.4)[0] @ Wk.U(k, 0.3, 0.4)[0].conj().T - np.eye(4), 2) for k in ks)
    chk(f'{n}: own construction unitary (theta=0.3), err {uerr:.1e}; rank G <= 3 (4th sv {Wk.svmin:.1e})', uerr < 1e-12 and Wk.svmin < 1e-10)
    chk(f'{n}: |W| = s sqrt(1-s^2): {np.linalg.norm(Wk.W):.6f} vs {abs(Wk.s)*np.sqrt(max(0,1-Wk.s**2)):.6f}',
        abs(np.linalg.norm(Wk.W) - abs(Wk.s)*np.sqrt(max(0, 1-Wk.s**2))) < 1e-7)
    chk(f'{n}: limiting speed s = {Wk.s:.4f} (note: {spd[n]})', abs(Wk.s - spd[n]) < 6e-4)
    om = {K.tobytes(): np.arccos(np.clip((Wk.F @ phi(K))[0], -1, 1)) for K in TR}
    X, M_, R = om[np.array([np.pi, 0, 0]).tobytes()], om[np.array([np.pi, np.pi, 0]).tobytes()], om[np.array([np.pi]*3).tobytes()]
    print(f"   {n}: TRIM angles X,M,R = {X:.4f} {M_:.4f} {R:.4f}")
    chk(f'{n}: TRIM table X,M,R matches note to 1e-3', np.allclose([X, M_, R], table[n], atol=1.5e-3))
    fK = [(Wk.F @ phi(K))[0] for K in TR]
    c0 = min((1 - fK[i])/(2*np.count_nonzero(TR[i])) for i in range(1, 8))
    chk(f'{n}: c0 = {c0:.4f} (note {c0tab[n]})', abs(c0 - c0tab[n]) < 6e-4)
    # Lemma V numerically: dense grid, max/min of f equal the TRIM max/min; f<1 off a ball around Gamma
    tg = np.linspace(-np.pi, np.pi, 33)
    KK = np.stack(np.meshgrid(tg, tg, tg, indexing='ij'), -1).reshape(-1, 3)
    C = np.cos(KK)
    PH = np.stack([np.ones(len(C)), C.sum(1), C[:,0]*C[:,1]+C[:,0]*C[:,2]+C[:,1]*C[:,2], C.prod(1)], 1)
    fg = PH @ Wk.F[0]
    chk(f'{n}: grid max f = TRIM max, grid min f >= TRIM min', fg.max() <= max(fK) + 1e-12 and fg.min() >= min(fK) - 1e-12)
    far = np.max(np.abs(KK), 1) >= np.pi/2
    chk(f'{n}: off-Gamma gap: |k_a| >= pi/2 => omega >= arccos(1 - c0) ({np.arccos(fg[far].max()):.4f} >= {np.arccos(1-c0):.4f})',
        np.arccos(np.clip(fg[far].max(), -1, 1)) >= np.arccos(1 - c0) - 1e-12)

# ---- O(a) coefficient: Richardson extraction of (H_a - H_D)/a at fixed p, both twists, sign check
m = 1.0
for n in ('bstar', 'iso'):
    Wk = W_[n]
    for chi in (0.0, np.pi/2, 1.0):
        errs = []
        for p in rng.normal(size=(6, 3)):
            vals = []
            for a in (2e-3, 1e-3):
                U, hh = Wk.U(a*p, m*a, chi)
                HD = -Wk.s*sum(p[i]*SS[i] for i in range(3)) - m*hh
                vals.append((Hlog(U, a) - HD)/a)
            lead = 2*vals[1] - vals[0]                     # removes O(a) of (H-HD)/a
            pred = 0.5*(p @ p)*(Wk.W[0]*T1 + Wk.W[1]*T2)
            errs.append(np.linalg.norm(lead - pred, 2)/np.linalg.norm(pred, 2))
        chk(f'{n} chi={chi:.2f}: Richardson O(a) coefficient of H_a equals +(1/2)|p|^2 W.tau (rel err {max(errs):.1e})', max(errs) < 1e-3)

# ---- twist dichotomy, spectral lower bound (any unitary identification): eigenphase matching distance
t = 1.0
for n in ('iso',):
    Wk = W_[n]
    for chi, exp in ((0.0, 1), (np.pi/2, 2)):
        ds = []
        for a in (0.02, 0.01, 0.005):
            nn = int(round(t/a)); d = 0
            for p in (np.array([1.0, 0.5, 0.2]), np.array([0.0, 1.5, 1.0])):
                U, hh = Wk.U(a*p, m*a, chi)
                E = np.sqrt(m**2 + Wk.s**2*(p @ p))
                ph = np.sort(np.angle(np.linalg.eigvals(np.linalg.matrix_power(U, nn))))
                ref = np.sort(np.angle(np.exp(-1j*t*np.array([E, E, -E, -E]))))
                d = max(d, np.max(np.abs(np.exp(1j*ph) - np.exp(1j*ref))))
            ds.append(d)
        sl = np.polyfit(np.log([0.02, 0.01, 0.005]), np.log(ds), 1)[0]
        chk(f'{n} chi={chi:.2f}: spectral distance of U^n vs exp(-itH_D) scales as a^{exp} (slope {sl:.2f}) -> lower bound for every unitary identification',
            abs(sl - exp) < 0.15)

# ---- gold: U_theta(X) = -U_theta(0)
Wk = W_['gold']
d = max(np.linalg.norm(Wk.U(np.array([np.pi, 0, 0]), th, chi)[0] + Wk.U(np.zeros(3), th, chi)[0], 2) for th in (0.1, 0.4) for chi in (0, 1.0))
chk(f'gold: U_theta(X) = -U_theta(0) (err {d:.1e})', d < 1e-12)

# ---- Lorentz: beta (cubic anisotropy) and quartic axis/diag coefficients from massless omega^2 fits
for n, (bt, ax, dg) in {'bstar': (0.0403, -0.0114, -0.0383), 'iso': (0.0, -0.0185, -0.0185), 'gold': (0.0486, 0.0, -0.0324)}.items():
    Wk = W_[n]
    def c4(nd):
        nd = np.array(nd)/np.linalg.norm(nd); cs = []
        for kk in (0.04, 0.02, 0.01):
            om = np.arccos(np.clip((Wk.F @ phi(kk*nd))[0], -1, 1))
            cs.append((om**2 - Wk.s**2*kk**2)/kk**4)
        return (4*cs[2] - cs[1])/3  # Richardson in k^2
    A, D = c4([1, 0, 0]), c4([1, 1, 1])
    beta_fit = (A - D)*3/2           # axis: alpha+beta, diag: alpha+beta/3
    print(f"   {n}: quartic axis {A:.5f}, diag {D:.5f}, beta {beta_fit:.5f}")
    chk(f'{n}: beta = {beta_fit:.4f} (note {bt}), axis {A:.4f} (note {ax}), diag {D:.4f} (note {dg})',
        abs(beta_fit - bt) < 6e-4 and abs(A - ax) < 6e-4 and abs(D - dg) < 6e-4)

# massive dispersion O(a^2) m^2 p^2 term: fit omega^2 - [theta^2 + s^2 k^2 - theta|W|cos chi k^2 + alpha k^4 + beta sum k^4] / (theta^2 k^2)
Wk = W_['bstar']; b0, b1, b2 = Wk.b; s = Wk.s
al = s*(s**3 + 3*b0 - 6*b1 - 9*b2)/12; be = -s*(b0 - b1 - 2*b2)/3
mp_res = []
for e_ in (0.02, 0.01):
    nd = np.array([0.3, -0.5, 0.81]); nd /= np.linalg.norm(nd); mu = 0.7; chi = 1.0
    U, _ = Wk.U(e_*nd, e_*mu, chi)
    om = np.max(np.abs(np.angle(np.linalg.eigvals(U))))
    rest = om**2 - (mu**2*e_**2 + s**2*e_**2 - mu*np.linalg.norm(Wk.W)*np.cos(chi)*e_**3 + (al + be*np.sum(nd**4))*e_**4)
    mp_res.append(rest/e_**4)
coef = 2*mp_res[1] - mp_res[0]
chk(f'bstar: theta^2 k^2 coefficient of omega^2 = -(s^2/3) ({coef/mu**2:.4f} vs {-s**2/3:.4f})', abs(coef/mu**2 + s**2/3) < 2e-3)

# ---- parent sextic at b_iso, 80 digits, by polynomial fit in k^2 (no subtraction of assumed lower terms)
mp.mp.dps = 80
b = [(mp.sqrt(6) + 2*mp.sqrt(15))/27, (5*mp.sqrt(6) - 2*mp.sqrt(15))/27, (2*mp.sqrt(15) - 2*mp.sqrt(6))/27]
Gi = mp.matrix(Gm(*[0, 0, 0]).tolist())
b0, b1, b2 = b
Gi = mp.matrix([[1 - 3*b0**2, -2*b0*b1, b1**2 - b0**2 - b0*b2, -3*b1*(b0 - b2)],
                [-2*b0*b1, b0**2 - 2*b1**2, b1*(b0 - b2), b0*b2 - b1**2 + b2**2],
                [b1**2 - b0**2 - b0*b2, b1*(b0 - b2), 2*b1**2 - b2**2, 2*b1*b2],
                [-3*b1*(b0 - b2), b0*b2 - b1**2 + b2**2, 2*b1*b2, 3*b2**2]])
av = Gi*mp.matrix([1, 3, 3, 1])
def om2(kv):
    c = [mp.cos(x) for x in kv]
    ph = [1, sum(c), c[0]*c[1] + c[0]*c[2] + c[1]*c[2], c[0]*c[1]*c[2]]
    return mp.acos(sum(av[i]*ph[i] for i in range(4)))**2
z = mp.sqrt(10)/9 - mp.mpf(16)/45
for nd in ((1, 0, 0), (1, 1, 1), (1, 1, 0)):
    nv = [mp.mpf(x)/mp.sqrt(sum(y*y for y in nd)) for x in nd]
    N4 = sum(x**4 for x in nv); P222 = nv[0]**2*nv[1]**2*nv[2]**2
    ks = [mp.mpf(j)/1000 for j in range(1, 7)]
    A = mp.matrix([[kk**(2*j) for j in range(1, 7)] for kk in ks])
    rhs = mp.matrix([om2([kk*x for x in nv]) for kk in ks])
    cf = mp.lu_solve(A, rhs)
    corr = mp.mpf(1)/1215 - N4/540 + z*P222; par = mp.mpf(1)/243 - N4/540 + z*P222
    print(f"   dir {nd}: k^2 {mp.nstr(cf[0],12)}, k^4 {mp.nstr(cf[1],12)}, k^6 {mp.nstr(cf[2],15)}; corrected {mp.nstr(corr,15)}, parent {mp.nstr(par,15)}")
    chk(f'b_iso dir {nd}: fitted k^6 coefficient = corrected (|k|^6 coeff 1/1215), not parent (1/243)',
        abs(cf[2] - corr) < mp.mpf('1e-20') and abs(cf[2] - par) > mp.mpf('1e-3')
        and abs(cf[0] - mp.mpf(2)/3) < mp.mpf('1e-30') and abs(cf[1] + mp.mpf(1)/54) < mp.mpf('1e-25'))

print(f"TOTAL: PASS={P} FAIL={F}")
sys.exit(1 if F else 0)
