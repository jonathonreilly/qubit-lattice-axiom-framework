"""Bounded challenges of native local source, word-color forms and spectroscopy.

Same-author checks. No independent audit and no infinite spectral extrapolation.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import ast
import hashlib
import json
import math
import time
import numpy as np
from scipy.sparse import coo_matrix, eye
from scipy.sparse.linalg import eigsh
from scipy.special import j1

START=time.monotonic(); CHECKS=Counter(); root=Path(__file__).resolve().parents[1]
def require(condition,label):
    if not condition: raise AssertionError(label)
    CHECKS[label]+=1

# Reuse only the native local-operator definitions, without executing or
# rewriting Block9's evidence. This is explicitly not an independent operator implementation.
source=root/'evidence/block9_polarized_word_check.py'
module=ast.parse(source.read_text()); selected=[]
needed={'shift','physical_edge','path_edges','n_value','neighbors','degree','native_a','transition','native_hop'}
for node in module.body:
    if isinstance(node,(ast.Import,ast.ImportFrom)):
        selected.append(node)
    elif isinstance(node,ast.FunctionDef) and node.name in needed:
        selected.append(node)
ns={'CHECKS':Counter(),'require':require}
exec(compile(ast.Module(body=selected,type_ignores=[]),str(source),'exec'),ns)

def closed_frame(state):
    m,w=state
    return complex((-1)**sum(m)) if len(w)%2 else 1j

native_count=0
for m in product((-1,0),repeat=3):
    for n in range(1,5):
        for w in product(range(3),repeat=n):
            x=(m,w); _,p=ns['path_edges'](x)
            for letter in range(3):
                for op,expected in [('append',-1j*(-1)**sum(p)),('prepend',1j*(-1)**sum(m))]:
                    y=ns['transition'](x,op,letter)
                    amplitude=ns['native_hop'](x,y)
                    require(amplitude==expected,'literal native endpoint amplitude has closed parity formula')
                    require(closed_frame(y)*amplitude*closed_frame(x).conjugate()==-1,
                            'explicit closed frame gives negative hopping')
                    native_count+=1
            for b in ((1,0,0),(0,-1,1),(1,1,1)):
                y=(tuple(m[i]+b[i] for i in range(3)),w)
                translated_phase=(-1)**(sum(b)*n)
                require(closed_frame(y)*translated_phase*closed_frame(x).conjugate()==1,
                        'physical translated-complemented Z action becomes anchor translation')
    for i in range(3):
        require(closed_frame((m,(i,)))*(-1)**sum(m)==1,'three-edge staggered local source maps to uniform color')

# Direct original-axis word matrix and a separate tensor color rotation.
u=np.ones(3)/math.sqrt(3)
w1=np.array([1,-1,0])/math.sqrt(2)
w2=np.array([1,1,-2])/math.sqrt(6)
color=np.stack([u,w1,w2],axis=1)
N=5
words=[w for n in range(1,N+1) for w in product(range(3),repeat=n)]
index={w:i for i,w in enumerate(words)}; dim=len(words)
counts=np.array([sum(c!=0 for c in w) for w in words])

def word_matrix(words,index,k,J,lam=1):
    rr=[];cc=[];vv=[]
    for word,col in index.items():
        for i in range(3):
            for target,factor in ((word+(i,),1),((i,)+word,np.exp(1j*k[i]))):
                if target in index:
                    row=index[target]; rr.extend([row,col]);cc.extend([col,row]);vv.extend([-lam*factor,-lam*np.conj(factor)])
        for j in range(len(word)-1):
            if word[j]!=word[j+1]:
                target=word[:j]+(word[j+1],word[j])+word[j+2:]
                rr.extend([col,index[target]]);cc.extend([col,col]);vv.extend([J,-J])
    return coo_matrix((vv,(rr,cc)),shape=(len(words),len(words))).tocsr()

blocks=[]
for n in range(1,N+1):
    b=np.array([[1.]])
    for j in range(n):b=np.kron(b,color)
    blocks.append(b)
from scipy.linalg import block_diag
rotation=block_diag(*blocks)
require(np.max(abs(rotation.T@rotation-np.eye(dim)))<2e-14,'full word tensor color rotation is unitary')
rotation_results=[]
for theta in (0.,.7,math.pi):
    H=word_matrix(words,index,(theta,)*3,J=2.3)
    transformed=rotation.T@(H@rotation)
    comm=transformed*(counts[None,:]-counts[:,None])
    require(np.max(abs(comm))<2e-14,'actual axis word Hamiltonian conserves rotated color count on diagonal')
    # Columns with all zero color labels are the radial subspace.
    zero=np.flatnonzero(counts==0)
    radial=transformed[np.ix_(zero,zero)]
    expected=np.zeros((N,N),complex)
    for n in range(N-1):
        expected[n+1,n]=-math.sqrt(3)*(1+np.exp(1j*theta))
        expected[n,n+1]=expected[n+1,n].conjugate()
    require(np.max(abs(radial-expected))<3e-14,'actual word matrix radial action equals exact half-line')
    outside=np.flatnonzero(counts!=0)
    require(np.max(abs(transformed[np.ix_(outside,zero)]))<2e-14,'symmetric local source is a reducing radial channel')
    rotation_results.append({'theta':theta,'commutator_max':float(np.max(abs(comm))),
                             'radial_error':float(np.max(abs(radial-expected)))})
Hgeneric=word_matrix(words,index,(.2,.7,-.4),2.3)
generic=rotation.T@(Hgeneric@rotation)
comm=generic*(counts[None,:]-counts[:,None])
require(np.max(abs(comm))>.1,'off-line momentum breaks the color conservation used by the theorem')

# Independently build fixed-marker matrices and the telescoping edge form.
def sector_words(M,N):
    return [w for n in range(max(1,M),N+1) for w in product(range(3),repeat=n) if sum(c!=0 for c in w)==M]

def fixed_matrix(ws,theta,J,a):
    ix={w:i for i,w in enumerate(ws)};rr=[];cc=[];vv=[]
    for w,c in ix.items():
        for y,z in (((0,)+w,np.exp(1j*theta)),(w+(0,),1)):
            if y in ix:
                r=ix[y];rr.extend([r,c]);cc.extend([c,r]);vv.extend([-a*z,-a*np.conj(z)])
        for j in range(len(w)-1):
            if w[j]!=w[j+1]:
                y=w[:j]+(w[j+1],w[j])+w[j+2:]
                rr.extend([c,ix[y]]);cc.extend([c,c]);vv.extend([J,-J])
    return coo_matrix((vv,(rr,cc)),shape=(len(ws),len(ws))).tocsr()+4*a*eye(len(ws)),ix

def insertions(word):
    # The u runs end immediately before the next non-u marker.
    positions=[i for i,c in enumerate(word) if c!=0]+[len(word)]
    return [word[:i]+(0,)+word[i:] for i in positions]

rng=np.random.default_rng(141709)
form_results=[]
for M in range(4):
    ws=sector_words(M,7);a=math.sqrt(3);theta=.9;J=1.7
    T,ix=fixed_matrix(ws,theta,J,a)
    f=rng.normal(size=len(ws))+1j*rng.normal(size=len(ws));f/=np.linalg.norm(f)
    def value(w):return f[ix[w]] if w in ix else 0j
    edge=0.;boundary=0.;internal=0.;telescoped=0.;seen=Counter()
    for w,c in ix.items():
        edge+=a*abs(value((0,)+w)-np.exp(1j*theta)*f[c])**2
        edge+=a*abs(value(w+(0,))-f[c])**2
        # Missing annihilation ranges are actual lower boundaries.
        if len(w)==1 or w[0]!=0:boundary+=a*abs(f[c])**2
        if len(w)==1 or w[-1]!=0:boundary+=a*abs(f[c])**2
        # The finite principal compression adds a second missing range at top.
        # The forward differences above already include its diagonal contribution.
        ins=insertions(w)
        terms=[value(ins[0])-np.exp(1j*theta)*f[c]]
        terms += [value(ins[j+1])-value(ins[j]) for j in range(M)]
        terms += [-(value(ins[-1])-f[c])]
        require(abs(sum(terms)-(1-np.exp(1j*theta))*f[c])<2e-15,'coefficient-level telescope including color sequence')
        q=a*(abs(terms[0])**2+abs(terms[-1])**2)+J*sum(abs(t)**2 for t in terms[1:-1])
        denom=2/a+M/J
        require(abs(sum(terms))**2<=denom*q+2e-15,'weighted telescoping Cauchy inequality')
        telescoped+=q
        for j in range(M):
            x,y=ins[j],ins[j+1]
            if x in ix and y in ix:seen[tuple(sorted((x,y)))]+=1
        for j in range(len(w)-1):
            if w[j]!=w[j+1]:
                y=w[:j]+(w[j+1],w[j])+w[j+2:]
                if w<y:
                    e=J*abs(f[c]-value(y))**2
                    internal+=e
    # Endpoint differences include diagonal 2a plus upper targets; with lower
    # range boundary they reproduce 4aI minus creation and annihilation exactly.
    direct=float(np.vdot(f,T@f).real)
    require(abs(direct-edge-boundary-internal)<2e-13,'complete endpoint boundary and swap form equals actual matrix')
    require(telescoped<=direct+2e-13,'summed telescoping forms use each allowed energy edge at most once')
    expected_edges=set()
    for w in ws:
        for j in range(len(w)-1):
            if (w[j]==0)!=(w[j+1]==0):
                y=w[:j]+(w[j+1],w[j])+w[j+2:]
                expected_edges.add(tuple(sorted((w,y))))
    require(set(seen)==expected_edges and all(v==1 for v in seen.values()),
            'every u-marker swap edge recovered exactly once by insertion base')
    delta=4*math.sin(theta/2)**2/(2/a+M/J)
    bottom=float(eigsh(T,k=1,which='SA',return_eigenvectors=False,tol=1e-11)[0]) if len(ws)>2 else float(np.linalg.eigvalsh(T.toarray())[0])
    require(bottom>=delta-1e-10,'finite full marker sector obeys analytic uniform lower bound')
    form_results.append({'M':M,'dimension':len(ws),'theta':theta,'J':J,'form_error':abs(direct-edge-boundary-internal),
                         'unique_swap_edges':len(seen),'bottom_above_full_threshold':bottom,'analytic_lower':delta})

# Exact finite-walk moments challenge the half-line and two-half-line measures.
def catalan(m):return math.comb(2*m,m)//(m+1)
moments=[]
for theta in (0.,.7,math.pi):
    H=word_matrix(words,index,(theta,)*3,J=0)
    for source_vec,label in ((u,'symmetric'),(w1,'orthogonal')):
        x=np.zeros(dim,complex);x[:3]=source_vec;y=x.copy()
        for power in range(9):
            if power%2==0:
                m=power//2
                if label=='symmetric':expected=catalan(m)*(12*math.cos(theta/2)**2)**m
                else:expected=sum(math.comb(2*m,2*j)*catalan(j)*catalan(m-j) for j in range(m+1))*3**m
                actual=np.vdot(x,y).real
                require(abs(actual-expected)<1e-8*max(1,abs(expected)),'untruncated closed-walk moment agrees with source spectral formula')
                moments.append({'theta':theta,'channel':label,'power':power,'actual':float(actual),'expected':expected})
            y=H@y
# Return to length one in <=8 steps never visits length>5: these moments
# have no upper-cutoff error even though later unmatched path powers do.

# Deterministic sine quadrature for the analytic Bessel integral, not a proof
# by spectral truncation. The proof is the explicit half-line sine transform.
response=[]
for h in (0.0,.8,2*math.sqrt(3)):
    for time_value in (.1,1.,3.):
        values=[]
        for mesh in (128,256):
            q=np.arange(1,mesh)*math.pi/mesh
            values.append(np.sum((2/mesh)*np.sin(q)**2*np.exp(2j*h*time_value*np.cos(q))))
        exact=1. if h==0 else j1(2*h*time_value)/(h*time_value)
        require(abs(values[0]-values[1])<1e-13 and abs(values[-1]-exact)<1e-13,
                'sine spectral integral agrees with Bessel response')
        response.append({'h':h,'time':time_value,'error':float(abs(values[-1]-exact))})

result={'status':'PASS_personal_bounded_source_and_form_challenges','native_forward_moves':native_count,
        'rotation_checks':rotation_results,'fixed_marker_form_checks':form_results,'source_moments':moments,
        'response_integrals':response,'checks':dict(CHECKS),'seconds':time.monotonic()-START,
        'limits':['same author; reused Block9 native operator definitions identified explicitly',
                  'finite matrix checks challenge analytic infinite-sector bounds',
                  'uniform M-sector lower bound is from injective edge counting and Cauchy-Schwarz',
                  'local-source spectral invisibility only on specified diagonal line and background',
                  'near-line Sylvester leakage bound analytic, no numerical certificate',
                  'no physical vacuum selection or independent audit'],
        'sha256':{str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in
                  [Path(__file__).resolve(),source,root/'notes/BLOCK10_LOCAL_SOURCE_SPECTRA_AND_DARK_THRESHOLD.md']}}
output=json.dumps(result,indent=2);Path(__file__).with_suffix('.json').write_text(output+'\n');print(output)
