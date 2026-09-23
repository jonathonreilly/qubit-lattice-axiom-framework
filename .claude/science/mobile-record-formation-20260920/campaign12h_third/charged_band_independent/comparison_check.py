"""Bounded post-seal charged-band comparison. Imports no author code."""
from pathlib import Path
from datetime import datetime,timezone
from itertools import product,combinations
import hashlib,json,math
import numpy as np
import sympy as s
from scipy.linalg import null_space
from scipy.sparse import diags,kron,eye,csr_matrix
from scipy.sparse.linalg import expm_multiply
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
OUT=HERE/'COMPARISON_RESULTS.json';assert not OUT.exists()
def row(p):
    p=Path(p);b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(r,p=None):
    v=row(p or r['path']);assert v['bytes']==r['bytes'] and v['sha256']==r['sha256'],(r,v)
prepath=HERE/'PRE_COMPARISON_SEAL.json';authpath=BASE/'CHARGED_BAND_AUTHOR_SEAL.json'
assert row(prepath)['sha256']=='4c13933f96f93217a20683f9b229d50c7e97fab28a556f90cce0226858ad3e48'
assert row(authpath)['sha256']=='c1c6420437307f014d547aaab23e261547d667e15eec0e736a600b0d75abf581'
pre=json.loads(prepath.read_text());auth=json.loads(authpath.read_text())
for r in pre['sources']+pre['artifacts']+auth['artifacts']:verify(r)
ctx=json.loads((BASE/'CHARGED_BAND_SOURCE_CONTEXT.json').read_text())
verify(ctx['target_source']);verify(ctx['target_source_seal'])

# Exact star matrix identity by its opposite-pair decomposition, independently
# testing invariant spaces instead of merely calling an eigenvalue routine.
stars=[]
for d in (2,3,4,7):
    z=2*d;opposite=s.zeros(z)
    for k in range(d):opposite[2*k,2*k+1]=opposite[2*k+1,2*k]=1
    lap=(z-1)*s.eye(z)+opposite-s.ones(z)
    assert lap*s.ones(z,1)==s.zeros(z,1)
    for k in range(d):
        v=s.zeros(z,1);v[2*k]=1;v[2*k+1]=-1
        assert lap*v==(z-2)*v
    for k in range(1,d):
        v=s.zeros(z,1);v[0]=v[1]=1;v[2*k]=v[2*k+1]=-1
        assert lap*v==z*v
    stars.append({'dimension':d,'exact_spectrum':{'0':1,str(z-2):d,str(z):d-1}})

# Independently assemble a rectangular torus and the alternative completed-star
# Gram matrix before eliminating the A-site phase variables.
periods=(6,10);d=2
vertices=list(product(*[range(L) for L in periods]));vi={x:i for i,x in enumerate(vertices)}
def shift(x,i,sign=1):
    y=list(x);y[i]=(y[i]+sign)%periods[i];return tuple(y)
edges=[(x,i) for x in vertices for i in range(d)];ei={e:k for k,e in enumerate(edges)}
As=[x for x in vertices if sum(x)%2==0];ai={x:i for i,x in enumerate(As)}
M=len(edges);n=len(As);V=len(vertices)
D=np.zeros((V,M));C=np.zeros((V,M));T=np.zeros((V,M));B=np.zeros((n,V))
for k,(x,i) in enumerate(edges):D[vi[x],k]=1;D[vi[shift(x,i)],k]=-1
for p,x in enumerate(vertices):
    c=[x,shift(x,0),shift(shift(x,0),1),shift(x,1)]
    legs=[(ei[x,0],1),(ei[shift(x,0),1],1),(ei[shift(x,1),0],-1),(ei[x,1],-1)]
    for k,sign in legs:C[p,k]=sign
    if sum(x)%2:c=c[1:]+c[:1];legs=legs[1:]+legs[:1]
    B[ai[c[0]],p]=1;B[ai[c[2]],p]=-1
    for j,(k,sign) in enumerate(legs):T[p,k]=sign*(1 if j<2 else -1)
Br=B[:-1];Pi=np.eye(V)-Br.T@np.linalg.solve(Br@Br.T,Br)
F=C.T@C+T.T@Pi@T
joint=np.zeros((M+n,M+n));lap=np.array([[2,0,-1,-1],[0,2,-1,-1],[-1,-1,2,0],[-1,-1,0,2]],float)
for b in vertices:
    if sum(b)%2==0:continue
    Z=np.zeros((4,M+n));k=0
    for i in range(d):
        for sg in (-1,1):
            a=shift(b,i,sg)
            if sg==-1:e=ei[a,i];sign=1
            else:e=ei[b,i];sign=-1
            Z[k,e]=sign;Z[k,M+ai[a]]=1;k+=1
    joint+=2*Z.T@lap@Z
# Ground the redundant constant f_A to avoid numerical pseudoinverse choices.
ff=joint[M:-1,M:-1];af=joint[:M,M:-1]
star_schur=joint[:M,:M]-af@np.linalg.solve(ff,af.T)
star_error=float(np.max(np.abs(F-star_schur)));assert star_error<1e-12
U=null_space(D);evF=np.linalg.eigvalsh(U.T@F@U)
assert evF[0]>4*(d-1)-1e-11 and evF[-1]<4*d+1e-11
pe=(n-2)/(2*(n-1));po=n/(2*(n-1))
Q=pe*C.T@C+po*T.T@Pi@T
hess=2*Q;evM=np.linalg.eigvalsh(U.T@hess@U)
lower=4*(d-1)*(n-2)/(n-1);upper=4*d*n/(n-1)
assert evM[0]>lower-1e-11 and evM[-1]<upper+1e-11
rect={'periods':periods,'physical_dimension':U.shape[1],'completed_star_schur_error':star_error,
      'F_eigenvalue_range':[float(evF[0]),float(evF[-1])],'F_bounds':[4*(d-1),4*d],
      'Hessian_eigenvalue_range':[float(evM[0]),float(evM[-1])],'Hessian_bounds':[lower,upper],
      'scope':'Whole physical tangent space, not one selected transverse family; finite floating corroboration of the exact local proof.'}

# Sign transformation: test different even geometries and an explicit out-of-scope
# odd-period obstruction to this same formula.
def flux(periods):
    d=len(periods);count=0;wrap=0;fail=0
    def plus(x,i):
        y=list(x);y[i]=(y[i]+1)%periods[i];return tuple(y)
    def nu(x,i):return sum(x[:i])%2
    for x in product(*[range(L) for L in periods]):
        for i,j in combinations(range(d),2):
            cycle=[x,plus(x,i),plus(plus(x,i),j),plus(x,j)]
            legs=[((x,i),1),((plus(x,i),j),1),((plus(x,j),i),-1),((x,j),-1)]
            if sum(x)%2:cycle=cycle[1:]+cycle[:1];legs=legs[1:]+legs[:1]
            wrapping=x[i]==periods[i]-1 or x[j]==periods[j]-1
            for q,r in product((-1,1),repeat=2):
                deltas=[-q,-q,-r,-r]
                parity=sum(nu(y,k)*sg*delta for ((y,k),sg),delta in zip(legs,deltas))%2
                count+=1;wrap+=int(wrapping);fail+=int(parity!=1)
    return {'periods':periods,'charge_sign_checks':count,'wrapping_charge_checks':wrap,'failures':fail}
signs=[flux((8,10)),flux((6,6,8)),flux((7,7))]
assert signs[0]['failures']==signs[1]['failures']==0 and signs[2]['failures']>0

# Rebuild the auxiliary six-component compact model and one finite evolution via
# Fourier coefficient matrices and Kronecker shifts; no author generator import.
words=[tuple(1 if k in plus else -1 for k in range(4)) for plus in combinations(range(4),2)]
index={q:i for i,q in enumerate(words)};m=len(words);cyc=[(0,1),(1,2),(2,3),(3,0)]
H0=s.zeros(m);H1=s.zeros(m);H2=s.zeros(m)
fourier={ell:np.zeros((m,m)) for ell in (-2,0,2)}
for edge,(a,c) in enumerate(cyc):
    for col,q in enumerate(words):
        out=list(q);out[a],out[c]=out[c],out[a];rr=index[tuple(out)]
        phase=(q[a]-q[c]) if edge==0 else 0
        H0[rr,col]-=2;H1[rr,col]+=2*s.I*phase;H2[rr,col]+=2*phase**2
        fourier[-phase][rr,col]-=2
u=s.ones(m,1)/s.sqrt(m);P=u*u.T;reduced=(H0+8*s.eye(m)+P).inv()-P
prime=-reduced*H1*u
norm=s.simplify((prime.conjugate().T*prime)[0])
curvature=s.simplify((u.T*H2*u-2*u.T*H1*reduced*H1*u)[0])
assert norm==s.Rational(5,12) and curvature==s.Rational(4,3)
h=1/64;grid=4096;cut=144
angles=2*np.pi*np.fft.fftfreq(grid)
z=np.clip((np.abs(angles)-.7)/.3,0,1);cutoff=1-10*z**3+15*z**4-6*z**5
band=np.tile(np.ones(m)/np.sqrt(m),(grid,1)).astype(complex)
for k in np.flatnonzero(cutoff):
    potential=sum(np.exp(1j*ell*angles[k])*a for ell,a in fourier.items())
    val,vec=np.linalg.eigh(potential);v=vec[:,0];phase=np.vdot(np.ones(m)/np.sqrt(m),v)
    assert abs(phase)>.5
    band[k]=v*np.exp(-1j*np.angle(phase))
alpha=math.sqrt(float(curvature)/2);x=angles/math.sqrt(h)
phi0=(alpha/np.pi)**.25*np.exp(-alpha*x*x/2);phi1=math.sqrt(2*alpha)*x*phi0
modes=np.arange(-cut,cut+1);nm=len(modes)
def coeff(phi):
    field=h**(-.25)*(cutoff*phi)[:,None]*band
    ft=np.fft.fft(field,axis=0)/grid
    return (np.sqrt(2*np.pi)*ft[modes%grid]).reshape(-1)
c0,c1=coeff(phi0),coeff(phi1)
packet_norm=np.linalg.norm((c0+c1)/np.sqrt(2));initial=(c0+c1)/(np.sqrt(2)*packet_norm)
Ham=kron(diags(h*modes*modes+8/h),eye(m),format='csr')
for ell,mat in fourier.items():
    shift=diags(np.ones(nm-abs(ell)),offsets=-ell,shape=(nm,nm))
    Ham+=kron(shift,csr_matrix(mat/h),format='csr')
assert np.max(np.abs((Ham-Ham.T).data),initial=0)<1e-13
res0=np.linalg.norm(Ham@c0-alpha*c0);res1=np.linalg.norm(Ham@c1-3*alpha*c1)
actual=expm_multiply(-1j*Ham,initial)
target=(np.exp(-1j*alpha)*c0+np.exp(-3j*alpha)*c1)/(np.sqrt(2)*packet_norm)
error=float(np.linalg.norm(actual-target));bound=float((res0+res1)/(np.sqrt(2)*packet_norm))
assert error<bound
recorded=json.loads((BASE/'CHARGED_BAND_PACKET_RESULTS.json').read_text())
reference=next(r for r in recorded['rows'] if r['h']==h)
reference_error=next(r for r in reference['times'] if r['time']==1)['state_norm_error']
assert abs(error-reference_error)<1e-9
assert max(abs(res0-reference['residuals'][0]),abs(res1-reference['residuals'][1]))<1e-10
packet={'h':h,'grid':grid,'cutoff':cut,'dimension':nm*m,'Hessian_exact':str(curvature),
 'band_derivative_norm_squared_exact':str(norm),'residuals':[float(res0),float(res1)],
 'time':1,'state_error':error,'Duhamel_bound':bound,'author_state_error':reference_error,
 'difference_from_author':error-reference_error,'unitarity_error':float(abs(np.linalg.norm(actual)-1)),
 'scope':'Independent one-row auxiliary compact matrix-model reconstruction; not a full cubic Gauss evolution or an interval error certificate.'}

# Read and authenticate successful streams/receipts and the archived refinement failure.
receipts=[]
for prefix,resultname in [('CHARGED_RECORD_POTENTIAL_HESSIAN_CHECK','CHARGED_RECORD_POTENTIAL_HESSIAN_RESULTS.json'),
 ('CHARGED_BAND_PACKET_CHECK','CHARGED_BAND_PACKET_RESULTS.json'),('CHARGED_BAND_GEOMETRY_CHECK','CHARGED_BAND_GEOMETRY_RESULTS.json')]:
    r=json.loads((BASE/(prefix+'_RECEIPT.json')).read_text());assert r['exit_code']==0
    for key in ['source','stdout','stderr']:verify(r[key])
    assert Path(r['stdout']['path']).read_bytes()==(BASE/resultname).read_bytes()
    receipts.append({'receipt':row(BASE/(prefix+'_RECEIPT.json')),'all_three_bindings_verified':True,'stdout_equals_result':True})
oldbase=BASE/'charged_band_source_history/initial_refinement_failure'
oldrec=json.loads((oldbase/'CHARGED_BAND_PACKET_CHECK_RECEIPT.json').read_text());assert oldrec['exit_code']==1
for key in ['source','stdout','stderr']:verify(oldrec[key],oldbase/Path(oldrec[key]['path']).name)
old=(oldbase/'charged_band_packet_check.py').read_text();new=(BASE/'charged_band_packet_check.py').read_text()
assert old.replace('math.ceil(8/math.sqrt(h))','math.ceil(12/math.sqrt(h))').replace('extra=20,grid=16384','extra=60,grid=16384')==new
out={'created_utc':datetime.now(timezone.utc).isoformat(),'source':row(__file__),
 'pre_seal':row(prepath),'author_seal':row(authpath),
 'authentication_counts':{'PRE':len(pre['sources'])+len(pre['artifacts']),'author':len(auth['artifacts']),'context':2},
 'convention':'Author M_J=2J Q_independent and Theta=T_independent/2; incidence orientations differ by a transpose/sign only.',
 'exact_star_controls':stars,'all_direction_rectangular_control':rect,'sign_controls':signs,
 'independent_packet_control':packet,'author_receipts':receipts,
 'author_failed_attempt':'Archived original authenticates; only cutoff8->12 and refinement20->60 changed. Original1e-9 threshold remains.',
 'status':'No material mathematical discrepancy found in the bounded comparison.',
 'limits':['No full author suite or dense full neutral cubic matter matrix replay.',
 'Finite floating checks are not interval enclosures.','Uniform quadratic curvature does not make packet error constants uniform in volume.',
 'Sign transformation changes only overall target ring sign on stipulated even boxes; no microscopic statistics theorem.']}
OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
