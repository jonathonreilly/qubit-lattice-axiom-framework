"""Portable independently written finite diagnostics for boundary reflection.

The original source-exposed implementation and execution receipts are preserved
under outputs/autonomous_boundary_reflection_2026_10_16_inputs/independent_check.
This adaptation returns reports to the primary runner. It is not a proof of
infinite volume or all future times. No helper registry change is needed:
the primary imports this module directly.
"""
import hashlib
import json
import math
import platform
import resource
import sys
import time
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import eigh_tridiagonal, expm
from scipy.special import roots_legendre, jv
import sympy as sp

AUDIT_TIMEOUT_SEC = 120

def run_reflection_checks():
    START = time.monotonic()
    RESULTS = {}


    def emit(name, value):
        RESULTS[name] = value
        print(name + ": " + json.dumps(value, sort_keys=True), flush=True)


    def norm(x):
        return float(np.linalg.norm(x))


    emit("runtime", {
        "executable": sys.executable,
        "python": sys.version,
        "platform": platform.platform(),
        "numpy": np.__version__,
        "scipy": scipy.__version__,
        "sympy": sp.__version__,
        "cpu_seconds_cap": 120,
        "wall_seconds_cap": "primary runner envelope",
        "largest_clock_dimension": 1024,
        "largest_quadrature_order": 768,
        "largest_full_spin_dimension": 64,
        "max_old_clock_isometry_rows": 3072,
        "claimed_scope": "Exact symbolic finite identities and finite numerical falsification only",
    })

    # Exact rational and local-matrix checks.  No expression read from the note.
    z, w, J = sp.symbols("z w J", nonzero=True)
    r = sp.symbols("r")
    E = 2*J-J*(z+1/z)
    boundary_equation = (2*J+w-E)*(1+r)-J*(1/z+r*z)
    r_solved = sp.solve(boundary_equation, r)[0]
    q = -J/w
    bound_orthogonality = sp.factor(1/(1-q/z)+r_solved/(1-q*z))
    bound_energy = sp.factor(2*J-J*(q+1/q))
    emit("exact_boundary", {
        "reflection_solved_from_row_zero": str(sp.factor(r_solved)),
        "geometric_bound_overlap_numerator": str(bound_orthogonality),
        "bound_energy_from_bulk_recurrence": str(bound_energy),
        "center_nominal_reflection": str(sp.simplify(r_solved.subs({z:sp.I,w:sp.Rational(4,3)*J}))),
        "center_free_reflection": str(sp.simplify(r_solved.subs({z:sp.I,w:0}))),
    })
    assert bound_orthogonality == 0
    assert sp.simplify(r_solved.subs({z:sp.I,w:sp.Rational(4,3)*J})-(-7-24*sp.I)/25) == 0

    u, sigma = sp.symbols("u sigma", positive=True)
    amp = sp.sqrt(15)/(4*sp.sqrt(sigma))
    f2 = sp.integrate(amp**2*(1-u*u)**2*sigma,(u,-1,1))
    f1 = sp.integrate(amp*(1-u*u)*sigma,(u,-1,1))
    fp = sp.integrate(4*amp*u,(u,0,1))
    emit("exact_packet_integrals", {"L2_squared":str(f2),"L1":str(f1),"derivative_L1":str(fp)})
    assert f2 == 1

    I2=sp.eye(2)
    Xs=sp.Matrix([[0,1],[1,0]])
    Zs=sp.diag(1,-1)
    as_=sp.Matrix([[0,1],[0,0]])
    ns=sp.diag(0,1)
    bond=sp.kronecker_product(ns,I2)+sp.kronecker_product(I2,ns)-sp.kronecker_product(as_.T,as_)-sp.kronecker_product(as_,as_.T)
    xx=sp.kronecker_product(Xs,Xs)
    zz=sp.kronecker_product(Zs,Zs)
    ks=2*sp.eye(4)+zz
    pminus=(sp.eye(4)-xx)/2
    bs=sp.kronecker_product(pminus,ns)
    Ws=((9+12*sp.I)*sp.eye(4)+(-16+12*sp.I)*xx)/25
    cs=(-7-24*sp.I)/25
    gate_identity=sp.simplify((sp.eye(4)-pminus)+cs*pminus-cs*Ws)
    emit("exact_local_blocks", {
        "clock_bond_divided_by_J_eigenvalue_multiplicity": {str(k):int(v) for k,v in bond.eigenvals().items()},
        "boundary_divided_by_w_eigenvalue_multiplicity": {str(k):int(v) for k,v in bs.eigenvals().items()},
        "old_K_eigenvalue_multiplicity": {str(k):int(v) for k,v in ks.eigenvals().items()},
        "K_XX_commutator_zero": bool(ks*xx-xx*ks==sp.zeros(4)),
        "R_equals_global_phase_W": bool(gate_identity==sp.zeros(4)),
        "W_unitary": bool(sp.simplify(Ws.conjugate().T*Ws)==sp.eye(4)),
    })
    assert gate_identity == sp.zeros(4)
    assert all(ev>=0 for ev in bond.eigenvals())
    assert all(ev>=0 for ev in bs.eigenvals())

    # Full 6-clock-qubit Hamiltonian from bit operations, including all occupations.
    # This finite interval contains J*n0 and every internal bond; its right endpoint
    # has one missing exterior bond.  It is not used for the time propagation check.
    Lspin=6
    Hspin=np.zeros((2**Lspin,2**Lspin))
    numbers=[]
    for b in range(2**Lspin):
        occ=[(b>>j)&1 for j in range(Lspin)]
        numbers.append(sum(occ))
        Hspin[b,b]+=occ[0]
        for j in range(Lspin-1):
            Hspin[b,b]+=occ[j]+occ[j+1]
            if occ[j]!=occ[j+1]:
                Hspin[b^(1<<j)^(1<<(j+1)),b]-=1
    spin_rows=[]
    for N in range(Lspin+1):
        idx=np.flatnonzero(np.array(numbers)==N)
        ev=np.linalg.eigvalsh(Hspin[np.ix_(idx,idx)])
        spin_rows.append({"N":N,"dimension":int(len(idx)),"minimum":float(ev[0]),"maximum":float(ev[-1]),"analytic_upper":4*N})
        assert ev[0]>-1e-12 and ev[-1]<=4*N+1e-12
    emit("all_occupation_spin_check_J1", spin_rows)

    # Independent finite Jacobi evolution, J=1.  The finite diagonal is 2J at both
    # endpoints (a remote Dirichlet wall); hence it matches the infinite half-line
    # on all rows except the last missing outward hopping.  Initial long tails and
    # this wall limit its use; it cannot prove any all-future statement.
    Jnum=1.0
    sigma_num=0.15
    T=80.0
    clock_sizes=(768,1024)
    quadrature_order=768
    sample_s=(T,2*T,3*T)
    w_values=(0.0,1.0,4/3,5/3)
    v=math.sqrt(3)
    F0=math.sqrt(15*sigma_num)/3
    F1=math.sqrt(15)/(2*math.sqrt(sigma_num))
    CA=F1+2/math.sqrt(3)*F0
    CB=F1+(11/3+2/math.sqrt(3))*F0
    c=complex((-7-24j)/25)


    def quadrature(L, Q):
        x, weight=roots_legendre(Q)
        k=math.pi/2+sigma_num*x
        f=math.sqrt(15)/(4*math.sqrt(sigma_num))*(1-x*x)
        weighted=weight*sigma_num*f/math.sqrt(2*math.pi)
        energy=2*(1-np.cos(k))
        pos=np.exp(1j*np.outer(np.arange(L),k))
        return k,weighted,energy,pos


    def solve_r(k, boundary_strength):
        # Solve the scalar boundary row, rather than inserting a quotient copied
        # from the proposal.  Bulk E and both plane-wave values enter the row.
        energy=2*(1-np.cos(k))
        row_diag=2+boundary_strength-energy
        return -(row_diag-np.exp(-1j*k))/(row_diag-np.exp(1j*k))


    def packets(qdata, s, boundary_strength):
        k,weighted,energy,pos=qdata
        g=weighted*np.exp(-1j*energy*s)
        incoming=pos.conj()@g
        outgoing=pos@(g*solve_r(k,boundary_strength))
        return incoming,outgoing


    emit("numerical_parameters", {
        "J":Jnum,"sigma":sigma_num,"T":T,"sizes":clock_sizes,
        "quadrature":quadrature_order,"s_samples":sample_s,"w_samples":w_values,
        "CA":CA,"CB":CB,
        "initial_b_tail_upper":CB/math.sqrt(math.pi*v*T),
        "note": "Widths and times chosen for finite diagnostics, not the sufficient epsilon schedule in (20).",
    })

    evolution_rows=[]
    bound_rows=[]
    coarse_results={}
    fine_results={}
    for L in clock_sizes:
        qdata=quadrature(L,quadrature_order)
        a_ready,_=packets(qdata,-T,0)
        A=norm(a_ready)
        chi=a_ready/A
        free_packets={s:packets(qdata,s,0)[1] for s in sample_s}
        for strength in w_values:
            diagonal=np.full(L,2.0)
            diagonal[0]+=strength
            eig,U=eigh_tridiagonal(diagonal,-np.ones(L-1))
            coeff=U.T@chi
            a0,b0=packets(qdata,-T,strength)
            continuum0=a0+b0
            if strength>1:
                qb=-1/strength
                bound=np.sqrt(1-qb*qb)*qb**np.arange(L)
                bound_rows.append({"L":L,"w":strength,
                    "top_eigenvalue":float(eig[-1]),"analytic_bound_energy":2+strength+1/strength,
                    "ready_bound_amplitude":float(abs(np.vdot(bound,chi))),
                    "continuum_bound_overlap":float(abs(np.vdot(bound,continuum0))),
                    "ready_minus_continuum":norm(chi-continuum0),
                    "twice_reflected_ready_tail":2*norm(b0)})
            for s in sample_s:
                elapsed=T+s
                actual=U@(np.exp(-1j*eig*elapsed)*coeff)
                af,bf=packets(qdata,s,strength)
                continuum=af+bf
                # This comparison uses full finite evolution on the left.
                beta=free_packets[s]/norm(free_packets[s])
                target=beta if strength==0 else c*beta
                err=norm(actual-target)
                delta=0.0 if strength==0 else (17/3)*sigma_num+2*abs(strength-4/3)
                analytic=2*CB/math.sqrt(math.pi*v*T)+2*CA/math.sqrt(math.pi*v*s)+delta
                evolution_rows.append({"L":L,"w":strength,"s":s,"elapsed":elapsed,
                    "A_ready":A,"finite_continuum_norm":norm(continuum),
                    "full_sector_target_error":err,"stated_upper_bound":analytic,
                    "actual_minus_continuum":norm(actual-continuum),
                    "initial_actual_minus_continuum":norm(chi-continuum0),
                    "incoming_tail_norm":norm(af),"incoming_tail_upper":CA/math.sqrt(math.pi*v*s),
                    "ready_reflected_tail_norm":norm(b0),
                    "rightmost_32_probability":float(np.vdot(actual[-32:],actual[-32:]).real)})
                assert err<=analytic+1e-8
                assert norm(af)<=CA/math.sqrt(math.pi*v*s)+1e-8
                assert norm(b0)<=CB/math.sqrt(math.pi*v*T)+1e-8
                (coarse_results if L==768 else fine_results)[(strength,s)]=(actual,beta)
    emit("bound_state_diagnostics",bound_rows)
    emit("finite_jacobi_evolution",evolution_rows)

    size_rows=[]
    for key,(coarse,_) in coarse_results.items():
        fine=fine_results[key][0]
        padded=np.pad(coarse,(0,len(fine)-len(coarse)))
        size_rows.append({"w":key[0],"s":key[1],"padded_size_difference":norm(padded-fine)})
    emit("finite_size_diagnostic",size_rows)

    # Quadrature order doubling/half-order check at the largest momentum phases.
    qd_low=quadrature(768,384)
    qd_high=quadrature(768,768)
    quad_rows=[]
    for strength in (0,4/3):
        for s in (-T,3*T):
            al,bl=packets(qd_low,s,strength)
            ah,bh=packets(qd_high,s,strength)
            quad_rows.append({"w":strength,"s":s,"incoming_change":norm(al-ah),"outgoing_change":norm(bl-bh)})
    emit("quadrature_order_change_384_to_768",quad_rows)

    # Complete old/clock input isometry: old Hamiltonian kept literally as 2I+ZZ.
    I4=np.eye(4)
    XX=np.array(xx,dtype=complex)
    K=np.array(ks,dtype=complex)
    W=np.array(Ws,dtype=complex)
    Pminus=(I4-XX)/2
    Pplus=I4-Pminus
    joint_rows=[]
    for s in sample_s:
        elapsed=T+s
        plus,beta=coarse_results[(0.0,s)]
        minus,_=coarse_results[(4/3,s)]
        old=expm(-1j*K*elapsed)
        actual=np.kron(old@Pplus,plus[:,None])+np.kron(old@Pminus,minus[:,None])
        target=np.kron(c*old@W,beta[:,None])
        missing_global=np.kron(old@W,beta[:,None])
        missing_K=np.kron(c*W,beta[:,None])
        joint_rows.append({"s":s,
            "full_joint_operator_error":float(np.linalg.norm(actual-target,2)),
            "maximum_sector_error":max(norm(plus-beta),norm(minus-c*beta)),
            "wrong_no_global_phase_error":float(np.linalg.norm(actual-missing_global,2)),
            "wrong_no_old_aging_error":float(np.linalg.norm(actual-missing_K,2))})
    emit("full_joint_phase_and_aging_discriminators",joint_rows)
    assert max(row["full_joint_operator_error"] for row in joint_rows) < 0.12
    assert min(row["wrong_no_global_phase_error"] for row in joint_rows) > 1
    assert min(row["wrong_no_old_aging_error"] for row in joint_rows) > 1


    # Conjugating the reflection coefficient must not solve the same boundary row.
    kprobe=np.linspace(math.pi/3,2*math.pi/3,101)
    rprobe=solve_r(kprobe,4/3)
    ep=2*(1-np.cos(kprobe))


    def row_residual(reflection):
        return (2+4/3-ep)*(1+reflection)-(np.exp(-1j*kprobe)+reflection*np.exp(1j*kprobe))


    emit("reflection_conjugation_discriminator",{
        "correct_max_boundary_residual":float(np.max(np.abs(row_residual(rprobe)))),
        "conjugated_max_boundary_residual":float(np.max(np.abs(row_residual(np.conj(rprobe))))),
        "conjugated_center_residual":float(abs(row_residual(np.conj(rprobe))[50])),
    })
    assert np.max(np.abs(row_residual(rprobe)))<1e-12
    assert np.max(np.abs(row_residual(np.conj(rprobe))))>1

    # The correction to the g support quantifier is necessary if 'band' means
    # the full spectral band.  At k=pi/12, n=0,t=1,J=1, E'(k)<sqrt(3).
    emit("support_quantifier_counterexample",{
        "k":math.pi/12,"n":0,"t":1,"J":1,
        "phase_derivative":2*math.sin(math.pi/12),
        "incorrect_full_band_claim_lower":math.sqrt(3),
        "scope": "Counterexample to the intermediate derivative claim on (0,pi), not to the packet theorem with its stated support.",
    })

    # Print the sufficient schedule without simulating its much larger apparatus.
    schedule=[]
    for epsilon in (1.0,0.5,0.1):
        sig=3*epsilon/68
        f0=math.sqrt(15*sig)/3
        f1=math.sqrt(15)/(2*math.sqrt(sig))
        ca=f1+2/math.sqrt(3)*f0
        cb=f1+(11/3+2/math.sqrt(3))*f0
        travel=max(1/v,16*(ca+cb)**2/(math.pi*v*epsilon**2))
        terms=[2*(ca+cb)/math.sqrt(math.pi*v*travel),(17/3)*sig,2*(epsilon/8)]
        schedule.append({"epsilon":epsilon,"J":1,"sigma":sig,"T":travel,"three_error_terms":terms,"sum":sum(terms)})
    emit("sufficient_schedule_arithmetic",schedule)

    emit("completion",{
        "elapsed_seconds":time.monotonic()-START,
        "ru_maxrss_platform_units":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "limitations": [
            "No finite numerical test certifies all future time or infinite volume.",
            "The numerical test uses J=1; it preserves the stated literal K and is distinct from the nominal local-load choice J=3/16.",
            "Finite-size, quadrature and floating-point errors are measured diagnostically, not rigorously enclosed.",
            "This is a source-exposed check; the target constants were known before implementation.",
        ],
    })
    return RESULTS


def run_readiness_checks():
    start=time.monotonic()
    results={}

    def emit(key,data):
        results[key]=data
        print(key+': '+json.dumps(data,sort_keys=True),flush=True)

    emit('runtime',{'python':sys.version,'executable':sys.executable,'platform':platform.platform(),
        'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__,
        'cpu_cap_seconds':120,'wall_cap_seconds':'primary runner envelope','largest_exact_matrix':12,
        'largest_numeric_clock_matrix':128,'largest_bessel_index':299})

    # Exact powers use rational entries and a long-enough finite surrogate.  At
    # degrees <=d the far boundary of the length-12 surrogate is unreachable,
    # so these particular matrix elements equal the infinite half-line exactly.
    J=sp.Rational(3,16)
    w=sp.Rational(1,4)
    rho=17*J/6
    c=rho
    N=3
    M=7
    L=12
    d=M-N+1

    def A_exact(length):
        A=sp.diag(*[(2*J-c)/rho for _ in range(length)])
        A[0,0]+=w/rho
        for j in range(length-1):
            A[j,j+1]=A[j+1,j]=-J/rho
        return A

    Am=A_exact(M)
    Al=A_exact(L)
    vm=sp.zeros(M,1)
    vl=sp.zeros(L,1)
    vm[N-1]=vl[N-1]=1
    path_rows=[]
    for degree in range(d+1):
        embedded=vm.col_join(sp.zeros(L-M,1))
        difference=vl-embedded
        nonzero=[{'site':j,'amplitude':str(difference[j])} for j in range(L) if difference[j]!=0]
        path_rows.append({'degree':degree,'nonzero_difference':nonzero})
        if degree<d:
            assert not nonzero
        else:
            assert nonzero==[{'site':M,'amplitude':str((-J/rho)**d)}]
        vm=Am*vm
        vl=Al*vl
    emit('exact_first_removed_site_path',{'J':str(J),'w':str(w),'rho':str(rho),'N':N,'M':M,'L':L,'first_nonmatching_degree':d,'rows':path_rows})

    # Exact finite-support normalization inequality: for orthogonal retained and
    # discarded pieces of norms B and q, A=sqrt(B^2+q^2), the squared distance is
    # 2(1-B/A).  Since 1-sqrt(1-x^2)<=x^2 for x=q/A in [0,1], distance<=sqrt(2)q/A,
    # and therefore the proposed 2q/A is valid with slack.  Check endpoint arithmetic
    # in A3 with the stated worst A>=3/4 and q<=eta/4.
    emit('normalization_slack',{'A_lower':'3/4','tail_upper':'eta_p/4',
        'A2_distance_upper':'2 tail / A','using_worst_bounds':'2 eta_p / 3 <= eta_p',
        'minimum_retained_norm_for_eta_le_half':'5/8',
        'comment':'The addendum uses the weaker 4*tail upper bound; its constants are safe.'})

    # Finite numerical horizon example, using the actual nominal dyadic J,w and
    # arbitrary normalized input with support N=3.  This probes A4/A5 only, not
    # the gate accuracy schedule.  The length-128 reference is finite.
    Jf=float(J)
    wf=float(w)
    rhof=float(rho)
    Nf=3
    Mf=24
    Lf=128
    mu=1.0
    Tobs=20.0
    zeta=0.001
    dMf=Mf-Nf+1
    threshold=(rhof*Tobs*math.sinh(mu)+math.log(4/((1-math.exp(-mu))*zeta)))/mu
    initial=np.array([1,1j,2],dtype=complex)/math.sqrt(6)

    def evolution(length,t):
        diag=np.full(length,2*Jf)
        diag[0]+=wf
        ev,U=eigh_tridiagonal(diag,-Jf*np.ones(length-1))
        chi=np.pad(initial,(0,length-Nf))
        return U@(np.exp(-1j*ev*t)*(U.T@chi))

    rows=[]
    for t in (0,5,10,20):
        finite=evolution(Mf,t)
        long=evolution(Lf,t)
        actual=float(np.linalg.norm(long-np.pad(finite,(0,Lf-Mf))))
        x=rhof*t
        finite_bessel_sum=4*float(np.sum(np.abs(jv(np.arange(dMf,300),x))))
        contour=4*math.exp(-mu*dMf+x*math.sinh(mu))/(1-math.exp(-mu))
        rows.append({'t':t,'finite_vs_length128_error':actual,'bessel_tail_through_299':finite_bessel_sum,'contour_bound':contour})
        assert actual<=contour+2e-13
    emit('finite_horizon_example',{'J':Jf,'w':wf,'rho':rhof,'N':Nf,'M':Mf,'L_reference':Lf,
        'd_M':dMf,'mu':mu,'Tobs':Tobs,'zeta':zeta,'required_real_distance':threshold,
        'A5_satisfied':dMf>=threshold,'rows':rows,
        'limit':'The length-128 reference and Bessel-tail truncation are diagnostic, not a certified infinite evolution.'})
    assert dMf>=threshold

    # Evaluate integer choices only; the large states for the sufficient gate
    # schedule are deliberately not constructed or numerically evolved.
    schedule=[]
    for epsilon,eta_p,zeta in ((1.0,0.5,0.1),(0.5,0.25,0.01),(0.1,0.1,0.01)):
        sig=3*epsilon/68
        F0=math.sqrt(15*sig)/3
        F1=math.sqrt(15)/(2*math.sqrt(sig))
        CA=F1+2/math.sqrt(3)*F0
        CB=F1+(11/3+2/math.sqrt(3))*F0
        v=math.sqrt(3)*Jf
        T=max(1/v,16*(CA+CB)**2/(math.pi*v*epsilon**2))
        required=max(1,2*Jf*T,16*(F1+F0)**2/(math.pi*eta_p**2))
        cutoff=math.ceil(2*Jf*T+required)
        gap=cutoff-2*Jf*T
        tail=(F1+F0)/math.sqrt(math.pi*gap)
        horizon=2*T
        distance=(rhof*horizon*math.sinh(1)+math.log(4/((1-math.exp(-1))*zeta)))
        sites=max(cutoff,cutoff-1+math.ceil(distance))
        horizon_bound=4*math.exp(-(sites-cutoff+1)+rhof*horizon*math.sinh(1))/(1-math.exp(-1))
        schedule.append({'epsilon':epsilon,'eta_p':eta_p,'zeta':zeta,'J':Jf,
            'T':T,'N':cutoff,'d':gap,'A1_tail_bound':tail,'eta_p_divided_by_four':eta_p/4,
            'Tobs':horizon,'M':sites,'integer_distance':sites-cutoff+1,
            'required_distance':distance,'A4_horizon_bound':horizon_bound})
        assert tail<=eta_p/4*(1+1e-13)
        assert gap>=max(1,2*Jf*T)
        assert horizon_bound<=zeta*(1+1e-8)
    emit('sufficient_integer_choices_not_evolved',schedule)
    emit('completion',{'elapsed_seconds':time.monotonic()-start,
        'ru_maxrss_platform_units':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    return results
