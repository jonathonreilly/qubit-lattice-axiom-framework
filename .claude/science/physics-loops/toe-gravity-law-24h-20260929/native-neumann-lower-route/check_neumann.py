"""Bounded author controls; no imported campaign numerical implementation."""
import datetime, hashlib, itertools, json, os, pathlib, resource, signal, time
ROOT=pathlib.Path(__file__).resolve().parent
RUN=pathlib.Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
start=time.perf_counter(); cpu=time.process_time()
assert time.time()<json.loads((RUN/'DEADLINE.json').read_text())['deadline_epoch']
assert not (RUN/'STOP_REQUESTED.json').exists()
assert all(os.environ.get(k)=='1' for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'])
resource.setrlimit(resource.RLIMIT_CPU,(30,30)); signal.alarm(180)
import numpy as np

unit=[tuple(int(i==j) for i in range(3)) for j in range(3)]
add=lambda x,y:tuple(a+b for a,b in zip(x,y))
sc=lambda c,x:tuple(c*a for a in x)
dirs=[sc(2,e) for e in unit]
for i,j in itertools.combinations(range(3),2):
    for r in (1,-1):dirs.append(add(unit[i],sc(r,unit[j])))

def oriented(x,y):
    delta=tuple(b-a for a,b in zip(x,y))
    if delta in dirs:return x,dirs.index(delta)
    delta=sc(-1,delta)
    if delta in dirs:return y,dirs.index(delta)
    raise ValueError((x,y))

def plus(*parts):
    out={}
    for weight,row in parts:
        for k,c in row.items():out[k]=out.get(k,0)+weight*c
    return {k:c for k,c in out.items() if c}

def words(x):
    axial=[{oriented(add(x,e),add(x,sc(-1,e))):1} for e in unit]
    plane=[]
    for i,j in itertools.combinations(range(3),2):
        plane.append([{oriented(add(x,sc(s,unit[i])),add(x,sc(t,unit[j]))):s*t}
                      for s,t in itertools.product((1,-1),repeat=2)])
    return axial,plane

def qrows(x):
    d,v=words(x)
    return [(plus((1,d[0]),(-1,d[1])),1/2),
            (plus((1,d[0]),(1,d[1]),(-2,d[2])),1/6)]+[
            (plus(*[(1,r) for r in plane]),1/4) for plane in v]

def cut_matrix(ell):
    cells=list(itertools.product(range(ell),repeat=3)); idx={x:i for i,x in enumerate(cells)}
    n=9*ell**3; K=np.zeros((n,n)); accepted=0
    def insert(row,weight):
        nonlocal accepted
        if any(anchor not in idx for anchor,d in row):return
        ix=np.array([9*idx[anchor]+d for anchor,d in row]); c=np.array(list(row.values()))
        K[np.ix_(ix,ix)]+=weight*np.outer(c,c); accepted+=1
    for x in itertools.product(range(-2,ell+2),repeat=3):
        d,v=words(x); insert(plus(*[(1,r) for r in d]),2/3)
        for plane in v:
            for a,b in itertools.combinations(plane,2):insert(plus((1,a),(-1,b)),1/4)
        q=qrows(x)
        for e in unit:
            qp=qrows(add(x,e))
            for (r,w),(rp,wp) in zip(q,qp):
                assert w==wp; insert(plus((1,rp),(-1,r)),w)
    lap=np.zeros((n,n))
    for x in cells:
        for e in unit:
            y=add(x,e)
            if y not in idx:continue
            for d in range(9):
                i,j=9*idx[x]+d,9*idx[y]+d
                lap[i,i]+=1;lap[j,j]+=1;lap[i,j]-=1;lap[j,i]-=1
    U=np.zeros((9,5));U[:3,:2]=[[1/np.sqrt(2),1/np.sqrt(6)],[-1/np.sqrt(2),1/np.sqrt(6)],[0,-2/np.sqrt(6)]]
    for j in range(3):U[3+2*j:5+2*j,2+j]=[-1/np.sqrt(2),1/np.sqrt(2)]
    soft=np.tile(U,(ell**3,1))/np.sqrt(ell**3)
    return K,lap,soft,idx,accepted

gap_controls=[]
for ell in (3,4):
    K,lap,soft,idx,rows=cut_matrix(ell)
    corner=9*idx[(0,0,0)]
    assert np.linalg.norm(K[:,corner])==0
    assert np.max(np.abs(K@soft))<2e-13
    naive=np.linalg.eigvalsh(K)
    for eps in (0.05,0.25):
        B=(1-eps)*K+eps/12*lap
        vals,vecs=np.linalg.eigh(B)
        assert sum(abs(vals)<1e-10)==5
        bound=eps/(12*14*ell**2)
        assert vals[5]>=bound-1e-12
        pin=[9*idx[(ell//2,)*3]+d for d in range(9)]
        gamma=(vecs[pin,5:]/vals[5:])@vecs[pin,5:].T
        lower=(1-1/ell**3)/26
        assert np.linalg.eigvalsh(gamma)[0]>=lower-1e-10
        gap_controls.append({'ell':ell,'epsilon':eps,'rows':rows,'naive_nullity':int(sum(abs(naive)<1e-10)),
                             'regularized_nullity':5,'gap':float(vals[5]),'gap_bound':bound,
                             'common_pin_min_green':float(np.linalg.eigvalsh(gamma)[0]),'lower_bound':lower})

# Literal Neumann cosine basis versus eight periodic reflection images.
ell=7; sites=list(itertools.product(range(ell),repeat=3)); index={x:i for i,x in enumerate(sites)}
n=np.arange(ell); phi1=np.cos(np.pi*(n[:,None]+0.5)*n[None,:]/ell)*np.sqrt((2-(n==0))/ell)
phi=np.kron(np.kron(phi1,phi1),phi1)
eigen1=2*(1-np.cos(np.pi*n/ell)); lam=(eigen1[:,None,None]+eigen1[None,:,None]+eigen1[None,None,:]).ravel()
inv=np.zeros_like(lam);inv[1:]=1/lam[1:]
GN=(phi*inv)@phi.T
t=2*ell;k=2*np.pi*np.arange(t)/t;one=2*(1-np.cos(k))
symbol=one[:,None,None]+one[None,:,None]+one[None,None,:]
rec=np.zeros_like(symbol);np.divide(1,symbol,out=rec,where=symbol>0)
GT=np.fft.ifftn(rec).real
rng=np.random.default_rng(731)
error=0.0; wrong_error=0.0
for _ in range(500):
    x=sites[int(rng.integers(len(sites)))];y=sites[int(rng.integers(len(sites)))];images=0.
    for signs in itertools.product((1,-1),repeat=3):
        yy=tuple(yj if s==1 else -yj-1 for yj,s in zip(y,signs))
        images+=GT[tuple((a-b)%t for a,b in zip(x,yy))]
    value=GN[index[x],index[y]]
    error=max(error,abs(value-images));wrong_error=max(wrong_error,abs(value-images/8))
assert error<1e-13 and wrong_error>0.01
pins=[(1,1,1),(1,5,5),(5,1,5),(5,5,1)]
ix=[index[x] for x in pins];gamma=GN[np.ix_(ix,ix)]
B=float(np.linalg.eigvalsh(gamma)[-1]);m=len(pins)
f=rng.normal(size=(ell,ell,ell,9))+1j*rng.normal(size=(ell,ell,ell,9))
for pin in pins:f[pin]=0
E=sum(float(np.sum(abs(np.diff(f,axis=j))**2)) for j in range(3))
c=f.mean(axis=(0,1,2));mass=float(np.sum(abs(f)**2))
mean_bound=m*float(np.sum(abs(c)**2))/B
mass_bound=m*mass/(ell**3*(B+m/(4*ell)))
assert E>=mean_bound and E>=mass_bound

# Physical removal counting, with no matching-sector normalization.
L=128;cell=32;w=4;R=5
neigh=dirs+[sc(-1,d) for d in dirs]
def dist(x,y):return max(min(abs(a-b),L-abs(a-b)) for a,b in zip(x,y))
def edges(S):
    return {tuple(sorted((x,add(x,d)))) for x in S for d in dirs if add(x,d) in S}
def good(S):
    return [e for e in edges(S) if all(min(dist(v,e[0]),dist(v,e[1]))>R for v in S-set(e))]
def cell_of(e):
    c=tuple(a//cell for a in e[0])
    if not all(tuple(a//cell for a in p)==c for p in e):return None
    if not all(w<=a%cell<cell-w for p in e for a in p):return None
    return c
def check_count(S):
    counts={}
    for e in good(S):
        c=cell_of(e)
        if c is not None:counts[c]=counts.get(c,0)+1
    lhs={}
    for e in edges(S):
        anchor,d=oriented(*e);c=tuple(a//cell for a in anchor)
        residual=S-set(e)
        m=sum(cell_of(other)==c for other in good(residual))
        lhs[c]=lhs.get(c,0)+m
    rhs={c:g*(g-1) for c,g in counts.items()}
    assert all(lhs.get(c,0)>=v for c,v in rhs.items())
    return {'N':len(S),'graph_edges':len(edges(S)),'selected_dimers':sum(counts.values()),
            'lhs':sum(lhs.values()),'rhs':sum(rhs.values())}
count_controls=[]
for case in range(8):
    S=set()
    for cx,cy,cz in ((0,0,0),(1,0,0),(0,1,1)):
        for j,p in enumerate(((7,7,7),(17,7,7),(7,17,17),(17,17,17))):
            x=tuple(v+cell*c for v,c in zip(p,(cx,cy,cz)));d=dirs[(case+j)%9]
            S.update((x,add(x,d)))
    # Boundary dimer and compact triangle are kept as real occupations.
    S.update(((1,1,1),(3,1,1),(50,50,50),(52,50,50),(51,51,50)))
    count_controls.append(check_count(S))
S=set()
for p in ((7,7,7),(17,7,7),(7,17,17)):S.update((p,add(p,(2,0,0))))
exact=check_count(S);assert exact['lhs']==exact['rhs']==6
assert exact['lhs']/2<exact['rhs']

result={'source_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        'gap_controls':gap_controls,'naive_corner_cut_zero_column':True,
        'neighbor_deletion_D_counterexample':{'one_graph_dimer_original_D':0,'delete_its_graph_edge_D':2},
        'neumann_reflection_max_error':error,'wrong_image_divide_eight_error':wrong_error,
        'pin_control':{'pins':pins,'max_green_eigenvalue':B,'literal_gradient_energy':E,'mean_pin_bound':mean_bound,'mass_pin_bound':mass_bound},
        'literal_count_controls':count_controls,'exact_three_dimer_count':exact,
        'cpu_seconds':time.process_time()-cpu,'wall_seconds':time.perf_counter()-start,
        'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(ROOT/'neumann_results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
