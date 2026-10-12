"""K5: tree-level one-cone support. Per configuration (3D periodic Poisson-Delaunay, circumcentric weights from
R1 check D, read-only import), test (i) sum_e w_e e e^T = V I  (scalar / electric star exact on constant fields) and
(ii) (L x)_i = 0 for linear functions (discrete harmonic => no homogenization corrector => c = 1 at k -> 0)."""
import numpy as np, sys
REPO = "/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/toe-leverage-analysis-e8a790/.claude/science/exercises/gravity-current-state-20261009/scripts/"
srcB = open(REPO + "R1_B_liquid_glass_crystal.py").read().split("which = sys.argv")[0]
ns = {}; exec(srcB, ns)
srcD = open(REPO + "R1_D_3d_circumcentric.py").read().split("if sys.argv[1:]")[0]
srcD = srcD.replace('src = open("B_liquid_glass_crystal.py").read().split("which = sys.argv")[0]', 'src = ""').replace("ns = {}; exec(src, ns)", "")
srcD = srcD.replace("periodic_delaunay, expm_sym = ns[\"periodic_delaunay\"], ns[\"expm_sym\"]", ""); exec(srcD, ns)
rng = np.random.default_rng(5)
for N in (300, 600):
    L = N**(1/3); A0 = L*np.eye(3); X = rng.uniform(0, L, (N, 3))
    vid, voff = ns["periodic_delaunay"](X, A0)
    K, W = ns["dec_laplacian"](X, A0, vid, voff)
    # edge vectors: rebuild from simplices (minimum image is safe at this density)
    T = np.zeros((3, 3)); Lx = np.zeros((N, 3))
    I, J = np.nonzero(np.triu(W, 1))
    D = X[J] - X[I]; D -= L*np.round(D/L)
    w = W[I, J]
    T = np.einsum('p,pi,pj->ij', w, D, D)
    np.add.at(Lx, I, w[:, None]*D); np.add.at(Lx, J, -w[:, None]*D)
    print(f"N={N}: sum_e w e e^T / V =\n{np.round(T/L**3, 12)}\n  max |(L x)_i| = {np.abs(Lx).max():.2e}")
