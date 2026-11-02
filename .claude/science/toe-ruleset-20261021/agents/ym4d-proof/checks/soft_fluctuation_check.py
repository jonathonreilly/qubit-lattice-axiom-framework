#!/usr/bin/env python3
"""Finite independent diagnostics for the explicitly stated one-step soft model.
No predecessor helper or external scientific data is imported. The analytic
all-volume bounds are in the source note, not proved by the finite tests.
"""
AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = []
import argparse, hashlib, itertools, json, math, platform, sys, time
from collections import defaultdict
from pathlib import Path
import numpy as np
import scipy
from scipy import sparse, linalg, special, integrate
from scipy.sparse.linalg import spsolve

L = 3
D = 4
HALF = (L-1)//2
SITES = list(itertools.product(range(-HALF, HALF+1), repeat=D))
SID = {x:i for i,x in enumerate(SITES)}
EDGES = [(x,mu) for x in SITES for mu in range(D)]
EID = {e:i for i,e in enumerate(EDGES)}
PAIRS = list(itertools.combinations(range(D),2))
ROOT = (0,)*D
TESTS=[]
DETAILS={}

def gate(name, condition, detail=None):
    TESTS.append({'name':name, 'pass':bool(condition), 'detail':detail})

def add(x,mu,amount=1):
    x=list(x); x[mu]+=amount; return tuple(x)

def word(start,end,order):
    p=start; out=[]
    for mu in order:
        while p[mu] != end[mu]:
            s=1 if end[mu]>p[mu] else -1
            base=p if s==1 else add(p,mu,-1)
            out.append((base,mu,s)); p=add(p,mu,s)
    assert p==end
    return out

def reverse(w): return [(x,mu,-s) for x,mu,s in reversed(w)]

def chain(w):
    a=defaultdict(int)
    for x,mu,s in w:a[x,mu]+=s
    return {k:v for k,v in a.items() if v}

def chain_sum(*args):
    a=defaultdict(int)
    for scale, z in args:
        for e,c in z.items():a[e]+=scale*c
    return {k:v for k,v in a.items() if v}

def boundary1(z):
    a=defaultdict(int)
    for (x,mu),c in z.items():a[x]-=c;a[add(x,mu)]+=c
    return {k:v for k,v in a.items() if v}

def boundary2(s):
    a=defaultdict(int)
    for (x,mu,nu),c in s.items():
        for e,v in [((x,mu),1),((add(x,mu),nu),1),((add(x,nu),mu),-1),((x,nu),-1)]:a[e]+=c*v
    return {k:v for k,v in a.items() if v}

def fill_cycle(z):
    """Coordinate chain homotopy, separate from path generation."""
    assert not boundary1(z)
    z=z.copy(); surface=defaultdict(int)
    for axis in range(D):
        projected=defaultdict(int)
        for (x,mu),c in z.items():
            if mu==axis:continue
            xp=list(x);xp[axis]=0;xp=tuple(xp)
            projected[xp,mu]+=c
            for k in range(min(0,x[axis]),max(0,x[axis])):
                base=list(x);base[axis]=k;base=tuple(base)
                sign=(1 if x[axis]>0 else -1)*(1 if axis<mu else -1)
                surface[base,min(axis,mu),max(axis,mu)]+=c*sign
        z={e:c for e,c in projected.items() if c}
    assert not z
    return {k:v for k,v in surface.items() if v}

def tree_edges():
    out=set()
    for x in SITES:
        if x==ROOT:continue
        mu=max(i for i in range(D) if x[i])
        p=add(x,mu,-(1 if x[mu]>0 else -1))
        out.add(EID[(p if x[mu]>0 else x),mu])
    return out

TREE=tree_edges()
FREE=[i for i in range(len(EDGES)) if i not in TREE]
FREEID={v:i for i,v in enumerate(FREE)}
NFREE=len(FREE)

WORDS=[]
BADWORDS=[]
ORDERS=list(itertools.permutations(range(D)))
for mu in range(D):
    root2=add(ROOT,mu,L)
    for y in SITES:
        y2=add(y,mu,L)
        for order in ORDERS:
            a=word(ROOT,y,order)
            b=word(y,y2,(mu,))
            c=word(root2,y2,order)
            WORDS.append(a+b+reverse(c))
            BADWORDS.append(a+b)
NPATH=len(SITES)*len(ORDERS)

def locate(x):
    block=tuple((x[i]+HALF)//L for i in range(D))
    local=tuple(x[i]-L*block[i] for i in range(D))
    return block,local

def vec_for_word(w,k,free=False):
    out=defaultdict(complex)
    for x,mu,s in w:
        b,v=locate(x);j=EID[v,mu]
        if free:
            if j not in FREEID:continue
            j=FREEID[j]
        out[j]+=s*np.exp(1j*np.dot(k,b))
    return out

def matrix_words(words,k,free=False):
    rr=[];cc=[];vv=[]
    for r,w in enumerate(words):
        for c,v in vec_for_word(w,k,free).items():
            if abs(v)>1e-15:rr.append(r);cc.append(c);vv.append(v)
    return sparse.coo_matrix((vv,(rr,cc)),shape=(len(words),NFREE if free else len(EDGES))).tocsr()

def plaquette_word(x,mu,nu):
    return [(x,mu,1),(add(x,mu),nu,1),(add(x,nu),mu,-1),(x,nu,-1)]

PWORDS=[plaquette_word(x,mu,nu) for x in SITES for mu,nu in PAIRS]

def matrices(k):
    p=matrix_words(WORDS,k)
    q=np.vstack([np.asarray(p[mu*NPATH:(mu+1)*NPATH].sum(axis=0))[0]/NPATH for mu in range(D)])
    d=matrix_words(PWORDS,k)
    pf=p[:,FREE];qf=q[:,FREE];df=d[:,FREE]
    pathgram=(pf.conj().T@pf).toarray()/NPATH
    spread=pathgram-qf.conj().T@qf
    return d,q,df,qf,spread,p

def grad(k):
    g=np.zeros((len(EDGES),len(SITES)),complex)
    for i,(x,mu) in enumerate(EDGES):
        b,y=locate(add(x,mu));g[i,SID[y]]+=np.exp(1j*np.dot(k,b));g[i,SID[x]]-=1
    return g

def geometry():
    gate('tree_edge_and_free_coordinate_counts',len(TREE)==L**4-1 and NFREE==3*L**4+1,
         {'tree':len(TREE),'free':NFREE})
    gate('all_7776_actual_contours',len(WORDS)==4*24*L**4,len(WORDS))
    lengths=[];areas=[];badboundary=0
    surface_mutation=None
    for row,w in enumerate(WORDS):
        mu=row//NPATH
        z=chain(w)
        ends={ROOT:-1,add(ROOT,mu,L):1}
        if boundary1(z)!=ends:badboundary+=1
        direct=chain(word(ROOT,add(ROOT,mu,L),(mu,)))
        loop=chain_sum((1,z),(-1,direct));s=fill_cycle(loop)
        if boundary2(s)!=loop:badboundary+=1
        if s and surface_mutation is None:
            mut=s.copy();del mut[next(iter(mut))]
            surface_mutation=boundary2(mut)!=loop
        lengths.append(len(w));areas.append(sum(abs(v) for v in s.values()))
    gate('exact_contour_endpoints_and_integer_fillings',badboundary==0,badboundary)
    gate('declared_path_length',max(lengths)<=5*L-4,max(lengths))
    gate('uniform_30L2_contour_filling_bound',max(areas)<=30*L**2,max(areas))
    gate('removed_plaquette_control',surface_mutation)
    crossing_areas=[];internal_areas=[]
    for x,mu in EDGES:
        y=add(x,mu)
        bx,xx=locate(x);by,yy=locate(y)
        rooty=tuple(L*v for v in by)
        w=word(ROOT,x,range(D))+[(x,mu,1)]+reverse(word(rooty,y,range(D)))
        if by==ROOT:
            loop=chain(w)
            target=internal_areas
        else:
            loop=chain_sum((1,chain(w)),(-1,chain(word(ROOT,rooty,(mu,)))))
            target=crossing_areas
        s=fill_cycle(loop)
        if boundary2(s)!=loop:badboundary+=1
        target.append(sum(abs(v) for v in s.values()))
    gate('exact_internal_and_crossing_fillings',badboundary==0)
    gate('declared_internal_crossing_filling_bounds',max(internal_areas+crossing_areas)<=30*L**2,
         {'internal_max':max(internal_areas),'crossing_max':max(crossing_areas)})
    # Different algebraic description: fine scalar gradient and coarse evaluation.
    for label,k in [('zero',np.zeros(D)),('generic',np.array([.37,-.29,.61,.19]))]:
        d,q,df,qf,b,p=matrices(k);g=grad(k)
        expected=np.zeros((D,len(SITES)),complex)
        expected[:,SID[ROOT]]=np.exp(1j*k)-1
        gate('actual_Qd_root_covariance_'+label,np.max(abs(q@g-expected))<3e-13,float(np.max(abs(q@g-expected))))
        gate('curl_gradient_'+label,np.max(abs(d@g))<3e-14)
        minor=g[np.array(sorted(TREE))][:,[i for i in range(len(SITES)) if i!=SID[ROOT]]]
        gate('tree_gradient_unimodular_minor_'+label,abs(abs(linalg.det(minor))-1)<1e-12)
        if label=='generic':
            bad=matrix_words(BADWORDS,k)
            qb=np.vstack([np.asarray(bad[mu*NPATH:(mu+1)*NPATH].sum(axis=0))[0]/NPATH for mu in range(D)])
            gate('missing_endpoint_leg_control',np.max(abs(qb@g-expected))>1e-3,float(np.max(abs(qb@g-expected))))
    DETAILS['geometry']={'path_filling_max':max(areas),'path_length_max':max(lengths),'free_per_block':NFREE,'colour_density_SU2':3*NFREE,'curvature_density_SU2':3*6*L**4}

def spectral():
    moms=[('zero',np.zeros(D)),('generic',np.array([.37,-.29,.61,.19])),('long_1e-3',np.array([1e-3,0,0,0])),('long_1e-7',np.array([1e-7,0,0,0]))]
    records=[]
    BF=60*L**2;CF=4*L**3*(L+4)*BF**2;CQ=2*L**3
    for label,k in moms:
        d,q,df,qf,b,p=matrices(k)
        f=(df.conj().T@df).toarray();qgram=qf.conj().T@qf
        ev0=linalg.eigvalsh(f)
        expectednull=4 if label=='zero' else 1
        if label!='long_1e-7':
            gate('bare_closed_slice_null_modes_'+label,np.count_nonzero(abs(ev0)<1e-9)==expectednull,int(np.count_nonzero(abs(ev0)<1e-9)))
        else:
            gate('long_wave_bare_near_zero_diagnostic',np.max(abs(ev0[:4]))<1e-10,{'first_four':ev0[:4].tolist(),'rank_not_resolved':True})
        gate('spread_semidefinite_'+label,linalg.eigvalsh(b)[0]>-1e-12,float(linalg.eigvalsh(b)[0]))
        for kap in [.1,1.,10.]:
            h=f+kap*qgram;e=linalg.eigvalsh(h)
            lower=1/max(CF,CQ/kap)
            gate('local_coercivity_'+label+'_k'+str(kap),e[0]>=lower*(1-1e-8),{'min':float(e[0]),'proof_bound':lower})
            if label=='generic' and kap==1:
                full=(d.conj().T@d).toarray()+q.conj().T@q
                ef=linalg.eigvalsh(full)
                gate('unfixed_pinned_gauge_nullity',np.count_nonzero(abs(ef)<1e-9)==L**4-1,int(np.count_nonzero(abs(ef)<1e-9)))
            records.append({'momentum':label,'kappa':kap,'min':float(e[0]),'max':float(e[-1])})
        if label!='zero':
            a=np.array([(np.exp(1j*k[mu])-1) if x[mu]==HALF else 0 for x,mu in (EDGES[i] for i in FREE)])
            ratio=float(np.vdot(qf@a,qf@a).real/np.vdot(a,a).real)
            gate('root_gradient_long_wave_charge_'+label,abs(ratio-L**-3)<1e-12,ratio)
            gate('root_gradient_zero_curl_'+label,np.linalg.norm(df@a)<1e-12)
        else:
            for mu in range(D):
                full=np.array([float(nu==mu) for x,nu in EDGES])
                tree=np.array([float(nu==mu and x[nu]==HALF)*L for x,nu in (EDGES[i] for i in FREE)])
                gate('harmonic_full_normalization_'+str(mu),abs(np.vdot(q@full,q@full).real/np.vdot(full,full).real-L**-2)<1e-12)
                gate('harmonic_tree_normalization_'+str(mu),abs(np.vdot(qf@tree,qf@tree).real/np.vdot(tree,tree).real-L**-3)<1e-12)
                gate('harmonic_retained_and_charged_'+str(mu),np.linalg.norm(df@tree)<1e-12 and np.linalg.norm(qf@tree)>0)
    DETAILS['spectra']=records
    DETAILS['analytic_constants']={'L':L,'C_F':CF,'C_Q':CQ,'a_kappa1':1/max(CF,CQ)}

def qmul(a,b):
    out=np.empty(4)
    out[0]=a[0]*b[0]-np.dot(a[1:],b[1:])
    out[1:]=a[0]*b[1:]+b[0]*a[1:]-np.cross(a[1:],b[1:])
    return out

def qexp(a):
    v=np.asarray(a)/math.sqrt(2);r=np.linalg.norm(v)
    return np.r_[math.cos(r),v*(math.sin(r)/r if r else 1)]

def nonlinear_density(z,u,haar=True):
    un=np.tile(np.array([1.,0,0,0]),(len(EDGES),1))
    for j,e in enumerate(FREE):un[e]=qexp(z[j])
    def product(w):
        out=np.array([1.,0,0,0])
        for x,mu,s in w:
            _,v=locate(x);v=un[EID[v,mu]].copy()
            if s<0:v[1:]*=-1
            out=qmul(out,v)
        return out
    wilson=sum(1-product(w)[0] for w in PWORDS)
    contour=np.array([product(w) for w in WORDS]).reshape((D,NPATH,4)).mean(axis=1)
    val=u*wilson
    t=u
    for m in contour:
        r=np.linalg.norm(m);x=t*r
        val+= -t*m[0]+math.log(2*special.ive(1,x)/x)+x
    if haar:
        for a in z:
            r=np.linalg.norm(a)/math.sqrt(2)
            if r:val-=2*math.log(math.sin(r)/r)
    return val

def su2():
    d,q,df,qf,b,p=matrices(np.zeros(D));f=(df.T@df).toarray().real;qgram=(qf.T@qf).real;b=b.real
    rng=np.random.default_rng(1241)
    z=rng.normal(size=(NFREE,3));z/=np.linalg.norm(z)
    z-=qf.real.T@linalg.solve(qf.real@qf.real.T,qf.real@z)
    z/=np.linalg.norm(z)
    gate('nonabelian_probe_zero_coarse_linear_data',np.linalg.norm(qf@z)<1e-13)
    gate('nonabelian_probe_nonzero_spread',sum(z[:,a]@b@z[:,a] for a in range(3))>1e-3)
    runs=[]
    for u in [2.,10.,40.]:
        c=special.ive(2,u)/special.ive(1,u)
        den=integrate.quad(lambda th: math.sin(th)**2*math.exp(u*(math.cos(th)-1)),0,math.pi,epsabs=1e-13)[0]
        num=integrate.quad(lambda th: math.cos(th)*math.sin(th)**2*math.exp(u*(math.cos(th)-1)),0,math.pi,epsabs=1e-13)[0]
        gate('bessel_vs_Haar_mean_u'+str(u),abs(c-num/den)<3e-13,{'c':c,'haar':num/den})
        h=(u/2)*(f+qgram+(1-c)*b)
        exact=sum(z[:,a]@h@z[:,a] for a in range(3))
        spread=(u/2)*(1-c)*sum(z[:,a]@b@z[:,a] for a in range(3))
        step=3e-4
        y0=nonlinear_density(np.zeros_like(z),u,False)
        yp=nonlinear_density(step*z,u,False);ym=nonlinear_density(-step*z,u,False)
        finite=(yp+ym-2*y0)/step**2
        yp_h=nonlinear_density(step*z,u,True);ym_h=nonlinear_density(-step*z,u,True)
        finite_h=(yp_h+ym_h-2*y0)/step**2
        gate('actual_normalized_SU2_Hessian_u'+str(u),abs(finite-exact)<=2e-6*max(1,abs(exact)),{'finite':finite,'quadratic':exact})
        gate('Haar_Lebesgue_Hessian_u'+str(u),abs(finite_h-(exact+1/3))<=2e-6*max(1,abs(exact+1/3)),{'finite':finite_h,'quadratic':exact+1/3})
        gate('finite_u_spread_omission_control_u'+str(u),abs(finite-(exact-spread))>1e-4,spread)
        wrong=(u/2)*sum(z[:,a]@(f+qgram+b)@z[:,a] for a in range(3))
        gate('normalizer_omission_control_u'+str(u),abs(finite-wrong)>1e-4,float(wrong-finite))
        gate('Haar_omission_control_u'+str(u),abs(finite_h-exact)>.25,float(finite_h-exact))
        runs.append({'u':u,'c':float(c),'spread_Hessian':float(spread),'finite_error':float(finite-exact),'haar_error':float(finite_h-exact-1/3)})
    DETAILS['SU2']=runs

def periodic():
    T=2
    blocks=list(itertools.product(range(T),repeat=D));bid={b:i for i,b in enumerate(blocks)}
    hs=[];cs=[];ss=[];ds=[]
    for b in blocks:
        k=2*math.pi*np.array(b)/T
        d,q,df,qf,spread,p=matrices(k)
        h=(df.conj().T@df).toarray()+qf.conj().T@qf
        vals,vecs=linalg.eigh(h)
        cs.append((vecs/vals)@vecs.conj().T)
        ss.append((vecs/np.sqrt(vals))@vecs.conj().T)
        hs.append(h);ds.append(df.toarray())
    shape=(T,)*D+(NFREE,NFREE)
    ck=np.asarray(cs).reshape(shape);sk=np.asarray(ss).reshape(shape);hk=np.asarray(hs).reshape(shape)
    cr=np.fft.ifftn(ck,axes=tuple(range(D))).reshape((len(blocks),NFREE,NFREE))
    sr=np.fft.ifftn(sk,axes=tuple(range(D))).reshape((len(blocks),NFREE,NFREE))
    gate('periodic_real_inverse_and_square_root',max(np.max(abs(cr.imag)),np.max(abs(sr.imag)))<1e-12)
    # Direct sparse matrix: paths at every physical block, no Fourier phases.
    def global_matrix(words_per_block):
        rr=[];cc=[];vv=[]
        for ib,bl in enumerate(blocks):
            for iw,w in enumerate(words_per_block):
                row=ib*len(words_per_block)+iw;entries=defaultdict(float)
                for x,mu,s in w:
                    rel,loc=locate(x);j=EID[loc,mu]
                    if j not in FREEID:continue
                    dst=tuple((bl[i]+rel[i])%T for i in range(D))
                    entries[bid[dst]*NFREE+FREEID[j]]+=s
                for col,v in entries.items():
                    if v:rr.append(row);cc.append(col);vv.append(v)
        return sparse.coo_matrix((vv,(rr,cc)),shape=(len(blocks)*len(words_per_block),len(blocks)*NFREE)).tocsr()
    dfull=global_matrix(PWORDS)
    # Coarse Q independently aggregates direct path incidences at each block.
    pfull=global_matrix(WORDS)
    aggregate=sparse.kron(sparse.eye(len(blocks)*D),np.full((1,NPATH),1/NPATH),format='csr')
    qfull=aggregate@pfull
    hfull=(dfull.T@dfull+qfull.T@qfull).tocsc()
    seed=np.zeros(len(blocks)*NFREE);seed[17]=1
    exactcol=spsolve(hfull,seed)
    fftcol=cr[:,:,17].real.ravel()
    gate('direct_periodic_inverse_vs_Bloch_periodization',np.max(abs(exactcol-fftcol))<2e-10,float(np.max(abs(exactcol-fftcol))))
    rng=np.random.default_rng(19);v=rng.normal(size=(T,)*D+(NFREE,))
    vh=np.fft.fftn(v,axes=tuple(range(D)))
    via=np.fft.ifftn(np.einsum('...ij,...j->...i',hk,vh),axes=tuple(range(D))).real.ravel()
    gate('direct_full_operator_vs_Bloch_counting',np.max(abs(hfull@v.ravel()-via))<2e-11,float(np.max(abs(hfull@v.ravel()-via))))
    gate('inverse_square_root_covariance_identity',max(np.linalg.norm(s@s-c,np.inf) for s,c in zip(ss,cs))<2e-10)
    weights=np.array([math.exp(.01*sum(min(x,T-x) for x in b)) for b in blocks])
    row=np.einsum('x,xij->i',weights,abs(sr));col=np.einsum('x,xij->j',weights,abs(sr))
    fk=np.einsum('xij,xjk->xik',np.asarray(ds),np.asarray(ss)).reshape((T,)*D+(6*L**4,NFREE))
    fr=np.fft.ifftn(fk,axes=tuple(range(D))).reshape((len(blocks),6*L**4,NFREE))
    frow=np.einsum('x,xij->i',weights,abs(fr));fcol=np.einsum('x,xij->j',weights,abs(fr))
    gate('distinct_input_output_densities',fr.shape[1]==6*L**4 and fr.shape[2]==3*L**4+1)
    # Total absolute mass identity exposes the omitted-density mutation.
    lhs=float(frow.sum());rhs=float(fcol.sum())
    gate('complete_row_column_mass',abs(lhs-rhs)<1e-9*max(lhs,rhs),{'output_total':lhs,'input_total':rhs})
    wrong=float(frow.mean()*NFREE)
    gate('wrong_output_density_control',abs(wrong-rhs)>.1*rhs,{'wrong':wrong,'actual':rhs})
    # Removing p=0 changes the actual inverse on a constant-block datum.
    zero_removed=cr[0]-cs[0]/len(blocks)
    gate('discarded_zero_momentum_control',np.linalg.norm(zero_removed-cr[0])>1)
    DETAILS['periodic']={'T':T,'matrix_dimension_one_colour':len(seed),'square_root_weighted_row_max':float(row.max()),'square_root_weighted_column_max':float(col.max()),'curvature_square_root_row_max':float(frow.max()),'curvature_square_root_column_max':float(fcol.max()),'direct_inverse_error':float(np.max(abs(exactcol-fftcol)))}

def gaussian():
    # Independent radial 2D integral checks all normalization factors directly.
    h=np.array([[2.,.4],[.4,1.3]])
    e,v=linalg.eigh(h);s=(v/np.sqrt(e))@v.T;c=linalg.inv(h)
    gate('normalized_square_root_gaussian',np.linalg.norm(s@s-c)<1e-13)
    integral=integrate.quad(lambda th:1/(np.array([math.cos(th),math.sin(th)])@h@np.array([math.cos(th),math.sin(th)])),0,2*math.pi,epsabs=1e-12)[0]
    predicted=2*math.pi/math.sqrt(linalg.det(h))
    gate('Gaussian_determinant_direct_integral',abs(integral-predicted)<1e-11,{'integral':integral,'prediction':predicted})
    gate('omitted_determinant_control',abs(integral-2*math.pi)>.1)
    source=np.array([[.15,.03],[.03,.08]])
    ratio=math.sqrt(linalg.det(h)/linalg.det(h+source))
    integral2=integrate.quad(lambda th:1/(np.array([math.cos(th),math.sin(th)])@(h+source)@np.array([math.cos(th),math.sin(th)])),0,2*math.pi,epsabs=1e-12)[0]
    gate('source_Gaussian_normalization',abs(integral2/integral-ratio)<1e-12)
    gate('colour_trace_factor_control',abs(ratio**3-ratio)>.01,{'one_colour':ratio,'SU2':ratio**3})
    BF=60*L**2;a=1/(4*L**3*(L+4)*BF**2);b=24+24*(5*L)**2+4/6
    m=.5*math.log1p(a/(2*b))
    gate('positive_declared_weighted_resolvent_rate',m>0 and b*math.expm1(2*m)<=a/2*(1+1e-14),{'a':a,'b':b,'m':m})
    # Periodized elementary kernel: a separate density/image check.
    eta=.7;T=2
    exact=math.cosh(eta/2)/math.sinh(eta/2)
    image_sum=sum(math.exp(-eta*abs(x+T*k)) for x in range(T) for k in range(-70,71))
    noimages=sum(math.exp(-eta*min(x,T-x)) for x in range(T))
    gate('periodic_images_unfold',abs(image_sum-exact)<1e-13)
    gate('omitted_periodic_images_control',abs(noimages-exact)>.1,{'actual':exact,'omitted':noimages})
    DETAILS['gaussian']={'two_dimensional_integral':integral,'source_ratio':ratio,'a':a,'b':b,'weighted_rate':m}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=['geometry','spectral','su2','periodic','gaussian','all'],default='all');args=parser.parse_args()
    start=time.monotonic()
    funcs={'geometry':geometry,'spectral':spectral,'su2':su2,'periodic':periodic,'gaussian':gaussian}
    try:
        for name,fn in funcs.items():
            if args.mode in (name,'all'):fn()
    except Exception as ex:
        import traceback
        traceback.print_exc()
        gate('execution_completed',False,repr(ex))
    out={'scope':'finite author diagnostics; all-volume theorem requires the written local proof','mode':args.mode,'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'elapsed_seconds':time.monotonic()-start,'passed':sum(x['pass'] for x in TESTS),'total':len(TESTS),'all_pass':all(x['pass'] for x in TESTS),'checks':TESTS,'details':DETAILS,'external_scientific_inputs_read':[],'integrity_reads':[],'full_existence_established':False,'physical_continuum_mass_gap_established':False}
    print(json.dumps(out,indent=2,allow_nan=False))
    return 0 if out['all_pass'] else 1
if __name__=='__main__':sys.exit(main())
