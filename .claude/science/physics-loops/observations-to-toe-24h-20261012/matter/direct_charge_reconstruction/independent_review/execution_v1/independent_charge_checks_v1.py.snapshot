#!/usr/bin/env python3
"""Independent, read-only validation of the pinned charge block.

No import or execution of the author's runner. Exact small representation
factor traces replace the author's 16x16 matrices; binary elimination replaces
its symbolic graph ranks; rational summary propagation precedes floating checks.
"""
from datetime import datetime, timezone
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement, product
from pathlib import Path
import hashlib
import json
import math
import sys
import sympy as S

HERE = Path(__file__).resolve().parent
SNAP = HERE / 'snapshots_v1'
R = json.loads((SNAP / 'evidence_v1/RESULTS.json').read_text())
OBS = json.loads((SNAP / 'OBSERVATION_INPUTS.json').read_text())
checks = []
detail = {}


def test(name, passed, **evidence):
    checks.append(dict(name=name, passed=bool(passed), **evidence))


def exact(name, lhs, rhs):
    difference = S.expand(lhs-rhs)
    test(name, difference == 0, difference=str(difference))


def near(name, observed, expected):
    error = abs(observed-float(expected))
    test(name, error <= 3e-14*max(1, abs(float(expected))),
         observed=observed, expected=float(expected), absolute_error=error)


def polynomial_checks():
    nc, q, u, d, l, e, n, h, ep, de = S.symbols('Nc q u d l e n h epsilon delta', real=True)
    mass = [q+h+u, q-h+d, l-h+e, l+h+n]
    mass_solution = S.linsolve(mass, [u,d,e,n])
    solution = dict(zip([u,d,e,n], next(iter(mass_solution))))
    # Summation over individual chiral species, keeping dimensions explicit.
    dimensions = [2*nc,nc,nc,2,1,1]
    hypercharges = [q,u,d,l,e,n]
    trace1 = sum(dim*y for dim,y in zip(dimensions,hypercharges)).subs(solution)
    trace3 = sum(dim*y**3 for dim,y in zip(dimensions,hypercharges)).subs(solution)
    weak = nc*q+l
    exact('Dirac mixed-gravity polynomial', trace1, 0)
    exact('Dirac cubic polynomial', trace3, -6*h*h*weak)
    exact('minimal mixed-gravity polynomial', trace1-solution[n], l+h)
    exact('minimal cubic polynomial', trace3-solution[n]**3, (l+h)**3-6*h*h*weak)
    exact('color bilinear anomaly', (2*q+u+d).subs(solution), 0)
    solved = S.solve([weak, trace1-solution[n]], [q,l], dict=True)
    test('minimal solution unique with nonzero Nc', solved == [{l:-h,q:h/nc}], solution=str(solved))
    family = {q:h*(1+2*ep)/nc, l:-h*(1+2*ep)}
    exact('Majorana common-charge coefficient', (2*n).subs(solution).subs(family), 4*h*ep)
    exact('Weinberg common-charge coefficient', (2*l+2*h).subs(family), -4*h*ep)
    t = S.symbols('t',real=True)
    a1 = trace1-solution[n]
    a3 = trace3-solution[n]**3
    for label,poly in [('gravity',a1),('cubic',a3),('weak',weak)]:
        total = sum(poly.subs({nc:3,q:h/3,l:li}) for li in [-h+t,-h-t,-h])
        exact('disconnected three-family '+label,total,0)
    # Q0 eigenvalues, then conjugate the all-LH singlets to physical particles.
    ys = {key:S.expand(value.subs(family).subs(nc,3)) for key,value in solution.items()}
    physical = {'up':-ys[u]/(2*h), 'down':-ys[d]/(2*h),
                'electron':-ys[e]/(2*h), 'neutrino':-ys[n]/(2*h), 'W':S.Integer(1)}
    physical['proton'] = 2*physical['up']+physical['down']
    physical['neutron'] = physical['up']+2*physical['down']
    normalized = {key:S.cancel((value/(1+ep)).subs(ep,de/(1-de))) for key,value in physical.items()}
    expected = {'up':(2-de)/3,'down':(-1+2*de)/3,'electron':-1,'neutrino':-de,'W':1-de,'proton':1,'neutron':de}
    for key in expected:
        exact('electron-unit '+key, normalized[key], expected[key])
        reported = S.sympify(R['derivation']['measured_electric_charges'][key],locals={'delta':de})
        exact('reported electron-unit '+key,reported,expected[key])
    exact('beta electric-charge conservation',normalized['proton']+normalized['electron']-normalized['neutrino'],normalized['neutron'])
    # Opposite-charge mass is a genuine boundary of the Majorana argument.
    charge = S.diag(1,-1)
    offdiag = S.Matrix([[0,1],[1,0]])
    test('opposite-charge offdiagonal mass allowed', charge.T*offdiag+offdiag*charge == S.zeros(2))
    test('equal nonzero-charge Majorana mass forbidden', S.eye(2).T*offdiag+offdiag*S.eye(2) != S.zeros(2))
    # This is a counterexample to the original blanket scalar-vev wording.
    test('nonzero hypercharge Higgs neutral vev counterexample', -S.Rational(1,2)+h/(2*h)==0)
    detail['polynomials'] = {'mass_solution':str(solution),'Dirac_cubic':str(S.factor(trace3)),
        'minimal_cubic':str(S.factor(a3)), 'physical_electron_unit':{k:str(v) for k,v in normalized.items()},
        'scalar_vev_wording_counterexample':'H has Y=h nonzero and T3=-1/2, hence Q0=0.'}


def elementary(n,i,j):
    out=S.zeros(n);out[i,j]=1;return out


def representation_checks():
    E=lambda i,j:elementary(3,i,j)
    # Generated from matrix units, not copied 16-dimensional generator blocks.
    color=[]
    for i,j in [(0,1),(0,2),(1,2)]:
        color.extend([(E(i,j)+E(j,i))/2,S.I*(E(j,i)-E(i,j))/2])
    color.insert(2,(E(0,0)-E(1,1))/2)
    color.append((E(0,0)+E(1,1)-2*E(2,2))/(2*S.sqrt(3)))
    weak=[(elementary(2,0,1)+elementary(2,1,0))/2,
          S.I*(elementary(2,1,0)-elementary(2,0,1))/2,S.diag(1,-1)/2]
    q,h=S.symbols('q h',real=True)
    species=[('fund','doublet',q),('anti','one',-q-h),('anti','one',h-q),
             ('one','doublet',-3*q),('one','one',3*q+h),('one','one',3*q-h)]
    @lru_cache(None)
    def factor_trace(kind,sequence):
        if kind=='one': return S.Integer(0 if sequence else 1)
        generators = weak if kind=='doublet' else color
        size = 2 if kind=='doublet' else 3
        out=S.eye(size)
        for j in sequence:
            generator = generators[j]
            if kind=='anti': generator=-generator.T
            out=out*generator
        return S.expand(S.trace(out))
    def ordered(sequence,fields=species):
        cs=tuple(i for i in sequence if i<8)
        ws=tuple(i-8 for i in sequence if 8<=i<11)
        ny=sum(i==11 for i in sequence)
        return S.expand(sum(factor_trace(c,cs)*factor_trace(w,ws)*y**ny for c,w,y in fields))
    expected_indices=list(combinations_with_replacement(range(12),3))
    rows=R['representation']['symmetric_cubic_rows']
    test('364 complete unique ordered-index triples',[tuple(row['indices']) for row in rows]==expected_indices)
    trace_rows=[]
    for row in rows:
        i,j,k=row['indices']
        result=S.expand(ordered((i,j,k))+ordered((i,k,j)))
        test('factorized cubic '+str((i,j,k)),result==0 and row['trace']=='0')
        trace_rows.append({'indices':[i,j,k],'independent_trace':str(result)})
    for i,reported in enumerate(R['representation']['gravity_traces']):
        exact('factorized gravity '+str(i),ordered((i,)),S.sympify(reported))
    # Check normalizations and the anti-representation's Lie bracket, too.
    for i,j in product(range(8),repeat=2):
        exact('fundamental quadratic normalization '+str((i,j)),S.trace(color[i]*color[j]),S.Rational(1,2) if i==j else 0)
        comm_anti=(-color[i].T)*(-color[j].T)-(-color[j].T)*(-color[i].T)
        test('anti Lie bracket '+str((i,j)),comm_anti==-(color[i]*color[j]-color[j]*color[i]).T)
    missing=species[:-1]
    exact('omitted n gravitational anomaly',ordered((11,),missing),h-3*q)
    exact('omitted n cubic anomaly',ordered((11,11,11),missing),-(3*q-h)**3)
    bad=species.copy();bad[1]=('fund','one',-q-h)
    bad_value=S.simplify(2*ordered((7,7,7),bad))
    exact('wrong-conjugate reported nonzero trace',bad_value,-S.sqrt(3)/3)
    test('wrong conjugate mutation killed',bad_value!=0)
    test('missing neutrino mutation killed at q=1/4 h=1/2',ordered((11,11,11),missing).subs({q:S.Rational(1,4),h:S.Rational(1,2)})!=0)
    detail['cubic_rows']=trace_rows
    detail['representations']={'route':'Trace over each color and weak factor separately, never a 16x16 block.',
        'wrong_conjugate_trace':str(bad_value),'omitted_n_gravity':str(ordered((11,),missing)),
        'omitted_n_cubic':str(ordered((11,11,11),missing))}


def rational_checks():
    rows=R['rational_rows']
    expected={(nc,h,ep) for nc,h,ep in product([3,5,7],[F(1,2),F(1),F(3,2)],[F(-1,10),F(0),F(1,100),F(2,3),F(2)])}
    seen=set()
    for row in rows:
        nc,h,ep=row['Nc'],F(row['h']),F(row['epsilon']);seen.add((nc,h,ep))
        c={key:F(v) for key,v in row['charges'].items()}
        q,u,d,l,e,n=[c[k] for k in ['Q','u','d','L','e','n']]
        mass=[q+h+u,q-h+d,l-h+e,l+h+n]
        anomaly=[2*q+u+d,nc*q+l,2*nc*q+nc*u+nc*d+2*l+e+n,
                 2*nc*q**3+nc*u**3+nc*d**3+2*l**3+e**3+n**3]
        # Define epsilon through the lepton charge; use constraints for q.
        valid=all(x==0 for x in mass+anomaly) and c['H']==h and -(l+h)/(2*h)==ep
        valid=valid and [F(x) for x in row['anomalies']]==anomaly and (nc+1)%2==0
        test('rational row '+str((nc,h,ep)),valid)
    test('45 complete rational inputs',len(rows)==45 and seen==expected)
    test('Witten parity cannot select 3 generations',all((g*4)%2==0 for g in range(1,20)))


def binary_rank(rows):
    basis={}
    for value in rows:
        while value:
            pivot=value.bit_length()-1
            if pivot not in basis:
                basis[pivot]=value;break
            value ^= basis[pivot]
    return len(basis)


def graph_checks():
    rows=R['mixing_graphs']['rows'];connected=0;independent=[]
    test('512 unique ordered graph masks',[r['mask'] for r in rows]==list(range(512)))
    for row in rows:
        mask=row['mask'];root=list(range(6));edges=[]
        def leader(a):
            while root[a]!=a:a=root[a]
            return a
        for b in range(9):
            if (mask>>b)&1:
                a,v=divmod(b,3);v+=3
                root[leader(a)]=leader(v);edges.append((a,v))
        groups={}
        for a in range(6):groups.setdefault(leader(a),[]).append(a)
        components=sorted(groups.values(),key=lambda c:c[0])
        rank=binary_rank([(1<<a)|(1<<b) for a,b in edges])
        is_connected=len(components)==1;connected+=is_connected
        valid=(rank==6-len(components)==row['rank'] and components==row['components']
               and len(edges)==row['edge_count'] and is_connected==row['connected'])
        test('GF2 incidence and union-find '+str(mask),valid)
        independent.append(dict(mask=mask,rank=rank,components=components))
    test('connected graph count',connected==205==R['mixing_graphs']['connected_support_count'])
    test('support matrices not asserted unitary',R['mixing_graphs']['any_claim_all_supports_unitary'] is False)
    detail['graph_rows']=independent
    # If a single edge constraint is dropped, disconnected components admit
    # independent charges: empty support has a six-dimensional kernel.
    test('false universal-flavor mutation killed',binary_rank([])!=5)


def lattice_checks():
    # Center characters evaluated as rational phases in turns, then mod 1.
    t={'Q':1,'u':-1,'d':-1,'L':0,'e':0,'n':0,'H':0}
    w={'Q':1,'u':0,'d':0,'L':1,'e':0,'n':0,'H':1}
    def weights(ep):
        return {'Q':1+2*ep,'u':-4-2*ep,'d':2-2*ep,'L':-3-6*ep,
                'e':6+6*ep,'n':6*ep,'H':F(3)}
    rows=R['global_lattices']['fixed_lattice_rows'];out=[]
    test('37 complete lattice inputs',[F(r['epsilon']) for r in rows]==[F(i,6) for i in range(-12,25)])
    for row in rows:
        ep=F(row['epsilon']);z=weights(ep)
        product_ok=all(v.denominator==1 for v in z.values())
        allowed={'product':product_ok}
        for name,power in [('Z2',3),('Z3',2),('Z6',1)]:
            allowed[name]=product_ok and all((power*(F(t[k],3)+F(w[k],2)+z[k]/6)).denominator==1 for k in z)
        test('center-character lattice '+str(ep),z=={k:F(v) for k,v in row['weights'].items()} and allowed==row['allowed'])
        out.append(dict(epsilon=str(ep),allowed=allowed))
    variable=R['global_lattices']['variable_primitive_lattice_examples']
    test('four complete compact-example exponents',[r['k'] for r in variable]==[3,6,12,22])
    for row in variable:
        D=10**row['k'];ep=F(1,D);ys={k:v/6 for k,v in weights(ep).items()}
        z={k:v*D for k,v in ys.items()}
        test('primitive compact example '+str(row['k']),all(v.denominator==1 for v in z.values())
             and z==row['primitive_weights'] and math.gcd(*(int(v) for v in z.values()))==1
             and z['n']==1 and z['H']==D//2 and F(row['epsilon'])==ep
             and F(row['primitive_unit'])==F(1,D) and F(row['delta'])==F(1,D+1)
             and row['fixed_H_weight_3'] is False)
    # Delta is strictly increasing on eps > -1. Positive lattice closest to
    # zero occurs at the smallest positive epsilon; only eps=-1/2 contributes
    # a negative product-lattice candidate and it has |delta|=1.
    test('product charge gap',F(1,2)/(1+F(1,2))==F(1,3) and abs(F(-1,2)/(1+F(-1,2)))==1
         and F(R['global_lattices']['positive_near_standard_gap_product'])==F(1,3))
    test('Z6 charge gap',F(3)/(1+F(3))==F(3,4) and F(R['global_lattices']['positive_near_standard_gap_Z6'])==F(3,4))
    test('compactness-implies-finite-gap mutation killed',F(variable[-1]['delta'])>0 and F(variable[-1]['delta'])<F(1,10**21))
    # Fixed character lattice need not be generated by the occupied weights.
    nonfaithful=weights(F(1))
    test('fixed-character-lattice versus matter-faithfulness distinction',math.gcd(*(int(v) for v in nonfaithful.values()))==3)
    detail['lattice_rows']=out
    detail['lattice_boundary']='At epsilon=1 all occupied z weights share gcd 3. The specified U(1) character lattice remains fixed; a faithful matter spectrum was not stipulated.'


def observations():
    y=F(OBS['neutron']['mean_in_1e_minus21']);vy=F(OBS['neutron']['reported_uncertainty_in_1e_minus21'])**2
    s=F(OBS['molecule']['mean_in_1e_minus21']);vs=F(OBS['molecule']['reported_uncertainty_in_1e_minus21'])**2
    Z=16+6*9;N=16+6*10;A=Z+N;c=F(N,A)
    test('nominal molecule reconstructed from S32 plus six F19',Z==70 and N==76 and A==146 and Z==OBS['molecule']['Z_nominal'] and A==OBS['molecule']['A_nominal'])
    prediction=c*y;vprediction=c*c*vy;residual=s-prediction;vresidual=vs+vprediction
    joint=(y*vs+c*s*vy)/(vs+c*c*vy);vjoint=vy*vs/(vs+c*c*vy)
    chi=(y-joint)**2/vy+(s-c*joint)**2/vs
    test('joint exact chi-square equals transfer squared pull',chi==residual**2/vresidual)
    general=[F(A,Z)*s-F(N,Z)*y,y,F(A,Z)*(s-y)]
    # Derivatives with respect to the independent source summaries (y,s).
    dy=[-F(N,Z),F(1),-F(A,Z)];ds=[F(A,Z),F(0),F(A,Z)]
    cov=[[dy[i]*dy[j]*vy+ds[i]*ds[j]*vs for j in range(3)] for i in range(3)]
    test('exact full correlated covariance rank2',S.Matrix(cov).rank()==2)
    test('exact general neutrino identity',general[0]-general[1]==general[2])
    o=R['observations'];cal=o['calibration_only'];trans=o['exposed_development_transfer'];j=o['optional_joint_summary_refit'];g=o['general_two_parameter_inversion']
    near('neutron calibration delta',cal['delta'],y);near('neutron sigma',cal['reported_sigma'],math.sqrt(vy))
    delta=y/F(10**21);ep=delta/(1-delta)
    test('exact physical delta and epsilon',F(cal['delta_exact'])==delta and F(cal['epsilon_exact'])==ep)
    exact_transfer={'predicted_s':prediction,'predicted_sigma':math.sqrt(vprediction),'observed_s':s,'reported_observed_sigma':math.sqrt(vs),
                    'residual':residual,'independent_Gaussian_combined_sigma':math.sqrt(vresidual),'standardized_residual':float(residual)/math.sqrt(vresidual)}
    for key,value in exact_transfer.items():near('transfer '+key,trans[key],value)
    test('transfer fixed design',F(trans['design_coefficient'])==c)
    for key,value in {'delta':joint,'sigma':math.sqrt(vjoint),'chi2':chi}.items():near('optional joint '+key,j[key],value)
    for i in range(3):
        near('general mean '+str(i),g['means'][i],general[i]);near('general sigma '+str(i),g['sigmas'][i],math.sqrt(cov[i][i]))
        for k in range(3):near('general covariance '+str((i,k)),g['covariance'][i][k],cov[i][k])
    p=OBS['molecule']['polarity_means_in_1e_minus21'];pmean=[F(v['mean']) for v in p];psig=[F(v['uncertainty']) for v in p]
    halfsum=sum(pmean)/2;halfdiff=(pmean[0]-pmean[1])/2;halfvar=sum(v*v for v in psig)/4
    pol=o['polarity_check'];near('polarity half sum',pol['half_sum'],halfsum);near('polarity odd nuisance',pol['half_difference_nuisance'],halfdiff)
    near('polarity sigma',pol['unrounded_independent_sigma'],math.sqrt(halfvar));near('polarity published rounded sigma',pol['published_rounded_sigma'],math.sqrt(vs))
    test('all fit/test roles explicit',cal['input']=='neutron' and trans['blind'] is False and trans['refit'] is False
         and j['calibration_inputs']==['neutron','SF6'] and j['independent_test'] is False and j['p_value_reported'] is False
         and j['summary_degrees_of_freedom']==1 and g['anomaly_family_imposed'] is False and g['neutrino_neutrality_imposed'] is False
         and pol['unconstrained_even_offset_degenerate_with_s'] is True)
    test('neutral-antineutrino-imposition mutation killed',c*y!=y)
    test('uncorrelated-general-inversion mutation killed',cov[0][1]!=0)
    test('pre-normalization-epsilon-is-measured-charge mutation killed',F(2,3)!=F(2,3)/(1+F(2,3)))
    detail['observations_exact']={'nominal_Z':Z,'nominal_N':N,'nominal_A':A,'coefficient':str(c),'prediction':str(prediction),
        'prediction_variance':str(vprediction),'residual':str(residual),'residual_variance':str(vresidual),
        'joint_delta':str(joint),'joint_variance':str(vjoint),'joint_chi2':str(chi),'general_means':[str(x) for x in general],
        'general_covariance':[[str(x) for x in row] for row in cov],'polarity_half_sum':str(halfsum),'polarity_half_difference':str(halfdiff),'polarity_half_variance':str(halfvar)}


def identity_checks():
    pins=json.loads((HERE/'SOURCE_PINS_v1.json').read_text())
    for row in pins['sources']:
        p=HERE/row['snapshot'];content=p.read_bytes()
        test('exact source snapshot '+row['path'],hashlib.sha256(content).hexdigest()==row['sha256'] and len(content)==row['bytes'])
    freeze=json.loads((SNAP/'evidence_v1/FREEZE.json').read_text())
    ex=json.loads((SNAP/'evidence_v1/EXECUTION.json').read_text())
    test('frozen/result source identity map',freeze['source_sha256']==R['source_sha256'])
    for path,h in freeze['source_sha256'].items():
        test('author executed input '+path,hashlib.sha256((SNAP/path).read_bytes()).hexdigest()==h
             and (SNAP/path).read_bytes()==(SNAP/'evidence_v1/source_snapshot'/path).read_bytes())
    initial=json.loads((SNAP/'FREEZE.json').read_text())
    test('freeze and execution order',initial['at']<freeze['at']==ex['started_at']<ex['ended_at']
         and initial['numeric_execution_started'] is False and initial['observational_summaries_already_exposed'] is True
         and initial['protocol_sha256']==freeze['source_sha256']['PROTOCOL.md'])
    test('author execution record success',ex['returncode']==0 and ex['error'] is None and ex['source_unchanged'] is True and (SNAP/'evidence_v1/stderr.txt').stat().st_size==0)
    test('stdout complete summary matches JSON',json.loads((SNAP/'evidence_v1/stdout.txt').read_text())==R['summary'])


def main():
    destination=Path(sys.argv[1])
    if destination.exists():raise RuntimeError('Preserve prior evidence; choose a new output name.')
    for operation in [identity_checks,polynomial_checks,representation_checks,rational_checks,graph_checks,lattice_checks,observations]:operation()
    result={'created_utc':datetime.now(timezone.utc).isoformat(),'method':'Independent implementation; no author imports or execution.',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'frozen_results_sha256':hashlib.sha256((SNAP/'evidence_v1/RESULTS.json').read_bytes()).hexdigest(),
            'check_count':len(checks),'failed_checks':[r for r in checks if not r['passed']],
            'passed':all(r['passed'] for r in checks),'checks':checks,'details':detail}
    destination.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:result[k] for k in ['created_utc','check_count','failed_checks','passed']},sort_keys=True))
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
