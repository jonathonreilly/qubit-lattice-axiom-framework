# numeric end-to-end check: build the 4x4 walk at the optimal b, check unitarity, masslessness, dispersion expansion
import numpy as np, mpmath as mp
mp.mp.dps = 40
r6,r15 = mp.sqrt(6), mp.sqrt(15)
b1 = (5*r6-2*r15)/27; b2 = (2*r15-2*r6)/27; b0 = b1+2*b2
def Gmat(b0,b1,b2):
    return mp.matrix([[1-3*b0**2, -2*b0*b1, -b0**2-b0*b2+b1**2, -3*b1*(b0-b2)],
                      [-2*b0*b1, b0**2-2*b1**2, b1*(b0-b2), b0*b2-b1**2+b2**2],
                      [-b0**2-b0*b2+b1**2, b1*(b0-b2), 2*b1**2-b2**2, 2*b1*b2],
                      [-3*b1*(b0-b2), b0*b2-b1**2+b2**2, 2*b1*b2, 3*b2**2]])
G = Gmat(b0,b1,b2); phi0 = mp.matrix([1,3,3,1])
a = G*phi0
H = G - a*a.T
E, Q = mp.eigsy(H)
print('eig(G - a a^T):', [mp.nstr(e,8) for e in E])
idx = sorted(range(4), key=lambda i: -E[i])[:2]
cs = [Q[:,i]*mp.sqrt(max(E[i],0)) for i in idx]
print('c_i . phi0 :', [mp.nstr((c.T*phi0)[0],5) for c in cs])
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1]);I2=np.eye(2)
def phi(k):
    c=[mp.cos(x) for x in k]; return mp.matrix([1,sum(c),c[0]*c[1]+c[0]*c[2]+c[1]*c[2],c[0]*c[1]*c[2]])
def U(k):
    p=phi(k); c=[mp.cos(x) for x in k]; s=[mp.sin(x) for x in k]
    f=(a.T*p)[0]; h=[(ci.T*p)[0] for ci in cs]
    g=[s[i]*(b0+b1*(c[(i+1)%3]+c[(i+2)%3])+b2*c[(i+1)%3]*c[(i+2)%3]) for i in range(3)]
    gs = float(g[0])*sx+float(g[1])*sy+float(g[2])*sz
    return float(f)*np.eye(4)+1j*float(h[0])*np.kron(sx,I2)+1j*float(h[1])*np.kron(sy,I2)+1j*np.kron(sz,gs)
rng=np.random.default_rng(1)
print('max |UU^dag - 1| over random k:', max(np.abs(U(rng.uniform(-np.pi,np.pi,3))@U(rng.uniform(0,0,3)).conj().T*0+U(k:=rng.uniform(-np.pi,np.pi,3))@U(k).conj().T-np.eye(4)).max() for _ in range(200)))
print('U(0)=', np.round(U([0,0,0]).real,12).diagonal())
# dispersion: omega^2 along directions, compare with s^2 r^2 + (alpha |n|^4 + beta sum n^4) r^4 + ...
s = b0+2*b1+b2; alpha = s**2*(s**2-1)/12
print('s =', mp.nstr(s,20), ' sqrt(6)/3 =', mp.nstr(r6/3,20), ' alpha=',mp.nstr(alpha,12))
def om2(k):
    F = (G*phi0).T*phi(k); return mp.acos(F[0])**2
for n0 in ([1,0,0],[1,1,0],[1,1,1],[3,5,-8]):
    n = np.array(n0)/np.linalg.norm(n0)
    n4 = float(np.sum(n**4))
    # fit coefficient of r^6 numerically via Richardson
    def r6coef(r):
        nm=[mp.mpf(x) for x in n0]; nr=mp.sqrt(sum(x*x for x in nm)); k=[mp.mpf(r)*x/nr for x in nm]
        return (om2(k)-s**2*r**2-alpha*r**4)/r**6
    vals=[r6coef(mp.mpf(10)**-e) for e in (3,4)]
    C1 = s**2*(324*0-0)  # placeholder
    sig=s/3
    C1 = sig**2*(324*sig**4-45*sig**2+2)/40; C2=-s**2/360; C3=-9*(b1+b2)*(2*b1-3*b2)/10
    pred = C1 + C2*n4 + C3*float(np.prod(n**2))
    print('dir',np.round(n,3),' numeric r^6 coef', mp.nstr(vals[-1],10), ' predicted', mp.nstr(pred,10))
