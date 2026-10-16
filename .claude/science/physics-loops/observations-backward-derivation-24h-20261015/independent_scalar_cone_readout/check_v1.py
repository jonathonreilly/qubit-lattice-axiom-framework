"""Independent pre-author scalar principal/readout controls."""
AUDIT_TIMEOUT_SEC=120
import sympy as s,json
checks=[]
def ck(n,b,detail=None):checks.append({'name':n,'pass':bool(b),'detail':detail})
eps,v,pt,px,py,pz,X,b,c=s.symbols('eps v pt px py pz X b c',real=True)
P=lambda q:q+b*q*q+c*q**3
XX=(v+eps*pt)**2/2-eps**2*(px*px+py*py+pz*pz)/2
quad=s.expand(P(XX)).coeff(eps,2);PX=s.diff(P(X),X).subs(X,v*v/2);PXX=s.diff(P(X),X,2).subs(X,v*v/2);K=PX+v*v*PXX
ck('quadratic_action_time_Hessian',s.simplify(s.diff(quad,pt,2)-K)==0)
ck('quadratic_action_spatial_Hessian',all(s.simplify(s.diff(quad,p,2)+PX)==0 for p in [px,py,pz]))
# Principal equation from divergence chain rule, independently using raised gradient.
g=s.diag(-1,1,1,1);grad=s.Matrix([-v,0,0,0]);eff=PX*g-PXX*grad*grad.T
om,k=s.symbols('omega k',nonzero=True,real=True);cov=s.Matrix([-om,0,0,k]);principal=(cov.T*eff*cov)[0]
ck('equation_action_principal_agreement',s.expand(principal+K*om**2-PX*k*k)==0)
ck('noncanonical_positive_example',K.subs({v:1,b:1,c:0})==4 and PX.subs({v:1,b:1,c:0})==2)
A=s.symbols('A',positive=True)
ck('physical_conformal_speed',s.simplify((om/A)**2/(k/A)**2-om**2/k**2)==0)
ck('timelike_does_not_ensure_no_ghost',K.subs({v:1,b:-1,c:0})<0)
# Build physical metric by conformal multiplication before extracting potentials.
U,slip=s.symbols('U slip');ein=s.diag(-(1+2*eps*U),1-2*eps*U,1-2*eps*U,1-2*eps*U)
phys=(1+2*eps*slip)*ein
psi=-s.expand(phys[0,0]).coeff(eps)/2;phi=-s.expand(phys[1,1]).coeff(eps)/2
ck('physical_lapse',psi==U+slip);ck('physical_spatial_potential',phi==U-slip)
ck('lensing_only_blind',s.expand(psi+phi)==2*U)
# Curvature direct tensor formula, retaining the plane's complex phase.
t,x,y,z=s.symbols('t x y z',real=True);coords=[t,x,y,z];plane=s.exp(s.I*(k*z-om*t));hh=s.diag(-2*psi*plane,-2*phi*plane,-2*phi*plane,-2*phi*plane)
R=s.Matrix(3,3,lambda i,j:s.simplify((s.diff(hh[0,j+1],coords[i+1],t)+s.diff(hh[i+1,0],t,coords[j+1])-s.diff(hh[0,0],coords[i+1],coords[j+1])-s.diff(hh[i+1,j+1],t,t))/2/plane))
T=R[0,0];L=R[2,2]
ck('transverse_curvature',s.expand(T+om**2*phi)==0)
ck('longitudinal_curvature',s.expand(L+k*k*psi+om*om*phi)==0)
ck('scalar_tensor_structure',R[0,0]==R[1,1] and all(R[i,j]==0 for i in range(3) for j in range(3) if i!=j))
mat=s.Matrix([T,L]).jacobian([U,slip]);ck('invertible_tidal_map',s.factor(mat.det())==2*k*k*om*om)
srec=(T/om**2-(L-T)/k**2)/2;urec=-(T/om**2+(L-T)/k**2)/2
ck('slip_exact_with_nonzero_U',s.simplify(srec-slip)==0);ck('U_exact_recovery',s.simplify(urec-U)==0)
ck('zero_frequency_rank_loss',mat.subs(om,0).rank()==1);ck('zero_k_rank_loss',mat.subs(k,0).rank()==1)
vals={U:s.Rational(7,3),slip:s.Rational(2,5),k:3,om:2}
ck('nonluminal_nonzero_U_witness',srec.subs(vals)==s.Rational(2,5))
# Wrong luminal projection leaves Einstein-potential contamination generally.
wrong=(T-L/2)/k**2
ck('tensor_speed_substitution_detected',s.simplify((wrong-slip).subs(vals))!=0,str(s.simplify((wrong-slip).subs(vals))))
ck('luminal_projection_conditional',s.simplify((T-L/2-k*k*slip).subs(om,k))==0)
alpha,dphi=s.symbols('alpha dphi');ck('zero_coupling_blind',(alpha*dphi).subs(alpha,0)==0)
cs2,m2=s.symbols('cs2 m2');disp=om**2-cs2*k*k-m2
ck('massless_luminal_phase',disp.subs({om:2,k:2,cs2:1,m2:0})==0)
ck('subluminal_massive_same_phase',disp.subs({om:2,k:2,cs2:s.Rational(1,2),m2:2})==0)
F=s.symbols('F',positive=True);ck('noncanonical_luminal_family',s.diff(F*X,X,2)==0 and s.diff(F*X,X)==F)
X0,lam=s.symbols('X0 lam');extra=lam*(X-X0)**3
ck('off_trajectory_two_jet_blind',all(s.diff(extra,X,j).subs(X,X0)==0 for j in range(3)) and s.diff(extra,X,3)==6*lam)
print(json.dumps({'scope':'Independent frozen-background principal and tidal algebra; no author sources or empirical records','checks':checks,'passed':sum(x['pass'] for x in checks),'failed':sum(not x['pass'] for x in checks),'tidal_matrix':str(mat),'principal_symbol':str(principal)},indent=2));raise SystemExit(any(not x['pass'] for x in checks))
