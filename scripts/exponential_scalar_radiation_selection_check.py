#!/usr/bin/env python3
"""Conditional radiation reduction and linear relaxation checks; no observed data."""
import json
import sys
import mpmath as mp
import sympy as sp

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/EXPONENTIAL_SCALAR_RADIATION_SELECTION_BOUNDED_THEOREM_NOTE_2026-10-14.md",
)


def check_transverse():
    s=sp
    rows=[]
    def ck(name,value): rows.append({'name':'transverse.'+name,'passed':bool(value)})
    def zero(name,expr):
        r=s.factor(s.cancel(expr))
        rows.append({'name':'transverse.'+name,'passed':r==0,'residual':str(r)})
    k,y,v,z,ell,u=s.symbols('k y v z ell u',real=True)
    b,a=s.symbols('b a',positive=True)
    # Original x,y large-y kinetic metric, pulled back by x=v exp(ell), y=exp(ell).
    old=s.diag(4*b/(3*(1+v*v)*s.exp(2*ell)),b/((1+v*v)*s.exp(2*ell)))
    pull=s.Matrix([[s.exp(ell),v*s.exp(ell)],[0,s.exp(ell)]])
    G=s.simplify(pull.T*old*pull)
    expected=b/(1+v*v)*s.Matrix([[s.Rational(4,3),4*v/3],[4*v/3,1+4*v*v/3]])
    for i in range(2):
     for j in range(2):zero(f'pullback_{i}{j}',G[i,j]-expected[i,j])
    Gi=s.simplify(G.inv());coords=(v,ell)
    Gamma=[[[s.simplify(sum(Gi[i,l]*(s.diff(G[l,h],coords[j])+s.diff(G[l,j],coords[h])-s.diff(G[j,h],coords[l]))/2 for l in range(2))) for h in range(2)] for j in range(2)] for i in range(2)]
    zero('Gamma_v_ell_ell_linear',s.diff(Gamma[0][1][1],v).subs(v,0)+s.Rational(1,4))
    zero('Gamma_v_v_ell_at_zero',Gamma[0][0][1].subs(v,0))
    zero('Gamma_ell_v_ell_at_zero',Gamma[1][0][1].subs(v,0))
    zero('Gamma_ell_ell_ell_linear',s.diff(Gamma[1][1][1],v).subs(v,0))
    # Potential differentiated in (v,ell) before identifying ell-log(y_b)=z.
    W=s.exp(2*ell)*(k*v*v/2+k/3)
    grad=s.Matrix([s.diff(W,c) for c in coords]);force=s.simplify(Gi*grad/s.exp(2*ell))
    zero('mixed_inverse_metric_potential_force',s.diff(force[0],v).subs(v,0)-k/(12*b))
    zero('ell_force_even',s.diff(force[1],v).subs(v,0))
    B0=k/(2*(1+k));HB0=2*(1+k)/3
    zero('normal_mass_force',s.diff(force[0],v).subs({v:0,b:B0})/HB0-s.Rational(1,4))
    r,q,h=s.symbols('r q h',real=True)
    vel=(r,q)
    normal=-(3+h)*r-sum(Gamma[0][i][j]*vel[i]*vel[j] for i in range(2) for j in range(2))-force[0]/HB0
    normal=normal.subs({b:B0,q:-2,h:-2})
    linear=s.Matrix([r,normal]).jacobian((v,r)).subs({v:0,r:0})
    target=s.Matrix([[0,1],[s.Rational(3,4),-1]])
    for i in range(2):
     for j in range(2):zero(f'normal_block_{i}{j}',linear[i,j]-target[i,j])
    lam=s.symbols('lambda')
    zero('normal_characteristic_polynomial',linear.charpoly(lam).as_expr()-(lam-s.Rational(1,2))*(lam+s.Rational(3,2)))
    zero('growing_eigenvector', (linear*s.Matrix([2,1])-s.Matrix([1,s.Rational(1,2)]))[1])
    ck('normal_hyperbolic_saddle',set(linear.eigenvals())=={s.Rational(1,2),-s.Rational(3,2)})

    # Independent original-field connection, using the full finite-y D factor.
    x=s.symbols('x',real=True)
    D=1+2*(1+k)*(x*x+y*y)/3
    Kx=4*k/(9*D);Ky=k/(3*D)
    Gxy=s.diff(Kx,y)/(2*Kx)
    Gyy=-s.diff(Ky,x)/(2*Kx)
    zero('original_mixed_connection_limit',s.limit(y*Gxy.subs(x,0),y,s.oo)+1)
    zero('original_normal_connection_limit',s.limit(y*y*s.diff(Gyy,x).subs(x,0),y,s.oo)-s.Rational(3,4))
    masscoef=s.limit(k/(Kx.subs(x,0)*y*y*HB0),y,s.oo)
    zero('original_potential_coefficient',masscoef-s.Rational(9,4))
    P_x=lam*lam+5*lam+s.Rational(21,4)
    zero('x_roots',P_x-(lam+s.Rational(3,2))*(lam+s.Rational(7,2)))
    zero('x_to_ratio_clock_shift',P_x.subs(lam,lam-2)-(lam*lam+lam-s.Rational(3,4)))
    zero('energy_ratio', (k*x*x/2)/(k*y*y/3)-3*(x/y)**2/2)

    # Damages: omit the off-diagonal inverse-metric force, mixed original-field
    # connection, or mistake decay of x for decay of its ratio to radiation.
    bad_force=s.diff((Gi[0,0]*grad[0]/s.exp(2*ell)),v).subs({v:0,b:B0})/HB0
    ck('damage.omitted_inverse_mixed_force',bad_force!=s.Rational(1,4))
    bad_x=lam*lam+(3-2)*lam+s.Rational(21,4)
    ck('damage.omitted_original_mixed_connection',s.expand(bad_x-P_x)!=0)
    ck('damage.x_decay_does_not_imply_ratio_decay',-s.Rational(3,2)<0 and -s.Rational(3,2)+2>0)
    ck('scope.fast_transverse_mode_also_exists',-s.Rational(7,2)+2<0)
    return dict(checks=rows,metric=str(G),inverse_metric=str(Gi),normal_jacobian=str(linear))


def run_checks():
    checks = []

    def check(name, ok, **extra):
        checks.append(dict(name=name, passed=bool(ok), **extra))

    def exact(name, expr):
        val = sp.factor(sp.cancel(expr))
        check(name, val == 0, residual=str(val))

    k = sp.symbols('k', positive=True)
    u, z, p, q, x = sp.symbols('u z p q x', real=True)
    y, Y, nu = sp.symbols('y Y nu', positive=True)
    a = (1-k)*(1+3*k)/4
    alpha = sp.sqrt(a)
    s = (1+k)/(k*(1-3*k))
    E = sp.exp(2*alpha*u)
    F = 1+s*E
    J = 1+(1-3*a)*s*E
    D_field = 1+2*(1+k)*(x*x+y*y)/3
    Ku = J/F**2
    Kx = (1+s)*4*k/(9*F*D_field)
    Ky = (1+s)*k/(3*F*D_field)
    C = (1+s)*E/F
    lx, ly = (1-k)/alpha, (1+k)/alpha
    U = (sp.Rational(3,2)+sp.Rational(3,2)*s*(E-1)**2/F**2
         +k*x*x*sp.exp(-lx*u)/2+k*y*y*sp.exp(-ly*u)/3
         +nu*(1+s)*u*u/(2*F**2))
    A = Ku
    B = (1+s)*k/(2*(1+k)*F)
    W = k*sp.exp(2*z-ly*u)/3
    ab = alpha/F
    exact('action.lambda_y_identity', ly-4*alpha*s/(1+s))
    exact('action.physical_clock_derivative', sp.diff(C,u)/(2*C)-ab)
    exact('action.vacuum_coupling', (ab*ab/Ku).subs(u,0)-k)
    exact('action.vacuum_J', J.subs(u,0)-a/k)
    exact('action.invariant_plane_potential', sp.diff(U,x).subs(x,0))
    exact('action.invariant_plane_Ku', sp.diff(Ku,x).subs(x,0))
    exact('action.invariant_plane_Ky', sp.diff(Ky,x).subs(x,0))
    exact('action.transverse_metric_ratio', Kx/Ky-sp.Rational(4,3))
    exact('action.transverse_potential_curvature', sp.diff(U,x,2).subs({x:0,u:0})-k)
    full_B = (Ky*y*y).subs(x,0)
    d = 2*(1+k)/3
    exact('action.full_ell_metric', full_B-B*d*y*y/(1+d*y*y))
    exact('action.large_y_metric_limit', sp.limit(full_B,y,sp.oo)-B)
    exact('action.large_y_potential_limit',
          sp.limit(U.subs({x:0,y:Y*sp.exp(z)})/Y**2,Y,sp.oo)-W)
    exact('action.fixed_physical_y_u_gradient',
          sp.limit(sp.diff(U,u).subs({x:0,y:Y*sp.exp(z)})/Y**2,Y,sp.oo)+ly*W)
    exact('action.ell_gradient',
          sp.limit((y*sp.diff(U,y)).subs({x:0,y:Y*sp.exp(z)})/Y**2,Y,sp.oo)-2*W)

    # Use the action.lambda_y_identity already checked above to normalize the
    # equivalent exponent before the full symbolic Jacobian. This avoids mixing
    # factored and expanded radicals for sqrt((1-k)(1+3k)).
    ly = 4*alpha*s/(1+s)
    W = k*sp.exp(2*z-ly*u)/3
    T = A*p*p+B*q*q
    HB = 2*(C*C+W)/(3-T)
    h = -4*C*C/(3*HB)-T
    flow = sp.Matrix([
        p,
        q+2+2*ab*p,
        -(3+h)*p-sp.diff(A,u)*p*p/(2*A)+sp.diff(B,u)*q*q/(2*A)+ly*W/(A*HB),
        -(3+h)*q-sp.diff(B,u)*p*q/B-2*W/(B*HB),
    ])
    exact('flow.Friedmann_constraint', (3-T)*HB-2*(C*C+W))
    exact('flow.Raychaudhuri', h+T+4*C*C/(3*HB))
    # Lowered equations from the diagonal (u,ell) kinetic metric, differentiated
    # before changing ell to z. No trace force is present for exact radiation.
    # Verify the lowered-to-raised algebra before expanding the exponential
    # coefficients. Expanding those coefficients first creates a large redundant
    # rational expression; each coefficient was independently bound to the action
    # by the exact identities and limits above.
    ag,bg,aug,bug,wg,lg,hg,Hg = sp.symbols('A B A_u B_u W lambda_y h Hbar')
    pg = -(3+hg)*p-aug*p*p/(2*ag)+bug*q*q/(2*ag)+lg*wg/(ag*Hg)
    qg = -(3+hg)*q-bug*p*q/bg-2*wg/(bg*Hg)
    exact('flow.lowered_u',ag*(pg+(3+hg)*p)+aug*p*p/2-bug*q*q/2-lg*wg/Hg)
    exact('flow.lowered_ell',bg*(qg+(3+hg)*q)+bug*p*q+2*wg/Hg)
    coefficient_bindings={ag:A,bg:B,aug:sp.diff(A,u),bug:sp.diff(B,u),wg:W,lg:ly,hg:h,Hg:HB}
    exact('flow.actual_u_matches_lowered_solution',flow[2]-pg.xreplace(coefficient_bindings))
    exact('flow.actual_ell_matches_lowered_solution',flow[3]-qg.xreplace(coefficient_bindings))
    exact('flow.Jordan_clock_conservation', flow[1]-q-2*(1+sp.diff(C,u)*p/(2*C)))
    fp = {u:0,z:0,p:0,q:-2}
    for i,r in enumerate(flow.subs(fp)):
        exact('fixed_point.'+str(i),r)
    exact('fixed_point.Hbar', HB.subs(fp)-2*(1+k)/3)
    exact('fixed_point.h', h.subs(fp)+2)
    exact('fixed_point.T', T.subs(fp)-2*k/(1+k))
    M = flow.jacobian([u,z,p,q]).subs(fp).applyfunc(lambda v:sp.factor(sp.simplify(v)))
    lam = sp.symbols('lambda')
    cp = sp.factor(M.charpoly(lam).as_expr())
    D = (1+k)*(1-3*k)**2
    n = -3*k**3+10*k*k+k+4
    S = 4*n/D
    P0 = 16*k/((1+k)*(1-3*k))
    target = (lam*lam+lam)**2+S*(lam*lam+lam)+P0
    exact('spectrum.characteristic_polynomial',cp-target)
    exact('spectrum.n_above_four', n-4-k*(1+k*(10-3*k)))
    exact('spectrum.S_above_sixteen', n-4*D-k*(16+(1-3*k)*(13*k+5)))
    exact('spectrum.ratio_P_over_S', P0/S-4*k*(1-3*k)/n)
    exact('spectrum.k_quadratic_bound', sp.Rational(1,12)-k*(1-3*k)-3*(k-sp.Rational(1,6))**2)
    check('spectrum.discriminant_bound',4*sp.Rational(1,12)/16<1)
    approx = -k+sp.Rational(35,16)*k*k+sp.Rational(869,128)*k**3
    exact('spectrum.slow_root_series',sp.series(target.subs(lam,approx),k,0,4).removeO())
    exact('spectrum.weak_limit',sp.limit(target,k,0)-lam*(lam+1)*(lam*lam+lam+16))
    exact('spectrum.simple_zero_root', sp.diff(sp.limit(target,k,0),lam).subs(lam,0)-16)

    L = 35+43*k-66*k*k+14*k**3+15*k**4-9*k**5
    exact('rate.sign_factorization',target.subs(lam,-k)+k*k*L/D)
    positive_decomposition = (43*k+14*k**3+15*k**4
                              +66*(sp.Rational(1,9)-k*k)
                              +9*(sp.Rational(1,243)-k**5))
    exact('rate.L_positive_decomposition',L-sp.Rational(746,27)-positive_decomposition)
    check('rate.L_lower_bound_positive',sp.Rational(746,27)>0)
    check('rate.large_factor_positive',16-sp.Rational(1,6)-sp.Rational(1,4)>0)
    check('rate.monotonicity_domain',sp.Rational(1,3)<sp.Rational(1,2))

    bad = M.copy()
    bad[1,2] = 0
    defect = sp.factor(bad.charpoly(lam).as_expr()-target)
    check('damage.omitted_clock_term',defect!=0,residual=str(defect))
    check('damage.wrong_series_coefficient',sp.series(target.subs(lam,-k+sp.Rational(9,4)*k*k),k,0,3).removeO()!=0)
    check('damage.exact_rate_equals_k',sp.factor(target.subs(lam,-k))!=0)
    # Pointwise, finite-chart counterexample to identifying another environment's
    # coupling g=a/J with k. It is not an on-shell stationary environment.
    g_other = (a/(1+(1-3*a)*s*sp.Rational(106360,7))).subs(k,sp.Rational(1,10))
    exact('scope.nonvacuum_example',g_other-sp.Rational(1,100000))
    check('scope.nonvacuum_g_is_not_k',g_other<sp.Rational(1,79999)<sp.Rational(1,10))

    mp.mp.dps = 80
    rows = []
    matrix_fn = sp.lambdify(k,M,'mpmath')
    for ks in ['0.000001','0.00001','0.001','0.01','0.1','0.3','0.32']:
        kk = mp.mpf(ks)
        sn = 4*(-3*kk**3+10*kk**2+kk+4)/((1+kk)*(1-3*kk)**2)
        pn = 16*kk/((1+kk)*(1-3*kk))
        rs = 2*pn/(sn+mp.sqrt(sn*sn-4*pn))
        rl = (sn+mp.sqrt(sn*sn-4*pn))/2
        slow = -2*rs/(1+mp.sqrt(1-4*rs))
        analytic = [slow,-1-slow,mp.mpc(-mp.mpf('.5'),mp.sqrt(4*rl-1)/2),
                    mp.mpc(-mp.mpf('.5'),-mp.sqrt(4*rl-1)/2)]
        eig,_ = mp.eig(matrix_fn(kk))
        maxerr = max(min(abs(v-t) for t in eig) for v in analytic)
        check('numeric.k'+ks+'.matrix_spectrum',maxerr<mp.mpf('1e-60'),max_error=mp.nstr(maxerr,12))
        check('numeric.k'+ks+'.Hurwitz',all(mp.re(v)<0 for v in eig))
        check('numeric.k'+ks+'.bounds',sn>16 and pn/sn<mp.mpf(1)/12 and 0<rs<mp.mpf(1)/6 and rl>16-mp.mpf(1)/6)
        check('numeric.k'+ks+'.rate_bound',0<-slow<kk)
        check('numeric.k'+ks+'.slow_retention',mp.exp(24*slow)>mp.exp(-24*kk))
        check('scope.k'+ks+'.fast_mode_not_subject_to_slow_bound',mp.exp(24*(-1-slow))<mp.exp(-24*kk))
        rows.append(dict(k=ks,slow_eigenvalue=mp.nstr(slow,40),linear_relaxation_e_folds=mp.nstr(-1/slow,40),
                         slow_mode_retained_after_24_Einstein_e_folds=mp.nstr(mp.exp(24*slow),40),
                         spectrum=[[mp.nstr(mp.re(v),30),mp.nstr(mp.im(v),30)] for v in analytic]))
    transverse=check_transverse()
    checks.extend(transverse['checks'])
    return dict(transverse=transverse,scope='Supplied action, fixed-k ideal radiation and local linear slow mode; no observed initial-state derivation or likelihood.',
                matrix=str(M),characteristic_polynomial=str(cp),checks=checks,rates=rows,
                exposed_proxy=dict(b='1/79999',DeltaN='24',role='Previously exposed conditional development illustration only',
                                   strict_retention_lower_bound=mp.nstr(mp.exp(-mp.mpf(24)/79999),45)),
                counts=dict(passed=sum(r['passed'] for r in checks),failed=sum(not r['passed'] for r in checks)))


if __name__ == '__main__':
    result = run_checks()
    print(json.dumps(result,indent=2,allow_nan=False))
    sys.exit(bool(result['counts']['failed']))
