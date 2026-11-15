"""h7: lane D session 4 checks (criteria: checks/h7_criteria.md, written first).

A: holomorphic continuation of NA-alg (a)'s fixed point and of phi (HIST Lemma TERM-an, NORM-an (i)).
B: polar vs chart comparison (HIST Lemma POL).
C: arithmetic of HIST section 26 constants (Theorem AE-red).
"""
import math
import time
import numpy as np
from scipy.linalg import expm

T0 = time.time()
RES = {}


def hs(Z):
    return float(np.sqrt(np.sum(np.abs(Z) ** 2)))


def op(Z):
    return float(np.linalg.norm(Z, 2))


def rand_su(N, rng):
    A = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    Z = (A - A.conj().T) / 2
    Z -= np.trace(Z) / N * np.eye(N)
    return Z / hs(Z)


def rand_sl(N, rng):
    Z = rand_su(N, rng) + 1j * rand_su(N, rng)
    return Z / hs(Z)


def haar_su(N, rng, n=None):
    shape = (N, N) if n is None else (n, N, N)
    Z = rng.normal(size=shape) + 1j * rng.normal(size=shape)
    Q, R = np.linalg.qr(Z)
    d = np.diagonal(R, axis1=-2, axis2=-1)
    Q = Q * (d / np.abs(d))[..., None, :]
    det = np.linalg.det(Q)
    Q = Q / (det ** (1.0 / N))[..., None, None]
    return Q


def P0(Z):
    N = Z.shape[0]
    return Z - np.trace(Z) / N * np.eye(N)


def PiR(Z):
    N = Z.shape[0]
    A = (Z - Z.conj().T) / 2
    return A - np.trace(A) / N * np.eye(N)


def build(Y, w):
    N = Y[0].shape[0]
    M = sum(wj * expm(Yj) for wj, Yj in zip(w, Y))
    Mc = sum(wj * expm(-Yj) for wj, Yj in zip(w, Y))
    Yb = sum(wj * Yj for wj, Yj in zip(w, Y))
    return M, Mc, Yb


def fixed_point_C(Y, w, tol=1e-15, cap=200):
    N = Y[0].shape[0]
    I = np.eye(N)
    M, Mc, Yb = build(Y, w)
    X = Yb.copy()
    for n in range(cap):
        K = expm(-X) @ M - I - (Yb - X)
        Kc = Mc @ expm(X) - I - (X - Yb)
        Xn = Yb + P0((K - Kc) / 2)
        if hs(Xn - X) <= tol:
            return Xn, n + 1, M, Mc, Yb
        X = Xn
    return X, None, M, Mc, Yb


def fixed_point_R(Y, w, tol=1e-15, cap=200):
    N = Y[0].shape[0]
    I = np.eye(N)
    M, Mc, Yb = build(Y, w)
    X = Yb.copy()
    for n in range(cap):
        K = expm(-X) @ M - I - (Yb - X)
        Xn = Yb + PiR(K)
        if hs(Xn - X) <= tol:
            return Xn, n + 1
        X = Xn
    return X, None


def phiC(V, X0, M, Mc):
    N = V.shape[0]
    Vi = np.linalg.inv(V)
    return (np.trace(expm(-X0) @ M) + np.trace(Mc @ expm(X0)) - np.trace(Vi @ M) - np.trace(Mc @ V)) / (2 * N)


def sample_Y(N, m, y, cplx, rng):
    Y = []
    for _ in range(m):
        u = rng.uniform(0.2, 1.0)
        Z = rand_sl(N, rng) if cplx else rand_su(N, rng)
        Y.append(y * u * Z)
    w = rng.dirichlet(np.ones(m))
    return Y, w


def cN(N):
    rN = min(1.0, 4.0 / math.sqrt(N))
    return max(math.pi ** 3 / 24, N / rN ** 2)


# ---------------- A ----------------
rng = np.random.default_rng(0)
A1 = A2 = A4 = True
worst = dict(A1a=0, A1b=0, A1c=0, A2res=0, A2ratio=0, A2X=0, A4a=0, A4b=0, A4c=0)
iters_max = 0
for N in (2, 3):
    for m in (3, 6):
        for y in (0.005, 0.02, 0.05):
            for cplx in (False, True):
                for smp in range(20):
                    Y, w = sample_Y(N, m, y, cplx, rng)
                    ymax = max(hs(Yj) for Yj in Y)
                    X0, it, M, Mc, Yb = fixed_point_C(Y, w)
                    if it is None:
                        A2 = False if cplx else A2
                        A1 = False if not cplx else A1
                        continue
                    iters_max = max(iters_max, it)
                    I = np.eye(N)
                    if not cplx:
                        ah = hs(X0 + X0.conj().T)
                        tr = abs(np.trace(X0))
                        worst['A1a'] = max(worst['A1a'], ah, tr)
                        XR, itR = fixed_point_R(Y, w)
                        d = hs(X0 - XR)
                        worst['A1b'] = max(worst['A1b'], d)
                        W0 = expm(X0)
                        f0 = np.real(np.trace(np.linalg.inv(W0) @ M))
                        gap = 0.0
                        for t in (1e-3, 1e-2, 0.1, 1.0):
                            for _ in range(50):
                                W = W0 @ expm(t * rand_su(N, rng))
                                gap = max(gap, np.real(np.trace(np.linalg.inv(W) @ M)) - f0)
                        Hs = haar_su(N, rng, 200)
                        vals = np.real(np.trace(np.linalg.inv(Hs) @ M, axis1=1, axis2=2))
                        gap = max(gap, float(np.max(vals - f0)))
                        worst['A1c'] = max(worst['A1c'], gap)
                        if ah > 1e-13 or tr > 1e-13 or d > 1e-13 or gap > 1e-13:
                            A1 = False
                        # A4 (a): real agreement of phi^C
                        for k in range(10):
                            V = haar_su(N, rng) if k < 5 else W0 @ expm(0.05 * rand_su(N, rng))
                            pc = phiC(V, X0, M, Mc)
                            pr = (np.real(np.trace(np.linalg.inv(W0) @ M)) - np.real(np.trace(np.linalg.inv(V) @ M))) / N
                            dd = abs(pc - pr)
                            worst['A4a'] = max(worst['A4a'], dd)
                            if dd > 1e-13:
                                A4 = False
                    else:
                        G = expm(-X0) @ M
                        Gc = Mc @ expm(X0)
                        res = hs(P0((G - Gc) / 2))
                        ratio = hs(X0 - Yb) / (9.2 * ymax ** 2)
                        xr = hs(X0) / (3 * ymax)
                        worst['A2res'] = max(worst['A2res'], res)
                        worst['A2ratio'] = max(worst['A2ratio'], ratio)
                        worst['A2X'] = max(worst['A2X'], xr)
                        if res > 1e-13 or ratio > 1 or xr > 1:
                            A2 = False
                        W0C = expm(X0)
                        # A4 (b): local expansion bound
                        for r in (1e-3, 1e-2, 0.05):
                            rho = r * rand_sl(N, rng)
                            V = W0C @ expm(-rho)
                            lhs = abs(phiC(V, X0, M, Mc) + np.trace(rho @ rho) / (2 * N))
                            rhs = 4.6 * ymax ** 2 * r ** 2 / N + math.exp(4 * ymax + r) * r ** 3 / (6 * math.sqrt(N))
                            worst['A4b'] = max(worst['A4b'], lhs / rhs)
                            if lhs > rhs:
                                A4 = False
                        # A4 (c): global Haar-shift form
                        th = 18.4 * ymax ** 2 * (2 + 2 * cN(N))
                        Hs = haar_su(N, rng, 500)
                        Hsi = np.linalg.inv(Hs)
                        WV = W0C[None] @ Hs
                        WVi = Hsi @ np.linalg.inv(W0C)[None]
                        c0 = np.trace(G) + np.trace(Gc)
                        ph = (c0 - np.trace(WVi @ M, axis1=1, axis2=2) - np.trace(Mc[None] @ WV, axis1=1, axis2=2)) / (2 * N)
                        sv = 1 - np.real(np.trace(Hs, axis1=1, axis2=2)) / N
                        rat = float(np.max(np.abs(ph - sv) / (th * sv)))
                        worst['A4c'] = max(worst['A4c'], rat)
                        if rat > 1:
                            A4 = False
RES['A1'] = A1
RES['A2'] = A2
RES['A4'] = A4
print("A: max fixed-point iterations %d" % iters_max)
print("A1 PASS" if A1 else "A1 FAIL", "| max antiherm/trace %.1e, |X0-XR| %.1e, max ascent gap %.1e" % (
    worst['A1a'], worst['A1b'], worst['A1c']))
print("A2 PASS" if A2 else "A2 FAIL", "| max stationarity residual %.1e, max |X0-Ybar|/(9.2y^2) %.3f, max |X0|/(3y) %.3f" % (
    worst['A2res'], worst['A2ratio'], worst['A2X']))

# A3 holomorphy (CR test) with non-holomorphic control
rng = np.random.default_rng(1)
h = 1e-6
A3 = True
cr_h, cr_phi, cr_ctrl = [], [], []
for N in (2, 3):
    for smp in range(20):
        Y, w = sample_Y(N, 3, 0.02, True, rng)
        D = [rand_sl(N, rng) for _ in Y]
        F0 = fixed_point_C(Y, w)[0]
        F1 = fixed_point_C([a + h * b for a, b in zip(Y, D)], w)[0]
        F2 = fixed_point_C([a + 1j * h * b for a, b in zip(Y, D)], w)[0]
        cr_h.append(hs((F2 - F0) - 1j * (F1 - F0)) / hs(F1 - F0))
        X0, _, M, Mc, _ = fixed_point_C(Y, w)
        V = expm(X0) @ expm(-0.02 * rand_sl(N, rng))

        def phi_of(Yv):
            Xv, _, Mv, Mcv, _ = fixed_point_C(Yv, w)
            return phiC(V, Xv, Mv, Mcv)
        p0 = phi_of(Y)
        p1 = phi_of([a + h * b for a, b in zip(Y, D)])
        p2 = phi_of([a + 1j * h * b for a, b in zip(Y, D)])
        cr_phi.append(abs((p2 - p0) - 1j * (p1 - p0)) / abs(p1 - p0))
        R0 = fixed_point_R(Y, w)[0]
        R1 = fixed_point_R([a + h * b for a, b in zip(Y, D)], w)[0]
        R2 = fixed_point_R([a + 1j * h * b for a, b in zip(Y, D)], w)[0]
        cr_ctrl.append(hs((R2 - R0) - 1j * (R1 - R0)) / hs(R1 - R0))
hol_ok = max(cr_h) <= 1e-3 and max(cr_phi) <= 1e-3
ctrl_fails = min(cr_ctrl) >= 0.1
A3 = hol_ok and ctrl_fails
RES['A3'] = A3
print("A3 PASS" if A3 else "A3 FAIL", "| CR defect X0: max %.2e; phi: max %.2e; control (real map): min %.3e median %.3e max %.3e" % (
    max(cr_h), max(cr_phi), min(cr_ctrl), float(np.median(cr_ctrl)), max(cr_ctrl)))
print("A4 PASS" if A4 else "A4 FAIL", "| real phi agreement %.1e; local bound ratio max %.3f; global |Delta|/(theta s) max %.4f" % (
    worst['A4a'], worst['A4b'], worst['A4c']))

# A5 Haar shift of the normalisation (soft / informational)
rng = np.random.default_rng(2)
Y, w = sample_Y(2, 3, 0.02, True, rng)
X0, _, M, Mc, _ = fixed_point_C(Y, w)
W0C = expm(X0)
G = expm(-X0) @ M
Gc = Mc @ expm(X0)
c0 = np.trace(G) + np.trace(Gc)
n_s = 200000
Hs = haar_su(2, rng, n_s)
Hsi = np.linalg.inv(Hs)
ph1 = (c0 - np.trace(Hsi @ M[None], axis1=1, axis2=2) - np.trace(Mc[None] @ Hs, axis1=1, axis2=2)) / 4
WV = W0C[None] @ Hs
WVi = Hsi @ np.linalg.inv(W0C)[None]
ph2 = (c0 - np.trace(WVi @ M[None], axis1=1, axis2=2) - np.trace(Mc[None] @ WV, axis1=1, axis2=2)) / 4
sv = 1 - np.real(np.trace(Hs, axis1=1, axis2=2)) / 2
ymax = max(hs(Yj) for Yj in Y)
th = 18.4 * ymax ** 2 * (2 + 2 * cN(2))
A5 = True
for ku in (20.0, 80.0):
    f1 = np.exp(-ku * ph1)
    f2 = np.exp(-ku * ph2)
    f0 = np.exp(-ku * sv)
    I1, I2, I0 = f1.mean(), f2.mean(), f0.mean()
    se = math.sqrt((np.var(f1.real) + np.var(f1.imag) + np.var(f2.real) + np.var(f2.imag)) / n_s)
    rel = abs(I1 - I2) / abs(I2)
    lim = max(5 * se / abs(I2), 0.05)
    ok = rel <= lim
    A5 = A5 and ok
    print("A5 kappa*u=%g: |I1-I2|/|I2| = %.3e (limit %.3e) %s; |I2/I0-1| = %.3e (theta = %.3e)" % (
        ku, rel, lim, "ok" if ok else "SOFT-FAIL", abs(I2 / I0 - 1), th))
RES['A5(soft)'] = A5

# ---------------- B ----------------
rng = np.random.default_rng(3)
B1 = B2 = True
b1w = 0.0
b2H = b2V = 0.0
b3 = 0.0
for N in (2, 3):
    for t in (1e-4, 1e-3, 1e-2, 0.1, 0.125):
        for smp in range(200):
            X = rand_su(N, rng)
            X = X / op(X) * rng.uniform(0, 0.125)
            Yv = rand_su(N, rng)
            Yv = Yv / op(Yv) * t
            A = expm(X + 1j * Yv)
            lam, U = np.linalg.eigh(A.conj().T @ A)
            H = 0.5 * (U * np.log(lam)) @ U.conj().T
            V = A @ expm(-H)
            e1 = max(abs(np.linalg.det(V) - 1), abs(np.trace(H)))
            b1w = max(b1w, e1)
            if e1 > 1e-12:
                B1 = False
            rH = op(H) / op(Yv)
            rV = op(V - expm(X)) / op(Yv)
            b2H = max(b2H, rH)
            b2V = max(b2V, rV)
            if rH > 4.19 or rV > 9.2:
                B2 = False
            b3 = max(b3, op(H - 1j * Yv) / (op(X) * op(Yv) + op(Yv) ** 2))
RES['B1'] = B1
RES['B2'] = B2
print("B1 PASS" if B1 else "B1 FAIL", "| max |det V - 1|, |tr H| = %.1e" % b1w)
print("B2 PASS" if B2 else "B2 FAIL", "| max ||H||/||Y|| = %.3f (bound 4.19); max ||V - e^X||/||Y|| = %.3f (bound 9.2)" % (b2H, b2V))
print("B3 (info) max ||H - iY|| / (||X|| ||Y|| + ||Y||^2) = %.3f" % b3)


# ---------------- C ----------------
def msg_eps(N, L, d, Aax):
    Ad = (d - 1) * L * (L - 1) / 2
    B = 2 * Ad + 2 + 2.02 * Ad / L ** 2
    Cst = max(1.011 * Aax, 2 * B * L / (L - 1))
    CM = max(Cst, 1.011 * (1.011 * L * Aax + 2 * Ad + 1))

    def ok(e):
        y = 1.011 * math.sqrt(N) * Ad * e
        return (Aax * e <= 0.5 and 18.8 * N * Ad ** 2 * e <= 1 and 18.4 * y ** 2 <= e and y <= 0.05
                and 33 * Cst ** 2 * e * math.exp(4 * Cst * e) <= 1 and Cst * e / L + B * e <= 0.5)
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if ok(mid):
            lo = mid
        else:
            hi = mid
    return lo, CM, Cst


def ae_constants(N, L, d, kap, CS):
    Ad = (d - 1) * L * (L - 1) / 2
    Ap = 2 * Ad
    pL = 5 * L - 4
    Cloc = ((2 * L - 1) / (L - 1)) * max(2.0, 16.0 / kap)
    CAE = 2 * Cloc * N
    cp = 1.0107 * math.sqrt(N)
    Cpp = max(2 * N, CAE)
    Cn = max(math.sqrt(Cpp), math.sqrt(4 * N / kap))
    epsM, CM, Cst = msg_eps(N, L, d, 12)
    epsS = epsM
    Ce = max(2 * math.sqrt(N) * pL ** 2 * math.exp(1 / 8) + 9.4 * N * pL ** 2
             + 36.8 * N ** 1.5 * pL ** 2 * math.exp(0.25), 4 * math.sqrt(N) * math.exp(0.25))
    KR = 64 * math.sqrt(8) * math.sqrt(N) * math.exp(0.5)
    C2 = (KR * math.sqrt(CS) + math.sqrt(8) * (L / (L - 1)) * Ce * (math.sqrt(2 * d * CS)
          + 1.011 * math.sqrt(N) * Cn * math.sqrt(2.4 * N / kap)) + 32 * math.sqrt(N) * math.exp(0.5) * CM ** 2 * Cn ** 2)

    def conds(eta):
        et = Cn * math.sqrt(eta)
        yp = cp * Ap * math.sqrt(Cpp * eta)
        yM = 1.011 * math.sqrt(N) * pL * CM * et
        r = 1.011 * math.sqrt(N) * et
        thv = 1.011 * math.sqrt(2 * N * eta)
        x = 18.4 * yp ** 2 + (2 * math.sqrt(N) / 3) * math.exp(r) * r
        delta = max(thv ** 2 / (12 - thv ** 2), x / (1 - x) if x < 1 else 1e9)
        lhs = math.sqrt(1.2 * Cloc * N) + C2 * math.sqrt(eta)
        c = dict(Z1=et <= epsS, Z2=(yp <= 0.05 and 2 * Ad * math.sqrt(Cpp * eta) <= 0.5
                                    and 73.6 * N * (cp * Ap) ** 2 * Cpp * math.sqrt(eta) <= math.sqrt(Cpp)),
                 Z3=(pL * CM * et <= 1 / 8 and 3 * yM + r <= 0.25 and yM <= 0.05), Z4=(1 + delta <= 1.2),
                 Z5=lhs <= math.sqrt(CAE))
        return c, lhs
    eta = None
    for n in range(0, 400):
        e = 2.0 ** (-n)
        c, lhs = conds(e)
        if all(c.values()):
            eta = e
            break
    c, lhs = conds(eta)
    Ccone = max(CAE / (2 * N), 2 / eta)
    return dict(Cloc=Cloc, CAE=CAE, Cn=Cn, Ce=Ce, C2=C2, epsM=epsM, CM=CM, eta=eta, lhs=lhs, rhs=math.sqrt(CAE),
                et=Cn * math.sqrt(eta), Ccone=Ccone, conds=c)


C1 = C2ok = True
for (N, L, d, kap) in ((2, 3, 4, 1.0), (3, 3, 4, 1.0)):
    for CS in (1.0, 1e2, 1e4):
        r = ae_constants(N, L, d, kap, CS)
        allc = all(r['conds'].values())
        c2 = r['eta'] <= (6.9e-6) ** 2 / r['CAE']
        C1 = C1 and allc
        C2ok = C2ok and c2
        print("C N=%d C_S=%.0e: C_loc=%.1f C'_AE=%.0f C_nat=%.2f C_e=%.3e C_2=%.3e eps_M=%.3e C_M=%.2f | eta_AE=%.3e "
              "eps~=%.2e closing %.4f<=%.4f | C_cone=%.2e | Z-all %s, eta<=eps_M^2/C'_AE %s" % (
                  N, CS, r['Cloc'], r['CAE'], r['Cn'], r['Ce'], r['C2'], r['epsM'], r['CM'], r['eta'], r['et'],
                  r['lhs'], r['rhs'], r['Ccone'], allc, c2))
RES['C1'] = C1
RES['C2'] = C2ok
print("C1 PASS" if C1 else "C1 FAIL", "| C2 PASS" if C2ok else "| C2 FAIL")

hard = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'C1', 'C2']
overall = all(RES[k] for k in hard)
print("OVERALL: %s (hard: %s; soft A5: %s)" % ("PASS" if overall else "FAIL",
      ", ".join("%s=%s" % (k, "PASS" if RES[k] else "FAIL") for k in hard), RES['A5(soft)']))
print("runtime %.1f s" % (time.time() - T0))
