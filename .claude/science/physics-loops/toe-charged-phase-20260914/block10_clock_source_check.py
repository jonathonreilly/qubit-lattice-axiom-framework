"""Personal independent constructions for the supplied finite-clock source."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import gcd
import numpy as np
from scipy.linalg import eigh
import mpmath as mp


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


if __name__=='__main__':
    square_gauss_compression()
    exact_patch_perturbation()
    single_face_spectral_curvature()
    modular_periods_and_quantized_source()
