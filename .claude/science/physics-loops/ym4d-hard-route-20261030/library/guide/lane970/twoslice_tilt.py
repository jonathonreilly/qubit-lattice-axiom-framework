# Row 970 (gap-direction2-max), GUIDE only. Two-slice law J_(b,phi) of row 968 at the layered pi-flux tilt u_xy.
# Model: SU(2) Wilson, temporal gauge, open time, slices 0..2T-1, half weight on the plaquettes of the two end
# slices. x = slice T-1, w = slice T. The time-like layer between x and w has coupling b (beta elsewhere).
# Linear tilt kx <u, x> + kw <u, w> with u = u_xy (u_y = (-1)^x, u_x = u_z = 1). Links are unit quaternions.
# Heat bath (Creutz sampler), checkerboard by direction and 4D site parity. Hot start.
# Observable: O_s^a = sum_n (-1)^(x+y) [E^a_x(n) - E^a_y(n)], E_l = Im(U_l u_l^-1), on s = x and s = w (row 950's mode,
# momentum (pi, pi, 0), polarisation (1, -1, 0)); lam_w = E (O_w^a)^2/(2 L^3), lam_sum = E (O_x^a + O_w^a)^2/(2 L^3).
import numpy as np, sys, time, json, resource
L, T, beta, b, kx, kw, ntherm, nmeas, seed = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9])
rng = np.random.default_rng(seed); Nt = 2*T; sx, sw = T-1, T
def qmul(p, q):
    r = np.empty_like(p)
    r[..., 0] = p[..., 0]*q[..., 0] - p[..., 1]*q[..., 1] - p[..., 2]*q[..., 2] - p[..., 3]*q[..., 3]
    r[..., 1] = p[..., 0]*q[..., 1] + q[..., 0]*p[..., 1] - (p[..., 2]*q[..., 3] - p[..., 3]*q[..., 2])
    r[..., 2] = p[..., 0]*q[..., 2] + q[..., 0]*p[..., 2] - (p[..., 3]*q[..., 1] - p[..., 1]*q[..., 3])
    r[..., 3] = p[..., 0]*q[..., 3] + q[..., 0]*p[..., 3] - (p[..., 1]*q[..., 2] - p[..., 2]*q[..., 1])
    return r
def conj(p):
    r = p.copy(); r[..., 1:] *= -1; return r
U = rng.normal(size=(Nt, L, L, L, 3, 4)); U /= np.linalg.norm(U, axis=-1, keepdims=True)
tt, xx, yy, zz = np.meshgrid(np.arange(Nt), np.arange(L), np.arange(L), np.arange(L), indexing='ij')
par = (tt + xx + yy + zz) % 2
usign = np.ones((L, L, L, 3)); usign[:, :, :, 1] = ((-1.0)**np.arange(L))[:, None, None]
wsp = np.full(Nt, beta); wsp[0] = beta/2; wsp[-1] = beta/2          # spatial plaquette weight per slice
ct = np.full(Nt-1, beta); ct[sx] = b                                 # time-like coupling of layer (tau, tau+1)
stag = ((-1.0)**(np.arange(L)[:, None, None] + np.arange(L)[None, :, None]))*np.ones((L, L, L))
def field(mu):
    A = np.zeros((Nt, L, L, L, 4))
    Um = U[..., mu, :]
    for nu in range(3):
        if nu == mu: continue
        Un = U[..., nu, :]
        f = qmul(qmul(np.roll(Un, -1, axis=1+mu), conj(np.roll(Um, -1, axis=1+nu))), conj(Un))
        Unm = np.roll(Un, 1, axis=1+nu)
        bk = qmul(qmul(conj(np.roll(Unm, -1, axis=1+mu)), conj(np.roll(Um, 1, axis=1+nu))), Unm)
        A += f + bk
    S = conj(A)*wsp[:, None, None, None, None]
    S[1:] += ct[:, None, None, None, None]*Um[:-1]
    S[:-1] += ct[:, None, None, None, None]*Um[1:]
    S[sx, ..., 0] += kx*usign[..., mu]; S[sw, ..., 0] += kw*usign[..., mu]
    return S
def sample_a0(k):
    n = k.size; a0 = np.empty(n); todo = np.arange(n)
    while todo.size:
        kk = k[todo]; em = np.exp(-2*kk)
        a = 1 + np.log(em + rng.random(todo.size)*(1 - em))/kk
        acc = rng.random(todo.size)**2 <= 1 - a*a
        a0[todo[acc]] = a[acc]; todo = todo[~acc]
    return a0
def sweep():
    for mu in range(3):
        for p in (0, 1):
            S = field(mu)[par == p]
            k = np.linalg.norm(S, axis=-1); k = np.maximum(k, 1e-6)
            a0 = sample_a0(k); rad = np.sqrt(np.maximum(0.0, 1 - a0*a0))
            v = rng.normal(size=(k.size, 3)); v /= np.linalg.norm(v, axis=-1, keepdims=True)
            V = np.concatenate([a0[:, None], rad[:, None]*v], axis=1)
            new = qmul(V, S/k[:, None])
            Um = U[..., mu, :]; Um[par == p] = new
def measure():
    out = []
    for s in (sx, sw):
        Ex = U[s, ..., 0, 1:]; Ey = U[s, ..., 1, 1:]*usign[..., 1][..., None]
        out.append(np.einsum('xyz,xyza->a', stag, Ex - Ey))
    return out
def plaq(s):
    P = 0.0
    for mu in range(3):
        for nu in range(mu+1, 3):
            Um, Un = U[s, ..., mu, :], U[s, ..., nu, :]
            P += qmul(qmul(Um, np.roll(Un, -1, axis=mu)), qmul(conj(np.roll(Um, -1, axis=nu)), conj(Un)))[..., 0].mean()
    return P/3
t0 = time.time()
for i in range(ntherm): sweep()
Ox = np.empty((nmeas, 3)); Ow = np.empty((nmeas, 3)); pl = []; ov = []; lv = []
for i in range(nmeas):
    sweep(); ox, ow = measure(); Ox[i] = ox; Ow[i] = ow
    if i % 50 == 0:
        pl.append(plaq(T+2)); ov.append((U[sx]*U[sw]).sum(-1).mean()); lv.append((U[sw]**2).mean())
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 2e9: sys.exit("RSS above 2 GB")
nrm = 2*L**3
def stat(v):
    blk = v.reshape(10, -1).mean(axis=1); return float(v.mean()), float(blk.std(ddof=1)/np.sqrt(10))
m = (nmeas//10)*10
lw = stat((Ow[:m]**2).mean(axis=1)/nrm); lx = stat((Ox[:m]**2).mean(axis=1)/nrm); ls = stat(((Ox[:m]+Ow[:m])**2).mean(axis=1)/nrm)
res = dict(L=L, T=T, beta=beta, b=b, kx=kx, kw=kw, ntherm=ntherm, nmeas=nmeas, seed=seed, lam_w=lw, lam_x=lx, lam_sum=ls,
           mean_Ow=[float(t) for t in Ow.mean(axis=0)], plaq_bulk=float(np.mean(pl)), tau_xw=float(np.mean(ov)),
           link_comp_var_w=float(np.mean(lv)), sec=round(time.time()-t0, 1), ms_per_sweep=round(1000*(time.time()-t0)/(ntherm+nmeas), 2))
print(json.dumps(res)); sys.stdout.flush()
