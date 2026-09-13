"""Exact finite challenges for parity, support and boundary interfaces.

The infinite-volume and probability bounds are analytical proofs in the
paired note. These finite checks cannot establish those quantified limits.
"""
from pathlib import Path
from itertools import product, permutations
from collections import deque
import hashlib, json, time
import sympy as s
from check_block03 import car, AXES, add, candidate, I2, X, Y, Z

HERE = Path(__file__).resolve().parent


def run():
    start = time.monotonic()
    checks = []
    def check(name, truth, **detail):
        assert bool(truth), name
        checks.append({'name':name, **detail})
    def eq(name,a,b):
        diff = a-b
        vals = diff if isinstance(diff,s.MatrixBase) else [diff]
        check(name, all(s.simplify(x) == 0 for x in vals))

    # A state with both parities and actual intra-parity coherences.
    ket = s.eye(16)
    even = (ket[:,0]+s.I*ket[:,3])/s.sqrt(2)
    odd = (ket[:,1]+ket[:,8])/s.sqrt(2)
    rho = s.Rational(2,5)*even*even.H+s.Rational(3,5)*odd*odd.H
    extension = s.zeros(32)
    for b,d in product(range(16),repeat=2):
        if (b.bit_count()-d.bit_count()) % 2 == 0:
            p = b.bit_count()%2
            extension[b+(p<<4),d+(p<<4)] = rho[b,d]
    totalparity = s.diag(*[(-1)**b.bit_count() for b in range(32)])
    eq('extended_state_total_parity_even',totalparity*extension,extension)
    marginal = s.Matrix(16,16,lambda b,d:sum(extension[b+(a<<4),d+(a<<4)] for a in(0,1)))
    eq('exact_bulk_marginal_both_parities_and_coherences',marginal,rho)
    eq('extended_state_normalized',s.trace(extension),1)
    check('extended_state_positive',all(x>=0 for x in extension.eigenvals()))
    c = car(5)
    g = c[4]+c[4].H
    b = [a*g for a in c[:4]]
    for i in range(4):
        eq('dressed_field_even_'+str(i),totalparity*b[i],b[i]*totalparity)
        for j in range(4):
            eq('dressed_CAR_'+str((i,j)),b[i]*b[j].H+b[j].H*b[i],s.eye(32) if i==j else s.zeros(32))
            eq('dressed_neutral_pair_'+str((i,j)),b[i]*b[j].H,c[i]*c[j].H)
        eq('dressed_field_square_zero_'+str(i),b[i]*b[i],s.zeros(32))
    h = c[0].H*c[3]+c[3].H*c[0]+s.I*(c[1].H*c[2]-c[2].H*c[1])
    h += s.Rational(2,7)*(c[0].H*c[0]-s.eye(32)/2)*(c[1].H*c[1]-s.eye(32)/2)
    eq('interacting_H_leaves_ancilla_idle',h*g,g*h)
    eq('dressed_correlator_time_derivative',
       (h*b[0]-b[0]*h)*b[3].H,(h*c[0]-c[0]*h)*c[3].H)

    # Literal growing prefix uses every recorded NN, including native sites.
    def neighbors(v):
        return [add(v,tuple(sign*t for t in a)) for a in AXES for sign in(-1,1)]
    def program(v):
        return sum(t%2 for t in v)>=2
    seeds = [(1,1,1),(2,1,1)]
    records = {seeds[0]:1,seeds[1]:1}
    prefix = []
    dist = {p:0 for p in seeds}
    queue = deque(seeds)
    while queue:
        v = queue.popleft()
        if dist[v] == 6:
            continue
        for w in neighbors(v):
            if program(w) and w not in dist:
                dist[w] = dist[v]+1
                queue.append(w)
    targets = sorted((p for p in dist if p not in records),key=lambda v:(dist[v],v))
    native = {}
    for v in product(range(-3,5),repeat=3):
        w = add(v,AXES[1])
        if candidate(v,w):
            center = add(tuple(2*t for t in v),AXES[1])
            transverse = [add(center,tuple(sign*t for t in AXES[a])) for a in(0,2) for sign in(-1,1)]
            native[center] = transverse
    support_visits = 0
    mixed_program_conditions = 0
    old_program_conditions_with_native = 0
    def kernel_p(v):
        values = [records[w] for w in neighbors(v) if w in records]
        assert values
        # Direct empirical-plus-complement atom count, preserving multiplicity.
        p = sum(s.Rational(3,4) if a==1 else s.Rational(1,4) for a in values)/len(values)
        assert p == s.Rational(1,2)+s.Rational(sum(values),4*len(values))
        return p, values
    def emit(v,kind):
        nonlocal support_visits,mixed_program_conditions,old_program_conditions_with_native
        p, values = kernel_p(v)
        assert s.Rational(1,4) <= p <= s.Rational(3,4)
        if kind=='program' and any(w in native and w in records for w in neighbors(v)):
            mixed_program_conditions += 1
        outcome = 1 if (len(prefix)+sum(v))%3 else -1
        records[v] = outcome
        prefix.append({'site':v,'kind':kind,'condition':values,'p_plus':str(p),'outcome':outcome})
        for old in records:
            oldp,_ = kernel_p(old)
            assert (oldp if records[old]==1 else 1-oldp)>0
            if program(old) and any(w in native and w in records for w in neighbors(old)):
                old_program_conditions_with_native += 1
            support_visits += 1
    for target in targets:
        assert any(w in records and program(w) for w in neighbors(target))
        emit(target,'program')
        for center,transverse in native.items():
            if center not in records and all(p in records for p in transverse):
                assert sum(w in records for w in neighbors(center)) == 4
                emit(center,'native')
    check('actual_two_seed_supported_growth_prefix',len(prefix)>100,
          events=len(prefix),support_visits=support_visits,
          native_events=sum(row['kind']=='native' for row in prefix),
          program_birth_conditions_with_native_Records=mixed_program_conditions,
          old_program_conditions_with_native_Records=old_program_conditions_with_native)
    check('candidate_waits_for_all_its_program_neighbors',mixed_program_conditions==0)
    check('old_program_support_rechecked_with_actual_native_neighbors',old_program_conditions_with_native>0)
    rotations = []
    for perm in permutations(range(3)):
        for signs in product((-1,1),repeat=3):
            mat = s.zeros(3)
            for i in range(3):
                mat[i,perm[i]] = signs[i]
            if mat.det() == 1:
                rotations.append((perm,signs))
    for perm,signs in rotations:
        transform = lambda v:tuple(signs[i]*v[perm[i]]+7 for i in range(3))
        transformed = {transform(v):a for v,a in records.items()}
        for v,a in records.items():
            oldvalues = sorted(records[w] for w in neighbors(v) if w in records)
            newvalues = sorted(transformed[w] for w in neighbors(transform(v)) if w in transformed)
            assert oldvalues == newvalues
    check('literal_NN_multisets_under_all_proper_rotations_and_translation',True,
          rotations=len(rotations),records=len(records))

    # Three cells at (0,0,0),(1,0,0),(1,1,0) challenge boundary distance two.
    c6 = car(6)
    ident = s.eye(64)
    onsite = s.zeros(64)
    for cell in range(3):
        n0,n1 = (c6[2*cell+r].H*c6[2*cell+r] for r in(0,1))
        onsite += s.Rational(51,22)*(n0-n1)+s.Rational(1,7)*(n0-ident/2)*(n1-ident/2)
    hopping = [(-Z+s.I*X)/2,(-Z+s.I*Y)/2]
    eq('straight_Wilson_hopping_is_nilpotent',hopping[0]**2,s.zeros(2))
    check('bent_Wilson_hopping_does_not_cancel',hopping[0]*hopping[1]!=s.zeros(2))
    bonds = []
    for cell in range(2):
        hbond = s.zeros(64)
        for r,q in product(range(2),repeat=2):
            term = hopping[cell][r,q]*c6[2*cell+r].H*c6[2*(cell+1)+q]
            hbond += term+term.H
        bonds.append(hbond)
    Hsmall = onsite+bonds[0]
    Hlarge = Hsmall+bonds[1]
    a = c6[0]
    eq('odd_field_disjoint_boundary_commutator',bonds[1]*a,a*bonds[1])
    small,large = a,a
    for order in range(3):
        if order<2:
            eq('boundary_distance_two_Taylor_order_'+str(order),small,large)
        else:
            check('boundary_difference_really_starts_at_distance_two',small!=large)
        small = s.I*(Hsmall*small-small*Hsmall)
        large = s.I*(Hlarge*large-large*Hlarge)
    density1 = c6[1].H*c6[1]-ident/2
    eq('actual_nonlinear_onsite_field_derivative',
       onsite*a-a*onsite,-s.Rational(51,22)*a-s.Rational(1,7)*a*density1)

    # Independently count intersecting nearest-neighbor bond chains in Z^3.
    def incident(v):
        return {tuple(sorted((v,w))) for w in neighbors(v)}
    chains = {edge:1 for edge in incident((0,0,0))}
    counts = []
    for length in range(1,7):
        count = sum(chains.values())
        assert count == 6*11**(length-1)
        assert count <= 2*12**length
        counts.append(count)
        nxt = {}
        for edge,multiplicity in chains.items():
            adjacent = incident(edge[0]) | incident(edge[1])
            assert len(adjacent)==11
            for other in adjacent:
                nxt[other] = nxt.get(other,0)+multiplicity
        chains = nxt
    check('intersecting_bond_chain_count_from_actual_graph',True,counts=counts)
    tau,E = s.symbols('tau E',positive=True)
    t = s.symbols('t')
    integrand = s.exp(-s.I*t*E)*tau/(s.pi*(t*t+tau*tau))
    eq('Poisson_positive_energy_contour_residue',
       -2*s.pi*s.I*s.residue(integrand,t,-s.I*tau),s.exp(-tau*E))
    gamma,beta = s.symbols('gamma beta',positive=True)
    wait = s.symbols('wait',nonnegative=True)
    eq('actual_clock_Laplace_transform',
       s.integrate(gamma*s.exp(-12*gamma*wait),(wait,0,s.oo)),s.Rational(1,12))
    return {'status':'pass','checks':checks,'total_pass':len(checks),'total_fail':0,
            'seconds':time.monotonic()-start,'prefix':prefix,
            'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'helper_sha256':hashlib.sha256((HERE/'check_block03.py').read_bytes()).hexdigest()}


if __name__=='__main__':
    out=run()
    (HERE/'BLOCK03_BOUNDARY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='prefix'},indent=2))
