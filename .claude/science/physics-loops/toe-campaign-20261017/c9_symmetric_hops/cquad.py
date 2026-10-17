exec(open('symstack2.py').read().split("print('quads commute:'")[0])
import itertools
def at_vertex4(d):
    a, s = bk.DIRS[d]
    return quad0[a] if s == 1 else shift4(quad0[a], tuple(-E[a][t] for t in range(3)))
syq = lambda x, y: int((x[:nq].astype(int) @ y[nq:].astype(int) + x[nq:].astype(int) @ y[:nq].astype(int)) % 2)
H4 = [at_vertex4(d) for d in range(6)]
C = [[syq(H4[i], H4[j]) for j in range(6)] for i in range(6)]
print('quad anticommutation at a vertex:', C)
tri = [(t, (C[t[0]][t[1]] + C[t[0]][t[2]] + C[t[1]][t[2]]) % 2) for t in itertools.combinations(range(6), 3)]
print('odd triangles:', [t for t, p in tri if p])
# switching set S (contains direction 0 by convention) making C zero: S = {d: C[0][d] = 1} ^ ...
S = {0} | {d for d in range(1, 6) if C[0][d] == 1}
ok = all(C[i][j] == ((i in S) != (j in S)) for i in range(6) for j in range(6) if i != j)
print('switching to zero possible:', ok, 'S =', sorted(S), 'directions', [bk.DIRS[d] for d in sorted(S)])
# also: do quads on non-adjacent edges commute (e.g. parallel neighbours)?
far = []
for d in range(3):
    for s in itertools.product(range(-2, 3), repeat=3):
        if s != (0, 0, 0):
            for d2 in range(3):
                if syq(quad0[d], shift4(quad0[d2], s)): far.append((d, d2, s))
print('anticommuting non-vertex-sharing quad pairs (sample):', [f for f in far if not (sum(map(abs, f[2])) <= 1)][:10], len(far))
