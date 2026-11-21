# GUIDE only (pure Python). Transverse spectrum of the open 3D box: nonzero
# eigenvalues of d*d versus {lambda_q with multiplicity r(q)-1}.
import math, itertools, sys

def box3(a):
    V = list(itertools.product(*[range(x) for x in a]))
    idx = {v: i for i, v in enumerate(V)}
    E = []
    for v in V:
        for d in range(3):
            w = list(v); w[d] += 1
            if tuple(w) in idx:
                E.append((v, d))
    eidx = {e: i for i, e in enumerate(E)}
    P = []
    for v in V:
        for d1 in range(3):
            for d2 in range(d1 + 1, 3):
                w1 = list(v); w1[d1] += 1; w1 = tuple(w1)
                w2 = list(v); w2[d2] += 1; w2 = tuple(w2)
                if w1 in idx and w2 in idx:
                    P.append([(eidx[(v, d1)], 1), (eidx[(w1, d2)], 1), (eidx[(w2, d1)], -1), (eidx[(v, d2)], -1)])
    return V, E, P

def jacobi_eigs(A, tol=1e-12):
    n = len(A)
    A = [row[:] for row in A]
    for sweep in range(100):
        off = sum(A[i][j]**2 for i in range(n) for j in range(n) if i != j)
        if off < tol:
            break
        for p in range(n - 1):
            for q in range(p + 1, n):
                apq = A[p][q]
                if abs(apq) < 1e-15:
                    continue
                theta = (A[q][q] - A[p][p]) / (2 * apq)
                t = (1 if theta >= 0 else -1) / (abs(theta) + math.sqrt(theta * theta + 1))
                c = 1 / math.sqrt(t * t + 1); s = t * c
                for k in range(n):
                    akp, akq = A[k][p], A[k][q]
                    A[k][p] = c * akp - s * akq; A[k][q] = s * akp + c * akq
                for k in range(n):
                    apk, aqk = A[p][k], A[q][k]
                    A[p][k] = c * apk - s * aqk; A[q][k] = s * apk + c * aqk
    return sorted(A[i][i] for i in range(n))

for a in ((2, 3, 4), (3, 3, 4), (3, 4, 5)):
    V, E, P = box3(a)
    n = len(E)
    K = [[0.0] * n for _ in range(n)]
    for row in P:
        for (i, si) in row:
            for (j, sj) in row:
                K[i][j] += si * sj
    ev = [x for x in jacobi_eigs(K) if x > 1e-9]
    pred = []
    for q in itertools.product(*[range(x) for x in a]):
        rq = sum(1 for qi in q if qi > 0)
        lam = sum(4 * math.sin(math.pi * qi / (2 * ai))**2 for qi, ai in zip(q, a))
        pred += [lam] * max(rq - 1, 0)
    pred.sort()
    dev = max(abs(x - y) for x, y in zip(ev, pred)) if len(ev) == len(pred) else None
    print("box", a, "|E|-|V|+1 =", len(E) - len(V) + 1, " #nonzero eig =", len(ev), " #predicted =", len(pred), " max dev =", dev)
    sys.stdout.flush()
