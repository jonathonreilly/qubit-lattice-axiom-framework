"""A30 q6_heat: is the heat released when a jam surface records a site thermal? (exact toy)

Free fermions (supplied entangled vacuum: half-filled chain), sites 1..M, hopping -t,
hard walls at 0 (the jam) and M+1.  One sharp two-outcome lock of the surface site 1 (menu
{occupied, empty}, Born odds C_11).  After the lock site 1 joins the jam (wall moves to 1).
Post-lock state (Gaussian, conditional correlation matrix) is resolved in the new walled
chain's modes.  Outputs: injected energy (cross-check with A28 c2), and the excitation
occupation n(eps) against a Fermi-Dirac form (local temperature T_loc(eps)).
"""
import signal
import numpy as np
from scipy.linalg import eigh_tridiagonal

signal.alarm(55)
t = 1.0


def chain(M):
    return eigh_tridiagonal(np.zeros(M), -t * np.ones(M - 1))


for M in [200, 400, 800]:
    e, U = chain(M)
    Np = M // 2
    C = U[:, :Np] @ U[:, :Np].T                      # C_ij = <c_i^dag c_j>, real
    E0_old = np.sum(e[:Np])
    e2, V = chain(M - 1)                            # new chain: sites 2..M
    res = []
    for occ in (1, 0):
        p = C[0, 0] if occ else 1 - C[0, 0]
        if occ:
            Cc = C[1:, 1:] - np.outer(C[1:, 0], C[0, 1:]) / C[0, 0]
            nlocked = 1
        else:
            Cc = C[1:, 1:] + np.outer(C[1:, 0], C[0, 1:]) / (1 - C[0, 0])
            nlocked = 0
        # energy under the old generator: full C' including site 1 occupation
        Cfull = np.zeros_like(C)
        Cfull[1:, 1:] = Cc
        Cfull[0, 0] = occ
        Hold = np.diag(-t * np.ones(M - 1), 1) + np.diag(-t * np.ones(M - 1), -1)
        dE_old = np.sum(Hold * Cfull) - E0_old
        nm = np.einsum('im,ij,jm->m', V, Cc, V)
        Nrem = Np - nlocked
        E_new_gs = np.sum(e2[:Nrem])
        excess = np.sum(e2 * nm) - E_new_gs
        res.append((p, dE_old, excess, nm, Nrem))
    pbar = sum(r[0] for r in res)
    dE = sum(r[0] * r[1] for r in res)
    ex = sum(r[0] * r[2] for r in res)
    print(f"M={M}: P(lock occupied)={res[0][0]:.6f}  mean dE under old generator={dE:.6f} J  "
          f"mean excess above new walled ground state={ex:.6f} J  (2*C_01={2*C[0,1]:.6f})")

# thermality test on the largest chain, 'occupied' branch
p, dE_old, excess, nm, Nrem = res[0]
eF = 0.5 * (e2[Nrem - 1] + e2[Nrem])
print(f"\nM=800, lock 'occupied': new Fermi level {eF:.4f}; excitation occupations (particles above, holes below)")
print("  eps-eF      n (particle) or 1-n (hole)   T_loc = |eps-eF| / ln(1/n - 1)")
for target in [0.01, 0.03, 0.1, 0.3, 0.6, 1.0, 1.5]:
    for sgn in (+1, -1):
        m = np.argmin(np.abs(e2 - (eF + sgn * target)))
        occ = nm[m] if sgn > 0 else 1 - nm[m]
        Tl = abs(e2[m] - eF) / np.log(1 / occ - 1) if 0 < occ < 0.5 else float('nan')
        print(f"  {e2[m]-eF:+.4f}    {occ:.3e}                    {Tl:.4f}")
# integrated: number of excitations within windows (log-scaling test)
above = e2 > eF
for W in [0.01, 0.03, 0.1, 0.3, 1.0, 2.0]:
    sel = above & (e2 - eF < W)
    print(f"  particles with 0<eps-eF<{W:4.2f}: {np.sum(nm[sel]):.4f}")
