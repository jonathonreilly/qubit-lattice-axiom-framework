"""Independent checks for the Lane RFW/F2 referee.

This intentionally does not import the worker's f2_common.py.  It rebuilds the
reduced first-jet system from the on-shell identity T0 = grad(E) tensor f and
uses a closed-form proportional-v witness instead of the worker's random root
finder.
"""

import numpy as np


D = 4
COMPS = [(i, j) for i in range(D) for j in range(i, D)]
W = np.array([1.0 if i == j else 2.0 for i, j in COMPS])
RNG = np.random.default_rng(8_675_309)


def shell_point(m2, lattice):
    p = RNG.normal(size=D) * 0.9 + 1j * RNG.normal(size=D) * 0.35
    if lattice:
        c3 = 1 + 0.5 * (np.sum(2 - 2 * np.cos(p[:3])) + m2)
        p[3] = np.arccos(c3 + 0j) * RNG.choice((-1, 1))
        assert abs(np.sum(2 - 2 * np.cos(p)) + m2) < 1e-10
    else:
        p[3] = np.sqrt(-(np.sum(p[:3] ** 2) + m2) + 0j) * RNG.choice((-1, 1))
        assert abs(np.sum(p * p) + m2) < 1e-10
    return p


def tangent_basis(n):
    pivot = int(np.argmax(np.abs(n)))
    out = []
    for _ in range(3):
        t = RNG.normal(size=D) + 1j * RNG.normal(size=D)
        t[pivot] -= np.dot(n, t) / n[pivot]
        assert abs(np.dot(n, t)) < 1e-10 * (1 + np.max(np.abs(t)))
        out.append(t)
    return out


def reduced_jet(m2, lattice, npoints=300):
    """Solve (F) after the independently proved consequence (Z) => A0 = 0."""
    rows = [[] for _ in COMPS]
    rhs = [[] for _ in COMPS]
    t0_values = []
    for _ in range(npoints):
        p = shell_point(m2, lattice)
        v = np.sin(p) if lattice else p
        n = 2 * v
        # T0 = n tensor f, with f=v in both the lattice and continuum controls.
        t0 = 2 * W * np.array([v[i] * v[j] for i, j in COMPS])
        t0_values.append(t0)
        scale = 1 / np.linalg.norm(t0)
        for t in tangent_basis(n):
            grad_fc_dot_t = np.cos(p[0]) * t[0] if lattice else t[0]
            row = np.concatenate([t[mu] * t0 for mu in range(D)]) * scale
            for a in range(len(COMPS)):
                rows[a].append(row)
                rhs[a].append(1j * grad_fc_dot_t * t0[a] * scale)

    numerator = 0.0
    denominator = 0.0
    ranks = []
    for a in range(len(COMPS)):
        matrix = np.asarray(rows[a])
        target = np.asarray(rhs[a])
        coeff, *_ = np.linalg.lstsq(matrix, target, rcond=None)
        numerator += np.linalg.norm(matrix @ coeff - target) ** 2
        denominator += np.linalg.norm(target) ** 2
        ranks.append(np.linalg.matrix_rank(matrix, tol=1e-9 * np.linalg.norm(matrix, 2)))
    return (
        np.sqrt(numerator / denominator),
        sorted(set(ranks)),
        np.linalg.matrix_rank(np.asarray(t0_values)),
    )


def jet_map_rank(radius):
    offsets = [
        np.asarray(raw) - radius
        for raw in np.ndindex(*(2 * radius + 1,) * D)
        if np.sum(np.abs(np.asarray(raw) - radius)) <= radius
    ]
    offsets = np.asarray(offsets)
    matrix = np.vstack((np.ones(len(offsets)), *(1j * offsets[:, mu] for mu in range(D))))
    return len(offsets), np.linalg.matrix_rank(matrix)


def algebraic_witness(m2):
    """Two exact shell points with identical v=sin(p) and opposite cos(p0).

    Put C=4+m2/2, a=C/2, and s^2=1-a^2.  The cosine vectors
    (a,a,a,-a) and (-a,a,a,a) both sum to C.  Giving both the same sine
    vector (s,s,s,s) therefore produces two complex shell points on the same
    v-ray.  For physical m2>=0, a>=2, so s and v1*v2^2 are nonzero.
    """
    C = 4 + m2 / 2
    a = C / 2
    s = np.sqrt(1 - a * a + 0j)
    v = np.full(D, s, dtype=complex)
    cos_plus = np.array([a, a, a, -a], dtype=complex)
    cos_minus = np.array([-a, a, a, a], dtype=complex)
    return {
        "shell_plus": np.sum(2 - 2 * cos_plus) + m2,
        "shell_minus": np.sum(2 - 2 * cos_minus) + m2,
        "trig_error": max(
            np.max(np.abs(cos_plus**2 + v**2 - 1)),
            np.max(np.abs(cos_minus**2 + v**2 - 1)),
        ),
        "cos0_difference": cos_plus[0] - cos_minus[0],
        "denominator_abs": abs(v[1] * v[2] ** 2),
    }


print("Independent reduced 1-jet system (no worker imports; A0 already eliminated):")
for lattice, label in ((False, "continuum"), (True, "lattice")):
    for mass2 in (0.0, 0.25, 1.0, 3.0):
        residual, ranks, span = reduced_jet(mass2, lattice)
        print(
            f"  {label:9s} m2={mass2:4.2f}: residual={residual:.12g} "
            f"rank(M)={ranks} span(T0)={span}/10"
        )

print("\nJet-map ranks:")
for radius in range(4):
    count, rank = jet_map_rank(radius)
    print(f"  r={radius}: offsets={count}, rank={rank}")

print("\nClosed-form proportional-v witnesses:")
for mass2 in (0.0, 0.25, 1.0, 3.0):
    values = algebraic_witness(mass2)
    print(
        f"  m2={mass2:4.2f}: |shell|=({abs(values['shell_plus']):.3g},"
        f"{abs(values['shell_minus']):.3g}), trig_error={values['trig_error']:.3g}, "
        f"cos0_difference={values['cos0_difference']}, "
        f"|v1*v2^2|={values['denominator_abs']:.12g}"
    )
    assert abs(values["shell_plus"]) < 1e-12
    assert abs(values["shell_minus"]) < 1e-12
    assert values["trig_error"] < 1e-12
    assert abs(values["cos0_difference"]) > 1
    assert values["denominator_abs"] > 1
