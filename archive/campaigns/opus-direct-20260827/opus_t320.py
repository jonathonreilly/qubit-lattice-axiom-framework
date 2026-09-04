"""
T320 - the framework's induced COSMOLOGICAL CONSTANT, and whether its gravity is
self-consistent.

The same proper-time regulator that induces the Einstein-Hilbert term (R132/R135)
also induces a vacuum energy from the a0 coefficient. That has never been
computed here, and with tau0 now known to 8 digits (R196) and N=6 derived (R195)
it is parameter-free.

  per real scalar:  Gamma_E/V = -(1/2) int_{tau0}^inf (dtau/tau) (4 pi tau)^{-2}
                              = -1/(64 pi^2 tau0^2)
  N fields:         |rho_vac| = N/(64 pi^2 tau0^2)
  Newton:           G = 12 pi tau0 / N            (R85/R132/R135, R195)

The striking part: the product G*rho_vac is INDEPENDENT of N --
  G |rho_vac| = (12 pi tau0/N)(N/(64 pi^2 tau0^2)) = 3/(16 pi tau0)
so the self-consistency question does not depend on the field content at all.

Einstein with a pure CC (T_munu = -rho g_munu), trace in d=4:
  -R = 8 pi G T = 8 pi G (-4 rho)  =>  |R| = 32 pi G |rho| = 6/tau0
The curvature radius is then |R|^{-1/2}. Compare it to the lattice spacing a:
if it is smaller than a, the flat-lattice starting point is inconsistent.
"""
import numpy as np
from scipy.special import ive
from scipy.integrate import quad
W4=quad(lambda t: ive(0,2*t)**4,0,np.inf,limit=400)[0]
tau0=1/(16*np.pi**2*W4)                 # R196, in units a=1
N=6                                      # R195
G=12*np.pi*tau0/N
lP=np.sqrt(G)
rho=N/(64*np.pi**2*tau0**2)
print(f"tau0            = {tau0:.7f} a^2      (R196, 8-digit)")
print(f"N               = {N}                  (R195)")
print(f"G               = {G:.7f} a^2")
print(f"ell_P           = {lP:.6f} a")
print(f"|rho_vac|       = {rho:.4f} a^-4")
print(f"                = {rho*lP**4:.6f} in Planck units (ell_P^-4)")
print()
GR=G*rho
print(f"G*|rho_vac|     = {GR:.6f} a^-2     3/(16 pi tau0) = {3/(16*np.pi*tau0):.6f}   [N-independent]")
R=32*np.pi*G*rho
print(f"|R| = 32 pi G rho = {R:.4f} a^-2      6/tau0 = {6/tau0:.4f}")
rad=1/np.sqrt(R)
print(f"curvature radius  = {rad:.5f} a   =  {rad/lP:.5f} ell_P")
print()
print(f"  lattice spacing a          = 1")
print(f"  curvature radius / a       = {rad:.5f}")
print(f"  -> spacetime curves {1/rad:.1f}x FASTER than the lattice spacing")
print()
# check N-independence explicitly
print("N-independence check (the conclusion must not move with field content):")
for n in (1,2,6,12,100):
    g=12*np.pi*tau0/n; r=n/(64*np.pi**2*tau0**2)
    print(f"    N={n:4d}   G={g:.5f}  |rho|={r:9.3f}   radius={1/np.sqrt(32*np.pi*g*r):.5f} a")
print()
obs=1.1e-123
print(f"observed rho_Lambda ~ {obs:.1e} in Planck units")
print(f"framework predicts  ~ {rho*lP**4:.3e}          ratio {rho*lP**4/obs:.2e}")
