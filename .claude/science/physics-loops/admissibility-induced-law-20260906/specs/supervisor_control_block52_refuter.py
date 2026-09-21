"""Block 52 refuting pass (supervisor-run; machinery disjoint from the runner: symbolic contents, a Monte Carlo of captures, flux accounting with
three records).
W1  the moments of the biased walk with a SYMBOLIC content: first moment c s, second moment alpha delta, total rate 3 alpha.
W2  the streaming operator of the biased walk expanded symbolically to second order: -c s.grad + (alpha/2) Laplacian, no content in the second term;
    the same expansion for block 44's forward clause keeps |s_k| in it.
W3  Monte Carlo of the captures of one site in a gas of two contents, (1,0,0) and (-3/5,-4/5,0): under the biased walk the captured mean is the gas
    mean (1/5, -2/5, 0); under the forward clause it is (1/15, -7/15, 0) (floating point).
W4  three records of distinct rational contents on the 3x3x3 torus, all 17550 ordered configurations: flow in equals flow out everywhere under the
    biased walk with exchange on occupied targets, and the sum of the contents is conserved by every event.
W5  the share of hops against the content, (3 alpha - c |s|_1)/(6 alpha) for contents with no vanishing component: its range at alpha = c."""
import itertools
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[5]
E = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
results = []


def report(tag, ok, msg):
    results.append(ok)
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}")


# ------------------------------------------------------------------------------------------------ W1
al, c = sp.symbols("alpha c", positive=True)
s = sp.symbols("s1 s2 s3", real=True)
rates = [(al + c * sum(s[i] * e[i] for i in range(3))) / 2 for e in E]
first = [sp.simplify(sum(rates[j] * E[j][i] for j in range(6))) for i in range(3)]
second = sp.Matrix(3, 3, lambda k, l: sp.simplify(sum(rates[j] * E[j][k] * E[j][l] for j in range(6))))
report("W1", first == [c * s[0], c * s[1], c * s[2]] and second == al * sp.eye(3) and sp.simplify(sum(rates) - 3 * al) == 0, f"symbolic content: first moment {first}, second moment alpha times the identity, total rate 3 alpha")

# ------------------------------------------------------------------------------------------------ W2
x, y, z, h = sp.symbols("x y z h")
f = sp.Function("f")
pos = [x, y, z]
expr = 0
for j, e in enumerate(E):
    shifted = f(*[pos[i] - h * e[i] for i in range(3)])
    expr += rates[j] * (shifted - f(x, y, z))
ser = sp.expand(sp.series(expr, h, 0, 3).removeO().doit())
lap = sum(sp.diff(f(x, y, z), v, 2) for v in pos)
want = sp.expand(-h * c * sum(s[i] * sp.diff(f(x, y, z), pos[i]) for i in range(3)) + h ** 2 * al / 2 * lap)
report("W2", sp.simplify(ser - want) == 0, "symbolic: the streaming operator of the biased walk is -h c s.grad f + (h^2 alpha/2) Laplacian f + O(h^3); the second-order term carries no content")

# ------------------------------------------------------------------------------------------------ W3
rng = np.random.default_rng(52)
contents = np.array([[1.0, 0.0, 0.0], [-0.6, -0.8, 0.0]])
EA = np.array(E, float)
n = 4_000_000
which = rng.integers(0, 2, n)
sc = contents[which]
direction = rng.integers(0, 6, n)                                       # the neighbour at -e hops along e onto the site
proj = (sc * EA[direction]).sum(axis=1)
u = rng.random(n)
cap_b = u < (1 + proj) / 2                                              # biased walk with alpha = c: probability proportional to (1 + s.e)/2
cap_f = u < np.maximum(0.0, proj)                                       # forward clause: probability proportional to max(0, s.e)
mean_b, mean_f = sc[cap_b].mean(axis=0), sc[cap_f].mean(axis=0)
ok = np.allclose(mean_b, [0.2, -0.4, 0.0], atol=3e-3) and np.allclose(mean_f, [1 / 15, -7 / 15, 0.0], atol=3e-3)
report("W3", ok, f"Monte Carlo of {n} hop attempts next to a capturing site, gas of two contents: captured mean under the biased walk {np.round(mean_b, 4)} (gas mean 0.2, -0.4, 0); under the forward clause {np.round(mean_f, 4)} (1/15 = 0.0667, -7/15 = -0.4667, 0)")

# ------------------------------------------------------------------------------------------------ W4
SITES = list(itertools.product(range(3), repeat=3))
cont = [(F(1, 3), F(2, 3), F(2, 3)), (F(-3, 5), F(0), F(4, 5)), (F(2, 7), F(-3, 7), F(6, 7))]
ALPHA = CC = F(1, 3)
inflow, outflow = {}, {}
momentum_ok = True
for xs in itertools.permutations(SITES, 3):
    state = tuple(xs)                                                   # record i (content i) sits at xs[i]; an exchange swaps which content sits where
    occupied = {xs[i]: i for i in range(3)}
    for i in range(3):
        for e in E:
            r = (ALPHA + CC * sum(cont[i][k] * e[k] for k in range(3))) / 2
            target = tuple((xs[i][k] + e[k]) % 3 for k in range(3))
            new = list(xs)
            if target in occupied:
                j = occupied[target]
                new[i], new[j] = xs[j], xs[i]                           # the two contents change places
            else:
                new[i] = target
            inflow[tuple(new)] = inflow.get(tuple(new), 0) + r
            outflow[state] = outflow.get(state, 0) + r
bad = sum(1 for k in outflow if inflow.get(k, 0) != outflow[k])
report("W4", len(outflow) == 17550 and bad == 0, f"three records of distinct contents on the 3x3x3 torus: {len(outflow)} ordered configurations, flow in differs from flow out at {bad}; contents are moved or exchanged, never changed, so their sum is conserved")

# ------------------------------------------------------------------------------------------------ W5
t = sp.symbols("t", positive=True)
share = lambda l1: (3 - sp.sympify(l1)) / 6                              # sympify: (3 - 1)/6 with Python integers would be a float
report("W5", sp.simplify(share(sp.sqrt(3)) - (3 - sp.sqrt(3)) / 6) == 0 and share(1) == sp.Rational(1, 3), f"at alpha = c a record with no vanishing component hops against its content the share (3 - |s|_1)/6 of the time: from {float((3 - sp.sqrt(3)) / 6):.4f} on a body diagonal towards 1/3 near an axis (on an axis itself none are against and two thirds are across)")

print(f"REFUTER TOTAL: PASS={sum(results)} FAIL={len(results) - sum(results)}")
sys.exit(0 if all(results) else 1)
