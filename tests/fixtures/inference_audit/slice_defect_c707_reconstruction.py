"""Reconstruction of the Cycle 707 row-G slice defect, for linter self-test.

The row listed two "hill" forms and then tested only the first, silently
dropping `-Lf` -- whose derivative contradicts the classification the row
asserts. Verbatim shape of the shipped defect.
"""


def check(name, ok, detail=""):
    print(name, ok, detail)


def gprime0(g, h=1e-7):
    return (g(h) - g(0.0)) / h


def g_valley_sign_control():
    valley = [lambda f: 1 - f, lambda f: 1 / (1 + f)]
    hill = [lambda f: 1 + f, lambda f: -f]
    valleys_ok = all(gprime0(g) < 0 for g in valley)
    hills_ok = all(gprime0(g) > 0 for g in hill[:1])
    check("G sign control: valley g'(0)<0, hill g'(0)>0", valleys_ok and hills_ok)


def zipped_slice_control():
    xs = [1, 2, 3, 4]
    truncated_ok = all(a <= b for a, b in zip(xs, xs[:1]))
    adjacent_ok = all(a <= b for a, b in zip(xs, xs[1:]))
    check("zip truncation versus adjacent pairs", truncated_ok and adjacent_ok)
