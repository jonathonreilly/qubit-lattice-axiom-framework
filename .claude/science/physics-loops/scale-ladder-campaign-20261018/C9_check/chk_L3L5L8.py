#!/usr/bin/env python3
"""C9 fresh-context check: L3 sign convention, L5 frame construction, L8 enlarged generator sets.
New code; imports nothing from the C9 runner.  Exact (sympy rationals, Groebner over QQ)."""
import sys, time, itertools, random
import sympy as sp

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}"); sys.stdout.flush()

def nbar(n, L):
    n %= L
    return n - L if n > L // 2 else n

def vbracket(V, W, xs):
    return [sp.expand(sum(V[j] * sp.diff(W[i], xs[j]) - W[j] * sp.diff(V[i], xs[j]) for j in range(len(xs))))
            for i in range(len(xs))]

# ------------------------------------------------------------------ L3 sign of the linearisation
def l3_sign():
    n = 3
    x = sp.symbols("x0:3")
    rnd = random.Random(3)
    A = sp.Matrix(n, n, lambda i, j: rnd.randint(-3, 3))
    B = sp.Matrix(n, n, lambda i, j: rnd.randint(-3, 3))
    X = sp.Matrix(x)
    VA = list(A * X); VB = list(B * X)
    br = sp.Matrix(vbracket(VA, VB, x))
    jac = br.jacobian(X)
    check("L3_linearisation_sign", jac == -(A * B - B * A) and jac != (A * B - B * A),
          "for linear fields V_A = (Ax).d: D[V_A,V_B] = -[A,B]; so [A_a,A_b] = -cbar(a,b) A_(a+b) "
          "(C9 writes +cbar; harmless: c -> -c preserves (S) and every ratio Lam_n/Lam_1)")

# ------------------------------------------------------------------ L5 frame construction
def l5(L, seed):
    rnd = random.Random(seed)
    cb = {}
    for a in range(L):
        for b in range(L):
            if a < b:
                cb[(a, b)] = sp.Rational(rnd.randint(-9, 9), rnd.randint(1, 5))
    cb[(0, 1)] = sp.Integer(-1)          # c(1,0) = 1 ... we set Lam_1 = c(0,1) = 1 below
    cb[(0, 1)] = sp.Integer(1); cb[(0, 2)] = sp.Integer(2)
    if L > 2: cb[(1, L - 1)] = sp.Integer(3)
    def c(a, b):
        a %= L; b %= L
        if a == b: return 0
        return cb[(a, b)] if a < b else -cb[(b, a)]
    u = sp.symbols(f"u0:{L}")
    F = sp.zeros(L, L)
    for a in range(L):
        F[a, a] += 1
        for k in range(L):
            F[a, (a + k) % L] -= sp.Rational(1, 2) * c(a, k) * u[k]
    V = [list(F.row(a)) for a in range(L)]
    Finv = F.inv()   # rational; frame wherever det F != 0 (det F(0) = 1)
    C = {}
    for a in range(L):
        for b in range(L):
            B = sp.Matrix([vbracket(V[a], V[b], u)])
            C[(a, b)] = (B * Finv).applyfunc(sp.cancel)
    z0 = {v: 0 for v in u}
    ok0 = all(sp.simplify(C[(a, b)][e].subs(z0) - (c(a, b) if e == (a + b) % L else 0)) == 0
              for a in range(L) for b in range(L) for e in range(L))
    # covariance: grade u_k by -k, d_m by +m; then C_ab^e has momentum (a+b-e): check monomial degrees
    cov = True
    for (a, b), row in C.items():
        for e in range(L):
            num, den = sp.fraction(sp.together(row[e]))
            for poly in (sp.Poly(num, *u), sp.Poly(den, *u)):
                pass
            # check at a T-transformed point: C(T^-1 u) = w^(a+b-e) C(u)  with u_k -> w^(k) u_k ; use L-th root symbolically
    # instead test covariance numerically-exactly with w a primitive root realised as companion: use degree bookkeeping
    def mom(expr):
        # momentum of each monomial: sum over -k * exponent(u_k) mod L ; returns set
        p = sp.Poly(sp.expand(expr), *u)
        return {(-sum(k * m[k] for k in range(L))) % L for m in p.monoms()}
    for (a, b), row in C.items():
        for e in range(L):
            num, den = sp.fraction(sp.together(row[e]))
            if num == 0: continue
            mn, md = mom(num), mom(den)
            if len(mn) != 1 or len(md) != 1 or (list(mn)[0] - list(md)[0] - (a + b - e)) % L != 0:
                cov = False
    # Jacobi identity with structure functions at a random rational point and L2 at 0
    jac_nonzero = any(sum(c(x, y) * c(x + y, z) for (x, y, z) in [(a, b, cc), (b, cc, a), (cc, a, b)]) != 0
                      for a, b, cc in itertools.product(range(L), repeat=3))
    l2 = True
    for a, b, cc in itertools.product(range(L), repeat=3):
        e = (a + b + cc) % L
        jac = sum(c(x, y) * c(x + y, z) for (x, y, z) in [(a, b, cc), (b, cc, a), (cc, a, b)])
        der = sum(sp.diff(C[(x, y)][e], u[z]).subs(z0) for (x, y, z) in [(a, b, cc), (b, cc, a), (cc, a, b)])
        if sp.simplify(jac - der) != 0: l2 = False
    check(f"L5_frame_L{L}", ok0 and cov and l2 and jac_nonzero,
          f"V_a = d_a - (1/2) sum_k cbar(a,k) u_k d_(a+k): C(0) = cbar (Lam_1 = 1, Lam_2 = 2), C rational and "
          f"T-covariant (monomial momenta), L2 identity holds, Jac(cbar) != 0")

# ------------------------------------------------------------------ L8
def sl2_semidirect(L):
    """sl2 |x V_(L-1) as (L+2)x(L+2) affine matrices; returns basis list [(name, mom, matrix)]"""
    m = L - 1
    dimV = m + 1
    # V_m basis w_k (k=0..m), weight m-2k ; H w_k=(m-2k)w_k, F w_k=(k+1)w_(k+1), E w_k=(m-k+1)w_(k-1)
    def rho(which):
        M = sp.zeros(dimV, dimV)
        for k in range(dimV):
            if which == "H": M[k, k] = m - 2 * k
            if which == "F" and k + 1 < dimV: M[k + 1, k] = k + 1
            if which == "E" and k - 1 >= 0: M[k - 1, k] = m - k + 1
        return M
    N = dimV + 1
    def emb(M=None, v=None):
        A = sp.zeros(N, N)
        if M is not None: A[:dimV, :dimV] = M
        if v is not None: A[v, dimV] = 1
        return A
    basis = [("D", 0, emb(rho("H") / 2)), ("E", 1, emb(rho("E"))), ("F", L - 1, emb(rho("F")))]
    for k in range(dimV):
        j = (m - 2 * k) // 2          # weight 2j ; momentum j mod L
        basis.append((f"v{j}", j % L, emb(v=k)))
    return basis

def decompose(Mat, basis):
    syms = sp.symbols(f"a0:{len(basis)}")
    expr = Mat - sum((s * b[2] for s, b in zip(syms, basis)), sp.zeros(*Mat.shape))
    sol = sp.solve(list(expr), syms, dict=True)
    if not sol: return None
    return [sol[0].get(s, 0) for s in syms]

def l8_sufficiency(L):
    basis = sl2_semidirect(L)
    graded = True
    for (n1, m1, A), (n2, m2, B) in itertools.product(basis, repeat=2):
        co = decompose(A * B - B * A, basis)
        if co is None: graded = False; continue
        for cf, (n3, m3, _) in zip(co, basis):
            if cf != 0 and m3 != (m1 + m2) % L: graded = False
    D = basis[0][2]
    # X_n := D, E, F at 0, +-1 ; v_n at other momenta
    X = {0: basis[0], 1: basis[1], L - 1: basis[2]}
    for b in basis[3:]:
        if b[1] not in X: X[b[1]] = b
    lam = {}
    for n, (nm, mo, A) in X.items():
        co = decompose(D * A - A * D, basis)
        idx = [b[0] for b in basis].index(nm)
        lam[n] = co[idx] if all((cf == 0) or (i == idx) for i, cf in enumerate(co)) else None
    spec = all(lam[n] == nbar(n, L) for n in range(L))
    EF = decompose(basis[1][2] * basis[2][2] - basis[2][2] * basis[1][2], basis)
    Sprime = EF[0] == 2 and all(cf == 0 for cf in EF[1:])
    dims = {n: sum(1 for b in basis if b[1] == n) for n in range(L)}
    # span G not closed: [F, X_2] has a component on v_1 (the extra at momentum 1)
    co = decompose(basis[2][2] * X[2][2] - X[2][2] * basis[2][2], basis)
    names = [b[0] for b in basis]
    not_closed = co[names.index("v1")] != 0
    check(f"L8_sl2xV_L{L}", graded and spec and Sprime and not_closed and dims[0] == dims[1] == dims[L - 1] == 2,
          f"affine-matrix realisation (Jacobi automatic): Z_L-graded, dims {dims}, [E,F] = 2D, Lam_n = nbar Lam_1 "
          f"for all n, span G not a subalgebra")

def l8_literalS_breaks_i():
    """D |x (Heisenberg-like): basis D, Z (mom 0), X_n n != 0; [D,X_n] = Lam_n X_n, [X_1,X_-1] = Z; rest 0.
    Lam_2 = 1/3 (with Lam_1 = 1): literal (S) holds and corollary (i) fails."""
    L = 5
    Lam = {1: 1, 4: -1, 2: sp.Rational(1, 3), 3: sp.Rational(-7, 5)}
    names = ["D", "Z"] + [f"X{n}" for n in range(1, L)]
    idx = {nm: i for i, nm in enumerate(names)}
    def br(i, j):
        out = [0] * len(names)
        a, b = names[i], names[j]
        if a == "D" and b.startswith("X"): out[j] = Lam[int(b[1:])]
        if b == "D" and a.startswith("X"): out[i] = -Lam[int(a[1:])]
        if a == "X1" and b == f"X{L-1}": out[idx["Z"]] = 1
        if b == "X1" and a == f"X{L-1}": out[idx["Z"]] = -1
        return out
    def brv(x, y):
        out = [0] * len(names)
        for i, xi in enumerate(x):
            if xi == 0: continue
            for j, yj in enumerate(y):
                if yj == 0: continue
                r = br(i, j)
                out = [o + xi * yj * rr for o, rr in zip(out, r)]
        return out
    e = lambda i: [1 if k == i else 0 for k in range(len(names))]
    ok = True
    for i, j, k in itertools.product(range(len(names)), repeat=3):
        s = [p + q + r for p, q, r in zip(brv(brv(e(i), e(j)), e(k)), brv(brv(e(j), e(k)), e(i)), brv(brv(e(k), e(i)), e(j)))]
        if any(v != 0 for v in s): ok = False
    check("L8_literalS_no_(i)", ok, "enlarged by one central Z at momentum 0: Jacobi exact, literal (S) "
          "([X_1,X_-1] = Z != 0, Lam_1 = 1) with Lam_2 = 1/3: corollary (i) fails without (S')")

def l8_necessity(extra, L=5, lam2=2):
    """General Z_L-graded algebra: basis D (mom 0), X_n (n != 0), plus extra generators at the momenta in
    `extra`.  Unknown structure constants respecting the grading; impose [D,X_1] = X_1, X_(-1) and X_2
    ad_D-eigenvectors, [D,X_2] = lam2 X_2, (S'): [X_1,X_-1] = c D, t c = 1; Jacobi on all basis triples."""
    basis = [("D", 0), ] + [(f"X{n}", n) for n in range(1, L)] + [(f"Y{n}", n) for n in extra]
    nb = len(basis)
    var = []
    cst = {}
    for i, j in itertools.combinations(range(nb), 2):
        mom = (basis[i][1] + basis[j][1]) % L
        for k in range(nb):
            if basis[k][1] == mom:
                s = sp.Symbol(f"c_{i}_{j}_{k}"); var.append(s); cst[(i, j, k)] = s
    def C(i, j, k):
        if i == j: return 0
        if i < j: return cst.get((i, j, k), 0)
        return -cst.get((j, i, k), 0)
    names = [b[0] for b in basis]
    I = {nm: i for i, nm in enumerate(names)}
    eqs = []
    t = sp.Symbol("t")
    # ad_D on X_1, X_-1, X_2: eigenvectors
    for nm, val in (("X1", 1), (f"X{L-1}", None), ("X2", lam2)):
        j = I[nm]
        for k in range(nb):
            if k == j:
                if val is not None: eqs.append(C(0, j, k) - val)
            else:
                eqs.append(C(0, j, k))
    # (S'): [X_1, X_-1] = c D with no other component
    for k in range(nb):
        if k != 0: eqs.append(C(I["X1"], I[f"X{L-1}"], k))
    eqs.append(t * C(I["X1"], I[f"X{L-1}"], 0) - 1)
    for i, j, k in itertools.combinations(range(nb), 3):
        for l in range(nb):
            e = 0
            for (x, y, z) in [(i, j, k), (j, k, i), (k, i, j)]:
                e += sum(C(x, y, m) * C(m, z, l) for m in range(nb))
            e = sp.expand(e)
            if e != 0: eqs.append(e)
    eqs = [e for e in eqs if e != 0]
    return eqs, var + [t], basis

def l8_necessity_checks():
    for extra, lam2, expect_incons, label in [((0,), 2, True, "extra at 0"),
                                               ((1, 4), 2, True, "extras at +-1"),
                                               ((0, 1), 2, True, "extras at 0, 1"),
                                               ((0,), sp.Rational(-1, 2), False, "control extra at 0, Lam_2 = -1/2")]:
        t0 = time.time()
        eqs, var, basis = l8_necessity(extra, lam2=lam2)
        G = sp.groebner(eqs, *var, order="grevlex")
        incons = list(G.exprs) == [1]
        check(f"L8_necessity_{label.replace(' ', '_')}", incons == expect_incons,
              f"L = 5, (S') + [D,X_2] = {lam2} X_2 + Jacobi: Groebner {'[1]' if incons else 'not [1]'} "
              f"({len(var)} vars, {time.time()-t0:.1f}s)")
    # control: sl2 |x V_4 with extras at 0, +-1 satisfies the same equation generator with Lam_2 = 2
    L = 5
    eqs, var, basis = l8_necessity((0, 1, 4), lam2=2)
    sb = sl2_semidirect(L)
    # map: D->D, X1->E, X4->F, X2->v2, X3->v(-2), Y0->v0, Y1->v1, Y4->v(-1)
    mp = {"D": "D", "X1": "E", "X4": "F", "X2": "v2", "X3": "v-2", "Y0": "v0", "Y1": "v1", "Y4": "v-1"}
    sbd = {b[0]: b for b in sb}
    mats = [sbd[mp[nm]][2] for nm, _ in basis]
    subs = {}
    for v in var:
        if v.name == "t": continue
        _, i, j, k = v.name.split("_"); i, j, k = int(i), int(j), int(k)
        co = decompose(mats[i] * mats[j] - mats[j] * mats[i], [(nm, mo, M) for (nm, mo), M in zip(basis, mats)])
        subs[v] = co[k]
    cDval = subs[[v for v in var if v.name == f"c_{1}_{4}_0"][0]]
    subs[sp.Symbol("t")] = 1 / sp.Integer(cDval)
    ok = all(sp.simplify(e.subs(subs)) == 0 for e in eqs)
    check("L8_necessity_control", ok, "sl2 |x V_4 (extras at 0, +-1) satisfies the same equation generator with Lam_2 = 2")

if __name__ == "__main__":
    l3_sign()
    for L, s in ((4, 1), (5, 2)):  # L = 6 symbolic inverse too slow in sympy; zeroth order is analytic
        t0 = time.time(); l5(L, s); print(f"   ({time.time()-t0:.1f}s)")
    for L in (5, 7, 9):
        l8_sufficiency(L)
    l8_literalS_breaks_i()
    l8_necessity_checks()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
