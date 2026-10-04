"""A52 c3b: exact free-fermion check on one coarse cube (12 link qubits, Z2 reduction of the hops).
Encoded hopping H = sum_l (i/2) A_l (B_v - B_w), A_l = X_l * (record-conditioned field factors),
B_v = product of the field factors on v's three cube legs (charge parity).  In each charge number N its
spectrum must equal the union over the 32 flux classes of free-fermion N-particle spectra on the cube graph.
Control: bare hops X_l (1 - B_v B_w)/2 must give hard-core bosons instead."""
import signal, itertools
signal.alarm(115)
import numpy as np
from a52lib import *

rng = np.random.default_rng(7)
CORN = [tuple(c) for c in itertools.product([0, 2], repeat=3)]
cid = {c: k for k, c in enumerate(CORN)}
LINKS = sorted({tuple(int(v) for v in (np.array(c) + np.array(d))) for c in CORN for d in DIRS
                if all(0 <= x <= 2 for x in np.array(c) + np.array(d))})
lid = {l: k for k, l in enumerate(LINKS)}
NQ = 12; DIM = 1 << NQ
def ends(l):
    x = np.array(l); a = [k for k in range(3) if x[k] % 2][0]; e = np.zeros(3, int); e[a] = 1
    return tuple(int(t) for t in x - e), 2 * a, tuple(int(t) for t in x + e), 2 * a + 1
def legs_in(v):
    return [i for i in range(6) if all(0 <= x <= 2 for x in np.array(v) + 2 * np.array(DIRS[i]))]
def lk(v, j):
    return lid[tuple(int(t) for t in np.array(v) + np.array(DIRS[j]))]
states = np.arange(DIM)
bits = ((states[:, None] >> np.arange(NQ)[None, :]) & 1).astype(np.int8)
Bpar = np.zeros((8, DIM), np.int8)
for v in CORN:
    for j in legs_in(v):
        Bpar[cid[v]] ^= bits[:, lk(v, j)]
Bv = 1 - 2 * Bpar.astype(float)                        # +-1
Ncharge = Bpar.sum(axis=0)

def decor_set(l, recs, Tof):
    v, i, w, ip = ends(l); S = []
    for (c, leg) in ((v, i), (w, ip)):
        T = Tof[recs[c]]
        for j in legs_in(c):
            if j != leg and T[leg][j]:
                S.append(lk(c, j))
    return S

def H_sector(N, recs, Tof, kind):
    """fermion: H = i M with M real antisymmetric -> spectrum from eig(-M^2) (memory-lean);
    boson: H real symmetric."""
    idx = np.nonzero(Ncharge == N)[0]; pos = -np.ones(DIM, int); pos[idx] = np.arange(len(idx))
    M = np.zeros((len(idx), len(idx)))
    for l in LINKS:
        q = lid[l]; v, i, w, ip = ends(l)
        S = decor_set(l, recs, Tof) if kind == 'fermion' else []
        sgn = (-1.0) ** (bits[idx][:, S].sum(axis=1) if S else 0)
        tgt = idx ^ (1 << q)
        if kind == 'fermion':
            amp = 0.5 * (Bv[cid[v], idx] - Bv[cid[w], idx]) * sgn       # H = i * amp (i/2 X Z_S (B_v - B_w))
        else:
            amp = 0.5 * (1 - Bv[cid[v], idx] * Bv[cid[w], idx]) * sgn    # X (1 - B_v B_w)/2
        ok = pos[tgt] >= 0
        M[pos[tgt[ok]], np.arange(len(idx))[ok]] += amp[ok]
    if kind == 'fermion':
        assert np.abs(M + M.T).max() < 1e-12
        mu = np.sort(np.clip(np.linalg.eigvalsh(-(M @ M)), 0, None))[::2]
        return np.sort(np.concatenate([-np.sqrt(mu), np.sqrt(mu)]))
    assert np.abs(M - M.T).max() < 1e-12
    return np.sort(np.linalg.eigvalsh(M))

# free side: 32 flux classes (spanning-tree gauge)
EDGES = [(cid[ends(l)[0]], cid[ends(l)[2]]) for l in LINKS]
tree = []; seen = {0}
while len(seen) < 8:
    for k, (a, b) in enumerate(EDGES):
        if k not in tree and ((a in seen) ^ (b in seen)):
            tree.append(k); seen |= {a, b}
free_edges = [k for k in range(12) if k not in tree]
def classes():
    for sg in itertools.product([1, -1], repeat=len(free_edges)):
        u = np.ones(12)
        for k, s in zip(free_edges, sg):
            u[k] = s
        yield u
def free_union(N, stat):
    out = []
    for u in classes():
        h = np.zeros((8, 8))
        for k, (a, b) in enumerate(EDGES):
            h[a, b] = h[b, a] = u[k]
        if stat == 'fermion':
            e = np.linalg.eigvalsh(h)
            out += [sum(c) for c in itertools.combinations(e, N)]
        else:
            basis = [s for s in itertools.combinations(range(8), N)]; bi = {s: k for k, s in enumerate(basis)}
            M = np.zeros((len(basis), len(basis)))
            for s in basis:
                for k, (a, b) in enumerate(EDGES):
                    for (x, y) in ((a, b), (b, a)):
                        if y in s and x not in s:
                            t = tuple(sorted(set(s) - {y} | {x}))
                            M[bi[t], bi[s]] += u[k]
            out += list(np.linalg.eigvalsh(M))
    return np.sort(np.array(out))

Tof0, _ = family(ALL_C3_T[0])
print("flux classes: %d (spanning tree of %d edges, %d free)" % (len(list(classes())), len(tree), len(free_edges)))
for N in (2, 4):
    FF = free_union(N, 'fermion'); HB = free_union(N, 'boson')
    eF = H_sector(N, {c: F0 for c in CORN}, Tof0, 'fermion')
    eB = H_sector(N, {c: F0 for c in CORN}, Tof0, 'boson')
    print("N=%d: dims %d | decorated vs free fermions max|diff| %.1e ; vs hard-core bosons %.2f" % (
        N, len(eF), np.max(np.abs(eF - FF)), np.max(np.abs(eF - HB))))
    print("      bare control vs hard-core bosons %.1e ; vs free fermions %.2f" % (np.max(np.abs(eB - HB)), np.max(np.abs(eB - FF))))
# record-direction and tournament independence (N = 2, 3)
ref = {N: H_sector(N, {c: F0 for c in CORN}, Tof0, "fermion") for N in (2,)}
worst = 0.0; runs = 0
for tk in (0, 9, 22, 31):
    Tof, _ = family(ALL_C3_T[tk])
    cfgs = [{c: f for c in CORN} for f in BD] + [{c: BD[rng.integers(8)] for c in CORN} for _ in range(3)]
    for recs in cfgs:
        for N in (2,):
            worst = max(worst, np.max(np.abs(H_sector(N, recs, Tof, 'fermion') - ref[N]))); runs += 1
print("spectra for 4 tournaments x (8 uniform f + 3 random backgrounds) x N=2: %d runs, max |diff| vs f0 = %.1e" % (runs, worst))
# zero-flux sector: S_p = +1 on all six faces -> must equal free fermions with all u = +1
FACES = []
for a, b in [(0, 1), (0, 2), (1, 2)]:
    k = 3 - a - b
    for hgt in (0, 2):
        v0 = [0, 0, 0]; v0[k] = hgt
        ea = np.eye(3, dtype=int)[a] * 2; eb = np.eye(3, dtype=int)[b] * 2
        FACES.append([tuple(v0), tuple(np.array(v0) + ea), tuple(np.array(v0) + ea + eb), tuple(np.array(v0) + eb)])
def apply_A(l, recs, Tof, st, sg):
    q = lid[l]; S = decor_set(l, recs, Tof)
    par = np.zeros(len(st), np.int64)
    for j in S:
        par ^= (st >> j) & 1
    return st ^ (1 << q), sg * (1 - 2 * par)
N = 2
idx = np.nonzero(Ncharge == N)[0]; pos = -np.ones(DIM, int); pos[idx] = np.arange(len(idx))
recs = {c: F0 for c in CORN}
P = np.eye(len(idx)); Smats = []
for cs in FACES:
    st = idx.copy(); sg = np.ones(len(idx))
    for kk in range(4)[::-1]:            # product A1 A2 A3 A4: A4 acts first
        l = tuple(int(t) for t in (np.array(cs[kk]) + np.array(cs[(kk + 1) % 4])) // 2)
        st, sg = apply_A(l, recs, Tof0, st, sg)
    assert np.all(pos[st] >= 0)
    Sp = np.zeros((len(idx), len(idx))); Sp[pos[st], np.arange(len(idx))] = sg
    Smats.append(Sp)
    P = P @ (np.eye(len(idx)) + Sp) / 2
print("   S_p mutually commute: %s; S_p^2 = 1: %s" % (all(np.allclose(a @ b, b @ a) for a in Smats for b in Smats), all(np.allclose(a @ a, np.eye(len(idx))) for a in Smats)))
w, V = np.linalg.eigh((P + P.T) / 2); Vr = V[:, w > 0.5]
Hfull = None
idx2 = idx
Hn = np.zeros((len(idx), len(idx)), complex)
for l in LINKS:
    v, i, ww, ip = ends(l)
    st, sg = apply_A(l, recs, Tof0, idx.copy(), np.ones(len(idx)))
    amp = 0.5j * (Bv[cid[v], idx] - Bv[cid[ww], idx]) * sg
    ok = pos[st] >= 0
    Hn[pos[st[ok]], np.arange(len(idx))[ok]] += amp[ok]
e0 = np.sort(np.linalg.eigvalsh(Vr.conj().T @ Hn @ Vr))
h = np.zeros((8, 8))
for (a, b) in EDGES:
    h[a, b] = h[b, a] = 1.0
ef = np.sort([sum(c) for c in itertools.combinations(np.linalg.eigvalsh(h), N)])
hpi = h.copy()
print("S_p = +1 sector (N=2): dim %d; spectrum vs free fermions at zero flux: max|diff| %.1e" % (
    Vr.shape[1], np.max(np.abs(e0 - ef)) if len(e0) == len(ef) else -1))
print("done")
# pi-flux sector: all six S_p = -1 -> free fermions with flux pi through every face of the cube
Pm = np.eye(len(idx))
for Sp in Smats:
    Pm = Pm @ (np.eye(len(idx)) - Sp) / 2
w, V = np.linalg.eigh((Pm + Pm.T) / 2); Vm = V[:, w > 0.5]
em = np.sort(np.linalg.eigvalsh(Vm.conj().T @ Hn @ Vm))
def face_prod(u):
    out = []
    for cs in FACES:
        pr = 1
        for kk in range(4):
            a, b = cid[cs[kk]], cid[cs[(kk + 1) % 4]]
            k = [m for m, e in enumerate(EDGES) if set(e) == {a, b}][0]
            pr *= u[k]
        out.append(pr)
    return out
upi = [u for u in classes() if all(x == -1 for x in face_prod(u))][0]
hp = np.zeros((8, 8))
for k, (a, b) in enumerate(EDGES):
    hp[a, b] = hp[b, a] = upi[k]
epi = np.sort([sum(c) for c in itertools.combinations(np.linalg.eigvalsh(hp), N)])
print("S_p = -1 sector (N=2): dim %d; vs free fermions with pi flux through every face: max|diff| %.1e" % (
    Vm.shape[1], np.max(np.abs(em - epi)) if len(em) == len(epi) else -1))
print("single-particle levels, zero flux: %s ; pi flux: %s" % (np.round(np.linalg.eigvalsh(h), 4), np.round(np.linalg.eigvalsh(hp), 4)))
