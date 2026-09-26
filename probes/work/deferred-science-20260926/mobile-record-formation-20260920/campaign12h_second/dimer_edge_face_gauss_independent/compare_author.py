#!/usr/bin/env python3
"""Post-seal authentication and selective independent matrix comparisons."""
from pathlib import Path
import json,hashlib,math,datetime
import numpy as np
import sympy as s
from scipy.linalg import eigh
import independent_check as own
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent

def ident(f):
    b=f.read_bytes();return dict(path=str(f.resolve()),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def direct_coefficients(K):
    eps=K**(-1/6);omega=math.sqrt(2);rt=(1-omega)/(1+omega);rz=(1-eps**2)/(1+eps**2)
    d=(rt+rz)/2;o=(rz-rt)/2;vac=((1-rt*rt)*(1-rz*rz))**.25;coef=np.zeros((K+1,K+1))
    for n in range(K+1):
        for m in range(K+1):
            for ell in range(min(n,m)+1):
                if (n-ell)%2 or (m-ell)%2:continue
                a=(n-ell)//2;b=(m-ell)//2
                coef[n,m]+=vac*math.sqrt(math.factorial(n)*math.factorial(m))*(d/2)**(a+b)*o**ell/(math.factorial(a)*math.factorial(b)*math.factorial(ell))
    return coef.ravel()/np.linalg.norm(coef)

def main():
    pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
    for x in pre['sources']+pre['artifacts']:assert ident(Path(x['path']))==x
    a=json.loads((ROOT/'dimer_edge_face_gauss_checks/RESULTS.json').read_text())
    for x in a['sources']:assert ident(Path(x['path']))==x
    baseline=json.loads((HERE/'INDEPENDENT_RESULTS.json').read_text());precision=json.loads((HERE/'PRECISION_RESULTS.json').read_text())
    incidence=[]
    for row in a['incidence']:
        L=row['L'];_,_,d0,C,d2=own.matrices(L);V=L**3
        assert row['exact_rank_curl']==2*V-2 and row['exact_rank_gradient']==V-1
        assert row['exact_kernel_dimension']==V+2 and row['zero_frequency_wavevectors']==1
        defect=C-C.T;norm=math.sqrt(2*float((defect.multiply(defect)).sum()))
        assert abs(norm-row['wrong_adjoint_energy_defect_frobenius'])<2e-14
        assert abs(2*math.sin(math.pi/L)-row['nonzero_frequency_min'])<1e-14
        # Repeat only the declared one-entry mutation, using independent matrices.
        broken=C.tolil();broken[0,0]+=1;broken=broken.tocsr()
        assert (broken@d0).nnz>0 and (d2@broken).nnz>0
        incidence.append(dict(L=L,independent_wrong_adjoint_defect=norm,declared_entry_mutation_detected=True))
    assert a['rotations']['proper_rotations']==24 and a['rotations']['exact_edge_face_chain_maps']==72
    for row in a['finite_qubit_algebra']['rows']:
        k=row['K'];assert row['physical_pair_product_dimension']==2**k and row['symmetric_dimension']==k+1
        assert s.simplify(s.sympify(row['exact_quadrature_norm'])**2-s.Rational(k,2))==0
    assert s.Rational(a['finite_qubit_algebra']['two_link_K1_finite_Gauss_commutator_squared_Frobenius'])==s.Rational(baseline['spin']['two_edge_finite_Gauss_commutator_Frobenius_squared'])/2
    own_index={(r['K'],e['time']):e for r in baseline['two_edge_squeezed_controls'] for e in r['evolutions']}
    common=[];all_arithmetic=0;tail_notes=[]
    mp_index={r['K']:r for r in precision['tail_rows']}
    uT=np.array([1,-1])/math.sqrt(2);uZ=np.array([1,1])/math.sqrt(2);omega=math.sqrt(2)
    for row in a['squeezed_motif']['rows']:
        K=row['K'];eps=K**(-1/6);assert row['physical_dimension']==(K+1)**2
        assert abs(row['epsilon']-eps)<1e-15
        assert abs(row['energy_error']-abs(row['energy']-omega/2))<1e-15
        assert abs(row['energy_error_over_K_minus_third']-row['energy_error']*K**(1/3))<1e-15
        assert abs(row['Gauss_over_K_minus_sixth']-row['Gauss_mean_square']*K**(1/6))<1e-15
        assert abs(row['canonical_Gauss_mean_square']-eps**2/2)<1e-15
        for w in row['Weyl_values']:
            e=np.array(w['e']);b=w['b']
            target=math.exp(-((e@uT)**2*omega+2*b*b/omega)/4)
            canonical=target*math.exp(-eps**2*(e@uZ)**2/4)
            value=complex(w['finite_real'],w['finite_imag'])
            assert abs(target-w['reduced_target'])<1e-15 and abs(canonical-w['canonical_squeezed_target'])<1e-15
            assert abs(abs(value-target)-w['error_to_reduced'])<1e-15
            assert abs(abs(value-canonical)-w['error_to_squeezed'])<1e-15;all_arithmetic+=1
        key=(K,row['time'])
        if key in own_index:
            r=own_index[key];de=abs(row['energy']-r['energy']);dg=abs(row['Gauss_mean_square']-r['gauge_mean_square'])
            assert max(de,dg)<3e-12;common.append(dict(K=K,time=row['time'],energy_difference=de,Gauss_difference=dg))
        if K in [32,64] and row['time']==0:
            tail_notes.append(dict(K=K,author_float_missing_probability=row['projection_missing_probability'],
               independent_90_digit_missing_probability=mp_index[K]['projection_tail_squared'],
               limitation='Float zero is unresolved subtraction near one, not an exact zero probability.'))
    # Closed coefficient sum and dense spectral functions, rather than the author recurrence/sparse exponentials.
    K=4;low=np.zeros((5,5))
    for n in range(1,5):low[n-1,n]=math.sqrt(n*(1-(n-1)/K))
    q=(low+low.T)/math.sqrt(2);p=1j*(low.T-low)/math.sqrt(2);I=np.eye(5)
    P0=np.kron(p,I);P1=np.kron(I,p);B=np.kron(q,I)-np.kron(I,q);H=(P0@P0+P1@P1+B@B)/2
    eh,U=eigh(H);phi=direct_coefficients(K);weyl=[]
    for row in a['squeezed_motif']['rows']:
        if row['K']!=K:continue
        t=row['time'];state=U@(np.exp(-1j*t*eh)*(U.conj().T@phi))
        for w in row['Weyl_values']:
            e=w['e'];Op=-e[0]*P0-e[1]*P1+w['b']*B;ev,V=eigh(Op)
            value=np.vdot(state,V@(np.exp(1j*ev)*(V.conj().T@state)))
            diff=abs(value-complex(w['finite_real'],w['finite_imag']));assert diff<3e-13
            weyl.append(dict(K=K,time=t,e=e,b=w['b'],independent_real=float(value.real),independent_imag=float(value.imag),difference=float(diff)))
    receipt=json.loads((ROOT/'DIMER_EDGE_FACE_GAUSS_RUN_RECEIPT.json').read_text())
    assert receipt['returncode']==0 and receipt['script_sha256']==ident(ROOT/'dimer_edge_face_gauss_check.py')['sha256']
    assert (ROOT/'DIMER_EDGE_FACE_GAUSS_RUN.stderr').read_bytes()==b''
    files=['DIMER_EDGE_FACE_GAUSS_QUANTUM_LIMIT.md','DIMER_EDGE_FACE_ENERGY_AND_GAUSS_MOMENT_ADDENDUM.md',
           'dimer_edge_face_gauss_check.py','dimer_edge_face_gauss_checks/RESULTS.json',
           'DIMER_EDGE_FACE_GAUSS_RUN.log','DIMER_EDGE_FACE_GAUSS_RUN.stderr','DIMER_EDGE_FACE_GAUSS_RUN_RECEIPT.json']
    result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_bindings=[ident(ROOT/f) for f in files],
      preseal_authenticated=True,complete_author_code_and_results_read=True,author_code_executed=False,
      incidence_comparisons=incidence,Gauss_commutator_normalization='Author G=-(P0+P1)/sqrt(2) has squared Frobenius norm 2; independent unnormalized G=P0+P1 has 4. These agree.',
      common_presealed_energy_Gauss_comparisons=common,all_36_Weyl_targets_and_errors_checked=all_arithmetic,
      dense_K4_Weyl_comparisons=weyl,tiny_tail_precision_limits=tail_notes,
      scope='Author K128 dynamics authenticated only. Common presealed state values are reused; only six K4 Weyl entries were independently recomputed after comparison. No source or proof repair needed.')
    (HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()
