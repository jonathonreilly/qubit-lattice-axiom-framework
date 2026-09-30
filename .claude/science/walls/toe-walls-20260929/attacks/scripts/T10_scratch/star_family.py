"""Test B: the June 'redundancy is rare' statistic and its dependence on the fragment definition and N.
Pointer qubit S (Z eigenvalue s=+-1), environment qubits in |0>, H = Z_S (sum_k c_k X_k + sum_<kl> d_kl X_k X_l).
All X-terms commute, so |E_s> = exp(-i s t B)|0..0> exactly.  chi_F (Holevo of the z-pointer, prior 1/2) from exact reduced states."""
import itertools, json
import numpy as np

rng = np.random.default_rng(20260929)

def h2(p):
    p = np.clip(p, 1e-15, 1 - 1e-15); return float(-p*np.log2(p) - (1-p)*np.log2(1-p))

def ent(rho):
    ev = np.linalg.eigvalsh(rho); ev = ev[ev > 1e-14]; return float(-(ev*np.log2(ev)).sum())

def branch_states(N, c, dpairs, t):
    # X-eigenbasis: B(x) = sum_k c_k x_k + sum d_kl x_k x_l with x=+-1
    xs = np.array(list(itertools.product([1, -1], repeat=N)))  # (2^N, N)
    B = xs @ c
    for (k, l), d in dpairs.items():
        B = B + d * xs[:, k] * xs[:, l]
    H1 = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    Hn = H1
    for _ in range(N - 1):
        Hn = np.kron(Hn, H1)
    # |0..0> in X basis has amplitude 2^{-N/2} on every x (with sign (+) since |0> = (|+>+|->)/sqrt2)
    amp = np.ones(2**N) / np.sqrt(2**N)
    out = {}
    for s in (+1, -1):
        psi_x = np.exp(-1j * s * t * B) * amp
        out[s] = Hn @ psi_x   # back to Z basis; ordering consistent with kron
    return out

def reduced(psi, N, keep):
    T = psi.reshape([2]*N)
    rest = [i for i in range(N) if i not in keep]
    M = np.transpose(T, list(keep) + rest).reshape(2**len(keep), -1)
    return M @ M.conj().T

def chi(psis, N, keep):
    r = {s: reduced(psis[s], N, keep) for s in psis}
    return ent(0.5*(r[1]+r[-1])) - 0.5*(ent(r[1]) + ent(r[-1]))

def R_blocks(psis, N, thr=0.9):
    best = 0
    for m in (1, 2, 3, 4, 6):
        if N % m: continue
        cnt = sum(chi(psis, N, list(range(a, a+m))) >= thr for a in range(0, N, m))
        best = max(best, cnt)
    return best

def experiment(N, dratio, nsamp=150, thr=0.9):
    Rs = []
    for _ in range(nsamp):
        c = rng.normal(size=N)
        dpairs = {(k, (k+1) % N): dratio*rng.normal() for k in range(N)} if dratio > 0 and N > 2 else {}
        if dratio > 0 and N == 2:
            dpairs = {(0, 1): dratio*rng.normal()}
        t = rng.uniform(0.2, 2.0)
        psis = branch_states(N, c, dpairs, t)
        Rs.append(R_blocks(psis, N, thr))
    Rs = np.array(Rs)
    return dict(N=N, dratio=dratio, frac_R_ge_2=float((Rs >= 2).mean()), frac_R_ge_3=float((Rs >= 3).mean()), mean_R=float(Rs.mean()))

if __name__ == "__main__":
    out = []
    # N=2, lane's definition: both single-qubit fragments carry the record (R=2), star (d=0) and with the range-2 term at equal scale (d=1)
    for N, dr in [(2, 0.0), (2, 1.0), (12, 0.0), (12, 0.1), (12, 0.3), (12, 1.0)]:
        o = experiment(N, dr, nsamp=300 if N == 2 else 60)
        print(o, flush=True); out.append(o)
    json.dump(out, open("star_family_results.json", "w"), indent=1)
