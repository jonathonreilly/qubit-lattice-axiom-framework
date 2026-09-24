"""Exact symbolic electric coefficient and Laurent H4 on compact flat modes."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/flat_compressed_operators.py', 'scripts/flat_band_spin_correction_probe.py')
from pathlib import Path
from fractions import Fraction
from collections import defaultdict
import hashlib,importlib.util,json
import sympy as sp
D=Path(__file__).resolve().parent
p=D/'flat_band_spin_correction_probe.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='791330246ebb0f35b696edd17cead1c95fc4db9ccd43792b569c01293e375d4b'
s=importlib.util.spec_from_file_location('probe',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
x=sp.symbols('f',real=True)

def hops_poly(s):
    q,E=s
    for source,c in enumerate(q):
        if not c:continue
        for direction in [-1,1]:
            dest=(source+direction)%8
            if q[dest]:continue
            edge=source if direction==1 else dest;k=-direction*c
            qq=list(q);qq[source]=0;qq[dest]=c;EE=list(E);EE[edge]+=k
            yield (tuple(qq),tuple(EE)),sp.expand((x+E[edge])*(x+E[edge]+k))

def d2(v):
    out=defaultdict(lambda:sp.Integer(0))
    for s,coef in v.items():
        for mid,a in hops_poly(s):
            for final,b in hops_poly(mid):
                if any(final[0][j]==0 for j in [0,2,4,6]):continue
                m.add_term(out,final,coef*(a+b)/2)
    return {s:sp.expand(a) for s,a in out.items() if sp.expand(a)!=0}

def w_path(v,sequence):
    for target_w in sequence:
        out=defaultdict(Fraction)
        for s,coef in v.items():
            for final,_ in m.hops(s):
                if sum(final[0][j]==0 for j in [0,2,4,6])==target_w:
                    m.add_term(out,final,-coef)
        v=dict(out)
    return v

rows=[]
for kind,C in enumerate([(0,1),(1,2)]):
    for r in range(6):
        initial=m.state(C,r,0)
        v=m.flat({initial:Fraction(1)})
        dv=d2(v);pdp=m.flat(dv)
        electric=sp.expand(pdp[initial]/v[initial])
        residual=m.combine((1,pdp),(-electric,v))
        assert all(sp.expand(a)==0 for a in residual.values())
        h4=m.combine((1,w_path(v,[1,0,1,0])),(Fraction(-1,2),w_path(v,[1,2,1,0])))
        assert m.flat(h4)==h4
        terms=[]
        for state,a in h4.items():
            C2,r2,shift=m.labels(state)
            if C2 not in [(0,1),(1,2)]:continue
            terms.append({'kind':[(0,1),(1,2)].index(C2),'r':r2,'circulation_shift':shift,'coefficient':str(2*a)})
        rows.append({'kind':kind,'r':r,'electric_quadratic':str(electric),
                     'leading_spin_leakage_norm_squared':str(sp.expand(sum(a*a for a in m.combine((1,dv),(-1,pdp)).values())/m.norm2(v))),
                     'H4_terms':sorted(terms,key=lambda a:(a['kind'],a['r'],a['circulation_shift']))})
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rows':rows,
     'status':'author exact symbolic identities in the compact flat basis',
     'scope':'Compression and invariant H4, not yet a joint-scaling time-limit proof.'}
p=D/'FLAT_COMPRESSED_OPERATORS_RESULTS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
