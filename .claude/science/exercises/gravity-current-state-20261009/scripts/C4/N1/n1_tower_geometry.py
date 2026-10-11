"""N1 check: geometry of the forced one-particle tower in an exactly
Poincare-closed lattice theory (A3 of the N1 report).

Exact closure + integrated positive-energy rep => on an isolated mass shell M1
the lattice-momentum fibre over Q carries E_n(Q) = sqrt(M1^2 + beta|Q-theta+2 pi n|^2),
n in Z^d.  Checks, d = 2, 3, theta = 0 and theta = (pi,...):
 (a) branch touching: min_n'!=n |E_n - E_n'| -> 0 at the zone faces (so no branch
     is an isolated band: BDN's isolated-shell hypothesis fails);
 (b) embedding: count of n != 0 members BELOW the two-particle threshold at the
     same Q (all others lie inside the continuum [thr(Q), inf), which is
     unbounded at fixed Q); and whether the n = 0 member is embedded;
 (c) energy-sorted lowest branch u0 = E0^2/2 on the torus: zone average of
     Hess u0 / beta - I is exactly -I (T1 sum rule), carried by face kinks.
Exact arithmetic is not needed; tolerances printed.
"""
import itertools, numpy as np
np.set_printoptions(precision=6, suppress=True)

def tower(Q, M, beta, theta, nmax, d):
    ns = np.array(list(itertools.product(range(-nmax, nmax+1), repeat=d)))
    p = Q[None, :] - theta[None, :] + 2*np.pi*ns
    return ns, np.sqrt(M**2 + beta*np.sum(p**2, axis=1))

def two_particle_threshold(Q, M, beta, theta, nmax, d):
    # pairs of shell states with total lattice momentum Q: p1 + p2 = Q - 2 theta + 2 pi n
    # minimal energy at fixed total Pi is sqrt(4M^2 + beta|Pi|^2)
    ns = np.array(list(itertools.product(range(-nmax, nmax+1), repeat=d)))
    Pi = Q[None, :] - 2*theta[None, :] + 2*np.pi*ns
    return np.min(np.sqrt(4*M**2 + beta*np.sum(Pi**2, axis=1)))

M, beta = 1.0, 1.0
for d in (2, 3):
    for thname, theta in (("0", np.zeros(d)), ("pi", np.pi*np.ones(d))):
        print(f"--- d={d}, theta={thname}, M1={M}, beta={beta}")
        # (a) touching along a line from zone centre to face, Q = t*(pi,0,..)
        for t in (0.0, 0.5, 0.9, 0.99, 0.999, 1.0):
            Q = np.zeros(d); Q[0] = t*np.pi
            Q = Q + theta  # measure from the tower centre
            ns, E = tower(Q, M, beta, theta, 3, d)
            Es = np.sort(E)
            gap01 = Es[1]-Es[0]
            thr = two_particle_threshold(Q, M, beta, theta, 3, d)
            nonzero = E[np.any(ns != 0, axis=1)]
            emb = int(np.sum(nonzero <= thr))  # n!=0 members NOT above the 2-particle threshold (finite)
            n0emb = E[np.all(ns == 0, axis=1)][0] > thr
            print(f"  |Q-theta|=({t:.3f} pi,0..): E_low={Es[0]:.6f} next={Es[1]:.6f} gap={gap01:.3e} "
                  f"2p-thr={thr:.6f}  #(n!=0 below 2p-thr) = {emb} of {len(nonzero)}  n=0 embedded? {n0emb}")
        # (c) energy-sorted lowest branch: zone average of Hess u0 via periodic FD
        N = 120 if d == 2 else 40
        g = (np.arange(N)+0.5)*2*np.pi/N  # avoid sitting exactly on the face
        h = 2*np.pi/N
        grids = np.meshgrid(*([g]*d), indexing="ij")
        Qs = np.stack(grids, axis=-1)
        p = (Qs - theta + np.pi) % (2*np.pi) - np.pi   # nearest tower member = sorted lowest
        u0 = 0.5*(M**2 + beta*np.sum(p**2, axis=-1))
        hess_avg = np.zeros((d, d))
        for b in range(d):
            ub = (np.roll(u0, -1, axis=b) - 2*u0 + np.roll(u0, 1, axis=b))/h**2
            hess_avg[b, b] = ub.mean()
        print(f"  zone-avg diag Hess(u0)/beta - 1 = {np.diag(hess_avg)/beta - 1}  (T1 sum rule predicts -1)")
        # bulk (away from faces) value
        mask = np.all(np.abs(p) < np.pi - 3*h, axis=-1)
        ub = (np.roll(u0, -1, axis=0) - 2*u0 + np.roll(u0, 1, axis=0))/h**2
        print(f"  bulk Hess_11(u0)/beta on {mask.mean():.3f} of zone: min {ub[mask].min():.6f} max {ub[mask].max():.6f}")
