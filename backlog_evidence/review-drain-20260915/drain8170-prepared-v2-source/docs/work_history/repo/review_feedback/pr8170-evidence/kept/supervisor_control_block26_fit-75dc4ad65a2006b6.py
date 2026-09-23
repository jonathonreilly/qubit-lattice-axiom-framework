# Summary table for block 26: magnetization runs (sphere), linear model against its prediction, six-axis side-by-side.
import numpy as np, re, glob, os
S = os.environ.get("B26_DATA", os.path.dirname(os.path.abspath(__file__))) + "/"
def A(x): return 1 / np.tanh(x) - 1 / x
c0 = 3 * np.sqrt(3) / (4 * np.pi)
def load_m(fn):
    """m_z = projection of the plane-averaged record on the initial direction (the memory); |m| only if m_z is absent."""
    t, m = [], []
    for l in open(fn):
        mm = re.match(r"\s*t=\s*(\d+)\s+\|m\|=([0-9.]+)(?:\s+m_z=(-?[0-9.]+))?", l)
        if mm: t.append(int(mm.group(1))); m.append(float(mm.group(3) if mm.group(3) is not None else mm.group(2)))
    return np.array(t), np.array(m)
def fit(t, m, a, b):
    sel = (t >= a) & (t <= b)
    return -np.polyfit(np.log(t[sel]), np.log(m[sel]), 1)[0]
print("sphere formation law, aligned start, periodic L x L plane, m = projection of the plane-averaged record on the initial direction (|m| for runs without it)")
print(f"{'beta':>5} {'L':>4} {'T':>6} {'m(500)':>7} {'m(5000)':>8} {'m(T)':>7} {'exp[500,5000]':>14} {'exp[5000,T]':>12} {'exp[500,T]':>11} {'gamma_lin':>10}")
for fn in sorted(glob.glob(S + "sim_b*_L*_T*.txt")) + sorted(glob.glob(S + "ref_sphere_b*_L*.txt")):
    mm = re.search(r"b(\d+)_L(\d+)", fn); beta, L = int(mm.group(1)), int(mm.group(2))
    t, m = load_m(fn)
    if len(t) < 10: continue
    T = t[-1]
    def at(tt): return m[np.argmin(abs(t - tt))]
    print(f"{beta:5d} {L:4d} {T:6d} {at(500):7.4f} {at(5000):8.4f} {m[-1]:7.4f} {fit(t,m,500,5000):14.4f} {fit(t,m,5000,T):12.4f} {fit(t,m,500,T):11.4f} {c0*A(3*beta)/(3*beta):10.5f}  {os.path.basename(fn)}")
print("\nlinear model (theta = average of predecessors + Gaussian noise of variance A(3 beta)/(3 beta) per component), v_t = mean |theta|^2 / 2")
for fn in sorted(glob.glob(S + "ref_linear_b*_L*.txt")):
    sim, pred = {}, {}
    for l in open(fn):
        a = re.match(r"\s*t=\s*(\d+)\s+v_t\(sim\)=([0-9.]+)", l)
        if a: sim[int(a.group(1))] = float(a.group(2))
        b = re.match(r"\s*prediction v_(\d+) = .* = ([0-9.]+)", l)
        if b: pred[int(b.group(1))] = float(b.group(2))
    for tt in sorted(sim)[::5]:
        print(f"  t={tt:6d}  v_sim={sim[tt]:.5f}  v_pred={pred.get(tt, float('nan')):.5f}  exp(-v_sim)={np.exp(-sim[tt]):.4f}   {os.path.basename(fn)}")
