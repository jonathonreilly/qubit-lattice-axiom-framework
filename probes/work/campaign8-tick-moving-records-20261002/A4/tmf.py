r"""Mean-field (product-closure) long-wave diffusion coefficient for crowd-tilted moves.

D_eff = -sum_w (2 w.e - 1) dPhi_{x->y}/drho_w ,  Phi_{x->y} = E_prod[ n_x (1-n_y) q(n) ],
with x = 0, y = e (unit vector along axis 0). Instability of uniform density at long wavelength <=> D_eff < 0.

q(n) for
  model K  (continuous-time rates): q = exp(g S_y)                    (nu = 1)
  model T1 (tick, heat-bath over destinations incl. stay, conflicts by relative odds):
           q = p_x(y) * E_B[ p_x(y) / (p_x(y) + sum_c B_c p_c(y)) ],  B_c ~ Bernoulli(p_c(y)), c in N(y)\{x} recorded.
Monte Carlo over product configurations with common random numbers for each pinned site.
usage: python3 tmf.py D model rho g1,g2,... [M]
"""
import sys, itertools
import numpy as np

D = int(sys.argv[1]); model = sys.argv[2]; rho = float(sys.argv[3])
gs = [float(v) for v in sys.argv[4].split(",")]
M = int(sys.argv[5]) if len(sys.argv) > 5 else 40000

def add(a, b): return tuple(i + j for i, j in zip(a, b))
units = []
for ax in range(D):
    for s in (1, -1):
        u = [0] * D; u[ax] = s; units.append(tuple(u))
def nbrs(s): return [add(s, u) for u in units]
X = tuple([0] * D)
e = list(X); e[0] = 1; Y = tuple(e)

# patch = L1 ball of radius 4 around X
patch = [c for c in itertools.product(range(-4, 5), repeat=D) if sum(abs(v) for v in c) <= 4]
idx = {c: i for i, c in enumerate(patch)}

def make_q(g):
    eg = lambda k: np.exp(g * k)
    def q(n):
        o = lambda s: n[idx[s]]
        cnt = lambda sites: sum(o(s) for s in sites)
        SyX = cnt([s for s in nbrs(Y) if s != X])
        if model == "K":
            return eg(SyX)
        def choice(c, dest):
            Zc = eg(cnt(nbrs(c)))
            for v in nbrs(c):
                Zc = Zc + (1 - o(v)) * eg(cnt([s for s in nbrs(v) if s != c]))
            return eg(cnt([s for s in nbrs(dest) if s != c])) / Zc
        px = choice(X, Y)
        comps = [c for c in nbrs(Y) if c != X]
        pc = [o(c) * choice(c, Y) for c in comps]
        W = np.zeros_like(px)
        for pat in itertools.product((0, 1), repeat=len(comps)):
            prob = np.ones_like(px); tot = px.copy()
            for b, p_ in zip(pat, pc):
                prob = prob * (p_ if b else (1 - p_))
                if b: tot = tot + p_
            W = W + prob * px / tot
        return px * W
    return q

rng = np.random.default_rng(int(sys.argv[6]) if len(sys.argv) > 6 else 2026)
base = (rng.random((len(patch), M)) < rho).astype(float)
base[idx[X]] = 1.0; base[idx[Y]] = 0.0
for g in gs:
    q = make_q(g)
    q0 = q(base)
    Qbar = q0.mean()
    Ssum = np.zeros(M)
    contrib = []
    for w in patch:
        if w in (X, Y): continue
        n1 = base.copy(); n1[idx[w]] = 1.0
        n0 = base.copy(); n0[idx[w]] = 0.0
        dq = q(n1) - q(n0)
        if np.abs(dq).max() == 0: continue
        coef = 2 * w[0] - 1
        Ssum += coef * dq
        contrib.append((w, dq.mean()))
    S = Ssum.mean()
    dsamp = q0 - rho * (1 - rho) * Ssum
    Deff = dsamp.mean()
    se = dsamp.std() / np.sqrt(M)
    line = f"D={D} model={model} rho={rho} g={g}: Qbar={Qbar:.5f} Gamma=S/Qbar={S/Qbar:.4f} D_eff={Deff:.5f} +- {se:.5f}  D_eff/Qbar={Deff/Qbar:.4f}  n_influential={len(contrib)}"
    if model == "K":
        z = 2 * D
        A = (1 - rho + rho * np.exp(g)) ** (z - 1)
        gam = (np.exp(g) - 1) / (1 - rho + rho * np.exp(g))
        line += f"  | closed form D=A[1-gam(z+1)rho(1-rho)]={A*(1-gam*(z+1)*rho*(1-rho)):.5f}"
    print(line, flush=True)
