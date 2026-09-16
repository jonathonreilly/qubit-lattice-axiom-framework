#!/usr/bin/env python3
"""Distinct Cartesian lattice sums and spherical low-frequency quadratures."""
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_FILES=[]
import hashlib,json,math,time
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss


def lattice(N):
    k=2*math.pi*np.arange(N)/N;q=2*np.sin(k/2);q2=q*q
    yz=q2[:,None]+q2[None,:];out=np.zeros(3)
    for x in q2:
        w2=x+yz;mask=w2>1e-25;w=np.sqrt(w2[mask]);p=1-x/w2[mask]
        out +=[np.sum(p/w),np.sum(p/w**2),np.sum(p/w**3)]
    return out/N**3


def sphere(lam,order):
    mu,wm=leggauss(order);phi=2*math.pi*np.arange(2*order)/(2*order)
    n=np.array(np.broadcast_arrays(np.sqrt(1-mu[:,None]**2)*np.cos(phi),np.sqrt(1-mu[:,None]**2)*np.sin(phi),mu[:,None]))
    angw=wm[:,None]*(2*math.pi/(2*order));r,wr=leggauss(order);r=(r+1)*lam/2;wr=wr*lam/2
    value=0.
    for rr,ww in zip(r,wr):
        jac=np.prod((1-rr*rr*n*n/4)**(-.5),axis=0)
        value+=ww*rr*np.sum(angw*(1-n[0]**2)*jac)/(2*math.pi)**3
    return float(value)


def run():
    started=time.time();rows=[]
    for N in [16,32,64,128,256]:
        a=lattice(N);rows.append({'N':N,'local_vertex_norm_squared':a[0],'inverse_half_energy_norm_squared':a[1],'inverse_energy_norm_squared':a[2]})
    c=1/(3*math.pi**2)
    slopes=[(rows[j]['inverse_energy_norm_squared']-rows[j-1]['inverse_energy_norm_squared'])/math.log(2) for j in range(1,len(rows))]
    assert abs(slopes[-1]-c)<2e-5,(slopes,c)
    assert abs(rows[-1]['local_vertex_norm_squared']-rows[-2]['local_vertex_norm_squared'])<2e-5
    assert rows[-1]['inverse_half_energy_norm_squared']<.2
    angular=[]
    for lam in [.5,.25,.125,.0625]:
        v=sphere(lam,32);v2=sphere(lam,48);base=lam*lam/(6*math.pi**2)
        predicted4=lam**4/(96*math.pi**2)
        row={'lambda':lam,'spectral_mass':v2,'quadrature_change':abs(v2-v),'quadratic_coefficient':v2/lam**2,'quadratic_coefficient_target':1/(6*math.pi**2),'positive_correction':v2-base,'rigorous_correction_upper':lam**4/(12*math.pi**2),'quartic_coefficient_ratio':(v2-base)/predicted4}
        assert abs(v2-v)<1e-14,row
        assert -1e-15<=v2-base<=lam**4/(12*math.pi**2)+1e-15,row
        angular.append(row)
    assert abs(angular[-1]['quartic_coefficient_ratio']-1)<.002
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'periodic_bulk_sums':rows,'inverse_energy_logarithmic_slopes':slopes,'logarithmic_coefficient_target':c,'sharp_low_frequency_quadratures':angular,'seconds':time.time()-started},indent=2))

if __name__=='__main__':run()
