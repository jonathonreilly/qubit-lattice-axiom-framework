#!/usr/bin/env python3
"""Exact, author-code-free checks. Sparse action, not a dense K matrix.

The theorem is proved in ANALYTIC_FINDINGS.md. These finite algebra fixtures
challenge its load-bearing identities; they are not simulations of a routed bus.
"""
from fractions import Fraction as F
from collections import defaultdict
import json


class Q:
    __slots__ = ('r', 'i')
    def __init__(self, r=0, i=0):
        if isinstance(r, Q):
            self.r, self.i = r.r, r.i
        else:
            self.r, self.i = F(r), F(i)
    def __add__(self, other):
        o = Q(other)
        return Q(self.r + o.r, self.i + o.i)
    __radd__ = __add__
    def __neg__(self):
        return Q(-self.r, -self.i)
    def __sub__(self, other):
        return self + (-Q(other))
    def __rsub__(self, other):
        return Q(other) + (-self)
    def __mul__(self, other):
        o = Q(other)
        return Q(self.r*o.r-self.i*o.i, self.r*o.i+self.i*o.r)
    __rmul__ = __mul__
    def __truediv__(self, other):
        if isinstance(other, Q):
            raise TypeError('Only real division is needed in this checker')
        return Q(self.r/F(other), self.i/F(other))
    def conj(self):
        return Q(self.r, -self.i)
    def __eq__(self, other):
        o = Q(other)
        return self.r == o.r and self.i == o.i
    def __bool__(self):
        return bool(self.r or self.i)
    def record(self):
        return [str(self.r), str(self.i)]


def matmul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def plus_scalar(a, x):
    return [[a[i][j]+(x if i == j else 0) for j in range(len(a))]
            for i in range(len(a))]


def sub(a, b):
    return [[x-y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def is_zero(a):
    return all(not x for row in a for x in row)


def bit(x, p):
    return (x >> p) & 1


def add(out, x, y):
    out[x] = out.get(x, Q()) + y


def gram(left, right, norm):
    return [[sum(v.conj()*right[j].get(x, Q())
                 for x, v in left[i].items())/norm
             for j in range(len(right))] for i in range(len(left))]


def old_matrices():
    # Two old qubits. H = X0/2 + Y0 Z1/3 + 2 Z0 X1/5 + 7 Z1/11.
    h = [[Q() for _ in range(4)] for _ in range(4)]
    b = [[Q() for _ in range(4)] for _ in range(4)]
    for x in range(4):
        z0, z1 = 1-2*bit(x, 0), 1-2*bit(x, 1)
        h[x][x] += F(7, 11)*z1
        h[x ^ 1][x] += Q(F(1, 2), F(z0*z1, 3))
        h[x ^ 2][x] += F(2, 5)*z0
        b[x][x] = Q(F(1, 2)+F(z0, 3))
    assert all(h[i][j] == h[j][i].conj() for i in range(4) for j in range(4))
    b2 = matmul(b, b)
    assert not is_zero(sub(matmul(h, b2), matmul(b2, h)))
    return h, b, b2


def occupation_recurrence(n):
    # Count bitstrings by (number, adjacent occupied bonds, last bit).
    counts = {(0, 0, 0): 1, (1, 0, 1): 1}
    for _ in range(1, n):
        new = defaultdict(int)
        for (k, d, last), count in counts.items():
            for nxt in (0, 1):
                new[k+nxt, d+last*nxt, nxt] += count
        counts = new
    assert sum(counts.values()) == 2**n
    def mean(fn):
        return sum((fn(k, d)*c for (k, d, _), c in counts.items()), F()) / 2**n
    mk, md = mean(lambda k, d: k), mean(lambda k, d: d)
    vk, vd = mean(lambda k, d: k*k)-mk*mk, mean(lambda k, d: d*d)-md*md
    cov = mean(lambda k, d: k*d)-mk*md
    ms = mean(lambda k, d: F(k*(k-1), n))
    vs = mean(lambda k, d: F(k*(k-1), n)**2)-ms*ms
    assert (mk, md, vk, vd, cov) == (
        F(n, 2), F(n-1, 4), F(n, 4), F(5*n-7, 16), F(n-1, 4))
    assert md == ms and vd-vs == F((n-2)*(n+1), 16*n)
    if n >= 3:
        assert vd != F(3*(n-1), 16)  # Mutant drops adjacent-bond covariance.
    return {'N': n, 'variance_D': str(vd), 'off_code_square': str(vd-vs),
            'count_states': len(counts)}


def release_fixture(q, n):
    h, b, b2 = old_matrices()
    xi, vp, bnorm = F(2, 9), F(3, 5), F(5, 6)
    bus = list(range(2, 2+q+1))
    source = [list(range(3+q+l*n, 3+q+(l+1)*n)) for l in range(q)]
    omega = [F(2*l+3, 5) for l in range(q)]
    u = [F((-1)**(l+1)*(l+2), 7) for l in range(q)]
    v = [F((-1)**l*(l+3), 11) for l in range(q)]
    jf = [F(l+3, 17) for l in range(q)]
    r = [F(l+2, 13) for l in range(q)]
    t = [F((-1)**l*(l+1), 19) for l in range(q)]
    onsite = [F(2*l+5, 7) for l in range(q+1)]
    phase = [Q(0, 1), Q(-1), Q(0, -1)][:q]
    # Exact physical reserves from the declared positive blocks. R_s=3 bounds H.
    reserve = (F(3)+sum(abs(x) for x in t)+xi*(vp*bnorm+sum(r))
               +xi*xi*sum(n*max(0, -u[l])+(n-1)*max(0, -v[l]) for l in range(q)))
    c0 = (F(3)+sum(onsite)+2*sum(abs(x) for x in t)
          +sum(n*omega[l]+2*(n-1)*jf[l] for l in range(q))
          +2*xi*(vp*bnorm+sum(r))
          +xi*xi*sum(n*abs(u[l])+(n-1)*abs(v[l]) for l in range(q)))
    columns = []
    for old in range(4):
        col = {}
        for bits in range(2**(q*n)):
            x, a = old, Q(1)
            for l in range(q):
                for j, p in enumerate(source[l]):
                    if bit(bits, l*n+j):
                        x |= 1 << p
                        a *= phase[l]
            col[x] = a
        columns.append(col)

    def act(col, compressed_density=False):
        out = {}
        for x, amp in col.items():
            old = x & 3
            for y in range(4):
                add(out, (x & ~3) | y, h[y][old]*amp)
            diag = reserve+sum(onsite[l]*bit(x, p) for l, p in enumerate(bus))
            for l, sites in enumerate(source):
                k = sum(bit(x, p) for p in sites)
                d = (F(k*(k-1), n) if compressed_density else
                     sum(bit(x, a)*bit(x, z) for a, z in zip(sites, sites[1:])))
                diag += (omega[l]+xi*xi*u[l])*k+xi*xi*v[l]*d
                for a, z in zip(sites, sites[1:]):
                    add(out, x, jf[l]*amp)
                    y = x ^ ((1 << a) | (1 << z)) if bit(x, a) != bit(x, z) else x
                    add(out, y, -jf[l]*amp)
            add(out, x, diag*amp)
            for l, coeff in enumerate(t):
                a, z = bus[l], bus[l+1]
                if bit(x, a) != bit(x, z):
                    add(out, x ^ ((1 << a) | (1 << z)), coeff*amp)
            for y in range(4):
                target = ((x & ~3) | y) ^ (1 << bus[0])
                add(out, target, xi*vp*b[y][old]*amp)
            for l, sites in enumerate(source):
                a, z = bus[l+1], sites[0]
                if bit(x, a) != bit(x, z):
                    add(out, x ^ ((1 << a) | (1 << z)), xi*r[l]*amp)
        return {x: a for x, a in out.items() if a}

    kc = [act(col) for col in columns]
    mutant = [act(col, True) for col in columns]
    norm = 2**(q*n)
    first, second = gram(columns, kc, norm), gram(kc, kc, norm)
    mutant_first, mutant_second = gram(columns, mutant, norm), gram(mutant, mutant, norm)
    mu, var = [], []
    for l in range(q):
        a, beta = omega[l]+xi*xi*u[l], xi*xi*v[l]
        mu.append(a*F(n, 2)+beta*F(n-1, 4))
        var.append(a*a*F(n, 4)+beta*beta*F(5*n-7, 16)+a*beta*F(n-1, 2))
    c = reserve+sum(mu)
    want_first = plus_scalar(h, c)
    want_second = plus_scalar(matmul(want_first, want_first), sum(var)+xi*xi*sum(x*x for x in r)/2)
    want_second = [[want_second[i][j]+xi*xi*vp*vp*b2[i][j]
                    for j in range(4)] for i in range(4)]
    assert is_zero(sub(first, want_first))
    assert is_zero(sub(second, want_second))
    assert is_zero(sub(mutant_first, first))
    loss = sum((xi*xi*x)**2*F((n-2)*(n+1), 16*n) for x in v)
    assert all(second[i][j]-mutant_second[i][j] == (loss if i == j else 0)
               for i in range(4) for j in range(4))
    assert (loss > 0) == (n >= 3)
    # Direct A action: remove the old H contribution, not a code projection.
    ac = []
    for k in range(4):
        col = dict(kc[k])
        for j in range(4):
            for x, amp in columns[j].items():
                add(col, x, -h[j][k]*amp)
        ac.append({x: a for x, a in col.items() if a})
    a2 = gram(ac, ac, norm)
    scalar = c*c+sum(var)+xi*xi*sum(x*x for x in r)/2
    want_a2 = [[xi*xi*vp*vp*b2[i][j]+(scalar if i == j else 0)
                for j in range(4)] for i in range(4)]
    assert is_zero(sub(a2, want_a2))
    g2 = scalar+xi*xi*vp*vp*bnorm*bnorm
    assert g2 <= c0*c0
    assert not is_zero(sub(second, matmul(first, first)))
    return {'sources': q, 'N': n, 'full_qubits': 3+q+q*n,
            'old_dimension': 4, 'max_KJ_support': max(map(len, kc)),
            'source_phases': [x.record() for x in phase],
            'full_second_minus_compressed_second_diagonal': str(loss),
            'G_squared': str(g2), 'C0_squared': str(c0*c0),
            'noncommuting_H_B2': True}


def swap_and_phase():
    # Exhaustive basis check: D=2 qubits, C=2, R=1, E=2, initially E=00.
    # Basis coverage proves the embedding identity, including all coherences.
    for d in range(4):
        for c in range(4):
            for r in range(2):
                before = d | (c << 2) | (r << 4)
                after = before
                for cp, ep in ((2, 5), (3, 6)):
                    if bit(after, cp) != bit(after, ep):
                        after ^= (1 << cp) | (1 << ep)
                assert after == d | (r << 4) | (c << 5)
    phase = Q(F(3, 5), F(4, 5))
    # Remove the common exp(-i pi/4)/sqrt(2) from the rotation identity.
    yphi_on_zero = [Q(), Q(0, 1)*phase]
    correct = [Q(1)-Q(0, 1)*yphi_on_zero[0], -Q(0, 1)*yphi_on_zero[1]]
    assert correct == [Q(1), phase]
    assert correct != [Q(1), phase.conj()]
    return {'full_swap_basis_inputs': 32, 'rotation_phase': phase.record(),
            'inverse_phase_mutant_rejected': True}


def main():
    recurrence = [occupation_recurrence(n) for n in range(2, 41)]
    fixtures = [release_fixture(q, n) for q, n in
                [(1, 2), (1, 3), (1, 4), (1, 6), (1, 8),
                 (2, 2), (2, 3), (2, 4), (3, 2), (3, 3)]]
    print(json.dumps({'arithmetic': 'Python Fraction Gaussian rationals; no external packages',
                      'occupation_recurrence': recurrence,
                      'release_fixtures': fixtures,
                      'swap_and_rotation': swap_and_phase(),
                      'author_code_imported': False,
                      'limits': 'Finite algebra fixtures; no full routed-bus evolution, no pulse propagation, no microscopic drive.'}, indent=2))


if __name__ == '__main__':
    main()
