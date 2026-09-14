#!/usr/bin/env python3
"""Personal finite challenges for the integer-graded local normal form.

No finite result proves the volume-uniform interaction estimates or a phase.
"""
from itertools import product, combinations
from pathlib import Path
import json
import math
import numpy as np
from scipy.linalg import expm, eigh, eigvalsh
from fractions import Fraction

BASE = Path(__file__).resolve().parent


def principal(a):
    return (np.asarray(a) + 1) % 3 - 1


def geometry(shape, periodic=False):
    vertices = list(product(*(range(n if periodic else n+1) for n in shape)))
    def shift(x, a):
        y = list(x); y[a] += 1
        if periodic: y[a] %= shape[a]
        return tuple(y)
    edges = [(a,x) for x in vertices for a in range(3) if periodic or x[a]<shape[a]]
    faces = [(aa,x) for x in vertices for aa in combinations(range(3),2)
             if periodic or all(x[a]<shape[a] for a in aa)]
    cubes = list(product(*(range(n) for n in shape)))
    ei={v:i for i,v in enumerate(edges)}; fi={v:i for i,v in enumerate(faces)}
    vi={v:i for i,v in enumerate(vertices)}
    F=np.zeros((len(faces),len(edges)),dtype=np.int16)
    D=np.zeros((len(cubes),len(faces)),dtype=np.int16)
    G=np.zeros((len(edges),len(vertices)),dtype=np.int16)
    for p,((a,b),x) in enumerate(faces):
        for edge,sign in [((a,x),1),((b,shift(x,a)),1),((a,shift(x,b)),-1),((b,x),-1)]:
            F[p,ei[edge]] += sign
    for c,x in enumerate(cubes):
        for a in range(3):
            aa=tuple(b for b in range(3) if b!=a)
            D[c,fi[aa,shift(x,a)]] += (-1)**a
            D[c,fi[aa,x]] -= (-1)**a
    for l,(a,x) in enumerate(edges):
        G[l,vi[shift(x,a)]]=1; G[l,vi[x]]=-1
    assert not np.any(D@F) and not np.any(F@G)
    return F,D,G,edges,faces,cubes


def geometry_and_grade_locality():
    F,D,G,edges,faces,cubes=geometry((4,4,4),True)
    face_edge=(F!=0).astype(np.int16)
    cube_face=(D!=0).astype(np.int16)
    cube_edge=(cube_face@face_edge)>0
    assert np.all(cube_edge.sum(axis=1)==12)
    assert np.all(cube_edge.sum(axis=0)==4)
    stars=[]
    for l in range(len(edges)):
        adjacent=np.flatnonzero(cube_edge[:,l])
        star=np.flatnonzero(np.any(cube_edge[adjacent],axis=0))
        assert len(adjacent)==4 and len(star)==33
        stars.append(star)
    anchor_count=np.bincount(np.concatenate(stars),minlength=len(edges))
    assert np.all(anchor_count==33)
    # A volume average cannot be read as an individual-cube statement.
    impulse=np.zeros(len(edges),dtype=np.int16)
    impulse[np.flatnonzero(F[0]>0)]=1
    impulse_charge=(D@principal(F@impulse))//3
    assert np.sum(impulse_charge**2)==2 and max(abs(impulse_charge))==1
    rng=np.random.default_rng(140921)
    a=rng.integers(0,3,size=(768,len(edges)),dtype=np.int16)
    b=principal(a@F.T); Q=(b@D.T)//3
    assert not np.any((b@D.T)%3) and np.max(np.abs(Q))<=2
    rows=[]; grades=set(); max_delta_q=0
    for l in [0,1,2,17,83,191]:
        adjacent=np.flatnonzero(cube_edge[:,l]); outside=np.setdiff1d(np.arange(len(cubes)),adjacent)
        for sign in [-1,1]:
            ap=a.copy();ap[:,l]=(ap[:,l]+sign)%3
            bp=principal(ap@F.T)
            qp=(bp@D.T)//3
            mismatch=(bp-b-sign*F[:,l])//3
            assert np.array_equal(bp-b-sign*F[:,l],3*mismatch)
            assert np.array_equal(qp-Q,mismatch@D.T)
            assert np.array_equal(qp[:,outside],Q[:,outside])
            delta=np.sum(qp*qp-Q*Q,axis=1)
            local=np.sum(qp[:,adjacent]**2-Q[:,adjacent]**2,axis=1)
            assert np.array_equal(delta,local) and max(abs(delta))<=16
            mu=.8;rates=np.exp(-mu*np.sum(mismatch*mismatch,axis=1))
            assert max(rates[delta!=0])<=math.exp(-mu)+1e-15
            grades.update(map(int,delta));max_delta_q=max(max_delta_q,int(np.max(abs(qp-Q))))
            # Outside-star coordinate changes cannot alter the initial grade or weight.
            aa=a.copy();other=np.setdiff1d(np.arange(len(edges)),stars[l])
            aa[:,other]=rng.integers(0,3,size=(len(a),len(other)))
            bb=principal(aa@F.T);qq=(bb@D.T)//3
            aa[:,l]=(aa[:,l]+sign)%3
            bbb=principal(aa@F.T);qqq=(bbb@D.T)//3
            mm=(bbb-bb-sign*F[:,l])//3
            assert np.array_equal(mm,mismatch)
            assert np.array_equal(np.sum(qqq*qqq-qq*qq,axis=1),delta)
            rows.append(dict(link=l,sign=sign,observed_grades=sorted(set(map(int,delta)))))
    return dict(torus_shape=[4,4,4],links=len(edges),cubes=len(cubes),star_links=33,
                stars_per_link=33,cubes_per_link=4,samples_per_update=len(a),
                tested_updates=len(rows),observed_grades=sorted(grades),
                maximum_observed_charge_change=max_delta_q,
                nontranslation_invariant_control=dict(total_charge_square=2,mean_charge_square=2/len(cubes),maximum_cube_charge_square=1))


def cube_model(t=.7,mu=.8,K=.4):
    F,D,G,edges,faces,cubes=geometry((1,1,1))
    states=np.array([b for b in product([-1,0,1],repeat=6) if (D@np.array(b)).item()%3==0],dtype=np.int16)
    index={tuple(b):i for i,b in enumerate(states)}
    Q=(states@D.T).ravel()//3; N=Q*Q
    B=np.diag(1.5*K*np.sum(states*states,axis=1))
    hops=[]
    for l in range(len(edges)):
        for sign in [-1,1]:
            hop=np.zeros_like(B)
            for j,b in enumerate(states):
                bp=principal(b+sign*F[:,l]);i=index[tuple(bp)]
                m=(bp-b-sign*F[:,l])//3
                hop[i,j]=-t*math.exp(-mu*int(m@m))
            B+=hop;hops.append(hop)
    assert len(states)==243 and np.max(abs(B-B.T))<1e-14
    # All original clock configurations independently certify the full gauge fibers.
    coord=np.array(list(product(range(3),repeat=12)),dtype=np.int16)
    flux=principal(coord@F.T)
    keys=(flux+1)@(3**np.arange(6))
    unique,counts=np.unique(keys,return_counts=True)
    assert len(unique)==243 and set(counts)=={3**7}
    grades=N[:,None]-N[None,:]
    parts={r:np.where(grades==r,B,0.) for r in np.unique(grades)}
    assert np.max(abs(sum(parts.values())-B))<1e-14
    for r,part in parts.items():
        assert np.max(abs(N[:,None]*part-part*N[None,:]-r*part))<1e-14
        assert np.max(abs(part.T-parts[-r]))<1e-14
    return B,N,Q,states,grades,parts,dict(full_coordinate_count=len(coord),physical_count=len(states),gauge_fiber=3**7)


def matrix_normal_form():
    B,N,Q,states,grades,parts,fiber=cube_model()
    p=np.flatnonzero(N==0); q=np.flatnonzero(N>0)
    B0=parts[0];off=B-B0
    inverse=np.divide(off,grades,out=np.zeros_like(B),where=grades!=0)
    assert np.max(abs(inverse+inverse.T))<1e-14
    assert np.max(abs(inverse*N[None,:]-N[:,None]*inverse+off))<1e-14
    C=-B[np.ix_(p,q)]@np.diag(1/N[q])@B[np.ix_(q,p)]
    comm=inverse@off-off@inverse
    assert np.max(abs(C-.5*comm[np.ix_(p,p)]))<1e-12
    assert eigvalsh(C)[-1]<1e-12 and eigvalsh(C)[0]<-1e-4
    # Rebuild the constrained hopping from unwrapped partial shifts. A
    # squared reverse shift is a distinct finite-mu term, not a first hop.
    F,D,G,edges,faces,cubes=geometry((1,1,1))
    lookup={tuple(b):i for i,b in enumerate(states)}
    projected_model=np.diag(1.5*.4*np.sum(states*states,axis=1))
    double_terms=np.zeros_like(B)
    for l in range(len(edges)):
        Z=np.zeros_like(B)
        for j,b in enumerate(states):
            bp=b+F[:,l]
            if max(abs(bp))<=1:Z[lookup[tuple(bp)],j]=1
        degree=int(np.count_nonzero(F[:,l]))
        double=math.exp(-degree*.8)*(Z@Z+Z.T@Z.T)
        projected_model-=.7*(Z+Z.T+double);double_terms+=double
    constrained_error=float(np.max(abs((projected_model-B)[np.ix_(p,p)])))
    assert constrained_error<2e-14
    assert np.linalg.norm(double_terms[np.ix_(p,p)],2)>1
    # The full neutral constraint space is locally distinguishable. It is
    # not automatically a locally topologically ordered ground code.
    observable=states[p,0]**2
    assert min(observable)==0 and max(observable)==1
    eval0,evec0=eigh(B[np.ix_(p,p)]); phi=np.zeros(len(N));phi[p]=evec0[:,0]
    correction=float(phi[p]@C@phi[p])
    kinetic=B-np.diag(1.5*.4*np.sum(states*states,axis=1))+2*.7*12*np.eye(len(N))
    assert eigvalsh(kinetic)[0]>=-1e-13
    rows=[]
    for lam in [32.,64.,128.,256.]:
        H=lam*np.diag(N)+B
        S=inverse/lam;U=expm(S);rot=U@H@U.T
        projected=rot[np.ix_(p,p)]
        residual=float(np.linalg.norm(projected-B[np.ix_(p,p)]-C/lam,2))
        vals,vec=eigh(H);ground=vec[:,0]
        leakage=float(np.dot(N*ground,ground))
        assert vals[0]<=1e-13
        assert leakage<=2*.7*12/lam+1e-13
        uall=np.eye(len(N)); current=H.copy(); offnorm=[]
        for iteration in range(4):
            V=np.where(grades!=0,current,0.)
            offnorm.append(float(np.linalg.norm(V,2)))
            generator=np.divide(V,lam*grades,out=np.zeros_like(V),where=grades!=0)
            transform=expm(generator)
            current=transform@current@transform.T;uall=transform@uall
        offnorm.append(float(np.linalg.norm(np.where(grades!=0,current,0.),2)))
        assert max(abs(uall@uall.T-np.eye(len(N))).ravel())<3e-13
        rotation_error=float(np.max(abs(current-uall@H@uall.T)))
        rotation_scale=float(np.linalg.norm(H,2))
        # The exact identity is checked relatively to the energy scale, since
        # four independent dense conjugations accumulate floating roundoff.
        assert rotation_error<2e-14*rotation_scale
        assert all(offnorm[j+1]<offnorm[j] for j in range(4))
        # A prepared dressed neutral state; no claim it is the actual ground state.
        psi=uall.T@phi; Ntilde=uall.T@np.diag(N)@uall
        V=np.where(grades!=0,current,0.)
        commnorm=float(np.linalg.norm(N[:,None]*V-V*N[None,:],2))
        times=[]
        for time in [0.,.05,.2,1.]:
            psit=vec@(np.exp(-1j*time*vals)*(vec.T@psi))
            dressed=float(np.vdot(psit,Ntilde@psit).real)
            bare=float(np.dot(abs(psit)**2,(N>0)))
            assert dressed>=-2e-13 and dressed<=commnorm*time+3e-12
            times.append(dict(time=time,dressed_charge_square=dressed,bare_defect_probability=bare,exact_commutator_bound=commnorm*time))
        rows.append(dict(penalty=lam,neutral_dimension=len(p),first_projected_remainder=residual,
                         scaled_projected_remainder=lam*lam*residual,ground_energy=float(vals[0]),
                         ground_first_energy_prediction=float(eval0[0]+correction/lam),
                         ground_charge_square=leakage,scaled_ground_charge_square=lam*lam*leakage,
                         rotation_identity_error=rotation_error,rotation_energy_scale=rotation_scale,
                         finite_matrix_off_norms=offnorm,prepared_state_times=times))
    assert rows[-1]['first_projected_remainder'] < rows[0]['first_projected_remainder']/40
    assert rows[-1]['ground_charge_square'] < rows[0]['ground_charge_square']/35
    k0=1/33;g=66*.7*(1+32*math.exp(-.8))*math.exp(33*k0)+6*.4*math.exp(4*k0)
    return dict(fiber_certificate=fiber,nonzero_hopping_grades=[int(r) for r,v in parts.items() if np.any(v)],
                second_effective_correction_minimum_eigenvalue=float(eigvalsh(C)[0]),
                projected_harmonic_identity_error=constrained_error,
                neutral_local_observable_spectrum=sorted(set(map(int,observable))),
                conservative_normal_form_penalty_threshold=128*g/k0,
                finite_matrix_scope='Moderate penalties below the conservative uniform-theorem threshold; these check identities and coefficients only.',checks=rows)


def equal_penalty_is_not_equal_charge():
    F,D,G,edges,faces,cubes=geometry((2,1,1))
    allstates=np.array(list(product([-1,0,1],repeat=11)),dtype=np.int16)
    states=allstates[np.all((allstates@D.T)%3==0,axis=1)]
    Q=(states@D.T)//3;N=np.sum(Q*Q,axis=1)
    witness=None
    for l in range(len(edges)):
        for sign in [-1,1]:
            bp=principal(states+sign*F[:,l]);qp=(bp@D.T)//3
            mask=(np.sum(qp*qp,axis=1)==N)&np.any(qp!=Q,axis=1)
            if np.any(mask):
                j=int(np.flatnonzero(mask)[0]);m=(bp[j]-states[j]-sign*F[:,l])//3
                witness=dict(link=l,sign=sign,before=states[j].tolist(),after=bp[j].tolist(),
                             charge_before=Q[j].tolist(),charge_after=qp[j].tolist(),
                             penalty=int(N[j]),mismatch=m.tolist())
                break
        if witness:break
    assert witness is not None
    return dict(physical_flux_states=len(states),witness=witness,qualification='Grade zero preserves total Q squared, not each cube charge.')


def logical_controls():
    false_vacua=[]
    for lam,h in [(10,1),(100,1),(1000,1)]:
        L=2*(lam//h+1);field=np.r_[np.ones(L//2,dtype=int),-np.ones(L//2,dtype=int)]
        # Exact dynamic programming for every classical chain configuration.
        energy={s:-h*field[0]*s for s in [-1,1]}
        for f in field[1:]:
            energy={s:min(energy[old]+lam*(old!=s)-h*f*s for old in [-1,1]) for s in [-1,1]}
        ground=min(energy.values());matched=lam-h*L
        assert ground==matched<0 and sum(field)==0
        false_vacua.append(dict(length=L,penalty=lam,local_field=h,neutral_energy=0,
                                exact_ground_energy=int(ground),one_wall_trial_energy=int(matched),normal_form_remainder=0))
    lam,eps=100.,1.
    H=np.array([[0.,-eps],[-eps,lam]])
    vals,vec=eigh(H);p=float(vec[1,0]**2)
    formula=(1-lam/math.sqrt(lam*lam+4*eps*eps))/2
    assert abs(p-formula)<1e-16
    global_fidelity=math.exp(1_000_000*math.log1p(-p))
    assert p<.00011 and global_fidelity<1e-40
    return dict(false_vacua=false_vacua,local_vs_global_rotation=dict(single_site_bare_probability=p,
                sites=1_000_000,global_neutral_fidelity=global_fidelity),
                qualification='Controls outside the cubic clock model. Small local rotations and exact constraint conservation do not imply global fidelity or ground-sector selection.')


def local_algebra_checks():
    # Independent Lie-Schwinger integral versus full matrix conjugation.
    rng=np.random.default_rng(92314)
    N=np.arange(4,dtype=float);grade=N[:,None]-N[None,:]
    x=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4));B=(x+x.conj().T)/8
    D=np.diag(np.diag(B));V=B-D
    nodes,weights=np.polynomial.legendre.leggauss(24)
    results=[]
    for lam in [8.,16.,32.]:
        S=np.divide(V,lam*grade,out=np.zeros_like(V),where=grade!=0)
        assert np.linalg.norm(S+S.conj().T)<1e-14
        H=lam*np.diag(N)+B;U=expm(S)
        R=U@H@U.conj().T-lam*np.diag(N)-D
        comm=S@V-V@S
        integral=np.zeros_like(V)
        for z,w in zip(nodes,weights):
            u=(z+1)/2;uu=expm(u*S)
            integral+=w/2*u*(uu@comm@uu.conj().T)
        independent=U@D@U.conj().T-D+integral
        error=float(np.linalg.norm(R-independent,2))
        bound=float(np.linalg.norm(S@D-D@S,2)+.5*np.linalg.norm(comm,2))
        assert error<3e-14 and np.linalg.norm(R,2)<=bound+1e-14
        results.append(dict(penalty=lam,integral_identity_error=error,remainder_norm=float(np.linalg.norm(R,2)),unitary_commutator_bound=bound))
    # Exact endpoint values of the monotone majorants in the analytic proof.
    assert Fraction(16,128-16)==Fraction(1,7)
    assert Fraction(4*(2+1),32-4)==Fraction(3,7)<Fraction(1,2)
    I=np.eye(2);X=np.array([[0,1],[1,0]],complex);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1.])
    def tensor(ops):
        out=np.array([[1]],complex)
        for op in ops:out=np.kron(out,op)
        return out
    def local(word,size):return tensor([word.get(i,I) for i in range(size)])
    def interaction_norm(terms,k,size):
        return max(sum(math.exp(k*len(support))*np.linalg.norm(value,2) for support,value in terms if i in support) for i in range(size))
    aa=[({0,1},.7*local({0:X,1:X},3)),({2},.2*local({2:Z},3)),({1,2},.4*local({1:Y,2:Y},3))]
    bb=[({0},.3*local({0:Z},3)),({1,2},.5*local({1:X,2:Z},3)),({0,1,2},.2*local({0:Y,1:Y,2:X},3))]
    cc=[(a|b,av@bv-bv@av) for a,av in aa for b,bv in bb if a&b]
    k,delta=.2,.1
    lhs=interaction_norm(cc,k-delta,3)
    rhs=4/(math.e*delta)*interaction_norm(aa,k,3)*interaction_norm(bb,k,3)
    assert lhs<=rhs
    # The support factor cannot be deleted: [sum Z_i, product X_i]
    # has norm 2q. Verify with a separate dense Clifford representation.
    size=6;sumz=sum(local({i:Z},size) for i in range(size));prodX=tensor([X]*size)
    exact_norm=float(np.linalg.norm(sumz@prodX-prodX@sumz,2))
    assert abs(exact_norm-2*size)<1e-13 and exact_norm>4
    # Local-conjugation and a direct conditional-expectation tail check.
    alpha=.001
    ss=[({i,i+1},1j*alpha*local({i:Z,i+1:X},size)) for i in range(size-1)]
    generator=sum(v for support,v in ss);snorm=interaction_norm(ss,k,size)
    U=expm(generator);O=local({0:Z},size);rotated=U.conj().T@O@U
    # Use X at site zero so that the first oriented bond actually acts.
    O=local({0:X},size);rotated=U.conj().T@O@U
    change=float(np.linalg.norm(rotated-O,2));assert change<=2*snorm
    gamma=4*snorm/delta;assert gamma<1
    tails=[]
    for radius in range(4):
        keep=2**(radius+1);rest=2**(size-radius-1)
        reduced=np.trace(rotated.reshape(keep,rest,keep,rest),axis1=1,axis2=3)/rest
        localpart=np.kron(reduced,np.eye(rest))
        error=float(np.linalg.norm(rotated-localpart,2))
        bound=2*gamma/(1-gamma)*math.exp(k)*math.exp(-(k-delta)*radius)
        assert error<=bound
        tails.append(dict(radius=radius,conditional_expectation_tail=error,analytic_tail_bound=bound))
    assert tails[2]['conditional_expectation_tail']<tails[0]['conditional_expectation_tail']/1e5
    return dict(lie_schwinger_integral=results,commutator_interaction_norm=lhs,commutator_majorant=rhs,
                exact_overlap_control_norm=exact_norm,local_conjugation_change=change,local_change_bound=2*snorm,
                finite_chain_tails=tails,iteration_majorants=['1/7','3/7'])


def main():
    import time
    start=time.monotonic()
    result=dict(status='author_finite_checks',geometry_and_grade_locality=geometry_and_grade_locality(),
                matrix_normal_form=matrix_normal_form(),equal_penalty_control=equal_penalty_is_not_equal_charge(),
                logical_controls=logical_controls(),local_algebra=local_algebra_checks(),qualification='Finite falsifiers and matrix checks. The uniform estimates require the analytic proof; no ground-phase or native-axiom inference.')
    result['seconds']=time.monotonic()-start
    (BASE/'BLOCK9_INTEGER_NORMAL_FORM_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
