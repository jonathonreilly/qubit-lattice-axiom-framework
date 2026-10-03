"""A14 check N4: event-paced change with idle sites as walls (1D toy, supplied model).
Single excitation on a chain; brickwork of small-dose partial swaps exp(-i th sigma_x)
on (x,x+1) pairs, even layer then odd layer each tick.  Each bond step happens only if
the bond is 'active' this tick:
  OR : at least one endpoint active  -> P = 1-(1-p)^2
  AND: both endpoints active (idle sites hold their possibilities = walls) -> P = p^2
Endpoint activity is drawn afresh each tick with probability p ('blinking').
Control: STATIC walls -- the same activity pattern frozen for all ticks.
Optional vacuum-relative phase e^{i th} on fired bonds touching the excitation (ph=1).
Reports centroid speed / (2 th P) and fidelity with the averaged generator th*P."""
import sys, signal, time
import numpy as np
signal.alarm(58)
L = 2048; th = float(sys.argv[1]); T = int(sys.argv[2]); ph = int(sys.argv[3])
x = np.arange(L); x0 = 300; sig = 30.0; k0 = -np.pi/2
psi0 = np.exp(-(x - x0)**2/(4*sig**2) + 1j*k0*x); psi0 /= np.linalg.norm(psi0)
c, s = np.cos(th), np.sin(th)
def layer(psi, par, fire):
    # bonds (i,i+1) with i = par, par+2, ... ; fire: bool per bond
    a = psi[par:L-1:2].copy(); b = psi[par+1:L:2].copy()
    n = min(len(a), len(b)); a = a[:n]; b = b[:n]; f = fire[:n]
    ph_ = np.exp(1j*th) if ph else 1.0
    na = np.where(f, ph_*(c*a - 1j*s*b), a); nb = np.where(f, ph_*(c*b - 1j*s*a), b)
    out = psi.copy(); out[par:par+2*n:2] = na; out[par+1:par+1+2*n:2] = nb
    return out
def run(mode, p, static, seed):
    rng = np.random.default_rng(seed); psi = psi0.copy()
    act_static = rng.random((2, L)) < p
    for t in range(T):
        for par in (0, 1):
            act = act_static[par] if static else (rng.random(L) < p)
            left = act[par:L-1:2]; right = act[par+1:L:2]; n = min(len(left), len(right))
            fire = (left[:n] & right[:n]) if mode == 'AND' else (left[:n] | right[:n])
            psi = layer(psi, par, fire)
    return psi
def avg(P):
    global c, s
    c0, s0 = c, s; c, s = np.cos(th*P), np.sin(th*P)
    psi = psi0.copy()
    for t in range(T):
        for par in (0, 1):
            psi = layer(psi, par, np.ones(L, bool))
    c, s = c0, s0
    return psi
t0 = time.time()
cen0 = np.sum(x*np.abs(psi0)**2)
print(f"th={th} T={T} vacuum-phase={ph}; clean speed check (P=1):", end=" ")
pc = avg(1.0); print(f"v/(2th) = {(np.sum(x*np.abs(pc)**2)-cen0)/T/(2*th):.4f}")
print(" mode p     P      blinking: v/(2 th P)  fidelity  width/w0 | static: v/(2 th P)")
for mode in ('OR', 'AND'):
    for p in (0.3, 0.6):
        P = 1-(1-p)**2 if mode == 'OR' else p*p
        ref = avg(P); wref = np.sqrt(np.sum((x-np.sum(x*np.abs(ref)**2))**2*np.abs(ref)**2))
        vb, fb, wb, vs = [], [], [], []
        for sd in range(3):
            pb = run(mode, p, False, 10+sd); pr = np.abs(pb)**2
            cb = np.sum(x*pr); vb.append((cb-cen0)/T/(2*th*P)); fb.append(abs(np.vdot(ref, pb))**2)
            wb.append(np.sqrt(np.sum((x-cb)**2*pr))/wref)
            psb = run(mode, p, True, 20+sd); vs.append((np.sum(x*np.abs(psb)**2)-cen0)/T/(2*th*P))
        print(f" {mode:3s} {p:.1f}  {P:.3f}   {np.mean(vb):.4f}           {np.mean(fb):.4f}   {np.mean(wb):.3f}  | {np.mean(vs):+.4f}")
print(f"elapsed {time.time()-t0:.1f}s")
