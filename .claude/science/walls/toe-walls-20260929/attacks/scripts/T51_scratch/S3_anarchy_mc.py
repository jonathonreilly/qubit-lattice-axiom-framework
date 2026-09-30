"""T51 S3 (outside route, random-matrix 'anarchy'): universal Y => m_nu = c M_R^{-1}.
Take M_R complex symmetric with iid complex Gaussian entries (unitary-invariant Takagi ensemble),
masses = 1/singular values of M_R, sorted; normalise the LARGEST mass to m3 = sqrt(2.5e-3) eV.
Report distribution of R = (m2^2-m1^2)/(m3^2-m1^2) and joint tails."""
import numpy as np
rng = np.random.default_rng(510)
N = 400_000
def sample(kind):
    if kind=='complex':
        X = rng.normal(size=(N,3,3)) + 1j*rng.normal(size=(N,3,3))
    else:
        X = rng.normal(size=(N,3,3)).astype(complex)
    M = (X + np.transpose(X,(0,2,1)))/np.sqrt(2)           # symmetric
    s = np.linalg.svd(M, compute_uv=False)                  # descending singular values
    m = 1.0/s                                               # masses: smallest sing. value -> largest mass
    m = np.sort(m, axis=1)                                  # ascending m1<m2<m3
    m = m / m[:,2:3] * np.sqrt(2.5e-3)                      # normalise atmospheric scale
    return m
SOL=(6.92e-5,8.05e-5); RAT=(0.0268,0.0328)
for kind in ['complex','real']:
    m = sample(kind)
    m1,m2,m3 = m.T
    dm21=m2**2-m1**2; dm31=m3**2-m1**2; R=dm21/dm31; S=m1+m2+m3
    inR=(R>=RAT[0])&(R<=RAT[1]); inS=S<0.072
    print(f'[{kind}] N={N}: median R={np.median(R):.3f}; P(R<=0.0328)={np.mean(R<=0.0328):.3f}; P(R in window)={inR.mean():.4f}; '
          f'P(Sigma<72 meV)={inS.mean():.3f}; P(R in window & Sigma<72)={(inR&inS).mean():.4f}; median Sigma={np.median(S)*1e3:.1f} meV; '
          f'P(R in window | both fixed atmospheric 50.0 meV)= same by normalisation')
    # width of window relative to per-log-R density: how informative is landing in it?
    print('   quantiles of R (5,25,50,75,95%):', np.round(np.quantile(R,[.05,.25,.5,.75,.95]),4))
    print('   quantiles of Sigma meV:', np.round(np.quantile(S,[.05,.25,.5,.75,.95])*1e3,1))

# where does the lane's retained benchmark sit in this ensemble?
m = sample('complex'); m1,m2,m3 = m.T
R = (m2**2-m1**2)/(m3**2-m1**2)
print('P(R >= 0.8328) in complex ensemble =', np.mean(R>=0.8328), ' (lane benchmark R)')
# spectrum shape: fraction of ensemble with m1/m3 <= 0.0866 (benchmark m1/m3) and m2/m3>=0.913 (near-degenerate top pair)
print('P(m2/m3 >= 0.913) =', np.mean(m2/m3>=0.913))
