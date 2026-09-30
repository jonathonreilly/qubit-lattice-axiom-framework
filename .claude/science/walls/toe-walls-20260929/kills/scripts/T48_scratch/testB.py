import numpy as np, json
from scipy.optimize import brentq
from common import *

def K0(phi):
    b = np.exp(1j*phi)
    K = np.zeros((3,3), complex)
    K[0,1]=b; K[1,0]=np.conj(b); K[1,2]=b; K[2,1]=np.conj(b); K[2,0]=b; K[0,2]=np.conj(b)
    return K

def U_of(diag, kappa, phi):
    H = np.diag(diag).astype(complex) + kappa*K0(phi)
    w, U = eig_sorted(H)   # sort by |eigenvalue|
    return w, U

def ckm_add(sname, p, kappa, phi):
    mu = np.array(MASSES[sname]["u"])**p; md = np.array(MASSES[sname]["d"])**p
    wu, Uu = U_of(mu, kappa, phi); wd, Ud = U_of(md, kappa, phi)
    a, J = ckm_from(Uu, Ud)
    return a, J, wu, wd

def theta_e(sname, p, kappa, phi):
    me = np.array(MASSES[sname]["e"])**p
    w, U = U_of(me, kappa, phi)
    a = np.abs(U)   # rows = corner (e,mu,tau flavour axes), cols = mass eigenstates
    th12 = np.degrees(np.arcsin(a[0,1]/np.sqrt(a[0,0]**2+a[0,1]**2)))
    return th12, a, w

out = {}
for sname in ("MZ","LOW"):
    for p in (1.0, 0.5):
        for phi_deg in (0, 30, 60, 90, 120):
            phi = np.radians(phi_deg)
            # fit kappa to |V_us| on the first branch (smallest kappa reaching Vus)
            ks = np.geomspace(1e-3*np.array(MASSES[sname]["d"])[1]**p, 5*np.array(MASSES[sname]["d"])[1]**p, 4000)
            vus = np.array([ckm_add(sname,p,k,phi)[0][0,1] for k in ks])
            idx = np.where(np.diff(np.sign(vus-OBS["Vus"])) != 0)[0]
            if len(idx)==0:
                print(sname,p,phi_deg,"no kappa reaches Vus"); continue
            i = idx[0]
            kappa = brentq(lambda k: ckm_add(sname,p,k,phi)[0][0,1]-OBS["Vus"], ks[i], ks[i+1])
            a, J, wu, wd = ckm_add(sname,p,kappa,phi)
            th12, ae, we = theta_e(sname,p,kappa,phi)
            # implied neutrino scale if nu is K-dominated: eigenvalues of kappa*K0 -> masses kappa^2*|lambda|^(1/p) (MeV units) with p=1/2 -> lambda^2
            lam = np.linalg.eigvalsh(kappa*K0(phi))
            mnu_MeV = np.abs(lam)**(1.0/p)
            sin13sq = (np.sin(np.radians(th12))**2)/2
            rec = dict(kappa=float(kappa), Vus=float(a[0,1]), Vcb=float(a[1,2]), Vub=float(a[0,2]), J=float(J),
                       Vcb_ratio=float(a[1,2]/OBS["Vcb"]), Vub_ratio=float(a[0,2]/OBS["Vub"]),
                       theta_e12_deg=float(th12), s13sq_TM2=float(sin13sq), Ue_row1=[float(x) for x in ae[0]],
                       nu_mass_scale_MeV=[float(x) for x in mnu_MeV], nu_scale_over_0p05eV=float(np.max(mnu_MeV)*1e6/0.05))
            out[f"{sname}_p{p}_phi{phi_deg}"] = rec
            print(f"{sname} p={p} phi={phi_deg:3d}: kappa={kappa:.4g}  Vus={a[0,1]:.4f} Vcb={a[1,2]:.4f} (x{a[1,2]/OBS['Vcb']:.2f}) Vub={a[0,2]:.4f} (x{a[0,2]/OBS['Vub']:.1f}) J={J:.2e}"
                  f"  theta_e12={th12:.2f} deg  s13^2(TM2)={sin13sq:.4f}  nu scale ~ {np.max(mnu_MeV):.3g} MeV = {np.max(mnu_MeV)*1e6/0.05:.2g} x 0.05 eV")
json.dump(out, open("testB_results.json","w"), indent=1)
