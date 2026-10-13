"""Independent checks for C5 probe R19-30.

This file intentionally does not import lib1930.py or any r1930_* worker code.
It reconstructs the scalar and D1 laws, the UD vertex, the eight character
projectors of (Z/2)^3, the placement repair, the one-loop face1 contraction,
and the pair-channel Ward completion directly.
"""

from itertools import product
import numpy as np


PI = np.pi
RNG = np.random.default_rng(301930)


def wrap(x):
    x = np.asarray(x, dtype=float)
    return (x + PI) % (2 * PI) - PI


def smooth_step(x):
    x = np.clip(np.asarray(x, dtype=float), 0.0, 1.0)
    with np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        a = np.where(x > 0, np.exp(-1.0 / np.where(x > 0, x, 1.0)), 0.0)
        b = np.where(x < 1, np.exp(-1.0 / np.where(x < 1, 1.0 - x, 1.0)), 0.0)
    return a / (a + b)


def placement_factor(q):
    q = np.asarray(q, dtype=float)
    return (9 * np.cos(q / 2) - np.cos(3 * q / 2)) / 8


class HalfIntervalIntegral:
    """Dense, symmetry-enforced cumulative quadrature on [0, 1]."""

    def __init__(self, fun, panels=1 << 18):
        self.x = np.linspace(0.0, 1.0, panels + 1)
        y = fun(self.x)
        dx = 1.0 / panels
        self.c = np.concatenate([[0.0], np.cumsum((y[:-1] + y[1:]) * (dx / 2))])

    def __call__(self, x):
        return np.interp(np.clip(x, 0.0, 1.0), self.x, self.c)


INT_STEP = HalfIntervalIntegral(smooth_step)
INT_WILSON = HalfIntervalIntegral(
    lambda x: 2 * np.sqrt(np.maximum(0.0, smooth_step(x) * (1 - smooth_step(x))))
)


class ScalarLaw:
    def __init__(self, mass=0.01, edge=2.5261508):
        self.mass = mass
        self.edge = edge
        self.width = PI - edge

    def sigma(self, k):
        k = wrap(k)
        a = np.abs(k)
        u = (a - self.edge) / self.width
        return np.sign(k) * np.where(a <= self.edge, a, a - self.width * INT_STEP(u))

    def dsigma(self, k):
        return 1 - smooth_step((np.abs(wrap(k)) - self.edge) / self.width)

    def f(self, k):
        return self.sigma(k) * self.dsigma(k)

    def energy(self, k):
        return np.sqrt(self.mass**2 + np.sum(self.sigma(k) ** 2, axis=-1))


class D1Law:
    def __init__(self, mass=0.01, edge=0.909103707957, r=0.555604225797):
        self.mass = mass
        self.edge = edge
        self.r = r
        self.width = PI - 2 * edge
        self.wpi = self.width * r * float(INT_WILSON(1.0))

    def S(self, k):
        k = wrap(k)
        a = np.abs(k)
        u = (a - self.edge) / self.width
        core = np.where(
            a <= self.edge,
            a,
            np.where(a >= PI - self.edge, PI - a, a - 2 * self.width * INT_STEP(u)),
        )
        return np.sign(k) * core

    def dS(self, k):
        return 1 - 2 * smooth_step((np.abs(wrap(k)) - self.edge) / self.width)

    def W(self, k):
        a = np.abs(wrap(k))
        u = (a - self.edge) / self.width
        return self.width * self.r * INT_WILSON(u)

    def dW(self, k):
        k = wrap(k)
        x = (np.abs(k) - self.edge) / self.width
        st = smooth_step(x)
        return np.sign(k) * 2 * self.r * np.sqrt(np.maximum(0.0, st * (1 - st)))

    def coeff(self, k):
        s = self.S(k)
        m = self.mass + np.sum(self.W(k), axis=-1)
        return np.concatenate([s, m[..., None]], axis=-1)

    def energy(self, k):
        return np.sqrt(np.sum(self.coeff(k) ** 2, axis=-1))

    def momentum(self, k):
        s = self.S(k)
        return s * self.dS(k) + (self.mass + np.sum(self.W(k), axis=-1))[..., None] * self.dW(k)

    def ud_coeff(self, k, i, j):
        p = self.momentum(k)
        ds = self.dS(k)
        dw = self.dW(k)
        out = np.zeros(k.shape[:-1] + (4,), dtype=float)
        out[..., i] += 0.5 * p[..., j] * ds[..., i]
        out[..., j] += 0.5 * p[..., i] * ds[..., j]
        out[..., 3] += 0.5 * (p[..., j] * dw[..., i] + p[..., i] * dw[..., j])
        return out


S1 = np.array([[0, 1], [1, 0]], complex)
S2 = np.array([[0, -1j], [1j, 0]], complex)
S3 = np.array([[1, 0], [0, -1]], complex)
Z2 = np.zeros((2, 2), complex)
I2 = np.eye(2, dtype=complex)
GAMMA = np.array(
    [np.block([[Z2, s], [s, Z2]]) for s in (S1, S2, S3)]
    + [np.block([[I2, Z2], [Z2, -I2]])]
)
I4 = np.eye(4, dtype=complex)


def matrix_from_coeff(c):
    return np.einsum("...a,aij->...ij", c, GAMMA)


def hamiltonian(law, k):
    return matrix_from_coeff(law.coeff(k))


def projector(law, k, sign):
    return 0.5 * (I4 + sign * hamiltonian(law, k) / law.energy(k)[..., None, None])


BITS = tuple(np.array(x, dtype=int) for x in product((0, 1), repeat=3))


def character_parts(fun, k):
    """Independent (Z/2)^3 character projection into the eight offset classes."""
    shifted = {tuple(e): fun(k + PI * e) for e in BITS}
    ans = {}
    for sigma in BITS:
        total = 0.0
        for e in BITS:
            total = total + (-1.0) ** int(np.dot(sigma, e)) * shifted[tuple(e)]
        ans[tuple(sigma)] = total / 8
    return ans


def target_parity(i, j):
    ans = np.zeros(3, dtype=int)
    ans[i] += 1
    ans[j] += 1
    return ans % 2


def repair_from_parts(parts, q, target):
    ans = 0.0
    for sigma_t, value in parts.items():
        sigma = np.array(sigma_t, dtype=int)
        amp = np.ones(q.shape[:-1], dtype=float)
        for ell in range(3):
            if sigma[ell] != target[ell]:
                amp *= placement_factor(q[..., ell])
        ans = ans + amp[..., None] * value
    return ans


def repaired(fun, kbar, q, i, j):
    return repair_from_parts(character_parts(fun, kbar), q, target_parity(i, j))


def placement_phase(q, i, j):
    return np.exp(-0.5j * (q[..., i] + q[..., j]))


def dirac_site_block(law, k2, q, i, j, mode):
    k1 = k2 + q
    kbar = k2 + q / 2
    fun = lambda x: law.ud_coeff(x, i, j)
    c = fun(kbar)
    if mode == "FF" and i != j:
        c = c * (placement_factor(q[..., i]) * placement_factor(q[..., j]))[..., None]
    elif mode == "PR":
        c = repaired(fun, kbar, q, i, j)
    x = matrix_from_coeff(c)
    pp1, pm1 = projector(law, k1, +1), projector(law, k1, -1)
    pp2, pm2 = projector(law, k2, +1), projector(law, k2, -1)
    pair = pp1 @ x @ pm2 + pm1 @ x @ pp2
    return placement_phase(q, i, j)[..., None, None] * pair


def parity_content_suite():
    scalar, dirac = ScalarLaw(), D1Law()
    k = RNG.uniform(-PI, PI, (12000, 3))
    print("OFFSET-PARITY CONTENT (independent character projectors)")
    for label, maker in (
        ("UD", lambda i, j: (lambda x: dirac.ud_coeff(x, i, j))),
        ("E1 U", lambda i, j: (lambda x: (scalar.f(x[..., i]) * scalar.f(x[..., j]))[..., None])),
    ):
        for i, j in ((0, 1), (0, 0)):
            fun = maker(i, j)
            parts = character_parts(fun, k)
            total = np.sqrt(np.mean(np.sum(np.abs(fun(k)) ** 2, axis=-1)))
            good = parts[tuple(target_parity(i, j))]
            share = np.sqrt(np.mean(np.sum(np.abs(good) ** 2, axis=-1))) / total
            active = sum(
                np.sqrt(np.mean(np.sum(np.abs(value) ** 2, axis=-1))) / total > 1e-10
                for value in parts.values()
            )
            print(f"  {label:4s} T^{i}{j}: correct-class RMS share {share:.4f}; active classes {active}/8")


def scalar_e1_site_block(law, k2, q, i, j, mode):
    k1 = q - k2
    kbar = k1 - q / 2
    fun = lambda x: (law.f(x[..., i]) * law.f(x[..., j]))[..., None]
    value = fun(kbar)
    if mode == "FF" and i != j:
        value = value * (placement_factor(q[..., i]) * placement_factor(q[..., j]))[..., None]
    elif mode == "PR":
        value = repaired(fun, kbar, q, i, j)
    norm = np.sqrt(law.energy(k1) * law.energy(k2))
    return placement_phase(q, i, j) * value[..., 0] / norm


def scalar_per_leg_site_block(law, k2, q, i, j, mode):
    k1 = q - k2
    value = -(law.f(k1[..., i]) * law.f(k2[..., j]) + law.f(k1[..., j]) * law.f(k2[..., i]))
    value /= 2 * np.sqrt(law.energy(k1) * law.energy(k2))
    if mode == "FF" and i != j:
        value *= placement_factor(q[..., i]) * placement_factor(q[..., j])
    return placement_phase(q, i, j) * value


def cut_jump(fun, ell, eps, samples=80):
    k2 = RNG.uniform(-PI, PI, (samples, 3))
    other = RNG.uniform(-2.3, 2.3, (samples, 3))
    qa, qb = other.copy(), other.copy()
    qa[:, ell], qb[:, ell] = PI - eps, -PI + eps
    a, b = fun(k2, qa), fun(k2, qb)
    return float(np.max(np.abs(a - b)))


def cut_suite():
    scalar = ScalarLaw()
    dirac = D1Law()
    print("CUT TEST (independent character decomposition)")
    tests = [
        ("per-leg U xy raw", lambda k, q: scalar_per_leg_site_block(scalar, k, q, 0, 1, "raw"), 0),
        ("per-leg U xy FF", lambda k, q: scalar_per_leg_site_block(scalar, k, q, 0, 1, "FF"), 0),
        ("E1 U xy raw", lambda k, q: scalar_e1_site_block(scalar, k, q, 0, 1, "raw"), 0),
        ("E1 U xy FF", lambda k, q: scalar_e1_site_block(scalar, k, q, 0, 1, "FF"), 0),
        ("E1 U xx FF", lambda k, q: scalar_e1_site_block(scalar, k, q, 0, 0, "FF"), 0),
        ("E1 U xy PR", lambda k, q: scalar_e1_site_block(scalar, k, q, 0, 1, "PR"), 0),
        ("E1 U xx PR", lambda k, q: scalar_e1_site_block(scalar, k, q, 0, 0, "PR"), 0),
        ("UD xy raw, x cut", lambda k, q: dirac_site_block(dirac, k, q, 0, 1, "raw"), 0),
        ("UD xy FF, z cut", lambda k, q: dirac_site_block(dirac, k, q, 0, 1, "FF"), 2),
        ("UD xx FF, x cut", lambda k, q: dirac_site_block(dirac, k, q, 0, 0, "FF"), 0),
    ]
    for label, fun, ell in tests:
        j5 = cut_jump(fun, ell, 1e-5)
        j7 = cut_jump(fun, ell, 1e-7)
        print(f"  {label:22s}: eps 1e-5 {j5:.3e}; eps 1e-7 {j7:.3e}")
    worst5 = worst7 = 0.0
    for i, j in ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)):
        for ell in range(3):
            fun = lambda k, q, i=i, j=j: dirac_site_block(dirac, k, q, i, j, "PR")
            worst5 = max(worst5, cut_jump(fun, ell, 1e-5, 30))
            worst7 = max(worst7, cut_jump(fun, ell, 1e-7, 30))
    print(f"  UD PR, all 6 comps/all 3 cuts: eps 1e-5 {worst5:.3e}; eps 1e-7 {worst7:.3e}")


def polarizations():
    a = np.array([1.0, -1.0, 0.0]) / np.sqrt(2)
    b = np.array([0.0, 0.0, 1.0])
    return {"face1": (0.5 * (np.outer(a, a) - np.outer(b, b)), np.array([1.0, 1.0, 0.0]) / np.sqrt(2))}


COMPONENTS = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))


def contracted_gamma(law, grid, e, q, variant):
    total = np.zeros(grid.shape[:-1] + (4,), dtype=complex)
    for i, j in COMPONENTS:
        weight = e[i, j] + (e[j, i] if i != j else 0.0)
        if weight == 0:
            continue
        fun = lambda x, i=i, j=j: law.ud_coeff(x, i, j)
        c = fun(grid)
        if variant == "literal":
            c = c * np.exp(0.5j * (q[i] + q[j]))
        elif variant == "PR":
            qq = np.broadcast_to(q, grid.shape)
            c = repaired(fun, grid, qq, i, j)
        total += weight * c
    return matrix_from_coeff(total)


def pi_pair(law, grid, e, q, variant):
    k1, k2 = grid + q / 2, grid - q / 2
    p1, m1 = projector(law, k1, +1), projector(law, k1, -1)
    p2, m2 = projector(law, k2, +1), projector(law, k2, -1)
    g = contracted_gamma(law, grid, e, q, variant)
    gd = np.swapaxes(g.conj(), -1, -2)
    t = np.einsum("...ij,...jk,...kl,...li->...", p1, g, m2, gd)
    t += np.einsum("...ij,...jk,...kl,...li->...", m1, g, p2, gd)
    return -float(np.mean(t.real / (law.energy(k1) + law.energy(k2))))


def face_shift_and_row_neutrality(n_grid=32, h=0.05):
    law = D1Law(mass=0.3)
    kg = (np.arange(n_grid) + 0.5) * 2 * PI / n_grid - PI
    grid = np.stack(np.meshgrid(kg, kg, kg, indexing="ij"), axis=-1).reshape(-1, 3)
    e, direction = polarizations()["face1"]
    vals = {}
    for variant in ("rows", "literal", "PR"):
        p0 = pi_pair(law, grid, e, 0 * direction, variant)
        p1 = pi_pair(law, grid, e, h * direction, variant)
        p2 = pi_pair(law, grid, e, 2 * h * direction, variant)
        vals[variant] = (16 * (p1 - p0) - (p2 - p0)) / (12 * h * h)
    print("FACE1 INDEPENDENT EVALUATOR (m=0.3, midpoint grid)")
    print(f"  N={n_grid}, h={h}: literal minus true-position row = {vals['literal'] - vals['rows']:+.8e}")
    print(f"  N={n_grid}, h={h}: PR minus true-position row      = {vals['PR'] - vals['rows']:+.8e}")

    print("ROW-KERNEL SCALING max |PR-raw|/s^4 (Dirac, 300 kbar)")
    kbar = RNG.uniform(-PI, PI, (300, 3))
    for name, n in (("axis", (0, 0, 1)), ("face", (1, 1, 0)), ("body", (1, 1, 1))):
        n = np.array(n, dtype=float)
        n /= np.linalg.norm(n)
        ans = []
        for s in (0.2, 0.1, 0.05):
            q = np.broadcast_to(s * n, kbar.shape)
            worst = 0.0
            for i, j in COMPONENTS:
                fun = lambda x, i=i, j=j: law.ud_coeff(x, i, j)
                worst = max(worst, float(np.max(np.abs(repaired(fun, kbar, q, i, j) - fun(kbar)))))
            ans.append(worst / s**4)
        print(f"  {name:4s}: " + " ".join(f"{x:.5e}" for x in ans))


def divergence(q):
    q = wrap(q)
    rho = smooth_step((2.5 - np.abs(q)) / 1.5)
    d = rho * q + (1 - rho) * 2 * np.sin(q / 2)
    return d * np.exp(0.5j * q)


def dirac_pair_completion(law, k2, q):
    k1 = k2 + q
    e1, e2 = law.energy(k1), law.energy(k2)
    pp1, pm1 = projector(law, k1, +1), projector(law, k1, -1)
    pp2, pm2 = projector(law, k2, +1), projector(law, k2, -1)
    d = divergence(q)
    spatial_x = {}
    for i in range(3):
        for j in range(3):
            fun = lambda x, i=i, j=j: law.ud_coeff(x, i, j)
            c = repaired(fun, (k2 + q / 2)[None, :], q[None, :], i, j)[0]
            spatial_x[i, j] = placement_phase(q, i, j) * matrix_from_coeff(c)
    out = [[np.zeros((4, 4), complex) for _ in range(4)] for _ in range(4)]
    for sign, pa, pb in ((+1, pp1, pm2), (-1, pm1, pp2)):
        mij = [[pa @ spatial_x[i, j] @ pb for j in range(3)] for i in range(3)]
        m0i = [sign * sum(d[j] * mij[j][i] for j in range(3)) / (e1 + e2) for i in range(3)]
        m00 = sign * sum(d[j] * m0i[j] for j in range(3)) / (e1 + e2)
        out[0][0] += m00
        for i in range(3):
            out[0][i + 1] += m0i[i]
            out[i + 1][0] += m0i[i]
            for j in range(3):
                out[i + 1][j + 1] += mij[i][j]
    return out


def ward_residual(law, k2, q, m):
    h1, h2 = hamiltonian(law, k2 + q), hamiltonian(law, k2)
    d = divergence(q)
    worst = 0.0
    for nu in range(4):
        lhs = h1 @ m[0][nu] - m[0][nu] @ h2
        rhs = sum(d[j] * m[j + 1][nu] for j in range(3))
        worst = max(worst, float(np.max(np.abs(lhs - rhs))))
    return worst


def ward_suite():
    law = D1Law()
    print("W1, independently rebuilt PR pair block")
    for label, qgen in (
        ("generic", lambda: RNG.uniform(-3.0, 3.0, 3)),
        ("x cut +", lambda: np.array([PI - 1e-8, *RNG.uniform(-2.5, 2.5, 2)])),
        ("x cut -", lambda: np.array([-PI + 1e-8, *RNG.uniform(-2.5, 2.5, 2)])),
    ):
        worst = 0.0
        for _ in range(80):
            k2, q = RNG.uniform(-PI, PI, 3), qgen()
            m = dirac_pair_completion(law, k2, q)
            worst = max(worst, ward_residual(law, k2, q, m))
        print(f"  Dirac {label:7s}: {worst:.3e}")

    scalar = ScalarLaw()
    worst = 0.0
    for _ in range(1500):
        k2, q = RNG.uniform(-PI, PI, 3), RNG.uniform(-PI, PI, 3)
        e1, e2 = scalar.energy(q - k2), scalar.energy(k2)
        d = divergence(q)
        fij = np.zeros((3, 3), complex)
        for i in range(3):
            for j in range(3):
                fij[i, j] = scalar_e1_site_block(scalar, k2[None, :], q[None, :], i, j, "PR")[0]
        f0i = np.array([np.dot(d, fij[:, i]) / (e1 + e2) for i in range(3)])
        f00 = np.dot(d, f0i) / (e1 + e2)
        four = np.zeros((4, 4), complex)
        four[1:, 1:] = fij
        four[0, 1:] = four[1:, 0] = f0i
        four[0, 0] = f00
        for nu in range(4):
            worst = max(worst, abs((e1 + e2) * four[0, nu] - np.dot(d, four[1:, nu])))
    print(f"  scalar E1 PR, 1500 whole-torus pairs: {worst:.3e}")


def covariance_suite():
    scalar, dirac = ScalarLaw(), D1Law()
    k = RNG.uniform(-PI, PI, (120, 3))
    q = RNG.uniform(-PI, PI, (120, 3))
    operations = {
        "C4z": (np.array([1, 0, 2]), np.array([-1.0, 1.0, 1.0])),
        "C3": (np.array([1, 2, 0]), np.array([1.0, 1.0, 1.0])),
        "C2": (np.array([1, 0, 2]), np.array([1.0, 1.0, -1.0])),
    }
    print("CUBIC COVARIANCE OF PR COEFFICIENTS")
    for name, (perm, signs) in operations.items():
        rk, rq = signs * k[:, perm], signs * q[:, perm]
        ws = wd = 0.0
        for i, j in COMPONENTS:
            fs_l = lambda x, i=i, j=j: (scalar.f(x[..., i]) * scalar.f(x[..., j]))[..., None]
            pi, pj = int(perm[i]), int(perm[j])
            fs_r = lambda x, pi=pi, pj=pj: (scalar.f(x[..., pi]) * scalar.f(x[..., pj]))[..., None]
            lhs_s = repaired(fs_l, rk, rq, i, j)[..., 0]
            rhs_s = signs[i] * signs[j] * repaired(fs_r, k, q, pi, pj)[..., 0]
            ws = max(ws, float(np.max(np.abs(lhs_s - rhs_s))))

            lhs_d = repaired(lambda x, i=i, j=j: dirac.ud_coeff(x, i, j), rk, rq, i, j)
            base_d = repaired(
                lambda x, i=i, j=j: dirac.ud_coeff(x, int(perm[i]), int(perm[j])),
                k,
                q,
                int(perm[i]),
                int(perm[j]),
            )
            rhs_d = np.empty_like(base_d)
            for a in range(3):
                rhs_d[..., a] = signs[i] * signs[j] * signs[a] * base_d[..., perm[a]]
            rhs_d[..., 3] = signs[i] * signs[j] * base_d[..., 3]
            wd = max(wd, float(np.max(np.abs(lhs_d - rhs_d))))
        print(f"  {name:3s}: scalar {ws:.3e}; Dirac coefficient tensor {wd:.3e}")


def q_only_counterexample():
    """A flat scalar cutoff is a q-only repair, refuting the unqualified no-go."""
    scalar = ScalarLaw()

    def flat_cutoff(q):
        # Exactly one for |q_l|<=1 and exactly zero for |q_l|>=2.5.
        return np.prod(smooth_step((2.5 - np.abs(wrap(q))) / 1.5), axis=-1)

    k2 = RNG.uniform(-PI, PI, (60, 3))
    other = RNG.uniform(-2.0, 2.0, (60, 3))
    qa, qb = other.copy(), other.copy()
    qa[:, 0], qb[:, 0] = PI - 1e-4, -PI + 1e-4
    raw_a = scalar_e1_site_block(scalar, k2, qa, 0, 1, "raw")
    raw_b = scalar_e1_site_block(scalar, k2, qb, 0, 1, "raw")
    fixed_a, fixed_b = flat_cutoff(qa) * raw_a, flat_cutoff(qb) * raw_b
    qsmall = RNG.uniform(-0.9, 0.9, (200, 3))
    print("Q-ONLY MULTIPLIER SCOPE")
    print(f"  raw mixed-parity cut jump: {np.max(np.abs(raw_a - raw_b)):.3e}")
    print(f"  flat-cutoff cut jump:       {np.max(np.abs(fixed_a - fixed_b)):.3e}")
    print(f"  max |chi-1| for |q_l|<0.9: {np.max(np.abs(flat_cutoff(qsmall) - 1)):.3e}")


if __name__ == "__main__":
    parity_content_suite()
    cut_suite()
    face_shift_and_row_neutrality()
    ward_suite()
    covariance_suite()
    q_only_counterexample()
