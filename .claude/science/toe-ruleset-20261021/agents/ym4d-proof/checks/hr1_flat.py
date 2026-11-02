#!/usr/bin/env python3
# checks/hr1_flat.py  --  exact integer test of the (HESS-rel) currency claim.
# Criteria: checks/hr1_criteria.md (written BEFORE this file existed).
# Pure python, exact integer arithmetic only.  No numpy, no BLAS, no lock.

T = 8  # torus side; 8 | T is needed for G(y) = g^{y1} to be periodic with Ad_g a quarter turn

I3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
R3 = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]        # Ad_g, quarter turn about axis 3 (order 4)
I1 = [[1]]                                     # abelian: Ad is trivial on a 1-dim algebra


def mm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def mT(A):
    return [list(r) for r in zip(*A)]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mpow(A, e):
    n = len(A)
    out = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for _ in range(e):
        out = mm(out, A)
    return out


def iszero(A):
    return all(all(v == 0 for v in r) for r in A)


def sites():
    return [(a, b) for a in range(T) for b in range(T)]


def build(Adg, curved=False):
    """Return (dim, Z, G) for the pure-gauge background Z(b)=G(y)G(y')^-1, G(y)=Adg^{y1}.
    curved=True perturbs one link so the configuration is no longer flat."""
    dim = len(Adg)
    G = {y: mpow(Adg, y[0]) for y in sites()}
    Z = {}
    for y in sites():
        for mu in (0, 1):
            yp = ((y[0] + 1) % T, y[1]) if mu == 0 else (y[0], (y[1] + 1) % T)
            Z[(y, mu)] = mm(G[y], mT(G[yp]))          # G orthogonal integer => inverse = transpose
    if curved:
        Z[((0, 0), 1)] = Adg                           # break flatness at one link
    return dim, Z, G


def plaq_U1_U2(Z, y):
    """U_1, U_2 of BFT_B (41.1) at the plaquette based at y with mu=0 < nu=1."""
    y_mu = ((y[0] + 1) % T, y[1])
    y_nu = (y[0], (y[1] + 1) % T)
    U1 = mm(Z[(y, 0)], Z[(y_mu, 1)])
    U2 = mm(Z[(y, 1)], Z[(y_nu, 0)])
    return U1, U2


def d_matrix(Z, dim, covariant):
    """Explicit integer matrix of d (covariant=False) or d_Z (covariant=True),
    from 0-forms (sites x dim) to 1-forms (links x dim).
    (d_Z lam)(b) = Z(b) lam(y') - lam(y),  b = (y -> y')."""
    S = sites()
    sidx = {y: i for i, y in enumerate(S)}
    links = [(y, mu) for y in S for mu in (0, 1)]
    lidx = {b: i for i, b in enumerate(links)}
    nrow, ncol = len(links) * dim, len(S) * dim
    M = [[0] * ncol for _ in range(nrow)]
    for b in links:
        y, mu = b
        yp = ((y[0] + 1) % T, y[1]) if mu == 0 else (y[0], (y[1] + 1) % T)
        A = Z[b] if covariant else [[1 if i == j else 0 for j in range(dim)] for i in range(dim)]
        r0, cY, cYp = lidx[b] * dim, sidx[y] * dim, sidx[yp] * dim
        for i in range(dim):
            M[r0 + i][cY + i] -= 1
            for j in range(dim):
                M[r0 + i][cYp + j] += A[i][j]
    return M


def gram(M):
    """M^T M as an exact integer matrix."""
    n, m = len(M), len(M[0])
    cols = [[M[r][c] for r in range(n)] for c in range(m)]
    return [[sum(cols[i][r] * cols[j][r] for r in range(n)) for j in range(m)] for i in range(m)]


def run(Adg, curved, tag):
    dim, Z, G = build(Adg, curved)
    # hr1-D : flatness precondition
    nonflat = [y for y in sites() if not iszero(msub(*plaq_U1_U2(Z, y)))]
    # hr1-A : the currency gate
    Lflat = gram(d_matrix(Z, dim, covariant=False))
    Lcov = gram(d_matrix(Z, dim, covariant=True))
    E = msub(Lcov, Lflat)
    Enz = sum(1 for r in E for v in r if v != 0)
    # witness: the standard basis vector maximising |E lam|^2
    best = (0, None)
    for c in range(len(E[0])):
        v = sum(E[r][c] ** 2 for r in range(len(E)))
        if v > best[0]:
            best = (v, c)
    w2, wc = best
    fw2 = sum(Lflat[r][wc] ** 2 for r in range(len(Lflat))) if wc is not None else 0
    # hr1-B : the two defects of BFT_B 41.2
    b1 = [y for y in sites() if not iszero(msub(*plaq_U1_U2(Z, y)))]
    b2 = []
    for y in sites():
        for mu in (0, 1):
            y1 = ((y[0] + 1) % T, y[1]) if mu == 0 else (y[0], (y[1] + 1) % T)
            y2 = ((y[0] + 2) % T, y[1]) if mu == 0 else (y[0], (y[1] + 2) % T)
            Row = mm(Z[(y, mu)], Z[(y1, mu)])          # straight level-l row, L = 2
            Zup = mm(G[y], mT(G[y2]))                  # the level-(l+1) link of the tower
            if not iszero(msub(Row, Zup)):
                b2.append((y, mu))
    print("[%s] dim=%d  T=%d  curved=%s" % (tag, dim, T, curved))
    print("    hr1-D non-flat plaquettes          : %d of %d" % (len(nonflat), T * T))
    print("    hr1-A nonzero entries of E         : %d  (E = d_Z^T d_Z - d^T d)" % Enz)
    print("    hr1-A witness |E lam|^2            : %s   (lam = standard basis vector #%s)" % (w2, wc))
    print("    hr1-C4 same lam, |(d^T d) lam|^2   : %s" % fw2)
    print("    hr1-B B1 defect nonzero at         : %d plaquettes" % len(b1))
    print("    hr1-B B2 defect nonzero at         : %d (site, direction) pairs" % len(b2))
    return Enz, len(b1), len(b2), len(nonflat)


print("=" * 78)
print("hr1 : MAIN  -- nonabelian pure gauge, G(y) = g^{y1}, Ad_g = quarter turn")
main = run(R3, False, "MAIN")
print()
print("hr1-C1 : CONTROL -- constant gauge G == 1 (E must be 0)")
c1 = run(I3, False, "C1")
print()
print("hr1-C2 : CONTROL -- abelian, Ad == 1 on a 1-dim algebra (E must be 0)")
c2 = run(I1, False, "C2")
print()
print("hr1-C3 : CONTROL -- curved background (B1 defect must be NONZERO)")
c3 = run(R3, True, "C3")
print()
print("=" * 78)
print("VERDICTS against checks/hr1_criteria.md")
print("  hr1-D  : %s  (flat precondition: %d non-flat plaquettes in MAIN)"
      % ("PASS" if main[3] == 0 else "FAIL", main[3]))
print("  hr1-A  : %s  (E %s 0 at exactly zero curvature)"
      % ("PASS (route survives)" if main[0] == 0 else "FAIL (route refuted)",
         "==" if main[0] == 0 else "!="))
print("  hr1-B  : %s  (B1 nonzero at %d plaquettes, B2 at %d pairs, E nonzero entries %d)"
      % ("PASS" if (main[1] or main[2]) else "FAIL (extension does not hold)",
         main[1], main[2], main[0]))
print("  hr1-C1 : %s  (control fires iff E == 0; got %d nonzero entries)"
      % ("FIRED" if c1[0] == 0 else "DID NOT FIRE", c1[0]))
print("  hr1-C2 : %s  (control fires iff E == 0; got %d nonzero entries)"
      % ("FIRED" if c2[0] == 0 else "DID NOT FIRE", c2[0]))
print("  hr1-C3 : %s  (control fires iff B1 != 0; got %d plaquettes)"
      % ("FIRED" if c3[1] > 0 else "DID NOT FIRE", c3[1]))
