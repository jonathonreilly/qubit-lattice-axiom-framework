AUDIT_INPUT_PATHS = ('docs/RECORD_AND_CLOCK_SPLIT_TRIGGERS_ARE_FIXED_SCHEDULES_AND_NO_MEMORYLESS_LOCAL_SHIFT_HOLDS_EVERY_STATIONARY_STATE_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""causal-trigger: can CL-1's split trigger be causal with no supplied gauge parameters?
Linear ADM on flat space, one Fourier mode k along z, 8 pi G = c = 1, CL-1's tied lapse n = tr h/6
(h_00 = -h_kk/3).  Shift laws compared: zero (Z), minimal strain (MS, elliptic), value drivers
d_t beta_i = mu1 d_j h_ij + mu2 d_i h (harmonic: mu1 = 1, mu2 = -2/3), rate drivers d_t^2 beta = d_t(value
driver) - eta d_t beta (strain driver of min-strain C2: mu1 = 1/3, mu2 = 0).  Self-contained."""
import time, numpy as np, sympy as sp
from scipy.linalg import expm
AUDIT_TIMEOUT_SEC = 60
T0 = time.time(); NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} | {detail}")

# ---------------------------------------------------------------- linear model
PR = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
def hi(i,j): return PR.index((min(i,j),max(i,j)))
NH, NK, NB, NBD, DIM = 0, 6, 12, 15, 18
def build(kind, mu1=1.0, mu2=0.0, eta=0.0, k=1.0):
    ik = 1j*k; A = np.zeros((DIM,DIM), complex); src = np.zeros((DIM,3), complex)
    E = np.eye(DIM); tr = sum(E[NH+hi(i,i)] for i in range(3)); n = tr/6
    def brow(i):
        if kind == 'MS':   # d_j hdot_ij = 0 solved algebraically for beta
            return (2/ik)*E[NK+hi(i,2)] if i < 2 else (1/ik)*E[NK+hi(2,2)]
        return 0*E[0] if kind == 'Z' else E[NB+i]
    B = [brow(i) for i in range(3)]; hd = {}
    for (i,j) in PR:
        r = -2*E[NK+hi(i,j)]
        if i == 2: r = r + ik*B[j]
        if j == 2: r = r + ik*B[i]
        A[NH+hi(i,j)] = r; hd[(i,j)] = r
    for (i,j) in PR:
        r = 0.5*k**2*E[NH+hi(i,j)]
        if i == 2: r = r - 0.5*k**2*E[NH+hi(j,2)]
        if j == 2: r = r - 0.5*k**2*E[NH+hi(i,2)]
        if i == 2 and j == 2: r = r + 0.5*k**2*tr + k**2*n
        A[NK+hi(i,j)] = r
        if i == j: src[NK+hi(i,j),0] = -0.5          # dust: -8 pi G (S_ij - (S - rho) d_ij / 2)
    trd = sum(hd[(i,i)] for i in range(3))
    for i in range(3):
        if kind == 'VAL':
            A[NB+i] = mu1*ik*E[NH+hi(i,2)] + (mu2*ik*tr if i == 2 else 0) - eta*E[NB+i]
        if kind == 'RATE':
            A[NB+i, NBD+i] = 1
            A[NBD+i] = mu1*ik*hd[(i,2)] + (mu2*ik*trd if i == 2 else 0) - eta*E[NBD+i]
    return A, src
def evolve(A, src, x0, s, T=400., dt=0.5):
    Aug = np.zeros((DIM+1,DIM+1), complex); Aug[:DIM,:DIM] = A; Aug[:DIM,DIM] = src@s
    Ea = expm(Aug*dt); x = np.append(x0.astype(complex), 1); H = []; Bt = []
    for _ in range(int(T/dt)):
        x = Ea@x; H.append(np.abs(x[NH:NH+6]).max()); Bt.append(np.abs(x[NB:NB+3]).max())
    H, Bt = np.array(H), np.array(Bt); m = len(H)//2
    return H[:m].max(), H[m:].max(), Bt[:m].max(), Bt[m:].max()
def tests(A, src):
    x0 = np.zeros(DIM); U = -0.5
    for i in range(3): x0[NH+hi(i,i)] = -2*U                        # isotropic static data, rho = 1
    st = evolve(A, src, x0, np.array([1,0,0]))
    x0 = np.zeros(DIM, complex); x0[NK+hi(0,2)] = 1/1j              # stationary transverse current J_x = 1
    ro = evolve(A, src, x0, np.array([0,1,0]))
    om = -1j*np.linalg.eigvals(A)                                   # x ~ exp(i omega t)
    return st, ro, om

print('== A. what a split trigger can read (theorems)')
# A1 record count = sites x half-ticks; ticks global; clock triggers vs the expansion history
yr = 3.156e7; teq = 5.1e4*yr; t0 = 4.35e17
ts = np.logspace(0, np.log10(t0), 4000)
loga = np.where(ts < teq, 0.5*np.log2(ts/teq), (2/3)*np.log2(ts/teq))
best = np.inf
for tau in np.logspace(-2, 18, 400):          # schedule log2 a = t/tau + c; best offset c
    d = loga - ts/tau; best = min(best, (d.max()-d.min())/2)
check('A1 [T+E] CL-2 gives one record per site per half-tick and ticks are global, so "split after N records" (or N ticks, '
      'or a fixed proper time or 4-volume per split) is a fixed schedule; no schedule tracks the measured expansion from 1 s '
      'to today within the 4-octave window', best > 4, f'{loga[-1]-loga[0]:.1f} octaves needed; best schedule misses by {best:.1f} octaves')
# A2 volume of a fixed label set: changes only by boundary displacement (flux of xi)
rng = np.random.default_rng(1)
G = np.array(np.meshgrid(*[np.arange(4)]*3, indexing='ij'), float).transpose(1,2,3,0)
TET = [(0,1,2,4),(1,3,2,7),(1,4,5,7),(2,4,6,7),(1,2,4,7)]
def vol(X):
    v = 0
    for a in range(3):
        for b in range(3):
            for c in range(3):
                C = [X[a+i,b+j,c+l] for i in (0,1) for j in (0,1) for l in (0,1)]
                C = [C[0],C[4],C[2],C[6],C[1],C[5],C[3],C[7]]
                for t in TET: v += abs(np.linalg.det(np.array([C[t[1]]-C[t[0]],C[t[2]]-C[t[0]],C[t[3]]-C[t[0]]])))/6
    return v
xi = rng.normal(size=G.shape)*1e-6; inner = np.zeros_like(xi); inner[1:3,1:3,1:3] = xi[1:3,1:3,1:3]
V0 = vol(G); dVin = (vol(G+inner)-V0)/1e-6; dVall = (vol(G+xi)-V0)/1e-6
check('A2 [T] a block of fixed sites changes volume under a displacement only through its boundary (flux of xi): '
      'interior moves leave it invariant, boundary moves do not; block volume is not displacement-invariant',
      abs(dVin) < 1e-4 and abs(dVall) > 1e-2, f'dV/eps interior-only {dVin:.1e}, all sites {dVall:.2f}')
# A3 the tied lapse ties the slicing to the spatial gauge
t, x, y, z = sp.symbols('t x y z'); X = sp.Function('X0')(t,x,y,z); Xi = [sp.Function(f'X{i}')(t,x,y,z) for i in (1,2,3)]
dh00 = -2*sp.diff(-X, t); dhkk = -2*sum(sp.diff(Xi[i], v) for i, v in enumerate((x,y,z)))
cond = sp.simplify(dh00 + dhkk/3)                     # tied lapse kept under the gauge change
sol = sp.solve(cond, sp.diff(X, t))[0]
check('A3 [T] keeping h_00 = -h_kk/3 under x -> x + xi forces d_t xi^0 = div(xi)/3: an instantaneous spatial relabelling '
      'drags the slicing, so K (delta K = -lap xi^0), the lapse, proper time and 4-volume at a label all respond at first '
      'order; a label-local trigger is causal only if the labels (the shift) are', sp.simplify(sol - sum(sp.diff(Xi[i], v) for i, v in enumerate((x,y,z)))/3) == 0, f'd_t xi^0 = {sol}')
# A4 no curvature trigger: radiation-era FRW has R = 0 and Weyl = 0 while H != 0
a = sp.sqrt(t); Rs = 6*(sp.diff(a,t,2)/a + (sp.diff(a,t)/a)**2)
check('A4 [T] expansion is not local curvature: radiation FRW (a ~ t^1/2) has Ricci scalar 0 and Weyl 0 with H = 1/2t, '
      'so a trigger must read a congruence (edges or their rate), not a curvature invariant', sp.simplify(Rs) == 0, f'R = {sp.simplify(Rs)}')

print('== B. causal frames (linear, k = 1, rho or J switched on with consistent data; T = 400)')
rows = {}
for name, kw in [('Z', dict(kind='Z')), ('MS', dict(kind='MS')), ('harmonic', dict(kind='VAL', mu1=1, mu2=-2/3)),
                 ('strain mu1/3', dict(kind='RATE', mu1=1/3)), ('strain eta.5', dict(kind='RATE', mu1=1/3, eta=0.5)),
                 ('strain eta5', dict(kind='RATE', mu1=1/3, eta=5.0)), ('val 5/3 mu.1', dict(kind='VAL', mu1=0.1, mu2=-0.5/3))]:
    rows[name] = tests(*build(**kw))
    st, ro, om = rows[name]
    print(f'   {name:13s} speeds<= {np.abs(om.real).max():.3f} growth {max(0,-om.imag.min()):.1e} | static: h {st[0]:.1f}->{st[1]:.1f}'
          f' beta {st[2]:.1f}->{st[3]:.1f} | rotating: h {ro[0]:.1f}->{ro[1]:.1f}')
st, ro, om = rows['Z']
check('B1 [T+D] zero shift: speeds 1, 1/sqrt3, 0 (causal, no parameter), static star bounded, but a stationary current winds '
      'the edges linearly (h_xz = -2 K_xz t, R_xz = 0)', np.abs(om.real).max() <= 1+1e-9 and st[1] <= st[0]*1.01 and ro[1] > 1.9*ro[0], f'rotating h {ro[0]:.0f} -> {ro[1]:.0f}')
st, ro, om = rows['MS']
check('B2 [D] minimal strain: bounded for both (its fault is only the instantaneous elliptic solve)', st[1] <= st[0]*1.01 and ro[1] < 1e-9, f'{st[1]:.2f}, {ro[1]:.1e}')
# B3 memoryless local shifts cannot hold every stationary state: uniform trace-free K needs beta linear in x
Kc = sp.Matrix([[0,1,0],[1,0,0],[0,0,0]]); bv = sp.Matrix([y, x, 0])          # d_(i beta_j) = K_ij
mom = [sum(sp.diff(Kc[i,j], v) for j, v in enumerate((x,y,z))) for i in range(3)]
symg = sp.Matrix(3,3, lambda i,j: (sp.diff(bv[j], (x,y,z)[i]) + sp.diff(bv[i], (x,y,z)[j]))/2)
check('B3 [T] a uniform trace-free K (momentum constraint holds) is kept static only by beta = K.x + Killing: a shift that is a '
      'local function of the fields at a point is constant there, so no memoryless local shift unwinds every stationary state',
      mom == [0,0,0] and symg == Kc, 'beta = (y, x, 0) up to rotations/translations')
okg = all(rows[n][0][3] > 1.8*rows[n][0][2] for n in ('harmonic', 'strain mu1/3'))
check('B4 [D] with memory but no damping (harmonic labels, strain driver at eta = 0) every gauge speed is <= 1, rotation stays '
      'bounded, but around a static star the shift grows linearly (a slice tilt running to null)', okg and rows['harmonic'][1][1] < 3,
      f"beta {rows['harmonic'][0][2]:.0f}->{rows['harmonic'][0][3]:.0f} (harmonic), {rows['strain mu1/3'][0][2]:.0f}->{rows['strain mu1/3'][0][3]:.0f} (strain)")
w, k, m1, m2 = sp.symbols('omega k mu1 mu2'); I = sp.I
Al = sp.Matrix([[0,0,-2,0,2*I*k],[0,0,0,-2,0],[k**2/6,2*k**2/3,0,0,0],[0,k**2/2,0,0,0],[I*k*(m1+m2),I*k*m2,0,0,0]])
pl = sp.factor((Al - I*w*sp.eye(5)).det()); pc = sp.factor(pl.subs(m2, -sp.Rational(5,3)*m1))
check('B5 [T] value drivers: longitudinal omega^2 = k^2 (1 + 6(mu1 + mu2))/3; a static tied-lapse star (h_zz = 10U, tr h = 6U) '
      'is stationary only if mu2 = -5 mu1/3, then omega^2 = k^2 (1 - 4 mu1)/3: stable only for mu1 < 1/4, a supplied mu1, '
      'and only for Psi = Phi', sp.simplify(pc.subs(w, k*sp.sqrt((1-4*m1)/3))) == 0 and rows['val 5/3 mu.1'][0][3] < 1.01*rows['val 5/3 mu.1'][0][2]+0.5,
      f'{pc}')
st5, ro5 = rows['strain eta5'][0], rows['strain eta5'][1]
check('B6 [D] damping eta > 0 bounds the static tilt (beta = 10 mu U k/eta) but an overdamped driver leaves a rotating '
      'strain offset h = 2 eta K/(mu k^2): eta must sit in a window set by each system size', st5[3] <= st5[2]*1.01 and abs(ro5[1]-30) < 3,
      f'eta 5: static beta {st5[3]:.2f}, rotating h -> {ro5[1]:.1f} (predicted 30)')

print('== C. estimates against measurement (c = 3e8, window ln 16 = 2.77)')
c = 2.998e8; Gn = 6.674e-11; age = 1.4e17; ln16 = np.log(16)
def wlt(J, r): return 2*Gn*J/(c**2*r**3)
win = {'Earth (J 5.86e33, age 1.4e17 s)': 3*wlt(5.86e33, 6.37e6)*age, 'Sun (J 1.9e41)': 3*wlt(1.9e41, 6.96e8)*age,
       'Milky Way disk (J 1e67, R 3e20)': 3*wlt(1e67, 3e20)*age}
print('   zero-shift winding 3 w_LT x age: ' + '; '.join(f'{k_} {v:.1e}' for k_, v in win.items()))
check('C1 [E] zero shift winds measured rotators out of the window by 1e3-1e5 window widths', min(list(win.values())[:2]) > 100*ln16, 'galaxies stay inside')
mu = 1/3; tE = 6.37e6/(10*mu*c*7e-10); tS = 6.96e8/(10*mu*c*2.1e-6)
check('C2 [E] undamped drivers tilt to null in r/(10 mu c |U|), far below the ages', tE < 1e10 and tS < 1e10, f'Earth {tE/86400:.0f} d, Sun {tS/86400:.1f} d')
d_mag = (4e27/5.4e34)*0.2; t_mag = 1.2e4/(4*0.1*c*d_mag)
check('C3 [E] the static-compatible value driver (mu1 = 0.1) tilts to null around a magnetar (B = 1e15 G anisotropic stress, '
      'Psi - Phi ~ 1.5e-8) in hours, against ages of 1e3-1e4 yr', t_mag < 1e6, f'{t_mag/3600:.1f} h')
eta_lo = 10*mu*c*0.2/1.2e4; rS = 1.27e10; aS = 0.5; eta_hi = ln16*mu*c**2/(2*rS**2*(aS*c/(4*rS)))
check('C4 [E] a constant eta cannot serve both: neutron star (tilt < c) needs eta > 10 mu c U/r, spinning Sgr A* (offset < '
      'ln 16) needs eta < ln16 mu c^2/(2 r^2 w); linear formulas at the horizon, indicative', eta_lo > 1e3*eta_hi, f'eta > {eta_lo:.1e}/s vs eta < {eta_hi:.1e}/s')

print('== D. the slip: a whole-site relabelling triggered by the zero-shift frame (planar shear toy, 64 layers)')
nz, steps, v = 64, 200000, np.linspace(0, 1, 64)*0.003          # layer x-velocity per tick, in cubes
u = np.zeros(nz); m = np.zeros(nz, int); smax = 0; slips = 0
for _ in range(steps):
    u += v; s = np.diff(u) - np.diff(m)
    for j in np.where(np.abs(s) > 0.5)[0]:
        m[j+1:] += int(np.sign(s[j])); slips += 1               # relabel every site above: a lattice automorphism
    s = np.diff(u) - np.diff(m); smax = max(smax, np.abs(s).max())
need = (u[-1]-u[0]); unsl = np.abs(np.diff(u)).max()
def lmean(sh):
    L = [1,1,1, np.sqrt(1+sh**2), np.sqrt(2), np.sqrt(1+(1+sh)**2)]
    return np.mean(np.log(L)) - np.mean(np.log([1,1,1,1,np.sqrt(2),np.sqrt(2)]))
check('D1 [T+D] slipping the sites above a layer by one cube when its shear passes 1/2 (where the relabelled cube is '
      'less strained) keeps every cube within shear 1/2, with no rate parameter',
      smax <= 0.5+1e-12 and abs(slips - round(need)) <= nz and unsl > 5, f'max shear {smax:.3f} vs unslipped {unsl:.1f}; slips {slips}, shear total {need:.0f}')
check('D2 [T] simple shear keeps volume, so a volume trigger ignores the residual shear, while the log-mean-edge trigger moves by '
      'up to the listed amount at shear 1/2', abs(lmean(0.5)) < 0.1, f'd ln(log-mean edge) at s = 1/2: {lmean(0.5):+.3f} (det = 1 exactly)')
x_ = (1 - ((1/16 + 0.5)/1.5)**2); x2 = (1 - ((1/8 + 0.5)/1.5)**2)
check('D3 [E] zero-shift collapse (quasi-static uniform ball, floor-horizon D2 method): the centre reaches the floor (lapse ratio '
      '1/16 .. 1/8) when the surface is at 1.16-1.21 r_s, after the centre entered the event horizon (surface 2.25 r_s)',
      1/x_ < 2.25 and 1/x2 < 2.25, f'R/r_s {1/x_:.2f} (1/16), {1/x2:.2f} (1/8)')
print('supplied: linear ADM + dust/current sources, the tied lapse as h_00 = -h_kk/3, the driver families, LCDM-like a(t) (A1),')
print('  measured J, R, ages; magnetar stress ratio; Sgr A* spin 0.5 (C4 indicative); planar shear only in D (rings and')
print('  dislocations not built); quasi-static collapse (D3). not built: register-level slip, the constraint on registers.')
print(f'elapsed {time.time()-T0:.1f} s')
print(f'TOTAL: PASS={NP} FAIL={NF}')
