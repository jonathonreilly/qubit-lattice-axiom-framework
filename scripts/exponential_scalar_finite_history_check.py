#!/usr/bin/env python3
"""Finite-amplitude history, conditional local past curve and physical curvature."""
import json
import sys
import sympy as s
import mpmath as mp

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/EXPONENTIAL_SCALAR_FINITE_HISTORY_BOUNDED_THEOREM_NOTE_2026-10-14.md",
    "docs/EXPONENTIAL_SCALAR_ALTERNATIVE_RADIATION_BOUNDED_THEOREM_NOTE_2026-10-14.md",
)

def run_checks():
    rows = []


    def check(name, ok, **extra):
        rows.append(dict(name=name, passed=bool(ok), **extra))


    def zero(name, expression):
        reduced = s.factor(s.cancel(expression))
        check(name, reduced == 0, residual=str(reduced))


    k, theta, eta, z, p, q = s.symbols('k theta eta z p q', real=True)
    a = (1-k)*(1+3*k)/4
    ss = (1+k)/(k*(1-3*k))
    Ex = (1-3*k)/(3*(1+k))
    E = Ex*s.exp(theta)
    F = 1+ss*E
    J = 1+(1-3*a)*ss*E
    d = 2*(1+k)/3
    A = J/(4*a*F**2)
    Binf = (1+ss)*2*k/(3*(1+k)*F)
    B = Binf/(1+eta/d)
    C = (1+ss)*E/F
    Kxx = (1+ss)*4*k/(9*F*(1+d/eta))
    zero('original.metric_x_transform', Kxx/eta-B)
    zero('metric.theta_derivative_ratio', s.diff(B,theta)/B+s.diff(F,theta)/F)
    zero('connection.ell_ell_ell', -eta*s.diff(B,eta)/B-eta/(d+eta))
    zero('connection.theta_ell_ell', -s.diff(B,theta)/(2*A)+s.diff(Binf,theta)/(2*A*(1+eta/d)))
    r = 1/(1+3*k)
    b = 2*k*(1-k)/((1+k)*(1-3*k))
    zero('original.branch_B', Binf.subs(theta,0)-b)
    zero('original.branch_Btheta', s.diff(Binf,theta).subs(theta,0)+r*b)
    zero('original.branch_clock', (1/F).subs(theta,0)-(1-r))

    # The complete U0 must not be included in the physical ell gradient.
    Vq, Vzero = s.symbols('Vq Vzero')
    Wtotal = s.exp(2*z)*(Vq+eta*Vzero)
    zero('potential.physical_ell_force', s.diff(Wtotal,z)-2*eta*s.diff(Wtotal,eta)-2*s.exp(2*z)*Vq)

    # A single finite-flow constructor is checked in generic lowered equations
    # and used by the full numerical derivative/tangent probes.
    def finite_flow(AA,At,BB,Bt,CC,WQ,Uzero,Uzero_t,ZZ,LL,FF,PP,QQ,EE,DD):
        TT=AA*PP**2+BB*QQ**2
        HB=2*(CC**2+WQ+EE*ZZ*Uzero)/(3-TT)
        hh=-4*CC**2/(3*HB)-TT
        return [PP,QQ+2+PP/FF,
            -(3+hh)*PP-At*PP**2/(2*AA)+Bt*QQ**2/(2*AA)+(LL*WQ-EE*ZZ*Uzero_t)/(AA*HB),
            -(3+hh)*QQ-Bt*PP*QQ/BB-EE*QQ**2/(DD+EE)-2*WQ/(BB*HB),
            -2*QQ*EE],HB,hh

    AA,At,BB,Bt,CC,WQ,Uzero,Uzero_t,ZZ,LL,FF,DD=s.symbols('AA At BB Bt CC WQ Uzero Uzero_t ZZ LL FF DD')
    flow,hhbar,hh=finite_flow(AA,At,BB,Bt,CC,WQ,Uzero,Uzero_t,ZZ,LL,FF,p,q,eta,DD)
    zero('full_flow.lowered_theta',AA*hhbar*(flow[2]+(3+hh)*p)+hhbar*At*p*p/2-hhbar*Bt*q*q/2-LL*WQ+eta*ZZ*Uzero_t)
    zero('full_flow.lowered_ell',BB*hhbar*(flow[3]+(3+hh)*q)+hhbar*Bt*p*q+hhbar*BB*eta*q*q/(DD+eta)+2*WQ)
    zero('full_flow.clock_binding',flow[1]-q-2-p/FF)
    zero('full_flow.eta_binding',flow[4]+2*q*eta)
    zero('full_flow.constraint',hhbar*(3-AA*p*p-BB*q*q)-2*(CC*CC+WQ+eta*ZZ*Uzero))

    # Original x,y pullback and determinant of the open smooth extension.
    ell,w=s.symbols('ell w',real=True)
    Bg=s.symbols('Bg',positive=True)
    xy_metric=s.diag(Bg/(s.exp(2*ell)*(1+w*w+eta/d)),3*Bg/(4*s.exp(2*ell)*(1+w*w+eta/d)))
    pull=s.Matrix([[s.exp(ell),0],[w*s.exp(ell),s.exp(ell)]])
    G2=s.simplify(pull.T*xy_metric*pull)
    Gexpected=Bg/(1+w*w+eta/d)*s.Matrix([[1+3*w*w/4,3*w/4],[3*w/4,s.Rational(3,4)]])
    for i in range(2):
        for jj in range(2):zero(f'metric.normal_pullback_{i}{jj}',G2[i,jj]-Gexpected[i,jj])
    zero('metric.extension_determinant',G2.det()-3*Bg**2/(4*(1+w*w+eta/d)**2))

    # Differentiate the exact finite-eta flow at theta=z=p=0, q=-2.
    bg, ag, rg, dg, v0, v1, H0 = s.symbols('b A r d v0 v1 H0', nonzero=True)
    D = 3-4*bg
    Bg = bg/(1+eta/dg)
    Bgtheta = -rg*bg/(1+eta/dg)
    C2 = s.Rational(3,2)*(1-2*bg)*H0
    Wq = bg*H0
    Wt = Wq+eta*H0*v0
    HB = 2*(C2+Wt)/(3-4*Bg)
    h = -4*C2/(3*HB)-4*Bg
    fp = 2*Bgtheta/ag+(2*rg*Wq-eta*H0*v1)/(ag*HB)
    fq = 2*(3+h)-4*eta/(dg+eta)-2*Wq/(Bg*HB)
    j = (2*v0-4*bg/dg)/D
    expected_fp = (2*rg*bg*(1/dg-j)-v1)/ag
    expected_fq = 4*v0-6/dg
    zero('full_flow.fixed_p', fp.subs(eta,0))
    zero('full_flow.fixed_q', fq.subs(eta,0))
    zero('forcing.Hbar_log_slope', (s.diff(HB,eta)/HB).subs(eta,0)-j)
    zero('forcing.p', s.diff(fp,eta).subs(eta,0)-expected_fp)
    zero('forcing.q', s.diff(fq,eta).subs(eta,0)-expected_fq)
    eta_flow = -2*q*eta
    zero('eta.chain_rule', eta_flow-(-2*s.exp(-2*s.Symbol('ell'))*q).subs(s.exp(-2*s.Symbol('ell')),eta))
    zero('eta.new_eigenvalue', s.diff(eta_flow,eta).subs(q,-2)-4)
    zero('eta.lower_left', s.diff(eta_flow,q).subs(eta,0))

    # Riemann contraction in an orthonormal flat-FLRW frame, not a lookup value.
    HH, DH = s.symbols('H Hdot', real=True)
    R = {}
    def add_component(i,j,l,m,value):
        for indices,sign in [((i,j,l,m),1),((j,i,l,m),-1),((i,j,m,l),-1),((j,i,m,l),1),((l,m,i,j),1),((m,l,i,j),-1),((l,m,j,i),-1),((m,l,j,i),1)]:
            if indices in R:
                assert s.simplify(R[indices]-sign*value)==0
            R[indices]=sign*value
    for i in range(1,4):
        add_component(0,i,0,i,-(DH+HH**2))
    for i in range(1,4):
        for j2 in range(i+1,4):
            add_component(i,j2,i,j2,HH**2)
    signature=[-1,1,1,1]
    kretsch=sum(signature[i]*signature[j2]*signature[l]*signature[m]*value**2 for (i,j2,l,m),value in R.items())
    zero('curvature.full_contraction', kretsch-12*(HH**4+(DH+HH**2)**2))
    zero('curvature.radiation_leading', kretsch.subs(DH,-2*HH**2)-24*HH**4)
    cc = s.symbols('c', positive=True)
    time_primitive=s.sqrt(eta)/(2*s.sqrt(cc))
    zero('time.finite_past_integrand', s.diff(time_primitive,eta)-1/(4*s.sqrt(cc)*s.sqrt(eta)))

    # Bind the implementation's coefficient functions to a separately
    # differentiated expression of the displayed complete action.
    nu_ref=s.symbols('nu_ref',positive=True)
    alpha_ref=s.sqrt(a)
    u_ref=(s.log(Ex)+theta)/(2*alpha_ref)
    U0_ref=s.Rational(3,2)+3*ss*(E-1)**2/(2*F**2)+nu_ref*(1+ss)*u_ref*u_ref/(2*F**2)
    fields_reference=s.lambdify((k,theta,nu_ref),[A,Binf,C,U0_ref,F], 'mpmath')
    U0t_reference=s.lambdify((k,theta,nu_ref),s.diff(U0_ref,theta),'mpmath')

    # Direct finite-action evaluation. mpmath differentiates the full functions;
    # no previous producer flow, matrix or numerical outputs are imported.
    mp.mp.dps=70
    numerics=[]
    for ks in ['0.0001','0.01','0.1','0.17']:
        for nus in ['0.1','1','10']:
            kv=mp.mpf(ks); nv=mp.mpf(nus)
            av=(1-kv)*(1+3*kv)/4; al=mp.sqrt(av)
            sv=(1+kv)/(kv*(1-3*kv)); ev=(1-3*kv)/(3*(1+kv))
            ux=mp.log(ev)/(2*al); dv=2*(1+kv)/3
            bv=2*kv*(1-kv)/((1+kv)*(1-3*kv)); cv=(1-kv)/(1+kv)
            hb0=2*cv**2/(3*(1-2*bv)); w0=bv*hb0
            lv=2/(1+3*kv); betasq=2*w0*mp.exp((1-kv)*ux/al)/kv

            def fields(t):
                ee=ev*mp.exp(t); ff=1+sv*ee
                aa=(1+(1-3*av)*sv*ee)/(4*av*ff**2)
                bb=(1+sv)*2*kv/(3*(1+kv)*ff)
                ccv=(1+sv)*ee/ff
                uu=ux+t/(2*al)
                u0=mp.mpf('1.5')+mp.mpf('1.5')*sv*(ee-1)**2/ff**2+nv*(1+sv)*uu**2/(2*ff**2)
                return aa,bb,ccv,u0,ff

            for tv in [mp.mpf('0'),mp.mpf('0.07')]:
                ref=mp.matrix(fields_reference(kv,tv,nv))
                got=mp.matrix(fields(tv))
                label=ks+'_'+nus+'_'+str(tv)
                check('action.coefficient_binding.'+label,mp.norm(ref-got)<mp.mpf('1e-50'))
                check('action.U0_gradient_binding.'+label,abs(U0t_reference(kv,tv,nv)-mp.diff(lambda tt:fields(tt)[3],tv))<mp.mpf('1e-50'))

            def flow(t,zz,pp,qq,ee):
                aa,bb0,ccv,u0,ff=fields(t)
                aa1=mp.diff(lambda tt:fields(tt)[0],t)
                bb1=mp.diff(lambda tt:fields(tt)[1],t)/(1+ee/dv)
                u01=mp.diff(lambda tt:fields(tt)[3],t)
                bb=bb0/(1+ee/dv)
                wq=w0*mp.exp(2*zz-lv*t); Z=betasq*mp.exp(2*zz)
                wt=wq+ee*Z*u0
                T=aa*pp**2+bb*qq**2
                hb=2*(ccv**2+wt)/(3-T); hh=-4*ccv**2/(3*hb)-T
                vals,_,_=finite_flow(aa,aa1,bb,bb1,ccv,wq,u0,u01,Z,lv,ff,pp,qq,ee,dv)
                return mp.matrix(vals)

            point=(mp.mpf(0),mp.mpf(0),mp.mpf(0),mp.mpf(-2),mp.mpf(0))
            matrix=mp.matrix(5)
            for i in range(5):
                for j2 in range(5):
                    def element(v):
                        xx=list(point);xx[j2]=v
                        return flow(*xx)[i]
                    matrix[i,j2]=mp.diff(element,point[j2])
            MM=matrix[:4,:4]; forcing=matrix[:4,4]
            A0v=fields(0)[0]; vv0=betasq*fields(0)[3]/hb0
            vv1=betasq*mp.diff(lambda tt:fields(tt)[3],0)/hb0
            jj=(2*vv0-4*bv/dv)/(3-4*bv)
            fhand=mp.matrix([0,0,(lv*bv*(1/dv-jj)-vv1)/A0v,4*vv0-6/dv])
            label=ks+'_'+nus
            check('numeric.forcing.'+label,mp.norm(forcing-fhand)<mp.mpf('1e-50'),error=mp.nstr(mp.norm(forcing-fhand),20))
            check('numeric.block.'+label,all(abs(matrix[4,i])<mp.mpf('1e-60') for i in range(4)) and abs(matrix[4,4]-4)<mp.mpf('1e-60'))
            tangent=mp.lu_solve(4*mp.eye(4)-MM,forcing)
            check('numeric.tangent_linear.'+label,mp.norm((4*mp.eye(4)-MM)*tangent-forcing)<mp.mpf('1e-50'))
            scaled=[]
            for fraction in ['0.0001','0.00001','0.000001']:
                ee=mp.mpf(fraction)/(1+mp.norm(tangent))
                xx=tangent*ee
                actual=flow(xx[0],xx[1],xx[2],-2+xx[3],ee)
                residual=actual[:4,0]-tangent*actual[4]
                scaled.append(mp.norm(residual)/ee**2)
            check('numeric.quadratic_residual.'+label,max(scaled)/min(scaled)<mp.mpf('1.03'),scaled=[mp.nstr(v,25) for v in scaled])
            numerics.append({'k':ks,'nu':nus,'forcing':[mp.nstr(v,40) for v in forcing],'tangent':[mp.nstr(v,40) for v in tangent],'quadratic_residual_scaled':[mp.nstr(v,30) for v in scaled]})


    # Clock conversion and finite proper-time leading coefficient.
    HE,L,LD,hE,Cg=s.symbols('HE L LD hE Cg',nonzero=True)
    # L-1=(ln sqrt(C))' and dot_J=(HE/sqrt(C))*d_N.
    hJ=(hE+LD/L-(L-1))/L
    HJ=HE*L/s.sqrt(Cg)
    HJ_N=s.diff(HJ,HE)*hE*HE+s.diff(HJ,L)*LD+s.diff(HJ,Cg)*2*(L-1)*Cg
    zero('clock.exact_conversion',HJ_N*HE/s.sqrt(Cg)/HJ**2-hJ)
    zero('clock.physical_limit',hJ.subs({L:1,LD:0,hE:-2})+2)
    rho_phys,rho_unit,rho_J,Q,Hv,beta=s.symbols('rho_phys rho_unit rho_J Q Hv beta',positive=True)
    zero('density.symbol_translation',(rho_unit/(2*Q*Hv**2))*rho_J-(rho_phys/(2*Q*Hv**2)).subs(rho_phys,rho_unit*rho_J))
    tau=s.symbols('tau',positive=True)
    zero('curvature.proper_time_coefficient',(24*HH**4).subs(HH,1/(2*tau))-s.Rational(3,2)/tau**4)
    Sx,Px,lam=s.symbols('Sx Px lambda')
    cp=(lam*lam+lam)**2+Sx*(lam*lam+lam)+Px
    zero('tangent.characteristic_evaluation',cp.subs(lam,4)-(400+20*Sx+Px))
    check('tangent.uniform_algebraic_lower_margin',400+20*s.Rational(46,5)==584)
    zero('weak.formal_log_density_contrast',4*s.Rational(5,16)/k-s.Rational(5,4)/k)
    return dict(scope='Supplied action, ideal radiation and selected local past limit. Conditional finite history and singular physical past; no observations fitted.',checks=rows,counts=dict(passed=sum(x['passed'] for x in rows),failed=sum(not x['passed'] for x in rows)),numeric_cases=numerics)


if __name__ == '__main__':
    result=run_checks()
    print(json.dumps(result,indent=2,allow_nan=False))
    sys.exit(bool(result['counts']['failed']))
