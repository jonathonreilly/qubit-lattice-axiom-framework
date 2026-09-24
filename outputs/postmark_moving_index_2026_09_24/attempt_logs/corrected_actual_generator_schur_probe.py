#!/usr/bin/env python3
"""Personal finite diagnostic of pole-safe Schur reconstruction.

Builds the supplied finite Jacobi matrix independently, diagonalizes the full
operator and deleted-anchor compression, reconstructs full eigenvectors from
anchor data away from interior poles, and falls back to direct eigenvectors
inside a fixed relative pole band. This is finite floating-point evidence only.
"""
import json
import numpy as np

ELL=(0,1,0,1,1)
PI=(-1,0,0,0,1)
RHO=(0,0,0,1,0)

def full_hamiltonian(S):
    C=S*(S+1)
    sites=np.arange(-5*S,5*S-3,dtype=np.int64)
    H=np.zeros((len(sites),len(sites)),dtype=float)
    def cas(m): return C-m*(m+1)
    for i,n0 in enumerate(sites):
        n=int(n0); k,s=divmod(n,5)
        left=cas(k+ELL[s]); prev_right=cas(k-1+RHO[(s-1)%5]) if s==0 else cas(k+RHO[s-1])
        # Use the source's physical 5-periodic labels directly for a cross-checkable build.
        H[i,i]=left+prev_right
        if i+1<len(sites):
            right=cas(k+RHO[s])
            if left<0 or right<0: raise ArithmeticError((S,n,left,right))
            H[i,i+1]=H[i+1,i]=-np.sqrt(left*right)
    return sites,H

def invsqrt(M):
    ev,U=np.linalg.eigh((M+M.conj().T)/2)
    if ev.min()<=0: raise ArithmeticError(("nonpositive metric",ev.min()))
    return (U*(1/np.sqrt(ev))[None,:])@U.conj().T

def one_spin(S):
    sites,H=full_hamiltonian(S)
    C=S*(S+1); t=0.25
    a_ids=np.flatnonzero(sites%5==0)
    i_ids=np.flatnonzero(sites%5!=0)
    perm=np.r_[a_ids,i_ids]
    Hp=H[np.ix_(perm,perm)]
    na=len(a_ids); ni=len(i_ids)
    Haa=Hp[:na,:na]; Hai=Hp[:na,na:]; Hia=Hp[na:,:na]; Hii=Hp[na:,na:]
    evals,U=np.linalg.eigh(H)
    Up=U[perm,:]
    poles=np.linalg.eigvalsh(Hii)
    gaps=np.min(np.abs(evals[:,None]-poles[None,:]),axis=1)/C
    pole_band=1e-8
    near=gaps<=pole_band
    z0=int(np.flatnonzero(sites==0)[0])
    z0p=int(np.flatnonzero(perm==z0)[0])
    prepared=np.abs(U[z0,:])**2
    mass_bands={}
    for band in (1e-2,1e-3,1e-4,1e-6,1e-8):
        m=gaps<=band
        mass_bands[f"{band:.0e}"]={"modes":int(m.sum()),"prepared_mass":float(prepared[m].sum())}
    Urec=Up.copy()
    max_recon=0.0; max_eq_resid=0.0; min_anchor=1.0
    far=np.flatnonzero(~near)
    eye=np.eye(ni)
    for j in far:
        E=evals[j]; x=Up[:na,j]
        y=np.linalg.solve(E*eye-Hii,Hia@x)
        rec=np.r_[x,y]
        nr=np.linalg.norm(rec)
        if nr==0: raise ArithmeticError(("zero reconstruction",S,int(j)))
        rec=rec/nr
        ov=np.vdot(rec,Up[:,j])
        if abs(ov): rec*=ov/abs(ov)
        max_recon=max(max_recon,float(np.linalg.norm(rec-Up[:,j])))
        max_eq_resid=max(max_eq_resid,float(np.linalg.norm((E*eye-Hii)@y-Hia@x)))
        min_anchor=min(min_anchor,float(np.linalg.norm(x)))
        Urec[:,j]=rec
    # The target generator is G_S=N_S^2-C*N_S, not H_S=C*N_S.
    # Since H_S has eigenvalue E=C*lambda, the exact target phase is
    # exp[-it(E^2/C^2-E)]. Compare direct and Schur-reconstructed target
    # character/readout using that phase.
    vdiag=np.exp(2j*np.pi*sites/3)
    vperm=vdiag[perm]
    Odiag=(1+vperm+vperm.conj())/3
    d=U[z0,:].conj()
    target_phase=np.exp(-1j*t*(evals**2/C**2-evals))
    coeff=target_phase*d
    psi=U@coeff
    q_direct=np.vdot(psi,vdiag*psi)
    o_direct=float(np.vdot(psi,((1+vdiag+vdiag.conj())/3)*psi).real)
    drec=Urec[z0p,:].conj()
    coeffrec=target_phase*drec
    psirec=Urec@coeffrec
    q_schur=np.vdot(psirec,vperm*psirec)
    o_schur=float(np.vdot(psirec,Odiag*psirec).real)
    Vov=Urec.conj().T@(vperm[:,None]*Urec)
    orth_err=float(np.linalg.norm(Urec.conj().T@Urec-np.eye(len(evals)),ord=2))
    vnorm=float(np.linalg.norm(Vov,ord=2))
    # Compare two-energy Q_V on selected non-pole eigenpairs and test its normalized contraction.
    valid=[int(j) for j in far]
    selected=sorted(set([valid[k] for k in np.linspace(0,len(valid)-1,min(7,len(valid)),dtype=int)])) if valid else []
    pair_error=0.0; contraction_max=0.0; metric_max=0.0; pairs=0
    Rs={}; Ts={}; Ms={}
    for j in selected:
        E=evals[j]
        R=np.linalg.solve(E*eye-Hii,eye)
        Tmat=np.vstack((np.eye(na),R@Hia))
        M=Tmat.conj().T@Tmat
        Rs[j]=R; Ts[j]=Tmat; Ms[j]=M
        iso=Tmat@invsqrt(M)
        metric_max=max(metric_max,float(np.linalg.norm(iso.conj().T@iso-np.eye(na),ord=2)))
    va=np.diag(vperm[:na]); vi=np.diag(vperm[na:])
    for j in selected:
        for k in selected:
            Q=va+Hai@Rs[j]@vi@Rs[k]@Hia
            xj=Up[:na,j]; xk=Up[:na,k]
            pred=np.vdot(xj,Q@xk)
            direct=np.vdot(Up[:,j],vperm*Up[:,k])
            pair_error=max(pair_error,float(abs(pred-direct)))
            normed=Ts[j].conj().T@(vperm[:,None]*Ts[k])
            normed=invsqrt(Ms[j])@normed@invsqrt(Ms[k])
            contraction_max=max(contraction_max,float(np.linalg.norm(normed,ord=2)))
            pairs+=1
    return {
      "S":S,"dimension":len(sites),"anchors":na,"interior":ni,
      "interior_pole_count_with_multiplicity":len(poles),
      "min_relative_full_to_interior_spectrum_gap":float(gaps.min()),
      "candidate_pole_modes_rel_gap_le_1e-8":int(near.sum()),
      "candidate_pole_prepared_mass":float(prepared[near].sum()),
      "prepared_mass_near_poles":mass_bands,
      "generic_modes_reconstructed":int(len(far)),
      "max_full_eigenvector_reconstruction_l2_error":max_recon,
      "max_reconstruction_equation_residual":max_eq_resid,
      "min_anchor_norm_among_generic_modes":min_anchor,
      "reconstructed_basis_orthogonality_error":orth_err,
      "unitary_character_compression_norm":vnorm,
      "selected_two_energy_pairs_checked":pairs,
      "max_two_energy_QV_vs_direct_overlap_error":pair_error,
      "max_normalized_QV_operator_norm_on_selected_pairs":contraction_max,
      "max_normalized_T_isometry_error":metric_max,
      "target_generator":"G_S=N_S^2-C*N_S, evaluated via H_S=C*N_S eigenvalues",
      "target_phase":"exp(-it*(E^2/C^2-E)) for H_S eigenvalue E",
      "direct_character_expectation":complex(q_direct).__repr__(),
      "schur_character_expectation_with_direct_pole_fallback":complex(q_schur).__repr__(),
      "character_expectation_difference":float(abs(q_direct-q_schur)),
      "direct_period_three_readout":o_direct,
      "schur_period_three_readout_with_direct_pole_fallback":o_schur,
      "period_three_readout_difference":abs(o_direct-o_schur),
      "interpretation":"actual supplied-generator finite readout plus sampled full-spectrum reconstruction and finite pole-neighborhood weights; no asymptotic pole-mass or phase-cancellation bound"
    }

def main():
    print(json.dumps({"status":"author-only finite pole-aware Schur diagnostic","base":"0e6ad8285096ed668816f18caaa6fbbfbd9c50e8","operator":"H_S=C N_S","prepared_state":"delta_0","observable":"1[n mod 3=0]","time":0.25,"spins":[one_spin(S) for S in (8,16,32,64)]},indent=2,sort_keys=True))
if __name__=="__main__":main()
