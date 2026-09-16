"""Exact rational-angle challenge to the raw-curl stability comparison.

The domain is a 3 by 3 vertex free square, not an isolated abstract face.
Rational arithmetic verifies the connection and its face curls; a rational
lower bound pi > 3 certifies the violated inequality without floating error.
This does not evaluate any theorem beyond the displayed comparison.
"""
AUDIT_TIMEOUT_SEC = 180
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import math


def main():
    vertices = list(product(range(-1, 2), repeat=2))
    phi = {v: F(0) for v in vertices}
    phi.update({(1, 0): F(1, 2), (1, 1): F(1), (0, 1): F(-1, 2)})
    theta, lifted = {}, {}
    for x in vertices:
        for j in range(2):
            y = tuple(x[k] + (k == j) for k in range(2))
            if y not in phi:
                continue
            q = phi[y] - phi[x]
            lifted[x, j] = q
            theta[x, j] = (q + 1) % 2 - 1

    def curl(field, x):
        return (field[x, 0] + field[(x[0] + 1, x[1]), 1]
                - field[(x[0], x[1] + 1), 0] - field[x, 1])

    faces = [x for x in vertices if x[0] < 1 and x[1] < 1]
    raw_curl = {x: (curl(theta, x)+1)%2-1 for x in faces}
    exact_curl = {x: curl(lifted, x) for x in faces}
    assert all(q == 0 for q in exact_curl.values())
    assert sorted(raw_curl.values()) == [0, 0, 0, 2]
    assert all(-1 < q < 1 for q in theta.values())
    assert all(q % 2 == 0 for q in raw_curl.values())

    cosine_half_turns = {F(0): F(1), F(1, 2): F(0), F(-1, 2): F(0)}
    mass_energy = sum(1 - cosine_half_turns[q] for q in theta.values())
    theta_norm = sum(q * q for q in theta.values())
    curl_norm = sum(q * q for q in raw_curl.values())
    assert (mass_energy, theta_norm, curl_norm) == (6, F(3, 2), 4)
    m = F(1, 10)
    lhs = m * mass_energy
    rhs_pi2_coefficient = (curl_norm + m * theta_norm) / 10
    assert lhs == F(3, 5)
    assert rhs_pi2_coefficient == F(83, 200)
    assert 9 * rhs_pi2_coefficient > lhs

    # A principal FACE curl vanishes. Confusing it with the raw real curl
    # would erase this witness and change the proposed Gaussian action.
    principal_curl = {x: (q + 1) % 2 - 1 for x, q in raw_curl.items()}
    assert all(q == 0 for q in principal_curl.values())
    result = {
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "domain": "free square with vertices {-1,0,1}^2",
        "vertices": len(vertices), "links": len(theta), "faces": len(faces),
        "nonzero_link_angles_over_pi": [str(q) for q in theta.values() if q],
        "raw_curls_over_pi": {str(x): str(q) for x, q in raw_curl.items()},
        "theta_norm_squared_over_pi_squared": str(theta_norm),
        "curl_norm_squared_over_pi_squared": str(curl_norm),
        "mass": str(m), "action": str(lhs),
        "claimed_lower_bound": float(rhs_pi2_coefficient) * math.pi ** 2,
        "exact_failure_certificate": "9*(83/200) > 3/5 and pi^2 > 9",
        "principal_face_curls_vanish": True,
        "scope": "counterexample to the displayed raw-curl comparison only",
        "status": "PASS"
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
