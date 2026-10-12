"""L3 check 4: classical lattice phi^4 on a periodic Z^3 box. Total energy current
 J_j = -1/2 sum_x (phi_{x+e_j}-phi_x)(pi_x+pi_{x+e_j})   (exact: J = d/dt sum_x x h_x, derived in report)
Free (lam=0): J conserved exactly. Interacting: does <J(t).J(0)>/<J^2> decay to 0 (zero Drude weight)?
If it decays, no conserved P = J + {H,W} (W local, extensive) with <P J> != 0 exists (Mazur), so no
first-class lapse+shift coupling to H_N (which needs P proportional to J + {H,W}) -- see report."""
import numpy as np, sys
rng = np.random.default_rng(1)
L = 8; m2 = 0.5; dt = 0.02
def force(phi, lam):
    lap = sum(np.roll(phi,1,a)+np.roll(phi,-1,a)-2*phi for a in range(3))
    return lap - m2*phi - lam*phi**3
def Jtot(phi, pi):
    return np.array([-0.5*np.sum((np.roll(phi,-1,a)-phi)*(pi+np.roll(pi,-1,a))) for a in range(3)])
def energy(phi, pi, lam):
    grad = sum(0.5*(np.roll(phi,-1,a)-phi)**2 for a in range(3))
    return np.sum(0.5*pi**2 + 0.5*m2*phi**2 + 0.25*lam*phi**4 + grad)
def run(lam, T=1.0, ntraj=12, teq=40.0, tmax=60.0):
    nmeas = int(tmax/dt); C = np.zeros(nmeas); J0sq = 0.0; drift = 0.0
    for t_ in range(ntraj):
        # free-field thermal sample in k space
        k = 2*np.pi*np.fft.fftfreq(L)
        KX,KY,KZ = np.meshgrid(k,k,k,indexing='ij')
        w2 = m2 + 4*(np.sin(KX/2)**2+np.sin(KY/2)**2+np.sin(KZ/2)**2)
        phik = np.fft.fftn(rng.normal(size=(L,L,L)))*np.sqrt(T/w2)
        phi = np.real(np.fft.ifftn(phik)); pi = rng.normal(size=(L,L,L))*np.sqrt(T)
        f = force(phi, lam)
        for s in range(int(teq/dt)):   # equilibrate
            pi += 0.5*dt*f; phi += dt*pi; f = force(phi, lam); pi += 0.5*dt*f
        E0 = energy(phi, pi, lam); J0 = Jtot(phi, pi); J0sq += J0@J0
        for s in range(nmeas):
            C[s] += Jtot(phi, pi)@J0
            pi += 0.5*dt*f; phi += dt*pi; f = force(phi, lam); pi += 0.5*dt*f
        drift = max(drift, abs(energy(phi,pi,lam)-E0)/abs(E0))
    C /= J0sq
    tt = np.arange(nmeas)*dt
    run_avg = np.cumsum(C)/np.arange(1,nmeas+1)
    return tt, C, run_avg, drift
for lam in (0.0, 0.5, 2.0):
    tt, C, ra, drift = run(lam)
    pick = [int(x/dt)-1 for x in (1, 5, 10, 20, 40, 60)]
    print(f"lam={lam}: C(t)=<J(t)J(0)>/<J^2> at t=1,5,10,20,40,60: {np.round(C[pick],3)} ; "
          f"time-average over [0,60]: {ra[-1]:.3f} ; avg over [30,60]: {np.mean(C[int(30/dt):]):.3f} ; max rel energy drift {drift:.1e}")
