"""Specified coefficient frame and embedding; source-mutated in controls."""
import numpy as np

FRAME_SIGN = +1
CONTINUUM_UNROTATE = True

def parameters(a, m=1., v=1.):
    sigma=np.sqrt(m*m/4+v*v/(a*a))
    return sigma/2+m/4, sigma/2-m/4

def phase(a,k,m=1.,v=1.):
    g,j=parameters(a,m,v)
    return np.angle(g-j*np.exp(-1j*np.asarray(k)))

def frame_ring(a,n,m=1.,v=1.):
    k=2*np.pi*np.fft.fftfreq(n)
    u=np.exp(-1j*k[:,None]*np.arange(n)[None,:])/np.sqrt(n)
    ft=np.kron(u,np.eye(2))
    d=np.empty(2*n,dtype=complex)
    p=np.exp(1j*FRAME_SIGN*phase(a,k,m,v)/2)
    d[0::2]=p;d[1::2]=p.conj()
    return ft.conj().T@(d[:,None]*ft)

def adapted_map(a,n,haar,m=1.,v=1.):
    return frame_ring(a/2,2*n,m,v).conj().T@haar@frame_ring(a,n,m,v)

def embedding_multiplier(a,q,m=1.,v=1.):
    fa=np.exp(1j*FRAME_SIGN*phase(a,a*np.asarray(q),m,v)/2)
    if CONTINUUM_UNROTATE:
        fc=np.exp(1j*FRAME_SIGN*np.arctan(v*np.asarray(q)/m)/2)
        return fc.conj()*fa
    return fa
