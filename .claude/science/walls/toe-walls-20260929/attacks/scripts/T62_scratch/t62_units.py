"""T62 test U: unit map and accounting.  SI with CODATA 2018 (external, approximate)."""
import numpy as np, itertools
c=299792458.0; hbar=1.054571817e-34; G=6.67430e-11; Mpc=3.0856775814913673e22
lP=np.sqrt(hbar*G/c**3); tP=lP/c; rhoP=c**7/(hbar*G**2)   # J/m^3
def cosmo(H0kms, OL):
    H0=H0kms*1e3/Mpc
    Hinf=np.sqrt(OL)*H0
    Lam=3*Hinf**2/c**2
    RL=c/Hinf
    rho=Lam*c**4/(8*np.pi*G)
    return H0,Hinf,Lam,RL,rho
print("l_P=%.4e m  t_P=%.4e s  rho_P=%.4e J/m^3"%(lP,tP,rhoP))
rows=[]
for H0k in (67.4,73.0):
    for OL in (0.68,0.685,0.70):
        H0,Hinf,Lam,RL,rho=cosmo(H0k,OL)
        rows.append((H0k,OL,RL/lP,Lam*lP**2,8*np.pi*rho/rhoP,3*(lP/RL)**2,rho/rhoP,H0*tP, 1/(H0*tP)))
print("\nU1  Lambda l_P^2 = 8 pi rho/rho_P = 3 (l_P/R_L)^2  (a=l_P)")
print("H0    OmL    R_L/a       Lam*a^2     8pi*rho/rhoP  3(a/R_L)^2   rho/rho_P   H0*a/c   age-ish 1/(H0 tP)")
for r in rows: print("%.1f  %.3f  %.3e  %.3e  %.3e    %.3e   %.3e  %.3e  %.3e"%r)
ok=all(abs(r[3]/r[4]-1)<1e-9 and abs(r[3]/r[5]-1)<1e-9 for r in rows)
print("identity holds to 1e-9 in all rows:",ok, " (tautology of definitions: R_L/a and rho_vac/rho_P are one number)")

H0,Hinf,Lam,RL,rho=cosmo(67.4,0.685)
T_age=13.8e9*3.15576e7/tP
print("\nreference point: R_L/a=%.3e  rho_L/rho_P=%.3e (log10 %.2f)  T_age/t_P=%.3e (13.8 Gyr)"%(RL/lP,rho/rhoP,np.log10(rho/rhoP),T_age))

print("\nU2  qubit counts in one horizon ball vs de Sitter entropy S=pi R^2/l_P^2")
S=np.pi*(RL/lP)**2
Nsites=(4*np.pi/3)*(RL/lP)**3
print("  sites (a=l_P): %.3e   S_dS=%.3e nats (%.3e bits)   excess %.2e = ~R/a"%(Nsites,S,S/np.log(2),Nsites/(S/np.log(2))))
ah=RL*((S/np.log(2))/((4*np.pi/3)))**(-1/3)*1.0   # (4pi/3)(R/a)^3 = S/ln2  => a = R*((4pi/3)/(S/ln2))^(1/3)
ah=RL*((4*np.pi/3)/(S/np.log(2)))**(1/3)
print("  holographic cell a_h with (4pi/3)(R/a_h)^3 = S/ln2:  a_h = %.3e m = %.2f fm  (= %.3e l_P);  (l_P^2 R)^(1/3) = %.3e m"%(ah,ah*1e15,ah/lP,(lP**2*RL)**(1/3)))

print("\nU3  numerology guard: hits of k*alpha^n in the observational band for R_L/a and rho^(1/4)/M_Pl")
aLM=0.0907; abare=1/(4*np.pi); ks=[1,2,3,4,8,16,np.pi,2*np.pi,4*np.pi,8*np.pi,3/(8*np.pi)]
ks=ks+[1/k for k in ks[1:]]
lo=[];hi=[]
for H0k in (67.4,73.0):
    for OL in (0.68,0.70):
        _,_,_,RL_,rho_=cosmo(H0k,OL); lo.append(RL_/lP)
        hi.append((rho_/rhoP)**0.25)
blo,bhi=min(lo),max(lo); rlo,rhi=min(hi),max(hi)
print("  band R_L/a in [%.3e, %.3e] (%.3f decades);  rho^(1/4)/M_P in [%.3e, %.3e] (%.3f decades)"%(blo,bhi,np.log10(bhi/blo),rlo,rhi,np.log10(rhi/rlo)))
for name,band,sgn in (("R_L/a",(blo,bhi),-1),("rho^(1/4)/M_P",(rlo,rhi),+1)):
    hits=[];M=0
    for al,an in ((aLM,'aLM'),(abare,'a_bare=1/4pi')):
        for n in range(1,131):
            for k in ks:
                M+=1
                v=k*al**(sgn*n) if sgn==-1 else k*al**n
                if band[0]<=v<=band[1]: hits.append((an,n,round(float(k),4)))
    span=(130*abs(np.log10(aLM)))
    exp_rand=M*np.log10(band[1]/band[0])/span
    print("  %s: %d hits of %d combos; expected for a random target ~ %.2f  -> %s"%(name,len(hits),M,exp_rand,hits[:6]))
print("  rho^(1/4)/M_P = alpha_LM^n with n = %.3f"%(np.log10((rho/rhoP)**0.25)/np.log10(aLM)))
