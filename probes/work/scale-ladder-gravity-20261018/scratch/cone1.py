"""E1: the record cone. One seed record; each tick every empty site with >= 1 recorded neighbour (6-NN) forms a record
with probability p (independent odds). Front reach along axis / face / body after T ticks, averaged over runs."""
import numpy as np
rng = np.random.default_rng(1)
L = 121; c = L//2
def run(p, T):
    R = np.zeros((L, L, L), bool); R[c, c, c] = True
    for t in range(T):
        nb = (np.roll(R, 1, 0) | np.roll(R, -1, 0) | np.roll(R, 1, 1) | np.roll(R, -1, 1) | np.roll(R, 1, 2) | np.roll(R, -1, 2)) & ~R
        R |= nb & (rng.random(R.shape) < p)
    return R
def reach(R, d):
    d = np.array(d); n = 0
    while True:
        q = c + (n + 1)*d
        if np.any(q < 0) or np.any(q >= L) or not R[tuple(q)]: break
        n += 1
    return n*np.linalg.norm(d)
if __name__ == "__main__":
     for p in (1.0, 0.5, 0.2, 0.05):
        T = int(min(50, 45/max(p, 0.4))) if p >= 0.2 else 400
        rows = []
        for rep in range(2):
            R = run(p, T)
            # radial extent: farthest recorded site within a narrow cone around each direction
            X, Y, Z = np.nonzero(R); P = np.stack([X - c, Y - c, Z - c], 1).astype(float); r = np.linalg.norm(P, axis=1) + 1e-9
            ext = {}
            for nm, d in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1)}.items():
                u = np.array(d, float); u /= np.linalg.norm(u); cosang = P @ u / r
                sel = cosang > 0.995; ext[nm] = r[sel].max() if sel.any() else 0
            rows.append(ext)
        m = {k: np.mean([r_[k] for r_ in rows]) for k in rows[0]}
        print(f"p={p:5.2f} T={T:3d}: front reach axis {m['axis']:.1f}, face {m['face']:.1f}, body {m['body']:.1f};  speed (axis) {m['axis']/T:.3f} sites/tick;  roundness body/axis {m['body']/m['axis']:.3f}, face/axis {m['face']/m['axis']:.3f}")
