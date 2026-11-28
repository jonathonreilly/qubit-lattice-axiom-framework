#!/usr/bin/env python3
"""Worst linear (WAM) ratio for the flat 4d composite block constraint.
See CRITERIA.md. Single job, BLAS threads 1, stops itself above 2 GB RSS."""
import argparse, json, math, os, resource, sys, time
import numpy as np, scipy.fft as sf

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
RSS_LIMIT = 2 * 2**30

def rss_guard():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss  # bytes on darwin
    if r > RSS_LIMIT:
        sys.exit(f"stop: rss {r/2**30:.2f} GB above limit")

class Flat:
    def __init__(s, B, M, single):
        s.B, s.M, s.N = B, M, B * M
        s.rt = np.float32 if single else np.float64
        s.ct = np.complex64 if single else np.complex128
        N = s.N
        k = 2 * np.pi * np.arange(N) / N
        with np.errstate(divide='ignore', invalid='ignore'):
            D = np.where(np.arange(N) % N == 0, 1.0,
                         np.sin(B * k / 2) / (B * np.sin(k / 2)))
        D = np.where(np.abs(np.sin(k / 2)) < 1e-14, 1.0, D)
        s.e1 = (np.exp(1j * k) - 1).astype(s.ct)
        s.f1 = (B * D * np.exp(1j * k * (B - 1) / 2)).astype(s.ct)
        s.D1 = D.astype(s.rt)
        s.sh = [tuple(N if i == mu else 1 for i in range(4)) for mu in range(4)]
        s.e = [s.e1.reshape(s.sh[mu]) for mu in range(4)]
        s.f = [s.f1.reshape(s.sh[mu]) for mu in range(4)]
        prod = np.ones((N,) * 4, s.rt)
        lap = np.zeros((N,) * 4, s.rt)
        for mu in range(4):
            prod = prod * s.D1.reshape(s.sh[mu])
            lap = lap + (np.abs(s.e1) ** 2).astype(s.rt).reshape(s.sh[mu])
        s.prod = prod
        s.ilap = np.where(lap > 1e-12, 1.0 / np.where(lap > 1e-12, lap, 1), 0).astype(s.rt)
        s._gram()

    def fold(s, a):
        B, M = s.B, s.M
        return a.reshape(B, M, B, M, B, M, B, M).sum(axis=(0, 2, 4, 6))

    def tile(s, c):
        B, M = s.B, s.M
        t = np.broadcast_to(c.reshape(1, M, 1, M, 1, M, 1, M), (B, M, B, M, B, M, B, M))
        return t.reshape((s.N,) * 4)

    def q(s, mu):
        return s.prod * s.f[mu]

    def _gram(s):
        M = s.M
        G = np.zeros((M, M, M, M, 4, 4), np.complex128)
        for mu in range(4):
            qm = s.q(mu)
            for nu in range(4):
                qn = s.q(nu)
                t = -qm * s.e[mu] * np.conj(s.e[nu]) * np.conj(qn) * s.ilap * s.ilap
                if mu == nu:
                    t = t + qm * np.conj(qn) * s.ilap
                G[..., mu, nu] = s.fold(t)
        P = 2 * np.pi * np.arange(M) / M
        ep = np.exp(1j * P) - 1
        grids = np.meshgrid(ep, ep, ep, ep, indexing='ij')
        ev = np.stack(grids, axis=-1)  # e'(p), shape (...,4)
        n2 = (np.abs(ev) ** 2).sum(-1)
        Gp = np.zeros_like(G)
        it = np.ndindex(M, M, M, M)
        rank = 0
        for ix in it:
            if n2[ix] < 1e-12:
                continue
            v = ev[ix] / math.sqrt(n2[ix])
            Pi = np.eye(4) - np.outer(v, np.conj(v))
            g = Pi @ G[ix] @ Pi
            g = (g + g.conj().T) / 2
            lam, U = np.linalg.eigh(g)
            good = lam > 1e-9 * lam.max()
            rank += int(good.sum())
            Gp[ix] = (U[:, good] / lam[good]) @ U[:, good].conj().T
        s.Gp = Gp
        s.rank = rank

    def dstar(s, Fh):
        out = [0, 0, 0, 0]
        for i, (m, n) in enumerate(PAIRS):
            out[n] = out[n] + np.conj(s.e[m]) * Fh[i]
            out[m] = out[m] - np.conj(s.e[n]) * Fh[i]
        return out

    def d(s, Ah):
        return [s.e[m] * Ah[n] - s.e[n] * Ah[m] for (m, n) in PAIRS]

    def lam_from(s, Xh):
        Y = s.dstar(Xh)
        c = np.stack([s.fold(s.q(mu) * Y[mu] * s.ilap) for mu in range(4)], axis=-1)
        return np.einsum('...ij,...j->...i', s.Gp, c)

    def P(s, X):
        Xh = [sf.fftn(x, norm='ortho', workers=1) for x in X]
        lam = s.lam_from(Xh)
        del Xh
        Ah = [np.conj(s.q(mu)) * s.tile(lam[..., mu].astype(s.ct)) * s.ilap for mu in range(4)]
        Fh = s.d(Ah)
        del Ah
        rss_guard()
        return [sf.ifftn(f, norm='ortho', workers=1).real.astype(s.rt) for f in Fh]

    def dA_real(s, A):
        return [np.roll(A[n], -1, m) - A[n] - np.roll(A[m], -1, n) + A[m] for (m, n) in PAIRS]

    def potential(s, F):
        Fh = [sf.fftn(x, norm='ortho') for x in F]
        Y = s.dstar(Fh)
        return [sf.ifftn(y * s.ilap, norm='ortho').real for y in Y]

    def Q_real(s, A):
        """Direct real-space path average at block centres; no symbols."""
        B, M, N = s.B, s.M, s.N
        off = range(-(B - 1) // 2, (B - 1) // 2 + 1)
        out = []
        for mu in range(4):
            a = A[mu]
            pth = sum(np.roll(a, -t, mu) for t in range(B))
            for ax in range(4):
                pth = sum(np.roll(pth, -o, ax) for o in off) / B
            out.append(pth[::B, ::B, ::B, ::B])
        return out

def weights(fl, profile, nu):
    N, B = fl.N, fl.B
    w = []
    def t(u):
        u = np.mod(u, N)
        return np.minimum(u, N - u) / B
    x = np.arange(N, dtype=np.float64)
    for (m, n) in PAIRS:
        tt = []
        for r in range(4):
            sh = 0.5 if r in (m, n) else 0.0
            v = t(x + sh)
            if profile == 'step':
                v = np.floor(v + 0.5)
            if profile == 'cos':
                v = (fl.M / (2 * np.pi)) * np.cos(2 * np.pi * (x + sh) / N)
            tt.append(v.reshape(fl.sh[r]))
        if profile == 'radial':
            ell = -(tt[0] + tt[1] + tt[2] + tt[3])
        elif profile == 'zig':
            ell = -tt[0] * np.ones((N,) * 4)
        elif profile in ('step', 'cos'):
            ell = -tt[0] * np.ones((N,) * 4)
        else:
            raise SystemExit('profile')
        w.append(np.exp(nu * ell).astype(fl.rt))
    return w

def top_ratio(fl, w, seed=1, itmax=70, tol=2e-6):
    sq = [np.sqrt(a) for a in w]
    isq = [1 / a for a in sq]
    def Z(v):
        x = fl.P([a * b for a, b in zip(isq, v)])
        x = fl.P([a * b for a, b in zip(w, x)])
        return [a * b for a, b in zip(isq, x)]
    rng = np.random.default_rng(seed)
    v = fl.P([rng.standard_normal(a.shape).astype(fl.rt) for a in w])
    v = [a * b for a, b in zip(isq, v)]
    nrm = math.sqrt(sum(float(np.vdot(a, a)) for a in v))
    v = [a / nrm for a in v]
    vprev, beta = None, 0.0
    al, be, last = [], [], None
    for it in range(itmax):
        z = Z(v)
        a = sum(float(np.vdot(p, q)) for p, q in zip(v, z))
        al.append(a)
        z = [p - a * q for p, q in zip(z, v)]
        if vprev is not None:
            z = [p - beta * q for p, q in zip(z, vprev)]
        beta = math.sqrt(sum(float(np.vdot(p, p)) for p in z))
        T = np.diag(al) + np.diag(be, 1) + np.diag(be, -1)
        top = float(np.linalg.eigvalsh(T)[-1])
        if last is not None and abs(top - last) < tol * max(top - 1, 1e-3):
            return top, it + 1
        last = top
        if beta < 1e-7:
            return top, it + 1
        be.append(beta)
        vprev, v = v, [p / beta for p in z]
    return last, itmax

def identities(fl):
    rng = np.random.default_rng(7)
    A = [rng.standard_normal((fl.N,) * 4) for _ in range(4)]
    F = fl.dA_real(A)
    X = [rng.standard_normal((fl.N,) * 4).astype(fl.rt) for _ in range(6)]
    Y = [rng.standard_normal((fl.N,) * 4).astype(fl.rt) for _ in range(6)]
    PX = fl.P(X); PPX = fl.P(PX); PY = fl.P(Y)
    nn = math.sqrt(sum(float((a ** 2).sum()) for a in PX))
    i1a = math.sqrt(sum(float(((a - b) ** 2).sum()) for a, b in zip(PX, PPX))) / nn
    s1 = sum(float((a * b).sum()) for a, b in zip(PX, Y))
    s2 = sum(float((a * b).sum()) for a, b in zip(X, PY))
    i1b = abs(s1 - s2) / abs(s1)
    Fs = fl.P([a.astype(fl.rt) for a in F])
    G = fl.potential([a - b for a, b in zip(F, Fs)])
    qg = fl.Q_real(G)
    res = 0.0
    for m in range(4):
        for n in range(m + 1, 4):
            c = (np.roll(qg[n], -1, m) - qg[n] - np.roll(qg[m], -1, n) + qg[m])
            res = max(res, float(np.abs(c).max()))
    gs = max(float(np.abs(a).max()) for a in G)
    i3 = sum(float((a ** 2).sum()) for a in Fs) / sum(float((a ** 2).sum()) for a in F)
    return dict(P2=i1a, sym=i1b, coarse_curl_rel=res / gs, energy_ratio=i3, rank=fl.rank)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--B', type=int, required=True)
    ap.add_argument('--M', type=int, required=True)
    ap.add_argument('--single', action='store_true')
    ap.add_argument('--nus', default='0.1,0.2,0.4')
    ap.add_argument('--profiles', default='radial,zig')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    fl = Flat(a.B, a.M, a.single)
    rec = dict(B=a.B, M=a.M, single=a.single, identities=None, runs=[])
    if not a.single or fl.N <= 36:
        rec['identities'] = identities(fl)
        print(rec['identities'], flush=True)
    for prof in a.profiles.split(','):
        for nu in [float(u) for u in a.nus.split(',')]:
            w = weights(fl, prof, nu)
            rho, its = top_ratio(fl, w)
            n = sum(x.size for x in w)
            kant = float(sum(np.sum(x, dtype=np.float64) for x in w)
                         * sum(np.sum(1 / x, dtype=np.float64) for x in w) / n ** 2)
            rr = dict(profile=prof, nu=nu, rho=rho, D2=(rho - 1) / nu ** 2, its=its,
                      control_rank1=kant, secs=round(time.time() - t0, 1))
            rec['runs'].append(rr)
            print(rr, flush=True)
            with open(a.out, 'w') as f:
                json.dump(rec, f, indent=1)
            rss_guard()
    print('done', round(time.time() - t0, 1), flush=True)

if __name__ == '__main__':
    main()
