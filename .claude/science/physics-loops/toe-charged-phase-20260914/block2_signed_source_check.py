"""Closed finite Fourier sums challenge the signed-source covariance lemma."""
from pathlib import Path
from itertools import product
import json
import numpy as np
from numpy.polynomial.hermite import hermgauss
from scipy.integrate import quad


def model(Q,B,z,U):
    eta=np.abs(z)*(1+np.abs(z))/(1-np.abs(z))**2;R=np.diag(eta)
    vals,vecs=np.linalg.eigh(Q);Qi=(vecs/np.sqrt(vals))@vecs.T
    delta=float(np.linalg.eigvalsh(Qi@B.T@R@B@Qi)[-1]);assert delta<1
    ns=np.array(list(product([-1,0,1],repeat=len(z))),float)
    coeff=np.prod(np.where(ns==0,1,z[None,:]/2),axis=1)
    current=ns@B;coeff=coeff*np.exp(-np.einsum('ni,ij,nj->n',current,np.linalg.inv(Q),current)/2)
    def exact(theta):
        weights=coeff*np.exp(1j*(ns@theta));partition=np.sum(weights)
        first=np.einsum('n,ni->i',weights,1j*ns);second=-np.einsum('n,ni,nj->ij',weights,ns,ns)
        assert abs(partition.imag)<1e-12 and partition.real>0
        H=(second/partition-np.outer(first,first)/partition**2)
        assert np.max(np.abs(H.imag))<1e-12
        return float(partition.real),H.real
    def quadrature(theta,n):
        nodes,weights=hermgauss(n);a=np.array(list(product(nodes,nodes)))*np.sqrt(2);w=np.prod(np.array(list(product(weights,weights))),axis=1)/np.pi
        a=a@Qi;f=np.prod(1+z[None,:]*np.cos(a@B.T+theta[None,:]),axis=1)
        return float(w@f)
    p0,H0=exact(np.zeros(len(z)));assert p0>0
    rng=np.random.default_rng(709);worst=0.;rows=[]
    for theta in [np.zeros(len(z)),np.arange(len(z))*.7,*rng.normal(size=(12,len(z)))*3]:
        p,H=exact(theta);lr=np.log(p/p0);bound=theta@R@theta/2
        assert np.linalg.eigvalsh(H+R)[0]>-1e-12
        assert np.linalg.eigvalsh(R/(1-delta)-H)[0]>-1e-12
        assert -bound-1e-12<=lr<=bound/(1-delta)+1e-12
        for n in [40,64]:worst=max(worst,abs(quadrature(theta,n)-p))
        rows.append({'phase_norm':float(np.linalg.norm(theta)),'log_ratio':float(lr),'lower':-float(bound),'upper':float(bound/(1-delta))})
    assert worst<1e-11
    return {'Q':Q,'B':B,'R':R,'U':U,'delta':delta,'partition0':p0,'H0':H0,'exact':exact,'rows':rows,'quadrature_error':worst}

Q1=np.diag([.8,1.3]);B1=np.array([[1,0],[0,1],[1,1],[1,-1.]])
z1=np.array([.02,-.025,.012,-.008]);U1=np.array([[1,.2],[-.3,1],[.4,-.2],[-.2,.5]])
Q2=np.array([[1.2,.2],[.2,1.7]]);B2=np.array([[.8,.1],[.2,.9],[1,-.4]])
z2=np.array([-.03,.015,-.01]);U2=np.array([[.5,-.1],[.4,.8],[.7,.2]])
models=[model(Q1,B1,z1,U1),model(Q2,B2,z2,U2)];G=np.diag([2.,3.]);Gi=np.diag(1/np.sqrt(np.diag(G)))
epsilon=max(float(np.linalg.eigvalsh(Gi@m['U'].T@m['R']@m['U']@Gi)[-1]) for m in models);delta=max(m['delta'] for m in models);assert epsilon<1
cs=np.array([1.,2.]);weights=cs*np.array([m['partition0'] for m in models]);weights/=sum(weights)
Cov=G+sum(w*m['U'].T@m['H0']@m['U'] for w,m in zip(weights,models))
assert np.linalg.eigvalsh(Cov-(1-epsilon)*G)[0]>0
assert np.linalg.eigvalsh((1+epsilon/(1-delta))*G-Cov)[0]>0
for h in [np.array([x,y]) for x,y in product([-.9,0,.5,2.],repeat=2)]:
    ratio=sum(w*m['exact'](m['U']@h)[0]/m['partition0'] for w,m in zip(weights,models));logM=h@G@h/2+np.log(ratio)
    assert (1-epsilon)*h@G@h/2-1e-12<=logM<=(1+epsilon/(1-delta))*h@G@h/2+1e-12
# Negative activity gives a strict shift-ratio increase, despite positive
# integrands and a valid convexity comparison.
z=-.2;Q=2.;p0=1+z*np.exp(-1/(2*Q));ppi=1-z*np.exp(-1/(2*Q));assert ppi>p0>0
# Derive the conditional Gaussian attenuation independently of source text.
beta=12.;n=6.;rho=.7;c=.4;var=beta/n
integrand=lambda a:np.exp(-(a+c)**2/(2*var))/np.sqrt(2*np.pi*var)
actual=quad(lambda a:integrand(a)*np.cos(rho*a),-np.inf,np.inf,epsabs=1e-12)[0]+1j*quad(lambda a:integrand(a)*np.sin(rho*a),-np.inf,np.inf,epsabs=1e-12)[0]
correct=np.exp(-beta*rho*rho/(2*n)-1j*rho*c);double_exponent=np.exp(-beta*rho*rho/n-1j*rho*c)
assert abs(actual-correct)<1e-11 and abs(actual-double_exponent)>.1
out={'models':[{'delta':m['delta'],'quadrature_error':m['quadrature_error'],'phase_cases':m['rows']} for m in models],'mixture':{'delta':delta,'epsilon':epsilon,'covariance':Cov.tolist(),'lower_covariance':((1-epsilon)*G).tolist(),'upper_covariance':((1+epsilon/(1-delta))*G).tolist()},'negative_activity_shift_ratio':ppi/p0,'conditional_Gaussian_correct_error':abs(actual-correct),'doubled_exponent_rejected_error':abs(actual-double_exponent)}
print(json.dumps(out,indent=2),flush=True)
Path(__file__).with_name('BLOCK2_SIGNED_SOURCE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
