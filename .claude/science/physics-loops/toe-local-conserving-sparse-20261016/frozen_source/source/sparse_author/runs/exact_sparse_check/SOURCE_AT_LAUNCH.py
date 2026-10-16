"""One bounded exact discriminator for the proposed sparse compiler.

No parent checker code is imported. Matrix identities are computed directly
in computational bases. Symbolic equalities here cover only the named small
instances; the general count is an analytic proposition.
"""
import itertools
import json
import platform
import sys

import sympy as s

I = s.I
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -I], [I, 0]])
Z = s.diag(1, -1)
S = s.diag(1, I)
R = (s.kronecker_product(X, X) + s.kronecker_product(Y, Y)) / 2


def clean(a):
    return a.applyfunc(s.simplify)


def zero(a):
    return all(s.simplify(x) == 0 for x in a)


def frob2(a):
    return s.simplify(sum(s.conjugate(x) * x for x in a))


def embed(u, sites, n):
    out = s.zeros(2**n)
    for col in range(2**n):
        bits = [(col >> (n - 1 - j)) & 1 for j in range(n)]
        small_col = sum(bits[j] << (len(sites) - 1 - k) for k, j in enumerate(sites))
        for small_row in range(2 ** len(sites)):
            val = u[small_row, small_col]
            if val == 0:
                continue
            target = bits[:]
            for k, j in enumerate(sites):
                target[j] = (small_row >> (len(sites) - 1 - k)) & 1
            row = sum(b << (n - 1 - j) for j, b in enumerate(target))
            out[row, col] += val
    return out


def xy(theta):
    return s.Matrix([[1, 0, 0, 0],
                     [0, s.cos(theta), I*s.sin(theta), 0],
                     [0, I*s.sin(theta), s.cos(theta), 0],
                     [0, 0, 0, 1]])


def special(u):
    out = s.eye(4)
    out[1:3, 1:3] = u
    return out


def controlled(u, pattern, n):
    out = s.eye(2**n)
    for suffix in range(2**(n-len(pattern))):
        bits = [b for _, b in pattern] + [
            (suffix >> (n-len(pattern)-1-j)) & 1
            for j in range(n-len(pattern))]
        # This helper deliberately only uses leading controls, as in the
        # four-qubit recurrence check below.
        if [j for j, _ in pattern] != list(range(len(pattern))):
            raise ValueError('leading controls required')
    offset = sum(b << (n-1-j) for j, b in pattern)
    dim = 2**(n-len(pattern))
    out[offset:offset+dim, offset:offset+dim] = u
    return out


checks = {}
evidence = {}
A = xy(s.pi/4)
S1 = embed(S, [0], 2)
D = (embed(Z, [0], 2)-embed(Z, [1], 2))/2
checks['variable_xy_generator_conjugation'] = zero(S1.H*A*D*A.H*S1-R)
checks['forward_sqrt_order_eight'] = zero(A**8-s.eye(4))
checks['forward_sqrt_inverse_seven'] = zero(A**7-A.H)

i12, i13, i23 = [embed(xy(s.pi/2), pair, 3) for pair in [(0,1),(0,2),(1,2)]]
F = i13*i23.H*i12
S3 = embed(S, [2], 3)
R23 = embed(R, [1,2], 3)
Z1 = embed(Z, [0], 3)
conjugated = clean(F.H*S3.H*R23*S3*F)
checks['paper_F_unitarity'] = zero(F.H*F-s.eye(8))
checks['paper_control_generator_all_angles'] = zero(conjugated-Z1*R23)
mutant = clean(F.H*S3*R23*S3.H*F-Z1*R23)
evidence['wrong_S_adjoint_mutant_frobenius_squared'] = str(frob2(mutant))
checks['wrong_S_adjoint_mutant_detected'] = not zero(mutant)

theta = s.pi/3
for b in [0,1]:
    circuit = embed(xy(theta/2), [1,2], 3)*F.H*S3.H*embed(xy((-1)**b*theta/2),[1,2],3)*S3*F
    expected = s.diag(1-b,b)
    target = s.kronecker_product(expected,xy(theta))+s.kronecker_product(s.eye(2)-expected,s.eye(4))
    checks[f'controlled_xy_bit_{b}'] = zero(circuit-target)

# A non-real SU(2) commutator, then the actual four-qubit split-control identity.
U = (s.eye(2)+I*(2*X+2*Y+4*Z))/5
AA = s.sqrt(15)*s.eye(2)/5+I*(X+Y+2*Z)/s.sqrt(15)
BB = I*(X-Y)/s.sqrt(2)
checks['complex_SU2_commutator'] = zero(AA*BB*AA.H*BB.H-U)
Ae = embed(special(AA), [2,3], 4)
Be = embed(special(BB), [2,3], 4)
P = embed(s.diag(0,1), [0], 4)
Q = embed(s.diag(1,0), [1], 4)
CA = P*Ae+(s.eye(16)-P)
CB = Q*Be+(s.eye(16)-Q)
split = clean(CA*CB*CA.H*CB.H)
target = P*Q*embed(special(U),[2,3],4)+(s.eye(16)-P*Q)
checks['split_control_pattern_10'] = zero(split-target)
evidence['omitted_inverse_mutant_frobenius_squared'] = str(frob2(CA*CB*CA*CB.H-target))
checks['omitted_inverse_mutant_detected'] = not zero(CA*CB*CA*CB.H-target)

# Determinant-one Givens elimination, including its unavoidable complex phases.
d=4
V=s.Matrix([[I**(j*k)/2 for k in range(d)] for j in range(d)])
work=V.copy(); factors=[]
for col in range(d-1):
    for row in range(d-1,col,-1):
        a,b=work[col,col],work[row,col]
        norm2=s.simplify(s.conjugate(a)*a+s.conjugate(b)*b)
        if norm2 == 0:
            g=s.eye(2)
        else:
            radius=s.sqrt(norm2)
            g=s.Matrix([[s.conjugate(a),s.conjugate(b)],[-b,a]])/radius
        T=s.eye(d)
        T[col,col],T[col,row],T[row,col],T[row,row]=g[0,0],g[0,1],g[1,0],g[1,1]
        factors.append(T)
        work=clean(T*work)
checks['six_givens_determinant_one'] = all(s.simplify(g.det()-1)==0 for g in factors)
checks['one_residual_phase'] = zero(work-s.diag(1,1,1,s.simplify(V.det())))
recovered=work
for g in reversed(factors): recovered=clean(g.H*recovered)
checks['givens_reconstructs_complex_target'] = zero(recovered-V)
evidence['Givens_count_d4'] = len(factors)
evidence['residual_phase'] = str(s.simplify(V.det()))

# Shared ancilla-one partner: two distinct phase corrections must still return A=0.
phases=[(0b100,I),(0b010,(1+I*s.sqrt(3))/2)]
joint=s.eye(16)
for b,z in phases:
    positions=[j for j in range(3) if (b>>(2-j))&1]
    clear=b & ~(1<<(2-positions[0]))
    phase=s.eye(16)
    phase[2*b,2*b]=z
    phase[2*clear+1,2*clear+1]=s.conjugate(z)
    joint=phase*joint
J=s.zeros(16,8)
for b in range(8):J[2*b,b]=1
desired=s.eye(8)
for b,z in phases:desired[b,b]=z
checks['shared_phase_partner_clean_ancilla'] = zero(joint*J-J*desired)
Nt=s.diag(*[bin(i).count('1') for i in range(16)])
checks['phase_pairs_conserve_total_number'] = zero(joint*Nt-Nt*joint)

# Exact integer enumeration of the selected, not V-minimal, prefix-code support.
q,L=2,1;M=L+2*q;sectors={}
for a in range(q,M+1):
    sectors[a]=[]
    for old in itertools.product([0,1],repeat=q):
        count=a-sum(old)
        sectors[a].append(old+(1,)*count+(0,)*(M-count))
all_states=[b for states in sectors.values() for b in states]
max_hd=max(sum(x!=y for x,y in zip(b,c)) for states in sectors.values() for b in states for c in states)
checks['prefix_support_count'] = len(all_states)==len(set(all_states))==(L+q+1)*2**q
checks['prefix_equal_weight_and_distance'] = all(sum(b)==a for a,states in sectors.items() for b in states) and max_hd<=2*q
evidence['prefix_case']={'q':q,'L':L,'M':M,'selected_basis_count':len(all_states),'sectors':len(sectors),'maximum_pair_hamming_distance':max_hd}

report={'python':sys.version,'sympy':s.__version__,'platform':platform.platform(),
        'checks':checks,'computed_evidence':evidence,
        'scope':'Exact small matrix/finite enumeration discriminator; not a proof of the general compiler, runtime, preparation or physical permissions.'}
print(json.dumps(report,indent=2,sort_keys=True))
sys.exit(0 if all(checks.values()) else 2)
