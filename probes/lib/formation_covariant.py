"""formation_covariant.py w0 w1 beta L T T0 seed [start]      (3+1: levels of records on the torus (Z/L)^3)

Block 93: in the 3+1 reading the pasts covariant under the cube's 24 rotations carry one weight w0 on the record below and one weight w1
on its six neighbours. The record at (t+1, x) forms on the sphere with density proportional to exp(beta s'.h), h = w0 s_t(x) +
w1 sum_j (s_t(x + e_j) + s_t(x - e_j)) (block 19's rule; exact sampling by inverting the cosine's distribution).
w1 = 0: the record below alone (no common direction should form); w0 = 0: the six neighbours alone (two classes, x1+x2+x3+t even or odd,
that never interact, each settling into the static sphere law with coupling beta w1); both > 0: block 90's bilayer.
start: 'aligned' (default: every record along z) or 'orthogonal' (even sites along z, odd along x).
Prints a memory table (level, |m|, |m_even|, |m_odd|, cos between the even and odd means) and a SUMMARY with the plateau |m| and the plateau
cosine over the second half of the run."""
import numpy as np, sys, time
w0 = float(sys.argv[1]); w1 = float(sys.argv[2]); beta = float(sys.argv[3]); L = int(sys.argv[4]); T = int(sys.argv[5]); T0 = int(sys.argv[6]); seed = int(sys.argv[7])
start = sys.argv[8] if len(sys.argv) > 8 else "aligned"
rng = np.random.default_rng(seed); N = L ** 3; par = np.indices((L, L, L)).sum(0) % 2
s = np.zeros((L, L, L, 3)); s[..., 2] = 1.0
if start == "orthogonal":
    s[par == 1] = np.array([1.0, 0.0, 0.0])
def sample(V):
    kap = np.linalg.norm(V, axis=1); kap = np.where(kap < 1e-12, 1e-12, kap); uu = V / kap[:, None]
    U = rng.random(len(V)); w = np.clip(1.0 + np.log(U + (1.0 - U) * np.exp(-2.0 * kap)) / kap, -1.0, 1.0); ph = 2 * np.pi * rng.random(len(V))
    a = np.where((np.abs(uu[:, 0]) < 0.9)[:, None], np.array([1.0, 0, 0]), np.array([0, 1.0, 0]))
    b1 = a - (a * uu).sum(1)[:, None] * uu; b1 /= np.linalg.norm(b1, axis=1)[:, None]; b2 = np.cross(uu, b1); r = np.sqrt(np.clip(1 - w * w, 0, 1))
    return w[:, None] * uu + r[:, None] * (np.cos(ph)[:, None] * b1 + np.sin(ph)[:, None] * b2)
marks = sorted(set(int(round(x)) for x in np.geomspace(1, T, 20))); tail_m = []; tail_c = []; t0 = time.time()
print(f"w0={w0} w1={w1} beta={beta} L={L} T={T} T0={T0} seed={seed} start={start}")
print("memory table: level, |m|, |m_even|, |m_odd|, cos(m_even, m_odd)")
for t in range(1, T + 1):
    h = w0 * s
    for ax in range(3):
        h = h + w1 * (np.roll(s, 1, axis=ax) + np.roll(s, -1, axis=ax))
    s = sample(beta * h.reshape(-1, 3)).reshape(L, L, L, 3)
    m = s.reshape(-1, 3).mean(0); me = s[par == 0].mean(0); mo = s[par == 1].mean(0)
    c = float(me @ mo / max(np.linalg.norm(me) * np.linalg.norm(mo), 1e-12))
    if t in marks: print(f"   {t:6d}  {np.linalg.norm(m):.4f}  {np.linalg.norm(me):.4f}  {np.linalg.norm(mo):.4f}  {c:+.4f}", flush=True)
    if t > T0: tail_m.append(np.linalg.norm(m)); tail_c.append(c)
print(f"SUMMARY: w0={w0} w1={w1} beta={beta} L={L} T={T} start={start} plateau_|m|={np.mean(tail_m):.4f} plateau_cos_even_odd={np.mean(tail_c):+.4f} seconds={time.time()-t0:.0f}")
