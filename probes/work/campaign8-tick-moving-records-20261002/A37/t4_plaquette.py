"""A37 t4: the 'flow around' step PS (record x -> y = x+e; y's content -> y+f; (y+f)'s -> x+f; (x+f)'s -> x),
with the side f chosen uniformly among the directions perpendicular to e.  Supplied toys.

2D: 3x3 patch, record at the centre (9 qubits), plus a distant partner b for the link test (10 qubits).
    K_{e,f} = sqrt(c/(4*2)) P_loop(e,f) sqrt(W_y),  K_stay = sqrt(1 - (c/4) sum_e W_{x+e});  W = content weight.
    Checks: completeness; covariance under the 4 soldered quarter turns about x; turning space alone;
    turning the possibilities alone; purity of the post-step state given the step direction (SW = 1);
    where a Bell link of y with b ends up (Z/X agreement, mutual information).
3D: window x, y = x+e, x+f, y+f for the 4 sides f (10 qubits): covariance of the 4-loop template under the
    soldered quarter turns about the step axis.
"""
import signal, itertools
import numpy as np
signal.alarm(55)
rng = np.random.default_rng(4)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1.0 + 0j, -1])
I2 = np.eye(2); pauli = [sx, sy, sz]

def su2_from_R(R):
    t = np.trace(R)
    if t > 0:
        s = np.sqrt(t + 1) * 2; w = s / 4; x = (R[2, 1] - R[1, 2]) / s; y = (R[0, 2] - R[2, 0]) / s; z = (R[1, 0] - R[0, 1]) / s
    elif R[0, 0] > R[1, 1] and R[0, 0] > R[2, 2]:
        s = np.sqrt(1 + R[0, 0] - R[1, 1] - R[2, 2]) * 2; w = (R[2, 1] - R[1, 2]) / s; x = s / 4; y = (R[0, 1] + R[1, 0]) / s; z = (R[0, 2] + R[2, 0]) / s
    elif R[1, 1] > R[2, 2]:
        s = np.sqrt(1 + R[1, 1] - R[0, 0] - R[2, 2]) * 2; w = (R[0, 2] - R[2, 0]) / s; x = (R[0, 1] + R[1, 0]) / s; y = s / 4; z = (R[1, 2] + R[2, 1]) / s
    else:
        s = np.sqrt(1 + R[2, 2] - R[0, 0] - R[1, 1]) * 2; w = (R[1, 0] - R[0, 1]) / s; x = (R[0, 2] + R[2, 0]) / s; y = (R[1, 2] + R[2, 1]) / s; z = s / 4
    return w * I2 - 1j * (x * sx + y * sy + z * sz)

def op_on(ops, N):
    out = np.array([[1.0 + 0j]])
    for k in range(N):
        out = np.kron(out, ops.get(k, I2))
    return out

def perm_op(pi, N):
    Dm = 2 ** N; P = np.zeros((Dm, Dm))
    for bb in range(Dm):
        bits = [(bb >> (N - 1 - k)) & 1 for k in range(N)]
        nb = [0] * N
        for i in range(N):
            nb[pi[i]] = bits[i]
        P[sum(bit << (N - 1 - k) for k, bit in enumerate(nb)), bb] = 1
    return P

def sqrtm_psd(A):
    w, V = np.linalg.eigh(A)
    return (V * np.sqrt(np.clip(w, 0, None))) @ V.conj().T

def rand_qubit():
    v = rng.normal(size=2) + 1j * rng.normal(size=2); return v / np.linalg.norm(v)

alpha, beta, c = 0.15, 0.85, 0.6
def Wmat(r): return beta * I2 + (alpha - beta) * np.outer(r, r.conj())

# ------------------------------------------------------------------ 2D patch
coords = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)]
cidx = {p: k for k, p in enumerate(coords)}
N2 = 9; X0 = cidx[(0, 0)]
E2 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def perp(e): return [(e[1], e[0]), (-e[1], -e[0])] if e[0] == 0 else [(0, 1), (0, -1)]
def add(p, q): return (p[0] + q[0], p[1] + q[1])
def loop_perm(e, f, N, cmap):
    x = (0, 0); y = add(x, e); yf = add(y, f); xf = add(x, f)
    pi = {k: k for k in range(N)}
    pi[cmap[x]] = cmap[y]; pi[cmap[y]] = cmap[yf]; pi[cmap[yf]] = cmap[xf]; pi[cmap[xf]] = cmap[x]
    return perm_op(pi, N)
def swap_perm(e, N, cmap):
    pi = {k: k for k in range(N)}
    pi[cmap[(0, 0)]] = cmap[e]; pi[cmap[e]] = cmap[(0, 0)]
    return perm_op(pi, N)
LOOPS = {(e, f): loop_perm(e, f, N2, cidx) for e in E2 for f in perp(e)}
SWAPS = {e: swap_perm(e, N2, cidx) for e in E2}

def kraus_PS(r, N=N2, cmap=cidx, loops=LOOPS):
    W = Wmat(r); sW = sqrtm_psd(W)
    K = {}
    for e in E2:
        for f in perp(e):
            K[(e, f)] = np.sqrt(c / 8) * loops[(e, f)] @ op_on({cmap[e]: sW}, N)
    K["stay"] = sqrtm_psd(np.eye(2 ** N) - (c / 4) * sum(op_on({cmap[e]: W}, N) for e in E2))
    return K
def kraus_SW(r):
    W = Wmat(r); sW = sqrtm_psd(W)
    K = {e: np.sqrt(c / 4) * SWAPS[e] @ op_on({cidx[e]: sW}, N2) for e in E2}
    K["stay"] = sqrtm_psd(np.eye(2 ** N2) - (c / 4) * sum(op_on({cidx[e]: W}, N2) for e in E2))
    return K

r = rand_qubit()
K = kraus_PS(r)
comp = np.abs(sum(k.conj().T @ k for k in K.values()) - np.eye(2 ** N2)).max()
# soldered quarter turns about x (rotation about the z axis, perpendicular to the plane)
def Rz(n):
    a = n * np.pi / 2
    return np.array([[np.cos(a), -np.sin(a), 0], [np.sin(a), np.cos(a), 0], [0, 0, 1]]).round(12)
dev_cov = dev_sp = dev_int = 0.0
for n in range(4):
    R3 = Rz(n); u = su2_from_R(R3)
    rot = lambda p: (int(round(R3[0, 0] * p[0] + R3[0, 1] * p[1])), int(round(R3[1, 0] * p[0] + R3[1, 1] * p[1])))
    P = perm_op({cidx[p]: cidx[rot(p)] for p in coords}, N2)
    UN = op_on({k: u for k in range(N2)}, N2)
    V = P @ UN
    Kr = kraus_PS(u @ r)
    for (e, f), k in [(key, K[key]) for key in K if key != "stay"]:
        tgt = (rot(e), rot(f))
        dev_cov = max(dev_cov, np.abs(V @ k @ V.conj().T - Kr[tgt]).max())
        dev_sp = max(dev_sp, np.abs(P @ k @ P.T - K[tgt]).max())
    dev_cov = max(dev_cov, np.abs(V @ K["stay"] @ V.conj().T - Kr["stay"]).max())
for _ in range(3):
    A = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); Uq, _r = np.linalg.qr(A)
    UN = op_on({k: Uq for k in range(N2)}, N2)
    Kr = kraus_PS(Uq @ r)
    for key in K:
        dev_int = max(dev_int, np.abs(UN @ K[key] @ UN.conj().T - Kr[key]).max())
print("2D flow-around step PS on a 3x3 patch (record at the centre):")
print(f"   completeness {comp:.1e}; covariance under the 4 soldered quarter turns {dev_cov:.1e}; "
      f"turning space alone {dev_sp:.1e}; turning the possibilities alone {dev_int:.1e}")

# purity of the post-step state given the step direction, random neighbourhood states
pur_PS, pur_SW = [], []
Ksw = kraus_SW(r)
for trial in range(20):
    v = rng.normal(size=2 ** 8) + 1j * rng.normal(size=2 ** 8); v /= np.linalg.norm(v)
    # insert the record content at the centre (qubit X0)
    t = v.reshape([2] * 8)
    full = np.tensordot(r, t, axes=0)                       # record qubit first
    order = [X0] + [k for k in range(N2) if k != X0]
    full = np.transpose(full, np.argsort(order))           # axis k <-> site k
    psi = full.reshape(-1); rho = np.outer(psi, psi.conj())
    for e in E2:
        rp = sum(K[(e, f)] @ rho @ K[(e, f)].conj().T for f in perp(e)); p = np.real(np.trace(rp))
        pur_PS.append(np.real(np.trace(rp @ rp)) / p ** 2)
        rs = Ksw[e] @ rho @ Ksw[e].conj().T; ps = np.real(np.trace(rs))
        pur_SW.append(np.real(np.trace(rs @ rs)) / ps ** 2)
print(f"   purity of the post-step state given the step direction (20 random neighbourhood states x 4 directions): "
      f"PS mean {np.mean(pur_PS):.4f} (min {np.min(pur_PS):.4f}, max {np.max(pur_PS):.4f}); SW {np.min(pur_SW):.6f}-{np.max(pur_SW):.6f}")

# where a Bell link of y with a distant b ends up (record content |0>, other sites the emptiness |1>)
# reduced to the 6 patch sites touched by +x steps plus b (7 qubits)
k0 = np.array([1.0, 0]); k1 = np.array([0, 1.0]); kp = (k0 + k1) / np.sqrt(2); km = (k0 - k1) / np.sqrt(2)
e = (1, 0); y = e
sub = [(0, 0), (1, 0), (1, 1), (1, -1), (0, 1), (0, -1)]
cmap3 = {p: k for k, p in enumerate(sub)}; N3 = 7; B = 6
psi = np.zeros(2 ** N3, complex)
for bval in (0, 1):
    bits = [1] * N3
    bits[cmap3[(0, 0)]] = 0; bits[cmap3[y]] = bval; bits[B] = bval
    psi[sum(bt << (N3 - 1 - k) for k, bt in enumerate(bits))] = 1 / np.sqrt(2)
rho = np.outer(psi, psi.conj())
def post(rule):
    if rule == "SW":
        P = swap_perm(e, N3, cmap3); return P @ rho @ P.T
    out = 0
    for f in perp(e):
        P = loop_perm(e, f, N3, cmap3); out = out + 0.5 * (P @ rho @ P.T)
    return out
def pair(rr, i, j, N):
    t = rr.reshape([2] * (2 * N)); ii = list(range(2 * N))
    for k in range(N):
        if k not in (i, j):
            ii[k + N] = ii[k]
    return np.einsum(t, ii, [i, j, i + N, j + N]).reshape(4, 4)
def ent(m):
    w = np.linalg.eigvalsh(m); w = w[w > 1e-14]; return float(-(w * np.log2(w)).sum())
def agree(r2, basis):
    return sum(np.real(np.trace(np.kron(np.outer(v, v), np.outer(v, v)) @ r2)) for v in basis)
print("   link test (record steps +x; y was Bell-linked with distant b): P(Z agree), P(X agree), I(site:b)")
for rule in ("SW", "PS"):
    rr = post(rule)
    cells = []
    for name, p in (("x", (0, 0)), ("y+f", (1, 1)), ("y-f", (1, -1)), ("x+f", (0, 1)), ("x-f", (0, -1))):
        r2 = pair(rr, cmap3[p], B, N3).reshape(4, 4)
        I = ent(np.einsum("ijkj->ik", r2.reshape(2, 2, 2, 2))) + ent(np.einsum("ijil->jl", r2.reshape(2, 2, 2, 2))) - ent(r2)
        cells.append(f"{name}: {agree(r2,(k0,k1)):.3f}/{agree(r2,(kp,km)):.3f}/{I:.3f}")
    print(f"     {rule}: " + " | ".join(cells) + f"   purity {np.real(np.trace(rr @ rr)):.3f}")

# ------------------------------------------------------------------ 3D template (vector-based, low memory)
x3 = (0, 0, 0); e3 = (1, 0, 0)
sides = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
W3 = [x3, e3] + [s for s in sides] + [tuple(np.add(e3, s)) for s in sides]
c3 = {p: k for k, p in enumerate(W3)}; N4 = len(W3)
def loop3_map(f):
    y = e3; yf = tuple(np.add(y, f)); xf = f
    pi = {k: k for k in range(N4)}
    pi[c3[x3]] = c3[y]; pi[c3[y]] = c3[yf]; pi[c3[yf]] = c3[xf]; pi[c3[xf]] = c3[x3]
    return pi
def apply_perm(pi, v):
    """Content of site i moves to site pi[i]."""
    t = v.reshape([2] * N4)
    src = [None] * N4
    for i in range(N4):
        src[pi[i]] = i
    return np.transpose(t, src).reshape(-1)
def apply_one(m, k, v):
    t = v.reshape([2] * N4)
    t = np.moveaxis(np.tensordot(m, t, axes=([1], [k])), 0, k)
    return t.reshape(-1)
def apply_all(m, v):
    for k in range(N4):
        v = apply_one(m, k, v)
    return v
def K3_apply(rr, f, v):
    v = apply_one(sqrtm_psd(Wmat(rr)), c3[e3], v)
    return np.sqrt(c / 24) * apply_perm(loop3_map(f), v)
Rx = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
u = su2_from_R(Rx.astype(float))
dev3 = 0.0; dev_single = 0.0
for n in range(1, 4):
    Rn = np.linalg.matrix_power(Rx, n); un = np.linalg.matrix_power(u, n)
    piR = {c3[p]: c3[tuple(Rn @ np.array(p))] for p in W3}
    V = lambda v: apply_perm(piR, apply_all(un, v))
    for _ in range(6):
        v = rng.normal(size=2 ** N4) + 1j * rng.normal(size=2 ** N4); v /= np.linalg.norm(v)
        for f in sides:
            lhs = V(K3_apply(r, f, v))
            rhs = K3_apply(un @ r, tuple(Rn @ np.array(f)), V(v))
            dev3 = max(dev3, np.abs(lhs - rhs).max())
            if f == (0, 1, 0):
                dev_single = max(dev_single, np.abs(lhs - K3_apply(un @ r, f, V(v))).max())
print("3D window around the step bond (10 qubits): the four flow-around loops under the soldered quarter turns about the step axis")
print(f"   (checked on random states) mixture template covariance error {dev3:.1e}; "
      f"a single fixed loop (side +y) is NOT covariant: deviation {dev_single:.3f}")
