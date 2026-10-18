# Chirality of U=+I nodes of the D'Ariano-Perinotti Weyl QCA A+_k = e^{-i kx sx/r3} e^{-i ky sy/r3} e^{-i kz sz/r3} (BCC, Eq.33 of 1306.1934)
import numpy as np, itertools
sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]]); sz=np.diag([1,-1]).astype(complex); I2=np.eye(2); S=[sx,sy,sz]
r3=np.sqrt(3)
def U(k): 
    out=I2
    for j in range(3): out=out@(np.cos(k[j]/r3)*I2-1j*np.sin(k[j]/r3)*S[j])
    return out
H=[np.array(h)/r3 for h in itertools.product([1,-1],repeat=3)]  # BCC neighbour vectors
def equiv0(k): return all(abs(np.exp(1j*np.dot(k,h))-1)<1e-9 for h in H)
def chir(k,e=1e-6):
    U0inv=np.linalg.inv(U(k)); a=np.zeros((3,3))
    for j in range(3):
        d=np.zeros(3); d[j]=e
        A=1j*(U(k+d)-U(k-d))/(2*e)@U0inv
        for b in range(3): a[j,b]=np.real(np.trace(A@S[b]))/2
    return int(np.sign(np.linalg.det(a)))
# scan a fine grid of one reciprocal cell for U ~ +I or -I, then classify
pts={'+I':[], '-I':[]}
g=np.linspace(-r3*np.pi, r3*np.pi, 41)
for k in itertools.product(g,repeat=3):
    k=np.array(k); u=U(k)
    for lab,t in (('+I',I2),('-I',-I2)):
        if np.linalg.norm(u-t)<1e-9:
            if not any(all(abs(np.exp(1j*np.dot(k-p,h))-1)<1e-7 for h in H) for p in pts[lab]): pts[lab].append(k)
for lab in pts:
    print(lab, [(np.round(p/(r3*np.pi),3).tolist(), chir(p)) for p in pts[lab]], 'net chirality =', sum(chir(p) for p in pts[lab]))
