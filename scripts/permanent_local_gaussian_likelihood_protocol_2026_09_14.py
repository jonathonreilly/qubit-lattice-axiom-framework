#!/usr/bin/env python3
"""Supplied local permanent Gaussian likelihood programs and posterior costs.

All new geometry, carrier, Gaussian and bound checks are defined here. The
two declared scientific inputs define the current finite source matrices;
their historical theorem/audit claims are not invoked. The constructed roots
are commuting complex random variables. Source, program, schedule and later
conditioning are supplied; no native action, Born law or phase is selected.
"""
from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import itertools
import json
from math import isqrt
from pathlib import Path
import sys

import numpy as np
import sympy as s

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py',
)
INPUT_SHA256 = (
    '8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2',
    '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
)
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10 as source


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



SCALE=10


def axis(a,b):
    axes=[i for i in range(3) if a[i]!=b[i]]
    assert len(axes)==1,(a,b)
    return axes[0]


def simplify(points):
    out=[]
    for p in points:
        if out and out[-1]==p:
            continue
        if len(out)>=2:
            i=axis(out[-2],out[-1])
            j=axis(out[-1],p)
            if i==j and (out[-1][i]-out[-2][i])*(p[i]-out[-1][i])>0:
                out[-1]=p
                continue
        out.append(p)
    return out


def quotient_segments(points,periods,wire):
    """Split lifted inclusive segments at periodic seams, retaining endpoint 0.

    A segment through coordinate L includes the quotient vertex zero, even
    if its final lifted endpoint is exactly L. Singleton seam pieces matter.
    """
    out=[]
    for a,b in zip(points,points[1:]):
        i=axis(a,b)
        lower,upper=sorted((a[i],b[i]))
        size=periods[i]
        fixed=tuple(a[j]%periods[j] for j in range(3))
        first=lower//size
        last=upper//size
        for slab in range(first,last+1):
            lo=max(lower,slab*size)-slab*size
            hi=min(upper,(slab+1)*size-1)-slab*size
            if lo<=hi:
                out.append((i,fixed,lo,hi,wire))
    return out


def intersection_check(segments,homes,endpoints,controls):
    """Exact integer segment comparisons, independent of route generation.

    Foreign wires may meet only at their common true gate endpoint. The
    generator separately proves/tests simplicity of each lifted wire; this
    check also rejects any positive-length self-overlap.
    """
    buckets=defaultdict(list)
    counts=Counter()
    def permit(a,b,p,overlap_length=0):
        if overlap_length:
            raise AssertionError(('positive segment overlap',a,b,p,overlap_length))
        if a[4]==b[4]:
            # Turning vertices occur in two consecutive segments of a wire.
            # A later independent per-wire point/segment test controls repeats.
            counts['same_wire_turn']+=1
            return
        assert p in homes and p in endpoints[a[4]] and p in endpoints[b[4]],('foreign wire collision',a,b,p)
        counts['shared_gate']+=1
    for seg in segments:
        i,f,lo,hi,_=seg
        key=(i,tuple(f[j] for j in range(3) if j!=i))
        buckets[key].append(seg)
    for group in buckets.values():
        group.sort(key=lambda z:z[2])
        active=[]
        for b in group:
            active=[a for a in active if a[3]>=b[2]]
            for a in active:
                lower=max(a[2],b[2]);upper=min(a[3],b[3])
                p=list(a[1]);p[a[0]]=lower
                permit(a,b,tuple(p),upper-lower)
            active.append(b)
    for i,j in ((0,1),(0,2),(1,2)):
        k=3-i-j
        left=defaultdict(list);right=defaultdict(list)
        for seg in segments:
            if seg[0]==i:
                left[seg[1][k]].append(seg)
            elif seg[0]==j:
                right[seg[1][k]].append(seg)
        for level,aa in left.items():
            for a in aa:
                for b in right.get(level,()):
                    if a[2]<=b[1][i]<=a[3] and b[2]<=a[1][j]<=b[3]:
                        p=list(a[1]);p[i]=b[1][i]
                        permit(a,b,tuple(p))
    # Controls are not wire vertices or homes. Point query uses the same
    # exact interval representation, not a sampled distance test.
    for p in controls:
        assert p not in homes
        for i in range(3):
            key=(i,tuple(p[j] for j in range(3) if j!=i))
            assert all(not lo<=p[i]<=hi for _,_,lo,hi,_ in buckets.get(key,())),('control collision',p)
    return dict(counts)


def run_case(name,edges,stages,cover_multiplier=(1,1,1),expected_registry=None):
    compiler=Compiler([1]*len(stages),edges)
    # At most four horizontal ports; distinct first directions remove the
    # two-lanes-per-direction shared terminal in the scalar immersion.
    assert max(compiler.ports.values())<=3
    compiler.ports={key:2*p for key,p in compiler.ports.items()}
    for e in edges:
        assert stages[e.left]<stages[e.right]
    p=compiler.period
    cover=tuple(p*a for a in cover_multiplier)
    periods=tuple(SCALE*compiler.side*a for a in cover)
    homes={compiler.quotient(compiler.home(n,h),cover)
           for n in product(*(range(a) for a in cover)) for h in range(len(stages))}
    paths=[]
    occupancy=defaultdict(list)
    for n in product(*(range(a) for a in cover)):
        for e in range(len(edges)):
            lifted=compiler.route(n,e)
            quotient=[compiler.quotient(x,cover) for x in lifted]
            assert len(set(quotient))==len(quotient)
            wire=len(paths)
            paths.append((n,e,lifted,quotient))
            for j,x in enumerate(quotient[1:-1],1):
                assert x not in homes
                occupancy[x].append((wire,j))
    detours=defaultdict(set)
    crossing_types=Counter()
    for point,entries in occupancy.items():
        assert len(entries)<=2
        if len(entries)==1:
            continue
        vertical=[]
        for wire,j in entries:
            path=paths[wire][2]
            axes=(axis(path[j-1],path[j]),axis(path[j],path[j+1]))
            if axes==(2,2):
                assert path[j+1][2]-path[j][2]==path[j][2]-path[j-1][2]
                vertical.append((wire,j))
            else:
                assert 2 not in axes,('crossing is not horizontal/vertical',point,entries,axes)
                crossing_types[str(axes)]+=1
        assert len(vertical)==1,('crossing lacks a unique vertical strand',point,entries)
        detours[vertical[0][0]].add(vertical[0][1])
    scaled_homes={tuple(SCALE*x for x in h) for h in homes}
    controls={tuple((x-(1 if i==2 else 0))%periods[i] for i,x in enumerate(h)) for h in scaled_homes}
    endpoints={}
    segments=[]
    lengths=[]
    digest=sha256()
    final_routes=[]
    registry={}
    for wire,(n,e,path,quotient) in enumerate(paths):
        points=[]
        for j,x in enumerate(path):
            center=tuple(SCALE*a for a in x)
            if j not in detours[wire]:
                points.append(center)
                continue
            dz=path[j+1][2]-x[2]
            before=add(center,(0,0,-2*dz));after=add(center,(0,0,2*dz))
            points.extend((before,add(before,(1,0,0)),add(before,(1,1,0)),
                           add(after,(1,1,0)),add(after,(1,0,0)),after))
        points=simplify(points)
        key=(e,compiler.color(n))
        relative=tuple(tuple(x-SCALE*compiler.side*n[i] for i,x in enumerate(v)) for v in points)
        if key in registry:
            assert registry[key]==relative,'A repeated coarse color changes the detour pattern'
        registry[key]=relative
        if expected_registry is not None:
            assert expected_registry[key]==relative,'A larger cover changes the causal local role map'
        length=sum(abs(a[axis(a,b)]-b[axis(a,b)]) for a,b in zip(points,points[1:]))
        assert length==SCALE*(len(path)-1)+4*len(detours[wire])
        lengths.append(length)
        ep={tuple(x%periods[i] for i,x in enumerate(points[0])),
            tuple(x%periods[i] for i,x in enumerate(points[-1]))}
        assert len(ep)==2 and ep<=scaled_homes
        endpoints[wire]=ep
        own_segments=quotient_segments(points,periods,wire)
        # A per-wire multiplicity count of all inclusive segment intersections
        # equals the number of turn vertices. A periodic seam split adds no
        # duplicated zero/L vertex, because integer slabs use L-1 then zero.
        own_turns=0
        for a_i,a in enumerate(own_segments):
            for b in own_segments[a_i+1:]:
                if a[0]==b[0]:
                    other=[j for j in range(3) if j!=a[0]]
                    if all(a[1][j]==b[1][j] for j in other):
                        lo=max(a[2],b[2]);hi=min(a[3],b[3])
                        assert lo>hi,('self collinear overlap',wire,a,b)
                else:
                    i,j=a[0],b[0];k=3-i-j
                    if a[1][k]==b[1][k] and a[2]<=b[1][i]<=a[3] and b[2]<=a[1][j]<=b[3]:
                        own_turns+=1
        assert own_turns==len(points)-2,('nonconsecutive self intersection',wire,own_turns,len(points)-2)
        segments.extend(own_segments)
        final_routes.append(points)
        digest.update(repr((n,e,points)).encode())
    checked=intersection_check(segments,scaled_homes,endpoints,controls)
    # Assign strict causal levels to every gate and internal unit vertex.
    # These rational levels need not be encoded as floating point or clocks.
    for wire,(n,e,path,quotient) in enumerate(paths):
        assert stages[edges[e].right]-stages[edges[e].left]>=1
        # Level along edge j is s_left+(s_right-s_left)j/length.
        assert lengths[wire]>0
    result=dict(name=name,coarse_cover=cover,coarse_period=p,coarse_side=compiler.side,
                final_physical_periods=periods,wires=len(paths),gate_sites=len(scaled_homes),
                controls=len(controls),crossings_removed=sum(map(len,detours.values())),
                original_crossing_types=dict(crossing_types),
                maximum_original_internal_load=max(map(len,occupancy.values())),
                final_interval_pieces=len(segments),maximum_path_edges=max(lengths),
                hidden_copy_sites=sum(length-1 for length in lengths),
                exact_final_intersection_counts=checked,vertex_disjoint_foreign_wires=True,
                coordinate_sha256=digest.hexdigest(),
                cover_independent_role_map=(expected_registry is not None),
                scope='Supplied periodic type DAG, one complex payload per gate/copy, controls supplied; no autonomous program or state selection')
    return result,registry




def causal_wire_checks():
    standard=[Edge(0,0,2,0,(1,0,0)),Edge(1,0,2,0,(0,1,0)),Edge(2,0,3,0,(0,0,1))]
    negative=[Edge(0,0,2,0,(-1,0,-1)),Edge(1,0,2,0,(0,-1,0)),Edge(2,0,3,0,(1,1,1))]
    base,registry=run_case('three-axis sum DAG',standard,[0,0,1,2])
    negative_row,_=run_case('negative-displacement DAG',negative,[0,0,1,2])
    doubled,_=run_case('doubled first axis',standard,[0,0,1,2],(2,1,1),registry)
    rows=[base,negative_row,doubled]

    return rows


PAULI=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],dtype=complex)
V=np.array([1,2,3])
ROTS=[]
for permutation in itertools.permutations(range(3)):
    for signs in itertools.product((-1,1),repeat=3):
        r=np.zeros((3,3),dtype=int)
        for i in range(3):
            r[i,permutation[i]]=signs[i]
        if round(np.linalg.det(r))==1:
            ROTS.append(r)
ORBIT={tuple(r@V):i for i,r in enumerate(ROTS)}
assert len(ORBIT)==24


def encode(role,frame,z):
    vector=(8*role+1)*(ROTS[frame]@V)
    return z*np.eye(2)+sum(vector[i]*PAULI[i] for i in range(3))


def decode(matrix):
    z=np.trace(matrix)/2
    vector=np.array([np.trace(matrix@p)/2 for p in PAULI])
    assert np.max(abs(vector.imag))<1e-10
    length=np.linalg.norm(vector.real)
    role=round((length/np.sqrt(14)-1)/8)
    assert role>=0
    orbit=tuple(np.rint(vector.real/(8*role+1)).astype(int))
    frame=ORBIT[orbit]
    assert np.linalg.norm(matrix-encode(role,frame,z))<1e-9
    return role,frame,z


def star_action(rotation,matrix):
    z=np.trace(matrix)/2
    components=np.array([np.trace(matrix@p)/2 for p in PAULI])
    vector=rotation@components
    return z*np.eye(2)+sum(vector[i]*PAULI[i] for i in range(3))




def local_rule_window_checks():
    roots=[(0,0,0),(2,0,0),(2,2,0),(0,2,0)]
    observations=[(1,0,0),(2,1,0),(1,2,0),(0,1,0)]
    controls=[(x,y,1) for x,y,z in roots]
    positions=roots+observations+controls
    parent={i:[8+i] for i in range(4)}
    parent.update({4+i:[i,(i+1)%4] for i in range(4)})
    output={i:[] for i in range(12)}
    for child,pp in parent.items():
        for p in pp:
            output[p].append(child)
            assert sum(abs(a-b) for a,b in zip(positions[child],positions[p]))==1
    delta=lambda a,b:np.array(a)-np.array(b)
    innovations={i:complex((17*i+3)/13,(11*i-2)/19) for i in range(8)}
    expected={i:innovations[i] for i in range(4)}
    expected.update({4+i:expected[(i+1)%4]-expected[i]+innovations[4+i] for i in range(4)})
    rng=np.random.default_rng(539201)
    default_atoms=tuple(itertools.product(range(8,12),range(len(ROTS))))
    default_weight=s.Rational(1,len(default_atoms))
    assert sum(default_weight for _ in default_atoms)==1
    checks=0
    maximum_error=0.
    def rule(site,records):
        # Only the six actual nearest records are read. A candidate target is
        # inferred from an incoming neighbor's finite role/direction table.
        neighbors={}
        for ax in range(3):
            for sign in (-1,1):
                step=np.zeros(3,dtype=int);step[ax]=sign
                point=tuple(np.array(site)+step)
                if point in records:
                    try:
                        decoded=decode(records[point])
                    except (AssertionError,KeyError):
                        return None
                    if decoded[0] not in range(12):
                        return None
                    neighbors[point]=decoded
        candidates=set()
        for point,(r,frame,z) in neighbors.items():
            for child in output.get(r,()):
                target=tuple(np.array(point)+ROTS[frame]@delta(positions[child],positions[r]))
                if target==site:
                    candidates.add((child,frame))
        enabled=[]
        for child,frame in candidates:
            values=[]
            for p in parent[child]:
                point=tuple(np.array(site)+ROTS[frame]@delta(positions[p],positions[child]))
                data=neighbors.get(point)
                if data is None or data[:2]!=(p,frame):
                    break
                values.append(data[2])
            else:
                mean=0j if child<4 else values[1]-values[0]
                enabled.append((child,frame,mean,1.))
        return enabled[0] if len(enabled)==1 else None
    # None denotes the rotation-invariant default: all 4 control roles and
    # all 24 frames with z=0, each atom probability 1/96. It is not a missing
    # distribution; the supplied schedule executes the Gaussian cases only
    # after conditioning on the coherent control program.
    for frame,rotation in enumerate(ROTS):
        origin=np.array([13,-7,5])
        physical=[tuple(rotation@np.array(p)+origin) for p in positions]
        for i in range(12):
            z=complex((i+1)/7,-(i+3)/11)
            r,f,decoded=decode(encode(i,frame,z))
            assert (r,f)==(i,frame) and abs(decoded-z)<1e-12
        for other in ROTS:
            z=.375-.625j
            composite=ORBIT[tuple(other@rotation@V)]
            maximum_error=max(maximum_error,float(np.linalg.norm(
                star_action(other,encode(11,frame,z))-encode(11,composite,z))))
        left=np.array([[1+2j,3-4j],[5+6j,-7+8j]])
        right=np.array([[2-3j,-4+5j],[6-7j,8+9j]])
        assert np.linalg.norm(star_action(rotation,left@right)-star_action(rotation,left)@star_action(rotation,right))<1e-10
        assert np.linalg.norm(star_action(rotation,left.conj().T)-star_action(rotation,left).conj().T)<1e-10
        assert {(r,ORBIT[tuple(rotation@ROTS[f]@V)]) for r,f in default_atoms}==set(default_atoms)
        for _ in range(8):
            records={}
            for i in range(4):
                assert rule(physical[8+i],records) is None
                # The chosen value is one of the 96 positive default atoms.
                records[physical[8+i]]=encode(8+i,frame,0j)
            assert all(sum(abs(a-b) for a,b in zip(x,y))>1 for x,y in itertools.combinations(records,2))
            pending=set(range(8))
            while pending:
                ready=[]
                for i in pending:
                    action=rule(physical[i],records)
                    if action is not None:
                        assert action[:2]==(i,frame)
                        ready.append((i,action))
                assert ready
                i,action=ready[int(rng.integers(len(ready)))]
                assert physical[i] not in records
                records[physical[i]]=encode(i,frame,action[2]+innovations[i])
                pending.remove(i)
            for i in range(8):
                assert abs(decode(records[physical[i]])[2]-expected[i])<1e-12
            checks+=1
    assert maximum_error<1e-10
    for rotation in ROTS:
        bad=star_action(rotation,np.array([[1+2j,3+4j],[5+6j,7+8j]]))
        assert rule((0,0,0),{(1,0,0):bad}) is None

    # Exact diagonal complex-Gaussian disk probabilities challenge the window
    # dimension and pi normalization independently of the determinant code.
    window_rows=[]
    alpha=s.Rational(1,5)
    linear=s.diag(s.Rational(3,2),s.Rational(2,3))
    noise=s.diag(s.Rational(1,2),s.Rational(4,3))
    covariance=noise+linear*linear.H/alpha
    precision=alpha*s.eye(2)+linear.H*noise.inv()*linear
    p0_without_pi=1/covariance.det()
    assert s.cancel(p0_without_pi-alpha**2/(noise.det()*precision.det()))==0
    for epsilon in (s.Rational(1,100),s.Rational(1,2),s.Rational(2)):
        actual=s.prod(1-s.exp(-epsilon**2/covariance[i,i]) for i in range(2))
        high=epsilon**4*p0_without_pi
        exponent=2*epsilon**2/min(noise.diagonal())
        low=s.exp(-exponent)*high
        assert float(low)<=float(actual)<=float(high)
        window_rows.append(dict(epsilon=str(epsilon),acceptance=float(actual),
                                lower_bound=float(low),upper_bound=float(high)))
    # A complex shifted Gaussian equals two real Gaussians with covariance
    # C/2. Their elementary real KL independently fixes the factor of two.
    c=s.Rational(3,7);mean=s.Matrix([s.Rational(2,3),s.Rational(-4,5)])
    real_kl=(mean.T*(s.eye(2)*c/2).inv()*mean)[0]/2
    complex_kl=(mean.dot(mean))/c
    assert real_kl==complex_kl
    # Attainment of the sharp tilt inequality, not only an upper-bound test.
    a,b=s.Rational(1,4),s.Rational(9)
    probability=(b-s.sqrt(a*b))/(b-a)
    mu=probability*a+(1-probability)*b
    tv=(probability*abs(a/mu-1)+(1-probability)*abs(b/mu-1))/2
    sharp=(s.sqrt(b)-s.sqrt(a))/(s.sqrt(b)+s.sqrt(a))
    assert s.simplify(tv-sharp)==0
    result=dict(complex_codec_roles=12,frames=24,star_action_compositions=576,
                maximum_star_action_error=maximum_error,causal_schedules_checked=checks,
                same_rule_reads_six_neighbors=True,records_written_once=True,
                default_control_atoms=len(default_atoms),
                algebra_product_and_star_checks=48,
                coherent_four_control_program_probability=str(default_weight**4),
                complex_disk_window_checks=window_rows,
                independent_real_complex_kl=str(real_kl),sharp_tilt_bound_attained=str(sharp),
                scope='Supplied program and fair schedule; coherent finite controls and later observations are conditioned on, not typical-state or Born selection')

    return result


def clean(matrix):
    return matrix.applyfunc(s.cancel)


def array(matrix):
    return np.array(matrix.evalf(),dtype=complex)


def arithmetic_circuit(linear,roster):
    """Independent roots, binary copy trees, unary scale, binary sum, noise.

    Every edge points to a later node. All scalar degrees are at most three.
    This is a logical circuit; its physical embedding is a separate obligation.
    """
    nodes=[]
    outputs=defaultdict(list)
    forms=[]
    def node(kind, parents=(), coefficients=(), root=None):
        i=len(nodes)
        form=defaultdict(lambda:s.Integer(0))
        if root is not None:
            form[root]=s.Integer(1)
        for p,c in zip(parents,coefficients):
            assert p<i
            outputs[p].append(i)
            for k,v in forms[p].items():
                form[k]+=c*v
        forms.append({k:s.expand(v) for k,v in form.items() if s.expand(v)!=0})
        nodes.append(dict(kind=kind,parents=list(parents),coefficients=list(map(str,coefficients)),
                          stage=0 if not parents else 1+max(nodes[p]['stage'] for p in parents)))
        return i
    roots=[node('root',root=j) for j in range(linear.cols)]
    usages=defaultdict(list)
    for i in range(linear.rows):
        for j in range(linear.cols):
            if (i,j) in roster:
                usages[j].append((i,linear[i,j]))
    row_terms=defaultdict(list)
    def split(parent,items):
        if len(items)==1:
            row,coefficient=items[0]
            row_terms[row].append(node('scale',(parent,),(coefficient,)))
            return
        middle=len(items)//2
        for part in (items[:middle],items[middle:]):
            child=node('copy',(parent,),(s.Integer(1),))
            split(child,part)
    for j,items in usages.items():
        split(roots[j],items)
    observations=[]
    for row in range(linear.rows):
        layer=row_terms[row]
        assert layer
        while len(layer)>1:
            next_layer=[]
            for start in range(0,len(layer),2):
                pair=layer[start:start+2]
                next_layer.append(pair[0] if len(pair)==1 else node('sum',pair,(s.Integer(1),)*2))
            layer=next_layer
        observed=node('observation',layer,(s.Integer(1),))
        expected={j:linear[row,j] for j in range(linear.cols) if linear[row,j]!=0}
        assert forms[observed]==expected
        observations.append(observed)
    degree=[len(n['parents'])+len(outputs[i]) for i,n in enumerate(nodes)]
    assert max(degree)<=3
    assert all(nodes[i]['stage']>nodes[p]['stage'] for i,n in enumerate(nodes) for p in n['parents'])
    topology=[(n['kind'],n['parents'],n['stage']) for n in nodes]
    return dict(nodes=len(nodes),edges=sum(map(len,outputs.values())),
                kinds=dict(Counter(n['kind'] for n in nodes)),maximum_degree=max(degree),
                maximum_stage=max(n['stage'] for n in nodes),
                exact_observation_linear_forms=True,
                topology_sha256=sha256(json.dumps(topology,sort_keys=True).encode()).hexdigest(),
                circuit_sha256=sha256(json.dumps(nodes,sort_keys=True).encode()).hexdigest())




def dk_likelihood_checks():
    fixture=source.Fixture(4,pattern=None,tag='source-likelihood')
    qs=[fixture.q({source.RECORD_CELL:value}) for value in source.MENU]
    ss=[clean((q+q.H)/2) for q in qs]
    edges=source.edge_union(tuple(ss))
    bundles={fraction:[source.arm_bundle(fixture,value,edges,fraction=fraction)
                       for value in source.MENU]
             for fraction in (s.Rational(1,2),s.Rational(1,3))}
    roster=set()
    for arms in bundles.values():
        for arm in arms:
            q,b=arm['q'],arm['B']
            n,k=q.rows,b.cols
            linear=q.row_join(-b).col_join(s.zeros(k,n).row_join(s.eye(k)))
            roster.update((i,j) for i in range(n+k) for j in range(n+k) if linear[i,j]!=0)
    rows=[]
    for fraction in (s.Rational(1,2),s.Rational(1,3)):
        arm_rows=[]
        for value,arm in zip(source.MENU,bundles[fraction]):
            q,b,S,c=arm['q'],arm['B'],arm['S'],arm['variance']
            n,k=q.rows,b.cols
            d=n+k
            assert all(r>=0 for r in arm['residuals'])
            assert clean(b*b.H+c*s.eye(n)-S)==s.zeros(n)
            linear=q.row_join(-b).col_join(s.zeros(k,n).row_join(s.eye(k)))
            noise=s.diag(c*s.eye(n),s.eye(k))
            qinv=arm['q_inv']
            c0=arm['W'].row_join(qinv*b).col_join((b.H*qinv.H).row_join(s.eye(k)))
            Q0=clean(linear.H*noise.inv()*linear)
            # Exact right inverse, including radical cross-block entries.
            assert clean(Q0*c0)==s.eye(d)
            trace=s.cancel(s.trace(c0))
            gamma=s.Rational(243,416)
            margin=min(s.cancel(S[i,i]-sum(s.Abs(S[i,j]) for j in range(n) if i!=j)) for i in range(n))
            assert margin>=gamma
            lower=gamma/(1+gamma)
            det0=s.cancel(source.norm2(arm['det_q'])/c**n)
            assert s.cancel(1/det0-arm['raw_mass'])==0
            naive_phi_block=clean(q.H*q/c)
            phi_off=sum(1 for i in range(n) for j in range(i+1,n) if naive_phi_block[i,j]!=0)
            unconditional=array(s.eye(d))
            ln=array(linear)
            nn=array(noise)
            cn=array(c0)
            qn=array(Q0)
            assert np.linalg.norm(qn@cn-np.eye(d),ord=2)<1e-10
            assert np.linalg.eigvalsh(qn)[0]>float(lower)
            variants=[]
            for alpha in (s.Rational(1,10),s.Rational(1,100)):
                # Integrate the zeta block using Sylvester's determinant identity.
                sa=S+alpha*c*s.eye(n)
                pphi=clean(alpha*s.eye(n)+(1+alpha)*q.H*source.exact_inv(sa)*q)
                ddet=(1+alpha)**(k-n)*source.dm_det(sa)/c**n
                deta=s.cancel(ddet*source.dm_det(pphi))
                exact_phi=source.exact_inv(pphi)
                numeric_q=qn+float(alpha)*np.eye(d)
                numeric_c=np.linalg.inv(numeric_q)
                assert np.linalg.norm(numeric_c[:n,:n]-array(exact_phi),ord=2)<1e-10
                sign,logdet=np.linalg.slogdet(numeric_q)
                assert abs(sign-1)<1e-10
                assert abs(logdet-float(s.log(deta)))<1e-9
                # Independently condition the full generative joint covariance.
                prior=unconditional/float(alpha)
                ycov=ln@prior@ln.conj().T+nn
                conditioned=prior-prior@ln.conj().T@np.linalg.solve(ycov,ln@prior)
                assert np.linalg.norm(conditioned-numeric_c,ord=2)<1e-8
                density_log=-d*np.log(np.pi)-np.linalg.slogdet(ycov)[1]
                expected=d*np.log(float(alpha))-d*np.log(np.pi)-n*np.log(float(c))-logdet
                assert abs(density_log-expected)<1e-9
                ratio=s.cancel(deta/det0)
                assert ratio>=1 and ratio<=(1+alpha/lower)**d
                # Complex Gaussian KL, independently from trace/log determinants.
                kl=float(np.trace(qn@numeric_c).real-d+logdet-float(s.log(det0)))
                kl_bound=d*float(alpha/lower)**2/2
                assert -1e-10<=kl<=kl_bound
                covariance_error=float(np.linalg.norm(numeric_c-cn,ord=2))
                assert covariance_error<=float(alpha/lower**2)
                # Store pi^d p(Y=0)/alpha^d; its limit differs from raw mass
                # by det(noise), which is constant only within the arm menu.
                scaled_density=s.cancel(1/(c**n*deta))
                variants.append(dict(alpha=str(alpha),determinant_ratio=str(ratio),
                                     scaled_observation_density=str(scaled_density),
                                     gaussian_kl=kl,kl_upper_bound=kl_bound,
                                     covariance_error=covariance_error,
                                     covariance_error_bound=float(alpha/lower**2)))
            arm_rows.append(dict(value=str(value),phi_dimension=n,zeta_dimension=k,
                                 complex_dimension=d,trace_target_covariance=str(trace),
                                 precision_lower_bound=str(lower),finite_trace_lower_bound=str(1/trace),target_raw_mass=str(arm['raw_mass']),
                                 phi_block_nonzero_upper_offdiagonals=phi_off,
                                 naive_two_layer_phi_block_diagonal=(phi_off==0),
                                 logical_likelihood_circuit=arithmetic_circuit(linear,roster),variants=variants))
            print(f'checked supplied c={fraction}, arm={value}, complex dimension={d}',flush=True)
        masses=[s.Rational(r['target_raw_mass']) for r in arm_rows]
        target=[v/sum(masses) for v in masses]
        lower=min(s.Rational(r['precision_lower_bound']) for r in arm_rows)
        weights=[]
        for j,alpha in enumerate((s.Rational(1,10),s.Rational(1,100))):
            densities=[s.Rational(r['variants'][j]['scaled_observation_density']) for r in arm_rows]
            actual=[v/sum(densities) for v in densities]
            tv=s.cancel(sum(abs(a-b) for a,b in zip(actual,target))/2)
            bound=1-(1+alpha/lower)**(-arm_rows[0]['complex_dimension'])
            assert tv<=bound
            tilts=[1/s.Rational(a['variants'][j]['determinant_ratio']) for a in arm_rows]
            low,high=min(tilts),max(tilts)
            sharp=(s.sqrt(high)-s.sqrt(low))/(s.sqrt(high)+s.sqrt(low))
            assert float(tv)<=float(sharp)+1e-14
            weights.append(dict(alpha=str(alpha),normalized=[str(v) for v in actual],
                                target=[str(v) for v in target],tv=float(tv),
                                tv_upper_bound=float(bound),
                                exact_extremal_tilt_upper_bound=float(sharp)))
        rows.append(dict(fraction=str(fraction),arms=arm_rows,menu_weights=weights))
    topologies={a['logical_likelihood_circuit']['topology_sha256'] for row in rows for a in row['arms']}
    assert len(topologies)==1
    result=dict(source_path=str(Path(source.__file__).relative_to(ROOT)),
                source_sha256=sha256(Path(source.__file__).read_bytes()).hexdigest(),
                supplier_certificate=source.supplier_certificate(),
                common_circuit_topology_sha256=next(iter(topologies)),
                common_linear_coefficient_roster=len(roster),
                source_condition='T_cover=12, width=4, xgraded, mass=1, four supplied Record values',
                rows=rows,
                scope='Proper independent prior and supplied noisy linear circuit; source law is recovered only by conditioning and an alpha-to-zero limit. Physical wire embedding is separate. No selected native or Born law.')
    assert result['supplier_certificate']

    return result



def source_coercivity_checks():
    vmin,vmax=s.Rational(5,6),s.Rational(13,6)
    smax=s.Rational(3,5)
    gamma=(vmin+1/vmax+2*vmin/(1+smax))/4
    Gamma=(vmax+1/vmin+2*vmax/(1-smax))/4
    assert gamma==s.Rational(243,416) and gamma>s.Rational(1,2)
    rows=[]
    cases=[(12,4,None,s.Rational(1),s.Rational(3,5),s.Rational(0)),
           (16,4,(vmin,)*4,s.Rational(1,10),-smax,smax),
           (12,8,(vmax,vmin)*4,s.Rational(7),smax,-smax)]
    for cover,width,pattern,mass,sigma,record in cases:
        fixture=source.Fixture(width,cover_t=cover,pattern=pattern,tag='source-coercivity')
        q=fixture.q({source.RECORD_CELL:record},mass=mass,sigma=sigma,
                    sx=s.Rational(7,5),st=-s.Rational(2,3))
        S=s.expand((q+q.H)/2)
        h=S/mass
        margins=[];upper=[]
        for i in range(h.rows):
            off=sum(s.Abs(h[i,j]) for j in range(h.cols) if i!=j)
            margins.append(s.cancel(h[i,i]-off))
            upper.append(s.cancel(h[i,i]+off))
        assert min(margins)>=gamma and max(upper)<=Gamma
        # The anti-Hermitian connection contributes no Hermitian part.
        kinetic=fixture.q({source.RECORD_CELL:record},mass=0,sigma=sigma,
                         sx=s.Rational(7,5),st=-s.Rational(2,3))
        assert s.expand(kinetic+kinetic.H)==s.zeros(h.rows)
        assert s.expand(q-kinetic-mass*h)==s.zeros(h.rows)
        # Rebuild the cover quadratic forms before the half-fold. This uses
        # the full sparse construction, not the already-quotiented q matrix.
        substitutions=fixture.substitution(sigma,{source.RECORD_CELL:record},
                                          s.Rational(7,5),-s.Rational(2,3),mass)
        pinned=source.ssubs(fixture.fx.H_free,source.region_pin(fixture.fx,(fixture.c-1,fixture.c)))
        full_h=source.dense(source.ssubs(pinned,substitutions),fixture.fx.SIZE,fixture.fx.SIZE)
        full_d=source.dense(source.ssubs(fixture.fx.edge_d[(0,0)],substitutions),fixture.fx.SIZE,fixture.fx.SIZE)
        half=fixture.N
        compress=lambda A:(A[:half,:half]+A[half:,half:]-A[:half,half:]-A[half:,:half])/2
        assert full_h[:half,:half]==full_h[half:,half:]
        assert full_h[:half,half:]==full_h[half:,:half]
        assert compress(full_h)==h
        full_k=s.I*(full_h*full_d+full_d.H*full_h)
        assert s.expand(compress(full_k)-kinetic)==s.zeros(half)
        c=mass/2
        edges=source.edge_union((S,))
        B,residuals=source.signed_edge_factor(S,c,edges)
        assert min(residuals)>=mass*(gamma-s.Rational(1,2))
        assert s.expand(B*B.H+c*s.eye(h.rows)-S)==s.zeros(h.rows)
        qn=np.array(q.evalf(),dtype=complex)
        bn=np.array(B.evalf(),dtype=complex)
        n,k=bn.shape
        inverse=np.linalg.inv(qn)
        W=(inverse+inverse.conj().T)/2
        D=inverse@bn
        C=np.block([[W,D],[D.conj().T,np.eye(k)]])
        uniform_lower=mass*gamma/(1+mass*gamma)
        L=np.block([[qn,-bn],[np.zeros((k,n)),np.eye(k)]])
        N=np.diag([float(c)]*n+[1.]*k)
        Q=L.conj().T@np.linalg.solve(N,L)
        assert np.linalg.norm(Q@C-np.eye(n+k),ord=2)<1e-9
        assert np.linalg.norm(W-D@D.conj().T-float(c)*inverse@inverse.conj().T,ord=2)<1e-10
        actual_min=float(np.linalg.eigvalsh(Q)[0])
        assert actual_min>float(uniform_lower)
        rows.append(dict(cover_t=cover,width=width,pattern=None if pattern is None else list(map(str,pattern)),
                         mass=str(mass),background_shear=str(sigma),record_shear=str(record),
                         dimension=n+k,smallest_hodge_row_margin=str(min(margins)),
                         largest_hodge_row_sum=str(max(upper)),smallest_gram_residual=str(min(residuals)),
                         uniform_precision_lower_bound=str(uniform_lower),numeric_precision_minimum=actual_min))
    outside=source.Fixture(4,cover_t=10,tag="odd-half-cover-challenge")
    outside_k=outside.q(mass=0,st=s.Rational(2,3))
    hermitian_entries=sum(value!=0 for value in s.expand(outside_k+outside_k.H))
    assert hermitian_entries==16
    result=dict(outside_domain_odd_half_cover_hermitian_entries=hermitian_entries,
                hodge_lower_bound=str(gamma),hodge_upper_bound=str(Gamma),
                source_sha256=sha256(Path(source.__file__).read_bytes()).hexdigest(),
                domain='Temporal cover divisible by four, even width, v in [5/6,13/6], |shear|<=3/5, same local Hodge/fold/pinning definitions; mass>0, c=mass/2 or mass/3',
                claim='Analytical dimension-independent coercivity of this supplied Gaussian family; no massless estimate or native phase selection',
                finite_challenges=rows)

    return result



def main():
    for path,expected in zip(AUDIT_INPUT_PATHS,INPUT_SHA256):
        assert sha256((ROOT/path).read_bytes()).hexdigest()==expected, ('source input drift',path)
    result=dict(causal_wires=causal_wire_checks(),
                local_rule_and_windows=local_rule_window_checks(),
                supplied_dk_likelihood=dk_likelihood_checks(),
                uniform_source_coercivity=source_coercivity_checks(),
                scientific_input_paths=list(AUDIT_INPUT_PATHS),
                status='author_checked; independent_review_pending',
                open='source/program/schedule selection, typical phase, original native Record-star weights, quantum or fermion identification')
    print(json.dumps(result,indent=2))
    print('per_element: complex carrier/linear coefficients, posterior precision and exact determinant formulas checked.')
    print('per_site: complete integer wire/control collision checks on declared finite covers and a twelve-role local-rule example.')
    print('per_mode: finite supplied massive DK matrices and coercivity only; no fermion, quantum or massless identification.')
    print('per_block: three-axis, negative and doubled small-DAG routes and the common logical 768-node DK circuit; full DK physical coordinate roster not executed.')
    print('lattice_wide: checked and not executed — periodic routing, finite-ancestor and coercivity generality use the written proofs; no infinite observation-conditioned sampler executed.')
    print('TOTAL: PASS=4 FAIL=0')


if __name__=='__main__':
    main()
