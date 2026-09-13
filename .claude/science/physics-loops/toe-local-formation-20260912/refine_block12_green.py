#!/usr/bin/env python3
"""Fixed positive return-series refinement; supplied A0 certificate conditional."""
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
import json,resource,signal,sys,time
from certify_block12_two_source import I,A0,C0,root_hi,sha,certify
HERE=Path(__file__).resolve().parent


def return_numerator(n):return comb(2*n,n)*sum(comb(n,j)**2*comb(2*j,j) for j in range(n+1))


def run():
    start=time.monotonic();manifest=json.loads((HERE/'BLOCK12_GREEN_INPUT_MANIFEST.json').read_text())
    assert sha(HERE/manifest['copy'])==manifest['sha256']
    source=json.loads((HERE/manifest['copy']).read_text());rows=[r for r in source['rows'] if r['s']=='0']
    assert len(rows)==1 and rows[0]['status']=='CERTIFIED_TARGET';green=I(*rows[0]['A'])
    checks=[]
    for n in range(11):
        direct=sum(factorial(2*n)//(factorial(a)*factorial(b)*factorial(n-a-b))**2 for a in range(n+1) for b in range(n-a+1))
        assert direct==return_numerator(n)
        checks.append({'n':n,'integer_counts_equal':True})
    assert return_numerator(1)!=sum(comb(1,j)**2*comb(2*j,j) for j in range(2))
    N=256;total=F(0);weighted=F(0)
    for n in range(N+1):
        prob=F(return_numerator(n),36**n);coef=F(comb(4*n,2*n),16**n)
        total+=prob;weighted+=coef*prob
    tail_hi=6*green.hi-total;assert tail_hi>=0
    coefficient=F(comb(4*N+4,2*N+2),16**(N+1))
    invsqrt_hi=root_hi(F(1,6));invsqrt_lo=invsqrt_hi-F(1,1<<128)
    assert invsqrt_lo**2<=F(1,6)<=invsqrt_hi**2
    c0=I(weighted*invsqrt_lo,(weighted+coefficient*tail_hi)*invsqrt_hi)
    assert c0.lo>F(2,5) and c0.hi<F(8,15)
    result=certify({A0:green,C0:c0})
    result['status']='completed_fixed_green_refinement';result['refinement_source_sha256']=sha(__file__)
    result['refinement_protocol_sha256']=sha(HERE/'BLOCK12_GREEN_REFINEMENT.md')
    result['green_input_manifest']=manifest
    result['return_series']={'N':N,'P_N':str(total),'S_N':str(weighted),'return_tail_upper':str(tail_hi),
                             'coefficient_upper':str(coefficient),'C0':c0.pair(),'width':str(c0.hi-c0.lo),
                             'integer_count_checks':checks,'omitted_binomial_mutant_rejected':True}
    seconds=time.monotonic()-start;rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes=rss if sys.platform=='darwin' else rss*1024
    assert seconds<=60 and rss_bytes<=384*1024**2
    result['total_seconds']=seconds;result['total_peak_rss_bytes']=rss_bytes
    return result


if __name__=='__main__':
    def deadline(signum,frame):raise TimeoutError('fixed60secondbudget')
    signal.signal(signal.SIGALRM,deadline);signal.alarm(60)
    result=run();signal.alarm(0)
    (HERE/'BLOCK12_GREEN_REFINED_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print('C0:',[float(F(z)) for z in result['return_series']['C0']])
    for mode,r in result['results'].items():print(mode,r['status'],[float(F(z)) for z in r['alpha']], 'F=',float(F(r['F_upper'])))
    print('seconds',result['total_seconds'],'peak_rss_bytes',result['total_peak_rss_bytes'])
