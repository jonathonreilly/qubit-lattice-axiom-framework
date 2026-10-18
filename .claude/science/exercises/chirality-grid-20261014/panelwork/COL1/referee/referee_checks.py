"""Independent low-memory checks for the COL-1 referee report.

This deliberately does not import the worker's constraint checker.  It checks
the occupation-changing pair-creation gate (which the worker's colour-blind
parse test does not cover) and gives an explicit counterexample to the broad
"shared physical qubits are classical" reading of OWN.
"""

from itertools import product
import numpy as np


def onehot_or_empty(n=3):
    return [tuple(1 if i == j else 0 for i in range(n)) for j in range(n)] + [(0,) * n]


def sat(constraints):
    """Exact finite-domain CSP solver, written independently of parse_lemma.py."""
    constraints = [(tuple(pos), tuple(allowed)) for pos, allowed in constraints]
    assignment = {}

    def options(index):
        pos, allowed = constraints[index]
        return [values for values in allowed
                if all(p not in assignment or assignment[p] == v
                       for p, v in zip(pos, values))]

    def search(remaining):
        if not remaining:
            return True
        scored = [(len(options(i)), i) for i in remaining]
        count, chosen = min(scored)
        if count == 0:
            return False
        rest = [i for i in remaining if i != chosen]
        pos, _ = constraints[chosen]
        for values in options(chosen):
            added = []
            for p, v in zip(pos, values):
                if p not in assignment:
                    assignment[p] = v
                    added.append(p)
            if search(rest):
                return True
            for p in added:
                del assignment[p]
        return False

    return search(list(range(len(constraints))))


def negate_constraint(constraint):
    pos, allowed = constraint
    allowed = set(allowed)
    return pos, {bits for bits in product((0, 1), repeat=len(pos)) if bits not in allowed}


def pullback(predicate, changes):
    """Predicate on the target bits, pulled back through a fixed bit update."""
    out = []
    for pos, allowed in predicate:
        allowed = set(allowed)
        source_allowed = set()
        for source in product((0, 1), repeat=len(pos)):
            target = tuple(changes.get(p, value) for p, value in zip(pos, source))
            if target in allowed:
                source_allowed.add(source)
        out.append((pos, source_allowed))
    return out


def xor_satisfiable(base, source_predicate, target_predicate, source_fixed_zero=()):
    """Whether base admits a state where a predicate changes truth value."""
    fixed = set(source_fixed_zero)
    for source_constraint, target_constraint in zip(source_predicate, target_predicate):
        pos = source_constraint[0]
        source_allowed = set(source_constraint[1])
        target_allowed = set(target_constraint[1])
        can_toggle = any(values in source_allowed and values not in target_allowed
                         and all(values[i] == 0 for i, p in enumerate(pos) if p in fixed)
                         for values in product((0, 1), repeat=len(pos)))
        if not can_toggle:
            continue
        if sat(base + source_predicate + [negate_constraint(target_constraint)]):
            return True
    for source_constraint, target_constraint in zip(source_predicate, target_predicate):
        pos = source_constraint[0]
        source_allowed = set(source_constraint[1])
        target_allowed = set(target_constraint[1])
        can_toggle = any(values in target_allowed and values not in source_allowed
                         and all(values[i] == 0 for i, p in enumerate(pos) if p in fixed)
                         for values in product((0, 1), repeat=len(pos)))
        if not can_toggle:
            continue
        if sat(base + target_predicate + [negate_constraint(source_constraint)]):
            return True
    return False


def z1_predicates():
    token = 19

    def group(z, offset):
        return tuple(range(z + offset, z + offset + 3))

    def valid(z):
        matter = set()
        for q in onehot_or_empty():
            for p in onehot_or_empty():
                if sum(q) + sum(p) <= 1:
                    matter.add(q + (0,) + p + (0,))
        link = set()
        for a in onehot_or_empty():
            for b in onehot_or_empty():
                if sum(a) == sum(b):
                    link.add(a + (0,) + b + (0,))
        return [((z, z + 1, z + 2), {(1, 1, 0)}),
                (tuple(range(z + 3, z + 11)), matter),
                (tuple(range(z + 11, z + 19)), link)]

    def gauge_gate(x):
        return valid(x) + valid(x - token)

    x, y = 0, token
    emptied = [group(x, o) for o in (3, 7, 11, 15)] + [group(y, o) for o in (3, 7)]
    base = gauge_gate(y) + [(g, {(0, 0, 0)}) for g in emptied]
    y_support = {p for constraint in gauge_gate(y) for p in constraint[0]}
    candidates = []
    for z in range(-2 * token - 2, 3 * token + 3):
        z_gate = gauge_gate(z)
        z_support = {p for constraint in z_gate for p in constraint[0]}
        if y_support.intersection(z_support) and sat(gauge_gate(y) + z_gate):
            candidates.append(z)
    violations = []
    for a, b in product(range(3), repeat=2):
        changes = {}
        for g, colour in ((group(x, 3), a), (group(x, 11), a),
                          (group(x, 15), b), (group(y, 7), b)):
            for i, site in enumerate(g):
                changes[site] = int(i == colour)
        for z in candidates:
            source = gauge_gate(z)
            target = pullback(source, changes)
            if xor_satisfiable(base, source, target, changes):
                violations.append((a, b, z))
    return violations


def z3_predicates():
    token = 35

    def add(p, d):
        return tuple(a + b for a, b in zip(p, d))

    def row(p, offset):
        return add(p, (offset, 0, 0))

    def group(p, offset):
        return tuple(row(p, offset + i) for i in range(3))

    units = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    def near(p, direction):
        if direction == 0:
            return add(p, (-token, 0, 0))
        return add(p, tuple(-v for v in units[direction]))

    def valid(p):
        matter = set()
        for q in onehot_or_empty():
            for aq in onehot_or_empty():
                if sum(q) + sum(aq) <= 1:
                    matter.add(q + (0,) + aq + (0,))
        link = set()
        for a in onehot_or_empty():
            for b in onehot_or_empty():
                if sum(a) == sum(b):
                    link.add(a + (0,) + b + (0,))
        constraints = [((row(p, 0), row(p, 1), row(p, 2)), {(1, 1, 0)}),
                       (tuple(row(p, o) for o in range(3, 11)), matter)]
        constraints.extend((tuple(row(p, o) for o in range(11 + 8 * k, 19 + 8 * k)), link)
                           for k in range(3))
        return constraints

    def gauge_gate(p):
        constraints = valid(p)
        for direction in range(3):
            constraints += valid(near(p, direction))
        return constraints

    p = (0, 0, 0)
    y = (0, 1, 0)
    q_p, aq_p = group(p, 3), group(p, 7)
    a_y, b_y = group(p, 19), group(p, 23)
    q_y, aq_y = group(y, 3), group(y, 7)
    emptied = (q_p, aq_p, a_y, b_y, q_y, aq_y)
    base = gauge_gate(y) + [(g, {(0, 0, 0)}) for g in emptied]
    # The worker's exact parse pass found precisely these nonzero relative
    # displacements.  Here they are inputs to an independent check of the
    # additional occupation-changing gate obligation that parse pass omitted.
    compatible_relative = [
        (-35, 0, 0), (-35, 0, 1), (-35, 1, 0),
        (0, -1, 0), (0, -1, 1), (0, 0, -1),
        (0, 0, 1), (0, 1, -1), (0, 1, 0),
        (35, -1, 0), (35, 0, -1), (35, 0, 0),
    ]
    candidates = [y] + [add(y, displacement) for displacement in compatible_relative]
    violations = []
    for a, b in product(range(3), repeat=2):
        changes = {}
        for g, colour in ((q_p, a), (a_y, a), (b_y, b), (aq_y, b)):
            for i, site in enumerate(g):
                changes[site] = int(i == colour)
        for z in candidates:
            source = gauge_gate(z)
            if not set(changes).intersection(site for constraint in source for site in constraint[0]):
                continue
            target = pullback(source, changes)
            if xor_satisfiable(base, source, target, changes):
                violations.append((a, b, z))
    return violations


def gell_mann_halves():
    matrices = np.zeros((8, 3, 3), complex)
    matrices[0, 0, 1] = matrices[0, 1, 0] = 1
    matrices[1, 0, 1], matrices[1, 1, 0] = -1j, 1j
    matrices[2, 0, 0], matrices[2, 1, 1] = 1, -1
    matrices[3, 0, 2] = matrices[3, 2, 0] = 1
    matrices[4, 0, 2], matrices[4, 2, 0] = -1j, 1j
    matrices[5, 1, 2] = matrices[5, 2, 1] = 1
    matrices[6, 1, 2], matrices[6, 2, 1] = -1j, 1j
    matrices[7] = np.diag((1, 1, -2)) / np.sqrt(3)
    return matrices / 2


def own_counterexample():
    """Two commuting SU(3)s sharing two physical qubits quantumly."""
    t = gell_mann_halves()
    rep = np.pad(t, ((0, 0), (0, 1), (0, 1)))  # 3 + 1 on two qubits
    identity4 = np.eye(4)
    # CNOT from overlap qubit q1 to overlap qubit q2, surrounded by q0 and q3.
    cnot = np.array([[1, 0, 0, 0], [0, 1, 0, 0],
                     [0, 0, 0, 1], [0, 0, 1, 0]], complex)
    u = np.kron(np.eye(2), np.kron(cnot, np.eye(2)))
    left = [u @ np.kron(r, identity4) @ u.conj().T for r in rep]
    right = [u @ np.kron(identity4, r) @ u.conj().T for r in rep]
    cross = max(np.max(np.abs(a @ b - b @ a)) for a in left for b in right)

    x = np.array([[0, 1], [1, 0]], complex)
    z = np.diag((1, -1)).astype(complex)
    local = []
    for site in (1, 2):
        for pauli in (x, z):
            factors = [np.eye(2)] * 4
            factors[site] = pauli
            op = factors[0]
            for factor in factors[1:]:
                op = np.kron(op, factor)
            local.append((site, op))
    touches = {}
    for name, algebra in (("left", left), ("right", right)):
        for site in (1, 2):
            touches[name, site] = max(np.max(np.abs(g @ op - op @ g))
                                      for g in algebra for s, op in local if s == site)
    return cross, touches


if __name__ == "__main__":
    cross, touches = own_counterexample()
    print("OWN counterexample: max cross commutator = %.1e" % cross)
    print("OWN counterexample: local-touch commutator norms =", touches)
    print("Z1 pair-creation gate predicate-toggle witnesses =", z1_predicates())
    print("Z3 y-link pair-creation gate predicate-toggle witness count =", len(z3_predicates()))
