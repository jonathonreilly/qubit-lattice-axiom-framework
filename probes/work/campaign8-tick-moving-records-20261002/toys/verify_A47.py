"""Coordinator check of A47's spin-wave competitors, written from scratch (no A43/A44 library).

Dual-frame rule H' = sum_NN s.s + j sum_fd s.s (Pauli units, s = 2S). Linear spin waves for
single-Q collinear states on the cubic lattice:
  A_k = S sum_d J_d [-c_d + (1+c_d)/2 cos k.d],  B_k = S sum_d J_d (1-c_d)/2 cos k.d,
  E/N = (S^2/2) sum_d J_d c_d + (1/2N) sum_k (w_k - A_k),  w_k = sqrt(A_k^2 - B_k^2),
with c_d = cos(Q.d) = +-1, J_NN = 4, J_fd = 4j, S = 1/2. Energy is reported per NN bond (3 per site).
Also checks A47's quoted significances from its table (pure arithmetic)."""
import itertools, math
import numpy as np

NN = [d for d in itertools.product((-1, 0, 1), repeat=3) if sum(map(abs, d)) == 1]
FD = [d for d in itertools.product((-1, 0, 1), repeat=3) if sum(map(abs, d)) == 2]
assert len(NN) == 6 and len(FD) == 12

def lswt(j, Q, L):
    k1 = 2 * np.pi * (np.arange(L) + 0.5) / L          # shifted grid avoids the k=0 Goldstone point
    kx, ky, kz = np.meshgrid(k1, k1, k1, indexing="ij")
    S = 0.5
    A = np.zeros_like(kx); B = np.zeros_like(kx); Ecl = 0.0
    for dset, J in ((NN, 4.0), (FD, 4.0 * j)):
        for d in dset:
            c = round(math.cos(np.dot(Q, d)))
            ck = np.cos(kx * d[0] + ky * d[1] + kz * d[2])
            A += S * J * (-c + (1 + c) / 2 * ck)
            B += S * J * (1 - c) / 2 * ck
            Ecl += S * S / 2 * J * c
    disc = A * A - B * B
    if disc.min() < -1e-9:
        return None
    w = np.sqrt(np.clip(disc, 0, None))
    return (Ecl + 0.5 * np.mean(w - A)) / 3.0

neel, col = np.array([np.pi] * 3), np.array([np.pi, np.pi, 0.0])
quoted = {0.20: (-0.9072, None), 0.25: (-0.8912, -0.7632), 0.30: (None, -0.7565),
          0.35: (None, -0.7752), 0.40: (None, -0.8018)}
ok = True
print(f"j=0 Neel (sanity, literature LSWT ~ -0.895 J/site -> -1.193 per bond): {lswt(0.0, neel, 40):.4f}")
for j, (qn, qc) in quoted.items():
    for name, Q, q in (("Neel", neel, qn), ("collinear", col, qc)):
        e40 = lswt(j, Q, 40)
        e8 = lswt(j, Q, 8)
        tag = "unstable" if e40 is None else f"{e40:.4f} (8^3 grid {e8:.4f})"
        if q is None:
            good = e40 is None
        else:
            good = e40 is not None and abs(e40 - q) < 2e-3
        ok &= good
        print(f"j={j:.2f} {name:9s} mine {tag:28s} A47 {('unstable' if q is None else q)!s:9s} {'OK' if good else 'MISMATCH'}")

# A47 table arithmetic: margin / combined error
def sig(a, ea, b, eb):
    return (b - a), (b - a) / math.hypot(ea, eb)
for label, a, ea, b, eb, qs in (("6^3 j=.30 margin", -0.77016, 28e-5, -0.76920, 40e-5, 2.0),
                                ("8^3 j=.30 margin", -0.76690, 29e-5, -0.76726, 36e-5, -0.8),
                                ("6^3 j=.30 gain", -0.77016, 28e-5, -0.76947, 26e-5, 1.8)):
    m, s = sig(a, ea, b, eb)
    good = abs(s - qs) < 0.15
    ok &= good
    print(f"{label}: {m:+.5f} = {s:+.2f} sigma (A47 {qs:+.1f}) {'OK' if good else 'MISMATCH'}")
print("TOTAL:", "PASS" if ok else "FAIL")
