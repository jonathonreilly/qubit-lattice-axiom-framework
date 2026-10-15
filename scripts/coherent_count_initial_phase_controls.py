#!/usr/bin/env python3
"""Exact synthetic controls for state-free contrasts; no empirical scalar fit."""
import collections
import random
import sympy as s

AUDIT_TIMEOUT_SEC = 120


def column_projector(M):
    cols=M.columnspace()
    if not cols: return s.eye(M.rows)
    V=s.Matrix.hstack(*cols)
    return s.eye(M.rows)-V*(V.T*V).inv()*V.T


def controls():
    counts=collections.Counter()
    def ok(name,value):
        assert bool(value), name
        counts[name]+=1
    ts=list(map(s.Rational,range(9))); n=len(ts)-1
    ops=[]; rows=[]
    for t in ts:
        a=1+t/100; b=1+t/80; c=s.Rational(1,4)+t*t/5000
        d=s.Rational(1,5)+t/200; e=s.Rational(1,6)+t*t/4000
        B=s.Matrix([[1,a,b],[1,a,c],[1,d,e]])
        ops.append(B); rows.append((s.Matrix([[1,0,0]])*B.inv()))
        ok('invertible_synthetic_phase_operators',B.det()!=0)
    W=s.Matrix.vstack(*rows)
    H=s.Matrix([[1,t,t*t] for t in ts]); sig=s.Matrix([t**4 for t in ts])
    K=W.row_join(H); P=column_projector(K)
    ok('projector_symmetric',P==P.T)
    ok('projector_idempotent',P*P==P)
    ok('projector_annihilates_declared_nuisance',P*K==s.zeros(len(ts),K.cols))
    norm=(sig.T*P*sig)[0]
    ok('signal_has_nonzero_observable_contrast',norm>0)
    h=P*sig/norm
    ok('contrast_unit_signal', (h.T*sig)[0]==1)
    ok('contrast_eliminates_initial_phase',h.T*W==s.zeros(1,3))
    ok('contrast_eliminates_H',h.T*H==s.zeros(1,H.cols))
    theta=s.Rational(3,7); beta=s.Matrix([100,-2,s.Rational(1,9)])
    G=theta*sig+H*beta
    states=[s.Matrix([G[i],1000+2*t+t*t,2000+t**3]) for i,t in enumerate(ts)]
    phases=[B*z for B,z in zip(ops,states)]
    increments=[phases[i]-phases[i-1] for i in range(1,n+1)]
    cumulative=[s.zeros(3,1)]
    for dq in increments: cumulative.append(cumulative[-1]+dq)
    r=s.Matrix([(rows[i]*cumulative[i])[0] for i in range(n+1)])
    ok('cumulative_count_identity',G==r+W*phases[0])
    recovered=(h.T*r)[0]
    ok('synthetic_amplitude_recovered',recovered==theta)
    # Recovery uses increments, known operators and declared nuisance/signature only.
    rng=random.Random(202610142)
    for scale in [1,10,1000,10**9]:
        for j in range(12):
            delta=s.Matrix([scale*rng.randint(-20,20) for _ in range(3)])
            G2=G+W*delta
            ok('arbitrary_initial_offset_contrast_invariant',(h.T*G2)[0]==theta)
            q2=[phases[i]+delta for i in range(n+1)]
            ok('initial_offset_preserves_all_counts',all(q2[i]-q2[i-1]==increments[i-1] for i in range(1,n+1)))
    # A target lying in the modeled nuisance span is honestly removed too.
    nuisance_signature=H*s.Matrix([2,3,4])
    ok('overlapping_signature_is_removed',P*nuisance_signature==s.zeros(n+1,1))
    # Coefficients of the independent count increments, not endpoint-white errors.
    b=[sum((h[i]*rows[i] for i in range(k,n+1)),s.zeros(1,3)) for k in range(1,n+1)]
    flat=s.Matrix([b[k][l] for k in range(n) for l in range(3)])
    E=s.Matrix([s.Rational(1,1000*(j+1)) for j in range(3*n)])
    eta=s.Matrix([s.sign(flat[j])*E[j] for j in range(3*n)])
    cumulative_err=[s.zeros(3,1)]
    for k in range(n): cumulative_err.append(cumulative_err[-1]+eta[3*k:3*k+3,0])
    endpoint_err=s.Matrix([(rows[i]*cumulative_err[i])[0] for i in range(n+1)])
    direct=(h.T*endpoint_err)[0]
    sum_form=(flat.T*eta)[0]
    box=sum(abs(flat[j])*E[j] for j in range(3*n))
    ok('increment_error_propagation_exact',direct==sum_form)
    ok('increment_box_bound_saturated',direct==box)
    u=s.Matrix([s.Rational((-1)**j,j+1) for j in range(3*n)])
    Sigma=s.eye(3*n)/100+u*u.T
    actual_variance=(flat.T*Sigma*flat)[0]
    formula=(flat.T*flat)[0]/100+(flat.T*u)[0]**2
    ok('correlated_increment_variance',actual_variance==formula and formula>=0)
    diag_only=sum(flat[j]**2*Sigma[j,j] for j in range(3*n))
    ok('dropping_increment_correlations_detected',actual_variance!=diag_only)
    # Counterfactuals discriminate errors in the construction.
    PH=column_projector(H)
    h_wrong=PH*sig/(sig.T*PH*sig)[0]
    ok('omitting_initial_nuisance_detected',(h_wrong.T*r)[0]!=theta)
    wrong_r=s.Matrix([0]+[(rows[i]*increments[i-1])[0] for i in range(1,n+1)])
    ok('omitting_cumulative_sum_detected',(h.T*wrong_r)[0]!=theta)
    # Perturb the inverse observation rows in a direction not canceled by h.
    dW=s.zeros(n+1,3);dW[1,0]=1
    leakage=(h.T*dW*s.Matrix([1,0,0]))[0]
    ok('nominal_elimination_not_uniform_under_operator_error',leakage!=0)
    ok('unbounded_state_amplifies_operator_error',(h.T*dW*s.Matrix([10**9,0,0]))[0]==10**9*leakage)
    # Stronger positive example: exact affine inverse-row family, all nonzero.
    W0=s.Matrix([[1,t,t*t] for t in ts])
    W1=s.Matrix([[0,t**3,t**4] for t in ts])
    Z=W0.row_join(W1); Pr=column_projector(Z)
    sr=s.Matrix([t**5 for t in ts]);hr=Pr*sr/(sr.T*Pr*sr)[0]
    ok('robust_affine_initial_elimination',hr.T*W0==s.zeros(1,3) and hr.T*W1==s.zeros(1,3))
    robust_cases=[]
    # Use fixed measured cumulative phases; each allowed operator defines its own G.
    c=[s.Matrix([t**6,t**3+2*t,t*t+3*t]) for t in ts]
    nominal_r=s.Matrix([(W0[i,:]*c[i])[0] for i in range(n+1)])
    for lam in [s.Rational(-1,5),s.Rational(0),s.Rational(1,10),s.Rational(1,4)]:
        WL=W0+lam*W1
        qinitial=s.Matrix([10**12,-10**15,10**18])
        GL=s.Matrix([(WL[i,:]*(qinitial+c[i]))[0] for i in range(n+1)])
        rl=s.Matrix([(WL[i,:]*c[i])[0] for i in range(n+1)])
        ok('robust_contrast_ignores_unbounded_initial_example',(hr.T*GL)[0]==(hr.T*rl)[0])
        # Each row is the first inverse row of an explicitly invertible B_i.
        for i in range(n+1):
            row=WL[i,:]
            B=s.Matrix([[1,-row[1],-row[2]],[0,1,0],[0,0,1]])
            ok('robust_rows_have_invertible_operator',s.Matrix([[1,0,0]])*B.inv()==row)
        err=abs((hr.T*(rl-nominal_r))[0])
        bound=sum(abs(hr[i])*sum(abs(lam*W1[i,j])*abs(c[i][j]) for j in range(3)) for i in range(n+1))
        ok('data_based_operator_bound',err<=bound)
        robust_cases.append({'lambda':str(lam),'actual_contrast_change':str(err),'bound':str(bound)})
    # Covariance does not determine residual mean: an exact finite distribution.
    delta=s.Rational(2,9); N=n+1
    population=[]
    for j in range(N):
        ej=s.eye(N)[:,j]*s.sqrt(N)
        population.extend([delta*sig+ej,delta*sig-ej])
    mean=sum(population,s.zeros(N,1))/(2*N)
    cov=sum(((e-mean)*(e-mean).T for e in population),s.zeros(N,N))/(2*N)
    mean_bias=sum((h.T*e)[0] for e in population)/(2*N)
    centered_bias=sum((h.T*(e-mean))[0] for e in population)/(2*N)
    ok('nonzero_mean_with_identity_covariance',cov==s.eye(N) and mean==delta*sig)
    ok('unit_response_contrast_bias_not_zero',mean_bias==delta and delta!=0)
    ok('known_mean_subtraction_removes_bias',centered_bias==0)
    # Joint uncertainty must use true-family count coefficients, not nominal.
    vnom=s.Matrix([1,0,0]);vtrue=s.Matrix([2,0,0])
    dqtrue=s.Matrix([1,0,0]);noise=s.Matrix([-1,0,0]);dqobs=dqtrue+noise
    operator_on_observed=abs(((vnom-vtrue).T*dqobs)[0])
    actual_error=abs((vnom.T*dqobs-vtrue.T*dqtrue)[0])
    nominal_count_bound=abs((vnom.T*noise)[0])
    uniform_count_bound=2
    ok('nominal_joint_bound_counterexample',actual_error==2 and operator_on_observed+nominal_count_bound==1)
    ok('uniform_true_family_joint_bound',actual_error<=operator_on_observed+uniform_count_bound)
    # Exact affine row family, bounded parameters, observed data plus uniform noise.
    b0=[sum((hr[i]*W0[i,:] for i in range(k,n+1)),s.zeros(1,3)) for k in range(1,n+1)]
    b1=[sum((hr[i]*W1[i,:] for i in range(k,n+1)),s.zeros(1,3)) for k in range(1,n+1)]
    limit=s.Rational(1,4)
    for trial in range(25):
        lam=s.Rational(rng.randint(-25,25),100)
        WL=W0+lam*W1
        er=[s.Matrix([s.Rational(rng.randint(-5,5),100) for _ in range(3)]) for _ in range(n)]
        ep=[s.zeros(3,1)]
        for v in er: ep.append(ep[-1]+v)
        observed=[c[i]+ep[i] for i in range(n+1)]
        est=sum(hr[i]*(W0[i,:]*observed[i])[0] for i in range(n+1))
        target=sum(hr[i]*(WL[i,:]*c[i])[0] for i in range(n+1))
        opbound=sum(abs(hr[i])*sum(limit*abs(W1[i,j])*abs(observed[i][j]) for j in range(3)) for i in range(n+1))
        countbound=sum((abs(b0[k][j])+limit*abs(b1[k][j]))*abs(er[k][j]) for k in range(n) for j in range(3))
        ok('affine_joint_operator_count_bound',abs(est-target)<=opbound+countbound)
    return {'check_families':dict(counts),'total_pass':sum(counts.values()),'total_fail':0,
            'synthetic_three_link_family':{'endpoints':len(ts),'W_rank':W.rank(),'joint_nuisance_rank':K.rank(),'available_contrast_dimension':len(ts)-K.rank(),'theta_true':str(theta),'theta_recovered':str(recovered),'contrast':[str(x) for x in h],'noise_box_bound':str(box),'correlated_variance':str(actual_variance)},
            'robust_affine_family':{'uncertainty_basis_rank':Z.rank(),'contrast_dimension':len(ts)-Z.rank(),'cases':robust_cases},
            'scope':'Exact rational synthetic tests of an explicitly supplied linear phase model. No actual plasma-free Cassini observable, physical covariance, scalar action/state/scale or empirical test is supplied.'}
