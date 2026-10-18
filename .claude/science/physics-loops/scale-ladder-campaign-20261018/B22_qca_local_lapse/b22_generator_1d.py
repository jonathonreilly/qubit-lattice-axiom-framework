"""B22 runner 2: smooth local lapse from the step's Floquet generator, 1D Dirac walk W = S.C.

Definition B (generator lapse): H_F = i log W (principal branch, eigenphases in (-pi, pi]),
H(N) = (1/2){N, H_F} with N the cell-diagonal lapse, W_N := exp(-i H(N)).  W_N = W^n for N = n.

Predictions (declared from the first-order Moyal/Weyl symbol calculus before running; not fitted):
  P1  [H(N), H(M)] = -i (1/2){w, Q} + O(d^3),  w = N M' - M N',  Q = Op( (1/2) d_k h(k)^2 ).
      For the walk h(k)^2 = omega(k)^2 * 1 (bands +-omega), so Q is the scalar omega*omega'
      = v^2 k + O(k^3) near k = 0, with v^2 = theta cot theta: the hypersurface-deformation
      form -i v^2 G[w] (G[w] = (1/2){w, p}) with the Lorentzian sign, at leading order.
  P2  quasi-energy offset: for H_F - E the bracket gains +i E (1/2){w, Op(d_k h)} (a lapse-weighted
      current, not a translation).  The walk's second species (k ~ pi) sits at quasi-energy pi, so
      the principal-branch generator gives it the non-geometric term; lapse in units of two steps
      (generator of W^2) puts both species at 0.
  P3  exponentiated: C = W_N W_M W_N^-1 W_M^-1 displaces a band packet at k0 by -w g(k0),
      g = (1/2) d_k^2 omega^2, the same for both chiralities/bands (contrast runner 1).
  P4  locality: H_F is exponentially local for theta > 0 (gaps at 0 and pi host the branch cut);
      for theta = 0 the cut crosses the bands and |H_F(r)| ~ 1/r.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qca1d import Brick1D, omega_walk, g1

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"\n        {detail}" if detail else ""))

t0 = time.time()
rng = np.random.default_rng(7)


class Gen1D:
    """FFT-applied generator h(k) (2x2 per k) on Lc cells, cell-diagonal lapses."""
    def __init__(self, B, power=1, E=0.0):
        self.B = B; self.Lc = B.Lc
        ks = B.kgrid(); self.ks = ks
        self.h = np.zeros((self.Lc, 2, 2), complex); self.dh = np.zeros_like(self.h); self.hsq_d = np.zeros_like(self.h)
        for n, k in enumerate(ks):
            self.h[n] = self.hk(k, power, E)
            dk = 1e-5
            hp, hm = self.hk(k + dk, power, E), self.hk(k - dk, power, E)
            self.dh[n] = (hp - hm) / (2 * dk)
            self.hsq_d[n] = 0.5 * (hp @ hp - hm @ hm) / (2 * dk)     # (1/2) d_k h^2
        self.X = np.arange(self.Lc, dtype=float)
    def hk(self, k, power, E):
        W = np.linalg.matrix_power(self.B.Wk(k), power)
        ev, V = np.linalg.eig(W)
        om = -np.angle(ev * np.exp(1j * E))          # principal branch of e^{iE} W
        return V @ np.diag(om) @ np.linalg.inv(V)
    def op(self, sym, psi):
        Ak = self.B.to_k(psi)
        return self.B.from_k(np.einsum('kij,kj->ki', sym, Ak))
    def H(self, psi): return self.op(self.h, psi)
    def lapse(self, N, psi):
        Nc = np.repeat(N(self.X), 2)
        return 0.5 * (Nc * self.H(psi) + self.H(Nc * psi))
    def bracket(self, N, M, psi):
        return self.lapse(N, self.lapse(M, psi)) - self.lapse(M, self.lapse(N, psi))
    def anti(self, wfun, sym, psi):
        wc = np.repeat(wfun(self.X), 2)
        return 0.5 * (wc * self.op(sym, psi) + self.op(sym, wc * psi))
    def expH(self, N, eps, psi, steps=None):
        """exp(-i eps H(N)) psi by repeated Taylor."""
        nrm = abs(eps) * np.pi * np.max(np.abs(N(self.X))) + 1e-12
        s = steps or int(np.ceil(nrm / 0.5))
        out = psi.copy()
        for _ in range(s):
            term = out.copy(); acc = out.copy()
            for j in range(1, 30):
                term = (-1j * eps / s) * self.lapse(N, term) / j
                acc += term
                if np.linalg.norm(term) < 1e-15: break
            out = acc
        return out


def lowenergy_state(B, kc, k_center=0.0, bands=(+1, -1)):
    ks = B.kgrid(); Ak = np.zeros((B.Lc, 2), complex)
    for n, k in enumerate(ks):
        q = (k - k_center + np.pi) % (2 * np.pi) - np.pi
        if abs(q) < kc:
            for s in bands:
                Ak[n] += (rng.normal() + 1j * rng.normal()) * np.exp(-(q / (0.5 * kc)) ** 2) * B.band(k, s)[1]
    psi = B.from_k(Ak); return psi / np.linalg.norm(psi)


# ------------------------------------------------------------------ P4 locality of H_F
for th, lab in ((0.5, "theta=0.5 (gapped)"), (0.0, "theta=0 (gapless)")):
    B = Brick1D(1024, th); G = Gen1D(B)
    Hr = np.fft.ifft(G.h, axis=0)              # H_r blocks (convention-independent magnitude)
    mag = np.array([np.abs(Hr[r]).max() for r in range(1, 200)])
    if th > 0:
        slope = np.polyfit(np.arange(10, 60), np.log(mag[9:59] + 1e-300), 1)[0]
        check(f"P4 [numerical] {lab}: H_F = i log W is exponentially local", slope < -0.3 and mag[60] < 1e-10,
              f"log|H_r| slope {slope:.3f} per cell; |H_60| = {mag[59]:.1e}")
    else:
        rr = np.arange(1, 200); odd = rr % 2 == 1
        pw = np.polyfit(np.log(rr[odd][5:60]), np.log(mag[odd][5:60]), 1)[0]
        check(f"P4 [numerical] {lab}: branch cut crosses the bands, |H_r| ~ 1/r (non-local generator)", abs(pw + 1) < 0.05,
              f"power-law exponent {pw:.3f}")

# ------------------------------------------------------------------ P1 generator bracket
Lc = 1024
print("\n  P1: relative error || [H(N),H(M)] psi - pred psi || / || pred psi ||, low-energy psi (|k| < 0.15, both bands)")
print("  theta  n   v^2(node)   err(symbol pred)   err(Dirac -i v^2 w p)   err(light-cone v=1)")
res = {}
for th in (0.0, 0.5, 1.0):
    B = Brick1D(Lc, th); G = Gen1D(B)
    v2 = 1.0 if th == 0 else th / np.tan(th)
    psi = lowenergy_state(B, 0.15)
    psym = np.zeros((Lc, 2, 2), complex); psym[:, 0, 0] = psym[:, 1, 1] = G.ks      # p = k on low-energy states
    for n in (1, 2, 4, 8):
        q = 2 * np.pi * n / Lc
        N = lambda X: np.cos(q * X); M = lambda X: np.sin(q * X); w = lambda X: q + 0 * X
        K = G.bracket(N, M, psi)
        pred = -1j * G.anti(w, G.hsq_d, psi)
        dirac = -1j * v2 * G.anti(w, psym, psi)
        lc = -1j * 1.0 * G.anti(w, psym, psi)
        e1 = np.linalg.norm(K - pred) / np.linalg.norm(pred)
        e2 = np.linalg.norm(K - dirac) / np.linalg.norm(dirac)
        e3 = np.linalg.norm(K - lc) / np.linalg.norm(lc)
        res[(th, n)] = (e1, e2, e3)
        print(f"  {th:.1f}  {n:2d}   {v2:.4f}     {e1:.2e}           {e2:.2e}              {e3:.2e}")
ok = all(res[(th, n)][0] < 1e-3 for th in (0.0, 0.5, 1.0) for n in (1, 2, 4))
sc = all(res[(th, 8)][0] / res[(th, 4)][0] > 3.0 for th in (0.5, 1.0))
check("P1 [numerical] smooth-lapse generator bracket equals the symbol prediction -i(1/2){w, omega omega'} on low-energy "
      "states (error < 1e-3, falling ~ q^2 with the lapse wavenumber)", ok and sc)
okd = all(res[(th, n)][1] < 0.02 for th in (0.0, 0.5, 1.0) for n in (1, 2))
disc = res[(1.0, 1)][2] > 10 * res[(1.0, 1)][1] and res[(0.5, 1)][2] > 5 * res[(0.5, 1)][1]
check("P1b [numerical] at low energy this is the hypersurface-deformation form -i v^2 G[w] with v^2 = theta cot theta "
      "(the node's cone, not the light-cone speed 1): within 2%, and the light-cone value is excluded for theta = 0.5, 1",
      okd and disc)

# ------------------------------------------------------------------ P2 quasi-energy offset; second species
th = 0.5; B = Brick1D(Lc, th); v2 = th / np.tan(th)
q = 2 * np.pi * 2 / Lc
N = lambda X: np.cos(q * X); M = lambda X: np.sin(q * X); w = lambda X: q + 0 * X
G0 = Gen1D(B); psi = lowenergy_state(B, 0.15)
E = 0.3; GE = Gen1D(B, E=E)
K0 = G0.bracket(N, M, psi); KE = GE.bracket(N, M, psi)
predE = K0 + 1j * E * G0.anti(w, G0.dh, psi)
eE = np.linalg.norm(KE - predE) / np.linalg.norm(KE - K0)
check("P2 [numerical] offsetting the generator by E (step e^{iE} W) adds exactly the lapse-weighted current "
      "+iE(1/2){w, d_k h}, not a translation", eE < 1e-2, f"relative residual {eE:.2e} (E = {E})")
# second species at k ~ pi, quasi-energy ~ pi
psi_pi = lowenergy_state(B, 0.15, k_center=np.pi)
psym_pi = np.zeros((Lc, 2, 2), complex)
qq = (G0.ks - np.pi + np.pi) % (2 * np.pi) - np.pi
psym_pi[:, 0, 0] = psym_pi[:, 1, 1] = qq
K = G0.bracket(N, M, psi_pi); dirac = -1j * v2 * G0.anti(w, psym_pi, psi_pi)
e_prin = np.linalg.norm(K - dirac) / np.linalg.norm(dirac)
Gm = Gen1D(B, E=np.pi)     # generator of -W: species at k ~ pi moved to quasi-energy ~ 0
K = Gm.bracket(N, M, psi_pi); e_flip = np.linalg.norm(K - dirac) / np.linalg.norm(dirac)
K = Gm.bracket(N, M, psi); dirac0 = -1j * v2 * G0.anti(w, np.repeat(G0.ks, 4).reshape(Lc, 2, 2) * np.eye(2), psi)
e_flip0 = np.linalg.norm(K - dirac0) / np.linalg.norm(dirac0)
G2 = Gen1D(B, power=2)     # lapse unit = two steps
K2a = G2.bracket(N, M, psi); K2b = G2.bracket(N, M, psi_pi)
# in units of two steps the cone is (2v)^2 and w carries lapse^2 in two-step units: same displacement as -i v^2 G[w] x 4
d2a = -1j * 4 * v2 * G0.anti(w, np.repeat(G0.ks, 4).reshape(Lc, 2, 2) * np.eye(2), psi)
d2b = -1j * 4 * v2 * G0.anti(w, psym_pi, psi_pi)
e2a = np.linalg.norm(K2a - d2a) / np.linalg.norm(d2a); e2b = np.linalg.norm(K2b - d2b) / np.linalg.norm(d2b)
check("P2b [numerical] species at k ~ pi (quasi-energy ~ pi): principal-branch generator fails the Dirac form; the "
      "generator of -W fixes it but breaks the k ~ 0 species; the generator of W^2 (lapse unit two steps) gives the "
      "Dirac form for both", e_prin > 1.0 and e_flip < 0.02 and e_flip0 > 1.0 and e2a < 0.02 and e2b < 0.02,
      f"rel. deviation from -i v^2 G[w]: principal {e_prin:.2f}; -W: k~pi {e_flip:.1e}, k~0 {e_flip0:.2f}; "
      f"W^2: k~0 {e2a:.1e}, k~pi {e2b:.1e}")

# ------------------------------------------------------------------ P3 exponentiated group commutator on packets
Lc = 4096; qL = 2 * np.pi / Lc
print("\n  P3: smooth-lapse group commutator, packets (sigma = 20 cells), N = A cos, M = A sin, w = A^2 q")
print("  theta  A   k0   band     dx        -w g(k0)   ratio")
rows = []
for th in (0.0, 0.2, 0.5):
    B = Brick1D(Lc, th); G = Gen1D(B)
    for A in (16, 32):
        N = lambda X: np.cos(qL * X); M = lambda X: np.sin(qL * X)
        w = A * A * qL
        for k0, sg in ((0.1, +1), (-0.1, +1), (0.1, -1), (0.3, +1)):
            psi = B.packet(k0, 1000.0, 20.0, sg)
            p = G.expH(M, -A, psi); p = G.expH(N, -A, p); p = G.expH(M, A, p); p = G.expH(N, A, p)
            dx = B.xmean(p) - B.xmean(psi)
            pr = -w * g1(k0, th)
            rows.append((th, A, k0, sg, dx, pr))
            print(f"  {th:.1f}  {A:2d}  {k0:+.1f}  {sg:+d}   {dx:9.4f}  {pr:9.4f}   {dx / pr:.4f}")
ok3 = all(abs(r[4] / r[5] - 1) < 0.03 for r in rows)
check("P3 [numerical] smooth-lapse group commutator displaces every packet (both chiralities and bands) by -w g(k0) "
      "within 3%; at small k0 this is -v^2 w", ok3)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}  ({time.time() - t0:.1f} s)")
