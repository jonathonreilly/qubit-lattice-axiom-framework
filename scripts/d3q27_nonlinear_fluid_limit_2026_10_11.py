#!/usr/bin/env python3
"""Exact author checks for supplied D3Q27 nonlinear-fluid correctors.

Standard library, deterministic, no repository imports or external inputs.
The primary discriminator constructs actual Fourier/time jets of an advected
shear and thermal wave, solves the full 27-velocity Poisson problem, and
evaluates the nonlinear residual at rational deltas. This finite certificate
is not a PDE convergence proof, physical identification, or audit verdict.
"""
from fractions import Fraction as F
from itertools import combinations, product
from time import perf_counter
from pathlib import Path
from hashlib import sha256
import sys

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = [
    'docs/D3Q27_NONLINEAR_FLUID_LIMIT_BOUNDED_THEOREM_NOTE_2026-10-11.md',
    'docs/D3Q27_DISSIPATIVE_HYDRODYNAMIC_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-10-09.md',
]


class QA:
    """Exact Q[alpha]/(536 alpha^2+4579 alpha-22183)."""
    __slots__ = ('a', 'b')
    u, v = F(22183, 536), F(-4579, 536)

    def __init__(self, a=0, b=0):
        if isinstance(a, QA):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = F(a), F(b)

    def __bool__(self):
        return bool(self.a or self.b)

    def __add__(self, other):
        q = QA(other)
        return QA(self.a + q.a, self.b + q.b)

    __radd__ = __add__

    def __neg__(self):
        return QA(-self.a, -self.b)

    def __sub__(self, other):
        return self + -QA(other)

    def __rsub__(self, other):
        return QA(other) + -self

    def __mul__(self, other):
        q = QA(other)
        return QA(self.a * q.a + self.b * q.b * self.u,
                  self.a * q.b + self.b * q.a + self.b * q.b * self.v)

    __rmul__ = __mul__

    def __truediv__(self, other):
        q = QA(other)
        norm = q.a * q.a + q.a * q.b * self.v - q.b * q.b * self.u
        return self * QA((q.a + q.b * self.v) / norm, -q.b / norm)

    def __eq__(self, other):
        q = QA(other)
        return (self.a, self.b) == (q.a, q.b)


def tuned_response_check(V, energies, M, reactions, axial_indices, K):
    """All eight Poisson sources at alpha_*, using the full collision map."""
    alpha = QA(0, 1)
    assert 536 * alpha * alpha + 4579 * alpha - 22183 == 0
    assert 536 + 4579 - 22183 < 0 < 536 * 16 + 4579 * 4 - 22183

    def B(phi, omit=None):
        out = [QA() for _ in V]
        for n, (i, j, k, l) in enumerate(reactions):
            if n == omit:
                continue
            rate = alpha if n in axial_indices else QA(1)
            flux = rate * M[i] * M[j] * (phi[k] + phi[l] - phi[i] - phi[j])
            for q, sign in ((i, -1), (j, -1), (k, 1), (l, 1)):
                out[q] = out[q] + sign * flux / M[q]
        return out

    def inner(a, b):
        return sum((m * x * y for m, x, y in zip(M, a, b)), QA())

    def solve(phi):
        bp = B(phi)
        bbp = B(bp)
        for i, j in combinations(range(27), 2):
            det = bp[i] * bbp[j] - bp[j] * bbp[i]
            if det:
                a = (phi[i] * bbp[j] - phi[j] * bbp[i]) / det
                b = (bp[i] * phi[j] - bp[j] * phi[i]) / det
                answer = [a * x + b * y for x, y in zip(phi, bp)]
                assert B(answer) == list(map(QA, phi))
                assert all(inner(inv, answer) == 0 for inv in K)
                return answer
        raise AssertionError('Missing rank-two Krylov minor')

    sources = [[F(v[0] ** 2 - v[1] ** 2, 2) for v in V],
               [F(v[1] ** 2 - v[2] ** 2, 2) for v in V],
               *[[F(v[a] * v[b]) for v in V] for a, b in ((0, 1), (0, 2), (1, 2))],
               *[[v[a] * (F(e) - F(5, 3)) for v, e in zip(V, energies)] for a in range(3)]]
    response = [solve(phi) for phi in sources]
    mu, chi = F(67, 1083), F(40, 441)
    for i in range(8):
        for j in range(8):
            target = mu if i == j and i < 5 else chi if i == j else 0
            if {i, j} == {0, 1}:
                target = -mu / 2
            assert inner(sources[i], response[j]) == target
    assert any(B(response[0], omit=n) != list(map(QA, sources[0])) for n in axial_indices)
    print('tuned alpha_*: full 27-component Krylov Poisson solves for 5 stresses and 3 heat sources; all 64 responses exact in Q(alpha); missing axial reaction rejected')


class QC:
    """Exact rational complex number."""
    __slots__ = ('re', 'im')

    def __init__(self, re=0, im=0):
        if isinstance(re, QC):
            self.re, self.im = re.re, re.im
        else:
            self.re, self.im = F(re), F(im)

    def __bool__(self):
        return bool(self.re or self.im)

    def __add__(self, other):
        if isinstance(other, QC):
            return QC(self.re + other.re, self.im + other.im)
        return QC(self.re + other, self.im)

    __radd__ = __add__

    def __neg__(self):
        return QC(-self.re, -self.im)

    def __sub__(self, other):
        return self + -QC(other)

    def __rsub__(self, other):
        return QC(other) + -self

    def __mul__(self, other):
        if isinstance(other, QC):
            return QC(self.re * other.re - self.im * other.im,
                      self.re * other.im + self.im * other.re)
        return QC(self.re * other, self.im * other)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, QC):
            d = other.re * other.re + other.im * other.im
            return QC((self.re * other.re + self.im * other.im) / d,
                      (self.im * other.re - self.re * other.im) / d)
        return QC(self.re / other, self.im / other)

    def __eq__(self, other):
        q = QC(other)
        return self.re == q.re and self.im == q.im

    def conj(self):
        return QC(self.re, -self.im)

    def __repr__(self):
        return f'({self.re},{self.im})'


ZERO_MODE = (0, 0, 0)


class Fourier:
    """Finite Fourier series on the 2pi torus, exact Q(i) coefficients."""
    __slots__ = ('d',)

    def __init__(self, value=0):
        if isinstance(value, Fourier):
            self.d = value.d.copy()
        elif isinstance(value, dict):
            self.d = {k: QC(v) for k, v in value.items() if v}
        else:
            self.d = {ZERO_MODE: QC(value)} if value else {}

    def __bool__(self):
        return bool(self.d)

    def __add__(self, other):
        other = Fourier(other)
        d = self.d.copy()
        for k, x in other.d.items():
            d[k] = d.get(k, QC()) + x
            if not d[k]:
                del d[k]
        return Fourier(d)

    __radd__ = __add__

    def __neg__(self):
        return Fourier({k: -x for k, x in self.d.items()})

    def __sub__(self, other):
        return self + -Fourier(other)

    def __rsub__(self, other):
        return Fourier(other) + -self

    def __mul__(self, other):
        if not isinstance(other, Fourier):
            return Fourier({k: x * other for k, x in self.d.items()})
        d = {}
        for k, x in self.d.items():
            for l, y in other.d.items():
                kl = tuple(a + b for a, b in zip(k, l))
                d[kl] = d.get(kl, QC()) + x * y
        return Fourier(d)

    __rmul__ = __mul__

    def __truediv__(self, other):
        return self * (1 / F(other))

    def __eq__(self, other):
        return self.d == Fourier(other).d

    def derivative(self, a):
        return Fourier({k: QC(0, k[a]) * x for k, x in self.d.items() if k[a]})

    def laplacian(self):
        return Fourier({k: -sum(a * a for a in k) * x for k, x in self.d.items()})

    def mean(self):
        return self.d.get(ZERO_MODE, QC())

    def remove_mean(self):
        return self - self.mean()

    def real(self):
        return all(self.d.get(tuple(-a for a in k), QC()) == x.conj()
                   for k, x in self.d.items())


def sin_mode(k):
    return Fourier({k: QC(0, F(-1, 2)), tuple(-a for a in k): QC(0, F(1, 2))})


def cos_mode(k):
    return Fourier({k: F(1, 2), tuple(-a for a in k): F(1, 2)})


def mm(a, b):
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def inverse(a):
    n = len(a)
    x = [[F(y) for y in row] + [F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for p in range(n):
        q = next(q for q in range(p, n) if x[q][p])
        x[p], x[q] = x[q], x[p]
        pivot = x[p][p]
        x[p] = [y / pivot for y in x[p]]
        for q in range(n):
            if q == p:
                continue
            z = x[q][p]
            if z:
                x[q] = [y - z * w for y, w in zip(x[q], x[p])]
    return [row[n:] for row in x]


def mplus(a, b, sign=1):
    return [[x + sign * y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def fv_add(a, b, sign=1):
    return [x + sign * y for x, y in zip(a, b)]


def fv_scale(a, s):
    return [x * s for x in a]


def fv_matrix(a, v):
    return [sum((x * h for x, h in zip(row, v) if x), Fourier()) for row in a]


def zero(v):
    return all(not h for h in v)


def mode_count(v):
    return len(set().union(*(set(h.d) for h in v)))


def main():
    started = perf_counter()
    executed_source = Path(__file__).read_bytes()
    V = list(product((-1, 0, 1), repeat=3))
    energies = [sum(a * a for a in v) for v in V]
    M = [F(2, 3) ** (3 - e) * F(1, 6) ** e for e in energies]
    K = [[F(1)] * 27, *[[F(v[a]) for v in V] for a in range(3)], list(map(F, energies))]
    A = [F(5 - 3 * e, 2) for e in energies]
    C = [F(3 * (e - 1), 2) for e in energies]
    reactions = []
    axial_indices = []

    def invariant(i, j):
        return tuple(V[i][a] + V[j][a] for a in range(3)) + (energies[i] + energies[j],)

    for a, b, c, d in combinations(range(27), 4):
        for i, j, k, l in ((a, b, c, d), (a, c, b, d), (a, d, b, c)):
            if invariant(i, j) != invariant(k, l):
                continue
            r = (i, j, k, l)
            d1 = [V[i][a] - V[j][a] for a in range(3)]
            d2 = [V[k][a] - V[l][a] for a in range(3)]
            nz1 = [a for a in range(3) if d1[a]]
            nz2 = [a for a in range(3) if d2[a]]
            if (len(nz1) == len(nz2) == 1 and nz1 != nz2
                    and abs(d1[nz1[0]]) == abs(d2[nz2[0]]) == 2):
                axial_indices.append(len(reactions))
            reactions.append(r)
    assert len(reactions) == 288 and len(axial_indices) == 9
    tuned_response_check(V, energies, M, reactions, axial_indices, K)

    # Rational alpha=1 is a deliberate finite control: the chosen shear uses
    # only off-diagonal stress response, which is independent of axial alpha.
    # General fluid isotropy at alpha_* remains a separate exact certificate.
    alpha = F(1)
    rates = [alpha if n in axial_indices else F(1) for n in range(288)]
    B = [[F(0)] * 27 for _ in V]
    for rate, (i, j, k, l) in zip(rates, reactions):
        assert M[i] * M[j] == M[k] * M[l]
        entries = ((i, -1), (j, -1), (k, 1), (l, 1))
        for inv in K:
            assert sum(s * inv[q] for q, s in entries) == 0
        for q, s in entries:
            for p, t in entries:
                B[q][p] += rate * M[i] * M[j] * s * t / M[q]
    P = [[M[q] * (A[p] + 3 * sum(V[p][a] * V[q][a] for a in range(3))
                    + C[p] * energies[q]) for q in range(27)] for p in range(27)]
    identity = [[F(i == j) for j in range(27)] for i in range(27)]
    zeros = [[F(0)] * 27 for _ in V]
    Q = mplus(identity, P, -1)
    R = mplus(inverse(mplus(B, P)), P, -1)
    assert mm(P, P) == P
    assert mm(B, P) == mm(P, B) == zeros
    assert mm(B, R) == mm(R, B) == Q
    assert mm(P, R) == mm(R, P) == zeros
    for i in range(27):
        for j in range(27):
            assert M[i] * P[i][j] == M[j] * P[j][i]
            assert M[i] * B[i][j] == M[j] * B[j][i]
            assert M[i] * R[i][j] == M[j] * R[j][i]
    print('finite collision and projection: 288 reactions, 9 axial, BR=RB=Q, PR=RP=0, weighted symmetries exact')

    def T(h):
        return [sum((f.derivative(a) * v[a] for a in range(3)), Fourier()) for f, v in zip(h, V)]

    def moments(h):
        return [sum((f * (M[i] * inv[i]) for i, f in enumerate(h)), Fourier()) for inv in K]

    def gamma(g, h):
        out = [Fourier() for _ in V]
        for rate, (i, j, k, l) in zip(rates, reactions):
            flux = (g[i] * h[j] + g[j] * h[i] - g[k] * h[l] - g[l] * h[k]) * (rate * M[i] * M[j] / 2)
            for q, s in ((i, -1), (j, -1), (k, 1), (l, 1)):
                out[q] = out[q] + flux * (s / M[q])
        return out

    def kernel(rho, j, energy=0):
        return [rho * A[i] + sum((j[a] * (3 * v[a]) for a in range(3)), Fourier())
                + Fourier(energy) * C[i] for i, v in enumerate(V)]

    def mv(a, x):
        return [sum(c * y for c, y in zip(row, x)) for row in a]

    def inner(a, b):
        return sum(m * x * y for m, x, y in zip(M, a, b))

    off = [F(v[0] * v[1]) for v in V]
    heat = [F(v[2]) * (F(e) - F(5, 3)) for v, e in zip(V, energies)]
    assert inner(off, mv(R, off)) == F(67, 1083)
    assert inner(heat, mv(R, heat)) == F(40, 441)
    assert inner(off, mv(R, heat)) == 0

    # All fields and both time derivatives at t=0 of the exact smooth family:
    # j=(ux+A exp(-nu t)sin(y-uy t),uy,uz),
    # rho=C exp(-D t)sin(z-(2/5)uz t). The time jets are analytic, not obtained
    # by imposing the kinetic hierarchy that the runner subsequently checks.
    nu, D, ct = F(67, 361), F(4, 49), F(2, 5)
    ux, uy, uz, amp, therm = F(2, 7), F(3, 11), F(-2, 9), F(5, 13), F(4, 15)
    sy, cy = sin_mode((0, 1, 0)), cos_mode((0, 1, 0))
    sz, cz = sin_mode((0, 0, 1)), cos_mode((0, 0, 1))
    j = [Fourier(ux) + amp * sy, Fourier(uy), Fourier(uz)]
    jt = [amp * (-nu * sy - uy * cy), Fourier(), Fourier()]
    jtt = [amp * ((nu * nu - uy * uy) * sy + 2 * nu * uy * cy), Fourier(), Fourier()]
    rho = therm * sz
    rhot = therm * (-D * sz - ct * uz * cz)
    rhott = therm * ((D * D - ct * ct * uz * uz) * sz + 2 * D * ct * uz * cz)
    assert sum((j[a].derivative(a) for a in range(3)), Fourier()) == 0
    for a in range(3):
        assert jt[a] + sum((j[b] * j[a].derivative(b) for b in range(3)), Fourier()) - nu * j[a].laplacian() == 0
    assert rhot + ct * sum((j[b] * rho.derivative(b) for b in range(3)), Fourier()) - D * rho.laplacian() == 0
    U, Ut, Utt = kernel(rho, j), kernel(rhot, jt), kernel(rhott, jtt)
    assert all(f.real() for f in U + Ut + Utt)
    assert zero(fv_matrix(B, U)) and zero(fv_matrix(P, T(U)))
    guu = gamma(U, U)
    assert guu == fv_matrix(B, [u * u / 2 for u in U])
    assert zero(moments(guu))
    guut = gamma(U, Ut)
    assert fv_scale(guut, 2) == fv_matrix(B, [u * ut for u, ut in zip(U, Ut)])
    assert zero(moments(guut))
    print('analytic fluid jet: nonconstant advected shear and thermal wave; equilibrium polarization exact')

    U2 = [u * u / 2 for u in U]
    microscopic = fv_add(fv_matrix(Q, U2), fv_matrix(R, T(U)), -1)
    microscopic_t = fv_add(fv_matrix(Q, [u * ut for u, ut in zip(U, Ut)]), fv_matrix(R, T(Ut)), -1)
    m = [(ct * rho * j[a] - D * rho.derivative(a)).remove_mean() for a in range(3)]
    mt = [(ct * (rhot * j[a] + rho * jt[a]) - D * rhot.derivative(a)).remove_mean() for a in range(3)]
    energy = sum((a * a for a in j), Fourier()).remove_mean()
    energy_t = (2 * sum((a * b for a, b in zip(j, jt)), Fourier())).remove_mean()
    w = fv_add(microscopic, kernel(Fourier(), m, energy))
    wt = fv_add(microscopic_t, kernel(Fourier(), mt, energy_t))
    expected_w_moments = [Fourier(), *m, energy]
    assert moments(w) == expected_w_moments
    assert all(not q.mean() for q in moments(w) + moments(wt))
    assert zero(fv_add(fv_add(T(U), fv_matrix(B, w)), guu, -1))
    guw = gamma(U, w)
    S2 = fv_add(fv_add(fv_scale(guw, 2), Ut, -1), T(w), -1)
    assert zero(fv_matrix(P, S2)) and zero(moments(S2))
    z = fv_matrix(R, S2)
    assert zero(moments(z))
    assert fv_matrix(B, z) == S2
    assert zero(fv_add(fv_add(fv_add(Ut, T(w)), fv_matrix(B, z)), fv_scale(guw, 2), -1))
    S2t = fv_add(fv_add(fv_add(fv_scale(gamma(Ut, w), 2), fv_scale(gamma(U, wt), 2)), Utt, -1), T(wt), -1)
    zt = fv_matrix(R, S2t)
    assert zero(fv_matrix(P, S2t))
    assert fv_matrix(B, zt) == S2t
    assert all(f.real() for f in w + wt + z + zt)
    print('full correctors: all 27 components at delta powers -2,-1,0 and time derivative; all five macro compatibility conditions exact')

    gww, guz, gwz, gzz = gamma(w, w), gamma(U, z), gamma(w, z), gamma(z, z)
    for nonlinear in (guw, gww, guz, gwz, gzz):
        assert zero(moments(nonlinear))
    r1 = fv_add(fv_add(fv_add(wt, T(z)), gww, -1), fv_scale(guz, 2), -1)
    r2 = fv_add(zt, fv_scale(gwz, 2), -1)
    assert not zero(gww) and not zero(gzz) and not zero(r1)
    for delta in (F(1, 3), F(1, 5), F(2, 11)):
        G = fv_add(fv_add(U, fv_scale(w, delta)), fv_scale(z, delta * delta))
        Gt = fv_add(fv_add(Ut, fv_scale(wt, delta)), fv_scale(zt, delta * delta))
        actual = fv_add(fv_add(fv_add(Gt, fv_scale(T(G), 1 / delta)), fv_scale(fv_matrix(B, G), 1 / (delta * delta))), fv_scale(gamma(G, G), 1 / delta), -1)
        expected = fv_add(fv_add(fv_scale(r1, delta), fv_scale(r2, delta * delta)), fv_scale(gzz, delta ** 3), -1)
        assert actual == expected
        assert not zero(actual)
        # A residual omitting the quadratic Gamma(w,w) term must fail on the
        # same fully evaluated kinetic residual, not on a declared token list.
        wrong_residual = fv_add(expected, fv_scale(gww, delta))
        assert actual != wrong_residual
        print(f'nonlinear residual delta={delta}: direct full operator equals exact residual in {mode_count(actual)} Fourier modes; missing quadratic term rejected')

    # Remove energy/pressure correction while retaining all microscopic terms.
    no_pressure_w = fv_add(microscopic, kernel(Fourier(), m))
    no_pressure_macro = fv_matrix(P, fv_add(Ut, T(no_pressure_w)))
    assert not zero(no_pressure_macro)
    p_mom = moments(no_pressure_macro)
    assert not p_mom[0] and not p_mom[4]
    for a in range(3):
        assert p_mom[a + 1] == -energy.derivative(a) / 3

    # Replace the candidate scalar advection coefficient by one consistently
    # in rho_t and in the macro flux m. The mass equation still cancels;
    # the energy equation exposes the wrong coefficient.
    wrong_rhot = therm * (-D * sz - uz * cz)
    wrong_Ut = kernel(wrong_rhot, jt)
    wrong_m = [(rho * j[a] - D * rho.derivative(a)).remove_mean() for a in range(3)]
    wrong_w = fv_add(microscopic, kernel(Fourier(), wrong_m, energy))
    wrong_macro = moments(fv_add(wrong_Ut, T(wrong_w)))
    assert not wrong_macro[0] and all(not q for q in wrong_macro[1:4])
    assert wrong_macro[4] == sum(((rho * j[a]).derivative(a) for a in range(3)), Fourier())
    assert wrong_macro[4]
    print('macro discriminators: removing pressure correction fails momentum; thermal coefficient 1 preserves mass but fails energy')
    print(f'parameters: axial_alpha={alpha}, viscosity={nu}, density_diffusion={D}, thermal_advection={ct}, ux={ux}, uy={uy}, uz={uz}, shear_amplitude={amp}, thermal_amplitude={therm}')
    print(f'Fourier support: U={mode_count(U)}, w={mode_count(w)}, z={mode_count(z)}, wt={mode_count(wt)}, zt={mode_count(zt)}')
    print('coverage: exact rational finite algebra and one analytic Fourier/time-jet family at t=0; no numerical time integrator or all-data PDE convergence proof')
    print('scope: tuned alpha_* full constitutive responses checked separately from the rational alpha=1 Fourier residual control; analytic proof supplies the general smooth-data result')
    print('result: all author discriminator identities and failing controls verified')
    print(f'runtime_seconds={perf_counter() - started:.6f}')
    print('python=' + sys.version.split()[0] + '; dependencies=Python standard library only')
    assert Path(__file__).read_bytes() == executed_source, 'Source changed during execution; rerun final source.'
    print('script_sha256=' + sha256(executed_source).hexdigest())


if __name__ == '__main__':
    main()
