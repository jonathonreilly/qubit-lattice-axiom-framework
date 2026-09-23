#!/usr/bin/env python3
"""Direct charged-sector polynomial vectors versus exact theta derivatives."""
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS = ('docs/ROTOR_ORTHOGONAL_TRANSVERSE_REFERENCE_CURRENT_VERTEX_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'scripts/rotor_gauss_affine_theta_check_2026_09_16.py')
import hashlib,json,math,time
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
for _input in AUDIT_INPUT_PATHS:
    _input_bytes = (_REPO / _input).read_bytes()
    if _input.endswith('.md') and 'BOUNDED_THEOREM_NOTE' in _input:
        assert ('claim_id: ' + Path(_input).stem.lower()).encode() in _input_bytes
import numpy as np
from scipy.linalg import eigh
from rotor_gauss_affine_theta_check_2026_09_16 import cube,matfun,integer_cycles,points,direct,dual


def run():
    started=time.time();D,C,B=cube(1);cy=integer_cycles(D);A=matfun(C.T@C,.5);K=matfun(C.T@C,-.5);P=A@K
    Ks=matfun(C.T@C,-.25);As=matfun(C.T@C,.25);w,U=eigh(A);U=U[:,w>1e-10]
    E0=np.zeros(D.shape[1]);E0[[0,4,8]]=[1,2,-1];a=P@E0;t=P[:,3];v=U.T@Ks@t
    results=[]
    for g,M in [(.8,8),(1.2,6),(1.6,6)]:
        z,mean,mom,_=direct(cy,K,a,g,M);ze,me,mome,_=direct(cy,K,a+t,g,M)
        cov=mom-np.outer(mean,mean);cove=mome-np.outer(me,me)
        G=2*g*g*U.T@Ks@cov@Ks@U;Ge=2*g*g*U.T@Ks@cove@Ks@U;Gi=matfun(Ge,-.5)
        th,df,ddf=dual(cy,A,a,g,4);the,dfe,ddfe=dual(cy,A,a+t,g,4);thm,dfm,ddfm=dual(cy,A,a+t/2,g,4)
        Gp=np.eye(len(G))+U.T@As@ddf@As@U/(2*g*g);Gep=np.eye(len(G))+U.T@As@ddfe@As@U/(2*g*g)
        m_mid=-A@dfm/(2*g*g);m_end=-A@dfe/(2*g*g)
        ov=math.exp(-g*g*t@K@t/4)*thm/math.sqrt(th*the)
        expected=math.sqrt(2)*g*matfun(Gep,-.5)@U.T@Ks@(m_mid+t/2-m_end)*ov
        observed=np.zeros(len(G));orth=np.zeros(len(G));gram=np.zeros_like(G)
        for x in points(cy.shape[1],M):
            n=x@cy.T+a
            q=np.einsum('ni,ij,nj->n',n,K,n)
            qe=np.einsum('ni,ij,nj->n',n+t,K,n+t)
            weight=np.exp(-g*g/2*(q+qe))/math.sqrt(z*ze)
            vectors=math.sqrt(2)*g*(n+t-me)@Ks@U@Gi
            observed+=weight@vectors
            prob=np.exp(-g*g*qe)/ze
            orth+=prob@vectors;gram+=(vectors.T*prob)@vectors
        leading=g/math.sqrt(2)*math.exp(-g*g*t@K@t/4)*v
        no_center=math.sqrt(2)*g*matfun(Gep,-.5)@U.T@Ks@(t/2)*ov
        row={'g':g,'cutoff':M,'gram_formula_error':float(np.linalg.norm(G-Gp)),'final_gram_formula_error':float(np.linalg.norm(Ge-Gep)),'orthogonality_error':float(np.linalg.norm(orth)),'orthonormality_error':float(np.linalg.norm(gram-np.eye(len(G)))),'one_photon_vertex_formula_error':float(np.linalg.norm(observed-expected)),'leading_vertex_norm':float(np.linalg.norm(leading)),'compact_vertex_difference':float(np.linalg.norm(observed-leading)),'omitted_affine_means_error':float(np.linalg.norm(observed-no_center)),'wrong_vertex_sign_error':float(np.linalg.norm(observed+leading)),'smallest_raw_gram_eigenvalue':float(np.linalg.eigvalsh(G)[0])}
        assert max(row['gram_formula_error'],row['final_gram_formula_error'])<2e-8,row
        assert row['orthogonality_error']<2e-12 and row['orthonormality_error']<2e-12,row
        assert row['one_photon_vertex_formula_error']<2e-8,row
        results.append(row)
    assert results[-1]['omitted_affine_means_error']>1e-3
    assert results[0]['wrong_vertex_sign_error']>.1
    helper=Path(__file__).with_name('rotor_gauss_affine_theta_check_2026_09_16.py')
    print(json.dumps({'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'helper_sha256':hashlib.sha256(helper.read_bytes()).hexdigest(),'rank_five_charge_sector_checks':results,'seconds':time.time()-started},indent=2))


def _completed_families():
    print('PASS: three rank-five centered/normalized vertex fixtures')
    print('PASS: omitted-means and wrong-sign adverse comparisons')
    print('per_element: executed — three rank-five centered/normalized vertex fixtures')
    print('per_site: executed — finite supplied-reference configurations at declared cutoffs')
    print('per_mode: executed — finite matrices or Fourier grids described in the JSON evidence')
    print('per_block: executed — omitted-means and wrong-sign adverse comparisons')
    print('lattice_wide: checked and not executed — written uniform bounds and limit proofs; no actual interacting infinite-volume state executed')
    print('TOTAL: PASS=2 FAIL=0')

if __name__=='__main__':
    run()
    _completed_families()
