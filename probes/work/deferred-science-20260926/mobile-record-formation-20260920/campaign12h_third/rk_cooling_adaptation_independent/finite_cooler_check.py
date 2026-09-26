#!/usr/bin/env python3
"""Independent exact finite controls for detuned and weighted plaquette coolers.

Reuses only the already sealed independent three-square geometry. All new
operators, stationary equations and polynomial identities are assembled here.
"""
from __future__ import annotations
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import sympy as s
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
OLD = HERE.parent/"gauge_readout_cooling_independent/COOLING_RESULTS.json"
OLD_HASH = "0707122f13d02f7c283df20dd8f50543872f97266311b9c598ac93573fbba0e4"


def zero(m):
    return all(s.cancel(v) == 0 for v in m)


def vec(m):
    return s.Matrix(list(m))  # row-major, consistently throughout


def jump(dim, pairs, r=s.Integer(1)):
    ell = s.zeros(dim)
    for a, b in pairs:
        ell[a, a] += r/(1+r*r)
        ell[a, b] -= 1/(1+r*r)
        ell[b, a] += r*r/(1+r*r)
        ell[b, b] -= r/(1+r*r)
    assert zero(ell*ell)
    assert zero((ell.H*ell)**2-ell.H*ell)
    return ell


def generator(h, jumps, rates):
    dim = h.rows
    columns = []
    for row in range(dim):
        for col in range(dim):
            unit = s.zeros(dim); unit[row, col] = 1
            out = -s.I*(h*unit-unit*h)
            for ell, rate in zip(jumps, rates):
                loss = ell.H*ell
                out += rate*(ell*unit*ell.H-(loss*unit+unit*loss)/2)
            columns.append(vec(out))
    return s.Matrix.hstack(*columns)


def exact_rank(m):
    return int(DomainMatrix.from_Matrix(m).to_field().rank())


def detuned(words, pairs, d):
    dim = len(words)
    jumps = [jump(dim, p) for p in pairs]
    rates = [s.Integer(1)]*len(jumps)
    delta = s.Rational(1, 5); j = s.Integer(1)
    dmat = s.diag(*d)
    pm = [ell.H*ell for ell in jumps]
    h = 2*j*sum(pm, s.zeros(dim))-delta*dmat
    loss = sum(pm, s.zeros(dim))
    p0 = s.ones(dim)/dim
    gen = generator(h, jumps, rates)
    assert exact_rank(gen) == dim*dim-1
    # Solve the trace-one stationary equation exactly in the rational complex field.
    a = s.Matrix(gen); rhs = s.zeros(dim*dim, 1)
    a[0, :] = vec(s.eye(dim)).T; rhs[0] = 1
    stationary = a.inv(method="DM")*rhs
    rho = s.Matrix(dim, dim, list(stationary))
    rho = rho.applyfunc(s.cancel)
    assert zero(gen*vec(rho)) and zero(rho-rho.H) and s.trace(rho) == 1
    minors = [s.cancel(rho[:k, :k].det(method="domain-ge")) for k in range(1, dim+1)]
    assert all(v.is_positive is True for v in minors)
    intensity = s.cancel(s.trace(loss*rho))
    purity = s.cancel(s.trace(rho*rho))
    assert 0 < intensity and purity < 1
    mean_d = s.Rational(sum(d), dim)
    variance_d = s.Rational(sum((a-mean_d)**2 for a in d), dim)
    defect = -s.I*(h*p0-p0*h)
    assert s.trace(defect.H*defect) == 2*delta**2*variance_d
    # Conservative fully elementary lower bound used in the proof.
    k_lower = min(rates)/((dim-1)**2)
    c_upper = 4*abs(j)*len(jumps)+abs(delta)*(max(d)-min(d))+2*sum(rates)
    rate_lower = s.cancel(k_lower*delta**2*variance_d/c_upper**2)
    assert intensity > rate_lower > 0
    # Constant-flippability physical one-square component: detuning is a scalar.
    one_ell = jump(2, [(0, 1)])
    one_h = 2*j*one_ell.H*one_ell-delta*s.eye(2)
    one_p0 = s.ones(2)/2
    assert zero(generator(one_h, [one_ell], [1])*vec(one_p0))
    return {"J": str(j), "delta": str(delta), "rates": list(map(str, rates)),
            "flippability": d, "uniform_variance_d": str(variance_d),
            "uniform_stationarity_defect_HS_squared_exact": str(s.trace(defect.H*defect)),
            "Liouvillian_rank_exact": exact_rank(gen),
            "stationary_density_exact": [[str(rho[i, k]) for k in range(dim)] for i in range(dim)],
            "positive_leading_principal_minors_exact": list(map(str, minors)),
            "stationary_purity_exact": str(purity),
            "stationary_jump_intensity_exact": str(intensity),
            "stationary_jump_intensity_numeric": float(intensity),
            "general_conservative_rate_lower_bound_exact": str(rate_lower),
            "constant_flippability_single_square_target_stationary": True,
            "zero_delta_original_target_stationary": zero(generator(h+delta*dmat, jumps, rates)*vec(p0))}


def weighted(words, pairs, d):
    dim = len(words)
    # theta=2 log2 makes all amplitudes and projectors exactly rational.
    amplitude = s.Matrix([s.Integer(2)**a for a in d])
    target = amplitude*amplitude.T/(amplitude.T*amplitude)[0]
    classes = []
    for p, row in enumerate(pairs):
        for m in sorted({d[b]-d[a] for a, b in row}):
            same = [(a, b) for a, b in row if d[b]-d[a] == m]
            classes.append((p, m, same))
    jumps = []
    lower_rows = []
    t = s.symbols("t", real=True)
    for p, m, same in classes:
        r = s.Integer(2)**m
        ell = jump(dim, same, r)
        assert zero(ell*amplitude)
        jumps.append(ell)
        delta_f = {words[b]-words[a] for a, b in same}
        assert len(delta_f) == 1
        shift = next(iter(delta_f))
        for degree in range(dim):
            f = t**degree
            diff = s.expand(f.subs(t, t+shift)-f)
            g = s.Integer(0)
            for k in range(degree):
                g -= r/(1+r*r)*(-r*r/(1+r*r))**k*diff
                diff = s.expand(diff.subs(t, t+shift)-diff)
            g = s.expand(g)
            assert g == 0 or s.degree(g, t) <= degree-1
            vf = s.Matrix([amplitude[i]*f.subs(t, a) for i, a in enumerate(words)])
            vg = s.Matrix([amplitude[i]*g.subs(t, a) for i, a in enumerate(words)])
            assert zero(ell.H*ell*vf-ell.H*vg)
        lower_rows.append({"p": p, "m": m, "r_exact": str(r), "pairs": same,
                           "weighted_degree_lowering_exact_degrees": [0, dim-1]})
    rates = [s.Integer(i+1) for i in range(len(jumps))]
    hs = [s.Rational((-1)**i*(i+2), 3) for i in range(len(jumps))]
    h = sum((hh*ell.H*ell for hh, ell in zip(hs, jumps)), s.zeros(dim))
    gen = generator(h, jumps, rates)
    rank = exact_rank(gen)
    assert rank == dim*dim-1
    assert zero(h*amplitude) and zero(gen*vec(target))
    common_rank = exact_rank(s.Matrix.vstack(*jumps))
    assert common_rank == dim-1
    # Resolving m is a real instrument change, even when theta=0.
    first, second = pairs[0]
    da = s.zeros(dim, 1); db = s.zeros(dim, 1)
    da[first[0]] = 1/s.sqrt(2); da[first[1]] = -1/s.sqrt(2)
    db[second[0]] = 1/s.sqrt(2); db[second[1]] = -1/s.sqrt(2)
    v = (da+db)/s.sqrt(2); rho = v*v.H
    whole = jump(dim, pairs[0])
    parts = [jump(dim, [pair]) for pair in pairs[0]]
    unsplit = whole*rho*whole.H
    split = sum((part*rho*part.H for part in parts), s.zeros(dim))
    assert zero(whole.H*whole-sum((part.H*part for part in parts), s.zeros(dim)))
    difference_squared = s.trace((unsplit-split).H*(unsplit-split))
    assert difference_squared == s.Rational(1, 2)
    return {"theta": "2 log(2)", "target_projector_exact": [[str(v) for v in target.row(i)] for i in range(dim)],
            "groups": lower_rows, "rates": list(map(str, rates)), "h": list(map(str, hs)),
            "common_dark_dimension_exact": dim-common_rank, "Liouvillian_rank_exact": rank,
            "weighted_target_stationary_exact": True,
            "theta_zero_resolved_m_vs_unresolved_jump_HS_squared": str(difference_squared),
            "instrument_scope": "Separate p,m jumps are the stipulated generator; theta=0 does not generally reconstruct the single unresolved L_p generator."}


def main():
    tic = time.monotonic()
    assert hashlib.sha256(OLD.read_bytes()).hexdigest() == OLD_HASH
    old = json.loads(OLD.read_text())["physical_controls"]
    words = old["component"]; pairs = old["oriented_pairs_by_plaquette"]
    d = [sum(any(i in pair for pair in row) for row in pairs) for i in range(len(words))]
    output = {"created_utc": datetime.now(timezone.utc).isoformat(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "reused_geometry_source": {"path": str(OLD), "sha256": OLD_HASH},
              "component": words, "detuned": detuned(words, pairs, d),
              "weighted": weighted(words, pairs, d), "runtime_seconds": time.monotonic()-tic}
    text = json.dumps(output, indent=2)+"\n"
    (HERE/"FINITE_COOLER_RESULTS.json").write_text(text)
    print(text, end="")


if __name__ == "__main__":
    main()
