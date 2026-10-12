#!/usr/bin/env python3
"""Read-only independent checks of a supplied frozen composition packet."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import datetime
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import time
import mpmath as mp
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.special import eval_legendre

mp.mp.dps = 60
records = []


def check(name, condition, evidence):
    records.append({'name': name, 'passed': bool(condition), 'evidence': evidence})
    print(('PASS ' if condition else 'FAIL ') + name, flush=True)


def angular(theta, k):
    """Equivalent exponential tilt formula, with regular endpoint values."""
    theta = np.asarray(theta)
    tilted = (np.pi-theta)*np.exp(2*k*np.cos(theta))
    return (tilted-theta)/(tilted+theta)


def f_mp(c, k):
    u = 2*mp.asin(c)/mp.pi
    positive = (1+u)*mp.exp(2*k*c)
    return (positive-(1-u))/(positive+(1-u))


def angular_mp(theta, k):
    positive = (mp.pi-theta)*mp.exp(2*k*mp.cos(theta))
    return (positive-theta)/(positive+theta)


def a3(k):
    return 7*mp.quad(lambda c: f_mp(c,k)*(5*c**3-3*c)/2,
                     [0,mp.mpf('.5'),mp.mpf('.9'),mp.mpf('.99'),1])


def gram_from_angles(directions, k):
    a = np.asarray(directions)
    cross = np.linalg.norm(np.cross(a[:,None,:],a[None,:,:]),axis=2)
    theta = np.arctan2(cross,a@a.T)
    return angular(theta,k)


def chsh_and_legendre(rows):
    rng = np.random.default_rng(190712)
    segments = rng.dirichlet(np.ones(4),size=24000)*np.pi
    segments = np.vstack((segments, [[np.pi/4]*4, [np.pi,0,0,0],
                        [np.pi/2+.1]*1+[(np.pi/2-.1)/3]*3]))
    sampled_excess, derivative_errors, max_second = [], [], []
    for k in (0.,.001,.3142403964367766,.4696142810683679,1.,5.):
        bound = 4*float(angular(np.pi/4,k))
        sampled_excess.append(float(np.max(np.sum(angular(segments,k),axis=1)-bound)))
        for theta in map(mp.mpf,('.0001','.02','.2','.7','1.2','1.5707')):
            kk = mp.mpf(str(k)); a = 2/mp.pi;u=1-a*theta;g=angular_mp(theta,kk)
            actual = mp.diff(lambda x: angular_mp(x,kk),theta,2)
            formula = (1-g*g)*(2*a*a*(u-g)/(1-u*u)**2
                -4*g*a*kk*mp.sin(theta)/(1-u*u)-2*g*kk*kk*mp.sin(theta)**2-kk*mp.cos(theta))
            derivative_errors.append(float(abs(actual-formula)))
            max_second.append(float(actual))
    check('global_chsh_relaxation_and_concavity', max(sampled_excess)<2e-12
          and max(derivative_errors)<1e-45 and max(max_second)<1e-45,
          {'relaxed_angle_quadruples_per_k':len(segments),
           'quadruples_with_segment_above_pi_over_2':int(np.sum(np.max(segments,axis=1)>np.pi/2)),
           'maximum_sample_excess':max(sampled_excess),
           'maximum_second_derivative_identity_error':max(derivative_errors),
           'role':'finite checks of the separately reviewed global analytic proof'})

    coeff_error, a3_error, interval_ok, chsh_error, root_bracket = [],[],[],[],[]
    values=[]
    for row in rows:
        k=row['k'];kk=mp.mpf(str(k));val=a3(kk)
        a3_error.append(float(abs(val-mp.mpf(row['a3_80dps']))))
        interval=row['a3_midpoint_enclosure'];interval_ok.append(interval['lower']<=val<=interval['upper'])
        def scalar(c):
            u=2*math.asin(c)/math.pi;e=(1+u)*math.exp(2*k*c)
            return (e-(1-u))/(e+(1-u))
        for ell,expected in zip(row['legendre_odd_ell'],row['legendre_by_order']['1024']):
            actual=quad(lambda c:(2*ell+1)*scalar(c)*eval_legendre(ell,c),0,1,
                        epsabs=3e-12,epsrel=3e-12,limit=200)[0]
            coeff_error.append(abs(actual-expected))
        global_value=4*angular_mp(mp.pi/4,kk)
        chsh_error.append(float(abs(global_value-mp.mpf(row['global_chsh_analytic_80dps']))))
        values.append({'k':k,'a3_direct_c_60dps':str(val),'global_chsh_60dps':str(global_value)})
    for k in (mp.mpf('.3183313595'),mp.mpf('.3183313596')):
        root_bracket.append({'k':str(k),'a3':str(a3(k))})
    check('legendre_and_chsh_recorded_values',max(a3_error)<1e-50 and max(coeff_error)<2e-10
          and all(interval_ok) and max(chsh_error)<1e-50,
          {'direct_c_a3_max_error':max(a3_error),'adaptive_c_all_odd_coefficients_max_error':max(coeff_error),
           'all_midpoint_intervals_contain_independent_values':all(interval_ok),
           'chsh_max_error':max(chsh_error),'values':values,
           'independent_numerical_root_bracket_not_formal_interval':root_bracket})
    baseline=a3(mp.mpf(0))
    derivative_samples=[7*mp.quad(lambda c:c*(5*c**3-3*c)/2*(1-f_mp(c,k)**2),[0,1])
                        for k in map(mp.mpf,('0','.314','.47','1','5'))]
    check('a3_baseline_and_monotonicity_controls', abs(baseline-mp.mpf(7)/64)<mp.mpf('1e-50')
          and all(v<0 for v in derivative_samples),
          {'baseline':str(baseline),'sampled_derivatives':list(map(str,derivative_samples)),
           'analytic_proof':'cP3 changes sign once and integrates to zero; strictly decreasing positive weight gives negative derivative'})


def recorded_witnesses(rows,directions):
    residuals=[];value_errors=[];norm_errors=[];counts=0
    for coords in directions.values():
        norm_errors.extend(abs(np.linalg.norm(coords,axis=1)-1))
    for row in rows:
        for scan in row['finite_gram_scans']:
            G=gram_from_angles(directions[scan['geometry']],row['k'])
            w=np.array(scan['witness_weights']);lam=scan['minimum_eigenvalue']
            residuals.append(np.max(abs(G@w-lam*w)))
            value_errors.append(abs(float(w@G@w)-lam))
            value_errors.append(abs(float(np.linalg.eigvalsh(G)[0])-lam))
            norm_errors.append(abs(w@w-1));counts+=1
    check('all_frozen_directional_witnesses',max(residuals)<2e-11 and max(value_errors)<2e-11
          and max(norm_errors)<2e-13,
          {'matrix_witnesses_checked':counts,'geometries':len(directions),
           'maximum_eigenvector_residual':float(max(residuals)),
           'maximum_quadratic_form_error':float(max(value_errors)),
           'maximum_vector_norm_error':float(max(norm_errors)),
           'kernel_route':'geodesic atan2(cross,dot), then exponential tilt; no author helpers'})


I2=np.eye(2);I4=np.eye(4)
px=np.array([[0,1],[1,0]],complex);py=np.array([[0,-1j],[1j,0]]);pz=np.diag([1.,-1.])
# A Clifford basis distinct from the one used by the author.
CLIFFORD=np.array([np.kron(px,px),np.kron(px,py),np.kron(px,pz),np.kron(py,I2),np.kron(pz,I2)])
PHI=np.eye(4).reshape(16)/2


def operators_and_probabilities(X,Y):
    A=np.array([sum(x*g for x,g in zip(v,CLIFFORD)) for v in X])
    B=np.array([-sum(y*g for y,g in zip(v,CLIFFORD)).T for v in Y])
    E=np.array([[np.vdot(PHI,np.kron(a,b)@PHI).real for b in B] for a in A])
    probabilities=np.empty((3,3,2,2))
    for i,j,aa,bb in itertools.product(range(3),range(3),range(2),range(2)):
        pa=(I4+(1-2*aa)*A[i])/2;pb=(I4+(1-2*bb)*B[j])/2
        probabilities[i,j,aa,bb]=np.vdot(PHI,np.kron(pa,pb)@PHI).real
    residual=max(np.max(abs(A@A-I4)),np.max(abs(B@B-I4)),
                 np.max(abs(A-A.conj().transpose(0,2,1))),np.max(abs(B-B.conj().transpose(0,2,1))))
    marginal=max(abs(np.vdot(PHI,np.kron(a,I4)@PHI)) for a in A)
    marginal=max(marginal,max(abs(np.vdot(PHI,np.kron(I4,b)@PHI)) for b in B))
    return A,B,E,probabilities,float(residual),float(marginal)


def quantum_and_counts(rows):
    sign=np.eye(3)-2*np.ones((3,3))/3
    errors=[];statuses=[];forecast_errors=[];feasible_count=0
    for row in rows:
        h=float(f_mp(mp.mpf('.5'),mp.mpf(str(row['k']))));G=np.full((3,3),-h);np.fill_diagonal(G,1)
        errors.extend([abs(h-float(row['h_80dps'])),np.max(abs(np.array(row['triangle_G'])-G)),
                       np.max(abs(np.array(row['triangle_E'])+G)),
                       abs(float(row['triangle_lambda_min_80dps'])-(1-2*h))])
        t=np.linalg.svd(G,compute_uv=False).sum()/3
        errors.extend([abs(t-row['gamma2_G']),abs(1/t-row['visibility_critical'])])
        for item in row['visibility_cases']:
            V=item['V'];E=np.array(item['E']);prob=np.array(item['joint_probabilities_AB_order_plus_minus'])
            errors.extend([np.max(abs(E+V*G)),np.max(abs(prob.sum(axis=(2,3))-1))])
            expected=(1+E[:,:,None,None]*np.array([[1,-1],[-1,1]]))/4
            errors.append(np.max(abs(prob-expected)))
            feasible=item['quantum_construction']['feasible'];statuses.append(feasible==(V*t<=1+1e-13))
            errors.extend([abs(-np.sum(sign*E)-item['bell_value']),abs(np.linalg.svd(E,compute_uv=False).sum()-item['nuclear_norm'])])
            if feasible:
                X=np.array(item['quantum_construction']['X']);Y=np.array(item['quantum_construction']['Y'])
                _,_,actual,p,res,marg=operators_and_probabilities(X,Y)
                errors.extend([np.max(abs(actual-E)),np.max(abs(actual-np.array(item['quantum_construction']['quantum_E']))),
                               np.max(abs(p-prob)),res,marg]);feasible_count+=1
            # Generic cell-wise variance calculation, not the simplified author expressions.
            variances=1-E*E;w=abs(sign);rootterms=w*np.sqrt(np.maximum(0,variances));z=rootterms.sum()
            optimal=z*z;uniform=9*np.sum(w*w*variances)
            forecast_errors.extend([abs(optimal-item['optimal_N_times_counting_variance']),abs(uniform-item['uniform_N_times_counting_variance'])])
            if item['margin']>1e-12:
                N=25*optimal/item['margin']**2
                forecast_errors.append(abs(N/item['illustrative_total_N_for_margin_5_counting_SE_optimal']-1))
    local=max(abs(np.array(a)@sign@np.array(b)) for a in itertools.product((-1,1),repeat=3) for b in itertools.product((-1,1),repeat=3))
    check('all_frozen_quantum_tables_and_counting_forecasts',max(errors)<3e-13 and all(statuses)
          and max(forecast_errors)<5e-12 and abs(local-3)<1e-14,
          {'feasible_recorded_tables':feasible_count,'all_recorded_tables':sum(len(x['visibility_cases']) for x in rows),
           'max_probability_operator_or_scalar_error':float(max(errors)),
           'max_forecast_error_absolute_or_relative_as_applicable':float(max(forecast_errors)),
           'local_64_strategy_bound':float(local),'systematic_l1_coefficient':float(np.sum(abs(sign)))})

    trials=[];example=None
    for h in (1/3,.5,.5236682492955412,.8,1.):
        G=np.full((3,3),-h);np.fill_diagonal(G,1)
        eig,U=np.linalg.eigh(G);t=max(1.,(1+4*h)/3);Vcrit=1/t
        for V in (0.,Vcrit/2,Vcrit):
            # Independent spectral-coordinate factorization, not the symmetric square root used by the author.
            base=U*np.sqrt(abs(eig));other=base*np.sign(eig)
            slack=math.sqrt(max(0,1-V*t))
            X=np.column_stack((np.sqrt(V)*base,np.full(3,slack),np.zeros(3)))
            Y=np.column_stack((np.sqrt(V)*other,np.zeros(3),np.full(3,slack)))
            A,B,E,p,res,marg=operators_and_probabilities(X,Y)
            cross=float(np.max(abs(E+V*G)))
            lower=float(np.linalg.svd(G,compute_uv=False).sum()/3)
            trials.append({'h':h,'V':V,'Vcrit':Vcrit,'nuclear_lower_bound':lower,'gamma2_t':t,'operator_residual':res,'correlator_error':cross,'marginal_error':marg,'min_probability':float(p.min())})
            if h==.5236682492955412 and V==Vcrit:
                example={'h':h,'V':V,'X':X.tolist(),'Y':Y.tolist(),'A_real':A.real.tolist(),'A_imag':A.imag.tolist(),'B_real':B.real.tolist(),'B_imag':B.imag.tolist(),'correlators':E.tolist(),'joint_probabilities':p.tolist()}
    check('independent_observables_at_visibility_boundary',all(max(t['operator_residual'],t['correlator_error'],t['marginal_error'],abs(t['nuclear_lower_bound']-t['gamma2_t']))<4e-14 and t['min_probability']>-2e-15 for t in trials),
          {'trial_count':len(trials),'trials':trials,'construction':'spectral factorization and alternate five-generator Clifford basis; direct 16-dimensional state/projector calculation'})
    return example


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--packet',type=Path,required=True);parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    started=time.monotonic()
    data=json.loads((args.packet/'COMPUTATION_RESULTS.json').read_text());directions=json.loads((args.packet/'finite_directions.json').read_text())
    chsh_and_legendre(data['rows']);recorded_witnesses(data['rows'],directions);example=quantum_and_counts(data['rows'])
    result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-started,
            'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'mpmath':mp.__version__},
            'read_inputs_sha256':{name:hashlib.sha256((args.packet/name).read_bytes()).hexdigest() for name in ('COMPUTATION_RESULTS.json','finite_directions.json')},
            'checks':records,'pass':sum(x['passed'] for x in records),'fail':sum(not x['passed'] for x in records),'independent_boundary_operator_example':example}
    args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(f"TOTAL: PASS={result['pass']} FAIL={result['fail']}")
    return bool(result['fail'])


if __name__=='__main__':
    raise SystemExit(main())
