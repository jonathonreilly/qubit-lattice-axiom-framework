exec(open('cleanhopL.py').read().split("for bs in found:")[0])
good = [([0, 1], [0, 3], [1, 3]), ([1, 3], [0, 1, 2, 3], [0, 1])]
def rot_vec(M, x):
    perm = np.zeros(n, int)
    for v in V:
        w = tuple(int(c) for c in M @ np.array(v))
        for a in range(3):
            d = M @ np.array(E[a]); b = int(np.nonzero(d)[0][0])
            p = w if d[b] == 1 else tuple(w[t] - (1 if t == b else 0) for t in range(3))
            perm[3 * (((v[0] % L) * L + (v[1] % L)) * L + (v[2] % L)) + a] = 3 * (((p[0] % L) * L + (p[1] % L)) * L + (p[2] % L)) + b
    y = np.zeros_like(x); y[perm] = x[:n]; y[n + perm] = x[n:]; return y
def shift(x, s):
    y = np.zeros_like(x)
    for v in V:
        for a in range(3):
            k = 3 * ((v[0] * L + v[1]) * L + v[2]) + a
            u = tuple((v[i] + s[i]) % L for i in range(3))
            k2 = 3 * ((u[0] * L + u[1]) * L + u[2]) + a
            y[k2] = x[k]; y[n + k2] = x[n + k]
    return y
def inspan(basis, r, x): return rref_rank(np.vstack([basis, x[None, :]]))[0] == r
for bs in good:
    beta = [[corners(c)[i] for i in bs[c]] for c in range(3)]
    Fr = bk.torus_rows(Fgens(beta), L); rF, bF = rref_rank(Fr); rFB, bFB = rref_rank(np.vstack([Fr, Brows]))
    hops = []
    for a in range(3):
        Aa = vec(bk.A((0, 0, 0), a, o0))
        rhs_F = (Fr[:, :n].astype(int) @ Aa[n:].astype(int) + Fr[:, n:].astype(int) @ Aa[:n].astype(int)) % 2
        A_ = np.vstack([symm(Fr, cols), symm(Brows, cols)])
        d = gf2_solve(A_, np.concatenate([rhs_F, np.zeros(len(Brows), int)]).astype(np.uint8))
        dv = np.zeros(2 * n, np.uint8); c = np.array(cols); dv[c] = d[:len(cols)]; dv[n + c] = d[len(cols):]
        hops.append(Aa ^ dv)
    print(bs, 'hop weights', [int((h[:n] | h[n:]).sum()) for h in hops])
    for M in stab:
        res = []
        for a in range(3):
            img = rot_vec(M, hops[a])
            dvec = M @ np.array(E[a]); b = int(np.nonzero(dvec)[0][0])
            # image edge: base at 0 if direction +, else base at -e_b
            base = (0, 0, 0) if dvec[b] == 1 else tuple(-E[b][t] for t in range(3))
            target = shift(hops[b], base)
            diff = img ^ target
            res.append('F' if inspan(bF, rF, diff) else ('F+B' if inspan(bFB, rFB, diff) else 'not in G'))
        print('  ', bk.kind(M), res)
# D3 invariance of F at this L
for bs in good:
    beta = [[corners(c)[i] for i in bs[c]] for c in range(3)]
    gs = Fgens(beta); Fr = bk.torus_rows(gs, L); rF, bF = rref_rank(Fr)
    print(bs, 'F invariant under', [bk.kind(M) for M in stab if rref_rank(np.vstack([bF, bk.torus_rows([rot_op(M, g) for g in gs], L)]))[0] == rF])
