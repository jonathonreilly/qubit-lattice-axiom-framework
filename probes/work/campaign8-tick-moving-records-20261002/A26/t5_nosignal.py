"""A26 t5_nosignal: does the fixed field coupling signal?  (supplied toy, A21 r2 pattern)
Qubits: b (distant), f (field site: its possibility |0>/|1> = field value U=0,h_xy=0 / U=U1,h_xy=H1),
m00, m01, m10, m11 (a 2x2 matter cell; qubit = occupation).  6 qubits, 64-dim.
FIXED coupling (CTRL): W = |0><0|_f (x) S(0) + |1><1|_f (x) S(1), where S(n) is the matter step with
  one-site phases mu*N(n)*eps/2 (before/after), hop gates exp(-i th0 N(n) e(n) (XX+YY)/2) on the 4 in-cell bonds
  (KS sign on y-bonds), and the frame sandwich R(beta(n)) = S P(beta(n)) S^dag on the x-bonds (shear).
  The field's possibilities enter coherently through a fixed unitary.
DIAL (contrast, A15-type): the same step but with N, e, beta computed from the branch state's <n_f> (nonlinear).
Then: formation instrument at m00 (Kraus sqrt(F)P_k sqrt(F), k=0,1, and 'none' sqrt(1-F)), record read at m11 (Z).
Report: max total-variation distance of local record odds between distant conditions at b (none / Z / X)."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(58)
import numpy as np
from scipy.linalg import expm

n = 6
I2 = np.eye(2); X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1.0, -1.0])
P = [np.diag([1.0, 0.0]), np.diag([0.0, 1.0])]
Hd = np.array([[1, 1], [1, -1]]) / np.sqrt(2); PX = [Hd @ p @ Hd for p in P]


def on(ops):
    out = np.array([[1.0 + 0j]])
    for k in range(n):
        out = np.kron(out, ops.get(k, I2))
    return out


B, F, M00, M01, M10, M11 = range(6)
nf = on({F: P[1]})
nocc = {s: on({s: P[1]}) for s in (M00, M01, M10, M11)}
def hop(a, b, sign=1.0):              # (XX+YY)/2 on matter sites a, b: one-excitation hop, number conserving
    return sign * 0.5 * (on({a: X, b: X}) + on({a: Y, b: Y}))
def hopim(a, b, sign=1.0):            # imaginary-amplitude hop (XY - YX)/2
    return sign * 0.5 * (on({a: X, b: Y}) - on({a: Y, b: X}))
# 2x2 cell: x-bonds (m00-m10), (m01-m11); y-bonds (m00-m01), (m10-m11) with KS sign (-1)^x
Gx = hop(M00, M10) + hop(M01, M11)
Gy = hop(M00, M01) + hop(M10, M11, -1.0)
eps = {M00: 1, M01: -1, M10: -1, M11: 1}
Meps = sum(eps[s] * nocc[s] for s in eps)
Sy = hop(M00, M01) + hop(M10, M11)                      # unsigned in-cell y-hop (sandwich S)
Px = hop(M00, M10) + hop(M01, M11, -1.0)                # x-hop with sign (-1)^y (sandwich P)
th0, mu, U1, H1 = 0.4, 0.15, 0.2, 0.1


def step(Nv, ev, beta):
    Mh = expm(-0.5j * mu * Nv * Meps)
    S = expm(-1j * np.pi / 4 * Sy)
    R = S @ expm(-1j * beta * Px) @ S.conj().T
    Ux = R @ expm(-1j * th0 * Nv * ev * Gx) @ R.conj().T
    Uy = expm(-1j * th0 * Nv * ev * Gy)
    return Mh @ Uy @ Ux @ Mh


S0 = step(1.0, 1.0, 0.0)
S1 = step(1 - U1, 1 - U1, 0.5 * np.arcsin(H1))
pf0, pf1 = on({F: P[0]}), on({F: P[1]})
W = pf0 @ S0 + pf1 @ S1                      # fixed controlled unitary (each S(n) acts on matter only)
print("controlled step unitary: |W W^dag - 1| = %.1e ; commutes with f's possibility projector: %.1e"
      % (np.abs(W @ W.conj().T - np.eye(64)).max(), np.abs(W @ pf1 - pf1 @ W).max()))
Fw = np.diag([0.3, 0.8]); sF = np.sqrt(Fw); s1F = np.sqrt(np.eye(2) - Fw)
kraus = [('none', on({M00: s1F}))] + [(('form', k), on({M00: sF @ P[k] @ sF})) for k in (0, 1)]


def local_stats(rho, rule):
    if rule == 'CTRL':
        rho = W @ rho @ W.conj().T
    else:                                    # DIAL: angles from the branch's <n_f> (nonlinear in the state)
        x = float(np.real(np.trace(nf @ rho)))
        Ud = step(1 - U1 * x, 1 - U1 * x, 0.5 * np.arcsin(H1) * x)
        rho = Ud @ rho @ Ud.conj().T
    out = {}
    for key, K in kraus:
        r1 = K @ rho @ K.conj().T
        for m in (0, 1):
            Mm = on({M11: P[m]})
            out[(key, m)] = float(np.real(np.trace(Mm @ r1 @ Mm)))
    return out


def distant(rho, cond):
    if cond == 'none':
        return [rho]
    proj = P if cond == 'Z' else PX
    return [on({B: proj[k]}) @ rho @ on({B: proj[k]}) for k in (0, 1)]


rng = np.random.default_rng(20261003)
worst = {'CTRL': 0.0, 'DIAL': 0.0}
for trial in range(60):
    v = rng.normal(size=64) + 1j * rng.normal(size=64); v /= np.linalg.norm(v)
    rho = np.outer(v, v.conj())
    for rule in worst:
        stats = {}
        for cond in ('none', 'Z', 'X'):
            agg = {}
            for br in distant(rho, cond):
                wgt = float(np.real(np.trace(br)))
                st = local_stats(br / wgt, rule)
                for k2, val in st.items():
                    agg[k2] = agg.get(k2, 0.0) + wgt * val
            stats[cond] = agg
        keys = set().union(*[set(s) for s in stats.values()])
        for c1 in ('Z', 'X'):
            tv = 0.5 * sum(abs(stats[c1].get(k, 0) - stats['none'].get(k, 0)) for k in keys)
            worst[rule] = max(worst[rule], tv)
for rule, tv in worst.items():
    print("rule %-4s: max TV of local record odds (formation at m00, record at m11) between distant conditions "
          "(60 random 6-qubit states) = %.3e" % (rule, tv))
# light cone: the step is a finite-depth circuit of gates on field-site + nearest matter sites;
# check the matter step leaves the distant qubit's reduced state untouched
v = rng.normal(size=64) + 1j * rng.normal(size=64); v /= np.linalg.norm(v); rho = np.outer(v, v.conj())
def red_b(r):
    R = r.reshape([2] * 12)
    return np.einsum('a' + 'bcdef' + 'g' + 'bcdef->ag', R)
print("reduced state of b before/after the controlled step: |diff| = %.1e"
      % np.abs(red_b(rho) - red_b(W @ rho @ W.conj().T)).max())
