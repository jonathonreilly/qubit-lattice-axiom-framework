#!/usr/bin/env python3
"""Exact counterexample to sufficiency of a selected finite weak-test family."""
from pathlib import Path
import sympy as s
import hashlib,json
def main():
    rows=[]
    def ck(n,b,**kw):
        assert bool(b),n
        rows.append(dict(name=n,passed=True,**kw))
    t=s.symbols('t',real=True);Om=s.symbols('Omega2',positive=True);q=1+t;delta=s.legendre(10,2*t-1)
    for j in range(5):
        psi=t*t*(1-t)**2*s.legendre(j,2*t-1)
        K=s.expand(q*q*s.diff(psi,t,2)+6*q*s.diff(q,t)*s.diff(psi,t)+(6*s.diff(q,t)**2+3*q*s.diff(q,t,2)+Om*q*q)*psi)
        value=s.factor(s.integrate(s.expand(delta*K),(t,0,1)))
        if j<4:ck('selected weak test blind '+str(j),value==0,degree=int(s.degree(K,t)))
        else:ck('additional reserved test detects perturbation',value!=0 and value/Om>0,exact_projection=str(value))
    point=s.expand(q*q*s.diff(delta,t,2)-2*q*s.diff(q,t)*s.diff(delta,t)+(2*s.diff(q,t)**2-q*s.diff(q,t,2)+Om*q*q)*delta)
    ck('modified force violates same-action equation',s.degree(point,t)==12 and s.Poly(point,t).LC()==Om*s.Poly(delta,t).LC())
    ck('test trajectories and function endpoints admissible',q.subs(t,0)>0 and all(s.diff(t*t*(1-t)**2,t,n).subs(t,e)==0 for n in [0,1] for e in [0,1]))
    note=Path(__file__).with_name('NETWORK_EVOLUTION_BLOCK19_v1.md')
    print(json.dumps({'summary':{'passed':len(rows),'failed':0},'checks':rows,
      'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),
      'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'empirical_validation':False,'scope':'Exact finite selected weak-test blindness witness; not a universal impossibility claim.'},indent=2,sort_keys=True))
if __name__=='__main__':main()
