# R13-2 s4c: assemble the pre-registered collapse fit from the HMC outputs, using for each (point, L) the run with
# acceptance >= 0.5 (runs with acceptance < 0.5 are listed and excluded).
import re, glob, numpy as np
runs={}
for f in sorted(glob.glob('rejected_acc0/s4_hmc_*.out')+glob.glob('s4_hmc_*_dt015.out')):
    txt=open(f).read().split('\n'); i=0
    while i<len(txt):
        m=re.match(r'L=(\d+) beta_t=([\d.]+)',txt[i])
        if m and i+1<len(txt) and 'acc=' in txt[i+1]:
            L=int(m.group(1)); bt=float(m.group(2)); acc=float(re.search(r'acc=([\d.]+)',txt[i+1]).group(1))
            vals={}
            for j in range(2,7):
                mm=re.match(r'\s+(\w+)\s*: m\^2=([-\d.]+)\+-([\d.]+).*=([-\w.]+)$',txt[i+j])
                vals[mm.group(1)]=(float(mm.group(2)),float(mm.group(3)),float(mm.group(4)) if mm.group(4)!='nan' else np.nan)
            point={4.0:'weak',1.0:'mid',0.4:'strong'}[bt]
            print(f"{f:40s} {point:6s} L={L} acc={acc:.2f} "+' '.join(f"{k}:m2={v[0]:+.4f}({v[1]:.4f}),Om={v[2]:.3f}" for k,v in vals.items()))
            if acc>=0.5:
                if (point,L) not in runs or runs[(point,L)][0]<acc: runs[(point,L)]=(acc,vals,f)
            i+=7
        else: i+=1
print("\ncollapse fit z = slope log Omega_eff(2pi/L) vs log(2pi/L), accepted runs only:")
for point in ('weak','mid','strong'):
    Ls=sorted(L for (p,L) in runs if p==point)
    line=[]
    for ch in ('B1','B2','E','A1a','A1t'):
        Om=np.array([runs[(point,L)][1][ch][2] for L in Ls])
        ok=np.isfinite(Om)&(Om>0)
        if ok.sum()>=3: z=np.polyfit(np.log(2*np.pi/np.array(Ls)[ok]),np.log(Om[ok]),1)[0]; line.append(f"{ch}: z={z:+.2f} Om={np.round(Om,3).tolist()}")
        else: line.append(f"{ch}: no fit (Om={np.round(Om,3).tolist()})")
    print(f"  {point:6s} L={Ls}: "+'; '.join(line))
