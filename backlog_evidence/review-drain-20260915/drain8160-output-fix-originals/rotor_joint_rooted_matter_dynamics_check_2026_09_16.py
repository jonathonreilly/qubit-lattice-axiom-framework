#!/usr/bin/env python3
"""Literal charged-ring challenge of rooted bounded matter dynamics.

Uses the explicit Gauss basis of the gauge propagation program, while
building the rooted CAR map and closing-loop difference separately.
"""
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.linalg import expm
from scipy.sparse.linalg import eigsh, expm_multiply

from rotor_joint_gauge_propagation_check_2026_09_16 import car_hop

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ROTOR_JOINT_BOUNDED_NEUTRAL_MATTER_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/ROTOR_UNIFORM_COMPACT_FIELD_SOFT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'docs/ROTOR_JOINT_EQUAL_TIME_WEYL_CAR_STATE_BOUNDED_THEOREM_NOTE_2026-09-16.md', 'scripts/rotor_joint_gauge_propagation_check_2026_09_16.py')
# Scientific helper: the declared package-local CAR sign function.
# Integrity reads: this source and helper source for hashes. No external data.

_REPO = Path(__file__).resolve().parents[1]
for _input_path in AUDIT_INPUT_PATHS:
    _input_bytes = (_REPO / _input_path).read_bytes()
    if _input_path.endswith('.md'):
        assert ('claim_id: ' + Path(_input_path).stem.lower()).encode() in _input_bytes

assert '(g^2 q^2/2)||W_E^(1/2)p_x||_2^2 a_x.' in (_REPO / AUDIT_INPUT_PATHS[0]).read_text()

TOL=3e-8
checks=0
report={}


def demand(condition,label):
    global checks
    if not bool(condition):
        raise AssertionError(label)
    checks+=1


def fixture(g):
    cutoff=math.ceil(8/g)
    matter=[b for b in range(256)
            if sum((b>>(2*x))&1 for x in range(4))==2
            and sum((b>>(2*x+1))&1 for x in range(4))==2]
    mi={b:i for i,b in enumerate(matter)}
    n=np.arange(-cutoff,cutoff+1)
    M,N=len(matter),len(n)
    dim=M*N
    im=sparse.eye(M,format="csr",dtype=complex)
    inn=sparse.eye(N,format="csr",dtype=complex)
    identity=sparse.eye(dim,format="csr",dtype=complex)
    shift=sparse.diags(np.ones(N-1),-1,format="csr",dtype=complex)
    U=sparse.kron(im,shift,format="csr")
    cosine=(U+U.getH())/2
    q=np.array([[((bits>>(2*x))&1)-((bits>>(2*x+1))&1) for x in range(4)] for bits in matter])
    prefix=np.cumsum(q,axis=1)
    E=(prefix[:,None,:]+n[None,:,None]).reshape(dim,4)
    e,bmag,hopping=np.array([1.,1.3,.8,1.1]),.9,-.7
    potential=np.array([-.7,.2,.4,-.1])
    onsite=np.array([sum(potential[x]*(((bits>>(2*x))&1)+((bits>>(2*x+1))&1))
                                  for x in range(4)) for bits in matter])
    H0=sparse.diags(onsite,format="csr",dtype=complex)
    Hm=sparse.kron(H0,inn,format="csr")
    closing=[]
    def fock_hop(create,annihilate,coefficient):
        rows,cols,values=[],[],[]
        for col,bits in enumerate(matter):
            moved=car_hop(bits,create,annihilate)
            if moved is not None:
                target,sign=moved
                rows.append(mi[target]);cols.append(col);values.append(coefficient*sign)
        return sparse.csr_matrix((values,(rows,cols)),shape=(M,M),dtype=complex)
    for l in range(4):
        for species,charge in [(0,1),(1,-1)]:
            T=fock_hop(2*l+species,2*((l+1)%4)+species,hopping)
            H0+=T+T.getH()
            flux_shift=inn if l!=3 else (shift if charge==1 else shift.getH())
            physical=sparse.kron(T,flux_shift,format="csr")
            Hm+=physical+physical.getH()
            if l==3:
                closing.append((T,charge))
    HE=sparse.diags(g*g/2*(E*E@e),format="csr",dtype=complex)
    H=HE+bmag/g**2*(identity-cosine)+Hm
    values,vectors=eigsh(H,k=1,which="SA",tol=2e-13,v0=np.ones(dim))
    energy,psi=float(values[0]),vectors[:,0]
    demand(np.linalg.norm(H@psi-energy*psi)<TOL,"charged ground eigen residual")
    # A two-link transfer plus a degree-four density polynomial.
    transfer=fock_hop(0,4,1.)
    density=np.array([((bits>>2)&1)*((bits>>5)&1) for bits in matter])
    B=transfer+.3*sparse.diags(density,format="csr",dtype=complex)
    BJ=sparse.kron(B,inn,format="csr")
    free_comm=sparse.kron(H0@B-B@H0,inn,format="csr")
    residual_op=H@BJ-BJ@H-free_comm
    electric=HE@BJ-BJ@HE
    loop_difference=sparse.csr_matrix((dim,dim),dtype=complex)
    loop_comm=sparse.csr_matrix((dim,dim),dtype=complex)
    for T,charge in closing:
        delta=(shift if charge==1 else shift.getH())-inn
        piece=sparse.kron(T,delta,format="csr")
        loop_difference+=piece+piece.getH()
        loop_comm+=sparse.kron(T@B-B@T,delta,format="csr")
        loop_comm+=sparse.kron(T.getH()@B-B@T.getH(),delta.getH(),format="csr")
    demand(sparse.linalg.norm(Hm-sparse.kron(H0,inn)-loop_difference)<TOL,"actual closing hop equals rooted free hop plus compact loop")
    demand(sparse.linalg.norm(residual_op-electric-loop_comm)<TOL,"electric and compact-loop residual decomposition")
    # Independently use the root path p_2=e_0+e_1 for the transfer term.
    delta_E=np.array([1.,1.,0.,0.])
    coefficient=g*g*(E@(e*delta_E))+.5*g*g*np.sum(e*delta_E**2)
    rooted_electric=sparse.kron(transfer,inn)@sparse.diags(coefficient)
    demand(sparse.linalg.norm(electric-rooted_electric)<TOL,"rooted electric commutator including quadratic path term")
    wrong=sparse.kron(transfer,inn)@sparse.diags(g*g*(E@(e*delta_E)))
    missing_scalar=float(sparse.linalg.norm(electric-wrong))
    demand(missing_scalar>.01,"omitted quadratic path term discriminator")
    Bnorm=float(np.linalg.norm(B.toarray(),2))
    E_norm=np.sqrt((np.abs(psi)**2)@(E*E))
    prefix_norm=np.max(np.abs(prefix),axis=0)
    electric_upper=float(g*g*Bnorm*np.sum(e*(2*prefix_norm*E_norm+2*prefix_norm**2)))
    defect_plus=float(np.linalg.norm((U-identity)@psi))
    defect_minus=float(np.linalg.norm((U.getH()-identity)@psi))
    loop_upper=4*abs(hopping)*Bnorm*(defect_plus+defect_minus)
    actual_residual=float(np.linalg.norm(residual_op@psi))
    demand(actual_residual<=electric_upper+loop_upper+TOL,"uniform-in-free-time finite CAR residual bound")
    H0dense=H0.toarray(); Bdense=B.toarray()
    G=H-energy*identity
    rows=[]
    for t in [.7,1.4]:
        free_unitary=expm(-1j*t*H0dense)
        Bt=free_unitary@Bdense@free_unitary.conj().T
        comparator=sparse.kron(sparse.csr_matrix(Bt),inn)@psi
        exact=expm_multiply(-1j*t*G,BJ@psi)
        error=float(np.linalg.norm(exact-comparator))
        upper=abs(t)*(electric_upper+loop_upper)
        demand(error<=upper+TOL,"bounded matter Duhamel norm estimate")
        opposite=free_unitary.conj().T@Bdense@free_unitary
        wrong_error=float(np.linalg.norm(exact-sparse.kron(sparse.csr_matrix(opposite),inn)@psi))
        demand(wrong_error>error+.02,"free-time sign discriminator")
        rows.append(dict(t=t,error=error,upper=upper,wrong_time_sign_error=wrong_error))
    layers=np.tile(np.abs(n)>=cutoff-2,M)
    boundary=float(np.sum(np.abs(psi[layers])**2))
    demand(boundary<1e-16,"charged ground flux tail")
    return dict(g=g,cutoff=cutoff,dimension=dim,ground_energy=energy,
        B_norm=Bnorm,electric_residual_norm=float(np.linalg.norm(electric@psi)),
        loop_residual_norm=float(np.linalg.norm(loop_comm@psi)),total_residual_norm=actual_residual,
        electric_upper=electric_upper,loop_upper=loop_upper,
        omitted_quadratic_path_discrepancy=missing_scalar,
        plaquette_unitary_defect=defect_plus,boundary_mass=boundary,dynamics=rows)


def main():
    report["charged_rooted_matter"]=[fixture(g) for g in [.6,.4,.25]]
    report["scope"]="Finite author challenge of rooted CAR residual and free time sign; not a thermodynamic phase calculation."
    report["tolerance"]=TOL
    report["runner_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    helper=Path(__file__).with_name('rotor_joint_gauge_propagation_check_2026_09_16.py')
    report["car_helper_sha256"]=hashlib.sha256(helper.read_bytes()).hexdigest()
    report["checks"]=checks
    Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
    for row in report["charged_rooted_matter"]:
        print(f"g={row['g']:.2f}: rooted residual={row['total_residual_norm']:.6g}, t=1.4 error={row['dynamics'][-1]['error']:.6g}")
    print('per_element: executed — CAR signs, quadratic path term and residual decomposition')
    print('per_site: executed — four-site charged ring in a 36-configuration fixed-number sector')
    print('per_mode: executed — three finite flux cutoffs with original 1e-16 tail threshold')
    print('per_block: executed — bounded matter propagation at times0.7 and1.4 with sign discriminator')
    print('lattice_wide: checked and not executed — uniform bounds and joint-limit/time arguments are written proofs; finite fixtures do not execute an infinite lattice')
    print(f"TOTAL: PASS={checks} FAIL=0")


if __name__=='__main__':
    main()
