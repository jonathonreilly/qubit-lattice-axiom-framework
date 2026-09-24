#!/usr/bin/env python3
"""Independent finite-battery and CP-step controls; no imported model builders.

The exact rational controls certify finite block unitarity, conservation, and
composition. Numerical controls exercise the reference-uniform proof, retained
reservoir correlations, and the complete sixteen-state microscopic star.
"""
from __future__ import annotations
import hashlib
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path
import sys
import numpy as np
from scipy.linalg import expm

HERE = Path(__file__).resolve().parent
FALLBACK = Path('/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude/science/mobile-record-formation-20260920/campaign12h_fourth')


def locate(relative):
    for root in (HERE.parent, FALLBACK):
        p = root / relative
        if p.is_file():
            return p
    raise FileNotFoundError(relative)


def authenticate():
    paths = {
        'microscopic_birth_energy_author/EXACT_MICROSCOPIC_ENERGY_AT_A_STAR_BIRTH.md': '41408b6da165147fec4ce48e4ce2b063daeda2d42d939ced0fe7927b54c4e32c',
        'microscopic_birth_energy_extension_author/FINITE_TIME_STAR_ENERGY_AND_SUPPLY_BOUND.md': 'f118d1fc459bafedd535cec6e7e22aaf940f4c89aae7260fb16017f0493d03d5',
        'microscopic_birth_energy_independent/FINAL_COMPARISON_SEAL.json': '7b01f616bb45c9374f770bb61ede83cfe8dbc24bf51a3771b8ed4e37cad29b50',
    }
    for relative, expected in paths.items():
        actual = hashlib.sha256(locate(relative).read_bytes()).hexdigest()
        assert actual == expected, (relative, actual)
    return paths


def opnorm(a):
    return float(np.linalg.norm(a, 2))


def trace_norm(a):
    return float(np.sum(np.linalg.svd(a, compute_uv=False)))


def sine(L):
    return np.sqrt(2 / (L + 1)) * np.sin(np.pi * np.arange(1, L + 1) / (L + 1))


def grid_lift(U, energies, L):
    d = max(energies)
    M = 2 * d + L - 1
    nr = M + 1
    na = len(energies)
    V = np.eye(na * nr, dtype=complex)
    for total in range(d, M + 1):
        inds = [a * nr + total - m for a, m in enumerate(energies)]
        V[np.ix_(inds, inds)] = U
    eta = np.zeros(nr)
    eta[d:d + L] = sine(L)
    energy = np.array([m + n for m in energies for n in range(nr)])
    return V, eta, energy


def vector_lift(U, labels, L):
    r = len(labels[0])
    ns = list(itertools.product(range(L + 2), repeat=r))
    lookup = {n:i for i,n in enumerate(ns)}
    nr = len(ns)
    V = np.eye(len(labels) * nr, dtype=complex)
    for q in itertools.product(range(1, L + 2), repeat=r):
        inds = [a * nr + lookup[tuple(qi - ki for qi, ki in zip(q, k))] for a, k in enumerate(labels)]
        V[np.ix_(inds, inds)] = U
    eta = np.array([math.prod(sine(L)[ni - 1] if 1 <= ni <= L else 0 for ni in n) for n in ns])
    charges = np.array([tuple(ki + ni for ki, ni in zip(k, n)) for k in labels for n in ns])
    return V, eta, charges


def rational_mul(a, b, n):
    brow = {}
    for (i,j),v in b.items():
        brow.setdefault(i, []).append((j,v))
    out = {}
    for (i,k),v in a.items():
        for j,w in brow.get(k, []):
            out[i,j] = out.get((i,j), Q(0)) + v*w
    return {k:v for k,v in out.items() if v}


def rational_transpose(a):
    return {(j,i):v for (i,j),v in a.items()}


def rational_lift(U, labels, L, vector):
    r = len(labels[0])
    if vector:
        ns = list(itertools.product(range(L + 2), repeat=r))
        complete = list(itertools.product(range(1, L + 2), repeat=r))
    else:
        d = max(k[0] for k in labels)
        M = 2*d + L - 1
        ns = [(n,) for n in range(M+1)]
        complete = [(q,) for q in range(d, M+1)]
    lookup = {n:i for i,n in enumerate(ns)}
    nr = len(ns); dim = len(labels)*nr
    V = {(i,i):Q(1) for i in range(dim)}
    for q in complete:
        inds = [a*nr+lookup[tuple(qi-ki for qi,ki in zip(q,k))] for a,k in enumerate(labels)]
        for i in inds:
            del V[i,i]
        for (a,b),val in U.items():
            if val:
                V[inds[a], inds[b]] = val
    charges = [tuple(ki+ni for ki,ni in zip(k,n)) for k in labels for n in ns]
    return V, charges, dim


def exact_controls():
    results = []
    for vector in (False, True):
        if vector:
            labels = [(0,0),(1,0),(0,1)]
            U1 = {(0,0):Q(3,5),(0,1):Q(-4,5),(1,0):Q(4,5),(1,1):Q(3,5),(2,2):Q(1)}
            U2 = {(0,0):Q(1),(1,1):Q(5,13),(1,2):Q(-12,13),(2,1):Q(12,13),(2,2):Q(5,13)}
        else:
            labels = [(0,),(2,)]
            U1 = {(0,0):Q(3,5),(0,1):Q(-4,5),(1,0):Q(4,5),(1,1):Q(3,5)}
            U2 = {(0,0):Q(5,13),(0,1):Q(-12,13),(1,0):Q(12,13),(1,1):Q(5,13)}
        V1,charges,n = rational_lift(U1,labels,3,vector)
        V2,_,_ = rational_lift(U2,labels,3,vector)
        VV,_,_ = rational_lift(rational_mul(U2,U1,len(labels)),labels,3,vector)
        assert rational_mul(rational_transpose(V1),V1,n)=={(i,i):Q(1) for i in range(n)}
        assert rational_mul(V2,V1,n)==VV
        assert all(charges[i]==charges[j] for (i,j),v in V1.items() if v)
        results.append({'model':'vector charges, physical levels 0,1,sqrt(2)' if vector else 'integer levels 0,2',
                        'arithmetic':'fractions.Fraction; exact equality, no numerical tolerance',
                        'dimension':n,'nonzero_entries':len(V1),'unitarity':True,'charge_conservation':True,'composition':True})
    return results


def haar(n, rng):
    x = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    q,r = np.linalg.qr(x)
    return q @ np.diag(np.diag(r)/np.abs(np.diag(r)))


def battery_controls():
    rng = np.random.default_rng(91827)
    rows = []
    for energies in ([0,1],[0,0,2],[0,1,3]):
        U = haar(len(energies),rng)
        for L in (3,7,15,31):
            V,eta,total = grid_lift(U,energies,L)
            embedding = np.kron(np.eye(len(energies)),eta[:,None])
            error = opnorm(V@embedding-embedding@U)
            c = 2*math.sin(math.pi/(2*(L+1)))
            assert error <= 2*max(energies)*c+2e-12
            unitary = float(np.linalg.norm(V.conj().T@V-np.eye(len(V))))
            conservation = float(np.linalg.norm((total[:,None]-total[None,:])*V))
            assert unitary < 2e-12 and conservation == 0
            rows.append({'energies':energies,'L':L,'reservoir_dimension':len(eta),'isometry_error':error,'isometry_bound':2*max(energies)*c,'unitarity_frobenius_error':unitary,'conservation_frobenius_error':conservation})
    labels=[(0,0),(1,0),(0,1)]
    U=haar(3,rng)
    vectorrows=[]
    for L in (3,7,15):
        V,eta,charges=vector_lift(U,labels,L)
        embedding=np.kron(np.eye(3),eta[:,None])
        error=opnorm(V@embedding-embedding@U)
        c=2*math.sin(math.pi/(2*(L+1)))
        total=charges@np.array([1.0,math.sqrt(2)])
        conservation=float(np.linalg.norm((total[:,None]-total[None,:])*V))
        assert error<=2*c+2e-12 and conservation==0
        vectorrows.append({'levels':[0,1,'sqrt(2)'],'L':L,'reservoir_dimension':len(eta),'isometry_error':error,'isometry_bound':2*c,'physical_energy_conservation_error':conservation})
    return {'integer_grid':rows,'arbitrary_spectrum':vectorrows}


def embed_two_qubit(U, which, n=3):
    out=np.zeros((2**n,2**n),complex)
    for col in range(2**n):
        bits=[(col>>(n-1-i))&1 for i in range(n)]
        inc=2*bits[which[0]]+bits[which[1]]
        for rowlocal in range(4):
            obits=bits.copy();obits[which[0]]=rowlocal//2;obits[which[1]]=rowlocal%2
            row=sum(bit<<(n-1-i) for i,bit in enumerate(obits))
            out[row,col]=U[rowlocal,inc]
    return out


def partial_rho(state, na, nr):
    psi=state.reshape(na,nr)
    return psi@psi.conj().T,psi.T@psi.conj()


def dephase_flags(rho, na=8, nref=2):
    out=rho.copy()
    for i in range(na*nref):
        for j in range(na*nref):
            if (i//nref)%4 != (j//nref)%4:
                out[i,j]=0
    return out


def sequential_control():
    rng=np.random.default_rng(77291)
    U1=embed_two_qubit(haar(4,rng),(0,1))
    U2=embed_two_qubit(haar(4,rng),(0,2))
    energies=[0]*4+[1]*4
    L=21
    V1,eta,_=grid_lift(U1,energies,L)
    V2,_,_=grid_lift(U2,energies,L)
    V12,_,_=grid_lift(U2@U1,energies,L)
    comp=float(np.linalg.norm(V2@V1-V12))
    assert comp<1e-12
    nr=len(eta)
    input_a=np.zeros(8,complex);input_a[0]=input_a[4]=1/math.sqrt(2)
    first=V1@np.kron(input_a,eta)
    ra,rr=partial_rho(first,8,nr)
    purity=float(np.trace(rr@rr).real)
    correlation=trace_norm(np.outer(first,first.conj())-np.kron(ra,rr))
    assert purity<0.99999 and correlation>1e-4
    # A, R, external reference order. Input S-reference maximally entangled,
    # both fresh zero-energy flags initially 0.
    psi=np.zeros((8,nr,2),complex)
    psi[0,:,0]=eta/math.sqrt(2);psi[4,:,1]=eta/math.sqrt(2)
    actual=(V2@V1@psi.reshape(8*nr,2)).reshape(8,nr,2)
    ideal=np.einsum('ab,brx->arx',U2@U1,psi)
    actual_ar=np.einsum('arx,bry->axby',actual,actual.conj()).reshape(16,16)
    ideal_ar=np.einsum('arx,bry->axby',ideal,ideal.conj()).reshape(16,16)
    history_error=trace_norm(dephase_flags(actual_ar)-dephase_flags(ideal_ar))
    joint_error=trace_norm(np.outer(actual.ravel(),actual.ravel().conj())-np.outer(ideal.ravel(),ideal.ravel().conj()))
    bound=min(2,8*math.sin(math.pi/(2*(L+1))))
    assert history_error<=joint_error+1e-12 and joint_error<=bound+1e-12
    return {'L':L,'flags':2,'reference_dimension':2,'composition_frobenius_error':comp,'reservoir_purity_after_first_gate':purity,'system_flags_reservoir_correlation_trace_norm':correlation,'joint_reference_trace_error':joint_error,'complete_discrete_flag_history_trace_error':history_error,'uniform_trace_bound':bound,'resets_used':False}


def build_star():
    states=[q for q in itertools.product((-1,0,1),repeat=4) if sum(q)==1]
    assert len(states)==16
    loc={q:i for i,q in enumerate(states)}
    F=np.zeros((16,16));W=np.diag([q[0]==0 for q in states]).astype(float)
    jumps=[]
    for b in range(1,4):
        for sigma in (-1,1):
            j=np.zeros((16,16))
            for q,i in loc.items():
                if q[0]==q[b]==0:
                    qq=list(q);qq[0]=sigma;qq[b]=-sigma
                    j[loc[tuple(qq)],i]=1
            jumps.append(j)
    for q,i in loc.items():
        if q[0]:
            for b in range(1,4):
                if q[b]==0:
                    qq=list(q);qq[b]=q[0];qq[0]=0
                    F[loc[tuple(qq)],i]+=1
    assert np.array_equal(W@F,F)
    gamma=sum(j.T@j for j in jumps)
    W1=np.diag([q[0]==0 and sum(v!=0 for v in q)==1 for q in states])
    assert np.array_equal(gamma,4*W1)
    assert all(np.array_equal(j@k,np.zeros((16,16))) for j in jumps for k in jumps)
    return states,F,W,jumps


def dissipator_super(Ls):
    n=len(Ls[0]);I=np.eye(n)
    G=sum(L.conj().T@L for L in Ls)
    return sum(np.kron(L.conj(),L) for L in Ls)-0.5*(np.kron(I,G)+np.kron(G.T,I))


def super_to_choi(S,n):
    choi=np.zeros((n*n,n*n),complex)
    for i in range(n):
        for j in range(n):
            E=np.zeros((n,n));E[i,j]=1
            out=(S@E.reshape(-1,order='F')).reshape(n,n,order='F')
            choi[i*n:(i+1)*n,j*n:(j+1)*n]=out
    return choi


def cp_step(H,Ls,tau):
    G=sum(L.conj().T@L for L in Ls)
    eig,Qm=np.linalg.eigh(np.eye(len(H))-tau*G)
    assert eig.min()>-1e-12
    root=(Qm*np.sqrt(np.maximum(eig,0)))@Qm.conj().T
    U=expm(-1j*tau*H)
    Ks=[U@root]+[math.sqrt(tau)*U@L for L in Ls]
    return Ks,root,G


def star_controls():
    states,F,W,js=build_star()
    rows=[];spectra=[]
    for S in (1,2,3):
        C=S*(S+1);eps=1/math.sqrt(C);K=0.7;kappa=0.4
        H=K*C*C*(W-eps*F).T@(W-eps*F)
        vals=np.linalg.eigvalsh(H)
        expected=np.array([0]*10+[K*C*C]*2+[K*(C*C+3*C)]*4)
        spectral_error=float(np.max(np.abs(vals-expected)))
        assert spectral_error<2e-11
        Ls=[math.sqrt(kappa*C)*j for j in js]
        h=K*C*(C+3);gamma=4*kappa*C
        actual_gamma=opnorm(sum(L.T@L for L in Ls))
        assert abs(actual_gamma-gamma)<1e-12
        spectra.append({'S':S,'C':C,'dimension':16,'spectrum_max_error':spectral_error,'h':h,'gamma':actual_gamma,'grid_gap':K})
        # Full 256-dimensional Liouvillian, not a symmetry-sector surrogate.
        I=np.eye(16)
        A=-1j*(np.kron(I,H)-np.kron(H.T,I));D=dissipator_super(Ls)
        T=0.02;exact=expm(T*(A+D))
        ell=np.zeros(16);ell[states.index((1,0,0,0))]=1
        for b in range(1,4):
            q=[0]*4;q[b]=1;ell[states.index(tuple(q))]=eps
        ell/=np.linalg.norm(ell)
        rho=np.outer(ell,ell)
        exactrho=(exact@rho.reshape(-1,order='F')).reshape(16,16,order='F')
        for N in (8,32,128):
            tau=T/N;Ks,root,G=cp_step(H,Ls,tau)
            completeness=float(np.linalg.norm(sum(k.conj().T@k for k in Ks)-I))
            step=sum(np.kron(k.conj(),k) for k in Ks)
            approximate=np.linalg.matrix_power(step,N)
            arho=(approximate@rho.reshape(-1,order='F')).reshape(16,16,order='F')
            # Normalized Choi state is the actual maximally entangled input.
            choi_error=trace_norm(super_to_choi(approximate-exact,16)/16)
            bound=4*T*tau*gamma*(h+gamma)
            state_error=trace_norm(arho-exactrho)
            E_error=abs(np.trace(H@(arho-exactrho)))
            E2_error=abs(np.trace(H@H@(arho-exactrho)))
            B=I-root
            psi=sum(np.kron(k.conj(),k) for k in [root]+[math.sqrt(tau)*L for L in Ls])
            identity_error=float(np.linalg.norm(psi-(np.eye(256)+tau*D)-dissipator_super([B])))
            assert completeness<2e-12 and identity_error<3e-12
            assert choi_error<=bound+1e-10 and state_error<=bound+1e-10
            assert E_error<=h*bound+1e-9 and E2_error<=h*h*bound+1e-8
            rows.append({'S':S,'N':N,'T':T,'tau_gamma':tau*gamma,'kraus_completeness_error':completeness,'exact_CP_remainder_identity_error':identity_error,'maximally_entangled_input_trace_error':choi_error,'dressed_input_trace_error':state_error,'dressed_energy_error':float(E_error),'dressed_second_moment_error':float(E2_error),'uniform_channel_bound':bound,'energy_bound':h*bound,'second_moment_bound':h*h*bound})
    return {'basis':[list(q) for q in states],'exact_integer_loss_matrix':True,'at_most_one_birth_matrix_identity':True,'spectra':spectra,'CP_convergence':rows}


def negative_controls():
    # Cyclic shift is unitary but fails energy conservation at its seam.
    M=5;shift=np.roll(np.eye(M),1,axis=0);nr=np.diag(np.arange(M))
    seam=float(np.linalg.norm(nr@shift-shift@nr-shift))
    assert seam>0
    # Naive Euler amplitude damping is not CP for any tau>0.
    L=np.array([[0,1],[0,0]],complex);tau=0.2
    euler=np.eye(4)+tau*dissipator_super([L])
    minimum=float(np.linalg.eigvalsh(super_to_choi(euler,2)).min())
    assert minimum<-1e-6
    return {'cyclic_shift_translation_identity_failure_norm':seam,'Euler_amplitude_damping_tau':tau,'Euler_Choi_minimum_eigenvalue':minimum,'interpretation':'Detected failure of two rejected routes; these are expected negative controls, not failed execution assertions.'}


def main():
    result={'source_bindings':authenticate(),'exact_rational_block_controls':exact_controls(),'finite_battery_controls':battery_controls(),'same_reservoir_sequence':sequential_control(),'complete_microscopic_star':star_controls(),'rejected_route_controls':negative_controls(),'tolerances':'Exact fractions for block identities; all floating thresholds are explicit in this script. Maximally entangled input errors are examples, not numerical certificates of diamond distance; the written proof supplies that bound.','all_assertions_passed':True}
    destination=Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'CONTROL_RESULTS.json'
    destination.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'all_assertions_passed':True,'exact_block_models':len(result['exact_rational_block_controls']),'integer_battery_cases':len(result['finite_battery_controls']['integer_grid']),'noncommensurate_battery_cases':len(result['finite_battery_controls']['arbitrary_spectrum']),'star_CP_cases':len(result['complete_microscopic_star']['CP_convergence']),'same_reservoir_sequence':result['same_reservoir_sequence'],'output':str(destination)},indent=2))


if __name__=='__main__':
    main()
