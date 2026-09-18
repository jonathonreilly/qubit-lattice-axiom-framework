"""Refuting pass, block 27 (independent machinery): (a) two runs from antipodal planes coupled site by site with the maximal
(overlap) coupling of K_{beta S} and K_{beta S'} built by rejection from the densities; the per-site mean chordal distance D_t and its
ratio per level against sqrt3 beta; (b) the total-variation sensitivity estimated by Monte Carlo (E[(1 - f'/f)^+]) at random pairs
against the bound 1/(2 sqrt3); (c) the one-site chain against A(3 beta)^t; (d) the mean-difference lower bound against 2 TV near V = 0."""
import numpy as np, sys
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 23)   # probes: seed override
def A(x): return 1/np.tanh(x) - 1/x
def logf(V, s):   # log density of K_V w.r.t. the surface measure
    n = np.linalg.norm(V, axis=-1)
    ln = np.where(n > 1e-12, np.log(np.maximum(n, 1e-300)) - np.log(np.sinh(np.maximum(n, 1e-12))), np.log(1.0)) - np.log(4*np.pi)
    return ln + (V * s).sum(-1)
def sample(V, rng):   # exact vMF sample(s) for an array of V's (shape (..., 3))
    n = np.linalg.norm(V, axis=-1); kap = np.maximum(n, 1e-12); u = V / kap[..., None]
    U = rng.random(n.shape); w = np.where(n > 1e-12, 1 + np.log(U + (1-U)*np.exp(-2*kap))/kap, 2*U - 1); w = np.clip(w, -1, 1)
    ph = 2*np.pi*rng.random(n.shape)
    a = np.where((np.abs(u[..., 0]) < 0.9)[..., None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    e1 = a - (a*u).sum(-1)[..., None]*u; e1 /= np.linalg.norm(e1, axis=-1)[..., None]; e2 = np.cross(u, e1)
    r = np.sqrt(np.clip(1 - w*w, 0, 1))
    s = w[..., None]*u + r[..., None]*(np.cos(ph)[..., None]*e1 + np.sin(ph)[..., None]*e2)
    # for |V| = 0 the frame above degenerates: draw uniform points on the sphere directly
    zero = n <= 1e-12
    if zero.any():
        g = rng.normal(size=s[zero].shape); s[zero] = g / np.linalg.norm(g, axis=-1)[..., None]
    return s
def maximal_coupling(V, Vp, rng):
    """Vectorised gamma-coupling: s ~ K_V; accept as common with prob min(1, f'/f); else s' ~ residual of K_V' by rejection."""
    s = sample(V, rng)
    acc = rng.random(V.shape[:-1]) < np.exp(np.minimum(0.0, logf(Vp, s) - logf(V, s)))
    sp = s.copy()
    todo = ~acc
    it = 0
    while todo.any() and it < 200:
        cand = sample(Vp[todo], rng)
        keep = rng.random(cand.shape[:-1]) >= np.exp(np.minimum(0.0, logf(V[todo], cand) - logf(Vp[todo], cand)))
        idx = np.flatnonzero(todo.ravel())
        sel = idx[keep]
        sp.reshape(-1, 3)[sel] = cand[keep]
        todo.ravel()[sel] = False
        it += 1
    return s, sp, todo.sum()
print("(a) coupled runs from antipodal planes, maximal coupling per site, L = 64")
for beta in (0.3, 0.5, 0.577):
    L = 64; s = np.zeros((L, L, 3)); s[..., 2] = 1; sp = -s.copy(); Ds = []
    for t in range(1, 21):
        S = s + np.roll(s, 1, 0) + np.roll(s, 1, 1); Sp = sp + np.roll(sp, 1, 0) + np.roll(sp, 1, 1)
        s, sp, left = maximal_coupling(beta*S, beta*Sp, rng)
        Ds.append(np.linalg.norm(s - sp, axis=-1).mean())
    ratios = [Ds[i+1]/Ds[i] for i in range(len(Ds)-1) if Ds[i] > 1e-6]
    print(f"  beta={beta}: D_t = {[round(d, 4) for d in Ds[:8]]}; ratios D_(t+1)/D_t (first 6) = {[round(r, 3) for r in ratios[:6]]}; sqrt3 beta = {np.sqrt(3)*beta:.3f}; unresolved sites at the end: {left}")
print("(b) Monte-Carlo total-variation sensitivity at 40 random pairs (10^5 samples each)")
worst = 0
for trial in range(40):
    V = rng.normal(size=3)*rng.choice([0.05, 0.3, 1, 3]); Vp = V + rng.normal(size=3)*rng.choice([0.05, 0.3, 1])
    Vs = np.broadcast_to(V, (100000, 3)).copy(); ss = sample(Vs, rng)
    tv = np.maximum(0, 1 - np.exp(logf(Vp, ss) - logf(V, ss))).mean()
    worst = max(worst, tv/np.linalg.norm(V - Vp))
print(f"  max TV/|V - V'| = {worst:.4f} against the bound {1/(2*np.sqrt(3)):.4f} (small-|V| value 0.25)")
print("(c) one-site chain at beta = 0.5, 20000 independent chains, 6 levels")
n = 20000; beta = 0.5; s = np.zeros((n, 3)); s[:, 2] = 1
for t in range(1, 7):
    s = sample(3*beta*s, rng); print(f"  t={t}: mean s.e = {s[:, 2].mean():.4f}  A(3 beta)^t = {A(3*beta)**t:.4f}")
print("(d) near V = 0: |F(V') - F(V)| against 2 TV, per unit |V' - V|")
for d in (0.05, 0.2, 0.5):
    V = np.zeros(3); Vp = np.array([0, 0, d]); Vs = np.broadcast_to(V, (200000, 3)).copy(); ss = sample(Vs, rng)
    tv = np.maximum(0, 1 - np.exp(logf(Vp, ss) - logf(V, ss))).mean()
    print(f"  |V'| = {d}: mean difference/|V'| = {A(d)/d:.4f} (>= 1/3 - d^2/45 = {1/3 - d*d/45:.4f}); 2 TV/|V'| = {2*tv/d:.4f}")
