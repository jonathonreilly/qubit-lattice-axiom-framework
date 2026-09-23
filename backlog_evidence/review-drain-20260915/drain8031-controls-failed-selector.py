import json,numpy as np,pathlib,hashlib,itertools
root=pathlib.Path('/private/tmp/review-drain-20260915'); raw=root/'drain8031-originals/.claude/science/physics-loops/finite-transporter-bridge-20260907/CANONICAL_RESULT.json'; d=json.loads(raw.read_text()); U=np.zeros((57,57))
vals={'sqrt(3)/3':1/np.sqrt(3),'1/2':.5,'-1/2':-.5}
for i,j,x in d['nonzero_U_entries']:U[i,j]=vals.get(x,float(x) if '/' not in x and 'sqrt' not in x else 0)
G=U.T@U; D=np.eye(57)-G; P=np.diag([1]*3+[0]*54); S=np.eye(57)-P
checks={}
def ck(n,v):checks[n]=bool(v);assert v,n
ck('raw_Gram_spectrum_15_ones_42_zeros',np.allclose(np.linalg.eigvalsh(G),[0]*42+[1]*15));ck('shell_support',np.allclose(D,S@D@S));ck('vacuum_isometry',np.allclose(P@G@P,P));ck('highest_weight_index3_kernel',np.allclose(U[:,3],0));ck('trace_offset38',sum((int(q)+t)**2-int(q)**2 for q in d['Cartan_link_generator'] for t in [1,-1,0])==38)
for R in range(1,41):ck('balanced_energy_'+str(R),min(p*p+p*(R-p)+(R-p)**2+3*R for p in range(R+1))==R*R-(R*R//4)+3*R)
# Distinct link projector identity with genuinely shared noncommuting color.
rng=np.random.default_rng(8031); dims=(3,3,2);n=18
local=[]
for e in range(2):
 z=rng.normal(size=(6,6))+1j*rng.normal(size=(6,6));w=np.linalg.qr(z)[0]; a=np.zeros((n,n),complex)
 for ix in itertools.product(*[range(x) for x in dims]):
  for iy in itertools.product(*[range(x) for x in dims]):
   if ix[1-e]==iy[1-e]:a[np.ravel_multi_index(ix,dims),np.ravel_multi_index(iy,dims)]=w[2*ix[e]+ix[2],2*iy[e]+iy[2]]
 local.append(a)
p0=np.diag([float(i<2) for i,j,c in itertools.product(range(3),range(3),range(2))]);p1=np.diag([float(j<2) for i,j,c in itertools.product(range(3),range(3),range(2))]);p=p0@p1; a,b=local
ck('shared_color_noncommuting',not np.allclose(a@b,b@a));ck('distinct_projection_identity',np.allclose(p@b@p@a@p,p@b@a@p));ck('repeated_link_adverse',not np.allclose(p0@a@p0@a@p0,p0@a@a@p0))
# Actual raw-matrix mutations detect coefficient and sign defects by the named invariants.
mut=U.copy();i,j=next((i,j) for i,j,x in d['nonzero_U_entries'] if x=='sqrt(3)/3');mut[i,j]*=2
ck('coefficient_mutation_caught_by_vacuum_isometry',not np.allclose(P@mut.T@mut@P,P))
q=np.repeat([int(x) for x in d['Cartan_link_generator']],3);t=np.tile([1,-1,0],19)
ck('covariance_independent_diagonal',np.allclose((q[:,None]-q[None,:]+t[:,None])*U,0));ck('wrong_sign_mutation_caught',not np.allclose((q[:,None]-q[None,:]-t[:,None])*U,0))
(root/'drain8031-controls.json').write_text(json.dumps(dict(checks=checks,raw_sha256=hashlib.sha256(raw.read_bytes()).hexdigest(),numpy=np.__version__,scope='Independent raw-matrix eigensolver, shell enumeration and distinct-link projector controls; no primary runner execution; surrogate path identity only, not SU3 path simulation.'),indent=2)+'\n');print(len(checks),'controls passed')
