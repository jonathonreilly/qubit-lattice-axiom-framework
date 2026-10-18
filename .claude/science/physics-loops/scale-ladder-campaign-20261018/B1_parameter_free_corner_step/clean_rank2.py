exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
import pickle
S=np.load('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/S_110_0.npy')
blS=blocks_from(S); SK=lambda k: Hk(blS,k)
wl,Vl=np.linalg.eigh(Lam)
Qs=[Vl[:,np.abs(wl-l)<1e-6]@Vl[:,np.abs(wl-l)<1e-6].conj().T for l in sorted(set(np.round(wl,6)))]
ph=[1,1j,-1,-1j]
def parse(name):
    U=np.eye(12,dtype=complex)
    for part in name.split("*"):
        if part[0]=="H": a,b=int(part[1]),int(part[2]); M=Ps[0]+ph[a]*Ps[1]+ph[b]*Ps[2]
        else: a,b,c=int(part[1]),int(part[2]),int(part[3]); M=Qs[0]+ph[a]*Qs[1]+ph[b]*Qs[2]+ph[c]*Qs[3]
        U=U@M
    return U
links={"S":SK,"S.RL":lambda k: SK(k)@RL(k),"RL.S":lambda k: RL(k)@SK(k)}
good=pickle.load(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/c20/cube_good.pkl','rb'))
print(len(good),"candidates")
g=np.linspace(-np.pi,np.pi,12,endpoint=False)
G=[np.array(k)+0.11 for k in itertools.product(g,repeat=3)]
G=[k for k in G if min(np.linalg.norm(wrap(k-kst)),np.linalg.norm(wrap(k+kst)))>0.5]
Gk={nm:[f(k) for k in G] for nm,f in links.items()}
res=[]
for lname,name,E,v in good:
    U=parse(name)
    m=min(np.min(np.abs(wrap(np.angle(np.linalg.eigvals(M@U))-E))) for M in Gk[lname])
    res.append((round(m,4),lname,name,E,v))
res.sort(reverse=True)
for r in res[:15]: print(r)
pickle.dump(res,open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/clean_rank2.pkl','wb'))
