#!/usr/bin/env python3
"""Post-fit exact validation of V2 central root classification, not another fit.

Rational interval arithmetic checks the sign of the reconstructed scale and
the domain/positivity inequalities on every exact Sturm isolating interval.
No new data or free parameters enter. The decimal central inputs are exact
rationals for this algebra certificate; their experimental errors are not.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from dataclasses import dataclass
from fractions import Fraction as Fr
import hashlib
import json
from math import isqrt
from pathlib import Path
import sympy as sp
from independent_v2 import exact_central_sturm

@dataclass(frozen=True)
class I:
    lo: Fr
    hi: Fr
    @staticmethod
    def cast(x): return x if isinstance(x,I) else I(Fr(x),Fr(x))
    def __add__(self,other):
        other=I.cast(other);return I(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return I(-self.hi,-self.lo)
    def __sub__(self,other): return self+-I.cast(other)
    def __rsub__(self,other): return I.cast(other)+-self
    def __mul__(self,other):
        other=I.cast(other)
        vals=[a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return I(min(vals),max(vals))
    __rmul__=__mul__
    def __truediv__(self,other):
        other=I.cast(other);assert not other.lo<=0<=other.hi
        return self*I(1/other.hi,1/other.lo)
    def __rtruediv__(self,other):return I.cast(other)/self
    def floats(self):return [float(self.lo),float(self.hi)]

def rational(q):
    assert q.is_Rational
    return Fr(int(q.p),int(q.q))

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    r=sp.Symbol('r');d=sp.sqrt(9149)
    denominator=10**20;n=isqrt(9149*denominator**2)
    di=I(Fr(n,denominator),Fr(n+1,denominator))
    assert di.lo**2<9149<di.hi**2
    w3=(1-d/100)/2;w2=sp.Rational(773,2500)*(1-w3)
    A=w2*r+w3;B=w2*r*r+w3;C=w2*r*r*r+w3
    h=B-A*A;N=C-2*A*B+A*A*A;Q=(1+r-A)*h-N;D=Q-N
    def evaluate(expr,ri):
        poly=sp.Poly(expr,r,extension=d)
        ans=I.cast(0)
        for cc in poly.all_coeffs():
            cc=sp.expand(cc);bb=cc.coeff(d);aa=sp.expand(cc-bb*d)
            ci=I.cast(rational(aa))+rational(bb)*di
            ans=ans*ri+ci
        return ans
    sturm=exact_central_sturm(-1);large=exact_central_sturm(1)
    assert sturm['exact_root_count_0_1']==2 and large['exact_root_count_0_1']==0
    checks=[];accepted=0
    for bracket in sturm['isolating_intervals']:
        ri=I(Fr(bracket['lo']),Fr(bracket['hi']))
        aa,hh,nn,dd=[evaluate(z,ri) for z in (A,h,N,D)]
        assert hh.lo>0
        diff=dd/hh;k=2*hh/dd
        record={'r_interval':ri.floats(),'a2_minus_a1_interval':diff.floats(),
                'positive_scale_interval':k.floats()}
        if k.hi<0:
            record['exact_decision']='rejected: strictly negative ordered-eigenvalue scale'
        else:
            assert k.lo>0
            ss=k*k*hh;shift=ss+2-2*nn/dd;bb=shift+k*aa
            assert ss.lo>1 and ss.hi<10 and bb.lo>1 and bb.hi<30 and shift.lo>0
            record.update({'s_interval':ss.floats(),'b_interval':bb.floats(),
                           'x1_interval':shift.floats(),
                           'infinite_positivity_margin':(bb-1).floats(),
                           'exact_decision':'accepted: strict nonnegative infinite support; inside declared domain; x1>0'})
            accepted+=1
        checks.append(record)
    assert accepted==1
    out={'status':'Exact central algebra validation; experimental errors not certified as exact constraints',
         'small_branch_exact_root_count_0_1':2,'large_branch_exact_root_count_0_1':0,
         'root_classifications':checks,'admissible_central_root_count':accepted,
         'sqrt9149_rational_bracket':[str(di.lo),str(di.hi)],
         'source_script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()
