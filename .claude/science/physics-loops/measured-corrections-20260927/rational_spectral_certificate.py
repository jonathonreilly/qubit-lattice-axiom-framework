"""Exact rational inertia certificates for the finite closed square spectrum.

Floating eigenvalues propose brackets only; every accepted endpoint uses exact
Fraction arithmetic and positive eliminated-block checks. No empirical claim.
"""
from fractions import Fraction as F
from pathlib import Path
import json,time

def count_below(S,K,delta,E):
    C=S*(S+1);x=delta/(K*C);lam=x*x*E/delta
    if not (lam<1 and (1-lam)*(2-lam)-4*x>0):
        raise ValueError('Positive Q-block condition not established')
    scalar=E*(1+4*x-lam)
    def d(n):return 1-F(n*(n+1),C)
    def r(dn):return (1-lam)*(2-lam)-4*x*dn
    pivot=None;negative=0
    for n in range(-S,S+1):
        a=d(n-1);b=d(n)
        diagonal=4*K*n*n-4*delta*(a*a/r(a)+b*b/r(b))-scalar
        if pivot is not None:
            off=-4*delta*a*a/r(a)
            diagonal-=off*off/pivot
        if diagonal==0:raise ArithmeticError('Zero LDL pivot; choose another rational endpoint')
        pivot=diagonal;negative+=pivot<0
    return negative

def certify(S,K,delta,proposals,radius=F(1,10**9)):
    intervals=[]
    for j,p in enumerate(proposals):
        center=F(str(p));lo=center-radius;hi=center+radius
        lc=count_below(S,K,delta,lo);hc=count_below(S,K,delta,hi)
        if (lc,hc)!=(j,j+1):raise ValueError(('Bracket lacks specified eigenvalue',S,j,lc,hc))
        intervals.append((lo,hi))
    return dict(S=S,K=str(K),delta=str(delta),energy_intervals=[[str(a),str(b)] for a,b in intervals],
                gap_intervals=[[str(a-intervals[0][1]),str(b-intervals[0][0])] for a,b in intervals[1:]],
                endpoint_inertia_counts=[[j,j+1] for j in range(len(intervals))],
                maximum_energy_width=str(2*radius),maximum_gap_width=str(4*radius))

if __name__=='__main__':
    start=time.monotonic();pack=Path(__file__).parent
    proposals=[json.loads(s) for s in (pack/'exact_schur_square.jsonl').read_text().splitlines()]
    for r in proposals:
        if r['S'] not in (20,50,120):continue
        out=certify(r['S'],F(1),F(str(r['delta_over_K'])),r['energies'])
        out['elapsed_sec']=time.monotonic()-start
        print(json.dumps(out),flush=True)
