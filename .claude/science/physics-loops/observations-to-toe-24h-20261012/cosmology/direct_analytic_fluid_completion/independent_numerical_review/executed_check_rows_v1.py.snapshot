#!/usr/bin/env python3
"""Independent complete row consumption and high-precision force/mode checks.

No parent Python source is imported. Force comes from differentiated canonical
Hamiltonian energy; modes use a convergent power series, not expm/closed forms.
"""
from pathlib import Path
import collections
import datetime
import hashlib
import json
import math
import mpmath as mp
import numpy as np

ROOT = Path(__file__).resolve().parent
SNAP = ROOT / 'source_snapshot'
AUTHOR = json.loads((SNAP / 'evidence_v1/RESULTS.json').read_text())
FIX = json.loads((SNAP / 'NUMERICAL_FIXTURES_v1.json').read_text())
CHECKS = []


def check(name, passed, **evidence):
    CHECKS.append({'name': name, 'passed': bool(passed), **evidence})


def compare(name, actual, expected, atol=2e-10, rtol=2e-10):
    aa, bb = np.asarray(actual, float), np.asarray(expected, float)
    units = np.abs(aa-bb) / (atol + rtol*np.maximum(np.abs(aa), np.abs(bb)))
    m = float(np.max(units))
    check(name, aa.shape == bb.shape and np.all(np.isfinite(aa)) and np.all(np.isfinite(bb)) and m <= 1,
          max_units=m, max_absolute_error=float(np.max(np.abs(aa-bb))))


def high_precision_force(row):
    mp.mp.dps = 70
    a, nu = mp.mpf(row['a']), mp.mpf(row['nu'])
    s = mp.sqrt(a)
    q = list(map(mp.mpf, row['case']['phi'])); q[0] *= s
    vel = list(map(mp.mpf, row['case']['velocity'])); vel[0] *= s
    sm, sr = map(mp.mpf, row['case']['densities'])

    def metric(q):
        u, x, y = q
        den = 1 + mp.mpf(2)/3*(1+a)*(x*x+y*y)
        return [mp.mpf(1), 4*a/(9*den), a/(3*den)]

    def potential(q):
        u, x, y = q
        return mp.mpf(3)/2 + (2*(u-s/4)**2+3*a/8)*x*x+a*y*y/3+nu*u*u/2

    k = metric(q)
    pi = [k[i]*vel[i] for i in range(3)]

    def energy(q):
        kk = metric(q)
        return sum(pi[i]**2/(2*kk[i]) for i in range(3))+potential(q)+sm+sr

    def derivative(fun, j):
        def one(z):
            changed = list(q); changed[j] = z
            return fun(changed)
        return mp.diff(one, q[j])

    energy_gradient = [derivative(energy, j) for j in range(3)]
    metric_derivative = [[derivative(lambda z, i=i: metric(z)[i], j) for j in range(3)] for i in range(3)]
    hh = mp.sqrt(2*energy(q)/3)
    kinetic = sum(pi[i]*vel[i] for i in range(3))
    hdot = -kinetic-sm-4*sr/3
    pidot = [-3*hh*pi[i]-energy_gradient[i]-(s*sm if i == 0 else 0) for i in range(3)]
    acceleration = [(pidot[i]-vel[i]*sum(metric_derivative[i][j]*vel[j] for j in range(3)))/k[i] for i in range(3)]
    nacc = [(acceleration[i]-vel[i]*hdot/hh)/hh**2 for i in range(3)]
    density_dot = [(-3*hh+s*vel[0])*sm, -4*hh*sr]
    edot = sum(energy_gradient[i]*vel[i]+vel[i]*pidot[i] for i in range(3))+sum(density_dot)
    target = -3*hh*(kinetic+sm+4*sr/3)
    out = {'q': list(map(float,q)), 'K': list(map(float,k)), 'V': float(potential(q)),
           'H': float(hh), 'H_J': float((hh+s*vel[0])/mp.exp(s*q[0])),
           'N_state': list(map(float,q))+list(map(float,[z/hh for z in vel]))+[float(sm),float(sr)],
           'N_acceleration': list(map(float,nacc)), 'N_density_dot': list(map(float,[z/hh for z in density_dot])),
           'energy_residual_70_digits': mp.nstr(edot-target,30),
           'V_gradient': list(map(float,[derivative(potential,j) for j in range(3)])),
           'dK_coordinate_first': np.array([[float(metric_derivative[i][j]) for i in range(3)] for j in range(3)]).tolist()}
    return out


def mode_series(mass, t):
    mp.mp.dps = 80
    m, tt = mp.mpf(mass), mp.mpf(t)
    coefficients = [mp.mpf('.2'), mp.mpf('-.1')]
    for n in range(400):
        coefficients.append(-(3*(n+1)*coefficients[n+1]+m*coefficients[n])/((n+2)*(n+1)))
    value = mp.fsum(coefficients[n]*tt**n for n in range(len(coefficients)))
    return float(value), mp.nstr(abs(coefficients[-1]*tt**(len(coefficients)-1)),20)


def physical_from_record(record, a, nu, hv, weights):
    q = np.asarray(record[:3],float)/weights
    pp = np.asarray(record[3:6],float)/weights
    sm, sr = record[6:8]
    u,x,y = q
    D = 1+2*(1+a)*(x*x+y*y)/3
    k = np.array([1,4*a/(9*D),a/(3*D)])
    V = hv*hv*(1.5+(2*(u-math.sqrt(a)/4)**2+3*a/8)*x*x+a*y*y/3+nu*u*u/2)
    hh2 = 2*(sm+sr+V)/(3-np.dot(k,pp*pp))
    return q, math.sqrt(hh2), 1.5*hh2


def main():
    freeze=json.loads((SNAP/'evidence_v1/FREEZE.json').read_text())
    execution=json.loads((SNAP/'evidence_v1/EXECUTION.json').read_text())
    for name, expected in freeze['source_sha256'].items():
        h=hashlib.sha256((SNAP/name).read_bytes()).hexdigest()
        hs=hashlib.sha256((SNAP/'evidence_v1/source_snapshot'/name).read_bytes()).hexdigest()
        check('lineage '+name,h==expected==hs==AUTHOR['source_sha256'][name] and execution['source_unchanged'][name])
    check('freeze precedes execution',freeze['created_at'] < execution['started_at'] <= AUTHOR['started_at'] <= AUTHOR['ended_at'] <= execution['ended_at'])
    check('record count',len(AUTHOR['checks'])==1492 and AUTHOR['passed']==1492 and AUTHOR['failed']==0 and all(c['passed'] for c in AUTHOR['checks']))
    counts={k:len(AUTHOR[k]) for k in ['off_trajectory','modes','tracking','disturbed']}
    check('complete fixture cardinalities',counts=={'off_trajectory':72,'modes':25,'tracking':12,'disturbed':48},counts=counts)

    byname={c['name']:c for c in AUTHOR['checks']}
    check('unique check names',len(byname)==len(AUTHOR['checks']))
    for index,c in enumerate(AUTHOR['checks']):
        name=c['name']
        if 'max_tolerance_units' in c:
            if name.startswith('tracking '): atol,rtol=FIX['tracking']['comparison_atol'],FIX['tracking']['comparison_rtol']
            elif name.startswith('disturbed '): atol,rtol=FIX['disturbed']['comparison_atol'],FIX['disturbed']['comparison_rtol']
            elif name.startswith('vacuum '): atol,rtol=1e-13,1e-12
            else: atol,rtol=2e-10,2e-10
            aa,bb=np.asarray(c['actual'],float),np.asarray(c['expected'],float)
            units=float(np.max(np.abs(aa-bb)/(atol+rtol*np.maximum(np.abs(aa),np.abs(bb)))))
            check(f'check arithmetic {index}',math.isfinite(units) and units<=1 and abs(units-c['max_tolerance_units'])<=2e-14*max(1,units))
        elif 'reduced_expression' in c:
            check(f'symbolic record {index}',c['reduced_expression']=='0')
        elif 'diagonal' in c:
            check(f'positive K record {index}',min(c['diagonal'])>0)
        elif 'value' in c:
            check(f'coercivity record {index}',c['value']>=c['lower']-1e-13*max(1,c['value']))
        else:
            check(f'noncomparison record retained {index}',c['passed'] is True and len(c)>=3)

    force=[]
    for i,row in enumerate(AUTHOR['off_trajectory']):
        expected_a=FIX['a'][i//24]; expected_nu=FIX['nu'][(i//6)%4]; expected_case=FIX['off_trajectory_cases'][i%6]
        check(f'force fixture order {i}',row['a']==expected_a and row['nu']==expected_nu and row['case']==expected_case)
        independent=high_precision_force(row); force.append(independent)
        for k in ['N_state','H','H_J']:
            compare(f'independent force {i} {k}',independent[k],row[k])
        compare(f'independent implemented KG {i}',independent['N_acceleration'],row['implemented_accelerations'])
        compare(f'independent parent momentum KG {i}',independent['N_acceleration'],row['momentum_oracle_accelerations'])
        for label,k in [('full conservation','N_density_dot'),('independent K','K'),('independent V','V'),('independent gradient','V_gradient'),('metric derivative','dK_coordinate_first')]:
            compare(f'independent force control {i} {label}',independent[k],byname[f'off trajectory {label} {i}']['actual'])
        check(f'independent Hamiltonian energy {i}',abs(mp.mpf(independent['energy_residual_70_digits']))<mp.mpf('1e-52'))

    modes=[]
    for i,row in enumerate(AUTHOR['modes']):
        expected,tail=mode_series(row['mass_squared_over_Hv_squared'],row['Hv_t'])
        for field in ['mode','matrix_exponential']:
            compare(f'series vacuum {i} {field}',expected,row[field],atol=1e-13,rtol=1e-12)
        modes.append({'mass':row['mass_squared_over_Hv_squared'],'time':row['Hv_t'],'independent_value':expected,'last_series_term':tail})

    tracking=[]
    omega=FIX['calibration']['Omega_gamma']; m=FIX['calibration']['m']; hv=math.sqrt(1-m-omega)
    tc=FIX['tracking']
    for i,row in enumerate(AUTHOR['tracking']):
        a,nu=row['a'],row['nu']
        x0=math.sqrt(3*m/(2*(1+a)*hv*hv));y0=math.sqrt(3*omega/(2*(1+a)*hv*hv))
        compare(f'tracking normalization {i}',[row[k]for k in ['Hv','x0','y0','S0','R0']],[hv,x0,y0,hv*hv*x0*x0,hv*hv*y0*y0])
        outputs=[]
        for j,run in enumerate(row['runs']):
            check(f'tracking refinement identity {i} {j}',run['refinement']==tc['refinements'][j])
            actual=np.array(run['states']); target=np.array([[0,1,1,0,-1.5,-2,-3*n,-4*n]for n in row['N_sites']])
            compare(f'all tracking states {i} {j}',actual,target,tc['comparison_atol'],tc['comparison_rtol'])
            recomputed=[]
            for k,(n,z) in enumerate(zip(row['N_sites'],actual)):
                ex,ey=x0*math.exp(-1.5*n),y0*math.exp(-2*n)
                record=np.r_[z[:3]*[1,ex,ey],z[3:6]*[1,ex,ey],hv*hv*x0*x0*math.exp(z[6]),hv*hv*y0*y0*math.exp(z[7])]
                _,hh,_=physical_from_record(record,a,nu,hv,np.ones(3)); intended=m*math.exp(-3*n)+omega*math.exp(-4*n)+hv*hv
                compare(f'tracking stored H2 {i} {j} {k}',hh*hh,run['H2'][k])
                compare(f'tracking target H2 {i} {j} {k}',hh*hh/intended,1,tc['comparison_atol'],tc['comparison_rtol'])
                recomputed.append(hh*hh)
            outputs.append(recomputed)
        compare(f'all tracking refinements {i}',row['runs'][0]['states'],row['runs'][1]['states'],tc['comparison_atol'],tc['comparison_rtol'])
        tracking.append({'a':a,'nu':nu,'recomputed_H2':outputs})

    disturbed=[];dc=FIX['disturbed']
    for i,row in enumerate(AUTHOR['disturbed']):
        a,nu=row['a'],row['nu']; weights=np.array([1,2*math.sqrt(a)/3,math.sqrt(a/3)])
        initial_u=row['case']['phi'][0]*math.sqrt(a);sm0,sr0=row['case']['densities']
        compare(f'disturbed stored cross comparison {i}',row['N_states'],row['proper_reference_states'],dc['comparison_atol'],dc['comparison_rtol'])
        summaries=[]
        for origin in ['N_states','proper_reference_states']:
            energies=[]
            for j,(n,z) in enumerate(zip(row['N'],row[origin])):
                q,hh,ee=physical_from_record(z,a,nu,1,weights);energies.append(ee)
                exactrho=[sm0*math.exp(-3*n+math.sqrt(a)*(q[0]-initial_u)),sr0*math.exp(-4*n)]
                compare(f'number radiation invariants {i} {origin} {j}',z[6:8],exactrho,atol=2e-12,rtol=2e-7)
                if origin=='proper_reference_states':
                    compare(f'proper energy stored {i} {j}',ee,row['energies'][j])
                    compare(f'proper fields stored {i} {j}',q,row['fields'][j])
            check(f'energy floor independent {i} {origin}',min(energies)>=1.5-dc['energy_tolerance'])
            check(f'energy monotonic independent {i} {origin}',max(np.diff(energies))<=dc['energy_tolerance']*max(1,energies[0]))
            summaries.append({'formulation':origin,'initial_energy':energies[0],'final_energy':energies[-1],'max_increment':float(max(np.diff(energies)))})
        check(f'disturbed times physical {i}',row['proper_times'][0]==0 and np.all(np.diff(row['proper_times'])>0) and np.all(np.array(row['proper_times'])<=np.array(row['N'])+1e-12))
        disturbed.append({'a':a,'nu':nu,'energy_checks':summaries})

    cal=json.loads((SNAP/'CALIBRATION_SCOPE_v1.json').read_text())
    upstream=json.loads((SNAP/'upstream_radiation_RESULTS.json').read_text())
    central=[r for r in upstream['thermal']['thermal_rows'] if r['sigma_shift']==0][0]
    check('imported calibration equality',central['Omega_gamma']==cal['Omega_gamma']==omega and central['temperature_K']==cal['temperature_K'])
    check('imported source exact hash',hashlib.sha256((SNAP/'upstream_radiation_RESULTS.json').read_bytes()).hexdigest()==cal['calibration_source_sha256'])
    check('scope declared photons only and no new test',cal['radiation']=='photons only' and cal['empirical_test']=='No independent observations newly tested.' and 'G_N=(1+a)G_*' in cal['calibration_bridge'])

    out={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'method':'Independent Hamiltonian differentiation and oscillator series; every supplied result class consumed without author imports.',
         'counts':counts,'off_trajectory':force,'modes':modes,'tracking':tracking,'disturbed':disturbed,'checks':CHECKS,
         'summary':{'total':len(CHECKS),'passed':sum(c['passed']for c in CHECKS),'failed':sum(not c['passed']for c in CHECKS)}}
    (ROOT/'ROW_CHECKS_v1.json').write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(out['summary'],sort_keys=True))
    for c in CHECKS:
        if not c['passed']: print(json.dumps(c,sort_keys=True))
    return int(out['summary']['failed']>0)


if __name__=='__main__':
    raise SystemExit(main())
