#!/usr/bin/env python3
"""Row 965 (gap-squeeze-opus), Step 5: endpoint quantities of the squeeze.
Arithmetic check of the hand computations in the note, plus a GUIDE diagonalisation.
Nothing here proves anything; the note gives the hand formulas and the series.

One plaquette Q_pl (free faces): class functions of the holonomy U = diag(e^{i th}, e^{-i th}),
Weyl measure (2/pi) sin^2 th dth, characters chi_j = sin((2j+1)th)/sin th (orthonormal).
T = M D M, M = exp((beta/2)(cos th - 1)), D chi_j = (c_j/d_j)^4 chi_j,
c_j/d_j = exp(-beta) (2/beta) I_{2j+1}(beta).
Hand bound: lambda_0 >= c_0^5, Tr T = sum_j (c_j/d_j)^4 e^{-beta}(2/beta) sum_{k=0}^{2j} (2k+1) I_{2k+1}(beta),
so S(1) <= Tr T / c_0^5 - 1 = sum_{j>=1/2} A_j^4 sum_{k=0}^{2j} (2k+1) A_k, A_k = I_{2k+1}/I_1.
Cube surface (free): Z = sum_j d_j^2 (c_j/d_j)^6 (closed surface, Euler characteristic 2).
"""
import math, sys, resource
import numpy as np

def rss_guard(limit_gb=2.0):
    # stop the job above 2 GB peak RSS (macOS reports bytes)
    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if peak > limit_gb*1024**3:
        sys.exit("RSS guard: peak %.2f GB above %.1f GB" % (peak/1024**3, limit_gb))

def I(nu, x, kmax=200):
    # modified Bessel function of integer order by its power series (terms in log space)
    s = 0.0
    lx = math.log(x/2)
    for k in range(kmax):
        s += math.exp((2*k+nu)*lx - math.lgamma(k+1) - math.lgamma(k+nu+1))
    return s

def series_terms(nu, x, n=6):
    return [(x/2)**(2*k+nu) / (math.factorial(k)*math.factorial(k+nu)) for k in range(n)]

def plaquette(beta, J2max=24, nq=4000):
    # basis n = 2j = 0..J2max
    A = [I(n+1, beta)/I(1, beta) for n in range(2*J2max+3)]
    c0 = math.exp(-beta)*(2/beta)*I(1, beta)
    D = np.array([(math.exp(-beta)*(2/beta)*I(n+1, beta))**4 for n in range(J2max+1)])
    # quadrature on th in (0, pi) with weight (2/pi) sin^2
    # midpoint rule on (0, pi): the integrands are trigonometric polynomials times an analytic
    # periodic weight, so the rule is exponentially accurate (no large companion matrix)
    th = (np.arange(nq)+0.5)*math.pi/nq; w = np.full(nq, math.pi/nq)
    wt = w*(2/math.pi)*np.sin(th)**2
    chi = np.array([np.sin((n+1)*th)/np.sin(th) for n in range(J2max+1)])
    M = np.exp((beta/2)*(np.cos(th)-1))
    Mmat = (chi*wt*M) @ chi.T
    G = (chi*wt) @ chi.T
    T = Mmat @ np.diag(D) @ Mmat
    ev = np.sort(np.linalg.eigvalsh(T))[::-1]
    lam0 = ev[0]; r = ev[1:]/lam0
    # chi_j chi_j = sum over INTEGER l = 0..2j of chi_l, so int M^2 |chi_j|^2 = e^{-beta}(2/beta) sum_{l=0}^{2j} (2l+1) I_{2l+1}
    # (corrected after the first run, which summed l only up to j)
    trT_formula = sum(D[n]*math.exp(-beta)*(2/beta)*sum((2*l+1)*I(2*l+1, beta) for l in range(0, n+1))
                      for n in range(J2max+1))
    num = 1 + sum(A[n]**4 * sum((2*l+1)*A[2*l] for l in range(0, n+1)) for n in range(1, J2max+1))
    den = sum((n+1)**2 * A[n]**6 for n in range(0, J2max+1))   # Rayleigh quotient with psi = M 1 (cube surface!)
    hand = num/den - 1                                           # S(1) <= Tr T / (Rayleigh lower bound of lambda_0) - 1
    num2 = 1 + sum(A[n]**4 * sum((2*l+1)*A[2*l] for l in range(0, n+1)) for n in range(1, 3))
    den2 = sum((n+1)**2 * A[n]**6 for n in range(0, 3))
    hand2 = num2/den2 - 1
    crude = num - 1                                              # with lambda_0 >= c_0^5 only
    return dict(c0=c0, A=A, lam0=lam0, lam0_over_c05=lam0/c0**5, r=r[:6],
                S=[float(np.sum(r**k)) for k in (1, 2, 3, 4)], gap=-math.log(r[0]),
                trT_num=float(np.trace(T)), trT_formula=trT_formula, hand_S1=hand, hand_S1_two_terms=hand2,
                orth_err=float(np.max(np.abs(G-np.eye(J2max+1)))), crude=crude, ray=den)

def cube_static(beta, J2max=30):
    cj = [math.exp(-beta)*(2/beta)*I(n+1, beta) for n in range(J2max+2)]
    w = [(n+1)**2 * (cj[n]/cj[0])**6 for n in range(J2max+1)]
    Z = sum(w)
    # mean of s_p on the cube surface: d/dbeta log(c_j/d_j) = -1 + 2j/beta + I_{2j+2}/I_{2j+1}
    s = sum(w[n]*(-1 + n/beta + I(n+2, beta)/I(n+1, beta)) for n in range(J2max+1))/Z
    # E[chi_1(U_f)] on the cube surface: face f weight c(U)chi_1(U) = sum_j c'_j chi_j,
    # c'_j = c_{j-1}[j>=1] + c_j[j>=1/2] + c_{j+1}  (in units n = 2j: n-2, n, n+2)
    # cj[n] is the NORMALISED coefficient c_j/d_j; the character coefficient is c_j = (n+1) cj[n]
    # (corrected after run 3, which used cj in place of c_j here)
    cfull = [(n+1)*cj[n] for n in range(len(cj))]
    cj = cj + [math.exp(-beta)*(2/beta)*I(J2max+3, beta)]
    cfull.append((J2max+3)*cj[-1])
    cprime = []
    for n in range(J2max+1):
        v = cfull[n+2]
        if n >= 1: v += cfull[n]
        if n >= 2: v += cfull[n-2]
        cprime.append(v)
    # with d_j = n+1 and coefficients c_j = d_j * (c_j/d_j): Z_ins = sum d^2 (c/d)^5 (c'/d)
    Zins = sum((n+1)**2 * (cj[n]/cj[0])**5 * (cprime[n]/((n+1)*cj[0])) for n in range(J2max+1))
    return dict(Z_over_c06=Z, mean_s=s, mean_x=1+s, E_chi1=Zins/Z, w=w[:4])

if __name__ == "__main__":
    betas = [2.3, 2.45, 2.6, 4.0, 8.0, 16.0, 32.0]
    print("Bessel series terms at x = 2.3 (nu = 1, 2):", [round(t, 6) for t in series_terms(1, 2.3)], [round(t, 6) for t in series_terms(2, 2.3)])
    for b in betas:
        p = plaquette(b, J2max=24 if b < 10 else 80, nq=2000 if b < 10 else 4000)
        rss_guard()
        cs = cube_static(b, J2max=30 if b < 40 else 80)
        print(f"beta={b}")
        print("  I_1..I_5:", [round(I(n, b), 6) for n in range(1, 6)])
        print("  A_1/2=I2/I1 %.6f  A_1=I3/I1 %.6f  A_3/2=I4/I1 %.6f  A_2=I5/I1 %.6f" % tuple(p['A'][1:5]))
        A = p['A'][1]
        print("  one plaquette: c0=%.6f  <x>=I2/I1=%.6f  Var(x)=1-3A/beta-A^2=%.6f" % (p['c0'], A, 1-3*A/b-A*A))
        print("  T=MDM: lam0/c0^5=%.6f  gap E1=%.4f  r_1..r_4=%s" % (p['lam0_over_c05'], p['gap'], [f"{x:.3e}" for x in p['r'][:4]]))
        print("  S(k) k=1..4:", [f"{x:.3e}" for x in p['S']], " hand bound S(1)<= %.4e (j<=1 terms only %.4e; crude lam0>=c0^5: %.4e)" % (p['hand_S1'], p['hand_S1_two_terms'], p['crude']))
        print("  Rayleigh lam0/c0^5 >= %.6f (true %.6f)" % (p['ray'], p['lam0_over_c05']))
        print("  TrT numeric %.6e  formula %.6e  basis orth err %.1e" % (p['trT_num'], p['trT_formula'], p['orth_err']))
        print("  cube surface: Z/c0^6=%.6f  <x>_cube=%.6f  E[chi_1(U_f)]=%.6f  face-loop leading term of S(1;cube) 6 A^4 (1 + E chi_1 - (2<x>)^2) = %.4e" % (
            cs['Z_over_c06'], cs['mean_x'], cs['E_chi1'], 6*A**4*(1+cs['E_chi1']-(2*cs['mean_x'])**2)))
    print("lattice oscillator limit of the one-plaquette gap: 2 arccosh(3) = %.4f" % (2*math.acosh(3)))
    sys.stdout.flush()
