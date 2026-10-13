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


import sys
for (A, w, Tr) in [(0.10, 1e9, 16.0), (0.10, 10.0, 16.0), (0.10, 10.0, 32.0)]:
    phases = [0.25, 0.5, 0.75]; ptimes = [ph*Tr for ph in phases]
    rec, rho0, afun = run(A, w, Tr, 0.75*Tr, 0.05, ptimes)
    pr(f'\n=== variant A={A}, w={w}, Tr={Tr} ===')
    for tp in ptimes:
        rho, a = rec[tp]; h = 1e-4; Hloc = (np.log(afun(tp+h)) - np.log(afun(tp-h)))/(2*h)
        rdyn = rho - rho_gs(a); pred = inv*Hloc**2/(4*a**2); c = Nz//2
        Hd = (np.log(afun(tp+h)) - 2*np.log(afun(tp)) + np.log(afun(tp-h)))/h**2
        pr(f'  phase {tp/Tr:4.2f}: r_dyn(centre) = {rdyn[c]:+.4e}, H^2 formula {pred[c]:+.4e}, ratio {rdyn[c]/pred[c]:.4f}; Hdot(centre)/a^2 = {Hd[c]/a[c]**2:+.3e}; (r_dyn-pred)/(Hdot/a^2) = {(rdyn[c]-pred[c])/(Hd[c]/a[c]**2):+.4e}')
open('r1917_dynamic_variants.out', 'w').write('\n'.join(out)+'\n')
