import itertools,json
import numpy as np
from scipy.optimize import brentq
from block6_mirror_check import slab,pauli

def matrix(L,k,kind,D=1.):
    H,B,s,b=slab(L,k);dhs=[]
    for a in range(3):
        ds=np.cos(k[a])*pauli[a];db=np.sin(k[a])*np.eye(L)
        dhs.append(np.block([[np.kron(np.eye(L),ds),np.kron(db,np.eye(2))],[np.kron(db.T,np.eye(2)),-np.kron(np.eye(L),ds)]]))
    if kind=='projected':return H[:-2,:-2],[d[:-2,:-2] for d in dhs]
    h=np.zeros((4*L+2,4*L+2),complex);h[:4*L,:4*L]=H
    h[4*L-2:4*L,4*L:]=D*np.eye(2);h[4*L:,4*L-2:4*L]=D*np.eye(2)
    ds=[]
    for d in dhs:
        u=np.zeros_like(h);u[:4*L,:4*L]=d;ds.append(u)
    return h,ds

def optical(kind,L,D,omega):
    zn,zw=np.polynomial.legendre.leggauss(6);corners=[]
    for bits in itertools.product((0,1),repeat=3):
        k0=np.pi*np.array(bits);b=2*sum(bits);S=sum(b**(2*j) for j in range(L));v=1. if kind=='projected' else S/(S+b**(2*L)/D**2)
        integ=0.
        for z,w in zip(zn,zw):
            for phi in np.arange(12)*2*np.pi/12:
                n=np.array([np.sqrt(1-z*z)*np.cos(phi),np.sqrt(1-z*z)*np.sin(phi),z])
                def energy(r):
                    vals=np.linalg.eigvalsh(matrix(L,k0+r*n,kind,D)[0]);mid=len(vals)//2;return vals[mid]-vals[mid-1]
                lo=omega/(4*v);hi=omega/v
                assert energy(lo)<omega<energy(hi)
                radius=brentq(lambda r:energy(r)-omega,lo,hi,xtol=1e-13)
                h,ds=matrix(L,k0+radius*n,kind,D);es,vs=np.linalg.eigh(h);mid=len(es)//2;minus=vs[:,mid-1];plus=vs[:,mid]
                dr=sum(n[a]*ds[a] for a in range(3));slope=(plus.conj()@dr@plus-minus.conj()@dr@minus).real
                vertex=abs(plus.conj()@ds[0]@minus)**2
                integ+=w*2*np.pi/12*radius**2*vertex/slope
        sigma=np.pi/omega/(2*np.pi)**3*integ
        corners.append({'pi_components':list(bits),'normalized_slope':float(sigma/omega*24*np.pi),'expected_inverse_speed':v**-1})
    total=sum(x['normalized_slope'] for x in corners);expected=sum(x['expected_inverse_speed'] for x in corners)
    assert abs(total/expected-1)<.001
    return {'kind':kind,'L':L,'D':D,'omega':omega,'sum_normalized_optical_slope':total,'predicted':expected,'relative_error':total/expected-1,'corners':corners}

if __name__=='__main__':
    print(json.dumps([optical(kind,3,1.,omega) for kind in ('projected','quadratic_dilation') for omega in (.001,.0005)],indent=2))
