#!/usr/bin/env python3
"""Synthetic cold-plasma and finite-count controls; no empirical theory test."""
import collections
import random

import mpmath as mp
import sympy as s

AUDIT_TIMEOUT_SEC = 120


def weights(a, b, c, d, e):
    if a == d or b == c:
        raise ValueError('singular carrier design')
    den = (a-d)*(b-c)
    return s.Matrix([(c*d-a*e)/den, (a*e-b*d)/den, a/(a-d)])


def design(a, b, c, d, e):
    return s.Matrix([[1,a,b], [1,a,c], [1,d,e]])


def run_checks():
    checks = collections.Counter()
    def ok(name, statement):
        assert bool(statement), name
        checks[name] += 1
    a,b,c,d,e = s.symbols('a b c d e', nonzero=True)
    A=design(a,b,c,d,e); w=weights(a,b,c,d,e)
    ok('symbolic_weights', all(s.factor(v)==0 for v in A.T*w-s.Matrix([1,0,0])))
    ok('determinant', s.factor(A.det()-(b-c)*(d-a))==0)
    ok('two_link_witness', A[:2,:]*s.Matrix([a,-1,0])==s.zeros(2,1))
    # Dispersion follows from the wave equation plus the fluid current.
    om,k,cl,ne,el,me,ep=s.symbols('omega k c n_e e m_e epsilon_0', positive=True)
    v=-s.I*el/(om*me)
    J=-ne*el*v
    # For exp(i(kz-omega t)), Maxwell gives k^2-omega^2/c^2-i omega J/(eps c^2)=0.
    wave=k*k-om*om/cl**2-s.I*om*J/(ep*cl**2)
    expected=(om*om-ne*el*el/(ep*me))/cl**2
    ok('maxwell_fluid_dispersion', s.simplify(s.solve(wave,k*k)[0]-expected)==0)
    x=s.symbols('x', nonnegative=True)
    f=1-s.sqrt(1-x)
    ok('plasma_remainder_second_derivative', s.simplify(s.diff(f,x,2)-1/(4*(1-x)**s.Rational(3,2)))==0)
    mp.mp.dps=70
    for eta in ['0.00001','0.01','0.25','0.75','0.99']:
        E=mp.mpf(eta)
        for j in range(1,31):
            X=E*j/30
            rem=1-mp.sqrt(1-X)-X/2
            upper=X*X/(8*(1-E)**mp.mpf('1.5'))
            ok('plasma_remainder_grid', 0<rem<=upper*(1+mp.mpf('1e-60')))
    rng=random.Random(20261014)
    t=s.symbols('t',real=True)
    for n in range(90):
        values=[s.Rational(rng.randint(1,20),rng.randint(2,21)) for _ in range(5)]
        aa,bb,cc,dd,ee=values
        if aa==dd or bb==cc: continue
        B=design(*values); q=weights(*values)
        ok('rational_inverse_weights', q==B.T.inv()*s.Matrix([1,0,0]))
        # Independently generated endpoint states include no smoothness assumption.
        z0=s.Matrix([rng.randint(-20,20) for _ in range(3)])
        z1=s.Matrix([rng.randint(-20,20) for _ in range(3)])
        T=s.Rational(rng.randint(1,11),rng.randint(1,9))
        measured=B*(z1-z0)/T
        ok('finite_count_endpoint_exactness', (q.T*measured)[0]==(z1[0]-z0[0])/T)
        noise=s.Matrix([s.Rational(rng.randint(-10,10),100) for _ in range(3)])
        error=(q.T*noise)[0]
        bound=sum(abs(q[i])*abs(noise[i]) for i in range(3))
        ok('deterministic_error_bound', abs(error)<=bound)
        R=s.Matrix(3,3,[rng.randint(-3,3) for _ in range(9)])
        C=R*R.T
        var=(q.T*C*q)[0]
        ok('correlated_covariance', var==sum((R.T*q)[i]**2 for i in range(3)) and var>=0)
        # Random symmetric matrix error would be unsafe without this PSD construction.
        change=s.Rational(1,1000+n)
        B1=B.copy();B1[2,1]+=change
        if B1.det()==0: continue
        q1=B1.T.inv()*s.Matrix([1,0,0])
        p0=B*z0; p1=B1*z1
        counts=(p1-p0)/T
        correction=((q1-q).T*p0)[0]/T
        recovered=(q1.T*counts)[0]+correction
        ok('changing_operator_exact_identity', s.simplify(recovered-(z1[0]-z0[0])/T)==0)
        coeff=q1.T*B-s.Matrix([[1,0,0]])
        ok('common_column_initial_G_cancels', coeff[0]==0)
        box=[s.Rational(5),s.Rational(7),s.Rational(9)]
        extremum=s.Matrix([s.sign(coeff[j])*box[j] for j in range(3)])
        supremum=sum(abs(coeff[j])*box[j] for j in range(3))/T
        ok('initial_box_bound_saturation', (coeff*extremum)[0]/T==supremum)
        # Exact polynomial integral tests for equal-duration shifted counts.
        delta=s.Rational(rng.randint(-10,10),20)
        aligned=[]; shifted=[]; limits=[]
        for _ in range(3):
            u,vv,ww=[s.Rational(rng.randint(-5,5)) for _ in range(3)]
            yy=u+vv*t+ww*t*t
            primitive=u*t+vv*t*t/2+ww*t*t*t/3
            aligned.append(primitive.subs(t,1)-primitive.subs(t,0))
            shifted.append(primitive.subs(t,1+delta)-primitive.subs(t,delta))
            limits.append((abs(vv)+3*abs(ww))*abs(delta))
        actual=abs((q.T*(s.Matrix(shifted)-s.Matrix(aligned)))[0])
        ok('aligned_interval_lipschitz_bound', actual<=sum(abs(q[i])*limits[i] for i in range(3)))
    A0=design(s.Rational(1),s.Rational(1),s.Rational(1,4),s.Rational(1,4),s.Rational(1,4))
    A1=design(s.Rational(1),s.Rational(1),s.Rational(1,4),s.Rational(1,5),s.Rational(1,4))
    z0=s.Matrix([0,1,0]); p=A0*z0; z1=A1.inv()*p
    ok('zero_count_changed_state_witness', z1[0]==s.Rational(1,16) and A1*z1-p==s.zeros(3,1))
    w0=A0.T.inv()*s.Matrix([1,0,0]); w1=A1.T.inv()*s.Matrix([1,0,0])
    correction=((w1-w0).T*p)[0]
    ok('witness_correction', correction==s.Rational(1,16))
    ok('omit_initial_state_is_detected', s.Rational(0)!=z1[0]-z0[0])
    # Distinguish raw phase counts from division by a time-varying carrier.
    phi0=s.Rational(7); phi1=phi0; f0=s.Rational(2); f1=s.Rational(3)
    delta_p=phi1/f1-phi0/f0
    reconstructed=(phi1-phi0)/f1+phi0*(1/f1-1/f0)
    ok('varying_normalization_identity', reconstructed==delta_p)
    ok('zero_raw_count_not_zero_normalized_change', phi1-phi0==0 and delta_p!=0)
    # A time-varying physical phase scale changes the first column too.
    S0=s.diag(2,3,4); S1=s.diag(3,4,7)
    C0=S0*A0; C1=S1*A1
    u0=C0.T.inv()*s.Matrix([1,0,0]); u1=C1.T.inv()*s.Matrix([1,0,0])
    zz0=s.Matrix([2,3,5]); zz1=s.Matrix([7,11,13])
    q0=C0*zz0; q1=C1*zz1
    ok('fixed_units_full_phase_operator', (u1.T*(q1-q0)+(u1-u0).T*q0)[0]==zz1[0]-zz0[0])
    ok('changing_first_column_keeps_initial_G', (u1.T*C0-s.Matrix([[1,0,0]]))[0]!=0)
    noise=s.Matrix([1,2,3])
    ok('constant_phase_error_survives_variable_weights', ((u1-u0).T*noise)[0]!=0)
    # Coefficient drift may preserve weights: scaling whole nuisance columns.
    A2=A0*s.diag(1,s.Rational(13,10),s.Rational(7,10))
    ok('nonconstant_design_same_weights', A2!=A0 and A2.T.inv()*s.Matrix([1,0,0])==w0)
    # A common clock drift is retained with exactly the same gain as G.
    common=s.Rational(7,10); plasma=s.Matrix([0,4,5])
    ok('common_nuisance_survives', (w0.T*(s.ones(3,1)*common+A0*plasma))[0]==common)
    for vals in [(1,2,3,1,4),(1,2,2,3,4)]:
        try: weights(*map(s.Rational,vals))
        except ValueError: checks['singular_design_rejected']+=1
        else: raise AssertionError('singular matrix accepted')
    # Frequencies here are illustrative; ratios are sourced instrument facts.
    xu=s.Rational(36,5); ku=s.Rational(34)
    xd=xu*s.Rational(880,749); kd1=xu*s.Rational(3344,749); kd2=ku*s.Rational(14,15)
    nominal=weights(1/xu**2,1/xd**2,1/kd1**2,1/ku**2,1/kd2**2)
    return {'counts_by_family':dict(checks),'total_pass':sum(checks.values()),'total_fail':0,
            'witness':{'A_start':str(A0),'A_end':str(A1),'z_start':str(z0),'z_end':str(z1),'counts':[0,0,0],'G_change':'1/16','initial_correction':'1/16'},
            'illustrative_constant_carriers_GHz':[str(v) for v in [xu,xd,kd1,ku,kd2]],
            'illustrative_weights':[{'exact':str(v),'approximate':float(v)} for v in nominal],
            'illustrative_error_amplification_l1':float(sum(abs(v) for v in nominal)),
            'carrier_role':'Nominal illustrative values; not measurements, calibration constants or actual Cassini ramp reconstruction.'}
