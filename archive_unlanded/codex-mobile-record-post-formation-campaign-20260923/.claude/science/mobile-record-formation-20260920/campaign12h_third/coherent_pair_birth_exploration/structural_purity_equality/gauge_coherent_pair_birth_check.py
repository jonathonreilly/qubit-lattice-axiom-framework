#!/usr/bin/env python3
"""Exact coherent neutral-pair birth and a complete gauge-loop preparation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,itertools,json
import sympy as s

HERE=Path(__file__).resolve().parent


def local():
    labels=list(itertools.product((0,1,-1),(0,1,-1),(0,1)))
    where={v:i for i,v in enumerate(labels)};D=len(labels)
    plus=s.zeros(D);minus=s.zeros(D)
    plus[where[(1,-1,1)],where[(0,0,0)]]=1
    minus[where[(-1,1,0)],where[(0,0,1)]]=1
    qx=s.diag(*(a for a,b,e in labels));qy=s.diag(*(b for a,b,e in labels))
    E=s.diag(*(s.Rational(2*e-1,2) for a,b,e in labels))
    Gx=E-qx;Gy=-E-qy
    number=s.diag(*(int(a!=0)+int(b!=0) for a,b,e in labels))
    Pvac=s.diag(*(int(a==b==0) for a,b,e in labels))
    V=plus+minus
    for J in (plus,minus,V):
        assert Gx*J==J*Gx and Gy*J==J*Gy
        assert number*J-J*number==2*J
    assert plus.T*minus==s.zeros(D) and minus.T*plus==s.zeros(D)
    assert V.T*V==Pvac and V*V==s.zeros(D)
    R=s.zeros(D)
    for j,(a,b,e) in enumerate(labels):R[where[(b,a,1-e)],j]=1
    assert R*plus*R.T==minus and R*minus*R.T==plus
    x,y=s.symbols('x y',real=True);chi=x+s.I*y
    gram=s.Matrix([[1,chi],[s.conjugate(chi),1]])
    assert s.expand(gram.det())==1-x*x-y*y
    swap=s.Matrix([[0,1],[1,0]])
    assert (swap*gram*swap-gram)==s.Matrix([[0,-2*s.I*y],[2*s.I*y,0]])
    return dict(local_dimension=D,Gauss_commutators_exact_zero=True,
                birth_adds_two_records=True,coherent_birth_isometry_on_vacant_field=True,
                same_total_loss_for_coherent_and_separate_channels=True,
                field_independent_birth_rate='beta',
                channel_parameter='chi=(sum_mu a_mu conjugate(b_mu))/beta, |chi|<=1',
                Gram_determinant=str(s.expand(gram.det())),
                edge_reversal_covariance='Im(chi)=0',
                pure_coherent_choices='chi=+1 or -1; relative phase only',
                separate_orientation_channels='chi=0')


def gauge_loop():
    # A four-cycle with cyclic reference orientations; all 16 field words
    # determine a valid zero-Gauss qutrit matter word q_i=b_i-b_(i-1).
    D=16;charges={z:tuple(((z>>i)&1)-((z>>((i-1)%4))&1) for i in range(4)) for z in range(D)}
    assert all(sum(q)==0 and all(abs(a)<=1 for a in q) for q in charges.values())
    n=[s.diag(*(int(charges[z][i]!=0) for z in range(D))) for i in range(4)]
    Q=s.diag(*(sum(a==0 for a in charges[z]) for z in range(D)))
    channels=[];loss=s.zeros(D)
    for e in range(4):
        pp=s.zeros(D);pm=s.zeros(D)
        for z in range(D):
            if charges[z][e]!=0 or charges[z][(e+1)%4]!=0:continue
            target=z^(1<<e)
            J=pp if not(z>>e&1) else pm;J[target,z]=1
        assert pp.T*pm==s.zeros(D) and pm.T*pp==s.zeros(D)
        assert Q*(pp+pm)-(pp+pm)*Q==-2*(pp+pm)
        K=pp.T*pp+pm.T*pm;loss+=K;channels.append((pp,pm,K))
    chi,beta,t=s.symbols('chi beta t',real=True)
    def born(rho,pp,pm):
        return pp*rho*pp.T+pm*rho*pm.T+chi*(pp*rho*pm.T+pm*rho*pp.T)
    def generator(rho):
        out=s.zeros(D)
        for pp,pm,K in channels:out+=beta*(born(rho,pp,pm)-(K*rho+rho*K)/2)
        return out
    cat=s.zeros(D,1);cat[0]=cat[15]=1;rho0=cat*cat.T/2
    after_first=[born(rho0,pp,pm) for pp,pm,K in channels]
    final=[]
    for e,rho in enumerate(after_first):
        pp,pm,_=channels[(e+2)%4]
        final.append(born(rho,pp,pm))
    assert all(s.trace(x)==1 for x in after_first+final)
    assert all(x==final[0] for x in final)
    rhoF=final[0];target=s.zeros(D)
    target[5,5]=target[10,10]=s.Rational(1,2)
    target[5,10]=target[10,5]=chi**2/2
    assert rhoF==target
    p0=s.exp(-4*beta*t);w=(s.exp(-beta*t)-s.exp(-4*beta*t))/3
    pF=1-(4*s.exp(-beta*t)-s.exp(-4*beta*t))/3
    rho=p0*rho0+w*sum(after_first,s.zeros(D))+pF*rhoF
    residual=(rho.diff(t)-generator(rho)).applyfunc(s.simplify)
    assert residual==s.zeros(D)
    assert s.simplify(s.trace(rho)-1)==0
    assert rho.subs(t,0)==rho0 and generator(rhoF)==s.zeros(D)
    assert all(nx*rho==rho*nx for nx in n)
    coherence=s.zeros(D);coherence[5,10]=coherence[10,5]=1
    assert s.trace(coherence*rhoF)==chi**2
    assert s.factor(s.trace(rhoF*rhoF))==(1+chi**4)/2
    # Full-occupation record cycle: two forward/reverse terms add to 2gX.
    Kcycle=s.zeros(D)
    for z,q in charges.items():
        if all(a!=0 for a in q) and all(2*((z>>i)&1)-1==q[i] for i in range(4)):
            target=z^15
            assert charges[target]==(q[-1],)+q[:-1]
            Kcycle[target,z]=1
    assert Kcycle+Kcycle.T==2*coherence
    assert coherence*rho==rho*coherence
    # The pure field plaquette only connects the two empty field words.
    field=s.zeros(D);field[0,15]=field[15,0]=1
    assert field*rho==rho*field
    return dict(physical_zero_Gauss_dimension=D,
                initial_state='(|all electric bits 0>+|all electric bits 1>)/sqrt(2), all matter vacant',
                birth_edges='All four edges, common beta>0; hopping absent in this exact preparation control.',
                exact_full_density_equation_residual_zero=True,
                full_occupation_probability=str(pF),
                mean_completion_time='5/(4 beta)',
                final_field_basis_indices=[5,10],
                final_density_in_two_state_basis='[[1,chi^2],[chi^2,1]]/2',
                terminal_gauge_invariant_cycle_coherence='chi^2',
                terminal_joint_purity='(1+chi^4)/2',
                arbitrary_occupation_monitoring_annihilates_entire_trajectory=True,
                field_plaquette_and_full_occupied_cycle_commute_with_entire_trajectory=True,
                cycle_Hamiltonian_in_full_space='2g X',
                source_of_coherence='Initially supplied gauge-loop phase; birth preserves or loses it, it is not generated from a classical mixture.',
                scope='Complete finite preparation control, not a photon phase or a native record-carrier construction.')


if __name__=='__main__':
    out=dict(created_utc=datetime.now(timezone.utc).isoformat(),
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             local_channel=local(),loop_control=gauge_loop())
    encoded=json.dumps(out,indent=2)+'\n';(HERE/'GAUGE_COHERENT_PAIR_BIRTH_RESULTS.json').write_text(encoded);print(encoded,end='')
