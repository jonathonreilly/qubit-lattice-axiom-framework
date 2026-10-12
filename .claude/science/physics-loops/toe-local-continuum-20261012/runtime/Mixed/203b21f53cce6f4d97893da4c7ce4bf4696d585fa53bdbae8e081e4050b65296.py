"""Executable Q1/Q2/Q15/Q19 and ordered Wick formulas under test."""
import numpy as np
from scipy.sparse import coo_matrix, diags
from scipy.sparse.linalg import expm_multiply

TIME_SIGN = 1.0
TRANSLATION_DIRECTION = -1
Q15_DISPLACEMENT_SIGN = -1.0
COVARIANCE_REAL_ONLY = False
PFAFFIAN_ALTERNATING = True

def couplings(a,m,v):
    d=np.sqrt(m*m/4+v*v/a**2)
    return d/2+m/4,d/2-m/4

def matrices(indices,a,m,v,finite_open=False):
    indices=np.asarray(indices);assert np.all(np.diff(indices)==1)
    g,J=couplings(a,m,v);size=2*len(indices)
    rows=[];cols=[];vals=[]
    def put(r,c,z):rows.append(r);cols.append(c);vals.append(z)
    for k,n in enumerate(indices):
        put(2*k,2*k+1,2j*g);put(2*k+1,2*k,-2j*g)
        if k>0:put(2*k,2*k-1,-2j*J)
        if k+1<len(indices):put(2*k+1,2*k+2,2j*J)
    D=coo_matrix((vals,(rows,cols)),shape=(size,size)).tocsr()
    X=diags(np.repeat(a*indices,2));B=(X@D+D@X)/2-a*D/2
    if finite_open:
        D=D.tolil();B=B.tolil()
        for k in [0,len(indices)-1]:
            D[2*k,2*k+1]-=1j*g;D[2*k+1,2*k]+=1j*g
        for k,z in [(0,1j*a*g*(1-indices[0])),(len(indices)-1,-1j*a*g*indices[-1])]:
            B[2*k,2*k+1]+=z;B[2*k+1,2*k]+=np.conj(z)
        D=D.tocsr();B=B.tocsr()
    return D,B

def shift(z,n):
    z=np.asarray(z);out=np.zeros_like(z);cells=z.reshape(-1,2);target=out.reshape(-1,2)
    if n==0:target[:]=cells;lost=0.
    elif 0<n<len(cells):target[n:]=cells[:-n];lost=np.linalg.norm(cells[-n:])
    elif -len(cells)<n<0:target[:n]=cells[-n:];lost=np.linalg.norm(cells[:-n])
    else:lost=np.linalg.norm(cells)
    return out,float(lost)

def lattice_word(z,word,a,D,B):
    z=np.asarray(z,dtype=complex).copy();loss=[]
    for kind,p in reversed(word):
        if kind=='t':z=expm_multiply(TIME_SIGN*1j*p*D,z,traceA=0)
        elif kind=='b':z=expm_multiply(-1j*p*B,z,traceA=0)
        elif kind=='x':
            z,lost=shift(z,TRANSLATION_DIRECTION*int(np.floor(p/a)))
            loss.append(lost)
        else:raise ValueError(kind)
    return z,loss

def positive_word(psi,q,word,m,v):
    q=np.asarray(q);factor=np.ones_like(q,dtype=complex);current=q.copy()
    for kind,p in word:
        E=np.sqrt(m*m+v*v*current**2)
        if kind=='t':factor*=np.exp(TIME_SIGN*1j*p*E)
        elif kind=='x':factor*=np.exp(-1j*TRANSLATION_DIRECTION*p*current)
        elif kind=='b':
            eta=v*p;after=current*np.cosh(eta)+E/v*np.sinh(eta)
            factor*=np.sqrt(np.sqrt(m*m+v*v*after**2)/E);current=after
        else:raise ValueError(kind)
    return factor*psi(current)

def q15_rhs(s,t,v):
    return [('x',Q15_DISPLACEMENT_SIGN*v*t*np.sinh(v*s)),('t',t*np.cosh(v*s))]

def q16_rhs(s,ell,v):
    return [('x',ell*np.cosh(v*s)),('t',-ell/v*np.sinh(v*s))]

def pair(f,g,P):
    result=2*np.vdot(f,P@g)
    return complex(result.real) if COVARIANCE_REAL_ONLY else complex(result)

def covariance(vectors,projected):
    result=2*np.asarray(vectors).conj()@np.asarray(projected).T
    return result.real.astype(complex) if COVARIANCE_REAL_ONLY else result

def pfaffian(upper):
    upper=np.asarray(upper);n=len(upper)
    if n==0:return 1.+0j
    assert n%2==0
    out=0j
    for j in range(1,n):
        sign=(-1)**(j+1) if PFAFFIAN_ALTERNATING else 1
        remaining=[k for k in range(1,n) if k!=j]
        out+=sign*upper[0,j]*pfaffian(upper[np.ix_(remaining,remaining)])
    return out

def periodic_project(vectors,indices,a,m,v,padding):
    assert padding>len(indices)
    work=np.zeros((len(vectors),padding,2),complex)
    slots=np.asarray(indices)%padding
    work[:,slots,:]=np.asarray(vectors).reshape(len(vectors),len(indices),2)
    hat=np.fft.fft(work,axis=1);q=2*np.pi*np.fft.fftfreq(padding,d=a)
    g,J=couplings(a,m,v)
    off=2j*(g-J*np.exp(-1j*a*q));E=np.abs(off)
    projected=np.empty_like(hat)
    projected[:,:,0]=(hat[:,:,0]+off[None,:]/E[None,:]*hat[:,:,1])/2
    projected[:,:,1]=(hat[:,:,1]+off.conj()[None,:]/E[None,:]*hat[:,:,0])/2
    back=np.fft.ifft(projected,axis=1)
    return back[:,slots,:].reshape(len(vectors),-1)
