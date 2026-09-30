"""T51 S4: build the lane's texture numerically; which mass states carry nu_e (U_e = I)? and what the
historic alpha^2 candidate does to the OTHER gaps under the lane's labels."""
import numpy as np
aLM = 2*0.045333918
MPl, v, y = 1.22089e19, 246.3, 6.66e-3
c = y**2*v**2*1e9
A = MPl*aLM**7; B = MPl*aLM**8
def texture(r): return np.array([[A,0,0],[0,r*B,B],[0,B,r*B]])
for label, r in [('retained r=alpha/2', aLM/2), ('historic candidate r=alpha^2', aLM**2)]:
    M = texture(r)
    w, U = np.linalg.eigh(M)                    # real symmetric; Takagi values = |w|
    m = c/np.abs(w)                             # light masses, eV, universal Y
    idx = np.argsort(m)                         # ascending mass = nu1,nu2,nu3 (lane labels)
    m = m[idx]; U = U[:,idx]
    print(f'== {label}: masses (meV) {np.round(m*1e3,3)}')
    print('   |U_ei|^2 with U_e=I (row e = flavour 1):', np.round(np.abs(U[0,:])**2,4), ' <- nu_e sits entirely in the lightest state')
    print('   |U_mu i|^2:', np.round(np.abs(U[1,:])**2,4), '  |U_tau i|^2:', np.round(np.abs(U[2,:])**2,4))
    print(f'   lane labels: dm21={m[1]**2-m[0]**2:.3e}  dm31={m[2]**2-m[0]**2:.3e}  dm32={m[2]**2-m[1]**2:.3e}')
    print('   data (NuFit 5.3 as quoted): dm21=7.41e-5  dm31~2.45-2.51e-3  dm32~dm31-dm21')
print('Historic note quotes "solar" 7.56e-5 = m3^2-m2^2 (i.e. dm32 in lane labels); data dm32 ~ 2.4e-3.')
