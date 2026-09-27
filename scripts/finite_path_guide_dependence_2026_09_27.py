"""Exact finite examples for the supplied weighted-path estimator theorem.

No external scientific inputs or repository reads occur inside this runner.
The cache envelope separately binds the paired note and this source. General
identities are proved in the note; these examples do not validate a simulator.
"""
from fractions import Fraction as F
from itertools import product
import json

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/FINITE_PATH_GUIDE_DEPENDENCE_AND_SHARED_CURVATURE_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-09-27.md",
)


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def mv(a, x):
    return [dot(row, x) for row in a]


def mm(a, b):
    return [[dot(row, col) for col in zip(*b)] for row in a]


def local_energy(h, psi):
    return [x/p for x, p in zip(mv(h, psi), psi)]


def endpoint_mean(h, g, psi):
    """Enumerate the joint endpoint law, independently of matrix numerator."""
    z = sum((psi[i]*g[i][j]*psi[j]
             for i in range(len(psi)) for j in range(len(psi))), F(0))
    el = local_energy(h, psi)
    return sum((psi[i]*g[i][j]*psi[j]*(el[i]+el[j])/2/z
                for i in range(len(psi)) for j in range(len(psi))), F(0))


def path_cancellation():
    a = [[F(0), F(2), F(3)], [F(2), F(0), F(1)],
         [F(3), F(1), F(0)]]
    diagonal = [F(-2), F(1), F(4)]
    checked = 0
    for psi in ([F(1), F(2), F(3)], [F(3), F(1), F(2)]):
        q = [[a[i][j]*psi[j]/psi[i] for j in range(3)] for i in range(3)]
        rates = [sum(row) for row in q]
        el = [diagonal[i]-rates[i] for i in range(3)]
        for jumps in range(5):
            for states in product(range(3), repeat=jumps+1):
                if any(x == y for x, y in zip(states, states[1:])):
                    continue
                proposal = psi[states[0]]**2
                physical = psi[states[0]]*psi[states[-1]]
                for x, y in zip(states, states[1:]):
                    proposal *= q[x][y]
                    physical *= a[x][y]
                assert proposal == physical, "path boundary factors"
                # Compare exponential arguments exactly, without exp rounding.
                holding = [F(i+1, (jumps+1)*(jumps+2)) for i in range(jumps+1)]
                assert sum((rates[x]+el[x])*t for x, t in zip(states, holding)) == sum(
                    diagonal[x]*t for x, t in zip(states, holding)), "path exponent"
                checked += 1
    return checked


def bounce_balance():
    # A separate discrete segment example, with exact reversible proposal.
    q = [[F(1, 2), F(1, 2)], [F(1, 8), F(7, 8)]]
    m = [F(1), F(4)]
    weight = [[F(2), F(3)], [F(3), F(1)]]
    paths = list(product(range(2), repeat=3))
    states = [(p, d) for p in paths for d in (-1, 1)]
    base = {p: m[p[0]]*q[p[0]][p[1]]*q[p[1]][p[2]]*
            weight[p[0]][p[1]]*weight[p[1]][p[2]] for p in paths}
    z = sum(base.values())
    pi = {(p, d): base[p]/(2*z) for p, d in states}
    incoming = {s: F(0) for s in states}
    for p, direction in states:
        total = F(0)
        for new in range(2):
            if direction == 1:
                proposal = q[p[-1]][new]
                new_path = (p[1], p[2], new)
                numerator, denominator = weight[p[-1]][new], weight[p[0]][p[1]]
            else:
                proposal = q[p[0]][new]
                new_path = (new, p[0], p[1])
                numerator, denominator = weight[new][p[0]], weight[p[1]][p[2]]
            acceptance = min(F(1), numerator/denominator)
            incoming[(new_path, direction)] += pi[(p, direction)]*proposal*acceptance
            incoming[(p, -direction)] += pi[(p, direction)]*proposal*(1-acceptance)
            total += proposal
        assert total == 1
    assert incoming == pi, "lifted bounce invariant measure"
    return len(states)


def endpoint_and_spectral():
    h = [[F(0), F(-1)], [F(-1), F(0)]]
    results = []
    for g, decay, targets in (
        ([[F(3), F(1)], [F(1), F(3)]], F(1, 2), [-1, F(-17, 19)]),
        ([[F(5, 4), F(3, 4)], [F(3, 4), F(5, 4)]], F(1, 4), [-1, F(-35, 37)]),
    ):
        for b, target in zip((F(1), F(2)), targets):
            psi = [F(1), b]
            direct = endpoint_mean(h, g, psi)
            contraction = dot(psi, mv(h, mv(g, psi)))/dot(psi, mv(g, psi))
            # Independent eigenvector reduction, eigenvalues -1 and +1.
            ground, excited = (1+b)**2, (1-b)**2*decay
            spectral = (-ground+excited)/(ground+excited)
            assert direct == contraction == spectral == target, "finite projection target"
            results.append(str(direct))
    return results


def capped_noncommutation():
    h = [[F(0), F(-1)], [F(-1), F(1)]]
    # Exactly zero jumps, Delta=log(2), M=2, D=diag(0,1).
    segment = [[F(1), F(0)], [F(0), F(1, 2)]]
    c = mm(segment, segment)
    psi = [F(1), F(2)]
    direct = endpoint_mean(h, c, psi)
    left = dot(psi, mv(h, mv(c, psi)))/dot(psi, mv(c, psi))
    right = dot(psi, mv(c, mv(h, psi)))/dot(psi, mv(c, psi))
    assert mm(h, c) != mm(c, h), "cap noncommutation witness"
    assert direct == left == right == F(-3, 4), "capped endpoint target"
    projected = mv(segment, psi)  # sqrt(C) is segment in this example.
    rayleigh = dot(projected, mv(h, projected))/dot(projected, projected)
    assert rayleigh == F(-1, 2) and rayleigh != direct, "capped Rayleigh distinction"
    return str(direct), str(rayleigh)


def projector_boundary():
    h = [[F(0), F(-1)], [F(-1), F(0)]]
    g = [[F(3), F(1)], [F(1), F(3)]]
    values = []
    for b in (F(1), F(2)):
        psi = [F(1), b]
        for initial in ([F(1, 2), F(1, 2)], [p*p/(1+b*b) for p in psi]):
            physical = [a/p for a, p in zip(initial, psi)]
            evolved = mv(g, physical)
            density = [p*x for p, x in zip(psi, evolved)]
            average = dot(local_energy(h, psi), density)/sum(density)
            functional = dot(psi, mv(h, evolved))/dot(psi, evolved)
            assert average == functional, "projector functional"
            values.append(average)
        assert values[-1] == endpoint_mean(h, g, psi), "matched projector boundary"
    assert values[2] != values[3], "different projector boundary witness"
    return list(map(str, values))


def covariance_cancellation():
    rows = []
    c = F(2, 3)
    scales = list(map(F, (1, 2, 3, 4, 5)))
    for signs in product((-1, 1), repeat=5):
        xa, xb, za, zb, y = [s*v for s, v in zip(signs, scales)]
        ca = c*(15*xa-16*y+za)
        cb = c*(15*xb-16*y+zb)
        difference = c*(15*(xa-xb)+za-zb)
        assert ca-cb == difference, "shared middle observation cancellation"
        rows.append((ca, cb, difference))
    va, vb, vd = [sum(row[i]**2 for row in rows)/len(rows) for i in range(3)]
    covariance = sum(row[0]*row[1] for row in rows)/len(rows)
    prediction = c*c*(225*(scales[0]**2+scales[1]**2)+scales[2]**2+scales[3]**2)
    assert vd == prediction == va+vb-2*covariance, "curvature covariance"
    assert va+vb-vd == 512*c*c*scales[4]**2, "double-counted middle variance"
    return {"difference_variance": str(vd), "naive_extra_variance": str(va+vb-vd)}


def main():
    print(json.dumps({
        "path_cancellation_examples": path_cancellation(),
        "lifted_bounce_states": bounce_balance(),
        "endpoint_and_spectral_energies": endpoint_and_spectral(),
        "cap_endpoint_and_rayleigh": capped_noncommutation(),
        "projector_boundary_means": projector_boundary(),
        "shared_curvature_covariance": covariance_cancellation(),
        "scope": "Exact finite examples for supplied matrices and ideal algorithms; no simulation, mixing, large-volume, observational or audit conclusion.",
    }, indent=2))


if __name__ == "__main__":
    main()
