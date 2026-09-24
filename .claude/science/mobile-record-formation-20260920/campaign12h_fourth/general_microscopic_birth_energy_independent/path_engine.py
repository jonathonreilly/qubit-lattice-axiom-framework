"""Independent local path engine written for microscopic-moment reconstruction.

No campaign builder is imported. Symbolic and numerical amplitudes share only
these directly specified charge/link actions. Full small-matrix controls use
an independently assembled tensor-product site basis in matrix_control.py.
"""
from collections import defaultdict
from itertools import combinations
import sympy as sp


class Graph:
    def __init__(self, n, A, edges):
        self.n, self.A = n, tuple(sorted(A))
        self.edges = tuple(sorted(tuple(sorted(e)) for e in edges))
        self.edge_index = {e: i for i, e in enumerate(self.edges)}
        self.adj = {a: tuple(b for b in range(n) if tuple(sorted((a,b))) in self.edge_index)
                    for a in range(n)}

    def gauss(self, state):
        q, E = state
        div = [0]*self.n
        for (x,y), e in zip(self.edges, E):
            div[x] += e
            div[y] -= e
        return all(sp.simplify(div[x]-q[x]+int(x in self.A)) == 0 for x in range(self.n))

    def initial(self, flux=None):
        return (tuple(int(x in self.A) for x in range(self.n)),
                tuple((flux or {}).get(e, 0) for e in self.edges))

    def spin_weight(self, electric, shift, C=None, S=None):
        if S is not None and abs(electric+shift)>S:
            return 0
        return sp.Integer(1) if C is None else sp.sqrt(1-electric*(electric+shift)/C)

    def hop(self, state, source, destination, C=None, S=None):
        q,E = state
        if not q[source] or q[destination]:
            return []
        e = self.edge_index[tuple(sorted((source,destination)))]
        shift = -q[source] if source<destination else q[source]
        weight = self.spin_weight(E[e], shift, C, S)
        if weight == 0:
            return []
        q2,E2=list(q),list(E)
        q2[destination],q2[source]=q2[source],0
        E2[e]+=shift
        return [((tuple(q2),tuple(E2)),weight)]

    def outward(self, state, C=None, S=None, center=None):
        answer=[]
        for a in self.A if center is None else (center,):
            for b in self.adj[a]:
                answer.extend(self.hop(state,a,b,C,S))
        return answer

    def inward(self, state, C=None, S=None, center=None):
        answer=[]
        for a in self.A if center is None else (center,):
            for b in self.adj[a]:
                answer.extend(self.hop(state,b,a,C,S))
        return answer

    def birth(self, state, edge, sign_at_A, C=None, S=None):
        q,E=state
        x,y=self.edges[edge]
        if q[x] or q[y]:
            return []
        answer=[]
        for sigma in (-1,1) if sign_at_A is None else (sign_at_A,):
            sign_lower=sigma if x in self.A else -sigma
            weight=self.spin_weight(E[edge], sign_lower,C,S)
            if weight==0:
                continue
            q2,E2=list(q),list(E)
            q2[x],q2[y]=sign_lower,-sign_lower
            E2[edge]+=sign_lower
            answer.append(((tuple(q2),tuple(E2)),weight))
        return answer

    def electric_D(self,state):
        q,E=state
        value=0
        for a in self.A:
            if not q[a]:
                continue
            for b in self.adj[a]:
                if q[b]:
                    continue
                i=self.edge_index[tuple(sorted((a,b)))]
                k=-q[a] if a<b else q[a]
                value+=E[i]*(E[i]+k)
        return sp.expand(value)

    def grade(self,state):
        return sum(state[0][a]==0 for a in self.A)


def apply(vector, action):
    result=defaultdict(lambda:sp.Integer(0))
    for state,coefficient in vector.items():
        for target,weight in action(state):
            result[target]+=coefficient*weight
    return {s:sp.simplify(v) for s,v in result.items() if sp.simplify(v)!=0}


def add(*terms):
    result=defaultdict(lambda:sp.Integer(0))
    for coefficient,vector in terms:
        for state,value in vector.items():
            result[state]+=coefficient*value
    return {s:sp.simplify(v) for s,v in result.items() if sp.simplify(v)!=0}


def inner(left,right):
    return sp.simplify(sum(sp.conjugate(value)*right.get(state,0) for state,value in left.items()))


def norm2(vector):
    return inner(vector,vector)


def cube():
    return Graph(8,(0,3,5,6),[(x,y) for x in range(8) for y in range(x+1,8) if (x^y).bit_count()==1])


def ring(n):
    assert n>=4 and n%2==0
    return Graph(n,range(0,n,2),[(x,(x+1)%n) for x in range(n)])


def circulation(graph,cycle,n):
    flux={}
    for x,y in zip(cycle,cycle[1:]+cycle[:1]):
        flux[tuple(sorted((x,y)))]=n if x<y else -n
    return flux


def birth_coefficients(graph,state,edge,sign,C=None,S=None):
    x={state:sp.Integer(1)}
    F=lambda v:apply(v,lambda s:graph.outward(s,C,S))
    j=lambda v:apply(v,lambda s:graph.birth(s,edge,sign,C,S))
    Fg=F(x)
    B=j(Fg)
    jZ=j(F(Fg))
    FB=F(B)
    R=add((sp.Rational(1,2),jZ),(-1,FB))
    a=next(x for x in graph.edges[edge] if x in graph.A)
    center=apply(B,lambda s:graph.outward(s,C,S,center=a))
    return B,R,center
