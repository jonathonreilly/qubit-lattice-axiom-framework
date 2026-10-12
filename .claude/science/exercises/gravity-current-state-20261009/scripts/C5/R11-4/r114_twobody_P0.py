"""R11-4 (b),(c),(iii): the actual d = 3 two-body triplet (R9-6 law: m = 0.5, kappa = 0.8, g_a = q_a b(|q|^2),
b = sstep(1 - q^2/kappa^2)/kappa) in the P = 0 fibre, where q = k1 = -k2 and every leg is in the exact box.
 - kinetic (constituent) forward stress  Pi_kin^ij = <sum_legs k_i k_j / eps>  = <2 q_i q_j / eps(q)>
 - interaction forward stress, from the Ward identity: int T_I^ij = i[W, D_ij] with D_ij = (1/2){r_i, q_j}, r = i d/dq
   (the relative part of the constituent momentum-density first moment; M_I's term i[H, M_I] has zero
   expectation in an H-eigenstate).  Von Laue: Pi_kin + Pi_int = 0.
 - comparator: h_ij coupled to the constituents only -> passive weight E + gamma tr Pi_kin at rest.
 - tidal quadrupole: constituent-dust T00 (free energy at the legs, interaction energy at the centre, R9-10 s3.1)
   vs the closed form (all energy at the centre): Q^ab = (1/2) <r_a eps r_b> (sym) vs 0.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
m, kap = 0.5, 0.8
eps = lambda r: np.sqrt(m*m + r*r)
b = lambda r: sstep(1 - r*r/kap**2)/kap
def db(r, h=1e-6): return (b(r+h) - b(r-h))/(2*h)
xr, wr = leggauss(400); r = 0.5*kap*(xr + 1); wr = 0.5*kap*wr       # radial nodes on [0, kappa]
M0 = 2*eps(r)
def pr(*a): print(*a, flush=True)
pr('m = %.2f, kappa = %.2f; radial GL 400 nodes; P = 0 fibre; triplet polarisation x' % (m, kap))
for Mb in (0.95, 0.85, 0.70):
    # lambda from 1 = lam <g_x|(Mb - M0)^-1|g_x>,  <g_x|F|g_x> = (4pi/3) int r^4 b^2 F dr
    G = (4*np.pi/3)*np.sum(wr*r**4*b(r)**2/(Mb - M0))
    lam = 1.0/G
    u = b(r)/(Mb - M0)                                    # phi_x = N q_x u(r)
    du = (db(r)*(Mb - M0) + b(r)*2*r/eps(r))/(Mb - M0)**2  # u'(r)  (d/dr of b/(Mb - 2 eps))
    N2 = 1.0/((4*np.pi/3)*np.sum(wr*r**4*u**2)); N = np.sqrt(N2)
    # check eigen-equation residual on the radial function: (M0 - Mb) u + lam b <g|phi>/N = 0
    gphi = (4*np.pi/3)*np.sum(wr*r**4*b(r)*u)               # <g_x|phi>/N
    res = np.max(np.abs((M0 - Mb)*u + lam*b(r)*gphi))
    # kinetic stress: <2 q_i q_j / eps>, angular: int q_i q_j q_x^2 dOmega = 4pi/15 r^4 (delta_ij + 2 d_ix d_jx)
    K1 = N2*(4*np.pi/15)*np.sum(wr*r**6*u**2*2/eps(r))    # coefficient of (delta_ij + 2 d_ix d_jx)
    Pkin = K1*np.diag([3.0, 1.0, 1.0])
    # interaction stress <i[V, D_ij]> = -2 I_ij, I_ij = int (V phi)(q_j d_i phi + delta_ij phi/2)
    # V phi = lam g_x <g_x|phi> = lam N gphi q_x b ; d_i phi = N(delta_ix u + q_x q_i u'/r)
    # angular integrals: int q_x * q_j (delta_ix u + q_x q_i u'/r) dOmega and int q_x q_x dOmega
    Iint = np.zeros((3,3))
    A2 = 4*np.pi/3; A4 = 4*np.pi/15
    for i in range(3):
        for j in range(3):
            # term1: int q_x q_j delta_ix u  -> delta_ix * A2 r^4 delta_jx  (times b r^?)
            t1 = (1.0 if (i == 0 and j == 0) else 0.0)*A2*np.sum(wr*r**2*r**2*b(r)*u)
            # term2: int q_x q_j q_x q_i u'/r -> A4 (delta_ij + 2 d_ix d_jx) r^4 * r^2 u'/r
            t2 = A4*((1.0 if i == j else 0.0) + 2*(1.0 if (i == 0 and j == 0) else 0.0))*np.sum(wr*r**2*r**4*b(r)*du/r)
            t3 = (0.5 if i == j else 0.0)*A2*np.sum(wr*r**2*r**2*b(r)*u)
            Iint[i,j] = lam*gphi*N2*(t1 + t2 + t3)
    Pint = -2*Iint
    Pint = 0.5*(Pint + Pint.T)
    vl = Pkin + Pint
    trk = np.trace(Pkin)
    # dust quadrupole of the constituent T00 (free energy at the legs r/2, -r/2): (1/2) int eps d_a phi d_b phi
    # d_a phi = N(delta_ax u + q_x q_a u'/r)
    Qd = np.zeros((3,3))
    for a_ in range(3):
        for b_ in range(3):
            dax = 1.0 if a_ == 0 else 0.0; dbx = 1.0 if b_ == 0 else 0.0
            s1 = dax*dbx*A2*np.sum(wr*r**2*eps(r)*u**2)                 # u^2 term (angular int of 1 = 4pi -> careful)
            s1 = dax*dbx*4*np.pi*np.sum(wr*r**2*eps(r)*u**2)
            s2 = (dax*A2*(1.0 if b_ == 0 else 0.0) + dbx*A2*(1.0 if a_ == 0 else 0.0))*np.sum(wr*r**2*r**2*eps(r)*u*du/r)
            s3 = A4*((1.0 if a_ == b_ else 0.0) + 2*dax*dbx)*np.sum(wr*r**2*r**4*eps(r)*du**2/r**2)
            Qd[a_,b_] = 0.5*N2*(s1 + s2 + s3)
    Qtl = Qd - np.trace(Qd)/3*np.eye(3)
    pr('\nM_b = %.2f (f_B = %.2f): lam = %.5f, radial eigen residual %.1e, <r^2>-scale' % (Mb, 1 - Mb, lam, res))
    pr('  kinetic forward stress Pi_kin (diag) = %s ; trace/M_b = %.6f' % (np.round(np.diag(Pkin), 8), trk/Mb))
    pr('  interaction forward stress (Ward: i[W, D]) diag = %s' % np.round(np.diag(Pint), 8))
    pr('  von Laue: max |Pi_kin + Pi_int| = %.2e  (relative to |Pi_kin| %.2e)' % (np.abs(vl).max(), np.abs(vl).max()/np.abs(Pkin).max()))
    pr('  comparator (h_ij sees constituents only): passive-weight shift gamma*tr Pi_kin/M_b = %.6f (gamma = 1)' % (trk/Mb))
    pr('  constituent-dust T00 quadrupole (pol. x): diag = %s; traceless spin-aligned part Q_xx - Q_yy = %.6f; closed form: 0'
       % (np.round(np.diag(Qd), 6), Qd[0,0] - Qd[1,1]))
    pr('  scale comparison: S^2/M_b (Kerr-like spin quadrupole scale, hbar = a = 1) = %.4f' % (2.0/Mb))
    globals().setdefault('rows', []).append((Mb, trk/Mb, Qd[0,0] - Qd[1,1]))
pr('\nEotvos-type comparator between binding fractions if h_ij couples to constituents only (gamma = 1, at rest):')
for i in range(len(rows)):
    for j in range(i+1, len(rows)):
        a1 = 1 + rows[i][1]; a2 = 1 + rows[j][1]
        pr('  f_B %.2f vs %.2f: eta = 2|a1 - a2|/(a1 + a2) = %.4f  (box stress with interaction term: 0, proved)' % (1-rows[i][0], 1-rows[j][0], 2*abs(a1-a2)/(a1+a2)))
