#!/usr/bin/env python3
"""Resolve tiny Gaussian projection tails, without a Fock evolution cutoff."""
from pathlib import Path
import json
import mpmath as mp
import sympy as s
HERE=Path(__file__).resolve().parent

def main():
    mu,z=s.symbols('mu z',positive=True);r2=mu/(1+mu)
    g=s.sqrt((1-r2)/(1-r2*z*z));d=g;mom=[s.Integer(1)]
    for n in range(1,5):
        d=z*s.diff(d,z);mom.append(s.simplify(d.subs(z,1)))
    assert mom==[1,mu,3*mu**2+2*mu,15*mu**3+18*mu**2+4*mu,105*mu**4+180*mu**3+84*mu**2+8*mu]
    mp.mp.dps=90;rows=[]
    for K in [2,4,8,16,32,64]:
        eps=mp.power(K,-mp.mpf(1)/6);w=mp.sqrt(2);rt=(1-w)/(1+w);rz=(1-eps*eps)/(1+eps*eps)
        a=(rt+rz)/2;b=(rz-rt)/2;c=[[mp.mpf(0) for _ in range(K+1)] for _ in range(K+1)]
        c[0][0]=mp.root((1-rt*rt)*(1-rz*rz),4)
        for m in range(2,K+1,2):c[0][m]=a*mp.sqrt(mp.mpf(m-1)/m)*c[0][m-2]
        for n in range(1,K+1):
            for m in range(K+1):
                c[n][m]=((a*mp.sqrt(n-1)*c[n-2][m] if n>=2 else 0)+(b*mp.sqrt(m)*c[n-1][m-1] if m else 0))/mp.sqrt(n)
        norm2=mp.fsum(x*x for row in c for x in row);tail2=1-norm2
        assert tail2>0
        assert max(abs(c[n][m]-c[m][n]) for n in range(K+1) for m in range(K+1))<mp.mpf('1e-80')
        rows.append(dict(K=K,precision_decimal_digits=mp.mp.dps,projection_tail_squared=mp.nstr(tail2,60),projection_tail_norm=mp.nstr(mp.sqrt(tail2),60)))
    result=dict(squeezed_number_moments_exact=[str(x) for x in mom],tail_rows=rows,
      scope='Supplement to float controls: tiny-tail zeros or 1e-8 norms from subtraction near one in the first log are roundoff, not assertions of exact zero tail.')
    (HERE/'PRECISION_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
