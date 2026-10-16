"""Constructed conditioning and an omission survivor with physical residuals.

The finite-field/noise protocol is attributed to the focused independent check;
this source regenerates its records rather than reading historical output.
"""
AUDIT_TIMEOUT_SEC = 120
import numpy as np
import sympy as s
from numpy.polynomial.legendre import leggauss, legval


def modal_inputs(omit_path=False, radius=s.Integer(1)):
    eta=s.symbols('eta',negative=True);r=s.symbols('r',positive=True)
    a=256/eta**8;dt=lambda z:s.diff(z,eta)/a
    L=lambda z:(s.diff(z,eta)+s.diff(z,r))/a;h=dt(a)/a
    reception=eta+r;gain=(reception+11)/10
    rows=[];target=[]
    for i in range(24):
        n=[0,3,4,5][i%4];ell=i+2
        # These ratios solve the original four-state eigensystem, checked in core.
        j=s.Rational(n*n-10*n+20,8-n)
        vel=-2*s.Rational(4-n,8-n)
        P=eta**n*r**ell;Z=-128*vel*eta**(n-7)*r**ell
        Y=-(1+j)*P+s.diff(Z,r)/a
        integral=sum(s.binomial(n,k)*reception**(n-k)*(-1)**k*r**(ell+k+1)/s.Integer(ell+k+1) for k in range(n+1))
        X=s.expand(gain*P);B=a*gain*integral
        W=s.expand(gain*Y+(0 if omit_path else integral/5))
        columns=[dt(W),L(W),W,L(L(dt(X))),L(dt(X)),dt(X),L(L(X)),L(X),X,dt(dt(B)),dt(B),B]
        at=lambda x:s.cancel(x).subs({eta:-2,r:radius})
        rows.append([at(z) for z in columns]);target.append(at(-L(dt(W))-h*L(W)-dt(h)*W))
    return s.Matrix(rows),s.Matrix(target)


def run_checks():
    checks=[];details={}
    def check(name,condition):checks.append({'name':name,'pass':bool(condition)})
    M,y=modal_inputs();truth,_=M.gauss_jordan_solve(y)
    check('actual_one_shell_exact_common_rank',M.rank()==12 and M.row_join(y).rank()==12)
    nodes,weights=leggauss(48);train=np.arange(0,48,2);test=np.arange(1,48,2)
    amplitudes=np.array([1e-5*np.sqrt((2*(i+2)+1)/2)/(2**([0,3,4,5][i%4])*(i+3)**4) for i in range(24)])
    angular=np.column_stack([legval(nodes,[0]*(i+2)+[1])*amplitudes[i] for i in range(24)])
    weighted=(angular@np.array(M,dtype=float))*np.sqrt(weights)[:,None]
    observed=(angular@np.array(y,dtype=float).ravel())*np.sqrt(weights)
    scales=np.linalg.norm(weighted[train],axis=0);A=weighted/scales
    singular=np.linalg.svd(A[train],compute_uv=False)
    th=np.array(truth,dtype=float).ravel();ztrue=scales*th
    rng=np.random.default_rng(2026101607);dA=rng.normal(size=A[train].shape);dA/=np.linalg.norm(dA,2)
    dy=rng.normal(size=len(train));dy/=np.linalg.norm(dy)
    noise=[]
    for eps in [0.,1e-12,1e-9,1e-6]:
        E=eps*np.linalg.norm(A[train],2)*dA;f=eps*np.linalg.norm(observed[train])*dy
        z,_,rank,_=np.linalg.lstsq(A[train]+E,observed[train]+f,rcond=None)
        got=z/scales;error=np.linalg.norm(z-ztrue)
        margin=singular[-1]-np.linalg.norm(E,2)
        bound=(np.linalg.norm(f)+np.linalg.norm(E,2)*np.linalg.norm(ztrue))/margin if margin>0 else None
        if eps>0:check('scaled_perturbation_bound_'+str(eps),bound is not None and error<=bound)
        else:check('noiseless_numerical_recovery',np.linalg.norm(got-th)/np.linalg.norm(th)<1e-8)
        noise.append({'epsilon':eps,'relative_coefficient_error':float(np.linalg.norm(got-th)/np.linalg.norm(th)),
                      'unused_angular_relative_residual':float(np.linalg.norm(A[test]@z-observed[test])/np.linalg.norm(observed[test])),
                      'recovered_beta':float(-got[9]/4),'scaled_actual_error':float(error),'input_error_bound':float(bound) if bound is not None else None})
    mutant,mutant_y=modal_inputs(True);mutant_theta,_=mutant.gauss_jordan_solve(mutant_y)
    check('omission_exactly_survives_one_shell_fit',mutant.rank()==12 and mutant.row_join(mutant_y).rank()==12)
    check('omission_is_bias_not_rejection_by_known_truth',mutant_theta!=truth)
    extracted=[]
    for rad in [s.Rational(9,10),s.Rational(11,10)]:
        mat,vec=modal_inputs(True,rad);theta,_=mat.gauss_jordan_solve(vec)
        beta=-theta[9]/4;extracted.append((theta[1]+beta,theta[6]+theta[3]*beta))
    dc=s.factor(extracted[1][0]-extracted[0][0]);de=s.factor(extracted[1][1]-extracted[0][1])
    check('omission_rejected_by_inferred_cross_shell_homogeneity',dc!=0 and de!=0)
    # Infer the mutant histories from its exact coefficient identity at reference r=1.
    # Freeze those histories in r before checking homogeneous original equations.
    eta,r=s.symbols('eta r');a=256/eta**8;dt=lambda z:s.diff(z,eta)/a
    h=dt(a)/a;G=(-eta/2)**7;d=2/G;beta=1/(a*(eta+12));C=G/2-beta;e=4-d*beta
    q=h-(e-1)/d;R=C*G;x=s.sqrt(q*G);b=s.sqrt(q/G);ell=h-q
    Ac=(-2/eta)**5*(eta+12)/10;HE=Ac*ell;speed=Ac*x;rE=Ac*Ac*R;bare=Ac*R
    potential=Ac*Ac*(3*ell*ell-x*x/2-R)
    force=(dt(potential)+bare*dt(Ac))/x;K=dt(C)+h*C;kfit=-7*G+2*beta
    at=lambda z:s.simplify(z.subs({eta:-2,r:1}))
    residuals={'Raychaudhuri':at(-2*Ac*dt(HE)-speed*speed-rE),
               'scalar_background':at(Ac*dt(speed)+3*HE*speed+force),
               'bare_dust_background':at(Ac*dt(bare)+3*HE*bare),
               'coefficient_k_consistency':at(dt(K)/K-kfit)}
    for name,value in residuals.items():check('omission_rejected_by_'+name,value!=0)
    details={'data_role':'Constructed original-action controls. Derivative-level perturbations, not primitive noise or observed data.',
             'protocol':'24 solid harmonics, 48 common-shell Gauss-Legendre angles, alternating train/unused rows; frozen baseline column norms; seed2026101607.',
             'scaled_condition_number':float(singular[0]/singular[-1]),'scaled_singular_values':singular.tolist(),
             'noise_cases':noise,'omission_one_shell_coefficients':[str(v) for v in mutant_theta],
             'omission_cross_shell':{'C_difference':str(dc),'e_difference':str(de)},
             'omission_original_residuals':{k:str(v) for k,v in residuals.items()},
             'limits':'The unused angular omission test fails to detect a wrong reconstruction; added cross-shell/original-residual checks are explicitly adaptive. No all-errors robustness claim.'}
    return checks,details
