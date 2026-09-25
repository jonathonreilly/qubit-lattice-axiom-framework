#!/usr/bin/env python3
"""Finite controls for the conditional ordinary microscopic cube energy theorem.

The written argument supplies all uniform and infinite-dimensional estimates.
Matrix definitions explicitly reuse the previous personal publication runners;
they are included here, not imported at runtime, and do not create independence.
No execution-time scientific input files are read. Declared notes bind the cache.
"""
AUDIT_TIMEOUT_SEC=900
AUDIT_INPUT_PATHS=(
    'docs/ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/SHARP_ACTUAL_ROTOR_CUBE_ENERGY_TAIL_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md',
)
from pathlib import Path
from collections import defaultdict
import hashlib,itertools,json,math,time
import numpy as np
import sympy as sp
from scipy.sparse import diags,eye,csr_matrix
from scipy.sparse.linalg import eigsh,splu
ROOT=Path(__file__).resolve().parents[1]
OUTPUT=ROOT/'outputs/ordinary_cube_birth_energy_20260924'
A=(0,3,5,6);B=(1,2,4,7)
EDGES=tuple((a,b) for a in A for b in B if a^b in (1,2,4))
CHORDS=(0,5,7,8,10)

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

def jump_matrix(m4,m6,sigma):
    rows=[];cols=[]
    for i,(q,E) in enumerate(zip(m4['q'],m4['E'])):
        if q[0] or q[1]:continue
        weight=1-int(E[0])*(int(E[0])+sigma)/2
        assert weight in (0,1)
        if not weight:continue
        ee=E.copy();ee[0]+=sigma;rows.append(m6['index'][tuple(int(x) for x in ee)]);cols.append(i)
    return csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(len(m6['E']),len(m4['E'])))

def normcols(x):
    return np.sum(abs(x)**2,axis=0)

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

def primitive_Q():
    words=[]
    for occupied in itertools.combinations(range(8),6):
        for negative in occupied:
            words.append(tuple((-1 if i==negative else 1) if i in occupied else 0 for i in range(8)))
    middle=[q for q in words if sum(not q[a] for a in A)==1]
    dark=[q for q in middle if not any(q[a]==q[b]==0 for a,b in EDGES)]
    bright=[q for q in middle if q not in dark]
    assert (len(middle),len(dark),len(bright))==(96,24,72)
    def hop(q,inward):
        for e,(a,b) in enumerate(EDGES):
            source,target=(b,a) if inward else (a,b)
            if not q[source] or q[target]:continue
            charge=q[source];qq=list(q);qq[target]=charge;qq[source]=0
            exponent=[0]*5
            if e in CHORDS:exponent[CHORDS.index(e)]=(1 if inward else -1)*charge
            yield tuple(qq),tuple(exponent)
    terms=defaultdict(int)
    for column,q in enumerate(dark):
        for inward,sign in ((True,1),(False,-1)):
            for q1,e1 in hop(q,inward):
                for q2,e2 in hop(q1,not inward):
                    terms[(q2,column,tuple(a+b for a,b in zip(e1,e2)))]+=sign
    terms={key:c for key,c in terms.items() if c}
    assert all(q in bright for q,column,e in terms), 'The entire dark-dark Laurent block must cancel.'
    rows=[defaultdict(dict) for _ in bright]
    for (q,column,e),c in terms.items():rows[bright.index(q)][column][e]=c
    return {'rows':[[{'column':column,'terms':[{'exponent':e,'coefficient':c} for e,c in cell.items()]} for column,cell in row.items()] for row in rows],
            'edges':EDGES,'chords':CHORDS,'dark_charge_words':dark,'bright_charge_words':bright}

def phase_and_weight_controls():
    data=primitive_Q()
    phases={'00000':1,'00011':1,'01101':2,'01110':1,
            '10100':1,'10111':2,'11001':4,'11010':2}
    rows=[]
    for bitstring,dimension in phases.items():
        bits=tuple(map(int,bitstring));Q=sp.zeros(72,24)
        for row,cells in enumerate(data['rows']):
            for cell in cells:
                for term in cell['terms']:
                    parity=sum(a*b for a,b in zip(bits,term['exponent']))%2
                    Q[row,cell['column']]+=term['coefficient']*(-1 if parity else 1)
        kernel=Q.nullspace();assert len(kernel)==dimension
        K=sp.Matrix.hstack(*kernel)
        assert Q*K==sp.zeros(72,dimension) and K.rank()==dimension
        # primitive_Q checks coefficientwise that G has no dark-dark block.
        # Thus its derivative compressions to this exact dark kernel vanish.
        # A spurious linear dark diagonal gives K* K, which is nonzero.
        gram=K.T*K
        assert gram.det()>0
        assert gram!=sp.zeros(dimension)
        rows.append({'phase':bitstring,'kernel_dimension':dimension,
                     'exact_kernel_gram_determinant':str(gram.det()),
                     'coefficientwise_zero_dark_block_checked_by_primitive_builder':True,
                     'linear_dark_diagonal_mutation_rejected':True})
    checks=[];linear_mutation=[]
    for S in (1,2,5,20):
        C=S*(S+1)
        for E in range(-S-2,S+3):
            for step in (-1,1):
                allowed=abs(E)<=S and abs(E+step)<=S
                amplitude=math.sqrt(max(0.,1-E*(E+step)/C)) if allowed else 0.
                scaled=C*abs(amplitude-1)
                assert scaled<=2*(1+E*E)+1e-12
                if scaled>2*(1+abs(E))+1e-12:
                    linear_mutation.append([S,E,step,scaled])
        # Missing a different edge outside the spin box also costs at most this
        # quadratic weight; checking only the currently shifted edge misses it.
        other=S+1
        assert C<=2*(1+other*other)
        checks.append({'spin':S,'max_source_field':S+2,'interior_and_box_boundary_checked':True})
    assert linear_mutation,'A linear field weight must fail in this tested family.'
    return {'phase_kernel_checks':rows,'spin_shift_weight_checks':checks,
            'linear_weight_mutation_witness':linear_mutation[0],
            'scope':'Exact dark-block/kernel algebra and finite scalar boundary controls, not a numerical proof of Sobolev decay or the joint limit.'}

def second_band_controls():
    models=complete_spin_one();m4,m6=models[4],models[6];F4,F6=m4['F'],m6['F']
    omega=np.zeros(F4.shape[0]);omega[m4['index'][(0,)*12]]=1
    marks=[jump_matrix(m4,m6,1),jump_matrix(m4,m6,-1)]
    marks.append(marks[0]+marks[1]);leading=[]
    for j in marks:
        a=j@(F4@(F4@(F4@omega)))
        b=F6@(j@(F4@(F4@omega)))
        c=F6@(F6@(j@(F4@omega)))
        residual=a-3*b+3*c;mutation=a-2*b+3*c
        assert np.count_nonzero(residual)==0 and np.linalg.norm(mutation)>0
        leading.append({'integer_residual_nonzeros':int(np.count_nonzero(residual)),
                        'changed_middle_coefficient_norm':float(np.linalg.norm(mutation))})
    rows=[]
    for epsilon in (.12,.08,.05,.03):
        started=time.monotonic();dressed,preparation=canonical_preparation(m4,epsilon)
        raw=np.column_stack([j@dressed for j in marks])
        X=raw/np.sqrt(normcols(raw))[None,:]
        h=(diags(m6['W'],dtype=float)-epsilon*(F6+F6.T)+epsilon**2*m6['C']).tocsc()
        heff=h-.5j*.7*epsilon**2*diags(m6['loss'],dtype=float)
        action=riesz_action(heff,X,2,32);refined=riesz_action(heff,X,2,48)
        difference=float(np.linalg.norm(action-refined))
        ratios=np.sqrt(normcols(refined))/epsilon**4
        assert difference<5e-11
        assert np.all((ratios>2)&(ratios<12))
        row={'epsilon':epsilon,'norm':np.sqrt(normcols(refined)).tolist(),
             'norm_over_epsilon_fourth':ratios.tolist(),'quadrature_difference':difference,
             'preparation':preparation,'elapsed_seconds':time.monotonic()-started}
        rows.append(row);print(json.dumps(row),flush=True)
    return {'complete_physical_dimensions':{str(n):len(m['E']) for n,m in models.items()},
            'leading_cancellation':leading,'projector_rows':rows,
            'scope':'Complete finite S=1 actual-preparation/projector consistency check. The written parity/analytic proof, not these four samples, supplies the uniform estimate.'}

def main():
    OUTPUT.mkdir(parents=True,exist_ok=True);started=time.monotonic()
    structural=phase_and_weight_controls()
    print(json.dumps(structural,indent=2),flush=True)
    second_band=second_band_controls()
    result={'structural':structural,'second_high_band':second_band,
            'elapsed_seconds':time.monotonic()-started,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'Finite author controls. Uniform Sobolev, weighted-analytic, growing-time, mean and mesoscopic-variance conclusions require the written proof and separate independent reconstruction.'}
    (OUTPUT/'ORDINARY_ENERGY_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)
    print('TOTAL: PASS=4 FAIL=0',flush=True)

if __name__=='__main__':main()
