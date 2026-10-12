"""C5 R13-5 (b)-(c): TT cone shifts for the W1-complete class, the class bound, birefringence tuning, and the split table.

Class W_V (stated in the report): W1-complete pair stresses (r135_w1_pair.py) whose TT pair vertex at q || z
 (i) depends only on the transverse pair momenta (R9-9's class V), and
 (ii) equals the continuum minimal vertex on box-transverse momenta |k_x|,|k_y| <= B (box exactness, transported to all k_z by (i)):
      T_2g: |V|^2 = 4 k_x^2 k_y^2,  E_g: |V|^2 = (k_x^2 - k_y^2)^2 on box-perp;  free (>= 0, smooth, right C4v parity) elsewhere.
Theorem T (R9-9, refereed): Xi = (1/32) < |V|^2 A_zz / eps^5 >, A_zz = u''(k_z)/2 - 1;  c_T^2 - 1 = 2 kappa_lat Xi.
Split decomposition: Xi = Xi_boxperp + Xi_edgeperp; Xi_edgeperp = (1/32) int_{edge-perp} |V|^2(k_perp) I(m^2 + u_x + u_y) d^2k/(2pi)^3,
 I(Bv) = int dk_z A_zz (Bv + u_z)^{-5/2}:  G: I < 0 for every Bv (proved, R9-9);  L: I > 0 on the scanned range (checked, R9-9).
Subtractions (named before the run): none. Xi is an exact identity of one-loop integrals; any q-independent (ultralocal) seagull
 drops out of Xi by construction; no channel or tail is subtracted. The matter-side J values are R11-1's (dD-M, lambda -> 0
 extrapolated, refereed and reproduced by the referee, vR11-1:15-17); nothing is subtracted from them here.
"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r99_profiles_copy import profile, B, B2, plateau

def grids(name, m, N):
    k = 2*np.pi*(np.arange(N) - N//2)/N
    u, up, upp = profile(name, k)
    p = up/2; A = upp/2 - 1.0
    ux, uy, uz = u[:, None, None], u[None, :, None], u[None, None, :]
    eps = np.sqrt(m*m + ux + uy + uz)
    W = A[None, None, :]/eps**5/32
    bperp = ((np.abs(k)[:, None] <= B + 1e-12) & (np.abs(k)[None, :] <= B + 1e-12))[:, :, None]
    eta = (1 - plateau(k, B, B2)[:, None]*plateau(k, B, B2)[None, :])[:, :, None]   # 0 on box-perp, 1 beyond B2
    kx, ky = k[:, None, None], k[None, :, None]
    verts = {'U': (4*p[:, None, None]**2*p[None, :, None]**2, (p[:, None, None]**2 - p[None, :, None]**2)**2),
             'M': (4*ux*uy, (ux - uy)**2),
             'cont': (4*kx**2*ky**2, (kx**2 - ky**2)**2)}
    return k, W, bperp, eta, verts

J = {('G', 1.0): -5.51217e-03, ('G', 0.3): -5.11254e-04, ('L', 1.0): -6.88690e-03, ('L', 0.3): -6.53589e-04}  # R11-1 dD-M
kap = 8*np.pi      # kappa_lat at a = l_P
X = {}
print('=== (b1) Xi split into box-perp (vertex fixed = continuum in W_V) and edge-perp (free) parts; N = 128 ===')
for name in ['G', 'L']:
    for m in [1.0, 0.3, 0.1, 0.01]:
        k, W, bperp, eta, verts = grids(name, m, 128)
        row = []
        for pol, ip in [('T2g', 0), ('Eg', 1)]:
            Vc = verts['cont'][ip]
            xb = np.mean(np.broadcast_to(Vc*bperp, W.shape)*W)
            out = {'box': xb}
            for mem in ['U', 'M']:
                V = verts[mem][ip]
                xe = np.mean(np.broadcast_to(V*(~bperp), W.shape)*W)
                xbm = np.mean(np.broadcast_to(V*bperp, W.shape)*W)
                out[mem] = (xbm + xe, xbm, xe)
            X[(name, m, pol)] = out
            row.append('%s: Xi_boxperp=%+.4e | U: total %+.4e (box %+.4e, edge %+.4e) | M: total %+.4e (edge %+.4e)'
                       % (pol, xb, out['U'][0], out['U'][1], out['U'][2], out['M'][0], out['M'][2]))
        print('[%s m=%.2f]\n   %s\n   %s' % (name, m, row[0], row[1]))
print('   (on box-perp the U and M vertices coincide with the continuum one: u = k^2, p = k there)')

print('\n=== (b2) class bound in W_V and sizes at a = l_P (kappa_lat = 8 pi): c_T - 1 ~ kappa Xi ===')
for name in ['G', 'L']:
    for m in [1.0, 0.3, 0.01]:
        for pol in ['T2g', 'Eg']:
            xb = X[(name, m, pol)]['box']
            rel = '<=' if name == 'G' else '>='
            print('  %s m=%.2f %-3s: every member has Xi %s %+.4e  -> 16pi^2|Xi| %s %.4f ; |c_T - 1| at a=l_P >= %.2e ; a/l_P needed for |dc| < 1e-15 (one species): >= %.1e'
                  % (name, m, pol, rel, xb, '>=', 16*np.pi**2*abs(xb), kap*abs(xb), np.sqrt(kap*abs(xb)/1e-15)))

print('\n=== (b3) birefringence in W_V: one smooth edge knob c (E_g edge-perp weight x (1 + (c-1) eta)), tuned at m = 1 ===')
for name in ['G', 'L']:
    for mem in ['U']:
        cs = {}
        for m in [1.0, 0.3, 0.1]:
            k, W, bperp, eta, verts = grids(name, m, 128)
            VT, VE = verts[mem]
            xT = np.mean(np.broadcast_to(VT, W.shape)*W)
            xE0 = np.mean(np.broadcast_to(VE*(1 - eta), W.shape)*W)
            xE1 = np.mean(np.broadcast_to(VE*eta, W.shape)*W)
            cs[m] = (xT, xE0, xE1)
        xT, xE0, xE1 = cs[1.0]
        c = (xT - xE0)/xE1
        print('  %s %s: c* = %.4f (>= 0: %s) makes Xi_Eg = Xi_T2g at m = 1;' % (name, mem, c, c >= 0))
        for m in [1.0, 0.3, 0.1]:
            xT, xE0, xE1 = cs[m]
            print('      m=%.1f: Xi_T2g=%+.5e  Xi_Eg(c*)=%+.5e  diff=%+.2e' % (m, xT, xE0 + c*xE1, xT - xE0 - c*xE1))

print('\n=== (b4) split table c_m - c_T = kappa_lat (2J - Xi), in kappa_lat/16pi^2 units; J = R11-1 dD-M (external = loop species mass) ===')
for name in ['G', 'L']:
    for m in [1.0, 0.3]:
        for pol in ['T2g', 'Eg']:
            o = X[(name, m, pol)]
            xU, xM, xb = o['U'][0], o['M'][0], o['box']
            lab = 'W_V bound' if name == 'G' else 'W_V bound'
            print('  %s m=%.1f %-3s: 2J=%+.4e | M: %+.4f | U: %+.4f | paired (Xi=0): %+.4f | at a=l_P: M %+.3e U %+.3e paired %+.3e'
                  % (name, m, pol, 2*J[(name, m)], 16*np.pi**2*(2*J[(name, m)] - xM), 16*np.pi**2*(2*J[(name, m)] - xU),
                     16*np.pi**2*2*J[(name, m)], kap*(2*J[(name, m)] - xM), kap*(2*J[(name, m)] - xU), kap*2*J[(name, m)]))
print('\n  Light external matter (m_ext a -> 0, Lemma M: J = m^2 J2 -> 0), loop species m = 0.01: c_m - c_T -> -kappa Xi:')
for name in ['G', 'L']:
    for pol in ['T2g', 'Eg']:
        o = X[(name, 0.01, pol)]
        print('  %s %-3s: U %+.4f, M %+.4f, W_V bound: |.| >= %.4f (kappa/16pi^2 units); at a = l_P: U %+.3e ; bound %.3e ; ratio to 1e-15 band >= %.1e'
              % (name, pol, -16*np.pi**2*o['U'][0], -16*np.pi**2*o['M'][0], 16*np.pi**2*abs(o['box']), -kap*o['U'][0], kap*abs(o['box']), kap*abs(o['box'])/1e-15))
print('  Paired unit (Theorem PT/S, matched masses): Xi = 0, so c_m - c_T = 2 kappa J = 4 kappa m^2 J2: proton at a = l_P (m a = 7.7e-20):'
      ' G %.1e, L %.1e' % (kap*2*(7.7e-20)**2*(-5.68e-3)*2/2, kap*2*(7.7e-20)**2*(-7.30e-3)*2/2))
