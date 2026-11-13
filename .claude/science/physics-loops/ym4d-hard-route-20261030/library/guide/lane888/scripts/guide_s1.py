# GUIDE only: check formula (S1) of Lemma 3.1 on random small matrices.
# K = diag(w) positive, M real symmetric with zero diagonal blocks pattern not required for the formula
# F(b) = log Tr((e^{bM/2} K e^{bM/2})^a); claim F''(0) = a*sum_{k=0}^{a-1} Tr(M K^k M K^{a-k})/Tr(K^a) - (F'(0))^2-term,
# with F'(0) = a Tr(M K^a)/Tr(K^a).  Take M with zero diagonal so F'(0)=0.
import numpy as np
from numpy.linalg import matrix_power as mp
rng = np.random.default_rng(7)
def expm_sym(X):
    w, V = np.linalg.eigh(X); return (V*np.exp(w))@V.T
for (d, a) in ((2,3),(5,4),(6,7)):
    w = rng.uniform(0.05, 1.0, size=d); K = np.diag(w)
    M = rng.normal(size=(d,d)); M = (M+M.T)/2; np.fill_diagonal(M, 0.0)
    def F(b):
        E = expm_sym(b*M/2); A = E@K@E
        return np.log(np.trace(mp(A,a)))
    h = 1e-3
    fd = (F(h) - 2*F(0) + F(-h))/h**2
    form = a*sum(np.trace(M@mp(K,k)@M@mp(K,a-k)) for k in range(a))/np.trace(mp(K,a))
    # pair form with g_a
    pair = 0.0
    for i in range(d):
        for j in range(i+1,d):
            x = w[j]/w[i]; g = sum(x**k for k in range(a)) + sum(x**k for k in range(1,a+1))
            pair += M[i,j]**2 * w[i]**a * g
    pair *= a/np.trace(mp(K,a))
    print(f"d={d} a={a}: finite difference {fd:.6f}   trace formula {form:.6f}   pair form with g_a {pair:.6f}")
