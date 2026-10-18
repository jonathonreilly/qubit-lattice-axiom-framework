import pickle
exec(open('b18lib.py').read())
res=pickle.load(open('doubler_iso_scan.pkl','rb'))
iso=[r for r in res for l in ("D+x","D-x") if r[l][0]==2 and not np.any(np.isnan(r[l][1])) and min(r[l][1])>1e-3 and abs(r[l][1][0]-r[l][1][1])<1e-4]
print(len(iso),"records with an isotropic doubler; examples:",[(r['link'],r['U'],r['E']) for r in iso[:6]])
def parse(un):
    U=np.eye(12,dtype=complex)
    for part in un.split("*"):
        U=U@(UHf(int(part[1]),int(part[2])) if part[0]=="H" else ULf(int(part[1]),int(part[2]),int(part[3])))
    return U
links={"S":SK,"S.RL":lambda k: SK(k)@RL(k),"RL.S":lambda k: RL(k)@SK(k)}
r=iso[0]; U=parse(r['U']); W=lambda k: links[r['link']](k)@U; E=r['E']
rng=np.random.default_rng(1); dd=rng.normal(size=(40,3)); dd/=np.linalg.norm(dd,axis=1)[:,None]
for lab,k0 in (("k*",kst),("D+x",kst+np.pi*EX[0]),("D-x",-kst+np.pi*EX[0])):
    for q in (4e-3,2e-3,1e-3):
        s=[]
        for d in dd:
            ee=wrap(np.angle(np.linalg.eigvals(W(k0+q*d)))-E); ee=np.sort(ee[np.abs(ee)<0.05]); s.append((ee[-1]-ee[0])/(2*q) if len(ee)==2 else np.nan)
        s=np.array(s); print(lab,q,"mean",np.nanmean(s),"spread",np.nanmax(s)-np.nanmin(s),"n2",np.sum(~np.isnan(s)))
print("levels k*",[(round(x,4),m) for x,m in levels(W,kst)]); print("levels D+x",[(round(x,4),m) for x,m in levels(W,kst+np.pi*EX[0])])
