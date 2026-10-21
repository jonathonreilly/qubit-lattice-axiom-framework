"""Portable finite algebra controls for the explicitly supplied constructions."""
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['archive/chirality_exact_review_2026_10_18/MANIFEST.json', 'archive/chirality_exact_review_2026_10_18/original-recovery.tar.gz', 'docs/CHIRALITY_CONSTRUCTIVE_FINITE_ALGEBRA_NOTE_2026-10-18.md', 'docs/CHIRALITY_FINITE_REFLECTION_KERNELS_NOTE_2026-10-18.md', 'docs/CHIRALITY_LOCAL_ENDPOINT_ALGEBRA_NOTE_2026-10-18.md', 'outputs/chirality_exact_review_2026_10_18/PROVENANCE.json', 'outputs/chirality_exact_review_2026_10_18/README.md', 'outputs/chirality_exact_review_2026_10_18/proofs/bare_scalar_integral.md', 'outputs/chirality_exact_review_2026_10_18/proofs/boundary_row_wilson_mode.md', 'outputs/chirality_exact_review_2026_10_18/proofs/cubic_invariant_spaces.md', 'outputs/chirality_exact_review_2026_10_18/proofs/filtered_corner_algebra.md', 'outputs/chirality_exact_review_2026_10_18/proofs/finite_reflection_kernels.md', 'outputs/chirality_exact_review_2026_10_18/proofs/free_overlap_and_rational_projectors.md', 'outputs/chirality_exact_review_2026_10_18/proofs/majorana_square_conventions.md', 'outputs/chirality_exact_review_2026_10_18/proofs/marker_su3.md', 'outputs/chirality_exact_review_2026_10_18/proofs/one_loop_covariance.md', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/CLS1/scripts/cls1_core.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/CLS1/scripts/cls1_count.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/CLS1/scripts/cls1_labels.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/OBS3/scripts/obs3_core.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/OBS3/scripts/univ.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/campaign/QMC1/scripts/x2model.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/BLEAK1/b1_core.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/BLEAK1/b1_semi.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/col1_tokens_z1_full.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/col1_tokens_z1_links.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/col1_z3.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/col1_z3_lowmem.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/parse_lemma.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/COL1/su3common.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/K2/k2t1_free_transfer_4d.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/o12.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/t22lib.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/v2_exact_witness.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/v2b_exact_vector.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/NT2/v3_o12_exact.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/SIGN1/common.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/SIGN1/kramers_fams.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/SIGN1/p6_fierz_lambda1_zero.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/SIGN1/pair_kramers_u1c.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/X2/x2_cert.py.source', 'outputs/chirality_exact_review_2026_10_18/provenance/scripts/X3/tx3_overlap_transfer.py.source', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md', 'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md']
from fractions import Fraction as F
import itertools
import math
import numpy as np
COUNT=0

def check(ok,label,detail):
    global COUNT
    if not bool(ok):raise AssertionError(label+': '+str(detail))
    COUNT+=1;print('[PASS] '+label+' '+str(detail),flush=True)


def marker():
    oh=[tuple(int(i==j) for i in range(3)) for j in range(3)];zero=(0,0,0)
    matter=[q+(0,)+p+(0,) for q in [zero]+oh for p in [zero]+oh if sum(q)+sum(p)<=1]
    links=[a+(0,)+b+(0,) for a in [zero]+oh for b in [zero]+oh if sum(a)==sum(b)]
    words={7:[(1,1,0)+q+(0,) for q in oh],19:[(1,1,0)+m+l for m in matter for l in links],35:[(1,1,0)+m+a+b+c for m in matter for a,b,c in itertools.product(links,repeat=3)]}
    for n,ws in words.items():
        for length in range(1,n):
            assert not ({w[:length] for w in ws}&{w[-length:] for w in ws})
    check([len(words[n]) for n in [7,19,35]]==[3,70,7000],'complete marker-word proper-overlap test',{n:len(w) for n,w in words.items()})
    # Independent role allocation for the 35-bit cubic construction.
    def starts(p):
        x,y,z=p;return [p,(x-35,y,z),(x,y-1,z),(x,y,z-1)]
    def groups(p):
        x,y,z=p
        out=[(x+o,y,z) for o in (3,7,11,19,27)]
        out += [(x-35+15,y,z),(x+23,y-1,z),(x+31,y,z-1)]
        return { (a+i,b,c) for a,b,c in out for i in range(3)}
    p=(0,0,0);compatible=0
    for q in itertools.product(range(-70,71),range(-1,2),range(-1,2)):
        if q==p:continue
        if all(a[1:]!=b[1:] or a[0]==b[0] or abs(a[0]-b[0])>=35 for a in starts(p) for b in starts(q)):
            assert not groups(p)&groups(q);compatible+=1
    check(compatible>0,'cubic token joint-sector register ownership',{'displacements_checked':141*9-1,'compatible':compatible})
    # Gell-Mann matrices embedded into the entire seven-qubit space.
    T=[]
    for i,j in itertools.combinations(range(3),2):
        a=np.zeros((3,3),complex);a[i,j]=a[j,i]=.5;T.append(a)
        b=np.zeros((3,3),complex);b[i,j]=-.5j;b[j,i]=.5j;T.append(b)
    T.extend([np.diag([.5,-.5,0]),np.diag([1,1,-2])/(2*math.sqrt(3))])
    idx=[sum(b<<(6-i) for i,b in enumerate(w)) for w in words[7]]
    V=np.eye(128)[:,idx];P=V@V.T;Gs=[V@t@V.T for t in T]
    err=max(np.max(np.abs(Gs[i]@Gs[j]-Gs[j]@Gs[i]-V@(T[i]@T[j]-T[j]@T[i])@V.T)) for i in range(8) for j in range(8))
    cas=sum(g@g for g in Gs)
    delta=np.eye(3).reshape(9)
    singerr=max(np.linalg.norm((np.kron(t,np.eye(3))+np.kron(np.eye(3),-t.conj()))@delta) for t in T)
    check(err<1e-13 and np.max(np.abs(cas-4*P/3))<1e-13 and singerr<1e-13,'full-space controlled SU3 and fundamental-conjugate singlet',{'dimension':128,'Lie_error':float(err),'singlet_error':float(singerr)})


def filters_and_cubic():
    table=[]
    for bits in itertools.product([0,1],repeat=3):
        x=list(map(F,bits));nn=(1-sum(1-2*t for t in x))/2;ff=1-sum(x[i]*math.prod(1-x[j] for j in range(3) if j!=i) for i in range(3))
        assert nn==sum(bits)-1 and ff==(0 if sum(bits)==1 else 1);table.append((bits,str(nn),str(ff)))
    # Exact Bernstein probability decomposition, not just corner values.
    for x in itertools.product([F(0),F(1,3),F(1)],repeat=3):
        probs=[math.prod(x[j] if b[j] else 1-x[j] for j in range(3)) for b in itertools.product([0,1],repeat=3)]
        assert sum(probs)==1 and all(p>=0 for p in probs)
    check(True,'filter corner and Bernstein decomposition',table)
    totals=[0,0,0,0];num=0
    for p in itertools.permutations(range(3)):
        psign=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        for signs in itertools.product([-1,1],repeat=3):
            if psign*math.prod(signs)!=1:continue
            num+=1;f=sum(p[i]==i for i in range(3));tr=sum(signs[i] for i in range(3) if p[i]==i)
            totals=[a+b for a,b in zip(totals,[f*f*(1+tr),f*(1+tr),f*f*(1+tr)*tr,f*(1+tr)*tr])]
    dims=[F(x,num) for x in totals]
    check(num==24 and dims==[2,1,5,2],'proper-cubic character multiplicities',list(map(str,dims)))


def wilson_and_overlap():
    X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1]);I=np.eye(2)
    chi=np.array([1,1])/math.sqrt(2);worst=0.
    for L in [2,3,5]:
        for k in [0,.13,.7,math.pi]:
            D=np.kron(np.eye(L),(1-math.cos(k))*I+1j*Y*math.sin(k))
            for t in range(L-1):
                D[2*t:2*t+2,2*t+2:2*t+4]=-(I-X)/2
                D[2*t+2:2*t+4,2*t:2*t+2]=-(I+X)/2
            psi=np.zeros(2*L,complex);psi[-2:]=chi;out=D@psi
            assert np.linalg.norm(out[:-2])<1e-13
            worst=max(worst,abs(np.vdot(out,out).real-4*math.sin(k/2)**2))
    check(worst<1e-13,'open Wilson boundary-row norm',{'sizes':[2,3,5],'momenta':[0,.13,.7,math.pi],'max_error':worst})
    G=[np.kron(X,X),np.kron(X,Y),np.kron(X,Z),np.kron(Z,I)];I4=np.eye(4);err=0.
    for p,M,t in [([.2,.3,-.4],.5,.7),([.7,-.2,.8],1.,1.1),([.1,.2,.3],1.5,.4)]:
        s=np.sin(p);S2=s@s;beta=1-M+sum(1-np.cos(p));v=sum(s[j]*G[j] for j in range(3))+G[3]*np.sin(t);b=beta-np.cos(t);om=np.sqrt(1+S2+beta*beta-2*beta*np.cos(t))
        D=I4+(1j*v+b*I4)/om;inv=I4/2-1j*v/(2*(om+b));err=max(err,float(np.max(np.abs(D@inv-I4))))
        if beta!=0:
            E=np.arccosh((1+S2+beta*beta)/(2*abs(beta)));z=(0 if beta>0 else math.pi)+1j*E
            vc=sum(s[j]*G[j] for j in range(3))+G[3]*np.sin(z);bc=beta-np.cos(z)
            assert np.max(np.abs((-1j*vc+bc*I4)@(1j*vc+bc*I4)))<1e-12
    check(err<1e-12,'free overlap inverse and analytic branch thresholds',{'fixtures':3,'max_inverse_error':err})


def covariance_and_integral():
    # Average an arbitrary tensor under the full simultaneous S3 action.
    B=np.arange(9).reshape(3,3)**2;A=np.zeros((3,3),int)
    for p in itertools.permutations(range(3)):A+=B[np.ix_(p,p)]
    assert len(set(A.diagonal()))==1 and len({A[i,j] for i in range(3) for j in range(3) if i!=j})==1
    alpha=F(int(A[0,1]),6);beta=F(int(A[0,0]-A[0,1]),6)
    iso=(alpha+beta/3);tet=beta
    assert F(int(A.sum()),54)==iso
    # This exact cancellation uses the proved torus divergence identity and integral QR=3/4.
    # tau/(2 Q²) integrates to 1/2-1/Q; no value for the Watson integral is imported.
    coeff_W=F(1,16)-F(2,32);constant=F(1,32)-F(1,6)+F(3,4)/6
    check(coeff_W==0 and constant==F(-1,96),'bare supplied scalar integral cancellation',{'Watson_coefficient':str(coeff_W),'constant':str(constant),'scope':'supplied stress/kernel, zero-mode prescription, no seagull or counterterm'})
    omega=np.exp(2j*np.pi/3);H=np.array([[omega**(i*j) for j in range(3)] for i in range(3)])/math.sqrt(3)
    assert np.max(np.abs(H.conj().T@H-np.eye(3)))<1e-13
    check(True,'full-S3 covariance and flat-column example',{'alpha':str(alpha),'beta':str(beta),'iso':str(iso),'tet':str(tet),'Hadamard':'Fourier3'})


def main():
    marker();filters_and_cubic();wilson_and_overlap();covariance_and_integral()
    print('per_element: supplied finite matrices, all marker words and exact coefficient identities are evaluated; no microscopic Standard Model supplier is inferred')
    print('per_site: seven-qubit controlled generators and explicitly allocated token registers are checked; ground-state selection is an additional unresolved problem')
    print('per_mode: all eight corners and selected free momentum fixtures are included; no full interacting spectrum or gap is certified')
    print('per_block: supplied tensor representations, local singlets and finite Wilson blocks are checked; allowed invariant coefficients are not forced dynamics')
    print('lattice_wide: translation-covariant algebraic constructions and conditional formulas only; continuum universality, chirality and physical reconstruction are not established')
    print(f'TOTAL: PASS={COUNT} FAIL=0')

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
