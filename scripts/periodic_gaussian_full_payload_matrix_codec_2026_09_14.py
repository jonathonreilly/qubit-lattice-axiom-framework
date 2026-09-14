#!/usr/bin/env python3
"""Finite checks of a supplied periodic Gaussian compiler and equivariant codecs.

All scientific definitions used by this primary runner are below. It reads
no repository scientific inputs. Finite checks challenge the accompanying
all-volume derivations; they are not independent audit or native law selection.
"""
AUDIT_TIMEOUT_SEC = 180


"""Personal finite checks of the chart and relay; periodic routing is separate."""
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.linalg import norm
import sympy as sp


EPS = .25
BASIS = np.array([np.eye(2), [[0, 1], [1, 0]], [[0, -1j], [1j, 0]],
                  [[1, 0], [0, -1]]], dtype=complex)/np.sqrt(2)
VECTOR = np.array([1, 2, 3])


def rotations():
    out = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            r = np.zeros((3, 3), dtype=int)
            r[np.arange(3), permutation] = signs
            if round(np.linalg.det(r)) == 1:
                out.append(r)
    assert len(out) == 24
    return out


def matrix(z):
    return np.einsum('a,aij->ij', z, BASIS)


def coefficients(m):
    return np.einsum('aij,ij->a', BASIS.conj(), m)


def action(r, m):
    z = coefficients(m)
    return matrix(np.r_[z[0], r@z[1:]])


def center(role, frame):
    return np.r_[8*role, frame@VECTOR].astype(complex)


def encode(role, frame, z):
    rotated = np.r_[z[0], frame@z[1:]]
    return matrix(center(role, frame)+EPS*rotated/np.sqrt(1+np.vdot(z,z).real))


def decode(m, group):
    c = coefficients(m)
    role = round(c[0].real/8)
    frames = [norm(c-center(role,r)) for r in group]
    index = int(np.argmin(frames))
    r = group[index]
    y = c-center(role,r)
    remaining = EPS**2-np.vdot(y,y).real
    assert remaining > 0, 'No finite radial inverse on/outside the chart boundary'
    rotated = y/np.sqrt(remaining)
    return role, r, np.r_[rotated[0], r.T@rotated[1:]]


def codec_checks():
    group = rotations()
    points = [r@VECTOR for r in group]
    separation_squared = min(int(np.dot(x-y,x-y)) for i,x in enumerate(points)
                             for y in points[i+1:])
    assert separation_squared == 6 and 2*EPS < np.sqrt(separation_squared)
    rng = np.random.default_rng(49260914)
    max_inverse = max_covariance = max_product = 0.
    cases = 0
    for role in (-2, 0, 3):
        for r in group:
            z = rng.normal(size=4)+1j*rng.normal(size=4)
            encoded = encode(role, r, z)
            decoded_role, decoded_r, decoded_z = decode(encoded, group)
            assert role == decoded_role and np.array_equal(r, decoded_r)
            max_inverse = max(max_inverse, norm(z-decoded_z))
            for s in group:
                max_covariance = max(max_covariance,
                    norm(action(s,encoded)-encode(role,s@r,z)))
                # Verify the ambient rotation is a genuine star-algebra map,
                # not just a permutation of codec labels.
                a = matrix(z)
                b = matrix(rng.normal(size=4)+1j*rng.normal(size=4))
                max_product = max(max_product,norm(action(s,a@b)-action(s,a)@action(s,b)),
                                  norm(action(s,a.conj().T)-action(s,a).conj().T))
                cases += 1
    assert max_inverse < 1e-10 and max_covariance < 1e-12 and max_product < 1e-12
    jacobians = []
    for scale in (.1, .5, 1.5):
        u = scale*rng.normal(size=8)
        z = u[:4]+1j*u[4:]
        role, r = 1, group[7]
        def output(v):
            m = encode(role, r, v[:4]+1j*v[4:]).reshape(-1)
            return np.r_[m.real,m.imag]
        step = 3e-5
        numeric = np.column_stack([(output(u+step*np.eye(8)[j])-
                                    output(u-step*np.eye(8)[j]))/(2*step)
                                   for j in range(8)])
        actual = abs(np.linalg.det(numeric))
        expected = EPS**8/(1+np.dot(u,u))**5
        relative = abs(actual/expected-1)
        assert relative < 3e-6
        singular = np.linalg.svd(numeric,compute_uv=False)
        radial = EPS/(1+np.dot(u,u))**1.5
        tangential = EPS/np.sqrt(1+np.dot(u,u))
        assert abs(singular[-1]/radial-1) < 3e-6
        assert max(abs(singular[:-1]/tangential-1)) < 3e-6
        jacobians.append(dict(norm_squared=float(np.dot(u,u)), determinant=actual,
                              analytic_determinant=expected, relative_error=relative))
    return dict(frame_orbit=24, role_frame_group_cases=cases,
                frame_min_separation_squared=separation_squared,
                inverse_error=max_inverse, covariance_error=max_covariance,
                algebra_automorphism_error=max_product, jacobians=jacobians)


def measure_checks():
    def density(r, wrong=False, condition=False):
        if r <= 0 or r >= EPS:
            return 0.
        d = EPS**2-r*r
        source_square = r*r/d
        log_jacobian = -8*np.log(EPS) if wrong else 2*np.log(EPS)-5*np.log(d)
        exponent = 7*np.log(r)-source_square+log_jacobian-np.log(3)
        if condition:
            exponent += 3*np.log1p(source_square)-2*np.log(EPS)
        return np.exp(exponent)
    mass = quad(density,0,EPS,epsabs=1e-11)[0]
    wrong = quad(lambda r:density(r,wrong=True),0,EPS,epsabs=1e-11)[0]
    condition = quad(lambda r:density(r,condition=True),0,EPS,epsabs=1e-9)[0]
    assert abs(mass-1) < 1e-10
    assert abs(wrong-1) > .5
    assert abs(condition-193/EPS**2) < 1e-6
    tails = []
    for distance in (.05,.02,.01):
        r = EPS-distance
        square = r*r/(EPS**2-r*r)
        predicted = np.exp(-square)*sum(square**j/float(sp.factorial(j)) for j in range(4))
        actual = quad(density,r,EPS,epsabs=1e-12)[0]
        assert abs(actual-predicted) < 1e-10
        tails.append(dict(boundary_distance=distance, mass=actual, gamma_tail=predicted))
    return dict(normalized_mass=mass, wrong_constant_jacobian_mass=wrong,
                mean_squared_inverse_differential=condition,
                boundary_layer_probabilities=tails,
                support_boundary='zero_probability_but_in_measure_support; no finite inverse')


def relay_checks():
    aa = sp.Rational(2,5)+sp.I*sp.Rational(3,7)
    original = sp.Matrix([[3,aa],[sp.conjugate(aa),2]])
    cases = []
    for hidden_count in range(1,10):
        h = hidden_count
        hidden = sp.diag(*([2]*(h-1)+[1]))
        for j in range(h-1):
            hidden[j,j+1]=hidden[j+1,j]=1
        inverse = hidden.inv()
        assert hidden.det()==1 and inverse[0,0]==1 and inverse[h-1,h-1]==h
        assert inverse[0,h-1]==(-1)**(h-1)
        cross = sp.zeros(2,h)
        cross[0,0]=1
        cross[1,h-1]=(-1)**h*sp.conjugate(aa)
        visible = sp.diag(3+1,2+h*abs(aa)**2)
        recovered = sp.simplify(visible-cross*inverse*cross.conjugate().T)
        assert recovered==original
        full = visible.row_join(cross).col_join(cross.conjugate().T.row_join(hidden))
        assert sp.simplify(full.det()-original.det())==0
        assert np.linalg.eigvalsh(np.array(full,dtype=complex)).min()>0
        wrong_hidden = hidden.copy()
        wrong_hidden[-1,-1]=2
        wrong = sp.simplify(visible-cross*wrong_hidden.inv()*cross.conjugate().T)
        assert wrong != original
        cases.append(dict(path_edges=h+1, hidden_determinant=str(hidden.det()),
                          recovered_precision=[[str(v) for v in recovered.row(j)] for j in range(2)],
                          full_determinant=str(full.det())))
    return dict(complex_edge=str(aa), cases=cases)



"""Exact tests of the optional Borel completion; it is not continuous."""
import json
from pathlib import Path
import sympy as s

CLOSED_EPS=s.Rational(1,4)


def ordinary(r):
    return s.simplify(CLOSED_EPS*r/s.sqrt(1+r*r))


def radius_encode(r):
    if r.is_Integer and r > 0:
        return CLOSED_EPS if r==1 else ordinary(r-1)
    return ordinary(r)


def radius_decode(t):
    if s.simplify(t-CLOSED_EPS)==0:
        return s.Integer(1)
    candidate=s.simplify(t/s.sqrt(CLOSED_EPS*CLOSED_EPS-t*t))
    if candidate.is_Integer and candidate > 0:
        return candidate+1
    return candidate




def closed_codec_checks():
    radii=[s.Integer(n) for n in range(12)]+[s.sqrt(2),s.Rational(7,3),s.Rational(1,100)]
    cases=[]
    for r in radii:
        image=radius_encode(r)
        back=radius_decode(image)
        assert s.simplify(back-r)==0
        assert 0 <= image <= CLOSED_EPS
        cases.append(dict(radius=str(r),image=str(image),inverse=str(back)))
    targets=[CLOSED_EPS,s.Integer(0),ordinary(s.Integer(1)),ordinary(s.Integer(4)),CLOSED_EPS/3]
    for t in targets:
        assert s.simplify(radius_encode(radius_decode(t))-t)==0
    # An eight-real-coordinate unit vector has all payload coordinates active.
    unit=s.Matrix(range(1,9))/s.sqrt(204)
    assert (unit.T*unit)[0]==1
    for r in radii[1:]:
        z=r*unit
        encoded=radius_encode(r)*unit
        decoded=radius_decode(s.sqrt((encoded.T*encoded)[0]))*unit
        assert s.simplify(decoded-z)==s.zeros(8,1)
    # Explicit discontinuity, rather than an implied smoothness inheritance.
    gap=s.simplify(CLOSED_EPS-ordinary(s.Integer(1)))
    assert gap>0
    result=dict(exact_radial_cases=cases,all_eight_coordinates=True,
                boundary_inverse_radius=str(radius_decode(CLOSED_EPS)),
                jump_at_radius_one=str(gap),
                measure_argument='maps differ only on countably many Lebesgue-null spheres',
                scope='Borel equivariant bijection to closed chart; not continuous or finite-precision stable')
    return result



"""Explicit periodic coordinates; geometry checks are separate from Gaussian algebra.

Author prototype. Input is a supplied grouped-payload periodic graph, not the
DK source and not an autonomous formation process. No retained claim status.
"""
from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import json
from math import isqrt
from pathlib import Path

import numpy as np



@dataclass(frozen=True)
class Edge:
    left: int
    left_slot: int
    right: int
    right_slot: int
    delta: tuple[int, int, int]


def add(x, y):
    return tuple(a+b for a,b in zip(x,y))


def walk(start, end, axis):
    current = list(start)
    sign = 1 if end[axis] > start[axis] else -1
    for _ in range(abs(end[axis]-start[axis])):
        current[axis] += sign
        yield tuple(current)


class Compiler:
    def __init__(self, payloads, edges):
        self.payloads = tuple(payloads)
        self.edges = tuple(edges)
        assert self.edges and all(1 <= n <= 4 for n in self.payloads)
        self.radius = max(max(map(abs,e.delta)) for e in edges)
        self.period = 2*self.radius+2
        self.colors = self.period**3
        self.columns = isqrt(self.colors*len(payloads))
        if self.columns*self.columns < self.colors*len(payloads):
            self.columns += 1
        self.z0 = 8
        self.side = max(20*self.columns+20,
                        self.z0+16+len(edges)*self.colors)+16
        self.period_side = self.period*self.side
        incidents = defaultdict(list)
        for i,e in enumerate(edges):
            assert 0 <= e.left_slot < payloads[e.left]
            assert 0 <= e.right_slot < payloads[e.right]
            assert e.left != e.right or e.delta != (0,0,0)
            incidents[e.left].append((i,0))
            incidents[e.right].append((i,1))
        assert max(map(len,incidents.values())) <= 8
        self.ports = {item:p for h in incidents for p,item in enumerate(incidents[h])}

    def color(self, n):
        return tuple(a % self.period for a in n)

    def color_id(self, n):
        c = self.color(n)
        return (c[0]*self.period+c[1])*self.period+c[2]

    def home(self, n, h):
        index = self.color_id(n)*len(self.payloads)+h
        offset = (10+20*(index % self.columns),
                  10+20*(index // self.columns), self.z0)
        return tuple(self.side*a+b for a,b in zip(n,offset))

    def escape(self, home, port):
        direction = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0))[port//2]
        level = -1 if port % 2 == 0 else 1
        distance = 4 if level == -1 else 6
        axis = 0 if direction[0] else 1
        first = add(home,direction)
        second = add(first,(0,0,level))
        pin = add(home,tuple(distance*x for x in direction))
        pin = add(pin,(0,0,level))
        return [first,second,*walk(second,pin,axis)]

    def route(self, n, e_index):
        e = self.edges[e_index]
        destination = add(n,e.delta)
        left, right = self.home(n,e.left),self.home(destination,e.right)
        left_arm = self.escape(left,self.ports[(e_index,0)])
        right_arm = self.escape(right,self.ports[(e_index,1)])
        # Put the horizontal plane above BOTH endpoints. This also permits
        # protected clusters whose terminal arms already include upward steps.
        plane = max(n[2],destination[2])*self.side+self.z0+8+e_index*self.colors+self.color_id(n)
        result = [left,*left_arm]
        result.extend(walk(result[-1],(result[-1][0],result[-1][1],plane),2))
        result.extend(walk(result[-1],(right_arm[-1][0],result[-1][1],plane),0))
        result.extend(walk(result[-1],(*right_arm[-1][:2],plane),1))
        result.extend(walk(result[-1],right_arm[-1],2))
        result.extend(reversed(right_arm[:-1]))
        result.append(right)
        assert len(result)-1 <= (3*self.radius+4)*self.side+16
        assert len(set(result)) == len(result), 'Lifted path self-intersection'
        assert all(sum(abs(a-b) for a,b in zip(x,y))==1 for x,y in zip(result,result[1:]))
        return result

    def quotient(self, site, cover):
        return tuple(a % (b*self.side) for a,b in zip(site,cover))

    def forbidden(self, site):
        return False

    def coordinates(self, cover, registry=None):
        assert all(n >= self.period and n % self.period == 0 for n in cover)
        homes = {}
        for n in product(*(range(l) for l in cover)):
            for h,load in enumerate(self.payloads):
                site = self.quotient(self.home(n,h),cover)
                assert site not in homes
                homes[site] = load
        occupancy = Counter(homes)
        local_roster = defaultdict(set)
        used_slots = set()
        sizes = []
        seam_edges = 0
        digest = sha256()
        route_vertices = 0
        for n in product(*(range(l) for l in cover)):
            for e_index,e in enumerate(self.edges):
                path = self.route(n,e_index)
                quotient = [self.quotient(v,cover) for v in path]
                assert len(set(quotient)) == len(quotient), 'Periodic self-alias'
                assert quotient[0] in homes and quotient[-1] in homes
                sizes.append(len(path)-1)
                assert quotient[-1] == self.quotient(self.home(add(n,e.delta),e.right),cover)
                for x,y in zip(quotient,quotient[1:]):
                    step = [min(abs(a-b),l*self.side-abs(a-b))
                            for a,b,l in zip(x,y,cover)]
                    assert sum(step)==1, 'Non-nearest quotient edge'
                    if sum(abs(a-b) for a,b in zip(x,y))!=1:
                        seam_edges += 1
                for j,site in enumerate(quotient[1:-1],1):
                    assert site not in homes, 'A route crosses a home'
                    assert not self.forbidden(site), 'A route crosses a protected blank'
                    occupancy[site] += 1
                    assert occupancy[site] <= 4, ('Payload overflow',site,occupancy[site])
                    key = (e_index,self.color(n),j)
                    local_site = tuple(a % self.period_side for a in site)
                    if registry is None:
                        assert key not in local_roster[local_site], 'Hidden-variable alias'
                        local_roster[local_site].add(key)
                    else:
                        assert key in registry[local_site], 'Larger cover changes local role map'
                        slot = registry[local_site].index(key)
                        assert 0 <= slot < 4
                        assert (site,slot) not in used_slots, 'Two variables share a physical payload slot'
                        used_slots.add((site,slot))
                    digest.update(repr((n,e_index,j,site)).encode())
                    route_vertices += 1
        if registry is None:
            registry = {site:sorted(keys) for site,keys in local_roster.items()}
        else:
            # Independently compare physical occupancy to periodic slot roster.
            for site,load in occupancy.items():
                if site not in homes:
                    assert load == len(registry[tuple(a % self.period_side for a in site)])
        return dict(cover=cover,coarse_cells=int(np.prod(cover)),
                    active_sites=len(occupancy),hidden_variables=route_vertices,
                    maximum_payload_load=max(occupancy.values()),
                    ordinary_maximum=max(load for site,load in occupancy.items() if site not in homes),
                    path_edges_min=min(sizes),path_edges_max=max(sizes),
                    wrap_steps=seam_edges,coordinate_sha256=digest.hexdigest()),registry


def covariance_checks(compiler):
    """Rotate the physical map and carrier algebra, with scalar payload labels fixed."""
    group = rotations()
    p = compiler.period
    worst = 0.
    vertices = 0
    rng = np.random.default_rng(448915)
    for n in ((0,0,0),(p-1,p-1,p-1),(-1,2,-3)):
        for e in range(len(compiler.edges)):
            base = np.array(compiler.route(n,e))
            for s in group:
                rotated_coarse = s@np.array(n)
                # The frame coordinates, not fixed ambient x/y colors, define
                # the co-rotated source condition and the finite role map.
                input_back = tuple(s.T@rotated_coarse)
                rotated = np.array(compiler.route(input_back,e))@s.T
                assert np.array_equal(rotated,base@s.T)
                assert np.all(np.sum(abs(np.diff(rotated,axis=0)),axis=1)==1)
                assert np.array_equal(rotated[0],s@compiler.home(n,compiler.edges[e].left))
                vertices += len(base)
                z = rng.normal(size=4)+1j*rng.normal(size=4)
                identity = np.eye(3,dtype=int)
                for role in (e, len(base)):
                    worst = max(worst,float(np.linalg.norm(
                        action(s,encode(role,identity,z))-encode(role,s,z))))
    assert worst < 1e-9
    return dict(rotations=24,rotated_vertices=vertices,carrier_error=worst,
                source_representation='decoded scalar labels fixed; frame and spatial graph co-rotate')


def whole_graph_energy_check(compiler):
    """Expand the whole routed action and independently evaluate its unit residual form."""
    p = compiler.period
    rng = np.random.default_rng(928451)
    cells = list(product(range(p),repeat=3))
    visible = {(n,h,s):complex(*rng.normal(size=2))
               for n in cells for h,count in enumerate(compiler.payloads) for s in range(count)}
    # On-site 5 and the displayed finite edge roster have a checked strict
    # Gershgorin margin. Internal home edges connect the four scalar species.
    coefficients = tuple(complex(.1*(i+1),.03*(-1)**i) for i in range(len(compiler.edges)))
    incident = defaultdict(float)
    source = 5*sum(abs(v)**2 for v in visible.values())
    for n in cells:
        for h,count in enumerate(compiler.payloads):
            for s in range(count-1):
                a_key,b_key=(n,h,s),(n,h,s+1)
                coefficient=1/7
                source += 2*(visible[a_key].conjugate()*coefficient*visible[b_key]).real
                incident[a_key] += coefficient
                incident[b_key] += coefficient
    on_site = source
    local_path = 0.
    squares = 0.
    all_hidden = 0
    largest_path_error = 0.
    for n in cells:
        for i,e in enumerate(compiler.edges):
            destination = tuple(t % p for t in add(n,e.delta))
            u_key,v_key = (n,e.left,e.left_slot),(destination,e.right,e.right_slot)
            u,v = visible[u_key],visible[v_key]
            a = coefficients[i]
            incident[u_key] += abs(a)
            incident[v_key] += abs(a)
            edge_energy = 2*(u.conjugate()*a*v).real
            source += edge_energy
            hidden_count = len(compiler.route(n,i))-2
            z = rng.normal(size=hidden_count)+1j*rng.normal(size=hidden_count)
            h = hidden_count
            diagonal = 2*np.vdot(z,z).real-abs(z[-1])**2
            neighbors = 2*np.vdot(z[:-1],z[1:]).real if h>1 else 0.
            ends = 2*(u.conjugate()*z[0]+z[-1].conjugate()*(-1)**h*a*v).real
            increment = abs(u)**2+h*abs(a*v)**2
            direct = diagonal+neighbors+ends+increment
            residuals = z+np.r_[u,z[:-1]]+(-1.)**np.arange(1,h+1)*a*v
            independent = float(np.vdot(residuals,residuals).real)+edge_energy
            largest_path_error = max(largest_path_error,abs(direct-independent))
            local_path += direct
            squares += float(np.vdot(residuals,residuals).real)
            all_hidden += h
    assert max(incident.values()) < 5
    compiled = on_site+local_path
    factorized = source+squares
    assert largest_path_error < 1e-8
    assert abs(compiled-factorized) < 1e-8*abs(factorized)
    assert source > 0 and squares > 0
    return dict(hidden_variables=all_hidden,compiled_action=compiled,
                visible_plus_unit_residual_action=factorized,
                relative_error=abs(compiled-factorized)/abs(factorized),
                maximum_path_error=largest_path_error,
                source_diagonal_dominance_margin=5-max(incident.values()),
                status='finite full routed action identity; Gaussian integral follows from proved unit triangular Jacobian')




def periodic_cases():
    edges = [Edge(0,i % 4,0,(i+1) % 4,d) for i,d in enumerate(
        ((1,0,0),(0,1,0),(0,0,1),(1,1,1)))]
    compiler = Compiler((4,),edges)
    p = compiler.period
    first,registry = compiler.coordinates((p,p,p))
    second,_ = compiler.coordinates((2*p,p,p),registry)
    assert second['active_sites']==2*first['active_sites']
    assert second['hidden_variables']==2*first['hidden_variables']
    assert first['wrap_steps'] > 0
    # Coordinate translation identity checked on full lifted paths, not counts.
    translated = 0
    for n in ((0,0,0),(p-1,p-1,p-1),(-1,2,-3)):
        for e in range(len(edges)):
            route = np.array(compiler.route(n,e))
            for a in range(3):
                shift = tuple(p if j==a else 0 for j in range(3))
                other = np.array(compiler.route(add(n,shift),e))
                assert np.array_equal(other,route+np.array(shift)*compiler.side)
                translated += len(route)
    result = dict(period=p,microcell_side=compiler.side,
                  edge_types=len(edges),home_types=1,external_endpoints=8,
                  fundamental=first,doubled=second,
                  finite_route_site_roles=len(registry),
                  translated_vertices_checked=translated,
                  whole_graph_energy=whole_graph_energy_check(compiler),
                  covariance=covariance_checks(compiler),
                  scope='generic connected periodic grouped graph; DK matching and Record star remain open')
    return result



"""Extra input rosters target negative displacements and multiple home types."""
import gc
import json
from pathlib import Path




def routing_stress_cases():
    cases=[]
    inputs=[
        ((4,3),[
            Edge(0,0,0,1,(1,0,0)), Edge(0,1,1,0,(0,1,0)),
            Edge(1,1,0,2,(0,0,-1)), Edge(1,2,1,0,(-1,1,-1)),
            Edge(0,3,1,1,(0,0,0))]),
        ((1,),[Edge(0,0,0,0,(-2,1,-2))]),
    ]
    for payloads,edges in inputs:
        compiler=Compiler(payloads,edges)
        p=compiler.period
        result,roster=compiler.coordinates((p,p,p))
        result.update(microcell_side=compiler.side,source_radius=compiler.radius,
                      home_payloads=payloads,edge_types=len(edges))
        assert result['ordinary_maximum']<=2
        assert result['wrap_steps']>0
        cases.append(result)
        del roster
        gc.collect()
    result=dict(cases=cases,scope='additional exact-coordinate finite falsifiers; not a proof by sampling')
    return result



"""Protected finite Record-star geometry inside the periodic routing template.

Port demands (8,1,1) are extracted from the actual width-four fixture.
The periodic edge roster below is a stress family, not an arbitrary-cover DK
source. It tests the local cluster template and its finite-period extension.
"""
import json
from math import isqrt
from pathlib import Path



class RecordCompiler(Compiler):
    OFFSETS=((1,0,0),(0,1,0),(0,0,1),(0,0,0))
    BLANKS={(-1,0,0),(0,-1,0),(0,0,-1)}

    def __init__(self, edges):
        super().__init__((4,3,2,3),edges)
        self.columns=isqrt(self.colors)
        if self.columns*self.columns<self.colors:
            self.columns+=1
        assert [sum(e.left==h for e in edges)+sum(e.right==h for e in edges)
                for h in range(4)]==[8,1,1,0]

    def cluster_center(self,n):
        index=self.color_id(n)
        offset=(10+20*(index % self.columns),10+20*(index//self.columns),self.z0)
        return tuple(self.side*a+b for a,b in zip(n,offset))

    def home(self,n,h):
        return add(self.cluster_center(n),self.OFFSETS[h])

    def escape(self,home,port):
        coarse=tuple(a//self.side for a in home)
        center=self.cluster_center(coarse)
        offset=tuple(a-b for a,b in zip(home,center))
        h=self.OFFSETS.index(offset)
        if h==0:
            legacy=(0,1,2,6,7,8,9,10)[port]
        else:
            assert h in (1,2) and port==0
            legacy=3  # negative x direction and branch -1
        group,slot=divmod(legacy,3)
        branch=(-1,0,1)[slot]
        if group in (0,1):
            sign=1 if group==0 else -1
            relative=[(sign,0,0),(2*sign,0,0),(3*sign,0,0)]
            if branch:
                relative.append((3*sign,branch,0))
            relative.append((3*sign,branch,1))
        else:
            assert group in (2,3)
            sign=1 if group==2 else -1
            relative=[(0,sign,0),(0,2*sign,0),(0,3*sign,0)]
            if branch:
                relative.append((branch,3*sign,0))
            relative.append((branch,3*sign,1))
        return [add(home,r) for r in relative]

    def forbidden(self,site):
        if site[2] % self.side not in (self.z0-1,self.z0):
            return False
        coarse=tuple(a//self.side for a in site)
        center=self.cluster_center(coarse)
        return tuple(a-b for a,b in zip(site,center)) in self.BLANKS




def record_cluster_cases():
    edges=[Edge(0,0,0,1,(1,0,0)),Edge(0,2,0,3,(0,1,0)),
           Edge(0,0,0,2,(0,0,1)),Edge(0,1,1,0,(-1,0,1)),
           Edge(0,3,2,0,(0,-1,-1))]
    compiler=RecordCompiler(edges)
    p=compiler.period
    first,roster=compiler.coordinates((p,p,p))
    second,_=compiler.coordinates((2*p,p,p),roster)
    assert second['active_sites']==2*first['active_sites']
    assert second['hidden_variables']==2*first['hidden_variables']
    assert first['ordinary_maximum']<=3
    assert first['maximum_payload_load']==4
    result=dict(template='supplied finite Record cluster',ports=[8,1,1],
                cluster_payloads=[4,3,2,3],blank_neighbors_preserved=True,
                microcell_side=compiler.side,fundamental=first,doubled=second,
                scope='supplied protected cluster geometry; no periodic DK source-family claim')
    return result



"""Separate finite-matrix checks of the explicit Gaussian congruence bounds."""
import json
from pathlib import Path
import numpy as np
from scipy.linalg import block_diag


def spectral_checks():
    rng=np.random.default_rng(912844)
    raw=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4))
    positive=raw.conj().T@raw/20
    rows=[]
    for mass in (.01,.3,2.):
        q=mass*np.eye(4)+positive
        edges=[(i,j,q[i,j]) for i in range(4) for j in range(i+1,4)]
        lengths=list(range(1,7))
        total=sum(lengths)
        triangular=np.zeros((total,total),complex)
        endpoint=np.zeros((total,4),complex)
        local=np.zeros((4+total,4+total),complex)
        local[:4,:4]=q
        cursor=0
        for (u,v,a),h in zip(edges,lengths):
            local[u,v]-=a
            local[v,u]-=a.conjugate()
            local[u,u]+=1
            local[v,v]+=h*abs(a)**2
            for j in range(h):
                k=cursor+j
                triangular[k,k]=1
                if j:
                    triangular[k,k-1]=1
                else:
                    endpoint[k,u]=1
                endpoint[k,v]=(-1)**(j+1)*a
                local[4+k,4+k]=1 if j==h-1 else 2
                if j:
                    local[4+k,3+k]=local[3+k,4+k]=1
            local[u,4+cursor]=local[4+cursor,u]=1
            last=4+cursor+h-1
            local[last,v]=(-1)**h*a
            local[v,last]=((-1)**h*a).conjugate()
            cursor+=h
        transform=np.block([[np.eye(4),np.zeros((4,total))],
                            [endpoint,triangular]])
        congruence=transform.conj().T@block_diag(q,np.eye(total))@transform
        assert np.max(abs(local-congruence))<1e-12
        h=max(lengths)
        degree=3
        amax=max(abs(a) for _,_,a in edges)
        b=np.sqrt((1+amax)*degree*max(1,h*amax))
        assert np.linalg.norm(endpoint,2)<=b
        assert np.linalg.norm(triangular,2)<=2
        assert np.linalg.norm(np.linalg.inv(triangular),2)<=h
        assert np.linalg.norm(transform,2)<=3+b
        assert np.linalg.norm(np.linalg.inv(transform),2)<=1+h*(1+b)
        qtop=np.linalg.eigvalsh(q)[-1]
        lower=min(mass,1)/(1+h*(1+b))**2
        upper=max(qtop,1)*(3+b)**2
        eig=np.linalg.eigvalsh(local)
        assert eig[0]>=lower and eig[-1]<=upper
        hidden=local[4:,4:]
        recovered=local[:4,:4]-local[:4,4:]@np.linalg.solve(hidden,local[4:,:4])
        assert np.max(abs(recovered-q))<1e-12
        assert abs(np.linalg.det(hidden)-1)<1e-12
        rows.append(dict(source_mass=mass,b_bound=b,lower_bound=lower,
                         actual_minimum=float(eig[0]),upper_bound=float(upper),
                         actual_maximum=float(eig[-1]),
                         schur_error=float(np.max(abs(recovered-q)))))
    return dict(cases=rows,hidden_variables=total,
                status='finite matrix congruence, norm, spectrum and Schur checks; all-volume bounds are proved separately')




def main():
    result = dict(codec=codec_checks(),
                  measure=measure_checks(),
                  closed_support_codec=closed_codec_checks(),
                  exact_relay=relay_checks(),
                  periodic_map=periodic_cases(),
                  routing_stress=routing_stress_cases(),
                  protected_cluster=record_cluster_cases(),
                  massive_spectral_bounds=spectral_checks(),
                  status='author_checked_finite_witnesses; independent_review_pending',
                  open='source/action/measure selection, periodic DK family and autonomous formation')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
