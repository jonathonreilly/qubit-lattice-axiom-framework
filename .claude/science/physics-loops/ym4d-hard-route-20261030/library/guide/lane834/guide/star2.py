# GUIDE only (not a proof): structured scans of the decimated price and of tau proxies.
import numpy as np, sys, time
from scipy.special import ive
from scipy.optimize import minimize
beta = float(sys.argv[1]); rng = np.random.default_rng(7)
ne, nx = 20, 28
ge, we = np.polynomial.legendre.leggauss(ne)
eta = (ge + 1) * np.pi / 4; we = we * np.pi / 4 * np.sin(eta) * np.cos(eta)
xs = 2 * np.pi * np.arange(nx) / nx
E, X1, X2 = np.meshgrid(eta, xs, xs, indexing='ij')
W = (we[:, None, None] * np.ones_like(X1)).ravel(); W /= W.sum()
H = np.stack([np.cos(E)*np.cos(X1), np.cos(E)*np.sin(X1), np.sin(E)*np.cos(X2), np.sin(E)*np.sin(X2)], -1).reshape(-1, 4)
def logz(r):
    out = np.empty_like(r); s = r < 1e-4; out[s] = r[s]**2/8; rr = r[~s]
    out[~s] = np.log(2*ive(1, rr)/rr) + rr; return out
def afun(k):
    out = np.empty_like(k); s = k < 1e-4; out[s] = 0.25 - k[s]**2/96; kk = k[~s]
    out[~s] = ive(2, kk)/(kk*ive(1, kk)); return out
def law(F0, Gs):
    lw = H @ F0
    for G in Gs: lw = lw + logz(np.linalg.norm(beta*H + G, axis=1))
    w = W*np.exp(lw - lw.max()); return w/w.sum()
def cov(w, A, B): return (A*w[:, None]).T @ B - np.outer(w @ A, w @ B)
def Lval(F0, Gs):
    w = law(F0, Gs); F = beta*H + Gs[0]; g = afun(np.linalg.norm(F, axis=1))[:, None]*F
    return np.linalg.svd(cov(w, H, g), compute_uv=False)[0]
def tau(F0, Gs): return np.linalg.eigvalsh(cov(law(F0, Gs), H, H))[-1]
z4 = np.zeros(4); e = np.eye(4)
t = afun(np.array([beta]))[0]*beta
t0 = time.time(); v0 = Lval(z4, [z4]*6); dt = time.time() - t0
print(f"beta={beta} t/4={t/4:.5f} beta/16={beta/16:.5f} L(0)={v0:.5f} eval {dt*1e3:.1f} ms", flush=True)
print("(a) perturbed leaf field G1=g e1 (or g e2), others 0:", flush=True)
for g in [0.5, 1, 2, 3, 5*beta]:
    print(f"   g={g:.2f}: L={Lval(z4, [g*e[0]] + [z4]*5):.5f}", flush=True)
print("(b) other leaves in opposite pairs +-g u, G1 = 0:", flush=True)
for g in [0.5, 1, 2, 3, 5*beta]:
    Gs1 = [z4, g*e[0], -g*e[0], g*e[1], -g*e[1], z4]
    Gs2 = [z4, g*e[1], -g*e[1], g*e[2], -g*e[2], g*e[3]]
    print(f"   g={g:.2f}: L(pairs along e1,e2)={Lval(z4, Gs1):.5f}  L(pairs e2,e3 + e4)={Lval(z4, Gs2):.5f}", flush=True)
print("(c) tau proxy (top eig of Cov) for S_5 laws, F=0:", flush=True)
for g in [0.5, 1, 2, 3, 5*beta]:
    pa = [g*e[0], -g*e[0], g*e[1], -g*e[1], z4]
    pb = [g*e[0], -g*e[0], z4, z4, z4]
    pc = [g*e[0], g*e[1], g*e[2], g*e[3], -g*e[0]]
    print(f"   g={g:.2f}: tau(pairs e1,e2)={tau(z4, pa):.5f} tau(pair e1)={tau(z4, pb):.5f} tau(mixed)={tau(z4, pc):.5f}", flush=True)
def search(fun, n, f0, trials, fev):
    best = 0
    for _ in range(trials):
        p0 = rng.normal(size=4*n + 4)*rng.uniform(0.1, 1.5)*beta
        def unpack(p):
            Gs = []
            for i in range(n):
                v = p[4*i:4*i+4]; r = np.linalg.norm(v); Gs.append(v if r <= 5*beta else v*5*beta/r)
            F0 = p[4*n:] if f0 else z4
            r = np.linalg.norm(F0); F0 = F0 if r <= 6*beta else F0*6*beta/r
            return F0, Gs
        res = minimize(lambda p: -fun(*unpack(p)), p0, method='Powell', options={'maxfev': fev, 'xtol': 1e-3, 'ftol': 1e-7})
        best = max(best, -res.fun)
    return best
t0 = time.time()
print(f"(d) local search max L, n=6, F0=0: {search(Lval, 6, False, 3, 500):.5f}", flush=True)
print(f"    local search max L, n=6, F0 free: {search(Lval, 6, True, 3, 500):.5f}", flush=True)
print(f"    local search max tau, S_5, F0 free: {search(tau, 5, True, 3, 500):.5f}", flush=True)
print(f"    search time {time.time()-t0:.0f} s", flush=True)
