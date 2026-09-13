"""Small exact countercheck of the analytical native-leaf derivation.

No prior runner is imported. Native operators use bit actions (LSB-first).
The second calculation uses classical occupation transitions from two-state
CAR rotations. This is a same-agent alternative calculation, not peer review.
"""
from pathlib import Path
import itertools
import json
import hashlib
import sympy as sp

OUT = Path(__file__).resolve().parent
I = sp.I
Q = sp.Rational
EDGES = ((0, 1), (0, 2), (1, 3), (0, 4))
VERTICES = ((0, 0, 0), (1, 0, 0), (0, 1, 0),
            (1, 1, 0), (0, 0, 1))
N = 1 << len(EDGES)
ID = sp.eye(N)
checks = {}


def eq(a, b):
    if isinstance(a, sp.MatrixBase) or isinstance(b, sp.MatrixBase):
        return all(sp.simplify(x) == 0 for x in a - b)
    return sp.simplify(a - b) == 0


def check(name, condition):
    checks[name] = bool(condition)
    if not condition:
        raise AssertionError(name)


def bit(word, edge):
    return (word >> edge) & 1


Z = [sp.diag(*[(-1) ** bit(x, e) for x in range(N)])
     for e in range(len(EDGES))]
B = []
for vertex in range(len(VERTICES)):
    B.append(sp.diag(*[
        (-1) ** sum(bit(x, e) for e, pair in enumerate(EDGES)
                    if vertex in pair)
        for x in range(N)]))
NUMBER = [(ID - b) / 2 for b in B]
T = []
for edge, (u, v) in enumerate(EDGES):
    mask = []
    for root, opposite in ((u, v), (v, u)):
        for f, pair in enumerate(EDGES):
            if f != edge and root in pair:
                other = pair[1] if pair[0] == root else pair[0]
                if other < opposite:
                    mask.append(f)
    A = sp.zeros(N)
    for x in range(N):
        sign = (-1) ** sum(bit(x, f) for f in mask)
        A[x ^ (1 << edge), x] = sign
    t = I * A * (B[u] - B[v]) / 2
    check(f"native_hopping_{edge}_Hermitian", eq(t, t.H))
    check(f"native_hopping_{edge}_cubic", eq(t ** 3, t))
    T.append(t)

P = (ID - NUMBER[2]) * NUMBER[3]
RHO = P / sp.trace(P)
check("ready_rank_four", eq(sp.trace(P), 4))


def pulse(t, cosine, sine):
    return ID + (cosine - 1) * t * t - I * sine * t


def projector(edge, outcome):
    return (ID + (-1) ** outcome * Z[edge]) / 2


def native_law(r0, s0, r1, s1, ct, st):
    U0 = pulse(T[1], r0, s0)
    U1 = pulse(T[2], r1, s1)
    D = pulse(T[0], ct, st)
    for tag, op in (("first", U0), ("second", U1), ("dwell", D)):
        check(f"unitary_{tag}_{r0}_{r1}_{ct}", eq(op.H * op, ID))
    check(f"old_Record_survives_dwell_{ct}", eq(D * Z[1], Z[1] * D))
    check(f"old_Record_survives_second_{r1}", eq(U1 * Z[1], Z[1] * U1))
    check(f"original_matter_number_dwell_{ct}",
          eq(D * (NUMBER[0] + NUMBER[1]),
             (NUMBER[0] + NUMBER[1]) * D))
    law, means = {}, {}
    for a in (0, 1):
        rho_a = projector(1, a) * U0 * RHO * U0.H * projector(1, a)
        mass = sp.simplify(sp.trace(rho_a))
        if mass != 0:
            means[a] = sp.simplify(sp.trace(NUMBER[0] * rho_a) / mass)
        for b in (0, 1):
            K = projector(2, b) * U1 * D
            rho_ab = K * rho_a * K.H
            law[a, b] = sp.simplify(sp.trace(rho_ab))
            check(f"permanent_{r0}_{r1}_{ct}_{a}{b}",
                  eq(projector(1, a) * rho_ab, rho_ab))
    check(f"law_normalized_{r0}_{r1}_{ct}", eq(sum(law.values()), 1))
    return law, means


def occupation_law(r0, r1, ct, st):
    """Separate occupation-route calculation; no native matrices or word masks."""
    result = dict.fromkeys(itertools.product((0, 1), repeat=2), sp.Integer(0))
    for n0, n1 in itertools.product((0, 1), repeat=2):
        first = [(0, n0, 1 if n0 == 0 else r0 ** 2)]
        if n0 == 1:
            first.append((1, 0, 1 - r0 ** 2))
        for a, after0, weight0 in first:
            if after0 == n1:
                hops = [(n1, 1)]
            else:
                hops = [(n1, ct ** 2), (after0, st ** 2)]
            for after1, hop_weight in hops:
                # Filled second leaf: no vacancy for transfer when n1=1.
                p_same = r1 ** 2 + (1 - r1 ** 2) * after1
                result[a, 1] += weight0 * hop_weight * p_same / 4
                result[a, 0] += weight0 * hop_weight * (1 - p_same) / 4
    return {key: sp.simplify(value) for key, value in result.items()}


fixtures = [
    (Q(3, 5), Q(4, 5), Q(3, 5), Q(4, 5), 1, 0),
    (Q(3, 5), Q(4, 5), Q(3, 5), Q(4, 5), sp.sqrt(2)/2, sp.sqrt(2)/2),
    (Q(3, 5), Q(4, 5), Q(5, 13), Q(12, 13), Q(3, 5), Q(4, 5)),
    (0, 1, Q(3, 5), Q(4, 5), 0, 1),
    (Q(3, 5), Q(4, 5), 1, 0, 0, 1),
    (1, 0, Q(3, 5), Q(4, 5), Q(3, 5), Q(4, 5)),
]
evidence = []
for fixture in fixtures:
    r0, s0, r1, s1, ct, st = map(sp.sympify, fixture)
    law, means = native_law(r0, s0, r1, s1, ct, st)
    other = occupation_law(r0, r1, ct, st)
    check(f"native_vs_occupation_{r0}_{r1}_{ct}",
          all(eq(law[k], other[k]) for k in law))
    conditional = {}
    for a in (0, 1):
        mass = sum(law[a, b] for b in (0, 1))
        if mass != 0:
            conditional[a] = sp.simplify(law[a, 1] / mass)
            pi0 = r0 ** 2 / (1 + r0 ** 2) if a == 0 else 0
            expected = r1 ** 2 + (1-r1 ** 2)*(ct ** 2/2+st ** 2*pi0)
            check(f"conditional_formula_{r0}_{r1}_{ct}_{a}",
                  eq(conditional[a], expected))
    if len(conditional) == 2:
        delta = sp.simplify(conditional[0] - conditional[1])
        expected_delta = (1-r1 ** 2)*st ** 2*r0 ** 2/(1+r0 ** 2)
        check(f"delta_formula_{r0}_{r1}_{ct}", eq(delta, expected_delta))
    else:
        delta = "undefined: one prefix has zero probability"
    if st == 0:
        p0 = (1+r0 ** 2)/2
        p1 = (1+r1 ** 2)/2
        expected = {(0,0):p0*(1-p1), (0,1):p0*p1,
                    (1,0):(1-p0)*(1-p1), (1,1):(1-p0)*p1}
        check("original_all_outcome_product", all(eq(law[k], expected[k]) for k in law))
    evidence.append({
        "r0": str(r0), "r1": str(r1), "dwell_cosine": str(ct),
        "joint_law": {str(k):str(v) for k,v in law.items()},
        "conditional_second_one": {str(k):str(v) for k,v in conditional.items()},
        "difference": str(delta),
        "post_first_matter_occupation": {str(k):str(v) for k,v in means.items()},
    })

# The all-mode characterization is analytic; this verifies its polynomial core.
r = sp.symbols("r", real=True)
M0 = sp.Matrix([[1,r*r],[0,1-r*r]])
M1 = sp.Matrix([[1-r*r,0],[r*r,1]])
check("both_channel_determinants", eq(M0.det(),1-r*r) and eq(M1.det(),1-r*r))
check("r1_information_boundary", M0.subs(r,1).rank() == M1.subs(r,1).rank() == 1)

# Literal physical geometry; unrecorded carrier qubits are not readable Records.
centers = [tuple(VERTICES[u][k]+VERTICES[v][k] for k in range(3))
           for u,v in EDGES]
x0, x1 = centers[1], centers[2]
program0, program1, bridge = (0,2,0), (2,2,0), (1,1,0)


def distance(a,b):
    return sum(abs(u-v) for u,v in zip(a,b))


def shell(x, records):
    return {y:value for y,value in records.items() if distance(x,y) == 1}


check("native_target_separation_two", distance(x0,x1) == 2)
check("bare_first_shell_empty", not shell(x0,{}))
check("bare_second_shell_empty_after_both_histories",
      not shell(x1,{x0:0}) and not shell(x1,{x0:1}))
check("same_program_shell_before_bridge",
      shell(x1,{program0:"C0",program1:"C1",x0:0}) ==
      shell(x1,{program0:"C0",program1:"C1",x0:1}))
check("bridge_is_one_local_step_each_side",
      distance(bridge,x0) == distance(bridge,x1) == 1)
check("bridge_sees_only_first_result",
      shell(bridge,{program0:"C0",program1:"C1",x0:0}) == {x0:0})

I2 = sp.eye(2)
P0, P1 = sp.diag(1,0), sp.diag(0,1)
Had = sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)


def decode_attenuation(C):
    h, k = (C+C.H)/2, (C-C.H)/(2*I)
    eigenvalues = sorted(h.eigenvals(), key=lambda x:float(x))
    w = eigenvalues[0]
    project = h-w*I2
    attenuation = sp.trace(k)/2-1
    return project, w, attenuation


for project in (P0,P1):
    for w in (0,Q(1,2),1):
        for attenuation in (0,Q(3,5),1):
            C=project+w*I2+I*(1+attenuation)*I2
            p,w2,r2=decode_attenuation(C)
            check(f"program_decode_{project[0,0]}_{w}_{attenuation}",
                  eq(p,project) and eq(w2,w) and eq(r2,attenuation))
            p2,_,_=decode_attenuation(Had*C*Had.H)
            check(f"program_covariance_{project[0,0]}_{w}_{attenuation}",
                  eq(p2,Had*project*Had.H))

case=evidence[1]
alphas=[sp.sympify(case["conditional_second_one"][str(a)]) for a in (0,1)]
A=alphas[0]*P0+alphas[1]*P1
C=A+I*(2*I2+P1)
A2=(C+C.H)/2
output=(C-C.H)/(2*I)-2*I2
check("effect_table_program_decode", eq(A2,A) and eq(output,P1))
for a, data in enumerate((P0,P1)):
    check(f"bridge_matches_actual_quantum_conditional_{a}",
          eq(sp.trace(A2*data),alphas[a]))
    check(f"table_covariance_{a}",
          eq(sp.trace((Had*A2*Had.H)*(Had*data*Had.H)),alphas[a]))

# These controls challenge actual derivation choices, not a requested PASS value.
check("wrong_pre_event_failure_mean_rejected",
      not eq(alphas[1], Q(9,25)+Q(16,25)*(Q(1,4)+Q(1,2))))
check("dropping_bridge_outcome_rejected", not eq(alphas[0],alphas[1]))
check("bare_ready_polarity_alias", not eq(Q(1,2)*(1-Q(9,25)),Q(1,2)*(1+Q(9,25))))

result={
    "claim_status":"conditional author derivation checked on stated finite fixtures",
    "independence":"same-agent native bit-action and occupation-transition routes",
    "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "source_pr8036":"6067254e3bca867aa6e737f7aa2bb6078e5d622d",
    "physical_centers":centers,
    "fixtures":evidence,
    "checks":checks,
    "TOTAL":{"PASS":sum(checks.values()),"FAIL":sum(not v for v in checks.values())},
    "limits":"No physical occurrence, program genesis, control selection, infinite renewal or independent review is proved.",
}
(OUT/"BLOCK01_CHECKS.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({key:value for key,value in result.items() if key!="checks"},indent=2))
