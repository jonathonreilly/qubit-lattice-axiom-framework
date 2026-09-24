#!/usr/bin/env python3
"""Finite controls; copied root definitions are explicit reuse, not independence.
The analytic proof, not these fixed-S/toy samples, supplies limiting statements.
"""
AUDIT_TIMEOUT_SEC=300
AUDIT_INPUT_PATHS=('docs/NO_FIRST_BIRTH_CUBE_ENERGY_AND_APPARATUS_COHERENCE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ACTUAL_CUBE_BIRTH_APPARATUS_COHERENCE_AND_ENERGY_RANGE_BOUNDED_THEOREM_NOTE_2026-09-24.md')
from pathlib import Path
from collections import defaultdict
import hashlib,itertools,json,math,time
import numpy as np
from scipy.sparse import diags,eye,csr_matrix
from scipy.sparse.linalg import eigsh,splu
HERE=Path(__file__).resolve().parents[1]/'outputs/no_first_birth_cube_energy_20260924'
A=(0,3,5,6);B=(1,2,4,7)
EDGES=tuple((a,b) for a in A for b in B if a^b in (1,2,4))

def complete_spin_one():
    inc=np.zeros((12,8),np.int8)
    for i,(a,b) in enumerate(EDGES):inc[i,a]=1;inc[i,b]=-1
    allE=np.indices((3,)*12,dtype=np.int8).reshape(12,-1).T-1
    allq=allE@inc+np.array([int(i in A) for i in range(8)],np.int8)
    valid=(np.abs(allq)<=1).all(axis=1);number=(allq*allq).sum(axis=1)
    models={}
    for N in (4,6,8):
        select=valid&(number==N);fields=allE[select].copy();charges=allq[select].copy()
        index={tuple(int(x) for x in E):i for i,E in enumerate(fields)};n=len(fields)
        W=(charges[:,A]==0).sum(axis=1)
        rows=[];cols=[];delta=np.zeros(n);loss=np.zeros(n)
        for i,(q,E) in enumerate(zip(charges,fields)):
            for e,(a,b) in enumerate(EDGES):
                if q[a]!=0 and q[b]==0:
                    weight=1-int(E[e])*(int(E[e])-int(q[a]))/2
                    assert weight in (0,1)
                    if weight:
                        ee=E.copy();ee[e]-=q[a];dest=index[tuple(int(x) for x in ee)]
                        rows.append(dest);cols.append(i)
                    if W[i]==0:delta[i]+=1-weight
                if q[a]==q[b]==0:loss[i]+=2-int(E[e])**2
        F=csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(n,n))
        P=diags((W==0).astype(float));C=P@(F.T@F)@P+diags(delta)
        if N==8:assert F.nnz==C.nnz==0 and np.max(W)==0 and np.max(loss)==0
        if N==6:assert np.all(loss[W!=1]==0)
        models[N]={'E':fields,'q':charges,'index':index,'W':W,'F':F,'C':C,'loss':loss}
    return models

def riesz_action(h,x,grade,n):
    """Trapezoidal contour integral; an approximate projector, never exact evidence."""
    result=np.zeros_like(x,dtype=complex)
    ident=eye(h.shape[0],format='csc',dtype=complex)
    for k in range(n):
        dz=.35*np.exp(2j*np.pi*(k+.5)/n)
        result+=dz*splu((grade+dz)*ident-h).solve(np.asarray(x,dtype=complex))/n
    return result

def canonical_preparation(m4,epsilon):
    h=diags(m4['W'],dtype=float)-epsilon*(m4['F']+m4['F'].T)+epsilon**2*m4['C']
    p=np.flatnonzero(m4['W']==0)
    seed=np.random.default_rng(92405).normal(size=h.shape[0])
    values,V=eigsh(h,k=len(p),sigma=-.01,which='LM',tol=2e-12,v0=seed)
    residual=float(np.linalg.norm(h@V-V*values));orth=float(np.linalg.norm(V.T@V-np.eye(len(p))))
    assert max(abs(values))<.2 and residual<2e-10 and orth<2e-10
    VP=V[p,:];gram=VP@VP.T;w,q=np.linalg.eigh(gram);assert w.min()>.6
    j=int(np.flatnonzero(p==m4['index'][(0,)*12])[0]);unit=np.eye(len(p))[:,j]
    v=V@(VP.T@((q/np.sqrt(w))@q.T@unit))
    assert abs(np.vdot(v,v).real-1)<2e-10
    return v,{'eigen_residual':residual,'orthogonality_error':orth,'minimum_overlap_eigenvalue':float(w.min())}

def geometry_and_words():
    rows=[]
    for occupied in itertools.combinations(range(8),4):
        occ=set(occupied);r=sum(a not in occ for a in A)
        vacant_edges=sum(a not in occ and b not in occ for a,b in EDGES)
        if r in (1,2,3):assert vacant_edges>=2
        if r in (0,4):assert vacant_edges==0
        rows.append({'occupied':occupied,'grade':r,'vacant_edges':vacant_edges})
    edge_index={e:i for i,e in enumerate(EDGES)}
    cycle=[0]*12
    for e,s in [((0,1),1),((3,1),-1),((3,2),1),((0,2),-1)]:cycle[edge_index[e]]=s
    word_rows=[]
    for flux in (-3,0,4):
        fields=tuple(flux*x for x in cycle)
        div=[0]*8
        for x,(a,b) in zip(fields,EDGES):div[a]+=x;div[b]-=x
        assert div==[0]*8
        outputs={}
        for edge,(a,b) in enumerate(EDGES):
            q=[int(v in A) for v in range(8)];q[a]=0;q[b]=1
            ee=list(fields);ee[edge]-=1
            gamma=2*sum(q[x]==q[y]==0 for x,y in EDGES)
            assert gamma==4
            key=(tuple(q),tuple(ee));assert key not in outputs;outputs[key]=gamma
        assert len(outputs)==12
        word_rows.append({'initial_cycle_flux':flux,'orthogonal_hops':12,'F_norm_squared':12,'loss_form':sum(outputs.values()),'squared_loss_action_norm':sum(g*g for g in outputs.values())})
    spin_rows=[]
    for S in (1,2,3,10,40):
        C=S*(S+1)
        losses=[]
        for m in range(-S,S+1):
            weights=[max(0.,1-m*(m+sign)/C) if abs(m+sign)<=S else 0. for sign in (1,-1)]
            assert abs(sum(weights)-2*(1-m*m/C))<1e-14
            assert sum(weights)>=2/(S+1)-1e-14
            losses.append(sum(weights))
        spin_rows.append({'S':S,'minimum_edge_loss':min(losses),'predicted_minimum':2/(S+1)})
    return {'all_70_occupancy_rows':rows,'rotor_word_rows':word_rows,'spin_edge_rows':spin_rows,
            'scope':'Exact occupancy and integer Gauss words; floating scalar spin identities. No entire large-spin evolution.'}

def two_level_controls():
    g=math.sqrt(12);kappa=.07;t=.3;rows=[]
    S4=math.exp(-48*kappa*t)
    for eps in (.15,.1,.07,.04,.02):
        h=np.array([[12*eps*eps,-eps*g],[-eps*g,1.]],complex)
        H=eps**-4*h;Gamma=np.diag([0.,4.]);heff=h-.5j*kappa*eps*eps*Gamma
        energy,Q=np.linalg.eigh(H);psi=Q[:,0]
        ev,V=np.linalg.eig(heff);z=np.linalg.solve(V,psi)
        v=V@(np.exp(-1j*t*eps**-4*ev)*z)
        p=float(np.vdot(v,v).real);mean=float(np.vdot(v,H@v).real)
        second=float(np.vdot(H@v,H@v).real)
        condvar=second/p-(mean/p)**2
        x=Q[:,0]*np.vdot(Q[:,0],v);y=Q[:,1]*np.vdot(Q[:,1],v)
        l=np.linalg.norm(x);u=np.linalg.norm(y);a=x/l;b=y/u
        witness=1j*(np.outer(b,a.conj())-np.outer(a,b.conj()))
        omega=np.outer(v,v.conj())
        derivative=abs(np.trace(omega@(1j*(H@witness-witness@H))))
        denominator=float(np.trace(omega@(witness@witness)).real)
        fisher=4*p*condvar
        assert abs(fisher-derivative**2/denominator)<1e-7*max(1,fisher)
        rows.append({'epsilon':eps,'noevent_probability':p,'predicted_probability':S4,
                     'scaled_conditional_variance':eps**2*condvar,'predicted_conditional_coefficient':48*kappa*kappa,
                     'scaled_weighted_Fisher':eps**2*fisher,'predicted_Fisher_coefficient':192*kappa*kappa*S4,
                     'first_high_amplitude_over_epsilon_cubed':float(u/eps**3),
                     'predicted_amplitude_coefficient':4*math.sqrt(3)*kappa*math.sqrt(S4),
                     'input_Fisher':float(4*(np.vdot(H@psi,H@psi).real-np.vdot(psi,H@psi).real**2)),
                     'phase_witness_saturation_error':float(abs(fisher-derivative**2/denominator))})
    assert abs(rows[-1]['scaled_conditional_variance']/(48*kappa*kappa)-1)<.025
    assert abs(rows[-1]['scaled_weighted_Fisher']/(192*kappa*kappa*S4)-1)<.025
    return {'rows':rows,'scope':'Two-level compensated toy with exact Hermitian zero-energy input; diagonalized full noevent evolution at a fixed later time, not the cube.'}

def actual_spin_one_controls():
    m=complete_spin_one()[4];dim=len(m['E'])
    omega=np.zeros(dim);omega[m['index'][(0,)*12]]=1
    gfo=m['loss']*(m['F']@omega)
    assert abs(np.vdot(gfo,gfo)-192)<1e-14
    assert np.min(m['loss'][m['W']==1])>=2
    kappa=.7;rows=[]
    for eps in (.1,.06,.035):
        start=time.monotonic();psi,prep=canonical_preparation(m,eps)
        h=diags(m['W'],dtype=float)-eps*(m['F']+m['F'].T)+eps**2*m['C']
        heff=(h-.5j*kappa*eps**2*diags(m['loss'],dtype=float)).tocsc()
        z=[riesz_action(heff,psi,r,32) for r in range(5)]
        norms=[float(np.linalg.norm(x)) for x in z]
        residual=float(np.linalg.norm(sum(z)-psi));assert residual<1e-9
        low_vector=eps**-3*(h@z[0]);expected=.5j*kappa*gfo
        row={'epsilon':eps,'dimension':dim,'Riesz_norms':norms,
             'high_norms_over_predicted_powers':[norms[r]/eps**(r+2) for r in range(1,5)],
             'expected_first_high_coefficient':4*math.sqrt(3)*kappa,
             'low_scaled_second_moment':float(np.vdot(low_vector,low_vector).real),
             'expected_low_coefficient':48*kappa*kappa,
             'low_vector_error':float(np.linalg.norm(low_vector-expected)),
             'decomposition_residual':residual,'preparation':prep,'elapsed_seconds':time.monotonic()-start}
        rows.append(row);print(json.dumps(row),flush=True)
    assert abs(rows[-1]['high_norms_over_predicted_powers'][0]/(4*math.sqrt(3)*kappa)-1)<.06
    assert rows[-1]['low_vector_error']<rows[0]['low_vector_error']
    return {'rows':rows,'builder_sha256':'4bdb0a05140d30e98f1afa85ccbba6c4684626c492550ec0625896d946356c5d','scope':'Actual canonical N=4 input and all five exact-cluster contour approximations at fixed S=1. No independent builder or joint-scaling numerical proof.'}

def main():
    HERE.mkdir(parents=True,exist_ok=True)
    started=time.monotonic()
    result={'geometry':geometry_and_words(),'toy':two_level_controls(),'actual_spin_one':actual_spin_one_controls(),
            'elapsed_seconds':time.monotonic()-started,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    data=json.dumps(result,indent=2)+'\n'
    (HERE/'NOEVENT_CONTROL_RESULTS.json').write_text(data)
    print(data,end='',flush=True)
    print('TOTAL: PASS=3 FAIL=0',flush=True)
if __name__=='__main__':main()
