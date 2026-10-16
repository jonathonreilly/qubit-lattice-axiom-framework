#!/usr/bin/env python3
"""Synthetic checks of conditional intervention/readout invariants."""
import json,math,hashlib
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import quad

def polynomial(u,y):
    return (u[0]-u[3])*(u[1]-u[2])*(y[0]-y[2])*(y[1]-y[3])-(u[0]-u[2])*(u[1]-u[3])*(y[0]-y[3])*(y[1]-y[2])

def certificate(u,v,eps):
    def term(i,j,k,l):
        e=eps[i]+eps[j];f=eps[k]+eps[l]
        return e*abs(v[k]-v[l])+f*abs(v[i]-v[j])+e*f
    return abs((u[0]-u[3])*(u[1]-u[2]))*term(0,2,1,3)+abs((u[0]-u[2])*(u[1]-u[3]))*term(0,3,1,2)

def main():
    rows=[]
    def check(name,condition,**kw):
        assert bool(condition),name
        rows.append(dict(name=name,passed=True,**kw))
    A,D,C,E=sp.symbols('A D C E');us=sp.symbols('u1:5')
    ys=[(A+D*u)/(C+E*u) for u in us]
    check('fractional-linear four-setting identity',sp.factor(polynomial(us,ys))==0)
    u=sp.symbols('u');a,b,G,B,J,H,g0=sp.symbols('a b G B J H g0')
    expression=B+G*(g0-(a+b*u)*H/(1+(a+b*u)*J))
    numerator,denominator=sp.fraction(sp.cancel(expression))
    check('unknown common instrument and affine calibration preserve degree',sp.degree(numerator,u)<=1 and sp.degree(denominator,u)<=1)
    setting=list(map(sp.Integer,[0,1,2,3]));under=lambda x:(2+3*x)/(1+5*x)
    curved=[under(x*x) for x in setting];projective=[under((2+3*x)/(4+x)) for x in setting]
    check('nonlinear calibration failure and projective ambiguity',polynomial(setting,curved)!=0 and polynomial(setting,projective)==0,curved_residual=str(polynomial(setting,curved)))
    physical=[1+x*x for x in setting];desired=[under(x) for x in setting];gain=[desired[i]/physical[i] for i in range(4)]
    check('varying gain can manufacture agreement',polynomial(setting,physical)!=0 and polynomial(setting,[physical[i]*gain[i] for i in range(4)])==0)
    rng=np.random.default_rng(7615);ratios=[];st=np.array([-.2,.3,1.1,2.0])
    exact=(1+2j+(3-.4j)*st)/(2+(1+.2j)*st)
    for _ in range(3000):
        errors=.01*(rng.normal(size=4)+1j*rng.normal(size=4))+.03*(rng.normal()+1j*rng.normal())
        measured=exact+errors;bound=certificate(st,measured,np.abs(errors));value=abs(polynomial(st,measured))
        assert value<=bound+1e-12,'instrument error certificate'
        ratios.append(value/bound)
    check('correlated complex errors',len(ratios)==3000,maximum_fraction=round(max(ratios),12))
    t,k,q0,v0,f=sp.symbols('t k q0 v0 f',positive=True,real=True)
    homogeneous=q0*sp.cos(sp.sqrt(k)*t)+v0/sp.sqrt(k)*sp.sin(sp.sqrt(k)*t)
    forced=f*(1-sp.cos(sp.sqrt(k)*t))/k
    plus=homogeneous+forced;minus=homogeneous-forced
    check('opposite forcing cancels unknown preparation',sp.simplify(sp.diff(plus,t,2)+k*plus-f)==0 and sp.simplify(sp.diff(minus,t,2)+k*minus+f)==0 and sp.simplify((plus-minus)/2-forced)==0)
    ratios=[]
    for _ in range(500):
        mat=rng.normal(size=(3,3));K=mat.T@mat+np.eye(3);q=rng.normal(size=3);v=rng.normal(size=3);c=rng.normal(size=3);time=rng.uniform(0,10)
        energy=.5*(v@v+q@K@q);vals,V=np.linalg.eigh(K);qt=V@(np.cos(np.sqrt(vals)*time)*(V.T@q)+np.sin(np.sqrt(vals)*time)/np.sqrt(vals)*(V.T@v))
        bound=math.sqrt(energy*(c@np.linalg.solve(K,c))/2);value=abs(c@qt)/2
        assert value<=bound+1e-12,'preparation-energy bound'
        ratios.append(value/bound)
    check('uniform preparation mismatch bound',len(ratios)==500,maximum_fraction=round(max(ratios),12))
    s=sp.symbols('s',nonnegative=True);count=0
    for d in range(4):
        for r in range(5):
            n=4*d+3
            leading=sp.integrate((t-s)**n*s**r,(s,0,t))/(sp.factorial(n)*sp.factorial(r))
            assert sp.simplify(leading-t**(n+r+1)/sp.factorial(n+r+1))==0,'finite-pulse leading term'
            tail=sp.integrate((t-s)**(n+2)*s**r,(s,0,t))/(sp.factorial(n+2)*sp.factorial(r))
            assert sp.simplify(tail-t**(n+r+3)/sp.factorial(n+r+3))==0,'finite-pulse remainder factor'
            count+=1
    check('finite pulse beta-integral coefficients',count==20,cases=count)
    K=np.array([[4,-1,0],[-1,5,-1],[0,-1,6]],float);w=np.array([0,1,-1]);theta=.7;changed=K+theta*np.outer(w,w);M=max(np.linalg.norm(K,2),np.linalg.norm(changed,2));d=1;rows_p=[]
    def impulse(mat,time):
        vals,V=np.linalg.eigh(mat);return np.sum(V[0,:]**2*np.sin(np.sqrt(vals)*time)/np.sqrt(vals))
    for r in range(4):
        for time in [.2,.8,2.0]:
            value=quad(lambda tau:(impulse(K,time-tau)-impulse(changed,time-tau))*tau**r/math.factorial(r),0,time,epsabs=1e-13)[0]
            lead=theta*time**(4*d+r+4)/math.factorial(4*d+r+4)
            bound=2*M**(2*d+2)*time**(4*d+r+6)/math.factorial(4*d+r+6)*math.cosh(math.sqrt(M)*time)
            assert abs(value-lead)<=bound+1e-13,'finite-pulse spectral remainder'
            rows_p.append(abs(value-lead)/bound)
    check('finite pulse spectral remainder',len(rows_p)==12,maximum_fraction=round(max(rows_p),12))
    note=Path(__file__).with_name('NETWORK_EVOLUTION_BLOCK11_v1.md')
    print(json.dumps({'summary':{'passed':len(rows),'failed':0},'checks':rows,'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'data_status':'Synthetic development controls only; no new observations.'},indent=2,sort_keys=True))
if __name__=='__main__':main()
