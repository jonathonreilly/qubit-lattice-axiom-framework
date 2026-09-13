"""Exact exterior-algebra challenges of a supplied local fermion interaction."""
from pathlib import Path
from itertools import combinations,product
import hashlib,json,time
import sympy as s
import numpy as np
HERE=Path(__file__).resolve().parent
SIG=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
rows=[]
def check(name,ok,**detail):
 assert bool(ok),(name,detail)
 rows.append(dict(name=name,**detail))
def tidy(p):return {m:s.expand(c) for m,c in p.items() if s.expand(c)!=0}
def add(*ps):
 r={}
 for p in ps:
  for m,c in p.items():r[m]=r.get(m,0)+c
 return tidy(r)
def scale(c,p):return tidy({m:c*a for m,a in p.items()})
def mul(a,b):
 r={}
 for m,c in a.items():
  for n,d in b.items():
   if set(m)&set(n):continue
   parity=sum(i>j for i in m for j in n)%2;k=tuple(sorted(m+n));r[k]=r.get(k,0)+(-1)**parity*c*d
 return tidy(r)
def prod(*ps):
 r={():s.S(1)}
 for p in ps:r=mul(r,p)
 return r
def eq(name,a,b):check(name,not add(a,scale(-1,b)))
def gen(i):return {(i,):s.S(1)}
def left(p,i):
 r={}
 for m,c in p.items():
  if i in m:
   k=m.index(i);r[m[:k]+m[k+1:]]=r.get(m[:k]+m[k+1:],0)+(-1)**k*c
 return tidy(r)
def right(p,i):
 r={}
 for m,c in p.items():
  if i in m:
   k=m.index(i);r[m[:k]+m[k+1:]]=r.get(m[:k]+m[k+1:],0)+(-1)**(len(m)-1-k)*c
 return tidy(r)
def pb(a,b):return scale(-s.I,add(*(add(mul(right(a,i+4),left(b,i)),mul(right(a,i),left(b,i+4))) for i in range(4))))
def dag(p):
 r={}
 for m,c in p.items():r=add(r,scale(s.conjugate(c),prod(*(gen((i+4)%8) for i in reversed(m)))))
 return tidy(r)
q=[gen(i+4) for i in range(4)];bar=[gen(i) for i in range(4)]
def bil(A):return add(*(scale(A[i,j],mul(bar[i],q[j])) for i,j in product(range(4),repeat=2)))
def action(p,G):
 # Even linear transformation of all eight odd generators.
 r={}
 for m,c in p.items():
  for k,i in enumerate(m):
   for j in range(8):
    if G[i,j]!=0:r=add(r,scale(c*G[i,j],prod(*(gen(x) for x in m[:k]),gen(j),*(gen(x) for x in m[k+1:]))))
 return r
def transform_matrix(A,barA):return s.diag(barA.T,A)
def kernel(generators,basis):
 mats=[]
 for G in generators:
  cols=[action({m:s.S(1)},G) for m in basis]
  mats.append(s.Matrix([[c.get(m,0) for c in cols] for m in basis]))
 mat=s.Matrix.vstack(*mats)
 return mat,mat.nullspace()
def vector(p,basis):return s.Matrix([p.get(m,0) for m in basis])
def car(n):
 ops=[]
 for j in range(n):
  a=np.zeros((2**n,2**n),complex)
  for k in range(2**n):
   if k>>j&1:a[k^(1<<j),k]=(-1)**((k&((1<<j)-1)).bit_count())
  ops.append(a)
 return ops
def operator(p,ann):
 ops=[a.conj().T for a in ann]+ann;r=np.zeros_like(ann[0])
 for m,c in p.items():
  v=np.eye(len(r),dtype=complex)
  for i in m:v=v@ops[i]
  r+=complex(c)*v
 return r

def run():
 start=time.monotonic()
 # Independent finite CAR operators challenge the graded bilinear bracket.
 rng=np.random.default_rng(2026091309);ann=car(4)
 for trial in range(5):
  A=s.Matrix(rng.integers(-2,3,size=(4,4)));B=s.Matrix(rng.integers(-2,3,size=(4,4)))
  f,h=bil(A),bil(B);br=pb(f,h);eq('graded_bilinear_'+str(trial),br,scale(-s.I,bil(A*B-B*A)))
  ma,mh=operator(f,ann),operator(h,ann)
  check('CAR_bilinear_'+str(trial),np.max(np.abs(operator(br,ann)+1j*(ma@mh-mh@ma)))<1e-12)
 nR=add(*(mul(bar[i],q[i]) for i in range(2)));nL=add(*(mul(bar[i],q[i]) for i in range(2,4)))
 jR=[add(*(scale(sig[i,j],mul(bar[i],q[j])) for i,j in product(range(2),repeat=2))) for sig in SIG]
 jL=[add(*(scale(sig[i,j],mul(bar[i+2],q[j+2])) for i,j in product(range(2),repeat=2))) for sig in SIG]
 r=mul(q[0],q[1]);l=mul(q[2],q[3]);cross=add(mul(nR,nL),*(mul(a,b) for a,b in zip(jR,jL)))
 for i in range(3):eq('single_Weyl_density_current_'+str(i),mul(nR,jR[i]),{})
 eq('single_Weyl_density_pair',mul(nR,nR),scale(2,mul(dag(r),r)))
 eq('single_Weyl_current_norm',add(*(mul(j,j) for j in jR)),scale(-3,mul(nR,nR)))
 S=add(mul(bar[0],q[2]),mul(bar[1],q[3]))
 eq('cross_scalar_Fierz',cross,scale(-2,mul(S,dag(S))))
 boosts=[];rots=[]
 for sig in SIG:
  boost=s.diag(sig/2,-sig/2);rot=s.diag(-s.I*sig/2,-s.I*sig/2)
  boosts.append(transform_matrix(boost,boost));rots.append(transform_matrix(rot,-rot))
 invariants=[mul(dag(r),r),mul(dag(l),l),mul(dag(r),l),mul(dag(l),r),cross]
 for idx,p in enumerate(invariants):
  for i,G in enumerate(boosts+rots):eq('invariant_generator_'+str((idx,i)),action(p,G),{})
 basis=[tuple(b+a) for b in combinations(range(4),2) for a in combinations(range(4,8),2)]
 mat,null=kernel(boosts+rots,basis);check('full_invariant_dimension',len(null)==5,dimension=len(null),domain_dimension=len(basis),constraint_rank=mat.rank())
 expected=s.Matrix.hstack(*(vector(p,basis) for p in invariants));check('explicit_invariant_span',expected.rank()==5 and mat*expected==s.zeros(mat.rows,5))
 rmat,rnull=kernel(rots,basis);check('rotation_only_dimension',len(rnull)==10,dimension=len(rnull))
 herm=[invariants[0],invariants[1],add(invariants[2],invariants[3]),scale(s.I,add(invariants[2],scale(-1,invariants[3]))),cross]
 for i,p in enumerate(herm):eq('Hermitian_invariant_'+str(i),p,dag(p))
 valley=s.diag(1,1,-1,-1);vg=transform_matrix(valley,-valley)
 vm,vnull=kernel(boosts+rots+[vg],basis);check('valley_preserving_dimension',len(vnull)==3,dimension=len(vnull))
 # Exact nonresonant phase expansion of the native on-site orbital interaction.
 z=s.symbols('z',nonzero=True)
 cc=[add(scale(z,q[0]),scale(1/z,q[2])),add(scale(z,q[1]),scale(-1/z,q[3]))]
 cb=[add(scale(1/z,bar[0]),scale(z,bar[2])),add(scale(1/z,bar[1]),scale(-z,bar[3]))]
 native=prod(cb[0],cb[1],cc[1],cc[0]);zero={m:s.expand(c).coeff(z,0) for m,c in native.items()};zero=tidy(zero)
 mixed=add(mul(q[1],q[2]),mul(q[0],q[3]));predicted=add(invariants[0],invariants[1],mul(dag(mixed),mixed))
 eq('native_phase_zero',zero,predicted)
 variations={}
 for name,gens in [('rotation',rots),('boost',boosts)]:
  for i,G in enumerate(gens):
   out=action(zero,G);variations[name+str(i)]={str(k):str(v) for k,v in out.items()}
   check('native_'+name+'_variation_'+str(i),bool(out)==(i<2 if name=='rotation' else i==2),nonzero_monomials=len(out))
 # General orbital-density kernels at zero and intervalley transfer.
 a0,b0,c0,aq,bq,cq=s.symbols('a0 b0 c0 aq bq cq',real=True)
 forward=s.Matrix([[a0,b0],[b0,c0]]);exchange=s.Matrix([[aq,bq],[bq,cq]])
 dens=[add(mul(bar[i],q[i]),mul(bar[i+2],q[i+2])) for i in range(2)]
 inter=[scale(1 if i==0 else -1,mul(bar[i],q[i+2])) for i in range(2)]
 density=add(*(scale(forward[i,j]/2,mul(dens[i],dens[j])) for i,j in product(range(2),repeat=2)),*(scale(exchange[i,j],mul(inter[i],dag(inter[j]))) for i,j in product(range(2),repeat=2)))
 equations=[]
 for G in boosts+rots:equations.extend(action(density,G).values())
 sol=s.linsolve(equations,[a0,b0,c0,aq,bq,cq])
 check('density_kernel_classification',sol==s.FiniteSet((aq+bq,0,bq+cq,aq,bq,cq)))
 imposed={a0:aq+bq,b0:0,c0:bq+cq}
 eq('density_kernel_invariant_image',tidy({m:c.subs(imposed) for m,c in density.items()}),scale(bq/2,cross))
 # Mean-zero interaction of the orbital density difference has only a scalar
 # intervalley channel at leading order.
 zero_mean={a0:0,b0:0,c0:0,aq:1,bq:-1,cq:1}
 tuned=tidy({m:c.subs(zero_mean) for m,c in density.items()})
 eq('mean_zero_orbital_density_scalar',tuned,scale(-s.Rational(1,2),cross))
 for i,G in enumerate(boosts+rots):eq('mean_zero_density_generator_'+str(i),action(tuned,G),{})
 # Orbital-blind density kernels form a separate restricted family.
 f0,fq=s.symbols('f0 fq',real=True);blind={a0:f0,b0:f0,c0:f0,aq:fq,bq:fq,cq:fq}
 blindpoly=tidy({m:c.subs(blind) for m,c in density.items()});be=[]
 for G in boosts+rots:be.extend(action(blindpoly,G).values())
 bsol=s.linsolve(be,[f0,fq])
 check('orbital_blind_invariant_coefficient_family',bsol==s.FiniteSet((0,0)))
 # Exact CAR evaluation of the same phase average, by direct operator products.
 avg=np.zeros((16,16),complex)
 for phase in np.exp(2j*np.pi*np.arange(9)/9):
  c0=phase*ann[0]+ann[2]/phase;c1=phase*ann[1]-ann[3]/phase
  avg+=c0.conj().T@c1.conj().T@c1@c0/9
 check('native_phase_CAR',np.max(np.abs(avg-operator(zero,ann)))<2e-12)
 # Filter values and noncanonical finite-cutoff CAR overlap are explicit.
 k,zeta=s.symbols('k zeta',real=True);vel=s.sqrt(1-zeta*zeta);fp=(1+s.sin(k)/vel)/2;fm=(1-s.sin(k)/vel)/2
 for w in [-1,1]:
  check('filter_node_'+str(w),s.simplify(fp.subs(k,w*s.acos(zeta))-(1+w)/2)==0 and s.simplify(fm.subs(k,w*s.acos(zeta))-(1-w)/2)==0)
 # Six microscopic modes at z=-1,0,+1 with two orbitals. Normal-ordered
 # exterior polynomials are evaluated in their actual finite CAR algebra.
 sites=car(6);v=.8;Fplus=[1j/(4*v),.5,-1j/(4*v)];Fminus=[-1j/(4*v),.5,1j/(4*v)]
 filtered=[sum((Fplus[j]*sites[2*j+a] for j in range(3)),np.zeros((64,64),complex)) for a in range(2)]
 filtered += [sum((Fminus[j]*sites[2*j+a]*(1 if a==0 else -1) for j in range(3)),np.zeros((64,64),complex)) for a in range(2)]
 ov=filtered[0]@filtered[2].conj().T+filtered[2].conj().T@filtered[0]
 check('filtered_CAR_overlap',np.max(np.abs(ov-(.25-1/(8*v*v))*np.eye(64)))<2e-12 and abs(.25-1/(8*v*v))>.01)
 parity=np.diag([(-1)**k.bit_count() for k in range(64)])
 for idx,p in enumerate([invariants[0],invariants[1],cross]):
  op=operator(p,filtered)
  check('filtered_quartic_Hermitian_'+str(idx),np.max(np.abs(op-op.conj().T))<2e-12)
  check('filtered_quartic_parity_'+str(idx),np.max(np.abs(op@parity-parity@op))<2e-12)
 # General normal-order identity used to encode a quartic by even bilinears.
 for i,j,k,l0 in [(0,1,2,3),(0,2,2,4),(1,3,5,1),(0,1,1,0)]:
  direct=sites[i].conj().T@sites[j].conj().T@sites[k]@sites[l0]
  coded=(int(j==k)*sites[i].conj().T@sites[l0]-(sites[i].conj().T@sites[k])@(sites[j].conj().T@sites[l0]))
  check('quartic_even_bilinear_dictionary_'+str((i,j,k,l0)),np.max(np.abs(direct-coded))<2e-12)
 # A direct two-particle position-space matrix element of the simple
 # mean-zero density stencil checks its sign, coefficient and scaling.
 kap=s.symbols('kappa',real=True);qtransfer=s.symbols('Q',real=True)
 check('mean_zero_stencil_transfer',s.trigsimp(s.cos(2*kap)-s.cos(4*kap)-2*s.sin(3*kap)*s.sin(kap))==0)
 cellmodes=car(6);dens3=[cellmodes[2*j].conj().T@cellmodes[2*j]-cellmodes[2*j+1].conj().T@cellmodes[2*j+1] for j in range(3)]
 W3=(dens3[0]@dens3[1]-dens3[0]@dens3[2])/2
 check('density_stencil_Hermitian_parity',np.max(np.abs(W3-W3.conj().T))<1e-12 and np.max(np.abs(W3@parity-parity@W3))<1e-12)
 pairs=[(np.array([1.,0]),np.array([1.,0])),(np.array([1.,0]),np.array([0.,1.])),(np.array([1.,1j])/np.sqrt(2),np.array([np.cos(.37),np.sin(.37)]))]
 errors={i:[] for i in range(3)};vel0=1/np.sqrt(2);kap0=np.pi/4
 for count in [16,32,64]:
  spacing=2*np.pi/count;volume=count**3;n=np.arange(count)
  for idx,(ur,vl) in enumerate(pairs):
   u=np.exp(1j*(kap0+spacing)*n)[:,None]*ur/np.sqrt(volume)
   vv=np.exp(1j*(-kap0+2*spacing)*n)[:,None]*(np.array([1,-1])*vl)/np.sqrt(volume)
   check('two_particle_normalization_'+str((count,idx)),abs(count**2*np.sum(abs(u)**2)-1)<2e-12 and abs(count**2*np.sum(abs(vv)**2)-1)<2e-12 and abs(count**2*np.sum(u.conj()*vv))<2e-12)
   W=0.
   for disp,coef in [(1,.5),(2,-.5)]:
    ush=np.roll(u,-disp,axis=0);vsh=np.roll(vv,-disp,axis=0)
    amplitude=u[:,:,None]*vsh[:,None,:]-vv[:,:,None]*ush[:,None,:]
    W+=coef*count**2*np.sum(abs(amplitude)**2*np.array([[1,-1],[-1,1]])[None,:,:])
   scaled=vel0*W/spacing**3
   overlap=abs(np.vdot(ur,vl))**2;transfer=2*kap0-spacing
   exact=-vel0*overlap*(np.cos(transfer)-np.cos(2*transfer))/(2*np.pi)**3
   limit=-vel0*overlap/(2*np.pi)**3
   check('two_particle_density_vertex_'+str((count,idx)),abs(scaled-exact)<2e-12,actual=float(scaled),exact=float(exact),continuum_limit=float(limit))
   err=abs(scaled-limit);errors[idx].append(float(err))
   check('two_particle_continuum_bound_'+str((count,idx)),err<.01*spacing,error=float(err),spacing=spacing)
 # These finite matrix elements do not control repeated interactions or the
 # interacting ground state at lambda proportional to a^-2.
 result={'status':'ok','check_count':len(rows),'checks':rows,'native_variations':variations,'invariants':[{str(m):str(c) for m,c in p.items()} for p in invariants],'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start,'scope':'Exact component and finite-CAR challenges. No quantum interacting constraint or continuum existence theorem.'}
 (HERE/'BLOCK09_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':run()
