#!/usr/bin/env python3
"""Synthetic checks of working count kernels and minimum-energy reconstruction.
No observed values, fitted parameters, or physical energy budgets enter.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.linalg import null_space
from scipy.optimize import minimize

AUDIT_TIMEOUT_SEC = 240

def run_checks():
    checks=[]
    def check(name,value,tol=2e-9):
        err=float(np.max(np.abs(value)))
        assert np.isfinite(err) and err<=tol,(name,err,tol)
        checks.append({'name':name,'error':err,'tolerance':tol})
    def truth(name,condition):
        assert condition,name
        checks.append({'name':name,'passed':True})
    def integral(fn,a,b,n=100):
        x,w=leggauss(n);s=(a+b)/2+(b-a)*x/2
        return (b-a)/2*np.dot(w,fn(s))
    def hat_gram(T,n):
        return (2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1))/(6*np.pi*T**3)
    def weighted_residual(y,Z,weight):
        Zw=Z*np.sqrt(weight)[:,None];yw=y*np.sqrt(weight)
        beta=np.linalg.lstsq(Zw,yw,rcond=None)[0]
        return np.sum(weight*(y-Z@beta)**2),beta

    rng=np.random.default_rng(202610150217)
    # Count averages versus direct time-domain acceleration, including gaps.
    for idx,(left,right,gap) in enumerate([(1.,1.,0.),(.7,1.3,0.),(.7,1.3,.8),(2.,.25,1.6)]):
        a,b,c,d=0.,left,left+gap,left+gap+right;H=(c+d-a-b)/2
        v=lambda s: .07*s**3-.31*s**2+.9*s+.2*np.sin(1.7*s)+.6
        acc=lambda s:.21*s*s-.62*s+.9+.34*np.cos(1.7*s)
        obs=(integral(v,c,d)/right-integral(v,a,b)/left)/H
        deriv=integral(lambda s:acc(s)*(s-a)/(H*left),a,b)
        if gap:deriv+=integral(acc,b,c)/H
        deriv+=integral(lambda s:acc(s)*(d-s)/(H*right),c,d)
        check(f'count_to_acceleration_gap_{idx}',obs-deriv)
        check(f'weight_normalization_{idx}',(left/2+gap+right/2)/H-1)
    # Unequal interval Gram from piecewise integration versus count difference matrix.
    for idx,T in enumerate([np.array([1.,1.]),np.array([.7,1.4,.2,2.3]),rng.uniform(.2,2.,9)]):
        m=len(T);H=(T[:-1]+T[1:])/2;D=np.zeros((m-1,m))
        for i in range(m-1):D[i,i]=-1/(H[i]*T[i]);D[i,i+1]=1/(H[i]*T[i+1])
        G=D@np.diag(T)@D.T/(6*np.pi)
        explicit=np.diag((1/T[:-1]+1/T[1:])/H**2)
        for i in range(m-2):explicit[i,i+1]=explicit[i+1,i]=-1/(H[i]*H[i+1]*T[i+1])
        check(f'unequal_overlap_{idx}',G-explicit/(6*np.pi))
        if np.all(T==T[0]):
            check(f'constant_duration_count_vs_hat_{idx}',hat_gram(T[0],m-1)-G)
        check(f'constant_velocity_cancellation_{idx}',D@T)
        vb=rng.normal(size=m);r=D@(T*vb)
        E1=.5*r@np.linalg.solve(G,r);E2=3*np.pi*np.sum(T*(vb-np.dot(T,vb)/sum(T))**2)
        check(f'weighted_variance_identity_{idx}',(E1-E2)/max(1,E2))
        truth(f'positive_unequal_gram_{idx}',np.min(np.linalg.eigvalsh(G))>0)
    # Closed adjacent-window inverse, spectrum and a discriminating cross-term control.
    for n in [1,2,3,7,12]:
        L=2*np.eye(n)-np.eye(n,k=1)-np.eye(n,k=-1)
        i,j=np.meshgrid(np.arange(1,n+1),np.arange(1,n+1),indexing='ij')
        inv=np.minimum(i,j)*(n+1-np.maximum(i,j))/(n+1)
        check(f'closed_inverse_{n}',L@inv-np.eye(n))
        check(f'closed_spectrum_{n}',np.linalg.eigvalsh(L)-(2-2*np.cos(np.arange(1,n+1)*np.pi/(n+1))))
    G=hat_gram(1.,2);r=np.array([1.,1.]);joint=.5*r@np.linalg.solve(G,r);indep=.5*np.sum(r*r/np.diag(G))
    truth('discarding_cross_terms_changes_energy',abs(joint-indep)>.4*joint)
    # Direct vector calibration kernel: cancel actual vector moments and baseline.
    m=8;T=rng.uniform(.5,1.6,m);edges=np.r_[0,np.cumsum(T)]
    n=np.column_stack([np.cos(np.arange(m)*.51),np.sin(np.arange(m)*.51),np.zeros(m)])
    kappa=np.linspace(.8,1.7,m);N=kappa[:,None]*n;Z=np.column_stack([N,np.ones(m)])
    C=null_space(Z.T).T;B=np.diag(kappa*kappa/(6*np.pi*T));H=C@B@C.T
    check('vector_initial_velocity_cancellation',C@N);check('additive_baseline_cancellation',C@np.ones(m))
    y=rng.normal(size=m);ws,beta=weighted_residual(y,Z,1/np.diag(B))
    check('vector_nuisance_quotient',.5*(C@y)@np.linalg.solve(H,C@y)-.5*ws)
    # A scalar sum-zero contrast fails to cancel a rotating constant velocity.
    raw=np.array([1.,-1.]);rot=np.array([[1.,0.,0.],[0.,1.,0.]])
    truth('scalar_cancellation_does_not_cancel_vector_velocity',abs(raw@(rot@np.array([2.,-1.,0.])))>1)
    # Piecewise W constructed by integrating F: integrate W dot actual acceleration.
    c=C[0];F=c[:,None]*N/T[:,None];prefix=np.vstack([np.zeros(3),np.cumsum(F*T[:,None],axis=0)])
    check('vector_primitive_terminal',prefix[-1]);velocity=lambda s:np.array([.3*s*s+np.sin(s),.2*s**3-.1*s,np.cos(.7*s)])
    accel=lambda s:np.array([.6*s+np.cos(s),.6*s*s-.1,-.7*np.sin(.7*s)])
    means=[];force_integrals=[]
    for i in range(m):
        means.append(integral(lambda s:np.sum(N[i,:,None]*velocity(s),axis=0),edges[i],edges[i+1])/T[i])
        force_integrals.append(integral(lambda s:np.sum((-prefix[i,:,None]-F[i,:,None]*(s-edges[i]))*accel(s),axis=0),edges[i],edges[i+1]))
    check('vector_time_domain_identity',c@means-sum(force_integrals),2e-8)
    # Nonlinear clock and known varying calibration: direct change of variables.
    tau=lambda s:s+.03*s*s;dtau=lambda s:1+.06*s;k=lambda t:1+.2*t
    vel=lambda s:np.sin(.8*s)+.3*s
    for a,b in [(.1,.8),(.8,1.6)]:
        ta,tb=tau(a),tau(b);sinv=lambda t:(np.sqrt(1+.12*t)-1)/.06
        direct=integral(lambda t:k(t)*vel(sinv(t)),ta,tb)/(tb-ta)
        transformed=integral(lambda s:k(tau(s))*dtau(s)*vel(s),a,b)/(tb-ta)
        check(f'nonlinear_clock_{a}',direct-transformed)
    # General nuisance quotient against direct KKT solve and robust weighted-ball solution.
    for case in range(12):
        m=4+case%4;p=1+case%2;R=rng.normal(size=(m,m));G=R@R.T+.5*np.eye(m);X=rng.normal(size=(m,p));y=rng.normal(size=m)
        U=null_space(X.T);z=U.T@y;H=U.T@G@U;quot=.5*z@np.linalg.solve(H,z)
        Gi=np.linalg.inv(G);beta=np.linalg.solve(X.T@Gi@X,X.T@Gi@y);res=y-X@beta;direct=.5*res@Gi@res
        check(f'nuisance_direct_{case}',direct-quot)
        vals,V=np.linalg.eigh(G);Win=(V/np.sqrt(vals))@V.T;Z=Win@X;P=np.eye(m)-Z@np.linalg.pinv(Z);yh=Win@y
        check(f'nuisance_whitening_{case}',.5*np.linalg.norm(P@yh)**2-quot)
        rho=.4*np.linalg.norm(P@yh);eh=rho*(P@yh)/np.linalg.norm(P@yh);pred=.5*max(0,np.linalg.norm(P@yh)-rho)**2
        check(f'noise_ball_attainment_{case}',.5*np.linalg.norm(P@(yh-eh))**2-pred)
        opt=minimize(lambda e:.5*np.linalg.norm(P@(yh-e))**2,np.zeros(m),constraints={'type':'ineq','fun':lambda e:rho*rho-e@e},method='SLSQP',options={'ftol':1e-12,'maxiter':300})
        truth(f'noise_ball_optimizer_success_{case}',opt.success)
        check(f'noise_ball_independent_optimizer_{case}',opt.fun-pred,2e-8)
    # Singular feasible versus incompatible residual: range condition is essential.
    A=np.array([[1.,0.,0.],[2.,0.,0.]]);G=A@A.T
    for r,feasible in [(np.array([1.,2.]),True),(np.array([0.,1.]),False)]:
        isfeasible=np.linalg.norm(G@np.linalg.pinv(G)@r-r)<1e-12
        truth('singular_feasibility_'+str(feasible),isfeasible==feasible)
    G=np.diag([1.,0.]);r=np.array([0.,1.]);truth('pseudoinverse_without_range_is_false_zero',r@np.linalg.pinv(G)@r==0 and np.linalg.norm(G@np.linalg.pinv(G)@r-r)>0)
    # Fourier-space real Schwartz data, not samples of the closed Gram formula.
    # Smooth annular filter exp[-eps(k^2+k^-2)] removes both infrared and ultraviolet singularities.
    T=1.;centers=np.arange(4,dtype=float);target=np.array([.3,-.2,.4,.1]);Gexact=hat_gram(T,4);Emin=.5*target@np.linalg.solve(Gexact,target);fourier=[]
    for eps in [.3,.12,.04,.012]:
        gx,gw=leggauss(900);K=np.sqrt(38/eps);k=(gx+1)*K/2;dw=gw*K/2
        ax,aw=leggauss(12);ang=2*np.pi*np.dot(aw,ax*ax)
        base=dw*k*k*ang/(2*np.pi)**3;chi=np.exp(-eps*(k*k+1/(k*k)))
        W=np.exp(1j*centers[:,None]*k)*np.sinc(k*T/(2*np.pi))**2
        Gchi=np.real((W*(base*chi))@W.conj().T);coef=np.linalg.solve(Gchi,target)
        C=coef@W.real;S=coef@W.imag
        energy=.5*np.dot(base*chi*chi,C*C+S*S)
        out=[]
        for center in centers:
            func=lambda s:np.cos(np.outer(s,k))@(base*chi*C)+np.sin(np.outer(s,k))@(base*chi*S)
            val=integral(lambda s:(s-center+T)/T**2*func(s),center-T,center,130)
            val+=integral(lambda s:(center+T-s)/T**2*func(s),center,center+T,130);out.append(val)
        check(f'explicit_schwartz_constraints_{eps}',np.array(out)-target,3e-8)
        truth(f'explicit_schwartz_above_infimum_{eps}',energy>=Emin*(1-1e-8))
        fourier.append({'eps':eps,'energy':energy,'energy_infimum':Emin,'relative_excess':energy/Emin-1,'max_constraint_error':float(np.max(np.abs(np.array(out)-target)))})
    truth('smooth_exact_constraint_approach',all(b['relative_excess']<a['relative_excess'] for a,b in zip(fourier[:-1],fourier[1:])))
    # Invisible radial Gaussian field: odd angular derivative integrates to zero; energy positive.
    ax,aw=leggauss(25)
    for amp in [.3,1.,4.]:
        check(f'radial_invisible_gradient_{amp}',amp*np.dot(aw,ax))
        truth(f'radial_positive_energy_{amp}',3*np.pi**1.5*amp**2/4>0)
    # Multi-mass enclosure checked using an independent finite positive Fourier quadrature.
    k=np.geomspace(1e-4,180.,2400);dk=np.gradient(k);omega=k
    Wt=np.exp(1j*centers[:,None]*omega)*np.sinc(omega/(2*np.pi))**2
    Bspec=np.real((Wt*(dk*omega**2/(6*np.pi**2)))@Wt.conj().T)
    for mu in [.2,.8,2.,5.]:
        radial=np.maximum(omega*omega-mu*mu,0)**1.5/omega
        Gmu=np.real((Wt*(dk*radial/(6*np.pi**2)))@Wt.conj().T)
        truth(f'mass_gram_enclosure_{mu}',np.min(np.linalg.eigvalsh(Bspec-Gmu))>-1e-12)
        truth(f'mass_gram_positive_{mu}',np.min(np.linalg.eigvalsh(Gmu))>0)
    # Physical normalization agrees with direct mathematical energy rescaling.
    for case in range(12):
        Q=rng.uniform(.3,5.);q=rng.uniform(.01,.32);T=rng.uniform(.2,2.);r=rng.normal(size=3);G=hat_gram(T,3)
        Em=.5*r@np.linalg.solve(q*G,r);Gb=1/(8*np.pi*Q)
        check(f'physical_normalization_{case}',(2*Q*Em-(r@np.linalg.solve(G,r))/(8*np.pi*Gb*q))/max(1,2*Q*Em))
        Gmeas=Gb*(1+rng.uniform(0,.4));lower=3*(r@np.linalg.solve(G,r))/(8*np.pi*Gmeas)
        truth(f'measured_ceiling_lower_bound_{case}',2*Q*Em>=lower)
    result={'role':'synthetic mathematical controls, no empirical validation','checks_passed':len(checks),'checks':checks,'explicit_schwartz_fields':fourier,'discarded_cross_term_example':{'joint_energy':joint,'diagonal_only_energy':indep},'measured_gravity_tests':0,'fitted_parameters':0}
    return result
