#!/usr/bin/env python3
"""Independent exact local operators, complete C4 density, and probe controls."""
from pathlib import Path
import json
import sympy as s

HERE=Path(__file__).resolve().parent


def zero(M):
    assert all(s.simplify(x)==0 for x in M)


def unit(dim,a,b):
    M=s.zeros(dim);M[a,b]=1;return M


def local():
    ap=unit(3,1,0);am=unit(3,2,0);q=unit(3,0,0)
    up=unit(2,1,0);E=s.diag(-s.Rational(1,2),s.Rational(1,2))
    Q=s.diag(0,1,-1);n=Q*Q
    vp=s.kronecker_product(ap,up,am)
    vm=s.kronecker_product(am,up.T,ap)
    P=s.kronecker_product(q,s.eye(2),q)
    N=s.kronecker_product(n,s.eye(2),s.eye(3))+s.kronecker_product(s.eye(3),s.eye(2),n)
    gx=s.kronecker_product(s.eye(3),E,s.eye(3))-s.kronecker_product(Q,s.eye(2),s.eye(3))
    gy=-s.kronecker_product(s.eye(3),E,s.eye(3))-s.kronecker_product(s.eye(3),s.eye(2),Q)
    rev=s.zeros(18)
    for a in range(3):
        for b in range(2):
            for c in range(3):rev[(c*2+1-b)*3+a,(a*2+b)*3+c]=1
    assert rev*rev==s.eye(18) and rev*vp*rev==vm
    assert vp.T*vm==s.zeros(18) and vp.T*vp+vm.T*vm==P
    V=vp+vm
    assert V.T*V==P and V*V==s.zeros(18)
    for A in (vp,vm):
        assert N*A-A*N==2*A
        assert gx*A==A*gx and gy*A==A*gy
    return vp,vm,P,N,V


def ring_control():
    chi,z,beta=s.symbols('chi z beta',real=True)
    qs=[];ns=[]
    for site in range(4):
        q=s.diag(*[((mask>>site)&1)-((mask>>((site-1)%4))&1) for mask in range(16)])
        qs.append(q);ns.append(q*q)
    channels=[]
    for e in range(4):
        vp=s.zeros(16);vm=s.zeros(16)
        for mask in range(16):
            if ns[e][mask,mask]==0 and ns[(e+1)%4][mask,mask]==0:
                new=mask^(1<<e)
                (vm if mask&(1<<e) else vp)[new,mask]=1
        assert vp.T*vm==s.zeros(16)
        P=(s.eye(16)-ns[e])*(s.eye(16)-ns[(e+1)%4])
        assert vp.T*vp+vm.T*vm==P
        channels.append((vp,vm,P))
    initial=(unit(16,0,0)+unit(16,15,15)+unit(16,0,15)+unit(16,15,0))/2
    A,B=5,10
    Xi=unit(16,A,B)+unit(16,B,A)
    terminal=(unit(16,A,A)+unit(16,B,B)+chi**2*Xi)/2
    a=(z-z**4)/3
    full=1-s.Rational(4,3)*z+s.Rational(1,3)*z**4
    rho=z**4*initial+full*terminal
    for e in range(4):
        i=1<<e;j=15^i
        rho+=a*(unit(16,i,i)+unit(16,j,j)+chi*(unit(16,i,j)+unit(16,j,i)))/2
    L=s.zeros(16)
    for vp,vm,P in channels:
        L+=beta*(vp*rho*vp.T+vm*rho*vm.T+chi*(vp*rho*vm.T+vm*rho*vp.T)-(P*rho+rho*P)/2)
    zero(L+beta*z*rho.diff(z))
    assert s.simplify(s.trace(rho))==1
    assert rho.subs(z,1)==initial and rho.subs(z,0)==terminal
    for n in ns:zero(n*rho-rho*n)
    W=unit(16,15,0)
    zero((W+W.T)*rho-rho*(W+W.T))
    cycle=s.zeros(16)
    for mask in range(16):
        q=[int(Q[mask,mask]) for Q in qs]
        if any(v==0 for v in q):continue
        bits=[(mask>>i)&1 for i in range(4)]
        out=[bits[i]-q[i] for i in range(4)]
        if all(v in (0,1) for v in out):
            target=sum(v<<i for i,v in enumerate(out))
            assert [int(Q[target,target]) for Q in qs]==[q[(i-1)%4] for i in range(4)]
            cycle[target,mask]=1
    assert cycle==Xi
    zero((cycle+cycle.T)*rho-rho*(cycle+cycle.T))
    assert s.trace(Xi*terminal)==chi**2
    full_projector=unit(16,A,A)+unit(16,B,B)
    assert s.simplify(s.trace(full_projector*rho)-full)==0
    charge_diss=qs[0]*terminal*qs[0]-(qs[0]**2*terminal+terminal*qs[0]**2)/2
    assert s.simplify(s.trace(Xi*charge_diss))==-2*chi**2
    return dict(complete_16_state_master_equation_verified=True,
        z_definition='exp(-beta*t)',vacuum_probability='z^4',
        each_of_four_two_record_sector_probabilities='(z-z^4)/3',
        full_probability=str(full),survival='(4*z-z^4)/3',
        mean_completion_time='5/(4*beta)',
        expected_record_number='4-(8/3)*z-(4/3)*z^4',
        terminal_cycle_coherence='chi^2',terminal_off_diagonal_density='chi^2/2',
        occupation_monitoring_annihilates_complete_density=True,
        real_field_loop_and_occupied_cycle_H_commute_with_complete_density=True,
        charge_monitoring_countercontrol='Unit-rate Q_0 dephasing changes terminal cycle expectation at rate -2*chi^2.')


def probe_control(vp,vm,P,N,V):
    fuel=unit(2,0,0);spent=unit(2,1,1);sf=unit(2,1,0)
    C=s.kronecker_product(V,sf)+s.kronecker_product(V.T,sf.T)
    M=s.kronecker_product(P,fuel)+s.kronecker_product(V*V.T,spent)
    assert C*C==M and C*C*C==C
    total=s.kronecker_product(N,s.eye(2))+2*s.kronecker_product(s.eye(18),fuel)
    assert total*C==C*total
    U=s.eye(36)+(s.sqrt(2)/2-1)*M-s.I*s.sqrt(2)/2*C
    zero(U.conjugate().T*U-s.eye(36))
    # Extract the two reduced Kraus operators with a pure fresh fuel input.
    kraus=[s.Matrix(18,18,lambda i,j:U[2*i+a,2*j]) for a in range(2)]
    zero(kraus[0]-(s.eye(18)-P+s.sqrt(2)/2*P))
    zero(kraus[1]+s.I*s.sqrt(2)/2*V)
    # Full finite-step Choi ranks: no-jump sector is independent of both births.
    vec0=kraus[0].vec();vecp=vp.vec();vecm=vm.vec()
    ranks=[]
    support=sorted(set(i for v in (vec0,vecp,vecm) for i,a in enumerate(v) if a))
    for chi in [-1,0,s.Rational(1,3),1]:
        J=vec0*vec0.T+s.Rational(1,2)*(vecp*vecp.T+vecm*vecm.T+chi*(vecp*vecm.T+vecm*vecp.T))
        rank=J.extract(support,support).rank()
        assert rank==(2 if abs(chi)==1 else 3)
        ranks.append(dict(chi=str(chi),choi_rank=rank))
    # Composition on a separate five-state representative of the partial-isometry algebra.
    p=unit(5,0,0)+unit(5,1,1);plus=unit(5,2,0);minus=unit(5,3,1)
    def channel(r,c,chi):
        k=s.eye(5)-p+c*p
        return k*r*k+(1-c*c)*(plus*r*plus.T+minus*r*minus.T+chi*(plus*r*minus.T+minus*r*plus.T))
    c1=s.sqrt(s.Rational(2,3));c2=s.sqrt(s.Rational(3,5));chi=s.Rational(1,3)
    for i in range(5):
        for j in range(5):
            r=unit(5,i,j)
            zero(channel(channel(r,c1,chi),c2,chi)-channel(r,c1*c2,chi))
    # Reuse at theta=pi/2 returns the original vacancy on the second collision.
    Uhalf=s.eye(36)-M-s.I*C
    psi=s.zeros(36,1);psi[0]=1
    psi1=Uhalf*psi;psi2=Uhalf*psi1
    assert (psi1.conjugate().T*s.kronecker_product(N,s.eye(2))*psi1)[0]==2
    assert psi2==-psi
    rho1=V*unit(18,0,0)*V.T
    assert V*rho1*V.T==s.zeros(18) and (s.eye(18)-P)*rho1*(s.eye(18)-P)==rho1
    return dict(C_cubic_identity=True,resonant_number_fuel_conservation=True,
        fresh_probe_unitary_and_Kraus_identity_at_theta_pi_over_4=True,
        finite_step_choi_ranks=ranks,
        two_fresh_channel_composition_verified_on_25_matrix_units=True,
        reused_probe_theta_pi_over_2='First collision creates two records; second returns exactly to the original vacancy state up to phase.',
        fresh_probe_theta_pi_over_2='The second fresh-fuel collision leaves the two records present.',
        exact_semigroup_parameter='cos(theta)=exp(-beta*dt/2), 0<=theta<=pi/2')


def missing_bijection_control():
    # Two same-occupation field configurations both map to one other pattern.
    H=unit(4,2,0)+unit(4,2,1)+unit(4,0,2)+unit(4,1,2)
    J=unit(4,3,2)
    patterns=[(1,1,0,0),(1,1,0,0),(1,0,1,0),(1,1,1,1)]
    rho=(unit(4,0,0)+unit(4,1,1)-unit(4,0,1)-unit(4,1,0))/2
    L=-s.I*(H*rho-rho*H)+J*rho*J.T-(J.T*J*rho+rho*J.T*J)/2
    for x in range(4):
        n=s.diag(*[a[x] for a in patterns])
        L+=n*rho*n-(n*n*rho+rho*n*n)/2
    assert L==s.zeros(4)
    return dict(graph_component_has_positive_loss=True,
        stationary_dark_density_despite_occupation_monitoring=True,
        violated_hypothesis='Off-pattern block map is not a partial bijection: two same-pattern configurations map to the same target.',
        dark_vector='(c1-c2)/sqrt(2)')


if __name__=='__main__':
    vp,vm,P,N,V=local()
    result={'local_18_state_Gauss_number_loss_and_reversal_identities':True,
        'C4':ring_control(),'probe':probe_control(vp,vm,P,N,V),
        'partial_bijection_countercontrol':missing_bijection_control()}
    (HERE/'COHERENT_INSTRUMENT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
