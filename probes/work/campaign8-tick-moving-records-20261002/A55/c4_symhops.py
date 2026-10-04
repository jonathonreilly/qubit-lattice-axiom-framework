"""A55 c4: which quadratic charge terms (on-site + hops up to range^2 R2, coarse units) are allowed by the pi-flux
law's symmetries, and can any of them gap the Kawamoto-Smit nodes at half filling?
Free-fermion level: KS gauge u_x=1, u_y=(-1)^x1, u_z=(-1)^(x1+x2) (period 2); each space-group element g=(R,a)
acts as S_g = G_g P_g (permutation + compensating gauge, found by BFS on an 8^3 torus).
Groups: FULL = all 24 corner turns x Z^3 (P432; contains cube-centre turns); C3T = C3 about (111) at every corner
x Z^3 (uniform record background f0); CYC = stabiliser of the cyclic texture (control: must admit eps on-site).
Templates: 2-periodic h[x, x+d] = w[x mod 2, d]; group average in template space; Hermitian; TR = real."""
import signal, sys, itertools
signal.alarm(105)
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, '/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A52')
from a52lib import ROT

R2 = int(sys.argv[1]) if len(sys.argv) > 1 else 3
L = 8
X = np.array(list(itertools.product(range(L), repeat=3)))
N = len(X)
idx = lambda x: ((x[..., 0] % L) * L + (x[..., 1] % L)) * L + (x[..., 2] % L)
def u(x, axis):
    return 1 if axis == 0 else (1 - 2 * (int(x[0]) % 2) if axis == 1 else 1 - 2 * (int(x[0] + x[1]) % 2))
H0 = np.zeros((N, N))
for i, x in enumerate(X):
    for axis in range(3):
        e = np.zeros(3, int); e[axis] = 1
        j = idx(x + e); H0[i, j] = -u(x, axis); H0[j, i] = -u(x, axis)
NBR = [np.nonzero(H0[i])[0] for i in range(N)]

def gauge_for(R, a):
    perm = idx((X @ R.T + a) % L)
    Hp = np.zeros_like(H0); Hp[np.ix_(perm, perm)] = H0
    G = np.zeros(N); G[0] = 1; stack = [0]
    while stack:
        i = stack.pop()
        for j in NBR[i]:
            if G[j] == 0:
                G[j] = H0[i, j] / (G[i] * Hp[i, j]); stack.append(j)
    res = np.abs(G[:, None] * Hp * G[None, :] - H0).max()
    for e in np.eye(3, dtype=int):                     # 2-periodicity of G up to a uniform sign
        r = G[idx(X + 2 * e)] * G
        res = max(res, np.abs(r - r[0]).max())
    return G, res

CL = list(itertools.product([0, 1], repeat=3)); CI = {c: i for i, c in enumerate(CL)}
OFF = [d for d in itertools.product(range(-3, 4), repeat=3) if sum(c * c for c in d) <= R2]
OI = {d: i for i, d in enumerate(OFF)}
nO = len(OFF); T = 8 * nO
def tix(c, d):
    return CI[tuple(int(v) % 2 for v in c)] * nO + OI[tuple(int(v) for v in d)]

C3s = [g for g, R in enumerate(ROT) if tuple(R @ np.array([1, 1, 1])) == (1, 1, 1)]
def cyc_stab():
    out = []
    F = lambda x: 1 - 2 * (np.array([x[1], x[2], x[0]]) % 2)
    for g, R in enumerate(ROT):
        for a in CL:
            if all(np.array_equal(F(R @ np.array(c) + np.array(a)), R @ F(np.array(c))) for c in CL):
                out.append((g, a))
    return out
GROUPS = {'TRANS': [(ROT.index(next(R for R in ROT if np.array_equal(R, np.eye(3)))) if False else [g for g, R in enumerate(ROT) if np.array_equal(R, np.eye(3, dtype=int))][0], a) for a in CL], 'FULL': [(g, a) for g in range(24) for a in CL], 'C3T': [(g, a) for g in C3s for a in CL], 'CYC': cyc_stab()}

def template_map(R, a, G):
    M = np.zeros((T, T))
    for ci_, c in enumerate(CL):
        p = R @ np.array(c) + np.array(a)
        for d in OFF:
            q = p + R @ np.array(d)
            M[tix(p, R @ np.array(d)), ci_ * nO + OI[d]] += G[idx(p)] * G[idx(q)]
    return M
Hm = np.zeros((2 * T, 2 * T))            # real form (re, im) of w -> w^dagger template
for ci_, c in enumerate(CL):
    for d in OFF:
        t = ci_ * nO + OI[d]; s = tix(np.array(c) + np.array(d), -np.array(d))
        Hm[t, s] = 1; Hm[T + t, T + s] = -1

CIa = np.repeat(np.arange(8), nO)
DA = np.array([OFF[t % nO] for t in range(T)])
CJa = np.array([CI[tuple((np.array(CL[t // nO]) + DA[t]) % 2)] for t in range(T)])
AMAP = np.zeros((T, 64)); AMAP[np.arange(T), CIa * 8 + CJa] = 1
def bloch(wr, wi, ks):
    w = wr + 1j * wi
    ph = np.exp(1j * (ks @ DA.T)) * w[None, :]
    return (ph @ AMAP).reshape(len(ks), 8, 8)
w0 = np.zeros(T)
for ci_, c in enumerate(CL):
    for axis in range(3):
        for s in [1, -1]:
            d = [0, 0, 0]; d[axis] = s
            x = np.array(c) if s == 1 else np.array(c) + np.array(d)
            w0[ci_ * nO + OI[tuple(d)]] = -u(x % 2, axis)
g1 = np.linspace(-np.pi / 2, np.pi / 2, 17)
KG = np.array(list(itertools.product(g1, repeat=3)))
def gaps(wr, wi):
    E = np.linalg.eigvalsh(bloch(wr, wi, KG))
    return (E[:, 4] - E[:, 3]).min(), E[:, 4].min() - E[:, 3].max(), KG[np.argmin(E[:, 4] - E[:, 3])]
def refine(wr, wi, k0):
    f = lambda k: (lambda E: E[4] - E[3])(np.linalg.eigvalsh(bloch(wr, wi, k[None, :])[0]))
    r = minimize(f, k0, method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-13, 'maxiter': 4000})
    return r.fun
eps_t = np.zeros(T)
for ci_, c in enumerate(CL):
    eps_t[ci_ * nO + OI[(0, 0, 0)]] = 1 - 2 * (sum(c) % 2)
print("R2 <= %d: %d offsets, template dim %d (complex)" % (R2, nO, T))
print("H0 bloch check: |E| = 2 sqrt(sum cos^2) max dev %.1e" % np.abs(np.sort(np.abs(np.linalg.eigvalsh(bloch(w0, 0 * w0, KG))), axis=1)
      - np.sort(np.repeat(2 * np.sqrt((np.cos(KG) ** 2).sum(1))[:, None], 8, 1), axis=1)).max())
rng = np.random.default_rng(4)
for name, els in GROUPS.items():
    P = np.zeros((T, T)); worst = 0
    for (g, a) in els:
        G, res = gauge_for(ROT[g], np.array(a)); worst = max(worst, res)
        P += template_map(ROT[g], np.array(a), G)
    P /= len(els)
    Q = np.kron(np.eye(2), P) @ (np.eye(2 * T) + Hm) / 2
    ev, V = np.linalg.eigh((Q + Q.T) / 2)
    B = V[:, ev > 0.5]
    D = B.shape[1]
    # TR-even (real) vs TR-odd (imaginary) parts
    Dre = np.linalg.matrix_rank(B[:T], 1e-8); Dim = np.linalg.matrix_rank(B[T:], 1e-8)
    in0 = np.linalg.norm(B @ (B.T @ np.concatenate([w0, 0 * w0])) - np.concatenate([w0, 0 * w0]))
    ine = np.linalg.norm(B @ (B.T @ np.concatenate([eps_t, 0 * eps_t])) - np.concatenate([eps_t, 0 * eps_t]))
    print("%s: |G|=%d, gauge residual %.1e, symmetric Hermitian terms D=%d (real part rank %d, imaginary part rank %d); "
          "KS hop in span: %.1e; eps on-site in span: %.1e (0 = allowed)" % (name, len(els), worst, D, Dre, Dim, in0, ine))
    # first-order mass content at the 8-fold node k0 = (pi/2)^3: H0(k0) = 0, alpha_i = dH0/dk_i;
    # Pi(M) = projection onto matrices anticommuting with all three alpha_i
    k0 = np.array([[np.pi / 2] * 3]); hk0 = bloch(w0, 0 * w0, k0)[0]
    al = []
    for i in range(3):
        dk = np.zeros((1, 3)); dk[0, i] = 1e-6
        al.append(((bloch(w0, 0 * w0, k0 + dk)[0] - bloch(w0, 0 * w0, k0 - dk)[0]) / 2e-6))
    def Pi(M):
        for A in al:
            M = (M - A @ M @ np.linalg.inv(A)) / 2
        return M
    mc = [np.linalg.norm(Pi(bloch(B[:T, j], B[T:, j], k0)[0])) for j in range(D)]
    if name == 'TRANS':
        print("   node check: |H0(k0)| = %.1e; alpha anticommutators max %.1e; alpha_i^2 = %s" % (np.abs(hk0).max(),
              max(np.abs(al[i] @ al[j] + al[j] @ al[i]).max() for i in range(3) for j in range(i)), [round(float(np.abs(A @ A).max()), 3) for A in al]))
    print("   first-order Dirac-mass content of the %d symmetric terms at the node: max %.1e" % (D, max(mc)))
    if len(sys.argv) > 2:
        continue
    best = (0, None)
    for trial in range(60 if name != 'CYC' else 20):
        c = rng.normal(size=D); c /= np.linalg.norm(c)
        wv = B @ c * (0.6 if trial % 2 == 0 else 2.5)
        wr = w0 + wv[:T]; wi = wv[T:]
        dg, ig, k0 = gaps(wr, wi)
        if dg > best[0] - 1e-12:
            best = (dg, (wr, wi, k0, ig))
    dg, (wr, wi, k0, ig) = best
    fine = refine(wr, wi, k0)
    print("   60 random symmetric additions (norms 0.6 and 2.5): best grid direct gap %.4f -> refined local min %.2e; indirect gap %.4f" % (dg, fine, ig))
    # pure-TR-odd and pure-TR-even subspaces separately
    for lab, sel in [('TR-even only', slice(0, T)), ('TR-odd only', slice(T, 2 * T))]:
        Bs = np.zeros_like(B); Bs[sel] = B[sel]
        U_, S_, _ = np.linalg.svd(Bs, full_matrices=False); Bs = U_[:, S_ > 1e-8]
        if Bs.shape[1] == 0:
            print("   %s: none" % lab); continue
        bb = (0, None)
        for trial in range(30):
            c = rng.normal(size=Bs.shape[1]); c /= np.linalg.norm(c)
            wv = Bs @ c * 0.6
            out = gaps(w0 + wv[:T], wv[T:])
            if out[0] > bb[0] - 1e-12:
                bb = (out[0], (w0 + wv[:T], wv[T:], out[2]))
        print("   %s (%d terms): best grid direct gap %.4f -> refined %.2e" % (lab, Bs.shape[1], bb[0], refine(*bb[1])))
print("done")
