#!/usr/bin/env python3
"""Exact Weyl-algebra and covariance check of the separately stipulated mode.

Normal-ordered monomials are q^m p^n, with [q,p]=i. No finite Fock truncation
and no author adaptation code are used.
"""
from __future__ import annotations
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time
import sympy as z

HERE = Path(__file__).resolve().parent


def clean(poly):
    return {k: value for k, v in poly.items() if (value := z.simplify(v)) != 0}


def plus(*polys):
    out = defaultdict(lambda: z.Integer(0))
    for poly in polys:
        for k, v in poly.items(): out[k] += v
    return clean(out)


def scale(c, poly):
    return clean({k: c*v for k, v in poly.items()})


def mul(a, b):
    out = defaultdict(lambda: z.Integer(0))
    for (m, n), av in a.items():
        for (u, v), bv in b.items():
            for k in range(min(n, u)+1):
                c = (-z.I)**k*z.binomial(n, k)*z.factorial(u)/z.factorial(u-k)
                out[m+u-k, n+v-k] += av*bv*c
    return clean(out)


def same(a, b):
    assert not plus(a, scale(-1, b)), (a, b)


def main():
    tic = time.monotonic()
    a, b, g, r = z.symbols("a b g r", positive=True)
    q, p, one = {(1, 0): z.Integer(1)}, {(0, 1): z.Integer(1)}, {(0, 0): z.Integer(1)}
    same(plus(mul(q, p), scale(-1, mul(p, q))), scale(z.I, one))
    h = plus(scale(a/2, mul(p, p)), scale(b/2, mul(q, q)))
    ell = plus(scale(z.sqrt(g/(2*r)), q), scale(z.I*z.sqrt(g*r/2), p))
    elld = {k: z.conjugate(v) for k, v in ell.items()}
    loss = mul(elld, ell)
    same(loss, scale(g/2, plus(scale(1/r, mul(q, q)), scale(r, mul(p, p)), scale(-1, one))))
    def dual(o):
        return plus(scale(z.I, plus(mul(h, o), scale(-1, mul(o, h)))),
                    mul(mul(elld, o), ell),
                    scale(-z.Rational(1, 2), plus(mul(loss, o), mul(o, loss))))
    qp = scale(z.Rational(1, 2), plus(mul(q, p), mul(p, q)))
    tests = {
        "q": (q, plus(scale(-g/2, q), scale(a, p))),
        "p": (p, plus(scale(-b, q), scale(-g/2, p))),
        "q2": (mul(q, q), plus(scale(-g, mul(q, q)), scale(2*a, qp), scale(g*r/2, one))),
        "p2": (mul(p, p), plus(scale(-g, mul(p, p)), scale(-2*b, qp), scale(g/(2*r), one))),
        "symmetric_qp": (qp, plus(scale(a, mul(p, p)), scale(-b, mul(q, q)), scale(-g, qp)))}
    for o, expected in tests.values(): same(dual(o), expected)
    A = z.Matrix([[-g/2, a], [-b, -g/2]])
    noise = z.diag(g*r/2, g/(2*r))
    difference = a/r-b*r
    denominator = g*g+4*a*b
    C = g*difference/(2*denominator)
    Q = r/2+a*difference/denominator
    P = 1/(2*r)-b*difference/denominator
    V = z.Matrix([[Q, C], [C, P]])
    assert (A*V+V*A.T+noise).applyfunc(z.simplify) == z.zeros(2)
    determinant = z.simplify(V.det())
    assert z.simplify(determinant-(1+difference**2/denominator)/4) == 0
    energy = z.simplify((a*P+b*Q)/2)
    assert z.simplify(energy-(a/r+b*r)/4) == 0
    n0 = z.simplify((Q/r+r*P-1)/2)
    assert z.simplify(n0-difference**2/(2*denominator)) == 0
    purity = z.sqrt(denominator/(denominator+difference**2))
    nh = energy/z.sqrt(a*b)-z.Rational(1, 2)
    eigenvar = z.symbols("lambda")
    assert z.expand(A.charpoly(eigenvar).as_expr()-((eigenvar+g/2)**2+a*b)) == 0
    retuned = V.subs(r, z.sqrt(a/b)).applyfunc(z.simplify)
    assert retuned == z.diag(z.sqrt(a/b)/2, z.sqrt(b/a)/2)
    assert z.simplify(n0.subs(r, z.sqrt(a/b))) == 0
    K, W, U, gamma, soft = z.symbols("K W U gamma soft", positive=True)
    sub = {a: K*soft, b: U+W*soft, g: gamma*soft, r: z.sqrt(K/W)}
    fields = {"Q": Q, "P": P, "C": C, "purity": purity, "energy": energy,
              "Hamiltonian_quanta": nh, "reference_quanta": n0, "jump_intensity": g*n0}
    fields = {name: z.simplify(value.subs(sub)) for name, value in fields.items()}
    expected_limits = {
        "Q": (fields["Q"], z.sqrt(K/W)/4),
        "soft_times_P": (soft*fields["P"], U/(4*z.sqrt(K*W))),
        "C": (fields["C"], -gamma/(8*z.sqrt(K*W))),
        "purity_over_sqrt_soft": (fields["purity"]/z.sqrt(soft), 2*z.sqrt(W/U)),
        "energy": (fields["energy"], U*z.sqrt(K/W)/4),
        "sqrt_soft_times_Hamiltonian_quanta": (z.sqrt(soft)*fields["Hamiltonian_quanta"], z.sqrt(U)/(4*z.sqrt(W))),
        "soft_times_reference_quanta": (soft*fields["reference_quanta"], U/(8*W)),
        "jump_intensity": (fields["jump_intensity"], gamma*U/(8*W))}
    limits = {}
    for name, (expr, expected) in expected_limits.items():
        value = z.simplify(z.limit(expr, soft, 0, dir="+"))
        assert z.simplify(value-expected) == 0, (name, value, expected)
        limits[name] = str(value)
    zero_u = {name: z.simplify(value.subs(U, 0)) for name, value in fields.items()}
    assert zero_u["purity"] == 1 and zero_u["C"] == 0
    assert zero_u["Hamiltonian_quanta"] == zero_u["reference_quanta"] == zero_u["jump_intensity"] == 0
    exact_sub = {K: 4, W: 1, U: 3, gamma: 2, soft: z.Rational(1, 5)}
    example = {name: str(z.simplify(value.subs(exact_sub))) for name, value in fields.items()}
    assert example["Q"] == "7/13" and example["P"] == "109/52" and example["C"] == "-3/26"
    assert example["energy"] == "17/10" and example["Hamiltonian_quanta"] == "9/16"
    assert example["reference_quanta"] == "45/26" and example["jump_intensity"] == "9/13"
    result = {"created_utc": datetime.now(timezone.utc).isoformat(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "exact_Weyl_dual_generator_checks": list(tests),
              "generic_covariance": [[str(v) for v in V.row(i)] for i in range(2)],
              "generic_determinant": str(z.factor(determinant)),
              "generic_energy": str(energy), "generic_reference_occupation": str(n0),
              "stationary_physical_parameters": {name: str(v) for name, v in fields.items()},
              "positive_U_soft_limits": limits,
              "U_zero_control": {name: str(v) for name, v in zero_u.items()},
              "exact_example_parameters": {str(k): str(v) for k, v in exact_sub.items()},
              "exact_example": example,
              "retuned_covariance": [[str(v) for v in retuned.row(i)] for i in range(2)],
              "retuned_purity": 1, "retuned_jump_intensity": 0,
              "limits": "A separately stipulated stable Gaussian Lindblad mode; no microscopic derivation or interchange of long-time and soft-mode limits.",
              "runtime_seconds": time.monotonic()-tic}
    text = json.dumps(result, indent=2)+"\n"
    (HERE/"GAUSSIAN_RESULTS.json").write_text(text)
    print(text, end="")


if __name__ == "__main__": main()
