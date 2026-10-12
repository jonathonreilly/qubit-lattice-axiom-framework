"""R8-4 script A: one-loop dressed dispersion of the explicit four-species fermion box Hamiltonian on Z^3 x R,
in infinite volume (on the vertex support every leg is inside the box, so lattice kinematics = continuum
kinematics there; Lemma L of R7-1).  Second-order Rayleigh-Schroedinger shift of the one-particle state
relative to the vacuum, built from the Hamiltonian's two pair-creating monomial families:

  forward  X_p -> (Y Z W)          amplitude  g Psi(k1,k2,k3) sqrt(h(E_p,W)) / sqrt(2E_p 2E1 2E2 2E3)
  vacuum   0 -> (X Y Z W), sum k=0  amplitude  g Psi6(all four)              / sqrt(2E_X 2E1 2E2 2E3)
  Psi(cluster) = prod_{pairs} F(s_ij),   Psi6 = prod over all six pairs (spectator pairs with X included!)
  F(s) = plateau(sqrt(s); Lam1, Lam2)   (C^inf, Gevrey-2, compact)

The one-particle shift (fermions; the Z part is the Pauli-blocked vacuum fluctuation, sign +):
  dE(p) = int d3k1 d3k2/(2pi)^6 [ |A_f|^2/(E_p - W) + |A_Z|^2/(E_p + W) ]
(the formula is checked against the explicit Fock-space Hamiltonian in script B).

Reported:  m2_eff(p) = 2 E_p dE(p)  (= the O(g^2) shift of E^2 - p^2), for p along z and along (1,1,1)/sqrt3.
Variants (comparators):  'INV'  : as built (C = 1 in h = (W(1+2C)-E)/(W+E));
                         'h=1'  : boson-type normalisation with fermionic Pauli sign;
                         'noZ'  : forward ordering only (no vacuum term);
                         'FF'   : frame-fixed form factor prod_i plateau(|k_i|) instead of Psi (both orderings, h).
g = 1 throughout (results are the g^2 coefficient)."""
import numpy as np, time, sys
from numpy.polynomial.legendre import leggauss
np.seterr(all='ignore')

OUT = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); OUT.append(s)

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
    e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
def plateau(x, x1, x2): return 1.0 - sstep((np.abs(x) - x1)/(x2 - x1))

m = float(sys.argv[1]) if len(sys.argv) > 1 else 0.05
LAM1, LAM2 = 1.0, 1.3
A1, A2 = 1.7, 2.1          # leg cutoff (frame-fixed, per component) -- must be inactive on the support
FF1, FF2 = 0.45, 0.75      # FF comparator: frame-fixed |k| plateau

def F(s): return plateau(np.sqrt(np.maximum(s, 0.0)), LAM1, LAM2)
def sinv(E1, k1, E2, k2):  # (k1+k2)^2 with on-shell 4-vectors
    return (E1+E2)**2 - ((k1[0]+k2[0])**2 + (k1[1]+k2[1])**2 + (k1[2]+k2[2])**2)
def legcut(k): return plateau(k[0], A1, A2)*plateau(k[1], A1, A2)*plateau(k[2], A1, A2)

def shift(pvec, nu=24, nz=48, h=0.07, K=1.45, C=1.0):
    """returns dict variant -> 2 E_p dE(p); p along an arbitrary direction is handled by rotating the grid:
    we put p along z' and keep the cubic leg cutoff evaluated in the true lattice frame."""
    p = np.array(pvec, float); pn = np.linalg.norm(p)
    # orthonormal frame with e3 along p (or z if p = 0)
    e3 = p/pn if pn > 0 else np.array([0, 0, 1.0])
    tmp = np.array([1.0, 0, 0]) if abs(e3[0]) < 0.9 else np.array([0, 1.0, 0])
    e1 = np.cross(e3, tmp); e1 /= np.linalg.norm(e1); e2 = np.cross(e3, e1)
    Ep = np.sqrt(m*m + pn*pn)
    # k1 = (rho,0,z) in the (e1,e2,e3) frame; weight 2 pi rho drho = pi du  (u = rho^2), axial symmetry
    # NOTE axial symmetry holds for the invariant parts; the cubic leg cutoff is not axially symmetric, but it is
    # inactive (checked: max leg component on the support is printed).
    xu, wu = leggauss(nu); U = K*K; u = 0.5*U*(xu+1); wu = 0.5*U*wu
    xz, wz = leggauss(nz); z = K*xz; wz = K*wz
    g1 = np.arange(-K, K+1e-12, h); w2 = h**3
    X2, Y2, Z2 = np.meshgrid(g1, g1, g1, indexing='ij'); X2 = X2.ravel(); Y2 = Y2.ravel(); Z2 = Z2.ravel()
    acc = {k: 0.0 for k in ('INV', 'h=1', 'noZ', 'FF', 'INV_nospect')}
    maxleg = 0.0; maxspect = 0.0; minW_minus_E = 1e9
    for iu in range(nu):
        rho = np.sqrt(u[iu])
        for iz in range(nz):
            wt = np.pi*wu[iu]*wz[iz]*w2
            k1 = rho*e1 + z[iz]*e3
            k2 = (X2[:, None]*e1 + Y2[:, None]*e2 + Z2[:, None]*e3).T if False else None
            k2x = X2*e1[0] + Y2*e2[0] + Z2*e3[0]; k2y = X2*e1[1] + Y2*e2[1] + Z2*e3[1]; k2z = X2*e1[2] + Y2*e2[2] + Z2*e3[2]
            k3x = p[0]-k1[0]-k2x; k3y = p[1]-k1[1]-k2y; k3z = p[2]-k1[2]-k2z
            E1 = np.sqrt(m*m + k1 @ k1); E2 = np.sqrt(m*m + k2x**2+k2y**2+k2z**2); E3 = np.sqrt(m*m + k3x**2+k3y**2+k3z**2)
            K1 = (np.full_like(k2x, k1[0]), np.full_like(k2x, k1[1]), np.full_like(k2x, k1[2]))
            K2 = (k2x, k2y, k2z); K3 = (k3x, k3y, k3z)
            s12 = sinv(E1, K1, E2, K2); s13 = sinv(E1, K1, E3, K3); s23 = sinv(E2, K2, E3, K3)
            Psi = F(s12)*F(s13)*F(s23)
            lc = legcut(K1)*legcut(K2)*legcut(K3)
            W = E1+E2+E3
            nrm = 1.0/(2*Ep*8*E1*E2*E3)
            hh = (W*(1+2*C) - Ep)/(W + Ep)
            # spectator pairs for the Z ordering: X at p, rest cluster at -p is the mirror of this cluster
            # s_XY = 2m^2 + 2(E_p E_Y + p.k_Y) for k_Y in the +p mirror
            def sXY(EY, KY): return 2*m*m + 2*(Ep*EY + p[0]*KY[0] + p[1]*KY[1] + p[2]*KY[2])
            sp = F(sXY(E1, K1))*F(sXY(E2, K2))*F(sXY(E3, K3))
            nz_ = Psi > 0
            if np.any(nz_):
                for KK in (K1, K2, K3):
                    maxleg = max(maxleg, float(np.max(np.abs(np.concatenate([KK[0][nz_], KK[1][nz_], KK[2][nz_]])))))
                maxspect = max(maxspect, float(np.max(np.sqrt(np.concatenate([sXY(E1, K1)[nz_], sXY(E2, K2)[nz_], sXY(E3, K3)[nz_]])))))
                minW_minus_E = min(minW_minus_E, float(np.min(W[nz_] - Ep)))
            fw = lc*Psi**2*nrm/(Ep - W); zz = lc*(Psi*sp)**2*nrm/(Ep + W); zz0 = lc*Psi**2*nrm/(Ep + W)
            acc['INV'] += wt*np.sum(hh*fw + zz)
            acc['INV_nospect'] += wt*np.sum(hh*fw + zz0)
            acc['h=1'] += wt*np.sum(fw + zz)
            acc['noZ'] += wt*np.sum(hh*fw)
            Pff = plateau(np.sqrt(K1[0]**2+K1[1]**2+K1[2]**2), FF1, FF2)*plateau(np.sqrt(k2x**2+k2y**2+k2z**2), FF1, FF2)*plateau(np.sqrt(k3x**2+k3y**2+k3z**2), FF1, FF2)
            acc['FF'] += wt*np.sum(Pff**2*nrm*(hh/(Ep - W) + 1.0/(Ep + W)))
    res = {k: 2*Ep*v/(2*np.pi)**6 for k, v in acc.items()}
    return res, maxleg, maxspect, minW_minus_E

if __name__ == '__main__':
    t0 = time.time()
    pr(f'# R8-4 A: m={m}  Lam1={LAM1} Lam2={LAM2}  leg cutoff plateau {A1}->{A2}  FF plateau {FF1}->{FF2}')
    pr('# columns: |p| dir  m2eff[INV]  m2eff[INV, spectators dropped]  m2eff[h=1]  m2eff[noZ]  m2eff[FF]  maxleg  max sqrt(s_spect)  min(W-E)')
    grids = [dict(nu=16, nz=32, h=0.09), dict(nu=24, nz=48, h=0.07)]
    if len(sys.argv) > 2 and sys.argv[2] == 'fine': grids = [dict(nu=32, nz=64, h=0.055)]
    for gi, gr in enumerate(grids):
        pr(f'## grid {gi}: {gr}')
        rows = []
        import os
        PL = [(0.0, 'z'), (0.1, 'z'), (0.2, 'z'), (0.2, 'diag'), (0.3, 'z'), (0.45, 'z')] if 'PSHORT' not in os.environ else [(0.0, 'z'), (0.1, 'z'), (0.2, 'z')]
        for pn, d in PL:
            dv = np.array([0, 0, 1.0]) if d == 'z' else np.ones(3)/np.sqrt(3)
            r, ml, ms, mw = shift(pn*dv, **gr)
            rows.append((pn, d, r))
            pr(f'{pn:5.2f} {d:4s}  {r["INV"]:+.9e}  {r["INV_nospect"]:+.9e}  {r["h=1"]:+.9e}  {r["noZ"]:+.9e}  {r["FF"]:+.9e}  {ml:.3f}  {ms:.3f}  {mw:.3f}   t={time.time()-t0:.0f}s')
        ref = rows[0][2]
        pr('# relative deviation (m2eff(p) - m2eff(0))/|m2eff(0)|:')
        for pn, d, r in rows:
            pr(f'{pn:5.2f} {d:4s}  ' + '  '.join(f'{k}:{(r[k]-ref[k])/abs(ref[k]):+.2e}' for k in ('INV', 'INV_nospect', 'h=1', 'noZ', 'FF')))
    open(__file__.replace('.py', f'_m{m}' + ('_fine' if len(sys.argv) > 2 else '') + '.out'), 'w').write('\n'.join(OUT) + '\n')
