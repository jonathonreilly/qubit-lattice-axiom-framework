from pathlib import Path
p=Path('/Users/jonreilly/Documents/Codex/toe-native-local-law-20260913/.claude/science/physics-loops/toe-native-local-law-20260913')
wt=Path('/Users/jonreilly/Documents/Codex/toe-flat-holonomy-spectral-floor-20260913')
exact=(p/'check_block15_exact_twist.py').read_text().split('zero=energy_interval(False)')[0]
ring=(p/'block15_holonomy_explore.py').read_text().split('rows=[]')[0]
carrier=(p/'block15_carrier_twists.py').read_text().split('rows=[]')[0]
extra='''

def square_and_metric_checks():
    import sympy as sy
    a,b,c,d,m,n,y=sy.symbols('a b c d m n y',real=True)
    one=sy.eye(2);x=sy.Matrix([[0,1],[1,0]]);yy=sy.Matrix([[0,-sy.I],[sy.I,0]]);z=sy.diag(1,-1)
    sx,syy,sz=[sy.kronecker_product(one,v) for v in [x,yy,z]]
    tx0,ty0,tz0=[sy.kronecker_product(v,one) for v in [x,yy,z]]
    h=(a*sy.eye(4)+b*tz0+m*tx0)*sx+y*syy+(c*sy.eye(4)+d*tz0+n*tx0)*sz
    scalar=y*y+a*a+b*b+c*c+d*d+m*m+n*n
    expected=scalar*sy.eye(4)+2*(a*b+c*d)*tz0+2*(a*m+c*n)*tx0+2*(b*n-d*m)*syy*ty0
    check((h*h-expected).applyfunc(sy.expand)==sy.zeros(4),'exact symbolic mixed-carrier square')
    check((syy*h.conjugate()*syy+h).applyfunc(sy.expand)==sy.zeros(4),'exact spectral anti-symmetry')
    gammas=[tz0,tx0,syy*ty0]
    for gamma in gammas:check(gamma*gamma==sy.eye(4),'Clifford square')
    for i in range(3):
        for j in range(i):check(gammas[i]*gammas[j]+gammas[j]*gammas[i]==sy.zeros(4),'Clifford anticommutator')
    K=sy.Matrix([[4,4],[4,8]]);A=sy.diag(1,0);L=sy.Matrix([[1,0],[-1,1]])
    check(L*K*L.T==4*sy.eye(2),'mixed normal/tangent metric diagonalization')
    check((K*A).eigenvals()=={sy.Integer(4):1,sy.Integer(0):1},'correct rank-one normal frequency')
    check(K[0,0]-K[0,1]**2/K[1,1]==2,'wrong Schur normal coefficient differs from 4')


def run_checks():
    square_and_metric_checks()
    zero=energy_interval(False);twist=energy_interval(True)
    difference=(twist[0]-zero[1],twist[1]-zero[0])
    check(difference[1]<Q(-14424,10000),'strict actual-carrier twist improvement')
    check(difference[0]>Q(-14425,10000),'strict actual-carrier difference lower bracket')
    for phi,interval in [([0,0,0],zero),([0,np.pi,0],twist)]:
        direct=direct_energy(phi,3);bloch_value=band_energy(phi,3)
        check(abs(direct-bloch_value)<1e-10,'independent full site versus Bloch spectrum')
        check(abs(direct-float(interval[0]))<1e-10,'site matrix versus exact radical certificate')
    for theta in np.linspace(0,2*np.pi,17):
        check(abs(free(theta)+2*(np.cos(theta/4)+np.sin(theta/4)))<2e-12,
              'direct ring one-particle matrix versus analytic filled-band energy')
    # Separate six-dimensional CAR construction checks the ring Fourier potential.
    for theta in [0,.71,np.pi,5.1]:
        annihilators=[]
        for j in range(4):
            op=np.zeros((16,16))
            for f in range(16):
                if f>>j&1:op[f^(1<<j),f]=(-1)**sum((f>>k)&1 for k in range(j))
            annihilators.append(op)
        many=np.zeros((16,16),complex)
        for j in range(4):
            term=annihilators[j].T@annihilators[(j+1)%4]*np.exp(1j*theta*(j==3))
            many+=term+term.conj().T
        check(abs(np.linalg.eigvalsh(many[np.ix_(states,states)])[0]-free(theta))<2e-12,
              'direct six-state CAR potential versus free filled spectrum')
    samples=[]
    for g in [.2,.05,.01]:
        S=int(np.ceil((3+np.log(1/g))/np.sqrt(g)))
        H,W=matrix(g,S);e,v=eigsh(H,k=4,which='SA',tol=2e-12)
        order=np.argsort(e);e=e[order];v=v[:,order]
        check(e[0]>=-2*np.sqrt(2)-1e-10,'positive electric lower bound on ring ground')
        samples.append(dict(g=g,S=S,levels=e.tolist(),loop_real=float(v[:,0]@(W@v[:,0])),
                            correction_over_g=float((e[0]+2*np.sqrt(2))/g),gap_over_g=float((e[1]-e[0])/g)))
    check(abs(samples[-1]['levels'][0]+2*np.sqrt(2))<.005,'sampled ring minimum limit')
    check(samples[-1]['levels'][3]-samples[-1]['levels'][0]<.026,'sampled low-level accumulation')
    check(samples[-1]['loop_real']<-.98,'sampled loop concentration at pi')
    check(abs(samples[-1]['correction_over_g']-2**(-5/4))<.004,'formal ground coefficient numerical challenge only')
    check(abs(samples[-1]['gap_over_g']-2**(-1/4))<.001,'formal slow-gap coefficient numerical challenge only')
    print('EXACT_TWIST',json.dumps(dict(identity_interval=list(map(str,zero[:2])),twist_interval=list(map(str,twist[:2])),difference_interval=list(map(str,difference)))))
    print('RING',json.dumps(samples))
    for label,message in [
        ('per_element','exact radical square-root brackets and flat-link phases checked; no chosen coupling derived'),
        ('per_site','direct site matrix and independent finite CAR actions checked'),
        ('per_mode','ring energy branches, normal metric coefficient and sampled slow levels checked'),
        ('per_block','strict 3-cubed actual-carrier flat-twist comparison certified with integer arithmetic'),
        ('lattice_wide','finite-graph localization proof proposed; no uniform growing-volume phase or payload rate established')]:print(label+': '+message)
    print(f'TOTAL: PASS={checks} FAIL=0')


if __name__=='__main__':run_checks()
'''
target=wt/'scripts/flat_holonomy_minimization_and_periodic_spectral_floor_2026_09_13.py'
target.write_text(exact+'\n'+ring+'\n'+carrier+'\n'+extra)
print(target)
