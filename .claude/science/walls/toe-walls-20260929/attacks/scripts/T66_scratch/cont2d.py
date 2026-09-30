"""2D continuum ADM reference pieces (fields depend on x,y; sector h_xx,h_yy,h_zz,h_xy) and a numeric-jet check of the
degree-2 hypersurface-deformation identity. K = alpha = 1."""
import sympy as sp, random, pickle, itertools
x, y, s = sp.symbols('x y s')
F_ = lambda n: sp.Function(n)(x, y)
hxx, hyy, hzz, hxy = [F_(n) for n in ('hxx', 'hyy', 'hzz', 'hxy')]
Pxx, Pyy, Pzz, Pxy = [F_(n) for n in ('Pxx', 'Pyy', 'Pzz', 'Pxy')]
N, M, XIx, XIy = [F_(n) for n in ('N', 'M', 'xix', 'xiy')]
FIELDS_H = [hxx, hyy, hzz, hxy]
FIELDS_P = [Pxx, Pyy, Pzz, Pxy]
K = sp.Integer(1); al = sp.Integer(1)
coords = [x, y, sp.Symbol('z')]


def trunc(e, order):
    e = sp.expand(e)
    return sum(e.coeff(s, k) * s ** k for k in range(order + 1))


def build_pieces(order=2):
    q = sp.Matrix([[1 + s * hxx, s * hxy, 0], [s * hxy, 1 + s * hyy, 0], [0, 0, 1 + s * hzz]])
    hmat = (q - sp.eye(3)) / s
    hmat = sp.simplify(hmat)
    # truncated inverse: I - s h + s^2 h^2 - s^3 h^3
    hm = sp.Matrix([[hxx, hxy, 0], [hxy, hyy, 0], [0, 0, hzz]])
    qinv = sp.eye(3) - s * hm + s ** 2 * hm * hm - s ** 3 * hm ** 3
    qinv = qinv.applyfunc(lambda e: trunc(e, 3))
    def dq(a, b, c):
        return sp.diff(q[a, b], coords[c])
    def Gam(a, b, c):
        return trunc(sum(qinv[a, d] * (dq(d, b, c) + dq(d, c, b) - dq(b, c, d)) for d in range(3)) / 2, 3)
    G = [[[Gam(a, b, c) for c in range(3)] for b in range(3)] for a in range(3)]
    def Riem(a, b, c, d):
        r = sp.diff(G[a][b][d], coords[c]) - sp.diff(G[a][b][c], coords[d])
        r += sum(G[a][c][e] * G[e][b][d] - G[a][d][e] * G[e][b][c] for e in range(3))
        return trunc(r, 3)
    Ric = sp.Matrix(3, 3, lambda b, d: trunc(sum(Riem(a, b, a, d) for a in range(3)), 3))
    Rs = trunc(sum(qinv[b, d] * Ric[b, d] for b in range(3) for d in range(3)), 3)
    trh = s * (hxx + hyy + hzz)
    tr_hh = s ** 2 * (hxx ** 2 + hyy ** 2 + hzz ** 2 + 2 * hxy ** 2)
    sqrtq = 1 + trh / 2 + (trh ** 2 / 8 - tr_hh / 4) + 0 * s ** 3   # order-2 accuracy (enough for V1,V2)
    sgR = trunc(sqrtq * Rs, order)
    V1 = sgR.coeff(s, 1); V2 = sgR.coeff(s, 2)
    # kinetic
    pi_ = sp.Matrix([[Pxx, Pxy / 2, 0], [Pxy / 2, Pyy, 0], [0, 0, Pzz]]) * s
    t1 = (q * pi_ * q * pi_).trace()
    t2 = (q * pi_).trace() ** 2
    # 1/sqrt(det q) series to order 1 (need T up to s^3: T ~ s^2 * (...) so 1/sqrt q to order s^1)
    invsq = 1 - trh / 2
    T = trunc((t1 - t2 / 2) * invsq / (4 * al), 3)
    T2 = T.coeff(s, 2); T3 = T.coeff(s, 3)
    return dict(V1=sp.expand(V1), V2=sp.expand(V2), T2=sp.expand(T2), T3=sp.expand(T3))


def lie_G(xi):
    """generator density G[xi] = P^{ij} L_xi q_ij with q = 1 + h (no truncation; polynomial)."""
    xx_, xy_ = xi
    d = lambda f, v: sp.diff(f, v)
    qxx, qyy, qzz, qxy = 1 + hxx, 1 + hyy, 1 + hzz, hxy
    def adv(f): return xx_ * d(f, x) + xy_ * d(f, y)
    Lxx = adv(hxx) + 2 * (qxx * d(xx_, x) + qxy * d(xy_, x))
    Lyy = adv(hyy) + 2 * (qyy * d(xy_, y) + qxy * d(xx_, y))
    Lzz = adv(hzz)
    Lxy = adv(hxy) + qxy * d(xx_, x) + qyy * d(xy_, x) + qxx * d(xx_, y) + qxy * d(xy_, y)
    return Pxx * Lxx + Pyy * Lyy + Pzz * Lzz + Pxy * Lxy


def structure_function():
    """xi^j = (K/4a) q^{jk} (d_k N M - N d_k M), q^{jk} inverse of the xy block to first order in h."""
    gx = (sp.diff(N, x) * M - N * sp.diff(M, x))
    gy = (sp.diff(N, y) * M - N * sp.diff(M, y))
    K4 = K / (4 * al)
    xi0 = (K4 * gx, K4 * gy)
    xi1 = (-K4 * (hxx * gx + hxy * gy), -K4 * (hxy * gx + hyy * gy))
    return xi0, xi1


def EL(L, f, nmax=3):
    tot = 0
    for a in range(nmax + 1):
        for b in range(nmax + 1 - a):
            if a == 0 and b == 0:
                var = f
            else:
                args = []
                if a: args.append((x, a))
                if b: args.append((y, b))
                var = sp.Derivative(f, *args)
            term = sp.diff(L, var)
            if a or b:
                dargs = []
                if a: dargs.append((x, a))
                if b: dargs.append((y, b))
                term = sp.diff(term, *dargs)
            tot += (-1) ** (a + b) * term
    return tot


def PB(A, B):
    return sum(EL(A, hh) * EL(B, pp) - EL(A, pp) * EL(B, hh) for hh, pp in zip(FIELDS_H, FIELDS_P))


def degpart(e, d):
    sc = sp.Symbol('sc')
    sub = {f: sc * f for f in FIELDS_H + FIELDS_P}
    return sp.expand(e.subs(sub, simultaneous=True).doit()).coeff(sc, d)


def check_identity(pieces, jets_seed=11):
    V1, V2, T2, T3 = pieces['V1'], pieces['V2'], pieces['T2'], pieces['T3']
    piece = {1: K * V1, 2: T2 + K * V2, 3: T3}
    br2 = 0
    for i in (1, 2, 3):
        j = 4 - i
        br2 += PB(N * piece[i], M * piece[j])
    xi0, xi1 = structure_function()
    G2 = degpart(sp.expand(lie_G(xi0)), 2) if False else None
    # degree-2 GR side: G2[xi0] (P h terms of the Lie-derivative generator at xi0) + G1[xi1]
    G_xi0 = sp.expand(lie_G(xi0))
    G_xi1 = sp.expand(lie_G(xi1))
    rhs = degpart(G_xi0, 2) + degpart(G_xi1, 2)
    diff = sp.expand(br2 - rhs)
    random.seed(jets_seed)
    def rp():
        return sum(sp.Rational(random.randint(-3, 3), random.randint(1, 3)) * x ** i * y ** j for i in range(3) for j in range(3) if i + j <= 3)
    jets = {f: rp() for f in FIELDS_H + FIELDS_P + [N, M]}
    pt = {x: sp.Rational(1, 3), y: sp.Rational(1, 5)}
    vals = []
    for f in FIELDS_H + FIELDS_P:
        e = EL(diff, f).subs(jets).doit().subs(pt)
        vals.append(sp.nsimplify(e))
    ref = []
    for f in FIELDS_H + FIELDS_P:
        e = EL(br2, f).subs(jets).doit().subs(pt)
        ref.append(sp.nsimplify(e))
    return vals, ref


if __name__ == '__main__':
    import time
    t0 = time.time()
    pieces = build_pieces()
    print("pieces built", round(time.time() - t0, 1), "s")
    for k, v in pieces.items():
        print(k, len(sp.Add.make_args(v)))
    pickle.dump(pieces, open('cont2d_pieces.pkl', 'wb'))
    vals, ref = check_identity(pieces)
    print("EL residual (should be all 0):", vals)
    print("EL of bracket (nonvacuity, nonzero):", ref[:3])
    print("secs", round(time.time() - t0, 1))
