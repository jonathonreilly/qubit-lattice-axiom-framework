"""Exact finite controls of the supplied projector target; no source imports."""
from fractions import Fraction as F
from itertools import product
import json

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/FINITE_PROJECTION_MIXED_ENERGY_AND_CURVATURE_TARGET_BOUNDED_THEOREM_NOTE_2026-09-27.md",
)


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def mv(a, x):
    return [dot(row, x) for row in a]


def mm(a, b):
    return [[dot(row, col) for col in zip(*b)] for row in a]


def normalize(x):
    return [v/sum(x) for v in x]


def generator_controls():
    h = [[F(2, 5), F(-1), F(-2)],
         [F(-1), F(-1, 3), F(0)],
         [F(-2), F(0), F(7, 4)]]
    total = 0
    for psi in product((F(1), F(2), F(3)), repeat=3):
        el = [v/p for v, p in zip(mv(h, psi), psi)]
        q = [[-h[y][x]*psi[y]/psi[x] if x != y else F(0)
              for y in range(3)] for x in range(3)]
        for x in range(3):
            q[x][x] = -sum(q[x])
        for x, y in product(range(3), repeat=2):
            lhs = q[y][x]-(el[x] if x == y else 0)
            rhs = -psi[x]*h[x][y]/psi[y]
            assert lhs == rhs, "weighted forward generator"
            total += 1
    return total


def mixed_energy(h, g, psi, p0):
    chi = [v/p for v, p in zip(p0, psi)]
    f = [p*v for p, v in zip(psi, mv(g, chi))]
    el = [v/p for v, p in zip(mv(h, psi), psi)]
    direct = dot(el, f)/sum(f)
    matrix = dot(psi, mv(h, mv(g, chi)))/dot(psi, mv(g, chi))
    assert direct == matrix, "mixed local-energy identity"
    return direct


def boundary_controls():
    h = [[F(0), F(-1)], [F(-1), F(0)]]
    g = [[F(3), F(1)], [F(1), F(3)]]  # exp(-tH) up to scalar at exp(2t)=2
    uniform = [F(1, 2), F(1, 2)]
    common = mixed_energy(h, g, [F(1), F(1)], uniform)
    mixed = mixed_energy(h, g, [F(1), F(2)], uniform)
    rayleigh = mixed_energy(h, g, [F(1), F(2)], [F(1, 5), F(4, 5)])
    assert (common, mixed, rayleigh) == (F(-1), F(-19, 17), F(-17, 19)), "right boundary"
    # Normalize after each exact-distribution step or just once at the end.
    psi = [F(1), F(2)]
    kernel = [[psi[i]*g[i][j]/psi[j] for j in range(2)] for i in range(2)]
    for p in (uniform, [F(1), F(0)], [F(1, 7), F(6, 7)]):
        assert normalize(mv(kernel, normalize(mv(kernel, p)))) == normalize(mv(mm(kernel, kernel), p)), "exact normalization composition"
    return {"common": str(common), "mixed": str(mixed), "psi_squared_initial": str(rayleigh)}


def single_walker_controls():
    h = [[F(2, 5), F(-1), F(-2)],
         [F(-1), F(-1, 3), F(0)],
         [F(-2), F(0), F(7, 4)]]
    field = [F(-2), F(1), F(3)]
    populations = ([F(1), F(0), F(0)], [F(1, 3)]*3,
                   [F(1, 7), F(2, 7), F(4, 7)])
    balance_entries = probe_cases = guides = 0
    for psi in product((F(1), F(2), F(3)), repeat=3):
        el = [v/p for v, p in zip(mv(h, psi), psi)]
        pi = normalize([p*p for p in psi])
        q = [[-h[x][y]*psi[y]/psi[x] if x != y else F(0)
              for y in range(3)] for x in range(3)]
        for x in range(3):
            q[x][x] = -sum(q[x])
        for x, y in product(range(3), repeat=2):
            assert pi[x]*q[x][y] == pi[y]*q[y][x], "single-walker detailed balance"
            balance_entries += 1
        assert all(dot(pi, column) == 0 for column in zip(*q)), "single-walker stationarity"
        assert dot(pi, el) == dot(psi, mv(h, psi))/dot(psi, psi), "single-walker Rayleigh target"
        for probe, population in product((F(1, 10), F(3, 20), F(1, 3)), populations):
            values = []
            for hh in (F(0), probe, 2*probe):
                shifted = [[h[x][y]-(hh*field[x] if x == y else 0)
                            for y in range(3)] for x in range(3)]
                energy = [v/p for v, p in zip(mv(shifted, psi), psi)]
                assert energy == [v-hh*f for v, f in zip(el, field)], "fixed-guide linear field energy"
                values.append(dot(population, energy))
            assert 15*values[0]-16*values[1]+values[2] == 14*probe*dot(population, field), "single-walker common-guide probe"
            probe_cases += 1
        guides += 1
    psi = [F(1), F(2)];toy = [[F(0), F(-1)], [F(-1), F(0)]]
    energy = dot(psi, mv(toy, psi))/dot(psi, psi)
    assert energy == F(-4, 5) and energy > -1, "single-walker nonground witness"
    return {"guides": guides, "balance_entries": balance_entries,
            "common_guide_probe_cases": probe_cases, "toy_stationary_energy": str(energy)}


# Coefficients of 1,h,h^2; all arithmetic is in Q[h]/(h^3).
def add(x, y):
    return tuple(a+b for a, b in zip(x, y))


def scale(x, a):
    return tuple(a*v for v in x)


def mul(x, y):
    return tuple(sum((x[i]*y[k-i] for i in range(k+1)), F(0)) for k in range(3))


def inv(x):
    a, b, c = x
    assert a != 0
    return (1/a, -b/a**2, b*b/a**3-c/a**2)


def curvature_controls():
    n = 0
    for a, c, beta, z, z2 in product(
            (F(1), F(2), F(3, 2)), (F(0), F(1), F(2)),
            (F(0), F(1, 2), F(-1)), (F(0), F(1, 3), F(3, 5)),
            (F(-2), F(0), F(7))):
        gamma = (a, F(0), c*c/(2*a))
        aa = (a, F(0), 2*a*beta*beta)
        zz = (z, F(0), z2)
        numerator = scale(mul(gamma, add(aa, mul(gamma, zz))), F(-1))
        energy = mul(numerator, inv(add(gamma, mul(aa, zz))))
        e = (1-z)/(1+z)
        expected = c*c/a*(1-e)+4*a*beta*beta*e
        assert energy[0] == -a and energy[1] == 0, "zero-field energy"
        assert -2*energy[2] == expected, "curvature with arbitrary tanh second coefficient"
        n += 1
    e = F(1, 2)
    common, per, ground = 4*(1-e), 4*(1-e)+e, F(4)
    assert (common, per, ground) == (F(2), F(5, 2), F(4)), "curvature witness"
    weights = [F(1, 6), F(1, 3), F(1, 2)]
    decays = [F(1, 2), F(1, 4), F(1, 8)]
    averaged_decay = dot(weights, decays)
    assert dot(weights, [4*(1-v)+v for v in decays]) == 4*(1-averaged_decay)+averaged_decay, "finite age average"
    ages = [F(3, 200)*j for j in range(501, 2001)]
    assert (len(ages), ages[0], ages[-1]) == (1500, F(1503, 200), F(30)), "generation indexing"
    return {"rational_expansions": n, "susceptibilities": list(map(str, (common, per, ground))), "averaged_decay": str(averaged_decay), "ages": [str(ages[0]), str(ages[-1])], "age_count": len(ages)}


def covariance_controls():
    alpha = [F(-2), F(3, 2), F(1, 3)]
    gamma = [F(1), F(-2), F(4)]
    sd_p = [F(1, 2), F(2), F(1, 5)]
    sd_c = [F(3), F(1, 4), F(2, 3)]
    lo = sum((abs(a)*s-abs(g)*t)**2 for a, g, s, t in zip(alpha, gamma, sd_p, sd_c))
    hi = sum((abs(a)*s+abs(g)*t)**2 for a, g, s, t in zip(alpha, gamma, sd_p, sd_c))
    variances = []
    for rho in product((F(-1), F(0), F(1)), repeat=3):
        var = sum(a*a*s*s+g*g*t*t-2*a*g*s*t*r for a, g, s, t, r in zip(alpha, gamma, sd_p, sd_c, rho))
        assert lo <= var <= hi, "paired covariance range"
        variances.append(var)
    assert min(variances) == lo and max(variances) == hi, "covariance extremizers"
    arbitrary = sum(abs(a)*s+abs(g)*t for a, g, s, t in zip(alpha, gamma, sd_p, sd_c))
    assert hi <= arbitrary**2, "joint covariance upper bound"
    return {"independent_pairs_variance_range": list(map(str, (lo, hi))), "arbitrary_joint_sd_upper": str(arbitrary), "models": len(variances)}


def probe_stencil_controls():
    rows = []
    for h in (F(1, 10), F(3, 20), F(1, 3)):
        got = []
        for degree in range(7):
            zero = F(1) if degree == 0 else F(0)
            got.append((15*zero-16*h**degree+(2*h)**degree)/(12*h*h))
        expected = [F(0), -F(7, 6)/h, F(-1), -F(2, 3)*h,
                    F(0), F(4, 3)*h**3, 4*h**4]
        assert got == expected, "finite-probe monomial coefficients"
        rows.append(list(map(str, got)))
    return rows


def main():
    print(json.dumps({
        "weighted_generator_entries": generator_controls(),
        "boundary_examples": boundary_controls(),
        "single_walker": single_walker_controls(),
        "curvature": curvature_controls(),
        "covariance": covariance_controls(),
        "probe_stencil_monomials_degrees_0_to_6": probe_stencil_controls(),
        "scope": "Exact supplied finite-matrix controls; no population convergence, source-simulator validation, actual ring bias, physical photon or audit conclusion.",
    }, indent=2))


if __name__ == "__main__":
    main()
