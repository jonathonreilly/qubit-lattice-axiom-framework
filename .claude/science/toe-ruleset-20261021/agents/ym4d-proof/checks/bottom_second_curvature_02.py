#!/usr/bin/env python3
"""Actual L=3 paired-S4' SU(2) one-step stationary Bloch second curvature.

No predecessor helper import. Complexification is bilinear, never Hermitian.
The quadratic response below is the st coefficient (twice polarization).
"""
import itertools,json,time
import numpy as np
start=time.time();ell=3;V=ell**4;E=4*V;kappa=.7
coords=np.array(list(itertools.product(range(ell),repeat=4)))
forms=[list(itertools.combinations(range(4),r)) for r in range(5)]
root=np.ones(4,dtype=int);rootid=np.ravel_multi_index(tuple(root),(ell,)*4)
keep=[i for i in range(V) if i!=rootid]
checks=[];records=[]
def chk(name,x,scale=1.,positive=False):
    val=float(np.max(np.abs(x)));threshold=1e-6 if positive else 1e-9*max(1.,float(scale))
    checks.append(dict(name=name,value=val,threshold=threshold,passed=val>threshold if positive else val<=threshold))
def edge(x,mu,sg=1):
    y=np.array(x,dtype=int).copy()
    if sg<0:y[mu]-=1
    return (mu*V+np.ravel_multi_index(tuple(y%ell),(ell,)*4),sg,y//ell)
def straight(start,end,order):
    x=np.array(start,dtype=int).copy();ans=[]
    for mu in order:
        while x[mu]!=end[mu]:
            sg=1 if end[mu]>x[mu] else -1
            ans.append(edge(x,mu,sg));x[mu]+=sg
    return ans
def pack(paths,labels,weights):
    length=max(map(len,paths));idx=np.full((len(paths),length),E,dtype=int)
    signs=np.zeros_like(idx);shifts=np.zeros(idx.shape+(4,),dtype=int)
    for i,path in enumerate(paths):
        for j,(e,s,c) in enumerate(path):idx[i,j]=e;signs[i,j]=s;shifts[i,j]=c
    return dict(idx=idx,sign=signs,shift=shifts,label=np.array(labels),weight=np.array(weights),length=length)
pp=[];plabel=[]
for ori,(mu,nu) in enumerate(forms[2]):
    for u,x in enumerate(coords):
        a=x.copy();a[mu]+=1;b=x.copy();b[nu]+=1
        pp.append([edge(x,mu),edge(a,nu),edge(b+np.eye(4,dtype=int)[mu],mu,-1),edge(b,nu,-1)])
        plabel.append(ori*V+u)
plaquettes=pack(pp,plabel,[1.]*len(pp))
sp=[];slabel=[]
for mu in range(4):
    er=np.eye(4,dtype=int)[mu];endroot=root+ell*er
    for perm in itertools.permutations(range(4)):
        for y in coords:
            left=straight(root,y,perm)
            middle=straight(y,y+ell*er,[mu])
            right=straight(endroot,y+ell*er,perm)
            rightinv=[(e,-s,c) for e,s,c in reversed(right)]
            sp.append(left+middle+rightinv);slabel.append(mu)
soft=pack(sp,slabel,[1./(24*ell**4)]*len(sp))
def phases(pat,p):return pat['sign']*np.exp(1j*np.einsum('...d,d->...',pat['shift'],p))
def values(pat,p,a):
    return np.vstack([a,np.zeros((1,3),dtype=complex)])[pat['idx']]*phases(pat,p)[...,None]
def crossB(pat,p,a,q,b):
    X=values(pat,p,a);Y=values(pat,q,b)
    px=np.cumsum(X,axis=1)-X;py=np.cumsum(Y,axis=1)-Y
    terms=np.sum(np.cross(px,Y)+np.cross(py,X),axis=1)*pat['weight'][:,None]
    out=np.zeros((int(pat['label'].max())+1,3),dtype=complex)
    np.add.at(out,pat['label'],terms);return out
def b_adj(pat,p,a,other,w):
    """Sum other dot B_cross(a,w), differentiate analytically in hidden w."""
    X=values(pat,p,a);prefix=np.cumsum(X,axis=1)-X
    suffix=np.sum(X,axis=1)[:,None,:]-prefix-X
    g=np.cross(other[pat['label']][:,None,:],prefix-suffix)
    g*=phases(pat,w)[...,None]*pat['weight'][:,None,None]
    out=np.zeros((E+1,3),dtype=complex)
    np.add.at(out,pat['idx'].ravel(),g.reshape(-1,3));return out[:E]
def cochain(r,p):
    M=np.zeros((len(forms[r+1])*V,len(forms[r])*V),dtype=complex)
    for out,axes in enumerate(forms[r+1]):
        for i,mu in enumerate(axes):
            inp=forms[r].index(tuple(x for x in axes if x!=mu));sg=(-1)**i
            for u,x in enumerate(coords):
                y=x.copy();y[mu]+=1;v=np.ravel_multi_index(tuple(y%ell),(ell,)*4)
                M[out*V+u,inp*V+v]+=sg*(np.exp(1j*p[mu]) if y[mu]==ell else 1)
                M[out*V+u,inp*V+u]-=sg
    return M
def Qmat(p,mutate_normalization=False):
    M=np.zeros((4,E+1),dtype=complex)
    vals=phases(soft,p)*soft['weight'][:,None]
    np.add.at(M,(np.broadcast_to(soft['label'][:,None],soft['idx'].shape).ravel(),soft['idx'].ravel()),vals.ravel())
    return M[:,:E]*(24 if mutate_normalization else 1)
cache={}
def linear(p):
    p=np.asarray(p,dtype=complex);key=tuple(p)
    if key in cache:return cache[key]
    ds=[cochain(r,p) for r in range(3)];dm=[cochain(r,-p) for r in range(3)]
    Q=Qmat(p);Qm=Qmat(-p);G=ds[0][:,keep];Gm=dm[0][:,keep]
    H=dm[1].T@ds[1]+kappa*Qm.T@Q+G@Gm.T
    Z=np.linalg.solve(H,kappa*Qm.T)
    dat=dict(p=p,d=ds,dm=dm,Q=Q,Qm=Qm,G=G,Gm=Gm,H=H,Z=Z)
    cache[key]=dat;return dat
vp=np.zeros((4,3),complex);vq=vp.copy()
vp[:,0]=[.8,-.4,.3,.6];vq[:,1]=[.2,.7,-.5,.4]
def low(a,k):
    A=a.reshape(-1,V,3)
    return np.mean(A*np.exp(-1j*(coords@k)/ell)[None,:,None],axis=1)
def source(p,q,direct=True):
    k=p+q;P=linear(p);Q=linear(q);K=linear(k);Km=linear(-k)
    a=P['Z']@vp;b=Q['Z']@vq
    fp=P['d'][1]@a;fq=Q['d'][1]@b;rp=vp-P['Q']@a;rq=vq-Q['Q']@b
    B=crossB(plaquettes,p,a,q,b);Bs=crossB(soft,p,a,q,b)
    PW=b_adj(plaquettes,p,a,fq,-k)+b_adj(plaquettes,q,b,fp,-k)
    PS=b_adj(soft,p,a,rq,-k)+b_adj(soft,q,b,rp,-k)
    S=K['dm'][1].T@B+PW+kappa*K['Qm'].T@Bs-kappa*PS
    # Top cubic derivative from THREE LINEAR STATIONARY LIFTS, before w2.
    current=Km['Z'].T@S-kappa*Bs
    Euler=K['Qm'].T@current-PW+kappa*PS
    Bianchi=K['d'][2]@B
    N=K['d'][1]@Euler+K['dm'][2].T@Bianchi
    ans=dict(k=k,a=a,b=b,fp=fp,fq=fq,rp=rp,rq=rq,B=B,Bs=Bs,PW=PW,PS=PS,S=S,current=current,Euler=Euler,Bianchi=Bianchi,N=N,Nlow=low(N,k))
    if direct:
        w=-np.linalg.solve(K['H'],S);g=K['d'][1]@w;F=g+B
        ans.update(w=w,g=g,F=F,Flow=low(F,k))
    return ans

cases=[('real',np.array([.53,-.31,.43,.22],complex),np.array([-.14,.27,.19,-.09],complex)),
       ('complex',np.array([.31+.007j,-.22+.003j,.17-.002j,.29+.001j]),np.array([-.13+.004j,.26-.006j,.08+.003j,-.11+.002j])),
       ('constant',np.zeros(4,complex),np.zeros(4,complex))]
wcone=np.array([.02,.02j,0,0],complex);kcone=2*ell*np.arcsin(wcone/(2*ell))
cases.append(('complex_zero',cases[1][1],kcone-cases[1][1]))
for name,p,q in cases:
    t=source(p,q);k=t['k'];P=linear(p);K=linear(k)
    chk(name+'_Qd_root',P['Q']@P['d'][0]-np.outer(np.exp(1j*p)-1,np.eye(V)[rootid]))
    chk(name+'_linear_gauge',P['Gm'].T@(P['Z']@vp))
    chk(name+'_linear_stationary',P['H']@P['Z']-kappa*P['Qm'].T)
    chk(name+'_dd_zero',K['d'][2]@K['d'][1])
    chk(name+'_cubic_source_gauge',K['Gm'].T@t['S'])
    chk(name+'_second_stationary',K['H']@t['w']+t['S'])
    chk(name+'_current_from_cubic',t['current']-kappa*(-K['Q']@t['w']-t['Bs']))
    chk(name+'_Euler',K['dm'][1].T@t['F']-t['Euler'])
    chk(name+'_Bianchi',K['d'][2]@t['F']-t['Bianchi'])
    phi=4*np.sum(np.sin(k/(2*ell))**2)
    chk(name+'_zero_alias_Hodge',t['Nlow']-phi*t['Flow'])
    rec=dict(name=name,Nlow_norm=float(np.max(np.abs(t['Nlow']))),Flow_norm=float(np.max(np.abs(t['Flow']))),Bianchi_norm=float(np.max(np.abs(t['Bianchi']))),current_norm=float(np.max(np.abs(t['current']))),soft_B_norm=float(np.max(np.abs(t['Bs']))))
    if name=='complex_zero':
        chk('complex_null_phi',phi);chk('actual_source_complex_divisibility',t['Nlow'])
        mutant=low(K['d'][1]@(t['Euler']+t['PW'])+K['dm'][2].T@t['Bianchi'],k)
        chk('reject_missing_Wilson_DB_term',mutant,positive=True)
        mutant=low(K['d'][1]@t['Euler'],k)
        chk('reject_missing_Bianchi_source',mutant,positive=True)
        mutant=low(K['d'][1]@(t['Euler']-kappa*t['PS'])+K['dm'][2].T@t['Bianchi'],k)
        chk('reject_missing_soft_DB_term',mutant,positive=True)
        rec['mutation_missing_soft_DB']=float(np.max(np.abs(mutant)))
    if name=='constant':
        chk('constant_paired_mean_B_zero',t['Bs'])
        chk('constant_harmonic_retained',t['Flow']-low(t['B'],k))
        chk('constant_g_zero_harmonic',low(t['g'],k))
        chk('constant_noncommuting_harmonic_is_nonzero',t['Flow'],positive=True)
    records.append(rec)

# Actual source Cauchy division: preserve an independent input momentum theta.
# Circle avoids all roots; values use current from three linear lifts only.
cauchy=[];rho=.06;M=48
for name,wp,theta in [
    ('harmonic',np.zeros(4,complex),np.zeros(4,complex)),
    ('two_input_complex_null',np.array([.005j,.005,0,0],complex),cases[1][1])]:
    kt=2*ell*np.arcsin(wp/(2*ell));target=source(theta,kt-theta)
    acc=np.zeros((6,3),complex);maxN=0.
    for j in range(M):
        z=rho*np.exp(2j*np.pi*j/M);wc=wp.copy();wc[0]=z
        kc=2*ell*np.arcsin(wc/(2*ell));s=source(theta,kc-theta,direct=False)
        NN=ell**4*s['Nlow'];den=z*z+np.sum(wp[1:]**2)
        acc+=NN/den*z/(z-wp[0])/M;maxN=max(maxN,float(np.max(np.abs(NN))))
    value=acc/ell**2
    chk(name+'_Cauchy_actual_stationary_match',value-target['Flow'])
    if name=='harmonic':chk('Cauchy_recovers_retained_B_harmonic',value-low(target['B'],np.zeros(4)))
    cauchy.append(dict(name=name,rho=rho,nodes=M,error=float(np.max(np.abs(value-target['Flow']))),source_numerator_sup=maxN,quotient_norm=float(np.max(np.abs(acc))),direct_curvature_norm=float(np.max(np.abs(target['Flow'])))))

# Independent local Bianchi factorization: exact gradient component has zero
# quadratic defect; measured remainder is at least bilinear in a and da.
rng=np.random.default_rng(20261029)
lam=rng.normal(size=(V,3));p=np.zeros(4,complex);D=linear(p)['d']
grad=D[0]@lam
Bg=.5*crossB(plaquettes,p,grad,p,grad)
chk('quadratic_Bianchi_of_exact_gradient',D[2]@Bg)
c=rng.normal(size=(E,3));mixed=crossB(plaquettes,p,grad,p,c)
for eps in [1.,.1,.01]:
    a=grad+eps*c
    defect=D[2]@(.5*crossB(plaquettes,p,a,p,a))
    expected=eps*(D[2]@mixed)+eps**2*(D[2]@(.5*crossB(plaquettes,p,c,p,c)))
    chk('local_Bianchi_exact_quadratic_factorization',defect-expected,scale=np.max(np.abs(defect)))

# Normalization/gauge mutations are checked against the actual S4' map.
p=cases[1][1];P=linear(p)
chk('reject_omitted_24_normalization',Qmat(p,True)@P['d'][0]-np.outer(np.exp(1j*p)-1,np.eye(V)[rootid]),positive=True)
chk('reject_complex_Hermitian_transpose',P['H']-linear(-p)['H'].conj().T,positive=True)
chk('analytic_negative_momentum_transpose',P['H']-linear(-p)['H'].T)
shift=p.copy();shift[0]+=2*np.pi
chk('actual_Q_periodic_face',Qmat(shift)-P['Q'])
chk('actual_linear_lift_periodic_face',linear(shift)['Z']-P['Z'])
out=dict(scope="actual d4 L3 paired-S4' SU2 one-step source, st coefficient, counting inner products",geometry=dict(ell=ell,sites=V,hidden_links=E,root=root.tolist(),gauge_scalar_dimension=len(keep),plaquettes=len(pp),soft_paths=len(sp),per_coarse_link=24*ell**4,max_soft_path_length=soft['length'],kappa=kappa),checks=checks,passed=sum(c['passed'] for c in checks),total=len(checks),records=records,cauchy=cauchy,elapsed_seconds=time.time()-start)
print(json.dumps(out,indent=2,allow_nan=False));raise SystemExit(0 if all(c['passed'] for c in checks) else 1)
