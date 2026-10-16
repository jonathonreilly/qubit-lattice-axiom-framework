#!/usr/bin/env python3
"""Explicit finite positive response family; no empirical scale inference."""
import json,hashlib
from pathlib import Path
import sympy as s
def main():
    checks=[]
    def ck(name,condition,**kw):
        assert bool(condition),name
        checks.append(dict(name=name,passed=True,**kw))
    z,lam,u,G=s.symbols('z lambda u G',positive=True,real=True)
    M=s.Matrix([[2,1],[1,3]]);K=s.Matrix([[4,-1],[-1,5]]);w=s.Matrix([1,-1]);b=s.Matrix([1,0]);c=s.Matrix([0,1]);A=z*z*M+K+(1+2*u)*w*w.T
    normal=G*(c.T*A.inv()*b)[0];scaled=lam*G*(c.T*(lam*A).inv()*b)[0]
    ck('entire frequency and command response preserved',s.simplify(normal-scaled)==0)
    ck('positive matrices and calibration scaling',all(M[:i,:i].det()>0 and K[:i,:i].det()>0 for i in [1,2]) and s.simplify((lam*M).inv()*(lam*K)-M.inv()*K)==s.zeros(2))
    ck('known gain distinguishes family',s.simplify(normal/lam-normal)!=0 and s.simplify(normal.subs({z:1,u:1,G:1}))!=0)
    F,m,k,t=s.symbols('F m k t',positive=True,real=True)
    q=F*(1-s.cos(s.sqrt(k/m)*t))/k
    ck('constant-force solution and initial state',s.simplify(m*s.diff(q,t,2)+k*q-F)==0 and q.subs(t,0)==0 and s.diff(q,t).subs(t,0)==0)
    qs=q.subs({m:lam*m,k:lam*k},simultaneous=True)
    ck('physical work changes as response gain compensates',s.simplify(lam*G*qs-G*q)==0 and s.simplify(F*qs-F*q/lam)==0)
    energy=(m*s.diff(q,t)**2+k*q*q)/2
    ck('delivered work equals stored mechanical energy',s.simplify(energy-F*q)==0)
    note=Path(__file__).with_name('NETWORK_EVOLUTION_BLOCK13_v1.md')
    print(json.dumps({'summary':{'passed':len(checks),'failed':0},'checks':checks,'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'empirical_validation':False,'scope':'Explicit indistinguishable response family under unknown common gain and affine intervention scale; calibrated energy/force/readout routes remain open.'},indent=2,sort_keys=True))
if __name__=='__main__':main()
