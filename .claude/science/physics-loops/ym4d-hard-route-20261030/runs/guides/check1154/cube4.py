# GUIDE only (pure Python). Curl projection on the open and periodic b^4 cubes:
# rank, minimum diagonal (claim >= 1/6), mean diagonal, periodic diagonal.
import math, itertools, sys

def cube4(b, periodic):
    V = list(itertools.product(range(b), repeat=4))
    idx = {v: i for i, v in enumerate(V)}
    def step(v, d):
        w = list(v); w[d] += 1
        if periodic:
            w[d] %= b
        w = tuple(w)
        return w if w in idx else None
    E = []
    for v in V:
        for d in range(4):
            if step(v, d) is not None:
                E.append((v, d))
    eidx = {e: i for i, e in enumerate(E)}
    P = []
    for v in V:
        for d1 in range(4):
            for d2 in range(d1 + 1, 4):
                w1 = step(v, d1); w2 = step(v, d2)
                if w1 is None or w2 is None:
                    continue
                P.append([(eidx[(v, d1)], 1), (eidx[(w1, d2)], 1), (eidx[(w2, d1)], -1), (eidx[(v, d2)], -1)])
    return V, E, P

def projection_diag(nF, cols):
    Q = []
    for c in cols:
        v = c[:]
        for _ in range(2):
            for qv in Q:
                dot = sum(a * b for a, b in zip(qv, v))
                if dot != 0.0:
                    v = [a - dot * b for a, b in zip(v, qv)]
        nrm = math.sqrt(sum(a * a for a in v))
        if nrm > 1e-8:
            Q.append([a / nrm for a in v])
    diag = [sum(qv[p] ** 2 for qv in Q) for p in range(nF)]
    return len(Q), diag

for (b, per) in ((3, False), (3, True)):
    V, E, P = cube4(b, per)
    nF = len(P)
    cols = [[0.0] * nF for _ in E]
    for p, row in enumerate(P):
        for (e, s) in row:
            cols[e][p] += s
    rank, diag = projection_diag(nF, cols)
    exp_rank = 3 * b**4 - 3 if per else 3 * b**4 - 4 * b**3 + 1
    ms = sum((x - 0.5) ** 2 for x in diag) / nF
    print("b=%d periodic=%s |V|=%d |E|=%d |F|=%d rank=%d expected=%d min diag=%.6f max diag=%.6f mean diag=%.6f mean sq dev from 1/2=%.6f"
          % (b, per, len(V), len(E), nF, rank, exp_rank, min(diag), max(diag), sum(diag) / nF, ms))
    sys.stdout.flush()
