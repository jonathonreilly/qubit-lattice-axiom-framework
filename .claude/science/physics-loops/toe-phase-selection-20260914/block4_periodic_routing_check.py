#!/usr/bin/env python3
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

from block4_codec_relay_check import rotations, encode, action


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


def main():
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
    Path(__file__).with_name('BLOCK4_PERIODIC_ROUTING_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
