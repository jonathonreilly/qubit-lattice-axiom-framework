#!/usr/bin/env python3
"""Finite charged ring checks with explicit hard-boundary exclusions."""

# Canonical packaging; supplied scientific fixtures below are unchanged.
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/EXACT_GAUGE_WARD_RESPONSE_IDENTITIES_BOUNDED_THEOREM_NOTE_2026-09-15.md', 'docs/EXACT_GAUSS_REDUCTION_AND_FIXED_VOLUME_WEAK_COUPLING_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-13.md']
from pathlib import Path as _InputPath
_REPO_ROOT = _InputPath(__file__).resolve().parents[1]
_INPUT_TEXT = {q: (_REPO_ROOT / q).read_text() for q in AUDIT_INPUT_PATHS}
assert 'exact_gauge_ward_response_identities_bounded_theorem_note_2026-09-15' in _INPUT_TEXT['docs/EXACT_GAUGE_WARD_RESPONSE_IDENTITIES_BOUNDED_THEOREM_NOTE_2026-09-15.md']
_OUTPUT_JSON = _REPO_ROOT / 'logs/runner-cache/response_identity_check_2026_09_15.json'
_OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
from pathlib import Path
import hashlib
import json
import numpy as np
import scipy.sparse as ss
import scipy.linalg as la


def car_hop(bits,create,annihilate):
    if not (bits>>annihilate)&1: return None
    sign=(-1)**((bits&((1<<annihilate)-1)).bit_count())
    b=bits^(1<<annihilate)
    if (b>>create)&1: return None
    sign*=(-1)**((b&((1<<create)-1)).bit_count())
    return b|(1<<create),sign


def comm(A,B): return A@B-B@A


def maxentry(A):
    return float(np.max(np.abs(A.data))) if A.nnz else 0.


def build(S=7):
    matter=[b for b in range(256)
            if sum((b>>(2*x))&1 for x in range(4))==2
            and sum((b>>(2*x+1))&1 for x in range(4))==2]
    states=[(b,n) for b in matter for n in range(-S,S+1)]
    index={s:i for i,s in enumerate(states)}; dim=len(states)
    def flux(b,n):
        q=np.array([((b>>(2*x))&1)-((b>>(2*x+1))&1) for x in range(4)])
        return n+np.cumsum(q)
    E=np.array([flux(b,n) for b,n in states],dtype=float)
    electric=[ss.diags(E[:,j],format='csr',dtype=complex) for j in range(4)]
    rows=[];cols=[]
    for col,(b,n) in enumerate(states):
        if n<S: rows.append(index[(b,n+1)]);cols.append(col)
    U=ss.csr_matrix((np.ones(len(rows)),(rows,cols)),shape=(dim,dim),dtype=complex)
    hops=[]; transition_count=0
    for l in range(4):
        r=[];c=[];data=[]
        for col,(b,n) in enumerate(states):
            for species,q in [(0,1),(1,-1)]:
                moved=car_hop(b,2*l+species,2*((l+1)%4)+species)
                if moved is None: continue
                target,sign=moved; nn=n+(q if l==3 else 0)
                if not -S<=nn<=S: continue
                row=index[(target,nn)]
                expected=np.zeros(4);expected[l]=q
                assert np.array_equal(E[row]-E[col],expected)
                # Same real conjugate hopping coefficient for +/- charges.
                r.append(row);c.append(col);data.append(-.7*sign)
                transition_count+=1
        hops.append(ss.csr_matrix((data,(r,c)),shape=(dim,dim),dtype=complex))
    onsite=[]
    potentials=np.array([-.7,.2,.4,-.1])
    for b,n in states:
        onsite.append(sum(potentials[x]*(((b>>(2*x))&1)+((b>>(2*x+1))&1))
                      for x in range(4)))
    return states,E,electric,U,hops,ss.diags(onsite,format='csr'),transition_count


def matrix_checks():
    S=7; g=.6; a=.7; bmag=.9; weights=np.array([1.,1.3,.8,1.1])
    states,E,Es,U,Ts,onsite,count=build(S)
    dim=len(states); I=ss.eye(dim,format='csr',dtype=complex)
    cosine=(U+U.getH())/2; sine=(U-U.getH())/(2j)
    HE=ss.diags(g*g/(2*a)*(E*E@weights),format='csr')
    HM=sum((T+T.getH())/a for T in Ts)+onsite/a
    H=HE+bmag/(a*g*g)*(I-cosine)+HM
    v=np.array([.3,-.8,.4,1.2])
    FE=ss.diags(g*(E@v),format='csr')
    electric_lhs=comm(FE,comm(H,FE))
    electric_rhs=bmag/a*sum(v)**2*cosine
    electric_rhs+=sum(-g*g/a*v[j]**2*(Ts[j]+Ts[j].getH()) for j in range(4))
    electric_error=maxentry(electric_lhs-electric_rhs)
    assert electric_error<2e-11
    FB=sine/g
    magnetic_lhs=comm(FB,comm(H,FB))
    magnetic_rhs=sum(weights)/a*(cosine@cosine)
    interior=np.array([abs(n)<=S-3 for _,n in states],dtype=float)
    P=ss.diags(interior,format='csr')
    magnetic_error=maxentry(P@(magnetic_lhs-magnetic_rhs)@P)
    assert magnetic_error<2e-11
    boundary_discrepancy=maxentry(magnetic_lhs-magnetic_rhs)
    assert boundary_discrepancy>1e-3
    # A graph with no plaquette energy retains a real harmonic link twist.
    H0=(HE+HM).toarray()
    uniform=np.ones(4)/4
    generator=E@uniform
    epsilon=.31
    phase=np.exp(1j*epsilon*generator)
    transformed=phase[:,None]*H0*phase.conj()[None,:]
    # Build the source directly from its CAR hop's actual electric increment.
    twisted=HE.astype(complex).copy()+onsite/a
    for l,T in enumerate(Ts):
        coo=T.tocoo(); q=E[coo.row,l]-E[coo.col,l]
        TT=ss.csr_matrix((coo.data*np.exp(1j*epsilon*uniform[l]*q),
                          (coo.row,coo.col)),shape=T.shape)
        twisted+=(TT+TT.getH())/a
    twist_error=float(np.max(np.abs(twisted.toarray()-transformed)))
    assert twist_error<2e-11
    eig,V=la.eigh(H0)
    gapmask=eig-eig[0]>1e-9
    psi=V[:,0]
    J=1j*(generator[:,None]*H0-H0*generator[None,:])
    D=-((generator[:,None]-generator[None,:])**2)*H0
    jmatrix=V.conj().T@J@psi
    diamagnetic=float(np.vdot(psi,D@psi).real)
    paramagnetic=float(2*np.sum(np.abs(jmatrix[gapmask])**2/(eig[gapmask]-eig[0])))
    ward_error=abs(diamagnetic-paramagnetic)
    assert ward_error<2e-10
    fpsi=g*generator*psi
    spectral_first=float(np.vdot(fpsi,(H0-eig[0]*np.eye(dim))@fpsi).real)
    sum_rule_error=abs(spectral_first-g*g*diamagnetic/2)
    assert sum_rule_error<2e-10
    return {'dimension':dim,'CAR_Gauss_transitions':count,
            'electric_double_commutator_error':electric_error,
            'magnetic_interior_error':magnetic_error,
            'magnetic_hard_boundary_discrepancy_retained':boundary_discrepancy,
            'flat_twist_unitary_error':twist_error,
            'diamagnetic':diamagnetic,'paramagnetic':paramagnetic,
            'ward_error':ward_error,'ground_degeneracy':int(np.sum(~gapmask)),
            'spectral_first_moment':spectral_first,'sum_rule_error':sum_rule_error}


def oscillator_check():
    g=.4; rho=1.7
    rows=[]
    for k in [.4,.1,.02,.004,0.]:
        stiffness=k*k/(g*g)+rho
        omega=g*np.sqrt(stiffness)
        # Direct completion after A -> A - rho*epsilon/stiffness.
        curvature=rho-rho*rho/stiffness
        expected=rho*k*k/(k*k+g*g*rho)
        assert abs(curvature-expected)<2e-14
        assert abs(omega*omega-(k*k+g*g*rho))<2e-14
        rows.append({'k':k,'frequency':omega,'static_curvature':curvature})
    assert rows[-1]['frequency']>.5 and abs(rows[-1]['static_curvature'])<1e-14
    return {'rho':rho,'g':g,'rows':rows,'scope':'distinct quadratic discriminator'}


def main():
    result={'status':'PASS','scope':'finite response identities, no cubic phase theorem',
            'charged_ring':matrix_checks(),'massive_screening_example':oscillator_check(),
            'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    output=json.dumps(result,indent=2)
    _OUTPUT_JSON.write_text(output+'\n');print(output)


if __name__=='__main__': main()

if __name__ == '__main__':
    print('TOTAL: PASS=1 FAIL=0')
    print('Completed family: complete finite companion program; individual checks and diagnostics remain in structured JSON')
    print('per_element: charged f-sum and Ward identities')
    print('per_site: finite charged-ring configurations')
    print('per_mode: finite matrix spectral/response controls; no pole or phase inference')
    print('per_block: one complete companion family; imported helpers are shared implementation, not independent evidence')
    print('lattice_wide: analytical claims and infinite/iterated limits checked in written proof, not executed here')
