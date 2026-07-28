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


def one_line_form(rule):
    return rule[0] != 0


def one_line_migrate(rule):
    return rule[0] != 0


LOW_LIMIT = 0
HIGH_LIMIT = 100


def below_low_limit(value):
    return value < LOW_LIMIT


def below_high_limit(value):
    return value < HIGH_LIMIT


def default_low_limit(limit=LOW_LIMIT):
    return 50 < limit


def default_low_limit_copy(bound=LOW_LIMIT):
    return 50 < bound


def default_high_limit(limit=HIGH_LIMIT):
    return 50 < limit


def make_low_predicate():
    def predicate(value):
        return value < LOW_LIMIT

    return predicate


def make_low_predicate_copy():
    def candidate(value):
        return value < LOW_LIMIT

    return candidate


def make_high_predicate():
    def predicate(value):
        return value < HIGH_LIMIT

    return predicate
