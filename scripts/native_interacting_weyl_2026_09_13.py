"""Finite exact challenges of the analytical interacting native construction.

The RG theorem, infinite-volume LR proof, and all-clock growth statement
are not proved by this runner. See the paired note for their premises.
"""
from pathlib import Path
from itertools import product, permutations
from collections import deque
import hashlib, json, time
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = (
    "docs/NATIVE_INTERACTING_WEYL_PROTECTED_PATHS_BOUNDED_THEOREM_NOTE_2026-09-13.md",
    "docs/NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
AXES = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
I2 = s.eye(2)
X = s.Matrix([[0, 1], [1, 0]])
Y = s.Matrix([[0, -s.I], [s.I, 0]])
Z = s.diag(1, -1)


def add(v, w):
    return tuple(a+b for a, b in zip(v, w))


def candidate(v, w):
    d = tuple(b-a for a, b in zip(v, w))
    if sum(abs(a) for a in d) != 1:
        return False
    axis = next(j for j, a in enumerate(d) if a)
    tail = v if d[axis] == 1 else w
    return axis == 1 and (tail[0]+tail[1]) % 2 == 1


def vertex(n, r):
    return (2*n[0]+r, n[1], n[2])


def route(v, w, x_bounds=None):
    """Construct the stated length<=3 route, independently of Pauli algebra."""
    dx, dy, dz = (b-a for a, b in zip(v, w))
    if dy == dz == 0:
        sign = 1 if dx > 0 else -1
        return [(v[0]+j*sign, v[1], v[2]) for j in range(abs(dx)+1)]
    if dx == dy == 0 or (dx == dz == 0 and not candidate(v, w)):
        return [v, w]
    if dx == dz == 0:
        detour = AXES[0]
        if x_bounds is not None and v[0]+1>x_bounds[1]:
            detour = (-1,0,0)
        return [v, add(v, detour), add(w, detour), w]
    assert abs(dx) == abs(dy) == 1 and dz == 0, (v, w)
    xfirst = (w[0], v[1], v[2])
    if not candidate(xfirst, w):
        return [v, xfirst, w]
    return [v, (v[0], w[1], v[2]), w]


def car(n):
    D = 1 << n
    return [s.SparseMatrix(D, D, {
        (b ^ (1 << j), b): (-1)**((b & ((1 << j)-1)).bit_count())
        for b in range(D) if b & (1 << j)}) for j in range(n)]


def native_graph(edges):
    D = 1 << len(edges)
    ident = s.eye(D)
    def diagonal(mask):
        return s.diag(*[(-1)**((b & mask).bit_count()) for b in range(D)])
    ze = {e: diagonal(1 << j) for j, e in enumerate(edges)}
    bv = {v: diagonal(sum(1 << j for j, e in enumerate(edges) if v in e))
          for v in set(sum((list(e) for e in edges), []))}
    avw = {}
    for j, (v, w) in enumerate(edges):
        mask = 0
        for endpoint, other in ((v, w), (w, v)):
            for k, e in enumerate(edges):
                if endpoint in e:
                    neighbor = e[1] if e[0] == endpoint else e[0]
                    if neighbor < other:
                        mask ^= 1 << k
        mat = s.SparseMatrix(D, D, {
            (b ^ (1 << j), b): (-1)**((b & mask).bit_count())
            for b in range(D)})
        avw[v, w] = mat
        avw[w, v] = -mat
    def path(vs):
        out = ident
        for v, w in zip(vs, vs[1:]):
            out = out*avw[v, w]
        return s.I**(len(vs)-2)*out
    return ident, ze, bv, avw, path


def run_model():
    start = time.monotonic()
    checks = []
    def check(name, truth, **detail):
        assert bool(truth), name
        checks.append({'name': name, **detail})
    def eq(name, a, b):
        d = a-b
        vals = d if isinstance(d, s.MatrixBase) else [d]
        check(name, all(s.simplify(x) == 0 for x in vals))

    # Reconstruct the symbol from independently enumerated oriented terms.
    zz = s.symbols('z1 z2 z3', nonzero=True)
    zeta, nu, lam = s.symbols('zeta nu lambda', real=True)
    W = [(-Z+s.I*X)/2, (-Z+s.I*Y)/2, -Z/2]
    target = ((zz[0]-1/zz[0])/(2*s.I)*X
              +(zz[1]-1/zz[1])/(2*s.I)*Y
              +(2+zeta-nu-sum((v+1/v)/2 for v in zz))*Z)
    assembled = (2+zeta-nu)*Z
    for a in range(3):
        assembled += W[a]/zz[a]+W[a].H*zz[a]
    eq('complete_Laurent_Wilson_symbol', assembled, target)
    k = s.symbols('k1 k2 k3', real=True)
    h = s.sin(k[0])*X+s.sin(k[1])*Y+(2+zeta-sum(s.cos(t) for t in k))*Z
    eq('source_inversion_symmetry', Z*h.subs(dict(zip(k, [-v for v in k])))*Z, h)
    eq('source_z_reflection', h.subs(k[2], -k[2]), h)
    eq('source_particle_hole_reflection', -X*h.subs(k[0], -k[0])*X, h)
    check('simple_time_reversal_is_broken',
          h.subs({k[0]:s.pi/2, k[1]:0, k[2]:0}) !=
          s.conjugate(h.subs({k[0]:-s.pi/2, k[1]:0, k[2]:0})))
    for sign in (-1, 1):
        point = {k[0]:0, k[1]:0, k[2]:sign*s.acos(zeta)}
        eq('exact_node_'+str(sign), h.subs(point), s.zeros(2))
        eq('node_z_velocity_'+str(sign), h.diff(k[2]).subs(point),
           sign*s.sqrt(1-zeta*zeta)*Z)
        eq('nonzero_quadratic_source_coefficient_'+str(sign),
           h.diff(k[2], 2).subs(point), zeta*Z)
    check('zeta_zero_violates_chosen_quadratic_hypothesis',
          h.diff(k[2], 2).subs({zeta:0,k[2]:s.pi/2}) == s.zeros(2))
    for a, w in enumerate(W):
        eig = (w.H*w).eigenvals()
        expected = {s.Integer(1):1, s.Integer(0):1} if a < 2 else {s.Rational(1,4):2}
        check('bond_squared_singular_values_'+str(a), eig == expected)
    npaths = 0
    for n in product(range(-2, 3), repeat=3):
        for a, w in enumerate(W):
            for direction in (-1, 1):
                m = add(n, tuple(direction*t for t in AXES[a]))
                coeff = w if direction == 1 else w.H
                for r, q in product(range(2), repeat=2):
                    if coeff[r, q] == 0:
                        continue
                    v, u = vertex(n, r), vertex(m, q)
                    p = route(v, u)
                    assert p[0] == v and p[-1] == u and len(set(p)) == len(p)
                    assert 1 <= len(p)-1 <= 3, p
                    assert all(sum(abs(x-y) for x,y in zip(b,c)) == 1
                               and not candidate(b,c) for b,c in zip(p,p[1:])), p
                    stars = set()
                    for b in p:
                        for ax in AXES:
                            for sign in (-1,1):
                                stars.add(add(tuple(2*t for t in b),tuple(sign*t for t in ax)))
                    assert len(stars) <= 5*(len(p)-1)+6
                    assert max(sum(abs(a-b) for a,b in zip(site,tuple(2*t for t in v)))
                               for site in stars) <= 7
                    npaths += 1
    check('every_nonzero_Wilson_hop_has_protected_bounded_path', True,
          routed_terms=npaths, cells=125)
    finite_paths = 0
    for shape in ((1,2,2),(2,3,1),(3,2,2)):
        cells = set(product(*(range(a) for a in shape)))
        bounds = (2*shape[0],shape[1],shape[2])
        for n in cells:
            for a,w in enumerate(W):
                m = add(n,AXES[a])
                if m not in cells:
                    continue
                for r,q in product(range(2),repeat=2):
                    if w[r,q] == 0:
                        continue
                    p = route(vertex(n,r),vertex(m,q),(0,bounds[0]-1))
                    assert all(all(0<=x<bound for x,bound in zip(v,bounds)) for v in p)
                    assert all(not candidate(v,u) for v,u in zip(p,p[1:]))
                    assert len(p)<=4
                    finite_paths += 1
    check('open_box_routes_need_no_extra_bulk_fermions',True,routed_terms=finite_paths)

    # Literal four-vertex square: candidate (1,3), protected detour 1,0,2,3.
    edges = [(0,1),(0,2),(1,3),(2,3)]
    ident, ze, bv, avw, path = native_graph(edges)
    cycle = avw[0,1]*avw[1,3]*avw[3,2]*avw[2,0]
    P = (ident+cycle)/2
    eq('native_cycle_projector', P*P, P)
    eq('native_code_dimension', s.trace(P), 8)
    vacproj = P
    for b in bv.values():
        vacproj = vacproj*(ident+b)/2
    eq('native_vacuum_rank_one', s.trace(vacproj), 1)
    col = next(vacproj[:,j] for j in range(16) if vacproj[:,j] != s.zeros(16,1))
    nvac = col/s.sqrt((col.H*col)[0])
    c = car(4)
    g = [a+a.H for a in c]
    cfB = [s.eye(16)-2*a.H*a for a in c]
    fvac = s.eye(16)[:,0]
    rootpaths = {1:[0,1],2:[0,2],3:[0,2,3]}
    even = [i for i in range(16) if i.bit_count()%2 == 0]
    V = s.zeros(16,8)
    for j, bits in enumerate(even):
        nf, ff = nvac, fvac
        for v in range(1,4):
            if bits & (1<<v):
                nf = path(rootpaths[v])*nf
                ff = (-s.I*g[0]*g[v])*ff
        assert sum(int(x != 0) for x in ff) == 1 and ff[bits] != 0
        V[:,j] = nf/ff[bits]
    eq('native_CAR_isometry', V.H*V, s.eye(8))
    eq('native_CAR_full_code_range', V*V.H, P)
    for v in range(4):
        eq('native_CAR_number_'+str(v), bv[v]*V, V*cfB[v].extract(even,even))
    pairs = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    routes = [[0,1],[0,2],[0,2,3],[1,0,2],[1,0,2,3],[2,3]]
    hnative, hcar = s.zeros(16), s.zeros(16)
    for j, ((v,w), p) in enumerate(zip(pairs,routes)):
        ap = path(p)
        eq('path_involution_'+str(p), ap*ap, ident)
        eq('path_hermitian_'+str(p), ap.H, ap)
        eq('path_native_CAR_'+str(p), ap*V, V*(-s.I*g[v]*g[w]).extract(even,even))
        T = s.I*ap*(bv[v]-bv[w])/2
        J = -ap*(ident-bv[v]*bv[w])/2
        TF = c[v].H*c[w]+c[w].H*c[v]
        JF = s.I*(c[v].H*c[w]-c[w].H*c[v])
        eq('real_hopping_sign_'+str(p), T*V, V*TF.extract(even,even))
        eq('imaginary_hopping_sign_'+str(p), J*V, V*JF.extract(even,even))
        hnative += (j+1)*T+(2-j)*J
        hcar += (j+1)*TF+(2-j)*JF
    hn_density = bv[0]*bv[1]/4
    hf_density = (c[0].H*c[0]-s.eye(16)/2)*(c[1].H*c[1]-s.eye(16)/2)
    eq('quartic_density_interaction_dictionary', hn_density*V, V*hf_density.extract(even,even))
    check('quartic_is_not_even_sector_constant',
          len(hf_density.extract(even,even).eigenvals()) == 2)
    hnative += lam*hn_density-nu*(bv[1]-bv[0])/2
    hcar += lam*hf_density-nu*(c[0].H*c[0]-c[1].H*c[1])
    eq('full_complex_interacting_native_CAR_H', hnative*V, V*hcar.extract(even,even))
    eq('interaction_preserves_candidate_Record', hnative*ze[1,3], ze[1,3]*hnative)
    eq('interaction_preserves_cycle', hnative*cycle, cycle*hnative)
    u, v = s.symbols('u v', real=True)
    pulse = u*ident+v*ze[1,3]*cycle
    eq('pulse_unitarity_polynomial', pulse.H*pulse, (u*u+v*v)*ident)
    eq('interaction_preserves_pulse', hnative*pulse, pulse*hnative)
    for outcome in (-1,1):
        q = (ident+outcome*ze[1,3])/2
        branch = q*pulse*V
        eq('scalar_branch_full_reference_identity_'+str(outcome),
           branch.H*branch, (u+outcome*v)**2*s.eye(8)/2)
        eq('scalar_branch_interacting_intertwiner_'+str(outcome),
           hnative*branch, branch*hcar.extract(even,even))
        eq('branch_Record_locked_'+str(outcome), ze[1,3]*branch, outcome*branch)
    for bias in (-4,-2,0,2,4):
        q = s.Rational(bias,8)
        cosine = s.sqrt((1+s.sqrt(1-q*q))/2)
        sine = q/(2*cosine)
        eq('actual_four_neighbor_pulse_normalized_'+str(bias), cosine**2+sine**2, 1)
        eq('actual_four_neighbor_pulse_bias_'+str(bias), 2*cosine*sine, q)
        for outcome in (-1,1):
            eq('actual_kernel_branch_probability_'+str((bias,outcome)),
               (cosine+outcome*sine)**2/2, (1+outcome*q)/2)

    # Compute the bond Fock norms, not merely the coefficient norms.
    for j, w in enumerate(W):
        bond = s.zeros(16)
        for r, q in product(range(2),repeat=2):
            term = w[r,q]*c[r].H*c[2+q]
            bond += term+term.H
        eig = bond.eigenvals()
        check('actual_bond_Fock_norm_'+str(j), max(abs(e) for e in eig) == 1,
              eigenvalues={str(k):m for k,m in eig.items()})

    return {'status':'pass','checks':checks,'total_pass':len(checks),'total_fail':0,
            'seconds':time.monotonic()-start,
            'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}



def run_boundary():
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
    check('initial_seed_Records_supported_before_any_new_event',
          all(kernel_p(seed)[0]>0 for seed in records))
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
            'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}



if __name__ == '__main__':
    result = {'model':run_model(), 'boundary':run_boundary()}
    receipt = ROOT/'outputs/native_interacting_weyl_2026_09_13.json'
    receipt.parent.mkdir(parents=True, exist_ok=True)
    receipt.write_text(json.dumps(result,indent=2)+'\n')
    for family, data in result.items():
        for row in data['checks']:
            print('PASS '+family+': '+row['name'])
    print('per_element: Exact finite native Pauli and ordinary CAR matrices check operator phases, quartic terms and event intertwining.')
    print('per_site: Physical midpoint placement, finite protected routes and all actual recorded nearest neighbors are enumerated.')
    print('per_mode: The Wilson symbol and tangent coefficients are exact identities; the interacting RG theorem remains an external import.')
    print('per_block: Finite even-code and parity-extension fixtures check the full stated operator maps, not selected state means alone.')
    print('lattice_wide: Analytical path, support, propagation and probability arguments are in the note; the runner does not enumerate infinity.')
    print('TOTAL: PASS='+str(sum(d['total_pass'] for d in result.values()))+' FAIL=0')
