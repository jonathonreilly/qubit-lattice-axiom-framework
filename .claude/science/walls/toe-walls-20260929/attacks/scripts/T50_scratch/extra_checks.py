"""T50 extra checks (output: extra_checks.out): scale-space midpoint, rung steps, y alternatives, geometric-midpoint form."""
import math
M_PL=1.2209e19; V=246.22; y=0.653**2/64; obs=2.453e-3
def dm(M1):
    m3=y*y*V*V/M1*1e9; return m3*m3
print("scale-space (arithmetic) midpoint M1=(M_Pl+v)/2:", f"Dm2={dm((M_PL+V)/2):.3e} eV^2, ratio to obs {dm((M_PL+V)/2)/obs:.2e}")
g=math.sqrt(M_PL*V)
print("log-midpoint M1=sqrt(M_Pl v)=%.4e GeV Dm2=%.4e (%+.2f%%)"%(g,dm(g),100*(dm(g)/obs-1)))
for k in (7,9):
    M1=M_PL**(1-k/16)*V**(k/16); print(f"rung k={k}: Dm2={dm(M1):.3e}  ratio {dm(M1)/obs:.1f}")
for name,f in (('g^2/32',2),('g^2/128',0.5),('g^2/64 * sqrt2',2**0.5),('g^2/64/sqrt2',2**-0.5)):
    print(name, f"Dm2={dm(g)*f**4:.3e} ratio {dm(g)*f**4/obs:.2f}")
