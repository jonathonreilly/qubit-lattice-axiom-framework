"""Working actual-ice graph transport check; no scientific file inputs."""
from collections import deque
from itertools import combinations,product
from fractions import Fraction
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.linalg import eigh


def geometry(L):
    volume=L**3
    roots=[(x,y,z) for z in range(L) for y in range(L) for x in range(L)]
    def site(r):return r[0]%L+L*(r[1]%L)+L*L*(r[2]%L)
    def edge(r,i):return i*volume+site(r)
    faces=[]
    for r in roots:
        for i,j in combinations(range(3),2):
            ri=list(r);ri[i]+=1;rj=list(r);rj[j]+=1
            ids=[edge(r,i),edge(ri,j),edge(rj,i),edge(r,j)]
            faces.append((r,(i,j),ids,sum(1<<q for q in ids)))
    start=sum(1<<edge(r,i) for r in roots for i in range(3) if r[i]%2)
    return roots,faces,start


def ice_component(L=2):
    roots,faces,start=geometry(L);states=[start];index={start:0};queue=deque([start]);arcs=[]
    while queue:
        state=queue.popleft();x=index[state]
        for f,(r,ij,ids,mask) in enumerate(faces):
            bits=[(state>>q)&1 for q in ids]
            if bits[0]!=bits[2] or bits[1]!=bits[3] or bits[0]==bits[1]:continue
            dest=state^mask
            if dest not in index:index[dest]=len(states);states.append(dest);queue.append(dest)
            y=index[dest];a=(-1)**sum(r)*(2*bits[0]-1)*int(ij==(0,1))
            arcs.append((x,y,f,a))
    edges=np.array([r for r in arcs if r[0]<r[1]],int)
    return roots,faces,states,edges


def graph_data(edges,N):
    x,y,_,a=edges.T;M=len(edges)
    B=sparse.coo_matrix((np.tile([-1,1],M),(np.repeat(np.arange(M),2),np.column_stack([x,y]).ravel())),shape=(M,N)).tocsr()
    lap=(B.T@B).astype(float).tocsr();b=-np.asarray(B.T@a).ravel()
    return B,lap,b,a


def check():
    roots,faces,states,edges=ice_component();N=len(states);B,lap,b,a=graph_data(edges,N)
    print('actual graph',N,len(edges),'source active edges',np.count_nonzero(a),flush=True)
    assert N==864 and len(edges)==3456
    phi=np.zeros(N);phi[1:]=spsolve(lap[1:,1:],b[1:]);assert np.max(abs(lap@phi-b))<1e-11
    d0=2*np.dot(a,a)/N;response=2*np.dot(a+B@phi,a+B@phi)/N
    assert abs(response-(d0-2*b@phi/N))<1e-12
    print('RK curvature',response/8,'direct',d0/8,'corrector max',max(abs(phi)),flush=True)
    rational=None
    for denom in [100,1000,10000,100000,1000000,10000000,100000000]:
        candidate=[Fraction(float(z)).limit_denominator(denom) for z in phi]
        # Exact integer graph-Laplacian action binds any rational reconstruction.
        residual=[Fraction(0) for _ in range(N)]
        for x,y,_,_ in edges:
            diff=candidate[x]-candidate[y];residual[x]+=diff;residual[y]-=diff
        if all(z==int(v) for z,v in zip(residual,b)):
            rational=candidate;print('exact rational corrector denominator bound',denom,flush=True);break
    if rational is not None:
        exact=Fraction(2,N)*(sum(int(z)**2 for z in a)-sum(int(z)*v for z,v in zip(b,rational)))
        print('EXACT RK chi',exact/8,flush=True)
    # Full matrix spectral response is a different computational path.
    x,y,_,a=edges.T
    A=sparse.coo_matrix((np.ones(2*len(edges)),(np.r_[x,y],np.r_[y,x])),shape=(N,N)).toarray()
    degree=np.diag(lap.toarray());H1=sparse.coo_matrix((np.r_[-1j*a,1j*a],(np.r_[x,y],np.r_[y,x])),shape=(N,N)).toarray()
    H2=sparse.coo_matrix((np.r_[a*a,a*a],(np.r_[x,y],np.r_[y,x])),shape=(N,N)).toarray()
    records=[]
    for V in [1.,.95,.9]:
        H=V*np.diag(degree)-A;e,u=eigh(H);psi=u[:,0]
        if psi.sum()<0:psi=-psi
        assert min(psi)>0
        w=psi[x]*psi[y];Lw=(B.T@sparse.diags(w)@B).tocsr();rhs=-B.T@(w*a)
        ph=np.zeros(N);ph[1:]=spsolve(Lw[1:,1:],rhs[1:])
        residual=a+B@ph;variational=2*np.dot(w,residual*residual)
        h1=u[:,1:].conj().T@H1@psi
        spectral=float((psi@H2@psi-2*np.dot(abs(h1)**2,1/(e[1:]-e[0]))).real)
        assert abs(variational-spectral)<1e-11
        current=w*residual;assert max(abs(B.T@current))<1e-12
        dual=2*(np.dot(current,a)**2)/np.dot(current/w,current)
        assert abs(dual-variational)<1e-11
        records.append((V,variational/8,spectral/8,float(e[1]-e[0])))
    print('full spectral/graph responses',records,flush=True)




def exact_rk_certificate():
    import sympy as sp
    _,_,states,edges=ice_component();N=len(states);B,lap,b,a=graph_data(edges,N)
    b=list(map(int,b));vectors=[b]
    def action(v):
        out=[0]*N
        for x,y,_,_ in edges:
            diff=v[x]-v[y];out[x]+=diff;out[y]-=diff
        return out
    for _ in range(6):vectors.append(action(vectors[-1]))
    coeff=[235008,-204608,69072,-11816,1092,-52,1]
    assert all(sum(coeff[j]*vectors[j][x] for j in range(7))==0 for x in range(N))
    phi=[-sum(Fraction(coeff[j]*vectors[j-1][x],coeff[0]) for j in range(1,7)) for x in range(N)]
    assert sum(phi)==0 and action(phi)==b
    current=[Fraction(int(a[e]))+phi[y]-phi[x] for e,(x,y,_,_) in enumerate(edges)]
    divergence=[Fraction(0) for _ in range(N)]
    for value,(x,y,_,_) in zip(current,edges):divergence[x]-=value;divergence[y]+=value
    assert all(z==0 for z in divergence)
    chi=Fraction(2,N*8)*sum(z*z for z in current)
    assert chi==Fraction(28261,99144)
    varphi=sum(z*z for z in phi)/N
    # Sturm root isolation of the exact current-channel polynomial proves all
    # contributing decay rates exceed 3 without assuming the global gap.
    z=sp.Symbol('z');poly=sum(c*z**j for j,c in enumerate(coeff))
    intervals=sp.polys.polytools.intervals(poly,eps=sp.Rational(1,1000))
    assert all(lo>3 and hi<15 and multiplicity==1 for (lo,hi),multiplicity in intervals)
    print('exact_rk_certificate',{'chi':str(chi),'corrector_variance':str(varphi),
          'finite_time_bias_bound_times_t':str(2*varphi),'current_channel_rate_lower_bound':3},flush=True)
    return chi


def reversible_toy_transport():
    from scipy.linalg import expm
    # Weighted triangle plus a parallel geometric edge; nonuniform Perron vector.
    endpoints=np.array([[0,1],[1,2],[0,2],[0,1]])
    J=np.array([.7,1.1,.9,.4]);source=np.array([1.,-2.,.5,-.25]);psi=np.array([1.,2.,3.]);psi/=np.linalg.norm(psi);pi=psi*psi
    x,y=endpoints.T;N=3;B=np.zeros((4,N));B[np.arange(4),x]=-1;B[np.arange(4),y]=1
    w=J*psi[x]*psi[y];Lw=B.T@np.diag(w)@B;L=-np.diag(1/pi)@Lw
    off=np.zeros((N,N));one=np.zeros((N,N));two=np.zeros((N,N))
    for xx,yy,j,a in zip(x,y,J,source):
        off[xx,yy]+=j;off[yy,xx]+=j
        one[xx,yy]+=j*psi[yy]/psi[xx]*a;one[yy,xx]-=j*psi[xx]/psi[yy]*a
        two[xx,yy]+=j*psi[yy]/psi[xx]*a*a;two[yy,xx]+=j*psi[xx]/psi[yy]*a*a
    H=np.diag(off@psi/psi)-off
    assert np.max(abs(H@psi))<1e-14 and np.max(abs(L@np.ones(N)))<1e-14
    assert np.max(abs(pi@L))<1e-14
    b=one@np.ones(N);assert abs(pi@b)<1e-14
    phi=np.zeros(N);phi[1:]=np.linalg.solve(Lw[1:,1:],(pi*b)[1:]);phi-=pi@phi
    assert np.max(abs(-L@phi-b))<1e-14
    d0=2*np.dot(w,source*source);C=2*np.dot(w,(source+B@phi)**2)
    assert abs(C-(d0-2*np.dot(pi*b,phi)))<1e-14
    vals,U=eigh(H);bb=U[:,1:].T@(psi*b);rates=vals[1:]
    previous=float('inf');rows=[]
    zero=np.zeros_like(L)
    generator=np.block([[L,zero,zero],[one,L,zero],[two,2*one,L]])
    for t in [.03,.2,1.,4.,12.]:
        moments=expm(t*generator)@np.r_[np.ones(N),np.zeros(2*N)]
        actual=pi@moments[2*N:]/t
        bias=2/t*np.dot(bb*bb,(1-np.exp(-rates*t))/rates**2)
        assert abs(actual-(C+bias))<1e-12
        assert C<actual<previous and bias<=2*np.dot(pi,phi*phi)/t
        previous=actual;rows.append((t,float(actual),float(bias)))
    # An exact gradient source is flat despite nonzero active jumps.
    f=np.array([.3,-.7,1.2]);gradient=B@f
    assert np.linalg.norm(gradient+B@(-f))<1e-14
    theta=.71;Hg=H.astype(complex)
    for xx in range(N):
        for yy in range(N):
            if xx!=yy:Hg[xx,yy]=0
    for xx,yy,j,a in zip(x,y,J,gradient):Hg[xx,yy]-=j*np.exp(1j*theta*a);Hg[yy,xx]-=j*np.exp(-1j*theta*a)
    D=np.diag(np.exp(-1j*theta*f));assert np.max(abs(Hg-D@H@D.conj().T))<1e-14
    print('reversible_toy_transport',{'exact_curvature':float(C),'finite_time_variance_ratios':rows,
          'gradient_source_response':0},flush=True)


def frozen_cubic_states():
    result=[]
    for L in [2,4,6]:
        roots,faces,_=geometry(L);N=L**3
        electric=np.array([[(-1)**r[1]/2,(-1)**r[2]/2,(-1)**r[0]/2] for r in roots])
        epsilon=np.array([(-1)**sum(r) for r in roots]);occupation=(.5+epsilon[:,None]*electric).astype(int)
        state=sum(int(occupation[q,i])<<(i*N+q) for i in range(3) for q in range(N))
        def site(r):return r[0]%L+L*(r[1]%L)+L*L*(r[2]%L)
        for q,r in enumerate(roots):
            div=0;degree=0
            for i in range(3):
                prev=list(r);prev[i]-=1;j=site(prev)
                div+=electric[q,i]-electric[j,i];degree+=occupation[q,i]+occupation[j,i]
            assert div==0 and degree==3
        flux=[sum(electric[q,i] for q,r in enumerate(roots) if r[i]==0) for i in range(3)]
        assert flux==[0,0,0]
        for r,ij,ids,mask in faces:
            bits=[(state>>q)&1 for q in ids]
            assert not(bits[0]==bits[2] and bits[1]==bits[3] and bits[0]!=bits[1])
        # Each actual local phased RK matrix is positive; the frozen vector
        # has zero support on either alternating word and hence zero energy.
        for theta in [.0,.3,1.2]:
            local=np.array([[1,-np.exp(1j*theta)],[-np.exp(-1j*theta),1]])
            assert np.max(abs(np.linalg.eigvalsh(local)-[0,2]))<1e-14
        result.append({'L':L,'links':3*N,'zero_flux':flux,'flippable_faces':0})
    print('frozen_cubic_states',result,flush=True)



def explicit_membrane_cycles():
    rows=[]
    for L in [2,4,6,8]:
        roots,faces,start=geometry(L);volume=L**3
        for z in range(L):
            selected=[f for f,(r,ij,_,_) in enumerate(faces) if ij==(0,1) and r[2]==z]
            levels={f:(-1)**z*((-1)**faces[f][0][0]-(-1)**faces[f][0][1]) for f in selected}
            ordered=sorted(selected,key=lambda f:-levels[f]);state=start;period=0;chain=np.zeros(len(faces),dtype=int)
            for level in [2,0,-2]:
                layer=[f for f in selected if levels[f]==level];used=set()
                for f in layer:
                    ids=faces[f][2];assert not used.intersection(ids);used.update(ids)
            for f in ordered:
                r,ij,ids,mask=faces[f];bits=[(state>>q)&1 for q in ids]
                assert bits[0]==bits[2] and bits[1]==bits[3] and bits[0]!=bits[1]
                coefficient=(-1)**sum(r)*(2*bits[0]-1);assert coefficient==1
                period+=coefficient;chain[f]+=coefficient;state^=mask
            assert state==start and period==L*L
            boundary=np.zeros(3*volume,dtype=int)
            for f in selected:
                for q,sign in zip(faces[f][2],[1,1,-1,-1]):boundary[q]+=chain[f]*sign
            assert np.max(abs(boundary))==0
        rows.append({'L':L,'disjoint_plane_cycles':L,'moves_per_cycle':L*L,'source_period':L*L,'parallel_layers':3})
    print('explicit_membrane_cycles',rows,flush=True)


if __name__=='__main__':
    check()
    exact_rk_certificate()
    reversible_toy_transport()
    frozen_cubic_states()
    explicit_membrane_cycles()
