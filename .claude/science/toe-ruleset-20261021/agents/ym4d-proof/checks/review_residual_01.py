"""Independent exact checks; no author-code imports or permutation determinant routine.
Finite algebra is not a lattice identification or a limiting field theory.
"""
import sympy as s
import json, sys, platform
from datetime import datetime, timezone
r=s.Rational
out={'started_utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'sympy':s.__version__,'checks':{},'details':{}}
def check(name,v):
    if isinstance(v,s.MatrixBase): v=all(s.cancel(x)==0 for x in v)
    else: v=bool(v)
    out['checks'][name]=v
    return v
def det(a): return a.det(method='domain-ge')
def diag(*a): return s.diag(*a)
def comm(a,b): return a*b-b*a
def cross(a): return s.Matrix([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0]])
def hcat(*a): return s.Matrix.hstack(*a)
def vcat(*a): return s.Matrix.vstack(*a)
def bmat(rows): return vcat(*(hcat(*x) for x in rows))
def coeff(m,t,k):
    if isinstance(m,s.MatrixBase): return m.applyfunc(lambda x:s.diff(x,t,k).subs(t,0)/s.factorial(k))
    return s.diff(m,t,k).subs(t,0)/s.factorial(k)

# Actual non-Abelian SO(3) adjoint gauge mechanics, using bracket = vector cross.
# S=1/2 |A1 x A2|^2, without space derivatives. This checks gauge signs,
# finite Hessians and noncommuting colour matrices, not continuum/lattice poles.
x=s.symbols('x:6'); z=s.Matrix(x); a=[s.Matrix(x[:3]),s.Matrix(x[3:])]
f=a[0].cross(a[1]); action=(f.dot(f))/2
E=s.Matrix([s.diff(action,xi) for xi in x]); H=s.hessian(action,x)
DA=vcat(*(cross(ai) for ai in a)); TE=vcat(cross(E[:3,0]),cross(E[3:,0]))
check('nonabelian_Wilson_gauge_row_identity_symbolic',H*DA-TE)
check('nonabelian_EOM_divergence_identity_symbolic',DA.T*E)
values=dict(zip(x,[1,2,-1,2,-1,3])); av=[ai.subs(values) for ai in a]
DA=DA.subs(values); E=E.subs(values); H=H.subs(values); mu=s.Integer(101)
bv=[av[j]+E[3*j:3*j+3,0]/mu for j in range(2)]
DB=vcat(*(cross(bi) for bi in bv)); T=DB-DA
DeltaA=DA.T*DA; DeltaB=DB.T*DB; K=DA.T*DB
check('saddle_K_selfadjoint_nonabelian',K-K.T)
check('saddle_h_stationarity_nonabelian',DB.T*(vcat(*bv)-vcat(*av)))
check('noncommuting_colour_Grams_control',comm(DeltaA,DeltaB)!=s.zeros(3))
# Differentiate the exponential gauge action through second order directly.
eta=s.symbols('e:3'); ev=s.Matrix(eta); eps=s.symbols('eps')
Brot=[b+eps*ev.cross(b)+eps**2*ev.cross(ev.cross(b))/2 for b in bv]
q=sum((Brot[j]-av[j]).dot(Brot[j]-av[j]) for j in range(2))*mu/2
qhh=s.hessian(s.expand(q).coeff(eps,2),eta)
check('q_hh_from_exponential_nonabelian_action',qhh-mu*K)
# Mixed B-h derivative is computed before substituting saddle, to test the sign.
u=s.symbols('u:6'); uv=[s.Matrix(u[:3]),s.Matrix(u[3:])]
qlinear=-mu*sum((uv[j]-av[j]).dot(cross(uv[j])*ev) for j in range(2))
qBh=s.Matrix([[s.diff(qlinear,ui,ei) for ei in eta] for ui in u])
check('q_Bh_uses_DA_not_DB',qBh+mu*DA)
check('wrong_q_Bh_control',qBh+mu*DB!=s.zeros(6,3))
qAh=mu*DB
Faa=H+mu*s.eye(6)-mu*DB*K.inv()*DB.T
Fab=-mu*s.eye(6)+mu*DB*K.inv()*DA.T
Fbb=mu*s.eye(6)-mu*DA*K.inv()*DA.T
check('fine_row_completion',Faa*DA)
check('mixed_fine_transversality',DA.T*Fab)
check('mixed_coarse_transversality',Fab*DB)
check('off_shell_row_not_zero',H*DA!=s.zeros(6,3))
Sa=hcat(*(DA.T.nullspace())); Sb=hcat(*(DB.T.nullspace()))
PA=s.eye(6)-DA*DeltaA.inv()*DA.T; PB=s.eye(6)-DB*DeltaB.inv()*DB.T
# Compress to rational transverse frames retaining their nontrivial Grams.
U=bmat([[Sa.T*(H+mu*s.eye(6))*Sa,-mu*Sa.T*Sb,mu*Sa.T*DB],[-mu*Sb.T*Sa,mu*Sb.T*Sb,-mu*Sb.T*DA],[mu*DB.T*Sa,-mu*DA.T*Sb,mu*K]])
Afromfull=U[:3,:3]-U[:3,3:]*U[3:,3:].inv()*U[3:,:3]
Afromh=Sa.T*Faa*Sa-Sa.T*Fab*Sb*(Sb.T*Fbb*Sb).inv()*Sb.T*Fab.T*Sa
formula=PA*H*PA+mu*PA*T*DeltaB.inv()*T.T*PA-mu*PA*(s.eye(6)+PB)*T*(K-T.T*PB*T).inv()*T.T*(s.eye(6)+PB)*PA
check('transverse_completion_full_elimination',Afromfull-Sa.T*formula*Sa)
check('transverse_completion_opposite_elimination',Afromh-Afromfull)
check('wrong_Wilson_transverse_replacement_rejected',Afromfull-Sa.T*H*Sa!=s.zeros(3))
Oaug=bmat([[H+mu*s.eye(6)+DA*DA.T,-mu*s.eye(6),mu*DB],[-mu*s.eye(6),mu*s.eye(6)+DB*DB.T,-mu*DA],[mu*DB.T,-mu*DA.T,mu*K]])
Shear=bmat([[s.eye(6),s.zeros(6),DA],[s.zeros(6),s.eye(6),s.zeros(6,3)],[s.zeros(3,6),s.zeros(3,6),-s.eye(3)]])
Osh=Shear.T*Oaug*Shear
L=bmat([[H+mu*s.eye(6),-mu*s.eye(6)],[-mu*s.eye(6),mu*s.eye(6)+DB*DB.T]])
check('shear_modulus_one',det(Shear)**2==1)
check('shear_lambda_square_Gram',Osh[12:,12:]-DeltaA**2)
check('shear_mixed_a_row',Osh[:6,12:]-DA*DeltaA)
check('shear_mixed_b_row_zero',Osh[6:12,12:])
check('shear_reduced_local_block',Osh[:12,:12]-Osh[:12,12:]*Osh[12:,12:].inv()*Osh[12:,:12]-L)
J=bmat([[Faa+DA*DA.T,Fab],[Fab.T,Fbb+DB*DB.T]])
Oeff=H+mu*DB*(mu*s.eye(3)+DeltaB).inv()*DB.T
W=H+DA*DA.T
dj,dl,dw,do=map(det,[J,L,W,Oeff])
check('gauge_shear_determinant_exact',dj*det(mu*K)==det(DeltaA)**2*dl)
check('massive_elimination_exact',dl==det(mu*s.eye(6)+DB*DB.T)*do)
check('rectangular_massive_factor',det(mu*s.eye(6)+DB*DB.T)==mu**6*det(s.eye(3)+DeltaB/mu))
# exp(2 Phi) computed directly from joint Hessian and level/ghost measure.
phi_direct=dj/dw*mu**(-(6-3))/det(DeltaB)
phi_formula=do/dw*det(DeltaA)**2/(det(DeltaB)*det(K))*det(s.eye(3)+DeltaB/mu)
check('all_mu_gauge_ghost_factors',s.cancel(phi_direct-phi_formula)==0)
check('missing_DeltaA_factor_control',s.cancel(phi_direct-phi_formula/det(DeltaA))!=0)
check('missing_h_determinant_control',s.cancel(phi_direct-phi_formula*det(mu*K))!=0)
check('missing_level_group_control',s.cancel(phi_direct-phi_formula*mu**3)!=0)
check('nontrivial_Gram_required',det(hcat(Sa,DA).T*W*hcat(Sa,DA))!=dw)
check('full_Gram_restores_W',det(hcat(Sa,DA).T*W*hcat(Sa,DA))==dw*det(Sa.T*Sa)*det(DeltaA))
out['details']['nonabelian_dimensions']={'oneforms':6,'gauge':3,'augmented':15,'mu':str(mu),'DeltaA':str(DeltaA),'DeltaB':str(DeltaB)}

# A two-gauge, two-transverse noncommuting Taylor family: coefficient -3.
t=s.symbols('t'); D0=vcat(s.eye(2),s.zeros(2)); R=s.Matrix([[1,2],[2,-1]]); V=s.Matrix([[1,3],[-2,1]])
T1=vcat(R,V); Db=D0+t*T1; Hw=bmat([[mu*t*R,mu*t*V.T],[mu*t*V,s.Matrix([[7,2],[2,5]])]])
S0=vcat(s.zeros(2),s.eye(2)); Pa=S0*S0.T; DbD=Db.T*Db; kk=D0.T*Db
# Taylor compute inverse jets directly by differentiating the full projected Schur complement.
Pb=s.eye(4)-Db*DbD.inv()*Db.T
Ae=Pa*Hw*Pa+mu*Pa*(t*T1)*DbD.inv()*(t*T1).T*Pa-mu*Pa*(s.eye(4)+Pb)*(t*T1)*(kk-(t*T1).T*Pb*(t*T1)).inv()*(t*T1).T*(s.eye(4)+Pb)*Pa
check('minus_three_multidimensional_coefficient',coeff(S0.T*(Ae-Pa*Hw*Pa)*S0,t,2)+3*mu*V*V.T)
check('noncommuting_Taylor_control',comm(V*V.T,s.Matrix([[7,2],[2,5]]))!=s.zeros(2))

# Analytic congruence: rational eigenvalues make the square root exactly rational,
# while D*H D and the Gram do not commute.
mu2=s.Integer(3); D=vcat(s.diag(3,6),s.zeros(2)); Delta=D.T*D
sqrtprof=s.diag(2,s.sqrt(13)); ff=Delta.inv()*(sqrtprof-s.eye(2))
HH=s.Matrix([[2,1,3,-1],[1,4,2,3],[3,2,7,1],[-1,3,1,9]])
CC=s.eye(4)+D*ff*D.T; profile=mu2*D*(mu2*s.eye(2)+Delta).inv()*D.T; TE=HH*D
RE=D*ff*TE.T+TE*ff*D.T+D*ff*(D.T*TE)*ff*D.T
check('profile_congruence_exact',s.simplify(CC*profile*CC-D*D.T))
check('profile_jacobian_exact',s.simplify(det(CC)**2-det(s.eye(2)+Delta/mu2))==0)
check('three_EOM_terms_exact_noncommuting',s.simplify(CC*(HH+profile)*CC-(HH+D*D.T+RE)))
check('last_EOM_term_missing_control',s.simplify(CC*(HH+profile)*CC-(HH+D*D.T+D*ff*TE.T+TE*ff*D.T))!=s.zeros(4))
check('EOM_Gram_noncommuting_control',comm(Delta,D.T*TE)!=s.zeros(2))

# Grouped second coefficient, checked against a direct determinant polynomial.
A0=s.Matrix([[5,1],[1,4]]); C0=s.Matrix([[4,-1],[-1,6]])
A1=s.Matrix([[1,2],[2,-2]]); C1=s.Matrix([[3,1],[1,-1]]); B1=s.Matrix([[1,3],[-2,2]])
A2=s.Matrix([[2,-1],[-1,3]]); C2=s.Matrix([[1,2],[2,4]]); B2=s.Matrix([[2,1],[1,-1]])
Jred=bmat([[A0+t*A1+t*t*A2,t*B1+t*t*B2],[(t*B1+t*t*B2).T,C0+t*C1+t*t*C2]])
p=s.Poly(det(Jred),t); d0=p.nth(0);d1=p.nth(1);d2=p.nth(2)
true2=(d2/d0-d1*d1/(2*d0*d0))/2
GA=A0.inv();GC=C0.inv()
groups=[s.trace(GA*A2)/2,-s.trace(GA*A1*GA*A1)/4,s.trace(GC*C2)/2,-s.trace(GC*C1*GC*C1)/4,-s.trace(GA*B1*GC*B1.T)/2]
check('five_group_trace_coefficient_exact',s.cancel(true2-sum(groups))==0)
for j in range(5): check('omit_trace_group_'+str(j)+'_control',s.cancel(true2-sum(groups)+groups[j])!=0)
check('wrong_half_bubble_coefficient_control',s.cancel(true2-(groups[0]+groups[2]+(groups[1]+groups[3]+groups[4])/2))!=0)
out['details']['five_groups']=[str(x) for x in groups]

# Moving orthonormal frame: independently differentiate an ambient rotation.
Rot=s.Matrix([[(1-t*t)/(1+t*t),-2*t/(1+t*t)],[2*t/(1+t*t),(1-t*t)/(1+t*t)]])
S=Rot[:,0:1]; I=Rot[:,1:2]; M0=s.Matrix([[5,2],[2,7]]); MM=Rot*M0*Rot.T
check('moving_frame_transverse_coefficient_zero',coeff((S.T*MM*S)[0],t,2)==0)
check('frozen_frame_control_detects_false_coefficient',coeff(MM[0,0],t,2)!=0)
check('moving_frame_full_determinant_unchanged',s.cancel(det(Rot.T*MM*Rot)-det(M0))==0)

# Stationary h jets: solve a genuinely two-dimensional implicit series with two
# independent source coordinates, then compare the entire quartic polynomial.
y1,y2,h1,h2=s.symbols('y1 y2 h1 h2'); y=s.Matrix([y1,y2]); h=s.Matrix([h1,h2])
G=s.Matrix([[5,2],[2,4]]); B=s.Matrix([[1,-2],[3,1]]); A=s.Matrix([[7,1],[1,6]])
Q=(h.T*G*h)[0]/2+(h.T*B*y)[0]+(y.T*A*y)[0]/2
Q3=h1*y1*y2+2*h2*y1**2+h1*h2*y2+h1**3/3+h2**3/2+y1*y2**2
Q4=h1**2*y2**2+2*h1*h2*y1*y2+h2**2*y1**2+h1**4/4+h1*h2**3/3+y1**2*y2**2
Q+=Q3+Q4; hv1=-G.inv()*B*y
sub1={h1:t*hv1[0],h2:t*hv1[1],y1:t*y1,y2:t*y2}
c=s.Matrix([s.expand(s.diff(Q3,hi).subs(sub1,simultaneous=True)).coeff(t,2) for hi in h])
hv2=-G.inv()*c
sub2={h1:t*hv1[0]+t*t*hv2[0],h2:t*hv1[1]+t*t*hv2[1],y1:t*y1,y2:t*y2}
implicit=s.Matrix([s.expand(s.diff(Q,hi).subs(sub2,simultaneous=True)).coeff(t,3) for hi in h]); hv3=-G.inv()*implicit
sub3={h1:t*hv1[0]+t*t*hv2[0]+t**3*hv3[0],h2:t*hv1[1]+t*t*hv2[1]+t**3*hv3[1],y1:t*y1,y2:t*y2}
value=s.Poly(s.expand(Q.subs(sub3,simultaneous=True)),t)
raw3=s.expand(Q3.subs({h1:hv1[0],h2:hv1[1]},simultaneous=True))
raw4=s.expand(Q4.subs({h1:hv1[0],h2:hv1[1]},simultaneous=True))
expected4=raw4-(c.T*G.inv()*c)[0]/2
check('stationary_second_jet_polarized',s.expand(value.nth(2)-(y.T*(A-B.T*G.inv()*B)*y)[0]/2)==0)
check('stationary_third_jet_polarized',s.expand(value.nth(3)-raw3)==0)
check('stationary_fourth_jet_polarized',s.expand(value.nth(4)-expected4)==0)
check('omitted_exchange_control',s.expand(value.nth(4)-raw4)!=0)
check('wrong_exchange_sign_control',s.expand(value.nth(4)-(raw4+(c.T*G.inv()*c)[0]/2))!=0)
check('exchange_has_genuine_mixed_source_terms',s.Poly(s.expand((c.T*G.inv()*c)[0]),y1,y2).coeff_monomial(y1*y2**3)!=0)

out['finished_utc']=datetime.now(timezone.utc).isoformat();out['passed']=sum(out['checks'].values());out['total']=len(out['checks'])
print(json.dumps(out,indent=2,sort_keys=True));sys.exit(0 if all(out['checks'].values()) else 1)
