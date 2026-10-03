"""Sampler check for magnon_toy: P(no record in the first T ticks), deterministic vs Monte Carlo."""
import os, sys, time
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "magnon_toy.py")).read()
exec(src.split("# exact checks")[0])
import numpy as np
rng.bit_generator.state = np.random.default_rng(5).bit_generator.state
x0 = N // 2
st = np.zeros(N, int)
U = change(st)
v = np.exp(1j * 0.3 * np.arange(N) - (np.arange(N) - x0) ** 2 / (2 * 3.0 ** 2)); psi0 = v / np.linalg.norm(v)

def k0_pass(vec, r):
    new = vec.copy()
    for x in range(r, N, 3):
        _, s1 = MATS[("A", UNL, UNL)]
        idx = [(x - 1) % N, x, (x + 1) % N]
        new[idx] = s1 @ new[idx]
    return new

T_list = (20, 60, 200)
det = {}
w = psi0.astype(complex).copy()
for t in range(max(T_list)):
    w = U @ w
    for r in range(3):
        w = k0_pass(w, r)
    if t + 1 in T_list:
        det[t + 1] = np.vdot(w, w).real
uni = np.ones(N) / np.sqrt(N)
print("deterministic P(no record in first T ticks):", {T: round(p, 5) for T, p in det.items()},
      f"; dark weight = {abs(np.vdot(uni, psi0))**2:.5f}")

NT = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
t0 = time.time()
first = []
for _ in range(NT):
    psi = psi0.astype(complex).copy()
    tf = None
    for t in range(max(T_list)):
        psi = U @ psi
        for r in range(3):
            xs = list(range(r, N, 3))
            a_list, p_list = [], []
            for x in xs:
                sF, _ = MATS[("A", UNL, UNL)]
                a = sF @ psi[[(x - 1) % N, x, (x + 1) % N]]
                a_list.append(a); p_list.append(np.vdot(a, a).real)
            cum = np.cumsum(p_list)
            if rng.uniform() < cum[-1]:
                tf = t
                break
            psi = k0_pass(psi, r); psi /= np.linalg.norm(psi)
        if tf is not None:
            break
    first.append(tf if tf is not None else 10 ** 9)
first = np.array(first)
for T in T_list:
    p = np.mean(first >= T); sd = np.sqrt(det[T] * (1 - det[T]) / NT)
    print(f"T={T:3d}: MC {p:.4f} vs deterministic {det[T]:.4f} (z = {(p - det[T]) / sd:+.2f})")
print(f"MC time {time.time() - t0:.1f} s")
