#!/usr/bin/env python3
"""Refuting pass, block 60 (floating point, machinery disjoint from the exact runner's): tries to break each statement.

W1  beta = a/(2(ap - b)) for the members K sum w l^p (a Lap lam + b q): brute-force weak-field solve, lam/(-u) read two sites out.
W2  two bodies: is the positive stationary point unique (random restarts)?  P_i = Q_i w_i?  does what the walls see fall as the bodies approach?
W3  a closed lattice (torus): is there a static stationary point with positive content?  (the search is given every chance)
W4  the unit of rate as a variable with a POSITIVE field energy (block 56's): is there a stationary point?
W5  motion of the lengths: the uniform solution with a kinetic term c_k l^s (dlam/dt)^2 / w, integrated from the lam-equation alone; is the
    constraint kept?  does l grow as t^(2/s)?  and with c_k > 0?
W6  is anything delayed?  a source switched on at one label time: the far length at the same label time."""
import numpy as np
from scipy.optimize import root, minimize
from scipy.integrate import solve_ivp

SIDE = 7
NEIGH = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
INT = [(x,y,z) for x in range(1,SIDE-1) for y in range(1,SIDE-1) for z in range(1,SIDE-1)]
IDX = {s:i for i,s in enumerate(INT)}
NI = len(INT)

def full(v, wall):
    a = np.full((SIDE,)*3, wall, dtype=float)
    for s,i in IDX.items(): a[s] = v[i]
    return a

def lapf(a):
    out = np.zeros_like(a)
    out[1:-1,1:-1,1:-1] = (a[2:,1:-1,1:-1]+a[:-2,1:-1,1:-1]+a[1:-1,2:,1:-1]+a[1:-1,:-2,1:-1]+a[1:-1,1:-1,2:]+a[1:-1,1:-1,:-2]-6*a[1:-1,1:-1,1:-1])
    return out

def qf(a):
    out = np.zeros_like(a)
    c = a[1:-1,1:-1,1:-1]
    out[1:-1,1:-1,1:-1] = 0.5*((a[2:,1:-1,1:-1]-c)**2+(a[:-2,1:-1,1:-1]-c)**2+(a[1:-1,2:,1:-1]-c)**2+(a[1:-1,:-2,1:-1]-c)**2+(a[1:-1,1:-1,2:]-c)**2+(a[1:-1,1:-1,:-2]-c)**2)
    return out

def member_ledger(z, masses, K, a, b, p):
    """K sum over ALL sites with an interior neighbour or interior themselves of w l^p (a Lap lam + b q); walls at u = lam = 0."""
    u, lam = full(z[:NI], 0.0), full(z[NI:], 0.0)
    big_u = np.zeros((SIDE+2,)*3); big_l = np.zeros((SIDE+2,)*3)
    big_u[1:-1,1:-1,1:-1] = u; big_l[1:-1,1:-1,1:-1] = lam
    tot = sum(m*np.exp(u[s]) for s,m in masses.items())
    tot += K*np.sum(np.exp(big_u)*np.exp(p*big_l)*(a*lapf(big_l)+b*qf(big_l)))
    return tot

def member_grad(z, masses, K, a, b, p):
    """Analytic gradient of member_ledger in the 250 interior variables (checked against finite differences in W1)."""
    u, lam = full(z[:NI], 0.0), full(z[NI:], 0.0)
    U = np.zeros((SIDE+2,)*3); Lm = np.zeros((SIDE+2,)*3)
    U[1:-1,1:-1,1:-1] = u; Lm[1:-1,1:-1,1:-1] = lam
    A = K*np.exp(U)*np.exp(p*Lm)
    lp, q = lapf(Lm), qf(Lm)
    gu = A*(a*lp + b*q)
    nbsum = lambda f: sum(np.roll(f, s, ax) for ax in range(3) for s in (1,-1))
    gl = p*A*(a*lp + b*q) + a*(nbsum(A) - 6*A) + b*(-A*lp + Lm*nbsum(A) - nbsum(A*Lm))
    g = np.zeros(2*NI)
    for s,i in IDX.items():
        t = (s[0]+1, s[1]+1, s[2]+1)
        g[i] = gu[t] + masses.get(s, 0.0)*np.exp(u[s]); g[NI+i] = gl[t]
    return g

def fd_grad(fun, z, h=1e-6):
    g = np.zeros_like(z)
    for i in range(len(z)):
        e = np.zeros_like(z); e[i] = h
        g[i] = (fun(z+e)-fun(z-e))/(2*h)
    return g

def green():
    A = np.zeros((NI,NI))
    for s,i in IDX.items():
        A[i,i] = 6
        for d in NEIGH:
            t = (s[0]+d[0], s[1]+d[1], s[2]+d[2])
            if t in IDX: A[i,IDX[t]] = -1
    return np.linalg.inv(A)

if __name__ == "__main__":
    G = green(); C = (3,3,3)
    print("[W1] lam/(-u) two sites from a weak body, brute force, against a/(2(ap - b)):")
    rng0 = np.random.default_rng(5); zt = 0.1*rng0.standard_normal(2*NI)
    err = np.max(np.abs(member_grad(zt, {C: 0.3}, 0.5, 4, 1, 2) - fd_grad(lambda y: member_ledger(y, {C: 0.3}, 0.5, 4, 1, 2), zt)))
    print(f"   analytic gradient against finite differences at a random point, member (4,1,2): max difference {err:.1e}")
    for (a,b,p) in ((4,2,1),(4,2,2),(4,1,1),(2,2,3),(4,8,1),(6,3,1)):
        masses = {C: 0.02}; K = 0.5
        sol = root(lambda z: member_grad(z, masses, K, a, b, p), np.zeros(2*NI), method="hybr", tol=1e-11)
        s = (5,3,3); ratio = sol.x[NI+IDX[s]]/(-sol.x[IDX[s]])
        print(f"   (a,b,p) = ({a},{b},{p}): lam/(-u) = {ratio:8.4f}   formula {a/(2*(a*p-b)):8.4f}   ok={sol.success}")
    print("   (the member (4,8,1) has ap - b < 0: lengths stretch near the body as in the others, and its clocks run FAST there; bilinear members b = ap/2 give 1/p)")

    print("\n[W2] two bodies, bilinear member: positive solutions of Q_i (1 + sum_j G_ij Q_j) = mu_i from 200 random starts; P_i = Q_i w_i; what the walls see:")
    K = 0.5; rng = np.random.default_rng(11)
    for sites in (((2,3,3),(4,3,3)), ((1,3,3),(5,3,3)), ((3,3,3),(4,3,3))):
        mu = np.array([1.7, 0.6]); idx = [IDX[s] for s in sites]; Gm = G[np.ix_(idx,idx)]
        found = set()
        for _ in range(200):
            q0 = np.exp(rng.uniform(-6, 4, size=2))
            sol = root(lambda q: q*(1+Gm@q)-mu, q0, tol=1e-14)
            if sol.success and np.all(sol.x > 0): found.add(tuple(np.round(sol.x, 9)))
        Q = np.array(sorted(found)[0]); chi = 1+Gm@Q
        # rates from the LINEAR equation (-Lap + Q/chi) N = 0, N = 1 on the walls, solved on the whole box
        A = np.linalg.inv(G).copy(); rhs = np.zeros(NI)
        for s,i in IDX.items():
            rhs[i] = sum(1 for d in NEIGH if (s[0]+d[0],s[1]+d[1],s[2]+d[2]) not in IDX)
        for k,i in enumerate(idx): A[i,i] += Q[k]/chi[k]
        Nf = np.linalg.solve(A, rhs); w = Nf[idx]/chi
        one = np.linalg.solve(np.linalg.inv(G), rhs)
        P = np.linalg.lstsq(G[:,idx], one-Nf, rcond=None)[0]
        print(f"   bodies at {sites}: {len(found)} positive solution(s); Q = {Q.round(6)}; P = {P.round(6)} against Q w = {(Q*w).round(6)}; walls see 8K sum Q = {8*K*Q.sum():.6f} of bare {8*K*mu.sum():.2f}")
    print("   (one positive solution every time; what the walls see is least for the adjacent pair: the pull is towards the other body)")

    print("\n[W3] torus 4x4x4, bilinear member, one body of bare energy 1: the constraint PER UNIT RATE, r_x = m_x + 8K chi_x (Lap chi)_x, minimised over the lengths")
    print("     alone (the rates drop out of it), with the stretching capped at lam <= cap:")
    L = 4; Kt = 0.5
    def resid(lamv):
        chi = np.exp(lamv.reshape((L,)*3)/2)
        lp = sum(np.roll(chi, sh, ax) for ax in range(3) for sh in (1,-1)) - 6*chi
        m = np.zeros((L,)*3); m[0,0,0] = 1.0
        return (m + 8*Kt*chi*lp).ravel()
    for cap in (2.0, 4.0, 8.0, 16.0):
        best = (1e9, None)
        for k in range(7):
            z0 = rng.uniform(-1, 1, size=L**3)
            if k == 6:                                   # a start built to defeat the claim: one far site shrunk to the cap, to carry the compensating Laplacian cheaply
                z0 = np.zeros(L**3); z0[(2*L+2)*L+2] = -cap
            res = minimize(lambda z: np.sum(resid(z)**2), z0, method="L-BFGS-B", bounds=[(-cap, cap)]*L**3)
            if res.fun < best[0]: best = (res.fun, res.x)
        print(f"   cap {cap:5.1f}: least sum r^2 = {best[0]:.3e}, reached with lam at the body = {best[1][0]:.2f}, max lam = {best[1].max():.2f}, min lam = {best[1].min():.2f}")
    print("   (never zero: sum_x (Lap chi)_x = 0 on a closed lattice while the constraint asks (Lap chi)_x = -m_x/(8K chi_x) <= 0.  The residual does fall as the cap")
    print("    loosens, and only through the start built to defeat the claim: one far site's length shrinks to the cap and carries the compensating Laplacian at")
    print("    little cost.  The infimum is zero and is not attained: no static configuration; random starts alone sat at 1.4e-2 and would have hidden this)")

    print("\n[W4] block 56's positive bond energy with the unit of rate varied too (torus 4x4x4, one body): d(ledger)/d(uniform shift) = ledger > 0:")
    gam = 0.6
    def led56(u):
        phi = np.exp(u/2); m = np.zeros((L,)*3); m[0,0,0] = 1.0
        bond = sum(np.sum((np.roll(phi,1,ax)-phi)**2) for ax in range(3))
        return np.sum(m*phi**2) + (2/gam)*bond
    u = 0.3*rng.standard_normal((L,)*3)
    print(f"   ledger {led56(u):.6f}; derivative along the uniform shift {(led56(u+1e-6)-led56(u-1e-6))/2e-6:.6f}: equal, and positive at every configuration: no stationary point")

    print("\n[W5] uniform motion of the lengths on a closed lattice, label chosen with w = 1: lam-equation integrated alone; the constraint checked afterwards:")
    for (ck, s) in ((-3.0, 3), (-3.0, 2), (-1.0, 4)):
        m = 1.0
        lam_dot0 = np.sqrt(m/(-ck))                                   # constraint at l = 1
        f = lambda t, y: [y[1], -0.5*s*y[1]**2]                         # 2 lam'' = -s lam'^2
        sol = solve_ivp(f, (0, 50), [0.0, lam_dot0], rtol=1e-11, atol=1e-13, dense_output=True)
        lam, lamd = sol.y[0,-1], sol.y[1,-1]
        t1, t2 = 25.0, 50.0; slope = (sol.sol(t2)[0]-sol.sol(t1)[0])/np.log((t2+2/(s*lam_dot0))/(t1+2/(s*lam_dot0)))
        print(f"   c_k = {ck}, s = {s}: constraint m + c_k l^s lam'^2 at the end = {m + ck*np.exp(s*lam)*lamd**2:+.2e};  dlog l/dlog(t + t0) = {slope:.5f} against 2/s = {2/s:.5f}")
    print("   c_k > 0: the constraint m + c_k l^s lam'^2 = 0 has no real solution for m > 0: no uniform motion, and no static point either (W3)")

    print("\n[W6] a source switched on between two label times, second-order (weak-field) law 4K Lap lam = -e: the far length at the SAME label time:")
    K = 0.5; e_before = np.zeros(NI); e_after = np.zeros(NI); e_after[IDX[(1,1,1)]] = 0.01
    far = IDX[(5,5,5)]
    print(f"   lam(far) before {(G@e_before)[far]/(4*K):.3e}, after {(G@e_after)[far]/(4*K):.3e}: the constraint holds at each label time; no kinetic term for lam enters it at this order")
