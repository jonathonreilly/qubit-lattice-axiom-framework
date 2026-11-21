#!/usr/bin/env python3
"""Monte Carlo test of the sup form of the interior estimate, criteria M1, M2.

Closed cube of half-side r, boundary links frozen (cold or Haar random), interior
links updated by checkerboard heat bath (Kennedy-Pendleton). Observable: average of
e_a over the inner cube of half-width max(1, r//3). Usage: upper-chain_ie4d.py beta r nsweeps ndraws seed
"""
import os, sys, resource, time
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np


def qmul(a, b):
    out = np.empty(np.broadcast_shapes(a.shape, b.shape), dtype=np.float64)
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    out[..., 0] = a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3
    out[..., 1] = a0 * b1 + a1 * b0 + a2 * b3 - a3 * b2
    out[..., 2] = a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1
    out[..., 3] = a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0
    return out


def qconj(a):
    out = -a.copy()
    out[..., 0] = a[..., 0]
    return out


def haar(shape, rng):
    q = rng.standard_normal(shape + (4,))
    q /= np.linalg.norm(q, axis=-1, keepdims=True)
    return q


def kp_sample(kappa, rng):
    """Sample a0 with density proportional to sqrt(1-a0^2) exp(kappa a0), Kennedy-Pendleton."""
    a0 = np.empty(kappa.shape)
    todo = np.arange(kappa.size)
    k = kappa.ravel()
    out = a0.ravel()
    while todo.size:
        kk = k[todo]
        r1 = 1 - rng.random(todo.size)
        r2 = 1 - rng.random(todo.size)
        r3 = 1 - rng.random(todo.size)
        lam2 = -(np.log(r1) + np.cos(2 * np.pi * r2) ** 2 * np.log(r3)) / (2 * kk)
        accept = rng.random(todo.size) ** 2 <= 1 - lam2
        out[todo[accept]] = 1 - 2 * lam2[accept]
        todo = todo[~accept]
    return out.reshape(kappa.shape)


class Cube:
    def __init__(self, r, beta, rng):
        self.N = N = 2 * r + 1
        self.beta = beta
        self.rng = rng
        self.U = [np.zeros((N, N, N, N, 4)) for _ in range(4)]
        for m in range(4):
            self.U[m][..., 0] = 1.0
        # update masks: x_nu in 1..N-2 for nu != mu, x_mu in 0..N-2
        self.masks = []
        idx = np.indices((N, N, N, N))
        for m in range(4):
            cond = np.ones((N, N, N, N), bool)
            par = np.zeros((N, N, N, N), int)
            for n in range(4):
                if n == m:
                    cond &= idx[n] <= N - 2
                else:
                    cond &= (idx[n] >= 1) & (idx[n] <= N - 2)
                    par += idx[n]
            self.masks.append((cond & (par % 2 == 0), cond & (par % 2 == 1)))

    def set_boundary(self, kind):
        N = self.N
        idx = np.indices((N, N, N, N))
        for m in range(4):
            cond_free = np.ones((N, N, N, N), bool)
            for n in range(4):
                if n == m:
                    cond_free &= idx[n] <= N - 2
                else:
                    cond_free &= (idx[n] >= 1) & (idx[n] <= N - 2)
            bdry = ~cond_free
            if kind == "cold":
                self.U[m][bdry] = (1.0, 0.0, 0.0, 0.0)
            elif kind == "haar":
                q = haar((int(bdry.sum()),), self.rng)
                self.U[m][bdry] = q
            else:
                raise ValueError(kind)

    def staple_sum(self, m):
        S = np.zeros_like(self.U[m])
        Um = self.U[m]
        for n in range(4):
            if n == m:
                continue
            Un = self.U[n]
            # forward: U_n(x+m) U_m^+(x+n) U_n^+(x)
            a = np.roll(Un, -1, axis=m)
            b = qconj(np.roll(Um, -1, axis=n))
            S += qmul(qmul(a, b), qconj(Un))
            # backward: U_n^+(x+m-n) U_m^+(x-n) U_n(x-n)
            c = qconj(np.roll(np.roll(Un, -1, axis=m), 1, axis=n))
            d = qconj(np.roll(Um, 1, axis=n))
            e = np.roll(Un, 1, axis=n)
            S += qmul(qmul(c, d), e)
        return S

    def sweep(self):
        for m in range(4):
            for mask in self.masks[m]:
                S = self.staple_sum(m)[mask]
                r = np.linalg.norm(S, axis=-1)
                # U_b with weight exp(beta (1/2) Tr U_b A), A = S (U_b S plaquette loop): V = U R
                R = S / np.maximum(r, 1e-300)[..., None]
                kappa = self.beta * r
                a0 = kp_sample(np.maximum(kappa, 1e-12), self.rng)
                sv = np.sqrt(np.maximum(1 - a0**2, 0.0))
                d = self.rng.standard_normal(a0.shape + (3,))
                d /= np.linalg.norm(d, axis=-1, keepdims=True)
                V = np.concatenate([a0[..., None], sv[..., None] * d], axis=-1)
                self.U[m][mask] = qmul(V, qconj(R))

    def plaq_trace(self, m, n):
        # (1/2) Tr U_{mn}(x), arrays at x, valid where x+m, x+n are in the cube
        Um, Un = self.U[m], self.U[n]
        a = qmul(Um, np.roll(Un, -1, axis=m))
        b = qmul(Un, np.roll(Um, -1, axis=n))
        return np.sum(a * b, axis=-1)  # Re Tr(a b^+)/2 = dot product

    def prepare_inner(self, w):
        """Weights so that sum_o sum_y weight_o(y) s_o(y) = sum_{x in inner} e_a(x)."""
        N = self.N
        c = N // 2
        inner = np.zeros((N, N, N, N))
        inner[(c - w):(c + w + 1), (c - w):(c + w + 1), (c - w):(c + w + 1), (c - w):(c + w + 1)] = 1.0
        self.inner_size = inner.sum()
        self.weights = {}
        for m in range(4):
            for n in range(m + 1, 4):
                wt = 0.25 * (inner + np.roll(inner, -1, axis=m) + np.roll(inner, -1, axis=n)
                             + np.roll(np.roll(inner, -1, axis=m), -1, axis=n))
                self.weights[(m, n)] = wt

    def center_energy(self):
        total = 0.0
        for (m, n), wt in self.weights.items():
            total += np.sum(wt * (1 - self.plaq_trace(m, n)))
        return total / self.inner_size


def run(beta, r, nsweeps, ndraws, seed):
    rng = np.random.default_rng(seed)
    out = {}
    t0 = time.time()
    for kind, draws in (("cold", 1), ("haar", ndraws)):
        vals_all = []
        for d in range(draws):
            cube = Cube(r, beta, rng)
            cube.set_boundary(kind)
            cube.prepare_inner(max(1, r // 3))
            therm = max(100, 20 * r * r)
            for _ in range(therm):
                cube.sweep()
            vals = []
            nmeas = nsweeps if kind == "cold" else nsweeps // draws
            for _ in range(nmeas):
                cube.sweep()
                vals.append(cube.center_energy())
            vals_all.append(np.array(vals))
            rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e9
            if rss > 2.0:
                sys.exit("RSS above 2 GB")
            print(f"# {kind} draw {d} mean {vals_all[-1].mean():.5f} t={time.time()-t0:.0f}s", flush=True)
        out[kind] = vals_all
    # binned errors
    def mean_err(arrs):
        means = []
        errs = []
        for a in arrs:
            nb = 20
            b = a[: len(a) // nb * nb].reshape(nb, -1).mean(axis=1)
            means.append(b.mean())
            errs.append(b.std(ddof=1) / np.sqrt(nb))
        means = np.array(means)
        if len(means) > 1:
            return means.mean(), max(means.std(ddof=1) / np.sqrt(len(means)), np.sqrt(np.sum(np.square(errs))) / len(means))
        return means[0], errs[0]
    mc, ec = mean_err(out["cold"])
    mh, eh = mean_err(out["haar"])
    delta = mh - mc
    err = np.hypot(ec, eh)
    print(f"RESULT beta={beta} r={r} cold={mc:.5f}+-{ec:.5f} haar={mh:.5f}+-{eh:.5f} "
          f"Delta={delta:.5f}+-{err:.5f} r4Delta={r**4*delta:.3f}+-{r**4*err:.3f} t={time.time()-t0:.0f}s", flush=True)


if __name__ == "__main__":
    beta, r, nsweeps, ndraws, seed = float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    run(beta, r, nsweeps, ndraws, seed)
