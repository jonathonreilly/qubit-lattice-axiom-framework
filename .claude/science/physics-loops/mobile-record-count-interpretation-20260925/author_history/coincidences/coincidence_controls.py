"""Author controls for two original marks and optical coincidence normalization.

Finite Fock operators check the independently hand-derived Gaussian moments.
Finite-g rows are uncut Gaussian initial-effect values, not full dynamics.
Spatial rows are static Fourier diagnostics of two translated local probes.
"""
from pathlib import Path
from itertools import product
import hashlib, json, time
import numpy as np
import mpmath as mp


def position(state, axis):
    x=np.moveaxis(state,axis,0); out=np.zeros_like(x)
    for n in range(1,len(x)):
        out[n-1]+=np.sqrt(n)*x[n]
        out[n]+=np.sqrt(n)*x[n-1]
    return np.moveaxis(out,0,axis)


def formula(v1,v2,c,chi1,chi2):
    a1=abs(chi1)**2; a2=abs(chi2)**2; cross=float(np.real(np.conj(chi1)*chi2))
    m1=v1+2*a1; m2=v2+2*a2
    fourth=v1*v2+2*c*c+2*v1*a2+2*v2*a1+8*c*cross
    corrected=(c*c+4*c*cross)/(2*a1*a2) if a1*a2>1e-28 else None
    return {'v1':v1,'v2':v2,'c':c,'A1':a1,'A2':a2,'Re_chi1_star_chi2':cross,
        'second1':m1,'second2':m2,'fourth':fourth,'raw_ratio':fourth/(m1*m2),
        'rho1':2*a1/m1,'rho2':2*a2/m2,'background_subtracted_ratio':corrected}


def gaussian_finite_g(v1,v2,c,chi1,chi2,g):
    d=lambda x:mp.mpf(str(float(x)))
    v1,v2,c,g=map(d,(v1,v2,c,g));a1=d(abs(chi1)**2);a2=d(abs(chi2)**2)
    cross=d(np.real(np.conj(chi1)*chi2));g2=g*g
    z1=1-mp.exp(-g2*v1/2);z2=1-mp.exp(-g2*v2/2)
    s1=g2*a1*mp.exp(-g2*v1/2);s2=g2*a2*mp.exp(-g2*v2/2)
    one1=z1+s1;one2=z2+s2
    def char(v,a):return mp.exp(-g2*v/2)*(1-g2*a)
    joint=1-char(v1,a1)-char(v2,a2)+(char(v1+v2+2*c,a1+a2+2*cross)+char(v1+v2-2*c,a1+a2-2*cross))/2
    correction=(joint-z1*one2-z2*one1+z1*z2)/(s1*s2) if a1*a2>mp.mpf('1e-28') else None
    assert joint>=0 and one1>=0 and one2>=0
    return {'g':str(g),'joint_effect_over_g4':str(joint/g**4),
            'raw_ratio':str(joint/(one1*one2)),
            'background_subtracted_ratio':str(correction) if correction is not None else None}


def fock_controls():
    seeds=[('balanced_plus',[1,1,0]),('balanced_minus',[1,-1,0]),
           ('balanced_quadrature',[1,1j,0]),('first_mode',[1,0,0]),
           ('unseen_mode',[0,0,1]),('complex_with_tail',[1+1j,2-1j,1-2j])]
    rows=[];v1=1.7;v2=.9
    for r in (0.,.1,-.2,1/3,.8):
        c=r*np.sqrt(v1*v2)
        for label,seed in seeds:
            alpha=np.array(seed,dtype=complex);alpha/=np.linalg.norm(alpha)
            state=np.zeros((6,6,6),dtype=complex)
            for mu in range(3):
                idx=[0,0,0];idx[mu]=1;state[tuple(idx)]=alpha[mu]
            q1=lambda x:np.sqrt(v1)*position(x,0)
            q2=lambda x:np.sqrt(v2)*(r*position(x,0)+np.sqrt(1-r*r)*position(x,1))
            second1=np.vdot(q1(state),q1(state));second2=np.vdot(q2(state),q2(state))
            fourth=np.vdot(state,q1(q1(q2(q2(state)))))
            ch1=np.sqrt(v1)*alpha[0];ch2=np.sqrt(v2)*(r*alpha[0]+np.sqrt(1-r*r)*alpha[1])
            f=formula(v1,v2,c,ch1,ch2)
            residual=max(abs(second1-f['second1']),abs(second2-f['second2']),abs(fourth-f['fourth']))
            assert residual<2e-13
            assert abs(f['raw_ratio']-(1-f['rho1']*f['rho2']+f['rho1']*f['rho2']*(f['background_subtracted_ratio'] or 0)))<2e-13 or f['background_subtracted_ratio'] is None
            if r==0:
                assert f['raw_ratio']>=.75-1e-14
                if f['background_subtracted_ratio'] is not None:assert f['background_subtracted_ratio']==0
            rows.append({'correlation_r':r,'packet':label,**f,'Fock_moment_max_residual':float(residual),
                'finite_g_uncut_initial_effect_rows':[gaussian_finite_g(v1,v2,c,ch1,ch2,g) for g in (.2,.1,.05,.025)]})
    return rows


def spatial_controls(L,separations):
    axis=2*np.pi*np.arange(L)/L;k=np.array(list(product(axis,repeat=3)))
    components=4*np.sin(k/2)**2;omega=np.sqrt(components.sum(axis=1));keep=omega>0
    k=k[keep];omega=omega[keep];xy=components[keep,:2].sum(axis=1);V=L**3
    weight=xy/(2*V*omega);vp=float(weight.sum());rows=[]
    for R in separations:
        phase=np.cos(k[:,0]*R);c=float(np.dot(weight,phase))
        for eps in (.4,.7,1.,3.5):
            band=omega<=eps;vlow=float(weight[band].sum());clow=float(np.dot(weight[band],phase[band]))
            denominator=vlow+clow
            if denominator<=1e-25:rows.append({'L':L,'separation':R,'epsilon':eps,'packet_available':False});continue
            # alpha is the normalized sum of the two band-projected mode vectors.
            A=denominator/2;chi=np.sqrt(A)
            mean=float(np.dot(weight[band]*omega[band],1+phase[band])/denominator)
            assert mean<=eps+1e-12
            f=formula(vp,vp,c,chi,chi)
            rows.append({'L':L,'separation':R,'epsilon':eps,'packet_available':True,
                'mean_reference_frequency':mean,'v_band':vlow,'band_covariance':clow,
                'full_vacuum_correlation_r':c/vp,**f})
    return rows


if __name__=='__main__':
    tic=time.perf_counter();mp.mp.dps=70
    result={'scope':__doc__,'fock_rows':fock_controls(),
        'spatial_rows':spatial_controls(32,(12,))+spatial_controls(64,(12,16,24)),
        'primary_normalization_illustration':{'rho':'0.34','raw_normalized_value_for_hypothetical_corrected_zero':'0.8844','status':'Algebraic normalization example, not a measured coincidence fit or an identification of experimental stray background with model vacuum.'},
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'elapsed_seconds':time.perf_counter()-tic}
    print(json.dumps(result,indent=2,allow_nan=False))
