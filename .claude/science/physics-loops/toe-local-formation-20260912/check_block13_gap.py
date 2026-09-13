#!/usr/bin/env python3
"""Exact finite inequalities in the reconstructed infinite native gap proof."""
from fractions import Fraction as F
from pathlib import Path
import json,time
from verify_block12_sign_witness import convolution,sha
from check_block13_elementary import elementary_scalars
HERE=Path(__file__).resolve().parent


def run():
    start=time.monotonic();env,_=elementary_scalars();a=F(17,60)
    assert env['A0'][1]<a
    # Polynomial division proves the elementary positive-integral pi bound.
    remainder=[F(0)]*4+[F(1),F(-4),F(6),F(-4),F(1)];quotient=[F(0)]*7
    for j in range(8,1,-1):
        quotient[j-2]=remainder[j];remainder[j-2]-=remainder[j];remainder[j]=0
    assert remainder[:2]==[-4,0] and not any(remainder[2:])
    assert sum(c/F(j+1) for j,c in enumerate(quotient))==F(22,7)
    assert 27*F(22,7)**3<1024
    assert F(177,686)>F(1,4)
    P=[F(1,9),F(0),4*a/9+8*a*a,F(0),4*a*a/9]
    assert sum(P)<1
    w=[1-P[0]]+[-v for v in P[1:]];poly=[F(1)];local=F(0)
    for n in range(1,13):
        poly=convolution(poly,w);local+=sum(c/F(j+1) for j,c in enumerate(poly))/n
    local*=F(7,44)
    tail=F(7,44)*sum(F(1,16)*(24-8/F(j,16)**2)/(F(j+1,16)**2+7)**2 for j in range(16,320))
    total=local+tail;assert total>F(1,4)
    # Removing the tail does not prove the claimed1/4 gap in this certificate.
    assert local<F(1,4)
    return {'status':'exact_gap_inequalities_passed','P_local':str(local),'P_tail':str(tail),'P_total':str(total),
            'O_lower':'177/686','A0_elementary_upper':str(env['A0'][1]),
            'omitted_positive_tail_competitor_rejected':True,'seconds':time.monotonic()-start,
            'source_sha256':sha(__file__),'derivation_sha256':sha(HERE/'BLOCK13_DERIVATION.md'),
            'scope':'finite rational inequalities; determinant, GNS convergence and core arguments are analytical proof obligations in the note'}


if __name__=='__main__':
    result=run();(HERE/'BLOCK13_GAP_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result['status'],'P=',float(F(result['P_total'])),'O=',float(F(result['O_lower'])),'A0_upper=',float(F(result['A0_elementary_upper'])))
