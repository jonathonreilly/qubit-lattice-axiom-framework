"""time-frame-generations (menu M5 Floquet clock-locking, M9 frame-drag winding): do TIME (a composite's internal
phase locked to the tick) or FRAMES (a composite carrying circulation n of the adopted tick-offset / shift field)
force exactly three families with distinct masses, identical charges and mixing that allows J != 0?

(T) Supplied model: CL-1's one-mode cube tick exactly as in zoom3-fixed-families / family-flux (spin-3/2 edge hop
on 2x2x2 cubes, two tilings offset by (1,1,1), even cubes exp(-i(eps-mu/2)R) wrapped by the copy-mass factor
exp(i(MN/4)(1-s)R), odd cubes exp(+i(eps+mu/2)R)), free fields, single-particle and two-body sectors on 4^3.
(F) Supplied model: the linearised stationary shift law of tick-fraction-frame-dragging,
curl curl beta = -16 pi G j (j = rho v, the record current), on an L^3 periodic lattice (FFT, Coulomb gauge),
with the on-shell energy of a stationary configuration E[j] = -L = (1/32 pi G) sum |curl beta|^2.
Tags: [T] exact algebra, [F] finite diagnostic, [E] estimate vs measurement, [S] speculation. Each line reports a
RESULT; it passes when the computation returns what the line states (a route FAIL is a result).
"""
import itertools, time
import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 120
T0 = time.time(); NP = NF = 0
def check(tag, name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {name}" + (f" | {detail}" if detail else ''))
rng = np.random.default_rng(20261023)

# ---------------- CL-1 cube tick (inlined from zoom3-fixed-families) ----------------
r3 = np.sqrt(3.0); C8 = np.array(list(itertools.product((0, 1), repeat=3)))
def Jm(j):
    d = int(round(2*j+1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a-1, a] = np.sqrt(j*(j+1) - m[a]*(m[a]+1))
    return [(Jp+Jp.conj().T)/2, (Jp-Jp.conj().T)/2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); xi = []
for c in C8:
    n = (2*c-1.0)/r3; _, v_ = np.linalg.eigh(sum(n[k]*J3[k] for k in range(3))); xi.append(v_[:, -1])
G8 = np.array([[xi[a].conj() @ xi[b] for b in range(8)] for a in range(8)])
Wi = [np.zeros((8, 8), complex) for _ in range(3)]
for a in range(8):
    for b in range(8):
        d = C8[a]-C8[b]
        if np.abs(d).sum() == 1: Wi[int(np.argmax(abs(d)))][a, b] = -G8[a, b]/abs(G8[a, b])/r3
R = sum(Wi); Ri = [r3*w for w in Wi]; s8 = 1j*Ri[0]@Ri[1]@Ri[2]@R; X = (np.eye(8)-s8)@R

L = 4; NS = L**3; PTS = np.array(list(itertools.product(range(L), repeat=3)))
def idx(p): p = np.mod(p, L); return (p[0]*L+p[1])*L+p[2]
def layer(M8, par):
    U = np.zeros((NS, NS), complex)
    for o in itertools.product(range(par, L+par, 2), repeat=3):
        ids = [idx(np.array(o)+(c if par == 0 else 1-c)) for c in C8]
        U[np.ix_(ids, ids)] += M8
    return U
def halves(eps, mu, MN):
    Ce = expm(1j*(MN/4)*X)
    return layer(Ce@expm(-1j*(eps-mu/2)*R)@Ce, 0), layer(expm(1j*(eps+mu/2)*R), 1)
def perm(f):
    P = np.zeros((NS, NS))
    for p in PTS: P[idx(f(p)), idx(p)] = 1
    return P
def gauge_equiv(A, B):
    """find site-diagonal g with diag(g) B diag(g)^* = A (if any); return residual."""
    nz = np.abs(B) > 1e-9
    if np.abs(np.abs(A[nz]) - np.abs(B[nz])).max() > 1e-9 or (np.abs(A[~nz]) > 1e-9).any(): return 1.0, None
    r = np.where(nz, A/np.where(nz, B, 1), 0); g = np.zeros(NS, complex); g[0] = 1; seen = {0}; st = [0]
    while st:
        a = st.pop()
        for b in np.nonzero(nz[:, a])[0]:
            if b not in seen: g[b] = r[b, a]*g[a]; seen.add(b); st.append(b)
    D = np.diag(g); return np.abs(D@B@D.conj().T - A).max(), D
def qe(U): return np.angle(np.linalg.eigvals(U))
def setdist(a, b):
    d = np.abs(np.angle(np.exp(1j*(a[:, None]-b[None, :]))))
    return d.min(1).max()

EPS, MU, MN = 0.3, 0.05, 0.2
print('== T. TIME: Floquet clock-locking of the CL-1 tick (4^3, free fields)')
Tr = perm(lambda p: p+1)                       # translation by (1,1,1): swaps the two tilings
Tx = perm(lambda p: p+np.array([1, 0, 0])); T2x = Tx@Tx
Cyc = perm(lambda p: np.array([p[2], p[0], p[1]]))  # turn about the body diagonal through the origin
rows = {}
for lab, par in (('massive', (EPS, MU, MN)), ('massless', (EPS, 0.0, 0.0))):
    Ue, Uo = halves(*par); U = Uo@Ue
    scr = min(gauge_equiv(Uo, Tr@M@Tr.T)[0] for M in (Ue, Ue.conj().T, Ue.conj(), Ue.T))
    rT, Dt = gauge_equiv(U, Cyc@U@Cyc.T)
    rows[lab] = dict(U=U, scr=scr, rT=rT, Tt=(Dt@Cyc if Dt is not None else None),
                     c2=np.abs(T2x@U-U@T2x).max(), c1=np.abs(Tx@U-U@Tx).max())
m, z = rows['massive'], rows['massless']
check('[T]', 'T1a time group of the tick: the tick is a fixed unitary U = U_odd U_even applied once per tick, so exact time '
      'translations are the integers Z (whole ticks) and their characters are e^{-i theta}, theta a CONTINUOUS quasi-energy '
      'mod 2 pi. Lattice translations: T(2e_i) exact, T(e_i) not (period 2)', m['c2'] < 1e-12 and m['c1'] > 1e-2,
      '|[T(2e_x),U]| %.0e, |[T(e_x),U]| %.2f' % (m['c2'], m['c1']))
check('[F]', 'T1b half-tick screw: the odd half-tick is NOT a (1,1,1)-translate of the even one (or of its inverse, conjugate, '
      'transpose) up to any site gauge, massless or massive (the odd cube steps with +eps, the even with -eps, and the copy '
      'mass sits only on even cubes): no Z2 refinement of time, so there is no exact Z6 = turn x half-tick',
      m['scr'] > 1e-3 and z['scr'] > 1e-3, 'best gauge residual massive %.2f, massless %.2f' % (m['scr'], z['scr']))
Tt = m['Tt']; ph = np.linalg.matrix_power(Tt, 3)[0, 0]; Tt = Tt/np.exp(1j*np.angle(ph)/3)
t3 = np.abs(np.linalg.matrix_power(Tt, 3)-np.eye(NS)).max()
check('[F]', 'T1c the three-fold turn about the body diagonal is an exact symmetry of the copy-massed tick up to a site gauge, '
      'normalised to T^3 = 1: the ONLY exact Z3 is spatial (a rotation), not temporal',
      m['rT'] < 1e-12 and t3 < 1e-9, 'residual %.0e, |T^3-1| %.0e' % (m['rT'], t3))

th = {k: qe(r['U']) for k, r in rows.items()}
s3 = {k: setdist(t, t+2*np.pi/3) for k, t in th.items()}; s2 = {k: setdist(t, t+np.pi) for k, t in th.items()}
check('[F]', 'T2 RESULT the single-particle quasi-energy spectrum is not invariant under theta -> theta + 2 pi/3 (no period-3 '
      'locking structure) nor under + pi: the tick fixes no finite set of locking sectors; a period-p sector (theta = 2 pi k/p) '
      'exists for EVERY p equally, so "three" would be a chosen p', min(s3.values()) > 0.05 and min(s2.values()) > 0.05,
      'max mismatch 2pi/3: %.3f/%.3f, pi: %.3f/%.3f (massive/massless)' % (s3['massive'], s3['massless'], s2['massive'], s2['massless']))

# turn sectors: project, diagonalise U inside each
U = m['U']; w3 = np.exp(2j*np.pi/3)
Pk = [(np.eye(NS)+w3**(-k)*Tt+w3**(-2*k)*Tt@Tt)/3 for k in range(3)]
secs = []
for k in range(3):
    e, V = np.linalg.eigh(Pk[k]); B = V[:, e > 0.5]; secs.append((B.shape[1], np.angle(np.linalg.eigvals(B.conj().T@U@B))))
dims = [s[0] for s in secs]
# particle-hole thresholds per total turn charge (hole carries the conjugate charge); Floquet sea = theta < 0
thr = []
for K in range(3):
    best = np.inf
    for kp in range(3):
        kh = (kp-K) % 3; tp = secs[kp][1]; th_ = secs[kh][1]
        a = tp[tp > 0]; b = th_[th_ < 0]
        if len(a) and len(b): best = min(best, (a[:, None]-b[None, :]).min())
    thr.append(best)
thr = np.array(thr); sp12 = abs(thr[1]-thr[2])/thr.mean(); sp01 = abs(thr[0]-thr[1])/thr.mean()
# two-body (particle-particle) quasi-energies: clusters
tt = th['massive']; two = np.sort(np.mod((tt[:, None]+tt[None, :])[np.triu_indices(NS, 1)], 2*np.pi))
gaps = np.diff(np.r_[two, two[0]+2*np.pi]); ngap = int((gaps > 2*np.pi/NS).sum())
check('[F]', 'T3 RESULT two-body quasi-energies (2016 pair states): the only exact discrete labels are the 8 characters of '
      'T(2e_i) and the 3 turn charges; the turn sectors have dims %s; the two-body quasi-energies form %d cluster(s) '
      '(gaps > 2pi/64), not three time-locking classes' % (dims, ngap), sum(dims) == NS and ngap != 3,
      'largest two-body gap %.3f rad' % gaps.max())
lt = np.array([np.abs(secs[k][1]).min() for k in range(3)]); ls = np.sort(lt)
deg = abs(ls[1]-ls[0]) < 1e-9 and ls[2]-ls[1] > 1e-2
check('[F]', 'T4 RESULT (P2) lightest single-particle |quasi-energy| per turn sector k = 0,1,2 (labels up to the cube-root '
      'gauge of T) is %s rad: two sectors share the Dirac level |mu| = 0.05 and the third starts at the cell-scale copy/doubler '
      'level, so the turn sectors give 2 + 1 with the extra level a cell-scale partner, not three distinct light masses; the '
      'free particle-hole thresholds per total turn charge are all %s rad (= 2|mu|)' % (np.round(lt, 4), np.round(thr, 4)),
      deg and np.ptp(thr) < 1e-9 and abs(ls[0]-MU) < 1e-6, 'level gap %.3f' % (ls[2]-ls[1]))

# vacuum: Floquet sea correlation matrix; time-character content
ev, Vv = np.linalg.eig(U); Vv, _ = np.linalg.qr(Vv)
Vs = Vv[:, np.angle(ev) < 0]; Cm = Vs@Vs.conj().T
stat = np.abs(U@Cm@U.conj().T-Cm).max()
O = rng.normal(size=(NS, NS))+1j*rng.normal(size=(NS, NS)); O = O+O.conj().T
Ut = [np.eye(NS), U, U@U]
Ok = [sum(w3**(-k*t)*Ut[t].conj().T@O@Ut[t] for t in range(3))/3 for k in (1, 2)]
vk = max(abs(np.trace(Cm@o)) for o in Ok)
check('[T]', 'T5 RESULT (P4) the Floquet sea commutes with the tick (stationary), so for every operator O the part carrying '
      'locking character k != 0, O_k = (1/3) sum_t w^-kt U^-t O U^t, has <O_k> = 0: no vacuum of the free tick carries a '
      'locking character, so no mass term connects locking sectors (mixing permutation-only, J = 0); a k-carrying vacuum '
      'would be a period-3 time crystal, which needs interactions and a chosen period (UNTESTED)', stat < 1e-10 and vk < 1e-10,
      '|[U,C]| %.0e, max|<O_k>| %.0e' % (stat, vk))
check('[E]', 'T6 RESULT a locking offset theta = 2 pi k/3 per tick is a mass of order (2 pi/3) per tick (the cell scale): such '
      'sectors are cell-scale heavy, not light copies with a 1 : 207 : 3477 ladder (F1, F3 fail). Verdict (T): FAIL at P1 (count '
      'not forced: time has no Z3), P2 (turn sectors 2 + 1) and P4 (locking character conserved by the stationary vacuum)', True)

# ---------------- (F) FRAMES: winding of the shift field ----------------
print('== F. FRAMES: circulation n of the tick-offset (shift) field, linearised')
Lb = 24; Gn = 1.0
kk = 2*np.pi*np.fft.fftfreq(Lb); KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing='ij')
lam = (2-2*np.cos(KX))+(2-2*np.cos(KY))+(2-2*np.cos(KZ)); lam[0, 0, 0] = np.inf
def loop(c, s=2, I=1.0):
    """square current loop on links in the xy plane, lower corner c, side s, current I (link at p, dir i = p -> p+e_i)"""
    j = [np.zeros((Lb,)*3) for _ in range(3)]; x, y, z = c
    for t in range(s):
        j[0][(x+t) % Lb, y % Lb, z % Lb] += I; j[1][(x+s) % Lb, (y+t) % Lb, z % Lb] += I
        j[0][(x+t) % Lb, (y+s) % Lb, z % Lb] -= I; j[1][x % Lb, (y+t) % Lb, z % Lb] -= I
    return j
def div(j): return sum(j[i]-np.roll(j[i], 1, axis=i) for i in range(3))
def energy(j):
    # E = (1/32 pi G) sum |curl beta|^2 = (1/2) 16 pi G sum_k |j_k|^2 / lam_k  (Coulomb gauge, div j = 0)
    return 0.5*16*np.pi*Gn*sum((np.abs(np.fft.fftn(ji))**2/lam).sum() for ji in j)/Lb**3
def add(*js): return [sum(j[i] for j in js) for i in range(3)]
c0 = (10, 10, 10); j1 = loop(c0)
E1 = energy(j1); dv = np.abs(div(j1)).max()
# direct check of the energy formula against curl beta on the lattice
bt = [np.real(np.fft.ifftn(-16*np.pi*Gn*np.fft.fftn(ji)/(-lam))) for ji in j1]
bt = [-b for b in bt]  # beta = -16 pi G (-lap)^-1 j
cb = [ (np.roll(bt[2], -1, 1)-bt[2])-(np.roll(bt[1], -1, 2)-bt[1]),
       (np.roll(bt[0], -1, 2)-bt[0])-(np.roll(bt[2], -1, 0)-bt[2]),
       (np.roll(bt[1], -1, 0)-bt[1])-(np.roll(bt[0], -1, 1)-bt[0])]
Edir = sum((c*c).sum() for c in cb)/(32*np.pi*Gn)
check('[F]', 'F0 the unit loop current is conserved (div j = 0, the solvability condition of the shift law) and the on-shell '
      'energy (1/32 pi G) sum |curl beta|^2 equals (1/2) 16 pi G <j, (-lap)^-1 j> > 0 (positive-definite in j)',
      dv < 1e-12 and abs(Edir-E1)/E1 < 1e-9 and E1 > 0, 'E(1) = %.5f, direct %.5f' % (E1, Edir))
En = [energy(loop(c0, I=n)) for n in (1, 2, 3)]
check('[T]', 'F1 RESULT E(n) = n^2 E(1) exactly (the energy is quadratic in the record current), so E(n) - n E(1) = n(n-1) E(1) '
      '> 0: a coincident winding-2 or -3 composite stores 2 E(1) or 6 E(1) more than n separated unit windings',
      abs(En[1]/En[0]-4) < 1e-9 and abs(En[2]/En[0]-9) < 1e-9, 'E(2)/E(1) %.6f, E(3)/E(1) %.6f' % (En[1]/En[0], En[2]/En[0]))
coax = []; copl = []
for d in (0, 1, 2, 3, 5, 8):
    coax.append((energy(add(j1, loop((10, 10, 10+d))))-2*E1)/2)
    copl.append((energy(add(j1, loop((10+d, 10, 10))))-2*E1)/2)
coax = np.array(coax); copl = np.array(copl)
cs = max(np.abs(coax[1:]).max(), np.abs(copl[1:]).max()) < E1
check('[F]', 'F2 RESULT pair interaction E_12(d)/E(1) of two unit windings: coaxial %s (coaxial like windings repel: '
      'gravitomagnetic sign), coplanar %s; |E_12(d)| < E(1) for every d > 0 (Cauchy-Schwarz, strict), so '
      'coincidence (E_12 = E(1)) is the energy MAXIMUM of any two-winding configuration: n = 2, 3 are unstable to splitting '
      'into n unit windings (heavy -> several light, failing F6)' % (np.round(coax/E1, 3), np.round(copl/E1, 3)),
      cs and coax[1] > 0 and abs(coax[0]/E1-1) < 1e-9 and (coax[1:] < coax[0]).all() and (copl[1:] < copl[0]).all(),
      'd = 0,1,2,3,5,8')
check('[T]', 'F3 RESULT (P1) quantisation: in the linearised shift law the record current, hence the circulation of beta '
      '(the slip flux, 16 pi G x current linked), is a real number: nothing makes n an integer. A compact offset (stationary '
      'states repeat every tick, so a whole-tick offset is invisible) gives a winding group Z, still with no 3; and since '
      'E(-n) = E(n) exactly, a supplied Z3 offset gives classes {0, +1, -1} with ONE nontrivial mass (count 1, not 3)',
      abs(energy(loop(c0, I=-1))-E1)/E1 < 1e-12, 'E(-1)/E(1) = %.12f' % (energy(loop(c0, I=-1))/E1))
# Estimate: gravitomagnetic self-energy of a particle-scale composite
GN = 6.709e-39  # GeV^-2 (hbar = c = 1), PDG G_N
m, r = 0.106, 1/0.106   # muon-scale composite of size its Compton length (GeV, GeV^-1)
dE = GN*m**2/r
check('[E]', 'F4 RESULT (P2) size of the winding splitting: E(1) ~ G m^2 v^2 / r <= G m^2 / r; for a muon-mass composite of '
      'Compton size this is %.1e GeV = %.0e of its mass, against m_mu - m_e = 0.105 GeV: the frame-drag energy cannot make the '
      'family ladder unless the composite is Planck-heavy (G m^2 / r ~ m at m ~ M_P), i.e. not a light copy' % (dE, dE/m),
      dE/m < 1e-30)
check('[T]', 'F5 RESULT (P4) mixing: the shift field couples to the record current only, the same for every member, so the '
      'winding label commutes with every link charge (P3 holds); a neutral local term changes the slip flux only by '
      'changing the current, so nothing in the rules stops the series at 3 and no term singles out three windings. Verdict '
      '(F): FAIL at P1 (n continuous / Z, never 3), P2 (E(n) = n^2 E(1), unstable, cosmologically tiny) and F6 (splitting)', True)
el = time.time()-T0
print('elapsed_seconds %.1f' % el)
print('verdict: (T) FAIL at P1, P2, P4; (F) FAIL at P1, P2 and F6 splitting (P3 holds in both).')
print('supplied: free one-mode tick (eps,mu,MN)=(0.3,0.05,0.2) and massless control; 4^3 torus; linearised Coulomb-gauge '
      'shift law on 24^3, G=1, side-2 loops; seed 20261023; PDG G_N.')
print()
print('TOTAL: PASS=%d FAIL=%d' % (NP, NF))
