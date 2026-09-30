"""T42 route-3 price: how much of the canonical SU(3) Wilson measure (beta = 6, g_bare = 1) lies on
plaquette-admissible fields (|| 1 - U_p || < eps for every plaquette), the support on which Luscher's
integer topological charge is defined (Luscher, Commun. Math. Phys. 85 (1982) 39)?
4^4 periodic lattice, Metropolis, seeded.  Sanity anchor: <P>(6) = 0.5934 (thermodynamic limit, repo value)."""
import numpy as np, time, sys
rng = np.random.default_rng(4242)
L = 4; beta = 6.0; N = 3
shape = (L, L, L, L)

def rand_su3(size, eps):
    A = rng.normal(size=size + (3, 3)) + 1j * rng.normal(size=size + (3, 3))
    H = (A + np.conj(np.swapaxes(A, -1, -2))) / 2
    tr = np.trace(H, axis1=-2, axis2=-1)[..., None, None] / 3
    H = H - tr * np.eye(3)
    w, v = np.linalg.eigh(H)
    return np.einsum('...ij,...j,...kj->...ik', v, np.exp(1j * eps * w), np.conj(v))

def dag(M): return np.conj(np.swapaxes(M, -1, -2))
def sh(M, mu, s): return np.roll(M, -s, axis=mu)     # value at x + s*e_mu

U = [np.broadcast_to(np.eye(3, dtype=complex), shape + (3, 3)).copy() for _ in range(4)]
par = np.indices(shape).sum(axis=0) % 2

def staple(mu):
    A = 0
    for nu in range(4):
        if nu == mu: continue
        # forward staple: U_nu(x+mu) U_mu^dag(x+nu) U_nu^dag(x)
        A = A + sh(U[nu], mu, 1) @ dag(sh(U[mu], nu, 1)) @ dag(U[nu])
        # backward staple: U_nu^dag(x+mu-nu) U_mu^dag(x-nu) U_nu(x-nu)
        A = A + dag(sh(sh(U[nu], mu, 1), nu, -1)) @ dag(sh(U[mu], nu, -1)) @ sh(U[nu], nu, -1)
    return A

def sweep(eps):
    acc = 0; tot = 0
    for mu in range(4):
        for p in (0, 1):
            A = staple(mu)
            R = rand_su3(shape, eps)
            Un = R @ U[mu]
            dS = -(beta / 3) * np.real(np.trace((Un - U[mu]) @ A, axis1=-2, axis2=-1))
            mask = (par == p)
            take = (rng.random(shape) < np.exp(-dS)) & mask
            U[mu] = np.where(take[..., None, None], Un, U[mu])
            acc += take.sum(); tot += mask.sum()
    return acc / tot

def plaquettes():
    out = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            P = U[mu] @ sh(U[nu], mu, 1) @ dag(sh(U[mu], nu, 1)) @ dag(U[nu])
            out.append(P.reshape(-1, 3, 3))
    return np.concatenate(out)

def reunitarize():
    for mu in range(4):
        q, r = np.linalg.qr(U[mu])
        d = np.diagonal(r, axis1=-2, axis2=-1)
        q = q * (d / np.abs(d))[..., None, :]
        det = np.linalg.det(q)
        q = q / (det ** (1 / 3))[..., None, None]
        U[mu] = q

import os
eps_step = float(os.environ.get('EPS_STEP', '0.5'))
t0 = time.time()
therm, meas = int(os.environ.get('THERM','400')), int(os.environ.get('MEAS','600'))
acc_list = []
for it in range(therm):
    acc_list.append(sweep(eps_step))
    if it % 20 == 0: reunitarize()
print(f"thermalised {therm} sweeps in {time.time()-t0:.1f}s, mean acceptance {np.mean(acc_list):.3f}")

eps_edges = [1/30, 0.1, 0.25, 0.5, 0.75, 1.0]
count = np.zeros(len(eps_edges)); ntot = 0
plq_mean = []
epsvals = []
for it in range(meas):
    sweep(eps_step)
    if it % 20 == 0: reunitarize()
    if it % 5 == 0:
        P = plaquettes()
        plq_mean.append(np.real(np.trace(P, axis1=-2, axis2=-1)).mean() / 3)
        lam = np.linalg.eigvals(P)                       # eigenvalues e^{i phi}
        e = np.abs(1 - lam).max(axis=1)                  # || 1 - U_p || (operator norm)
        epsvals.append(e)
        for k, ee in enumerate(eps_edges): count[k] += (e < ee).sum()
        ntot += len(e)
pm = np.mean(plq_mean); ps = np.std(plq_mean) / np.sqrt(len(plq_mean) / 10)
print(f"<P> = {pm:.4f} (+- ~{ps:.4f}); repo thermodynamic value 0.5934")
allE = np.concatenate(epsvals)
print(f"|| 1 - U_p || quantiles (5,25,50,75,95%): {np.percentile(allE,[5,25,50,75,95]).round(3)}, min {allE.min():.3f}")
nplaq = 6 * L ** 4
print(f"plaquettes per configuration: {nplaq}")
for k, ee in enumerate(eps_edges):
    f = count[k] / ntot
    if f > 0:
        lg = nplaq * np.log10(f)
        print(f"  eps={ee:.4f}: fraction of plaquettes with ||1-U_p||<eps = {f:.3e};  "
              f"(fraction)^{nplaq} ~ 10^{lg:.0f}")
    else:
        print(f"  eps={ee:.4f}: fraction = 0 in {ntot} plaquettes (< {1/ntot:.1e})")
# fraction of configurations (measured) with ALL plaquettes below eps
allmask = [ (e < 1.0).all() for e in epsvals ]
print("measured configurations with every plaquette below eps=1.0:", sum(allmask), "of", len(epsvals))
print(f"elapsed {time.time()-t0:.1f}s")
