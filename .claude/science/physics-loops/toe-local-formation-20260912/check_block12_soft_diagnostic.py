#!/usr/bin/env python3
"""A finite two-frequency diagnostic, explicitly NOT the native infinite alpha."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import time
import sympy as s

HERE=Path(__file__).resolve().parent


def car(n):
    out=[]
    for j in range(n):
        f=s.zeros(1<<n)
        for state in range(1<<n):
            if (state>>j)&1:
                f[state^(1<<j),state]=(-1)**((state&((1<<j)-1)).bit_count())
        out.append(f)
    return out


def run():
    start=time.monotonic();checks=[]
    def equal(name,left,right):
        diff=left-right
        if isinstance(diff,s.MatrixBase):
            assert all(s.simplify(x)==0 for x in diff),(name,diff)
        else:assert s.simplify(diff)==0,(name,diff)
        checks.append(name)
    a,b=s.symbols('a b',positive=True)
    c=s.Rational(1,3);ss=s.sqrt(2)/3
    vA=s.Matrix([c,ss,0]);vC=s.Matrix([c,-ss/2,s.sqrt(3)*ss/2])
    f=car(3);g=f[0]+f[0].T;vac=s.eye(8)[:,0]
    H=a*f[0].T*f[0]+b*(f[1].T*f[1]+f[2].T*f[2])
    def field_b(v):return sum((s.I*v[j]*(f[j].T-f[j]) for j in range(3)),s.zeros(8))
    BA=-s.I*a*g*field_b(vA);BC=-s.I*a*g*field_b(vC)
    DA=H+BA;DC=H+BC
    IA=DA.inv();IC=DC.inv()
    xA=IA*vac;xC=IC*vac
    LA=-s.I*a*field_b(vA);LC=-s.I*a*field_b(vC)
    yA=IA*LA*xA;yC=IC*LC*xC
    ustate=f[0].T*vac
    def particle(v):return sum((v[j]*f[j].T*vac for j in range(3)),s.zeros(8,1))
    expected_x=(3/a+2/b)*vac-3/b*f[0].T*particle(vA)
    expected_y=3/(2*a)*ustate+(9/(2*b)+3*a/b**2)*particle(vA)
    equal("literal_first_inverse_state",xA,expected_x)
    equal("literal_inner_inverse_source",yA,expected_y)
    kernel=(xC.conjugate().T*xA+yC.conjugate().T*g*xA+xC.conjugate().T*g*yA)[0]
    target=18/a**2+27/(a*b)+18/b**2+6*a/b**3
    equal("literal_disjoint_Ward_kernel",kernel,target)
    vacuum_kernel=(ustate.T*IC*g*IA*vac)[0]
    equal("distinct_regular_vacuum_kernel",vacuum_kernel,s.Rational(3,2)*(3/a**2+3/(a*b)+1/b**2))
    equal("even_determinant",s.det(s.Matrix([[a/3,a*ss],[a*ss,2*a/3+b]])),a*b/3)
    equal("odd_determinant",s.det(s.Matrix([[2*a/3,-a*ss],[-a*ss,a/3+b]])),2*a*b/3)

    # A separate literal fourth zero mode extracts the derivative of the vertex.
    # Pick two unequal frequencies; this is a finite exact rational CAR check.
    fq=car(4);G=fq[0]+fq[0].T;Q=fq[3]+fq[3].T;V0=s.eye(16)[:,0]
    aa=s.Rational(2);bb=s.Rational(3)
    H4=aa*fq[0].T*fq[0]+bb*(fq[1].T*fq[1]+fq[2].T*fq[2])
    def fb4(v):return sum((s.I*v[j]*(fq[j].T-fq[j]) for j in range(3)),s.zeros(16))
    dc=[];iv=[];prime=[]
    for v in (vA,vC):
        field=fb4(v);d=H4-s.I*aa*G*field
        dc.append(d);iv.append(d.inv());prime.append(-s.I*aa*Q*field)
    IA4,IC4=iv;VA,VC=prime
    derivative=IC4*Q*IA4-IC4*VC*IC4*G*IA4-IC4*G*IA4*VA*IA4
    extracted=(V0.T*fq[3]*derivative*V0)[0]
    equal("literal_soft_mode_vertex_derivative",extracted,target.subs({a:aa,b:bb}))
    equal("reference_zero_mode",H4*Q,Q*H4)
    wrong=IC4*Q*IA4  # Dropping both resolvent derivatives is a false shortcut.
    assert s.simplify((V0.T*fq[3]*wrong*V0)[0]-extracted)!=0
    checks.append("omitted_impurity_derivatives_rejected")
    return {"status":"passed","checks":checks,"count":len(checks),"seconds":time.monotonic()-start,
            "ordered_pair_soft_kernel":str(s.factor(target)),
            "complete_diagnostic_soft_scalar":str(s.factor(s.Rational(90,8)*target)),
            "scope":"finite two-frequency diagnostic only; no native alpha value or sign",
            "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "plan_sha256":hashlib.sha256((HERE/'BLOCK12_WORKING_PLAN.md').read_bytes()).hexdigest()}


if __name__=='__main__':
    result=run();(HERE/'BLOCK12_SOFT_DIAGNOSTIC_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
