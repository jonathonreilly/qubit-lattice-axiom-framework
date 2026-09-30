"""T62 test C: which counting law can produce rho_Lambda/rho_P ~ 1.1e-123 at all?
rho_vac a^4 = xi * N^(-p);  N is what the record lattice can count in the causal patch."""
import numpy as np
from scipy.integrate import quad
c=299792458.0; hbar=1.054571817e-34; G=6.67430e-11; Mpc=3.0856775814913673e22
lP=np.sqrt(hbar*G/c**3); tP=lP/c
H0=67.4e3/Mpc; Om=0.315; OL=0.685; Or=9.2e-5
E=lambda a: np.sqrt(Or/a**4+Om/a**3+OL+ (1-Om-OL-Or)/a**2)
# cosmic time t(a), conformal distance chi(a) (units of c/H0 -> convert to Planck)
t_of_a=lambda a: quad(lambda x: 1/(x*E(x)), 1e-12, a, limit=400)[0]/H0
t0=t_of_a(1.0)
# past light cone: comoving radius chi(a) = int_a^1 da'/(a'^2 H)  (c=1) ; proper radius r = a*chi
chi=lambda a: quad(lambda x: 1/(x*x*E(x)), a, 1.0, limit=400)[0]/H0*c   # metres (comoving)
# V4 = int dt (4pi/3) r^3 = int da/(a H) (4pi/3) (a chi)^3
def integrand(a): 
    r=a*chi(a)
    return (4*np.pi/3)*r**3/(a*H0*E(a))
V4=quad(integrand, 1e-6, 1.0, limit=200)[0]          # m^3 s
V4_planck=V4/(lP**3*tP)
Tage=t0/tP
print("age t0=%.3f Gyr (flat LCDM Planck-like, incl. radiation), T=t0/tP=%.3e"%(t0/3.15576e16,Tage))
print("past-light-cone 4-volume V4=%.3e Planck 4-volumes = %.3f * T^4 (T^4=%.3e)"%(V4_planck,V4_planck/Tage**4,Tage**4))

fobs=1.134e-123                       # rho_Lambda/rho_P (H0=67.4, OL=0.685), from t62_units.py
Rl=1.026e61
N3=(4*np.pi/3)*Tage**3                # sites in a ball of radius c*t0 (upper bound on records: one per site, permanent)
S=np.pi*Rl**2                         # de Sitter entropy in nats
laws=[
 ("A. Poisson creations only        N<=sites(3D)   p=1/2", N3,0.5),
 ("B. Poisson site-tick events      N=V4 (4D)      p=1/2", V4_planck,0.5),
 ("C. hyperuniform density fluct.   Var=N^(2/3)    dN/N=N^(-2/3)", N3,2/3),
 ("D. inverse area count            N=S_dS         p=1", S,1.0),
 ("E. inverse volume count          N=sites(3D)    p=1", N3,1.0),
 ("F. Poisson on area count         N=S_dS         p=1/2", S,0.5),
]
print("\nobserved log10(rho_L/rho_P) = %.2f"%np.log10(fobs))
print("%-62s %8s %10s %14s %s"%("law","p*q","log10pred","xi needed","pass(<=1.5 dec)"))
for name,N,p in laws:
    pred=N**(-p)
    lp=-p*np.log10(N)
    xi=fobs/pred
    q=np.log10(N)/np.log10(Tage)
    print("%-62s %8.3f %10.2f %14.3e %s"%(name,p*q,lp,xi,"PASS" if abs(np.log10(xi))<=1.5 else "FAIL (%.1f decades)"%abs(np.log10(xi))))
print("\nTracking check: a law with p*q=2 gives rho_vac ~ 1/T^2 ~ H^2 at every epoch, i.e. Omega_vac ~ const, not a constant Lambda (w=-1 would need L fixed).")
