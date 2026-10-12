# O4 numbers: record bounds from observations. Pure arithmetic; no downloads.
import math
hbar=1.054571817e-34; c=2.99792458e8; G=6.67430e-11; u=1.66053907e-27
me=9.1093837e-31; mn=1.67492750e-27; mN=1.6726e-27; eps0=8.8541878e-12; e=1.602176634e-19
alpha=e**2/(4*math.pi*eps0*hbar*c)
lP=math.sqrt(hbar*G/c**3); rho=1/lP**4          # events per m^4 (x0=ct)
print(f"lP={lP:.4e} m, rho=lP^-4={rho:.3e} m^-4, events/m^3/s={rho*c:.3e}")
Vn=4/3*math.pi*(0.84e-15)**3
print(f"Planck events per nucleon volume per s = {rho*c*Vn:.3e}")
# --- Lemma C check: integral of (1/|x-a|-1/|x-b|)^2 d^3x = 4 pi d  (numeric radial check via Fourier formula)
from math import sin
def I_num(d,N=400000,umax=4000.0):
    # int_0^inf (1-sin u/u)/u^2 du should be pi/4
    s=0.0; h=umax/N
    for i in range(1,N+1):
        x=i*h; s+= (1-sin(x)/x)/x**2 if x>1e-3 else 1/6
    s*=h; s+= 1/umax  # tail ~ int_umax^inf du/u^2
    return s
print(f"int (1-sinu/u)/u^2 = {I_num(1):.6f}  vs pi/4={math.pi/4:.6f}")
# --- experiments: (name, mass kg, d m, T s, status)
exps=[
 ("electron (illustrative biprism)", me, 1e-5, 6e-10, "illustrative d,T"),
 ("neutron perfect-crystal interferometer", mn, 1e-2, 25e-6, "d~cm, T~25us (NIST typical)"),
 ("Cs-133 lattice interferometer, 70 s (Panda 2024)", 133*u, 1e-6, 70.0, "d taken 1 um (lower bound guess)"),
 ("Rb-87 54 cm, 2.08 s (Kovachy 2015)", 87*u, 0.54, 2.08, "superposition reading disputed"),
 ("25 kDa molecule (Fein 2019)", 25000*u, 2.66e-7, 7e-3, "d ~ grating period"),
 ("Na cluster >170 kDa (Pedalino 2026)", 1.7e5*u, 1.33e-7, None, "d ~ UV grating period; T not verified"),
]
print("\n== Theorem C: Poisson count=volume records at rho=lP^-4 tracking matter volume element ==")
print("fine:  -lnV = 2 pi (mc^2/hbar)^2 (d/c) T ;  coarse (cells l_c=c tau_c >> d, tau_c>=T): -lnV=(2pi/3)(d/lamC)^2 (cT)^2/(l_c c tau_c)")
for name,m,d,T,st in exps:
    lamC=hbar/(m*c)
    single=(2*math.pi/3)*(d/lamC)**2      # experiment-sized cell, l_c=c tau_c=cT
    fine= 2*math.pi*(m*c**2/hbar)**2*(d/c)*T if T else float('nan')
    # coarse scale needed for -lnV <= 0.1 with l_c = c tau_c
    lc_req = math.sqrt((2*math.pi/3)/0.1)*(d/lamC)*c*T if T else float('nan')
    print(f"{name:48s} lamC={lamC:.2e} m  (d/lamC)^2={ (d/lamC)**2:.2e}  fine -lnV={fine:.2e}  single-cell -lnV={single:.2e}  l_c needed={lc_req:.2e} m  [{st}]")
print(f"(Hubble radius ~1.3e26 m; 1 kpc = 3.1e19 m)")
# --- heating: Gaussian position lock of resolution a: dE = 3 hbar^2/(8 m a^2) per lock (3 axes)
Pkg=47e12/5.97e24
Pn=Pkg*mN
print(f"\n== Heating: Earth heat flow {Pkg:.2e} W/kg -> {Pn:.2e} W per nucleon (all heat; anomalous allowance smaller) ==")
Nev=rho*c*Vn
for a in [lP,1e-19,1e-15,1e-10,1e-7,1e-6]:
    dE=3*hbar**2/(8*mN*a**2)
    G_n=Pn/dE
    print(f"a={a:.2e} m: dE/lock={dE:.2e} J ({dE/1.602e-13:.2e} MeV); max lock rate per nucleon={G_n:.2e} /s; max fraction of Planck events={G_n/Nev:.2e}")
# CSL cross-check: lambda <= P * 4 m rC^2/(3 hbar^2)
rC=1e-7
print(f"CSL-convention Earth-heat bound at rC=1e-7: lambda <= {Pn*4*mN*rC**2/(3*hbar**2):.2e} /s")
# --- EM field-strength records at vacuum-limited resolution: -lnV ~ alpha c T/(4 kappa d) (far zone), kappa=O(1)
print("\n== EM field-strength records at vacuum-limited resolution (far zone only, kappa=1) ==")
for d,T in [(1e-5,6e-10),(1e-6,6e-10),(1e-4,1e-9)]:
    print(f"charge e, d={d:.0e} m, T={T:.0e} s: -lnV ~ {alpha*c*T/(4*d):.2e}")
# gravity field-strength records: far zone ~ G m^2 T/(4 hbar d)  (DP-like), near zone cut at cell size -> DP with R0=cell
for name,m,d,T,st in exps:
    if T: print(f"grav far-zone DP-like {name:40s}: G m^2 T/(4 hbar d) = {G*m**2*T/(4*hbar*d):.2e}")
# DP near-zone with R0 = lP per nucleon: rate ~ G mN^2/(hbar lP)
print(f"DP self-energy rate per nucleon with R0=lP: {G*mN**2/(hbar*lP):.2e} /s ; with R0=0.54 A: {G*mN**2/(hbar*0.54e-10):.2e} /s")
# Coherence-only bounds (energy-free locks of conserved local quantities)
print("\n== Coherence-only bounds on energy-free locks ==")
print(f"ion hyperfine qubit >1 h: lock rate on that qubit <= ~{1/3600:.1e} /s ; per Planck event touching the ion volume (~(1e-10 m)^3): {1/3600/(rho*c*1e-30):.1e}")
print(f"Cs 70 s spatial: per atom <= ~{1/70:.1e} /s; per nucleon (incoherent) <= {1/70/133:.1e} /s")
