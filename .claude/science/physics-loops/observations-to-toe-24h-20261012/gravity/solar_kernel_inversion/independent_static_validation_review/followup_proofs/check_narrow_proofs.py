#!/usr/bin/env python3
"""Fresh rational/synthetic controls; no author computational helpers imported."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import datetime
from fractions import Fraction as Q
import hashlib
import json
import math
from pathlib import Path
import resource
import time
import mpmath as mp
import numpy as np

HERE=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT=RUNTIME/'gravity/response_inverse/independent_static_validation_review/followup_proofs'
MANIFEST=json.loads((OUT/'snapshot_manifest_v1.json').read_text())


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def guard():
    assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((RUNTIME/n).exists() for n in ['STOP_REQUESTED.json','USER_STOP_REQUESTED','STOP_CAMPAIGN.json'])
    for row in MANIFEST['sources']:
        assert sha(row['snapshot'])==row['sha256']
        if not row['scope'].startswith('section 7'):
            assert sha(row['original'])==row['sha256']


def central(n):return Q(math.comb(2*n,n),4**n)


def rodrigues(ell):
    result=[Q(0) for _ in range(ell+1)]
    for j in range(ell//2+1):
        result[ell-2*j]=Q((-1)**j*math.factorial(2*ell-2*j),
                          2**ell*math.factorial(j)*math.factorial(ell-j)*math.factorial(ell-2*j))
    return result


def laplace_polynomial(ell):
    # Expand (x+i sqrt(1-x^2) cos(phi))^ell and integrate powers of cos(phi).
    result=[Q(0) for _ in range(ell+1)]
    for j in range(ell//2+1):
        factor=math.comb(ell,2*j)*(-1)**j*central(j)
        for k in range(j+1):
            result[ell-2*j+2*k]+=factor*math.comb(j,k)*(-1)**k
    return result


def exact_coefficient(ell):
    # Independent monomial moments, derived by integration by parts plus the
    # beta integral: int_-1^1 (2/pi) asin(x)*x^(2m+1) dx=(1-C_(m+1))/(m+1).
    answer=Q(0)
    for degree,coefficient in enumerate(rodrigues(ell)):
        if degree%2:
            m=(degree-1)//2
            answer+=coefficient*(1-central(m+1))/(m+1)
    return Q(2*ell+1,2)*answer


def kinetic_controls():
    rows=[]
    for n in [Q(-3),Q(0),Q(1),Q(3),Q(101)]:
        k=[[Q(0),Q(1)],[Q(1),-n]]
        inverse=[[n,Q(1)],[Q(1),Q(0)]]
        assert k[0][0]*k[1][1]-k[0][1]*k[1][0]==-1
        assert [[sum(k[i][a]*inverse[a][j] for a in range(2)) for j in range(2)] for i in range(2)]==[[1,0],[0,1]]
        for c in [Q(-2),Q(3,5)]:
            p=[Q(2,3),Q(-5,7)]
            velocity=[sum(inverse[i][j]*p[j] for j in range(2))/(2*c) for i in range(2)]
            lagrangian=c*sum(velocity[i]*k[i][j]*velocity[j] for i in range(2) for j in range(2))
            legendre=sum(p[i]*velocity[i] for i in range(2))-lagrangian
            formula=sum(p[i]*inverse[i][j]*p[j] for i in range(2) for j in range(2))/(4*c)
            assert legendre==formula
            witnesses=[]
            for sign in [-1,1]:
                px,py=Q(1),(Q(sign)-n)/2
                energy=(n*px*px+2*px*py)/(4*c)
                assert energy==Q(sign)/(4*c)
                witnesses.append(str(energy))
            rows.append({'N0':str(n),'C':str(c),'Legendre_H_equals_inverse_formula':True,
                         'opposite_sign_H_witnesses':witnesses})
    return {'exact_rational_cases':rows,'time_Hessian_determinant':'-4*C^2 < 0 for real C != 0',
            'redefinition_scope':'Sylvester inertia applies to an invertible real point-field Jacobian.'}


def harmonic_controls():
    for ell in range(35):assert laplace_polynomial(ell)==rodrigues(ell)
    rows=[]
    for ell in list(range(25))+[31,41,51]:
        independent=exact_coefficient(ell)
        if ell%2:
            n=(ell-1)//2
            proposed=central(n)**2-central(n+1)**2
        else:proposed=Q(0)
        assert independent==proposed
        rows.append({'ell':ell,'coefficient':str(independent)})
    moments=[]
    for count in [0,1,7,31,128]:
        weights=[central(n)**2-central(n+1)**2 for n in range(count+1)]
        tail=central(count+1)**2
        first=sum((2*n+1)*a for n,a in enumerate(weights))
        telescope=1+2*sum(central(n)**2 for n in range(1,count+1))-(2*count+1)*tail
        assert sum(weights)+tail==1 and first==telescope
        assert 2*tail<=Q(2,count+2)
        moments.append({'N':count,'tail':str(tail),'first_moment_float':float(first),
                        'normalization_and_moment_identity_exact':True})
    author=json.loads(Path(MANIFEST['author_resource_receipt']['path']).read_text())
    assert sha(MANIFEST['author_resource_receipt']['path'])==MANIFEST['author_resource_receipt']['sha256']
    mp.mp.dps=75
    relative=[]
    for row in author['coefficients']:
        exact=exact_coefficient(row['l'])
        expected=mp.mpf(exact.numerator)/exact.denominator
        err=abs(mp.mpf(row['coefficient'])/expected-1)
        assert err<mp.mpf('1e-60');relative.append(float(err))
    return {'Laplace_identity_exact_polynomial_degrees':list(range(35)),
            'independent_exact_arcsine_coefficients':rows,'exact_moment_controls':moments,
            'author_receipt_coefficient_max_relative':max(relative)}


def cusp_and_escape_controls():
    mp.mp.dps=75
    cusps=[]
    for k in [mp.mpf('0'),mp.mpf('.17'),mp.mpf('1'),mp.mpf('3')]:
        theta=mp.mpf('1e-16');t=mp.tanh(k*mp.cos(theta))
        # Algebraically stable independent quotient, not subtracting two near units.
        measured=(2/mp.pi)*(1-t)/(1+(1-2*theta/mp.pi)*t)
        exact=(2/mp.pi)*mp.exp(-2*k)
        error=abs(measured/exact-1)
        assert error<mp.mpf('1e-15')
        cusps.append({'k':str(k),'slope':str(exact),'relative_error':str(error),
                      'positive_Legendre_expansion_asserted_for_this_k':False})
    x=np.linspace(-1,1,4001);exact=2/np.pi*np.arcsin(x)
    escapes=[]
    for count in [0,1,4,16,32]:
        coef=np.zeros(2*count+2)
        for n in range(count+1):coef[2*n+1]=float(central(n)**2-central(n+1)**2)
        tail=float(central(count+1)**2);coef[1]+=tail
        approximation=np.polynomial.legendre.legval(x,coef)
        error=float(max(abs(approximation-exact)))
        assert error<=2*tail+1e-13
        assert abs(sum(coef)-1)<1e-14 and min(coef)>=0
        assert abs(approximation[-1]-1)<1e-14 and abs(approximation[0]+1)<1e-14
        escapes.append({'N':count,'sampled_sup_error':error,'proved_uniform_bound':2*tail,
                        'conservative_bound':2/(count+2)})
    return {'cusp_checks':cusps,'finite_accuracy_checks':escapes,
            'scope':'Finite tests do not replace the all-order dominated-convergence or tail proof.'}


def reduced_state_control():
    # N=2 truncated construction, with the tail moved to ell=1; total dimension 42.
    ell=[1,3,5]
    weights=[float(central(n)**2-central(n+1)**2) for n in range(3)]
    weights[0]+=float(central(3)**2)
    dimension=sum(2**l for l in ell)
    state=np.zeros((dimension,dimension));energies=[];start=0
    for l,a in zip(ell,weights):
        size=2**l
        state[start:start+size,start:start+size]=np.eye(size)*math.sqrt(a/size)
        energies += [l]*size;start+=size
    rho=state@state.T
    spectrum=np.linalg.eigvalsh(rho)
    entropy=-float(np.dot(spectrum,np.log(spectrum)))
    formula=sum(-a*math.log(a)+a*l*math.log(2) for l,a in zip(ell,weights))
    energy=float(np.dot(np.diag(rho),energies));moment=sum(a*l for l,a in zip(ell,weights))
    assert abs(np.trace(rho)-1)<1e-14 and abs(entropy-formula)<1e-14
    assert abs(energy-moment)<1e-14
    return {'local_dimension':dimension,'entropy_from_partial_trace':entropy,
            'entropy_from_sector_formula':formula,'energy_for_sector_H_equal_ell':energy,
            'first_moment':moment}


def main():
    guard();started=time.time()
    result={'kinetic':kinetic_controls(),'harmonic':harmonic_controls(),
            'cusp_and_escape':cusp_and_escape_controls(),'reduced_state':reduced_state_control()}
    guard()
    result.update(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),passed=True,
                  script_sha256=sha(__file__),snapshot_manifest_sha256=sha(OUT/'snapshot_manifest_v1.json'),
                  elapsed_seconds=time.time()-started,max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  empirical_inputs=False,full_sphere_classification_reviewed=False)
    with (OUT/'independent_checks_v1.json').open('x') as stream:json.dump(result,stream,indent=2);stream.write('\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
