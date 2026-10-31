#!/usr/bin/env python3
"""Order calculus on the twisted algebra and Leaf Scalar. Consumer: `library/twisted-order-calculus.md`, Theorem P1.

Written before running. Flux theta = 2 pi m / N in the (1, 2) plane, N prime, in the N x N Bloch representation of T_1, T_2, with T_1 T_2 = e^{i theta} T_2 T_1. Directions 3, 4 enter through rho := |p_3^|^2 + |p_4^|^2, a commuting number. X := X_12 + rho, G := X^-1, D_mu := T_mu - 1.

Model of the operator E. The true E_theta is known only through its orders. So take E with those orders and arbitrary coefficients:
 E_munu = Op(f_munu) + theta Op(g_munu) + theta^2 Op(u_munu),
with f of order 4, g of order 2, u of order 0, where rho counts as order 2, with the reflection properties of the real operator (g off-diagonal i times an even kernel; g diagonal odd under each reflection). Y := G (sum D_mu^* E_munu D_nu + rho E_perp) G, r := 1 + Y, L(theta) := per-site log det r, integrated over p_3, p_4.

PRE-STATED criteria.
 A. Landau gap: the bottom of X_12 is at least theta/2 for every N.
 B. Orders. For B in {T_1, D_1, D_1^*, delta_1 X, E_11, delta_1 E_11, delta_1 delta_2 E_11, dE_11/dtheta, Y, dY}, of order m in the note, n(B, s, N) := ||X^s B X^(-s - m/2)|| at rho = 0, for s in {-5/2, -3/2, -1/2, 0, 1/2, 3/2, 5/2}. PASS if, for each B, the maximum over s at N = 509 is at most 1.5 times the maximum over s at N = 61. dY is the kernel derivative in theta of Y, computed by the formula of the note.
 C. Leaf Scalar. Q(N) := (L(theta_N) - L(0)) / theta_N^2 at m = 1, N = 61, 127, 251, 509. With d_1, d_2, d_3 the successive differences: PASS if |d_3| <= 0.8 |d_2| or |d_3| <= 0.01 |Q(509)|.
 D. Control on C's power: the same with an E of order 2, f_11 = 0.6 |s_1|^2, f_22 = 0.2 |s_2|^2, f_perp = 0.3 rho, g = u = 0. The note says that this is outside the theorem, and a logarithm is expected. PASS of the control if |d_3| >= 0.8 |d_2| with d_2, d_3 of one sign. If the control converges too, C has no power and C is reported as uninformative.
 F. Derivative formula. L'(theta) = tau(R dY) - (i/2) eps^{ab} int_0^infty tau(S delta_a r S delta_b r S) ds at fixed rho, against a five-point difference in m at N = 251, m = 3, 5, rho = 0.05, 0.5. PASS if the difference is at most 1e-6 + 1e-3 |L'|.
 K. Control on the Bloch average: |L at k = 0 minus L at the half-period point| <= 1e-9 at N >= 61, at rho = nodes 0, 5, 20.
FAIL if A, B, C, F or K fails. D is reported as a control.

Limits. The operator E here is a model with the stated orders, so this tests the calculus and the theorem's mechanism, and it is not a test of Prop 3.11, which supplies the orders of the true E. RSS guard 2 GB.
"""
import os
import resource
import sys

import numpy as np

CASES = {}


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")


def padd(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0) + v
    return out


def pmul(a, b):
    out = {}
    for (x, y), v in a.items():
        for (u, w), z in b.items():
            k = (x + u, y + w)
            out[k] = out.get(k, 0) + v * z
    return out


def pscale(c, a):
    return {k: c * v for k, v in a.items()}


S1 = {(0, 0): 2.0, (1, 0): -1.0, (-1, 0): -1.0}
S2 = {(0, 0): 2.0, (0, 1): -1.0, (0, -1): -1.0}
ONE = {(0, 0): 1.0}
SS = {(1, 1): -0.25, (1, -1): 0.25, (-1, 1): 0.25, (-1, -1): -0.25}  # sin q_1 sin q_2
Q11 = pmul(S1, S1)
Q22 = pmul(S2, S2)
Q12 = pmul(S1, S2)


def symbol(p, q1, q2):
    out = 0
    for (x, y), v in p.items():
        out = out + v * np.exp(1j * (x * q1 + y * q2))
    return np.real(out)


def main_model(rho):
    """Kernels f, g, u at this rho, orders 4, 2, 0, with rho of order 2."""
    f = {
        (0, 0): padd(pscale(0.5, Q12), pscale(0.3, Q11), pscale(0.1, Q22), pscale(0.4 * rho, S1), pscale(0.15 * rho * rho, ONE)),
        (1, 1): padd(pscale(0.2, Q12), pscale(0.5, Q22), pscale(0.1, Q11), pscale(0.2 * rho, S2), pscale(0.1 * rho, S1), pscale(0.25 * rho * rho, ONE)),
        "perp": padd(pscale(0.2, Q11), pscale(0.1, Q12), pscale(0.3 * rho, S2), pscale(0.1 * rho * rho, ONE)),
    }
    g = {
        (0, 0): pscale(0.3, SS),
        (1, 1): pscale(-0.2, SS),
        (0, 1): pscale(0.4j, padd(S1, pscale(0.5, S2), pscale(rho, ONE))),
        (1, 0): pscale(-0.4j, padd(S1, pscale(0.5, S2), pscale(rho, ONE))),
    }
    u = {
        (0, 0): padd(pscale(0.3, ONE), pscale(0.05, S1)),
        (1, 1): padd(pscale(0.2, ONE), pscale(0.05, S2)),
        "perp": pscale(0.1, ONE),
    }
    return f, g, u


def control_model(rho):
    f = {(0, 0): pscale(0.6, S1), (1, 1): pscale(0.2, S2), "perp": pscale(0.3 * rho, ONE)}
    return f, {}, {}


class Alg:
    def __init__(self, N, m, k1=0.0, k2=0.0):
        self.N, self.m = N, m
        self.theta = 2 * np.pi * m / N
        self.k1, self.k2 = k1, k2
        self.j = np.arange(N)
        self.T1 = self.op({(1, 0): 1.0})
        self.T2 = self.op({(0, 1): 1.0})
        self.I = np.eye(N, dtype=complex)
        self.X12 = self.op(padd(S1, S2))
        self.dX = [-(self.T1 - self.T1.conj().T), -(self.T2 - self.T2.conj().T)]
        self.D = [self.T1 - self.I, self.T2 - self.I]
        self.Ds = [d.conj().T for d in self.D]
        self.dD = [[self.T1, 0 * self.I], [0 * self.I, self.T2]]  # dD[a][mu] = delta_a D_mu
        self.dDs = [[-self.T1.conj().T, 0 * self.I], [0 * self.I, -self.T2.conj().T]]

    def op(self, poly, weight=None):
        """Op_theta(kernel): W_y e_j = e^{-i theta y1 y2 / 2} e^{i (k1 y1 + k2 y2)} w^{-j y2} e_{j + y1}."""
        N, th = self.N, self.theta
        out = np.zeros((N, N), dtype=complex)
        for (y1, y2), v in poly.items():
            c = v if weight is None else v * weight(y1, y2)
            if c == 0:
                continue
            ph = np.exp(1j * (-th * y1 * y2 / 2 + self.k1 * y1 + self.k2 * y2)) * np.exp(-1j * th * self.j * y2)
            out[(self.j + y1) % N, self.j] += c * ph
        return out

    def dop(self, poly, a):
        return self.op(poly, weight=(lambda y1, y2: (y1, y2)[a]))

    def ddop(self, poly, a, b):
        return self.op(poly, weight=(lambda y1, y2: (y1, y2)[a] * (y1, y2)[b]))


def build_E(alg, model, rho):
    """Returns E[key], dE[a][key] (delta_a), Edot[key], with key in (mu, nu) or 'perp'."""
    f, g, u = model(rho)
    th = alg.theta
    keys = set(f) | set(g) | set(u)
    E, dE, Ed, dEd = {}, [{}, {}], {}, [{}, {}]
    for key in keys:
        fk, gk, uk = f.get(key, {}), g.get(key, {}), u.get(key, {})
        E[key] = alg.op(fk) + th * alg.op(gk) + th * th * alg.op(uk)
        Ed[key] = alg.op(gk) + 2 * th * alg.op(uk)
        for a in (0, 1):
            dE[a][key] = alg.dop(fk, a) + th * alg.dop(gk, a) + th * th * alg.dop(uk, a)
            dEd[a][key] = alg.dop(gk, a) + 2 * th * alg.dop(uk, a)
    return E, dE, Ed, dEd


def eps_pairs():
    return ((0, 1, 1.0), (1, 0, -1.0))


def build_M(alg, E, dE, Ed, rho):
    N = alg.N
    M = np.zeros((N, N), dtype=complex)
    dM = [np.zeros((N, N), dtype=complex), np.zeros((N, N), dtype=complex)]
    Mdot = np.zeros((N, N), dtype=complex)
    for key, e in E.items():
        if key == "perp":
            M += rho * e
            Mdot += rho * Ed[key]
            for a in (0, 1):
                dM[a] += rho * dE[a][key]
            continue
        mu, nu = key
        Dsm, Dn = alg.Ds[mu], alg.D[nu]
        M += Dsm @ e @ Dn
        Mdot += Dsm @ Ed[key] @ Dn
        for a in (0, 1):
            dM[a] += alg.dDs[a][mu] @ e @ Dn + Dsm @ dE[a][key] @ Dn + Dsm @ e @ alg.dD[a][nu]
        for a, b, sg in eps_pairs():
            Mdot += (0.5j * sg) * (alg.dDs[a][mu] @ dE[b][key] @ Dn + alg.dDs[a][mu] @ e @ alg.dD[b][nu] + Dsm @ dE[a][key] @ alg.dD[b][nu])
    return M, dM, Mdot


def elements(alg, model, rho):
    E, dE, Ed, dEd = build_E(alg, model, rho)
    M, dM, Mdot = build_M(alg, E, dE, Ed, rho)
    X = alg.X12 + rho * alg.I
    G = np.linalg.inv(X)
    Y = G @ M @ G
    dG = [-G @ alg.dX[a] @ G for a in (0, 1)]
    Gdot = np.zeros_like(G)
    for a, b, sg in eps_pairs():
        Gdot += (0.5j * sg) * G @ alg.dX[a] @ G @ alg.dX[b] @ G
    dY = [dG[a] @ M @ G + G @ dM[a] @ G + G @ M @ dG[a] for a in (0, 1)]
    Ydot = Gdot @ M @ G + G @ Mdot @ G + G @ M @ Gdot
    for a, b, sg in eps_pairs():
        Ydot += (0.5j * sg) * (dG[a] @ dM[b] @ G + dG[a] @ M @ dG[b] + G @ dM[a] @ dG[b])
    return dict(E=E, dE=dE, Ed=Ed, M=M, X=X, G=G, Y=Y, dY=dY, Ydot=Ydot)


def logdet_r(alg, model, rho):
    el = elements(alg, model, rho)
    r = alg.I + el["Y"]
    r = 0.5 * (r + r.conj().T)
    c = np.linalg.cholesky(r)
    return 2 * float(np.sum(np.log(np.real(np.diag(c))))) / alg.N


def L0_at(model, rho, q, w):
    f, g, u = model(rho)
    Q1, Q2 = np.meshgrid(q, q, indexing="ij")
    s1, s2 = 2 - 2 * np.cos(Q1), 2 - 2 * np.cos(Q2)
    num = s1 * symbol(f[(0, 0)], Q1, Q2) + s2 * symbol(f[(1, 1)], Q1, Q2) + rho * symbol(f["perp"], Q1, Q2)
    Y0 = num / (s1 + s2 + rho) ** 2
    return float(np.sum(np.outer(w, w) * np.log1p(Y0)))


def graded_grid(n):
    x, w = np.polynomial.legendre.leggauss(n)
    v = 0.5 * (x + 1)
    q = np.pi * v**3
    wq = 0.5 * w * np.pi * 3 * v**2 / np.pi  # integral over (-pi, pi) d q / (2 pi) = 2 * integral_0^pi d q / (2 pi)
    return q, wq


NODES = 48


def rho_nodes():
    x, w = np.polynomial.legendre.leggauss(NODES)
    u = 0.5 * (x + 1)
    bary = (-1.0) ** np.arange(NODES) * np.sqrt((1 - x**2) * w)
    return u, x, bary


def transverse_weights():
    """Weights W_i with integral d p_3 d p_4 / (2 pi)^2 F(rho) = sum W_i F(rho_i), through interpolation in u = (rho/8)^(1/4)."""
    u, x, bary = rho_nodes()
    q, wq = graded_grid(500)
    P3, P4 = np.meshgrid(q, q, indexing="ij")
    rho = (2 - 2 * np.cos(P3)) + (2 - 2 * np.cos(P4))
    xi = 2 * (rho / 8) ** 0.25 - 1
    ww = np.outer(wq, wq)
    W = np.zeros(NODES)
    den = np.zeros_like(xi)
    terms = []
    for i in range(NODES):
        t = bary[i] / (xi - x[i])
        den += t
        terms.append(t)
    for i in range(NODES):
        W[i] = float(np.sum(ww * terms[i] / den))
    return W, 8 * u**4


def F_check():
    ok = True
    N = 251
    for m in (3, 5):
        for rho in (0.05, 0.5):
            model = main_model
            alg = Alg(N, m)
            el = elements(alg, model, rho)
            r = alg.I + el["Y"]
            r = 0.5 * (r + r.conj().T)
            lam, V = np.linalg.eigh(r)
            R = (V / lam) @ V.conj().T
            first = np.trace(R @ el["Ydot"]) / N
            da = [V.conj().T @ el["dY"][a] @ V for a in (0, 1)]
            # int_0^infty ds tau(S da S db S) = sum_ij da_ij db_ji I(lam_i, lam_j), I(a, b) := int ds / ((a + s)^2 (b + s)).
            la, lb = np.meshgrid(lam, lam, indexing="ij")
            diff = la - lb
            with np.errstate(divide="ignore", invalid="ignore"):
                I = (la * np.log(la / lb) - diff) / (la * diff**2)
                I = np.where(np.abs(diff) < 1e-4, 1 / (2 * la * la), I)
            second = 0.0
            for a, b, sg in eps_pairs():
                second += -(0.5j * sg) * np.sum(da[a] * da[b].T * I) / N
            formula = complex(first + second)
            dth = 2 * np.pi / N
            vals = [logdet_r(Alg(N, m + d), model, rho) for d in (-2, -1, 1, 2)]
            fd = (vals[0] - 8 * vals[1] + 8 * vals[2] - vals[3]) / (12 * dth)
            good = abs(formula - fd) <= 1e-6 + 1e-3 * abs(fd)
            ok = ok and good
            print(f" F N={N} m={m} rho={rho}: formula={formula.real:.8f}{formula.imag:+.1e}i (tau R dY {complex(first).real:.8f}, second {complex(second).real:.8f}) difference quotient={fd:.8f}: {good}", flush=True)
    return ok


def B_check():
    ok = True
    ss = (-2.5, -1.5, -0.5, 0.0, 0.5, 1.5, 2.5)
    table = {}
    for N in (61, 509):
        alg = Alg(N, 1)
        el = elements(alg, main_model, 0.0)
        lam, V = np.linalg.eigh(alg.X12)
        fns = {
            "T_1": (alg.T1, 0),
            "D_1": (alg.D[0], 1),
            "D_1^*": (alg.Ds[0], 1),
            "delta_1 X": (alg.dX[0], 1),
            "E_11": (el["E"][(0, 0)], 4),
            "delta_1 E_11": (el["dE"][0][(0, 0)], 3),
            "dE_11": (el["Ed"][(0, 0)], 2),
            "Y": (el["Y"], 2),
            "dY": (el["Ydot"], 0),
        }
        f00, g00, u00 = main_model(0.0)
        th = alg.theta
        fns["delta_1 delta_2 E_11"] = (alg.ddop(f00[(0, 0)], 0, 1) + th * alg.ddop(g00[(0, 0)], 0, 1) + th * th * alg.ddop(u00[(0, 0)], 0, 1), 2)
        for name, (B, m) in fns.items():
            best = 0.0
            Bt = V.conj().T @ B @ V
            for s in ss:
                A = (lam**s)[:, None] * Bt * (lam ** (-s - m / 2))[None, :]
                best = max(best, float(np.linalg.norm(A, 2)))
                guard()
            table[(name, N)] = best
    for name in sorted({k[0] for k in table}):
        a, b = table[(name, 61)], table[(name, 509)]
        good = b <= 1.5 * a
        ok = ok and good
        print(f" B {name}: max_s n at N=61 {a:.3f}, at N=509 {b:.3f}: {good}", flush=True)
    return ok


def run_Q(model, label, W, rhos):
    q, wq = graded_grid(300)
    L0 = np.array([L0_at(model, r, q, wq) for r in rhos])
    Qs = {}
    for N in (61, 127, 251, 509):
        alg = Alg(N, 1)
        Lt = np.array([logdet_r(alg, model, r) for r in rhos])
        val = float(np.sum(W * (Lt - L0)))
        Qs[N] = val / alg.theta**2
        guard()
        print(f" {label} N={N} theta={alg.theta:.5f}: L-L0={val:.6e} Q={Qs[N]:.6f} rss={rss_gb():.2f}GB", flush=True)
    d1, d2, d3 = Qs[127] - Qs[61], Qs[251] - Qs[127], Qs[509] - Qs[251]
    return Qs, d1, d2, d3


def main():
    ok = True
    print("A", flush=True)
    for N in (17, 31, 61, 127, 251, 509):
        alg = Alg(N, 1)
        bot = float(np.linalg.eigvalsh(alg.X12)[0])
        good = bot >= alg.theta / 2
        ok = ok and good
        print(f" A N={N} theta={alg.theta:.5f}: bottom={bot:.6f} bottom/theta={bot / alg.theta:.4f}: {good}", flush=True)
    print("K", flush=True)
    _, rhos = transverse_weights()
    for N in (61, 127):
        for i in (0, 5, 20):
            a = logdet_r(Alg(N, 1), main_model, rhos[i])
            b = logdet_r(Alg(N, 1, np.pi / N, np.pi / N), main_model, rhos[i])
            good = abs(a - b) <= 1e-9
            ok = ok and good
            print(f" K N={N} rho={rhos[i]:.2e}: |diff|={abs(a - b):.1e}: {good}", flush=True)
    print("F", flush=True)
    ok = F_check() and ok
    print("B", flush=True)
    ok = B_check() and ok
    print("C", flush=True)
    W, rhos = transverse_weights()
    print(f" control on the transverse weights: sum W={np.sum(W):.10f}, mean of rho={np.sum(W * rhos):.8f} (exact 4)", flush=True)
    Qs, d1, d2, d3 = run_Q(main_model, "main", W, rhos)
    good = abs(d3) <= 0.8 * abs(d2) or abs(d3) <= 0.01 * abs(Qs[509])
    ok = ok and good
    print(f" C differences {d1:.5f} {d2:.5f} {d3:.5f}: {good}", flush=True)
    print("D", flush=True)
    Qc, d1, d2, d3 = run_Q(control_model, "control", W, rhos)
    ctrl = abs(d3) >= 0.8 * abs(d2) and d2 * d3 > 0
    print(f" D differences {d1:.5f} {d2:.5f} {d3:.5f}: control shows growth: {ctrl}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
