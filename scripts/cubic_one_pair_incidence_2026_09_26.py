"""Exact simultaneous two-hole incidence reconstruction; no primary imports.

Callable helper preserved from the blind reconstruction.
All pairs sharing a B neighbor are generated on each whole periodic torus.
All ordered distinct destination assignments are retained for each pair.
"""
from collections import Counter, defaultdict
from itertools import product, combinations
from pathlib import Path
import argparse
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parent


def parity(p):
    return sum(p) % 2


def baseline(p):
    return 1 - parity(p)


def key(q, e):
    return (tuple(sorted((p, v) for p, v in q.items() if v != baseline(p))),
            tuple(sorted((edge, v) for edge, v in e.items() if v)))


def decode(raw, length=None):
    def pos(p):
        return tuple(x % length for x in p) if length else tuple(p)
    q = {pos(p): v for p, v in raw[0]}
    e = {(pos(edge[0]), pos(edge[1])): v for edge, v in raw[1]}
    assert len(q) == len(raw[0]) and len(e) == len(raw[1])
    return key(q, e)


def encode(k):
    return [list(k[0]), list(k[1])]


class Torus:
    def __init__(self, length):
        assert length >= 8 and length % 2 == 0
        self.length = length
        self.vertices = tuple(product(range(length), repeat=3))
        self.a_sites = tuple(p for p in self.vertices if parity(p) == 0)
        self.b_sites = tuple(p for p in self.vertices if parity(p) == 1)
        self.neighbors = {}
        for p in self.vertices:
            nbrs = []
            for axis in range(3):
                for sign in (-1, 1):
                    q = list(p)
                    q[axis] = (q[axis] + sign) % length
                    nbrs.append(tuple(q))
            assert len(set(nbrs)) == 6
            self.neighbors[p] = tuple(sorted(nbrs))
        self.edges = tuple((a, b) for a in self.a_sites for b in self.neighbors[a])
        pairs = set()
        for b in self.b_sites:
            pairs.update(combinations(self.neighbors[b], 2))
        self.pairs = tuple(sorted(pairs))
        assert len(self.pairs) == 9 * len(self.a_sites)
        assert len(self.edges) == 3 * length**3

    def check(self, k):
        q, e = map(dict, k)
        div = Counter()
        for (a, b), value in e.items():
            assert parity(a) == 0 and parity(b) == 1
            assert b in self.neighbors[a]
            div[a] += value
            div[b] -= value
        failures = []
        for p in self.vertices:
            charge = q.get(p, baseline(p))
            assert charge in (-1, 0, 1)
            defect = div[p] - (charge - baseline(p))
            if defect:
                failures.append([p, defect])
        costs = []
        total = 0
        for a, b in self.edges:
            charge = q.get(a, 1)
            if q.get(b, 0) == 0:
                value = e.get((a, b), 0)
                cost = value * (value - charge)
                assert cost >= 0
                total += cost
                if cost:
                    costs.append({'edge': [a, b], 'E': value,
                                  'q_a': charge, 'cost': cost})
        vacancies = [p for p in self.a_sites if q.get(p, 1) == 0]
        return {'gauss_failures': failures, 'D': total, 'D_terms': costs,
                'a_vacancies': vacancies,
                'records_over_background': sum(abs(q.get(p, baseline(p))) - baseline(p)
                                               for p in self.vertices),
                'charge_over_background': sum(q.get(p, baseline(p)) - baseline(p)
                                              for p in self.vertices)}

    def two_hole(self, k, a, c):
        """Construct both outward hops simultaneously, without hop composition."""
        q, e = map(dict, k)
        qa, qc = q.get(a, 1), q.get(c, 1)
        assert qa and qc
        out = Counter()
        routes = defaultdict(list)
        empty_a = [b for b in self.neighbors[a] if q.get(b, 0) == 0]
        empty_c = [d for d in self.neighbors[c] if q.get(d, 0) == 0]
        for b in empty_a:
            for d in empty_c:
                if b == d:
                    continue
                oq = dict(q)
                oe = dict(e)
                oq.update({a: 0, c: 0, b: qa, d: qc})
                oe[a, b] = e.get((a, b), 0) - qa
                oe[c, d] = e.get((c, d), 0) - qc
                k_out = key(oq, oe)
                out[k_out] += 1
                routes[k_out].append([a, b, c, d])
        return out, routes

    def fixed_birth(self, k, a, b, sigma):
        """Original resolved B_(a,b,sigma)=P j_(a,b,sigma) F_a P."""
        q, e = map(dict, k)
        qa = q.get(a, 1)
        assert qa and q.get(b, 0) == 0 and sigma in (-1, 1)
        assert a in self.a_sites and b in self.neighbors[a]
        out = Counter()
        routes = defaultdict(list)
        for d in self.neighbors[a]:
            if d == b or q.get(d, 0):
                continue
            oq, oe = dict(q), dict(e)
            oq.update({a: sigma, b: -sigma, d: qa})
            oe[a, d] = e.get((a, d), 0) - qa
            oe[a, b] = e.get((a, b), 0) + sigma
            k_out = key(oq, oe)
            out[k_out] += 1
            routes[k_out].append(d)
        return out, routes

