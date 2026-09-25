#!/usr/bin/env python3
"""Own all-color six-leaf primitive Laurent Gram control; no author imports."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json
import time

HERE = Path(__file__).resolve().parent
tic = time.perf_counter()
Z = 6
zero = (0,) * Z
words = [(a,) + b for a in (-1, 1) for b in product((-1, 0, 1), repeat=Z)]
vacancies = [w[1:].count(0) for w in words]


def shift(e, i, q):
    x = list(e)
    x[i] += q
    return tuple(x)


def outward(w):
    """Outward from A, with all link orientations A to B."""
    a = w[0]
    if not a:
        return []
    out = []
    for b in range(Z):
        if not w[b + 1]:
            dest = list(w)
            dest[0], dest[b + 1] = 0, a
            out.append((tuple(dest), shift(zero, b, -a)))
    return out


def birth(w, e, b, sigma):
    if w[0] or w[b + 1]:
        return None
    dest = list(w)
    dest[0], dest[b + 1] = sigma, -sigma
    return tuple(dest), shift(e, b, sigma)


def gram(paths):
    """paths = (source id, output matter, electric shift); retain every phase."""
    groups = defaultdict(list)
    for i, w, e in paths:
        groups[w].append((i, e))
    out = Counter()
    for items in groups.values():
        for i, e in items:
            for j, f in items:
                out[(i, j, tuple(y - x for x, y in zip(e, f)))] += 1
    return out, groups


fpaths = [(i, dest, e) for i, w in enumerate(words) for dest, e in outward(w)]
M, fgroups = gram(fpaths)
resolved = Counter()
coherent = Counter()
channel_counts = []
for b in range(Z):
    both = []
    for sigma in (-1, 1):
        paths = []
        for i, w, e in fpaths:
            result = birth(w, e, b, sigma)
            if result is not None:
                dest, f = result
                paths.append((i, dest, f))
        G, _ = gram(paths)
        resolved.update(G)
        both.extend(paths)
        channel_counts.append(dict(b=b, sigma=sigma, paths=len(paths),
                                   distinct_laurent_entries=len(G)))
    G, _ = gram(both)
    coherent.update(G)

expected = Counter({key: 2 * (vacancies[key[1]] - 1) * value
                    for key, value in M.items()
                    if 2 * (vacancies[key[1]] - 1) * value})
assert resolved == expected == coherent
assert all(vacancies[i] == vacancies[j] for i, j, e in M)
assert all(vacancies[i] == vacancies[j] for i, j, e in resolved)
assert all(M[(j, i, tuple(-x for x in e))] == c for (i, j, e), c in M.items())
assert all(resolved[(j, i, tuple(-x for x in e))] == c
           for (i, j, e), c in resolved.items())

column_counts = Counter(i for i, _, _ in fpaths)
row_sums = Counter()
for (i, j, e), c in M.items():
    row_sums[i] += c
groups_by_v = defaultdict(list)
for w, items in fgroups.items():
    v = w[1:].count(0) + 1
    assert len(items) == 7 - v
    groups_by_v[v].append(len(items))

rows = []
for v in range(7):
    ids = [i for i, x in enumerate(vacancies) if x == v]
    bound = v * (7 - v)
    assert all(column_counts[i] == v for i in ids)
    assert all(row_sums[i] == bound for i in ids)
    coefficient = Fraction(7 - 2 * v, 5)
    # For a nonpositive coefficient the operator upper bound is zero,
    # not the product of the coefficient with an upper spectral endpoint.
    upper = max(coefficient, 0) * bound
    assert upper <= 6
    gamma_upper = 2 * max(v - 1, 0) * bound
    assert gamma_upper <= 80
    rows.append(dict(v=v, input_words=len(ids), outward_column_count=v,
                     intermediate_row_count=(7 - v if v else 0),
                     intermediate_matter_words=len(groups_by_v[v]),
                     zero_angle_M_row_sum=bound,
                     affine_coefficient=str(coefficient),
                     certified_affine_upper=str(upper),
                     gamma_over_kappa_upper=gamma_upper))

entries = dict(
    convention="Entry (bra input, ket input, electric shift) with A-to-B links.",
    input_words=words,
    M=[[i, j, list(e), c] for (i, j, e), c in sorted(M.items())],
    Gamma_over_kappa=[[i, j, list(e), c] for (i, j, e), c in sorted(resolved.items())])
data_path = HERE / 'STAR_LAURENT_ENTRIES.json'
with data_path.open('x') as out:
    json.dump(entries, out, separators=(',', ':'))
    out.write('\n')
result = dict(
    control="Independent primitive all-color local star Laurent Gram enumeration",
    original_resolved_and_unnormalized_coherent=True,
    source_words=len(words), outward_paths=len(fpaths), M_entries=len(M),
    Gamma_entries=len(resolved), identities_exact=True,
    channels=channel_counts, vacancy_blocks=rows,
    derivation_limit="Norm proof is Schur/Cauchy on exact paths; enumeration is a bounded corroboration, not a global spectral computation.",
    entries_sha256=hashlib.sha256(data_path.read_bytes()).hexdigest(),
    elapsed_seconds=time.perf_counter() - tic)
with (HERE / 'STAR_CONTROL_RESULTS.json').open('x') as out:
    json.dump(result, out, indent=2)
    out.write('\n')
print(json.dumps(result, indent=2))
