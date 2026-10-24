"""Finite supplied binary guarded crossings; no spatial or physical claims."""
import argparse
import itertools
from dataclasses import dataclass

AUDIT_INPUT_PATHS = ["docs/FINITE_GUARDED_UPDATE_INVOLUTION_NOTE_2026-10-24.md"]


@dataclass(frozen=True)
class Unit:
    read: tuple
    write: tuple
    a: tuple
    b: tuple


class Layer:
    """Direct finite incidence and integer-bit crossing implementation."""
    def __init__(self, n, units, graph="full", distance_two=True, both_states=True):
        if type(n) is not int or n < 0:
            raise ValueError("nonnegative integer site count required")
        if graph not in ("full", "write_only"):
            raise ValueError("unknown graph")
        self.n, self.units = n, tuple(units)
        self.distance_two, self.both_states = distance_two, both_states
        self.masks = []
        for u in self.units:
            if any(type(i) is not int or not 0 <= i < n for i in u.read + u.write):
                raise ValueError("site outside domain")
            if len(set(u.read)) != len(u.read) or len(set(u.write)) != len(u.write):
                raise ValueError("duplicate site declaration")
            if not set(u.write) <= set(u.read):
                raise ValueError("write outside read")
            if len(u.a) != len(u.read) or len(u.b) != len(u.read):
                raise ValueError("pattern length")
            if any(type(x) is not int or x not in (0, 1) for x in u.a + u.b):
                raise ValueError("binary patterns required")
            changed = {i for i, a, b in zip(u.read, u.a, u.b) if a != b}
            if not changed or not changed <= set(u.write):
                raise ValueError("distinct patterns must agree outside write set")
            self.masks.append(sum(1 << i for i in changed))
        self.n1 = [set() for _ in self.units]
        for i, u in enumerate(self.units):
            for j, v in enumerate(self.units):
                conflict = (set(u.write) & set(v.read) or set(v.write) & set(u.read))
                if graph == "write_only":
                    conflict = set(u.write) & set(v.write)
                if i != j and conflict:
                    self.n1[i].add(j)
        self.n2 = [set().union(*(self.n1[j] for j in near)) - near - {i}
                   for i, near in enumerate(self.n1)]

    def candidate(self, i, c):
        u = self.units[i]
        pattern = tuple((c >> k) & 1 for k in u.read)
        return pattern == u.a or pattern == u.b

    def cross(self, i, c):
        return c ^ self.masks[i] if self.candidate(i, c) else c

    def active(self, c):
        if type(c) is not int or not 0 <= c < (1 << self.n):
            raise ValueError("configuration outside binary domain")
        candidates = {i for i in range(len(self.units)) if self.candidate(i, c)}
        return {i for i in candidates
                if not self.n1[i] & candidates
                and (not self.distance_two or not self.n2[i] & candidates)
                and (not self.both_states or
                     not any(self.candidate(j, self.cross(i, c)) for j in self.n1[i]))}

    def apply(self, c):
        active = self.active(c)
        result = c
        for i in sorted(active):
            # Each selected unit is a candidate in the original state.
            # Freeze its crossing there, including in deliberately weakened controls.
            result ^= self.masks[i]
        return result


def reference(units, bits):
    """Separate tuple replacement and direct two-step relation evaluator."""
    def candidate(u, state):
        return tuple(state[k] for k in u.read) in (u.a, u.b)

    def crossing(u, state):
        local = tuple(state[k] for k in u.read)
        if local not in (u.a, u.b):
            return state
        target = u.b if local == u.a else u.a
        out = list(state)
        for position, site in enumerate(u.read):
            out[site] = target[position]
        return tuple(out)

    def adjacent(i, j):
        if i == j:
            return False
        u, v = units[i], units[j]
        return any(k in v.read for k in u.write) or any(k in u.read for k in v.write)

    active = []
    for i, u in enumerate(units):
        if not candidate(u, bits):
            continue
        other = crossing(u, bits)
        blocked = False
        for j, v in enumerate(units):
            if adjacent(i, j):
                if candidate(v, bits) or candidate(v, other):
                    blocked = True
            elif j != i and any(adjacent(i, k) and adjacent(k, j) for k in range(len(units))):
                if candidate(v, bits):
                    blocked = True
        if not blocked:
            active.append(i)
    # Simultaneous replacement from the original state, not sequential crossing.
    out = list(bits)
    for i in active:
        crossed = crossing(units[i], bits)
        for k in units[i].write:
            out[k] = crossed[k]
    return set(active), tuple(out)


def flip(site):
    return Unit((site,), (site,), (0,), (1,))


def fixtures():
    controlled_x = Unit((0, 1), (0,), (0, 0), (1, 0))
    controlled_y = Unit((0, 1), (1,), (0, 0), (0, 1))
    joint = Unit((0, 1, 2), (2,), (1, 1, 0), (1, 1, 1))
    return {
        "empty_sites": (0, ()),
        "empty_family": (3, ()),
        "single_flip": (1, (flip(0),)),
        "duplicates": (1, (flip(0), flip(0))),
        "write_dependency": (2, (controlled_x, controlled_y)),
        "distance_two": (3, (flip(0), flip(1), joint)),
        "other_state": (2, (flip(0), Unit((0, 1), (1,), (1, 0), (1, 1)))),
        "enabled_overlap": (4, (Unit((0, 2), (0,), (0, 0), (1, 0)),
                                 Unit((1, 2), (1,), (0, 1), (1, 1)), joint, flip(3))),
        "conserving_swaps": (4, (Unit((0, 1), (0, 1), (0, 1), (1, 0)),
                                  Unit((2, 3), (2, 3), (0, 1), (1, 0))))}


def main(inject_failure=False):
    checks = []
    def check(label, value):
        checks.append(bool(value))
        print(("PASS " if value else "FAIL ") + label)

    families = fixtures()
    for name, (n, units) in families.items():
        layer = Layer(n, units)
        agree, invariant, inverse, disjoint, commute, subsets = [], [], [], [], [], []
        max_active = 0
        for c in range(1 << n):
            a, d = layer.active(c), layer.apply(c)
            bits = tuple((c >> i) & 1 for i in range(n))
            ra, rd = reference(units, bits)
            agree.append(a == ra and d == sum(v << i for i, v in enumerate(rd)))
            invariant.append(layer.active(d) == a)
            inverse.append(layer.apply(d) == c)
            disjoint.append(all(not set(units[i].write) & set(units[j].write)
                                for i, j in itertools.combinations(a, 2)))
            max_active = max(max_active, len(a))
            reversed_result = c
            for i in sorted(a, reverse=True):
                reversed_result = layer.cross(i, reversed_result)
            commute.append(reversed_result == d)
            for size in range(len(a) + 1):
                for selected in itertools.combinations(sorted(a), size):
                    intermediate = c
                    for i in selected:
                        intermediate = layer.cross(i, intermediate)
                    subsets.append(a <= layer.active(intermediate))
        print(f"INFO fixture={name} configurations={1 << n} max_active={max_active}")
        check(name + " reference agreement", all(agree))
        check(name + " active-set equality", all(invariant))
        check(name + " involution", all(inverse))
        check(name + " write disjointness/order/subset persistence", all(disjoint + commute + subsets))
    overlap = Layer(*families["enabled_overlap"])
    check("genuine overlapping-read fixture enables two simultaneous units", overlap.active(0) == {0, 3})
    for name, kwargs, expected in (
        ("write_dependency", {"graph": "write_only"}, 3),
        ("distance_two", {"distance_two": False}, 3),
        ("other_state", {"both_states": False}, 1)):
        broken = Layer(*families[name], **kwargs)
        d = broken.apply(0)
        print(f"INFO counterexample={name} input=0 first={d} second={broken.apply(d)}")
        check(name + " specified weakening is not an involution", d == expected and broken.apply(d) == expected)
    swaps = Layer(*families["conserving_swaps"])
    check("supplied swaps conserve count", all(c.bit_count() == swaps.apply(c).bit_count() for c in range(16)))
    check("two-state structure alone does not conserve count", Layer(1, (flip(0),)).apply(0).bit_count() == 1)
    invalid = [Unit((0,), (1,), (0,), (1,)), Unit((0,), (0,), (0,), (0,)),
               Unit((0, 1), (0,), (0, 0), (0, 1)), Unit((0, 0), (0,), (0, 0), (1, 1)),
               Unit((2,), (2,), (0,), (1,)), Unit((0,), (0, 0), (0,), (1,)),
               Unit((0,), (0,), (0, 1), (1,)), Unit((0,), (0,), (0,), (2,))]
    for i, bad in enumerate(invalid):
        rejected = False
        try:
            Layer(2, (bad,))
        except ValueError:
            rejected = True
        check(f"invalid declaration {i} rejected", rejected)
    if inject_failure:
        check("deliberately injected failure for exit-status control", False)
    failed = len(checks) - sum(checks)
    print(f"TOTAL: PASS={sum(checks)} FAIL={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inject-failure", action="store_true")
    raise SystemExit(main(parser.parse_args().inject_failure))
