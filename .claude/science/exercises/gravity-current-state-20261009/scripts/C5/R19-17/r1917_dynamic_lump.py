"""C5 R19-17 (a)/(b): a LOCAL strain rate on a V1 lattice. Does the evolved vacuum track a local adiabatic
functional, and is the vacuum's response causal (no instantaneous channel)?
Model as r1917_static_lump.py (NN massless scalar, planar local scale factor), now a(z,t) = exp(A g(z) s(t)),
g = gaussian of width w, s(t) a smooth 0->1 ramp of duration Tr. Start: exact ground state at a = 1.
Evolution: exact flow of the frozen midpoint Hamiltonian per step (symplectic), Heisenberg mode functions,
independent per transverse momentum (midpoint grid NT x NT).
Measures:
 (i)  causality: |rho(z,t) - rho(z,0)| outside the lattice light cone |z| > zl + v_max t (v_max = 1);
 (ii) lag above the INSTANTANEOUS ground state of H(t) (exact static GS at the current a(z,t)):
      r_dyn(z,t) = rho(z,t) - rho_GS[a(.,t)](z), compared with the local homogeneous adiabatic formula
      <1/Omega> H_loc^2/(4 a^2), H_loc = d ln a/dt at the same z (R19-14 s = 0, per minimal massless dof);
 (iii) rate^2 scaling: Tr -> 2 Tr at equal ramp phase (local adiabatic order 2 => ratio 4);
 (iv) after the ramp: residual above the final ground state (non-adiabatic production)."""
import numpy as np, time
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

NT = 6
kt = 2*np.pi*(np.arange(NT)+0.5)/NT
gk = 4*np.sin(kt/2)**2
OM2 = (gk[:, None] + gk[None, :]).ravel()
Nz = 96; z = np.arange(Nz) - Nz/2
idx = np.arange(Nz); nxt = (idx+1) % Nz

def KM(a, O2):
    ah = 0.5*(a + np.roll(a, -1))
    K = np.diag(a*O2 + ah + np.roll(ah, 1)); K[idx, nxt] -= ah; K[nxt, idx] -= ah
    return K, a**3

def energy_density(U, P, a, O2):
    ah = 0.5*(a + np.roll(a, -1)); M = a**3
    Gff = (U @ U.conj().T).real; Gpp = (P @ P.conj().T).real
    dg = np.diag(Gff); dphi2 = dg + dg[nxt] - 2*Gff[idx, nxt]
    site = np.diag(Gpp)/(2*M) + a*O2*dg/2; link = ah*dphi2/2
    return (site + 0.5*(link + np.roll(link, 1)))/a**3

def gs_modes(a, O2):
    K, M = KM(a, O2); Mi = 1/np.sqrt(M)
    w2, V = np.linalg.eigh(Mi[:, None]*K*Mi[None, :]); w = np.sqrt(w2)
    U = (Mi[:, None]*V)/np.sqrt(2*w)[None, :]
    P = -1j*(np.sqrt(M)[:, None]*V)*np.sqrt(w/2)[None, :]
    return U, P, w

def rho_gs(a):
    return np.mean([energy_density(*gs_modes(a, O2)[:2], a, O2) for O2 in OM2], axis=0)

def ramp(t, Tr):
    x = np.clip(t/Tr, 0, 1); f = lambda y: np.where(y > 0, np.exp(-1/np.maximum(y, 1e-300)), 0.0)
    return f(x)/(f(x) + f(1-x))

def run(A, w, Tr, Ttot, dt, probe_times):
    gz = np.exp(-z**2/(2*w*w))
    afun = lambda t: np.exp(A*gz*ramp(t, Tr))
    states = []
    for O2 in OM2:
        U, P, _ = gs_modes(np.ones(Nz), O2); states.append([U, P])
    rho0 = np.mean([energy_density(U, P, np.ones(Nz), O2) for (U, P), O2 in zip(states, OM2)], axis=0)
    rec = {}; t = 0.0; nsteps = int(round(Ttot/dt)); pt = sorted(probe_times)
    for n in range(nsteps+1):
        if pt and abs(t - pt[0]) < dt/2:
            a = afun(t)
            rho = np.mean([energy_density(U, P, a, O2) for (U, P), O2 in zip(states, OM2)], axis=0)
            rec[pt.pop(0)] = (rho, a)
        if n == nsteps: break
        am = afun(t + dt/2)
        for i, O2 in enumerate(OM2):
            K, M = KM(am, O2); Mi = 1/np.sqrt(M); w2, V = np.linalg.eigh(Mi[:, None]*K*Mi[None, :]); W = np.sqrt(w2)
            U, P = states[i]
            Q = V.T @ (np.sqrt(M)[:, None]*U); Pq = V.T @ (Mi[:, None]*P)
            c = np.cos(W*dt)[:, None]; s = np.sin(W*dt)[:, None]
            Qn = c*Q + s/W[:, None]*Pq; Pn = -W[:, None]*s*Q + c*Pq
            states[i] = [Mi[:, None]*(V @ Qn), np.sqrt(M)[:, None]*(V @ Pn)]
        t += dt
    return rec, rho0, afun

# <1/Omega> on this grid (homogeneous a = 1)
kz = 2*np.pi*np.arange(Nz)/Nz; gz_ = 4*np.sin(kz/2)**2
inv = np.mean(1/np.sqrt(OM2[:, None] + gz_[None, :]))
pr(f'grid: Nz={Nz}, NT={NT}; <1/Omega> = {inv:.5f}; e0 = {rho_gs(np.ones(Nz))[0]:.6f}')

A, w = 0.10, 5.0
for Tr in (16.0, 32.0):
    t0 = time.time()
    phases = [0.25, 0.5, 0.75, 1.0]
    ptimes = [ph*Tr for ph in phases] + [Tr + 8.0]
    dt = 0.05
    rec, rho0, afun = run(A, w, Tr, Tr + 8.0, dt, ptimes)
    pr(f'\n=== A={A}, w={w}, ramp Tr={Tr}, dt={dt} ({time.time()-t0:.0f}s) ===')
    for tp in ptimes:
        rho, a = rec[tp]
        # local H at this time: d ln a/dt by central difference
        h = 1e-4; Hloc = (np.log(afun(tp + h)) - np.log(afun(tp - h)))/(2*h)
        rgs = rho_gs(a); rdyn = rho - rgs
        pred = inv*Hloc**2/(4*a**2)
        c = Nz//2
        # causality: outside light cone of the lump support (|z| > 4w + t)
        out_sel = np.abs(z) > 4*w + tp
        dout = np.abs(rho - rho0)[out_sel].max() if np.any(out_sel) else float('nan')
        dlump_edge = np.abs(rho - rho0)[np.abs(z) <= 4*w].max()
        pr(f'  t={tp:5.1f} (phase {tp/Tr:4.2f}): r_dyn(centre) = {rdyn[c]:+.4e}, local formula {pred[c]:+.4e} (ratio {rdyn[c]/pred[c] if pred[c] else float("nan"):.3f});'
           f' max|rho-rho0| inside lump = {dlump_edge:.2e}, outside cone (|z|>4w+t, {out_sel.sum()} sites) = {dout:.2e}')
        if tp/Tr in (0.5,):
            sel = np.abs(z) <= 3*w
            pr('     profile z: ' + ' '.join(f'{int(zz):+d}' for zz in z[sel][::3]))
            pr('     r_dyn    : ' + ' '.join(f'{v:+.2e}' for v in rdyn[sel][::3]))
            pr('     formula  : ' + ' '.join(f'{v:+.2e}' for v in pred[sel][::3]))
        if tp == ptimes[1]:
            globals().setdefault('mid', {})[Tr] = rdyn[c]
        if tp == ptimes[-1]:
            pr(f'     after ramp: max|r_dyn| (excess above final GS) = {np.abs(rdyn).max():.3e}')
pr(f'\nrate^2 scaling at phase 0.5, centre: r_dyn(Tr=16)/r_dyn(Tr=32) = {mid[16.0]/mid[32.0]:.3f} (local order 2: 4)')
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out)+'\n')
