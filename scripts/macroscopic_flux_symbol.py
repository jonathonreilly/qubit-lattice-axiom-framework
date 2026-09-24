#!/usr/bin/env python3
"""Exact path-polynomial and macroscopic-flux edge mismatch check."""

AUDIT_TIMEOUT_SEC = 3600
AUDIT_INPUT_PATHS = ('scripts/macroscopic_flux_symbol.py', 'scripts/core_derivation.py')
from fractions import Fraction
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("core", HERE / "core_derivation.py")
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
nodes = core.walk_nodes(100)
d_data = json.loads((HERE / "D_RESIDUE_POLYNOMIALS.json").read_text())

def edge_x_pair(n):
    paths = [p for p in core.two_hop_paths(nodes[n]) if p[0] == nodes[n + 1]]
    assert len(paths) == 1, (n, paths)
    m1, a1, m2, a2 = paths[0][3]
    return (m1 * (m1 + a1), m2 * (m2 + a2))

def return_x_values(n):
    paths = [p for p in core.two_hop_paths(nodes[n]) if p[0] == nodes[n]]
    assert len(paths) == 2, (n, paths)
    out=[]
    for p in paths:
        m1,a1,m2,a2=p[3]
        x1=m1*(m1+a1); x2=m2*(m2+a2)
        assert x1==x2, (n,p[3],x1,x2)
        out.append(x1)
    return tuple(out)

def interpolate(vals):
    y0, y1, y2 = vals
    A = Fraction(y2 - 2*y1 + y0, 2)
    B = Fraction(y1 - y0) - A
    return (A, B, Fraction(y0))

edge_polynomials = []
for r in range(15):
    samples = [edge_x_pair(r + 15*k) for k in (0, 1, 2)]
    p1 = interpolate([x[0] for x in samples])
    p2 = interpolate([x[1] for x in samples])
    for k in (-1, 3):
        actual = edge_x_pair(r + 15*k)
        predicted = tuple(p[0]*k*k + p[1]*k + p[2] for p in (p1, p2))
        assert actual == predicted, (r, k, actual, predicted)
    assert p1[0] == p2[0] == 9
    d_edge = tuple(Fraction(x) for x in d_data["rows"][r]["right"]["quadratic_k2_k_const"])
    assert tuple((p1[i] + p2[i]) / 2 for i in range(3)) == d_edge
    diff = tuple(p1[i] - p2[i] for i in range(3))
    assert diff[0] == 0 and diff[1] in (0, 6)
    edge_polynomials.append({"residue": r,
        "x1_k2_k_const": [str(x) for x in p1],
        "x2_k2_k_const": [str(x) for x in p2],
        "difference_slope": str(diff[1])})

# Check the two diagonal return-path polynomials used for the explicit
# interior witness. At fixed residue, each link flux is affine in k.
return_polys={}
for r in (0,1):
    samples=[return_x_values(r+15*k) for k in (0,1,2)]
    polys=[interpolate([x[j] for x in samples]) for j in (0,1)]
    for k in (-1,3):
        actual=return_x_values(r+15*k)
        predicted=tuple(p[0]*k*k+p[1]*k+p[2] for p in polys)
        assert actual==predicted,(r,k,actual,predicted)
    return_polys[str(r)]=[[str(x) for x in p] for p in polys]
assert return_polys["0"] == [["9","-3","0"],["9","3","0"]]
assert return_polys["1"] == [["9","9","2"],["9","3","0"]]

# For n=r+15k, k/S -> xi/15, |xi|<5, and rho=xi^2/25.
# The H2-plus-D edge difference has the exact identity
# C/2*(sqrt(1-x1/C)-sqrt(1-x2/C))^2.
# Its limit is gamma^2 xi^2/[1800(1-rho)]. The H4 edge difference
# tends to 4(1-rho)^2-4 because Q2 is absent and M=A* A is tridiagonal.
formula = "gamma^2*xi^2/(1800*(1-xi^2/25)) - 8*xi^2/25 + 4*xi^4/625"

# Explicit interior sequence: S=15k, n=15k (residue zero, xi=1).
# Here both off-diagonal x values are x+=9k^2+3k, so the H2+D
# edge comparison is exact at every k. Return paths give the two M diagonals.
samples = []
for k in (1, 2, 5, 10, 50, 100):
    S = 15*k
    C = S*(S+1)
    xlow = 9*k*k - 3*k
    xhigh = 9*k*k + 3*k
    xnext2 = 9*k*k + 9*k + 2
    assert 0 <= xlow < C and xhigh < C and xnext2 < C
    b = Fraction(C - xhigh, C)
    mdiag_n = Fraction(2*C - 18*k*k, C)
    mdiag_next = Fraction(2*C - (18*k*k + 12*k + 2), C)
    exact_h2_edge = -C*b
    candidate_h2_d_edge = -C + xhigh
    assert exact_h2_edge == candidate_h2_d_edge
    exact_h4_edge = b*(mdiag_n + mdiag_next)
    exact_minus_candidate = exact_h4_edge - 4
    samples.append({"k": k, "S": S, "n": S,
        "finite_minus_candidate_edge": str(exact_minus_candidate),
        "decimal": float(exact_minus_candidate)})

# Limiting value: b -> 24/25, both M diagonals -> 48/25.
limit = Fraction(24, 25) * (Fraction(48, 25) + Fraction(48, 25)) - 4
assert limit == Fraction(-196, 625)
out = {
    "status": "exact path-polynomial identities and a proved macroscopic interior edge limit",
    "edge_polynomials": edge_polynomials,
    "witness_return_polynomials": return_polys,
    "macroscopic_sequence": "S=15k, n=15k, so n/S=1 and both endpoints are physical for k>=1",
    "full_generator_edge_difference_limit": str(limit),
    "general_residue_limit_formula": formula,
    "gamma_rule": "gamma=6 for residues 1,4,6,9,11,14; gamma=0 otherwise",
    "finite_sequence_samples": samples,
    "scope": "matrix-entry mismatch at macroscopic-flux states; it does not establish that the frozen n=0 state reaches these states at a declared time"
}
(HERE / "MACROSCOPIC_FLUX_SYMBOL.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
