"""SU(2) Wilson lattice gauge theory in d=4: heat-bath (Kennedy-Pendleton) + overrelaxation.
Numerical evidence only (not proof). Action S = beta * sum_p (1 - 1/2 Tr U_p), beta = 4/g^2.
Quaternion representation U = a0 + i a.sigma, stored as [...,4].
Usage: python su2_mc.py L beta ntherm nmeas nor seed outfile
"""
import sys, json, time
import numpy as np

def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    # (a0 b0 - a.b, a0 b + b0 a - a x b)
    return np.stack([
        a0*b0 - a1*b1 - a2*b2 - a3*b3,
        a0*b1 + b0*a1 - (a2*b3 - a3*b2),
        a0*b2 + b0*a2 - (a3*b1 - a1*b3),
        a0*b3 + b0*a3 - (a1*b2 - a2*b1)], axis=-1)

def qdag(a):
    return a * np.array([1., -1., -1., -1.])

def sh(x, mu, s):
    # field at x + s*mu  (axis mu of the site grid = axis mu of array without the link/quaternion axes)
    return np.roll(x, -s, axis=mu)

def staple(U, mu):
    A = np.zeros_like(U[0])
    for nu in range(4):
        if nu == mu: continue
        Unu, Umu = U[nu], U[mu]
        # up: U_nu(x+mu) U_mu(x+nu)^dag U_nu(x)^dag
        up = qmul(qmul(sh(Unu, mu, 1), qdag(sh(Umu, nu, 1))), qdag(Unu))
        # down: U_nu(x+mu-nu)^dag U_mu(x-nu)^dag U_nu(x-nu)
        Unu_m = sh(Unu, nu, -1)
        dn = qmul(qmul(qdag(sh(Unu_m, mu, 1)), qdag(sh(Umu, nu, -1))), Unu_m)
        A += up + dn
    return A

def kp_sample(alpha, rng):
    """sample x0 with density ~ sqrt(1-x0^2) exp(alpha x0) (Kennedy-Pendleton)."""
    n = alpha.size
    out = np.empty(n); todo = np.arange(n)
    while todo.size:
        a = alpha[todo]
        r1, r2, r3, r4 = (1.0 - rng.random((4, todo.size)))
        lam2 = -(np.log(r1) + np.cos(2*np.pi*r2)**2*np.log(r3)) / (2*a)
        ok = r4**2 <= 1 - lam2
        out[todo[ok]] = 1 - 2*lam2[ok]
        todo = todo[~ok]
    return out

def random_su2_from_x0(x0, rng):
    n = x0.size
    r = np.sqrt(np.clip(1 - x0**2, 0, None))
    v = rng.normal(size=(n, 3)); v /= np.linalg.norm(v, axis=1, keepdims=True)
    return np.concatenate([x0[:, None], r[:, None]*v], axis=1)

def update(U, beta, mask, rng, kind):
    for mu in range(4):
        for par in (0, 1):
            m = mask[par]
            A = staple(U, mu)[m]
            k = np.sqrt((A**2).sum(-1))
            V = A / k[:, None]
            if kind == 'hb':
                X = random_su2_from_x0(kp_sample(beta*k, rng), rng)
                new = qmul(X, qdag(V))
            else:  # overrelaxation U -> V^dag U^dag V^dag
                new = qmul(qmul(qdag(V), qdag(U[mu][m])), qdag(V))
            new /= np.linalg.norm(new, axis=-1, keepdims=True)
            U[mu][m] = new

def plaq_field(U, mu, nu):
    return qmul(qmul(U[mu], sh(U[nu], mu, 1)), qmul(qdag(sh(U[mu], nu, 1)), qdag(U[nu])))

def wilson_loop(U, mu, nu, R, T):
    # R links along mu, T links along nu, starting at every x
    def line(d, n, start_shift=None):
        P = U[d].copy(); X = U[d]
        for i in range(1, n):
            P = qmul(P, sh(X, d, i))
        return P
    Lmu = line(mu, R); Lnu = line(nu, T)
    loop = qmul(qmul(Lmu, sh(Lnu, mu, R)), qmul(qdag(sh(Lmu, nu, T)), qdag(Lnu)))
    return loop[..., 0].mean()

def measure(U):
    L = U.shape[1]
    P = {}
    for mu in range(4):
        for nu in range(mu+1, 4):
            P[(mu, nu)] = plaq_field(U, mu, nu)[..., 0]
    plaq = np.mean([p.mean() for p in P.values()])
    # 0++ operator: spatial plaquettes (mu,nu in 0..2) summed over each time slice t (axis 3)
    sp = P[(0,1)] + P[(0,2)] + P[(1,2)]
    Ot = sp.sum(axis=(0,1,2))
    W = {}
    for (R, T) in [(1,1),(1,2),(2,2),(2,3),(3,3)]:
        if max(R,T) < L:
            vals = []
            for mu in range(4):
                for nu in range(4):
                    if mu != nu: vals.append(wilson_loop(U, mu, nu, R, T))
            W[f"{R}x{T}"] = float(np.mean(vals))
    # Polyakov loop along axis 3
    Pl = U[3].copy()
    for i in range(1, L): Pl = qmul(Pl, sh(U[3], 3, i))
    poly = float(np.abs(Pl[..., 0].mean(axis=(0,1,2))[0]))
    return float(plaq), Ot.tolist(), W, poly

def main():
    L, beta, ntherm, nmeas, nor, seed, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
    rng = np.random.default_rng(seed)
    start = sys.argv[8] if len(sys.argv) > 8 else 'cold'
    if start == 'hot':
        U = rng.normal(size=(4, L, L, L, L, 4)); U /= np.linalg.norm(U, axis=-1, keepdims=True)
    else:
        U = np.zeros((4, L, L, L, L, 4)); U[..., 0] = 1.0
    idx = np.indices((L, L, L, L)).sum(0) % 2
    mask = [idx == 0, idx == 1]
    t0 = time.time()
    for i in range(ntherm):
        update(U, beta, mask, rng, 'hb')
        for _ in range(nor): update(U, beta, mask, rng, 'or')
    recs = []
    for i in range(nmeas):
        update(U, beta, mask, rng, 'hb')
        for _ in range(nor): update(U, beta, mask, rng, 'or')
        p, Ot, W, poly = measure(U)
        recs.append({"plaq": p, "Ot": Ot, "W": W, "poly": poly})
    json.dump({"L": L, "beta": beta, "ntherm": ntherm, "nmeas": nmeas, "nor": nor, "seed": seed,
               "start": start, "seconds": time.time()-t0, "recs": recs}, open(out, "w"))
    print(L, beta, "done", round(time.time()-t0, 1), "s, <P>=", np.mean([r["plaq"] for r in recs]))

if __name__ == "__main__":
    main()
