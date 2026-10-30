#!/usr/bin/env python3
"""Check that the contour part of Balaban's linearised average (CMP 109 (0.4)) is a coarse gradient,
so that coarse curls of Q = curls of Q_path, and that Q_path has the product symbol
    Qhat_mumu(q) = D_L(q_mu)^2 prod_{nu != mu} D_L(q_nu) / L^4 ,  D_L(q)=sin(Lq/2)/sin(q/2).

PRE-STATED criteria (d=4 replaced by d=3 only for speed of the brute force, the identity is dimension free):
 C1. For random fine bond field theta on a periodic fine lattice: for every coarse plaquette,
     sum over its 4 bonds of (Q theta) equals sum of (Q_path theta), up to 1e-10.
 C2. Q theta (c) = Q_path theta (c) + Phi(y) - Phi(y') for every coarse bond, with the block functional
     Phi(y) = avg_{x in B(y)} avg_Gamma theta(Gamma_{y,x}).
 C3. The Fourier symbol of Q_path on plane waves agrees with the product formula up to 1e-10.
 FAIL if any residual exceeds the tolerance.
"""
import itertools, cmath, math, random
import numpy as np

def run(d=3, L=3, ncoarse=3, seed=1):
    N = L*ncoarse
    rng = np.random.default_rng(seed)
    theta = rng.normal(size=(d,)+(N,)*d)   # theta[rho][x] on bond x -> x+e_rho
    R = (L-1)//2
    pts = list(itertools.product(range(-R, R+1), repeat=d))
    def bond_val(z, rho, th):
        return th[(rho,)+tuple(int(v) % N for v in z)]
    def contour_sum(y, x, th):
        """average over shortest axial contours from y to y+x of the signed sum of th"""
        nz = [i for i in range(d) if x[i] != 0]
        perms = list(itertools.permutations(nz)) if nz else [()]
        tot = 0.0
        for p in perms:
            cur = list(y)
            for i in p:
                target = y[i]+x[i]
                while cur[i] != target:
                    if target > cur[i]:
                        tot += bond_val(cur, i, th); cur[i] += 1
                    else:
                        cur[i] -= 1; tot -= bond_val(cur, i, th)
        return tot/len(perms)
    def Phi(y, th):
        return sum(contour_sum(y, x, th) for x in pts)/len(pts)
    def Qpath(y, mu, th):
        s = 0.0
        for x in pts:
            z = [y[i]+x[i] for i in range(d)]
            for _ in range(L):
                s += bond_val(z, mu, th); z[mu] += 1
        return s/len(pts)
    def Qfull(y, mu, th):
        yp = list(y); yp[mu] += L
        s = 0.0
        for x in pts:
            s += contour_sum(y, x, th)
            z = [y[i]+x[i] for i in range(d)]
            for _ in range(L):
                s += bond_val(z, mu, th); z[mu] += 1
            s -= contour_sum(yp, x, th)
        return s/len(pts)
    res2 = 0.0
    for yc in itertools.product(range(ncoarse), repeat=d):
        y = [L*v for v in yc]
        for mu in range(d):
            yp = list(y); yp[mu] += L
            res2 = max(res2, abs(Qfull(y, mu, theta)-(Qpath(y, mu, theta)+Phi(y, theta)-Phi(yp, theta))))
    res1 = 0.0
    for yc in itertools.product(range(ncoarse), repeat=d):
        y = [L*v for v in yc]
        for mu, nu in itertools.combinations(range(d), 2):
            ym = list(y); ym[mu] += L
            yn = list(y); yn[nu] += L
            a = Qfull(y, mu, theta)+Qfull(ym, nu, theta)-Qfull(yn, mu, theta)-Qfull(y, nu, theta)
            b = Qpath(y, mu, theta)+Qpath(ym, nu, theta)-Qpath(yn, mu, theta)-Qpath(y, nu, theta)
            res1 = max(res1, abs(a-b))
    # C3: plane wave in component mu
    res3 = 0.0
    for trial in range(20):
        n = rng.integers(0, N, size=d)
        q = 2*math.pi*n/N
        mu = int(rng.integers(0, d))
        def Dk(qq):
            return L if abs(math.sin(qq/2)) < 1e-14 else math.sin(L*qq/2)/math.sin(qq/2)
        th = np.zeros((d,)+(N,)*d, dtype=complex)
        for z in itertools.product(range(N), repeat=d):
            th[(mu,)+z] = cmath.exp(1j*sum(q[i]*z[i] for i in range(d)))
        # bond at y: centre of block average; take y=0
        val = Qpath([0]*d, mu, th)
        pred = Dk(q[mu])**2
        for nu in range(d):
            if nu != mu:
                pred *= Dk(q[nu])
        pred = pred/L**d*cmath.exp(1j*q[mu]*(L-1)/2)
        res3 = max(res3, abs(val-pred))
    return res1, res2, res3

if __name__ == '__main__':
    r = run()
    print("C1 max |curl Q - curl Q_path| =", r[0])
    print("C2 max |Q - Q_path - grad Phi| =", r[1])
    print("C3 max |Q_path plane wave - product symbol| =", r[2])
    print("PASS" if max(r) < 1e-10 else "FAIL")
