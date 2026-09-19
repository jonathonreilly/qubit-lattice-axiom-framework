#!/usr/bin/env python3
"""J:attack-g:PR8180 — brute-force T1's identification of the two C_s formulas.

T1 (note, as written): for every mode k,
  Cov(theta_k(t), theta_k(t+s)) = phi(k)^s Var(theta_k(t))
with phi(k) = (1 + exp(i k1) + exp(i k2))/3 the multiplier of the recursion
theta_{t+1} = P theta_t + xi, P the average over the three predecessors, and
  C_s = sigma^2 (I - P P*)^{-1} P*^s
as an operator on the plane (P* = P^T on the real torus).  The two displays
are equated by 'i.e.'.  Executed in the note/runner only on cosine characters,
where Re(phi^s) = Re(conj(phi)^s) so conjugation is invisible.

This script enumerates the L=3 torus (the note's tiny-torus size) in the field
Q(i sqrt(3)): Fourier mode f_x = exp(-i k.x) of the recursion (P f = phi f),
exact rational P and Sigma_t = P Sigma_{t-1} P^T + I from theta_0 = 0, and the
Rayleigh quotient of Sigma_t (P^T)^s against phi^s and conj(phi)^s.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product


class Z:
    """a + i b sqrt(3), a,b Fraction. Closed under +, *, conj; |omega|=1."""

    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a = F(a)
        self.b = F(b)

    def __add__(self, o):
        o = o if isinstance(o, Z) else Z(o)
        return Z(self.a + o.a, self.b + o.b)

    def __sub__(self, o):
        o = o if isinstance(o, Z) else Z(o)
        return Z(self.a - o.a, self.b - o.b)

    def __mul__(self, o):
        o = o if isinstance(o, Z) else Z(o)
        # (a + i b√3)(c + i d√3) = (ac - 3 bd) + i (ad + bc) √3
        return Z(self.a * o.a - 3 * self.b * o.b, self.a * o.b + self.b * o.a)

    def __rmul__(self, o):
        return self * o

    def __truediv__(self, o):
        o = o if isinstance(o, Z) else Z(o)
        den = o.a * o.a + 3 * o.b * o.b
        return Z((self.a * o.a + 3 * self.b * o.b) / den, (self.b * o.a - self.a * o.b) / den)

    def conj(self):
        return Z(self.a, -self.b)

    def __pow__(self, n):
        n = int(n)
        if n == 0:
            return Z(1)
        if n < 0:
            return Z(1) / (self ** (-n))
        r = Z(1)
        b = self
        while n:
            if n & 1:
                r = r * b
            b = b * b
            n >>= 1
        return r

    def __eq__(self, o):
        o = o if isinstance(o, Z) else Z(o)
        return self.a == o.a and self.b == o.b

    def __repr__(self):
        return f"({self.a} + {self.b}*i*sqrt(3))"


def omega():
    # exp(2 pi i / 3) = -1/2 + i sqrt(3)/2
    return Z(F(-1, 2), F(1, 2))


def idx(L, i, j):
    return (i % L) * L + (j % L)


def build_P(L):
    N = L * L
    P = [[F(0) for _ in range(N)] for _ in range(N)]
    for i, j in product(range(L), repeat=2):
        s = idx(L, i, j)
        for di, dj in ((0, 0), (-1, 0), (0, -1)):
            P[s][idx(L, i + di, j + dj)] += F(1, 3)
    return P


def matT(A):
    n = len(A)
    return [[A[j][i] for j in range(n)] for i in range(n)]


def matmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def matadd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def eye(n):
    return [[F(1 if i == j else 0) for j in range(n)] for i in range(n)]


def zeros(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def fourier_mode(L, n1, n2):
    """f_x = exp(-i k.x), k = 2 pi (n1, n2)/L, as Z-values. L=3 only."""
    w = omega()
    # w^{n} = exp(2 pi i n / 3); exp(-i k.x) = w^{-(n1 i + n2 j)}
    return [w ** (-(n1 * i + n2 * j)) for i in range(L) for j in range(L)]


def phi_of(n1, n2):
    """phi(k) = (1 + exp(i k1) + exp(i k2))/3 with k = 2 pi (n1,n2)/3."""
    w = omega()
    return (Z(1) + w ** n1 + w ** n2) / 3


def rayleigh(M, f):
    """(f^H M f) / (f^H f) with M real-Fraction, f a list of Z."""
    n = len(f)
    num = Z(0)
    den = Z(0)
    for x in range(n):
        den = den + f[x].conj() * f[x]
        acc = Z(0)
        row = M[x]
        for y in range(n):
            acc = acc + row[y] * f[y]
        num = num + f[x].conj() * acc
    return num / den


def cosine_vec(L, n1, n2):
    # cos(2 pi (n1 i + n2 j)/L) as Fraction; L=3 table
    table = {0: F(1), 1: F(-1, 2), 2: F(-1, 2)}
    return [table[(n1 * i + n2 * j) % L] for i in range(L) for j in range(L)]


def quad(c, M):
    n = len(c)
    s = F(0)
    for x in range(n):
        acc = F(0)
        row = M[x]
        for y in range(n):
            acc += row[y] * c[y]
        s += c[x] * acc
    return s


def main():
    L = 3
    N = L * L
    T, smax = 6, 3
    P = build_P(L)
    PT = matT(P)
    I = eye(N)
    Pp = [eye(N)]
    for s in range(1, smax + 1):
        Pp.append(matmul(P, Pp[-1]))
    PTp = [eye(N)]
    for s in range(1, smax + 1):
        PTp.append(matmul(PT, PTp[-1]))

    modes = [(n1, n2) for n1, n2 in product(range(L), repeat=2) if (n1, n2) != (0, 0)]
    n_op_is_conj = 0
    n_op_is_phi = 0
    n_cos_ok = 0
    n_pf = 0
    witnesses = []

    Sigma = zeros(N)
    for t in range(1, T + 1):
        Sigma = matadd(matmul(matmul(P, Sigma), PT), I)
        for n1, n2 in modes:
            f = fourier_mode(L, n1, n2)
            phi = phi_of(n1, n2)
            # P f = phi f  (the note's multiplier)
            lam_P = rayleigh(P, f)
            lam_PT = rayleigh(PT, f)
            if lam_P == phi:
                n_pf += 1
            var = rayleigh(Sigma, f)
            c = cosine_vec(L, n1, n2)
            var_c = quad(c, Sigma)
            for s in range(1, smax + 1):
                Cs = matmul(Sigma, PTp[s])  # Sigma (P^s)^T  as written
                ratio = rayleigh(Cs, f) / var
                is_phi = ratio == (phi ** s)
                is_conj = ratio == (phi.conj() ** s)
                if is_conj:
                    n_op_is_conj += 1
                if is_phi:
                    n_op_is_phi += 1
                if not is_phi:
                    witnesses.append(
                        (
                            t,
                            s,
                            n1,
                            n2,
                            phi ** s,
                            phi.conj() ** s,
                            ratio,
                            lam_P,
                            lam_PT,
                        )
                    )
                if var_c != 0:
                    cov_c = quad(c, Cs)
                    # Re(phi^s) = a of (phi^s) written as a + i b sqrt(3)
                    re = (phi ** s).a
                    if cov_c / var_c == re:
                        n_cos_ok += 1

    n_ratio = T * smax * len(modes)
    print(f"L=3 modes={len(modes)} t=1..{T} s=1..{smax}  ratio-slots={n_ratio}")
    print(f"P f = phi f on every (mode,t) check: {n_pf}/{T * len(modes)}")
    print(f"Sigma (P^s)^T Rayleigh / Var  == phi^s : {n_op_is_phi}/{n_ratio}")
    print(f"Sigma (P^s)^T Rayleigh / Var  == conj(phi)^s : {n_op_is_conj}/{n_ratio}")
    print(f"cosine Cov/Var == Re(phi^s) : {n_cos_ok}/{n_ratio}")

    # one exact witness
    t, s, n1, n2, phs, cphs, ratio, lam_P, lam_PT = witnesses[0]
    print(
        f"witness: t={t} s={s} k=2pi({n1},{n2})/3  "
        f"phi^s={phs}  conj(phi)^s={cphs}  operator-ratio={ratio}"
    )
    print(f"  P-multiplier={lam_P}  P^T-multiplier={lam_PT}")

    if n_op_is_phi != n_ratio and n_op_is_conj == n_ratio:
        print(
            "HIT: T1 equates C_s(k)=sigma^2 phi(k)^s/(1-|phi|^2) with the operator "
            "C_s=sigma^2 (I-PP*)^{-1} P*^s; on the L=3 torus, for every nonzero mode "
            "and every t<=6, s<=3, the Rayleigh quotient of the written real-space "
            "identity Sigma_t (P^s)^T on the Fourier mode of the recursion (P f = phi f) "
            f"is conj(phi)^s, not phi^s ({n_op_is_conj}/{n_ratio} slots). "
            "The runner's cosine check is blind to this (Re(phi^s)=Re(conj(phi)^s); "
            f"cosine identity held in {n_cos_ok}/{n_ratio} slots)."
        )
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on T1's identification of the mode "
            "kernel phi^s/(1-|phi|^2) with (I-PP*)^{-1} P*^s (PR #8180): the two "
            "formulas differ by complex conjugation on every nonzero mode of the L=3 "
            "torus (exact Q(i sqrt(3))); cosine characters hide it."
        )
    elif n_op_is_phi == n_ratio:
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on T1's identification of the mode "
            "kernel with (I-PP*)^{-1} P*^s (PR #8180): holds on L=3, t<=6, s<=3 for "
            "every nonzero Fourier mode; pattern has purchase and the step holds as written"
        )
    else:
        print(
            "HIT: T1 mode/operator identification matches neither phi^s nor conj(phi)^s "
            f"uniformly (phi {n_op_is_phi}/{n_ratio}, conj {n_op_is_conj}/{n_ratio})"
        )
        print(
            "SUMMARY: PROOF STEP BY BRUTE FORCE on T1's C_s identification (PR #8180): "
            "the L=3 Rayleigh quotients of Sigma (P^s)^T match neither written formula uniformly"
        )


if __name__ == "__main__":
    main()
