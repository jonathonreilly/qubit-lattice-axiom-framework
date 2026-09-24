"""Exact cube high-flux birth control, independent of repository builders.

This is a finite path calculation, not an autonomous-reservoir model.
"""
import json

A = {0, 3, 5, 6}
EDGES = [(x, y) for x in range(8) for y in range(x + 1, 8)
         if (x ^ y).bit_count() == 1]
EDGE = {pair: i for i, pair in enumerate(EDGES)}


def gauss(q, field):
    divergence = [0] * 8
    for (x, y), value in zip(EDGES, field):
        divergence[x] += value
        divergence[y] -= value
    return all(divergence[x] == q[x] - int(x in A) for x in range(8))


def electric(q, field):
    assert all(q[a] for a in A)
    value = 0
    for e, (x, y) in enumerate(EDGES):
        if x in A and q[y] == 0:
            value += field[e] * (field[e] - q[x])
        if y in A and q[x] == 0:
            value += field[e] * (field[e] + q[y])
    return value


def move(q, field, source, target):
    assert q[source] != 0 and q[target] == 0
    e = EDGE[tuple(sorted((source, target)))]
    shift = -q[source] if source < target else q[source]
    qq, ff = list(q), list(field)
    qq[target], qq[source] = qq[source], 0
    ff[e] += shift
    assert gauss(qq, ff)
    return qq, ff


def birth(q, field, charge=1):
    assert q[0] == q[1] == 0
    qq, ff = list(q), list(field)
    qq[0], qq[1] = charge, -charge
    ff[EDGE[0, 1]] += charge
    assert gauss(qq, ff)
    return qq, ff


def initial(n):
    q = [int(x in A) for x in range(8)]
    f = [0] * 12
    for edge, sign in [((0, 1), 1), ((1, 3), 1),
                       ((2, 3), -1), ((0, 2), -1)]:
        f[EDGE[edge]] = sign * n
    assert gauss(q, f)
    return q, f


def run():
    rows = []
    for n in [0, 1, 2, 3, 7, 19, 100]:
        q, f = initial(n)
        assert electric(q, f) == 4 * n * n
        output = []
        for old_destination in [2, 4]:
            mid_q, mid_f = move(q, f, 0, old_destination)
            out_q, out_f = birth(mid_q, mid_f)
            value = electric(out_q, out_f)
            expected = 0 if old_destination == 2 else 2 * n * n
            assert value == expected
            assert sum(x != 0 for x in out_q) == 6
            output.append({"old_destination": old_destination,
                           "D": value, "charges": out_q, "field": out_f})
        assert output[0]["charges"] != output[1]["charges"]
        rows.append({"n": n, "initial_D": 4 * n * n,
                     "resolved_first_mark_squared_norm": 2,
                     "conditional_post_D_mean": n * n,
                     "conditional_post_D_variance": n ** 4,
                     "outputs": output})
    return {"graph": "cube", "oriented_edges": EDGES,
            "marked_edge": [0, 1], "birth_charge_at_0": 1,
            "claim": "exact diagonal electric energies for an actual resolved first mark",
            "rows": rows}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
