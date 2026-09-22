"""Finite-circuit block gauge test when H2 is not scalar."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
import sys
import sympy as s

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
assert sha256((HERE/'finite_spin_check.py').read_bytes()).hexdigest()=='3b4e969e07835ba6d87c95d0736a520a2c3854ebca61ac9d5a3f4f7763de2bb6'
import finite_spin_check as own


def conjugate(series,G,power,order):
    out=[x.copy() for x in series]
    for degree,a in enumerate(series):
        term=a
        for k in range(1,(order-degree)//power+1):
            term=(G*term-term*G)/k
            if not any(term):break
            out[degree+k*power]+=term
    return out


def run(S):
    m=own.square(S);dim=len(m['states']);zero=s.zeros(dim);order=4
    N=s.diag(*m['nb']);pieces=[]
    for site in (1,3):
        series=[zero.copy() for _ in range(order+1)]
        series[0]=s.diag(*[int(q[site]!=0) for q,e in m['states']]);pieces.append(series)
    for h in m['hops']:
        series=[zero.copy() for _ in range(order+1)];series[1]=-h;pieces.append(series)
    gate_counts=[]
    for power in range(1,order+1):
        frozen=[]
        for series in pieces:
            a=series[power];G=zero.copy()
            for i in range(dim):
                for j in range(dim):
                    gap=N[i,i]-N[j,j]
                    if gap:G[i,j]=a[i,j]/gap
            assert G.T==-G
            if any(G):frozen.append(G)
        for G in frozen:pieces=[conjugate(x,G,power,order) for x in pieces]
        gate_counts.append(len(frozen))
    normal=[sum((p[k] for p in pieces),zero.copy()).applyfunc(s.simplify) for k in range(order+1)]
    for k,a in enumerate(normal):
        assert N*a==a*N
        if k%2:assert a==zero
    P=m['low'];inv=s.diag(*[s.Rational(1,x) if x else 0 for x in m['nb']]);T=m['h']
    h2=-(T*inv*T).extract(P,P);metric=(T*inv*inv*T).extract(P,P)
    h4=-(T*inv*T*inv*T*inv*T).extract(P,P)-(metric*h2+h2*metric)/2
    assert normal[2].extract(P,P)==h2
    assert s.simplify(normal[4].extract(P,P)-h4)==s.zeros(len(P))
    assert len(set(h2.diagonal()))>1
    return {'S':S,'dimension':dim,'gate_counts':gate_counts,'second_order_block_is_nonconstant':True,
            'circuit_and_normalized_fourth_order_blocks_identical':True,
            'H4':own.strings(h4)}


if __name__=='__main__':
    result={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','cases':[run(S) for S in (1,2)],
            'scope':'Exact independently assembled square circuits through order four. The general identification is the report argument, not this enumeration.'}
    (HERE/'CIRCUIT_GAUGE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
