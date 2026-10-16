#!/usr/bin/env python3
"""Division-free necessary adaptive-response identity; synthetic controls."""
from pathlib import Path
import sympy as s
import numpy as np
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss
import json,hashlib

def main():
    rows=[]
    def ck(n,b,**kw):
        assert bool(b),n
        rows.append(dict(name=n,passed=True,**kw))
    t=s.symbols('t',real=True);q=s.Function('q')(t);w=s.Function('w')(t);psi=s.Function('psi')(t)
    g,G,Om=s.symbols('g G Omega2',nonzero=True);R=g*q*w
    L=lambda r:q*q*s.diff(r,t,2)-2*q*s.diff(q,t)*s.diff(r,t)+(2*s.diff(q,t)**2-q*s.diff(q,t,2))*r
    ck('polynomial elimination has no coordinate division',s.expand(L(R)-g*q**3*s.diff(w,t,2))==0)
    A=q*q*s.diff(psi,t,2)+6*q*s.diff(q,t)*s.diff(psi,t)+(6*s.diff(q,t)**2+3*q*s.diff(q,t,2))*psi
    adj=s.diff(q*q*psi,t,2)+s.diff(2*q*s.diff(q,t)*psi,t)+(2*s.diff(q,t)**2-q*s.diff(q,t,2))*psi
    ck('weak adjoint coefficients',s.expand(A-adj)==0)
    ck('linear stiffness derivative part vanishes',s.expand(L(q))==0)
    ck('hidden forcing closes polynomial identity',s.expand((L(R)+Om*q*q*R+G*q**5/2).subs(s.diff(w,t,2),-Om*w-G*q*q/(2*g)))==0)
    mn,kn,tn,Cn,gn,ln=1.2,1.1,.9,2.3,.8,.11;on=Cn/tn;Gn=gn*gn/tn
    truth=np.array([-on,mn,mn*on,kn*on,4*ln,4*ln*on-Gn/2])
    nodes,weights=leggauss(160);xx=s.symbols('x');psis=[]
    for j in range(4):
        poly=xx**2*(1-xx)**2*s.legendre(j,2*xx-1)
        psis.append([s.lambdify(xx,s.diff(poly,xx,d),'numpy') for d in [0,1,2]])
    specs=[(.7,.1,.4,-.3),(.9,.5,-.7,.2),(1.1,-.4,.9,.1),(1.4,.7,-1.1,.6)]
    matrices=[];targets=[];max_residual=0.;sign_ranges=[]
    for freq,phase,w0,v0 in specs:
        qexpr=s.sin(freq*t+phase)+.2*s.cos(1.7*freq*t)
        funcs=[s.lambdify(t,s.diff(qexpr,t,d),'numpy') for d in [0,1,2]]
        def rhs(tt,y):return [y[1],(-Cn*y[0]-.5*gn*funcs[0](tt)**2)/tn]
        sol=solve_ivp(rhs,[0,8],[w0,v0],rtol=2e-12,atol=2e-14,dense_output=True);assert sol.success
        sample=funcs[0](np.linspace(0,8,501));sign_ranges.append([float(sample.min()),float(sample.max())])
        X=[];Y=[]
        for start,end in [(0,2),(2,4),(4,6),(6,8)]:
            length=end-start;x=(nodes+1)/2;tt=start+length*x;weights_t=weights*length/2
            qq,qd,qdd=[f(tt) for f in funcs];force=mn*qdd+kn*qq+4*ln*qq**3+gn*sol.sol(tt)[0]*qq
            integral=lambda v:float(weights_t@v)
            for f0,f1,f2 in psis:
                pp=f0(x);p1=f1(x)/length;p2=f2(x)/length**2
                aa=qq**2*p2+6*qq*qd*p1+(6*qd**2+3*qq*qdd)*pp;bb=qq**2*pp
                row=[integral(force*bb),integral(qdd*aa),integral(qdd*bb),integral(qq**3*pp),integral(qq**3*aa),integral(qq**5*pp)]
                yy=integral(force*aa);X.append(row);Y.append(yy)
                max_residual=max(max_residual,abs(yy-np.array(row)@truth))
        matrices.append(np.array(X));targets.append(np.array(Y))
    ck('signed histories cross zero',all(lo<0<hi for lo,hi in sign_ranges),sample_ranges=sign_ranges)
    ck('arbitrary-preparation weak identity through zeros',max_residual<1e-9,maximum_residual=max_residual)
    X=np.vstack(matrices[:3]);y=np.concatenate(targets[:3]);scales=np.linalg.norm(X,axis=0)
    scaled,_,rank,sv=np.linalg.lstsq(X/scales,y,rcond=None);fit=scaled/scales;err=float(np.max(np.abs(fit-truth)))
    ck('common coefficients from signed synthetic development histories',rank==6 and err<1e-7,rank=int(rank),maximum_error=err,scaled_condition=float(sv[0]/sv[-1]))
    test=float(np.max(np.abs(targets[3]-matrices[3]@fit)))
    ck('additional signed synthetic history without refit',test<1e-9,maximum_residual=test)
    ck('identically zero path is blind',s.simplify(A.subs(q,0).doit())==0)
    # A sharp force-only error bound for fixed exact trajectory/test function.
    xxn=(nodes+1)/2;qq=xxn-.5;qd=np.ones_like(qq);qdd=np.zeros_like(qq)
    pp=psis[0][0](xxn);p1=psis[0][1](xxn);p2=psis[0][2](xxn)
    kernel=qq**2*p2+6*qq*qd*p1+(6*qd**2+3*qq*qdd+on*qq**2)*pp
    eps=.003;error=float((weights/2)@(eps*np.sign(kernel)*kernel));bound=float(eps*((weights/2)@np.abs(kernel)))
    ck('force-only deterministic certificate',abs(error-bound)<1e-15,bound=bound)
    note=Path(__file__).with_name('NETWORK_EVOLUTION_BLOCK18_v1.md')
    print(json.dumps({'summary':{'passed':len(rows),'failed':0},'checks':rows,'fit':fit.tolist(),
      'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),
      'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'empirical_validation':False,'scope':'Necessary division-free weak response of the chosen adaptive action; zero-path blindness and physical calibration limits explicit.'},indent=2,sort_keys=True))
if __name__=='__main__':main()
