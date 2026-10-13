"""R19-10: static in-progress excess delta(g) = E0(H(g)) - E0(H_B) for Wilson-Dirac (r = 1) plane insertion,
H(g) = (1-g) H_A + g H_B; H_A = old ring (Lx sites) + new site with on-site <h0> = beta (m + 3r) (its local ground
state = best site-product, r1910_insert_product), H_B = new ring (Lx + 1).  Per inserted site, Lp x Lp
antiperiodic transverse sectors.  Also the energy of the ramp's starting state above H_B's ground state (= P-loc dE).
Lattice units."""
import numpy as np
exec(open('r1910_insert_product.py').read().split("pr('=== 1D ring")[0])
r = 1.0; Tx = al[0]/(2j) - 0.5*r*be
def HAB(N, h0, hbar):
    Ho = dirac_ring(N, h0, Tx)
    HA = np.zeros((4*(N+1), 4*(N+1)), complex); HA[:4*N, :4*N] = Ho; HA[4*N:, 4*N:] = hbar
    HB = dirac_ring(N, h0, Tx, insert=True)
    return HA, HB
def E0(H):
    w = np.linalg.eigvalsh(H); return w[w < 0].sum()
gs = [0.0, 0.25, 0.5, 0.75, 1.0]
taus, wt = np.polynomial.legendre.leggauss(8); taus = 0.5*(taus+1); wt = 0.5*wt
def sstep(x):
    if x <= 0: return 0.0
    if x >= 1: return 1.0
    e1 = np.exp(-1/x); e2 = np.exp(-1/(1-x)); return e1/(e1+e2)
for m in (0.0, 1.0):
    Lp, N = 8, 24
    kp = 2*np.pi*(np.arange(Lp) + 0.5)/Lp
    hbar = be*(m + 3*r)
    acc = np.zeros(len(gs)); accm = 0.0
    for ky in kp:
        for kz in kp:
            h0 = be*(m + r*(2 - np.cos(ky) - np.cos(kz)) + r) + al[1]*np.sin(ky) + al[2]*np.sin(kz)
            HA, HB = HAB(N, h0, hbar); eB = E0(HB)
            acc += np.array([E0((1-g)*HA + g*HB) - eB for g in gs])
            accm += sum(w*(E0((1-sstep(t))*HA + sstep(t)*HB) - eB) for t, w in zip(taus, wt))
    acc /= Lp*Lp; accm /= Lp*Lp
    pr('Wilson-Dirac m=%.1f: delta(g) per inserted site: ' % m + ', '.join('g=%.2f: %+.5f' % (g, d) for g, d in zip(gs, acc)))
    pr('   smoothstep-path mean delta-bar = %+.5f per inserted site (adiabatic limit: A_law -> T * delta-bar)' % accm)
