#!/usr/bin/env python3
"""Exact one-step weight norm of Balaban's linearised bond average (CMP 109 (0.4)), d=4.

theta_bar(c) = avg_{x in B(y)} [ avg_{Gamma in G(y,x)} theta(Gamma) + theta([x,x'])
                                 - avg_{Gamma' in G(y',x')} theta(Gamma') ]
with y' = y + L e_mu, x' = x + L e_mu.  G(y,x) = shortest axial contours, one per
permutation of the coordinate directions in which x-y is nonzero.

PRE-STATED criterion. Sigma2(L) := sum_b w_b^2 (exact rational arithmetic).
  If Sigma2(L) > 1 the composite weights grow (checked separately in the composite script).
Prints Sigma2 for odd L. Exact: uses Fractions via the closed formula, cross-checked for
small L by brute-force enumeration over x and permutations.
"""
import sys, itertools
from fractions import Fraction as Fr
from math import comb, factorial

d = 4

def contour_weight_table(L):
    """w(z,rho) for contours from the centre 0 of B(0), R=(L-1)/2.
    For a bond b=(z,z+e_rho) (z_rho>=0, traversed +) or (z_rho<0, traversed -; sign -).
    A = {i != rho : z_i != 0}. Returns dict (abs size a=|A|, n_rho=#x_rho values) -> weight
    (unsigned), with L^-d normalisation."""
    R = (L-1)//2
    tab = {}
    for a in range(0, d):       # a = |A|
        m = d-1-a               # free directions besides A and rho
        s = Fr(0)
        for e in range(0, m+1):
            # e extra nonzero directions, each (L-1) choices; m-e zero (1 choice)
            s += comb(m, e) * (L-1)**e * Fr(factorial(a)*factorial(e), factorial(a+e+1))
        tab[a] = s / L**d       # still to multiply by the count of x_rho
    return R, tab

def brute_force(L):
    """Full bond dictionary by enumeration; exact. Feasible for small L only."""
    R = (L-1)//2
    rng = range(-R, R+1)
    w = {}
    def add(b, v):
        w[b] = w.get(b, Fr(0)) + v
    mu = 0
    pts = list(itertools.product(rng, repeat=d))
    norm = Fr(1, L**d)
    for x in pts:
        nz = [i for i in range(d) if x[i] != 0]
        perms = list(itertools.permutations(nz)) if nz else [()]
        wt = norm * Fr(1, len(perms))
        for base, sign in (((0,)*d, 1), (tuple([L]+[0]*(d-1)), -1)):
            xx = tuple(base[i]+x[i] for i in range(d))
            for p in perms:
                cur = list(base)
                for i in p:
                    step = 1 if xx[i] > cur[i] else -1
                    while cur[i] != xx[i]:
                        if step == 1:
                            add((tuple(cur), i), sign*wt)
                        else:
                            prev = list(cur); prev[i] -= 1
                            add((tuple(prev), i), -sign*wt)
                        cur[i] += step
        # straight part [x,x'] along mu
        cur = list(x)
        for _ in range(L):
            add((tuple(cur), mu), norm)
            cur[mu] += 1
    return w

def sigma2_formula(L):
    """Sum of squares of total weight. Contour weights from both blocks plus the path part."""
    R, tab = contour_weight_table(L)
    # Build on the fly: the only overlaps are between direction-mu bonds of the path tube
    # and direction-mu contour bonds with the same transverse position. Handle by explicit
    # one-dimensional profiles.
    mu = 0
    total = Fr(0)
    # bonds in directions rho != mu: contributions from the two blocks are disjoint.
    # Block at 0: for rho != mu, position z with z_rho in [-R,R-1], others in [-R,R].
    def count_xrho(zrho):
        # number of x_rho for which the bond (zrho,zrho+1) in direction rho is on the way
        return R - zrho if zrho >= 0 else zrho + R + 1
    for rho in range(1, d):
        s = Fr(0)
        for zrho in range(-R, R):
            c = count_xrho(zrho)
            for a in range(0, d):
                # number of positions of the other 3 coordinates with exactly a nonzero
                npos = comb(d-1, a) * (L-1)**a
                s += npos * (c * tab[a])**2
        total += 2*s   # two blocks
    # direction mu: profile along mu for fixed transverse position with a_perp nonzero.
    for a in range(0, d):
        npos = comb(d-1, a) * (L-1)**a
        prof = {}
        for zmu in range(-R, R+L):
            v = Fr(0)
            # path part: count of x_mu with x_mu <= zmu < x_mu+L
            lo = max(-R, zmu-L+1); hi = min(R, zmu)
            if hi >= lo:
                v += Fr(hi-lo+1, L**d)
            # contour from block at 0 (sign + when traversed forward, zmu>=0; - otherwise)
            if -R <= zmu < R:
                v += (1 if zmu >= 0 else -1) * count_xrho(zmu) * tab[a]
            # contour from block at L enters with overall sign -: position zmu-L
            zz = zmu - L
            if -R <= zz < R:
                v -= (1 if zz >= 0 else -1) * count_xrho(zz) * tab[a]
            prof[zmu] = v
        total += npos * sum(u*u for u in prof.values())
    return total

if __name__ == '__main__':
    for L in (3, 5):
        w = brute_force(L)
        s2 = sum(v*v for v in w.values())
        f2 = sigma2_formula(L)
        print(f"L={L}: brute Sigma2 = {float(s2):.10f}  formula = {float(f2):.10f}  equal={s2==f2}")
    print(" L   Sigma2(L)   (contour-free Sigma2 would be ~ 2/(3L^2)-ish)")
    for L in list(range(3, 62, 2)) + [81, 101, 151, 201]:
        print(f"{L:4d}  {float(sigma2_formula(L)):.6f}")
