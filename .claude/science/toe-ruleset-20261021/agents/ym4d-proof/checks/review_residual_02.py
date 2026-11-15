"""Supplementary noncommuting block and polarized Schur-jet checks.
No imports of author or first reviewer runner; original failed fixture retained.
"""
import sympy as s
import json,sys,platform
from datetime import datetime,timezone
out={'started_utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'sympy':s.__version__,'checks':{},'details':{}}
def check(n,v):
 if isinstance(v,s.MatrixBase): v=all(s.cancel(x)==0 for x in v)
 out['checks'][n]=bool(v)
def det(a):return a.det(method='domain-ge')
def bmat(rows):return s.Matrix.vstack(*(s.Matrix.hstack(*r) for r in rows))
def basis(d):return s.Matrix.hstack(*(d.T.nullspace()))
mu=s.Integer(11);D=s.Matrix([[1,0],[0,2],[1,1],[0,1],[2,-1]])
H=s.Matrix([[4,1,0,0,1],[1,5,1,0,0],[0,1,6,1,0],[0,0,1,7,2],[1,0,0,2,8]])
B=D+H*D/mu;T=B-D;DA=D.T*D;DB=B.T*B;K=D.T*B
check('Gram_commutator_nonzero',DA*DB-DB*DA!=s.zeros(2))
check('K_and_DeltaA_noncommute',K*DA-DA*K!=s.zeros(2))
check('K_selfadjoint',K-K.T);check('exact_fine_row',H*D-mu*T)
check('all_scalar_blocks_invertible',all(det(a)!=0 for a in [DA,DB,K]))
I=s.eye(5);Faa=H+mu*I-mu*B*K.inv()*B.T;Fab=-mu*I+mu*B*K.inv()*D.T;Fbb=mu*I-mu*D*K.inv()*D.T
Z=Faa+D*D.T;X=Fbb+B*B.T;J=bmat([[Z,Fab],[Fab.T,X]]);W=H+D*D.T
L=bmat([[H+mu*I,-mu*I],[-mu*I,mu*I+B*B.T]])
O=H+mu*B*(mu*s.eye(2)+DB).inv()*B.T
check('joint_and_W_invertible',det(J)!=0 and det(W)!=0)
check('noncommuting_shear_determinant',det(J)*det(mu*K)==det(DA)**2*det(L))
check('noncommuting_massive_elimination',det(L)==det(mu*I+B*B.T)*det(O))
Sa=basis(D);Sb=basis(B);ga=Sa.T*Sa;gb=Sb.T*Sb
zt=Sa.T*Z*Sa;yt=Sa.T*Fab*Sb;xt=Sb.T*X*Sb;b=Sb.T*X*B;c=B.T*X*B
At=zt-yt*xt.inv()*yt.T;Bt=-yt*xt.inv()*b;Ct=c-b.T*xt.inv()*b
Jr=bmat([[At,Bt],[Bt.T,Ct]])
# Correct all rational, nonorthonormal frame Grams; no square root is needed.
xdet=det(xt)/det(gb);jrdet=det(Jr)/(det(ga)*det(DB))
check('full_Hodge_Schur_factorization',det(J)==det(DA)*xdet*jrdet)
phi=det(J)*mu**(-3)/(det(DB)*det(W))
six=xdet*mu**(-3)*det(DA)/det(DB)*jrdet/det(W)
check('six_determinant_residual_exact',s.cancel(phi-six)==0)
model=det(O)/det(W)*det(DA)**2/(det(DB)*det(K))*det(s.eye(2)+DB/mu)
check('all_model_factors_noncommuting',s.cancel(phi-model)==0)
check('missing_transverse_Gram_control',s.cancel(phi-six*det(gb))!=0)
check('missing_gauge_Gram_control',s.cancel(phi-six*det(DB))!=0)
check('missing_h_factor_control',s.cancel(phi-model*det(mu*K))!=0)
PA=I-D*DA.inv()*D.T;PB=I-B*DB.inv()*B.T
Ae=PA*H*PA+mu*PA*T*DB.inv()*T.T*PA-mu*PA*(I+PB)*T*(K-T.T*PB*T).inv()*T.T*(I+PB)*PA
check('transverse_schur_noncommuting',At-Sa.T*Ae*Sa)
check('wrong_transverse_completion_control',At-Sa.T*H*Sa!=s.zeros(3))
out['details']['noncommuting_Delta_commutator']=str(DA*DB-DB*DA)
out['details']['Grams']={'fine_transverse':str(det(ga)),'coarse_transverse':str(det(gb)),'fine_gauge':str(det(DA)),'coarse_gauge':str(det(DB))}

x,y=s.symbols('x y');zero={x:0,y:0}
X0=s.Matrix([[5,1],[1,4]]);Xi=s.Matrix([[1,2],[2,3]]);Xj=s.Matrix([[2,-1],[-1,1]]);Xij=s.Matrix([[1,1],[1,-2]])
Y0=s.Matrix([[1,2],[-2,3]]);Yi=s.Matrix([[2,1],[0,-1]]);Yj=s.Matrix([[-1,3],[2,1]]);Yij=s.Matrix([[1,2],[3,4]])
Z0=s.Matrix([[7,2],[2,9]]);Zi=s.Matrix([[1,2],[2,1]]);Zj=s.Matrix([[3,1],[1,-1]]);Zij=s.Matrix([[2,-1],[-1,3]])
bi=s.Matrix([[1,2],[-1,3]]);bj=s.Matrix([[3,-1],[2,1]]);bij=s.Matrix([[2,1],[3,-2]])
c0=s.Matrix([[4,1],[1,3]]);ci=s.Matrix([[1,-1],[-1,2]]);cj=s.Matrix([[2,3],[3,-1]]);cij=s.Matrix([[3,1],[1,2]])
xx=X0+x*Xi+y*Xj+x*y*Xij;yy=Y0+x*Yi+y*Yj+x*y*Yij;zz=Z0+x*Zi+y*Zj+x*y*Zij;bb=x*bi+y*bj+x*y*bij;cc=c0+x*ci+y*cj+x*y*cij
rr=xx.inv();aa=zz-yy*rr*yy.T;BB=-yy*rr*bb;CC=cc-bb.T*rr*bb
R=X0.inv();Ri=-R*Xi*R;Rj=-R*Xj*R;Rij=R*Xi*R*Xj*R+R*Xj*R*Xi*R-R*Xij*R
D1=lambda f:s.diff(f,x).subs(zero);D2=lambda f:s.diff(f,x,y).subs(zero)
check('Schur_fixture_noncommuting',Xi*R-R*Xi!=s.zeros(2))
check('inverse_first_jet',D1(rr)-Ri);check('inverse_mixed_jet',D2(rr)-Rij)
Ai=Zi-Yi*R*Y0.T-Y0*Ri*Y0.T-Y0*R*Yi.T
Aij=Zij-Yij*R*Y0.T-Y0*R*Yij.T-Yi*R*Yj.T-Yj*R*Yi.T-Yi*Rj*Y0.T-Yj*Ri*Y0.T-Y0*Ri*Yj.T-Y0*Rj*Yi.T-Y0*Rij*Y0.T
Bii=-Y0*R*bi;Bij=-Yi*R*bj-Yj*R*bi-Y0*Ri*bj-Y0*Rj*bi-Y0*R*bij
Cij=cij-bi.T*R*bj-bj.T*R*bi
check('A_first_jet',D1(aa)-Ai);check('A_mixed_jet',D2(aa)-Aij)
check('B_first_jet_at_b0',D1(BB)-Bii);check('B_mixed_jet_at_b0',D2(BB)-Bij)
check('C_first_jet_at_b0',D1(CC)-ci);check('C_mixed_jet_at_b0',D2(CC)-Cij)
check('omitted_A_cross_derivative_control',D2(aa)-(Aij+Yi*R*Yj.T)!=s.zeros(2))
check('omitted_C_pairing_control',D2(CC)-(Cij+bi.T*R*bj)!=s.zeros(2))
out['finished_utc']=datetime.now(timezone.utc).isoformat();out['passed']=sum(out['checks'].values());out['total']=len(out['checks']);print(json.dumps(out,indent=2,sort_keys=True));sys.exit(0 if all(out['checks'].values()) else 1)
