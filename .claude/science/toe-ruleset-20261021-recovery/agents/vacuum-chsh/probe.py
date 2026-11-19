#!/usr/bin/env python3
"""Vacuum CHSH vs separation on the half-filled staggered sea (supplied model).

Free-fermion Gaussian state; block reduced states are built from the correlation
matrix C_ij = <c_i^dag c_j>, never from a many-body ground state.
See criteria.md (pre-registered) for definitions and tolerances.
"""
import os
for v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
          "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import sys
import itertools
import numpy as np

RNG = np.random.default_rng(20261027)

# ---------------------------------------------------------------- lattice sea
def eta(mu, x):
    """KS phase eta_mu(x) = (-1)^{x_0+...+x_{mu-1}}."""
    return -1.0 if (sum(x[:mu]) % 2) else 1.0


def eps(x):
    return -1.0 if (sum(x) % 2) else 1.0


def hrow(x, m):
    """Nonzero entries h[x, z] of the single-particle staggered matrix."""
    out = [(tuple(x), m * eps(x))]
    for mu in range(3):
        e = [0, 0, 0]
        e[mu] = 1
        xp = tuple(x[i] + e[i] for i in range(3))
        xm = tuple(x[i] - e[i] for i in range(3))
        out.append((xp, 0.5j * eta(mu, x)))
        out.append((xm, -0.5j * eta(mu, x)))
    return out


class Sea:
    """P_minus(x,y) = delta/2 - (1/2) sum_z h(x,z) F(z-y), F = FT of (h^2)^{-1/2}.

    Uses h^2 = sum sin^2 k + m^2 (staggered hops anticommute; eps anticommutes).
    Antiperiodic L^3 torus; F is extended antiperiodically to the covering lattice.
    """

    def __init__(self, L, m):
        self.L, self.m = L, m
        k = (2 * np.arange(L) + 1) * np.pi / L
        s2 = np.sin(k) ** 2
        f = 1.0 / np.sqrt(s2[:, None, None] + s2[None, :, None] + s2[None, None, :] + m * m)
        F = np.fft.ifftn(f)  # sum_n e^{2 pi i n z/L} f_n / L^3
        z = np.arange(L)
        ph = np.exp(1j * np.pi * z / L)
        self.F = F * ph[:, None, None] * ph[None, :, None] * ph[None, None, :]

    def Fz(self, z):
        L = self.L
        sgn = 1.0
        idx = []
        for c in z:
            q, r = divmod(c, L)
            if q % 2:
                sgn = -sgn
            idx.append(r)
        return sgn * self.F[tuple(idx)]

    def Pminus(self, x, y):
        val = 0.5 if tuple(x) == tuple(y) else 0.0
        for z, hv in hrow(x, self.m):
            val -= 0.5 * hv * self.Fz(tuple(z[i] - y[i] for i in range(3)))
        return val

    def C(self, sites):
        n = len(sites)
        P = np.array([[self.Pminus(sites[a], sites[b]) for b in range(n)] for a in range(n)])
        return P.T  # C_ij = <c_i^dag c_j> = (P_-)_{ji}


def dense_check(L=8, m=0.3):
    """Dense diagonalisation on an antiperiodic L^3 torus vs the FFT formula."""
    sites = list(itertools.product(range(L), repeat=3))
    ix = {s: i for i, s in enumerate(sites)}
    N = len(sites)
    h = np.zeros((N, N), complex)
    for x in sites:
        h[ix[x], ix[x]] += m * eps(x)
        for mu in range(3):
            y = list(x)
            y[mu] += 1
            tw = -1.0 if y[mu] == L else 1.0
            y[mu] %= L
            amp = 0.5j * eta(mu, x) * tw
            h[ix[x], ix[tuple(y)]] += amp
            h[ix[tuple(y)], ix[x]] += np.conj(amp)
    w, V = np.linalg.eigh(h)
    occ = V[:, w < 0]
    P = occ @ occ.conj().T
    sea = Sea(L, m)
    test = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 1), (2, 0, 1), (3, 2, 1)]
    err = 0.0
    for a in test:
        for b in test:
            err = max(err, abs(P[ix[a], ix[b]] - sea.Pminus(a, b)))
    return err, int((w < 0).sum()), N


# ---------------------------------------------------------------- Fock tools
def jw_ops(N):
    a = np.array([[0, 1], [0, 0]], complex)
    Z = np.diag([1.0, -1.0]).astype(complex)
    I = np.eye(2, dtype=complex)
    ops = []
    for j in range(N):
        mats = [Z] * j + [a] + [I] * (N - j - 1)
        M = mats[0]
        for t in mats[1:]:
            M = np.kron(M, t)
        ops.append(M)
    return ops


_JW = {}


def gaussian_rho(C):
    N = C.shape[0]
    if N not in _JW:
        _JW[N] = jw_ops(N)
    c = _JW[N]
    nu, U = np.linalg.eigh(C)
    D = 2 ** N
    rho = np.eye(D, dtype=complex)
    for k in range(N):
        d = sum(U[j, k] * c[j] for j in range(N))
        n = d.conj().T @ d
        rho = rho @ (nu[k] * n + (1 - nu[k]) * (np.eye(D) - n))
    rho = 0.5 * (rho + rho.conj().T)
    # reproduce C
    err = max(abs(np.trace(rho @ c[i].conj().T @ c[j]) - C[i, j])
              for i in range(N) for j in range(N))
    return rho, err, abs(np.trace(rho) - 1)


def bits(N):
    return np.array([[(s >> (N - 1 - j)) & 1 for j in range(N)] for s in range(2 ** N)])


def fermion_pt(rho, nA, nB):
    """Shapourian-Shiozaki-Ryu partial time reversal on A (JW order A then B)."""
    N = nA + nB
    B = bits(N)
    D = 2 ** N
    tauA = B[:, :nA].sum(1)
    tauB = B[:, nA:].sum(1)
    out = np.zeros_like(rho)
    wA = 2 ** nB
    for s in range(D):
        for t in range(D):
            v = rho[s, t]
            if v == 0:
                continue
            a, b = divmod(s, wA)
            ab, bb = divmod(t, wA)
            ta = tauA[s] + tauA[t]
            tb = tauB[s] + tauB[t]
            phase = (1j if ta % 2 else 1.0) * (-1.0) ** (ta * tb)
            out[ab * wA + b, a * wA + bb] += phase * v
    return out


def logneg_direct(rho, nA, nB):
    sv = np.linalg.svd(fermion_pt(rho, nA, nB), compute_uv=False)
    return float(np.log(sv.sum()))


def logneg_gauss(C, nA):
    N = C.shape[0]
    G = np.eye(N) - 2 * C
    Gp = G.astype(complex).copy()
    Gm = G.astype(complex).copy()
    Gp[:nA, :nA] = Gm[:nA, :nA] = -G[:nA, :nA]
    Gp[:nA, nA:] = 1j * G[:nA, nA:]
    Gp[nA:, :nA] = 1j * G[nA:, :nA]
    Gm[:nA, nA:] = -1j * G[:nA, nA:]
    Gm[nA:, :nA] = -1j * G[nA:, :nA]
    Gx = 0.5 * (np.eye(N) - np.linalg.solve(np.eye(N) + Gp @ Gm, Gp + Gm))
    xi = np.linalg.eigvals(Gx)
    zeta = np.linalg.eigvalsh(C)
    t1 = np.sum(np.log(np.sqrt(xi) + np.sqrt(1 - xi)))
    t2 = 0.5 * np.sum(np.log((1 - zeta) ** 2 + zeta ** 2))
    return float(np.real(t1 + t2))


def parity_diag(n):
    return np.array([(-1) ** bin(s).count("1") for s in range(2 ** n)], float)


def ssr_project(rho, nA, nB):
    pA = parity_diag(nA)
    pB = parity_diag(nB)
    p = np.kron(pA, np.ones(2 ** nB)) , np.kron(np.ones(2 ** nA), pB)
    mask = (p[0][:, None] == p[0][None, :]) & (p[1][:, None] == p[1][None, :])
    return rho * mask


# ---------------------------------------------------------------- CHSH
def horodecki(rho):
    s = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
    T = np.array([[np.real(np.trace(rho @ np.kron(a, b))) for b in s] for a in s])
    ev = np.sort(np.linalg.eigvalsh(T.T @ T))[::-1]
    return 2 * np.sqrt(ev[0] + ev[1])


def sgn(M):
    w, V = np.linalg.eigh(0.5 * (M + M.conj().T))
    return (V * np.where(w >= 0, 1.0, -1.0)) @ V.conj().T


def seesaw(rho, nA, nB, ssr, restarts=12, iters=400):
    dA, dB = 2 ** nA, 2 ** nB
    R = rho.reshape(dA, dB, dA, dB)
    pA, pB = parity_diag(nA), parity_diag(nB)
    mA = (pA[:, None] == pA[None, :]) if ssr else np.ones((dA, dA), bool)
    mB = (pB[:, None] == pB[None, :]) if ssr else np.ones((dB, dB), bool)
    vals = []
    for _ in range(restarts):
        Bs = []
        for _ in range(2):
            X = RNG.normal(size=(dB, dB)) + 1j * RNG.normal(size=(dB, dB))
            Bs.append(sgn((X + X.conj().T) * mB))
        prev = -9
        for _ in range(iters):
            M0 = np.einsum("ajbk,kj->ab", R, Bs[0] + Bs[1])
            M1 = np.einsum("ajbk,kj->ab", R, Bs[0] - Bs[1])
            A0, A1 = sgn(M0 * mA), sgn(M1 * mA)
            N0 = np.einsum("iajb,ji->ab", R, A0 + A1)
            N1 = np.einsum("iajb,ji->ab", R, A0 - A1)
            Bs = [sgn(N0 * mB), sgn(N1 * mB)]
            val = np.real(np.trace(N0 @ Bs[0]) + np.trace(N1 @ Bs[1]))
            if abs(val - prev) < 1e-13:
                break
            prev = val
        vals.append(val)
    vals = np.array(vals)
    return vals.max(), vals.max() - np.median(vals)


# ---------------------------------------------------------------- blocks
def shapes(direction):
    s1 = [(0, 0, 0)]
    s2 = [(0, 0, 0), (0, 1, 0)]
    s4 = [(0, 0, 0), (0, 1, 0), (0, 0, 1), (0, 1, 1)]
    cube = list(itertools.product(range(2), repeat=3))
    p3 = [(0, a, b) for a in range(3) for b in range(3)]
    p4 = [(0, a, b) for a in range(4) for b in range(4)]
    return {"s1": s1, "s2": s2, "s4": s4, "cube": cube, "p3x3": p3, "p4x4": p4}


def shift(block, r, n):
    return [tuple(x[i] + r * n[i] for i in range(3)) for x in block]


def disjoint(A, B):
    return not (set(A) & set(B))


# ---------------------------------------------------------------- driver
MASSES = [0.0, 0.1, 0.3, 1.0]
DIRS = {"axis": (1, 0, 0), "diag": (1, 1, 1)}
RMAX = {"axis": 16, "diag": 10}
L_MAIN = 96


def point(sea, A, B, do_chsh=True):
    nA, nB = len(A), len(B)
    C = sea.C(A + B)
    out = {"EN_g": logneg_gauss(C, nA)}
    if nA + nB <= 8:
        rho, e1, e2 = gaussian_rho(C)
        out["rho_err"] = max(e1, e2)
        out["EN"] = logneg_direct(rho, nA, nB)
        out["ESSR"] = logneg_direct(ssr_project(rho, nA, nB), nA, nB)
        if do_chsh:
            if nA == 1 and nB == 1:
                out["noSSR"] = (max(2.0, horodecki(rho)), 0.0)  # +-I settings give 2
                out["SSR"] = (2.0, 0.0)  # even 1-mode algebra is commutative
            else:
                out["noSSR"] = seesaw(rho, nA, nB, ssr=False)
                out["SSR"] = seesaw(rho, nA, nB, ssr=True)
    return out


def checks():
    print("== checks")
    for m in (0.0, 0.3):
        err, nocc, N = dense_check(8, m)
        print(f"dense L=8 m={m}: max|P_fft-P_dense|={err:.1e} filled {nocc}/{N}")
    sea = Sea(L_MAIN, 0.3)
    A = shapes("axis")["s2"]
    B = shift(A, 1, (1, 0, 0))
    C = sea.C(A + B)
    rho, e1, e2 = gaussian_rho(C)
    print(f"gaussian rho reproduces C: {e1:.1e}, trace err {e2:.1e}, "
          f"min eig {np.linalg.eigvalsh(rho).min():.1e}")
    print(f"E_N direct {logneg_direct(rho, 2, 2):.12f} gauss {logneg_gauss(C, 2):.12f}")
    for r in (1, 2, 3):
        A = shapes("axis")["s1"]
        B = shift(A, r, (1, 0, 0))
        rho, _, _ = gaussian_rho(sea.C(A + B))
        h = horodecki(rho)
        s, sp = seesaw(rho, 1, 1, ssr=False, restarts=8)
        print(f"s1 r={r}: Horodecki {h:.10f} seesaw {s:.10f} (spread {sp:.1e})")
    # see-saw self-test: one particle shared between dual rails in each block
    psi = np.zeros(16, complex)
    psi[0b0110] = psi[0b1001] = 2 ** -0.5  # |01>_A|10>_B + |10>_A|01>_B
    rt = np.outer(psi, psi.conj())
    print(f"self-test dual-rail state: SSR {seesaw(rt, 2, 2, True)[0]:.9f} "
          f"noSSR {seesaw(rt, 2, 2, False)[0]:.9f} (target 2.828427125)")
    s48, s64 = Sea(64, 0.0), Sea(96, 0.0)
    A = shapes("axis")["s4"]
    for r in (1, 5, 11):
        B = shift(A, r, (1, 0, 0))
        d = np.abs(s48.C(A + B) - s64.C(A + B)).max()
        print(f"m=0 s4 r={r}: max|C_64-C_96|={d:.1e}")


def scan(masses):
    for m in masses:
        sea = Sea(L_MAIN, m)
        print(f"\n== m={m}")
        for dname, n in DIRS.items():
            for sh in ("s1", "s2", "s4"):
                A = shapes(dname)[sh]
                rows = []
                for r in range(1, RMAX[dname] + 1):
                    B = shift(A, r, n)
                    if not disjoint(A, B):
                        continue
                    p = point(sea, A, B)
                    rows.append((r, p))
                print(f"-- {dname} {sh}: r  CHSH_SSR(best,spread)  CHSH_noSSR(best,spread)  E_N  E_SSR")
                for r, p in rows:
                    print(f"{r:3d} {p['SSR'][0]:.9f} {p['SSR'][1]:.0e}  {p['noSSR'][0]:.9f} "
                          f"{p['noSSR'][1]:.0e}  {p['EN']:.3e} {p['ESSR']:.3e}"
                          f"  |EN-ENg|={abs(p['EN']-p['EN_g']):.0e} rho_err={p['rho_err']:.0e}")
            for sh in ("cube", "p3x3", "p4x4"):
                A = shapes(dname)[sh]
                vals = []
                for r in range(1, 25 if dname == "axis" else 13):
                    B = shift(A, r, n)
                    if disjoint(A, B):
                        vals.append((r, point(sea, A, B, do_chsh=False)["EN_g"]))
                print(f"-- {dname} {sh} E_N(gauss): " +
                      " ".join(f"{r}:{v:.1e}" for r, v in vals))
        sys.stdout.flush()


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "checks"
    if mode == "checks":
        checks()
    else:
        scan([float(x) for x in sys.argv[2:]] or MASSES)
