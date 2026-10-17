exec(open('fluxconv.py').read().split("t0 = time.time(); found = []")[0])
found = [([1], [0, 2, 3], [1]), ([2], [2], [2]), ([0, 1], [0, 3], [1, 3]), ([0, 2], [], [2, 3]), ([1, 3], [0, 1, 2, 3], [0, 1]), ([2, 3], [1, 2], [0, 2]), ([0, 1, 3], [0, 1, 3], [0, 1, 3]), ([0, 2, 3], [1], [0, 2, 3])]
n = 3 * L**3
def vec(op):
    x = np.zeros(2 * n, np.uint8)
    for (p, a), l in op.items():
        k = 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a
        if l in (1, 2): x[k] ^= 1
        if l in (2, 3): x[n + k] ^= 1
    return x
def gf2_solve(A, b):
    M = np.concatenate([A, b[:, None]], 1).astype(np.uint8) % 2; m, nn = A.shape; piv = []; r = 0
    for c in range(nn):
        nz = np.flatnonzero(M[r:, c])
        if nz.size == 0: continue
        p = r + nz[0]; M[[r, p]] = M[[p, r]]
        rows = np.flatnonzero(M[:, c]); rows = rows[rows != r]; M[rows] ^= M[r]; piv.append(c); r += 1
        if r == m: break
    if M[r:, -1].any(): return None
    x = np.zeros(nn, np.uint8)
    for i, c in enumerate(piv): x[c] = M[i, -1]
    return x
V = list(itertools.product(range(L), repeat=3))
Brows = np.array([vec(bk.B(v)) for v in V])
win = [(p, a) for p in itertools.product(range(-1, 3), repeat=3) for a in range(3)]
cols = sorted({3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + a for p, a in win})
def symm(R, x_cols):
    # coefficient matrix: rows R (full vectors), unknown on cols (X part then Z part)
    c = np.array(x_cols)
    return np.concatenate([R[:, n + c], R[:, c]], 1)
for bs in found:
    beta = [[corners(c)[i] for i in bs[c]] for c in range(3)]
    Fr = bk.torus_rows(Fgens(beta), L)
    ok = []
    for a in range(3):
        Aa = vec(bk.A((0, 0, 0), a, o0))
        rhs_F = (Fr[:, :n].astype(int) @ Aa[n:].astype(int) + Fr[:, n:].astype(int) @ Aa[:n].astype(int)) % 2
        A_ = np.vstack([symm(Fr, cols), symm(Brows, cols)])
        b_ = np.concatenate([rhs_F, np.zeros(len(Brows), int)]).astype(np.uint8)
        ok.append(gf2_solve(A_, b_) is not None)
    # also: does F intersect <B> beyond identity? (rank test)
    rF = rref_rank(Fr)[0]; rFB = rref_rank(np.vstack([Fr, Brows]))[0]
    print(bs, 'clean hops exist per direction:', ok, ' rank F', rF, 'rank F+B', rFB, flush=True)
print('reference (beta empty, ordering o0):', end=' ')
Fr = bk.torus_rows(Fgens([[], [], []]), L); print(rref_rank(Fr)[0], rref_rank(np.vstack([Fr, Brows]))[0])
