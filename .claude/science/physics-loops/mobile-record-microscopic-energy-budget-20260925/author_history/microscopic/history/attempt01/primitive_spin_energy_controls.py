#!/usr/bin/env python3
"""Root primitive finite-spin controls; no author/parent helper imports.

Full Gauss spaces on even cycles, every charge and electric word in the
specified spin box. Independent of the analytic all-graph argument below;
numerical arithmetic except the S=1 coefficient identities.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib,json,time
import numpy as np
from scipy import sparse as sp

HERE=Path(__file__).resolve().parent
TIC=time.perf_counter()

def cycle_space(length,spin):
    A=tuple(range(0,length,2));B=tuple(range(1,length,2))
    edges=tuple((i,(i+1)%length) if i%2==0 else ((i+1)%length,i) for i in range(length))
    neighbours={a:tuple((k,b) for k,(aa,b) in enumerate(edges) if aa==a) for a in A}
    words=[]
    for q in product((-1,0,1),repeat=length):
        if sum(q)!=len(A):continue
        sums=[];v=0
        for i,x in enumerate(q):v+=x-int(i in A);sums.append(v)
        for winding in range(max(-spin-x for x in sums),min(spin-x for x in sums)+1):
            E=tuple((1 if i%2==0 else -1)*(winding+x) for i,x in enumerate(sums))
            words.append((q,E))
    words=tuple(words);index={x:i for i,x in enumerate(words)}
    for q,E in words:
        div=[0]*length
        for (a,b),e in zip(edges,E):div[a]+=e;div[b]-=e
        assert div==[q[i]-int(i in A) for i in range(length)]
    return A,B,edges,neighbours,words,index

def outgoing(state,a,neighbours,spin=None):
    q,E=state
    if not q[a]:return []
    rows=[]
    for k,b in neighbours[a]:
        if q[b]:continue
        s=q[a];r=list(q);f=list(E);r[a]=0;r[b]=s;f[k]-=s
        if spin is None:w=1.0
        elif abs(f[k])>spin:continue
        else:w=np.sqrt(max(0.,1-E[k]*(E[k]-s)/(spin*(spin+1))))
        if w:rows.append(((tuple(r),tuple(f)),w))
    return rows

def create(state,a,k,b,sigma,spin=None):
    q,E=state
    if q[a] or q[b]:return None
    f=list(E);r=list(q);r[a]=sigma;r[b]=-sigma;f[k]+=sigma
    if spin is None:w=1.0
    elif abs(f[k])>spin:return None
    else:w=np.sqrt(max(0.,1-E[k]*(E[k]+sigma)/(spin*(spin+1))))
    return ((tuple(r),tuple(f)),w) if w else None

def sparse_paths(words,index,fn):
    rows=[];cols=[];data=[]
    for i,state in enumerate(words):
        for dest,w in fn(state):rows.append(index[dest]);cols.append(i);data.append(w)
    return sp.csr_matrix((data,(rows,cols)),shape=(len(words),len(words)))

def rectangular(paths,cols):
    outputs=sorted(set(state for column in paths for state in column))
    idx={x:i for i,x in enumerate(outputs)};r=[];c=[];d=[]
    for i,column in enumerate(paths):
        for state,w in column.items():r.append(idx[state]);c.append(i);d.append(w)
    return sp.csr_matrix((d,(r,c)),shape=(len(outputs),cols))

def dense_norm(mat):
    x=mat.toarray() if sp.issparse(mat) else mat
    return float(np.max(np.abs(x))) if x.size else 0.

def build(length,spin):
    A,B,edges,nb,words,idx=cycle_space(length,spin);C=spin*(spin+1);dim=len(words)
    W=np.array([sum(q[a]==0 for a in A) for q,E in words])
    P=np.flatnonzero(W==0);one=np.flatnonzero(W==1);two=np.flatnonzero(W==2)
    Fs={a:sparse_paths(words,idx,lambda x,a=a:outgoing(x,a,nb,spin)) for a in A}
    Ds={a:np.array([sum(E[k]*(E[k]-q[a]) for k,b in nb[a] if q[a] and not q[b]) for q,E in words]) for a in A}
    D=sum(Ds.values());assert min(D)>=0
    T=-sum((F+F.T for F in Fs.values()),sp.csr_matrix((dim,dim)))
    compensation=sp.csr_matrix((dim,dim));overlap=[]
    local={a:[c for c in A if c==a or set(b for k,b in nb[a])&set(b for k,b in nb[c])] for a in A}
    for a in A:
        gate=np.array([all(q[c] for c in local[a] if c!=a) for q,E in words],dtype=float)
        compensation+=(Fs[a].T@Fs[a]+sp.diags(Ds[a]/C))@sp.diags(gate)
    assert dense_norm(compensation-compensation.T)<1e-12
    As=T[one][:,P];Z=T[two][:,one]@As;M=As.T@As;C0=compensation[P][:,P];C1=compensation[one][:,one]
    H4=M@M-(M@C0+C0@M)/2+As.T@C1@As-Z.T@Z/2
    Q=sp.csr_matrix((len(P),len(P)));QR=Q.copy();correction=Q.copy()
    pwords=tuple(words[i] for i in P)
    for a in A:
        Ma=(Fs[a].T@Fs[a])[P][:,P]
        for c in local[a]:
            Dc=sp.diags(Ds[c][P]);correction-=(Ma@Dc+Dc@Ma)/(2*C)
        for c in A:
            if c<=a or c not in local[a]:continue
            overlap.append((a,c));S=(Fs[c]@Fs[a])[:,P];Q+=S.T@S
            paths=[]
            for word in pwords:
                d=Counter()
                for first,v in outgoing(word,a,nb):
                    for second,w in outgoing(first,c,nb):d[second]+=v*w
                paths.append(d)
            SR=rectangular(paths,len(P));QR+=SR.T@SR
    claimed=-2*Q+correction
    residual=dense_norm(H4-claimed);second=dense_norm(C0-M-sp.diags(D[P]/C))
    assert residual<3e-12 and second<3e-14,(length,spin,residual,second)
    if spin==1:assert residual==0 and second==0
    # Complete original resolved and unnormalized coherent losses.
    jumps=[];Bj=[];GR=sp.csr_matrix((len(P),len(P)))
    resolved=sp.csr_matrix((dim,dim));coherent=resolved.copy()
    for a in A:
        for k,b in nb[a]:
            pair=[]
            for sigma in (-1,1):
                def births(x,a=a,k=k,b=b,sigma=sigma):
                    z=create(x,a,k,b,sigma,spin)
                    return [] if z is None else [z]
                j=sparse_paths(words,idx,births);jumps.append(j);pair.append(j);resolved+=j.T@j
                bs=(j@Fs[a])[:,P];Bj.append(bs)
                paths=[]
                for word in pwords:
                    d=Counter()
                    for mid,v in outgoing(word,a,nb):
                        z=create(mid,a,k,b,sigma)
                        if z is not None:d[z[0]]+=v*z[1]
                    paths.append(d)
                BR=rectangular(paths,len(P));GR+=BR.T@BR
            js=pair[0]+pair[1];coherent+=js.T@js
    assert dense_norm(resolved-coherent)==0
    GS=sum((x.T@x for x in Bj),sp.csr_matrix((len(P),len(P))))
    # Every outgoing spin/rotor path has nonincreasing full vacancy-gated D.
    def energy(word):
        q,E=word
        return sum(E[k]*(E[k]-q[a]) for k,(a,b) in enumerate(edges) if q[a] and not q[b])
    path_count=0;boundary=0
    for word in words:
        for a in A:
            for dest,w in outgoing(word,a,nb):
                assert energy(dest)<=energy(word);path_count+=1
                boundary+=int(any(abs(e)>spin for e in dest[1]))
    row={'cycle_length':length,'spin':spin,'full_dimension':dim,'P_dimension':len(P),'one_hole_dimension':len(one),'two_hole_dimension':len(two),'overlapping_A_pairs':len(overlap),'ordered_local_pairs':sum(map(len,local.values())),'distant_ordered_A_pairs':len(A)**2-sum(map(len,local.values())),'coefficient_identity_max_abs':residual,'second_order_identity_max_abs':second,'S1_exact_rational_identity':spin==1,'all_resolved_coherent_losses_equal':True,'full_outward_D_monotonic_paths':path_count,'rotor_boundary_paths_retained':boundary,'correction_max_abs':dense_norm(correction),'all_full_Gauss_words_enumerated':True}
    return row,dict(A=A,words=words,P=P,W=W,T=T,C=compensation,H4=H4,D=D[P],QR=QR,GR=GR,GS=GS,jumps=jumps,Bj=Bj)

identity=[]
for length,spins in [(4,(1,2,4)),(8,(1,2,3))]:
    for spin in spins:
        row,data=build(length,spin);identity.append(row)

spectral=[]
for spin in (1,2,4,8):
    row,d=build(4,spin);C=spin*(spin+1);delta=1.;K=100.;epsilon=np.sqrt(delta/(K*C));P=d['P'];npdim=len(P)
    small=sp.diags(d['W'])+epsilon*d['T']+epsilon**2*d['C']
    H=(delta*epsilon**-4*small).toarray()
    val,vec=np.linalg.eigh(small.toarray());low=np.flatnonzero(val<.5)
    assert len(low)==npdim and np.min(val[npdim:])>.5
    V=vec[:,low];cross=V[P,:];q=V@cross.T;G=cross@cross.T
    gv,gu=np.linalg.eigh(G);U=q@(gu*(gv**-.5))@gu.T
    assert np.max(np.abs(U.T@U-np.eye(npdim)))<1e-12
    target=sp.diags(K*d['D'])+delta*d['H4'];lowH=U.T@H@U
    remainder=float(np.linalg.norm(lowH-target.toarray(),2))
    jump_error=max(float(np.linalg.norm(j@U/epsilon-b.toarray(),2)) for j,b in zip(d['jumps'],d['Bj']))
    ground=V[:,0];phi=U.T@ground
    fast_energy=float(val[0]*delta*epsilon**-4)
    rotor_energy=float(K*np.dot(d['D'],phi**2)-2*delta*np.dot(phi,d['QR']@phi))
    fast_rate=sum(float(np.linalg.norm(j@ground)**2/epsilon**2) for j in d['jumps'])
    rotor_rate=float(np.dot(phi,d['GR']@phi))
    target_energy=float(np.dot(phi,target@phi));Dmean=float(np.dot(d['D'],phi**2))
    residual=float(np.linalg.norm(H@ground-fast_energy*ground))
    q0=tuple(int(i%2==0) for i in range(4));i=d['words'].index((q0,(0,)*4))
    bare_energy=float(H[i,i]);bare_rate=sum(float(np.linalg.norm(j[:,i].toarray())**2/epsilon**2) for j in d['jumps'])
    assert bare_rate==0 and abs(bare_energy-4*K*C)<1e-8
    spectral.append({'spin':spin,'epsilon':epsilon,'full_dimension':len(d['W']),'low_cluster_dimension':npdim,'full_ground_energy':fast_energy,'ground_residual_norm':residual,'ground_D_in_rotated_P':Dmean,'rotated_target_energy':target_energy,'embedded_rotor_energy':rotor_energy,'full_ground_intensity':fast_rate,'embedded_rotor_intensity':rotor_rate,'low_block_remainder_norm':remainder,'remainder_over_epsilon_squared':remainder/epsilon**2,'microscopic_jump_amplitude_error':jump_error,'jump_error_over_epsilon':jump_error/epsilon,'bare_P_energy':bare_energy,'bare_P_intensity':bare_rate,'scope':'Small cycle fixed K=100,delta=kappa=1; tests the transfer mechanism only, not the degree-six ground/formation bound or physical parameters.'})

integer=[]
for q in (-1,1):
    for sigma in (-1,1):
        values=[2*e*(e-q)+2-e*(e+sigma) for e in range(-100,101)]
        assert min(values)>=0
        integer.append({'q':q,'sigma':sigma,'minimum_over_minus100_to100':min(values),'scope':'Analytic integer quadratic inequality supplies all-e proof; finite list is only a control.'})
result={'scope':'Personal primitive full-space finite-spin controls; no empirical fit, independent review or degree-six spectral simulation. Floating matrix results are not interval enclosures.','identity_rows':identity,'spectral_rows':spectral,'integer_rows':integer,'all_assertions_passed':True,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.perf_counter()-TIC}
text=json.dumps(result,indent=2,allow_nan=False)+'\n'
(HERE/'SPIN_ENERGY_CONTROL_RESULTS.json').write_text(text);print(text,end='')
