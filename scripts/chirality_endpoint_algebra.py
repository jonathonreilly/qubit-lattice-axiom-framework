"""Finite Spin(10) endpoint: exact dyadic coefficient enumeration, no Monte Carlo.
Original pair conventions are reproduced explicitly; no original executable imports.
"""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['archive/chirality_exact_review_2026_10_18/MANIFEST.json', 'archive/chirality_exact_review_2026_10_18/original-recovery.tar.gz', 'docs/CHIRALITY_CONSTRUCTIVE_FINITE_ALGEBRA_NOTE_2026-10-18.md', 'docs/CHIRALITY_FINITE_REFLECTION_KERNELS_NOTE_2026-10-18.md', 'docs/CHIRALITY_LOCAL_ENDPOINT_ALGEBRA_NOTE_2026-10-18.md', 'outputs/chirality_exact_review_2026_10_18/PROVENANCE.json', 'outputs/chirality_exact_review_2026_10_18/README.md', 'outputs/chirality_exact_review_2026_10_18/proofs/bare_scalar_integral.md', 'outputs/chirality_exact_review_2026_10_18/proofs/boundary_row_wilson_mode.md', 'outputs/chirality_exact_review_2026_10_18/proofs/cubic_invariant_spaces.md', 'outputs/chirality_exact_review_2026_10_18/proofs/filtered_corner_algebra.md', 'outputs/chirality_exact_review_2026_10_18/proofs/finite_reflection_kernels.md', 'outputs/chirality_exact_review_2026_10_18/proofs/free_overlap_and_rational_projectors.md', 'outputs/chirality_exact_review_2026_10_18/proofs/majorana_square_conventions.md', 'outputs/chirality_exact_review_2026_10_18/proofs/marker_su3.md', 'outputs/chirality_exact_review_2026_10_18/proofs/one_loop_covariance.md', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/CLS1/scripts/cls1_core.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/CLS1/scripts/cls1_count.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/CLS1/scripts/cls1_labels.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/OBS3/scripts/obs3_core.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/OBS3/scripts/univ.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/QMC1/scripts/x2model.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/BLEAK1/b1_core.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/BLEAK1/b1_semi.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/col1_tokens_z1_full.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/col1_tokens_z1_links.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/col1_z3.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/col1_z3_lowmem.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/parse_lemma.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/su3common.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/K2/k2t1_free_transfer_4d.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/o12.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/t22lib.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/v2_exact_witness.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/v2b_exact_vector.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/v3_o12_exact.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/SIGN1/common.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/SIGN1/kramers_fams.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/SIGN1/p6_fierz_lambda1_zero.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/SIGN1/pair_kramers_u1c.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/X2/x2_cert.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/X3/tx3_overlap_transfer.py.source', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md', 'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md']
import itertools
import json
import numpy as np


def check(ok, label, detail):
    if not bool(ok):
        raise AssertionError(label + ': ' + str(detail))
    print('[PASS] ' + label + ' ' + str(detail), flush=True)


def clifford9():
    # Exact real Pauli-word search; anticommutation is decided combinatorially.
    words=[s for s in itertools.product('IXZE',repeat=4) if s.count('E')%2==0 and any(c!='I' for c in s)]
    def anti(a,b):return sum(x!=y and x!='I' and y!='I' for x,y in zip(a,b))%2==1
    def search(chosen, remaining):
        if len(chosen)==9:return chosen
        for j,w in enumerate(remaining):
            tail=[v for v in remaining[j+1:] if anti(w,v)]
            if len(chosen)+1+len(tail)>=9:
                got=search(chosen+[w],tail)
                if got:return got
        return None
    selected=search([],words)
    assert selected is not None
    mats={'I':np.eye(2,dtype=int),'X':np.array([[0,1],[1,0]]),'Z':np.diag([1,-1]),'E':np.array([[0,1],[-1,0]])}
    out=[]
    for word in selected:
        a=np.ones((1,1),dtype=int)
        for c in word:a=np.kron(a,mats[c])
        out.append(a)
    for i,g in enumerate(out):
        assert np.array_equal(g,g.T) and np.array_equal(g@g,np.eye(16))
        for h in out[:i]:assert not np.any(g@h+h@g)
    return out, [''.join(w) for w in selected]


def multiply(a,b):
    out={}
    for x,c in a.items():
        for y,d in b.items():
            # Each left generator crosses the smaller-index right generators.
            sign=(-1)**sum((y & ((1<<i)-1)).bit_count() for i in range(64) if x>>i&1)
            z=x^y;out[z]=out.get(z,0)+sign*c*d
    return {k:v for k,v in out.items() if v!=0}


def pair_majorana(M):
    # psi=(gamma_0..31 + i gamma_32..63)/2; all numbers are exact dyadics.
    U=np.hstack([np.eye(32),1j*np.eye(32)])/2
    K=U.T@M@U
    assert np.array_equal(K,-K.T)
    return {(1<<i)|(1<<j):2*K[i,j] for i in range(64) for j in range(i+1,64) if K[i,j]!=0}


def add(target,source,scale=1):
    for k,v in source.items():target[k]=target.get(k,0)+scale*v


def dagger(a):
    return {k:np.conj(v)*(-1)**(k.bit_count()*(k.bit_count()-1)//2) for k,v in a.items()}


def main():
    G,words=clifford9();I=np.eye(16);E=np.array([[0,1],[-1,0]]);X=np.array([[0,1],[1,0]]);Z=np.diag([1,-1]);Y=1j*np.array([[0,-1],[1,0]])
    P=(I+G[8])/2;Q=I-P
    vectors=[np.kron(E,n)/2 for n in G+[1j*I]]
    families=[]
    for label,taus,kappa in [('sing',[E],1.5),('trip',[E@X,E@Y,E@Z],-.5)]:
        matrices=[]
        for tau in taus:
            for g in G[:8]:
                T=np.kron(tau,P@g@Q); matrices.append((T-T.T)/2)
        families.append((label,matrices,kappa))
    quads=np.array(list(itertools.combinations(range(32),4)));i,j,k,l=quads.T
    def coeff(M):return M[i,j]*M[k,l]-M[i,k]*M[j,l]+M[i,l]*M[j,k]
    target=sum(coeff(M) for M in vectors)
    rhs=sum(kappa*sum(coeff(M) for M in ms) for _,ms,kappa in families)
    check(np.array_equal(target,rhs),'all annihilator quartic coefficients',{'components':len(quads),'Cl9_words':words,'kappa':[1.5,-.5,0,0]})
    # Full operator equality, including scalar and quadratic grades, without Fock matrices.
    lhs={};right={}
    for M in vectors:
        b=pair_majorana(M);bd=dagger(b)
        add(lhs,multiply(b,b),-.25);add(lhs,multiply(bd,bd),-.25)
    O=np.block([[np.kron(E,I),np.zeros((32,32))],[np.zeros((32,32)),-np.kron(E,I)]])
    channels=0
    for label,ms,kappa in families:
        for M in ms:
            b=pair_majorana(M);bd=dagger(b)
            re={};im={};add(re,b,.5);add(re,bd,.5);add(im,b,-.5j);add(im,bd,.5j)
            for a,c in [(re,-kappa/2),(im,kappa/2)]:
                assert dagger(a)==a
                add(right,multiply(a,a),c)
                # Transform antiunitarily on Majorana coefficient matrix.
                K=np.zeros((64,64),complex)
                for mask,v in a.items():
                    pair=[t for t in range(64) if mask>>t&1];u,vv=pair
                    K[u,vv]=v/2;K[vv,u]=-v/2
                tr=O.T@K.conj()@O
                expected=K if c<0 else -K
                assert np.array_equal(tr,expected)
                channels+=1
    lhs={k:v for k,v in lhs.items() if v!=0};right={k:v for k,v in right.items() if v!=0}
    check(lhs==right,'complete Majorana operator identity',{'nonzero_coefficients':len(lhs),'grades':sorted({k.bit_count() for k in lhs}),'scalar':str(lhs.get(0,0)),'quadratic_terms':sum(k.bit_count()==2 for k in lhs)})
    check(np.array_equal(O@O,-np.eye(64)) and channels==64,'endpoint antiunitary channel parities',{'channels':channels,'Theta_squared':-1,'scope':'local endpoint channels; no gap or Monte Carlo inference'})
    print('per_element: all 35960 annihilator quartic components and every generated Majorana coefficient are checked exactly in dyadic arithmetic')
    print('per_site: one explicitly supplied 32-complex-mode vertex is checked; arbitrary interacting lattice states are not tested')
    print('per_mode: all internal channel indices are enumerated; no spatial momentum spectrum or excitation gap is inferred')
    print('per_block: complete local scalar, quadratic and quartic Clifford grades are compared; the wider coupling cone is not certified')
    print('lattice_wide: local endpoint algebra and antiunitary parities only; lattice kinetics and all auxiliary-field histories need their own hypotheses')
    print('TOTAL: PASS=3 FAIL=0')

def _deadline(signum, frame):
    raise TimeoutError('Declared scientific runtime cap exceeded; partial stdout retained')

if __name__=='__main__':
    import signal
    import sys
    if sys.flags.optimize:
        raise RuntimeError('Assertions must remain enabled')
    signal.signal(signal.SIGALRM, _deadline)
    signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC)
    try:
        main()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
