#!/usr/bin/env python3
"""Independent real-space disk normalization and synthetic fit controls."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key]='1'
import datetime,json
import numpy as np
from scipy.integrate import quad
from scipy.special import ellipkm1,ellipe
from galaxy_forward import guard,OUT,basis,G,digest
from compare_responses import prediction,fit

guard();checks=[]
for R in [.3,1.,3.,10.]:
    def integrand(a):
        if a==0:return 0.
        complement=((R-a)/(R+a))**2
        angular=2/(R*a)*((R*R+a*a)/(R+a)*ellipkm1(complement)-(R+a)*ellipe(1-complement))
        return a*a*np.exp(-a*a/2)/(2*np.pi)*angular
    direct,err=quad(integrand,0,14,points=[R],epsabs=1e-11,epsrel=1e-10,limit=200)
    hankel=basis(np.array([R]),np.array([0.]),1.,0,lambdas=np.array([]),nodes=2048)[0,0,0]/(G*R)
    checks.append({'R':R,'direct':direct,'hankel':float(hankel),'relative':float(abs(direct/hankel-1)),'quad_error':err})
    assert abs(direct/hankel-1)<1e-8,checks
R=np.geomspace(.3,15,40);g=np.array([100*(R/(R+3))]);d=np.array([800*R*np.exp(-R/3)+80])
data={'R':R,'gas':g,'disk':d,'weight':np.ones(40)/40}
true={'U':.47,'a0':1.6e-10};data['v']=prediction(data,'NL',true)
p,info=fit(data,'NL',False)
assert abs(p['U']/.47-1)<1e-5 and abs(p['a0']/1.6e-10-1)<1e-5
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'code_sha256':digest(__file__),
 'real_space_gaussian_checks':checks,'synthetic_nonlinear_parameter_recovery':p,'recovery_rms':info['loss']**.5,
 'no_target_Vobs_used':True,'repair_note':'Initial throwaway direct-space control used ellipk(1-complement), rounding to its singular argument near a=R; it stopped at an assertion before target fits. Stable ellipkm1(complement) resolves the integrable logarithm without relaxing tolerances.'}
(OUT/'preflight_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
