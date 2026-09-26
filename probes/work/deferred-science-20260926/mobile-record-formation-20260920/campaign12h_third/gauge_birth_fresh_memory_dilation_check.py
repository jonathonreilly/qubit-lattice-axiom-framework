#!/usr/bin/env python3
"""Exact finite unitary collision, energy account, and environment-rank control."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,itertools,json
import sympy as s

HERE=Path(__file__).resolve().parent


def check():
    basis=list(itertools.product((0,1,-1),(0,1,-1),(0,1)))
    index={x:i for i,x in enumerate(basis)};D=len(basis)
    vp=s.zeros(D);vm=s.zeros(D)
    vp[index[(1,-1,1)],index[(0,0,0)]]=1
    vm[index[(-1,1,0)],index[(0,0,1)]]=1
    V=vp+vm;P=V.T*V;R=V*V.T;I=s.eye(D)
    N=s.diag(*(int(a!=0)+int(b!=0) for a,b,e in basis))
    Qx=s.diag(*(a for a,b,e in basis));Qy=s.diag(*(b for a,b,e in basis))
    E=s.diag(*(s.Rational(2*e-1,2) for a,b,e in basis))
    gx=E-Qx;gy=-E-Qy
    assert P*R==s.zeros(D) and V*V==s.zeros(D)
    assert N*V-V*N==2*V
    fuel=s.diag(1,0);spent=s.diag(0,1);lower=s.Matrix([[0,0],[1,0]])
    A=s.kronecker_product(V,lower);C=A+A.T
    C2=s.kronecker_product(P,fuel)+s.kronecker_product(R,spent)
    assert C*C==C2 and C*C2==C
    theta=s.symbols('theta',real=True)
    U=s.eye(2*D)+(s.cos(theta)-1)*C2-s.I*s.sin(theta)*C
    assert (U.conjugate().T*U-s.eye(2*D)).applyfunc(s.trigsimp)==s.zeros(2*D)
    resource=s.kronecker_product(N,s.eye(2))+2*s.kronecker_product(I,fuel)
    assert resource*C==C*resource
    for G in (gx,gy):
        GG=s.kronecker_product(G,s.eye(2))
        assert GG*C==C*GG
    columns=[2*j for j in range(D)]
    K0=U.extract(columns,columns)
    K1=U.extract([2*j+1 for j in range(D)],columns)
    assert K0==I-P+s.cos(theta)*P and K1==-s.I*s.sin(theta)*V
    # Birth cannot remove or overwrite an occupied endpoint with a fresh fuel
    # probe. The full unitary still has the inverse channel on a spent probe.
    assert K0*(I-P)==I-P and K1*(I-P)==s.zeros(D)
    c,d=s.symbols('c d',real=True)
    M=lambda z:I-P+z*P
    assert M(c)*M(d)==M(c*d)
    assert M(c)*V==V and V*M(d)==d*V
    assert s.expand((1-d*d)+(1-c*c)*d*d-(1-c*c*d*d))==0
    # The complete 18-dimensional finite channel has one no-event Choi vector,
    # orthogonal to the two linearly independent formation-transition vectors.
    chi=s.symbols('chi',real=True);p=1-c*c
    vectors=s.Matrix.hstack(M(c).vec(),vp.vec(),vm.vec())
    gram=vectors.T*vectors
    assert gram==s.diag(16+2*c*c,1,1)
    block=p*s.Matrix([[1,chi],[chi,1]])
    assert s.expand(block.det()-p*p*(1-chi*chi))==0
    assert s.expand(s.trace(block)+gram[0,0]-D)==0
    # Explicit recurrence countercontrol. Reusing the same probe at theta=pi/2
    # returns the born pair to vacancy. Every fresh collision leaves it present.
    incoming=s.zeros(2*D,1);incoming[2*index[(0,0,0)]]=1
    perfect=U.subs(theta,s.pi/2)
    once=perfect*incoming;twice=perfect*once
    assert twice==-incoming
    sys_number=s.kronecker_product(N,s.eye(2))
    assert (once.conjugate().T*sys_number*once)[0]==2
    assert (twice.conjugate().T*sys_number*twice)[0]==0
    # A neutral event flag does not distinguish input electric orientation:
    # arbitrary coherent input gives one common spent-bath output on birth.
    alpha,beta=s.symbols('alpha beta')
    psi=s.zeros(D,1);psi[index[(0,0,0)]]=alpha;psi[index[(0,0,1)]]=beta
    initial=s.kronecker_product(psi,s.Matrix([1,0]))
    expected=s.cos(theta)*initial-s.I*s.sin(theta)*s.kronecker_product(V*psi,s.Matrix([0,1]))
    assert U*initial==expected
    return dict(system_dimension=D,fresh_probe_dimension=2,full_unitary_dimension=2*D,
                all_unitary_and_Gauss_identities_exact=True,
                interaction='C=V tensor |spent><fuel|+V^dagger tensor |fuel><spent|',
                resource_conserved='N_record+2 P_fuel',
                exact_mass_energy_conservation='H_free=m N_record+2m P_fuel commutes with C; no kinetic or magnetic energy included in this energy statement.',
                reduced_Kraus=['I-P+cos(theta)P','-i sin(theta)V'],
                channel_composition='Phi_c o Phi_d = Phi_(c d)',
                exact_birth_semigroup_match='cos(theta)=exp(-beta Delta_t/2)',
                small_step_coupling='theta/Delta_t ~ sqrt(beta/Delta_t)',
                occupied_record_support_unchanged_with_fresh_probe=True,
                no_orientation_information_in_event_flag=True,
                Choi_nonzero_eigenvalues_real_chi=['16+2c^2','(1-c^2)(1+chi)','(1-c^2)(1-chi)'],
                minimal_pure_environment_dimension={'chi_plus_or_minus_one':2,'absolute_chi_less_than_one':3},
                pure_environment_premise_explicit=True,
                reused_probe_control={'theta':'pi/2','record_count_after_first_collision':2,'record_count_after_second_collision':0},
                scope='Supplied fresh neutral fuel/memory qubit and interaction; no autonomous native lattice compiler or full interacting energy derivation.')


if __name__=='__main__':
    out=dict(created_utc=datetime.now(timezone.utc).isoformat(),
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),result=check())
    encoded=json.dumps(out,indent=2)+'\n';(HERE/'GAUGE_BIRTH_FRESH_MEMORY_DILATION_RESULTS.json').write_text(encoded);print(encoded,end='')
