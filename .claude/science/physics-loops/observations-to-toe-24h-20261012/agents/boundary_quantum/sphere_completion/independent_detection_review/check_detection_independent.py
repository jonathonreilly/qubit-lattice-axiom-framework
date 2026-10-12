#!/usr/bin/env python3
"""Small independent all-trial loss-map checks; no author helpers or data fits."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
import sys
sys.dont_write_bytecode=True
import hashlib
import itertools
import json
import resource
import time
from datetime import datetime,timezone
from decimal import Decimal,localcontext
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
RT=Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
OUT=RT/'quantum/detection_readout/independent_detection_review'

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def guard():
    assert time.time()<json.loads((RT/'DEADLINE.json').read_text())['packaging_epoch']
    assert not any((RT/n).exists() for n in ('STOP_REQUESTED.json','USER_STOP_REQUESTED.json',
                    'STOP_REQUESTED','USER_STOP_REQUESTED','STOP_CAMPAIGN.json'))

def readq(row):
    return Q(int(row['numerator']),int(row['denominator']))

def packed(x):
    with localcontext() as ctx:
        ctx.prec=45
        dec=str(Decimal(x.numerator)/Decimal(x.denominator))
    return {'numerator':str(x.numerator),'denominator':str(x.denominator),'decimal':dec}

def ceilq(x):
    return x.numerator//x.denominator+bool(x.numerator%x.denominator)

def polynomial_root_bracket(function):
    # Exact bisection of the efficiency-gap polynomial, independent of author's isqrt route.
    lo,hi=Q(0),Q(1)
    assert function(lo)<0<function(hi)
    for _ in range(140):
        mid=(lo+hi)/2
        if function(mid)<0:
            lo=mid
        else:
            hi=mid
    assert function(lo)<=0<=function(hi)
    return lo,hi

def full_readout(joint,etaA,etaB,random_assignment):
    total=Q(0)
    for (x,y),prob in joint.items():
        for da,db in itertools.product((0,1),repeat=2):
            losses=(etaA if da else 1-etaA)*(etaB if db else 1-etaB)
            bits=list(itertools.product((-1,1),repeat=2)) if random_assignment else [(1,1)]
            for ra,rb in bits:
                total+=prob*losses*Q(1,len(bits))*(da*x+(1-da)*ra)*(db*y+(1-db)*rb)
    return total

def run():
    start=time.perf_counter()
    guard()
    manifest=json.loads((OUT/'snapshot_manifest_v1.json').read_text())
    v3=json.loads((OUT/'v3_wording_snapshot.json').read_text())
    records=manifest['sources']+manifest['receipts']+v3['records']
    for r in records:
        assert sha(r['original'])==sha(r['snapshot'])==r['sha256']
    freeze=json.loads((OUT/'snapshot_FREEZE.json').read_text())
    execution=json.loads((OUT/'snapshot_EXECUTION_SOURCE_v1.json').read_text())
    result=json.loads((OUT/'snapshot_RESULTS_v1.json').read_text())
    angular=json.loads((OUT/'snapshot_ANGULAR_RESULTS_v1.json').read_text())
    premise=json.loads((HERE/'DIRECT_REFLECTION_RESULT.json').read_text())
    by_name={Path(r['original']).name:r['sha256'] for r in manifest['sources']}
    by_original={r['original']:r['sha256'] for r in records}
    for name,h in freeze['sources'].items():
        assert (by_original[name] if Path(name).is_absolute() else by_name[name])==h
    assert execution['freeze_sha256']==result['freeze_sha256']==sha(OUT/'snapshot_FREEZE.json')
    assert execution['script_sha256']==result['script_sha256']==by_name['direct_detection_readout_check.py']
    assert 'direct_detection_readout_check.py' not in freeze['sources']  # Execution-pinned, not pre-freeze claim.
    assert freeze['equal_efficiencies']==['1','199/200','99/100','197/200','49/50','39/40','97/100']
    assert freeze['assignments']==['independent_fair_bits','constant_plus_one_fair_candidate']
    J=Q(111,20)
    ideal_B=Q(19,20)*(1-2*readq(premise['a3_interval'][1]))
    ideal_gap=ideal_B-1
    perturbed_gap=ideal_gap-J*(2*Q(19,20)*readq(angular['L_certified_upper'])*Q(1,1000)+Q(1,1000))
    angular_row=next(r for r in angular['rows'] if r['angle_per_side_rad']=='1/1000' and r['extra_candidate_error']=='1/1000')
    assert perturbed_gap==readq(angular_row['effective_gap_lower'])
    budget_gaps={'ideal':ideal_gap,'angle_and_candidate_error':perturbed_gap}
    rows=[]
    threshold_controls=[]
    for label,delta in budget_gaps.items():
        threshold=next(t for t in result['thresholds'] if t['budget']==label)
        functions={'random_assignment_eta_threshold':lambda eta:eta**2*(1+delta)-1,
                   'constant_plus_eta_threshold':lambda eta:delta*eta**2+2*eta-2}
        brackets={}
        for name,function in functions.items():
            independent=polynomial_root_bracket(function)
            published=tuple(map(readq,threshold[name]))
            assert function(published[0])<=0<=function(published[1])
            assert published[0]<=independent[0]<independent[1]<=published[1]
            brackets[name]=independent
        assert brackets['random_assignment_eta_threshold'][1] < brackets['constant_plus_eta_threshold'][0]
        threshold_controls.append({'budget':label,'independent_brackets':{k:[packed(x) for x in v] for k,v in brackets.items()}})
        for eta_text in freeze['equal_efficiencies']:
            eta=Q(eta_text)
            for assignment in freeze['assignments']:
                # Derive each gap through its polynomial, not by calling the published implementation.
                gap=(eta**2*(1+delta)-1 if assignment=='independent_fair_bits'
                     else delta*eta**2+2*eta-2)
                n=ceilq(40*J**2/gap**2) if gap>0 else None
                recorded=next(r for r in result['rows'] if r['budget']==label and r['eta_per_side']==eta_text and r['assignment']==assignment)
                assert gap==readq(recorded['gap_lower']) and n==recorded['N_for_each_error_at_most_1_percent']
                if n is not None:
                    target=40*J**2/gap**2
                    assert n-1<target<=n and Q(n)*gap**2/(8*J**2)>=5
                rows.append({'budget':label,'eta':eta_text,'assignment':assignment,'gap':packed(gap),'N':n})
    assert len(result['rows'])==len(rows)==28
    assert sum(r['N'] is None for r in rows)==10
    # Fair/random model never has a smaller certified gap than +1 assignment here.
    for i in range(0,28,2):
        random_gap,constant_gap=readq(rows[i]['gap']),readq(rows[i+1]['gap'])
        eta=Q(rows[i]['eta'])
        assert random_gap-constant_gap==(1-eta)**2

    # Exhaust the ideal outcomes, two detection bits and both assignment bits.
    biased={(1,1):Q(1,2),(1,-1):Q(1,5),(-1,1):Q(1,10),(-1,-1):Q(1,5)}
    fair={(1,1):Q(3,8),(1,-1):Q(1,8),(-1,1):Q(1,8),(-1,-1):Q(3,8)}
    etaA,etaB=Q(3,5),Q(4,5)
    enumerated=[]
    for label,joint in [('biased',biased),('fair',fair)]:
        assert sum(joint.values())==1 and min(joint.values())>=0
        mA=sum(p*x for (x,y),p in joint.items())
        mB=sum(p*y for (x,y),p in joint.items())
        C=sum(p*x*y for (x,y),p in joint.items())
        random=full_readout(joint,etaA,etaB,True)
        constant=full_readout(joint,etaA,etaB,False)
        general=etaA*etaB*C+etaA*(1-etaB)*mA+(1-etaA)*etaB*mB+(1-etaA)*(1-etaB)
        fair_formula=etaA*etaB*C+(1-etaA)*(1-etaB)
        assert random==etaA*etaB*C and constant==general
        if label=='fair':assert constant==fair_formula
        else:assert constant!=fair_formula
        enumerated.append({'fixture':label,'mA':str(mA),'mB':str(mB),'C':str(C),
                           'random_C':str(random),'constant_C':str(constant),
                           'constant_fair_formula':str(fair_formula)})

    # Same correlation, opposite small biases in equally weighted histories.
    # These probabilities are nonnegative for every C in [-.95,.95], not just test points.
    history_fixture=[]
    eta=Q(99,100)
    for s in (Q(1,100),Q(-1,100)):
        for C in (Q(-19,20),Q(0),Q(19,20)):
            joint={(x,y):(1+s*x+s*y+C*x*y)/4 for x,y in itertools.product((-1,1),repeat=2)}
            assert min(joint.values())>0 and sum(joint.values())==1
            assert sum(p*x*y for (x,y),p in joint.items())==C
            assert sum(p*x for (x,y),p in joint.items())==s
            assert full_readout(joint,eta,eta,True)==eta**2*C
            assert full_readout(joint,eta,eta,False)==eta**2*C+(1-eta)**2+2*eta*(1-eta)*s
        marginal_B_term=-2*eta*(1-eta)*s
        history_fixture.append({'conditional_mA_and_mB':str(s),'same_C_in_both_histories':True,
                                'B_offset_missing_if_only_unconditionally_fair':str(marginal_B_term)})
    assert sum(Q(r['conditional_mA_and_mB']) for r in history_fixture)==0
    # The two arms' shared loss bit, independent of ideal outputs, defeats etaA*etaB factorization.
    correlated_loss_C=Q(1,2)  # Ideal XY=1, common D=1 half the time; independent fair fill-ins otherwise.
    product_efficiency_prediction=Q(1,2)**2
    assert correlated_loss_C!=product_efficiency_prediction
    # Unconditional per-arm mean efficiency .99 can include a history with .97 and no positive gap.
    average_eta=Q(2,3)*1+Q(1,3)*Q(97,100)
    assert average_eta==Q(99,100)
    apparent_gap=average_eta**2*ideal_B-1
    low_history_gap=Q(97,100)**2*ideal_B-1
    assert apparent_gap>0>low_history_gap

    # POVM control with setting-dependent AND outcome-dependent efficiencies.
    z,wz=np.polynomial.legendre.leggauss(8)
    phi=2*np.pi*np.arange(17)/17
    a=np.array([[np.sqrt(1-zz*zz)*np.cos(pp),np.sqrt(1-zz*zz)*np.sin(pp),zz] for zz in z for pp in phi])
    weights=np.repeat(wz/34,17)
    b=a[:,[1,2,0]]
    sigma=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],dtype=complex)
    identity=np.eye(2,dtype=complex)
    def observables(directions):
        plus_eta=.2+.6*(1+directions[:,2])/2
        minus_eta=.9-.6*(1+directions[:,0])/2
        n_sigma=np.einsum('ni,ijk->njk',directions,sigma)
        Ep=plus_eta[:,None,None]*(identity+n_sigma)/2
        Em=minus_eta[:,None,None]*(identity-n_sigma)/2
        E0=identity-Ep-Em
        for effect in (Ep,Em,E0):assert np.min(np.linalg.eigvalsh(effect))>-1e-14
        random=Ep-Em
        constant=identity-2*Em
        assert np.max(np.abs(np.linalg.eigvalsh(random)))<=1+1e-14
        assert np.max(np.abs(np.linalg.eigvalsh(constant)))<=1+1e-14
        return {'random':random,'constant':constant}
    obsA,obsB=observables(a),observables(b)
    P3=(5*(a@a.T)**3-3*(a@a.T))/2
    values={}
    for assignment in ('random','constant'):
        # Singlet correlation for A=cI+v.sigma and B=dI+w.sigma: c*d-v.w.
        AA,BB=obsA[assignment],obsB[assignment]
        ca=np.trace(AA,axis1=1,axis2=2).real/2
        cb=np.trace(BB,axis1=1,axis2=2).real/2
        va=np.einsum('njk,ikj->ni',AA,sigma).real/2
        vb=np.einsum('njk,ikj->ni',BB,sigma).real/2
        C=ca[:,None]*cb[None,:]-va@vb.T
        B=-np.sum(weights*np.diag(C))+14*np.sum(weights[:,None]*weights[None,:]*P3*C)
        assert abs(B)<=1+1e-12
        values[assignment]=float(B)
    guard()
    for r in records:
        assert sha(r['original'])==sha(r['snapshot'])==r['sha256']
    output={'at':datetime.now(timezone.utc).isoformat(),'status':'PASS_WITH_V3_CONDITIONAL_FAIRNESS',
            'reviewer_script_sha256':sha(__file__),'source_records':records,
            'method':'Exact outcome/loss/fill-in enumeration, polynomial-root bisection, independent rational gap/count propagation, common-qubit POVM controls; no author helpers imported.',
            'rows':rows,'threshold_controls':threshold_controls,'enumerated_readouts':enumerated,
            'conditional_fairness_fixture':history_fixture,
            'correlated_loss_fixture':{'actual_C':str(correlated_loss_C),'etaA_etaB_prediction':str(product_efficiency_prediction)},
            'unconditional_efficiency_fixture':{'average_eta':str(average_eta),'apparent_gap':packed(apparent_gap),'low_history_gap':packed(low_history_gap)},
            'setting_and_outcome_dependent_quantum_POVMs':values,
            'provenance_limit':'Declared efficiencies/input sources frozen; checker is pinned by execution receipt, not listed in the earlier freeze. Current source and all rational results independently agree.',
            'scope':'Conditional prospective independent-loss model, fixed horizon, all heralded trials included before fresh choices. No empirical efficiency estimate or loophole-free apparatus validation.',
            'elapsed_seconds':time.perf_counter()-start,'max_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    with (OUT/'detection_independent_checks_v1.json').open('x') as f:json.dump(output,f,indent=2)
    print(json.dumps({'status':output['status'],'matched_rows':len(rows),'nonpositive_rows':sum(r['N'] is None for r in rows),
                      'quantum_POVM_values':values,'elapsed_seconds':output['elapsed_seconds'],'max_rss_bytes':output['max_rss_bytes']},indent=2))

if __name__=='__main__':
    run()
