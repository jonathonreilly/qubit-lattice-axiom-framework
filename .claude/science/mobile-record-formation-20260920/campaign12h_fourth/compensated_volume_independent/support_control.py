"""Exact decorated-lattice support bounds, assembled independently."""
import itertools
import json
from pathlib import Path


def neighbors(x):
    for i in range(len(x)):
        for sign in (-1, 1):
            y = list(x)
            y[i] += sign
            yield tuple(y)


def edge(x, y):
    a, b = (x, y) if sum(x) % 2 == 0 else (y, x)
    return ('e', a, b)


def star(a):
    out = {('v', a)}
    for b in neighbors(a):
        out.add(('v', b))
        out.add(edge(a, b))
    return out


def electric_enlargement(x):
    incident = {factor for factor in x if factor[0] == 'e'}
    for factor in x:
        if factor[0] == 'v':
            incident.update(edge(factor[1], b) for b in neighbors(factor[1]))
    out = set(x)
    for e in incident:
        out.update((e, ('v', e[1]), ('v', e[2])))
    return out


def dist(x, y):
    if x == y:
        return 0
    xx = x[1:] if x[0] == 'e' else (x[1],)
    yy = y[1:] if y[0] == 'e' else (y[1],)
    physical = min(sum(abs(a-b) for a, b in zip(u, v)) for u in xx for v in yy)
    return 2*physical + int(x[0] == 'e') + int(y[0] == 'e')


def diameter(x):
    return max(dist(a, b) for a in x for b in x)


def check(d):
    zero = (0,)*d
    close_A = [x for x in itertools.product(range(-2, 3), repeat=d)
               if sum(map(abs, x)) == 2]
    assert len(close_A) == 2*d*d
    pairs = []
    for c in close_A:
        common = set(neighbors(zero)).intersection(neighbors(c))
        assert common
        original = star(zero) | star(c)
        enlarged = electric_enlargement(original)
        assert original <= enlarged
        assert diameter(original) <= 8
        assert diameter(enlarged) <= 12
        pairs.append({'c': c, 'common_B': len(common),
                      'original_factors': len(original), 'enlarged_factors': len(enlarged),
                      'original_incidence_diameter': diameter(original),
                      'enlarged_incidence_diameter': diameter(enlarged)})
    jump = star(zero)
    jump_plus = electric_enlargement(jump)
    assert diameter(jump) == 4 and diameter(jump_plus) == 8
    assert max(x['enlarged_incidence_diameter'] for x in pairs) == 12
    return {'d': d, 'A_neighbors_sharing_B': len(close_A),
            'jump_original_diameter': diameter(jump), 'jump_enlarged_diameter': diameter(jump_plus),
            'maximum_pair_enlarged_diameter': 12, 'all_pair_rows': pairs}


if __name__ == '__main__':
    rows = [check(d) for d in (2, 3, 4)]
    result = {'method': 'exact incidence distances and local electric-support union; no author imports',
              'rows': rows, 'proof_boundary': 'Commutativity, not iterative support expansion, proves that only one enlargement is needed.'}
    target = Path(__file__).resolve().parent/'SUPPORT_RESULTS.json'
    if target.exists():
        raise FileExistsError(target)
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': 'passed', 'dimensions': [x['d'] for x in rows],
                      'pair_diameter_after_one_electric_enlargement': 12,
                      'jump_diameter_after_one_electric_enlargement': 8,
                      'output': str(target)}, indent=2))
