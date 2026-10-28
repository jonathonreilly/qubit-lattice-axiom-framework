#!/usr/bin/env python3
# checks/hr1_wilson.py -- the CORRECTED currency gate: d_Z acting on 1-FORMS (the Wilson
# block of Hess F_k), per the AMENDMENT of 2026-10-28 21:53:48 UTC in checks/hr1_criteria.md.
# POST-HOC relative to checks/hr1_flat.py, which is kept unaltered and is not rerun.
# Pure python, exact integer arithmetic only. No numpy, no BLAS, no lock.

T = 8

I3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
R3 = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
I1 = [[1]]


def mm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def mT(A):
    return [list(r) for r in zip(*A)]


def mpow(A, e):
    n = len(A)
    out = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(e):
        out = mm(out, A)
    return out


def iszero(A):
    return all(all(v == 0 for v in r) for r in A)


S = [(a, b) for a in range(T) for b in range(T)]
SIDX = {y: i for i, y in enumerate(S)}
LINKS = [(y, mu) for y in S for mu in (0, 1)]
LIDX = {b: i for i, b in enumerate(LINKS)}
PLAQ = list(S)                      # in d = 2 one plaquette (mu=0 < nu=1) per site
PIDX = {y: i for i, y in enumerate(PLAQ)}


def shift(y, mu, s=1):
    return ((y[0] + s) % T, y[1]) if mu == 0 else (y[0], (y[1] + s) % T)


def build(Adg):
    dim = len(Adg)
    G = {y: mpow(Adg, y[0]) for y in S}
    Z = {}
    for y in S:
        for mu in (0, 1):
            Z[(y, mu)] = mm(G[y], mT(G[shift(y, mu)]))
    return dim, Z, G


def d01(Z, dim, cov):
    """d or d_Z : 0-forms -> 1-forms."""
    M = [[0] * (len(S) * dim) for _ in range(len(LINKS) * dim)]
    for b in LINKS:
        y, mu = b
        yp = shift(y, mu)
        A = Z[b] if cov else [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]
        r0, cY, cYp = LIDX[b] * dim, SIDX[y] * dim, SIDX[yp] * dim
        for i in range(dim):
            M[r0 + i][cY + i] -= 1
            for j in range(dim):
                M[r0 + i][cYp + j] += A[i][j]
    return M


def d12(Z, dim, cov):
    """d or d_Z : 1-forms -> 2-forms.
    (d_Z u)(p) = u(z,0) + Ad_{Z(z,0)} u(z+e0,1) - Ad_{Z(z,1)} u(z+e1,0) - u(z,1)."""
    ident = [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]
    M = [[0] * (len(LINKS) * dim) for _ in range(len(PLAQ) * dim)]

    def add(prow, link, A, sgn):
        c0 = LIDX[link] * dim
        for i in range(dim):
            for j in range(dim):
                M[prow + i][c0 + j] += sgn * A[i][j]

    for z in PLAQ:
        r0 = PIDX[z] * dim
        add(r0, (z, 0), ident, +1)
        add(r0, (shift(z, 0), 1), Z[(z, 0)] if cov else ident, +1)
        add(r0, (shift(z, 1), 0), Z[(z, 1)] if cov else ident, -1)
        add(r0, (z, 1), ident, -1)
    return M


def gram(M):
    """M^T M, exact integers."""
    n, m = len(M), len(M[0])
    cols = [[M[r][c] for r in range(n)] for c in range(m)]
    return [[sum(cols[i][r] * cols[j][r] for r in range(n)) for j in range(m)] for i in range(m)]


def cogram(M):
    """M M^T, exact integers (acts on the domain of M^T)."""
    return gram(mT(M))


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def nz(A):
    return sum(1 for r in A for v in r if v != 0)


def colnorm2(A, c):
    return sum(A[r][c] ** 2 for r in range(len(A)))


def run(Adg, tag):
    dim, Z, G = build(Adg)
    # hr1-D' : flatness, from the 1-form differential's own data
    nonflat = 0
    for z in PLAQ:
        U1 = mm(Z[(z, 0)], Z[(shift(z, 0), 1)])
        U2 = mm(Z[(z, 1)], Z[(shift(z, 1), 0)])
        if not iszero(msub(U1, U2)):
            nonflat += 1
    Wcov, Wflat = gram(d12(Z, dim, True)), gram(d12(Z, dim, False))
    EW = msub(Wcov, Wflat)                      # Wilson block on 1-forms
    Ccov, Cflat = cogram(d01(Z, dim, True)), cogram(d01(Z, dim, False))
    EH = msub([[Wcov[i][j] + Ccov[i][j] for j in range(len(Wcov))] for i in range(len(Wcov))],
              [[Wflat[i][j] + Cflat[i][j] for j in range(len(Wflat))] for i in range(len(Wflat))])
    best = max(range(len(EW[0])), key=lambda c: colnorm2(EW, c)) if EW else 0
    w2 = colnorm2(EW, best)
    f2 = colnorm2(Wflat, best)
    print("[%s] dim=%d T=%d" % (tag, dim, T))
    print("    hr1-D' non-flat plaquettes              : %d of %d" % (nonflat, len(PLAQ)))
    print("    hr1-A' nonzero entries of E_W (1-forms) : %d" % nz(EW))
    print("    hr1-A' witness |E_W u|^2                : %d  (u = basis 1-form #%d)" % (w2, best))
    print("    hr1-C4' same u, |(d^*d) u|^2            : %d" % f2)
    print("    hr1-A'' nonzero entries of E_H          : %d" % nz(EH))
    return nz(EW), nz(EH), nonflat, w2, f2


print("=" * 78)
print("hr1-A'/A'' MAIN  -- nonabelian pure gauge, G(y) = g^{y1}, Ad_g = quarter turn")
m = run(R3, "MAIN")
print()
print("hr1-C1' CONTROL -- constant gauge (E_W and E_H must both be 0)")
c1 = run(I3, "C1'")
print()
print("hr1-C2' CONTROL -- abelian, Ad == 1 (E_W and E_H must both be 0)")
c2 = run(I1, "C2'")
print()
print("=" * 78)
print("VERDICTS against the AMENDMENT in checks/hr1_criteria.md")
print("  hr1-D'  : %s (%d non-flat plaquettes)" % ("PASS" if m[2] == 0 else "FAIL", m[2]))
print("  hr1-A'  : %s  (E_W %s 0 at exactly zero curvature; witness %d vs flat %d)"
      % ("PASS (route survives)" if m[0] == 0 else "FAIL (route refuted)",
         "==" if m[0] == 0 else "!=", m[3], m[4]))
print("  hr1-A'' : %s  (E_H %s 0)"
      % ("PASS (route survives)" if m[1] == 0 else "FAIL (route refuted)",
         "==" if m[1] == 0 else "!="))
print("  hr1-C1' : %s (E_W=%d, E_H=%d)"
      % ("FIRED" if (c1[0] == 0 and c1[1] == 0) else "DID NOT FIRE", c1[0], c1[1]))
print("  hr1-C2' : %s (E_W=%d, E_H=%d)"
      % ("FIRED" if (c2[0] == 0 and c2[1] == 0) else "DID NOT FIRE", c2[0], c2[1]))
print("  hr1-C4' : %s (|(d^*d)u|^2 = %d > 0 required)"
      % ("FIRED" if m[4] > 0 else "DID NOT FIRE", m[4]))
