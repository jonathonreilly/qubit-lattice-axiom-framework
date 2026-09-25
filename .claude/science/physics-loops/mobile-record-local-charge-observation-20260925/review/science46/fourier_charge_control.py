#!/usr/bin/env python3
"""Fresh exact PRE46 cubic Fourier check in Z[z]/(z^(L/2)+1), L=4,8,16.
No floating scientific arithmetic, numerical diagonalizer, or imported code.
"""
from itertools import product
import json
import time


def add_monomial(coefficients, exponent, multiplier, L):
    r = exponent % L
    if r >= L//2:
        coefficients[r-L//2] -= multiplier
    else:
        coefficients[r] += multiplier


def dot(k, x):
    return sum(a*b for a, b in zip(k, x))


def main():
    started = time.perf_counter()
    groups = []
    for L in (4, 8, 16):
        vertices = tuple(product(range(L), repeat=3))
        V = len(vertices)
        edges = []
        for a in vertices:
            if sum(a) % 2:
                continue
            neighbors = set()
            for axis in range(3):
                for sign in (-1, 1):
                    b = list(a)
                    b[axis] = (b[axis]+sign) % L
                    neighbors.add(tuple(b))
            assert len(neighbors) == 6
            edges.extend((a, b) for b in sorted(neighbors))
        assert len(edges) == 3*V
        modes = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (L//2,)*3, (L-1, 0, 0))
        means = []
        covariances = []
        for k in modes:
            total = [0]*(L//2)
            for x in vertices:
                add_monomial(total, dot(k, x), -60*((-1)**sum(x)), L)
            expected = [-60*V]+[0]*(L//2-1) if k == (L//2,)*3 else [0]*(L//2)
            assert total == expected
            means.append(dict(k_index=k, mean_times_sqrt_volume_over_kappa=total))
            laplacian = [6]+[0]*(L//2-1)
            for ki in k:
                add_monomial(laplacian, ki, -1, L)
                add_monomial(laplacian, -ki, -1, L)
            for ell in modes:
                total = [0]*(L//2)
                for a, b in edges:
                    for x, sx in ((a, 1), (b, -1)):
                        for y, sy in ((a, 1), (b, -1)):
                            add_monomial(total, dot(ell, y)-dot(k, x), 20*sx*sy, L)
                assert all(c % V == 0 for c in total)
                normalized = [c//V for c in total]
                expected = [20*c for c in laplacian] if k == ell else [0]*(L//2)
                assert normalized == expected
                covariances.append(dict(k_index=k, ell_index=ell,
                                        derivative_over_kappa_polynomial=normalized))
        groups.append(dict(L=L, vertices=V, oriented_edges=len(edges),
                           cyclotomic_polynomial=f'z^{L//2}+1', mean_rows=means,
                           Hermitian_covariance_rows=covariances))
    print(json.dumps(dict(status='All exact cubic Fourier normalization checks passed',
                          groups=groups, mean_rows=18, covariance_rows=108,
                          normalization='f_k(x)=exp(2 pi i k.x/L)/sqrt(L^3); polynomial z=exp(2 pi i/L)',
                          scientific_arithmetic='integer cyclotomic coefficients only',
                          prior_or_author_code_imported=False,
                          elapsed_seconds=time.perf_counter()-started), indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
