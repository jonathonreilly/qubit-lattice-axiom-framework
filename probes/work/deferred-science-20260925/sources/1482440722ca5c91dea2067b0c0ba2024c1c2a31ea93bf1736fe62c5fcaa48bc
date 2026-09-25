#!/usr/bin/env python3
"""Finite controls for the conditional integrated microscopic variance theorem.

Matrix and author-control definitions are included from pinned earlier source;
this acknowledged reuse is not independent evidence. The written arguments,
not the fixed-S floating controls, supply all uniform limiting quantifiers.
"""
AUDIT_TIMEOUT_SEC=240
AUDIT_INPUT_PATHS=('docs/TIME_INTEGRATED_MICROSCOPIC_CUBE_BIRTH_VARIANCE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md')
from pathlib import Path
from collections import defaultdict
from fractions import Fraction
import hashlib,itertools,json,math,time
import numpy as np
import sympy as sp
from scipy.sparse import diags,eye,csr_matrix
from scipy.sparse.linalg import eigsh,splu
HERE=Path(__file__).resolve().parents[1]/'outputs/integrated_cube_birth_variance_20260924'
A=(0,3,5,6);B=(1,2,4,7)
EDGES=tuple((a,b) for a in A for b in B if a^b in (1,2,4))
ZERO=(0,)*12

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


def riesz_action(h,x,grade,n):
    """Trapezoidal contour integral; an approximate projector, never exact evidence."""
    result=np.zeros_like(x,dtype=complex)
    ident=eye(h.shape[0],format='csc',dtype=complex)
    for k in range(n):
        dz=.35*np.exp(2j*np.pi*(k+.5)/n)
        result+=dz*splu((grade+dz)*ident-h).solve(np.asarray(x,dtype=complex))/n
    return result


def charges(E):
    q=[int(v in A) for v in range(8)]
    for e,(a,b) in enumerate(EDGES):q[a]+=E[e];q[b]-=E[e]
    assert max(abs(x) for x in q)<=1
    return q


def clean(v):return {k:x for k,x in v.items() if x}


def hop(v):
    out=defaultdict(int)
    for E,c in v.items():
        q=charges(E)
        for e,(a,b) in enumerate(EDGES):
            if q[a]!=0 and q[b]==0:
                ee=list(E);ee[e]-=q[a];charges(ee);out[tuple(ee)]+=c
    return clean(out)


def mark(v,edge,signs):
    out=defaultdict(int);a,b=EDGES[edge]
    for E,c in v.items():
        q=charges(E)
        if q[a] or q[b]:continue
        for sign in signs:
            ee=list(E);ee[edge]+=sign;charges(ee);out[tuple(ee)]+=c
    return clean(out)


def gamma(v):
    out={}
    for E,c in v.items():
        q=charges(E);loss=sum(2 for a,b in EDGES if q[a]==q[b]==0)
        assert loss in (0,2)
        if loss:out[E]=loss*c
    return out


def dot(a,b):return sum(x*b.get(k,0) for k,x in a.items())


def original_word_controls():
    rows=[]
    for label,signs,want in [('plus',(1,),2),('minus',(-1,),2),('coherent',(1,-1),4)]:
        birth=mark(hop({ZERO:1}),0,signs);b=dot(birth,birth);assert b==want
        fb=hop(birth);gfb=gamma(fb)
        rate=Fraction(dot(fb,gfb),b)
        gsq=Fraction(dot(gfb,gfb),b)
        original_outputs=[]
        total=0
        for edge in range(12):
            for sign in (1,-1):
                final=mark(fb,edge,(sign,));norm=dot(final,final);total+=norm
                if norm:
                    assert all(sum(x*x for x in charges(E))==8 for E in final)
                    original_outputs.append({'edge':EDGES[edge],'sign':sign,'norm_squared_over_b':str(Fraction(norm,b))})
        assert Fraction(total,b)==rate and gsq==2*rate and rate>0
        # Deleting one active resolved outcome changes the complete original loss.
        assert original_outputs and Fraction(total,b)-Fraction(original_outputs[0]['norm_squared_over_b'])<rate
        row={'mark':label,'b':b,'effective_loss_expectation':str(rate),
             'Gamma_F_norm_squared':str(gsq),'low_component_scaled_M2_over_kappa_squared':str(gsq/4),
             'original_second_birth_outputs':original_outputs,
             'birth_words':[{'fields':E,'coefficient':c} for E,c in sorted(birth.items())]}
        rows.append(row)
    return {"rows":rows,"scope":"Exact integer original cube words and complete resolved loss; no joint-limit simulation."}

def local_star_controls():
    rows=[]
    for total,expected in [(2,{1:2,4:1}),(0,{0:1,1:2,3:2,4:1})]:
        inputs=[]
        for leaf in range(3):
            for sign in (1,-1):
                other=total-sign
                if other not in (1,-1):continue
                q=[sign,0,0,0];q[1+leaf]=other;inputs.append(tuple(q))
        outputs=sorted({tuple([0]+list(q)) for q in itertools.product((-1,0,1),repeat=3) if sum(x*x for x in q)==2 and sum(q)==total})
        M=sp.zeros(len(outputs),len(inputs))
        for j,q in enumerate(inputs):
            for leaf in range(1,4):
                if q[leaf]:continue
                out=list(q);out[leaf]=q[0];out[0]=0
                M[outputs.index(tuple(out)),j]+=1
        gram=M.T*M;ev=gram.eigenvals();assert ev==expected
        rows.append({'local_total_charge':total,'hop_matrix':M.tolist(),'Gram_eigenvalues':{str(k):v for k,v in ev.items()}})
    cover=[]
    for vacant in itertools.combinations(B,2):
        active=[a for a in A if all((a,b) in EDGES for b in vacant)]
        assert len(active)==2
        local_pairs=[{a}|{b for aa,b in EDGES if aa==a and b not in vacant} for a in active]
        assert all(len(x)==2 for x in local_pairs) and not (local_pairs[0]&local_pairs[1])
        occupied=set(range(8))-set(vacant)
        for negative in sorted(occupied):
            guarantees=sum(negative not in x for x in local_pairs)
            assert guarantees>=1
            cover.append({'vacant_B':vacant,'negative_site':negative,'active_A':active,'same_sign_centers':guarantees})
    assert len(cover)==36
    counts={k:sum(x['same_sign_centers']==k for x in cover) for k in (1,2)}
    assert counts=={1:24,2:12}
    # An oriented incidence matrix is a different local hopping convention.
    wrong=sp.Matrix([[0,1,-1],[-1,0,1],[1,-1,0]])
    assert min(wrong.T.__mul__(wrong).eigenvals())==0
    return {'local_blocks':rows,'cover':cover,'cover_counts':counts,'wrong_oriented_sign_model_has_kernel':True,
            'scope':'Exact local algebra and charge cover; the written Gauss-star direct-sum proof extends them to the physical rotor space. PRE-origin argument, root publication control.'}

def exponential_integral(z,a,b):
    if abs(z)<1e-12:return b-a
    return np.exp(z*a)*np.expm1(z*(b-a))/z


def three_grade_controls():
    W=np.diag([0.,1.,2.]);T=np.array([[0.,-1.,0.],[-1.,0.,-1.],[0.,-1.,0.]])
    C=np.diag([1.,0.,0.]);Gamma=np.diag([0.,2.,0.]);kappa=.7;a=.2;b=.8
    target=kappa/2*(math.exp(-2*kappa*a)-math.exp(-2*kappa*b));rows=[]
    for eps in (.15,.1,.07,.05,.03):
        h=W+eps*T+eps**2*C;H=eps**-4*h;heff=h-.5j*kappa*eps**2*Gamma
        ev,J=np.linalg.eig(heff);order=np.argsort(ev.real);ev=ev[order];J=J[:,order]
        for j in range(3):J[:,j]*=np.exp(-1j*np.angle(J[j,j]))
        K=-1j*eps**-4*ev
        assert np.max(K.real)<1e-10 and np.linalg.cond(J)<2
        weights=np.array([1.,eps,eps**4],complex)
        weights/=np.linalg.norm(J@weights)
        M=J.conj().T@H@J;N=(H@J).conj().T@(H@J)
        frequencies=K.conj()[:,None]+K[None,:]
        coeff=weights.conj()[:,None]*weights[None,:]
        integrals=np.array([[exponential_integral(z,a,b) for z in row] for row in frequencies])
        M2=np.sum(coeff*N*integrals)
        mean_coeff=(coeff*M).ravel();freq=frequencies.ravel();mean_square=0j
        for i in range(9):
            for j in range(9):
                mean_square+=mean_coeff[i]*mean_coeff[j]*exponential_integral(freq[i]+freq[j],a,b)
        assert abs(M2.imag)<1e-7 and abs(mean_square.imag)<1e-7
        variance=M2.real-mean_square.real;assert variance>0
        diagonal=float(np.sum(np.diag(coeff*N*integrals)).real)
        cross=float(M2.real-diagonal)
        low=float((coeff*N*integrals)[0,0].real)
        wrong_low=abs(weights[0])**2*abs(eps**-4*ev[0])**2*exponential_integral(2*K[0].real,a,b)
        row={'epsilon':eps,'scaled_integrated_variance':eps**2*variance,
             'predicted_limit':target,'scaled_low_energy_norm_integral':eps**2*low,
             'scaled_integrated_mean_square':eps**2*mean_square.real,
             'scaled_cross_terms':eps**2*cross,
             'wrong_use_of_noevent_energy_scaled_low_norm':float(eps**2*wrong_low),
             'low_survival_exponent':float(2*K[0].real),
             'eigen_residual':float(np.linalg.norm(heff@J-J*ev))}
        rows.append(row)
    assert abs(rows[-1]['scaled_integrated_variance']/target-1)<.03
    assert rows[-1]['wrong_use_of_noevent_energy_scaled_low_norm']<target/50
    return {'rows':rows,'scope':'Three-grade supplied toy with one absorbed zero-energy sector; spectral integration includes all nonorthogonal cross terms. Not an actual cube simulation.'}


def actual_cube_low_controls():
    models=complete_spin_one();m4,m6=models[4],models[6]
    omega=np.zeros(len(m4['E']));omega[m4['index'][(0,)*12]]=1
    marks=[jump_matrix(m4,m6,1),jump_matrix(m4,m6,-1)]
    marks.append(marks[0]+marks[1]);bnorm=np.sqrt([2.,2.,4.])
    beta=np.column_stack([j@(m4['F']@omega) for j in marks])/bnorm
    gfb=m6['loss'][:,None]*(m6['F']@beta)
    assert np.max(abs(np.sum(abs(gfb)**2,axis=0)-16))<1e-13
    kappa=.7;expected=.5j*kappa*gfb;rows=[]
    for eps in (.08,.04,.02):
        start=time.monotonic();psi,prep=canonical_preparation(m4,eps)
        raw=np.column_stack([j@psi for j in marks]);phi=raw/np.sqrt(np.sum(abs(raw)**2,axis=0))
        h=diags(m6['W'],dtype=float)-eps*(m6['F']+m6['F'].T)+eps**2*m6['C']
        heff=(h-.5j*kappa*eps**2*diags(m6['loss'],dtype=float)).tocsc()
        v0=riesz_action(heff,phi,0,32)
        vector=eps**-3*(h@v0)
        row={'epsilon':eps,'scaled_low_second_moment':np.sum(abs(vector)**2,axis=0).tolist(),
             'predicted_coefficient':[4*kappa*kappa]*3,
             'vector_difference_norm':np.sqrt(np.sum(abs(vector-expected)**2,axis=0)).tolist(),
             'noevent_energy_vector_norm':np.sqrt(np.sum(abs(eps**-4*(heff@v0))**2,axis=0)).tolist(),
             'preparation':prep}
        if eps==.02:
            refined=riesz_action(heff,phi,0,48)
            weighted_difference=float(np.linalg.norm(eps**-3*(h@(refined-v0))))
            assert weighted_difference<1e-7
            row['energy_weighted_contour_refinement_difference']=weighted_difference
        row['elapsed_seconds']=time.monotonic()-start;rows.append(row)
        print(json.dumps(row),flush=True)
    assert max(rows[-1]['vector_difference_norm'])<max(rows[0]['vector_difference_norm'])
    return {'rows':rows,'builder_provenance':'Definitions included from pinned author runner 4bdb0a05140d30e98f1afa85ccbba6c4684626c492550ec0625896d946356c5d; no runtime source import',
            'scope':'Author reuse of complete S=1 matrices and approximate Riesz contour. Epsilon varies at fixed S; no joint-limit numerical proof. All three actual first marks are used.'}


def main():
    HERE.mkdir(parents=True,exist_ok=True)
    started=time.monotonic()
    result={'original_words':original_word_controls(),'local_rotor_loss':local_star_controls(),
            'three_grade':three_grade_controls(),'actual_cube_low':actual_cube_low_controls(),
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'elapsed_seconds':time.monotonic()-started,
            'scope':'Finite corroboration with explicit reused author definitions; no pointwise variance or sharp integral limit.'}
    data=json.dumps(result,indent=2,default=lambda x:int(x))+'\n'
    (HERE/'INTEGRATED_VARIANCE_CONTROL_RESULTS.json').write_text(data)
    print(data,end='',flush=True)
    print('TOTAL: PASS=4 FAIL=0',flush=True)
if __name__=='__main__':main()
