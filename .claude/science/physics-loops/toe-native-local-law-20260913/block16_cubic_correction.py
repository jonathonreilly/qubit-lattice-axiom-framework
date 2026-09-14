"""Explore the next nodal Fourier term; coefficient arithmetic is floating."""
from pathlib import Path
import numpy as np,json,hashlib

p=Path(__file__).resolve().parent
source=(p/'block16_casimir_check.py').read_text()
ns={};exec(source.split('rows=[]')[0],ns)
energy,leading,G,xn,zn=ns['energy'],ns['leading'],ns['G'],ns['xn'],ns['zn']


class Jet:
    def __init__(self,data):self.d=data if isinstance(data,dict) else {(0,0,0):float(data)}
    def __add__(self,other):
        other=other if isinstance(other,Jet) else Jet(other);out=self.d.copy()
        for k,v in other.d.items():out[k]=out.get(k,0)+v
        return Jet(out)
    __radd__=__add__
    def __neg__(self):return Jet({k:-v for k,v in self.d.items()})
    def __sub__(self,other):return self+-Jet(other) if not isinstance(other,Jet) else self+-other
    def __rsub__(self,other):return -self+other
    def __mul__(self,other):
        other=other if isinstance(other,Jet) else Jet(other);out={}
        for a,v in self.d.items():
            for b,w in other.d.items():
                c=tuple(x+y for x,y in zip(a,b))
                if sum(c)<=3:out[c]=out.get(c,0)+v*w
        return Jet(out)
    __rmul__=__mul__
    def __truediv__(self,x):return self*(1/x)
    def __pow__(self,n):
        out=Jet(1)
        for _ in range(n):out=out*self
        return out


def coefficients(signx,signz):
    qx,qy,qz=[Jet({tuple(int(i==j) for i in range(3)):1}) for j in range(3)]
    cx0=np.cos(xn);sx0=signx*np.sin(xn);cz0=np.cos(zn);sz0=signz*np.sin(zn)
    cx=cx0-sx0*qx-cx0*qx**2/2+sx0*qx**3/6
    sx=sx0+cx0*qx-sx0*qx**2/2-cx0*qx**3/6
    L=np.sqrt(.96)+sz0*qz+(qy**2+cz0*qz**2)/2-sz0*qz**3/6
    S=qy**2+L**2+1-1.2*L*cx+.04
    U=.64*L**2*sx**2+.04*((.6*L-cx)**2+sx**2)
    u0=U.d[(0,0,0)];delta=(U-u0)/u0
    root=np.sqrt(u0)*(1+delta/2-delta**2/8+delta**3/16)
    F=S-2*root
    for power,v in F.d.items():
        if sum(power)<2:assert abs(v)<2e-12
        if sum(power)==2:
            expected=G[power.index(2)] if 2 in power else 0
            assert abs(v-expected)<2e-12
    return {power:v for power,v in F.d.items() if sum(power)==3 and abs(v)>1e-13}


nodes=[(sx,sz,coefficients(sx,sz)) for sx in [-1,1] for sz in [-1,1]]


def correction(L,phi,M):
    m=np.indices((2*M+1,)*3).reshape(3,-1).T-M;m=m[np.any(m,axis=1)]
    u=m/G;v=np.sum(m*m/G,axis=1);total=np.zeros(len(m),complex)
    for sx,sz,coeff in nodes:
        D=np.zeros(len(m))
        for powers,c in coeff.items():
            i,j,k=[axis for axis,power in enumerate(powers) for _ in range(power)]
            derivative=-48*u[:,i]*u[:,j]*u[:,k]/v**4
            derivative+=8*((i==j)*u[:,k]/G[i]+(i==k)*u[:,j]/G[i]+(j==k)*u[:,i]/G[j])/v**3
            D+=c*derivative
        total+=1j*np.exp(-1j*L*(m[:,0]*sx*xn+m[:,2]*sz*zn))*D
    return float(np.real(np.sum((np.exp(1j*m@np.array(phi))-1)*total))/(4*np.pi**2*np.sqrt(np.prod(G))*L**2))


rows=[]
for phi in [[0,np.pi,0],[np.pi,np.pi,np.pi]]:
    for L in [8,16,32,48]:
        exact=float(energy(L,phi)-energy(L,[0,0,0]));first=leading(L,phi,24);second=correction(L,phi,16)
        rows.append(dict(L=L,phi=phi,full_lattice=exact,leading=first,second=second,
                         residual=exact-first-second,L3_residual=L**3*(exact-first-second)))
out=dict(helper_sha256=hashlib.sha256(source.encode()).hexdigest(),
         cubic_coefficients=[dict(sign_x=sx,sign_z=sz,coefficients={str(k):v for k,v in cs.items()}) for sx,sz,cs in nodes],rows=rows,
         limitation='Floating jet coefficients and finite reciprocal sums. No certified numerical asymptotic remainder or interacting result.')
(p/'BLOCK16_CUBIC_CORRECTION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
