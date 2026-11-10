#!/usr/bin/env python3
"""Independent global-state oracle for detector-refinement-v1 certificates.

No primary imports, parser calls, or certificate-provided expected probabilities.
Execution (including diagnostic self-enumerations) belongs to the supervisor's
numeric lease. This worker only syntax-checked the file.
"""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys


PALETTE = frozenset((0, 1, 2, 3, 4, 100, 101, 102, 103))
UNIT = Fraction(1)


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def integer(value, where):
    require(type(value) is int, where + ': expected integer, excluding bool')
    return value


def exact_keys(obj, names, where):
    require(type(obj) is dict and set(obj) == set(names), where + ': wrong object keys')


def coordinate(value, where):
    require(type(value) is list and len(value) == 3, where + ': expected coordinate list')
    return tuple(integer(x, where) for x in value)


def rational(value, where, probability=False):
    require(type(value) is list and len(value) == 2, where + ': expected rational pair')
    num, den = (integer(x, where) for x in value)
    require(den > 0, where + ': denominator must be positive')
    result = Fraction(num, den)
    require(result >= 0 and (not probability or result <= 1), where + ': invalid mass/rate')
    return result


def records(value, where):
    require(type(value) is list, where + ': expected records list')
    result = {}
    for entry in value:
        require(type(entry) is list and len(entry) == 2, where + ': malformed record')
        site = coordinate(entry[0], where)
        content = integer(entry[1], where)
        require(content in PALETTE, where + ': content outside protocol palette')
        require(site not in result, where + ': repeated record site')
        result[site] = content
    return result


def frozen(record_map):
    return tuple(sorted(record_map.items()))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def proper_frame(basis):
    return (all(dot(a, a) == 1 for a in basis)
            and all(dot(basis[i], basis[j]) == 0 for i in range(3) for j in range(i))
            and dot(basis[0], cross(basis[1], basis[2])) == 1)


def decode_seed(seed):
    """Global labelled-header reconstruction, never a local parser."""
    require(len(seed) == 25, 'seed must contain exactly 25 records')
    marker = {}
    for value in range(100, 104):
        locations = [site for site, content in seed.items() if content == value]
        require(len(locations) == 1, 'seed must have one of each header value')
        marker[value] = locations[0]
    origin = marker[100]
    basis = tuple(tuple(marker[v][d] - origin[d] for d in range(3)) for v in (101, 102, 103))
    require(proper_frame(basis), 'header does not encode a proper cubic frame')

    def place(local):
        return tuple(origin[d] + sum(local[j]*basis[j][d] for j in range(3)) for d in range(3))

    required = {(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 0, 0)}
    required.update((2+i, 2+t, 0) for i in range(4) for t in range(4))
    required.update((2+i, 6, 0) for i in range(4))
    require(set(seed) == {place(site) for site in required}, 'seed site set differs from template')
    selector = seed[place((2, 0, 0))]
    require(0 <= selector <= 3, 'invalid preparation selector')
    columns = tuple(tuple(seed[place((2+i, 2+t, 0))] for i in range(4)) for t in range(4))
    require(all(all(0 <= x <= 4 for x in col) and sum(col) == 4 for col in columns),
            'program columns must be compositions of four')
    groups = tuple(seed[place((2+i, 6, 0))] for i in range(4))
    require(all(g in (0, 1) for g in groups), 'invalid grouping bit')
    pool = tuple(place((2+j % 4, 8+(j//4) % 2, j//8)) for j in range(16))
    fine, coarse = place((0, 8, 0)), place((0, 9, 0))
    patch = set(seed) | set(pool) | {fine, coarse}
    require(len(patch) == 43, 'patch collision')
    require(all(sum(abs(a[d]-b[d]) for d in range(3)) <= 16 for a in patch for b in patch),
            'patch exceeds radius-sixteen all-pairs visibility')
    return dict(origin=origin, basis=basis, selector=selector, columns=columns,
                groups=groups, pool=pool, fine=fine, coarse=coarse)


def expected_graph(seed, decoded, q):
    """Construct all global prefixes by appending the three protocol records."""
    column = decoded['columns'][decoded['selector']]
    labels = tuple(i for i, count in enumerate(column) for _ in range(count ** q))
    require(1 <= len(labels) <= 16, 'invalid active pool size')
    graph = {frozen(seed): {decoded['pool'][j]: (1, UNIT) for j in range(len(labels))}}
    for j, outcome in enumerate(labels):
        stage = dict(seed)
        stage[decoded['pool'][j]] = 1
        graph[frozen(stage)] = {decoded['fine']: (outcome + 1, UNIT)}
        stage[decoded['fine']] = outcome + 1
        graph[frozen(stage)] = {decoded['coarse']: (decoded['groups'][outcome], UNIT)}
        stage[decoded['coarse']] = decoded['groups'][outcome]
        graph[frozen(stage)] = {}
    require(len(graph) == 1 + 3*len(labels), 'global-prefix state collision')
    return graph, labels


def expected_support(state, site, graph):
    remaining = dict(state)
    content = remaining.pop(site)
    enabling = graph.get(frozen(remaining), {}).get(site)
    if enabling is not None:
        return Fraction(int(content == enabling[0]))
    # All patch records are visible to every patch site. Absence is not value zero.
    k = len(remaining)
    ones = sum(value == 1 for value in remaining.values())
    p = (Fraction(1, 2) + ones) / (1 + k)
    mass = Fraction(1, 18)
    if content == 1:
        mass += p/2
    elif content == 0:
        mass += (1-p)/2
    return mass


def parse_events(value, where):
    require(type(value) is list, where + ': expected event list')
    result = {}
    for event in value:
        exact_keys(event, ('site', 'content', 'rate'), where)
        site = coordinate(event['site'], where)
        require(site not in result, where + ': repeated event site')
        result[site] = (integer(event['content'], where), rational(event['rate'], where))
    return result


def parse_support(value, where):
    require(type(value) is list, where + ': expected support list')
    result = {}
    for item in value:
        exact_keys(item, ('site', 'p_content'), where)
        site = coordinate(item['site'], where)
        require(site not in result, where + ': repeated support site')
        result[site] = rational(item['p_content'], where, probability=True)
    return result


def terminal_law(seed, graph, decoded):
    """Propagate exact competing-priority probabilities through the global DAG."""
    incoming = defaultdict(Fraction)
    incoming[frozen(seed)] = UNIT
    fine = [Fraction() for _ in range(4)]
    coarse = [Fraction(), Fraction()]
    for state in sorted(graph, key=len):
        events = graph[state]
        mass = incoming[state]
        require(mass > 0, 'unreachable generated state')
        if not events:
            rec = dict(state)
            fine[rec[decoded['fine']]-1] += mass
            coarse[rec[decoded['coarse']]] += mass
            continue
        total_rate = sum(rate for _, rate in events.values())
        for site, (content, rate) in events.items():
            next_records = dict(state)
            require(site not in next_records, 'attempt to rewrite a record')
            next_records[site] = content
            target = frozen(next_records)
            require(target in graph, 'event target absent from complete graph')
            incoming[target] += mass * rate / total_rate
    require(sum(fine) == sum(coarse) == 1, 'terminal probability loss')
    return tuple(fine), tuple(coarse)


def check_case(case, index):
    prefix = 'case[%d]' % index
    exact_keys(case, ('name', 'q', 'seed', 'nodes'), prefix)
    require(type(case['name']) is str, prefix + ': name must be a string')
    q = integer(case['q'], prefix)
    require(q in (1, 2), prefix + ': q must be one or two')
    seed = records(case['seed'], prefix + '.seed')
    decoded = decode_seed(seed)
    graph, labels = expected_graph(seed, decoded, q)
    require(type(case['nodes']) is list, prefix + ': nodes must be a list')
    seen, min_mass = set(), UNIT
    support_count = 0
    for ni, node in enumerate(case['nodes']):
        where = prefix + '.nodes[%d]' % ni
        exact_keys(node, ('records', 'events', 'support'), where)
        rec = records(node['records'], where)
        state = frozen(rec)
        require(state not in seen, where + ': duplicate global state')
        require(state in graph, where + ': state outside reachable prefix graph')
        seen.add(state)
        require(parse_events(node['events'], where) == graph[state], where + ': event mismatch')
        masses = parse_support(node['support'], where)
        require(set(masses) == set(rec), where + ': support entries must cover exactly present sites')
        for site, claimed in masses.items():
            expected = expected_support(rec, site, graph)
            require(claimed == expected, where + ': support mass mismatch at ' + str(site))
            require(expected > 0, where + ': an old record has lost admissibility')
            min_mass = min(min_mass, expected)
            support_count += 1
    require(seen == set(graph), prefix + ': omitted reachable states')
    fine, coarse = terminal_law(seed, graph, decoded)
    # A second route: equal continuous iid priorities make each active slot equiprobable.
    counts = Counter(labels)
    require(fine == tuple(Fraction(counts[i], len(labels)) for i in range(4)),
            prefix + ': graph probability disagrees with uniform-priority argument')
    return dict(q=q, decoded=decoded, fine=fine, coarse=coarse,
                nodes=len(graph), supports=support_count, min_mass=min_mass)


def compositions4():
    return {v for v in itertools.product(range(5), repeat=4) if sum(v) == 4}


def all_frames():
    axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    result = set()
    for permutation in itertools.permutations(axes):
        for signs in itertools.product((-1, 1), repeat=3):
            basis = tuple(tuple(signs[j]*x for x in permutation[j]) for j in range(3))
            if proper_frame(basis):
                result.add(basis)
    return result


def response_vector(columns, groups, q):
    return tuple(Fraction(sum(g*n**q for g, n in zip(groups, col)), sum(n**q for n in col))
                 for col in columns)


def coverage(checked):
    composed, orbits, named_menus = set(), set(), set()
    tomography = defaultdict(set)
    menu_probabilities = defaultdict(set)
    for result in checked:
        d, q = result['decoded'], result['q']
        cols, groups = d['columns'], d['groups']
        if d['selector'] == 0 and cols[1:] == ((4, 0, 0, 0),)*3:
            composed.add((q, cols[0]))
        if cols == ((1, 1, 2, 0),)*4 and groups == (1, 1, 0, 0):
            orbits.add((q, d['origin'], d['basis']))
        for name, menu, grouping in (('direct', (2, 2, 0, 0), (1, 0, 0, 0)),
                                     ('refined', (1, 1, 2, 0), (1, 1, 0, 0))):
            if d['selector'] == 0 and cols == (menu,)*4 and groups == grouping:
                named_menus.add((q, name))
                menu_probabilities[(q, name)].add(result['coarse'][1])
        if response_vector(cols, groups, q) == (1, 1, 0, 0):
            tomography[(cols, groups)].add((q, d['selector']))
    required_compositions = {(q, c) for q in (1, 2) for c in compositions4()}
    required_orbits = {(q, origin, frame) for q in (1, 2)
                       for origin in ((0, 0, 0), (7, -5, 3)) for frame in all_frames()}
    required_menus = {(q, name) for q in (1, 2) for name in ('direct', 'refined')}
    required_tomography = {(q, s) for q in (1, 2) for s in range(4)}
    best_tomography = max((len(v & required_tomography) for v in tomography.values()), default=0)
    missing = dict(compositions=len(required_compositions-composed),
                   orbits=len(required_orbits-orbits),
                   direct_refined=len(required_menus-named_menus),
                   one_program_tomography=8-best_tomography)
    probabilities = {str(q)+'_'+name: [str(x) for x in sorted(values)]
                     for (q, name), values in sorted(menu_probabilities.items())}
    return dict(missing=missing, complete=not any(missing.values()),
                direct_refined_coarse_probabilities=probabilities,
                scope='diagnostic seed families only; not all 35^4 programs')


def finite_diagonal_checks():
    """Independent exact finite coordinate-effect identities, not certificate data."""
    effects = tuple(itertools.product(range(5), repeat=2))
    pairs = 0
    for a in effects:
        complement = tuple(4-x for x in a)
        require(complement in effects, 'finite complement escaped domain')
        for b in effects:
            if any(x+y > 4 for x, y in zip(a, b)):
                continue
            pairs += 1
            for s in range(2):
                # A legal menu realizes the pair and its residual as three outcomes.
                col = (a[s], b[s], 4-a[s]-b[s], 0)
                labels = tuple(i for i, n in enumerate(col) for _ in range(n))
                group_mass = Fraction(sum(i in (0, 1) for i in labels), len(labels))
                require(group_mass == Fraction(a[s], 4)+Fraction(b[s], 4),
                        'summable-pair operational identity failed')
    return dict(effects=len(effects), ordered_summable_pairs=pairs,
                comparison='diagonal coordinate dictionary only')


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'duplicate JSON object key: ' + key)
        result[key] = value
    return result


def reject_constant(value):
    raise Invalid('non-JSON numeric constant: ' + value)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--source-sha256', required=True)
    parser.add_argument('--allow-partial-bank', action='store_true',
                        help='relax diagnostic-bank coverage only; never node semantics')
    args = parser.parse_args()
    try:
        require(re.fullmatch('[0-9a-f]{64}', args.source_sha256) is not None,
                'external source hash must be 64 lowercase hexadecimal characters')
        raw = args.certificate.read_bytes()
        data = json.loads(raw, object_pairs_hook=unique_object, parse_constant=reject_constant)
        exact_keys(data, ('schema', 'source_sha256', 'cases'), 'certificate')
        require(data['schema'] == 'detector-refinement-v1', 'wrong schema identifier')
        require(data['source_sha256'] == args.source_sha256, 'external source hash mismatch')
        require(type(data['cases']) is list and data['cases'], 'cases must be a nonempty list')
        checked = [check_case(case, i) for i, case in enumerate(data['cases'])]
        bank = coverage(checked)
        require(args.allow_partial_bank or bank['complete'], 'incomplete diagnostic bank: ' + str(bank['missing']))
        result = dict(ok=True, source_sha256=args.source_sha256,
                      certificate_sha256=hashlib.sha256(raw).hexdigest(),
                      checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      cases=len(checked), q_counts=dict(Counter(x['q'] for x in checked)),
                      nodes=sum(x['nodes'] for x in checked),
                      support_entries=sum(x['supports'] for x in checked),
                      minimum_support_mass=str(min(x['min_mass'] for x in checked)),
                      coverage=bank, finite_diagonal=finite_diagonal_checks(),
                      scope='finite supplied protocol; no quantum calibration or axiom derivation')
        print(json.dumps(result, sort_keys=True, separators=(',', ':')))
        return 0
    except Exception as error:
        print(json.dumps(dict(ok=False, error=type(error).__name__ + ': ' + str(error)), sort_keys=True))
        return 1


if __name__ == '__main__':
    sys.exit(main())
