"""
T238 - does the framework's own regulator induce a MAXWELL term?

R85/R132/R135: the heat trace Tr e^{-s Delta} induces the Einstein-Hilbert term
with coefficient 1.00000 +- 0.00003 -- Sakharov's mechanism, verified.  The SAME
Seeley-DeWitt coefficient a2 that carries the curvature-squared terms also
carries F_{mu nu}F^{mu nu}.  So the same regulator should induce a Maxwell term.

This checks the coefficient against an EXACT answer.  For a constant field the
continuum gauged heat kernel is the Landau-level result

      (4 pi s) K(s) / V  =  sB / sinh(sB)  =  1 - (sB)^2/6 + ...

so a2 = -B^2/6 per unit volume in 2D; with F_{mu nu}F^{mu nu} = 2B^2 that is
      a2 = -(1/12) F_{mu nu} F^{mu nu}
which is the standard gauge term.  Nothing is imported: the lattice spectrum is
computed and compared with sB/sinh(sB).

Gauge: A_x = 0, A_y = phi * x1 with phi = 2 pi m / L, which is periodic in x1 and
puts flux phi through every plaquette.  Translation invariance in x2 lets each
k2 be diagonalised separately.
"""
import numpy as np

def spectrum(L, m):
    phi = 2*np.pi*m/L                       # flux per plaquette = B (a=1)
    ev = []
    x1 = np.arange(L)
    for j in range(L):
        k2 = 2*np.pi*j/L
        d = 4 - 2*np.cos(k2 + phi*x1)       # y-hops with the gauge phase
        M = np.diag(d).astype(complex)
        for i in range(L):                  # x-hops
            M[i, (i+1) % L] += -1.0
            M[(i+1) % L, i] += -1.0
        ev.append(np.linalg.eigvalsh(M))
    return np.concatenate(ev), phi

def heat(ev, s):
    return np.array([np.sum(np.exp(-si*ev)) for si in s])

print("continuum target:  (4 pi s) K/V = sB/sinh(sB) = 1 - (sB)^2/6 + (7/360)(sB)^4 ...\n")
for L, m in ((64,1), (96,1), (128,1)):
    ev, B = spectrum(L, m)
    ev0, _ = spectrum(L, 0)
    xs = np.array([0.05, 0.1, 0.2, 0.3, 0.5, 0.8])       # in units of 1/B
    s = xs/B
    K = heat(ev, s); K0 = heat(ev0, s)
    lhs = (4*np.pi*s)*K/(L*L)
    lhs0 = (4*np.pi*s)*K0/(L*L)
    tgt = (s*B)/np.sinh(s*B)
    print(f"=== L={L}, flux/plaquette B = {B:.5f} ===")
    print("   sB      (4pi s)K/V    sB/sinh(sB)     ratio      free-field (4pi s)K0/V")
    for i in range(len(s)):
        print(f"  {s[i]*B:5.2f}   {lhs[i]:11.6f}   {tgt[i]:11.6f}   {lhs[i]/tgt[i]:8.5f}"
              f"      {lhs0[i]:11.6f}")
    # extract the (sB)^2 coefficient from the MEASURED curve, free part divided out
    r = lhs/lhs0
    A = np.vstack([(s*B)**2, (s*B)**4]).T
    c, *_ = np.linalg.lstsq(A, r-1.0, rcond=None)
    print(f"   fit  K_B/K_0 - 1 = c2 (sB)^2 + c4 (sB)^4 :"
          f"   c2 = {c[0]:+.6f}   (continuum -1/6 = {-1/6:+.6f})"
          f"   -> a2 coefficient of F^2 = {c[0]/2:+.6f} (continuum -1/12 = {-1/12:+.6f})\n")

# ---------------------------------------------------------------------------
# the residual is an O(a) lattice artefact: B = 2 pi/L in lattice units, so
# extrapolate c2(B) -> B = 0.
# ---------------------------------------------------------------------------
print("=== continuum extrapolation of the induced Maxwell coefficient ===")
Bs, c2s = [], []
for L in (48, 64, 96, 128, 160):
    ev, B = spectrum(L, 1); ev0, _ = spectrum(L, 0)
    xs = np.array([0.05,0.1,0.2,0.3,0.5,0.8]); s = xs/B
    r = ((4*np.pi*s)*heat(ev,s)/(L*L)) / ((4*np.pi*s)*heat(ev0,s)/(L*L))
    A = np.vstack([(s*B)**2, (s*B)**4]).T
    c,*_ = np.linalg.lstsq(A, r-1.0, rcond=None)
    Bs.append(B); c2s.append(c[0])
    print(f"   L={L:4d}  B={B:.5f}   c2 = {c[0]:+.6f}   "
          f"implied slope k = {(c[0]+1/6)/B:+.5f}")
Bs = np.array(Bs); c2s = np.array(c2s)
p = np.polyfit(Bs, c2s, 1)
print(f"\n   linear fit  c2 = c2(0) + k B :  c2(0) = {p[1]:+.6f}   k = {p[0]:+.5f}")
print(f"   continuum value -1/6 = {-1/6:+.6f}   ->  error {abs(p[1]+1/6):.2e}")
print(f"   a2 coefficient of F_munu F^munu = {p[1]/2:+.6f}  "
      f"(continuum -1/12 = {-1/12:+.6f}, error {abs(p[1]/2+1/12):.2e})")
print("""
=== why this singles out d = 4 for the gauge sector ===
   the induced action is  int dtau/tau (4 pi tau)^{-d/2} tau^2 int a2  ~  tau0^{2-d/2}
     d < 4 : positive power  -> super-renormalisable, coupling has mass dimension
     d = 4 : LOG divergent   -> the gauge coupling is DIMENSIONLESS (marginal)
     d > 4 : negative power  -> non-renormalisable
   four dimensions is the unique case in which the induced gauge coupling is
   marginal.""")
