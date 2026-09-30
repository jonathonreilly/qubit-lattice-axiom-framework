import sys,csv,collections,math
files=sys.argv[1:]
rows=[]
for fn in files:
    for line in open(fn):
        f=line.split()
        if len(f)<14: continue
        menu,L,beta,z,g,c,rho,varN,kurt,m2,m2e,U,Ue,cold=f[0],int(f[1]),float(f[2]),float(f[3]),float(f[4]),float(f[5]),float(f[6]),float(f[7]),float(f[8]),float(f[9]),float(f[10]),float(f[11]),float(f[12]),int(f[13])
        rows.append(dict(menu=menu,L=L,beta=beta,z=z,g=g,c=c,rho=rho,varN=varN,kurt=kurt,m2=m2,m2e=m2e,U=U,Ue=Ue,cold=cold))
D=collections.defaultdict(dict)
for r in rows:
    gk='one' if (r['menu']=='s' and abs(r['c']-1)<1e-4 and abs(r['g']-1)>1e-3) else 'g=%.3g'%r['g']
    D[(r['menu'],r['z'],gk)][(r['beta'],r['L'])]=r
for key in sorted(D):
    menu,z,gk=key; d=D[key]
    betas=sorted({b for b,L in d})
    Ls=sorted({L for b,L in d})
    print(f"\n=== menu={menu} z={z:g} scale={gk}   (c/c0 = g;  'one' means c=1)")
    hdr="beta   c      "+"  ".join(f"rho{L:<3d} m2_{L:<3d} U_{L:<3d}     " for L in Ls)+"  U12-U8 (sig)  kurt(rho)"
    print(hdr)
    prev=None; cross=None
    for b in betas:
        cells=[]; 
        for L in Ls:
            r=d.get((b,L))
            cells.append(f"{r['rho']:.3f} {r['m2']:.4f} {r['U']:.3f}±{r['Ue']:.3f}" if r else "   -   ")
        r8=d.get((b,8)); r12=d.get((b,12))
        dU=None; sig=None; ku=None
        if r8 and r12:
            dU=r12['U']-r8['U']; sig=dU/math.sqrt(r12['Ue']**2+r8['Ue']**2+1e-12); ku=min(r8['kurt'],r12['kurt'])
        cr=r8 or r12
        print(f"{b:4.2f} {cr['c']:.4f}  "+"  ".join(cells)+ (f"   {dU:+.3f} ({sig:+.1f})  {ku:.2f}" if dU is not None else ""))
        if dU is not None:
            if prev is not None and prev[1]<0 and dU>=0 and cross is None:
                b0,d0=prev; cross=b0+(b-b0)*(-d0)/(dU-d0)
            prev=(b,dU)
    print("  crossing (U12=U8) at beta_c ~", ("%.2f"%cross) if cross else "none in grid")
