"""OBS-4 R1 table: B-gen (conjugated) and B-gen120 carrier couplings in the mass basis at equal vevs (v_K = v/2):
aligned (diagonal) part vs flavour-changing entries that drive K, D, B_d, B_s mixing."""
import numpy as np
from obs4_core import *
from obs4_r1 import realisations, physical
R = realisations(); vK = VEV / 2
for name in ('B-gen(as fitted)', 'B-gen120(as fitted)'):
    Mu, Md, cj = physical(*R[name]); mb = mass_basis(Mu, Md); Pu, Pd = carrier_hats(Mu, Md, mb)
    print(f"{name}{' [conj]' if cj else ''}: carrier couplings Yhat = Phat/v_K at v_K = {vK:.2f} GeV")
    print("  K  | diag u,c,t (aligned)        | |uc| |cu|      | diag d,s,b (aligned)          | |sd| |ds|        | |bd| |db|        | |bs| |sb|")
    for K in CARRIERS:
        U = Pu[K] / vK; D = Pd[K] / vK
        print(f"  {K}  | {np.abs(np.diag(U))[0]:.3f} {np.abs(np.diag(U))[1]:.3f} {np.abs(np.diag(U))[2]:.3f} | {abs(U[0,1]):.3f} {abs(U[1,0]):.3f} | "
              f"{np.abs(np.diag(D))[0]:.2e} {np.abs(np.diag(D))[1]:.2e} {np.abs(np.diag(D))[2]:.2e} | {abs(D[1,0]):.2e} {abs(D[0,1]):.2e} | "
              f"{abs(D[2,0]):.2e} {abs(D[0,2]):.2e} | {abs(D[2,1]):.2e} {abs(D[1,2]):.2e}")
    U = sum(Pu.values()) / VEV; D = sum(Pd.values()) / VEV
    print(f"  light h direction (sum_K v_K Yhat^K / v = M/v): max |off-diag| up {np.abs(U-np.diag(np.diag(U))).max():.1e}, down {np.abs(D-np.diag(np.diag(D))).max():.1e}")
