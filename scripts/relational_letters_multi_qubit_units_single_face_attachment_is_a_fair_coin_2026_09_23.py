#!/usr/bin/env python3
"""A single-face symmetry bound for local joint-unit formation.

The product bound assumes sequential face-connected growth from one seed, and at each attachment the conditional law given the whole past depends only on its local input. Fresh draws realize the attaining example; shared hidden randomness is excluded. A first span extension has at most one occupied face, and face connectivity supplies that face; one such event cannot first extend two axes. These assumptions are supplied, not consequences of covariance. No exclusion of all bounded units, seed schemes, or physical multi-qubit formation is claimed.

See the companion note for proofs and exact execution scope.
"""
import sys

AUDIT_TIMEOUT_SEC = 900
from itertools import permutations, product

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


TH = (1, 2, 5)
M = 12
NB = 3


def proper_rotations():
    out = []
    for pi in permutations(range(3)):
        par = 1 if sum(1 for i in range(3) for j in range(i + 1, 3) if pi[i] > pi[j]) % 2 == 0 else -1
        for sg in product((1, -1), repeat=3):
            if sg[0] * sg[1] * sg[2] * par == 1:
                out.append((pi, sg))
    return out


def pattern(g, flip):
    pi, sg = g
    return lambda x: (flip * sum(TH[i] * sg[i] * x[pi[i]] for i in range(3))) % M


def signed_index(delta):
    for p in range(3):
        for s in (1, -1):
            if (s * TH[p]) % M == delta % M:
                return p, s
    return None


def missing_angle(alpha, beta):
    ia, ib = signed_index(alpha), signed_index(beta)
    if ia is None or ib is None or ia[0] == ib[0]:
        return None
    return ia, ib, ({0, 1, 2} - {ia[0], ib[0]}).pop()


def copy_sign_step(alpha, beta):
    m = missing_angle(alpha, beta)
    return None if m is None else (m[0][1] * TH[m[2]]) % M


def back_step(alpha, beta):
    m = missing_angle(alpha, beta)
    return None if m is None else TH[m[2]] % M


G = proper_rotations()
PATTERNS = [pattern(g, flip) for g in G for flip in (1, -1)]

print("A. a single face cannot tell the continuation's sign")
equiv_ok, step_ok, views = True, True, []
for g in G:
    for flip in (1, -1):
        P = pattern(g, flip)
        for d in range(3):
            a, b = (d + 1) % 3, (d + 2) % 3
            pos = lambda u, v: tuple(u if k == a else v if k == b else 0 for k in range(3))
            face = {(u, v): P(pos(u, v)) for u in (0, 1) for v in (0, 1)}
            view = lambda fc: (fc[(0, 0)], (fc[(1, 0)] - fc[(0, 0)]) % M, (fc[(0, 1)] - fc[(0, 0)]) % M)
            reversed_face = {k: (-v) % M for k, v in face.items()}
            turned_face = {(u, v): face[(1 - u, 1 - v)] for u in (0, 1) for v in (0, 1)}
            FV, RV = view(reversed_face), view(turned_face)
            equiv_ok = equiv_ok and FV[1:] == RV[1:]
            t = (P(tuple(int(k == d) for k in range(3))) - P((0, 0, 0))) % M
            turned = lambda x: tuple(1 - x[k] if k in (a, b) else x[k] for k in range(3))
            t_turned = (P(turned(tuple(int(k == d) for k in range(3)))) - P(turned((0, 0, 0)))) % M
            t_reversed = (-t) % M
            step_ok = step_ok and t_turned == t and t_reversed != t
            views.append((view(face), FV, RV, t))
check("reversing the circle and the half turn about the growth axis give the same face view up to a rotation of the circle",
      equiv_ok and step_ok and len(views) == 144,
      "for all 24 proper orientations, both circle orientations and all three growth axes: the reversed view is the "
      "half-turned view plus a constant, while the correct step is negated by the one and kept by the other")
no_det = not any((2 * t) % M == 0 for t in {x % M for x in TH} | {(-x) % M for x in TH})
missing = lambda v: None if missing_angle(*v) is None else missing_angle(*v)[2]
coin_cov = all(missing(V[1:]) is not None and missing(V[1:]) == missing(FV[1:]) == missing(RV[1:]) for V, FV, RV, t in views)
check("so no deterministic covariant rule continues through a single face, and a randomised one is right with probability at most 1/2",
      no_det and equiv_ok and coin_cov,
      "a covariant step law is symmetric under t -> -t; no valid step (1, 2, 5 units of 30 degrees, either sign) "
      "satisfies t = -t modulo 12; the fair coin over the sign of the missing angle is covariant (the missing angle "
      "is the same in all three views, 144 of 144)")

print("B. what growth needs")


def single_face_attachments(n):
    return sum(1 for B in product(range(n), repeat=3) if B != (0, 0, 0) and sum(1 for k in range(3) if B[k] > 0) == 1)


counts = {n: single_face_attachments(n) for n in (2, 3, 4, 5)}
check("corner growth of n units per side has exactly 3(n - 1) single-face attachments, so registration is at most 2^(-3(n - 1))",
      all(c == 3 * (n - 1) for n, c in counts.items()),
      "; ".join(f"n = {n}: {c} attachments, bound 1/{2 ** c}" for n, c in counts.items())
      + "; in any growth, a unit that extends the formed span along an axis touches the formed region through one face")


def corner(B, d):
    return tuple(2 * B[k] - (k == d) for k in range(3))


def shift(x, d, s):
    return tuple(x[k] + s * (k == d) for k in range(3))


def face_steps(A, B, d):
    a, b = (d + 1) % 3, (d + 2) % 3
    p = corner(B, d)
    return (A[shift(p, a, 1)] - A[p]) % M, (A[shift(p, b, 1)] - A[p]) % M


def grow(first, single_step):
    A = {x: first(x) for x in product(range(2), repeat=3)}
    for B in sorted(product(range(NB), repeat=3), key=sum):
        if B == (0, 0, 0):
            continue
        faces = [d for d in range(3) if B[d] > 0]
        steps = {}
        for d in faces:
            if len(faces) == 1:
                steps[d] = single_step(A, B, d)
            else:
                p = corner(B, next(k for k in faces if k != d))
                steps[d] = (A[shift(p, d, 1)] - A[p]) % M
            if steps[d] is None:
                return None
        for o in product(range(2), repeat=3):
            s = tuple(2 * B[k] + o[k] for k in range(3))
            vals = {(A[tuple(2 * B[k] - 1 if k == d else s[k] for k in range(3))] + (o[d] + 1) * steps[d]) % M
                    for d in faces}
            if len(vals) != 1:
                return None
            A[s] = vals.pop()
    return A


def registers(P, single_step):
    A = grow(P, single_step)
    return A is not None and all(A[x] == P(x) for x in product(range(2 * NB), repeat=3))


def fair_coin(signs):
    draws = iter(signs)

    def rule(A, B, d):
        m = missing_angle(*face_steps(A, B, d))
        return None if m is None else (next(draws) * TH[m[2]]) % M
    return rule


calls = []


def counting(A, B, d):
    calls.append(B)
    return (A[corner(B, d)] - A[shift(corner(B, d), d, -1)]) % M


grow(PATTERNS[0], counting)
n_single = len(calls)
per_pattern = []
if n_single == single_face_attachments(NB) == 6:
    per_pattern = [sum(registers(P, fair_coin(signs)) for signs in product((1, -1), repeat=n_single)) for P in PATTERNS]
check("the covariant fair coin attains the bound: exactly one of its 2^6 sign draws registers the 3 x 3 x 3 grid of units",
      len(per_pattern) == 48 and all(c == 1 for c in per_pattern),
      f"the growth makes {n_single} single-face attachments; registering draws per pattern: "
      f"{sorted(set(per_pattern))} over all 48 first-unit patterns, so registration has probability exactly 1/64")

print("C. rules that break a covariance do better")


def copy_sign(A, B, d):
    return copy_sign_step(*face_steps(A, B, d))


def treat_as_back(A, B, d):
    return back_step(*face_steps(A, B, d))


wins = {name: sum(registers(P, rule) for P in PATTERNS)
        for name, rule in (("copy an in-face sign", copy_sign), ("treat the face as the back side", treat_as_back))}
check("covariance-breaking rules register the frame in 12 and 6 of the 48 first-unit patterns",
      wins == {"copy an in-face sign": 12, "treat the face as the back side": 6},
      "exact over 24 proper orientations and both circle orientations on a 3 x 3 x 3 grid of units")
neg = lambda x: None if x is None else (-x) % M
copy_rev = all(copy_sign_step(*FV[1:]) == neg(copy_sign_step(*V[1:])) is not None for V, FV, RV, t in views)
copy_turn = sum(copy_sign_step(*RV[1:]) == copy_sign_step(*V[1:]) for V, FV, RV, t in views)
back_turn = all(back_step(*RV[1:]) == back_step(*V[1:]) is not None for V, FV, RV, t in views)
back_rev = sum(back_step(*FV[1:]) == neg(back_step(*V[1:])) for V, FV, RV, t in views)
right = {name: sum(fn(*V[1:]) == t for V, FV, RV, t in views) for name, fn in (("copy", copy_sign_step), ("back", back_step))}
check("each control keeps one covariance and breaks the other",
      copy_rev and copy_turn == 0 and back_turn and back_rev == 0 and right == {"copy": 72, "back": 72},
      "copying an in-face sign commutes with the reversal on 144 of 144 views and with the half turn on "
      f"{copy_turn}; treating the face as the back side commutes with the half turn on 144 of 144 and with the "
      f"reversal on {back_rev}; each is right on {right['copy']} and {right['back']} of the 144 views")

print("D. the nearest-neighbour premise carries the bound")


def two_back(A, B, d):
    p = corner(B, d)
    return (A[p] - A[shift(p, d, -1)]) % M


reach = sum(registers(P, two_back) for P in PATTERNS)
check("a unit that reads two layers back sees the step along the growth axis and registers the frame in all 48 patterns",
      reach == 48,
      f"{reach} of 48; the site two layers back is not a neighbour of the unit, so this read is outside local formation")

print('per_element: Exact arithmetic tests the declared angle, star or linear-system objects; no physical qubit encoding is inferred.')
print('per_site: Site checks cover only the explicit finite boxes, tori and samples printed above; boundary freedoms remain as stated in the note.')
print('per_mode: Analytic mode or symmetry arguments are conditional source proofs; finite runner cases alone do not prove untested universality.')
print('per_block: This is one bounded support result in a supplied relational record model, with the controls and counts declared above.')
print('lattice_wide: No physical infinite-volume conclusion is inferred; any whole-lattice or all-size statement is limited to the explicit source theorem hypotheses.')
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
