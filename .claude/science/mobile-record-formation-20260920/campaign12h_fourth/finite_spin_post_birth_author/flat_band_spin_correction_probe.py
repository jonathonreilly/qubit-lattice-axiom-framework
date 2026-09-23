"""Author exact core expansion and compact flat-projector controls.

No finite spin, field or time cutoff is used for the rational D2 calculation.
Finite-S normalized hopping is only evaluated on declared finite supports.
"""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import itertools
import json
import math


def state(C,r,f):
    occupied=sorted([0,2,4,6]+[2*b+1 for b in C])
    q=tuple(0 if a not in occupied else -1 if a==occupied[r] else 1 for a in range(8))
    E=[];last=f
    for a in range(8):
        last+=q[a]-int(a%2==0)
        E.append(last)
    assert E[-1]==f
    return q,tuple(E)


def valid(s):
    q,E=s
    return all(E[a]-E[(a-1)%8]+int(a%2==0)==q[a] for a in range(8))


def labels(s):
    q,E=s
    C=tuple(j for j in range(4) if q[2*j+1])
    sequence=[x for x in q if x]
    return C,sequence.index(-1),E[-1]


def add_term(out,s,value):
    out[s]+=value
    if out[s]==0:del out[s]


def flat(v):
    out=defaultdict(Fraction)
    for s,a in v.items():
        C,r,f=labels(s)
        if C in [(0,2),(1,3)]:continue
        if C==(0,1):
            partner=state((2,3),(r-1)%6,f+(-1 if r==0 else 1))
        elif C==(2,3):
            old_r=(r+1)%6
            partner=state((0,1),old_r,f-(-1 if old_r==0 else 1))
        elif C==(1,2):partner=state((0,3),r,f)
        elif C==(0,3):partner=state((1,2),r,f)
        else:raise AssertionError(C)
        add_term(out,s,a/2)
        add_term(out,partner,-a/2)
    return dict(out)


def hops(s):
    q,E=s
    for source,c in enumerate(q):
        if not c:continue
        for direction in [-1,1]:
            dest=(source+direction)%8
            if q[dest]:continue
            edge=source if direction==1 else dest
            k=-direction*c
            qq=list(q);qq[source]=0;qq[dest]=c
            EE=list(E);EE[edge]+=k
            out=(tuple(qq),tuple(EE))
            assert valid(out)
            yield out,E[edge]*(E[edge]+k)


def action(v,which,S=None):
    out=defaultdict(Fraction if which!='finite_spin' else float)
    Cspin=S*(S+1) if S is not None else None
    for s,coef in v.items():
        for mid,a in hops(s):
            for final,b in hops(mid):
                if any(final[0][a]==0 for a in [0,2,4,6]):continue
                if which=='rotor':weight=-1
                elif which=='correction':weight=Fraction(a+b,2)
                elif which=='finite_spin':
                    if any(abs(e)>S for q,E in [s,mid,final] for e in E):continue
                    weight=-math.sqrt(1-a/Cspin)*math.sqrt(1-b/Cspin)
                else:raise ValueError(which)
                add_term(out,final,coef*weight)
    return dict(out)


def combine(*terms):
    out=defaultdict(Fraction)
    for scalar,v in terms:
        for s,a in v.items():add_term(out,s,scalar*a)
    return dict(out)


def norm2(v):return sum(a*a for a in v.values())


def main():
    rows=[]
    for C,r,f in itertools.product([(0,1),(1,2)],range(6),[-2,0,3]):
        v=flat({state(C,r,f):Fraction(1)})
        assert norm2(v)==Fraction(1,2)
        assert flat(v)==v
        fast=action(v,'rotor')
        assert not combine((1,fast),(4,v)), (C,r,f)
        slow=action(v,'correction')
        leak=combine((1,slow),(-1,flat(slow)))
        rows.append({'C':list(C),'minus_word_index':r,'initial_circulation':f,
                     'flat_vector_norm_squared':str(norm2(v)),
                     'D2_norm_squared':str(norm2(slow)),
                     'D2_leakage_norm_squared':str(norm2(leak)),
                     'flat_compressed_expectation':str(sum(a*slow.get(s,0) for s,a in v.items())/norm2(v))})
    s0=state((0,3),1,0)
    v=flat({s0:Fraction(1)})
    d2=action(v,'correction');rotor=action(v,'rotor')
    finite=[]
    for S in [8,16,32,64,128]:
        spin=action(v,'finite_spin',S)
        residual=combine((S*(S+1),spin),(-S*(S+1),rotor),(-1,d2))
        finite.append({'S':S,'core_expansion_residual_norm':math.sqrt(float(norm2(residual)))})
    out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'status':'author exploratory exact-rational flat-projector and leading spin correction controls',
         'exact_rows':rows,'finite_spin_core_expansion':finite,
         'invariant_under_D2_on_tested_vectors':all(r['D2_leakage_norm_squared']=='0' for r in rows),
         'scope':'Finite-support core identities do not establish uniform ordinary-time convergence or an invariant finite-spin band.'}
    p=Path(__file__).with_name('FLAT_BAND_SPIN_CORRECTION_RESULTS.json')
    assert not p.exists()
    p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
