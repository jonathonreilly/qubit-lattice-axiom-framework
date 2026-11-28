#!/usr/bin/env python3
"""Linear (WAM) worst ratio over CLOSED trials F in Ran d. See CRITERIA.md, post hoc section."""
import argparse, json, math, time
import numpy as np, scipy.fft as sf
from lin_wam_4d import Flat, weights, rss_guard

def ip(a, b):
    return sum(float(np.vdot(x, y)) for x, y in zip(a, b))

def pi_exact(fl, X):
    Xh = [sf.fftn(x, norm='ortho', workers=1) for x in X]
    Y = fl.dstar(Xh)
    del Xh
    Ah = [y * fl.ilap for y in Y]
    del Y
    Fh = fl.d(Ah)
    del Ah
    return [sf.ifftn(f, norm='ortho', workers=1).real.astype(fl.rt) for f in Fh]

def rho_closed(fl, w, seed=3, itmax=60, tol=3e-6, cgtol=None):
    cgtol = cgtol or (1e-5 if fl.rt is np.float32 else 1e-9)
    def Bop(v):
        return pi_exact(fl, [a * b for a, b in zip(w, v)])
    def Aop(v):
        x = fl.P(v)
        x = fl.P([a * b for a, b in zip(w, x)])
        return x
    def solveB(r):
        # CG on the exact subspace; B is well conditioned for slow weights.
        x = [np.zeros_like(a) for a in r]
        res = [a.copy() for a in r]
        p = [a.copy() for a in r]
        rr = ip(res, res); r0 = rr
        for _ in range(200):
            if rr <= cgtol ** 2 * r0 or rr == 0:
                break
            Bp = Bop(p)
            al = rr / ip(p, Bp)
            x = [a + al * b for a, b in zip(x, p)]
            res = [a - al * b for a, b in zip(res, Bp)]
            r2 = ip(res, res)
            be = r2 / rr
            p = [a + be * b for a, b in zip(res, p)]
            rr = r2
        return x
    rng = np.random.default_rng(seed)
    v = fl.P([rng.standard_normal(a.shape).astype(fl.rt) for a in w])
    n = math.sqrt(ip(v, Bop(v)))
    v = [a / n for a in v]
    vprev, beta = None, 0.0
    al, be, last = [], [], None
    for it in range(itmax):
        Av = Aop(v)
        a = ip(v, Av)
        al.append(a)
        z = solveB(Av)
        z = [p - a * q for p, q in zip(z, v)]
        if vprev is not None:
            z = [p - beta * q for p, q in zip(z, vprev)]
        beta = math.sqrt(max(ip(z, Bop(z)), 0.0))
        T = np.diag(al) + np.diag(be, 1) + np.diag(be, -1)
        top = float(np.linalg.eigvalsh(T)[-1])
        rss_guard()
        if last is not None and abs(top - last) < tol * max(abs(top - 1), 1e-4):
            return top, it + 1
        last = top
        if beta < 1e-8:
            return top, it + 1
        be.append(beta)
        vprev, v = v, [p / beta for p in z]
    return last, itmax

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--B', type=int, required=True)
    ap.add_argument('--M', type=int, required=True)
    ap.add_argument('--single', action='store_true')
    ap.add_argument('--nus', default='0.1,0.2,0.4')
    ap.add_argument('--profiles', default='radial,zig,step')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    t0 = time.time()
    fl = Flat(a.B, a.M, a.single)
    rec = dict(B=a.B, M=a.M, single=a.single, runs=[])
    w1 = [np.ones((fl.N,) * 4, fl.rt) for _ in range(6)]
    rec['control_w1'], _ = rho_closed(fl, w1)
    print('control w=1', rec['control_w1'], flush=True)
    for prof in a.profiles.split(','):
        for nu in [float(u) for u in a.nus.split(',')]:
            w = weights(fl, prof, nu)
            rho, its = rho_closed(fl, w)
            rr = dict(profile=prof, nu=nu, rho_c=rho, D2c=(rho - 1) / nu ** 2, its=its,
                      secs=round(time.time() - t0, 1))
            rec['runs'].append(rr)
            print(rr, flush=True)
            with open(a.out, 'w') as f:
                json.dump(rec, f, indent=1)
    print('done', round(time.time() - t0, 1), flush=True)

if __name__ == '__main__':
    main()
