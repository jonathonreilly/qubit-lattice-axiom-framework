"""Fixed two-coordinate discriminator, not a cubic-gauge simulation."""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = ['docs/FIXED_BOX_SLOW_SPECTRUM_AND_HARMONIC_METRIC_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/FLAT_HOLONOMY_MINIMIZATION_AND_PERIODIC_SPECTRAL_FLOOR_BOUNDED_THEOREM_NOTE_2026-09-13.md', 'docs/FREE_WEYL_HOLONOMY_MINIMIZATION_BOUNDED_THEOREM_NOTE_2026-09-15.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'fixed_box_slow_spectrum_and_harmonic_metric_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/FIXED_BOX_SLOW_SPECTRUM_AND_HARMONIC_METRIC_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/slow_fast_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
from pathlib import Path
import json, math, time
import numpy as np
import sympy as sp
from scipy.sparse import diags, eye, kron, csr_matrix
from scipy.sparse.linalg import eigsh

m=2.;v=.7;lam=.9
sz=csr_matrix([[1.,0.],[0.,-1.]])
sx=csr_matrix([[0.,1.],[1.,0.]])
sy=csr_matrix([[0.,-1j],[1j,0.]])
id2=eye(2,format='csr')

def build(g,nq,nt):
    dq,dt=2*nq+1,2*nt+1
    # exp(i q) sends |n> to |n+1> for D=-i partial in exp(i n q).
    tq=kron(diags(np.ones(dq-1),-1),eye(dt),format='csr')
    tt=kron(eye(dq),diags(np.ones(dt-1),-1),format='csr')
    q,t=np.meshgrid(np.arange(-nq,nq+1),np.arange(-nt,nt+1),indexing='ij')
    sig=np.array([1.,-1.])[None,:]
    pq=q.reshape(-1,1)+.15*sig;pt=t.reshape(-1,1)+.23*sig
    electric=(g*g/2*(4*pq*pq+2*pq*pt+2*pt*pt)).reshape(-1)
    H=diags(electric)+kron((eye(dq*dt)-.5*(tq+tq.T))/g**2,id2)
    H=H-kron(eye(dq*dt),v/2*sz)
    block1=-m/2*sz+1j*m/2*sx
    block2=-v/4*sz+1j*v/4*sx
    H=H+kron(tt,block1)+kron(tt.T,block1.conj().T)
    H=H+kron(tt@tt,block2)+kron(tt.T@tt.T,block2.conj().T)
    bq=-1j*lam/2*sy
    H=H+kron(tq,bq)+kron(tq.T,bq.conj().T)
    H=H.tocsr()
    herm=H-H.conj().T
    assert not herm.nnz or np.max(np.abs(herm.data))<1e-13
    return H

def solve(g,pad=0):
    nq=math.ceil(5/g)+pad;nt=math.ceil(6/math.sqrt(g))+pad
    H=build(g,nq,nt)
    rng=np.random.default_rng(21001)
    start=rng.normal(size=H.shape[0])+1j*rng.normal(size=H.shape[0])
    tick=time.monotonic()
    # A shift below the proved model lower bound avoids a large spectral width.
    # Magnetic/electric >=0 and ||h||<=m+v+lam; -4 is below that.
    vals,vec=eigsh(H,k=4,sigma=-4.,which='LM',tol=2e-11,v0=start)
    order=np.argsort(vals);vals=vals[order];vec=vec[:,order]
    res=np.linalg.norm(H@vec-vec*vals[None,:],axis=0)
    assert max(res)<2e-8
    omega=math.sqrt(7*v/4)
    predicted=np.array([-1.7+g*omega*(j+.5) for j in range(4)])
    return {'g':g,'nq':nq,'nt':nt,'dimension':H.shape[0],
        'energies':vals.tolist(),'residuals':res.tolist(),
        'scaled_coefficients':((vals+1.7)/g).tolist(),
        'scaled_gap':float((vals[1]-vals[0])/g),
        'gap_coefficient_error':float((vals[1]-vals[0])/g-omega),
        'scaled_level_errors':((vals-predicted)/g).tolist(),
        'elapsed_seconds':time.monotonic()-tick}

def main():
    K=sp.Matrix([[4,1],[1,2]]);J=sp.Matrix([[1,0],[-sp.Rational(1,4),1]])
    assert J*K*J.T==sp.diag(4,sp.Rational(7,4))
    # The local rotated matter vector has a nonzero derivative into its partner.
    t=sp.symbols('t',real=True)
    u=sp.Matrix([sp.cos(t/2),sp.sin(t/2)])
    assert (u.diff(t).T*u.diff(t))[0]==sp.Rational(1,4) or sp.simplify((u.diff(t).T*u.diff(t))[0])==sp.Rational(1,4)
    # Independently integrate the literal matrix potential in exp(i n.theta).
    nq,nt=1,2;gg=.3
    modes=np.array([(i,j) for i in range(-nq,nq+1) for j in range(-nt,nt+1)])
    pts=np.array([(2*math.pi*i/9,2*math.pi*j/9) for i in range(9) for j in range(9)])
    dense=np.zeros((len(modes)*2,len(modes)*2),complex)
    for q0,t0 in pts:
        ph=np.exp(1j*(modes@np.array([q0,t0])))
        pot=(-(m+v*math.cos(t0))*(math.cos(t0)*sz.toarray()+math.sin(t0)*sx.toarray())).astype(complex)
        pot+=lam*math.sin(q0)*sy.toarray()+(1-math.cos(q0))/gg**2*np.eye(2)
        dense+=np.kron(np.outer(ph.conj(),ph),pot)/len(pts)
    for j,(qn,tn) in enumerate(modes):
        for s,sgn in enumerate([1.,-1.]):
            pp=np.array([qn+.15*sgn,tn+.23*sgn])
            dense[2*j+s,2*j+s]+=gg**2/2*(pp@np.array(K,dtype=float)@pp)
    literal_error=float(np.max(np.abs(dense-build(gg,nq,nt).toarray())))
    assert literal_error<2e-12
    rows=[]
    for g in [.24,.16,.10,.07,.05]:
        r=solve(g);rows.append(r);print(json.dumps(r),flush=True)
    refine=solve(.10,pad=6)
    old=next(r for r in rows if r['g']==.10)
    delta=float(max(abs(np.array(refine['energies'])-old['energies'])))
    assert delta<2e-7
    assert abs(rows[-1]['gap_coefficient_error'])<abs(rows[0]['gap_coefficient_error'])/3
    assert max(abs(np.array(rows[-1]['scaled_level_errors'])))<max(abs(np.array(rows[0]['scaled_level_errors'])))/3
    out={'status':'author_checks_not_independent_review','scope':'two-coordinate analytic fixture, not cubic model',
         'predicted_fast_floor':1.,'predicted_matter_minimum':-2.7,
         'predicted_slow_frequency':math.sqrt(7*v/4),
         'wrong_unsheared_frequency':math.sqrt(2*v),
         'literal_position_Fourier_matrix_error':literal_error,
         'matter_derivative_norm_squared':'1/4','rows':rows,
         'refinement':refine,'cutoff_refinement_max_error':delta}
    _OUTPUT_JSON.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: integer cycle/harmonic metric or local matrix identities')
    print('per_site: finite periodic cycle coordinates and two-coordinate fixture')
    print('per_mode: finite sparse slow spectra and cutoff refinement, not cubic interacting phase')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
