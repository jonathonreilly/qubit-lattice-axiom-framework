#!/usr/bin/env python3
"""Fixed separate-source three-by-three trial construction and certificate."""
from fractions import Fraction as F
from pathlib import Path
import json,resource,signal,sys,time
import sympy as s
from certify_block12_two_source import HERE,I,A0,C0,ODD,LOCALS,load_inputs,check_formulas,envelopes,evaluate,root_hi,sha,frac


def trial_source(moments,env):
    candidates=[]
    for name,Q in envelopes():
        H=[s.expand(sum(c*moments[j+k] for k,c in enumerate(Q))) for j in range(7)]
        h_intervals=[evaluate(z,env) for z in H]
        h=[s.Rational(z.lo+z.hi)/2 for z in h_intervals]
        matrix=s.Matrix(3,3,lambda i,j:h[i+j+2]);vector=s.Matrix(h[1:4])
        minors=[matrix[:j,:j].det() for j in (1,2,3)]
        record={'envelope':name,'midpoint_leading_minors':[str(z) for z in minors]}
        if not all(z>0 for z in minors):
            record['status']='rejected_nonpositive_midpoint_matrix';candidates.append(record);continue
        exact=matrix.inv()*vector;scale=1<<80
        q=[]
        for v in exact:
            value=frac(v);rounded=(value*scale+F(1,2)).numerator//(value*scale+F(1,2)).denominator
            q.append(s.Rational(rounded,scale))
        residual=H[0]-2*sum(q[j]*H[j+1] for j in range(3))+sum(q[i]*q[j]*H[i+j+2] for i in range(3) for j in range(3))
        bound=evaluate(residual,env);assert bound.hi>=0,('negative_error_upper',name)
        record.update(status='certified_trial',q=[str(z) for z in q],squared_error=bound.pair())
        candidates.append(record)
    valid=[z for z in candidates if z['status']=='certified_trial'];assert valid,'no_valid_candidate'
    best=min(valid,key=lambda z:F(z['squared_error'][1]))
    return {'selected':best,'Y_upper':str(root_hi(best['squared_error'][1])),'candidates':candidates}


def run():
    started=time.monotonic();inp,accepted,env,manifest=load_inputs()
    prior=json.loads((HERE/'BLOCK12_GREEN_REFINED_RESULT.json').read_text())
    assert prior['status']=='completed_fixed_green_refinement'
    assert prior['source_sha256']==sha(HERE/'certify_block12_two_source.py')
    assert prior['refinement_source_sha256']==sha(HERE/'refine_block12_green.py')
    env.update({A0:I(*prior['scalar_inputs']['A0']),C0:I(*prior['scalar_inputs']['C0'])})
    moment_data,comparisons,_=check_formulas(env,accepted)
    source_trials={kind:trial_source(moment_data[kind]['ward'],env) for kind in ('P','O')}
    q={kind:[s.Rational(z) for z in source_trials[kind]['selected']['q']] for kind in ('P','O')}
    formulas=json.loads((HERE/'BLOCK12_SEPARATE_FORMULAS.json').read_text())
    check=json.loads((HERE/'BLOCK12_SEPARATE_CHECKS.json').read_text())
    assert check['status']=='passed' and check['ordered_pairs']==90 and check['norm_checks']==30
    assert formulas['source_sha256']==sha(HERE/'derive_block12_separate.py')
    assert check['source_sha256']==sha(HERE/'check_block12_separate.py')
    for packet in (formulas,check):
        for name,value in packet['helper_sha256'].items():assert value==sha(HERE/name)
    p_syms=s.symbols('p0:3',real=True);r_syms=s.symbols('r0:3',real=True)
    q_syms=s.symbols('q0:3',real=True);u_syms=s.symbols('u0:3',real=True)
    local=LOCALS|{str(z):z for z in p_syms+r_syms+q_syms+u_syms}
    nominal_expr=s.sympify(formulas['complete_nominal'],locals=local)
    results={}
    for mode,data in inp.items():
        p={kind:[s.Rational(z) for z in data['rows'][kind]['p']] for kind in ('P','O')}
        substitutions=dict(zip(p_syms,p['P']))|dict(zip(r_syms,p['O']))|dict(zip(q_syms,q['P']))|dict(zip(u_syms,q['O']))
        nominal=evaluate(nominal_expr.subs(substitutions),env)
        a2=I(0);b2=I(0);E2=F(0);F2=F(0);rows={}
        for kind in ('P','O'):
            count=12 if kind=='P' else 3
            E=F(prior['results'][mode]['rows'][kind]['errors']['vacuum']['error_upper'])
            Y=F(source_trials[kind]['Y_upper']);w=root_hi(72*env[A0].hi if kind=='P' else 12)
            ferr=Y+w*E;E2+=count*E**2;F2+=count*ferr**2
            nx,nv=[evaluate(s.sympify(z,locals=local).subs(dict(zip(p_syms,p[kind]))|dict(zip(q_syms,q[kind]))),env) for z in formulas['norms'][kind]]
            assert nx.hi>=0 and nv.hi>=0
            a2+=count*nx;b2+=count*nv
            rows[kind]={'p':[str(z) for z in p[kind]],'q':[str(z) for z in q[kind]],
                        'E_upper':str(E),'Y_upper':str(Y),'Ward_norm_upper':str(w),'v_error_upper':str(ferr),
                        'x_trial_squared_norm':nx.pair(),'v_trial_squared_norm':nv.pair()}
        E=root_hi(E2);FF=root_hi(F2);a=root_hi(a2.hi);b=root_hi(b2.hi)
        chi=min(root_hi(240),a+E);psi=min(root_hi(30720),b+FF)
        error=6*(E*(a+chi)+min(E*b+chi*FF,E*psi+a*FF))
        interval=I((nominal.lo-error)/8,(nominal.hi+error)/8)
        results[mode]={'rows':rows,'nominal':nominal.pair(),'alpha':interval.pair(),
                       'a_upper':str(a),'b_upper':str(b),'E_upper':str(E),'F_upper':str(FF),'comparison_error':str(error),
                       'status':'inconclusive_zero_in_interval' if interval.lo<=0<=interval.hi else 'conditional_sign_resolved'}
    seconds=time.monotonic()-started;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes=rss if sys.platform=='darwin' else rss*1024
    assert seconds<=60 and rss_bytes<=384*1024**2,('budget_exceeded',seconds,rss_bytes)
    return {'status':'completed_fixed_separate_source_protocol','seconds':seconds,'peak_rss_bytes':rss_bytes,
            'scope':'conditional supplied native model/gap/scalars, same-author algebra/arithmetic; no independent source audit',
            'source_sha256':sha(__file__),'protocol_sha256':sha(HERE/'BLOCK12_SEPARATE_PROTOCOL.md'),
            'dependencies_sha256':{name:sha(HERE/name) for name in ('certify_block12_two_source.py','BLOCK12_GREEN_REFINED_RESULT.json','BLOCK12_SEPARATE_FORMULAS.json','BLOCK12_SEPARATE_CHECKS.json')},
            'source_trials':source_trials,'results':results,'scalar_inputs':{str(k):v.pair() for k,v in env.items()},
            'input_manifest':manifest}


if __name__=='__main__':
    def deadline(signum,frame):raise TimeoutError('fixed60secondbudget')
    signal.signal(signal.SIGALRM,deadline);signal.alarm(60);result=run();signal.alarm(0)
    (HERE/'BLOCK12_SEPARATE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    for kind,row in result['source_trials'].items():print(kind,row['selected']['envelope'],[float(s.Rational(z)) for z in row['selected']['q']],'Y=',float(F(row['Y_upper'])))
    for mode,row in result['results'].items():print(mode,row['status'],'N=',[float(F(z)) for z in row['nominal']],'alpha=',[float(F(z)) for z in row['alpha']],'F=',float(F(row['F_upper'])))
    print('seconds',result['seconds'],'peak_rss_bytes',result['peak_rss_bytes'])
