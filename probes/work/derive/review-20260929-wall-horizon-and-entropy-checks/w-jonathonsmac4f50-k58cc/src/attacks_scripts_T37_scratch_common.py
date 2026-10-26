"""Shared helpers for the T37 attack. Reads (never edits) the repo runner to reuse its comparator RG."""
import io, contextlib, math, sys
import numpy as np
REPO = "/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/main_wt"
RUNNER = REPO + "/scripts/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.py"

def load_runner():
    g = {"__file__": RUNNER, "__name__": "repo_runner"}
    src = open(RUNNER).read()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        exec(compile(src, RUNNER, "exec"), g)
    return g

def Qf(m):
    m = np.asarray(m, float); x = np.sqrt(m); return m.sum() / x.sum() ** 2
def rf(m):
    return (3 * Qf(m) - 1) / 2
def delta_lep_convention(m):
    """Brannen phase in the lepton convention: x_k = a(1 + A cos theta_k), A = sqrt(2 r), heaviest at
    theta = delta (0 <= delta <= pi/3), lightest at delta + 2 pi/3."""
    x = np.sqrt(np.sort(np.asarray(m, float))[::-1])
    a = x.sum() / 3; r = rf(m); A = 2 * math.sqrt(r)
    c = (x[0] / a - 1) / A
    return math.acos(max(-1, min(1, c)))
M_LEP_POLE = np.array([0.5109989461, 105.6583745, 1776.86])  # MeV
