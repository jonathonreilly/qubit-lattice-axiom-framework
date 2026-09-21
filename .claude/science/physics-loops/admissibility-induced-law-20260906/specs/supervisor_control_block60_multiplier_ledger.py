#!/usr/bin/env python3
"""Supervisor control, block 60 (floating point; NOT the exact runner): a ledger linear in the rates, solved by brute force.

Box 7x7x7, walls held at w = 1 and l = 1.  Variables: u_x = log w_x and lam_x = log l_x at the 125 interior sites; chi = exp(lam/2), N = w chi.
Ledger (bond form, every bond with an interior end):   E = sum_x m_x w_x  -  8 K sum_bonds (N_y - N_x)(chi_y - chi_x).
The stationary point in ALL 250 variables is found by a Newton-type root search on the analytic gradient, with no Green function anywhere,
and is compared with the closed form  chi = 1 + Q g,  Q (1 + Q g0) = m/(8K),  w0 = 1/(1 + 2 Q g0),  ledger = 8 K Q = m/chi0.
A second member with the same second-order form, K sum w l (4 Lap lam + 2 q), is solved the same way to show what depends on the member."""
import numpy as np
from scipy.optimize import root

SIDE = 7
NEIGH = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
INT = [(x,y,z) for x in range(1,SIDE-1) for y in range(1,SIDE-1) for z in range(1,SIDE-1)]
IDX = {s:i for i,s in enumerate(INT)}
N_INT = len(INT)
C = (3,3,3)

def full(v, wall):
    a = np.full((SIDE,)*3, wall, dtype=float)
    for s,i in IDX.items(): a[s] = v[i]
    return a

def lap(a, s):
    return sum(a[s[0]+d[0], s[1]+d[1], s[2]+d[2]] for d in NEIGH) - 6*a[s]

def grad_bilinear(z, masses, K):
    u, lam = full(z[:N_INT], 0.0), full(z[N_INT:], 0.0)
    w, chi = np.exp(u), np.exp(lam/2)
    Nf = w*chi
    g = np.zeros(2*N_INT)
    for s,i in IDX.items():
        g[i] = w[s]*(masses.get(s,0.0) + 8*K*chi[s]*lap(chi,s))
        g[N_INT+i] = 0.5*chi[s]*8*K*(w[s]*lap(chi,s) + lap(Nf,s))
    return g

def ledger_bilinear(z, masses, K):
    u, lam = full(z[:N_INT], 0.0), full(z[N_INT:], 0.0)
    w, chi = np.exp(u), np.exp(lam/2)
    Nf = w*chi
    tot = sum(m*w[s] for s,m in masses.items())
    for x in range(SIDE):
        for y in range(SIDE):
            for zz in range(SIDE):
                for d in NEIGH[::2]:
                    t = (x+d[0], y+d[1], zz+d[2])
                    if max(t) >= SIDE: continue
                    if (x,y,zz) in IDX or t in IDX:
                        tot -= 8*K*(Nf[t]-Nf[x,y,zz])*(chi[t]-chi[x,y,zz])
    return tot

def ledger_second(z, masses, K):
    u, lam = full(z[:N_INT], 0.0), full(z[N_INT:], 0.0)
    w, l = np.exp(u), np.exp(lam)
    tot = sum(m*w[s] for s,m in masses.items())
    for x in range(SIDE):
        for y in range(SIDE):
            for zz in range(SIDE):
                s = (x,y,zz)
                nb = [lam[x+d[0],y+d[1],zz+d[2]] for d in NEIGH if 0<=x+d[0]<SIDE and 0<=y+d[1]<SIDE and 0<=zz+d[2]<SIDE]
                if s not in IDX and not any((x+d[0],y+d[1],zz+d[2]) in IDX for d in NEIGH): continue
                lp = sum(v-lam[s] for v in nb); q = 0.5*sum((v-lam[s])**2 for v in nb)
                tot += K*w[s]*l[s]*(4*lp + 2*q)
    return tot

def num_grad(fun, z, h=1e-6):
    g = np.zeros_like(z)
    for i in range(len(z)):
        e = np.zeros_like(z); e[i] = h
        g[i] = (fun(z+e)-fun(z-e))/(2*h)
    return g

def green():
    A = np.zeros((N_INT,N_INT))
    for s,i in IDX.items():
        A[i,i] = 6
        for d in NEIGH:
            t = (s[0]+d[0], s[1]+d[1], s[2]+d[2])
            if t in IDX: A[i,IDX[t]] = -1
    return np.linalg.inv(A)

if __name__ == "__main__":
    K = 0.5
    G = green(); g0 = G[IDX[C],IDX[C]]
    print(f"box Green function at the origin g0 = {g0:.6f}")
    print("\n[W1] analytic gradient of the bilinear member against finite differences of the bond-form ledger (random point):")
    rng = np.random.default_rng(3)
    z0 = 0.2*rng.standard_normal(2*N_INT); masses = {C: 1.3, (2,3,4): 0.7}
    ga = grad_bilinear(z0, masses, K); gn = num_grad(lambda z: ledger_bilinear(z, masses, K), z0)
    print(f"     max |analytic - numeric| = {np.max(np.abs(ga-gn)):.2e}  (the wall terms of the bond form are what put N = 1 on the walls)")
    print("\n[W2] one body at the centre, every interior rate and length varied; closed form against the brute-force stationary point:")
    print("      m      u0(brute)   u0(closed)   lam0(brute)  lam0(closed)  ledger(brute)  8KQ = m/chi0   lam/(-u) one site out, two sites out")
    start = np.zeros(2*N_INT); SOL = {}
    for m in (0.05, 0.5, 5.0, 50.0, 150.0, 500.0):
        masses = {C: m}
        sol = root(lambda z: grad_bilinear(z, masses, K), start, method="hybr", tol=1e-13)
        start = sol.x.copy(); SOL[m] = sol.x.copy()      # continuation in m: the search is started from the previous stationary point
        u0, l0 = sol.x[IDX[C]], sol.x[N_INT+IDX[C]]
        mu = m/(8*K); Q = (-1+np.sqrt(1+4*mu*g0))/(2*g0); chi0 = 1+Q*g0
        led = ledger_bilinear(sol.x, masses, K)
        r1 = sol.x[N_INT+IDX[(4,3,3)]]/(-sol.x[IDX[(4,3,3)]]); r2 = sol.x[N_INT+IDX[(5,3,3)]]/(-sol.x[IDX[(5,3,3)]])
        print(f"   {m:7.2f}  {u0:10.6f}  {-np.log(1+2*Q*g0):10.6f}   {l0:10.6f}   {2*np.log(chi0):10.6f}   {led:12.6f}  {8*K*Q:12.6f}     {r1:.4f}  {r2:.4f}   ok={sol.success}")
    print("     (weak field: lam = -u, the exponent beta = 1;  strong field: the lengths' coefficient 2Q exceeds the rates' P + Q, P = Q/(1 + 2 Q g0))")
    print("\n[W3] far-field coefficients read off the brute-force solution two sites out, against 2Q and P + Q:")
    for m in (0.05, 5.0, 500.0):
        x = SOL[m]
        mu = m/(8*K); Q = (-1+np.sqrt(1+4*mu*g0))/(2*g0); P = Q/(1+2*Q*g0)
        s = (5,3,3); gs = G[IDX[s],IDX[C]]
        chi_s = np.exp(x[N_INT+IDX[s]]/2); N_s = np.exp(x[IDX[s]])*chi_s
        print(f"   m = {m:7.2f}: (chi-1)/g = {(chi_s-1)/gs:.6f} against Q = {Q:.6f};   (1-N)/g = {(1-N_s)/gs:.6f} against P = {P:.6f};   bending/fall = 1 + 2Q/(P+Q) = {1+2*Q/(P+Q):.4f}")
    print("\n[W4] the member K sum w l (4 Lap lam + 2 q) (same second-order form, not bilinear), by brute force on its finite-difference gradient:")
    for m in (0.05, 5.0):
        masses = {C: m}
        sol = root(lambda z: num_grad(lambda y: ledger_second(y, masses, K), z), np.zeros(2*N_INT), method="krylov", tol=1e-9)
        u0, l0 = sol.x[IDX[C]], sol.x[N_INT+IDX[C]]
        mu = m/(8*K); Q = (-1+np.sqrt(1+4*mu*g0))/(2*g0)
        r2 = sol.x[N_INT+IDX[(5,3,3)]]/(-sol.x[IDX[(5,3,3)]])
        print(f"   m = {m:5.2f}: u0 = {u0:.6f} (bilinear member {-np.log(1+2*Q*g0):.6f}), lam0 = {l0:.6f} (bilinear {2*np.log(1+Q*g0):.6f}), lam/(-u) two sites out {r2:.4f}, ledger {ledger_second(sol.x, masses, K):.6f} (bilinear {8*K*Q:.6f})   ok={sol.success}")
