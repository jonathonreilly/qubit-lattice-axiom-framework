"""Root source-convolution control, explicitly not the microscopic cube.

An exact finite GKLS cascade has one initial state, a three-dimensional born
sector, and a terminal state. The born sector contains a zero-energy low
state and a coupled dark/bright high pair. This tests recent-age integration,
normalization, total variance and the danger of inferring QFI from variance.
"""
from pathlib import Path
import hashlib,json,math,time
import numpy as np
from scipy.linalg import expm,solve_continuous_lyapunov

HERE=Path(__file__).resolve().parent

def subnormalized_fisher(rho,H):
    values,V=np.linalg.eigh((rho+rho.conj().T)/2)
    assert values.min()>-1e-13
    values=np.maximum(values,0);m=V.conj().T@H@V
    denominator=values[:,None]+values[None,:]
    quotient=np.divide((values[:,None]-values[None,:])**2,denominator,
                       out=np.zeros_like(denominator),where=denominator>1e-22)
    return float(2*np.sum(quotient*abs(m)**2))

def controls():
    delta,kappa,g,b,r=1.3,.4,.8,2.,4.
    G=np.array([[0,g],[g,0]],complex)
    bright=np.diag([0.,1.]);dark=np.array([1.,0.],complex)
    D=np.outer(dark,dark.conj());Z=-1j*delta*G-kappa*bright
    X0=solve_continuous_lyapunov(Z,-D)
    assert np.linalg.norm(Z@X0+X0@Z.conj().T+D)<1e-12
    Iinfty=float(np.trace(X0).real)
    age_cap=1.75
    Ecap=expm(age_cap*Z)
    IA=float(np.trace(X0-Ecap@X0@Ecap.conj().T).real)
    assert Iinfty>IA>0
    nodes,weights=np.polynomial.legendre.leggauss(96)
    ages=(nodes+1)*age_cap/2;weights=weights*age_cap/2
    profiles=np.array([expm(tau*Z)@dark for tau in ages])
    quadrature=float(np.dot(weights,np.sum(abs(profiles)**2,axis=1)))
    assert abs(quadrature-IA)<2e-13
    rows=[]
    for t in (.6,1.2):
        q0=math.exp(-kappa*b*t)
        for eps in (.12,.06,.03,.015):
            lam=kappa*(b+eps**2*r);q=math.exp(-lam*t)
            Am=Z+.5*lam*eps**2*np.eye(2)
            X=solve_continuous_lyapunov(Am,-D)
            assert np.linalg.eigvalsh(X).min()>0
            Et=expm((t/eps**2)*Am)
            rh= kappa*eps**4*r*q*(X-Et@X@Et.conj().T)
            rh=(rh+rh.conj().T)/2
            p0=kappa*b*(-math.expm1(-lam*t))/lam
            Kh=-1j*delta*eps**-4*np.eye(2)+eps**-2*Z
            growth=math.exp(lam*t)*np.exp(-1j*delta*t/eps**4)*expm((t/eps**2)*Z)
            cross=kappa*eps*math.sqrt(b*r)*q*np.linalg.solve(lam*np.eye(2)+Kh,(growth-np.eye(2))@dark)
            rho=np.zeros((3,3),complex);rho[0,0]=p0;rho[1:,1:]=rh
            rho[1:,0]=cross;rho[0,1:]=cross.conj()
            terminal=1-q-float(np.trace(rho).real)
            assert terminal>=-1e-12 and np.linalg.eigvalsh(rho).min()>-1e-13
            Hh=delta*eps**-4*(np.eye(2)+eps**2*G)
            H=np.zeros((3,3),complex);H[1:,1:]=Hh
            mean=float(np.trace(H@rho).real)
            second=float(np.trace(H@H@rho).real)
            variance=second-mean**2
            fisher=subnormalized_fisher(rho,H)
            assert variance>0 and 0<=fisher<=4*variance*(1+1e-12)
            scaled_var=eps**4*variance
            target=kappa*delta**2*r*q0*Iinfty

            EA=expm(age_cap*Am)
            rh_recent=kappa*eps**4*r*q*(X-EA@X@EA.conj().T)
            recent_high_probability=float(np.trace(rh_recent).real)
            recent_mean=float(np.trace(Hh@rh_recent).real)
            recent_second=float(np.trace(Hh@Hh@rh_recent).real)
            scaled_within=0.
            Hscaled=delta*(np.eye(2)+eps**2*G)
            for tau,wgt,v in zip(ages,weights,profiles):
                source=kappa*math.exp(-lam*(t-eps**2*tau))
                norm=float(np.vdot(v,v).real)
                mv=float(np.vdot(v,Hscaled@v).real)
                m2=float(np.vdot(Hscaled@v,Hscaled@v).real)
                scaled_within+=wgt*source*(r*m2-eps**2*r*r*mv*mv/(b+eps**2*r*norm))
            recent_target=kappa*delta**2*r*q0*IA
            assert scaled_var>=scaled_within-1e-10
            row={'t':t,'epsilon':eps,'initial_sector_probability':q,
                 'born_low_probability':p0,'born_high_probability':float(np.trace(rh).real),
                 'terminal_probability':terminal,'born_density_min_eigenvalue':float(np.linalg.eigvalsh(rho).min()),
                 'full_mean':mean,'limiting_mean':kappa*delta*r*q0*Iinfty,
                 'eps4_full_variance':scaled_var,'limiting_eps4_variance':target,
                 'relative_scaled_variance_error':abs(scaled_var/target-1),
                 'full_Fisher':fisher,'Fisher_over_four_variance':fisher/(4*variance),
                 'high_low_block_norm_over_eps5':float(np.linalg.norm(cross)/eps**5),
                 'recent_high_probability_over_eps4':recent_high_probability/eps**4,
                 'recent_high_probability_target':kappa*r*q0*IA,
                 'recent_mean':recent_mean,'recent_mean_target':kappa*delta*r*q0*IA,
                 'eps4_recent_second_moment':eps**4*recent_second,
                 'eps4_recent_within_path_variance':scaled_within,
                 'recent_variance_target':recent_target,
                 'field_only_mutant_high_probability':0.}
            rows.append(row)
        block=rows[-4:]
        assert block[-1]['relative_scaled_variance_error']<.002
        assert block[-1]['relative_scaled_variance_error']<.3*block[-2]['relative_scaled_variance_error']
        assert abs(block[-1]['eps4_recent_within_path_variance']/recent_target-1)<.002
        assert block[-1]['Fisher_over_four_variance']<1e-5
    return {'parameters':{'delta':delta,'kappa':kappa,'g':g,'b':b,'r':r,'age_cap':age_cap},
            'fast_integral_infinite':Iinfty,'fast_integral_capped':IA,
            'quadrature_absolute_error':abs(quadrature-IA),'rows':rows,
            'scope':'Exact finite toy cascade and source integration only. Not the cube, its large-spin limit, a microscopic N=4 derivation, or a conserving apparatus. A cube QFI upper bound is not inferred.'}

def main():
    started=time.monotonic();result=controls()
    result['elapsed_seconds']=time.monotonic()-started
    result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    data=json.dumps(result,indent=2)+'\n'
    (HERE/'RECENT_BIRTH_CONTROL_RESULTS.json').write_text(data);print(data,end='')
if __name__=='__main__':main()
