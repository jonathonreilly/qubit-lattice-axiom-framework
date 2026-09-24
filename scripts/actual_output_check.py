"""Checks of actual-output clock bounds and finite electric-window statistics."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/actual_output_check.py', 'scripts/finite_spin_dynamics_check.py')
from pathlib import Path
from collections import defaultdict
import importlib.util,hashlib,json,math
import numpy as np
import sympy as sp
D=Path(__file__).resolve().parent
p=D/'finite_spin_dynamics_check.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='90186b1c250d1978003dbb121e43c3b6486830f54b44cab4f8c4fafd2b2be945'
spec=importlib.util.spec_from_file_location('spin',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def hops(q,E,S):
    C=S*(S+1)
    for e in range(8):
        j=(e+1)%8
        for origin,dest,direction in ((e,j,1),(j,e,-1)):
            if q[origin] and not q[dest]:
                k=-direction*q[origin]
                if abs(E[e]+k)>S:continue
                coefficient=-math.sqrt(max(0.,1-E[e]*(E[e]+k)/C))
                qq=list(q);qq[origin]=0;qq[dest]=q[origin]
                EE=list(E);EE[e]+=k
                yield tuple(qq),tuple(EE),coefficient

def first_counts(S):
    q0=tuple(int(i%2==0) for i in range(8));E0=(0,)*8
    one=list(hops(q0,E0,S));two=defaultdict(float)
    for q,E,c in one:
        for qq,EE,d in hops(q,E,S):
            if sum(qq[x]==0 for x in (0,2,4,6))==2:two[qq,EE]+=c*d
    M=sum(c*c for q,E,c in one);Z2=sum(c*c for c in two.values())
    marks=[]
    for e in range(8):
        j=(e+1)%8;bycharge=[]
        for sigma in (-1,1):
            image=defaultdict(float)
            for q,E,c in one:
                if q[e] or q[j] or abs(E[e]+sigma)>S:continue
                qq=list(q);qq[e]=sigma;qq[j]=-sigma
                if any(qq[x]==0 for x in (0,2,4,6)):continue
                EE=list(E);EE[e]+=sigma
                g=math.sqrt(max(0.,1-E[e]*(E[e]+sigma)/(S*(S+1))))
                image[tuple(qq),tuple(EE)]-=c*g
            norm=sum(c*c for c in image.values())
            assert norm==1
            bycharge.append(image)
        coherent=defaultdict(float)
        for image in bycharge:
            for s,c in image.items():coherent[s]+=c
        assert sum(c*c for c in coherent.values())==2
        marks.append({'edge':e,'resolved_grams':[1,1],'coherent_gram':2})
    assert len(one)==8 and len(two)==20 and M==8 and Z2==80
    return {'S':S,'one_hop_paths':len(one),'distinct_grade2_outputs':len(two),
            'A_dagger_A':M,'Z_dagger_Z':Z2,'H2':-M,'H4':M*M-Z2/2,
            'first_marks':marks}

first=[first_counts(S) for S in (1,2,4,8)]
loss=[]
for S in (1,2,4,8):
    words,H,G=m.finite_target(S)
    diagonal=G.diagonal().real;off=G-m.diags(G.diagonal(),format='csr')
    assert not off.nnz or max(abs(off.data))<1e-13
    assert min(diagonal)>=-1e-13 and max(diagonal)<=4+1e-13
    loss.append({'S':S,'P_dimension':len(words),'minimum_loss_without_kappa':float(min(diagonal)),
                 'maximum_loss_without_kappa':float(max(diagonal)),
                 'off_diagonal_nonzero_entries':off.nnz})

k,t,s=sp.symbols('k t s',positive=True)
conv=sp.integrate(16*k*sp.exp(-16*k*s)*(1-sp.exp(-4*k*(t-s)))/2,(s,0,t))
bound=sp.Rational(1,2)-sp.Rational(2,3)*sp.exp(-4*k*t)+sp.Rational(1,6)*sp.exp(-16*k*t)
assert sp.simplify(conv-bound)==0

# Historical high-spin saved-vector replay is deferred on the original branch.
out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'first_sector_exact_weight_controls':first,'complete_finite_spin_loss_controls':loss,
     'symbolic_two_birth_lower_bound':str(bound),
     'scope':'Fresh exact path/loss/convolution controls only; historical saved-vector diagnostics are not replayed by this control.'}
p=D/'ACTUAL_OUTPUT_CONTROLS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
