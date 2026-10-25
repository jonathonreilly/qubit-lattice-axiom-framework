import numpy as np
d=0.6
def C3(w,d=d):
    w=np.asarray(w,float); E=lambda k: np.exp(1j*k*d*w)
    num=(-2j*d**3*w**3*E(4)+2j*d**3*w**3*E(2)-6*d**2*w**2*E(4)-6*d**2*w**2*E(2)-3j*d*w*E(6)-9j*d*w*E(4)+9j*d*w*E(2)+3j*d*w+3*E(6)-3*E(4)-3*E(2)+3)
    return (4*num*E(-3)/w**6).real
W=20000
ws=np.arange(-W,W+1).astype(float)
c=np.zeros_like(ws); nz=ws!=0
c[nz]=C3(ws[nz])
# w=0 limit: numeric from sympy later; get via small w
c[W]=304*d**6/15
print('C(0)~',c[W],'C(1)',c[W+1])
# kappa on grid
for N in (16,24,32,48,64,96,128):
    # lambda_j = N sum_{w=j mod N} C(w)
    lam=[N*c[(ws%N)==j].sum() for j in range(N)]
    # torus: kappa^2 spectrum: conv
    print(N, 'min lam %.4e'%min(lam), 'argmin', int(np.argmin(lam)), 'max %.4f'%max(lam), 'rel %.3e'%(min(lam)/max(lam)))
# kappa(Delta) on fine grid then square, FFT
M=4096
th=2*np.pi*np.arange(M)/M
kap=np.zeros(M)
# kappa = sum_w C(w) e^{iw th}; use FFT: coefficients array
coef=np.zeros(M,complex)
for w,v in zip(ws.astype(int),c): coef[w%M]+=v
kap=np.fft.ifft(coef).real*M
print('kappa(0)',kap[0],'min kappa',kap.min())
k2=kap**2
sp=np.fft.fft(k2)/M
print('torus-time uniform pool spectrum min/max (kappa^2):',sp.real.min(),sp.real.max())
