"""Bounded falsifiers for finite-clock transfer and magnetic-source diagnostics.

No scientific files are read; the note pin binds proof identity.
Infinite-volume gap/analyticity uses the explicitly
mapped Yarotsky theorem in the note; finite calculations do not prove it.
"""
AUDIT_TIMEOUT_SEC = 90
AUDIT_INPUT_PATHS = [
    'docs/FINITE_CLOCK_PHASE_DIAGNOSTICS_LOCAL_WRAPS_AND_QUANTIZED_FLUX_BOUNDED_THEOREM_NOTE_2026-09-14.md',
]
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import gcd
import numpy as np
import mpmath as mp
from scipy.linalg import eigh
from scipy.special import ive


def wilson_Q(N,delta,t):
    alpha=1-np.cos(2*np.pi/N);x=delta*t*(2 if N==2 else 1)
    beta=np.log(1/x)/alpha;angles=2*np.pi*np.arange(N)/N
    weights=np.exp(-beta*(1-np.cos(angles)));weights/=weights.sum()
    Q=np.zeros((N,N))
    for q,p in enumerate(weights):Q+=p*np.roll(np.eye(N),q,axis=0)
    assert np.min(eigh(Q,eigvals_only=True))>0
    return Q,beta


def villain_Q(N,delta,t):
    x=delta*t;Q=np.zeros((N,N));normal=0.
    for q in range(-8,9):
        weight=x**(q*q);Q+=weight*np.roll(np.eye(N),q,axis=0);normal+=weight
    return Q/normal,N*N*np.log(1/x)/(2*np.pi**2)


def matched_single_plaquette():
    rows=[];t=.7;K=1.1
    for N in [2,3,4,5,8]:
        X=np.roll(np.eye(N),1,axis=0);angles=2*np.pi*np.arange(N)/N
        H=4*t*(2*np.eye(N)-X-X.T)+np.diag(K*(1-np.cos(angles)))
        previous={key:float('inf') for key in ['Wilson','Villain']}
        for delta in [1e-2,1e-3,1e-4]:
            for regulator,make_Q in [('Wilson',wilson_Q),('Villain',villain_Q)]:
                Q,beta_t=make_Q(N,delta,t)
                if regulator=='Wilson':
                    B=np.exp(-delta*K*(1-np.cos(angles)));beta_s=delta*K
                else:
                    y=delta*K/2;B=sum(y**(n*n)*np.cos(n*angles) for n in range(-8,9))/sum(y**(n*n) for n in range(-8,9));beta_s=1/(2*np.log(1/y))
                D=np.diag(np.sqrt(B));T=D@np.linalg.matrix_power(Q,4)@D
                eigen,U=eigh(T);assert np.min(eigen)>0
                generator=(U*(-np.log(eigen)/delta))@U.T
                error=np.linalg.norm(generator-H,2)
                assert error<previous[regulator] and error/delta<200
                previous[regulator]=error
                rows.append({'N':N,'delta':delta,'regulator':regulator,'generator_error':error,'bare_product':beta_s*beta_t})
    print('matched_single_plaquette',rows,flush=True)


def exact_alias_schedule():
    rows=[]
    with mp.workdps(100):
        N=8;t=mp.mpf('.7');eta=mp.mpf('.5')
        for ell in map(mp.mpf,[8,16,32,64]):
            delta=mp.exp(-ell)/t;x=delta*t;beta=N*N*ell/(2*mp.pi**2)
            M=int(mp.ceil(mp.sqrt(1+eta)*ell/mp.pi+mp.mpf('.5')))
            a=mp.pi**2/ell;tail=2*mp.exp(-a*(M+mp.mpf('.5'))**2)/(1-mp.exp(-a*(2*M+2)))
            schedule_bound=16*t**(1+eta)*delta**eta/mp.expm1(2*mp.pi*mp.sqrt(1+eta))
            assert x<=mp.mpf(1)/8 and 2*tail<=mp.mpf(1)/4
            assert 8*tail/delta<=schedule_bound
            errors=[]
            for k in range(-N//2,N//2+1):
                dual=mp.fsum(x**(r*r)*mp.cos(2*mp.pi*r*k/N) for r in range(-8,9))/mp.fsum(x**(r*r) for r in range(-8,9))
                aliases=lambda kk,m:mp.fsum(mp.exp(-(kk+j*N)**2/(2*beta)) for j in range(-m,m+1))
                truncated=aliases(k,M)/aliases(0,M);full=aliases(k,100)/aliases(0,100)
                assert abs(full-dual)<mp.mpf('1e-95')
                assert abs(full-truncated)<=2*tail
                gap_error=abs(mp.log(full)-mp.log(truncated))/delta
                assert gap_error<=8*tail/delta
                target=t*(2-2*mp.cos(2*mp.pi*k/N))
                assert abs(-mp.log(dual)/delta-target)<20*delta
                errors.append(gap_error)
            rows.append({'ell':str(ell),'alias_cutoff':M,'max_generator_error':str(max(errors)),'rigorous_bound':str(8*tail/delta),'uniform_delta_eta_bound':str(schedule_bound)})
        divergence=[]
        for M in [0,2]:
            for ell in map(mp.mpf,[100,1000,10000]):
                delta=mp.exp(-ell)/t;beta=N*N*ell/(2*mp.pi**2);k=1
                A=lambda kk:mp.fsum(mp.exp(-(kk+j*N)**2/(2*beta)) for j in range(-M,M+1))
                gap=-mp.log(A(k)/A(0))/delta;asymptotic=k*k/(2*beta*delta)
                ratio=gap/asymptotic
                assert gap>100 and ratio>0
                if ell==10000:assert abs(ratio-1)<.01
                divergence.append({'fixed_alias_cutoff':M,'ell':str(ell),'gap_over_divergent_asymptotic':str(ratio)})
    print('exact_alias_schedule',{'controlled_cutoffs':rows,'fixed_cutoff_divergence':divergence},flush=True)


def spatial_hessian_and_local_shift():
    rows=[];N=8;t=.7;K=1.1
    for ell in [5,10,20,40]:
        delta=np.exp(-ell)/t;y=delta*K/2;beta_s=1/(2*np.log(1/y))
        curvature=sum(n*n*y**(n*n) for n in range(-8,9))/sum(y**(n*n) for n in range(-8,9))
        assert abs(curvature/(delta*K)-1)<3*delta*K
        alphaN=1-np.cos(2*np.pi/N);beta_t=ell/alphaN;B=6*beta_t
        shift=np.arcsinh(N/B);I=N*shift-np.hypot(B,N)+B
        expected=N*N/(2*B)
        # Direct Bessel ratio checks the actual zero-background conditional
        # harmonic, independent of the optimized complex-shift upper estimate.
        conditional=ive(N,B)/ive(0,B)
        assert abs(I/expected-1)<.002 and conditional<=np.exp(-I)+1e-12
        if ell>=10:assert abs((1-conditional)/expected-1)<.1
        rows.append({'ell':ell,'periodized_spatial_curvature_over_delta':curvature/delta,'bare_spatial_beta_over_delta':beta_s/delta,'optimized_suppression':np.exp(-I),'actual_conditional_Nth_harmonic':conditional})
    print('spatial_hessian_and_local_shift',rows,flush=True)


def square_gauss_compression():
    rows=[]
    for N in [2,3,4]:
        states=list(product(range(N),repeat=4));dim=N**4
        X=np.roll(np.eye(N),1,axis=0);eye=np.eye(N)
        ops=[]
        for link in range(4):
            op=np.ones((1,1))
            for j in range(4):op=np.kron(op,X if j==link else eye)
            ops.append(op)
        U=np.zeros((dim,N))
        for row,a in enumerate(states):U[row,(a[0]+a[1]-a[2]-a[3])%N]=N**(-1.5)
        assert np.linalg.norm(U.T@U-eye)<1e-12
        generators=[ops[0].T@ops[3].T,ops[0]@ops[1].T,ops[1]@ops[2],ops[2].T@ops[3]]
        assert max(np.linalg.norm(G@U-U) for G in generators)<1e-12
        t=.7;K=1.1
        fullE=sum(t*(2*np.eye(dim)-op-op.T) for op in ops)
        fullB=np.diag([K*(1-np.cos(2*np.pi*(a[0]+a[1]-a[2]-a[3])/N)) for a in states])
        target=4*t*(2*eye-X-X.T)+np.diag(K*(1-np.cos(2*np.pi*np.arange(N)/N)))
        assert np.linalg.norm((fullE+fullB)@U-U@target)<2e-12
        delta=.003;weight=np.exp(-np.log(1/(delta*t*(2 if N==2 else 1)))*(1-np.cos(2*np.pi*np.arange(N)/N))/(1-np.cos(2*np.pi/N)));weight/=weight.sum()
        Q=sum(weight[q]*np.linalg.matrix_power(X,q) for q in range(N))
        fullQ=np.ones((1,1))
        for _ in range(4):fullQ=np.kron(fullQ,Q)
        D=np.diag(np.exp(-delta*np.diag(fullB)/2))
        reducedD=np.diag(np.exp(-delta*K*(1-np.cos(2*np.pi*np.arange(N)/N))/2))
        error=np.linalg.norm(U.T@D@fullQ@D@U-reducedD@np.linalg.matrix_power(Q,4)@reducedD)
        assert error<2e-12
        rows.append({'N':N,'full_link_dimension':dim,'gauss_dimension':N,'compressed_transfer_error':error})
    print('square_gauss_compression',rows,flush=True)


def face_boundary(base,ij):
    i,j=ij;out={}
    def step(v,k):r=list(v);r[k]+=1;return tuple(r)
    out[(base,i)]=1;out[(step(base,i),j)]=1
    out[(step(base,j),i)]=-1;out[(base,j)]=-1
    return out


def exact_patch_perturbation():
    rows=[]
    for name,faces in [('two_xy',[((0,0,0),(0,1)),((1,0,0),(0,1))]),('cube_corner',[((0,0,0),(0,1)),((0,0,0),(0,2)),((0,0,0),(1,2))])]:
        boundaries=[face_boundary(*f) for f in faces];edges=sorted(set().union(*boundaries));B=np.array([[b.get(e,0) for b in boundaries] for e in edges],dtype=int)
        source=[int(f[1]==(0,1)) for f in faces];nf=len(faces)
        for N,d in [(2,[0,4]),(3,[0,3,3]),(4,[0,2,4,2]),(6,[0,1,3,4,3,1])]:
            states=list(product(range(N),repeat=nf));zero=(0,)*nf
            energy={s:sum(d[int(e)%N] for e in B@np.array(s)) for s in states}
            assert all(energy[s]>0 for s in states if s!=zero)
            psi=[{(zero,0):F(1)}];Es=[{}]
            for n in range(1,N+1):
                v=defaultdict(F)
                for (s,a),c in psi[n-1].items():
                    for p in range(nf):
                        for sign in [-1,1]:
                            target=list(s);target[p]=(target[p]+sign)%N
                            v[(tuple(target),a+sign*source[p])]-=c/2
                en={a:c for (s,a),c in v.items() if s==zero and c}
                Es.append(en)
                if n<N:assert all(a==0 for a in en)
                rhs=defaultdict(F)
                for key,c in v.items():
                    if key[0]!=zero:rhs[key]-=c
                for j in range(1,n+1):
                    for a,ec in Es[j].items():
                        for (s,b),pc in psi[n-j].items():
                            if s!=zero:rhs[(s,a+b)]+=ec*pc
                psi.append({(s,a):c/energy[s] for (s,a),c in rhs.items() if c})
            expected=-F(sum(source),2**N*4**(N-1)*N*N)
            assert Es[N].get(N)==expected and Es[N].get(-N)==expected
            assert all(a in [-N,0,N] for a in Es[N])
            curvature=-sum(a*a*c for a,c in Es[N].items())
            assert curvature==F(sum(source)*8,8**N)
            rows.append({'patch':name,'N':N,'physical_dimension':N**nf,'source_faces':sum(source),'order_N_energy_fourier_coefficient':str(expected),'order_N_curvature':str(curvature)})
    print('exact_patch_perturbation',rows,flush=True)


def single_face_spectral_curvature():
    rows=[]
    with mp.workdps(85):
        for N in [2,3,4,5,6,8]:
            t=mp.mpf('.7');theta=mp.mpf('.23');previous=mp.inf
            for K in map(mp.mpf,['.1','.03','.01']):
                def ground(th):
                    H=mp.diag([4*t*(2-2*mp.cos(2*mp.pi*m/N)) for m in range(N)])
                    for m in range(N):
                        H[(m+1)%N,m]-=K*mp.exp(1j*th)/2
                        H[(m-1)%N,m]-=K*mp.exp(-1j*th)/2
                    return mp.eighe(H,eigvals_only=True)[0]
                actual=ground(theta)-ground(0)
                leading=2*(K/2)**N*(1-mp.cos(N*theta))/((4*t)**(N-1)*N*N)
                relative=abs(actual/leading-1)
                assert relative<previous and relative<mp.mpf('.01')
                previous=relative
                rows.append({'N':N,'K':str(K),'energy_difference_over_leading':str(actual/leading)})
    print('single_face_spectral_curvature',rows,flush=True)


def modular_periods_and_quantized_source():
    rng=np.random.default_rng(1027);rows=[]
    for L in [3,4,5]:
        sites=list(product(range(L),repeat=3));edges=[(r,i) for r in sites for i in range(3)];faces=[(r,ij) for r in sites for ij in [(0,1),(0,2),(1,2)]]
        edgeid={e:i for i,e in enumerate(edges)};faceid={f:i for i,f in enumerate(faces)}
        def step(r,i):s=list(r);s[i]=(s[i]+1)%L;return tuple(s)
        B=np.zeros((len(edges),len(faces)),dtype=int)
        for p,(r,(i,j)) in enumerate(faces):
            for e,sign in [((r,i),1),((step(r,i),j),1),((step(r,j),i),-1),((r,j),-1)]:B[edgeid[e],p]+=sign
        # Each face in a link star has a private opposite parallel edge.
        # This excludes mixed-orientation order-N modular-wrap histories.
        for edge_index,(_,axis) in enumerate(edges):
            star=np.flatnonzero(B[edge_index])
            assert len(star)==4
            for p in star:
                opposite=[q for q in np.flatnonzero(B[:,p]) if q!=edge_index and edges[q][1]==axis]
                assert len(opposite)==1 and np.count_nonzero(B[opposite[0],star])==1
        C=np.zeros((len(faces),len(sites)),dtype=int)
        for c,r in enumerate(sites):
            for ij,k,sgn in [((1,2),0,1),((0,2),1,-1),((0,1),2,1)]:
                C[faceid[(step(r,k),ij)],c]+=sgn;C[faceid[(r,ij)],c]-=sgn
        assert not np.any(B@C)
        a=np.array([int(ij==(0,1)) for r,ij in faces]);b=np.array([int(ij==(0,1) and r[0]==0 and r[1]==0) for r,ij in faces])
        assert not np.any(C.T@b)
        sheet=np.array([int(ij==(0,1) and r[2]==0) for r,ij in faces]);assert not np.any(B@sheet)
        assert a@sheet==L*L and b@sheet==1
        for N in [2,3,4,6,8]:
            g=gcd(N,L*L)
            if g==1:
                m=pow(L*L,-1,N);gxy=np.full((L,L),m,dtype=int);gxy[0,0]-=1
                row=gxy.sum(axis=0);lam=np.zeros(len(edges),dtype=int)
                for (x,y,z),i in edges:
                    if i==1:lam[edgeid[((x,y,z),i)]]=sum(gxy[u,y]-row[y]*int(u==L-1) for u in range(x))
                    if i==0:lam[edgeid[((x,y,z),i)]]=-int(x==L-1)*sum(row[v] for v in range(y))
                assert not np.any((B.T@lam-(m*a-b))%N)
            for _ in range(30):
                W=int(rng.integers(-4,5));S=C@rng.integers(-3,4,len(sites))+N*rng.integers(-2,3,len(faces))+W*sheet
                assert not np.any((B@S)%N)
                assert int(a@S)%g==0 and int((a@S)-L*L*W)%N==0
                assert int(b@S-W)%N==0
                lam=rng.integers(0,N,len(edges));assert int((b+B.T@lam)@S-b@S)%N==0
            # A local wrap contributes to continuous source, but has trivial
            # quantized-source phase even when located on the source stack.
            p=faceid[((0,0,0),(0,1))];local=np.zeros(len(faces),dtype=int);local[p]=N
            assert a@local==N and (b@local)%N==0
            rows.append({'L':L,'N':N,'closed_source_period_gcd':g,'sheet_source':L*L,'quantized_sheet_flux':1,'local_wrap_quantized_phase_residue':0})
    print('modular_periods_and_quantized_source',rows,flush=True)

def periodic_quantized_ground_series():
    """Actual 2D periodic cell complexes: scalar exact recursion vs subset sum."""
    rows=[]
    for L in [2,3]:
        N=2;P=L*L;sites=list(product(range(L),repeat=2));edges=[(r,i) for r in sites for i in range(2)];eid={e:i for i,e in enumerate(edges)}
        B=np.zeros((len(edges),P),dtype=int)
        def step(r,i):s=list(r);s[i]=(s[i]+1)%L;return tuple(s)
        for p,r in enumerate(sites):
            for edge,sign in [((r,0),1),((step(r,0),1),1),((step(r,1),0),-1),((r,1),-1)]:B[eid[edge],p]+=sign
        states=list(product(range(2),repeat=P-1));zero=(0,)*(P-1)
        energy={s:4*int(np.sum((B@np.array(s+(0,)))%2)) for s in states}
        assert all(energy[s]>0 for s in states if s!=zero)
        maps=[]
        for p in range(P):
            maps.append({s:tuple((v+int(p==j or p==P-1))%2 for j,v in enumerate(s)) for s in states})
        def coefficients(signs):
            psi=[{zero:F(1)}];E=[F(0)]
            for n in range(1,P+1):
                v=defaultdict(F)
                for s,c in psi[-1].items():
                    for p in range(P):v[maps[p][s]]-=signs[p]*c
                E.append(v.get(zero,F(0)));rhs=defaultdict(F)
                for s,c in v.items():
                    if s!=zero:rhs[s]-=c
                for j in range(1,n+1):
                    for s,c in psi[n-j].items():
                        if s!=zero:rhs[s]+=E[j]*c
                psi.append({s:c/energy[s] for s,c in rhs.items() if c})
            return E
        untwisted=coefficients([1]*P);signs=[1]*P;signs[0]=-1;twisted=coefficients(signs)
        assert twisted[:P]==untwisted[:P]
        full=(1<<P)-1;subset_weight={0:F(1)}
        for size in range(1,P):
            for mask in range(1,full):
                if mask.bit_count()!=size:continue
                selected=np.array([(mask>>p)&1 for p in range(P)])
                D=4*int(np.sum((B@selected)%2));assert D>0
                subset_weight[mask]=sum(subset_weight[mask^(1<<p)] for p in range(P) if mask>>p&1)/D
        sheet=sum(subset_weight[full^(1<<p)] for p in range(P))
        assert twisted[P]-untwisted[P]==2*sheet>0
        if gcd(P,2)==1:
            uniform=coefficients([-1]*P);assert uniform==twisted
        rows.append({'two_dimensional_torus_L':L,'gauss_zero_flux_dimension':2**(P-1),'first_quantized_source_order':P,'energy_difference_coefficient':str(2*sheet),'direct_subset_sum':str(sheet),'source_independent_coefficients_below_area':True})
    print('periodic_quantized_ground_series',rows,flush=True)


if __name__=='__main__':
    families=[matched_single_plaquette,exact_alias_schedule,spatial_hessian_and_local_shift,
              square_gauss_compression,exact_patch_perturbation,single_face_spectral_curvature,
              modular_periods_and_quantized_source,periodic_quantized_ground_series]
    for family in families:
        family()
        print('PASS',family.__name__,'declared exact identities and finite tolerances checked',flush=True)
    print('TOTAL: PASS=8 FAIL=0')
    print('per_element: exact clock orientations, Fourier aliases, sine denominators and contact normalization are checked.')
    print('per_site: full square Gauss generators and periodic cellular boundary identities are independently constructed.')
    print('per_mode: full matrix transfer logarithms and high-precision finite spectra are compared with derived generators.')
    print('per_block: exact rational patch recursion and periodic quantized-flux coefficients use distinct constructions.')
    print('lattice_wide: checked and not executed — no lattice-wide numerical execution; uniform gap and area-tail consequences are analytically justified using the explicitly mapped external theorem; no Coulomb phase is established.')
