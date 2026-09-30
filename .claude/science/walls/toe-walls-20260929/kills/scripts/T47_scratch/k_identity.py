import sys, math
sys.dont_write_bytecode=True
import numpy as np
import ladder_infvol as L
rh=L.rh; tcomp=rh.tcomp
for N in (15,41,81):
    sysm=rh.build_size_system(N)
    pe=rh.phi_from_q(sysm,rh.E0); ps=rh.phi_from_q(sysm,rh.S_UNIT)
    d=pe-ps; c=(N-1)//2
    nz=np.argwhere(np.abs(d)>1e-13)
    print("N=%d: max|phi_E0-phi_S| = %.3e ; #sites with |diff|>1e-13: %d ; at origin diff=%.6f (1/6=%.6f)"%(N,np.abs(d).max(),len(nz),d[c,c,c],1/6))
    print("   nonzero sites (rel. to centre):",[tuple(x-c) for x in nz][:10])
    print("   anchors E0,S:",rh.anchor(sysm,rh.E0),rh.anchor(sysm,rh.S_UNIT))
