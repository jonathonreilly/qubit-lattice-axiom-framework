#!/usr/bin/env python3
"""Restricted coherent-chirp model controls, not a Cassini physical fit."""
import collections
import sympy as s

AUDIT_TIMEOUT_SEC = 120


def run():
    checks=collections.Counter()
    def ok(name,value):
        assert bool(value),name
        checks[name]+=1
    a,b,c,d,e,X,K=s.symbols('a b c d e X K',nonzero=True)
    A=s.Matrix([[1,a,b],[1,a,c],[1,d,e]])
    w=A.T.inv()*s.Matrix([1,0,0]); chirp=s.Matrix([X,X,K])
    B=s.Matrix.hstack(chirp,s.diag(1/X,1/X,1/K)*A[:,1:])
    denominator=(w.T*s.Matrix([X**2,X**2,K**2]))[0]
    v=s.diag(X,X,K)*w/denominator
    ok('symbolic_inverse_row',all(s.factor(x)==0 for x in B.T*v-s.Matrix([1,0,0])))
    ok('symbolic_determinant',s.factor(B.det()-A.det()*denominator/(X**2*K))==0)
    ok('diversity_denominator',s.factor(denominator-(a*K**2-d*X**2)/(a-d))==0)
    # Exact rational synthetic carriers; source ratios, illustrative frequencies.
    fx=s.Rational(36,5);fk=s.Rational(34)
    ratios=[s.Rational(880,749),s.Rational(3344,749),s.Rational(14,15)]
    ref=[fx,fx,fk]
    A0=s.Matrix([[1,1/ref[i]**2,1/(ratios[i]*ref[i])**2] for i in range(3)])
    w0=A0.T.inv()*s.Matrix([1,0,0])
    ts=list(map(s.Rational,range(9))); t=s.symbols('t',real=True)
    scaleX=1+t/1000+t*t/100000
    scaleK=1+t/700+t*t/80000
    primitiveX=t+t*t/2000+t**3/300000
    primitiveK=t+t*t/1400+t**3/240000
    ok('uplink_phase_derivative_X',s.diff(primitiveX,t)==scaleX)
    ok('uplink_phase_derivative_K',s.diff(primitiveK,t)==scaleK)
    rows=[]; ops=[]; denominators=[]; scales=[]
    for ti in ts:
        xx=scaleX.subs(t,ti);kk=scaleK.subs(t,ti)
        ss=s.Matrix([xx,xx,kk])
        D=sum(w0[j]*ss[j]**2 for j in range(3))
        BB=s.Matrix.hstack(ss,s.diag(1/xx,1/xx,1/kk)*A0[:,1:])
        vv=s.Matrix([w0[j]*ss[j]/D for j in range(3)])
        ok('exact_rational_inverse',BB.T*vv==s.Matrix([1,0,0]))
        ok('finite_positive_conditioning_domain',D>0 and xx>0 and kk>0)
        rows.append(vv.T);ops.append(BB);denominators.append(D);scales.append(ss)
    W=s.Matrix.vstack(*rows)
    ok('two_independent_chirps_rank_two',W.rank()==2)
    commonW=s.Matrix.vstack(*[(w0/scaleX.subs(t,ti)).T for ti in ts])
    ok('common_chirp_rank_one',commonW.rank()==1)
    alpha=s.Matrix([scales[i][0]/denominators[i] for i in range(len(ts))])
    beta=s.Matrix([scales[i][2]/denominators[i] for i in range(len(ts))])
    components=alpha*s.Matrix([[w0[0],w0[1],0]])+beta*s.Matrix([[0,0,w0[2]]])
    ok('architecture_factorization',W==components)
    # The inverse loses uplink diversity exactly when actual frequencies coincide.
    xx=s.Rational(6,5);kk=fx*xx/fk
    ss=s.Matrix([xx,xx,kk])
    singular=s.Matrix.hstack(ss,s.diag(1/xx,1/xx,1/kk)*A0[:,1:])
    ok('actual_uplink_frequency_collision',singular.det()==0)
    # Exact emitted phase rather than a midpoint-frequency substitute.
    signature=s.Matrix([(ti/8)**4 for ti in ts]);H=s.Matrix([[1,ti] for ti in ts])
    theta=s.Rational(3,700000);G=theta*signature+H*s.Matrix([s.Rational(1,100000),s.Rational(1,1000000)])
    Q=[]; E=[]; Ebounds=[]
    for i,ti in enumerate(ts):
        U=100+ti**3;Dcol=200+2*ti*ti
        zi=s.Matrix([G[i],U,Dcol]);linear=ops[i]*zi
        exact=[];bounds=[]
        for j in range(3):
            primitive=primitiveX if j<2 else primitiveK
            phase_geom=primitive.subs(t,ti+G[i])-primitive.subs(t,ti)
            # Direct carrier cycles: k*F_ref*phase_geom, divided by k*F_ref.
            carrier_geom=ratios[j]*ref[j]*phase_geom/(ratios[j]*ref[j])
            plasma_cycles=ratios[j]*U/(ref[j]*scales[i][j])+Dcol/(ratios[j]*ref[j]*scales[i][j])
            normalized_plasma=plasma_cycles/(ratios[j]*ref[j])
            exact.append(carrier_geom+normalized_plasma)
            maxabs=max(abs(ti),abs(ti+G[i]))
            slopebound=(s.Rational(1,1000)+2*maxabs/100000) if j<2 else (s.Rational(1,700)+2*maxabs/80000)
            bounds.append(slopebound*G[i]**2/2)
        qq=s.Matrix(exact);ee=qq-linear
        ok('quadratic_emission_phase_remainder',all(abs(ee[j])<=bounds[j] for j in range(3)))
        Q.append(qq);E.append(ee);Ebounds.append(bounds)
    # Construct a signal contrast after eliminating initial phases and chosen H.
    nuisance=W.row_join(H);cols=nuisance.columnspace();C=s.Matrix.hstack(*cols)
    P=s.eye(len(ts))-C*(C.T*C).inv()*C.T
    ok('chirped_signal_survives_declared_nuisance',(signature.T*P*signature)[0]>0)
    h=P*signature/(signature.T*P*signature)[0]
    ok('initial_phase_and_clock_basis_eliminated',h.T*nuisance==s.zeros(1,nuisance.cols))
    increments=[Q[i]-Q[i-1] for i in range(1,len(ts))]
    cumulative=[s.zeros(3,1)]
    for inc in increments:cumulative.append(cumulative[-1]+inc)
    r=s.Matrix([(rows[i]*cumulative[i])[0] for i in range(len(ts))])
    estimated=(h.T*r)[0]
    exact_error=sum(h[i]*(rows[i]*E[i])[0] for i in range(len(ts)))
    bound=sum(abs(h[i])*sum(abs(rows[i][j])*Ebounds[i][j] for j in range(3)) for i in range(len(ts)))
    ok('nonlinear_count_error_exact',estimated-theta==exact_error)
    ok('nonlinear_emission_error_bounded',abs(estimated-theta)<=bound)
    # Deliberately omit common frequency normalization: it must fail.
    badrows=s.Matrix.vstack(*[(w0/denominators[i]).T for i in range(len(ts))])
    ok('missing_chirp_numerator_detected',any(badrows[i,:]*ops[i]!=s.Matrix([[1,0,0]]) for i in range(1,len(ts))))
    return {'families':dict(checks),'total_pass':sum(checks.values()),'total_fail':0,
            'synthetic_model':{'endpoint_count':len(ts),'phase_initial_row_rank':W.rank(),'joint_nuisance_rank':nuisance.rank(),'remaining_contrasts':len(ts)-nuisance.rank(),'true_theta':str(theta),'actual_error_approx':float(estimated-theta),'bound_approx':float(bound),'exact_error':str(estimated-theta),'exact_bound':str(bound)},
            'scope':'Common nominal emission and separable frequency-scaled rays are premises. Nonlinear emission phase tested exactly in a synthetic chirp; plasma ray/time cross terms and real calibration errors are not supplied. No empirical scalar test.'}
