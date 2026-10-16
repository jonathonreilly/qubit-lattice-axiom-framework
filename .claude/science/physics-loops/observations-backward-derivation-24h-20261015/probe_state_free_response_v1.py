#!/usr/bin/env python3
"""Conditional adaptive response identity; all numerical data are synthetic."""
from pathlib import Path
import hashlib,json
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp
from numpy.polynomial.legendre import leggauss

def main():
    checks=[]
    def ck(name,ok,**kw):
        assert bool(ok),name
        checks.append(dict(name=name,passed=True,**kw))
    t=s.symbols('t',real=True)
    m,k,Om,G,lam,g=s.symbols('m k Omega2 G lambda4 g',positive=True)
    a=s.Function('a')(t);b=s.Function('b')(t);w=s.Function('w')(t)
    z=m*a+k+4*lam*b+g*w
    target=-Om*z+m*s.diff(a,t,2)+m*Om*a+k*Om+4*lam*s.diff(b,t,2)+(4*lam*Om-G/2)*b
    residual=s.expand(s.diff(z,t,2)-target)
    ck('elimination for arbitrary hidden solution',
       s.expand(residual.subs(s.diff(w,t,2),-Om*w-G*b/(2*g)))==0)
    cz=-Om;ca2=m;ca=m*Om;cb2=4*lam;cb=4*lam*Om-G/2
    ck('shared coefficient restrictions and stability equivalence',
       s.expand(ca+cz*ca2)==0 and s.expand(cb/(4*Om)-(lam-G/(8*Om)))==0)
    # Chosen, declared parameters; no observation is used for this selection.
    mn,kn,tn,Cn,gn,ln=1.2,1.1,.9,2.3,.8,.11
    on=Cn/tn;Gn=gn*gn/tn
    truth=np.array([-on,mn,mn*on,kn*on,4*ln,4*ln*on-Gn/2])
    nodes,weights=leggauss(160)
    xx=s.symbols('x',real=True)
    psis=[]
    for j in range(4):
        poly=xx**2*(1-xx)**2*s.legendre(j,2*xx-1)
        ck('clamped test endpoints '+str(j),all(s.diff(poly,xx,n).subs(xx,e)==0 for n in [0,1] for e in [0,1]))
        psis.append((s.lambdify(xx,poly,'numpy'),s.lambdify(xx,s.diff(poly,xx,2),'numpy')))
    # Split fixed before generating data; two additional shapes are withheld
    # from numerical coefficient estimation, but are still synthetic controls.
    specs=[(.65,.1,.4,-.3),(.9,.5,-.7,.2),(1.15,-.4,.9,.1),
           (1.3,.7,-1.1,.6),(1.6,-.2,.2,-.8)]
    all_rows=[];all_y=[];max_truth_residual=0.;minimum_q=10.
    for index,(freq,phase,w0,v0) in enumerate(specs):
        qexpr=1.3+.25*s.sin(freq*t+phase)+.17*s.cos(1.7*freq*t)+.07*s.sin(2.9*freq*t)
        qfun=s.lambdify(t,qexpr,'numpy');qdd=s.lambdify(t,s.diff(qexpr,t,2),'numpy')
        def rhs(time,y):return [y[1],(-Cn*y[0]-.5*gn*qfun(time)**2)/tn]
        sol=solve_ivp(rhs,[0,6],[w0,v0],rtol=2e-12,atol=2e-14,dense_output=True)
        assert sol.success
        rows=[];ys=[]
        for start,end in [(0,2),(2,4),(4,6)]:
            length=end-start;x=(nodes+1)/2;tt=start+length*x;ww=weights*length/2
            q=qfun(tt);acc=qdd(tt);hidden=sol.sol(tt)[0]
            force=mn*acc+kn*q+4*ln*q**3+gn*hidden*q
            zz=force/q;aa=acc/q;bb=q*q
            minimum_q=min(minimum_q,float(q.min()))
            for fun,fun2 in psis:
                psi=fun(x);psi2=fun2(x)/length**2
                integ=lambda y:float(ww@y)
                row=[integ(zz*psi),integ(aa*psi2),integ(aa*psi),
                     integ(psi),integ(bb*psi2),integ(bb*psi)]
                yy=integ(zz*psi2)
                rows.append(row);ys.append(yy)
                max_truth_residual=max(max_truth_residual,abs(yy-np.array(row)@truth))
        all_rows.append(np.array(rows));all_y.append(np.array(ys))
    ck('all histories with unrelated hidden preparations obey weak identity',
       max_truth_residual<1e-10 and minimum_q>.8,maximum_residual=max_truth_residual,minimum_sampled_q=minimum_q)
    X=np.vstack(all_rows[:3]);y=np.concatenate(all_y[:3]);scale=np.linalg.norm(X,axis=0);Xs=X/scale
    fit_scaled,_,rank,sv=np.linalg.lstsq(Xs,y,rcond=None);fit=fit_scaled/scale
    error=float(np.max(np.abs(fit-truth)));condition=float(sv[0]/sv[-1])
    ck('shared synthetic coefficients identified on declared development shapes',
       rank==6 and error<1e-7,rank=int(rank),scaled_condition_number=condition,maximum_parameter_error=error)
    Xt=np.vstack(all_rows[3:]);yt=np.concatenate(all_y[3:]);test_error=float(np.max(np.abs(yt-Xt@fit)))
    ck('reserved synthetic shapes predict without refitting or shared preparation',
       test_error<1e-9,maximum_residual=test_error,rows=len(yt))
    wrong=fit.copy();wrong[2]*=1.03
    mutation=float(np.max(np.abs(yt-Xt@wrong)))
    ck('wrong common coefficient fails reserved synthetic identity',mutation>1e-5,maximum_residual=mutation)
    # A selected constant q makes a=0 and b constant. With clamped psi,
    # columns a*psi2,a*psi,b*psi2 vanish; b*psi is proportional to psi.
    const=np.array([[.1,0,0,.2,0,.4],[.7,0,0,.3,0,.6],[.3,0,0,.6,0,1.2]])
    ck('constant-path design is not full rank',np.linalg.matrix_rank(const)<6)
    # Numerical confirmation of the deterministic bound using correlated errors.
    x=(nodes+1)/2;ww=weights/2;psi=psis[0][0](x);psi2=psis[0][1](x)
    P=psi2+on*psi;B=4*ln*psi2+(4*ln*on-Gn/2)*psi
    ez,ea,eb=.002,.003,.004
    dz=ez*np.sign(P);da=-ea*np.sign(P);db=-eb*np.sign(B)
    value=abs(float(ww@((dz-mn*da)*P-db*B)))
    bound=float((ez+mn*ea)*(ww@np.abs(P))+eb*(ww@np.abs(B)))
    ck('correlated-error weak residual certificate',value<=bound+1e-15,bound=bound,achieved=value)
    note=Path(__file__).with_name('NETWORK_EVOLUTION_BLOCK16_v1.md')
    result={'summary':{'passed':len(checks),'failed':0},'checks':checks,
            'synthetic_fit':{'truth':truth.tolist(),'fit':fit.tolist(),'training_profiles':3,'reserved_profiles':2,'initial_hidden_states':[[r[2],r[3]] for r in specs]},
            'note_sha256':hashlib.sha256(note.read_bytes()).hexdigest(),
            'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'empirical_validation':False,
            'scope':'Necessary finite-window response of a chosen adaptive action, arbitrary hidden initial states; physical calibration and action selection remain conditional.'}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
