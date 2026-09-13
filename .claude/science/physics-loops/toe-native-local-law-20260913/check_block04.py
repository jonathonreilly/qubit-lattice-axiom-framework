"""Finite falsification checks for BLOCK04's previously written proofs.

No optimization scan is treated as a quantified diamond norm proof. Exact
Choi algebra and a separately built symmetric-qubit apparatus challenge the
load-bearing formulas; seeded numerical inputs test unanticipated directions.
"""
from pathlib import Path
import hashlib
import json
import math
import time
import numpy as np
import sympy as s

HERE = Path(__file__).resolve().parent
I = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
Z = s.diag(1, -1)


def vec(a):
    # output tensor input, so explicit row-major convention
    return s.Matrix([a[i, j] for i in range(a.rows) for j in range(a.cols)])


def choi(ks):
    return sum((vec(k)*vec(k).H for k in ks), s.zeros(4))


def ptr_output(a):
    return s.Matrix(2, 2, lambda j, k: sum(a[2*i+j, 2*i+k] for i in range(2)))


def run():
    start = time.monotonic()
    checks = []

    def check(name, ok, **detail):
        assert bool(ok), name
        checks.append(dict(name=name, **detail))

    def eq(name, lhs, rhs):
        d = lhs-rhs
        entries = list(d) if isinstance(d, s.MatrixBase) else [d]
        check(name, all(s.simplify(x) == 0 for x in entries))

    r = s.symbols('r', real=True, positive=True)
    pn = [(I+Z)/2, (I-Z)/2]
    m = (2*r*X+(1-r*r)*Z)/(1+r*r)
    pm = [(I+m)/2, (I-m)/2]
    kappa = 1/(1+r*r)
    dblocks = []
    for a in range(2):
        eq('sharp_projector_'+str(a), pm[a]*pm[a], pm[a])
        eq('Choi_overlap_'+str(a), (vec(pn[a]).H*vec(pm[a]))[0], kappa)
        d = choi([pn[a]])-choi([pm[a]])
        dblocks.append(d)
        eq('Choi_cubic_'+str(a), d**3, (1-kappa*kappa)*d)
    eq('Choi_absolute_partial_trace_squared',
       sum((ptr_output(d*d) for d in dblocks), s.zeros(2)),
       2*(1-kappa*kappa)*I)
    # Non-real projectors challenge the input transpose convention.
    pu = [(I+Y)/2, (I-Y)/2]
    pv = [(I+(2*X+3*Y+6*Z)/7)/2, (I-(2*X+3*Y+6*Z)/7)/2]
    kap = s.Rational(5, 7)
    ds = [choi([pu[a]])-choi([pv[a]]) for a in range(2)]
    eq('complex_axes_partial_trace', sum((ptr_output(d*d) for d in ds), s.zeros(2)),
       2*(1-kap*kap)*I)
    # Actual antipodal Choi witness, with eigenvalues evaluated separately.
    antipodal = [choi([pn[a]])-choi([pn[1-a]]) for a in range(2)]
    eq('antipodal_entangled_trace_norm',
       sum(sum(abs(e)*mult for e,mult in d.eigenvals().items()) for d in antipodal)/2, 2)

    alpha = s.symbols('alpha', positive=True)
    u = s.symbols('u', real=True)
    beta = s.sqrt(alpha*(1-alpha))
    # Polynomial expressions use beta^2, avoiding an unstated conjugate rule.
    b2 = alpha*(1-alpha)
    jplus = s.Matrix([[0,0,0,alpha],[0,b2,0,0],[0,0,0,0],[alpha,0,0,alpha**2]])
    jminus = s.diag(0,b2,0,alpha**2-2*alpha)
    eq('spin_channel_trace_preserving_difference', ptr_output(jplus+jminus), s.zeros(2))
    eq('ellipse_discriminant', (4-3*alpha)**2+4-alpha**2,
       4*(5-6*alpha+2*alpha**2))
    f = (4-3*alpha)*u+s.sqrt(4*u-(4-alpha**2)*u**2)
    eq('ellipse_endpoint_derivative', s.diff(f,u).subs(u,1), -2*(alpha-1)**2/alpha)
    eq('ellipse_second_derivative', s.diff(f,u,2),
       -4/(4*u-(4-alpha**2)*u**2)**s.Rational(3,2))

    samples = []
    for k in (1,2,3,6,15):
        a = s.Rational(1,k+1)
        b = s.sqrt(a*(1-a))
        kp = [s.diag(1,a),s.Matrix([[0,b],[0,0]])]
        km = [s.diag(0,1-a),s.Matrix([[0,-b],[0,0]])]
        eq('Kraus_completeness_'+str(k),sum((v.H*v for v in kp+km),s.zeros(2)),I)
        eq('plus_effect_'+str(k),sum((v.H*v for v in kp),s.zeros(2)),s.diag(1,a))
        eq('plus_Choi_formula_'+str(k),choi(kp)-choi([pn[0]]),jplus.subs(alpha,a))
        eq('minus_Choi_formula_'+str(k),choi(km)-choi([pn[1]]),jminus.subs(alpha,a))
        B = 4-a*a
        C = 4-3*a
        us = 2*(1+C/s.sqrt(C*C+B))/B
        exact = 2*a*(C+s.sqrt(C*C+B))/B
        check('optimizer_inside_'+str(k),0 < float(us) < 1)
        eq('ellipse_optimizer_value_'+str(k),a*f.subs({alpha:a,u:us}),exact)
        af = float(a)
        vals = [af*((4-3*af)*x+math.sqrt(max(0,4*x-(4-af*af)*x*x)))
                for x in np.linspace(0,1,501)]
        check('finite_grid_below_proved_max_'+str(k),max(vals)<=float(exact)+1e-13)
        check('reference_improves_over_down_input_'+str(k),float(exact)>float(4*a-2*a*a))
        samples.append({'k':k,'diamond':float(exact),'down_input':float(4*a-2*a*a),
                        'outcome_L1':float(2*a),'program_max_infidelity':float(2*a*(1-a)),
                        'optimal_down_weight':float(us)})

    # Independent apparatus: symmetrize one down spin among k+1 actual qubits.
    # Only its two input columns are needed. Qubit ordering is data then program.
    for k in (1,2,3,6):
        n = 2**k
        vp = s.zeros(2*n,2)
        inp = s.zeros(2*n,2)
        inp[0,0] = 1
        inp[n,1] = 1
        vp[0,0] = 1
        for bit in range(k+1):
            vp[1<<bit,1] = s.Rational(1,k+1)
        vm = inp-vp
        eq('literal_joint_completeness_'+str(k),vp.H*vp+vm.H*vm,I)
        eq('literal_joint_outcome_orthogonality_'+str(k),vp.H*vm,s.zeros(2))
        ksp = [s.Matrix(2,2,lambda i,j:vp[i*n+p,j]) for p in range(n)]
        ksm = [s.Matrix(2,2,lambda i,j:vm[i*n+p,j]) for p in range(n)]
        a = s.Rational(1,k+1)
        eq('literal_symmetric_plus_Choi_'+str(k),choi(ksp)-choi([pn[0]]),jplus.subs(alpha,a))
        eq('literal_symmetric_minus_Choi_'+str(k),choi(ksm)-choi([pn[1]]),jminus.subs(alpha,a))
        return_prob = sum(abs(v[i*n,1])**2 for v in (vp,vm) for i in range(2))
        eq('literal_program_disturbance_'+str(k),1-return_prob,2*a*(1-a))

    rng = np.random.default_rng(20260913)
    paulis = [np.array(p,dtype=complex) for p in(X,Y,Z)]

    def projectors(axis):
        h = sum((x*p for x,p in zip(axis,paulis)),np.zeros((2,2),complex))
        return [(np.eye(2)+h)/2,(np.eye(2)-h)/2]

    def cqout(kraus,psi):
        rho = np.outer(psi,psi.conj())
        return [sum((np.kron(v,np.eye(2))@rho@np.kron(v.conj().T,np.eye(2))
                     for v in ks),np.zeros((4,4),complex)) for ks in kraus]

    def tnorm(a):
        return np.linalg.svd(a,compute_uv=False).sum()

    max_angle_resid = 0.0
    max_spin_resid = 0.0
    for index in range(60):
        n,m = rng.normal(size=(2,3))
        n /= np.linalg.norm(n)
        m /= np.linalg.norm(m)
        p,q = projectors(n),projectors(m)
        bound = 2*math.sqrt(max(0,1-((1+n@m)/2)**2))
        psi = rng.normal(size=4)+1j*rng.normal(size=4)
        psi /= np.linalg.norm(psi)
        outputs = cqout([[p[0]],[p[1]]],psi),cqout([[q[0]],[q[1]]],psi)
        val = sum(tnorm(x-y) for x,y in zip(*outputs))
        max_angle_resid = max(max_angle_resid,val-bound)
        check('arbitrary_axis_reference_input_'+str(index),val<=bound+1e-12)
        bell = np.array([1,0,0,1])/math.sqrt(2)
        outputs = cqout([[p[0]],[p[1]]],bell),cqout([[q[0]],[q[1]]],bell)
        check('arbitrary_axis_lower_witness_'+str(index),
              abs(sum(tnorm(x-y) for x,y in zip(*outputs))-bound)<1e-12)
        k = (1,2,3,6,15)[index%5]
        a = 1/(k+1)
        b = math.sqrt(a*(1-a))
        # Same n=z model but genuinely arbitrary complex entangled input.
        ops = [[np.diag([1,a]),np.array([[0,b],[0,0]])],
               [np.diag([0,1-a]),np.array([[0,-b],[0,0]])]]
        outputs = cqout(ops,psi),cqout([[np.diag([1,0])],[np.diag([0,1])]],psi)
        val = sum(tnorm(x-y) for x,y in zip(*outputs))
        bound = 2*a*(4-3*a+2*math.sqrt(5-6*a+2*a*a))/(4-a*a)
        max_spin_resid = max(max_spin_resid,val-bound)
        check('spin_arbitrary_reference_input_'+str(index),val<=bound+1e-12)
        if index < 5:
            B,C = 4-a*a,4-3*a
            us = 2*(1+C/math.sqrt(C*C+B))/B
            witness = np.array([math.sqrt(1-us),0,0,math.sqrt(us)])
            outputs = cqout(ops,witness),cqout([[np.diag([1,0])],[np.diag([0,1])]],witness)
            value = sum(tnorm(x-y) for x,y in zip(*outputs))
            check('spin_reference_attains_bound_'+str(k),abs(value-bound)<1e-12)

    # Geometry of deterministic sharp banks, not a general processor lower bound.
    for eps in (s.Rational(1,10),s.Rational(1,2),s.S.One):
        cap = 1-s.sqrt(1-eps*eps/4)
        costheta = 1-2*cap
        eq('cap_boundary_exact_'+str(eps),4*(1-((1+costheta)/2)**2),eps**2)
        delta_cos_half = s.sqrt(1-eps*eps/8)
        eq('net_error_squared_'+str(eps),4*(1-delta_cos_half**4),
           eps**2-eps**4/16)
    eq('six_qubit_bank_bound',2*s.sqrt(2*s.Rational(1,64)-s.Rational(1,64)**2),s.sqrt(127)/32)
    result = {'status':'PASS','checks':len(checks),'details':checks,
              'samples':samples,'elapsed_seconds':time.monotonic()-start,
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'limitations':'Finite author checks; quantified diamond and permanence proofs are in BLOCK04_DERIVATION.md; no independent review or axiom no-go.'}
    (HERE/'BLOCK04_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='details'},indent=2))


if __name__ == '__main__':
    run()
