#!/usr/bin/env python3
"""Independent row-1087 GUIDE calculation. All spin labels here are doubled.

No import from either earlier implementation. See the companion note for
normalizations and derivation. Floating eigensystems discharge no proof.
"""
import os
for _key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS",
             "BLIS_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
from functools import lru_cache
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np
from scipy.linalg import eigh
from scipy.special import ive


def memory_check():
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    size = peak if sys.platform == "darwin" else 1024 * peak
    if size > 2_000_000_000:
        raise MemoryError("2 GB RSS limit exceeded")
    return size


def triangle(a, b, c):
    return min(a, b, c) >= 0 and abs(a-b) <= c <= a+b and (a+b+c) % 2 == 0


@lru_cache(None)
def factorial(n):
    return math.factorial(n)


def delta_sq(a, b, c):
    if not triangle(a, b, c):
        return Fraction(0)
    return Fraction(factorial((a+b-c)//2) * factorial((a-b+c)//2)
                    * factorial((-a+b+c)//2), factorial((a+b+c)//2+1))


@lru_cache(None)
def half_sixj_sq(a, b, d, e, f):
    """Exact square of {a/2 b/2 1/2; d/2 e/2 f/2}.

    Its Racah sum has one term. No floating alternating factorial sum.
    """
    c = 1
    pref = (delta_sq(a, b, c) * delta_sq(a, e, f)
            * delta_sq(d, b, f) * delta_sq(d, e, c))
    if not pref:
        return 0.0
    low = [(a+b+c)//2, (a+e+f)//2, (d+b+f)//2, (d+e+c)//2]
    high = [(a+b+d+e)//2, (a+c+d+f)//2, (b+c+e+f)//2]
    z = max(low)
    assert z == min(high), (a, b, c, d, e, f)
    denom = math.prod(factorial(z-x) for x in low)
    denom *= math.prod(factorial(x-z) for x in high)
    term = Fraction(factorial(z+1), denom)
    return float(pref * term * term)


@lru_cache(None)
def cg(j, m, k, n, p, q):
    """Condon-Shortley Clebsch-Gordan coefficient, exact factorial sum."""
    if (m+n != q or not triangle(j, k, p) or abs(m) > j or abs(n) > k
            or abs(q) > p or (j-m) % 2 or (k-n) % 2 or (p-q) % 2):
        return 0.0
    pref = Fraction((p+1) * factorial((p+j-k)//2)
                    * factorial((p-j+k)//2) * factorial((j+k-p)//2),
                    factorial((j+k+p)//2+1))
    pref *= math.prod(factorial(v//2) for v in
                     (p+q, p-q, j-m, j+m, k-n, k+n))
    a, b, c = (j+k-p)//2, (j-m)//2, (k+n)//2
    d, e = (p-k+m)//2, (p-j-n)//2
    total = Fraction(0)
    for z in range(max(0, -d, -e), min(a, b, c)+1):
        den = math.prod(factorial(v) for v in
                        (z, a-z, b-z, c-z, d+z, e+z))
        total += Fraction((-1)**z, den)
    return math.sqrt(float(pref)) * float(total)


@lru_cache(None)
def magnetic_overlap(p, j, k, jp, kp):
    if not triangle(j, k, p) or not triangle(jp, kp, p):
        return 0.0
    terms = []
    for m in range(-j, j+1, 2):
        n = p-m
        initial = cg(j, m, k, n, p, p)
        if not initial:
            continue
        for alpha in (-1, 1):
            terms.append(initial * cg(jp, m+alpha, kp, n-alpha, p, p)
                         * cg(j, m, 1, alpha, jp, m+alpha)
                         * cg(k, n, 1, -alpha, kp, n-alpha)
                         * (-1)**((1-alpha)//2))
    return math.fsum(terms)


def sheet_generator(p, q, jmax):
    basis = [(j, k) for j in range(jmax+1) for k in range(jmax+1)
             if triangle(j, k, p) and triangle(j, k, q)]
    positions = {state: i for i, state in enumerate(basis)}
    X = np.zeros((len(basis), len(basis)))
    for col, (j, k) in enumerate(basis):
        for jp in (j-1, j+1):
            for kp in (k-1, k+1):
                row = positions.get((jp, kp))
                if row is None:
                    continue
                X[row, col] = (0.5 * math.sqrt((j+1)*(k+1)/((jp+1)*(kp+1)))
                               * magnetic_overlap(p, j, k, jp, kp)
                               * magnetic_overlap(q, j, k, jp, kp))
    asymmetry = float(np.max(np.abs(X-X.T)))
    assert asymmetry < 1e-11, (p, q, asymmetry)
    if p == q == 0:
        want = 0.5 * (np.eye(len(basis), k=1) + np.eye(len(basis), k=-1))
        assert np.max(np.abs(X-want)) < 1e-12
    values, vectors = eigh((X+X.T)/2)
    assert np.max(np.abs(values)) <= 1+1e-11
    memory_check()
    return basis, values, vectors, asymmetry


def ratios(beta, largest_spin):
    return ive(np.arange(1, largest_spin+2), beta) / ive(1, beta)


def zero_block(beta, chars):
    # Character index is doubled spin, 0 .. chars-1.
    r = ratios(beta, 2*chars)
    w = np.outer(r[:chars]**2, r[:chars]**2).ravel()
    Z = np.zeros((chars**2, chars**2))
    for J in range(2*chars-1):
        fusion = np.array([[triangle(a, c, J) for c in range(chars)]
                           for a in range(chars)], dtype=float)
        Z += r[J]**4 * np.kron(fusion, fusion)
    A = w[:, None] * Z * w[None, :]
    # Resolve exact center and layer-swap symmetries first. The small-beta
    # swap splitting is far below the full matrix's absolute solver scale.
    candidates = []
    for center in (-1, 1):
        for swap in (-1, 1):
            columns = []
            for a in range(chars):
                for b in range(a, chars):
                    if (-1)**(a+b) != center or (a == b and swap == -1):
                        continue
                    v = np.zeros(chars**2)
                    if a == b:
                        v[a*chars+b] = 1
                    else:
                        v[a*chars+b] = 1/math.sqrt(2)
                        v[b*chars+a] = swap/math.sqrt(2)
                    columns.append(v)
            Q = np.column_stack(columns)
            block = Q.T @ A @ Q
            bv, bu = eigh(block, subset_by_index=(max(0, len(columns)-3), len(columns)-1))
            candidates.extend((float(value), Q @ vector)
                              for value, vector in zip(bv, bu.T))
    candidates.sort(key=lambda item: item[0], reverse=True)
    vals = np.array([item[0] for item in candidates[:3]])
    vecs = np.column_stack([item[1] for item in candidates[:3]])
    residuals = [float(np.linalg.norm(A @ vecs[:, i]-vals[i]*vecs[:, i]))
                 for i in range(3)]
    parity = np.array([(-1)**(a+b) for a in range(chars) for b in range(chars)])
    centers = [float(np.dot(parity, vecs[:, i]**2)) for i in range(3)]
    swaps = [float(np.sum(vecs[:, i].reshape(chars, chars)
                         * vecs[:, i].reshape(chars, chars).T)) for i in range(3)]
    return vals, (w[:, None]*vecs).reshape(chars, chars, 3), residuals, centers, swaps


def leakage(beta, chars, loop_max):
    """loop_max is largest doubled spin on each collapsed side loop."""
    values, G, residuals, centers, swaps = zero_block(beta, chars)
    # Triangle u <= J+b. Output range exhausts finite inputs, no extra cutoff.
    out_max = loop_max+chars-1
    pairs = [(u, v) for u in range(out_max+1) for v in (u-1, u+1)
             if 0 <= v <= out_max]
    r = ratios(beta, out_max)
    L = np.zeros((2, 2))
    for which, arc in enumerate((1, 2)):
        ampl = np.zeros((2, len(pairs), len(pairs)))
        for J in range(loop_max+1):
            for H in (J-1, J+1):
                if not 0 <= H <= loop_max:
                    continue
                R = np.zeros((len(pairs), chars))
                for row, (u, v) in enumerate(pairs):
                    for b in range(chars):
                        R[row, b] = (math.sqrt((u+1)*(v+1))
                                     * half_sixj_sq(u, v, H, J, b))
                pref = 2*(J+1)*(H+1)*r[J]**arc*r[H]**(4-arc)
                for i in range(2):
                    ampl[i] += pref * R @ G[:, :, i].T @ R.T
            memory_check()
        weights = np.array([r[u]**arc*r[v]**(4-arc) for u, v in pairs])
        for i in range(2):
            L[i, which] = np.sum(ampl[i]**2 * weights[:, None]*weights[None, :])
    ell = (4*L[:, 0]+2*L[:, 1])/values[:2]**2
    # Deliberately wrong adjacent-pair multiplicity, for a negative control.
    mutant = (L[:, 0]+2*L[:, 1])/values[:2]**2
    return dict(beta=beta, chars=chars, loop_max=loop_max,
                output_spin_max=out_max, eigenvalues=values.tolist(),
                residuals=residuals, center_parities=centers, swap_parities=swaps,
                l0=float(ell[0]), l1=float(ell[1]), difference=float(ell[1]-ell[0]),
                m_betaL_zero=float(math.log(values[0]/values[1])),
                mutant_l1=float(mutant[1]))


def face_all(betas, jmax, sector_max):
    # All p,q <= sector_max (doubled spins), not only constant cycles.
    tops = [np.zeros((sector_max+1, sector_max+1)) for b in betas]
    singlet_second = [None for b in betas]
    max_asymmetry = 0.0
    largest_matrix = 0
    for p in range(sector_max+1):
        for q in range(p, sector_max+1):
            if (p-q) % 2:
                continue
            basis, ev, U, asym = sheet_generator(p, q, jmax)
            max_asymmetry = max(max_asymmetry, asym)
            largest_matrix = max(largest_matrix, len(basis))
            for bi, beta in enumerate(betas):
                a = ratios(beta, jmax)
                w = np.array([math.sqrt(a[j]*a[k]) for j, k in basis])
                # exp(-beta) is a common stabilizing scalar; no change to ratios.
                E = (U*np.exp(beta*(ev-1))) @ U.T
                T = w[:, None]*E*w[None, :]
                eig = eigh(T, eigvals_only=True, subset_by_index=(len(basis)-2, len(basis)-1))
                tops[bi][p, q] = tops[bi][q, p] = eig[-1]
                if p == q == 0:
                    singlet_second[bi] = eig[-2]
            memory_check()
    results = []
    for beta, mu, second in zip(betas, tops, singlet_second):
        vacuum = mu[0, 0]**4
        candidates = [(mu[0, 0]**3*second, "one singlet excitation")]
        for cycle in itertools.product(range(sector_max+1), repeat=4):
            if cycle == (0, 0, 0, 0):
                continue
            product = math.prod(mu[cycle[i], cycle[(i+1) % 4]] for i in range(4))
            candidates.append((product, list(cycle)))
        candidates.sort(key=lambda x: x[0], reverse=True)
        results.append(dict(beta=beta, jmax=jmax, sector_max=sector_max,
                            m_betaL_infinity=math.log(vacuum/candidates[0][0]),
                            winning_doubled_sector_cycle=candidates[0][1],
                            singlet_sheet_gap=math.log(mu[0, 0]/second),
                            max_X_asymmetry=max_asymmetry,
                            largest_sheet_matrix=largest_matrix,
                            next_distinct_candidates=[(float(v/vacuum), c)
                                                      for v, c in candidates[:4]]))
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--chars", type=int, required=True)
    parser.add_argument("--loops", type=int, required=True)
    parser.add_argument("--jmax", type=int, required=True)
    parser.add_argument("--sectors", type=int, default=4)
    parser.add_argument("--betas", type=float, nargs="+", default=[2.4, 8, 9, 10])
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--small-beta", action="store_true")
    args = parser.parse_args()
    start = time.monotonic()
    record = dict(grade="GUIDE", implementation="independent exact recoupling / magnetic sums",
                  truncations=vars(args).copy(), leakage=[], face=[])
    record["truncations"]["output"] = str(args.output)
    def save():
        record["elapsed_seconds"] = time.monotonic()-start
        record["peak_RSS_bytes"] = memory_check()
        args.output.write_text(json.dumps(record, indent=2)+"\n")
    for beta in args.betas:
        value = leakage(beta, args.chars, args.loops)
        record["leakage"].append(value)
        save()
        print("LEAKAGE", json.dumps(value), flush=True)
    if args.small_beta:
        record["small_beta"] = []
        for beta in (0.02, 0.05, 0.1):
            x = leakage(beta, 6, 8)
            a_half = ratios(beta, 1)[1]
            item = dict(beta=beta, l0_over_16a4=x["l0"]/(16*a_half**4),
                        l1_over_b2quarter=x["l1"]/(beta**2/4),
                        mutant_ratio=x["mutant_l1"]/(beta**2/4))
            record["small_beta"].append(item)
            print("SMALL_BETA", json.dumps(item), flush=True)
        save()
    record["face"] = face_all(args.betas, args.jmax, args.sectors)
    for item, leak in zip(record["face"], record["leakage"]):
        item["endpoint_difference"] = leak["m_betaL_zero"]-item["m_betaL_infinity"]
        print("FACE", json.dumps(item), flush=True)
    save()
    print("COMPLETE", record["elapsed_seconds"], record["peak_RSS_bytes"], flush=True)


if __name__ == "__main__":
    main()
