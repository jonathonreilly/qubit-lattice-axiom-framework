"""hg55_4 -- (library code identical to hg55_3; new run())  hg55_3 -- Lemma SG's identity and Lemma NC3 (no cubic term in the w-chart) on the lane's soft density at N = 3.

phi_hat(M;V) = Re tr(W_0^{-1}M) - Re tr(V^{-1}M), W_0 = e^{X_0}, X_0 the NA-alg (a) fixed point (computed as an exact
power series).  d = 2, L = 3 (18 S4' words).  Exact truncated series in eps (through eps^K) with dual numbers (t^2 = 0);
3x3 Gaussian-rational matrices.  Criteria: checks/hg55_3_criteria.md (written first).  No floats.
"""
import itertools
import random
import sys
from fractions import Fraction as F

K = 4
NN = 3
D = 2
L = 3
O = (L - 1) // 2
MU = 0
Z0 = (F(0), F(0))
ONE = (F(1), F(0))


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def csub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cconj(a):
    return (a[0], -a[1])


def mzero():
    return tuple([Z0] * (NN * NN))


def mid():
    return tuple(ONE if i == j else Z0 for i in range(NN) for j in range(NN))


MZ = mzero()
MI = mid()


def madd(A, B):
    return tuple(cadd(x, y) for x, y in zip(A, B))


def msub(A, B):
    return tuple(csub(x, y) for x, y in zip(A, B))


def mscal(r, A):
    return tuple((r * x[0], r * x[1]) for x in A)


def mmul(A, B):
    out = []
    for i in range(NN):
        for j in range(NN):
            s = Z0
            for k in range(NN):
                a = A[i * NN + k]
                b = B[k * NN + j]
                if a == Z0 or b == Z0:
                    continue
                s = cadd(s, cmul(a, b))
            out.append(s)
    return tuple(out)


def mconjT(A):
    return tuple(cconj(A[j * NN + i]) for i in range(NN) for j in range(NN))


def mtrace(A):
    s = Z0
    for i in range(NN):
        s = cadd(s, A[i * NN + i])
    return s


def mPi(A):
    ah = mscal(F(1, 2), msub(A, mconjT(A)))
    t = mtrace(ah)
    return msub(ah, tuple((t[0] / NN, t[1] / NN) if i == j else Z0 for i in range(NN) for j in range(NN)))


def E(i, j):
    return tuple(ONE if (r == i and c == j) else Z0 for r in range(NN) for c in range(NN))


def ci(A):
    return tuple(cmul((F(0), F(1)), x) for x in A)


BASIS = [
    msub(E(0, 1), E(1, 0)), msub(E(0, 2), E(2, 0)), msub(E(1, 2), E(2, 1)),
    ci(madd(E(0, 1), E(1, 0))), ci(madd(E(0, 2), E(2, 0))), ci(madd(E(1, 2), E(2, 1))),
    ci(msub(E(0, 0), E(1, 1))), ci(msub(E(1, 1), E(2, 2))),
]


def vec_to_mat(v):
    out = MZ
    for c, B in zip(v, BASIS):
        if c:
            out = madd(out, mscal(F(c), B))
    return out


# ---------- series (list of K+1 matrices); dual series = (p0, p1) ----------
def s_zero():
    return [MZ] * (K + 1)


def s_const(A):
    s = s_zero()
    s[0] = A
    return s


def s_add(x, y):
    return [madd(a, b) for a, b in zip(x, y)]


def s_sub(x, y):
    return [msub(a, b) for a, b in zip(x, y)]


def s_scal(r, x):
    return [mscal(r, a) for a in x]


def s_mul(x, y):
    z = s_zero()
    for i in range(K + 1):
        if x[i] == MZ:
            continue
        for j in range(K + 1 - i):
            if y[j] == MZ:
                continue
            z[i + j] = madd(z[i + j], mmul(x[i], y[j]))
    return z


def d_add(X, Y):
    return (s_add(X[0], Y[0]), s_add(X[1], Y[1]))


def d_sub(X, Y):
    return (s_sub(X[0], Y[0]), s_sub(X[1], Y[1]))


def d_scal(r, X):
    return (s_scal(r, X[0]), s_scal(r, X[1]))


def d_mul(X, Y):
    return (s_mul(X[0], Y[0]), s_add(s_mul(X[0], Y[1]), s_mul(X[1], Y[0])))


def d_const(A):
    return (s_const(A), s_zero())


def d_exp(A):
    assert A[0][0] == MZ
    res = d_const(MI)
    term = d_const(MI)
    for n in range(1, K + 2):
        term = d_scal(F(1, n), d_mul(term, A))
        res = d_add(res, term)
    return res


def d_log1p(Y):
    # log(1 + Y), Y with zero eps^0 non-dual part
    assert Y[0][0] == MZ
    res = (s_zero(), s_zero())
    powy = d_const(MI)
    for n in range(1, K + 2):
        powy = d_mul(powy, Y)
        res = d_add(res, d_scal(F((-1) ** (n + 1), n), powy))
    return res


def d_conjT(X):
    return ([mconjT(a) for a in X[0]], [mconjT(a) for a in X[1]])


def d_Pi(X):
    return ([mPi(a) for a in X[0]], [mPi(a) for a in X[1]])


def s_retr(x):
    return [mtrace(a)[0] for a in x]


# ---------- contours ----------
def axial_steps(start, end, order):
    steps = []
    cur = list(start)
    for nu in order:
        while cur[nu] != end[nu]:
            if end[nu] > cur[nu]:
                steps.append((tuple(cur), nu, +1))
                cur[nu] += 1
            else:
                steps.append((tuple(cur), nu, -1))
                cur[nu] -= 1
    return steps


def step_letter(step):
    site, nu, sgn = step
    if sgn > 0:
        return ((site, nu), +1)
    lower = list(site)
    lower[nu] -= 1
    return ((tuple(lower), nu), -1)


def contour_letters(order, y):
    cX = tuple([O] * D)
    cY = tuple(cX[i] + (L if i == MU else 0) for i in range(D))
    yL = tuple(y[i] + (L if i == MU else 0) for i in range(D))
    letters = [step_letter(st) for st in axial_steps(cX, y, order)]
    cur = list(y)
    for _ in range(L):
        letters.append(step_letter((tuple(cur), MU, +1)))
        cur[MU] += 1
    for st in reversed(axial_steps(cY, yL, order)):
        link, sgn = step_letter(st)
        letters.append((link, -sgn))
    return letters


CONTOURS = [contour_letters(o, y) for o in itertools.permutations(range(D)) for y in itertools.product(range(L), repeat=D)]
NC = len(CONTOURS)
LINKS = sorted({lk for w in CONTOURS for (lk, _) in w})
QCB = {lk: F(0) for lk in LINKS}
for w in CONTOURS:
    for (lk, s) in w:
        QCB[lk] += F(s, NC)


class Model:
    def __init__(self, Xlink):
        """Xlink: dict link -> non-dual series (list) of the link variable."""
        self.Xlink = Xlink
        self.exps = {}
        for lk in LINKS:
            A = (Xlink[lk], s_zero())
            self.exps[(lk, +1)] = d_exp(A)
            self.exps[(lk, -1)] = d_exp(d_scal(F(-1), A))
        q = s_zero()
        for lk in LINKS:
            q = s_add(q, s_scal(QCB[lk], Xlink[lk]))
        self.Qx = q

    def soft(self, pert_link=None, pert_mat=None, use_maximiser=True):
        def lexp(lk, s):
            if pert_link is not None and lk == pert_link:
                A1 = s_zero()
                A1[0] = pert_mat
                A = (self.Xlink[lk], A1)
                if s < 0:
                    A = d_scal(F(-1), A)
                return d_exp(A)
            return self.exps[(lk, s)]
        Msum = (s_zero(), s_zero())
        Ysum = (s_zero(), s_zero())
        for w in CONTOURS:
            T = d_const(MI)
            for (lk, s) in w:
                T = d_mul(T, lexp(lk, s))
            Msum = d_add(Msum, T)
            Ysum = d_add(Ysum, d_log1p(d_sub(T, d_const(MI))))
        M = d_scal(F(1, NC), Msum)
        Yb = d_scal(F(1, NC), Ysum)
        if use_maximiser:
            Em = d_sub(d_sub(M, d_const(MI)), Yb)
            X = Yb
            for _ in range(K + 3):
                R = d_add(d_sub(d_exp(d_scal(F(-1), X)), d_const(MI)), X)
                Kx = d_add(d_add(R, Em), d_mul(d_sub(R, X), d_add(Yb, Em)))
                X = d_add(Yb, d_Pi(Kx))
        else:
            X = Yb
        return M, Yb, X



def run():
    rng = random.Random(55004)

    def say(*a):
        print(" ".join(str(x) for x in a), flush=True)

    def rsu3(lo=-2, hi=2):
        while True:
            v = [rng.randint(lo, hi) for _ in range(8)]
            if any(v):
                return v

    test_links = [((1, 1), 1), ((2, 1), 0), ((4, 1), 1)]
    for lk in test_links:
        assert lk in QCB
    D1 = D2 = D3 = True
    D4_fires = False
    n1 = 0
    n4fail = 0

    def compare(model, vbase, use_max):
        nonlocal D3
        out = []
        perts = [("link", lk, BASIS[0]) for lk in test_links] + [("link", lk, BASIS[4]) for lk in test_links] + \
                [("v", None, BASIS[0]), ("v", None, BASIS[6])]
        for kind, lk, Amat in perts:
            if kind == "link":
                M, Yb, X = model.soft(pert_link=lk, pert_mat=Amat, use_maximiser=use_max)
                vv = (vbase, s_zero())
            else:
                M, Yb, X = model.soft(use_maximiser=use_max)
                A1 = s_zero()
                A1[0] = Amat
                vv = (vbase, A1)
            W0inv = d_exp(d_scal(F(-1), X))
            G = d_mul(W0inv, M)
            Vinv = d_exp(d_scal(F(-1), vv))
            VM = d_mul(Vinv, M)
            phi1 = [a - b for a, b in zip(s_retr(G[1]), s_retr(VM[1]))]
            W0 = d_exp(X)
            rho = d_log1p(d_sub(d_mul(Vinv, W0), d_const(MI)))
            Theta = d_sub(d_exp((rho[0], s_zero())), d_const(MI))[0]
            V = d_exp(vv)
            Zs = s_mul(Vinv[0], V[1])
            rhs = [a + b for a, b in zip([-x for x in s_retr(s_mul(s_mul(Theta, W0inv[0]), M[1]))],
                                         s_retr(s_mul(s_mul(Zs, Theta), G[0])))]
            out.append((phi1 == rhs, any(c != 0 for c in phi1[1:]), phi1, rhs))
            if use_max:
                stat = d_Pi(d_mul(W0inv, M))
                if any(a != MZ for a in stat[0]) or any(a != MZ for a in stat[1]):
                    D3 = False
                if G[0][1] != MZ:
                    D3 = False
                for a in G[0]:
                    ah = mscal(F(1, 2), msub(a, mconjT(a)))
                    for i in range(NN):
                        for j in range(NN):
                            if i != j and ah[i * NN + j] != Z0:
                                D3 = False
                            if i == j and ah[i * NN + i] != ah[0]:
                                D3 = False
        return out

    for smp in range(2):
        Xlink = {}
        for lk in LINKS:
            s = s_zero()
            s[1] = vec_to_mat(rsu3())
            Xlink[lk] = s
        model = Model(Xlink)
        omega = vec_to_mat(rsu3())
        vbase = list(model.Qx)
        vbase[1] = msub(vbase[1], omega)
        res = compare(model, vbase, True)
        for ok, nonvac, phi1, rhs in res:
            n1 += 1
            if not ok:
                D1 = False
                say("[D1 sample %d] mismatch: dual phi" % smp, [str(c) for c in phi1], "SG", [str(c) for c in rhs])
            if not nonvac:
                D2 = False
        say("[D1 sample %d]" % smp, sum(1 for r in res if r[0]), "/", len(res), "exact; nonvacuous:",
            sum(1 for r in res if r[1]), "/", len(res), "; e.g. dual phi =", [str(c) for c in res[0][2]])
        res4 = compare(model, vbase, False)
        nf = sum(1 for r in res4 if not r[0])
        n4fail += nf
        if nf > 0:
            D4_fires = True
        firstbad = next((r for r in res4 if not r[0]), None)
        say("[D4 control sample %d] comparisons failing with W_0 := e^{Ybar}:" % smp, nf, "/", len(res4),
            ("; first failing: phi'" + str([str(c) for c in firstbad[2]]) + " vs formula " + str([str(c) for c in firstbad[3]])) if firstbad else "")

    say("D1 (Lemma SG identity, N = 3, homogeneous family, %d comparisons):" % n1, "PASS" if D1 else "FAIL")
    say("D2 (non-vacuity of every dual part):", "PASS" if D2 else "FAIL")
    say("D3 (maximiser sanity):", "PASS" if D3 else "FAIL")
    say("D4 (control: non-maximiser e^{Ybar} breaks the identity):", "FIRES (%d failures)" % n4fail if D4_fires else "DOES NOT FIRE")
    overall = D1 and D2 and D3 and D4_fires
    say("OVERALL hg55_4:", "PASS" if overall else "FAIL")
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(run())
