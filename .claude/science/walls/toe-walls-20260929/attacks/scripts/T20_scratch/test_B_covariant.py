"""Test B: all translation-invariant, Hermitian, finite-range one-particle laws on l2(Z^3) x C^2 that are
covariant under the proper cubic group acting on the site lattice AND on the qubit by one of the four
soldering actions. Report the covariant space and its band-touching structure."""
import itertools
import sys
import numpy as np
from scipy.optimize import least_squares
from common import O, KINDS, rho, su2_of_rotation, SIG, I2

rng = np.random.default_rng(20)


def hop_set(rng_inf):
    return [np.array(v) for v in itertools.product(range(-rng_inf, rng_inf + 1), repeat=3) if any(v)]


def hop_set_nn():
    out = []
    for i in range(3):
        for s in (1, -1):
            v = [0, 0, 0]; v[i] = s; out.append(np.array(v))
    return out


def build(kind, V, extra_internal_invariance=False):
    """Return (basis, meta): basis = list of (C, {v: A_v}) spanning the covariant space."""
    keyv = lambda v: tuple(int(x) for x in v)
    Vp = [v for v in V if next(x for x in v if x != 0) > 0]      # representatives
    nparam = 4 + 8 * len(Vp)

    def unpack(x):
        c = x[:4]
        C = c[0] * I2 + c[1] * SIG[0] + c[2] * SIG[1] + c[3] * SIG[2]      # Hermitian
        A = {}
        for j, v in enumerate(Vp):
            y = x[4 + 8 * j: 4 + 8 * j + 8]
            M = np.array([[y[0] + 1j * y[1], y[2] + 1j * y[3]], [y[4] + 1j * y[5], y[6] + 1j * y[7]]])
            A[keyv(v)] = M
            A[keyv(-v)] = M.conj().T
        return C, A

    Us = {i: su2_of_rotation(rho(kind, g)) for i, g in enumerate(O)}

    def constraints(x):
        C, A = unpack(x)
        res = []
        for i, g in enumerate(O):
            U = Us[i]
            D = C - U @ C @ U.conj().T
            res += [D.real.flatten(), D.imag.flatten()]
            for v in V:
                gv = g @ v
                D = A[keyv(gv)] - U @ A[keyv(v)] @ U.conj().T
                res += [D.real.flatten(), D.imag.flatten()]
        if extra_internal_invariance:
            for s in SIG:
                D = s @ C - C @ s
                res += [D.real.flatten(), D.imag.flatten()]
                for v in V:
                    D = s @ A[keyv(v)] - A[keyv(v)] @ s
                    res += [D.real.flatten(), D.imag.flatten()]
        return np.concatenate(res)

    # linear map: build matrix column by column
    cols = [constraints(np.eye(nparam)[j]) for j in range(nparam)]
    M = np.array(cols).T
    u, sv, vt = np.linalg.svd(M)
    rank = int((sv > 1e-9).sum())
    null = vt[rank:]
    basis = [unpack(n) for n in null]
    return basis, unpack


def Hk(C, A, k):
    H = C.astype(complex).copy()
    for v, M in A.items():
        H = H + M * np.exp(1j * float(np.dot(k, v)))
    return H


def dvec(C, A, k):
    H = Hk(C, A, k)
    return np.array([0.5 * np.trace(s @ H).real for s in SIG]), 0.5 * np.trace(H).real


def jac(C, A, k, h=1e-6):
    J = np.zeros((3, 3))
    for m in range(3):
        e = np.zeros(3); e[m] = h
        J[:, m] = (dvec(C, A, k + e)[0] - dvec(C, A, k - e)[0]) / (2 * h)
    return J


def combo(basis):
    w = rng.normal(size=len(basis))
    C = sum(wi * b[0] for wi, b in zip(w, basis))
    keys = basis[0][1].keys()
    A = {v: sum(wi * b[1][v] for wi, b in zip(w, basis)) for v in keys}
    return C, A


def component_rank(C, A, N=400):
    ks = rng.uniform(-np.pi, np.pi, size=(N, 3))
    D = np.array([dvec(C, A, k)[0] for k in ks])
    sv = np.linalg.svd(D, compute_uv=False)
    return int((sv > 1e-7 * max(sv[0], 1e-12)).sum()) if sv[0] > 1e-9 else 0, sv


def find_nodes(C, A, starts=400):
    found = []
    for _ in range(starts):
        k0 = rng.uniform(-np.pi, np.pi, size=3)
        r = least_squares(lambda k: dvec(C, A, k)[0], k0, method="lm", xtol=1e-14, ftol=1e-14, gtol=1e-14)
        if np.linalg.norm(r.fun) < 1e-9:
            k = (r.x + np.pi) % (2 * np.pi) - np.pi
            if not any(np.linalg.norm(((k - q + np.pi) % (2 * np.pi)) - np.pi) < 1e-5 for q in found):
                found.append(k)
    return found


def report_nodes(C, A, nodes):
    rows = []
    for k in nodes:
        J = jac(C, A, k)
        sv = np.linalg.svd(J, compute_uv=False)
        chi = int(np.sign(np.linalg.det(J))) if sv[-1] > 1e-6 else 0
        rows.append((k, sv, chi))
    return rows


if __name__ == "__main__":
    V_nn = hop_set_nn()
    print("=" * 78)
    print("NEAREST-NEIGHBOUR hops (6 directions)")
    for kind in KINDS:
        basis, unpack = build(kind, V_nn)
        print(f"\n-- action {kind}: covariant space dimension (real) = {len(basis)}")
        # generic member
        for trial in range(3):
            C, A = combo(basis)
            r, sv = component_rank(C, A)
            nodes = find_nodes(C, A, 250) if r == 3 else []
            rows = report_nodes(C, A, nodes)
            iso = [x for x in rows if x[1][-1] > 1e-6]
            print(f"   member {trial}: #independent d-components r = {r}; zero set found: {len(nodes)} pts; isolated rank-3 nodes: {len(iso)}")
            if kind == "full" and trial == 0:
                for k, sv_, chi in sorted(rows, key=lambda t: tuple(np.round(np.abs(t[0]), 3))):
                    print(f"      node k/pi = {np.round(k/np.pi, 4)}  chirality {chi:+d}  Jacobian singular values {np.round(sv_, 4)}")
                chis = [x[2] for x in rows]
                print(f"      total chirality = {sum(chis)},  #(+) = {chis.count(1)}, #(-) = {chis.count(-1)}")
        if kind == "full":
            # identify the family: fit d(k) = a sin k, d0 = e0 + e1 sum cos k
            C, A = combo(basis)
            ks = rng.uniform(-np.pi, np.pi, size=(50, 3))
            X = []; y = []
            for k in ks:
                d, d0 = dvec(C, A, k)
                X.append(np.concatenate([np.eye(3) * 0 + np.diag(np.sin(k))] )) ; y.append(d)
            # least squares: d_i = a sin k_i  (one unknown a)
            Xa = np.concatenate([np.sin(k) for k in ks]); ya = np.concatenate([dvec(C, A, k)[0] for k in ks])
            a = (Xa @ ya) / (Xa @ Xa)
            resid = np.linalg.norm(ya - a * Xa)
            X0 = np.array([[1, np.sum(np.cos(k))] for k in ks]); y0 = np.array([dvec(C, A, k)[1] for k in ks])
            sol, res, *_ = np.linalg.lstsq(X0, y0, rcond=None)
            print(f"   family check: d(k) = a sin k with a = {a:.5f}, residual {resid:.2e};  d0(k) = e0 + e1 sum cos k with (e0,e1) = {np.round(sol,5)}, residual {np.linalg.norm(X0@sol-y0):.2e}")
        # basis: d(0) and Jacobian at Gamma
        worst_d0 = 0; Js = []
        for (C, A) in basis:
            d, d0 = dvec(C, A, np.zeros(3)); worst_d0 = max(worst_d0, np.linalg.norm(d))
            Js.append(jac(C, A, np.zeros(3)))
        print(f"   basis: max |d(Gamma)| = {worst_d0:.2e};  max |Jacobian at Gamma| = {max(np.abs(J).max() for J in Js):.2e}")

    print("\n" + "=" * 78)
    print("STRONG READING of 'no possibility is privileged' (invariance under ALL internal rotations) + full soldering, NN")
    basis, _ = build("full", V_nn, extra_internal_invariance=True)
    print("   covariant-and-internally-invariant space dimension:", len(basis))
    if basis:
        worst = 0
        for (C, A) in basis:
            for k in rng.uniform(-np.pi, np.pi, size=(20, 3)):
                worst = max(worst, np.linalg.norm(dvec(C, A, k)[0]))
        print("   max |d(k)| over basis and 20 random k (0 means no sigma-dependence, i.e. a = 0):", f"{worst:.2e}")

    for R in (1, 2):
        print("\n" + "=" * 78)
        V = hop_set(R)
        print(f"RANGE |v|_inf <= {R} ({len(V)} hop vectors): covariant spaces and behaviour at Gamma")
        for kind in KINDS:
            basis, _ = build(kind, V)
            maxd0 = 0; maxJ = 0; offdiag = 0; a_vals = []
            for (C, A) in basis:
                d, _ = dvec(C, A, np.zeros(3)); maxd0 = max(maxd0, np.linalg.norm(d))
                J = jac(C, A, np.zeros(3)); maxJ = max(maxJ, np.abs(J).max())
                if kind == "full":
                    offdiag = max(offdiag, np.abs(J - np.eye(3) * np.trace(J) / 3).max())
                    a_vals.append(np.trace(J) / 3)
            extra = f";  max deviation of J(Gamma) from a*Identity = {offdiag:.2e}" if kind == "full" else ""
            print(f"   {kind:8s}: dim = {len(basis):3d};  max|d(Gamma)| = {maxd0:.2e};  max|J(Gamma)| = {maxJ:.2e}{extra}")
