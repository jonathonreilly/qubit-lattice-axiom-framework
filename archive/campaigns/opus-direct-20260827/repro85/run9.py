"""Is the R57 reality criterion (index even under flux reversal) even restrictive in d=4?
Complex conjugation flips ALL fluxes at once. Test the ORDINARY COMPLEX Wilson-Dirac in d=4."""
import numpy as np, importlib.util
spec=importlib.util.spec_from_file_location("m","run_d4.py")
import sys
src=open("run_d4.py").read().split("Gam,Gbar,G=kd_gammas(4)")[0]
g={}; exec(src,g)
build_DW4=g['build_DW4']; idx_of=g['idx_of']; gg=g['g']; g5=g['g5']
print("d=4, ORDINARY 4-component Wilson-Dirac (gamma_2 = i*sigma_1(x)sigma_2 -> COMPLEX gammas)")
print(f"  max|Im gamma_mu| = {max(np.max(np.abs(x.imag)) for x in gg):.3f}   (NOT real)")
print(f"  L=4, m_rho=1.0.  index_cont = n12*n34")
print(f"{'(n12,n34)':>12} {'gap':>7} {'GW':>10} {'index':>9}")
for nn in [(0,0),(1,1),(-1,-1),(1,-1),(-1,1),(2,1),(-2,-1),(1,2)]:
    DW=build_DW4(4,nn[0],nn[1],gg); hh,gw,gap,ind=idx_of(DW,g5)
    print(f"{str(nn):>12} {gap:7.3f} {gw:10.2e} {ind:+9.5f}")
print("  => index(n12,n34) == index(-n12,-n34) for the COMPLEX Dirac operator too.")
print("     In d=4 the index is quadratic in F, so evenness under total flux reversal is")
print("     automatic (charge conjugation) and carries NO information about reality.")
