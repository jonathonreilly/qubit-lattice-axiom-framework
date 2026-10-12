"""R15-4: lag-free variants. Constraint algebra (proved): int_0^inf (1 - G_t(x0)) dt = G'(x0) - 1/x0, so the first-order
response to a slow comoving-energy release in a sector of rate x0 vanishes iff G'(x0) = 1/x0. Scan exact-constraint designs
(M registers = M constraints): G(3)=G(4)=1 plus optionally G'(4)=1/4, G'(3)=1/3. Report positivity of the radiation step
response H(t) (>=0 needed, reheating), T_K, G(0.75), and int(1-G_t(4))dt."""
import numpy as np, itertools
def solve(betas, cons):
    b = np.array(betas, float); A = []; r = []
    for (kind, x0) in cons:
        if kind == 'G': A.append(x0/(b-x0)); r.append(1.0)
        else: A.append(b/(b-x0)**2); r.append(1.0/x0)
    return b, np.linalg.solve(np.array(A), np.array(r))
def stats(b, k):
    t = np.linspace(0, 25, 50001)
    H = np.array([np.sum(k*(1-np.exp(-(b-4)*tt))/(b-4)) for tt in t])
    G = lambda x: np.sum(k*x/(b-x))
    lag = np.sum(4*k/(b-4)**2)
    return H.min(), np.max(np.abs(1-4*H)), G(0.75), G(0.3), lag
if __name__ == '__main__':
    for cons, nreg in (([('G',3),('G',4)],2), ([('G',3),('G',4),('dG',4)],3), ([('G',3),('G',4),('dG',4),('dG',3)],4)):
        print('constraints', cons)
        best = []
        grid = [5,6,7,8,10,12,14,16,20,24,30]
        for bs in itertools.combinations(grid, nreg):
            try: b, k = solve(bs, cons)
            except np.linalg.LinAlgError: continue
            Hmin, TK, g75, g3, lag = stats(b, k)
            best.append((TK if Hmin >= -1e-12 else 1e9, bs, Hmin, TK, g75, g3, lag, k))
        best.sort(key=lambda z: z[0])
        for row in best[:4]:
            print(f'   beta={row[1]}: min H={row[2]:+.2e} (positive={row[2]>=-1e-12}), T_K={row[3]:.3f}, G(0.75)={row[4]:.3f}, G(0.3)={row[5]:.3f}, lag int(1-G_t)={row[6]:+.3e}, k={np.round(row[7],3)}')
