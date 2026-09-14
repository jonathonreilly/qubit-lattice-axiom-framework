"""Topology and geometry challenges for the provisional periodic proof."""
import itertools,json,math
from pathlib import Path
import numpy as np
from scipy.sparse import csr_matrix,eye,kron
from fractions import Fraction


def close(a,b,tol=2e-10):
    e=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    assert e<tol,(e,tol)
    return e


def periodic_complex(L):
    points=list(itertools.product(range(L),repeat=4))
    cells={k:[(x,I) for x in points for I in itertools.combinations(range(4),k)] for k in range(5)}
    ids={k:{c:i for i,c in enumerate(cells[k])} for k in cells}
    ds=[]
    for k in range(4):
        rows=[];cols=[];vals=[]
        for i,(x,I) in enumerate(cells[k+1]):
            for j,a in enumerate(I):
                J=I[:j]+I[j+1:];y=list(x);y[a]=(y[a]+1)%L;y=tuple(y)
                rows.extend([i,i]);cols.extend([ids[k][(y,J)],ids[k][(x,J)]])
                vals.extend([(-1)**j,-(-1)**j])
        ds.append(csr_matrix((vals,(rows,cols)),shape=(len(cells[k+1]),len(cells[k])),dtype=float))
    return cells,ids,ds


def star(values,k,L,cells,ids):
    result=np.zeros(len(cells[4-k]))
    for value,(x,I) in zip(values,cells[k]):
        J=tuple(j for j in range(4) if j not in I)
        perm=I+J
        sign=(-1)**sum(perm[a]>perm[b] for a in range(4) for b in range(a+1,4))
        y=tuple((x[a]-(a in J))%L for a in range(4))
        result[ids[4-k][(y,J)]]=sign*value
    return result


def star_matrix(k,L,cells,ids):
    rows=[];cols=[];values=[]
    for column,(x,I) in enumerate(cells[k]):
        J=tuple(j for j in range(4) if j not in I);perm=I+J
        sign=(-1)**sum(perm[a]>perm[b] for a in range(4) for b in range(a+1,4))
        y=tuple((x[a]-(a in J))%L for a in range(4))
        rows.append(ids[4-k][(y,J)]);cols.append(column);values.append(sign)
    return csr_matrix((values,(rows,cols)),shape=(len(cells[4-k]),len(cells[k])))


def apply_potential_inverse(r,L):
    # Edge cells are point-major, component-minor. Fourier calculus gives an
    # independent inverse of curl^T curl on its positive range.
    field=np.asarray(r).reshape((L,L,L,L,4))
    hat=np.fft.fftn(field,axes=(0,1,2,3))
    freqs=np.meshgrid(*([2*np.pi*np.fft.fftfreq(L)]*4),indexing='ij')
    # fftfreq gives cycles per site; multiplying by 2pi gives lattice k.
    v=np.stack([np.exp(1j*k)-1 for k in freqs],axis=-1)
    lam=np.sum(abs(v)**2,axis=-1)
    mask=lam>1e-12
    dot=np.sum(v.conj()*hat,axis=-1)
    out=np.zeros_like(hat)
    out[mask]=(hat[mask]-v[mask]*dot[mask,None]/lam[mask,None])/lam[mask,None]
    return np.fft.ifftn(out,axes=(0,1,2,3)).real.reshape(-1)


def torus_checks():
    L=4
    cells,ids,ds=periodic_complex(L);d0,d1,d2,d3=ds
    for a,b in zip(ds[1:],ds[:-1]):
        z=a@b;assert z.nnz==0 or np.max(abs(z.data))==0
    rng=np.random.default_rng(14)
    form=rng.integers(-3,4,len(cells[3])).astype(float)
    primal=d2.T@form
    left=star(primal,2,L,cells,ids)
    right=d1@star(form,3,L,cells,ids)
    # Freeze the convention-fixed sign; choosing it adaptively would not
    # challenge an accidental Hodge sign change.
    sign=-1
    close(left,sign*right)
    full_hodge=star_matrix(2,L,cells,ids)@d2.T+d1@star_matrix(3,L,cells,ids)
    assert full_hodge.nnz==0 or np.max(abs(full_hodge.data))==0
    close(np.dot(form,form),np.dot(star(form,3,L,cells,ids),star(form,3,L,cells,ids)))
    # The two-form Hodge Laplacian is the componentwise scalar Laplacian.
    f=rng.normal(size=len(cells[2]));lap=d1@(d1.T@f)+d2.T@(d2@f)
    shaped=f.reshape((L,L,L,L,6));scalar=np.zeros_like(shaped)
    for a in range(4):scalar+=2*shaped-np.roll(shaped,1,axis=a)-np.roll(shaped,-1,axis=a)
    close(lap,scalar.reshape(-1))
    full_laplacian=d1@d1.T+d2.T@d2-kron(d0.T@d0,eye(6))
    assert full_laplacian.nnz==0 or np.max(abs(full_laplacian.data))==0
    harmonic=np.zeros((len(cells[2]),6))
    for i,(x,I) in enumerate(cells[2]):harmonic[i,list(itertools.combinations(range(4),2)).index(I)]=1/np.sqrt(L**4)
    close(harmonic.T@harmonic,np.eye(6));close(d2@harmonic,0);close(d1.T@harmonic,0)
    # Separated opposite winding loops. They must survive as a PAIR under
    # harmonic averaging even though a single winding loop averages to zero.
    rho=[]
    for y,sgn in [(0,1),(2,-1)]:
        r=np.zeros(len(cells[1]))
        for x in range(L):r[ids[1][((x,y,0,0),(0,))]]=sgn*2*np.pi
        rho.append(r)
    rho=np.array(rho);close(rho@d0.toarray(),0)
    Q=d1.T@d1;diag=Q.diagonal()
    close(diag,np.full(len(diag),6.))
    colors=np.array([I[0]*8+sum((x[b]%2)*2**j for j,b in enumerate(a for a in range(4) if a!=I[0])) for x,I in cells[1]])
    tilde=[];cost=[];selected=[]
    for r in rho:
        weights=[np.sum(r[colors==c]**2) for c in range(32)]
        c=int(np.argmax(weights));sel=np.where((colors==c)&(r!=0))[0]
        u=np.zeros_like(r);u[sel]=r[sel]/diag[sel]
        rt=r-Q@u;close(rt[sel],0);close(d0.T@rt,0)
        tilde.append(rt);cost.append(r@u);selected.extend(sel)
    close(Q[np.ix_(selected,selected)].toarray(),np.diag(diag[selected]))
    tilde=np.array(tilde);cost=np.array(cost)
    phase=rho@rng.normal(size=len(cells[1]));beta=.03;amps=np.array([.4,.5])
    z=amps*np.exp(-beta*cost/2)
    def averaged_integral(freq,amp):
        total=0j;survive=0
        for sig in itertools.product((-1,0,1),repeat=2):
            sig=np.array(sig);r=sig@freq
            winding=r.reshape((L,L,L,L,4)).sum(axis=(0,1,2,3))
            if np.max(abs(winding))>1e-9:continue
            close(d0.T@r,0)
            v=apply_potential_inverse(r,L)
            close(Q@v,r)
            coeff=np.prod(np.where(sig==0,1.,amp/2))
            total+=coeff*np.exp(-beta*(r@v)/2+1j*(sig@phase));survive+=1
        close(total.imag,0)
        return float(total.real),survive
    original,survive=averaged_integral(rho,amps)
    transformed,_=averaged_integral(tilde,z)
    close(original,transformed)
    assert abs(original-1)>1e-3  # dropping all winding factors is wrong
    return dict(side=L,cell_counts={str(k):len(v) for k,v in cells.items()},
                star_codelta_to_curl_sign=sign,harmonic_two_form_rank=6,
                complete_hodge_operator_identity=True,complete_scalar_laplacian_identity=True,
                winding_pair_original=original,winding_pair_renormalized=transformed,
                surviving_harmonic_terms=survive,wrong_winding_drop_error=abs(original-1))


def path_from_corner(x,b):
    cur=list(b);out={}
    for j in range(4):
        while cur[j]<x[j]:
            e=(tuple(cur),j);out[e]=out.get(e,0)+1;cur[j]+=1
    return out


def add(out,inp,scale=1):
    for k,v in inp.items():
        out[k]=out.get(k,0)+scale*v
        if out[k]==0:del out[k]


def plaquette_boundary(x,j,k):
    xj=list(x);xj[j]+=1;xj=tuple(xj)
    xk=list(x);xk[k]+=1;xk=tuple(xk)
    return {(x,j):1,(xj,k):1,(xk,j):-1,(x,k):-1}


def edge_filling(x,j,b):
    result={}
    for k in range(j+1,4):
        for a in range(b[k],x[k]):
            v=tuple(x[l] if l<k else a if l==k else b[l] for l in range(4))
            result[(v,j,k)]=-1
    return result


def homotopy_checks():
    b=(-2,-1,0,1);R=4;count=0;maxarea=0
    for dx in itertools.product(range(R+1),repeat=4):
        x=tuple(a+c for a,c in zip(b,dx))
        for j in range(4):
            if dx[j]>=R:continue
            y=list(x);y[j]+=1;y=tuple(y)
            filling=edge_filling(x,j,b);actual={}
            for (v,a,c),weight in filling.items():add(actual,plaquette_boundary(v,a,c),weight)
            expected={(x,j):1};add(expected,path_from_corner(x,b));add(expected,path_from_corner(y,b),-1)
            assert actual==expected,(x,j,actual,expected)
            area=sum(abs(v) for v in filling.values());assert area<=3*R
            count+=1;maxarea=max(maxarea,area)
    return dict(edge_chain_identities=count,box_side=R,max_filling_area=maxarea)


def constants_check():
    # Integer segment distance, independent of the hand count in the proof.
    reference=[(0,1),(0,0),(0,0),(0,0)];counts=[0]*4
    for origin in itertools.product(range(-3,4),repeat=4):
        for j in range(4):
            intervals=[(origin[a],origin[a]+int(a==j)) for a in range(4)]
            distance2=sum(max(0,A-D,C-B)**2 for (A,B),(C,D) in zip(reference,intervals))
            if distance2<=1:counts[j]+=1
    assert counts==[23,28,28,28]
    assert sum(counts)==107
    # Exact conservative rational arithmetic, separate from the more precise
    # floating evaluation. log3<1.1, log2<.7 follow from lower Taylor sums.
    def exp_lower(x,degree):
        return sum(x**k/math.factorial(k) for k in range(degree+1))
    assert exp_lower(Fraction(11,10),5)>3
    assert exp_lower(Fraction(7,10),4)>2
    beta1_upper=(107*Fraction(11,10)+Fraction(14,10))/36
    assert beta1_upper<Fraction(10,3)
    a_lower=Fraction(2000,384)-Fraction(10,3)
    assert a_lower==Fraction(15,8)
    assert 18*a_lower>48*Fraction(7,10)
    assert Fraction(1+719*Fraction(1,1024),1-7*Fraction(1,1024))<2
    delta_upper=Fraction(3200,3)*8765200/Fraction(2**48)
    assert delta_upper<Fraction(1,1000)
    dual_beta_lower=Fraction(16384**2,64*2000)
    assert dual_beta_lower>2000
    beta1=(107*math.log(3)+math.log(4))/(4*math.pi**2)
    a=2000/384-beta1;q=math.exp(-2*math.pi**2*a)
    S5=q*(1+26*q+66*q*q+26*q**3+q**4)/(1-q)**6
    S6=q*(1+57*q+302*q*q+302*q**3+57*q**4+q**5)/(1-q)**7
    delta=2000*(8503056*S6+262144*S5)/(a*math.e)
    return dict(neighbor_counts_by_orientation=counts,beta1=beta1,
                beta_2000_delta_evaluation=delta,rigorous_delta_upper=str(delta_upper),
                rigorous_dual_beta_lower=str(dual_beta_lower),N=16384,
                qualification='The rational inequalities certify the stated constants only conditional on the analytic ensemble and geometry estimates.')


if __name__=='__main__':
    result=dict(status='personal_torus_geometry_checks_pass',torus=torus_checks(),homotopy=homotopy_checks(),constants=constants_check(),
                limits='No universal small-current lifting or packing proof is inferred from these finite checks; the infinite-volume phase remains provisional.')
    Path(__file__).with_name('BLOCK7_TORUS_GEOMETRY_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
