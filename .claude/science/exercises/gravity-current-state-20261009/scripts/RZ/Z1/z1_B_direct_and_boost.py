"""Z1 (B): (1) direct 3D-momentum evaluation of the node-level noise PSD p(sigma) at FINITE gamma with the exact Phi (op0),
       p(sigma) = (2pi)^-4 * 4pi int k^2 dk |Phi(k^2 - sigma^2 + gamma^2/4 - i gamma sigma)|^2,
   compared with the white level 1/(8 pi^2 c2^2 gamma): flat from sigma = 0 (DC) to sigma ~ 1/gamma, i.e. NOT concentrated at the carrier.
(2) observer boosted by rapidity eta_b relative to the growth direction N: low-frequency level
       p_obs(sigma) = (2pi)^-4 int d^3k |Phi(w)|^2, w = |k|^2 - sigma^2 + gamma^2/4 - i gamma (sigma cosh eta_b - k mu sinh eta_b),
   predicted p_obs/p_rest = eta_b/sinh(eta_b) (pole part Phi = 1/(c2 w), which is exact as gamma*sigma*e^{eta_b} -> 0).
"""
import numpy as np, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from rl2_core_copy import OPS, fvals, c2_of
from z1_A_spectrum import Phi, sv
t0 = time.time()
C = OPS[0]; fs = fvals(C, sv); c2 = c2_of(C)
def p_direct(sig, gam, nv=1601, PhiF=None):
    a = gam/2.0
    vlo = np.arcsinh(-sig/a); vhi = np.arcsinh(3e3/a)
    vv = np.linspace(vlo, vhi, nv); k = sig + a*np.sinh(vv); dk = a*np.cosh(vv)*(vv[1]-vv[0])
    w = k**2 - sig**2 + gam**2/4 - 1j*gam*sig
    P = PhiF(w) if PhiF else Phi(fs, w)
    return 4*np.pi*np.sum(k**2*np.abs(P)**2*dk)/(2*np.pi)**4
print("(1) op0, c2 = %.6f. Direct p(sigma) * 8 pi^2 c2^2 gamma (white level -> 1):" % c2)
for gam in [1e-2, 1e-3]:
    row = []
    for sig in [0.0, 0.1*gam, gam, 10*gam, 0.1, 1.0, 0.1/gam, 1/gam, 10/gam]:
        p = p_direct(sig, gam); row.append((sig, p*8*np.pi**2*c2**2*gam))
    print("  gamma = %.0e: " % gam + "  ".join("s=%.2g:%.4f" % r for r in row)); sys.stdout.flush()
print("  (G(b)/G(0+) from z1_A at b = gamma*sigma should match the large-sigma entries)")
# (2) boosted observer, pole part
def p_boost(sig, gam, eta, nk=3001, nmu=3001):
    # per-direction near-shell map: shell width in k is gam*D(mu)/2, D = cosh(eta) - mu sinh(eta)
    x = np.linspace(0, 1, nmu); mu = 1 - 2*x**3; dmu = 6*x**2*(x[1]-x[0])
    s = np.linspace(0, 1, nk); tot = 0.0
    for m, dm in zip(mu, dmu):
        if dm == 0: continue
        D = np.cosh(eta) - m*np.sinh(eta); a = max(gam*D/2.0, 1e-300)
        vlo, vhi = np.arcsinh(-sig/a), np.arcsinh(50*sig/a)
        vv = vlo + (vhi-vlo)*s; k = sig + a*np.sinh(vv); dk = a*np.cosh(vv)*(vhi-vlo)/(nk-1)
        w = k**2 - sig**2 + gam**2/4 - 1j*gam*(sig*np.cosh(eta) - k*m*np.sinh(eta))
        tot += dm*np.sum(k**2/np.abs(c2*w)**2*dk)
    return 2*np.pi*tot/(2*np.pi)**4
print("(2) boosted observer, pole part Phi = 1/(c2 w); gamma = 1e-6, sigma = 1e-3:")
gam = 1e-6; sig = 1e-3; p0 = p_boost(sig, gam, 0.0)
print("   eta_b = 0: p*8pi^2c2^2 gamma = %.4f" % (p0*8*np.pi**2*c2**2*gam))
for eta in [0.5, 1.0, 2.0, 4.0, 6.0]:
    pb = p_boost(sig, gam, eta)
    print("   eta_b = %.1f: p_obs/p_rest = %.5f ; eta/sinh(eta) = %.5f" % (eta, pb/p0, eta/np.sinh(eta))); sys.stdout.flush()
print("elapsed %.0fs" % (time.time()-t0))
