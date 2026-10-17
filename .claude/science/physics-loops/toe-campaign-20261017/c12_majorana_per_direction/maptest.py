exec(open('gse_pair2.py').read().split("if __name__ == '__main__':")[0])
rng = np.random.default_rng(1)
M = next(Mm for Mm in O if bk.kind(Mm) == 'C2edge')
pi = [bk.rotdir(M, d) for d in range(6)]
eps = next(e for e in itertools.product((1, -1), repeat=6) if np.prod(e) == perm_sign(pi))
def randP():
    return [rng.integers(0, 2, n).astype(np.uint8), rng.integers(0, 2, n).astype(np.uint8), int(rng.integers(0, 4))]
bad = 0
for _ in range(20):
    P, Q = randP(), randP()
    lhs = map_pauli(rb.mulp(P, Q), M, eps); rhs = rb.mulp(map_pauli(P, M, eps), map_pauli(Q, M, eps))
    bad += int(not ((lhs[0] == rhs[0]).all() and (lhs[1] == rhs[1]).all() and lhs[2] == rhs[2]))
print('homomorphism failures', bad)
# gamma images
g_bad = 0
for v in V[:5]:
    for d in range(6):
        im = map_pauli(gamma(v, d), M, eps); tgt = gamma(tuple(int(x) for x in M @ np.array(v)), pi[d])
        tgt = [tgt[0], tgt[1], (tgt[2] + (0 if eps[d] == 1 else 2)) % 4]
        g_bad += int(not ((im[0] == tgt[0]).all() and (im[1] == tgt[1]).all() and im[2] == tgt[2]))
print('gamma image failures', g_bad)
# Hermiticity of gammas
print('gamma hermitian:', all((gamma((0,0,0), d)[2] - int(gamma((0,0,0), d)[0].astype(int) @ gamma((0,0,0), d)[1].astype(int))) % 2 == 0 for d in range(6)))
