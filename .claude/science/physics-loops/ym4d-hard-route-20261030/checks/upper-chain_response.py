#!/usr/bin/env python3
"""Criteria A1-A3: local response R_k(x) = Cov(e(y+x), G_k(y)) for iterated blocking. Usage: T beta nsweeps every seed"""
import importlib.util, itertools, os, resource, sys, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np

here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("es", os.path.join(here, "upper-chain_energy_sign.py"))
es = importlib.util.module_from_spec(spec); spec.loader.exec_module(es)
ie = es.ie
C1 = 0.5  # weight of each staple path relative to the straight path


def block(U):
    """Coarse links at even sites: straight two-link path plus six staples, quaternion mean. Input list of 4 arrays side T."""
    out = []
    for m in range(4):
        Um = U[m]
        total = ie.qmul(Um, np.roll(Um, -1, axis=m))
        for n in range(4):
            if n == m:
                continue
            Un = U[n]
            # up: U_n(x) U_m(x+n) U_m(x+n+m) U_n^+(x+2m)
            a = ie.qmul(Un, np.roll(Um, -1, axis=n))
            a = ie.qmul(a, np.roll(np.roll(Um, -1, axis=n), -1, axis=m))
            a = ie.qmul(a, ie.qconj(np.roll(Un, -2, axis=m)))
            total = total + C1 * a
            # down: U_n^+(x-n) U_m(x-n) U_m(x-n+m) U_n(x-n+2m)
            dn = np.roll(Un, 1, axis=n)
            b = ie.qmul(ie.qconj(dn), np.roll(Um, 1, axis=n))
            b = ie.qmul(b, np.roll(np.roll(Um, 1, axis=n), -1, axis=m))
            b = ie.qmul(b, np.roll(dn, -2, axis=m))
            total = total + C1 * b
        total /= np.maximum(np.linalg.norm(total, axis=-1, keepdims=True), 1e-12)
        out.append(total[::2, ::2, ::2, ::2])
    return out


def plaq_s(U):
    s = {}
    for m in range(4):
        for n in range(m + 1, 4):
            a = ie.qmul(U[m], np.roll(U[n], -1, axis=m))
            b = ie.qmul(U[n], np.roll(U[m], -1, axis=n))
            s[(m, n)] = 1 - np.sum(a * b, axis=-1)
    return s


def clover(s):
    e = 0
    for (m, n), a in s.items():
        e = e + 0.25 * (a + np.roll(a, 1, axis=m) + np.roll(a, 1, axis=n) + np.roll(np.roll(a, 1, axis=m), 1, axis=n))
    return e


def main(T, beta, nsweeps, every, seed):
    rng = np.random.default_rng(seed)
    lat = es.Torus(T, beta, rng)
    t0 = time.time()
    for _ in range(300):
        lat.sweep()
    # orbits of x under the hypercubic group about the origin
    half = T // 2
    c = np.minimum(np.arange(T), T - np.arange(T))
    grids = np.meshgrid(c, c, c, c, indexing="ij")
    key = np.sort(np.stack(grids, axis=-1), axis=-1)
    code = key[..., 0] * (half + 1) ** 3 + key[..., 1] * (half + 1) ** 2 + key[..., 2] * (half + 1) + key[..., 3]
    uniq, inv, counts = np.unique(code, return_inverse=True, return_counts=True)
    inv = inv.ravel()
    nb = 10
    levels = (1, 2)
    per = max(1, (nsweeps // every) // nb)
    prof = {k: np.zeros((nb, uniq.size)) for k in levels}
    gm = {k: np.zeros(nb) for k in levels}
    wg = {k: np.zeros(nb) for k in levels}
    em = np.zeros(nb)
    ww = np.zeros(nb)
    nmeas = 0
    for it in range(nsweeps):
        lat.sweep()
        if it % every:
            continue
        ib = min(nmeas // per, nb - 1)
        e = clover(plaq_s(lat.U))
        Fe = np.fft.fftn(e)
        em[ib] += e.mean()
        w = e.sum()
        ww[ib] += w
        V = lat.U
        for k in range(1, max(levels) + 1):
            V = block(V)
            if k in levels:
                G = clover(plaq_s(V))
                g = np.zeros((T, T, T, T))
                st = 2**k
                g[::st, ::st, ::st, ::st] = G
                ng = G.size
                # R(x) = (1/ng) sum_y e(y+x) G(y)
                corr = np.real(np.fft.ifftn(Fe * np.conj(np.fft.fftn(g)))) * (T**4 / ng) / T**4
                prof[k][ib] += np.bincount(inv, weights=corr.ravel(), minlength=uniq.size) / counts
                gm[k][ib] += G.mean()
                wg[k][ib] += w * G.mean()
        nmeas += 1
        if it % 500 == 0 and resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9 > 2.0:
            sys.exit("RSS")
    nper = np.bincount(np.minimum(np.arange(nmeas) // per, nb - 1), minlength=nb).astype(float)
    em /= nper; ww /= nper
    print(f"# T={T} beta={beta} meas={nmeas} <e>={em.mean():.5f} t={time.time()-t0:.0f}s")
    for k in levels:
        P = prof[k] / nper[:, None]
        gb = gm[k] / nper
        wgb = wg[k] / nper
        # jackknife over bins for connected profile and the sum rule
        jk = np.zeros((nb, uniq.size))
        jt = np.zeros(nb)
        for i in range(nb):
            mask = np.arange(nb) != i
            jk[i] = P[mask].mean(0) - em[mask].mean() * gb[mask].mean()
            jt[i] = wgb[mask].mean() - ww[mask].mean() * gb[mask].mean()
        R = jk.mean(0)
        err = np.sqrt((nb - 1) * jk.var(axis=0))
        total = float(np.sum(R * counts))
        terr = float(np.sqrt((nb - 1) * (jk * counts).sum(1).var()))
        cw = jt.mean(); cwerr = np.sqrt((nb - 1) * jt.var())
        z = R / np.maximum(err, 1e-30)
        i = int(np.argmin(z))
        res = np.abs(z) > 3
        print(f"k={k} sum_R={total:.5f}+-{terr:.5f} Cov(W,G)={cw:.5f}+-{cwerr:.5f} worst_z={z[i]:.2f} at orbit {tuple(key.reshape(-1,4)[np.argmax(inv==i)])} R={R[i]:.3e}")
        print(f"   resolved orbits {int(res.sum())}: pos {float(np.sum((R*counts)[res & (R>0)])):.5f} neg {float(np.sum((R*counts)[res & (R<0)])):.5f}; rho_resolved={float(np.sum((np.abs(R)*counts)[res]))/abs(total):.3f} rho_all={float(np.sum(np.abs(R)*counts))/abs(total):.3f}")
        order = np.argsort(key.reshape(-1, 4)[[np.argmax(inv == j) for j in range(uniq.size)]].sum(1))[:12]
        line = " ".join(f"{tuple(int(v) for v in key.reshape(-1,4)[np.argmax(inv==j)])}:{R[j]:.2e}({err[j]:.0e})" for j in order)
        print("   near: " + line, flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
