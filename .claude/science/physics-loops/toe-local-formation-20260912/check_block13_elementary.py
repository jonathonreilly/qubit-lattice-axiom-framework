#!/usr/bin/env python3
"""Fixed elementary-source interval probe with rounded rational coefficients."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,time,resource,sys,signal
from verify_block12_sign_witness import Polynomial,parse,coefficients,envelope,convolution,root,sha
HERE=Path(__file__).resolve().parent


def elementary_scalars(N=256):
    assert N==256;probabilities=[F(comb(2*n,n)*sum(comb(n,j)**2*comb(2*j,j) for j in range(n+1)),36**n) for n in range(N+1)]
    total=sum(probabilities);tail=F(1,8)
    env={'A0':(total/6,(total+tail)/6)}
    root_hi=root(F(6));root_lo=root_hi-F(1,1<<128);assert root_lo**2<=6<=root_hi**2
    rows=[]
    for r in (-1,1,3,5,7,9):
        exponent=F(r,2);coef=F(1);weighted=F(1)
        for n in range(1,N+2):
            m=2*n-2;coef=coef*(exponent-m)*(exponent-m-1)/((m+1)*(m+2))
            if n<=N:weighted+=coef*probabilities[n]
        omitted=coef;assert 0<(exponent-2*N-2)*(exponent-2*N-3)/((2*N+3)*(2*N+4))<1
        lo=weighted+min(F(0),omitted*tail);hi=weighted+max(F(0),omitted*tail)
        # 6^(r/2)=6^((r-1)/2)*sqrt6, with r=-1 handled exactly.
        prefactor=F(6)**((r-1)//2);value=(prefactor*root_lo*lo,prefactor*root_hi*hi)
        assert value[0]>0 and value[0]<=value[1]
        env['C0' if r==-1 else 'L'+str(r)]=value
        rows.append({'r':r,'last_coefficient':str(omitted),'interval':[str(v) for v in value]})
    return env,{'N':N,'return_partial_sum':str(total),'return_tail_upper':str(tail),'rows':rows}


def run():
    start=time.monotonic();env,scalar_record=elementary_scalars()
    old=json.loads((HERE/'BLOCK12_SIGN_WITNESS.json').read_text())
    witness={'p':{},'q':{}}
    for name in ('p','q'):
        for kind in ('P','O'):
            vals=[]
            for v in old[name][kind]:
                z=F(v)*1000+F(1,2);vals.append(F(z.numerator//z.denominator,1000))
            witness[name][kind]=vals
    raw=json.loads((HERE/'BLOCK12_MOMENT_FORMULAS.json').read_text())['moments']
    formulas=json.loads((HERE/'BLOCK12_SEPARATE_FORMULAS.json').read_text())
    Q=envelope(F(1,4),F(4),F(8));E2=F(0);F2=F(0);a2=F(0);b2=F(0);rows={}
    for kind in ('P','O'):
        errors={}
        for source,p in (('vacuum',witness['p'][kind]),('ward',witness['q'][kind])):
            m=[parse(z) for z in raw[kind][source]];d=convolution([F(1)]+[-v for v in p],[F(1)]+[-v for v in p])
            expr=Polynomial.constant(0)
            for j,c in enumerate(Q):
                for k,e in enumerate(d):expr=expr+m[j+k].scale(c*e)
            interval=expr.interval(env);assert interval[1]>=0
            errors[source]=root(interval[1])
        E=errors['vacuum'];Y=errors['ward'];w=root(72*env['A0'][1] if kind=='P' else F(12))
        count=12 if kind=='P' else 3;E2+=count*E**2;F2+=count*(Y+w*E)**2
        vals=coefficients(witness['p'][kind],'p')|coefficients(witness['q'][kind],'q')
        nx,nv=[parse(z,vals).interval(env) for z in formulas['norms'][kind]]
        assert nx[1]>=0 and nv[1]>=0;a2+=count*nx[1];b2+=count*nv[1]
        rows[kind]={'E':str(E),'Y':str(Y),'W':str(w),'nx':list(map(str,nx)),'nv':list(map(str,nv))}
    vals=coefficients(witness['p']['P'],'p')|coefficients(witness['p']['O'],'r')|coefficients(witness['q']['P'],'q')|coefficients(witness['q']['O'],'u')
    nominal=parse(formulas['complete_nominal'],vals).interval(env)
    a,b,E,FF=map(root,(a2,b2,E2,F2));err=6*(E*(2*a+E+b+FF)+a*FF)
    alpha=((nominal[0]-err)/8,(nominal[1]+err)/8)
    coarse=(F(1871,200),F(2724,125),F(1473,1000),F(1761,125))
    assert all(x<y for x,y in zip((a,b,E,FF),coarse))
    aa,bb,ee,ff=coarse;coarse_error=6*(ee*(2*aa+ee+bb+ff)+aa*ff)
    assert 1345<nominal[0]<=nominal[1]<1347 and coarse_error<1287
    assert (1345-coarse_error)/8>7 and (1347+coarse_error)/8<330
    seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes=rss if sys.platform=='darwin' else rss*1024
    assert seconds<60 and rss_bytes<=384*1024**2
    return {'status':'positive_elementary_candidate' if alpha[0]>0 else 'inconclusive_elementary_candidate','alpha':list(map(str,alpha)),
            'p':{k:list(map(str,v)) for k,v in witness['p'].items()},'q':{k:list(map(str,v)) for k,v in witness['q'].items()},
            'norms':{k:str(v) for k,v in zip(('a','b','E','F'),(a,b,E,FF))},'nominal':list(map(str,nominal)),
            'error':str(err),'source_rows':rows,'coarse_interval':['7','330'],'coarse_error':str(coarse_error),
            'peak_rss_bytes':rss_bytes,'scalar_certificate':scalar_record,
            'seconds':seconds,'source_sha256':sha(__file__),'protocol_sha256':sha(HERE/'BLOCK13_WORKING_PLAN.md'),
            'dependencies_sha256':{n:sha(HERE/n) for n in ('verify_block12_sign_witness.py','BLOCK12_SIGN_WITNESS.json','BLOCK12_MOMENT_FORMULAS.json','BLOCK12_SEPARATE_FORMULAS.json')},
            'scope':'all radial scalar bounds from elementary return-series estimates; native-model algebra/gap and Dirac identification still require the separate analytical proof'}


if __name__=='__main__':
    def deadline(signum,frame):raise TimeoutError('fixed60secondbudget')
    signal.signal(signal.SIGALRM,deadline);signal.alarm(60);result=run();signal.alarm(0)
    (HERE/'BLOCK13_ELEMENTARY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'],'alpha',[float(F(z)) for z in result['alpha']])
    print('p',result['p'],'q',result['q']);print('norms',{k:float(F(v)) for k,v in result['norms'].items()})
    print('nominal',[float(F(z)) for z in result['nominal']],'seconds',result['seconds'])
