#!/usr/bin/env python3
"""Symbolically derive the enlarged kernels before native scalar evaluation."""
from pathlib import Path
import hashlib,json,time
import sympy as s
from block12_clifford import A0,C0,ODD
import block12_nominal as old
from block12_separate import CLASSES,kernel,norms
HERE=Path(__file__).resolve().parent


def run():
    start=time.monotonic();p=s.symbols('p0:3',real=True);r=s.symbols('r0:3',real=True)
    q=s.symbols('q0:3',real=True);u=s.symbols('u0:3',real=True);kernels=[];total=0
    for a,c,m,count in CLASSES:
        value=kernel(a,c,m,p,r,q)
        assert s.expand(value.subs(dict(zip(q,p)))-old.kernel(a,c,m,p,r))==0
        kernels.append({'A':a,'C':c,'opposites':m,'multiplicity':count,'expression':str(value)})
        # Use simultaneous substitution: p=P outer, r=O outer, q=P inner,u=O inner.
        total+=count*value.subs(dict(zip(p,p if a=='P' else r))|dict(zip(r,p if c=='P' else r))|dict(zip(q,q if a=='P' else u)),simultaneous=True)
    old_total=sum(count*old.kernel(a,c,m,p if a=='P' else r,p if c=='P' else r) for a,c,m,count in CLASSES)
    assert s.expand(total.subs(dict(zip(q,p))|dict(zip(u,r)),simultaneous=True)-old_total)==0
    normrows={}
    for kind in ('P','O'):
        value=norms(kind,p,q)
        assert s.expand(value[1].subs(dict(zip(q,p)))-old.norm_formulas(kind,p)[1])==0
        assert all(s.Poly(v,A0,C0).total_degree()<=1 for v in value)
        normrows[kind]=[str(z) for z in value]
    return {'status':'symbolically_derived_separate_source_trial','kernels':kernels,'norms':normrows,
            'complete_nominal':str(s.factor(total)),'equal_polynomial_limit_checked':True,
            'seconds':time.monotonic()-start,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'helper_sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in ('block12_clifford.py','block12_nominal.py','block12_separate.py')},
            'scope':'proposed native algebra; finite covariance check and new interval evaluation pending'}


if __name__=='__main__':
    result=run();(HERE/'BLOCK12_SEPARATE_FORMULAS.json').write_text(json.dumps(result,indent=2)+'\n')
    print('seconds',result['seconds']);print('complete nominal:',result['complete_nominal'])
