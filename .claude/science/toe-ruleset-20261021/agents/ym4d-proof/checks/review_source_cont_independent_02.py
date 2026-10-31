"""Independent continuation controls; no author-checker imports."""
import sympy as s
import mpmath as mp
import json,itertools,datetime,time
started=time.monotonic()
checks={}; controls={}; details={}
def check(name,value):
    checks[name]=bool(value)
    if not checks[name]: raise AssertionError(name)
def control(name,value):
    controls[name]=bool(value)
    if not controls[name]: raise AssertionError(name)
def zero(expr): return s.cancel(s.expand(expr))==0
R=s.Rational; ii=s.I
x,y,t=s.symbols('x y t', real=True)
p=R(3,2); sig=R(2,5)
C0=s.Matrix([[2,R(1,4)],[R(1,4),R(3,2)]])
E=s.Matrix([[ii/13,R(1,17)],[R(1,17),-ii/19]])
b0=s.Matrix([R(1,7),-R(1,11)])
d=s.Matrix([(1+ii)/23,(-2+ii)/29])
C=C0+t*E; W=s.Matrix([x,y]); aa=b0+t*d+sig*C*W
f=1+aa[0]**2+(1+ii)*aa[0]*aa[1]/7+aa[1]**3/11
J=sig**2*C.det()
def interval_poly(expr,vars):
    pol=s.Poly(s.expand(expr),*vars)
    out=0
    for degrees,coef in pol.terms():
        moment=1
        for k in degrees:
            moment*=0 if k%2 else 2*p**(k+1)/R(k+1)
        out+=coef*moment
    return s.expand(out)
volume=interval_poly(J*f,(x,y))
# Oriented boundary minors, constructed without inverse/determinant differentiation.
flux_vector=sig*C.adjugate()*d+sig**2*C.adjugate()*E*W
faces=[interval_poly((f*flux_vector[0]).subs(x,p),(y,)),
       -interval_poly((f*flux_vector[0]).subs(x,-p),(y,)),
       interval_poly((f*flux_vector[1]).subs(y,p),(x,)),
       -interval_poly((f*flux_vector[1]).subs(y,-p),(x,))]
flux=sum(faces)
check('affine_density_volume_derivative_equals_oriented_minors',zero(s.diff(volume,t)-flux))
check('affine_example_noncommuting_C0_E',C0*E!=E*C0)
control('omit_Jacobian_trace_term_detected',not zero((interval_poly(J*s.diff(f,t),(x,y))-flux).subs(t,R(2,5))))
control('reverse_one_face_detected',not zero((s.diff(volume,t)-(flux-2*faces[1])).subs(t,R(2,5))))
control('omit_coordinate_sigma_Jacobian_detected',not zero((volume-volume/sig**2).subs(t,R(2,5))))
details['affine_flux_at_s_2_5']=str(s.cancel(flux.subs(t,R(2,5))))
# Actual nonlinear force/Hessian interpolation, with independently differentiated F.
a1,a2=s.symbols('a1 a2'); b1=b0+d
C1=s.Matrix([[R(7,5),R(1,6)],[R(1,6),R(6,5)]])
K1=C1.inv()*C1.inv(); z=s.Matrix([a1,a2])-b1
F=(z.T*K1*z)[0]/2+z[0]**3/19
bs=b0+t*d; H=s.hessian(F,(a1,a2)); gs=s.Matrix([s.diff(F,a1),s.diff(F,a2)]).subs({a1:bs[0],a2:bs[1]})
Ht=H.subs({a1:bs[0],a2:bs[1]})
u=s.symbols('u',real=True)
force_integral=s.integrate(Ht.subs(t,u)*d,(u,t,1))
check('actual_force_equals_integrated_Hessian',all(zero(q) for q in gs+force_integral))
Cs=C0+t*(C1-C0); Q=Cs.T*Ht*Cs-s.eye(2)
Qsum=(Cs-C1).T*Ht*Cs+C1.T*(Ht-K1)*Cs+C1.T*K1*(Cs-C1)
check('quadratic_mismatch_subtracts_matching_identity',all(zero(q) for q in Q-Qsum))
control('missing_Hessian_difference_detected',any(not zero(q) for q in C1.T*(Ht-K1)*Cs))
# Seven independent spins, different connected component and disconnected bulk.
a,b,c,e,h,u0,r0,t0=s.symbols('a b c e h u r t0')
Z=0; pin=0; insertion=0
for ww in itertools.product((-1,1),repeat=7):
    weight=(1+a*ww[0]*ww[1])*(1+b*ww[1]*ww[2])*(1+c*ww[2]*ww[3])*(1+e*ww[3]*ww[4])*(1+h*ww[4])*(1+u0*ww[5]*ww[6])*(1+r0*ww[5])*(1+t0*ww[6])
    Z+=weight/R(128)
    if ww[0]==1:
        pin+=weight/R(64)
        insertion+=ww[2]*weight/R(64)
Z=s.expand(Z); pin=s.expand(pin); insertion=s.expand(insertion)
bulk=1+u0*r0*t0
check('spin_partition_disconnected_bulk_exact',zero(Z-bulk))
check('spin_pinned_ratio_exact',zero(pin/Z-(1+h*a*b*c*e)))
check('spin_remote_insertion_exact',zero(insertion/Z-(a*b+h*c*e)))
check('disconnected_replicas_cancel',zero((insertion*bulk**4)/(Z*bulk**4)-(a*b+h*c*e)))
control('omit_bulk_normalization_detected',not zero(insertion-(a*b+h*c*e)))
control('omit_remote_marked_attachment_detected',not zero(insertion/Z-a*b))
control('omit_remote_W_endpoint_detected',not zero(insertion/Z-pin/Z))
control('omit_original_remote_source_detected',s.diff(s.cancel(insertion/Z),h)==c*e)
# Label {0,2} loses the intervening connector on the host path.
def connected(label):
    if not label:return False
    seen={min(label)}
    while True:
        nxt=seen|{q for q in label if any(abs(q-v)==1 for v in seen)}
        if nxt==seen:return nxt==set(label)
        seen=nxt
check('velocity_connector_support_connected',connected({0,1,2}))
control('endpoint_only_label_is_disconnected',not connected({0,2}))
small=mp.mpf(2)**-18
h_bound=2*mp.exp(8)*small/(1-small)+mp.exp(4)*small/(1-small)
check('spin_model_has_small_complex_input_regime',h_bound<mp.mpf(1)/4)
details['spin_formula']={'Z':str(Z),'pin_ratio':str(s.cancel(pin/Z)),'insertion_ratio':str(s.cancel(insertion/Z)),'beta4_input_bound':str(h_bound)}
# Complex quadratic with nonzero B, fixed source-independent sector.
mp.mp.dps=80
sigq=mp.mpf(1)/7; cut=mp.mpf(5)/3; B=mp.mpf(1)/50; eps=mp.mpc(2,3)/10000; vacuum=mp.mpf(1)/4000
lo=B-sigq*cut; hi=B+sigq*cut
Fq=lambda aa:(aa-B)**2/2+eps*aa**2/2+vacuum
Iraw=mp.quad(lambda aa:mp.exp(-Fq(aa)/sigq**2),[lo,hi])
k=1+eps; center=B/k; Fmin=vacuum+B*B*eps/(2*k)
Ierf=mp.exp(-Fmin/sigq**2)*sigq/mp.sqrt(k)*mp.sqrt(mp.pi/2)*(mp.erf((hi-center)*mp.sqrt(k)/(mp.sqrt(2)*sigq))-mp.erf((lo-center)*mp.sqrt(k)/(mp.sqrt(2)*sigq)))
zcut=mp.erf(cut/mp.sqrt(2)); phi=lambda w:mp.exp(-w*w/2)/mp.sqrt(2*mp.pi)
reduced=mp.quad(lambda w:phi(w)*mp.exp(-eps*(B*w/sigq+w*w/2)),[-cut,cut])/zcut
prefactor=sigq*mp.sqrt(2*mp.pi)*zcut*mp.exp(-(vacuum+eps*B*B/2)/sigq**2)
Ifixed=prefactor*reduced
check('quadratic_direct_completed_square_agree',abs(Iraw-Ierf)<mp.mpf('1e-65'))
check('quadratic_direct_fixed_reference_agree',abs(Iraw-Ifixed)<mp.mpf('1e-65'))
wronglin=prefactor*mp.quad(lambda w:phi(w)*mp.exp(-eps*w*w/2),[-cut,cut])/zcut
control('omit_source_linear_term_detected',abs(Iraw-wronglin)>mp.mpf('1e-12'))
control('omit_cutoff_probability_detected',abs(Iraw-Ifixed/zcut)>mp.mpf('1e-3'))
control('omit_action_vacuum_detected',abs(Iraw-Ifixed*mp.exp((vacuum+eps*B*B/2)/sigq**2))>mp.mpf('1e-4'))
control('omit_completed_square_determinant_detected',abs(Iraw-Ierf*mp.sqrt(k))>mp.mpf('1e-6'))
details['quadratic']={'direct_error':mp.nstr(abs(Iraw-Ierf),20),'reference_error':mp.nstr(abs(Iraw-Ifixed),20),'omit_linear_error':mp.nstr(abs(Iraw-wronglin),20)}
# D=8 ball appropriate to the SU(3) scalar link count.
D=8; pb=mp.mpf(7)/4; alpha=mp.mpc(1,2)/300; ss=mp.mpf(3)/7
cscale=lambda ss:1+alpha*ss
radconst=1/(mp.mpf(2)**(D/2-1)*mp.gamma(D/2))
Iball=lambda ss:cscale(ss)**D*radconst*mp.quad(lambda rr:rr**(D-1)*mp.exp(-cscale(ss)**2*rr**2/2),[0,pb])
zref=radconst*mp.quad(lambda rr:rr**(D-1)*mp.exp(-rr**2/2),[0,pb])
qref=radconst*pb**(D-1)*mp.exp(-pb**2/2)
cval=cscale(ss)
Zred=Iball(ss)/(cval**D*zref)
surf_ratio=mp.exp(-(cval*cval-1)*pb*pb/2)/Zred
fluxball=qref/zref*(alpha/cval)*pb*surf_ratio
ball_derivative=mp.diff(Iball,ss)/Iball(ss)
check('D8_radial_volume_derivative_equals_normal_flux',abs(ball_derivative-fluxball)<mp.mpf('1e-65'))
control('omit_radial_p_to_D_minus_1_detected',abs(ball_derivative-fluxball/pb**(D-1))>mp.mpf('1e-5'))
control('omit_radial_velocity_p_detected',abs(ball_derivative-fluxball/pb)>mp.mpf('1e-5'))
wrongdim=lambda tt:Iball(tt)/cscale(tt)**(D-1)
control('use_link_count_instead_of_scalar_Jacobian_detected',abs(mp.diff(wrongdim,ss)/wrongdim(ss)-fluxball)>mp.mpf('1e-4'))
rr=s.symbols('rr',positive=True)
zz=1-s.exp(-rr**2/2)*(1+rr**2/2+rr**4/8+rr**6/48)
check('D8_ball_mass_derivative_symbolic',s.simplify(s.diff(zz,rr)-rr**7*s.exp(-rr**2/2)/48)==0)
details['D8_ball_error']=mp.nstr(abs(ball_derivative-fluxball),20)
# A different nonabelian plaquette. X=i sigma1, Y=i sigma2; fixed coordinate convention.
BB,dd=s.symbols('BB dd',real=True)
X=s.Matrix([[0,ii],[ii,0]]); Y=s.Matrix([[0,1],[-1,0]])
RX=lambda z:s.eye(2)*s.cos(z)+X*s.sin(z)
RY=lambda z:s.eye(2)*s.cos(z)+Y*s.sin(z)
P=RX(BB)*RY(2*BB)*RX(BB+dd)*RY(-BB)
source_matrix=2-s.trace(P)
# Quaternion scalar product identity for four alternating axes.
x1,y1,x2,y2=s.symbols('x1 y1 x2 y2',real=True)
qscalar=s.cos(x1)*s.cos(x2)*s.cos(y1+y2)-s.sin(x1)*s.sin(x2)*s.cos(y1-y2)
source_quaternion=(2-2*qscalar).subs({x1:BB,y1:2*BB,x2:BB+dd,y2:-BB})
check('SU2_noncommuting_matrix_quaternion_agree',s.trigsimp(s.expand_trig(source_matrix-source_quaternion))==0)
force=s.trigsimp(s.diff(source_quaternion,dd).subs(dd,0))
leading=s.limit(force/BB,BB,0)
check('SU2_nontrivial_background_linear_source',leading==4)
control('SU2_omit_background_force_detected',force.subs(BB,s.pi/12)!=0)
wrongplaquette=2-s.trace(RX(BB)*RX(BB+dd)*RY(-BB))
control('SU2_omit_noncommuting_link_detected',s.trigsimp((source_matrix-wrongplaquette).subs({BB:s.pi/12,dd:s.pi/10}))!=0)
details['SU2_force']=str(force)
# Hard history at a fixed physical-coordinate threshold; chart center moves with B.
# F=(a-B)^2/2, sigma=1, |W|<=1, Xi=1_(a>1).
overlap_length=s.Max(0,s.Min(1+BB,2)-s.Max(1,BB-1))
check('hard_history_negative_background_domain_empty',overlap_length.subs(BB,-R(1,10))==0)
history_positive=s.sqrt(s.pi/2)*(s.erf(1/s.sqrt(2))-s.erf((1-BB)/s.sqrt(2)))
check('hard_history_right_derivative_nonzero',s.simplify(s.diff(history_positive,BB).subs(BB,0)-s.exp(-R(1,2)))==0)
details['history_counterexample']={'B_nonpositive':'D_h(B)=0 for -1<B<=0','B_positive':'D_h(B)=integral_(1-B)^1 exp(-w^2/2)dw for 0<B<1','left_derivative':'0','right_derivative':'exp(-1/2)','scope':'Disproves unqualified complex-B continuation of arbitrary hard histories, not the empty-history theorem.'}
# Coefficient majorant identities and analytically conservative constants.
zz0,xx=s.symbols('zz0 xx',nonnegative=True)
fmaj=(1-zz0)**-3
T3=(1-zz0-xx)**-3-fmaj-xx*s.diff(fmaj,zz0)-xx**2*s.diff(fmaj,zz0,2)/2
for n in range(3,8):
    for m in range(0,8-n):
        actual=s.diff(T3,xx,n,zz0,m).subs({xx:0,zz0:0})/(s.factorial(n)*s.factorial(m))
        expected=s.binomial(n+m+2,2)*s.binomial(n+m,n)
        check(f'taylor_allocation_n{n}_m{m}',actual==expected)
control('background_incidence_derivative_nonzero',s.diff(T3,zz0).subs({zz0:R(1,8),xx:R(1,8)})>0)
control('fluctuation_incidence_derivative_nonzero',s.diff(T3,xx).subs({zz0:R(1,8),xx:R(1,8)})>0)
print(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-started,'checks':checks,'controls':controls,'details':details},indent=2))
