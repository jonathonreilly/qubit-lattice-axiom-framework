"""Author controls for singular energy accounting; explicitly not the cube."""
from pathlib import Path
import hashlib,json,time
import numpy as np
from numpy.polynomial.legendre import leggauss

HERE=Path(__file__).resolve().parent


def phi_laplace(s,T):
    return 1/s-2/(T*s*s)+2*(-np.expm1(-s*T))/(T*T*s*s*s)


def mean(eps,t,a,b,lam,delta):
    return delta*a/(b-lam*eps*eps)*np.exp(-lam*t)*(-np.expm1(-(b/eps**2-lam)*t))


def controls():
    # Trace-one classical three-state Markov chain: q -> high with rate
    # a eps^2, q -> terminal with rate lam-a eps^2, high -> terminal at
    # b/eps^2. Energies are (0,delta eps^-4,0), initially q=1.
    a=.21;b=1.8;lam=.4;delta=1.3;T=1.4
    evalues=[.2,.1,.05,.025,.0125]
    initial=[];physical=[];distribution=[]
    nodes,weights=leggauss(160)
    impulse=delta*a/b
    limit_integral=impulse*(1-lam*phi_laplace(lam,T))
    for eps in evalues:
        assert lam-a*eps**2>0
        for tau in [0.,.2,1.,3.,10.]:
            t=eps**2*tau;m=mean(eps,t,a,b,lam,delta)
            high=m*eps**4/delta;q=np.exp(-lam*t);terminal=1-q-high
            assert min(q,high,terminal)>-1e-14
            target=impulse*(-np.expm1(-b*tau))
            initial.append(dict(epsilon=eps,tau=tau,mean=m,profile=target,
                                eps4_variance=delta*m-eps**4*m*m,
                                variance_profile=delta*target,probabilities=[q,high,terminal]))
        for t in [.2,.7,1.4]:
            m=mean(eps,t,a,b,lam,delta)
            gain=delta*a/eps**2*np.exp(-lam*t);loss=b/eps**2*m
            deriv=delta*a/(b-lam*eps**2)*(-lam*np.exp(-lam*t)+b/eps**2*np.exp(-b*t/eps**2))
            assert abs((gain-loss)-deriv)<2e-10
            physical.append(dict(epsilon=eps,t=t,mean=m,
                                 mean_limit=impulse*np.exp(-lam*t),
                                 eps2_gain=eps**2*gain,eps2_loss=eps**2*loss,
                                 common_scaled_flow=delta*a*np.exp(-lam*t),
                                 net_power=deriv,regular_power_limit=-lam*impulse*np.exp(-lam*t)))
        # Test phi(t)=(1-t/T)^2, zero after T; C1 at T. Its integral
        # against power has a short positive term and a regular negative term.
        exact=delta*a/(b-lam*eps**2)*(-lam*phi_laplace(lam,T)+b/eps**2*phi_laplace(b/eps**2,T))
        cap=min(T/eps**2,40/b)
        tau=(nodes+1)*cap/2
        fast_quad=b*cap/2*np.dot(weights,(1-eps**2*tau/T)**2*np.exp(-b*tau))
        checked=delta*a/(b-lam*eps**2)*(fast_quad-lam*phi_laplace(lam,T))
        assert abs(exact-checked)<2e-13
        distribution.append(dict(epsilon=eps,test_integral=exact,
                                 limit_including_initial_impulse=limit_integral,
                                 omitted_impulse_mutant_limit=limit_integral-impulse,
                                 fast_age_quadrature_error=abs(exact-checked)))
    # An exact band-loss term need not be nonnegative when the density has
    # interband coherence, even though Gamma itself is positive.
    Hband=np.diag([0.,2.]);Gamma=np.array([[1.,.6],[.6,1.]])
    A=(Hband@Gamma+Gamma@Hband)/2
    values,vectors=np.linalg.eigh(A);psi=vectors[:,0]
    negative=float(np.vdot(psi,A@psi).real)
    assert negative<0 and np.linalg.eigvalsh(Gamma).min()>0
    return {'parameters':dict(a=a,b=b,lam=lam,delta=delta,T=T),
            'initial_profile_rows':initial,'physical_flow_rows':physical,
            'distribution_rows':distribution,'impulse':impulse,
            'loss_sign_control':{'Hband':Hband.tolist(),'Gamma':Gamma.tolist(),
                                 'state':psi.tolist(),'band_loss':negative,
                                 'exact_smallest_eigenvalue':1-np.sqrt(1+.6**2)},
            'scope':'Separate trace-one three-state Markov injection/depletion model and a two-band algebra control. No actual cube dynamics, large-spin convergence proof, physical reservoir, or independent reconstruction. The omitted-impulse mutant is an actually evaluated wrong limiting expression, not a modified microscopic evolution.'}


def main():
    start=time.monotonic();result=controls()
    result['elapsed_seconds']=time.monotonic()-start
    result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    data=json.dumps(result,indent=2)+'\n'
    (HERE/'INITIAL_ENERGY_BALANCE_CONTROL_RESULTS.json').write_text(data)
    print(data,end='')


if __name__=='__main__':main()
