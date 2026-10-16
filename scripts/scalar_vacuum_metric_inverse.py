"""Synthetic, personally authored nonlinear physical-metric inverse probe."""
from pathlib import Path
import json
import time
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp, cumulative_simpson



def geometry_functions():
    r, b, bp, bpp, e1, e2, e3 = sp.symbols('r b bp bpp e1 e2 e3')
    gt = (b - 1) / r**2 + bp / r
    gr = (b - 1) / r**2 + 2 * b * e1 / r
    ga = b * (e2 + e1**2 + e1 / r) + bp * (e1 + 1/r) / 2
    u = (ga - gt) / (b * (1/r - e1))
    up = sum(sp.diff(u, q) * dq for q, dq in
             [(r, 1), (b, bp), (bp, bpp), (e1, e2), (e2, e3)])
    hh = gr - gt - b * (up + u*u) - (bp/2 - b*e1)*u
    jj = b*u*u/(2*hh)
    ww = -gt - hh/2 - b*(up + u*u) - (bp/2 + 2*b/r)*u
    args = (r, b, bp, bpp, e1, e2, e3)
    return sp.lambdify(args, (u, up, hh, jj, ww, gt, gr, ga), 'numpy')


def make_generator(k_value, hv_value, nu_value, deformation=0):
    # Synthetic generator chooses state and parameters. Inverse below sees
    # only physical-metric jets, not these hidden source values.
    r, z, v, b = sp.symbols('r z v b', positive=True)
    q = (r, z, v, b)
    k = sp.Rational(str(k_value))
    hv = sp.Rational(str(hv_value))
    nu = sp.Rational(str(nu_value))
    aa = (1-k)*(1+3*k)/4
    lam = aa/(1-3*aa)
    ss = (1+k)/(k*(1-3*k))
    ff, zz = ss+z*z, 1/lam
    vv = hv*hv*(3*(ss+z**4)+nu*z**4*sp.log(z)**2/aa+sp.Rational(str(deformation))*(z*z-1)**3)
    fz, fzz, vz = sp.diff(ff,z), sp.diff(ff,z,2), sp.diff(vv,z)
    box = (vz-2*fz*vv/ff-fz*b*v*v*(zz+3*fzz/2)/ff)/(2*zz+3*fz*fz/(2*ff))
    ep = (b*zz*v*v-vv-ff*(b-1)/r**2-2*b*fz*v/r)/(b*(2*ff/r+fz*v))
    bd = r/ff*(-ff*(b-1)/r**2-b*(zz+fzz)*v*v-vv-fz*box+b*fz*ep*v)
    vd = box/b-(bd/(2*b)+ep+2/r)*v
    vec = sp.Matrix([1, v, vd, bd])
    fun = sp.lambdify(q, (vd, bd, ep), 'numpy', cse=True)
    epg = sp.lambdify(q, sp.Matrix([ep]).jacobian(q), 'numpy', cse=True)
    eph = sp.lambdify(q, sp.hessian(ep,q), 'numpy', cse=True)
    jac = sp.lambdify(q, vec.jacobian(q), 'numpy', cse=True)
    pot = sp.lambdify(z, (vv,vz), 'numpy', cse=True)

    def rhs(rr,state):
        z0,v0,b0,ell0 = state
        vd0,bd0,ep0 = fun(rr,z0,v0,b0)
        return [v0,vd0,bd0,ep0]

    def jets(rr,state):
        z0,v0,b0,_ = state
        args = (rr,z0,v0,b0)
        vd0,bd0,ep0 = fun(*args)
        flow = np.array([1,v0,vd0,bd0],dtype=float)
        gg = np.array(epg(*args),dtype=float).reshape(4)
        hh = np.array(eph(*args),dtype=float)
        jj = np.array(jac(*args),dtype=float)
        acc = jj@flow
        return [rr,b0,bd0,acc[3],ep0,gg@flow,flow@hh@flow+gg@acc]
    return rhs, jets, pot, {'k':float(k),'Hv':float(hv),'nu':float(nu),
                          'a':float(aa),'lambda':float(lam),'s':float(ss)}


def invert_metric(rs, metric_jets, geom):
    # No source field or parameter argument. First two calibration indices
    # reconstruct lambda; later rows check the integral identity.
    if not np.all(np.isfinite(metric_jets)) or np.any(metric_jets[:, 0] <= 0) or np.any(metric_jets[:, 1] <= 0):
        raise ValueError('Nonregular metric input')
    radial_null_denominator = metric_jets[:, 1]*(1/rs-metric_jets[:, 4])
    if np.any(np.abs(radial_null_denominator) < 1e-12):
        raise ValueError('Excluded tangential-null denominator')
    vals = np.array([geom(*row) for row in metric_jets],dtype=float).T
    u,up,hh,jj,ww,gt,gr,ga = vals
    if not np.all(np.isfinite(vals)) or np.any(np.abs(u) < 1e-12) or np.any(hh <= 0):
        raise ValueError('Excluded constant or nonpositive-kinetic branch')
    integral = cumulative_simpson(u,x=rs,initial=0)
    ia,ib = 0,len(rs)//3
    ee = np.exp(-(integral[ib]-integral[ia]))
    if abs(1-ee) < 1e-12:
        raise ValueError('Excluded integral denominator')
    lam = (jj[ib]-ee*jj[ia])/(1-ee)
    if lam <= 1 or np.any(jj <= 0) or np.any(lam <= jj):
        raise ValueError('Outside candidate positive parameter domain')
    k = (1-2/np.sqrt(1+3*lam))/3
    aa = lam/(1+3*lam)
    ss = (1+k)/(k*(1-3*k))
    yy = ss*jj/(lam-jj)
    xx = ss+yy
    pp = xx*ww
    a0 = 3*(ss+yy*yy)
    a1 = yy*yy*np.log(yy)**2/(4*aa)
    # Potential coefficients use those same two radii, leaving later
    # points as synthetic validation. They are not empirical holdouts.
    mat = np.array([[a0[ia],a1[ia]],[a0[ib],a1[ib]]])
    if abs(np.linalg.det(mat)) < 1e-12:
        raise ValueError('Excluded potential determinant')
    h2,h2nu = np.linalg.solve(mat,pp[[ia,ib]])
    if not np.all(np.isfinite([h2,h2nu])) or h2 <= 0 or h2nu <= 0:
        raise ValueError('Outside positive candidate potential domain')
    predicted_j = lam+(jj[0]-lam)*np.exp(-integral)
    result = {'k':float(k),'lambda':float(lam),'Hv_squared':float(h2),
              'nu':float(h2nu/h2),'potential_matrix_det':float(np.linalg.det(mat)),
              'potential_condition':float(np.linalg.cond(mat)),
              'max_integral_identity_error':float(np.max(np.abs(jj-predicted_j))),
              'max_potential_residual':float(np.max(np.abs(pp-h2*a0-h2nu*a1))),
              'max_later_integral_identity_error':float(np.max(np.abs(jj[ib+1:]-predicted_j[ib+1:]))),
              'max_later_potential_residual':float(np.max(np.abs((pp-h2*a0-h2nu*a1)[ib+1:]))),
              'min_lambda_minus_j':float(np.min(lam-jj)),
              'min_H':float(np.min(hh)),'min_abs_u':float(np.min(np.abs(u))),
              'calibration_indices':[ia,ib],'test_row_count':len(rs)-ib-1,'test_first_index':ib+1}
    return result,yy,vals


def lambda_error_bound(jahat, jbhat, ihat, eja, ejb, ei):
    """A deterministic bound conditional on admitted j and integral errors."""
    if not np.all(np.isfinite([jahat,jbhat,ihat,eja,ejb,ei])):
        raise ValueError('Nonfinite error input')
    with np.errstate(over='ignore',invalid='ignore'):
        eh = np.exp(-ihat)
        ee = eh*np.expm1(ei)
    gap = abs(1-eh)-ee
    if not np.all(np.isfinite([eh,ee,gap])) or min(eja,ejb,ei) < 0 or gap <= 0:
        raise ValueError('No certified inverse denominator')
    lh = (jbhat-eh*jahat)/(1-eh)
    error=(ejb+(eh+ee)*eja+abs(lh-jahat)*ee)/gap
    if not np.all(np.isfinite([lh,error])):
        raise ValueError('Nonfinite inverse/error result')
    return lh,error


def symbolic_controls():
    checks=[]
    def exact(name,expression):
        value=sp.simplify(expression)
        checks.append({'name':name,'passed':value==0,'residual':str(value)})
    r,t,theta,phi=sp.symbols('r t theta phi',positive=True)
    b=sp.Function('B')(r); ell=sp.Function('ell')(r)
    coords=(t,r,theta,phi)
    metric=sp.diag(-sp.exp(2*ell),1/b,r*r,r*r*sp.sin(theta)**2)
    inverse=metric.inv()
    gamma={}
    for a in range(4):
        for j in range(4):
            for k in range(4):
                v=sum(inverse[a,n]*(sp.diff(metric[n,k],coords[j])+
                    sp.diff(metric[n,j],coords[k])-sp.diff(metric[j,k],coords[n]))/2
                    for n in range(4))
                if v!=0:gamma[a,j,k]=sp.simplify(v)
    def g(a,j,k):return gamma.get((a,j,k),sp.S.Zero)
    ric=[]
    for j in range(4):
        v=sum(sp.diff(g(a,j,j),coords[a])-sp.diff(g(a,j,a),coords[j])+
              sum(g(a,j,j)*g(n,a,n)-g(n,j,a)*g(a,j,n) for n in range(4))
              for a in range(4))
        ric.append(sp.simplify(v*inverse[j,j]))
    curv=sp.simplify(sum(ric))
    gt=(b-1)/r**2+sp.diff(b,r)/r
    gr=(b-1)/r**2+2*b*sp.diff(ell,r)/r
    ga=b*(sp.diff(ell,r,2)+sp.diff(ell,r)**2+sp.diff(ell,r)/r)+sp.diff(b,r)*(sp.diff(ell,r)+1/r)/2
    for name,a,v in [('time',0,gt),('radial',1,gr),('angular',2,ga),('azimuth',3,ga)]:
        exact('direct_Christoffel_'+name,ric[a]-curv/2-v)
    z=sp.Function('z')(r); f0,ss,lam=sp.symbols('f0 s lambda',positive=True)
    ff=f0*(ss+z*z); zz=f0/lam; vv=sp.Function('V')(z)
    fp=sp.diff(ff,r); fpp=sp.diff(ff,r,2); zp=sp.diff(z,r)
    ep=sp.diff(ell,r); bp=sp.diff(b,r)
    rho=-ff*gt-b*zz*zp*zp-vv-b*fpp-(bp/2+2*b/r)*fp
    pr=ff*gr-b*zz*zp*zp+vv+b*(ep+2/r)*fp
    pt=ff*ga+b*zz*zp*zp+vv+b*fpp+(bp/2+b*ep+b/r)*fp
    exact('tangential_null_stress',rho+pt-(ff*(ga-gt)-b*(1/r-ep)*fp))
    exact('radial_null_stress',rho+pr-(ff*(gr-gt)-2*b*zz*zp*zp-b*fpp-(bp/2-b*ep)*fp))
    boxz=b*sp.diff(z,r,2)+(bp/2+b*ep+2*b/r)*zp
    ez=2*zz*boxz+f0*z*curv-sp.diff(vv,z)
    conservation=sp.diff(pr,r)+ep*(rho+pr)+2*(pr-pt)/r
    exact('original_Bianchi_scalar_contraction',conservation+ez*zp)
    y,u,h,j=sp.symbols('Y u H j',positive=True)
    x=ss+y
    exact('kinetic_ratio',b*u*u/(2*(b*x*u*u/(2*lam*y)))-lam*y/x)
    exact('algebraic_Y', (ss*j/(lam-j)-y).subs(j,lam*y/(ss+y)))
    exact('integrability_identity',sp.diff(lam*sp.Function('Y')(r)/(ss+sp.Function('Y')(r)),r)
          -sp.diff(sp.Function('Y')(r),r)/(ss+sp.Function('Y')(r))*(lam-lam*sp.Function('Y')(r)/(ss+sp.Function('Y')(r))))
    ja,jb,ee=sp.symbols('ja jb E')
    exact('pair_inverse',((jb-ee*ja)/(1-ee)-lam).subs(jb,lam+(ja-lam)*ee))
    k=sp.symbols('k',positive=True); aa=(1-k)*(1+3*k)/4
    exact('lambda_parameter_identity',aa/(1-3*aa)-(1+2*k-3*k*k)/(1-3*k)**2)
    exact('potential_basis',3*(ss+y*y)+sp.symbols('nu')*y*y*sp.log(y)**2/(4*aa)
          -(3*(ss+y*y)+sp.symbols('nu')*y*y*sp.log(sp.sqrt(y))**2/aa))
    # Constant z=1 Schwarzschild-de Sitter: all candidate k,nu share metric.
    mass,hv=sp.symbols('M Hv',positive=True)
    bs=1-2*mass/r-hv*hv*r*r
    es=sp.log(bs)/2
    substitution={b:bs,ell:es}
    for name,v in [('tt',gt),('rr',gr),('theta',ga)]:
        exact('constant_branch_'+name,v.subs(substitution).doit()+3*hv*hv)
    zc,nuc=sp.symbols('zc nuc',positive=True)
    vc=f0*hv*hv*(3*(ss+zc**4)+nuc*zc**4*sp.log(zc)**2/aa)
    exact('constant_branch_scalar',(f0*zc*12*hv*hv-sp.diff(vc,zc)).subs(zc,1))
    # A geometrically nonconstant, pointwise-positive algebraic candidate
    # need not be integrable: N=1, B=2/3, fixed lambda=2 gives Y=s/3.
    upoint=sp.simplify(((ga-gt)/(b*(1/r-ep))).subs({b:sp.Rational(2,3),ell:0}).doit())
    hpoint=sp.simplify((gr-gt).subs({b:sp.Rational(2,3),ell:0}).doit()-sp.Rational(2,3)*(sp.diff(upoint,r)+upoint**2))
    jpoint=sp.simplify(sp.Rational(2,3)*upoint**2/(2*hpoint));lpoint=sp.Integer(2)
    exact('false_positive_geometry_j',jpoint-sp.Rational(1,2))
    ypoint=ss*jpoint/(lpoint-jpoint)
    exact('false_positive_integrability_residual',sp.diff(sp.log(ss+ypoint),r)-upoint+1/(2*r))
    checks.append({'name':'false_positive_residual_is_nonzero','passed':bool(upoint!=0)})
    return checks


def controls():
    checks=symbolic_controls()
    details=[]
    def add(name,condition,**data):
        checks.append({'name':name,'passed':bool(condition),**data})
    geom=geometry_functions()
    cases=[(0.1,0.03,1.2,1.4,0.22,0.9,0),
           (0.22,0.05,0.7,1.2,-0.12,0.95,0),
           (0.1,0.03,1.2,1.4,0.22,0.9,0.15)]
    for ci,(k,hv,nu,z0,v0,b0,deformation) in enumerate(cases):
        rhs,jets,pot,source=make_generator(k,hv,nu,deformation)
        rs=np.linspace(1,1.8,601)
        sol=solve_ivp(rhs,(rs[0],rs[-1]),[z0,v0,b0,0],method='DOP853',
                      rtol=2e-12,atol=2e-14,dense_output=True)
        add(f'fixture{ci}_ODE_completed',sol.success)
        if not sol.success:continue
        states=sol.sol(rs).T
        mj=np.array([jets(rr,state) for rr,state in zip(rs,states)])
        try:
            inv,yy,vals=invert_metric(rs,mj,geom)
            add(f'fixture{ci}_inverse_admitted',True)
        except ValueError as error:
            add(f'fixture{ci}_inverse_admitted',False,error=str(error))
            continue
        residuals=[]
        for ii,(rr,state,row) in enumerate(zip(rs,states,mj)):
            zz,vv,bb,_=state;_,_,bp,bpp,e1,e2,e3=row
            vd=rhs(rr,state)[1]
            ff=source['s']+zz*zz;kin=1/source['lambda']
            fp=2*zz*vv;fpp=2*vv*vv+2*zz*vd
            vp,vpz=pot(zz)
            gt,gr,ga=vals[5:,ii]
            ett=ff*gt+bb*kin*vv*vv+vp+bb*fpp+(bp/2+2*bb/rr)*fp
            err=ff*gr-bb*kin*vv*vv+vp+bb*(e1+2/rr)*fp
            eaa=ff*ga+bb*kin*vv*vv+vp+bb*fpp+(bp/2+bb*e1+bb/rr)*fp
            curvature=-(gt+gr+2*ga)
            scalar=2*kin*(bb*vd+(bp/2+bb*e1+2*bb/rr)*vv)+zz*curvature-vpz
            residuals.append([ett,err,eaa,scalar])
        max_res=np.max(np.abs(residuals),axis=0)
        for ii,label in enumerate(['tt','rr','theta','scalar']):
            add(f'fixture{ci}_original_{label}',max_res[ii]<1e-10,max_residual=float(max_res[ii]))
        add(f'fixture{ci}_recovered_k',abs(inv['k']-k)<2e-8,error=abs(inv['k']-k))
        erry=float(np.max(np.abs(yy-states[:,0]**2)))
        add(f'fixture{ci}_recovered_profile',erry<2e-7,error=erry)
        add(f'fixture{ci}_integral_reserved_rows',inv['max_later_integral_identity_error']<1e-8)
        if not deformation:
            add(f'fixture{ci}_recovered_Hv2',abs(inv['Hv_squared']-hv*hv)<2e-9)
            add(f'fixture{ci}_recovered_nu',abs(inv['nu']-nu)<2e-7)
            add(f'fixture{ci}_potential_reserved_rows',inv['max_later_potential_residual']<1e-9)
            scaled=mj.copy();factor=7.
            scaled[:,0]*=factor
            for idx,power in [(2,1),(3,2),(4,1),(5,2),(6,3)]:scaled[:,idx]/=factor**power
            si,sy,_=invert_metric(rs*factor,scaled,geom)
            add(f'fixture{ci}_length_scale_k_nu',abs(si['k']-inv['k'])<1e-8 and abs(si['nu']-inv['nu'])<2e-7)
            add(f'fixture{ci}_length_scale_Hv',abs(si['Hv_squared']*factor**2-inv['Hv_squared'])<2e-9)
            add(f'fixture{ci}_profile_scale_invariance',float(np.max(np.abs(sy-yy)))<2e-7)
        else:
            add('altered_potential_fails_reserved_rows',inv['max_later_potential_residual']>1e-8,
                residual=inv['max_later_potential_residual'])
        details.append({'source':source,'initial':[z0,v0,b0,0], 'deformation':deformation,
                        'inverse':inv,'original_equation_residuals':max_res.tolist(),
                        'field_error':erry,'domain':[1,1.8],'rows':len(rs)})
    # Numerical branch guards are fixture guards, not certified observation errors.
    rr=np.linspace(2,3,31);mm=0.1;hh=0.03
    r=sp.symbols('r',positive=True);bs=1-2*mm/r-hh*hh*r*r;es=sp.log(bs)/2
    funcs=sp.lambdify(r,[bs,sp.diff(bs,r),sp.diff(bs,r,2),sp.diff(es,r),sp.diff(es,r,2),sp.diff(es,r,3)],'numpy')
    mj=np.array([[x]+list(funcs(x)) for x in rr])
    with np.errstate(all='ignore'):
        try:invert_metric(rr,mj,geom);rejected=False
        except ValueError:rejected=True
    add('constant_field_metric_rejected_by_inverse',rejected)
    # Preserve exact generated instances, with no tuning to a numerical answer.
    max_violation=0.
    for ja in [.1,.3,.8]:
        for lam in [1.2,2.4,11.2]:
            for ii in [-.3,.2,.6]:
                jb=lam+(ja-lam)*np.exp(-ii)
                for sa,sb,si in [(-1,-1,-1),(1,1,1),(-1,1,-1),(1,-1,1)]:
                    ja_h=ja+sa*1e-5;jb_h=jb+sb*2e-5;i_h=ii+si*1e-4
                    lh,err=lambda_error_bound(ja_h,jb_h,i_h,1e-5,2e-5,1e-4)
                    max_violation=max(max_violation,abs(lh-lam)-err)
    add('conditional_finite_error_enclosure',max_violation<=1e-12,max_violation=max_violation)
    try:lambda_error_bound(.1,.2,1e-8,1e-5,1e-5,1e-4);guard=False
    except ValueError:guard=True
    add('finite_error_denominator_guard',guard)
    for field in range(6):
        args=[.1,.3,.2,1e-5,2e-5,1e-4];args[field]=float('nan')
        try:lambda_error_bound(*args);guard=False
        except ValueError:guard=True
        add('nonfinite_error_input_'+str(field),guard)
    rhs,jets,_,_=make_generator(.1,.03,-1.2)
    rr=np.linspace(1,1.15,61)
    sol=solve_ivp(rhs,(rr[0],rr[-1]),[1.4,.22,.9,0.],method='DOP853',rtol=2e-12,atol=2e-14,dense_output=True)
    mj=np.array([jets(r0,sol.sol(r0)) for r0 in rr])
    try:invert_metric(rr,mj,geom);guard=False
    except ValueError as error:guard='positive candidate potential' in str(error)
    add('negative_potential_parameter_guard',guard,solver_success=bool(sol.success),scope='extra short local domain-refusal fixture, not an admitted candidate')
    return {'checks':checks,'synthetic_fixtures':details,
            'empirical_tests':0,'new_observation_arrays':0}
