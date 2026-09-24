#!/usr/bin/env python3
"""Separate finite-Fock characteristic and finite-sum packet checks."""
from pathlib import Path
import json,hashlib,time
import numpy as np
from scipy.linalg import eigh

start=time.monotonic()
N=12
ann=np.diag(np.sqrt(np.arange(1,N)),1);q=ann+ann.T
d=np.array([.7,-.4]);X=d[0]*np.kron(q,np.eye(N))+d[1]*np.kron(np.eye(N),q)
ev,U=eigh(X);vac=np.zeros(N*N,dtype=complex);vac[0]=1
alpha=np.array([np.sqrt(.3),1j*np.sqrt(.7)]);omega=np.array([.9,1.7])
fock=[]
for g in (.1,.25,.4):
    W=(U*np.exp(1j*g*ev))@U.T
    for t in (0.,.7,2.,4.):
        at=alpha*np.exp(-1j*omega*t);psi=np.zeros(N*N,dtype=complex)
        psi[N]=at[0];psi[1]=at[1]
        chi=np.dot(at,d);expected=np.exp(-g*g*np.dot(d,d)/2)*(1-g*g*abs(chi)**2)
        actual=np.vdot(psi,W@psi);error=abs(actual-expected)
        assert error<2e-13
        fock.append({'g':g,'time':t,'chi_abs_squared':float(abs(chi)**2),
                     'actual_real':float(actual.real),'actual_imaginary':float(actual.imag),
                     'formula':float(expected),'absolute_error':float(error)})

L=64;V=L*6*6;k=2*np.pi*np.array([5,6,7])/L;k0=k[1];sigma=k[2]-k0
omegas=2*np.sin(k/2);omega0=2*np.sin(k0/2);velocity=np.cos(k0/2)
weights=np.array([1.,2.,1.])/np.sqrt(6)*np.exp(-1j*k*10)
d0=(np.exp(1j*k)-1)/np.sqrt(2*V)/np.sqrt(omegas)
A=float(np.sum(abs(weights*d0)));M=float(np.pi/(k0-sigma));xs=np.arange(L)
packets=[]
for t in (0.,8.,20.):
    actual=np.exp(1j*np.outer(xs,k))@(weights*d0*np.exp(-1j*omegas*t))
    linear=np.exp(1j*np.outer(xs,k))@(weights*d0*np.exp(-1j*(omega0+velocity*(k-k0))*t))
    error=float(np.max(abs(actual-linear)));bound=A*M*t*sigma*sigma/2
    contrast_error=float(np.max(abs(abs(actual)**2-abs(linear)**2)))
    contrast_bound=A*A*M*t*sigma*sigma
    assert error<=bound+1e-16 and contrast_error<=contrast_bound+1e-16
    packets.append({'time':t,'max_amplitude_error':error,'amplitude_bound':bound,
                    'max_intensity_error':contrast_error,'intensity_bound':contrast_bound,
                    'actual_peak_site':int(np.argmax(abs(actual)**2)),
                    'linear_peak_site':int(np.argmax(abs(linear)**2))})
result={'scope':'Separate Fock space and harmonic packet controls, not telescope data or full postbirth propagation',
        'finite_fock_rows':fock,'packet_parameters':{'V':V,'k0':float(k0),'band_radius':float(sigma),
              'group_velocity_sites_per_time':float(velocity),'coarse_Hessian_bound':M,'A':A},
        'packet_rows':packets,'elapsed_seconds':time.monotonic()-start,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_name('NARROW_PACKET_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
