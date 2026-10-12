"""R6-5 (a), qubit-native form: one fermion mode per site (staggered) carrying b0.
Kawamoto-Smit spin diagonalisation psi_x = Omega_x chi_x, Omega_x = s1^x1 s2^x2 s3^x3, maps the 2-component naive Weyl law
    h2 = sum_j sigma_j (i/2)(hop_{+j} - hop_{-j})  +  t3 * (1/8) sum_{delta in {+-1}^3} hop_delta   (= t3 c1 c2 c3)
onto two identical copies of a 1-component law. Check: Omega_x^+ Omega_{x+delta} is a phase times the identity for every
NN and body-diagonal delta (so the 1-component law exists), and spectrum(naive) = spectrum(staggered) doubled on L=6."""
import itertools
import numpy as np
s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1.]).astype(complex)]
L = 6; t3 = 0.3
sites = list(itertools.product(range(L), repeat=3)); idx = {x: i for i, x in enumerate(sites)}
def Om(x):
    return np.linalg.matrix_power(s[0], x[0] % 2) @ np.linalg.matrix_power(s[1], x[1] % 2) @ np.linalg.matrix_power(s[2], x[2] % 2)
# requires L even so that Omega is periodic
hops = []   # (delta, 2x2 amplitude): h2 = sum_x sum_delta psi_x^+ T_delta psi_{x+delta}
for j in range(3):
    e = np.zeros(3, int); e[j] = 1
    hops.append((tuple(e), s[j] / (2j)))      # sigma_j sin k_j  <-  (1/2i)(psi^+_x s_j psi_{x+j} - psi^+_x s_j psi_{x-j})
    hops.append((tuple(-e), -s[j] / (2j)))
for dlt in itertools.product([1, -1], repeat=3):
    hops.append((dlt, t3 / 8 * np.eye(2)))
Hn = np.zeros((2 * L ** 3, 2 * L ** 3), complex); Hs = np.zeros((L ** 3, L ** 3), complex)
maxdev = 0.0
for x in sites:
    for dlt, T in hops:
        y = tuple((np.array(x) + np.array(dlt)) % L)
        i, k = idx[x], idx[y]
        Hn[2 * i:2 * i + 2, 2 * k:2 * k + 2] += T
        A = Om(x).conj().T @ T @ Om(y)            # must be (phase) * identity
        maxdev = max(maxdev, abs(A[0, 1]), abs(A[1, 0]), abs(A[0, 0] - A[1, 1]))
        Hs[i, k] += A[0, 0]
print("max deviation of Omega_x^+ T Omega_{x+delta} from (scalar)*1 : %.1e" % maxdev)
print("Hermiticity: naive %.1e, staggered %.1e" % (abs(Hn - Hn.conj().T).max(), abs(Hs - Hs.conj().T).max()))
en = np.sort(np.linalg.eigvalsh(Hn)); es = np.sort(np.linalg.eigvalsh(Hs))
print("max |spec(naive) - spec(staggered) doubled| = %.1e" % abs(en - np.sort(np.concatenate([es, es]))).max())
# body-diagonal staggered amplitudes (phases) seen from the origin
print("staggered body-diagonal amplitudes from x=(0,0,0):", {d: np.round(Hs[idx[(0,0,0)], idx[tuple(np.array(d) % L)]], 4) for d in itertools.product([1, -1], repeat=3)})
