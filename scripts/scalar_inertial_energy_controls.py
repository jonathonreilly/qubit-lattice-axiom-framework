#!/usr/bin/env python3
"""Direct-author controls: inertial full conformal force, fixed lab energy.
Synthetic fields only. No measured trajectory, scalar energy, or fit.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad

AUDIT_TIMEOUT_SEC = 240

def run_checks():
    checks=[]
    def check(name,x,tol=2e-9):
     e=float(np.max(np.abs(x)));assert np.isfinite(e) and e<=tol,(name,e,tol)
     checks.append({'name':name,'error':e,'tolerance':tol})
    def truth(name,ok):
     assert ok,name
     checks.append({'name':name,'passed':True})
    def nodes(a,b,n):
     x,w=leggauss(n);return (a+b)/2+(b-a)*x/2,w*(b-a)/2

    def tensor(beta):
     x=beta*beta
     if x<1e-5:
      par=(1-x)**2/(2*np.pi)*sum(x**n/(2*n+3) for n in range(10))
      perp=(1-x)/(2*np.pi)*sum(x**n/((2*n+1)*(2*n+3)) for n in range(10))
     else:
      L=np.arctanh(beta)/beta
      par=(1-x)**2*(L-1)/(2*np.pi*x)
      perp=(1-x)*(1-(1-x)*L)/(4*np.pi*x)
     return np.diag([perp,perp,par])

    # Independently integrate the original lab-angle tensor; no Lorentz substitution.
    for b in [0.,1e-5,.001,.07,.4,.8,.95,.99]:
     pa=(1-b*b)**2/(4*np.pi)*quad(lambda z:(z-b)**2/(1-b*z)**3,-1,1,epsabs=1e-12)[0]
     pe=(1-b*b)**2/(8*np.pi)*quad(lambda z:(1-z*z)/(1-b*z)**3,-1,1,epsabs=1e-12)[0]
     M=tensor(b);check('lab_angle_tensor_'+str(b),np.diag(M)-[pe,pe,pa])
     truth('tensor_positive_'+str(b),np.linalg.eigvalsh(M)[0]>0)
     truth('stationary_enclosure_'+str(b),np.linalg.eigvalsh(np.eye(3)/(6*np.pi)-M)[0]>=-1e-13)
    check('zero_velocity_tensor',tensor(0)-np.eye(3)/(6*np.pi))

    # Four general vector windows, each a sum of two normalized Gaussians.
    # Schwartz windows are admissible by H1 closure; count kernels themselves are compact.
    rng=np.random.default_rng(202610150235)
    coeff=rng.normal(size=(4,2,3));centers=np.array([[-.8,.2],[-.1,.9],[.6,1.4],[-1.1,.5]])
    widths=np.array([.55,.9])
    def transform(lam):
     lam=np.asarray(lam);return np.einsum('jar,ja...->j...r',coeff,np.exp(1j*centers[(...,)+(None,)*lam.ndim]*lam)*np.exp(-.5*widths[(None,slice(None))+(None,)*lam.ndim]**2*lam**2))
    def time_gram(M):
     out=np.zeros((4,4))
     for j in range(4):
      for k in range(4):
       for a in range(2):
        for b in range(2):
         D=widths[a]**2+widths[b]**2;delta=centers[j,a]-centers[k,b]
         dprod=np.exp(-delta*delta/(2*D))/np.sqrt(2*np.pi*D)*(1/D-delta*delta/D**2)
         out[j,k]+=dprod*coeff[j,a]@M@coeff[k,b]
     return out

    def lab_gram(beta,mu,omit_time=False):
     # Direct lab radial/angle integral of (k-omega*u), using exact azimuth integration.
     k,kw=nodes(0,14/(min(widths)*(1-beta)),650);z,zw=nodes(-1,1,90)
     om=np.sqrt(k*k+mu*mu);lam=om[:,None]-beta*k[:,None]*z
     W=transform(lam);K=k[:,None];O=om[:,None]
     transverse=np.pi*K*K*(1-z*z)/(O*O)
     longitudinal=2*np.pi*(K*z-(0 if omit_time else beta)*O)**2/(O*O)
     wt=kw[:,None]*K*K*zw*(1-beta*beta)**2/(2*np.pi)**3
     return np.real(np.einsum('jazr,kazr,azr->jk',W,W.conj(),wt[:,:,None]*np.stack([transverse,transverse,longitudinal],axis=-1)))

    def boosted_gram(beta,mu):
     gamma=1/np.sqrt(1-beta*beta);lo=mu/gamma
     lam,lw=nodes(lo,max(14/min(widths),lo+1),450);z,zw=nodes(-1,1,100)
     r=np.sqrt(np.maximum(0,1-(lo/lam)**2));den=1+beta*r[:,None]*z
     aper=np.pi*np.sum(zw*(1-z*z)/den,axis=1)
     apar=2*np.pi*np.sum(zw*z*z/den,axis=1)/(gamma*gamma)
     weight=(1-beta*beta)/(2*np.pi)**3*lw*lam*lam*r**3
     diag=weight[:,None]*np.stack([aper,aper,apar],axis=-1)
     W=transform(lam)
     return np.real(np.einsum('jkr,lkr,kr->jl',W,W.conj(),diag))

    samples=[]
    for beta in [0.,.35,.72,.9]:
     G0=time_gram(tensor(beta));truth('massless_general_vector_pd_'+str(beta),np.linalg.eigvalsh(G0)[0]>0)
     check('massless_lab_vs_time_'+str(beta),lab_gram(beta,0)-G0,2e-8)
     check('massless_boost_vs_time_'+str(beta),boosted_gram(beta,0)-G0,2e-9)
     for mu in [.25,1.,3.]:
      lab=lab_gram(beta,mu);boost=boosted_gram(beta,mu)
      check('massive_lab_vs_boost_'+str((beta,mu)),lab-boost,1e-7)
      truth('massive_gram_positive_'+str((beta,mu)),np.linalg.eigvalsh(boost)[0]>0)
      eig=np.linalg.eigvalsh(G0-boost);truth('massive_gram_enclosure_'+str((beta,mu)),eig[0]>-1e-10)
      samples.append({'beta':beta,'mu':mu,'lab_boost_max_error':float(np.max(np.abs(lab-boost))),'smallest_mass_gap_eigenvalue':float(eig[0])})
     wrong=lab_gram(beta,0,True)
     if beta:truth('omitting_partial_time_changes_response_'+str(beta),np.linalg.norm(wrong-G0)>.02*np.linalg.norm(G0))
    # A shared multimode energy budget and stationary enclosure on general vector kernels.
    stationary=time_gram(tensor(0));beta=.61;mu=[0.,.4,1.7];alpha=np.array([.23,-.41,.13]);q=alpha@alpha
    actual=sum(a*a*boosted_gram(beta,m) for a,m in zip(alpha,mu));enclosure=q*stationary
    truth('mixed_modes_shared_energy_enclosure',np.min(np.linalg.eigvalsh(enclosure-actual))>0)
    y=np.array([.3,-.1,.5,.8]);required=.5*y@np.linalg.solve(actual,y);lower=.5*y@np.linalg.solve(enclosure,y)
    truth('inverse_energy_inequality',required>=lower)
    # Nonoverlapping rotating count directions with exact vector cancellation.
    from scipy.linalg import null_space
    T=np.array([.7,1.1,.8,1.4,.6,1.2]);directions=rng.normal(size=(6,3));directions/=np.linalg.norm(directions,axis=1)[:,None]
    C=null_space(directions.T).T;M=tensor(.67)
    B=np.diag(np.einsum('ij,jk,ik->i',directions,M,directions)/T);Bstat=np.diag(1/(6*np.pi*T));G=C@B@C.T
    check('count_vector_cancellation',C@directions)
    truth('count_metric_enclosure',np.min(np.linalg.eigvalsh(C@(Bstat-B)@C.T))>0)
    obs=rng.normal(size=6);z=C@obs;minimum=.5*z@np.linalg.solve(G,z)
    Q=np.diag(1/np.diag(B));bc=np.linalg.solve(directions.T@Q@directions,directions.T@Q@obs);res=obs-directions@bc
    check('inertial_count_nuisance_quotient',minimum-.5*res@Q@res,2e-8)
    result={'role':'synthetic operator controls; no physical trajectory or data fit','checks_passed':len(checks),'checks':checks,'mass_samples':samples,'mixed_mode_energy':{'actual_required':required,'stationary_enclosure_lower':lower},'new_empirical_values':0}
    return result
