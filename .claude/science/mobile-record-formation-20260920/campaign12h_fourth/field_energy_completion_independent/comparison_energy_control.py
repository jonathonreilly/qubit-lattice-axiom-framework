#!/usr/bin/env python3
"""Post-PRE checks using only the frozen independent primitive-path model.

Targets are known from source comparison; no parameter is fitted. All output
paths stay beside this file. Adjacent source lookup precedes absolute fallback.
"""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict, Counter
from itertools import product
import hashlib, importlib.util, json

HERE=Path(__file__).resolve().parent
FALLBACK=Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/science/mobile-record-formation-20260920/campaign12h_fourth')
def source(rel):
    for base in (HERE.parent,FALLBACK):
        p=base/rel
        if p.exists(): return p
    raise FileNotFoundError(rel)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
PRE=HERE/'exact_control.py'
assert sha(PRE)=='294170fa9b47a9ed2f9d207bef79364ca7a28dc6f8da431b4001e7997b80d4cb'
spec=importlib.util.spec_from_file_location('frozen_electric_PRE',PRE)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
g=m.Graph(8,(0,3,5,6),[(u,v) for u in range(8) for v in range(u+1,8) if (u^v) in (1,2,4)])

def dot(v,w): return sum((a*w.get(s,0) for s,a in v.items()),Q(0))
def scale(v,c): return m.clean({s:a*c for s,a in v.items()})
def init(n):
    q=tuple(int(x in g.aa) for x in range(8));ee=[0]*12
    for edge,sg in (((0,1),1),((0,2),-1),((1,3),1),((2,3),-1)):ee[g.idx[edge]]=sg*n
    s=(q,tuple(ee));assert g.gauss(s)
    return {s:Q(1)}
def B(v,a,b,c):
    out=defaultdict(Q)
    for s,amp in v.items():
        for target,weight,d in g.marked_paths(s,a,b,c):
            assert weight==1
            out[target]+=amp
    return m.clean(out)
def Bstar(v,a,b,c):
    out=defaultdict(Q);i=g.idx[tuple(sorted((a,b)))];sg=1 if a<b else -1
    for (q,ee),amp in v.items():
        if (q[a],q[b])!=(c,-c):continue
        qq,ff=list(q),list(ee);qq[a]=qq[b]=0;ff[i]-=sg*c
        middle=(tuple(qq),tuple(ff));assert g.gauss(middle)
        for d in g.nb[a]:
            res=g.shift(middle,d,a)
            if res is not None and g.W(res[0])==0:out[res[0]]+=amp
    return m.clean(out)
def diagonal(v,lam):
    out={}
    for s,a in v.items():
        e2,d=g.electric(s);value=(1-lam)*d+lam*e2
        if value:out[s]=a*value
    return out
def h4(v):return g.H4(v)[0]
def serial(v):return [{'q':s[0],'E':s[1],'amplitude':str(a)} for s,a in sorted(v.items())]

rows=[];author_match_rows={};certificate_own=None
for n in (-101,-7,-2,-1,0,1,2,19,101):
    omega=init(n);first=B(omega,0,1,1);second=B(first,6,7,1)
    norm=dot(first,first);assert norm==dot(second,second)==2
    hv=h4(first);hv0=h4(omega)
    hm=dot(first,hv)/norm;hsecond=dot(hv,hv)/norm;hvar=hsecond-hm*hm
    assert hm==-20 and hsecond==792 and hvar==392
    assert all(hv[s]==-20*a for s,a in first.items())
    assert dot(omega,hv0)==-84
    if n==0:certificate_own=hv
    first_values=[{'q':s[0],'E':s[1],'E2':g.electric(s)[0],'D':g.electric(s)[1]} for s in first]
    assert [x['D'] for x in first_values]==[0,2*n*n]
    assert [x['E2'] for x in first_values]==[4*n*n+4*n+2,4*n*n+2*n+2]
    instruments={}
    for coherent in (False,True):
        vv=[];gamma={};cross=[]
        for u,v in g.edges:
            a,b=(u,v) if u in g.aa else (v,u)
            plus,minus=B(omega,a,b,1),B(omega,a,b,-1)
            zp=g.hop_sum(g.hop_sum(plus,target_w=1),target_w=2)
            zm=g.hop_sum(g.hop_sum(minus,target_w=1),target_w=2)
            cross.append(dot(zp,zm))
            if coherent:
                vc=m.add((1,plus),(1,minus));vv.append(vc)
                gamma=m.add((1,gamma),(1,Bstar(vc,a,b,1)),(1,Bstar(vc,a,b,-1)))
            else:
                vv.extend((plus,minus))
                gamma=m.add((1,gamma),(1,Bstar(plus,a,b,1)),(1,Bstar(minus,a,b,-1)))
        assert gamma==scale(omega,48) and all(z==0 for z in cross)
        post_d=sum(dot(v,diagonal(v,Q(0))) for v in vv)
        post_e2=sum(dot(v,diagonal(v,Q(1))) for v in vv)
        post_h4=sum(dot(v,h4(v)) for v in vv)
        assert (post_d,post_e2,post_h4)==(96*n*n,192*n*n+96,-816)
        instruments['coherent' if coherent else 'resolved']={'marks':len(vv),'loss_eigenvalue':48,'post_D':str(post_d),'post_E2':str(post_e2),'post_H4':str(post_h4),'E2_drift_over_kappa':str(post_e2-48*4*n*n),'D_drift_over_kappa':str(post_d-48*4*n*n),'H4_drift_over_kappa':str(post_h4-48*(-84)),'Z_cross_terms':list(map(str,cross))}
    lr=[]
    for lam in (Q(0),Q(1,3),Q(1,2),Q(1),Q(2,7),Q(5,9)):
        dv=diagonal(first,lam)
        mean=dot(first,dv)/norm;var=dot(dv,dv)/norm-mean*mean
        cov=dot(dv,hv)/norm-mean*hm
        assert mean==(1+3*lam)*n*n+3*lam*n+2*lam
        assert var==((1-lam)*n*n-lam*n)**2 and cov==0
        delta_e=mean-4*n*n
        all_drift=(1-lam)*post_d+lam*post_e2-48*4*n*n
        assert all_drift==-96*(1-lam)*n*n+96*lam
        term_energies=[lam*g.electric(s)[0] for s in second]
        frequency=abs(term_energies[0]-term_energies[1])
        assert frequency==2*lam*abs(n)
        lr.append({'lambda':str(lam),'first_D_lambda_mean':str(mean),'first_D_lambda_variance':str(var),'D_lambda_H4_covariance':str(cov),'terminal_frequency_over_K_absolute':str(frequency),'selected_mean_change_K_coefficient':str(delta_e),'selected_mean_change_delta_coefficient':'64','variance_K2_coefficient':str(var),'variance_Kdelta_coefficient':str(2*cov),'variance_delta2_coefficient':str(hvar),'initial_drift_over_kappa_K_coefficient':str(all_drift),'initial_drift_over_kappa_delta_coefficient':'3216'})
    row={'n':n,'first_paths':first_values,'first_H4_mean':str(hm),'first_H4_second_moment':str(hsecond),'first_H4_variance':str(hvar),'first_H4_image':serial(hv),'terminal_states':serial(second),'instruments':instruments,'lambdas':lr}
    rows.append(row);author_match_rows[n]=row
    print(json.dumps({'n':n,'lambda_cases':len(lr),'first_H4_words':len(hv),'H4_variance':str(hvar),'all_mark_E2_drift':96,'all_mark_H4_drift':3216},sort_keys=True))

# Save the reconstructed data before comparing against the author values.
(HERE/'COMPARISON_OWN_ENERGY_RESULTS.json').write_text(json.dumps({'own_frozen_model_sha256':sha(PRE),'rows':rows},indent=2,sort_keys=True)+'\n')
cert_path=source('high_flux_energy_extension_author/SELECTED_H4_IMAGE_CERTIFICATE.json')
assert sha(cert_path)=='e2266dbcb0de8faddfcd265a6e7c3c995bb66cc9d9ce17f84826f360af676b39'
cert=json.loads(cert_path.read_text())
cert_vec={(tuple(x['charges']),tuple(x['field'])):Q(x['amplitude']) for x in cert['H4_image']}
assert certificate_own==cert_vec
author_path=source('field_energy_completion_author/COMPLETION_AND_TERMINAL_PHASE_RESULTS.json')
assert sha(author_path)=='3af79c54800f5c826a2d4f87260e49bbadc389cae203b9b2dfbbaff451dfc1e4'
author=json.loads(author_path.read_text());comparisons=0
for ar in author['rows']:
    own=author_match_rows[ar['n']]
    assert {(tuple(x['q']),tuple(x['E'])) for x in ar['terminal_states']}=={(tuple(x['q']),tuple(x['E'])) for x in own['terminal_states']}
    assert ar['ordered_two_mark_norm_squared']==2
    assert ar['small_time_history_probability_over_kappa2_t2']==1
    diff=tuple(x-y for x,y in zip(own['terminal_states'][0]['E'],own['terminal_states'][1]['E']))
    assert tuple(ar['wilson_translation_difference']) in (diff,tuple(-x for x in diff))
    assert sorted(sum(e*e for e in x['E']) for x in own['terminal_states'])==ar['terminal_E2_eigenvalues']
    for al in ar['lambdas']:
        mine=next(l for l in own['lambdas'] if l['lambda']==al['lambda'])
        for key,value in al.items():assert mine[key]==value,(ar['n'],key,mine[key],value)
        comparisons+=1
local=[]
for row in author['local_diagonal_bounds']:
    S=row['S'];cc=S*(S+1);maximum=Q(0)
    for e in range(-S,S+1):
        for qa,qb,sg in product((-1,0,1),(-1,0,1),(-1,1)):
            active=qa!=0 and qb==0
            numerator=sg*qa*e if active else e*e
            maximum=max(maximum,abs(Q(numerator,cc)))
    assert maximum==Q(row['exact_largest_abs_local_R'])==Q(S,S+1)
    local.append({'S':S,'maximum':str(maximum)})
# Explicit counterexample to an unconditional terminal-sector existence claim.
full_six_cycle_words=[q for q in product((-1,1),repeat=6) if sum(q)==3]
assert not full_six_cycle_words
# Discriminating controls for the new energy terms and full covariance.
case1=author_match_rows[1]
one=next(x for x in case1['lambdas'] if x['lambda']=='1')
assert Q(one['first_D_lambda_mean'])!=1 # incorrectly retaining D
assert Q(one['initial_drift_over_kappa_K_coefficient'])!=0 # dropping two unit shifts
assert Q(one['variance_delta2_coefficient'])!=0 # keeping only support diagonal H4
summary={'own_frozen_model_sha256':sha(PRE),'author_rows_compared':len(author['rows']),'author_lambda_rows_compared':comparisons,'own_n_values':[r['n'] for r in rows],'own_total_lambda_cases':sum(len(r['lambdas']) for r in rows),'H4_certificate_words_matched':len(cert_vec),'H4_coefficient_histogram':dict(sorted(Counter(str(x) for x in cert_vec.values()).items())),'sharp_local_bounds':local,'six_cycle_Gauss_compatible_full_occupancy_words':len(full_six_cycle_words),'negative_controls_detected':['replace D_lambda by D at lambda=1','drop constant E2 birth drift','discard off-support H4 image'],'sources':{str(p):sha(p) for p in (PRE,author_path,cert_path)}}
(HERE/'COMPARISON_EXACT_MATCHES.json').write_text(json.dumps(summary,indent=2,sort_keys=True)+'\n')
print(json.dumps(summary,sort_keys=True))
print('COMPARISON CONTROL COMPLETE: all exact comparisons passed; scope correction required for terminal-sector existence.')
