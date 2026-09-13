"""Exact Laurent/Bloch, finite CAR and physical-role checks for block02.
This is a finite check of an analytical infinite-volume proof, not a fit of
density-of-states exponents or an independently reviewed physics result.
"""
from pathlib import Path
from itertools import product,combinations
import hashlib,json,time
import sympy as s
HERE=Path(__file__).resolve().parent
I2=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Z=s.diag(1,-1)
sites=list(product((0,1),repeat=3));index={r:i for i,r in enumerate(sites)}
z=s.symbols('z_x z_y z_z',nonzero=True)
hx,hy,hz=s.symbols('h_x h_y h_z',positive=True)
def matrix_zero(M):return all(s.expand(x)==0 for x in M)
def K_symbol(kind,weights=(hx,hy,hz)):
 K=s.zeros(8)
 for r in sites:
  for axis,h in enumerate(weights):
   for direction in (-1,1):
    w=list(r);w[axis]+=direction;tail=r if direction==1 else tuple(w)
    if kind=='row' and axis==0 and tail[1]%2:continue
    if kind=='matching' and axis==1 and (tail[0]+tail[1])%2:continue
    cell=[x//2 for x in w];sub=tuple(x%2 for x in w)
    K[index[r],index[sub]]+=h*direction*(-1)**sum(r[:axis])*s.prod(t**n for t,n in zip(z,cell))
 return K
def CAR(n):
 out=[];D=1<<n
 for j in range(n):
  out.append(s.SparseMatrix(D,D,{(b^(1<<j),b):(-1)**((b&((1<<j)-1)).bit_count()) for b in range(D) if b&(1<<j)}))
 return out
def run():
 start=time.monotonic();checks=[]
 def check(name,ok,**data):
  assert bool(ok),name
  checks.append({'name':name,**data})
 def eq(name,a,b):
  d=a-b
  check(name,matrix_zero(d) if isinstance(d,s.MatrixBase) else s.simplify(d)==0)
 I=s.eye(8);G=[s.kronecker_product(X,I2,I2),s.kronecker_product(Z,X,I2),s.kronecker_product(Z,Z,X)]
 P=s.kronecker_product(I2,(I2+Z)/2,I2)
 Krow=K_symbol('row',(1,1,1));K=K_symbol('matching')
 t=s.symbols('t_x t_y t_z',nonzero=True)
 phase=s.diag(*[s.prod(v**p for v,p in zip(t,r)) for r in sites])
 Kg=phase.inv()*Krow.subs(dict(zip(z,[v*v for v in t])),simultaneous=True)*phase
 target=(t[0]-1/t[0])*G[0]*P+(t[1]-1/t[1])*G[1]+(t[2]-1/t[2])*G[2]
 eq('literal_row_deletion_gauge_symbol',Kg,target)
 aa,bb,cc=s.symbols('a b c',real=True);A=aa*G[0]*P+bb*G[1]+cc*G[2]
 eq('row_Gamma_z_anticommutation',G[2]*(A-cc*G[2])+(A-cc*G[2])*G[2],s.zeros(8))
 eq('row_nodal_line_kernel',A.subs({bb:0,cc:0})*(I-P),s.zeros(8))
 eq('row_nodal_line_kernel_dimension',s.trace(I-P),4)
 eq('row_missing_linear_y_on_kernel',(I-P)*G[1]*(I-P),s.zeros(8))
 eq('row_second_order_y_effect',-(I-P)*G[1]*G[0]*P*G[1]*(I-P),(I-P)*G[0])
 # This quartic follows independently from the literal 4D xy block.
 xy=s.Matrix([[aa,bb,0,0],[bb,0,0,0],[0,0,-aa,bb],[0,0,bb,0]])
 lam=s.symbols('lambda')
 eq('row_xy_characteristic_polynomial',xy.charpoly(lam).as_expr(),lam**4-(aa*aa+2*bb*bb)*lam**2+bb**4)
 rr=s.symbols('r',positive=True)
 vec=s.Matrix([-rr,bb])
 # Impose only the exact eigenvalue equation b²=r(r+a), rather than treating
 # the weight as an independent target constant.
 eq('row_low_even_sublattice_weight_from_eigenvector',
    (vec.dot(vec)*rr/(2*rr+aa)-rr**2).subs(bb**2,rr*(rr+aa)),0)
 eq('matching_skew_adjoint_Laurent',K.T.subs(dict(zip(z,[1/v for v in z])),simultaneous=True),-K)
 ix=[i for i,r in enumerate(sites) if r[2]==0]
 Kxy=K.subs(z[2],1).extract(ix,ix)
 ap=hx*(1-1/z[0]);bp=hx*(z[0]-1)
 targetxy=s.Matrix([[0,hy,ap,0],[-hy,0,0,ap],[bp,0,0,hy/z[1]],[0,bp,-hy*z[1],0]])
 eq('matching_actual_xy_matrix',Kxy,targetxy)
 Q=Kxy.extract([0,3],[1,2]);Qadj=Q.T.subs({z[0]:1/z[0],z[1]:1/z[1]},simultaneous=True)
 base_xy=hy**2-hx**2*(z[0]+1/z[0]-2)
 eq('matching_xy_determinant',s.det(Q),hx**2*(2-z[0]-1/z[0])-hy**2*z[1])
 for j in range(2):
  eq('QQstar_equal_diagonal_'+str(j),(Q*Qadj)[j,j],base_xy)
  eq('QstarQ_equal_diagonal_'+str(j),(Qadj*Q)[j,j],base_xy)
 base=base_xy-hz**2*(z[2]+1/z[2]-2)
 disc=hx**2*hy**2*(2-z[0]-1/z[0])*(2+z[1]+1/z[1])
 L=-K*K;shift=L-base*I
 eq('matching_full_squared_symbol_identity',shift*shift,disc*I)
 for j in range(8):eq('matching_squared_symbol_diagonal_'+str(j),L[j,j],base)
 grading=s.diag(*[(-1)**sum(r) for r in sites])
 eq('physical_bipartite_grading',grading*K*grading,-K)
 eq('z_anticommuting_square_split',K*K-K.subs(z[2],1)**2,hz**2*(z[2]+1/z[2]-2)*I)
 # Lower spectral projector has diagonal 1/2, and the odd sign contribution
 # to its positive half has diagonal zero. Both are Laurent identities.
 for j in range(8):eq('odd_cubic_diagonal_'+str(j),(K**3)[j,j],0)
 for sign in (1,-1):
  point={hx:s.sqrt(2),hy:2,hz:1,z[0]:sign*s.I,z[1]:1,z[2]:1}
  Kn=K.subs(point);P0=I+Kn*Kn/16
  eq('node_projector_'+str(sign),P0*P0,P0)
  eq('node_kernel_'+str(sign),Kn*P0,s.zeros(8))
  eq('node_nullity_'+str(sign),s.trace(P0),4)
  deriv=[P0*(-v*K.diff(v)).subs(point)*P0 for v in z]
  for a in range(3):
   eq('node_tangent_square_'+str((sign,a)),deriv[a]*deriv[a],P0)
   for b in range(a):eq('node_tangent_cross_'+str((sign,a,b)),deriv[a]*deriv[b]+deriv[b]*deriv[a],s.zeros(8))
  for j in range(8):eq('node_lower_local_projector_diagonal_'+str((sign,j)),P0[j,j],s.Rational(1,2))
 # Exact sublevel chart and the derived positive local coefficient.
 x,y,w=s.symbols('kx ky kz',real=True)
 U=2*hx*s.sin(x/2)-hy*s.cos(y/2);V=hy*s.sin(y/2);W=2*hz*s.sin(w/2)
 q=hy**2+4*hx**2*s.sin(x/2)**2-4*hx*hy*s.sin(x/2)*s.cos(y/2)+4*hz**2*s.sin(w/2)**2
 eq('positive_node_chart_exact_radial_identity',s.expand(U*U+V*V+W*W-q).trigsimp(),0)
 jac=s.Matrix([U,V,W]).jacobian([x,y,w]).det()
 eq('isotropic_node_chart_Jacobian',jac.subs({hx:s.sqrt(2),hy:2,hz:1,x:s.pi/2,y:0,w:0}),1)
 E,h=s.symbols('E h',positive=True)
 volume=4*s.pi*E**3/3
 eq('two_nodes_local_weight_and_Jacobian',2*s.Rational(1,2)*volume/((2*s.pi)**3*h**3),E**3/(6*s.pi**2*h**3))
 eq('local_measure_versus_band_count',8*s.Rational(1,2),4)
 check('chart_radical_bound_63',s.Rational(63,16)>s.Rational(49,16))
 check('chart_radical_bound_47',s.Rational(47,16)>s.Rational(9,4))
 check('chart_inverse_upper_bound',s.Rational(256,147)<2)
 check('chart_inverse_lower_bound',s.Rational(1,2)<1/s.sqrt(2))
 # Literal candidate and detour geometry, including negative coordinates.
 def candidate(v,w):
  d=tuple(b-a for a,b in zip(v,w))
  if sum(abs(a) for a in d)!=1:return False
  axis=next(j for j,a in enumerate(d) if a)
  tail=v if d[axis]==1 else w
  return axis==1 and (tail[0]+tail[1])%2==1
 def add(r,a):return tuple(x+y for x,y in zip(r,a))
 axes=[(1,0,0),(0,1,0),(0,0,1)]
 count=0
 for r in product(range(-2,3),repeat=3):
  adjacent=[add(r,tuple(sign*x for x in a)) for a in axes for sign in(-1,1)]
  assert sum(candidate(r,w) for w in adjacent)==1,r
  top=add(r,axes[1])
  if not candidate(r,top):continue
  detour=[r,add(r,axes[0]),add(top,axes[0]),top]
  assert all(not candidate(v,w) for v,w in zip(detour,detour[1:]))
  center=add(tuple(2*x for x in r),axes[1])
  transverse=[add(center,tuple(sign*x for x in axes[a])) for a in (0,2) for sign in(-1,1)]
  assert len(set(transverse))==4 and all(sum(x%2 for x in p)==2 for p in transverse)
  endpoints=[tuple(2*x for x in r),tuple(2*x for x in top)]
  assert all(sum(x%2 for x in p)==0 for p in endpoints)
  count+=1
 check('literal_matching_detours_and_four_program_neighbors',count>0,candidates=count,vertices=125)
 # Separate ordinary CAR identities: both Majorana species give iK hopping.
 ann=CAR(3);dim=8;Id=s.eye(dim)
 ge=[a+a.H for a in ann];go=[-s.I*(a-a.H) for a in ann]
 Kf=s.Matrix([[0,2,-3],[-2,0,0],[3,0,0]])
 Hmajor=sum((s.I*Kf[v,w]*(ge[v]*ge[w]+go[v]*go[w])/2 for v,w in combinations(range(3),2)),s.zeros(dim))
 Hcomplex=sum((s.I*Kf[v,w]*(ann[v].H*ann[w]-ann[w].H*ann[v]) for v,w in combinations(range(3),2)),s.zeros(dim))
 eq('doubled_Majorana_equals_complex_hopping',Hmajor,Hcomplex)
 B=[Id-2*a.H*a for a in ann]
 Hnative=s.zeros(dim)
 for v,w in combinations(range(3),2):
  A=-s.I*ge[v]*ge[w]
  Hnative+=-Kf[v,w]*A*(Id-B[v]*B[w])/2
 eq('native_protected_current_normalization',Hnative,Hcomplex)
 for j in range(3):eq('both_Majorana_species_move_'+str(j),Hmajor*go[j]-go[j]*Hmajor,s.I*sum((Kf[k,j]*go[k] for k in range(3)),s.zeros(dim)))
 # Mixed-parity coherent density and its even extension, ancilla highest bit.
 v=s.zeros(8,1);v[0]=s.Rational(3,5);v[3]=s.Rational(4,5)
 wv=s.zeros(8,1);wv[1]=1/s.sqrt(2);wv[2]=s.I/s.sqrt(2)
 rho=s.Rational(2,5)*v*v.H+s.Rational(3,5)*wv*wv.H
 par=s.diag(*[(-1)**b.bit_count() for b in range(8)])
 rp=(Id+par)*rho/2;rm=(Id-par)*rho/2
 ext=s.diag(1,0);ext=s.kronecker_product(ext,rp)+s.kronecker_product(s.diag(0,1),rm)
 totalpar=s.kronecker_product(Z,par)
 eq('finite_extension_normalization',s.trace(ext),1)
 eq('finite_extension_even_total_parity',totalpar*ext,ext)
 eq('finite_extension_exact_bulk_marginal',ext[:8,:8]+ext[8:,8:],rho)
 check('finite_extension_both_parities_nonzero',s.trace(rp)>0 and s.trace(rm)>0)
 # Reconstruct from positive rank-one terms, not an untested PSD predicate.
 eq('finite_extension_positive_decomposition',ext,
    s.Rational(2,5)*s.kronecker_product(s.diag(1,0),v*v.H)+s.Rational(3,5)*s.kronecker_product(s.diag(0,1),wv*wv.H))
 for name,O in [('hopping',Hcomplex),('local_number',ann[1].H*ann[1]),('parity',par)]:
  eq('finite_extension_even_observable_'+name,s.trace(ext*s.kronecker_product(s.eye(2),O)),s.trace(rho*O))
 return {'status':'pass','checks':checks,'total_pass':len(checks),'total_fail':0,'seconds':time.monotonic()-start,
 'scope':'exact finite symbol, tangent, geometry and CAR checks; infinite sublevel asymptotics are proved in BLOCK02_DERIVATION.md; no exponent fit',
 'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
if __name__=='__main__':
 out=run();(HERE/'BLOCK02_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
