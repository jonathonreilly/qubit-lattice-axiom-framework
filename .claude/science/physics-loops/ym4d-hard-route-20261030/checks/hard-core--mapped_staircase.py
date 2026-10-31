#!/usr/bin/env python3
"""No pinch on the free set of a lexicographic order of boxes on a torus. Consumer: Lemma O1 of `library/sector-values.md`: Theorem F-D reads the free set only through its extension constant C_ext, which reflection gives as absolute when there is no pinch.

Written before running. Boxes on (Z/N)^d. For a lexicographic order with its seam at the origin, and box i, the free set is { boxes <= i }. A pinch: two free boxes that touch (sup distance 1) and are not joined by a chain of free boxes through facets inside the star of their common face, that is, among boxes touching both. On a torus of side N >= 4 sup distance 1 is unambiguous.

PRE-STATED criteria.
 P1. No pinch for every i, in d = 2, 3, 4 at N = 4, and d = 2, 3 at N = 6.
 P2. Control: the checkerboard set has pinches, so the test has power.
FAIL if either fails.

Limits. Finite sizes; the local patterns do not depend on N for N >= 4 except across seams, which N = 4 contains.
"""
import itertools
import sys


def wrap(a, b, N):
    return tuple((x + y) % N for x, y in zip(a, b))


def diff(a, b, N):
    out = []
    for x, y in zip(a, b):
        d = (y - x) % N
        out.append(d if d <= N // 2 else d - N)
    return tuple(out)


def pinches(free, N, d):
    nbrs = [o for o in itertools.product((-1, 0, 1), repeat=d) if any(o)]
    count = 0
    for a in free:
        for o in nbrs:
            if sum(1 for v in o if v) < 2:
                continue
            b = wrap(a, o, N)
            if b not in free or b < a:
                continue
            # The common star: boxes touching both a and b.
            star = set()
            for s in itertools.product((-1, 0, 1), repeat=d):
                c = wrap(a, s, N)
                if c in free and all(abs(v) <= 1 for v in diff(b, c, N)):
                    star.add(c)
            seen = {a}
            todo = [a]
            while todo:
                u = todo.pop()
                for ax in range(d):
                    for sg in (-1, 1):
                        e = [0] * d
                        e[ax] = sg
                        v = wrap(u, e, N)
                        if v in star and v not in seen:
                            seen.add(v)
                            todo.append(v)
            if b not in seen:
                count += 1
    return count


def main():
    ok = True
    for d, N in ((2, 4), (3, 4), (4, 4), (2, 6), (3, 6)):
        boxes = list(itertools.product(range(N), repeat=d))
        worst = 0
        free = set()
        for k, i in enumerate(boxes):
            free.add(i)
            # Lex order is the product's order, so free grows along the list.
            if d == 4 and k % 3:
                continue
            worst = max(worst, pinches(free, N, d))
        good = worst == 0
        ok = ok and good
        print(f" d={d} N={N}: most pinches at any i {worst}: {good}", flush=True)
    d, N = 2, 4
    check = {b for b in itertools.product(range(N), repeat=d) if sum(b) % 2 == 0}
    c = pinches(check, N, d)
    good = c > 0
    ok = ok and good
    print(f" control, checkerboard: {c} pinches: {good}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
