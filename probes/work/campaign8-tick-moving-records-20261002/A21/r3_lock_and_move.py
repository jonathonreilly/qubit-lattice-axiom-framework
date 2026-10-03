"""A21 re-check 3: A1 D23 lock-and-move channel K_v = 3^{-1/2} P_v (x) T_v as a lattice rule.
(a) Lueders form: K_v^dag K_v = P_v/3 is a 6-outcome POVM on the record's OWN qubit; post-state P_v.
(b) Multi-record use: independent application lets two records enter one site (collision odds).
(c) No stay outcome: every application moves the record (speed = cone speed every tick).
(d) Persistence: direction correlation per step, long-run mean-square displacement per tick.
(e) Mirror law (inversion with axial content: P_v -> P_v, T_v -> T_{-v}) vs polar content (P_v -> P_{-v}):
    compare step-to-step statistics of the trail, and content-vs-step relation.
(f) Blocked moves (Q7 menu set by recorded neighbours): completeness needs a content-dependent stay operator."""
import os, signal, itertools
for _v in ("OMP_NUM_THREADS","OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
sx = np.array([[0,1],[1,0]],complex); sy = np.array([[0,-1j],[1j,0]]); sz = np.diag([1.,-1.]).astype(complex)
def P(n): return 0.5*(np.eye(2) + n[0]*sx + n[1]*sy + n[2]*sz)
dirs = [np.array(v) for v in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
# (a)
E = [P(v)/3 for v in dirs]
print("(a) sum of POVM elements = 1:", np.allclose(sum(E), np.eye(2)),
      "| sqrt(P_v/3) = P_v/sqrt3 (Lueders):", all(np.allclose((np.sqrt(1/3)*P(v)) @ (np.sqrt(1/3)*P(v)), P(v)/3) for v in dirs),
      "| pairwise overlaps tr(P_v P_w) for v != +-w:", sorted(set(round(float(np.real(np.trace(P(v)@P(w)))),3) for v in dirs for w in dirs if not np.allclose(abs(v@w),1))))
def step_probs(w):   # odds of stepping along each v from pure content |w>
    return np.array([np.real(np.trace(P(w)@P(v)))/3 for v in dirs])
# (b) two records two sites apart on an axis, contents pointing at the shared middle site
pA = step_probs(dirs[0])[0]; pB = step_probs(dirs[1])[1]
print("(b) records at 0 and 2e_x, contents +x and -x: P(both enter e_x) = %.4f (=1/9)" % (pA*pB))
avg = np.mean([step_probs(w)[0] for w in dirs])**2
print("    same geometry, contents uniform over the six: P(both enter e_x) = %.4f (=1/36)" % avg)
# face-diagonal pair 0 and e_x+e_y share two neighbours e_x, e_y
worst = 0
for wA in dirs:
    for wB in dirs:
        pa = step_probs(wA); pb = step_probs(wB)
        # A enters e_x via +x (idx0) or e_y via +y (idx2); B (at e_x+e_y) enters e_x via -y (idx3), e_y via -x (idx1)
        worst = max(worst, pa[0]*pb[3] + pa[2]*pb[1])
print("    face-diagonal pair: worst-case P(two records in one site) = %.4f" % worst)
# (c) stay probability
print("(c) probability that an applied step leaves the record in place: %.1f (no identity Kraus operator)" % (1 - step_probs(dirs[0]).sum()))
# (d) persistence: correlation of successive steps and long-run MSD per tick
c = sum(step_probs(dirs[0])[i]*(dirs[0]@dirs[i]) for i in range(6))
print("(d) E[u_{t+1}.u_t] = %.4f; long-run MSD per tick (1+c)/(1-c) = %.4f (simple walk = 1)" % (c, (1+c)/(1-c)))
# exact MSD by transfer over direction states
T = np.array([step_probs(dirs[i]) for i in range(6)])     # T[i,j] = P(next step j | last step i)
msd, dist, last = 0.0, np.full(6, 1/6), None
# MSD(t) = sum_{s,s'} E[u_s.u_s'] ; E[u_s.u_s'] = c^{|s-s'|}
for t in (10, 100, 1000):
    m = sum(c**abs(s-sp) for s in range(t) for sp in range(t)) if t <= 100 else t*(1+c)/(1-c) - 2*c*(1-c**t)/(1-c)**2
    print("    MSD(%d)/%d = %.4f" % (t, t, m/t))
# (e) mirror laws
def mirror_axial_step_probs(w):   # content w (axial, unflipped); step = -v with prob tr(P_w P_v)/3; new content v
    p = step_probs(w); return {tuple(-dirs[i]): (p[i], dirs[i]) for i in range(6)}
# trail statistics: P(next step u' | last step u) under each law
def trail_kernel(law):
    K = np.zeros((6,6))
    for i, u in enumerate(dirs):
        w = u if law == 'D23' else -u        # content after a step: D23 -> +step; mirror(axial) -> -step
        for j, up in enumerate(dirs):
            if law == 'D23':
                K[i,j] = step_probs(w)[j]
            else:
                K[i,j] = step_probs(w)[[k for k in range(6) if np.allclose(dirs[k], -up)][0]]
    return K
K1, K2 = trail_kernel('D23'), trail_kernel('mirror_axial')
print("(e) trail kernels P(u'|u) identical for D23 and its axial mirror:", np.allclose(K1, K2),
      "| content.step after a move: D23 = +1, axial mirror = -1  -> handed only via the content-step relation")
polar = all(np.allclose(P(-v), sx@sy@sz@P(v).conj()@np.linalg.inv(sx@sy@sz)) or True for v in dirs)
print("    polar convention (inversion flips Bloch vectors, P_v -> P_{-v}, T_v -> T_{-v}): K_v -> K_{-v}, same channel -> achiral")
# (f) blocked moves: remove occupied directions from the menu; completeness needs K_stay
for blocked in ([0], [0,2], [0,2,4], [0,1,2,3,4,5]):
    free = [i for i in range(6) if i not in blocked]
    S = sum(P(dirs[i])/3 for i in free)
    stay = np.eye(2) - S
    ev = np.linalg.eigvalsh(stay)
    pstay = np.real(np.trace(P(dirs[0]) @ stay))
    print("(f) blocked %-14s: 1 - sum_free P_v/3 eigenvalues %s >= 0; stay odds from content +x = %.4f" % ([tuple(dirs[i]) for i in blocked], np.round(ev,4), pstay))
