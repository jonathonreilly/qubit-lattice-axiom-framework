"""F1-F7 of CRITERIA.md. Plane-wave cubic form, (3.4), soft limit, d dependence, isotropic kernel."""
import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(777)
I = 1j


def khat(k):
    return 2 * np.sin(k / 2)


def direct_form(a1, a2, a3, k1, k2, k3):
    """Sum of V_p over the plaquettes at one site, actual (not tilde) polarisations."""
    d = len(k1)
    tot = 0
    for mu in range(d):
        for nu in range(mu + 1, d):
            inc = []
            for a, k in ((a1, k1), (a2, k2), (a3, k3)):
                inc.append([a[mu], a[nu] * np.exp(I * k[mu]), -a[mu] * np.exp(I * k[nu]), -a[nu]])
            P = [sum(x) for x in inc]
            for s in range(4):
                for t in range(s + 1, 4):
                    M = np.array([[P[j], inc[j][s], inc[j][t]] for j in range(3)])
                    tot += np.linalg.det(M)
    return tot


def to_actual(atil, k):
    return atil * np.exp(I * k / 2)


def form(a1, a2, a3, k1, k2, k3):
    """bracket of Lemma 3.6, tilde polarisations. sum V_p = -2i form."""
    D1, D2, D3 = np.cos(k1 / 2), np.cos(k2 / 2), np.cos(k3 / 2)
    Y12, Y23, Y31 = 2 * np.sin((k1 - k2) / 2), 2 * np.sin((k2 - k3) / 2), 2 * np.sin((k3 - k1) / 2)
    return (np.sum(a1 * D3 * a2) * np.sum(Y12 * a3) + np.sum(a2 * D1 * a3) * np.sum(Y23 * a1)
            + np.sum(a3 * D2 * a1) * np.sum(Y31 * a2))


def cplx(d):
    return rng.normal(size=d) + I * rng.normal(size=d)


def proj_perp(v, n):
    return v - n * (v @ n) / (n @ n)


def F1(d=4, n=500):
    worst = 0
    for _ in range(n):
        k1, k2 = rng.uniform(-np.pi, np.pi, d), rng.uniform(-np.pi, np.pi, d)
        k3 = -k1 - k2
        a1, a2, a3 = cplx(d), cplx(d), cplx(d)
        dv = direct_form(to_actual(a1, k1), to_actual(a2, k2), to_actual(a3, k3), k1, k2, k3)
        fm = -2 * I * form(a1, a2, a3, k1, k2, k3)
        worst = max(worst, abs(dv - fm) / abs(fm))
    print(f"F1 d={d} closed form vs direct, worst rel {worst:.2e} {'PASS' if worst<1e-12 else 'FAIL'}")


eps3 = np.zeros((3, 3, 3))
eps3[0, 1, 2] = eps3[1, 2, 0] = eps3[2, 0, 1] = 1
eps3[0, 2, 1] = eps3[2, 1, 0] = eps3[1, 0, 2] = -1


def Z_direct(E1, E2, E3, k1, k2, k3):
    """E_i: arrays shape (3,3,d) colour a,f then polarisation. eps_abc eps_fgh form(E1^af, E2^bg, E3^ch)."""
    tot = 0
    for a, b, c in np.argwhere(eps3 != 0):
        for f, g, h in np.argwhere(eps3 != 0):
            tot += eps3[a, b, c] * eps3[f, g, h] * form(E1[a, f], E2[b, g], E3[c, h], k1, k2, k3)
    return tot


def aMN(M, N):
    return np.trace(M) * np.trace(N) - np.trace(M @ N)


def F2(d=4, n=100):
    worst = 0
    for _ in range(n):
        k1, k2 = rng.uniform(-np.pi, np.pi, d), rng.uniform(-np.pi, np.pi, d)
        k3 = -k1 - k2
        ks = [k1, k2, k3]
        kh = [khat(k) for k in ks]
        ksq = [x @ x for x in kh]
        vs = [proj_perp(cplx(d), kh[i]) for i in range(3)]
        hs = [rng.normal(size=(3, 3)) + I * rng.normal(size=(3, 3)) for _ in range(3)]
        Es = []
        for i in range(3):
            E = np.zeros((3, 3, d), dtype=complex)
            for a in range(3):
                E[a, a] += vs[i] / ksq[i]
                for f in range(3):
                    E[a, f] += kh[i] * hs[i][a, f]
            Es.append(E)
        lhs = Z_direct(*Es, *ks)
        D = [np.cos(k / 2) for k in ks]
        us = [vs[i] / ksq[i] for i in range(3)]
        rhs = 6 * form(us[0], us[1], us[2], *ks)
        ts = [np.trace(h) for h in hs]
        lam = [np.sum(vs[0] * D[2] * kh[1]), np.sum(vs[1] * D[0] * kh[2]), np.sum(vs[2] * D[1] * kh[0])]
        for (i, j, l) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
            rhs += 2 * ts[l] * np.sum(vs[i] * D[l] * vs[j]) * (1 / ksq[i] - 1 / ksq[j])
            rhs -= aMN(hs[j], hs[l]) * lam[i]
        worst = max(worst, abs(lhs - rhs) / abs(lhs))
    print(f"F2 d={d} (3.4) vs direct colour contraction, worst rel {worst:.2e} {'PASS' if worst<1e-11 else 'FAIL'}")


def F3(d=4):
    worst = 0
    for _ in range(100):
        k = rng.uniform(-2, 2, d)
        a1 = proj_perp(cplx(d), khat(k))
        a2 = proj_perp(cplx(d), khat(k))
        H = lambda q: khat(q) @ khat(q) * np.eye(d) - np.outer(khat(q), khat(q))
        for nu in range(d):
            h = 1e-6
            ep = np.zeros(d)
            ep[nu] = h
            fd = (a2 @ H(k + ep) @ a1 - a2 @ H(k - ep) @ a1) / (2 * h)
            ev = np.zeros(d)
            ev[nu] = 1
            lhs = form(a1, a2, ev, k, -k, 0 * k)
            worst = max(worst, abs(lhs - fd) / max(1e-9, abs(fd)))
    print(f"F3 soft identity (3.6) at level 0 by finite difference, worst rel {worst:.2e} {'PASS' if worst<1e-5 else 'FAIL'}")


def F4():
    worst = 0
    for _ in range(200):
        k1, k2 = rng.uniform(-np.pi, np.pi, 2), rng.uniform(-np.pi, np.pi, 2)
        k3 = -k1 - k2
        a = [np.array([z, 0], dtype=complex) for z in (cplx(1)[0], cplx(1)[0], cplx(1)[0])]
        worst = max(worst, abs(form(a[0], a[1], a[2], k1, k2, k3)))
        worst = max(worst, abs(direct_form(to_actual(a[0], k1), to_actual(a[1], k2), to_actual(a[2], k3), k1, k2, k3)))
    print(f"F4 d=2 axial slice: |form| worst {worst:.2e} {'PASS' if worst<1e-12 else 'FAIL'}")


def null_real(*vs, d):
    M = np.array(vs)
    u, s, vh = np.linalg.svd(M)
    return vh[len(vs):].T  # columns


def axial_field(v, k):
    """colour isotropic slice E_last = 0, E = v / khat^2 + khat h, h = -v_d / (khat^2 khat_d)"""
    kh = khat(k)
    ks = kh @ kh
    h = -v[-1] / (ks * kh[-1])
    return v / ks + kh * h, h


def F56(d):
    print(f"--- axial slice in d={d}: k3hat^2 * Z on v1 in S1^0, v2 in S2^0, v3 in Q, and the full form at finite k3")
    for trial in range(3):
        k = rng.normal(size=d)
        k *= 0.6 / np.linalg.norm(k)
        qdir = rng.normal(size=d)
        qdir /= np.linalg.norm(qdir)
        for eta in (1e-1, 1e-2, 1e-3, 1e-4):
            k3 = eta * qdir
            k1 = k
            k2 = -k1 - k3
            kh1, kh2, kh3 = khat(k1), khat(k2), khat(k3)
            D1, D2, D3 = np.cos(k1 / 2), np.cos(k2 / 2), np.cos(k3 / 2)
            # S1^0 = {khat1, D3 khat2}^perp; S2^0 = {khat2, D1 khat3}^perp; Q = {khat3, e_d}^perp
            B1 = null_real(kh1, D3 * kh2, d=d)
            B2 = null_real(kh2, D1 * kh3, d=d)
            ed = np.zeros(d)
            ed[-1] = 1
            B3 = null_real(kh3, ed, d=d)
            mx = 0
            val = None
            for i in range(B1.shape[1]):
                for j in range(B2.shape[1]):
                    for l in range(B3.shape[1]):
                        E1, _ = axial_field(B1[:, i], k1)
                        E2, _ = axial_field(B2[:, j], k2)
                        E3, _ = axial_field(B3[:, l], k3)
                        z = 6 * form(E1, E2, E3, k1, k2, k3) * (kh3 @ kh3)
                        mx = max(mx, abs(z))
            # full slice: generic members of slice, unrestricted (no S^0)
            Bf1 = null_real(kh1, d=d)
            Bf2 = null_real(kh2, d=d)
            Bf3 = null_real(kh3, d=d)
            mf = 0
            for i in range(Bf1.shape[1]):
                for j in range(Bf2.shape[1]):
                    for l in range(Bf3.shape[1]):
                        E1, _ = axial_field(Bf1[:, i], k1)
                        E2, _ = axial_field(Bf2[:, j], k2)
                        E3, _ = axial_field(Bf3[:, l], k3)
                        mf = max(mf, abs(6 * form(E1, E2, E3, k1, k2, k3) * (kh3 @ kh3)))
            print(f"  trial {trial} eta={eta:.0e}: max |k3^2 Z| restricted {mx:.3e}; unrestricted {mf:.3e}")


def F7():
    d = 4
    print("--- F7 isotropic kernel")
    for trial in range(4):
        k = rng.normal(size=d)
        k *= 0.5 / np.linalg.norm(k)
        q = rng.normal(size=d)
        q /= np.linalg.norm(q)
        kh = khat(k)
        D = np.cos(k / 2)
        sk = np.sin(k)
        P = null_real(kh, D * q, d=d)  # columns e1, e2 of P_k (eta -> 0)
        S = null_real(q, d=d)  # columns: basis of S_{k3} (eta -> 0 direction)
        ksq2 = (kh @ kh) ** 2
        # basis of symmetric quadratics in v = x e1 + y e2 : xx, xy, yy
        # R(v, v3) = 12 (v,v) (v3, sk)/k^4 + 2 phi(v) (v3, D v)
        def resid(phi, Qb):
            out = []
            e1, e2 = P[:, 0], P[:, 1]
            for l in range(Qb.shape[1]):
                v3 = Qb[:, l]
                al = 12 * (v3 @ sk) / ksq2
                c1, c2 = 2 * (v3 @ (D * e1)), 2 * (v3 @ (D * e2))
                out += [al + phi[0] * c1, phi[0] * c2 + phi[1] * c1, al + phi[1] * c2]
            return np.array(out)
        # (a) the gap: phi with isotropic kernel v = e1 + i e2: at that v the equation is 0 = 0
        v = P[:, 0] + I * P[:, 1]
        print(f"  trial {trial}: (v,v) at isotropic v = {abs(v @ v):.1e}: displayed equation at this v carries no information")

        def best(Qb):
            A = []
            b = []
            e1, e2 = P[:, 0], P[:, 1]
            for l in range(Qb.shape[1]):
                v3 = Qb[:, l]
                al = 12 * (v3 @ sk) / ksq2
                c1, c2 = 2 * (v3 @ (D * e1)), 2 * (v3 @ (D * e2))
                A += [[c1, 0], [c2, c1], [0, c2]]
                b += [-al, 0, -al]
            A = np.array(A, dtype=complex)
            b = np.array(b, dtype=complex)
            phi, *_ = np.linalg.lstsq(A, b, rcond=None)
            return np.linalg.norm(A @ phi - b), phi

        # param Q = ker t in S (3 dim), t complex unit in the basis of S. dist(Q, P_k): how far t is from the normal of P_k in S
        kperp = S.T @ sk
        kperp = kperp / np.linalg.norm(kperp)  # coordinates of sin k direction in S; P_k = its orthogonal complement in S (to O(k^2))

        def obj(z):
            t = z[:3] + I * z[3:]
            t = t / np.linalg.norm(t)
            Qc = np.linalg.svd(t.reshape(1, 3))[2].conj().T[:, 1:]  # null space of bilinear t. : conj handling below
            Qb = S @ Qc
            r, _ = best(Qb)
            dist = np.sqrt(max(1e-30, 1 - abs(np.sum(t.conj() * kperp)) ** 2))
            return r / dist, r, dist

        # minimise r/dist over t
        bestv = np.inf
        for s in range(60):
            z0 = rng.normal(size=6)
            res = minimize(lambda z: obj(z)[0], z0, method="Nelder-Mead", options={"maxiter": 3000, "xatol": 1e-5, "fatol": 1e-8})
            if res.fun < bestv:
                bestv = res.fun
                zb = res.x
        _, r, dist = obj(zb)
        print(f"  trial {trial}: min over Q, phi of residual / dist(Q,P_k) = {bestv:.3f} at residual {r:.3f}, dist {dist:.3f}; typical size 12|sin k|/k^4 = {12*np.linalg.norm(sk)/ksq2:.1f}; compare 12 k_perp/k^4 = {12*np.linalg.norm(S.T@sk)/ksq2:.1f}")


if __name__ == "__main__":
    F1(4)
    F1(3)
    F1(2)
    F2(4)
    F2(3)
    F3()
    F4()
    F56(3)
    F56(4)
    F7()
