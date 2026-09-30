"""T51 S5: independent check of the feasible point with explicit 3x3 matrices and Takagi via SVD (complex-safe)."""
import numpy as np
aLM = 2*0.045333918
MPl, v, y = 1.22089e19, 246.3, 6.66e-3
c = y**2*v**2*1e9
A = MPl*aLM**7; B = MPl*aLM**8
for label,x,r in [('retained',1.0,aLM/2),('feasible pt',2.97,0.678),('rational (x=3,r=2/3)',3.0,2/3),('rational + retained atm anchor',(1-aLM/2)/(1-2/3),2/3)]:
    Bp=x*B; M=np.array([[A,0,0],[0,r*Bp,Bp],[0,Bp,r*Bp]],dtype=complex)
    s=np.linalg.svd(M,compute_uv=False); m=np.sort(c/s)
    print(f'{label:34s} x={x:.3f} r={r:.4f}  m(meV)={np.round(m*1e3,2)} dm21={m[1]**2-m[0]**2:.3e} dm31={m[2]**2-m[0]**2:.3e} R={(m[1]**2-m[0]**2)/(m[2]**2-m[0]**2):.4f} Sigma={m.sum()*1e3:.1f} meV  RH eig ratios (in units of smallest): {np.round(np.sort(s)/np.min(s),3)[::-1][::-1]}')
