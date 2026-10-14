#!/usr/bin/env python3
"""Supplied-action alternative radiation and conditional physical readout."""
import json
import sys
import mpmath as mp
import sympy as s

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/EXPONENTIAL_SCALAR_ALTERNATIVE_RADIATION_BOUNDED_THEOREM_NOTE_2026-10-14.md",
)


def run_checks():
    rows = []

    def ck(name, ok, **extra):
        rows.append(dict(name=name, passed=bool(ok), **extra))

    def zero(name, value):
        residual = s.factor(s.cancel(value))
        ck(name, residual == 0, residual=str(residual))

    k = s.symbols('k', positive=True)
    theta, z, p, q, x, y, w, ell = s.symbols('theta z p q x y w ell', real=True)
    e, nu, yb, beta = s.symbols('e nu yb beta', positive=True)
    a = (1-k)*(1+3*k)/4
    alpha = s.sqrt(a)
    ss = (1+k)/(k*(1-3*k))
    ex = (1-3*k)/(3*(1+k))
    d = 2*(1+k)/3
    E = ex*s.exp(theta)
    F = 1+ss*E
    J = 1+(1-3*a)*ss*E
    l = 2/(1+3*k)
    A = J/(4*a*F**2)
    B = (1+ss)*2*k/(3*(1+k)*F)
    C = (1+ss)*E/F
    b = 2*k*(1-k)/((1+k)*(1-3*k))
    cx = (1-k)/(1+k)
    hx = 2*cx**2/(3*(1-2*b))
    wx = b*hx
    W = wx*s.exp(2*z-l*theta)

    # Original action in a generic positive E chart. Derivatives use u,
    # then theta=2alpha(u-u_x); no background equation is fitted.
    u = s.symbols('u', real=True)
    Fu = 1+ss*s.exp(2*alpha*u)
    Ju = 1+(1-3*a)*ss*s.exp(2*alpha*u)
    D = 1+d*(x*x+y*y)
    Ku = Ju/Fu**2
    Kx = (1+ss)*4*k/(9*Fu*D)
    Ky = (1+ss)*k/(3*Fu*D)
    lx = (1-k)/alpha
    ly = (1+k)/alpha
    U0 = s.Rational(3,2)+3*ss*(s.exp(2*alpha*u)-1)**2/(2*Fu**2)+nu*(1+ss)*u*u/(2*Fu**2)
    U = U0+k*x*x*s.exp(-lx*u)/2+k*y*y*s.exp(-ly*u)/3
    zero('action.lambda_x_theta', lx/(2*alpha)-l)
    zero('action.lambda_y_balance', ly-4*alpha*ss/(1+ss))
    zero('action.lambda_gap', ly-lx-2*k/alpha)
    zero('action.invariant_y_potential', s.diff(U,y).subs(y,0))
    zero('action.invariant_y_metric', s.diff(Kx,y).subs(y,0))
    zero('action.kinetic_ratio', Ky/Kx-s.Rational(3,4))
    Bfull = (x*x*Kx).subs(y,0)
    Bu = (1+ss)*2*k/(3*(1+k)*Fu)
    zero('action.finite_radial_metric', Bfull-Bu*d*x*x/(1+d*x*x))
    zero('action.large_x_metric', s.limit(Bfull,x,s.oo)-Bu)
    zero('action.implemented_B_binding', B-Bu.xreplace({s.exp(2*alpha*u):E}))
    Cu = (1+ss)*s.exp(2*alpha*u)/Fu
    zero('action.implemented_C_binding', C-Cu.xreplace({s.exp(2*alpha*u):E}))
    zero('action.normal_potential_curvature', s.diff(U,y,2)-2*k*s.exp(-ly*u)/3)
    zero('action.plane_potential_limit', s.limit(U.subs({x:beta*yb*s.exp(z),y:0})/yb**2,yb,s.oo)-k*beta**2*s.exp(2*z-lx*u)/2)
    zero('action.plane_radial_gradient', s.limit((x*s.diff(U,x)).subs({x:beta*yb*s.exp(z),y:0})/yb**2,yb,s.oo)-k*beta**2*s.exp(2*z-lx*u))
    zero('action.plane_u_gradient', s.limit(s.diff(U,u).subs({x:beta*yb*s.exp(z),y:0})/yb**2,yb,s.oo)+lx*k*beta**2*s.exp(2*z-lx*u)/2)
    ux = s.log(ex)/(2*alpha)
    beta2 = 2*wx*s.exp(lx*ux)/k
    normalized_tail = s.powsimp(k*beta2*s.exp(2*z-lx*(ux+theta/(2*alpha)))/2,force=True)
    zero('action.implemented_W_binding', s.powsimp(W-normalized_tail,force=True))
    zero('action.implemented_W_radial_gradient', s.diff(W,z)-2*W)
    zero('action.implemented_W_theta_gradient', s.diff(W,theta)+l*W)
    zero('action.theta_metric', Ku.xreplace({s.exp(2*alpha*u):E})/(4*a)-A)
    zero('action.normal_metric_limit', s.limit((x*x*Kx).subs(y,w*x),x,s.oo)-Bu/(1+w*w))
    zero('action.clock_gradient', s.diff(C,theta)/(2*C)-1/(2*F))
    zero('action.vacuum_coupling', ((alpha/Fu)**2/Ku).subs(u,0)-k)

    zero('branch.B', B.subs(theta,0)-b)
    zero('branch.C', C.subs(theta,0)-cx)
    zero('branch.u_balance', l-2*ss*ex/(1+ss*ex))
    delta = 1-6*k+k*k
    zero('branch.domain_factor', 1-2*b-delta/((1+k)*(1-3*k)))
    kc = 3-2*s.sqrt(2)
    zero('branch.critical_polynomial', delta.subs(k,kc))
    ck('branch.critical_interval', 0<kc<s.Rational(1,5)<s.Rational(1,3))

    # The finite nonzero mixed-ratio ansatz. Positivity and u sign provide
    # the contradiction in the note; these identities are exact witnesses.
    v, X, Y, Bg, lamx, lamy = s.symbols('v X Y Bg lamx lamy', real=True)
    t = v*v
    Gll = Bg*(3+4*t)/(3*(1+t))
    Gvl = 4*Bg*v/(3*(1+t))
    Wmix = k*(t*X/2+Y/3)
    ratio = 4*(3+2*t)/(3*(3+t))
    mixed = s.factor(s.diff(Wmix,v)/Wmix-2*(Gvl+s.diff(Gll,v))/Gll)
    zero('mixed.required_ratio', mixed.subs(X,ratio*Y))
    zero('mixed.strict_ratio', ratio-1-(3+5*t)/(3*(3+t)))
    weighted = (3*t*lamx*X+2*lamy*Y)/(3*t*X+2*Y)
    zero('mixed.weighted_gap', lamy-weighted-3*t*X*(lamy-lamx)/(3*t*X+2*Y))
    zero('mixed.rhs_gap', 4*alpha*ss*e/(1+ss*e)-4*alpha*ss/(1+ss)-4*alpha*ss*(e-1)/((1+ss*e)*(1+ss)))

    # One nonlinear constructor supplies the equations, generic lowered
    # action bindings and coefficient-jet Jacobian. Cubic drift is caught
    # by the lowered bindings even though it leaves the Jacobian unchanged.
    def flow(AA, At, BB, Bt, CC, WW, lc, FF):
        T = AA*p*p+BB*q*q
        HB = 2*(CC*CC+WW)/(3-T)
        h = -4*CC*CC/(3*HB)-T
        return s.Matrix([p,q+2+p/FF,
            -(3+h)*p-At*p*p/(2*AA)+Bt*q*q/(2*AA)+lc*WW/(AA*HB),
            -(3+h)*q-Bt*p*q/BB-2*WW/(BB*HB)]),HB,h

    AA,At,BB,Bt,CC,WW,lc,FF = s.symbols('AA At BB Bt CC WW lc FF')
    generic,HH,hh = flow(AA,At,BB,Bt,CC,WW,lc,FF)
    zero('flow.lowered_theta', AA*HH*(generic[2]+(3+hh)*p)+HH*At*p*p/2-HH*Bt*q*q/2-lc*WW)
    zero('flow.lowered_radial', BB*HH*(generic[3]+(3+hh)*q)+HH*Bt*p*q+2*WW)
    zero('flow.physical_clock', generic[1]-q-2-p/FF)
    full,HB,h = flow(A,s.diff(A,theta),B,s.diff(B,theta),C,W,l,F)
    fp = {theta:0,z:0,p:0,q:-2}
    for i,val in enumerate(full.subs(fp)):
        zero('flow.fixed_'+str(i), val)
    zero('flow.fixed_Hbar', HB.subs(fp)-hx)
    zero('flow.fixed_h', h.subs(fp)+2)

    A0,A1,B0,B1,B2,C0,C1,W0,W1,W2,L = s.symbols('A0 A1 B0 B1 B2 C0 C1 W0 W1 W2 L')
    jet,_h,_d = flow(A0+A1*theta,A1,B0+B1*theta+B2*theta**2/2,B1+B2*theta,C0+C1*theta,W0+W1*theta+W2*z,L,F)
    at_origin = {theta:0,z:0}
    bind = {A0:A.subs(theta,0),A1:s.diff(A,theta).subs(theta,0),B0:B.subs(theta,0),B1:s.diff(B,theta).subs(theta,0),B2:s.diff(B,theta,2).subs(theta,0),C0:C.subs(theta,0),C1:s.diff(C,theta).subs(theta,0),W0:W.subs(at_origin),W1:s.diff(W,theta).subs(at_origin),W2:s.diff(W,z).subs(at_origin),L:l}
    bind = {key:s.factor(s.cancel(val)) for key,val in bind.items()}
    M = jet.jacobian([theta,z,p,q]).subs(fp).applyfunc(lambda val:s.factor(s.cancel(val.xreplace(bind))))
    lam = s.symbols('lambda')
    cp = s.factor(M.charpoly(lam).as_expr())
    nx = 5-7*k-21*k*k+7*k**3
    sx = 4*nx/((1+k)*(1-3*k)*(1+3*k))
    px = 64*k*(1-k)**2*delta/((1+k)**2*(1-3*k)**2*(1+3*k))
    target = (lam*lam+lam)**2+sx*(lam*lam+lam)+px
    zero('spectrum.exact_quartic', cp-target)
    zero('spectrum.n_lower', nx-s.Rational(69,25)-(7*(s.Rational(1,5)-k)+21*(s.Rational(1,25)-k*k)+7*k**3))
    zero('spectrum.denominator_upper', (1+k)-(1+k)*(1-3*k)*(1+3*k)-9*k*k*(1+k))
    zero('spectrum.ratio', px/sx-16*k*(1-k)**2*delta/((1+k)*(1-3*k)*nx))
    zero('spectrum.delta_upper', (1-3*k)-delta-k*(3-k))
    zero('spectrum.square_upper', (1+k)-(1-k)**2-k*(3-k))
    ck('spectrum.Hurwitz_margin', s.Rational(46,5)>4*s.Rational(80,69)>0)
    zero('spectrum.weak_limit', s.limit(cp,k,0)-lam*(lam+1)*(lam*lam+lam+20))
    zero('spectrum.simple_zero_root', s.diff(s.limit(cp,k,0),lam).subs(lam,0)-20)
    zero('spectrum.slow_coefficient', s.series(cp.subs(lam,-s.Rational(16,5)*k),k,0,2).removeO())

    # Pull back the original x,y metric, retaining the mixed term.
    # The common large-x action coefficient is B; Ky/Kx was checked above.
    old = s.diag(Bg/((1+w*w)*s.exp(2*ell)),3*Bg/(4*(1+w*w)*s.exp(2*ell)))
    pull = s.Matrix([[0,s.exp(ell)],[s.exp(ell),w*s.exp(ell)]])
    G = s.simplify(pull.T*old*pull)
    Gexpected = Bg/(1+w*w)*s.Matrix([[s.Rational(3,4),3*w/4],[3*w/4,1+3*w*w/4]])
    for i in range(2):
        for j in range(2):zero(f'normal.pullback_{i}{j}',G[i,j]-Gexpected[i,j])
    Gi = s.simplify(G.inv())
    coords = (w,ell)
    gam = [[[s.simplify(sum(Gi[i,l0]*(s.diff(G[l0,h0],coords[j])+s.diff(G[l0,j],coords[h0])-s.diff(G[j,h0],coords[l0]))/2 for l0 in range(2))) for h0 in range(2)] for j in range(2)] for i in range(2)]
    R, vel = s.symbols('R vel',real=True)
    V = Bg*s.exp(2*ell)*(1+2*R*w*w/3)
    force = s.simplify(Gi*s.Matrix([s.diff(V,w),s.diff(V,ell)])/s.exp(2*ell))
    normal = -vel-sum(gam[0][i][j]*[vel,-2][i]*[vel,-2][j] for i in range(2) for j in range(2))-force[0]
    normal_matrix = s.Matrix([vel,normal]).jacobian([w,vel]).subs({w:0,vel:0})
    omega = -s.Rational(2,3)+16*R/9
    zero('normal.characteristic', normal_matrix.charpoly(lam).as_expr()-(lam*lam+lam+omega))
    zero('normal.friction', normal_matrix[1,1]+1)
    ck('normal.bound', -s.Rational(2,3)+s.Rational(16,9)==s.Rational(10,9)>s.Rational(1,4))

    # Dimensionful physical density and a specified vacuum dynamical readout.
    Q0,Hv,rho,runit,rhoJ,gamma = s.symbols('Q0 Hv rho runit rhoJ gamma',positive=True)
    Q = Q0*(1+k)
    HE2 = Hv**2*hx*rho/(2*Q*Hv**2)
    HJ2 = HE2/cx
    rh = (1-k)*(1-3*k)/((1+k)*delta)
    zero('bridge.density_translation', (runit/(2*Q*Hv**2))*rhoJ-(rho/(2*Q*Hv**2)).subs(rho,runit*rhoJ))
    zero('bridge.physical_ratio', HJ2/(rho/(3*Q0))-rh)
    zero('bridge.Hv_cancels', s.diff(HJ2/(rho/(3*Q0)),Hv))
    zero('bridge.Q0_cancels', s.diff(HJ2/(rho/(3*Q0)),Q0))
    zero('bridge.strict_excess', rh-1-k*(1+8*k-k*k)/((1+k)*delta))
    poly = 1+16*k-38*k*k+8*k**3-3*k**4
    zero('bridge.derivative', s.diff(rh,k)-poly/((1+k)**2*delta**2))
    zero('bridge.derivative_positive_split', poly-((1-3*k**4)+k*(16-38*k)+8*k**3))
    ck('bridge.derivative_bounds', 1-s.Rational(3,625)>0 and 16-s.Rational(38,5)>0)
    zero('bridge.weak_series', s.series(rh,k,0,3).removeO()-(1+k+13*k*k))
    zero('bridge.weak_endpoint', s.limit(rh,k,0)-1)
    ck('bridge.upper_endpoint_numerator', ((1-k)*(1-3*k)).subs(k,kc)>0)
    zero('bridge.scalar_fraction', (4*b+2*wx/hx)/3-2*b)
    zero('bridge.branch_coupling_norm', (1/(4*F*F*A)).subs(theta,0)-3*k*(1-k)/(1+3*k))
    ck('scope.scalar_fraction_not_excess', s.factor(2*b-(rh-1))!=0)
    ck('scope.omitted_clock_wrong', s.factor(HE2/(rho/(3*Q0))-rh)!=0)
    zero('scope.unknown_calibration', (HJ2/(gamma*rho/(3*Q0)))-rh/gamma)
    zero('scope.lensing_normalization', (1/(8*s.pi*Q0*(1+k)))/(1/(8*s.pi*Q0))-1/(1+k))

    mp.mp.dps=70
    Mf=s.lambdify(k,M,'mpmath'); Sf=s.lambdify(k,sx,'mpmath'); Pf=s.lambdify(k,px,'mpmath')
    spectra=[]
    for ks in ['0.000001','0.00001','0.001','0.01','0.1','0.16','0.1715']:
        kv=mp.mpf(ks);sv=Sf(kv);pv=Pf(kv)
        rsmall=2*pv/(sv+mp.sqrt(sv*sv-4*pv));rlarge=(sv+mp.sqrt(sv*sv-4*pv))/2
        roots=[]
        for rr in [rsmall,rlarge]:roots.extend([(-1+mp.sqrt(1-4*rr))/2,(-1-mp.sqrt(1-4*rr))/2])
        eig,_=mp.eig(Mf(kv));err=max(min(abs(rr-vv) for vv in eig) for rr in roots)
        ck('numeric.'+ks+'.spectrum',err<mp.mpf('1e-55'),max_error=mp.nstr(err,10))
        ck('numeric.'+ks+'.stability',all(mp.re(vv)<0 for vv in eig))
        spectra.append(dict(k=ks,eigenvalues=[[mp.nstr(mp.re(vv),35),mp.nstr(mp.im(vv),35)] for vv in eig]))
    return dict(scope='Supplied action; fixed-k ideal large-field radiation, local stability and conditional vacuum-calibrated expansion. No observational fit.',checks=rows,counts=dict(passed=sum(r['passed'] for r in rows),failed=sum(not r['passed'] for r in rows)),matrix=str(M),normal_matrix=str(normal_matrix),spectra=spectra)


if __name__=='__main__':
    result=run_checks()
    print(json.dumps(result,indent=2,allow_nan=False))
    sys.exit(bool(result['counts']['failed']))
