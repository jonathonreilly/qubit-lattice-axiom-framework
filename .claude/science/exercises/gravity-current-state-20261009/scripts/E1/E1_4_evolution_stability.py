"""E1: does the realization noise stay bounded when the field is actually propagated?

Retarded explicit evolution on a sprinkled diamond (the BD operator is lower-triangular):
    B_eps phi(x) = 0  <=>  phi(x) = eps * sum_{y<x} f(n(x,y),eps) phi(y)   (4D)
                          phi(x) = 2 eps * sum f2 phi(y)                     (2D: -1/2 phi(x))
Initial data phi = 1 (an exact solution of the mean equation) on elements whose past
diamond is small (tau_b < tau0); every later element is evolved.  We compare
  open loop  : d_open(x)   = (W 1)(x) - 1   (element-wise noise, no feedback)
  closed loop: d_closed(x) = phi(x) - 1     (noise fed back through the evolution)
binned by tau_b (proper height of the element's past diamond).
Prediction (ARGUED): white jitter is amplified by the white-noise gain A^2 = sum_y w^2;
in 4D A^2 ~ c' eps tau^2 grows, so d_closed blows up once A^2 >~ 1; in 2D A^2 ~ eps log.
"""
import numpy as np, time, sys
from math import sqrt
from bd_core import (sprinkle4d, bd4d_weights, csr_apply, evolve,
                     sprinkle2d, bd2d_weights)

rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 7)


def run4d(eps, T, tau0, nreal):
    print(f"\n== 4D eps={eps} T={T} tau0={tau0} ==", flush=True)
    bins = np.arange(tau0, T + 0.01, 1.0)
    acc_o = [[] for _ in bins[:-1]]; acc_c = [[] for _ in bins[:-1]]; acc_g = [[] for _ in bins[:-1]]
    t0 = time.time()
    for r in range(nreal):
        P = sprinkle4d(1/eps, T, rng)
        tb = np.sqrt(np.maximum(P[:, 0]**2 - (P[:, 1:]**2).sum(1), 0))
        allx = np.arange(len(P))
        ip, ix, w = bd4d_weights(P, allx, eps)
        is_init = tb < tau0
        phi = evolve(ip, ix, w, allx, np.ones(len(P)), is_init)
        d_open = csr_apply(ip, ix, w, np.ones(len(P))) - 1.0
        d_closed = phi - 1.0
        gain = np.array([np.sum(w[ip[a]:ip[a+1]]**2) for a in allx])
        for k in range(len(bins)-1):
            m = (tb >= bins[k]) & (tb < bins[k+1])
            acc_o[k] += list(d_open[m]); acc_c[k] += list(d_closed[m]); acc_g[k] += list(gain[m])
    print(f"   N~{len(P)}  [{time.time()-t0:.0f}s]")
    for k in range(len(bins)-1):
        if len(acc_o[k]) < 10: continue
        o = np.array(acc_o[k]); c = np.array(acc_c[k]); g = np.array(acc_g[k])
        print(f"   tau in [{bins[k]:.1f},{bins[k+1]:.1f}) n={o.size:6d}  <A^2>={g.mean():8.3f}"
              f"  rms open={sqrt((o**2).mean()):10.3e}  rms closed={sqrt((c**2).mean()):10.3e}"
              f"  closed/open={sqrt((c**2).mean()/(o**2).mean()):9.3e}", flush=True)


def run2d(eps, U, u0, nreal):
    print(f"\n== 2D eps={eps} U={U} (init: u*v < {u0}) ==", flush=True)
    edges = np.array([u0, 2*u0, 4*u0, 8*u0, 16*u0, 32*u0, 64*u0, 1e9])
    acc_o = [[] for _ in edges[:-1]]; acc_c = [[] for _ in edges[:-1]]; acc_g = [[] for _ in edges[:-1]]
    t0 = time.time()
    for r in range(nreal):
        u, v = sprinkle2d(1/eps, U, rng)
        order = np.argsort(u + v)  # time order
        u = u[order]; v = v[order]
        allx = np.arange(u.size)
        ip, ix, w = bd2d_weights(u, v, U, allx, eps)
        w2 = 2.0*w  # phi(x) = 2 eps sum f2 phi(y)
        vol = u*v
        is_init = vol < u0
        phi = evolve(ip, ix, w2, allx, np.ones(u.size), is_init)
        d_open = csr_apply(ip, ix, w2, np.ones(u.size)) - 1.0
        d_closed = phi - 1.0
        gain = np.array([np.sum(w2[ip[a]:ip[a+1]]**2) for a in allx])
        for k in range(len(edges)-1):
            m = (vol >= edges[k]) & (vol < edges[k+1])
            acc_o[k] += list(d_open[m]); acc_c[k] += list(d_closed[m]); acc_g[k] += list(gain[m])
    print(f"   N~{u.size}  [{time.time()-t0:.0f}s]")
    for k in range(len(edges)-1):
        if len(acc_o[k]) < 10: continue
        o = np.array(acc_o[k]); c = np.array(acc_c[k]); g = np.array(acc_g[k])
        print(f"   uv in [{edges[k]:.0f},{min(edges[k+1],U*U):.0f}) n={o.size:6d}  <A^2>={g.mean():7.4f}"
              f"  rms open={sqrt((o**2).mean()):9.3e}  rms closed={sqrt((c**2).mean()):9.3e}"
              f"  closed/open={sqrt((c**2).mean()/(o**2).mean()):7.3f}", flush=True)


if __name__ == "__main__":
    which = sys.argv[2] if len(sys.argv) > 2 else "all"
    if which in ("2d", "all"):
        run2d(1/16, 24.0, 10.0, 6)
        run2d(1/64, 24.0, 10.0, 3)
    if which in ("4d", "all"):
        run4d(0.02, 6.0, 3.0, 2)
        run4d(0.05, 7.0, 3.0, 2)
        run4d(0.1, 8.0, 3.0, 2)
        run4d(0.2, 9.0, 3.0, 3)
