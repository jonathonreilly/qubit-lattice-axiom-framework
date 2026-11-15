"""hg55_2 -- order-by-order slot structure of the lane's actual soft density (N = 2, d = 2, L = 3), exact.

phi_hat(M; V) = Re tr(W_0^{-1} M) - Re tr(V^{-1} M)  (TOWER-VAR / NA-alg (b)),  W_0 = SU(2) polar maximiser of M.
For SU(2): M (a real combination of SU(2) matrices) = sqrt(det M) * W_0, so phi_hat = sqrt(det M) (2 - Re tr(e^{-v} W_0)).
Exact truncated power series in eps (through eps^K) with dual numbers t (t^2 = 0); Gaussian-rational 2x2 matrices.
Criteria: checks/hg55_2_criteria.md (written first).  No floats.
"""
import itertools
import random
import sys
from fractions import Fraction as F

K = 4          # eps order kept
D = 2
L = 3
O = (L - 1) // 2
MU = 0

# ---------------- Gaussian rationals and 2x2 matrices ----------------
Z0 = (F(0), F(0))


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def csub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cscal(r, a):
    return (r * a[0], r * a[1])


def madd(A, B):
    return tuple(cadd(x, y) for x, y in zip(A, B))


def msub(A, B):
    return tuple(csub(x, y) for x, y in zip(A, B))


def mscal(r, A):
    return tuple(cscal(r, x) for x in A)


def mcscal(c, A):
    return tuple(cmul(c, x) for x in A)


def mmul(A, B):
    a, b, c, d = A
    e, f, g, h = B
    return (cadd(cmul(a, e), cmul(b, g)), cadd(cmul(a, f), cmul(b, h)),
            cadd(cmul(c, e), cmul(d, g)), cadd(cmul(c, f), cmul(d, h)))


MZ = (Z0, Z0, Z0, Z0)
MI = ((F(1), F(0)), Z0, Z0, (F(1), F(0)))
I_ = (F(0), F(1))
TAU = [
    ((F(0), F(1)), Z0, Z0, (F(0), F(-1))),            # [[i,0],[0,-i]]
    (Z0, (F(1), F(0)), (F(-1), F(0)), Z0),            # [[0,1],[-1,0]]
    (Z0, (F(0), F(1)), (F(0), F(1)), Z0),             # [[0,i],[i,0]]
]


def mtrace(A):
    return cadd(A[0], A[3])


def vec_to_mat(v):
    out = MZ
    for j in range(3):
        out = madd(out, mscal(F(v[j]), TAU[j]))
    return out


def mat_coords(A):
    # A = sum a_j tau_j  ->  a_j = -tr(A tau_j)/2 ; must be real for su(2) elements
    out = []
    for j in range(3):
        t = mtrace(mmul(A, TAU[j]))
        c = cscal(F(-1, 2), t)
        out.append(c)
    return out


def comm(A, B):
    return msub(mmul(A, B), mmul(B, A))


# ---------------- series: (part0, part1), each a list of K+1 coefficients ----------------
def mser_zero():
    return ([MZ] * (K + 1), [MZ] * (K + 1))


def mser_const(A):
    p0 = [MZ] * (K + 1)
    p0[0] = A
    return (p0, [MZ] * (K + 1))


def mser_add(X, Y):
    return ([madd(a, b) for a, b in zip(X[0], Y[0])], [madd(a, b) for a, b in zip(X[1], Y[1])])


def mser_sub(X, Y):
    return ([msub(a, b) for a, b in zip(X[0], Y[0])], [msub(a, b) for a, b in zip(X[1], Y[1])])


def mser_scal(r, X):
    return ([mscal(r, a) for a in X[0]], [mscal(r, a) for a in X[1]])


def _mconv(x, y):
    z = [MZ] * (K + 1)
    for i in range(K + 1):
        if x[i] == MZ:
            continue
        for j in range(K + 1 - i):
            if y[j] == MZ:
                continue
            z[i + j] = madd(z[i + j], mmul(x[i], y[j]))
    return z


def mser_mul(X, Y):
    z0 = _mconv(X[0], Y[0])
    z1a = _mconv(X[0], Y[1])
    z1b = _mconv(X[1], Y[0])
    return (z0, [madd(a, b) for a, b in zip(z1a, z1b)])


def mser_exp(A):
    assert A[0][0] == MZ, "exp needs zero eps^0 non-dual part"
    res = mser_const(MI)
    term = mser_const(MI)
    for n in range(1, K + 2):
        term = mser_scal(F(1, n), mser_mul(term, A))
        res = mser_add(res, term)
    return res


# scalar (Gaussian) series
def sser_const(c):
    p0 = [Z0] * (K + 1)
    p0[0] = c
    return (p0, [Z0] * (K + 1))


def _sconv(x, y):
    z = [Z0] * (K + 1)
    for i in range(K + 1):
        if x[i] == Z0:
            continue
        for j in range(K + 1 - i):
            if y[j] == Z0:
                continue
            z[i + j] = cadd(z[i + j], cmul(x[i], y[j]))
    return z


def sser_mul(X, Y):
    z0 = _sconv(X[0], Y[0])
    z1a = _sconv(X[0], Y[1])
    z1b = _sconv(X[1], Y[0])
    return (z0, [cadd(a, b) for a, b in zip(z1a, z1b)])


def sser_add(X, Y):
    return ([cadd(a, b) for a, b in zip(X[0], Y[0])], [cadd(a, b) for a, b in zip(X[1], Y[1])])


def sser_scal(r, X):
    return ([cscal(r, a) for a in X[0]], [cscal(r, a) for a in X[1]])


def binom_half(n):
    # C(1/2, n)
    c = F(1)
    for k in range(n):
        c *= (F(1, 2) - k)
        c /= (k + 1)
    return c


def sser_sqrt_1pu(U):
    # sqrt(1+U), U with zero eps^0 non-dual part
    assert U[0][0] == Z0
    res = sser_const((F(1), F(0)))
    powu = sser_const((F(1), F(0)))
    for n in range(1, K + 2):
        powu = sser_mul(powu, U)
        res = sser_add(res, sser_scal(binom_half(n), powu))
    return res


def sser_inv_1pu(U):
    assert U[0][0] == Z0
    res = sser_const((F(1), F(0)))
    powu = sser_const((F(1), F(0)))
    for n in range(1, K + 2):
        powu = sser_scal(F(-1), sser_mul(powu, U))
        res = sser_add(res, powu)
    return res


def mser_times_sser(X, s):
    # matrix series times scalar series
    def conv(x, y):
        z = [MZ] * (K + 1)
        for i in range(K + 1):
            for j in range(K + 1 - i):
                if y[j] == Z0 or x[i] == MZ:
                    continue
                z[i + j] = madd(z[i + j], mcscal(y[j], x[i]))
        return z
    z0 = conv(X[0], s[0])
    z1 = [madd(a, b) for a, b in zip(conv(X[0], s[1]), conv(X[1], s[0]))]
    return (z0, z1)


def mser_det(X):
    a = ([m[0] for m in X[0]], [m[0] for m in X[1]])
    b = ([m[1] for m in X[0]], [m[1] for m in X[1]])
    c = ([m[2] for m in X[0]], [m[2] for m in X[1]])
    d = ([m[3] for m in X[0]], [m[3] for m in X[1]])
    ad = sser_mul(a, d)
    bc = sser_mul(b, c)
    return ([csub(x, y) for x, y in zip(ad[0], bc[0])], [csub(x, y) for x, y in zip(ad[1], bc[1])])


def mser_trace(X):
    return ([mtrace(m) for m in X[0]], [mtrace(m) for m in X[1]])


# ---------------- contours (LINEAR_PACKAGE §1.2 in d = 2) ----------------
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


def make_contours(single=False):
    if single:
        return [contour_letters((0, 1), (O + 0, O + 1))]
    out = []
    for order in itertools.permutations(range(D)):
        for y in itertools.product(range(L), repeat=D):
            out.append(contour_letters(order, y))
    return out


# ---------------- the soft density and its derivatives ----------------
class Config:
    def __init__(self, contours, xbar, g, rho2):
        self.contours = contours
        self.n = len(contours)
        self.links = sorted({lk for w in contours for (lk, _) in w})
        self.xbar = xbar      # dict dir -> int vector
        self.g = g            # dict link -> int vector
        self.rho2 = rho2      # int vector
        # Q_{cb}
        self.Q = {lk: F(0) for lk in self.links}
        for w in contours:
            for (lk, s) in w:
                self.Q[lk] += F(s, self.n)
        # link field series (non-dual)
        self.X = {}
        for lk in self.links:
            p0 = [MZ] * (K + 1)
            p0[1] = vec_to_mat(xbar[lk[1]])
            p0[2] = vec_to_mat(g[lk])
            self.X[lk] = (p0, [MZ] * (K + 1))
        self.expX = {}
        for lk in self.links:
            self.expX[(lk, +1)] = mser_exp(self.X[lk])
            self.expX[(lk, -1)] = mser_exp(mser_scal(F(-1), self.X[lk]))
        # (Q x)(c) as a series
        qx = mser_zero()
        for lk in self.links:
            qx = mser_add(qx, mser_scal(self.Q[lk], self.X[lk]))
        r = mser_zero()
        r[0][2] = vec_to_mat(rho2)
        self.v = mser_sub(qx, r)

    def phi(self, pert_link=None, pert_dir=None, pert_v=None):
        """phi_hat as a dual series; perturbation t*tau at one link (or at v)."""
        def link_exp(lk, s):
            if pert_link is not None and lk == pert_link:
                A = self.X[lk]
                A = (A[0], [MZ] * (K + 1))
                A[1][0] = TAU[pert_dir]
                if s < 0:
                    A = mser_scal(F(-1), A)
                return mser_exp(A)
            return self.expX[(lk, s)]
        Msum = mser_zero()
        for w in self.contours:
            T = mser_const(MI)
            for (lk, s) in w:
                T = mser_mul(T, link_exp(lk, s))
            Msum = mser_add(Msum, T)
        M = mser_scal(F(1, self.n), Msum)
        detM = mser_det(M)
        U = (list(detM[0]), list(detM[1]))
        U[0][0] = csub(U[0][0], (F(1), F(0)))
        assert U[0][0] == Z0
        s = sser_sqrt_1pu(U)
        sm1 = (list(s[0]), list(s[1]))
        sm1[0][0] = csub(sm1[0][0], (F(1), F(0)))
        sinv = sser_inv_1pu(sm1)
        W0 = mser_times_sser(M, sinv)
        v = self.v
        if pert_v is not None:
            v = (v[0], [MZ] * (K + 1))
            v[1][0] = TAU[pert_v]
        E = mser_exp(mser_scal(F(-1), v))
        tr = mser_trace(mser_mul(E, W0))
        two_minus = ([cscal(F(-1), c) for c in tr[0]], [cscal(F(-1), c) for c in tr[1]])
        two_minus[0][0] = cadd(two_minus[0][0], (F(2), F(0)))
        ph = sser_mul(s, two_minus)
        # Re part; record imaginary part for sanity
        self._last_det = detM
        self._last_W0 = W0
        return ph

    def deriv(self, **kw):
        ph = self.phi(**kw)
        return [c[0] for c in ph[1]], [c[1] for c in ph[1]], ph


def bch2_row_prediction(cfg, link, i):
    """Independent: D_{b,i} a^{(2)}(xbar) in tau-coordinates, via the bilinear BCH2 form (no series)."""
    acc = MZ
    for w in cfg.contours:
        zbar = [mscal(F(s), vec_to_mat(cfg.xbar[lk[1]])) for (lk, s) in w]
        dz = [mscal(F(s), TAU[i]) if lk == link else MZ for (lk, s) in w]
        p = len(w)
        for a in range(p):
            for b in range(a + 1, p):
                acc = madd(acc, comm(dz[a], zbar[b]))
                acc = madd(acc, comm(zbar[a], dz[b]))
    acc = mscal(F(1, 2 * cfg.n), acc)
    co = mat_coords(acc)
    for c in co:
        assert c[1] == 0
    return [c[0] for c in co]


def main():
    rng = random.Random(55002)
    log = []

    def say(*a):
        s = " ".join(str(x) for x in a)
        log.append(s)
        print(s, flush=True)

    full = make_contours()
    single = make_contours(single=True)
    say("contours (S4' in d=2):", len(full), " max letters:", max(len(w) for w in full), "; control contours:", len(single))
    test_links = [((1, 1), 1), ((0, 1), 0), ((2, 1), 0), ((3, 0), 0), ((4, 1), 1), ((3, 2), 0)]
    full_links = {lk for w in full for (lk, _) in w}
    for lk in test_links:
        assert lk in full_links, lk

    def rvec(lo, hi, nonzero=False):
        while True:
            v = tuple(rng.randint(lo, hi) for _ in range(3))
            if not nonzero or v != (0, 0, 0):
                return v

    def new_config(contours, rho_zero):
        xbar = {nu: rvec(-3, 3, nonzero=True) for nu in range(D)}
        links = {lk for w in contours for (lk, _) in w} | set(test_links)
        g = {lk: rvec(-2, 2) for lk in sorted(links)}
        rho2 = (0, 0, 0) if rho_zero else rvec(-3, 3, nonzero=True)
        return Config(contours, xbar, g, rho2)

    B1 = B2 = B3 = B5 = True
    B2_nonvac = False
    B3_nonvac_P = False
    B3_nonvac_O = False
    B4_fires = False

    def run(cfg, tag, mode):
        nonlocal B1, B2, B3, B5, B2_nonvac, B3_nonvac_P, B3_nonvac_O, B4_fires
        # Omega_i = - d phi / d nu_i
        Om = []
        for i in range(3):
            re, im, ph = cfg.deriv(pert_v=i)
            if any(x != 0 for x in im) or any(c[1] != 0 for c in ph[0]):
                B5 = False
                say(tag, "B5 FAIL: phi not real")
            Om.append([-x for x in re])
        # sanity B5 on det M and det W0
        detM = cfg._last_det
        if any(c[1] != 0 for c in detM[0]):
            B5 = False
            say(tag, "B5 FAIL: det M not real")
        dW = mser_det(cfg._last_W0)
        if dW[0][0] != (F(1), F(0)) or any(c != Z0 for c in dW[0][1:]):
            B5 = False
            say(tag, "B5 FAIL: det W0 != 1")
        P = {}
        for lk in test_links:
            for i in range(3):
                re, im, ph = cfg.deriv(pert_link=lk, pert_dir=i)
                if any(x != 0 for x in im):
                    B5 = False
                    say(tag, "B5 FAIL: dphi not real")
                P[(lk, i)] = [re[n] - cfg.Q.get(lk, F(0)) * Om[i][n] for n in range(K + 1)]
        say(tag, "Omega coefficients eps^0..eps^4 per i:", [[str(c) for c in Om[i]] for i in range(3)])
        if mode == "B12":
            for i in range(3):
                ok = Om[i][0] == 0 and Om[i][1] == 0 and Om[i][2] == 2 * cfg.rho2[i]
                if not ok:
                    B1 = False
                    say(tag, "B1 FAIL i", i, Om[i])
            for lk in test_links:
                for i in range(3):
                    pred_vec = bch2_row_prediction(cfg, lk, i)
                    pred = 2 * sum(F(cfg.rho2[j]) * pred_vec[j] for j in range(3))
                    p = P[(lk, i)]
                    ok = p[0] == 0 and p[1] == 0 and p[2] == 0 and p[3] == pred
                    if pred != 0:
                        B2_nonvac = True
                    if not ok:
                        B2 = False
                        say(tag, "B2 FAIL link", lk, "i", i, "P", [str(c) for c in p], "pred", pred)
            say(tag, "sample P eps^3 vs BCH2-row prediction:",
                [(str(P[(lk, 0)][3]), str(2 * sum(F(cfg.rho2[j]) * bch2_row_prediction(cfg, lk, 0)[j] for j in range(3))))
                 for lk in test_links[:3]])
        elif mode == "B3":
            for i in range(3):
                if not (Om[i][0] == 0 and Om[i][1] == 0 and Om[i][2] == 0):
                    B3 = False
                    say(tag, "B3 FAIL Omega i", i, Om[i])
                if Om[i][3] != 0:
                    B3_nonvac_O = True
            for key, p in P.items():
                if not (p[0] == 0 and p[1] == 0 and p[2] == 0 and p[3] == 0):
                    B3 = False
                    say(tag, "B3 FAIL P", key, [str(c) for c in p])
                if p[4] != 0:
                    B3_nonvac_P = True
            say(tag, "P eps^3, eps^4 coefficients (first 3 links, i=0):",
                [(str(P[(lk, 0)][3]), str(P[(lk, 0)][4])) for lk in test_links[:3]])
        elif mode == "B4":
            fired = any(Om[i][2] != 0 for i in range(3)) or any(p[3] != 0 for p in P.values())
            say(tag, "control: Omega eps^2 coeffs", [str(Om[i][2]) for i in range(3)],
                "; P eps^3 coeffs (test links present in the single contour):",
                [(lk, str(P[(lk, 0)][3])) for lk in test_links if lk in cfg.Q])
            if fired:
                B4_fires = True

    for smp in range(3):
        cfg = new_config(full, rho_zero=False)
        run(cfg, "[B1/B2 sample %d]" % smp, "B12")
    for smp in range(2):
        cfg = new_config(full, rho_zero=True)
        run(cfg, "[B3 sample %d]" % smp, "B3")
    cfg = new_config(single, rho_zero=True)
    # Q for links absent from the single contour is 0; derivative there is 0
    run(cfg, "[B4 control]", "B4")

    say("B1 (Omega = 2 eps^2 rho2 + O(eps^3)):", "PASS" if B1 else "FAIL")
    say("B2 (P = O(eps^3), eps^3 coeff == independent BCH2-row prediction; nonvacuous):",
        "PASS" if (B2 and B2_nonvac) else "FAIL", "[match:", B2, " nonvacuous:", B2_nonvac, "]")
    say("B3 (rho = 0: Omega = O(eps^3), P = O(eps^4); nonvacuous):",
        "PASS" if (B3 and B3_nonvac_P and B3_nonvac_O) else "FAIL",
        "[orders:", B3, " P eps^4 nonzero somewhere:", B3_nonvac_P, " Omega eps^3 nonzero somewhere:", B3_nonvac_O, "]")
    say("B4 (control, single contour, no S4' average):", "FIRES" if B4_fires else "DOES NOT FIRE")
    say("B5 (sanity: phi, dphi, det M real; det W0 == 1):", "PASS" if B5 else "FAIL")
    overall = B1 and B2 and B2_nonvac and B3 and B3_nonvac_P and B3_nonvac_O and B5 and B4_fires
    say("OVERALL hg55_2:", "PASS" if overall else "FAIL")
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
