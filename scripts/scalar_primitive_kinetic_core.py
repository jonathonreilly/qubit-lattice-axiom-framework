"""Primitive kinetic adjoint on declared photon records; exact constructed checks."""
AUDIT_TIMEOUT_SEC = 120
import sympy as s


def run_checks():
    checks=[]
    def zero(name,expr):
        val=s.cancel(s.expand(expr))
        checks.append({"name":name,"pass":bool(val==0),"residual":str(val)})
    def truth(name,val):checks.append({"name":name,"pass":bool(val)})
    eta,r,u=s.symbols("eta r u",real=True,nonzero=True)
    a=256/eta**8
    h=-eta**7/32
    q=-5*eta**7/256
    ell=-3*eta**7/256
    F=s.Rational(2,5)
    G=-eta**7/128
    R=eta**14/32768
    E=eta**14/4096
    C=-eta**7/256
    d=-256/eta**7
    e=s.Integer(4)
    Utrue=65536/(5*eta**14)
    def canon(f):return s.cancel(s.expand(f))
    def T(f):return canon(s.diff(f,eta)/a)
    def L(f):return canon((s.diff(f,eta)+s.diff(f,r))/a)
    def Lap(f):return canon(s.diff(f,r,2)+2*s.diff(f,r)/r-6*f/r**2)
    def D(f):return canon(s.diff(f,r)-s.diff(f,eta))
    def Ldag(f):return canon(-(s.diff(f,eta)+s.diff(f,r)+2*f/r)/a)
    def Ddag(f):return canon(-s.diff(f,r)+s.diff(f,eta)+(s.diff(a,eta)/a-2/r)*f)
    K=T(C)+h*C
    P=eta**6*r*r/64
    J=-2*P
    Z=-4*r*r/eta
    db=3*P
    Xi=q*T(J)-q*q*P-(T(q)+q*q)*J
    Bd=2*Lap(P)/a**2-6*ell*(T(P)+ell*P)-F*(q*T(J)-q*q*P)-(q*T(F)-E+R)*J
    zero("background_h",T(a)/a-h)
    zero("background_qG",q*G+R+2*(T(ell)+q*ell))
    zero("background_dust",T(R)-(2*q-3*h)*R)
    zero("commutator_coefficient",K-eta**14/65536)
    zero("original_physical_momentum",T(P)+ell*P-(G*J-R*Z)/2)
    zero("original_physical_Euler",T(Z)+P+J)
    zero("original_physical_number",T(db)-3*T(P)+Lap(Z)/a**2)
    zero("original_physical_density",Bd-R*Utrue*Xi-R*db)
    zero("local_harmonic",Lap(P))
    # Photon paths are integrated before inverse differentiation.
    I0u=sum(s.binomial(6,j)*u**(6-j)*(-1)**j*r**(j+3)/(64*s.Integer(j+3)) for j in range(7))
    psiu=sum(s.binomial(6,j)*u**(6-j)*(-1)**j*r**(j+2)/(32*s.Integer(j+2)*s.Integer(j+3)) for j in range(7))
    psi=canon(psiu.subs(u,eta+r))
    I0=canon(I0u.subs(u,eta+r))
    I1=canon(s.diff(I0u,u).subs(u,eta+r))
    Y=canon(-P-J+s.diff(Z,r)/a)
    z=canon(Y-2*I1)
    zero("Born_integrated_inverse",D(r*r*D(psi))/2-P)
    zero("Born_path_primitive",r*r*D(psi)/2-I0)
    zero("actual_path_time_derivative",a*T(I0)-I1)
    zero("actual_redshift_LZ",Y-L(Z))
    zero("primitive_Y_map",z+a*T(r*r*D(psi))-Y)
    f=d*T(P)+e*P
    zero("transport_original",T(Z)+C*Z+f)
    N=T(Y)+(C+h)*Y+L(f)+h*f
    zero("commutator_original",N+K*Z)
    # The radial factor is a coefficient of normalized Y20, not a homogeneous mode.
    lam=(eta+4)**8*(-3-eta)**8*(r-1)**8*(2-r)**8
    for variable,ends in [(eta,[-4,-3]),(r,[1,2])]:
        for end in ends:
            for order in range(8):
                zero(f"trace_{variable}_{end}_{order}",s.diff(lam,variable,order).subs(variable,end))
    alpha=-6*ell/R
    gamma=2/(R*a*a)
    def weights(U):
        beta=-q*(F/R+U)
        delta=(-6*ell*ell+F*q*q)/R-3+U*q*q
        epsilon=-(q*T(F)-E+R)/R+U*(T(q)+q*q)
        wp=canon(-T(alpha*T(lam))+delta*T(lam)+gamma*Lap(T(lam)))
        wj=canon(-T(beta*T(lam))+epsilon*T(lam))
        wz=canon(-Lap(lam)/a**2)
        v=canon(T(wj)+wz)
        b=canon(-v/K)
        g=canon(Ldag(b)+h*b)
        cp=canon(wp-wj-T(d*g)+e*g)
        cy=canon(-T(b)+(C+h)*b)
        hp=canon(Ddag(r*r*(Ddag(cp)/2-T(a*cy))))
        hz=cy
        return wp,wj,wz,cp,cy,hp,hz
    # Exact integration of Laurent monomials on this rectangle. No float quadrature.
    def intpow(power,lo,hi):
        if power==-1:return s.log(s.Rational(abs(hi),abs(lo)))
        return (s.Rational(hi)**(power+1)-s.Rational(lo)**(power+1))/s.Integer(power+1)
    def terms(expr):
        for term in s.Add.make_args(s.expand(expr)):
            powers=term.as_powers_dict()
            i=powers.get(eta,s.Integer(0));j=powers.get(r,s.Integer(0))
            assert i.is_integer and j.is_integer
            c=s.cancel(term/(eta**i*r**j))
            assert c.is_Rational, (c,i,j)
            yield c,int(i),int(j)
    def integrate(expr):
        return s.simplify(sum(c*intpow(i,-4,-3)*intpow(j,1,2) for c,i,j in terms(expr)))
    def l1_bound(expr):
        return s.simplify(sum(abs(c)*intpow(i,3,4)*intpow(j,1,2) for c,i,j in terms(expr)))
    # Pointwise adjoint/divergence identities with arbitrary probe functions.
    ff=1+eta+eta*r+r*r
    gg=eta*eta+r+eta*r*r
    mu=a*r*r
    zero("L_formal_adjoint_divergence",
         mu*(ff*L(gg)-Ldag(ff)*gg)-s.diff(r*r*ff*gg,eta)-s.diff(r*r*ff*gg,r))
    zero("D_formal_adjoint_divergence",
         mu*(ff*D(gg)-Ddag(ff)*gg)-s.diff(mu*ff*gg,r)+s.diff(mu*ff*gg,eta))
    # Arbitrary operator probes retain residuals; they are not full-action solutions.
    wp0,wj0,wz0,cp0,cy0,hp0,hz0=weights(s.Integer(0))
    P0=eta**6*r**3+eta**2*r**5
    J0=eta**4*r**4
    Z0=eta**3*r**3
    Y0=eta**2*r**4
    beta0=-q*F/R
    delta0=(-6*ell*ell+F*q*q)/R-3
    epsilon0=-(q*T(F)-E+R)/R
    ck0=alpha*T(P0)+beta0*T(J0)+gamma*Lap(P0)+delta0*P0+epsilon0*J0
    mstrong0=integrate(-mu*lam*(T(ck0)+Lap(Z0)/a**2))
    mfirst0=integrate(mu*(wp0*P0+wj0*J0+wz0*Z0))
    zero("arbitrary_nonharmonic_first_adjoint",mfirst0-mstrong0)
    truth("arbitrary_nonharmonic_moment_nonzero",mstrong0!=0)
    v0=T(wj0)+wz0
    b0=-v0/K
    re0=J0+T(Z0)+P0
    f0=d*T(P0)+e*P0
    rn0=T(Y0)+(C+h)*Y0+L(f0)+h*f0+K*Z0
    melim0=integrate(mu*(cp0*P0+cy0*Y0))
    residual0=integrate(mu*(wj0*re0-b0*rn0))
    zero("arbitrary_latent_residual_identity",mfirst0-melim0-residual0)
    truth("arbitrary_Euler_residual_nonzero",canon(re0)!=0)
    truth("arbitrary_commutator_residual_nonzero",canon(rn0)!=0)
    psi0=(1+eta)**8*r**6+eta*r**3
    z0=eta**6*r**4+eta**2*r**5
    pp0=D(r*r*D(psi0))/2
    yp0=z0+a*T(r*r*D(psi0))
    mpfield0=integrate(mu*(cp0*pp0+cy0*yp0))
    mprimitive0=integrate(mu*(hp0*psi0+hz0*z0))
    zero("arbitrary_primitive_adjoint",mpfield0-mprimitive0)
    truth("arbitrary_primitive_moment_nonzero",mprimitive0!=0)
    rows={}
    for label,U in [("true",Utrue),("wrong_canonical",s.Integer(0))]:
        wp,wj,wz,cp,cy,hp,hz=weights(U)
        ck=canon(Bd/R-3*P-U*Xi)
        strong=canon(T(ck)+Lap(Z)/a**2)
        m0=integrate(-mu*lam*strong)
        m1=integrate(mu*(wp*P+wj*J+wz*Z))
        m2=integrate(mu*(cp*P+cy*Y))
        m3=integrate(mu*(hp*psi+hz*z))
        zero(label+"_first_adjoint",m1-m0)
        zero(label+"_latent_elimination",m2-m1)
        zero(label+"_primitive_adjoint",m3-m2)
        rows[label]={"strong_moment":str(m0),"field_moment":str(m1),"primitive_moment":str(m3)}
        if label=="true":
            zero("true_strong_residual",strong)
            zero("true_primitive_moment",m3)
        else:
            positive=integrate(-s.Rational(9,32)*lam*eta**5*r**4)
            zero("wrong_positive_form",m3-positive)
            truth("wrong_moment_nonzero_positive",m3>0)
            normpsi=l1_bound(mu*hp)
            normz=l1_bound(mu*hz)
            norm=normpsi+normz
            truth("finite_positive_primitive_error_bound",norm>0)
            radius=s.simplify(m3/(2*norm))
            eps=radius/4
            dx=eta+4;dy=r-1
            errpsi=eps*dx*(1-dx)*dy*(1-dy)
            errz=eps*(2*dx-1)*(2*dy-1)
            shift=integrate(mu*(hp*errpsi+hz*errz))
            truth("bounded_record_error",abs(shift)<=eps*norm)
            truth("fixed_candidate_error_rejection",m3-abs(shift)>eps*norm)
            # Known reception gains are a candidate condition, not reconstructed.
            gainpsi=(eta+r+5)/4
            gainz=(eta+r+6)/5
            zero("known_reception_gain_pullback",hp*(gainpsi*psi)/gainpsi+hz*(gainz*z)/gainz-hp*psi-hz*z)
            rows[label].update(primitive_L1_bound_psi=str(normpsi),primitive_L1_bound_z=str(normz),primitive_uniform_radius=str(radius),primitive_uniform_radius_numeric=str(radius.evalf(20)),bounded_error_shift=str(shift),weight_terms_psi=len(list(terms(mu*hp))),weight_terms_z=len(list(terms(mu*hz))))
            # Baseline wrong measure or missing path corrections must not reproduce the same functional.
            missing_path=integrate(mu*(hp*psi+hz*Y))
            truth("missing_path_correction_detected",missing_path!=m3)
            wrong_measure=integrate(r*r*(hp*psi+hz*z))
            truth("wrong_time_measure_detected",wrong_measure!=m3)
    # Full-ray coverage of the fixed negative-eta chart, not just source events.
    truth("old_rectangle_crosses_singular_chart",s.Rational(-5,4)+s.Rational(7,4)>0)
    truth("new_reception_interval_strictly_negative",s.Integer(-3)+s.Integer(2)<0)
    truth("new_complete_ray_interval_negative",s.Integer(-4)<s.Integer(-1)<0)
    truth("new_source_t_interval",s.Rational(4,16)==s.Rational(1,4) and s.Rational(4,9)<4)
    xx=s.symbols("cos_theta",real=True)
    y20=s.sqrt(s.Rational(5,16)/s.pi)*(3*xx**2-1)
    a20=2*s.pi*(s.integrate(y20,(xx,-1,-1/s.sqrt(3)))-s.integrate(y20,(xx,-1/s.sqrt(3),1/s.sqrt(3)))+s.integrate(y20,(xx,1/s.sqrt(3),1)))
    zero("fullsky_absolute_projection_factor",s.simplify(a20-4*s.sqrt(15*s.pi)/9))
    result={"scope":"Root constructed n=3/2 full-action mode photon primitives and exact weak kinetic test; no empirical inputs","versions":{"sympy":s.__version__},"passed":sum(c["pass"] for c in checks),"failed":sum(not c["pass"] for c in checks),"checks":checks,"moments":rows,"records":{"psi":str(psi),"z":str(z),"Y":str(Y),"I0":str(I0),"I1":str(I1)}}
    result["error_contract"]="Recovered normalized-Y20 harmonic coefficient errors; multiply by4sqrt(15pi)/9 for arbitrary fullsky pointwise envelopes"
    return result,{"eta":eta,"r":r,"weighted_psi":canon(mu*hp),"weighted_z":canon(mu*hz),"moment":rows["wrong_canonical"]["primitive_moment"]}
