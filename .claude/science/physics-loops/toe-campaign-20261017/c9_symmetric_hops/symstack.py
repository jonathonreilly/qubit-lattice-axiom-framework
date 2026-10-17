"""O-covariant 4-copy stack built from a D3-symmetric clean hop system; condense the quad boson."""
import os, time
exec(open('symhopL.py').read().split("for bs in good:")[0])
bs = good[0]
beta = [[corners(c)[i] for i in bs[c]] for c in range(3)]
Fg = Fgens(beta)                      # copy-0 flux generators (dict ops at origin)
Fr = bk.torus_rows(Fg, L); rF, bF = rref_rank(Fr)
hops0 = []
for a in range(3):
    Aa = vec(bk.A((0, 0, 0), a, o0))
    rhs_F = (Fr[:, :n].astype(int) @ Aa[n:].astype(int) + Fr[:, n:].astype(int) @ Aa[:n].astype(int)) % 2
    A_ = np.vstack([symm(Fr, cols), symm(Brows, cols)])
    d = gf2_solve(A_, np.concatenate([rhs_F, np.zeros(len(Brows), int)]).astype(np.uint8))
    dv = np.zeros(2 * n, np.uint8); c = np.array(cols); dv[c] = d[:len(cols)]; dv[n + c] = d[len(cols):]
    hops0.append(Aa ^ dv)
# commutation table of copy-0 hops at a vertex (6 directions)
def at_vertex(d):
    a, s = bk.DIRS[d]
    return hops0[a] if s == 1 else shift(hops0[a], tuple(-E[a][t] for t in range(3)))
sy = lambda x, y: int((x[:n].astype(int) @ y[n:].astype(int) + x[n:].astype(int) @ y[:n].astype(int)) % 2)
print('copy-0 symmetric hops, anticommutation at a vertex:', [[sy(at_vertex(i), at_vertex(j)) for j in range(6)] for i in range(6)], flush=True)
# B_tail B_head content of the rotated hops
for M in stab:
    out = []
    for a in range(3):
        img = rot_vec(M, hops0[a]); dvec = M @ np.array(E[a]); b = int(np.nonzero(dvec)[0][0])
        base = (0, 0, 0) if dvec[b] == 1 else tuple(-E[b][t] for t in range(3))
        diff = img ^ shift(hops0[b], base)
        tb = vec(bk.prod(bk.B(base), bk.B(tuple(base[t] + E[b][t] for t in range(3)))))
        out.append('F' if inspan(bF, rF, diff) else ('F*BtBh' if inspan(bF, rF, diff ^ tb) else 'other'))
    print('  rotation', bk.kind(M), out, flush=True)
np.save('hops0_L%d.npy' % L, np.array(hops0)); np.save('F0_L%d.npy' % L, Fr)
