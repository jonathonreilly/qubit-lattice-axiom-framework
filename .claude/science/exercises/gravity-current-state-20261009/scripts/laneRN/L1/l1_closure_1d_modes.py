import numpy as np
L=64
x=np.arange(L)
S=np.roll(np.eye(L),1,axis=1)  # (S f)_u = f_{u+1}
I=np.eye(L)
def D(xi):  # delta phi_u = 1/2[xi_u(phi_{u+1}-phi_u) + xi_{u-1}(phi_u-phi_{u-1})]
    return 0.5*(np.diag(xi)@(S-I) + np.diag(np.roll(xi,1))@(I-S.T))
xi=np.cos(2*np.pi*x/L); et=np.sin(2*np.pi*x/L)*0.7+0.2
C=D(xi)@D(et)-D(et)@D(xi)
# fit by D(zeta)
B=np.array([D(np.eye(L)[k]).ravel() for k in range(L)]).T
sol=np.linalg.lstsq(B,C.ravel(),rcond=None)[0]
print("rel resid",np.linalg.norm(B@sol-C.ravel())/np.linalg.norm(C))
lie = xi*np.gradient(et)-et*np.gradient(xi)  # continuum [xi,eta]
print("fitted zeta vs continuum Lie bracket (first 5):",np.round(sol[:5],4),np.round(lie[:5],4))
print("norm C",np.linalg.norm(C), "norm D(lie)", np.linalg.norm(D(lie)))
F=np.fft.fft(np.eye(L))/np.sqrt(L)
k=2*np.pi*np.fft.fftfreq(L)
xh=x+0.5  # link centres
xi=np.cos(2*np.pi*xh/L); et=np.sin(2*np.pi*xh/L)*0.7+0.2
dxi=-2*np.pi/L*np.sin(2*np.pi*xh/L); det=0.7*2*np.pi/L*np.cos(2*np.pi*xh/L)
C=D(xi)@D(et)-D(et)@D(xi)
lie=xi*det-et*dxi
Dl=D(lie)
for kc in (0.2,0.5,1.0,np.pi+0.1):
    sel=np.abs(k)<kc
    Fs=F[:,sel]
    a=Fs.conj().T@C@Fs; b=Fs.conj().T@Dl@Fs
    print(f"kc={kc:.2f}: |C - D([xi,eta])| / |C| on modes |k|<kc = {np.linalg.norm(a-b)/np.linalg.norm(a):.4f}  (sign check {np.linalg.norm(a+b)/np.linalg.norm(a):.3f})")
