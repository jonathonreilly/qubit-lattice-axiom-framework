"""T47 Test A: infinite-volume ladder of the Route-2 readout. Imports the repo runner read-only.
Speed-up: cache the cubic-spline prefilter of each phi grid (numerically identical to map_coordinates(order=3, mode='nearest'))."""
import sys, math, time
sys.dont_write_bytecode = True
MAIN='/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt/scripts'
sys.path.insert(0, MAIN)
import numpy as np
from scipy.ndimage import map_coordinates, spline_filter
import frontier_quark_route2_honest_gravity_metric_rhoe_characterization as rh
tcomp = rh.tcomp

_cache = {'id': None, 'ref': None, 'coef': None}
def fast_interp(phi_grid, point_xyz):
    if _cache['ref'] is not phi_grid:
        _cache['ref'] = phi_grid
        padded = np.pad(phi_grid, 12, mode='edge')
        _cache['coef'] = spline_filter(padded, 3, output=np.float64, mode='nearest')
    center = (phi_grid.shape[0] - 1) / 2.0 + 12
    coords = np.array([[center + point_xyz[0]], [center + point_xyz[1]], [center + point_xyz[2]]], dtype=float)
    return float(map_coordinates(_cache['coef'], coords, order=3, mode='nearest', prefilter=False)[0])
tcomp.interpolated_phi = fast_interp

# --- fast exact Dirichlet Poisson solver (DST-I), replacing SuperLU on the sparse Laplacian ---
from scipy.fft import dstn, idstn
import frontier_same_source_metric_ansatz_scan as same
_LAM = {}
def _lam(n):
    if n not in _LAM:
        k = np.arange(1, n+1)
        l1 = 2.0*(1.0 - np.cos(np.pi*k/(n+1)))
        _LAM[n] = l1[:,None,None] + l1[None,:,None] + l1[None,None,:]
    return _LAM[n]
def dst_solve(f):          # f: (n,n,n) interior source; returns u with -Lap u = f, zero Dirichlet outside
    n = f.shape[0]
    return idstn(dstn(f, type=1)/_lam(n), type=1)
def build_size_system_fast(size):
    interior = size - 2
    center = interior // 2
    support = [same.flat_idx(center + v[0], center + v[1], center + v[2], interior) for v in same.SUPPORT_COORDS]
    cols = []
    for site in support:
        f = np.zeros(interior**3); f[site] = 1.0
        cols.append(dst_solve(f.reshape(interior,interior,interior)).reshape(-1))
    g0p = np.column_stack(cols)
    return rh.SizeSystem(size=size, interior=interior, support=support, g0p=g0p, gs=g0p[support, :])
rh.build_size_system = build_size_system_fast
def solve_from_source_fast(source_grid):
    out = np.zeros_like(source_grid)
    out[1:-1,1:-1,1:-1] = dst_solve(source_grid[1:-1,1:-1,1:-1])
    return out
rh.shell_replay.solve_from_source = solve_from_source_fast


def tf_spatial(einstein):
    sp = einstein[1:,1:]
    return sp - np.eye(3)*np.trace(sp)/3.0

def make(variant, radius):
    def base(phi_grid):
        vals=[]
        for point in rh.probe_points(radius):
            _, ein = tcomp.ricci_and_einstein(
                lambda p: tcomp.adm_metric(phi_grid, p, eps_vec=0.0, eps_ten=0.0, omega=0.0),
                point, h=rh.RICCI_H)
            tf = tf_spatial(ein)
            if variant=='xx_probe0_signed': vals.append(tf[0,0])
            elif variant=='frob_probe0': vals.append(np.linalg.norm(tf))
            else: vals.append(float(np.max(np.abs(tf))))
        if variant in ('xx_probe0_signed','frob_probe0'): return float(vals[0])
        return float(max(vals))
    return base

def row(size, variant, radius=4.25):
    rh.ETA_CACHE.clear(); rh.ANCHOR_CACHE.clear()
    rh.base_eta_floor = make(variant, radius)
    r = rh.compute_row(size)
    return dict(N=size, qT=r.gamma_t_center/r.gamma_t_shell, sTE=r.gamma_t_shell/r.gamma_e_shell,
                rhoE=r.rho_e, qE=r.q_e, gTc=r.gamma_t_center, gTs=r.gamma_t_shell, gEc=r.gamma_e_center, gEs=r.gamma_e_shell)

if __name__=='__main__':
    which = sys.argv[1]
    sizes = [int(x) for x in sys.argv[2].split(',')]
    radius = float(sys.argv[3]) if len(sys.argv)>3 else 4.25
    for s in sizes:
        t=time.time()
        d=row(s, which, radius)
        print(f"{which:18s} R={radius:5.2f} N={d['N']:3d} qT={d['qT']:+.5f} sTE={d['sTE']:+.5f} rhoE={d['rhoE']:+.4f} qE={d['qE']:+.5f} gTc={d['gTc']:+.4e} gTs={d['gTs']:+.4e} gEc={d['gEc']:+.4e} gEs={d['gEs']:+.4e} [{time.time()-t:.0f}s]", flush=True)
