"""Different finite native implementations for the analytical scalar proof."""
AUDIT_TIMEOUT_SEC = 60
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
from collections import Counter
from functools import lru_cache
from itertools import product,combinations
from pathlib import Path
from fractions import Fraction
import hashlib,json,time
import numpy as np
import sympy as s
from native_ward_scalar_algebra_2026_09_13 import A0,C0,ODD,SeparateAlgebra,CLASSES,separate_kernel as kernel,separate_norms as norms
HERE=Path(__file__).resolve().parents[1]/'.claude/science/physics-loops/native-positive-ward-scalar-20260913'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def car(n):
    out=[]
    for j in range(n):
        f=s.zeros(1<<n)
        for state in range(1<<n):
            if (state>>j)&1:
                f[state^(1<<j),state]=(-1)**((state&((1<<j)-1)).bit_count())
        out.append(f)
    return out



def covariance_check():
    start=time.monotonic();L=8;points=list(product(range(L),repeat=3));ix={r:j for j,r in enumerate(points)};M=L**3
    K=np.zeros((M,M))
    for r in points:
        for ax in range(3):
            v=list(r);v[ax]=(v[ax]+1)%L
            sign=(-1)**sum(r[:ax])*(-1 if r[ax]==L-1 else 1)
            K[ix[r],ix[tuple(v)]]=sign;K[ix[tuple(v)],ix[r]]=-sign
    freq,U=np.linalg.eigh(1j*K);Gamma=(K@(U*(1/np.abs(freq)))@U.conj().T).real
    env={A0:float(np.mean(np.abs(freq)**-2)),C0:float(np.mean(np.abs(freq)**-1)),
         ODD[1]:float(np.mean(np.abs(freq))),ODD[3]:float(np.mean(np.abs(freq)**3))}
    legs=[]
    for ax in range(3):
        for direction in (1,-1):
            r=[0,0,0];r[ax]=direction%L;legs.append((ax,direction,ix[tuple(r)]))
    a=np.eye(M)[:,0];vectors=[a,K@a];channels={}
    witness=json.loads((HERE/'WITNESS.json').read_text())
    p={k:tuple(float(Fraction(x)) for x in v) for k,v in witness['p'].items()}
    q={k:tuple(float(Fraction(x)) for x in v) for k,v in witness['q'].items()}
    def local_x(coeff,d,kd):
        p0,p1,p2=coeff
        return [((),-p0-2*p2),((0,d),-1j*p1),((1,d),p2),((0,kd),p2)]
    for A in combinations(range(6),2):
        d=np.zeros(M)
        for j in A:d[legs[j][2]]=-K[0,legs[j][2]]
        index=len(vectors);vectors.extend((d,K@d,6*np.linalg.solve(K,d)))
        kind='O' if legs[A[0]][0]==legs[A[1]][0] else 'P'
        x=local_x(p[kind],index,index+1);xq=local_x(q[kind],index,index+1)
        v=[((index+2,)+word,-c) for word,c in x]+[((index+2,)+word,c) for word,c in xq]
        v.extend([((index,),-2j*q[kind][1]),((index+1,),2*q[kind][2])])
        channels[A]=(kind,x,v,[((0,)+word,c) for word,c in v],index)
    vectors=np.stack(vectors);dot=vectors@vectors.T;kap=vectors@Gamma@vectors.T;cov=dot+1j*kap
    @lru_cache(None)
    def wick(word):
        if not word:return 1
        if len(word)%2:return 0
        return sum((-1)**(j-1)*cov[word[0],word[j]]*wick(word[1:j]+word[j+1:]) for j in range(1,len(word)))
    def inner(x,y):return sum(np.conjugate(c)*d*wick(w[::-1]+v) for w,c in x for v,d in y)
    tableerr=0.;nomerr=0.;normerr=0.;total=0.;prediction=0.;seen=set();count=0
    for A,(kindA,xA,vA,gvA,idxA) in channels.items():
        for C,(kindC,xC,vC,gvC,idxC) in channels.items():
            if set(A)&set(C) and A!=C:continue
            m=sum(legs[i][0]==legs[j][0] and legs[i][1]!=legs[j][1] for i in A for j in C)
            if A==C:m=0
            key=(kindA,kindC,m,A==C)
            if key not in seen:
                alg=SeparateAlgebra(kindA,kindC,m);bank=[idxA+2,idxC+2,0,1,idxA,idxA+1,idxC,idxC+1]
                # For self fixtures use A labels on both slots: C is the same physical vector.
                if A==C:bank=[idxA+2,idxA+2,0,1,idxA,idxA+1,idxA,idxA+1]
                for j,k in product(range(8),repeat=2):
                    if A==C and (j not in (0,2,3,4,5) or k not in (0,2,3,4,5)):
                        continue  # self check uses one slot; distinct C is not relabeled as A
                    expected=[float(z.subs(env)) for z in alg.table(j,k)]
                    actual=[dot[bank[j],bank[k]],kap[bank[j],bank[k]]]
                    tableerr=max(tableerr,max(abs(x-y) for x,y in zip(actual,expected)))
                seen.add(key)
            if A==C:continue
            count+=1;actual=(inner(xC,xA)-inner(xC,gvA)).real
            expected=float(kernel(kindA,kindC,m,p[kindA],p[kindC],q[kindA]).subs(env))
            nomerr=max(nomerr,abs(actual-expected));total+=actual;prediction+=expected
        nx,nv=norms(kindA,p[kindA],q[kindA]);normerr=max(normerr,abs(inner(xA,xA)-complex(nx.subs(env))),abs(inner(vA,vA)-complex(nv.subs(env))))
    assert count==90 and tableerr<5e-11 and nomerr<5e-11 and normerr<5e-11,(count,tableerr,nomerr,normerr)
    dropped=0.
    for A,(ka,xa,va,gva,ia) in channels.items():
        local=[((0,ia),-2j*q[ka][1]),((0,ia+1),2*q[ka][2])]
        for C,(kc,xc,vc,gvc,ic) in channels.items():
            if not set(A)&set(C):dropped+=(inner(xc,xa)-inner(xc,local)).real
    assert abs(dropped-total)>1
    return {'status':'passed','ordered_pairs':count,'norm_checks':30,'table_fixture_classes':len(seen),
            'max_table_absolute_error':tableerr,'max_kernel_absolute_error':nomerr,'max_norm_absolute_error':normerr,
            'complete_nominal_direct':total,'complete_nominal_formula':prediction,
            'omitted_W_p_minus_q_mutant_rejected':True,'seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'scope':'finite native covariance algebra check; no infinite alpha sign or source re-audit'}


def fock_moment_check():
    start=time.monotonic();L=16;shape=(L,)*3;coords=np.indices(shape);M=L**3
    theta=(2*np.pi*coords+np.pi)/L;frequency=2*np.sqrt(np.sum(np.sin(theta)**2,axis=0))
    twist=np.exp(1j*np.pi*np.sum(coords,axis=0)/L)
    def radial(f,power):
        out=twist*np.fft.ifftn(np.fft.fftn(f/twist)*frequency**power)
        return out if np.iscomplexobj(f) else out.real
    def K(f):
        out=np.zeros(shape)
        for ax in range(3):
            sign=(-1.)**np.sum(coords[:ax],axis=0) if ax else 1.
            plus=np.where(coords[ax]==L-1,-1.,1.);minus=np.where(coords[ax]==0,-1.,1.)
            out+=sign*(np.roll(f,-1,axis=ax)*plus-np.roll(f,1,axis=ax)*minus)
        return out
    a=np.zeros(shape);a[0,0,0]=1
    assert np.linalg.norm(K(K(a))+radial(a,2))<1e-12
    radial_moments={r:float(np.mean(frequency**r)) for r in (-2,-1,1,3,5,7,9)}
    # Local even radial moments through6 have no alias on this AP grid.
    from math import comb,factorial
    for n in range(7):
        exact=sum(factorial(n)//(factorial(i)*factorial(j)*factorial(n-i-j))*comb(2*i,i)*comb(2*j,j)*comb(2*(n-i-j),n-i-j) for i in range(n+1) for j in range(n-i+1))
        assert abs(np.mean(frequency**(2*n))-exact)/(1+exact)<2e-14
    raw=json.loads((HERE/'MOMENT_FORMULAS.json').read_text());rows=[]
    for kind,sites in {'P':((1,0,0),(0,1,0)),'O':((1,0,0),(L-1,0,0))}.items():
        d=np.zeros(shape);ka=K(a)
        for site in sites:d[site]=ka[site]
        w=-6*K(radial(d,-2));bank=[];aa=a;dd=d
        for n in range(6):bank.extend((aa,dd));aa=K(aa);dd=K(dd)
        bank.append(w);fields=np.stack(bank).reshape(13,M)
        gamma=np.stack([K(radial(f,-1)) for f in bank]).reshape(13,M)
        dot=fields@fields.T;kap=fields@gamma.T;scales=np.sqrt(np.diag(dot))
        scale_matrix=scales[:,None]*scales[None,:];C=(dot+1j*kap)/scale_matrix
        # gamma.T columns are Gamma f_j; the contraction is <f_i,Gamma f_j>.
        # Work with actual positive-frequency one-particle vectors. A Gram
        # eigensolve squares the source condition number unnecessarily.
        physical=(fields+1j*gamma).T/np.sqrt(2)
        U,singular,Vh=np.linalg.svd(physical/scales[None,:],full_matrices=False)
        keep=singular>max(singular)*1e-10;basis=U[:,keep];rank=int(sum(keep))
        Z=basis.conj().T@physical
        reconstruction=np.linalg.norm((Z.conj().T@Z)/scale_matrix-C)/np.linalg.norm(C)
        assert reconstruction<2e-11,reconstruction
        abs_basis=np.stack([radial(basis[:,j].reshape(shape),1).ravel() for j in range(rank)],axis=1)
        hm=basis.conj().T@abs_basis
        hermitian_error=np.linalg.norm(hm-hm.conj().T)/np.linalg.norm(hm)
        assert hermitian_error<2e-9,hermitian_error
        hm=(hm+hm.conj().T)/2;energies,V=np.linalg.eigh(hm);assert min(energies)>0
        # On all needed derivatives through order4, H0 gamma(f)Omega=i gamma(Kf)Omega.
        commutator_error=max(np.linalg.norm(hm@Z[:,j]-1j*Z[:,j+2])/(1+np.linalg.norm(Z[:,j+2])) for j in range(10))
        commutator_error=max(commutator_error,np.linalg.norm(hm@Z[:,12]-6j*Z[:,1])/(1+6*np.linalg.norm(Z[:,1])))
        assert commutator_error<2e-8,commutator_error
        Z=V.conj().T@Z;dimension=1<<rank;indices=np.arange(dimension);mode_data=[];energy=np.zeros(dimension)
        for j,e in enumerate(energies):
            low=indices[(indices&(1<<j))==0];high=low+(1<<j)
            signs=np.array([(-1)**int(i&((1<<j)-1)).bit_count() for i in low])
            mode_data.append((low,high,signs));energy+=e*((indices>>j)&1)
        def majorana(vector,state):
            out=np.zeros(dimension,dtype=complex)
            for coefficient,(low,high,signs) in zip(vector,mode_data):
                out[high]+=coefficient*signs*state[low]
                out[low]+=np.conjugate(coefficient)*signs*state[high]
            return out
        def D(state):return energy*state+1j*majorana(Z[:,0],majorana(Z[:,1],state))
        vacuum=np.zeros(dimension,dtype=complex);vacuum[0]=1
        maximum=0.;checks=[]
        local={s.Symbol('A0'):radial_moments[-2],s.Symbol('C0'):radial_moments[-1]}
        local.update({s.Symbol('L'+str(r)):radial_moments[r] for r in (1,3,5,7,9)})
        for source,initial in (('vacuum',vacuum),('ward',majorana(Z[:,12],vacuum))):
            states=[initial]
            for _ in range(5):states.append(D(states[-1]))
            for n in range(11):
                actual=np.vdot(states[n//2],states[n-n//2])
                expected=float(s.sympify(raw['moments'][kind][source][n]).subs(local))
                error=abs(actual-expected)/(1+abs(expected));maximum=max(maximum,error)
                assert error<2e-8,(kind,source,n,error,actual,expected)
                checks.append({'source':source,'order':n,'scaled_error':error})
        rows.append({'class':kind,'modes':rank,'Fock_dimension':dimension,'Gram_reconstruction_error':reconstruction,
                     'free_generator_hermiticity_error':hermitian_error,'free_commutator_error':commutator_error,
                     'max_moment_scaled_error':maximum,'checks':checks})
    return {'status':'passed','finite_AP_L':L,'moment_checks':44,'rows':rows,'seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'formula_sha256':hashlib.sha256((HERE/'MOMENT_FORMULAS.json').read_bytes()).hexdigest(),
            'scope':'different finite native Fock implementation checks the moment identities; the infinite gap and scalar bounds are analytical in the note; independent source review pending'}


def gap_fixture_check():
    started=time.monotonic();checks=[];finite_shifts=[]
    for L in (4,8):
        points=list(product(range(L),repeat=3));ix={r:j for j,r in enumerate(points)};M=L**3
        K=np.zeros((M,M))
        for r in points:
            for ax in range(3):
                v=list(r);v[ax]=(v[ax]+1)%L
                sign=(-1)**sum(r[:ax])*(-1 if r[ax]==L-1 else 1)
                K[ix[r],ix[tuple(v)]]=sign;K[ix[tuple(v)],ix[r]]=-sign
        e=np.eye(M)[:,0];old=np.linalg.eigvalsh(1j*K)
        for kind,sites in {'P':((1,0,0),(0,1,0)),'O':((1,0,0),(L-1,0,0))}.items():
            d=np.zeros(M)
            for site in sites:d[ix[site]]=-K[0,ix[site]]
            delta=2*(np.outer(e,d)-np.outer(d,e));changed=K+delta
            if L==4:
                new=np.linalg.eigvalsh(1j*changed);shift=(sum(abs(old))-sum(abs(new)))/8
                assert abs(shift-(np.sqrt(6)-2))<1e-12
                finite_shifts.append(shift)
                checks.append({'name':kind+'_finite_full_skew_energy','L':L,'gap':shift})
            for ss in (0.,.5,1.,2.,4.):
                A=float(e@np.linalg.solve(ss*ss*np.eye(M)-K@K,e));z=ss*ss*A
                expected=1-8*(1-z)**2/9 if kind=='O' else (1+2*z)**2/9+8*ss*ss*A*A
                before=np.linalg.slogdet(ss*np.eye(M)-K);after=np.linalg.slogdet(ss*np.eye(M)-changed)
                ratio=after[0]/before[0]*np.exp(after[1]-before[1]);assert abs(ratio-expected)<2e-11
                checks.append({'name':kind+'_finite_determinant','L':L,'s':ss,'absolute_error':abs(ratio-expected)})
                if L==8 and ss==1:
                    other=(1+2*z)**2/9+8*A*A if kind=='O' else 1-8*(1-z)**2/9
                    assert abs(ratio-other)>1e-3
                    checks.append({'name':kind+'_nonflat_geometry_swap_rejected','difference':abs(ratio-other)})
            mutant=K+delta/2
            ratio=np.exp(np.linalg.slogdet(np.eye(M)-mutant)[1]-np.linalg.slogdet(np.eye(M)-K)[1])
            A=float(e@np.linalg.solve(np.eye(M)-K@K,e));z=A
            expected=1-8*(1-z)**2/9 if kind=='O' else (1+2*z)**2/9+8*A*A
            assert abs(ratio-expected)>1e-3
    f=car(2);omega=s.sqrt(6);g=f[0]+f[0].T
    b0=s.I*(f[0].T-f[0]);b1=s.I*(f[1].T-f[1]);d=-omega*(b0+s.sqrt(2)*b1)/3
    H=omega*(f[0].T*f[0]+f[1].T*f[1]);D=H+s.I*g*d
    eigen=list(D.eigenvals());minimum=min(eigen,key=lambda x:float(x))
    assert s.simplify(D.det()-8)==0
    assert omega-2 in eigen and all(float(v)>=float(omega-2)-1e-14 for v in eigen)
    for full_trace_shift in finite_shifts:
        assert abs(full_trace_shift-float(minimum))<1e-12
        assert abs(full_trace_shift/2-float(minimum))>1e-3
    checks.append({'name':'independent_small_Fock_minimum','exact':'sqrt6-2','wrong_half_energy_rejected':True})
    return {'status':'passed','count':len(checks),'checks':checks,'half_bond_reversal_mutant_rejected':True,
            'seconds':time.monotonic()-started,'source_sha256':sha(__file__),
            'scope':'finite native determinant/Fock normalization checks; no extrapolated infinite gap'}
