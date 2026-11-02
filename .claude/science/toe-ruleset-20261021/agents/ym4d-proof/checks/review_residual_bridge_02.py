"""Independent exact checks: mixed-boundary Kronecker cell and dense gauge-compatible algebra.
No author script, helper, or saved author result is imported.
"""
import sympy as s
from itertools import product
from datetime import datetime,timezone
import json,sys,platform
checks={};details={};started=datetime.now(timezone.utc).isoformat()
def ck(n,v):checks[n]=bool(v)
def zero(A):return all(s.cancel(z)==0 for z in A)
def det(A):return A.det(method='domain-ge')
def bd(*args):return s.diag(*args)
# Mixed Bloch point (pi,pi,0,0), not the author's all-antiperiodic point.
anti=s.Matrix([[2,-1,1],[-1,2,-1],[1,-1,2]])
period=s.Matrix([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
Delta=s.zeros(81)
for mu in range(4):
 ops=[s.eye(3)]*4;ops[mu]=anti if mu<2 else period
 Delta+=s.kronecker_product(*ops)
root=40;keep=[j for j in range(81) if j!=root];I=s.eye(81)[:,keep];J=s.eye(81)[:,root:root+1]
Di=I.T*Delta*I;ellint=Di.inv(method='DM')*(-I.T*Delta*J);lift=J+I*ellint
S=(J.T*Delta*lift)[0];green=Delta.inv(method='DM')[root,root]
alias=[a+b+c+d for a,b,c,d in product([1,4,1],[1,4,1],[0,3,3],[0,3,3])]
alias_green=sum(s.Rational(1,x) for x in alias)/81
ck('all_81_aliases',len(alias)==81 and min(alias)==2)
ck('exact_mixed_twist_root_green',green==alias_green)
ck('harmonic_lift_boundary',zero(J.T*lift-s.ones(1)))
ck('harmonic_lift_Dirichlet',zero(I.T*Delta*lift))
ck('harmonic_source_JS',zero(Delta*lift-J*S))
ck('harmonic_energy_S',(lift.T*Delta*lift)[0]==S)
ck('harmonic_Gram_S_squared',(lift.T*Delta**2*lift)[0]==S**2)
ck('harmonic_projector',zero(s.eye(81)-Delta*lift*(lift.T*Delta**2*lift).inv()*lift.T*Delta-(s.eye(81)-J*J.T)))
ck('root_inverse_S',green*S==1)
delta_det=det(Delta);interior_det=det(Di)
ck('exact_root_cofactor',delta_det==interior_det*S)
ck('all_alias_determinant',delta_det==s.prod(alias))
ck('omit_nonprincipal_aliases_control',green!=s.Rational(1,81*alias[0]))
ck('unit_root_Delta_8',(J.T*Delta*J)[0]==8)
ck('unit_root_Delta_squared_72',(J.T*Delta**2*J)[0]==72)
details['mixed_twist']={'green':str(green),'S':str(S),'alias_min':min(alias),'detDelta':str(delta_det),'detInterior':str(interior_det)}
# A generic noncommuting, multidimensional geometry and Hessian.
t=s.symbols('t',real=True)
Dbase=s.Matrix([[1,0,0,0],[0,2,0,0],[0,0,1,0],[0,0,0,2],[1,1,1,0],[0,1,1,1]])
Dvary=Dbase.copy();Dvary[5,0]=t
I=s.eye(4)[:,:2];J=s.eye(4)[:,2:];ev=J.T
Dc=s.Matrix([[1,1],[0,2],[1,0],[2,1]])
Cov=s.Matrix([[3,1,0,0],[1,4,1,0],[0,1,5,1],[0,0,1,6]])
Metric=s.diag(*range(3,15))
for j in range(11):Metric[j,j+1]=Metric[j+1,j]=1
mix=s.Matrix([[1,2,0,1,-1,0],[0,1,3,0,1,2],[2,0,1,2,0,-1],[1,-1,0,1,2,1]])
for it,value in enumerate([s.Rational(0),s.Rational(1,7)]):
 D=Dvary.subs(t,value);De=D.T*D;Di=I.T*De*I;L=J-I*Di.inv()*I.T*De*J;S=s.simplify(J.T*De*L)
 R=De.inv()*D.T;P=s.eye(6)-D*R
 Z=s.zeros(12);Z[:6,:6]=P;Z[6:10,6:10]=s.eye(4);Z[10:,:6]=ev*R;Z[10:,10:]=s.eye(2)
 H=Z.T*Metric*Z;N=D.col_join(s.zeros(4,4)).col_join(-ev)
 ck(f'actual_null_premise_control_{it}',zero(H*N))
 ck(f'genuine_noncommuting_scalar_blocks_{it}',not zero(De*bd(Di,s.eye(2))-bd(Di,s.eye(2))*De))
 HH=H[10:,10:];Hloc=H[:10,:10];Aug=H+bd(D*D.T,Dc*Dc.T,s.zeros(2))
 Jmin=Aug[:10,:10]-Aug[:10,10:]*HH.inv()*Aug[10:,:10]
 G=J.T*De**2*J;QP=s.eye(4)-De*J*G.inv()*J.T*De
 LP=Hloc+bd(D*QP*D.T,Dc*Dc.T);LH=Hloc+bd(D*I*I.T*D.T,Dc*Dc.T)
 ck(f'point_shear_determinant_{it}',det(Jmin)*det(HH)==det(G)*det(LP))
 ck(f'harmonic_shear_determinant_{it}',det(Jmin)*det(HH)==det(S)**2*det(LH))
 ck(f'multidimensional_harmonic_Gram_{it}',zero(L.T*De**2*L-S**2))
 ck(f'harmonic_scalar_change_unit_determinant_{it}',abs(det(I.row_join(L)))==1)
 W=s.eye(6)+D*D.T;Delta_c=Dc.T*Dc;Gc=Dc.T*Cov.inv()*Dc
 direct=det(Jmin)*det(Cov)*det(Gc)/(det(Delta_c)**2*det(W))
 harmonic=det(LH)/det(W)*(det(De)/det(Di))**2/det(HH)*det(Cov)*det(Gc)/det(Delta_c)**2
 ck(f'all_normalized_phi_factors_{it}',direct==harmonic)
 ck(f'omit_Dirichlet_determinant_control_{it}',direct!=harmonic*det(Di)**2)
 ck(f'replace_S_squared_by_S_control_{it}',det(Jmin)*det(HH)!=det(S)*det(LH))
 Hbad=H.copy();Hbad[0,0]+=1;Abad=Hbad+bd(D*D.T,Dc*Dc.T,s.zeros(2))
 Jbad=Abad[:10,:10]-Abad[:10,10:]*HH.inv()*Abad[10:,:10]
 Lbad=Hbad[:10,:10]+bd(D*I*I.T*D.T,Dc*Dc.T)
 ck(f'remove_null_premise_control_{it}',not zero(Hbad*N) and det(Jbad)*det(HH)!=det(S)**2*det(Lbad))
 # Independently construct a free Hodge-compatible action with nontrivial M,C.
 T=s.Matrix.hstack(*D.T.nullspace());Ht=3*P+P*s.diag(1,2,3,4,5,6)*P
 M=Dc*ev*R+mix*P;Rc=(s.eye(2)+Dc.T*Cov*Dc).inv()
 ck(f'free_covariance_{it}',zero(M*D-Dc*ev))
 Oh=Ht+D*I*I.T*D.T+M.T*Dc*Rc*Dc.T*M
 HTdet=det(T.T*Ht*T)/det(T.T*T)
 predicted=HTdet*det(Di)**2*det(Delta_c)**2*det(Rc)/det(De)
 ck(f'free_Hodge_determinant_{it}',det(Oh)==predicted)
 coords=T.row_join(D*I).row_join(D*L)
 ck(f'one_form_Hodge_Gram_{it}',det(coords.T*coords)==det(T.T*T)*det(De))
 ck(f'omit_one_form_Gram_control_{it}',det(Oh)!=predicted*det(De))
 block=(Ht+M.T*Cov.inv()*M).row_join(-M.T*Cov.inv()).col_join((-Cov.inv()*M).row_join(Cov.inv()))
 LHfree=block+bd(D*I*I.T*D.T,Dc*Dc.T)
 A6=HTdet*det(Di)**2*det(Delta_c)**2/(det(De)*det(Cov))
 ck(f'free_A6_massive_block_cancellation_{it}',det(LHfree)==A6)
 Wfree=Ht+D*D.T
 phifree=det(LHfree)/det(Wfree)*(det(De)/det(Di))**2/det(Gc)*det(Cov)*det(Gc)/det(Delta_c)**2
 ck(f'complete_free_Phi_zero_{it}',phifree==1)
 details[f'generic_geometry_{it}']={'t':str(value),'det_Dirichlet':str(det(Di)),'det_S':str(det(S)),'nontrivial_lift':str(L)}
# Moving interior/Gram jets are independently visible before a determinant simplification.
De=Dvary.T*Dvary;Di=I.T*De*I;f=s.factor(det(Di));L=J-I*Di.inv()*I.T*De*J
logjet=s.simplify((s.diff(f,t,2)/f-(s.diff(f,t)/f)**2).subs(t,0))
ck('moving_harmonic_frame_derivative',not zero(L.diff(t).subs(t,0)))
ck('omitted_moving_Dirichlet_twojet_control',logjet!=0)
details['moving_Dirichlet']={'det':str(f),'log_second_jet_at_0':str(logjet),'lift_first_jet_at_0':str(L.diff(t).subs(t,0))}
result={'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'sympy':s.__version__,'scope':'exact finite algebra and scalar geometry; generic dense controls do not identify off-shell actual action vertices','checks':checks,'passed':sum(checks.values()),'total':len(checks),'details':details}
print(json.dumps(result,indent=2,sort_keys=True));sys.exit(0 if all(checks.values()) else 1)
