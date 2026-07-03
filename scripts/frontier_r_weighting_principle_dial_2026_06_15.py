from fractions import Fraction
import math
import random
import sys


TOL = 1e-10


def eye(n):
    return [[1.0 + 0.0j if i == j else 0.0 + 0.0j for j in range(n)] for i in range(n)]


def zero(n):
    return [[0.0 + 0.0j for _ in range(n)] for _ in range(n)]


def add(*matrices):
    n = len(matrices[0])
    out = zero(n)
    for matrix in matrices:
        for i in range(n):
            for j in range(n):
                out[i][j] += matrix[i][j]
    return out


def sub(a, b):
    n = len(a)
    return [[a[i][j] - b[i][j] for j in range(n)] for i in range(n)]


def scale(matrix, factor):
    n = len(matrix)
    return [[factor * matrix[i][j] for j in range(n)] for i in range(n)]


def mul(a, b):
    n = len(a)
    out = zero(n)
    for i in range(n):
        for j in range(n):
            out[i][j] = sum(a[i][k] * b[k][j] for k in range(n))
    return out


def adjoint(matrix):
    n = len(matrix)
    return [[matrix[j][i].conjugate() for j in range(n)] for i in range(n)]


def trace(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


def fro_norm(matrix):
    return math.sqrt(sum(abs(entry) ** 2 for row in matrix for entry in row))


def close_value(a, b, tol=TOL):
    return abs(a - b) <= tol


def close_matrix(a, b, tol=TOL):
    return fro_norm(sub(a, b)) <= tol


def outer(v, w):
    return [[v[i] * w[j].conjugate() for j in range(len(v))] for i in range(len(v))]


def matrix_from_columns(columns):
    return [[columns[j][i] for j in range(len(columns))] for i in range(len(columns[0]))]


def r_from_weights(w_singlet, w_doublet):
    assert w_singlet > 0
    assert w_singlet + w_doublet == 1
    return w_doublet / (2 * w_singlet)


def q_from_r(r):
    return Fraction(1, 3) + Fraction(2, 3) * r


def state_from_weights(p_singlet, p_doublet, w_singlet, w_doublet):
    return add(
        scale(p_singlet, float(w_singlet)),
        scale(p_doublet, float(w_doublet) / 2.0),
    )


def block_weight(projector, rho):
    return trace(mul(projector, rho)).real


def record_map(p_singlet, p_doublet, rho):
    return add(mul(mul(p_singlet, rho), p_singlet), mul(mul(p_doublet, rho), p_doublet))


def random_density(seed):
    rng = random.Random(seed)
    a = [
        [complex(rng.uniform(-1, 1), rng.uniform(-1, 1)) for _ in range(3)]
        for _ in range(3)
    ]
    rho = mul(a, adjoint(a))
    return scale(rho, 1.0 / trace(rho).real)


class GateRunner:
    def __init__(self):
        self.pass_count = 0
        self.fail_count = 0

    def check(self, name, condition):
        if condition:
            self.pass_count += 1
            print(f"PASS: {name}")
        else:
            self.fail_count += 1
            print(f"FAIL: {name}")

    def finish(self):
        print(f"TOTAL: PASS={self.pass_count} FAIL={self.fail_count}")
        if self.fail_count:
            sys.exit(1)


def main():
    gates = GateRunner()

    ident = eye(3)
    c = [
        [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j],
        [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
        [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
    ]
    c2 = mul(c, c)
    c3 = mul(c2, c)
    s = add(c, c2)
    p_singlet = scale(add(s, ident), 1.0 / 3.0)
    p_doublet = sub(ident, p_singlet)

    gates.check("cyclic shift has order three", close_matrix(c3, ident))
    gates.check(
        "singlet projector is the +2 eigenspace",
        close_matrix(mul(s, p_singlet), scale(p_singlet, 2.0)),
    )
    gates.check(
        "doublet projector is the -1 eigenspace",
        close_matrix(mul(s, p_doublet), scale(p_doublet, -1.0)),
    )
    gates.check(
        "projectors are complete and orthogonal with ranks 1 and 2",
        close_matrix(add(p_singlet, p_doublet), ident)
        and close_matrix(mul(p_singlet, p_singlet), p_singlet)
        and close_matrix(mul(p_doublet, p_doublet), p_doublet)
        and close_matrix(mul(p_singlet, p_doublet), zero(3))
        and close_value(trace(p_singlet).real, 1.0)
        and close_value(trace(p_doublet).real, 2.0),
    )

    dim_weights = (Fraction(1, 3), Fraction(2, 3))
    equal_sector_weights = (Fraction(1, 2), Fraction(1, 2))
    r_dim = r_from_weights(*dim_weights)
    q_dim = q_from_r(r_dim)
    r_equal = r_from_weights(*equal_sector_weights)
    q_equal = q_from_r(r_equal)

    gates.check("dimension weighting computes r=1 and Q=1", r_dim == 1 and q_dim == 1)
    gates.check(
        "equal-sector weighting computes r=1/2 and Q=2/3",
        r_equal == Fraction(1, 2) and q_equal == Fraction(2, 3),
    )
    gates.check("the two weighting principles give different r", r_dim != r_equal)

    for label, weights in (
        ("dimension", dim_weights),
        ("equal-sector", equal_sector_weights),
    ):
        rho = state_from_weights(p_singlet, p_doublet, *weights)
        gates.check(
            f"{label} state realizes the declared block weights",
            close_value(trace(rho).real, 1.0)
            and close_matrix(rho, adjoint(rho))
            and close_value(block_weight(p_singlet, rho), float(weights[0]))
            and close_value(block_weight(p_doublet, rho), float(weights[1])),
        )

    record_conserves_all_samples = True
    for seed in range(20260615, 20260620):
        rho = random_density(seed)
        recorded = record_map(p_singlet, p_doublet, rho)
        record_conserves_all_samples = record_conserves_all_samples and close_value(
            block_weight(p_singlet, recorded),
            block_weight(p_singlet, rho),
        )
        record_conserves_all_samples = record_conserves_all_samples and close_value(
            block_weight(p_doublet, recorded),
            block_weight(p_doublet, rho),
        )
    gates.check("record map conserves both block weights on random states", record_conserves_all_samples)

    u = [1.0 / math.sqrt(3.0)] * 3
    v = [1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0), 0.0]
    w = [1.0 / math.sqrt(6.0), 1.0 / math.sqrt(6.0), -2.0 / math.sqrt(6.0)]
    basis = matrix_from_columns([u, v, w])
    angle = 0.37
    rotation = [
        [math.cos(angle), -math.sin(angle), 0.0],
        [math.sin(angle), math.cos(angle), 0.0],
        [0.0, 0.0, 1.0],
    ]
    mixer = mul(mul(basis, rotation), adjoint(basis))
    pure_singlet = outer(u, u)
    mixed = mul(mul(mixer, pure_singlet), adjoint(mixer))
    gates.check(
        "non-block-diagonal unitary control changes a block weight",
        abs(block_weight(p_singlet, pure_singlet) - block_weight(p_singlet, mixed)) > 1e-3,
    )

    valid_outputs = {
        r_from_weights(*dim_weights),
        r_from_weights(*equal_sector_weights),
    }
    gates.check("firewall keeps r=1 and r=1/2 as valid map outputs", valid_outputs == {1, Fraction(1, 2)})

    gates.finish()


if __name__ == "__main__":
    main()
