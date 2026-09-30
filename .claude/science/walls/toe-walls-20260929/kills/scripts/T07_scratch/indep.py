"""Independent re-implementation of the Bell-protocol ensemble master equation for T07 kill check.
Differences from the attacker's code: full 2304-dim two-walker Hamiltonian built by kron; wave by kron of
single-ring propagators; currents from explicit pair list of 4x4 Hamiltonian blocks (no np.roll); generator built
from a pair list with scipy.sparse coo; Metropolis noise built from the pair list.
"""
import numpy as np, scipy.sparse as sp, sys, json, time
from scipy.integrate import solve_ivp

L = 24
sz = np.diag([1.0, -1.0]); sy = np.array([[0, -1j], [1j, 0]]); I2 = np.eye(2)
# single ring, basis index = 2*x + c
H1 = np.zeros((2 * L, 2 * L), complex)
for x in range(L):
    y = (x + 1) % L
    for c in range(2):
        s = sz[c, c]
        H1[2 * x + c, 2 * y + c] += s / (2j)      # psi_x^dag (sz/2i) psi_{x+1}
        H1[2 * y + c, 2 * x + c] += np.conj(s / (2j))
assert np.allclose(H1, H1.conj().T)
E1, V1 = np.linalg.eigh(H1)
def U1(t): return (V1 * np.exp(-1j * E1 * t)) @ V1.conj().T
# two walkers: index = (2L)*iA + iB with iA = 2 xA + cA
H = np.kron(H1, np.eye(2 * L)) + np.kron(np.eye(2 * L), H1)
def rot(th):
    return np.cos(th / 2) * I2 - 1j * np.sin(th / 2) * sy
singlet = np.zeros(4, complex); singlet[1] = 1 / np.sqrt(2); singlet[2] = -1 / np.sqrt(2)  # (|up,dn> - |dn,up>)/sqrt2 , index cA*2+cB
def psi0(thA, thB, w=1.5, c=12):
    g = np.exp(-(np.arange(L) - c) ** 2 / (2 * w ** 2))
    coin = np.kron(rot(thA), rot(thB)) @ singlet           # coin tensor, index cA*2+cB
    out = np.zeros((L, L, 2, 2), complex)                   # xA, xB, cA, cB
    out[:] = g[:, None, None, None] * g[None, :, None, None] * coin.reshape(2, 2)[None, None]
    out = out.transpose(0, 2, 1, 3).reshape(-1)              # -> (xA,cA,xB,cB) flattened = 2L*iA + iB
    return out / np.linalg.norm(out)
def wave(p0, t):
    U = U1(t)
    return (U @ p0.reshape(2 * L, 2 * L) @ U.T).reshape(-1)
# config index n = xA*L + xB ; coin block indices
def block(xa, xb):
    return [ (2 * xa + ca) * (2 * L) + (2 * xb + cb) for ca in range(2) for cb in range(2)]
cfg_blocks = np.array([block(a, b) for a in range(L) for b in range(L)])   # (576,4)
pairs = []   # (src, dst)
for a in range(L):
    for b in range(L):
        n = a * L + b
        for (da, db) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            m = ((a + da) % L) * L + (b + db) % L
            pairs.append((n, m))
pairs = np.array(pairs); src, dst = pairs[:, 0], pairs[:, 1]
Hblk = np.array([H[np.ix_(cfg_blocks[d], cfg_blocks[s])] for s, d in pairs])   # (2304,4,4), H_{dst,src}
def Pof(psi):
    return (np.abs(psi[cfg_blocks]) ** 2).sum(1)       # (576,)
def gen(psi, gamma=0.0, cap=1e5):
    P = Pof(psi)
    ps = psi[cfg_blocks]                                # (576,4)
    J = 2 * np.imag(np.einsum('pi,pij,pj->p', ps[dst].conj(), Hblk, ps[src]))   # flow src->dst
    rate = np.where(P[src] > 1e-300, np.maximum(J, 0) / np.maximum(P[src], 1e-300), 0.0)
    rate = np.minimum(rate, cap)
    if gamma > 0:
        rate = rate + gamma * np.minimum(1.0, P[dst] / np.maximum(P[src], 1e-300))
    n = L * L
    W = sp.coo_matrix((rate, (dst, src)), shape=(n, n)).tocsc()
    out = np.asarray(W.sum(0)).ravel()
    return P, (W - sp.diags(out)).tocsc()
def evolve(p0, rho0, ts, gamma=0.0, rtol=1e-8, atol=1e-12):
    f = lambda t, y: gen(wave(p0, t), gamma)[1] @ y
    jac = lambda t, y: gen(wave(p0, t), gamma)[1]
    sol = solve_ivp(f, (0, ts[-1]), rho0, method='Radau', jac=jac, t_eval=ts, rtol=rtol, atol=atol)
    assert sol.success
    return sol.y.T
x = np.arange(L)
side = np.where(x >= 12, 1.0, -1.0)
sidecfg_A = np.repeat(side, L); sidecfg_B = np.tile(side, L)
SETS = [(0.0, np.pi / 4), (0.0, -np.pi / 4), (np.pi / 2, np.pi / 4), (np.pi / 2, -np.pi / 4)]
def gauss(w, c=12):
    g = np.exp(-(x - c) ** 2 / (2 * w ** 2)); return g / g.sum()
def starts(P0):
    ma = P0.reshape(L, L).sum(1); mb = P0.reshape(L, L).sum(0)
    s = {}
    s['0 eq'] = P0.copy()
    s['1 wide'] = np.outer(gauss(2 * 1.5 / np.sqrt(2)), gauss(2 * 1.5 / np.sqrt(2))).ravel()
    s['2 narrow'] = np.outer(gauss(0.4 * 1.5 / np.sqrt(2)), gauss(0.4 * 1.5 / np.sqrt(2))).ravel()
    s['3 shift2'] = np.outer(np.roll(ma, 2), np.roll(mb, 2)).ravel()
    pm = np.zeros(L * L); pm[12 * L + 12] = 1; s['5 point'] = pm
    sg = np.where(x >= 12, 1.0, -1.0); c6 = P0 * (1 + 0.5 * np.outer(sg, sg).ravel()); s['6 corr'] = c6 / c6.sum()
    for k in s: s[k] = s[k] / s[k].sum()
    return s
def kl(r, P):
    m = r > 1e-300
    return float((r[m] * np.log(r[m] / P[m])).sum())
def run(name, gamma=0.0, TE=8.0):
    p0s = {s: psi0(*s) for s in SETS}
    P0 = Pof(p0s[SETS[0]])
    rho0 = starts(P0)[name]
    res = {}
    for s in SETS:
        R = evolve(p0s[s], rho0, np.array([0.0, TE]), gamma)[-1]
        Pt = Pof(wave(p0s[s], TE))
        res[s] = dict(rho=R, P=Pt, D=kl(R, Pt), TV=0.5 * np.abs(R - Pt).sum())
    pB = {s: float((res[s]['rho'] * (sidecfg_B > 0)).sum()) for s in SETS}
    pA = {s: float((res[s]['rho'] * (sidecfg_A > 0)).sum()) for s in SETS}
    sAB = max(abs(pB[(0.0, tb)] - pB[(np.pi / 2, tb)]) for tb in (np.pi / 4, -np.pi / 4))
    sBA = max(abs(pA[(ta, np.pi / 4)] - pA[(ta, -np.pi / 4)]) for ta in (0.0, np.pi / 2))
    E = {s: float((res[s]['rho'] * sidecfg_A * sidecfg_B).sum()) for s in SETS}
    Ep = {s: float((res[s]['P'] * sidecfg_A * sidecfg_B).sum()) for s in SETS}
    chsh = lambda E: abs(E[SETS[0]] + E[SETS[1]] + E[SETS[2]] - E[SETS[3]])
    D0 = np.mean([kl(rho0, Pof(p0s[s])) for s in SETS])
    out = dict(name=name, gamma=gamma, D0=float(D0), D8=float(np.mean([res[s]['D'] for s in SETS])),
               TV8_by_setting=[res[s]['TV'] for s in SETS], S8=max(sAB, sBA), chsh_rec=chsh(E), chsh_psi=chsh(Ep))
    return out
if __name__ == '__main__':
    name = sys.argv[1]; gamma = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
    t0 = time.time(); o = run(name, gamma); o['time'] = time.time() - t0
    print(json.dumps(o))
