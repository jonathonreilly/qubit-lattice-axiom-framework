"""Finite challenges of conditional image noise and positive-time reconstruction."""
AUDIT_TIMEOUT_SEC = 180
import itertools
import json
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import logsumexp


def close(a,b,tol=2e-10):
    assert np.allclose(a,b,atol=tol,rtol=tol),(np.asarray(a),np.asarray(b))


def image_law(beta,angle,cut=50):
    k=np.arange(-cut,cut+1);X=np.sqrt(beta)*(angle-2*np.pi*k);logs=-X*X/2;p=np.exp(logs-logsumexp(logs));mean=float(p@X);xi=X-mean;var=float(p@(xi*xi));third=float(p@abs(xi)**3)
    return X,xi,p,mean,var,third


def conditional_moments_and_score():
    rows=[]
    for beta in [.03,.1,.4,1.,3.]:
        c=2*math.pi**2*beta;D=3+2*math.exp(-2*c)/(1-math.exp(-4*c));lower=4*math.pi**2*beta*math.exp(-c)/(D*D);vmin=math.inf;vmax=0.;score_error=0.
        for angle in np.linspace(-np.pi,np.pi,121):
            X,xi,p,mean,v,m3=image_law(beta,angle);assert v>=lower*(1-1e-12);vmin=min(vmin,v);vmax=max(vmax,v)
            n=np.arange(1,100);coeff=np.exp(-n*n/(2*beta));phi=1+2*np.sum(coeff*np.cos(n*angle));score=2*np.sum(n*coeff*np.sin(n*angle))/(np.sqrt(beta)*phi)
            phi_prime=-2*np.sum(n*coeff*np.sin(n*angle));phi_second=-2*np.sum(n*n*coeff*np.cos(n*angle))
            curvature=-phi_second/phi+(phi_prime/phi)**2
            close(v,1-curvature/beta,2e-7)
            close(mean,score,2e-8);score_error=max(score_error,abs(mean-score))
            # Raw second moments split without assuming the conditional mean is zero.
            close(float(p@(X*X)),mean*mean+v)
        rows.append(dict(beta=beta,D_beta=D,variance_lower=lower,minimum_observed_variance=vmin,maximum_observed_variance=vmax,score_representation_error=score_error))
    assert rows[-1]['maximum_observed_variance']>1
    return rows


def two_clock_score_alias():
    rows=[]
    for beta in [.1,.5,1.,3.]:
        values=[image_law(beta,u)[3] for u in [0,np.pi]];assert max(abs(v) for v in values)<1e-13
        v0=image_law(beta,0)[4];vpi=image_law(beta,np.pi)[4]
        rows.append(dict(beta=beta,score_at_clock_values=values,variance_at_zero=v0,variance_at_pi=vpi))
    # N=3 has a nonzero score at its nontrivial angle.
    assert abs(image_law(1.,2*np.pi/3)[3])>1
    return rows


def conditional_characteristic_clt():
    rows=[]
    for beta,angle in [(.1,.7),(.4,np.pi/3),(1.,np.pi)]:
        X,xi,p,mean,v,m3=image_law(beta,angle);t=.65;errors=[];bounds=[]
        for side in [2,3,4,5,8]:
            count=side**4;u=t/math.sqrt(count);chi=complex(p@np.exp(1j*u*xi));actual=count*np.log(chi);target=-v*t*t/2
            zeta=v*u*u/2;assert zeta<.5
            bound=count*(m3*abs(u)**3/6+zeta*zeta/(2*(1-zeta)))
            error=abs(actual-target);assert error<=bound+3e-12;errors.append(float(error));bounds.append(bound)
        assert errors[-1]<=errors[0]+1e-12
        rows.append(dict(beta=beta,angle=angle,conditional_mean=mean,variance=v,log_characteristic_errors=errors,explicit_taylor_bounds=bounds))
    return rows


def conditional_stability_and_mixture():
    beta=.4;angles=[0.,np.pi];laws=[image_law(beta,u) for u in angles];variances=np.array([z[4] for z in laws]);prob=np.array([.35,.65]);B=np.exp(1j*np.array([.2,1.1]));t=.7;rows=[]
    target=prob@(B*np.exp(-variances*t*t/2))
    naive=(prob@B)*math.exp(-float(prob@variances)*t*t/2)
    assert abs(target-naive)>1e-3
    for count in [16,256,4096]:
        chis=np.array([complex(p@np.exp(1j*t*xi/np.sqrt(count)))**count for X,xi,p,mean,v,m3 in laws]);actual=prob@(B*chis)
        rows.append(dict(count=count,stable_characteristic_error=float(abs(actual-target))))
    assert rows[-1]['stable_characteristic_error']<1e-4
    meanv=float(prob@variances);varv=float(prob@(variances-meanv)**2)
    # Fourth cumulant and cross-time squared-noise covariance of the mixture.
    fourth=3*float(prob@(variances**2));kappa4=fourth-3*meanv**2;close(kappa4,3*varv);assert kappa4>0
    return dict(rows=rows,correct_target=[target.real,target.imag],averaged_variance_target=[naive.real,naive.imag],random_variance=variances.tolist(),fourth_cumulant=kappa4,central_squared_noise_os_norm=varv)


def white_noise_os_intertwiner():
    times=np.array([.4,.9,1.7]);charges=np.array([.7,-1.1,.3]);r=.8;self_F=1/(2*r);noise=.65
    cross=np.exp(-r*(times[:,None]+times[None,:]))/(2*r)
    def gram(selfvar):
        return np.exp(-.5*selfvar*(charges[:,None]**2+charges[None,:]**2)+charges[:,None]*charges[None,:]*cross)
    HF=gram(self_F);HX=gram(self_F+noise);D=np.exp(-noise*charges**2/2);close(HX,D[:,None]*HF*D[None,:])
    assert np.linalg.eigvalsh(HX).min()>-1e-12 and np.linalg.eigvalsh(HF).min()>-1e-12
    means=np.exp(-noise*charges**2/2);HW=means[:,None]*means[None,:];centered=HW-np.outer(means,means);close(centered,0)
    assert np.linalg.matrix_rank(HW,tol=1e-11)==1
    # A temporally correlated added Gaussian is not white contact noise.
    extra_cross=noise*np.exp(-1.3*(times[:,None]+times[None,:]));Hcolored=HX*np.exp(charges[:,None]*charges[None,:]*extra_cross)
    assert np.max(abs(Hcolored-D[:,None]*HF*D[None,:]))>.005
    # The diagonal averaging factors do not depend on a positive time shift.
    shift=.6;shifted=np.exp(-r*(times[:,None]+times[None,:]+2*shift))/(2*r)
    shiftedF=np.exp(-.5*self_F*(charges[:,None]**2+charges[None,:]**2)+charges[:,None]*charges[None,:]*shifted)
    shiftedX=np.exp(-.5*(self_F+noise)*(charges[:,None]**2+charges[None,:]**2)+charges[:,None]*charges[None,:]*shifted)
    close(shiftedX,D[:,None]*shiftedF*D[None,:])
    return dict(F_gram_eigenvalues=np.linalg.eigvalsh(HF).tolist(),X_gram_eigenvalues=np.linalg.eigvalsh(HX).tolist(),white_gram_rank=1,colored_noise_intertwining_error=float(np.max(abs(Hcolored-D[:,None]*HF*D[None,:]))))


def exterior_matrix(p,k):
    domain=list(itertools.combinations(range(4),k));codomain=list(itertools.combinations(range(4),k+1));D=np.zeros((len(codomain),len(domain)))
    for i,I in enumerate(codomain):
        for n,j in enumerate(I):D[i,domain.index(I[:n]+I[n+1:])]=(-1)**n*p[j]
    return D


def current_sector_blindness():
    rows=[]
    for p in [np.array([.7,1.2,-.3,.6]),np.array([1.,0.,0.,0.]),np.array([.2,.4,.8,-.5])]:
        d1=exterior_matrix(p,1);d2=exterior_matrix(p,2);Pe=d1@d1.T/(p@p);I=np.eye(6)
        close(Pe@Pe,Pe);close(d2@Pe,0);close(d1.T@Pe,d1.T);close(d1.T@I@d1,d1.T@Pe@d1)
        assert np.linalg.matrix_rank(Pe,tol=1e-10)==3 and np.linalg.norm(d2@I@d2.T)>0
        rng=np.random.default_rng(13);j=rng.normal(size=(4,3));h=d1@j;close(h.T@I@h,h.T@Pe@h)
        rows.append(dict(momentum=p.tolist(),exact_rank=3,current_covariance_error=float(np.max(abs(d1.T@(I-Pe)@d1))),white_bianchi_covariance_norm=float(np.linalg.norm(d2@I@d2.T))))
    # Independent temporal Fourier integral gives a nonzero full-field norm.
    magnetic=[]
    for p in [np.array([1.,.3,.2]),np.array([.4,.6,-.8])]:
        r=float(np.linalg.norm(p));s2=float(p[0]**2+p[1]**2);tau=1.3
        integral=quad(lambda w:s2/(math.pi*(w*w+r*r)),0,np.inf,weight='cos',wvar=tau,epsabs=1e-11,limit=200)[0]
        kernel=s2/(2*r)*math.exp(-r*tau);close(integral,kernel,2e-9)
        laplace=(math.exp(-.5*r)-math.exp(-1.2*r))/r;norm=s2/(2*r)*laplace**2;assert norm>0
        magnetic.append(dict(spatial_momentum=p.tolist(),positive_time_kernel=kernel,nonzero_full_field_os_norm=norm))
    # A current covariance is a local differential contact distribution.
    # Gaussian frequency regularization tends to zero at strict time separation.
    tau=1.;r=.9;contact=[]
    for eps in [.04,.02,.01,.005]:
        kernel=(r*r+1/(2*eps)-tau*tau/(4*eps*eps))*math.exp(-tau*tau/(4*eps))/(2*math.sqrt(math.pi*eps));contact.append(kernel)
        direct=quad(lambda w:(w*w+r*r)*math.exp(-eps*w*w)/math.pi,0,np.inf,weight='cos',wvar=tau,epsabs=2e-10,limit=200)[0]
        close(direct,kernel,2e-9)
    assert abs(contact[-1])<1e-16
    return dict(hodge=rows,magnetic=magnetic,regularized_current_contact=contact)


def main():
    result=dict(conditional_moments_and_score=conditional_moments_and_score(),two_clock_score_alias=two_clock_score_alias(),conditional_characteristic_clt=conditional_characteristic_clt(),conditional_stability_and_mixture=conditional_stability_and_mixture(),white_noise_os_intertwiner=white_noise_os_intertwiner(),current_sector_blindness=current_sector_blindness())
    print(json.dumps(result,indent=2))
    print('TOTAL: PASS=6 FAIL=0')
    print('per_element: executed finite Gaussian-image and Fourier score identities, conditional variance bounds and complex characteristic remainders at declared beta and angle values.')
    print('per_site: executed the zero score on both N=2 clock plaquette values and the contrasting N=3 value; this checks an observable, not the entire clock theory.')
    print('per_mode: executed exterior-algebra current projections and independent temporal Fourier integrals at the declared four- and three-momenta.')
    print('per_block: executed conditional-noise arrays, a nonergodic variance-mixture countercontrol, and finite positive-time exponential Gram identities with colored-noise failure controls.')
    print('lattice_wide: checked and not executed; conditional white-noise scaling and OS equivalence rely on the stated analytic hypotheses, and fixed-law Gaussian photon closure remains open.')

if __name__=='__main__':main()
