exec(open('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/qca/walklib.py').read())
from scipy.linalg import expm
loc=np.array(loc0); reps=[]
for P,s in rots:
    M=np.zeros((nV,nV)); M[P,np.arange(nV)]=(-1.0)**s; reps.append(M[np.ix_(loc,loc)])
def comm_avg(A): return sum(R@A@R.T for R in reps)/24
rng=np.random.default_rng(9)
def rU():
    A=rng.normal(size=(12,12))+1j*rng.normal(size=(12,12)); return expm(1j*comm_avg(A+A.conj().T))
U1,U2=rU(),rU()
analyse(lambda k: RL(k)@U1@RL(k)@U2,"RL U1 RL U2 (random symmetric on-site)")
# Hamiltonian analogue: H0 + random on-site symmetric complex term
Hc=comm_avg(rng.normal(size=(12,12))+1j*rng.normal(size=(12,12))); Hc=Hc+Hc.conj().T
f=lambda k: Hk(blon,k)*(-1)+0.2*(-1)*Hk(blli,k)+0.3*Hc
e=np.linalg.eigvalsh(f(kst)); print("H0+onsite: k* levels",np.round(e,4))
for i in range(0,12):
    if i+1<12 and abs(e[i+1]-e[i])<1e-8 and (i==0 or abs(e[i]-e[i-1])>1e-8) and (i+2>=12 or abs(e[i+2]-e[i])>1e-8):
        S=[]
        for d in DIRS[:20]:
            ee=np.linalg.eigvalsh(f(kst+1e-3*d)); S.append((ee[i+1]-ee[i])/2e-3)
        print("   doublet at",round(e[i],4),"half-split/q",round(np.mean(S),6))
