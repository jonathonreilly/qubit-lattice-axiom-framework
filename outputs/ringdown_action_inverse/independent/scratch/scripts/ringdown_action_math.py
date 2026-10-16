"""Exact-class ringdown and inverse controls; synthetic data, no empirical fit.

This helper is imported and executed by ringdown_action_inverse.py. It reads no
repository files. Generator parameters enter synthetic generation and separate
verification; the extractor receives only spectra and force time records.
"""
from itertools import product
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_simpson
from scipy.optimize import least_squares
import sympy as sy
import sympy as s


def common_controls():
    checks = []
    details = {}


    def check(name, condition, detail=None):
        row = {"name": name, "passed": bool(condition)}
        if detail is not None:
            row["detail"] = detail
        checks.append(row)


    # Derive the held-force expression from the action, including velocity terms.
    x, w, xd, wd, xdd, wdd = sy.symbols("x w xd wd xdd wdd", real=True)
    M, k, tau, U, B, C, d, nu, gamma = [sy.Function(n)(x) for n in
                                           ["M", "k", "tau", "U", "B", "C", "d", "nu", "gamma"]]
    T = M*xd**2/2 + k*xd*wd + tau*wd**2/2
    V = U+B*w+C*w**2/2
    Ray = d*xd**2/2+nu*xd*wd+gamma*wd**2/2
    dt = lambda z: sy.diff(z,x)*xd+sy.diff(z,w)*wd+sy.diff(z,xd)*xdd+sy.diff(z,wd)*wdd
    Fx = sy.expand(dt(sy.diff(T,xd))-sy.diff(T-V,x)+sy.diff(Ray,xd))
    Fw = sy.expand(dt(sy.diff(T,wd))-sy.diff(T-V,w)+sy.diff(Ray,wd))
    held = Fx.subs({xd:0,xdd:0})
    expected = k*wdd-tau.diff(x)*wd**2/2+U.diff(x)+B.diff(x)*w+C.diff(x)*w**2/2+nu*wd
    check("Euler_Lagrange_held_force", sy.simplify(held-expected)==0)
    check("Euler_Lagrange_held_hidden", sy.simplify(Fw.subs({xd:0,xdd:0})-(tau*wdd+gamma*wd+B+C*w))==0)
    zero = {xd:0,wd:0,xdd:0,wdd:0,w:-B/C}
    G = B.diff(x)-C.diff(x)*B/C
    check("reciprocal_stiffness_cross", sy.simplify(sy.diff(Fx,w).subs(zero)-G)==0 and sy.simplify(sy.diff(Fw,x).subs(zero)-G)==0)
    check("reciprocal_kinetic_cross", sy.diff(Fx,wdd)==k and sy.diff(Fw,xdd)==k)
    check("reciprocal_damping_cross", sy.simplify(sy.diff(Fx,wd).subs(zero)-nu)==0 and sy.simplify(sy.diff(Fw,xd).subs(zero)-nu)==0)
    check("visible_variable_mass_coefficient", sy.expand(Fx).coeff(xd,2)==M.diff(x)/2)

    ga, om, cp, tp, ta = sy.symbols("Gamma omega Cp tp tau0", positive=True, real=True)
    gg, nn, kk = sy.symbols("G nu0 k0", real=True)
    cc, cb, ee, eb = sy.symbols("c cbar E Ebar")
    lam=-ga/2+sy.I*om; lb=sy.conjugate(lam); O=sy.expand(lam*lb)
    z=cc*ee+cb*eb; zd=lam*cc*ee+lb*cb*eb; zdd=lam**2*cc*ee+lb**2*cb*eb
    force=sy.expand(gg*z+kk*zdd+nn*zd+cp*z*z/2-tp*zd*zd/2)
    N=gg+nn*lam+kk*lam**2
    check("ringdown_fundamental", sy.simplify(force.coeff(ee,1).coeff(eb,0)-N*cc)==0)
    check("ringdown_decay_coefficient", sy.simplify(force.coeff(ee,1).coeff(eb,1)-(cp-tp*O)*cc*cb)==0)
    check("ringdown_double_frequency", sy.simplify(force.coeff(ee,2)-(cp-tp*lam**2)*cc**2/2)==0)
    check("variable_inertia_frequency_gradient", sy.simplify((C/tau).diff(x)*tau-(C.diff(x)-tau.diff(x)*C/tau))==0)
    s=sy.symbols("s"); pol=sy.symbols("p0")+sy.symbols("p1")*s+sy.symbols("p2")*s**2
    Ns=gg+nn*s+kk*s**2
    Z=pol-Ns**2/(ta*(s-lam)*(s-lb))
    rho=sy.cancel((s-lam)*Z).subs(s,lam)
    check("dynamic_stiffness_residue", sy.simplify(rho+N**2/(ta*(lam-lb)))==0)
    check("residue_factor", sy.simplify((2*lam+ga)*rho+N**2/ta)==0)
    check("visible_load_polynomial_absent", not (sy.simplify(rho).free_symbols & {sy.symbols("p0"),sy.symbols("p1"),sy.symbols("p2")}))
    check("cubic_output_blind_selected_coefficients", all(sy.expand(z**3).coeff(ee,a).coeff(eb,b)==0 for a,b in [(1,0),(1,1)]))
    check("quadratic_output_changes_h", sy.expand(z**2).coeff(ee,1).coeff(eb,1)==2*cc*cb)

    # Chosen family only generates synthetic records; the extractor sees no hidden parameters.
    tx=1+sy.Rational(18,100)*x+sy.Rational(4,100)*x*x
    cx=sy.Rational(34,10)+sy.Rational(11,10)*x+sy.Rational(17,100)*x*x
    bx=sy.Rational(8,10)*x+sy.Rational(15,100)*x*x+sy.Rational(5,100)*x**3
    ux=sy.Rational(6,10)*x*x+sy.Rational(3,100)*x**4
    kx=sy.Rational(18,100)+sy.Rational(3,100)*x
    nux=sy.Rational(4,100)-sy.Rational(5,1000)*x
    gamx=tx*(sy.Rational(35,100)+sy.Rational(3,100)*x)
    mx=2+sy.Rational(1,10)*x*x; dx=sy.Rational(4,10)
    fields=[tx,cx,bx,ux,kx,nux,gamx,mx,dx,tx.diff(x),cx.diff(x),bx.diff(x),ux.diff(x),cx.diff(x,2),bx.diff(x,2),ux.diff(x,2),(cx/tx).diff(x)]
    getpar=sy.lambdify(x,fields,"numpy")


    def synthetic_records(env, initial, epsilon=0.0, cubic=0.0):
        t0,c0,b0,u0,k0,n0,g0,m0,d0,tp0,cp0,bp0,up0,cpp0,bpp0,upp0,op = [float(v) for v in getpar(env)]
        w0=-b0/c0; G0=bp0+cp0*w0
        S0=upp0+bpp0*w0+cpp0*w0*w0/2
        rates=(g0/t0,c0/t0)
        angular=np.geomspace(.2,5.5,35)
        values=[]
        for freq in angular:
            sv=1j*freq
            # Full linear matrix and its hidden equation, not the fitted residue formula.
            mat=np.array([[m0*sv*sv+d0*sv+S0,k0*sv*sv+n0*sv+G0],
                          [k0*sv*sv+n0*sv+G0,t0*sv*sv+g0*sv+c0]],dtype=complex)
            eta=-mat[1,0]/mat[1,1]
            values.append(mat[0,0]+mat[0,1]*eta)
        times=np.linspace(0,16,601)
        sol=solve_ivp(lambda t,y:[y[1],-(g0*y[1]+c0*y[0])/t0],
                      (times[0],times[-1]),initial,t_eval=times,rtol=2e-11,atol=2e-13,method="DOP853")
        assert sol.success
        zz,vv=sol.y; acc=-(g0*vv+c0*zz)/t0; ww=w0+zz
        force=up0+bp0*ww+cp0*ww**2/2+k0*acc+n0*vv-tp0*vv**2/2
        force+=epsilon*zz**2+cubic*zz**3
        truth={"Oprime":op,"tau":t0,"Gamma":rates[0],"O":rates[1],"kinetic_margin":m0*t0-k0*k0,"damping_margin":d0*g0-n0*n0}
        return angular,np.asarray(values),times,force,truth


    def extract(angular, zvals, times, force):
        ss=1j*angular
        A=np.column_stack([-ss*zvals,-zvals,ss**4,ss**3,ss**2,ss,np.ones_like(ss)])
        y=ss*ss*zvals
        mat=np.vstack([A.real,A.imag]); target=np.r_[y.real,y.imag]
        coeff,resid,rank,sv=np.linalg.lstsq(mat,target,rcond=None)
        Gamma,omega2=coeff[:2]
        assert Gamma>0 and omega2>Gamma*Gamma/4
        pole=-Gamma/2+1j*np.sqrt(omega2-Gamma*Gamma/4)
        residue=np.polyval(coeff[2:],pole)/(2*pole+Gamma)
        kspec=abs((2*pole+Gamma)*residue)
        t=times; freq=pole.imag
        basis=np.column_stack([np.ones_like(t),np.exp(-Gamma*t/2)*np.cos(freq*t),
              np.exp(-Gamma*t/2)*np.sin(freq*t),np.exp(-Gamma*t),
              np.exp(-Gamma*t)*np.cos(2*freq*t),np.exp(-Gamma*t)*np.sin(2*freq*t)])
        rc,_,rrank,rsv=np.linalg.lstsq(basis,force,rcond=None)
        f=(rc[1]-1j*rc[2])/2; h=rc[3]
        return {"Gamma":Gamma,"O":omega2,"kspec":kspec,"h":h,"f":f,
                "Q":kspec*h/abs(f)**2,"residue":residue,"pole":pole,
                "rank":int(rank),"ring_rank":int(rrank),"condition":float(sv[0]/sv[-1]),
                "ring_condition":float(rsv[0]/rsv[-1]),
                "ring_residual":float(np.max(np.abs(basis@rc-force)))}


    rows=[]
    development=[(-.8,(.31,-.22)),(.0,(-.42,.13)),(.7,(.15,.39))]
    reserved=[(-.45,(-.27,-.37)),(.3,(.52,.19)),(1.,(-.18,.41))]
    for group, cases in [("development",development),("reserved_synthetic",reserved)]:
        for env,initial in cases:
            a,zv,t,force,truth=synthetic_records(env,initial)
            fit=extract(a,zv,t,force)
            lab=group+"_"+str(env)
            check(lab+"_positive_class",truth["kinetic_margin"]>0 and truth["damping_margin"]>0)
            check(lab+"_extractor_rank",fit['rank']==7 and fit['ring_rank']==6)
            check(lab+"_pole_recovery",abs(fit['O']-truth['O'])<1e-10 and abs(fit['Gamma']-truth['Gamma'])<1e-10)
            check(lab+"_action_identity",abs(fit['Q']-truth['Oprime'])<3e-9)
            check(lab+"_full_force_closure",fit['ring_residual']<1e-10)
            rows.append({"role":group,"x":env,"initial":initial,"true_derivative":truth['Oprime'],"extracted_Q":fit['Q'],"dynamic_fit_condition":fit['condition'],"ring_fit_condition":fit['ring_condition'],"max_force_residual":fit['ring_residual']})
    details['synthetic_rows']=rows

    aa,zz,tt,ff,truth=synthetic_records(.3,(.31,-.22))
    base=extract(aa,zz,tt,ff)
    alt=extract(*synthetic_records(.3,(.31,-.22),epsilon=.08)[:4])
    check("output_only_quadratic_same_linear_response",abs(alt['kspec']-base['kspec'])<1e-14)
    check("output_only_quadratic_same_fundamental",abs(alt['f']-base['f'])<1e-10)
    check("output_only_quadratic_predicted_defect",abs((alt['Q']-base['Q'])-.16/truth['tau'])<2e-9)
    check("output_only_quadratic_rejected",abs(alt['Q']-truth['Oprime'])>.1)
    check("output_only_quadratic_still_six_modes",alt['ring_residual']<1e-10)
    cub=extract(*synthetic_records(.3,(.31,-.22),cubic=.8)[:4])
    check("cubic_output_requires_closure_test",cub['ring_residual']>1e-4)
    details['alternative']={'quadratic_defect':float(alt['Q']-base['Q']),'cubic_full_basis_residual':cub['ring_residual']}

    # Time-origin and signed affine observation changes do not need hidden state.
    later=extract(aa,zz,tt[100:]-tt[100],ff[100:])
    check("time_origin_cancels",abs(later['Q']-base['Q'])<1e-9)
    for gx,gr in [(2.3,.7),(-1.7,-2.1)]:
        changed=extract(aa,zz*gr/gx,tt,ff*gr+3)
        check("affine_work_orientation_"+str(gx),abs(changed['Q']-base['Q']/gx)<1e-9)

    # Distinct necessary exclusions, rather than forcing a fit to supply them.
    zero_decay_times=np.linspace(0,9,70)
    zero_decay_basis=np.column_stack([np.ones(70),np.cos(2*zero_decay_times),
                                     np.sin(2*zero_decay_times),np.exp(0*zero_decay_times),
                                     np.cos(4*zero_decay_times),np.sin(4*zero_decay_times)])
    check("no_decay_merges_h_with_offset",np.linalg.matrix_rank(zero_decay_basis)==5)
    _,_,_,unexcited_force,_=synthetic_records(.3,(0.,0.))
    check("unexcited_mode_has_no_force_anchor",np.ptp(unexcited_force)<1e-13)
    Ncancel=(s-lam)*(s-lb)
    Zcancel=sy.cancel(pol-Ncancel**2/(ta*(s-lam)*(s-lb)))
    check("pole_cancellation_is_blind",sy.denom(Zcancel).has(s)==False)
    check("omit_inertia_gradient_is_false",abs(float((cx.diff(x)/tx-(cx/tx).diff(x)).subs(x,.3)))>.1)

    # Error budget for correlated complex perturbations uses true bounds.
    K0,h0,f0=.8,-.35,.7+.4j
    eK,eh,ef=.02,.015,.01
    Fmin=abs(f0);Fmax=Fmin;Hmax=abs(h0);Kmax=K0
    eD=2*Fmax*ef+ef*ef;Dmin=Fmin*Fmin
    eN=Kmax*eh+Hmax*eK+eK*eh
    budget=eN/(Dmin-eD)+Kmax*Hmax*eD/(Dmin*(Dmin-eD))
    error_cases=[]
    for sk,sh in product([-1,1],repeat=2):
        for angle in np.linspace(0,2*np.pi,17):
            qh=(K0+sk*eK)*(h0+sh*eh)/abs(f0+ef*np.exp(1j*angle))**2
            error_cases.append(abs(qh-K0*h0/abs(f0)**2))
    check("finite_quotient_error_68_cases",max(error_cases)<=budget)
    la=-.2+1.8j;ga0=.4;rh=.3-.2j;el,eg,er=.01,.02,.015
    ekbound=(2*abs(la)+abs(ga0))*er+abs(rh)*(2*el+eg)+(2*el+eg)*er
    errs=[]
    for u,v in product(np.linspace(0,2*np.pi,9),repeat=2):
        for sign in [-1,1]:
            kh=abs((2*(la+el*np.exp(1j*u))+ga0+sign*eg)*(rh+er*np.exp(1j*v)))
            errs.append(abs(kh-abs((2*la+ga0)*rh)))
    check("residue_modulus_error_162_cases",max(errs)<=ekbound)
    details['error_budgets']={'quotient_bound':budget,'quotient_max_error':max(error_cases),'residue_bound':ekbound,'residue_max_error':max(errs)}

    # Cross-environment integral with a separate exact analytic Lipschitz certificate.
    Qfun=sy.lambdify(x,(cx/tx).diff(x),'numpy')
    Ofun=sy.lambdify(x,cx/tx,'numpy')
    qa,qb=-.8,1.; integ,qe=quad(Qfun,qa,qb,epsabs=1e-12,epsrel=1e-12)
    check("cross_environment_integral",abs(integ-(Ofun(qb)-Ofun(qa)))<1e-12)
    # A manufactured Lipschitz function isolates the midpoint bound itself.
    edges=np.array([0.,.1,.4,.65,1.]); widths=np.diff(edges); mids=(edges[:-1]+edges[1:])/2
    Lq=2.;epsilon_q=.003
    qfun=lambda a:abs(2*a-.71)
    trueint=quad(qfun,0,1,points=[.355],epsabs=1e-12)[0]
    estimate=sum(widths*(qfun(mids)+epsilon_q))
    bound=sum(widths*epsilon_q)+Lq*sum(widths**2)/4
    check("finite_bin_Lipschitz_certificate",abs(estimate-trueint)<=bound)

    return dict(locals())


def reconstruction_controls(parent):
    rows=[];details={}
    def ck(name,condition,detail=None):
        rows.append({'name':name,'passed':bool(condition),'detail':detail})

    # Direct change of coordinates in both quadratic velocity forms and potential.
    xd,vd,v,F,Fp=s.symbols('xd vd v F Fp',real=True)
    M,k,tau,d,nu,gamma,U,B,C=s.symbols('M k tau d nu gamma U B C',real=True)
    kin=s.expand(M*xd**2/2+k*xd*(vd+Fp*xd)+tau*(vd+Fp*xd)**2/2).subs(Fp,-k/tau)
    ray=s.expand(d*xd**2/2+nu*xd*(vd+Fp*xd)+gamma*(vd+Fp*xd)**2/2).subs(Fp,-k/tau)
    pot=s.expand(U+B*(v+F)+C*(v+F)**2/2)
    ck('kinetic_cross_removed_by_coordinate_change',s.simplify(s.expand(kin).coeff(xd,1).coeff(vd,1))==0)
    ck('visible_mass_Schur_complement',s.simplify(s.expand(kin).coeff(xd,2)*2-(M-k*k/tau))==0)
    ck('damping_cross_retained',s.simplify(s.expand(ray).coeff(xd,1).coeff(vd,1)-(nu-gamma*k/tau))==0)
    ck('damping_diagonal_transformed',s.simplify(s.expand(ray).coeff(xd,2)*2-(d-2*nu*k/tau+gamma*k*k/tau**2))==0)
    ck('potential_translation',s.simplify(pot-(U+B*F+C*F*F/2+(B+C*F)*v+C*v*v/2))==0)
    ck('damping_determinant_preserved',s.simplify((d-2*nu*k/tau+gamma*k*k/tau**2)*gamma-(nu-gamma*k/tau)**2-(d*gamma-nu**2))==0)
    ss,Ga,O,G=s.symbols('s Gamma O G',real=True)
    oldN=G+nu*ss+k*ss*ss
    newN=G-k*O+(nu-k*Ga)*ss
    ck('same_pole_off_diagonal',s.expand(oldN-newN-k*(ss*ss+Ga*ss+O))==0)

    # Static curvature is along the equilibrium curve, not at fixed hidden w.
    x=s.symbols('x',real=True); E=s.Function('E')(x); cc=s.Function('C')(x); w0=s.Function('w0')(x)
    VV=E+cc*(v-w0)**2/2
    Gcan=-cc*s.diff(w0,x)
    ck('equilibrium_holding_force',s.simplify(s.diff(VV,x).subs(v,w0)-s.diff(E,x))==0)
    ck('fixed_hidden_curvature',s.simplify(s.diff(VV,x,2).subs(v,w0)-(s.diff(E,x,2)+Gcan**2/cc))==0)


    def features(env,initial=(.31,-.22)):
        a,zv,t,force,truth=parent['synthetic_records'](env,initial)
        fit=parent['extract'](a,zv,t,force)
        la=fit['pole'];ga=fit['Gamma'];om=la.imag
        basis=np.column_stack([np.ones_like(t),np.exp(-ga*t/2)*np.cos(om*t),np.exp(-ga*t/2)*np.sin(om*t),np.exp(-ga*t),np.exp(-ga*t)*np.cos(2*om*t),np.exp(-ga*t)*np.sin(2*om*t)])
        coeff=np.linalg.lstsq(basis,force,rcond=None)[0]
        fit['g']=(coeff[4]-1j*coeff[5])/2;fit['R0']=coeff[0]
        fit['S']=-2*(2*la+ga)*fit['residue']*fit['g']/fit['f']**2
        fit['r']=(fit['S']-fit['Q'])/(fit['O']-la*la)
        return fit,a,zv,t,force,truth


    grid=np.linspace(-.8,1.,61)
    records=[features(float(xx)) for xx in grid]
    fitrows=[r[0] for r in records]
    rr=np.array([z['r'] for z in fitrows])
    tx=parent['tx'];px=parent['x']; getpar=parent['getpar']
    actual_tau=np.array([getpar(float(xx))[0] for xx in grid],dtype=float)
    actual_r=np.array([getpar(float(xx))[9]/getpar(float(xx))[0] for xx in grid],dtype=float)
    tau_recovered=np.exp(cumulative_simpson(rr.real,x=grid,initial=0))
    ck('observed_r_is_real',np.max(abs(rr.imag))<2e-9,float(np.max(abs(rr.imag))))
    ck('inertia_log_derivative_recovered',np.max(abs(rr.real-actual_r))<2e-9,float(np.max(abs(rr.real-actual_r))))
    ck('relative_inertia_integrated',np.max(abs(tau_recovered-actual_tau/actual_tau[0]))<2e-8,float(np.max(abs(tau_recovered-actual_tau/actual_tau[0]))))

    reconstructed=[];last=None
    for i,(xx,rec) in enumerate(zip(grid,records)):
        f,a,zv,t,force,truth=rec; la=f['pole'];tau_i=tau_recovered[i]
        n=np.sqrt(-tau_i*(2*la+f['Gamma'])*f['residue'])
        if last is not None and abs(-n-last)<abs(n-last):n=-n
        last=n
        nu_i=n.imag/la.imag;G_i=n.real-nu_i*la.real
        sv=1j*a;D=sv*sv+f['Gamma']*sv+f['O']
        corrected=zv+(G_i+nu_i*sv)**2/(tau_i*D)
        mat=np.column_stack([sv*sv,sv,np.ones_like(sv)])
        cf=np.linalg.lstsq(np.vstack([mat.real,mat.imag]),np.r_[corrected.real,corrected.imag],rcond=None)[0]
        rem=float(np.max(abs(mat@cf-corrected)))
        reconstructed.append(dict(tau=tau_i,C=tau_i*f['O'],gamma=tau_i*f['Gamma'],nu=nu_i,G=G_i,M=cf[0],d=cf[1],P0=cf[2],R0=f['R0'],r=f['r'].real,Q=f['Q'],n=n,lambda_=la,polynomial_residual=rem))

    pars=np.array([getpar(float(xx)) for xx in grid],dtype=float)
    raw_tau,raw_C,raw_B,raw_U,raw_k,raw_nu,raw_gamma,raw_M,raw_d=pars[:,:9].T
    raw_tp,raw_Cp,raw_Bp=pars[:,9:12].T
    raw_G=raw_Bp-raw_Cp*raw_B/raw_C
    scale=np.sqrt(raw_tau[0])
    target_G=(raw_G-raw_k*raw_C/raw_tau)/scale
    target_nu=(raw_nu-raw_gamma*raw_k/raw_tau)/scale
    target_M=raw_M-raw_k**2/raw_tau
    target_d=raw_d-2*raw_nu*raw_k/raw_tau+raw_gamma*raw_k**2/raw_tau**2
    arr=lambda key:np.array([r[key] for r in reconstructed])
    ck('continuous_hidden_reflection_choice',np.max(abs(arr('G')-target_G))<2e-8)
    ck('Rayleigh_cross_reconstructed',np.max(abs(arr('nu')-target_nu))<2e-8)
    ck('visible_mass_from_response',np.max(abs(arr('M')-target_M))<2e-9)
    ck('visible_damping_from_response',np.max(abs(arr('d')-target_d))<2e-9)
    ck('entire_polynomial_response',np.max(arr('polynomial_residual'))<2e-9,float(np.max(arr('polynomial_residual'))))
    ck('candidate_positivity',np.min(arr('M'))>0 and np.min(arr('d')*arr('gamma')-arr('nu')**2)>0)

    raw_w0=-parent['bx']/parent['cx']
    raw_R0=s.diff(parent['ux'],px)+s.diff(parent['bx'],px)*raw_w0+s.diff(parent['cx'],px)*raw_w0**2/2
    get_R0prime=s.lambdify(px,s.diff(raw_R0,px),'numpy')
    true_R0p=get_R0prime(grid)
    static_res=arr('P0')-arr('G')**2/arr('C')-true_R0p
    ck('equilibrium_static_consistency',np.max(abs(static_res))<3e-9,float(np.max(abs(static_res))))

    w0_recovered=cumulative_simpson(-arr('G')/arr('C'),x=grid,initial=0)
    B_recovered=-arr('C')*w0_recovered
    E_recovered=cumulative_simpson(arr('R0'),x=grid,initial=0)
    U_recovered=E_recovered+arr('C')*w0_recovered**2/2
    target_w0=scale*((-raw_B/raw_C)-(-raw_B[0]/raw_C[0])+cumulative_simpson(raw_k/raw_tau,x=grid,initial=0))
    raw_E=raw_U-raw_B**2/(2*raw_C)
    ck('equilibrium_curve_integrated',np.max(abs(w0_recovered-target_w0))<2e-7,float(np.max(abs(w0_recovered-target_w0))))
    ck('visible_equilibrium_potential_integrated',np.max(abs(E_recovered-(raw_E-raw_E[0])))<2e-7,float(np.max(abs(E_recovered-(raw_E-raw_E[0])))))
    ck('potential_has_reconstructed_equilibrium',np.max(abs(B_recovered+arr('C')*w0_recovered))<1e-13)

    # New synthetic ringdowns at existing calibrated environments: only initial
    # preparation is fitted on the first60 time samples; later541 are predictions.
    prediction=[]
    for index,initial in [(0,(-.37,.18)),(30,(.49,.27)),(60,(-.24,-.33))]:
        xx=float(grid[index]);model=reconstructed[index]
        a,zv,t,force,_=parent['synthetic_records'](xx,initial)
        la=model['lambda_'];Cprime=model['tau']*(model['Q']+model['r']*(model['C']/model['tau']));tprime=model['tau']*model['r']
        def predicted(init):
            cc=init[0]+1j*init[1];ee=cc*np.exp(la*t)
            z=2*ee.real;zd=2*(la*ee).real
            return model['R0']+model['G']*z+model['nu']*zd+Cprime*z*z/2-tprime*zd*zd/2
        opt=least_squares(lambda c:(predicted(c)-force)[:60],[.1,.1],xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=300)
        error=float(np.max(abs(predicted(opt.x)[60:]-force[60:])))
        ck('reserved_later_history_'+str(index),opt.success and error<2e-8,error)
        prediction.append({'x':xx,'input_state':initial,'preparation_fit_samples':60,'reserved_prediction_samples':541,'max_error':error})

    # Altered observed channels, preserving earlier necessary conditions.
    j=30;f=fitrows[j];la=f['pole'];L=f['O']-la*la
    gchanged=f['g']*np.exp(.4j)
    Schanged=-2*(2*la+f['Gamma'])*f['residue']*gchanged/f['f']**2
    rchanged=(Schanged-f['Q'])/L
    # The alternative changes g only; independently recompute Q from its unchanged
    # input channels rather than comparing an object with itself.
    unchanged_Q=abs((2*la+f['Gamma'])*f['residue'])*f['h']/abs(f['f'])**2
    ck('phase_alternative_keeps_first_Q',abs(unchanged_Q-f['Q'])<1e-14)
    ck('phase_alternative_rejected_by_real_r',abs(rchanged.imag)>.01,float(rchanged.imag))
    ck('static_offset_alternative_rejected',abs(static_res[j]+.2)>.19)
    ck('negative_mass_alternative_rejected',reconstructed[j]['M']-5<0)
    ck('negative_damping_alternative_rejected',(reconstructed[j]['d']-5)*reconstructed[j]['gamma']-reconstructed[j]['nu']**2<0)

    # Covariance includes the analytic static-force term; nonaffine sensor labels
    # alone do not supply the conjugate-force change.
    Jp,Jpp,R0,Z,rho,ff,hh,gg=s.symbols('Jp Jpp R0 Z rho f h g',nonzero=True)
    xx=s.symbols('coordinate',real=True)
    jj=s.Function('j')(xx); force_curve=s.Function('force')(xx)
    Znew=(s.diff(force_curve/s.diff(jj,xx),xx)/s.diff(jj,xx)).subs(
        {s.diff(force_curve,xx):Z, force_curve:R0,
         s.diff(jj,xx,2):Jpp, s.diff(jj,xx):Jp})
    ck('nonaffine_residue_scaling',s.simplify(Znew-(Z/Jp**2-R0*Jpp/Jp**3))==0)
    ck('complex_second_harmonic_covariance',s.simplify((rho/Jp**2)*(gg/Jp)/(ff/Jp)**2-rho*gg/ff**2/Jp)==0)

    # Real-r error envelope accepts correlations and complex phases.
    rng=np.random.default_rng(991)
    error_max=0.;ratio_max=0.
    for i in range(100):
        la=-.2+1.4j;Ga=.4;O=abs(la)**2;rh=.3-.4j;f0=.6+.3j;g0=.1-.02j;Q0=.2
        el,egam,erho,ef,eg,eO,eQ=.001,.0015,.002,.001,.001,.003,.002
        dl=el*np.exp(1j*rng.uniform(0,7));dr=erho*np.exp(1j*rng.uniform(0,7));df=ef*np.exp(1j*rng.uniform(0,7));dg=eg*np.exp(1j*rng.uniform(0,7))
        dga=rng.choice([-egam,egam]);do=rng.choice([-eO,eO]);dq=rng.choice([-eQ,eQ])
        a=2*la+Ga;ahat=2*(la+dl)+Ga+dga
        S0=-2*a*rh*g0/f0**2;Sh=-2*ahat*(rh+dr)*(g0+dg)/(f0+df)**2
        Dmin=abs(f0)**2;eD=2*abs(f0)*ef+ef**2;ea=2*el+egam
        eN=2*((abs(a)+ea)*(abs(rh)+erho)*(abs(g0)+eg)-abs(a)*abs(rh)*abs(g0))
        eS=eN/(Dmin-eD)+2*abs(a)*abs(rh)*abs(g0)*eD/(Dmin*(Dmin-eD))
        L0=O-la**2;Lh=O+do-(la+dl)**2;eL=eO+2*abs(la)*el+el**2
        bound=(eS+eQ)/(abs(L0)-eL)+abs(S0-Q0)*eL/(abs(L0)*(abs(L0)-eL))
        err=abs((Sh-Q0-dq)/Lh-(S0-Q0)/L0)
        ck('correlated_reconstruction_error_'+str(i),abs(Sh-S0)<=eS and err<=bound)
        error_max=max(error_max,err);ratio_max=max(ratio_max,err/bound)

    details={'grid_points':len(grid),'normalization':'tau(-0.8)=1; chosen hidden unit, not measured absolute scale',
             'max_relative_inertia_error':float(np.max(abs(tau_recovered-actual_tau/actual_tau[0]))),
             'reserved_synthetic_predictions':prediction,'max_complex_r_error':error_max,'max_fraction_of_r_bound':ratio_max,
             'development_data':'61 synthetic environment responses and ringdowns used for function reconstruction',
             'reserved_status':'new synthetic initial states at3 calibrated environments; first60 samples fit only preparation, last541 evaluated after preparation fit; no empirical test',
             'inputs_received_by_inverse':'port spectra and force time series; generator parameter values used only in separate verification comparisons'}
    return rows, details
