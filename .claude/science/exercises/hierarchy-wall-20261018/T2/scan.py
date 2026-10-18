import numpy as np, glob, re
rows=[]
for f in sorted(glob.glob('data/scan_L*_b*.bin')):
    L,b=re.findall(r'L(\d+)_b([\d.]+)\.bin',f)[0]; L=int(L); b=float(b); NV=2*L**3
    w=np.fromfile(f).reshape(-1,4); m2=w[:,1]; fk=w[:,3]
    R=np.mean(m2**2)/np.mean(m2)**2
    chi=np.mean(m2)/NV; chik=np.mean(fk)/NV
    xi=np.sqrt(max(chi/chik-1,0))/(2*np.sin(np.pi/L))
    rows.append((L,b,R,xi/L,chi))
for r in sorted(rows): print('L=%2d beta=%.3f R=%.4f xi/L=%.4f chi=%.2f'%r)
