#!/usr/bin/env python3
"""Bounded symbolic derivation of the finite source table, before any evaluation."""
from pathlib import Path
import hashlib
import json
import time
import sympy as s
from block12_clifford import Algebra,A0,C0,ODD

HERE=Path(__file__).resolve().parent


def run():
    start=time.monotonic();out={}
    for kind in ('P','O'):
        alg=Algebra(kind);vac,vc=alg.moments(False);ward,wc=alg.moments(True)
        assert vac[:3]==[1,ODD[1]/3,2]
        assert ward[0]==(72*A0 if kind=='P' else 12)
        assert s.expand(ward[1]-ward[0]*ODD[1]/3-(24*C0 if kind=='P' else 4*ODD[1]))==0
        for expr in ward:
            assert s.Poly(expr,A0,C0).total_degree()<=1
            assert s.expand(expr-s.conjugate(expr))==0
        for expr in vac:assert s.expand(expr-s.conjugate(expr))==0
        out[kind]={'vacuum':[str(s.factor(x)) for x in vac],
                   'ward':[str(s.factor(x)) for x in ward],
                   'vacuum_state_word_counts':vc,'ward_state_word_counts':wc}
    return {'status':'derived','moments':out,'seconds':time.monotonic()-start,
            'helper_sha256':hashlib.sha256((HERE/'block12_clifford.py').read_bytes()).hexdigest(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'symbolic conditional native source moments; accepted-input comparison pending'}


if __name__=='__main__':
    result=run();(HERE/'BLOCK12_MOMENT_FORMULAS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='moments'},indent=2))
    for kind,data in result['moments'].items():print(kind,data['vacuum_state_word_counts'],data['ward_state_word_counts'])
