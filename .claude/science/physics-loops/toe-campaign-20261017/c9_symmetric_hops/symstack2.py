import os, time
exec(open('symhopL.py').read().split("for bs in good:")[0])
hops0 = list(np.load('hops0_L%d.npy' % L)); F0 = np.load('F0_L%d.npy' % L)
hs = []; reps = []
for M in O:
    h = H[bk.rot_order(M, o0)]
    if h not in hs: hs.append(h); reps.append(M)
hidx = {h: i for i, h in enumerate(hs)}
nq = 4 * n
def embed(x, j):
    y = np.zeros(2 * nq, np.uint8); y[4 * np.arange(n) + j] = x[:n]; y[nq + 4 * np.arange(n) + j] = x[n:]; return y
def copy_hop(j, b):
    Rj = reps[j]
    for a in range(3):
        d = Rj @ np.array(E[a]); bb = int(np.nonzero(d)[0][0])
        if bb == b:
            img = rot_vec(Rj, hops0[a])
            return img if d[bb] == 1 else shift(img, tuple(E[b]))
quad0 = [np.bitwise_xor.reduce([embed(copy_hop(j, b), j) for j in range(4)]) for b in range(3)]
def shift4(y, s):
    x = np.zeros_like(y)
    for j in range(4):
        x ^= embed(shift(np.concatenate([y[:nq][j::4], y[nq:][j::4]]), s), j)
    return x
Fj = [np.array([embed(rot_vec(reps[j], r), j) for r in F0]) for j in range(4)]
def Bv(j, v): return embed(vec(bk.B(v)), j)
evenB = np.array([Bv(0, v) ^ Bv(k, v) for v in V for k in (1, 2, 3)])
Q = np.array([shift4(qv, v) for v in V for qv in quad0])
sym = lambda X, Y: (X[:, :nq].astype(np.int32) @ Y[:, nq:].T.astype(np.int32) + X[:, nq:].astype(np.int32) @ Y[:, :nq].T.astype(np.int32)) % 2
print('quads commute:', not sym(Q, Q).any(), ' F^j commute with quads:', all(not sym(F, Q).any() for F in Fj), flush=True)
Gp = np.vstack(Fj + [evenB, Q]).astype(np.uint8)
t0 = time.time(); r, basis = rref_rank(Gp)
print('L', L, 'log2 dim', nq - r, round(time.time() - t0), 's', flush=True)
piv = np.array([int(np.flatnonzero(row)[0]) for row in basis])
def inG(Vs):
    Vs = np.atleast_2d(Vs); recon = (Vs[:, piv].astype(np.int32) @ basis.astype(np.int32)) % 2
    return (recon == Vs).all(axis=1)
# O-invariance: images of origin-cell generators
cell = [embed(rot_vec(reps[j], r), j) for j in range(4) for r in F0[:3 * 1]]  # placeholder replaced below
def rot4(M, y):
    pi = [hidx[H[bk.rot_order(M, bk.rot_order(reps[j], o0))]] for j in range(4)]
    out = np.zeros_like(y)
    for j in range(4):
        x = np.concatenate([y[:nq][j::4], y[nq:][j::4]])
        out ^= embed(rot_vec(M, x), pi[j])
    return out
# generators near origin: take all rows of Gp whose support touches the origin vertex's edges
orig = set(4 * e + j for e in range(3) for j in range(4))
near = [g for g in Gp if any(g[k] or g[nq + k] for k in orig)]
print('testing', len(near), 'generators touching the origin', flush=True)
bad = Counter()
for M in O:
    imgs = np.array([rot4(M, g) for g in near])
    bad[bk.kind(M)] += int((~inG(imgs)).sum())
print('generators whose rotated image is NOT in the group, per rotation type:', dict(bad), flush=True)
np.save('symstack_basis_L%d.npy' % L, basis)
