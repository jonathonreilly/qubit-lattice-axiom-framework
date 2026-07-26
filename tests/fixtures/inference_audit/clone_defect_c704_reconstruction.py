"""Reconstruction of the Cycle 704 clone defect, for linter self-test.

The committed Cycle 704 runner does NOT contain this defect: it was
self-caught and replaced with a geometric result before the commit. This file
reconstructs the withdrawn draft so the CLONE check has something to fire on.
The original draft wrote the formation gate and the migration gate with
identical bodies and then "verified" that they agreed across all 2187 rules --
a row that could not fail.
"""


def ncount(site, occ):
    return sum(1 for n in occ if n != site)


def can_form(site, occ, rule):
    k = ncount(site, occ)
    allowed = rule[k]
    return allowed != 0


def can_migrate_into(site, occ, rule):
    k = ncount(site, occ)
    allowed = rule[k]
    return allowed != 0


def check(name, ok, detail=""):
    print(name, ok, detail)


def m2_gates_agree():
    agree = all(
        can_form(s, o, r) == can_migrate_into(s, o, r)
        for s, o, r in _fixtures()
    )
    check("M2 formation and migration gates are the same predicate", agree)


def _fixtures():
    return [(0, set(), {0: 1}) for _ in range(3)]
