"""Conditional direction-law geometry; no physical noise calibration.

All floating evaluations are numerical diagnostics. Mathematical statements and
strict inequalities require the explicit domains in the paired canonical note.
"""
AUDIT_TIMEOUT_SEC = 180
import math
import numpy as np
from scipy.stats import f as f_law


def ratio_tau(r, s, alpha):
    if not (r >= 1 and s >= 1 and 0 < alpha < 1):
        raise ValueError('positive complex ranks and tail probability required')
    if r == 1:
        return math.sqrt(math.expm1(-math.log(alpha)/s))
    return math.sqrt(r/s*f_law.isf(alpha, 2*r, 2*s))


def cone_distance(a, b, tau):
    if min(a,b,tau)<0:
        raise ValueError('nonnegative norms and cone width required')
    return max(0.,a-tau*b)/math.hypot(1.,tau)


def times(n, fs):
    return (np.arange(n)-(n-1)/2)/fs


def carrier_components(z, f, g, fs=1000.):
    n=len(z);t=times(n,fs);uf=np.exp(2j*np.pi*f*t)
    delta=(g-f+fs/2)%fs-fs/2
    if delta == 0.:
        return dict(rank=1,a=0.,b=float(np.linalg.norm(z-uf*np.vdot(uf,z)/n)))
    # expm1 avoids subtraction of nearly equal tones near the rank-one limit.
    e=np.expm1(2j*np.pi*delta*t);v=uf*(e-e.mean())
    v/=np.linalg.norm(v)
    d=np.vdot(v,z);res=z-uf*np.vdot(uf,z)/n-v*d
    return dict(rank=2,a=float(abs(d)),b=float(np.linalg.norm(res)))


def carrier_accepts(z,f,g,alpha,q,fs=1000.):
    r=carrier_components(z,f,g,fs)
    if r['rank']==1:
        return True
    tau=ratio_tau(1,len(z)-2,alpha)
    return cone_distance(r['a'],r['b'],tau)<=q


def amplitude_disk(z,f,alpha,q,fs=1000.):
    n=len(z);u=np.exp(2j*np.pi*f*times(n,fs));c=np.vdot(u,z)/n
    b=float(np.linalg.norm(z-c*u));tau=ratio_tau(1,n-1,alpha)
    radius=(tau*b+q*math.hypot(1.,tau))/math.sqrt(n)
    return c,radius


def global_carrier_arc(z,g,alpha,q,fs=1000.):
    """Conservative continuous arc if the Dirichlet outer bound is useful.

    Frequency is always modulo fs. The extra .999 factor makes the far-region
    inequality strict in real arithmetic; it is not a formal floating proof.
    """
    n=len(z);z_norm=float(np.linalg.norm(z));tau=ratio_tau(1,n-2,alpha)
    if z_norm==0:
        return dict(half_width_Hz=fs/2,strict_margin=None)
    ug=np.exp(2j*np.pi*g*times(n,fs))/math.sqrt(n)
    R=float(abs(np.vdot(ug,z))/z_norm)
    m=R-tau-q*math.hypot(1.,tau)/z_norm
    if m<=1/n:
        return dict(half_width_Hz=fs/2,strict_margin=None,R=R,m=m)
    k=.999*m
    if k<=1/n:
        return dict(half_width_Hz=fs/2,strict_margin=None,R=R,m=m)
    D=fs/math.pi*math.asin(1/(n*k))
    return dict(half_width_Hz=D,strict_margin=m-k,R=R,m=m)


def spectral_parts(z,f,fs=1000.):
    n=len(z);t=times(n,fs);freq=np.fft.fftfreq(n,1/fs)
    h=np.abs(freq)>=fs/4;l=(np.abs(freq)>0)&(~h)
    coeff=np.fft.fft(z*np.exp(-2j*np.pi*f*t))/math.sqrt(n)
    return float(np.linalg.norm(coeff[l])),float(np.linalg.norm(coeff[h])),int(l.sum()),int(h.sum())


def color_score(z,f,tau,low_tail=True,fs=1000.):
    a,b,_,_=spectral_parts(z,f,fs)
    if not low_tail:a,b=b,a
    return a-tau*b


def color_arc_exclusion(z,g,alpha_record,q,fs=1000.,max_step=.01):
    """Conservative in exact arithmetic; float output is a diagnostic only.

    Uses alpha/2 for carrier and alpha/4 for each color tail. No independence
    of these three statistics or across records is assumed by the union bound.
    """
    arc=global_carrier_arc(z,g,alpha_record/2,q,fs)
    if arc['half_width_Hz']>=fs/2:
        return dict(arc=arc,numerically_excluded=False,reason='no useful global carrier arc')
    D=arc['half_width_Hz'];cells=max(1,math.ceil(2*D/max_step))
    step=2*D/cells;freq=g-D+(np.arange(cells)+.5)*step
    _,_,r,s=spectral_parts(z,g,fs)
    tauL=ratio_tau(r,s,alpha_record/4);tauH=ratio_tau(s,r,alpha_record/4)
    lipschitz_base=2*math.pi*float(np.linalg.norm(times(len(z),fs)*z))
    marginL=(1+tauL)*lipschitz_base*step/2+q*math.hypot(1.,tauL)
    marginH=(1+tauH)*lipschitz_base*step/2+q*math.hypot(1.,tauH)
    bounds=[];qnorm=float(np.linalg.norm(z))
    for f in freq:
        a,b,_,_=spectral_parts(z,float(f),fs)
        # Either tail may reject a cell. If a cell remains, the result is inconclusive.
        bounds.append(max(a-tauL*b-marginL,b-tauH*a-marginH))
    margin=min(bounds)
    return dict(arc=arc,cells=cells,mesh_Hz=step,minimum_lower_score=margin,
                normalized_lower_score=margin/qnorm if qnorm else None,
                numerically_excluded=bool(margin>0),
                color_low_rank=r,color_high_rank=s,tau_low=tauL,tau_high=tauH,
                roundoff_certified=False)


def controls():
    out=[];rng=np.random.default_rng(20261015)
    # Construct the nearest radial point on the cone, including b=0.
    for a,b,tau in [(4.,1.,.5),(0.,0.,2.),(3.,0.,2.),(1.,4.,.4),(2.,3.,0.)]:
        d=cone_distance(a,b,tau)
        if a>tau*b:
            bp=(tau*a+b)/(1+tau*tau);ap=tau*bp
        else:ap,bp=a,b
        assert abs(math.hypot(a-ap,b-bp)-d)<1e-12
        assert ap<=tau*bp+1e-14
        out.append(dict(control='cone_nearest_witness',a=a,b=b,tau=tau))
    n=40;fs=100.;t=times(n,fs);z=rng.normal(size=n)+1j*rng.normal(size=n)
    for f,g in [(2.,2.),(2.,2.+1e-10),(2.,7.),(-49.,49.)]:
        v=carrier_components(z,f,g,fs)
        uf=np.exp(2j*np.pi*f*t);ug=np.exp(2j*np.pi*g*t)
        if v['rank']==2:
            Q,_=np.linalg.qr(np.column_stack([uf,ug]));normS=np.linalg.norm(Q.conj().T@z)**2
            normf=abs(np.vdot(uf,z))**2/n
            if abs(f-g)>1e-6:
                assert abs(v['a']**2-(normS-normf))<1e-10
                assert abs(v['b']**2-(np.vdot(z,z).real-normS))<1e-10
        else:assert carrier_accepts(z,f,g,.01,0.,fs)
        out.append(dict(control='orthogonal_projection',f=f,g=g,rank=v['rank']))
    for alpha in [.1,.01,1e-5]:
        tau=ratio_tau(1,38,alpha)
        assert abs(tau*tau-f_law.isf(alpha,2,76)/38)<1e-10
        out.append(dict(control='rank_one_tail_formula',alpha=alpha))
    for f,g in [(1.,3.),(-49.,49.),(2.,2.+1e-8)]:
        a,b,r,s=spectral_parts(z,f,fs);assert r+s==n-1
        energy=a*a+b*b;u=np.exp(2j*np.pi*f*t)
        assert abs(energy-(np.vdot(z,z).real-abs(np.vdot(u,z))**2/n))<1e-10
        r1,s1,_,_=spectral_parts(z,g,fs)
        L=2*math.pi*np.linalg.norm(t*z)
        assert abs(a-r1)<=L*abs(g-f)+1e-10
        assert abs(b-s1)<=L*abs(g-f)+1e-10
        out.append(dict(control='color_parseval_lipschitz',f=f,g=g))
    # Scaling both the data and its quantizer radius leaves every test unchanged.
    for f in [1.,3.,40.]:
        assert carrier_accepts(z,f,2.,.01,1.,fs)==carrier_accepts(17*z,f,2.,.01,17.,fs)
        c,rad=amplitude_disk(z,f,.01,1.,fs);cc,rr=amplitude_disk(17*z,f,.01,17.,fs)
        assert abs(cc-17*c)<1e-12 and abs(rr-17*rad)<1e-12
        out.append(dict(control='scale_equivariance',f=f))
    # A large discrepancy aligned with the numerator defeats covariance-only claims.
    # Equal covariance can still have atomic, nonuniform directions: choose a
    # random coordinate with random phase. Its ratio is zero or infinite.
    atom_reject_probability=1/n
    assert atom_reject_probability>.01
    out.append(dict(control='isotropic_covariance_is_insufficient',dimension=n,
                    nominal_tail=.01,actual_atomic_tail=atom_reject_probability))
    # Pure tones must never be excluded by the full finite-arc search.
    for f in [-49.8,.123,49.8]:
        zz=(3+2j)*np.exp(2j*np.pi*f*t)
        res=color_arc_exclusion(zz,f+.03,.01,0.,fs,max_step=.03)
        assert not res['numerically_excluded'],res
        out.append(dict(control='pure_tone_not_rejected',f=f))
    # Returned outer arc must actually satisfy the Dirichlet sufficient bound.
    zz=20*np.exp(2j*np.pi*2*t)+.2*z
    arc=global_carrier_arc(zz,2.03,.01,math.sqrt(2*n),fs)
    assert arc['half_width_Hz']<fs/2
    k_bound=1/(n*math.sin(math.pi*arc['half_width_Hz']/fs))
    assert k_bound<arc['m']
    for ff in np.linspace(-fs/2,fs/2,401,endpoint=False):
        d=abs((ff-2.03+fs/2)%fs-fs/2)
        if d>=arc['half_width_Hz']:
            assert not carrier_accepts(zz,float(ff),2.03,.01,math.sqrt(2*n),fs)
    out.append(dict(control='global_dirichlet_outer_exclusion'))
    # The ADC term is necessary even for an adversarial radial perturbation.
    tau=.4;a=tau*3.;b=3.;q=.7
    aa=a+q/math.hypot(1,tau);bb=b-q*tau/math.hypot(1,tau)
    assert abs(cone_distance(aa,bb,tau)-q)<1e-12
    out.append(dict(control='adversarial_quantizer_boundary'))
    # Direct orthogonal-mode witness for carrier cell enlargement.
    u0=np.ones(n,dtype=complex)/math.sqrt(n)
    u1=np.exp(2j*np.pi*(fs/n)*t)/math.sqrt(n)
    u2=np.exp(2j*np.pi*(2*fs/n)*t)/math.sqrt(n)
    tau=ratio_tau(1,n-2,.01);q=.7;b=3.
    zz=10*u0+(tau*b+q*math.hypot(1,tau))*u1+b*u2
    assert carrier_accepts(zz,0.,fs/n,.01,q+1e-10,fs)
    assert not carrier_accepts(zz,0.,fs/n,.01,0.,fs)
    out.append(dict(control='carrier_adc_boundary_modes'))
    # Attain the amplitude disk boundary with an actual analog perturbation.
    zz=(2+3j)*math.sqrt(n)*u0+3*u1;q=.7
    center,radius=amplitude_disk(zz,0.,.01,q,fs)
    c_true=center+radius;tau=ratio_tau(1,n-1,.01)
    a=math.sqrt(n)*radius;b=3.
    bp=(tau*a+b)/(1+tau*tau);ap=tau*bp
    analog=c_true*math.sqrt(n)*u0-ap*u0+bp*u1
    assert abs(np.linalg.norm(zz-analog)-q)<1e-11
    assert abs(abs(np.vdot(u0,analog-c_true*math.sqrt(n)*u0))-tau*np.linalg.norm(analog-u0*np.vdot(u0,analog)))<1e-11
    out.append(dict(control='amplitude_disk_attained_adc_boundary'))
    return out
