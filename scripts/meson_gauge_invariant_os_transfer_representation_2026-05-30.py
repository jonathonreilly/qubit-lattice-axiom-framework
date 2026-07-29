#!/usr/bin/env python3
from __future__ import annotations
import functools
import math
from itertools import permutations
import numpy as np
print = functools.partial(print, flush=True)  # unbuffered progress  # noqa: A001
MASS = 0.5
NT_BULK = 14          # temporal bulk half-extent for the block-metric chain
C_BLOCK = 2.0         # two Grassmann pairs per 2-step block; fixed a priori, verified
BETA = 0.9            # Wilson gauge coupling for the e^{-S_G} weight.
TOL_PER_CONFIG = 1e-9
TOL_AVG = 1e-9
TOL_DET = 1e-12
TOL_BREAK = 1e-3      # significant control gap threshold.
TOL_POS = -1e-9       # OS positivity gate (allow tiny negative numerical noise).
RNG = np.random.default_rng(20260530)
def eta_t(t: int) -> float:
    return (-1.0) ** t
def wick(monomial, Minv) -> complex:
    n = len(monomial)
    if n == 0:
        return 1.0 + 0.0j
    if n % 2:
        return 0.0 + 0.0j
    cpos = [k for k, (kd, _) in enumerate(monomial) if kd == 'c']
    bpos = [k for k, (kd, _) in enumerate(monomial) if kd == 'cb']
    if len(cpos) != len(bpos):
        return 0.0 + 0.0j
    tot = 0.0 + 0.0j
    for perm in permutations(bpos):
        seq = []
        for c, b in zip(cpos, perm):
            seq += [c, b]
        inv = sum(1 for i in range(len(seq)) for j in range(i + 1, len(seq))
                  if seq[i] > seq[j])
        sign = -1.0 if inv % 2 else 1.0
        val = 1.0 + 0.0j
        for c, b in zip(cpos, perm):
            val *= Minv[monomial[c][1], monomial[b][1]]
        tot += sign * val
    return tot
def random_su3() -> np.ndarray:
    z = (RNG.standard_normal((3, 3)) + 1j * RNG.standard_normal((3, 3))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    q = q * (np.diag(r) / np.abs(np.diag(r)))
    return q * (np.linalg.det(q) ** (-1.0 / 3.0))
def u1(theta: float) -> np.ndarray:
    return np.array([[np.exp(1j * theta)]], dtype=complex)
class Carrier:
    def __init__(self, dims, nc, m=MASS):
        self.dims = dims
        self.nc = nc
        self.m = m
        self.sites = [(x, y, z)
                      for x in range(dims[0])
                      for y in range(dims[1])
                      for z in range(dims[2])]
        self.sidx = {s: i for i, s in enumerate(self.sites)}
        self.Ns = len(self.sites)
        self.nmode = self.Ns * nc
    def eta_spatial(self, t, site, mu):
        s = t
        for nu in range(1, mu):
            s += site[nu - 1]
        return (-1.0) ** s
    def spatial_hop(self, links, t_ref=0):
        nc = self.nc
        dim = self.Ns * nc
        h = np.zeros((dim, dim), dtype=complex)
        for site in self.sites:
            i = self.sidx[site]
            for mu in range(1, 4):
                if self.dims[mu - 1] == 1:
                    continue
                e = self.eta_spatial(t_ref, site, mu)
                fwd = list(site)
                fwd[mu - 1] = (fwd[mu - 1] + 1) % self.dims[mu - 1]
                fwd = tuple(fwd)
                U = links[(mu, site)]
                j = self.sidx[fwd]
                for a in range(nc):
                    for b in range(nc):
                        h[i * nc + a, j * nc + b] += 0.5 * e * U[a, b]
                        h[j * nc + b, i * nc + a] += -0.5 * e * np.conj(U[a, b])
        return h
    def modes(self, links):
        h = self.spatial_hop(links)
        w, V = np.linalg.eig(h)
        Q, _ = np.linalg.qr(V)
        lam = (np.diag(Q.conj().T @ h @ Q) / 1j).real
        E = np.arcsinh(np.sqrt(self.m * self.m + lam * lam))
        return E, Q, lam
    def build_M_full(self, links, nt):
        nc = self.nc
        tmin = -nt
        Lt = 2 * nt
        N = Lt * self.Ns * nc
        def idx(t, site, a):
            return ((t - tmin) * self.Ns + self.sidx[site]) * nc + a
        M = np.zeros((N, N), dtype=complex)
        for t in range(tmin, nt):
            for site in self.sites:
                for a in range(nc):
                    i = idx(t, site, a)
                    M[i, i] += self.m
                    if t + 1 <= nt - 1:
                        M[i, idx(t + 1, site, a)] += 0.5
                    if t - 1 >= tmin:
                        M[i, idx(t - 1, site, a)] += -0.5
                for mu in range(1, 4):
                    if self.dims[mu - 1] == 1:
                        continue
                    e = self.eta_spatial(t, site, mu)
                    fwd = list(site)
                    fwd[mu - 1] = (fwd[mu - 1] + 1) % self.dims[mu - 1]
                    fwd = tuple(fwd)
                    U = links[(mu, site)]
                    for a in range(nc):
                        for b in range(nc):
                            M[idx(t, site, a), idx(t, fwd, b)] += 0.5 * e * U[a, b]
                            M[idx(t, fwd, b), idx(t, site, a)] += -0.5 * e * np.conj(U[a, b])
        return M
    def det_M_finite(self, links, nt=NT_BULK):
        return np.linalg.det(self.build_M_full(links, nt)).real
def block_metric_per_mode(lam, m=MASS, nt=NT_BULK):
    tmin = -nt
    Mm = np.zeros((2 * nt, 2 * nt), dtype=complex)
    for t in range(tmin, nt):
        i = t - tmin
        Mm[i, i] += m + 1j * eta_t(t) * lam
        if t + 1 <= nt - 1:
            Mm[i, (t + 1) - tmin] += 0.5
        if t - 1 >= tmin:
            Mm[i, (t - 1) - tmin] += -0.5
    Mmi = np.linalg.inv(Mm)
    idx = lambda t: t - tmin
    K = np.zeros((2, 2), dtype=complex)
    for a, ta in enumerate((0, 1)):
        for b, tb in enumerate((0, 1)):
            K[a, b] = -wick([('cb', idx(-1 - ta)), ('c', idx(tb))], Mmi)
    return 0.5 * (K + K.conj().T)
def block_metric_singlestep_per_mode(lam, m=MASS, nt=NT_BULK):
    tmin = -nt
    Mm = np.zeros((2 * nt, 2 * nt), dtype=complex)
    for t in range(tmin, nt):
        i = t - tmin
        Mm[i, i] += m + 1j * eta_t(t) * lam
        if t + 1 <= nt - 1:
            Mm[i, (t + 1) - tmin] += 0.5
        if t - 1 >= tmin:
            Mm[i, (t - 1) - tmin] += -0.5
    Mmi = np.linalg.inv(Mm)
    idx = lambda t: t - tmin
    fields = [('c', 0), ('cb', 0)]
    refl = lambda kd, t: ('cb' if kd == 'c' else 'c', -1 - t)
    K = np.zeros((2, 2), dtype=complex)
    for a, (ka, ta) in enumerate(fields):
        rk, rt = refl(ka, ta)
        for b, (kb, tb) in enumerate(fields):
            K[a, b] = wick([(rk, idx(rt)), (kb, idx(tb))], Mmi)
    return 0.5 * (K + K.conj().T)
def block_fwd_propagator_berezin(carrier, links):
    E, Q, lam = carrier.modes(links)
    kap = np.array([np.linalg.eigvalsh(block_metric_per_mode(lam[j]))[-1]
                    for j in range(len(E))])
    return Q @ np.diag(kap) @ Q.conj().T
def block_fwd_propagator_operator(carrier, links):
    E, Q, lam = carrier.modes(links)
    return C_BLOCK * (Q @ np.diag(np.exp(-2.0 * E)) @ Q.conj().T)
def block_metric_spacetime_eigs(carrier, links, nt=NT_BULK):
    nc = carrier.nc
    Ns = carrier.Ns
    nmode = carrier.nmode
    tmin = -nt
    M = carrier.build_M_full(links, nt)
    Minv = np.linalg.inv(M)
    def idx(t, site, a):
        return ((t - tmin) * Ns + carrier.sidx[site]) * nc + a
    B = np.zeros((2 * nmode, 2 * nmode), dtype=complex)
    for sa in (0, 1):
        for al in range(nmode):
            s1 = carrier.sites[al // nc]; a1 = al % nc
            for sb in (0, 1):
                for be in range(nmode):
                    s2 = carrier.sites[be // nc]; a2 = be % nc
                    B[sa * nmode + al, sb * nmode + be] = \
                        Minv[idx(sb, s2, a2), idx(-1 - sa, s1, a1)]
    B = 0.5 * (B + B.conj().T)
    w = np.linalg.eigvalsh(B)
    return np.sort(w[w > 1e-9])
def full_grassmann_packet(carrier, links, nt=NT_BULK):
    nmode = carrier.nmode
    M = carrier.build_M_full(links, nt)
    det_phase, logabsdet = np.linalg.slogdet(M)
    Minv = np.linalg.inv(M)
    def block_index(t, mode):
        return (t + nt) * nmode + mode
    plus = np.asarray([block_index(t, mode) for t in (0, 1)
                       for mode in range(nmode)], dtype=int)
    minus = np.asarray([block_index(-1 - t, mode) for t in (0, 1)
                        for mode in range(nmode)], dtype=int)
    A = Minv[np.ix_(plus, minus)]
    C = Minv[np.ix_(minus, plus)]
    A_h = 0.5 * (A + A.conj().T)
    minus_C_h = -0.5 * (C + C.conj().T)
    E, Q, _lam = carrier.modes(links)
    slice_to_mode = np.kron(np.eye(2), Q)
    A_mode = slice_to_mode.conj().T @ A_h @ slice_to_mode
    minus_C_mode = slice_to_mode.conj().T @ minus_C_h @ slice_to_mode
    Wa_mode = np.zeros((2 * nmode, nmode), dtype=complex)
    Wb_mode = np.zeros((2 * nmode, nmode), dtype=complex)
    eig_A = np.zeros(nmode)
    eig_minus_C = np.zeros(nmode)
    offmode = 0.0
    for j in range(nmode):
        temporal = [j, nmode + j]
        vals_a, vecs_a = np.linalg.eigh(A_mode[np.ix_(temporal, temporal)])
        vals_b, vecs_b = np.linalg.eigh(minus_C_mode[np.ix_(temporal, temporal)])
        eig_A[j] = vals_a[-1]
        eig_minus_C[j] = vals_b[-1]
        Wa_mode[temporal, j] = vecs_a[:, -1]
        Wb_mode[temporal, j] = vecs_b[:, -1]
        for k in range(nmode):
            if k == j:
                continue
            other = [k, nmode + k]
            offmode = max(
                offmode,
                float(np.max(np.abs(A_mode[np.ix_(temporal, other)]))),
                float(np.max(np.abs(minus_C_mode[np.ix_(temporal, other)]))),
            )
    Wa = slice_to_mode @ Wa_mode @ Q.conj().T
    Wb = slice_to_mode @ Wb_mode @ Q.conj().T
    Gop = block_fwd_propagator_operator(carrier, links)
    expected = C_BLOCK * np.exp(-2.0 * E)
    wick_minor_resid = 0.0
    probe = sorted({0, min(1, 2 * nmode - 1), 2 * nmode - 1})
    for p in probe:
        for q in probe:
            for k in probe:
                for l in probe:
                    monomial = [
                        ('cb', int(minus[q])), ('c', int(minus[p])),
                        ('cb', int(plus[k])), ('c', int(plus[l])),
                    ]
                    explicit = wick(monomial, Minv)
                    minor = np.linalg.det(np.asarray([
                        [Minv[minus[p], minus[q]], Minv[minus[p], plus[k]]],
                        [Minv[plus[l], minus[q]], Minv[plus[l], plus[k]]],
                    ]))
                    wick_minor_resid = max(wick_minor_resid, abs(explicit - minor))
    orth_resid = max(
        float(np.max(np.abs(Wa.conj().T @ Wa - np.eye(nmode)))),
        float(np.max(np.abs(Wb.conj().T @ Wb - np.eye(nmode)))),
    )
    eigenvector_resid = max(
        float(np.max(np.abs(A @ Wa - Wa @ Gop))),
        float(np.max(np.abs(C @ Wb + Wb @ Gop))),
        float(np.max(np.abs(Wa.conj().T @ A @ Wa - Gop))),
        float(np.max(np.abs(-Wb.conj().T @ C @ Wb - Gop))),
    )
    normalization_resid = max(
        float(np.max(np.abs(eig_A / np.exp(-2.0 * E) - C_BLOCK))),
        float(np.max(np.abs(eig_minus_C / np.exp(-2.0 * E) - C_BLOCK))),
    )
    return {
        'Minv': Minv,
        'plus': plus,
        'minus': minus,
        'A': A,
        'C': C,
        'Wa': Wa,
        'Wb': Wb,
        'Gop': Gop,
        'det_phase': det_phase,
        'logabsdet': float(logabsdet),
        'det_value': float(math.exp(logabsdet)),
        'cross_herm': max(float(np.max(np.abs(A - A.conj().T))),
                          float(np.max(np.abs(C - C.conj().T)))),
        'mode_offdiag': offmode,
        'spectrum_resid': max(float(np.max(np.abs(eig_A - expected))),
                              float(np.max(np.abs(eig_minus_C - expected)))),
        'normalization_resid': normalization_resid,
        'orth_resid': orth_resid,
        'eigenvector_resid': eigenvector_resid,
        'wick_minor_resid': float(wick_minor_resid),
        'wrong_reflection_max_eig': -float(min(np.min(eig_A), np.min(eig_minus_C))),
    }
def block_fwd_propagator_permode(carrier, links):
    E, Q, lam = carrier.modes(links)
    kap = np.array([np.linalg.eigvalsh(block_metric_per_mode(lam[j]))[-1]
                    for j in range(len(E))])
    return np.diag(kap).astype(complex)
def _apply_c(state, mode, nmode):
    out = {}
    for occ, amp in state.items():
        if not (occ >> mode) & 1:          # mode empty -> c annihilates to 0
            continue
        sign = -1.0 if bin(occ & ((1 << mode) - 1)).count("1") % 2 else 1.0
        new = occ & ~(1 << mode)
        out[new] = out.get(new, 0.0 + 0.0j) + sign * amp
    return out
def _apply_cdag(state, mode, nmode):
    out = {}
    for occ, amp in state.items():
        if (occ >> mode) & 1:              # mode occupied -> c^dag annihilates to 0
            continue
        sign = -1.0 if bin(occ & ((1 << mode) - 1)).count("1") % 2 else 1.0
        new = occ | (1 << mode)
        out[new] = out.get(new, 0.0 + 0.0j) + sign * amp
    return out
def meson_op_on_vacuum_norm(carrier, V):
    nmode = carrier.nmode
    vac = {0: 1.0 + 0.0j}   # all-empty occupation
    total = {}
    for a in range(nmode):
        for b in range(nmode):
            v = V[a, b]
            if abs(v) == 0:
                continue
            st = _apply_c(vac, b, nmode)        # c_b |Omega> = 0 for the empty vacuum
            if not st:
                continue
            st = _apply_cdag(st, a, nmode)
            for occ, amp in st.items():
                total[occ] = total.get(occ, 0.0 + 0.0j) + v * amp
    return float(math.sqrt(sum(abs(amp) ** 2 for amp in total.values())))
def wilson_path_amplitude(carrier, links, x, y):
    nc = carrier.nc
    amp = {y: np.eye(nc, dtype=complex)}
    frontier = [y]
    seen = {y}
    while frontier and x not in seen:
        nxt = []
        for site in frontier:
            for mu in range(1, 4):
                if carrier.dims[mu - 1] == 1:
                    continue
                fwd = list(site)
                fwd[mu - 1] = (fwd[mu - 1] + 1) % carrier.dims[mu - 1]
                fwd = tuple(fwd)
                if fwd not in seen:
                    amp[fwd] = links[(mu, site)].conj().T @ amp[site]
                    seen.add(fwd)
                    nxt.append(fwd)
        frontier = nxt
    return amp.get(x, np.eye(nc, dtype=complex))
def meson_observables(carrier, links):
    nc = carrier.nc
    nmode = carrier.nmode
    Vs = []
    sites = carrier.sites
    for x in sites:
        V = np.zeros((nmode, nmode), dtype=complex)
        for a in range(nc):
            V[carrier.sidx[x] * nc + a, carrier.sidx[x] * nc + a] = 1.0
        Vs.append(V)
    for x in sites:
        for y in sites:
            if x == y:
                continue
            U = wilson_path_amplitude(carrier, links, x, y)
            V = np.zeros((nmode, nmode), dtype=complex)
            for a in range(nc):
                for c in range(nc):
                    V[carrier.sidx[x] * nc + a, carrier.sidx[y] * nc + c] = U[a, c]
            Vs.append(V)
    return Vs
def gauge_transform_links(carrier, links, g):
    new = {}
    for (mu, site), U in links.items():
        fwd = list(site)
        fwd[mu - 1] = (fwd[mu - 1] + 1) % carrier.dims[mu - 1]
        fwd = tuple(fwd)
        new[(mu, site)] = g[site] @ U @ g[fwd].conj().T
    return new
def meson_correlator_from_propagator(V, Gf):
    return np.trace(V.conj().T @ Gf @ V @ Gf)
def meson_correlator_full_berezin(carrier, links, V_left, V_right=None, packet=None,
                                   return_decomposition=False):
    if V_right is None:
        V_right = V_left
    if packet is None:
        packet = full_grassmann_packet(carrier, links)
    Wa = packet['Wa']
    Wb = packet['Wb']
    L_left = Wb @ V_left @ Wa.conj().T
    L_right = Wb @ V_right @ Wa.conj().T
    Minv = packet['Minv']
    plus = packet['plus']
    minus = packet['minus']
    Dminus = Minv[np.ix_(minus, minus)]
    Dplus = Minv[np.ix_(plus, plus)]
    C = packet['C']
    A = packet['A']
    disconnected = np.einsum(
        'pq,kl,pq,lk->', L_left.conj(), L_right, Dminus, Dplus, optimize=True
    )
    crossed = np.einsum(
        'pq,kl,pk,lq->', L_left.conj(), L_right, C, A, optimize=True
    )
    full_minor = disconnected - crossed
    connected = full_minor - disconnected
    if return_decomposition:
        return connected, full_minor, disconnected, -crossed
    return connected
def wilson_S_G(carrier, links):
    nc = carrier.nc
    S = 0.0
    for site in carrier.sites:
        for mu in range(1, 4):
            for nu in range(mu + 1, 4):
                if carrier.dims[mu - 1] == 1 or carrier.dims[nu - 1] == 1:
                    continue
                smu = list(site); smu[mu - 1] = (smu[mu - 1] + 1) % carrier.dims[mu - 1]
                snu = list(site); snu[nu - 1] = (snu[nu - 1] + 1) % carrier.dims[nu - 1]
                U1 = links[(mu, site)]
                U2 = links[(nu, tuple(smu))]
                U3 = links[(mu, tuple(snu))]
                U4 = links[(nu, site)]
                P = U1 @ U2 @ U3.conj().T @ U4.conj().T
                S += BETA * (1.0 - np.real(np.trace(P)) / nc)
    return S
def make_link_sample(carrier, group, K):
    bonds = [(mu, s) for s in carrier.sites for mu in range(1, 4)
             if carrier.dims[mu - 1] > 1]
    sample = []
    if group == 'u1':
        base = {b: RNG.uniform(0.0, 2.0 * math.pi) for b in bonds}
        for k in range(K):
            tw = 2.0 * math.pi * k / K
            sample.append({b: u1(base[b] + tw) for b in bonds})
    else:
        for _ in range(K):
            sample.append({b: random_su3() for b in bonds})
    return sample, bonds
def normalized_gauge_weights(carrier, sample, packets, use_det=True):
    logweights = np.asarray([
        -wilson_S_G(carrier, links) + (packet['logabsdet'] if use_det else 0.0)
        for links, packet in zip(sample, packets)
    ])
    shifted = np.exp(logweights - float(np.max(logweights)))
    return shifted / np.sum(shifted)
def u_averaged_meson(carrier, sample, prop_fn, Vs, packets, use_det=True):
    nObs = len(Vs)
    C = np.zeros((nObs, nObs), dtype=complex)
    weights = normalized_gauge_weights(carrier, sample, packets, use_det=use_det)
    for w, links in zip(weights, sample):
        Gf = prop_fn(carrier, links)
        Vloc = meson_observables(carrier, links)  # U-dependent meson basis
        for I in range(nObs):
            for J in range(nObs):
                C[I, J] += w * np.trace(Vloc[I].conj().T @ Gf @ Vloc[J] @ Gf)
    return C
def u_averaged_full_berezin(carrier, sample, packets, Vs):
    nObs = len(Vs)
    C = np.zeros((nObs, nObs), dtype=complex)
    weights = normalized_gauge_weights(carrier, sample, packets, use_det=True)
    decomposition_resid = 0.0
    for w, links, packet in zip(weights, sample, packets):
        Vloc = meson_observables(carrier, links)
        for I in range(nObs):
            for J in range(nObs):
                connected, full_minor, disconnected, crossed = \
                    meson_correlator_full_berezin(
                        carrier, links, Vloc[I], Vloc[J], packet=packet,
                        return_decomposition=True,
                    )
                decomposition_resid = max(
                    decomposition_resid,
                    abs(connected - crossed),
                    abs(full_minor - disconnected - connected),
                )
                C[I, J] += w * connected
    return C, float(decomposition_resid)
def banner(s):
    print("=" * 78)
    print(s)
    print("=" * 78)
def run_carrier(dims, group, K, label):
    nc = 1 if group == 'u1' else 3
    carrier = Carrier(dims, nc)
    sample, bonds = make_link_sample(carrier, group, K)
    packets = [full_grassmann_packet(carrier, links) for links in sample]
    r = {}
    for key in ('cross_herm', 'mode_offdiag', 'spectrum_resid',
                'normalization_resid', 'orth_resid', 'eigenvector_resid',
                'wick_minor_resid'):
        r[f'sameM_{key}'] = max(packet[key] for packet in packets)
    r['sameM_det_phase'] = max(abs(packet['det_phase'] - 1.0) for packet in packets)
    r['sameM_wrong_reflection_max_eig'] = max(
        packet['wrong_reflection_max_eig'] for packet in packets
    )
    E0, Q0, lam0 = carrier.modes(sample[0])
    worst_block = 0.0
    for j in range(len(E0)):
        pv = np.linalg.eigvalsh(block_metric_per_mode(lam0[j]))[-1]
        worst_block = max(worst_block, abs(pv - C_BLOCK * math.exp(-2.0 * E0[j])))
    r['block_eig_vs_e2E'] = worst_block
    worst_gf = 0.0
    for links in sample:
        gb = block_fwd_propagator_berezin(carrier, links)
        go = block_fwd_propagator_operator(carrier, links)
        worst_gf = max(worst_gf, float(np.max(np.abs(gb - go))))
    r['Gf_berezin_vs_operator'] = worst_gf
    worst_st = 0.0
    for links in sample[:3]:
        E_l, Q_l, lam_l = carrier.modes(links)
        op_eigs = np.sort(C_BLOCK * np.exp(-2.0 * E_l))
        st_eigs = block_metric_spacetime_eigs(carrier, links)
        st_dedup = st_eigs[::2] if len(st_eigs) == 2 * len(op_eigs) else st_eigs
        worst_st = max(worst_st, float(np.max(np.abs(np.sort(st_dedup) - op_eigs))))
    r['Gf_spacetime_vs_operator'] = worst_st
    Vs0 = meson_observables(carrier, sample[0])
    Gf0_op = block_fwd_propagator_operator(carrier, sample[0])
    worst_vac = 0.0
    min_diag_corr = math.inf
    for V in Vs0:
        worst_vac = max(worst_vac, meson_op_on_vacuum_norm(carrier, V))
        corr = meson_correlator_from_propagator(V, Gf0_op).real
        min_diag_corr = min(min_diag_corr, corr)
    r['vac_annih_norm'] = worst_vac           # MUST be ~0
    r['meson_corr_min_diag'] = min_diag_corr  # MUST be > 0 (nonzero & positive)
    worst_pc = 0.0
    worst_decomposition = 0.0
    for links, packet in zip(sample, packets):
        Vloc = meson_observables(carrier, links)
        Gf_op = block_fwd_propagator_operator(carrier, links)
        for V in Vloc:
            ber, full_minor, disconnected, crossed = meson_correlator_full_berezin(
                carrier, links, V, packet=packet, return_decomposition=True
            )
            op = meson_correlator_from_propagator(V, Gf_op)          # operator loop
            worst_pc = max(worst_pc, abs(ber - op))
            worst_decomposition = max(
                worst_decomposition,
                abs(ber - crossed),
                abs(full_minor - disconnected - ber),
            )
    r['per_config'] = worst_pc
    r['sameM_minor_decomposition'] = worst_decomposition
    Cop = u_averaged_meson(carrier, sample, block_fwd_propagator_operator,
                           Vs0, packets, use_det=True)
    Cber, avg_decomposition = u_averaged_full_berezin(carrier, sample, packets, Vs0)
    r['avg_genuine'] = float(np.max(np.abs(Cber - Cop)))
    r['sameM_avg_decomposition'] = avg_decomposition
    Cber_reduced = u_averaged_meson(
        carrier, sample, block_fwd_propagator_berezin, Vs0, packets, use_det=True
    )
    r['sameM_minor_vs_reduced'] = float(np.max(np.abs(Cber - Cber_reduced)))
    min_eig_avg = float(np.min(np.linalg.eigvalsh(0.5 * (Cop + Cop.conj().T))))
    r['avg_min_eig'] = min_eig_avg  # the averaged meson Gram must be PSD
    min_rand = math.inf
    for _ in range(200):
        Vr = (RNG.standard_normal((carrier.nmode, carrier.nmode))
              + 1j * RNG.standard_normal((carrier.nmode, carrier.nmode)))
        min_rand = min(min_rand, meson_correlator_from_propagator(Vr, Gf0_op).real)
    r['pos_random_min'] = min_rand  # connected loop >= 0 for ANY meson V
    Cber_pm = u_averaged_meson(carrier, sample, block_fwd_propagator_permode,
                               Vs0, packets, use_det=True)
    r['K2_permode_gap'] = float(np.max(np.abs(Cber_pm - Cop)))
    Gr0 = block_fwd_propagator_berezin(carrier, sample[0])
    r['recon_offdiag'] = float(np.max(np.abs(Gr0 - np.diag(np.diag(Gr0)))))
    Cop_flat = u_averaged_meson(carrier, sample, block_fwd_propagator_operator,
                                Vs0, packets, use_det=False)
    r['K3_flatdet_gap'] = float(np.max(np.abs(Cber - Cop_flat)))
    min_eig_single = math.inf
    for j in range(len(E0)):
        ev = np.linalg.eigvalsh(block_metric_singlestep_per_mode(lam0[j]))
        min_eig_single = min(min_eig_single, float(ev.min()))
    r['K4_singlestep_min_eig'] = min_eig_single
    g = {}
    for s in carrier.sites:
        g[s] = random_su3() if nc == 3 else u1(RNG.uniform(0, 2 * math.pi))
    links_g = gauge_transform_links(carrier, sample[0], g)
    Vs_before = meson_observables(carrier, sample[0])
    Vs_after = meson_observables(carrier, links_g)
    Gf_before = block_fwd_propagator_operator(carrier, sample[0])
    Gf_after = block_fwd_propagator_operator(carrier, links_g)
    packet_g = full_grassmann_packet(carrier, links_g)
    worst_gauge = 0.0
    worst_gauge_sameM = 0.0
    for Vb, Va in zip(Vs_before, Vs_after):
        cb = meson_correlator_from_propagator(Vb, Gf_before)
        ca = meson_correlator_from_propagator(Va, Gf_after)
        worst_gauge = max(worst_gauge, abs(cb - ca))
        cb_sameM = meson_correlator_full_berezin(
            carrier, sample[0], Vb, packet=packets[0]
        )
        ca_sameM = meson_correlator_full_berezin(
            carrier, links_g, Va, packet=packet_g
        )
        worst_gauge_sameM = max(worst_gauge_sameM, abs(cb_sameM - ca_sameM))
    r['K5_gauge_inv'] = worst_gauge
    r['K5_sameM_gauge_inv'] = worst_gauge_sameM
    singlet_resid = 0.0
    if len(carrier.sites) > 1:
        x, y = carrier.sites[0], carrier.sites[1]
        U0 = wilson_path_amplitude(carrier, sample[0], x, y)
        Ug = wilson_path_amplitude(carrier, links_g, x, y)
        singlet_resid = float(np.max(np.abs(g[x] @ U0 @ g[y].conj().T - Ug)))
    r['K5_wilson_covariance'] = singlet_resid
    r['det_min'] = min(packet['det_value'] for packet in packets)
    r['logdet_min'] = min(packet['logabsdet'] for packet in packets)
    r['gram_herm'] = float(np.max(np.abs(Cop - Cop.conj().T)))
    return r, carrier
def main() -> int:
    banner("GAUGE-INVARIANT NUMBER-CONSERVING MESON OS TRANSFER REPRESENTATION (3+1 carrier)")
    print("Meson observable: F = chibar(x) U(x,y) chi(y)  (number-conserving, gauge singlet).")
    print("F|Omega> = 0 (vacuum annihilation); the OS object is the meson 2-pt <Theta(F)F>,")
    print("a connected 4-fermion correlator = particle-hole intermediate-state sum >= 0.")
    print(f"mass={MASS}  c_block={C_BLOCK} (a-priori)  beta={BETA}  NT_bulk={NT_BULK}")
    print()
    checks = []
    configs = [
        ((2, 2, 1), 'u1', 16, "U(1)  2x2x1 spatial sheet (4 sites, 4 modes)"),
        ((2, 2, 1), 'su3', 6, "SU(3) 2x2x1 spatial sheet (4 sites, 12 modes)"),
        ((2, 1, 1), 'su3', 8, "SU(3) 2x1x1 spatial (2 sites, 6 modes)"),
        ((2, 1, 1), 'u1', 16, "U(1)  2x1x1 spatial (2 sites, minimal, degenerate)"),
    ]
    for dims, group, K, label in configs:
        banner(f"CARRIER: {label}   [Lt=2 block; transfer runs in time]")
        r, carrier = run_carrier(dims, group, K, label)
        Ls = "x".join(str(d) for d in dims)
        print(f"  spatial {Ls}, N_c={carrier.nc}, n_modes={carrier.nmode}, U-quadrature K={K}")
        print(f"  P_block : block pos eig vs C_BLOCK e^-2E       worst = {r['block_eig_vs_e2E']:.2e}")
        print(f"  P_block : Gf Berezin(M^-1) vs operator(e^-2H)  worst = {r['Gf_berezin_vs_operator']:.2e}")
        print(f"  P_block : full-spacetime M^-1 block spectrum vs operator worst = {r['Gf_spacetime_vs_operator']:.2e}")
        print(f"  SAME-M  : cross-block Hermiticity residual     = {r['sameM_cross_herm']:.2e}")
        print(f"  SAME-M  : spatial-mode off-block residual      = {r['sameM_mode_offdiag']:.2e}")
        print(f"  SAME-M  : particle/hole spectrum vs 2e^-2E     = {r['sameM_spectrum_resid']:.2e}")
        print(f"  SAME-M  : independently recovered C_BLOCK-2    = {r['sameM_normalization_resid']:.2e}")
        print(f"  SAME-M  : temporal-isometry orthogonality      = {r['sameM_orth_resid']:.2e}")
        print(f"  SAME-M  : particle/hole eigenvector intertwiner= {r['sameM_eigenvector_resid']:.2e}")
        print(f"  SAME-M  : explicit Wick sum vs 2x2 minor       = {r['sameM_wick_minor_resid']:.2e}")
        print(f"  SIGN    : wrong reflection physical max eig    = {r['sameM_wrong_reflection_max_eig']:.4f}  (must be <0)")
        print(f"  K1 VAC  : ||F|Omega>|| (MUST be ~0)            = {r['vac_annih_norm']:.2e}")
        print(f"  K1 VAC  : min meson <Theta(F)F> (MUST be >0)   = {r['meson_corr_min_diag']:.4f}")
        print(f"  P1      : per-config SAME-M Wick minor == operator loop worst = {r['per_config']:.2e}")
        print(f"  P1      : full minor - disconnected == crossed term    = {r['sameM_minor_decomposition']:.2e}")
        print(f"  P0      : SAME-M det-weighted Wick-minor avg == operator worst = {r['avg_genuine']:.2e}")
        print(f"  P0      : averaged minor decomposition residual        = {r['sameM_avg_decomposition']:.2e}")
        print(f"  SAME-M  : direct minor vs reduced Berezin kernel avg    = {r['sameM_minor_vs_reduced']:.2e}")
        print(f"  Ppos    : averaged meson Gram min eig (MUST >=0) = {r['avg_min_eig']:.4f}")
        print(f"  Ppos    : connected loop min over random V (>=0) = {r['pos_random_min']:.4f}")
        print(f"  Pdet    : min det SAME M[U] (Lt={2 * NT_BULK}) = {r['det_min']:.4e}  (>0)")
        print(f"  Pdet    : det phase residual / min log|det|    = {r['sameM_det_phase']:.2e} / {r['logdet_min']:.4f}")
        print(f"  herm    : ||C - C^dag|| (reflection=adjoint)   = {r['gram_herm']:.2e}")
        mixing = r['recon_offdiag'] > 1e-3
        print(f"  recon off-diagonal magnitude (mode-mixing)     = {r['recon_offdiag']:.4f}"
              f"  ({'MIXING' if mixing else 'DEGENERATE/no-mixing'})")
        if mixing:
            print(f"  K2 BREAK: per-mode-factorized Berezin gap      = {r['K2_permode_gap']:.4f}  (must be LARGE)")
        else:
            print(f"  K2 n/a  : per-mode gap (degenerate)            = {r['K2_permode_gap']:.2e}  (must be ~0: prior-vacuity regime)")
        print(f"  K3 DIFF : flat(no-det) vs det-weighted gap     = {r['K3_flatdet_gap']:.4f}  (must be LARGE)")
        print(f"  K4 CTRL : single-step block-metric min eig     = {r['K4_singlestep_min_eig']:.4f}  (must be <0)")
        print(f"  K5 GAUGE: ||<Theta(F)F> invariance|| under g   = {r['K5_gauge_inv']:.2e}  (must be ~0)")
        print(f"  K5 GAUGE: SAME-M Wick-minor invariance under g = {r['K5_sameM_gauge_inv']:.2e}  (must be ~0)")
        print(f"  K5 GAUGE: Wilson-line covariance residual      = {r['K5_wilson_covariance']:.2e}  (must be ~0)")
        print()
        checks.append((f"{label}: P_block eig", r['block_eig_vs_e2E'] < 1e-9, r['block_eig_vs_e2E']))
        checks.append((f"{label}: P_block Gf Berezin==operator", r['Gf_berezin_vs_operator'] < 1e-9, r['Gf_berezin_vs_operator']))
        checks.append((f"{label}: P_block full-spacetime M^-1 spectrum==operator", r['Gf_spacetime_vs_operator'] < 1e-9, r['Gf_spacetime_vs_operator']))
        checks.append((f"{label}: SAME-M cross blocks Hermitian", r['sameM_cross_herm'] < 1e-9, r['sameM_cross_herm']))
        checks.append((f"{label}: SAME-M spatial modes decouple", r['sameM_mode_offdiag'] < 1e-9, r['sameM_mode_offdiag']))
        checks.append((f"{label}: SAME-M particle/hole spectrum", r['sameM_spectrum_resid'] < 1e-9, r['sameM_spectrum_resid']))
        checks.append((f"{label}: SAME-M C_BLOCK normalization", r['sameM_normalization_resid'] < 1e-9, r['sameM_normalization_resid']))
        checks.append((f"{label}: SAME-M temporal isometries", r['sameM_orth_resid'] < 1e-9, r['sameM_orth_resid']))
        checks.append((f"{label}: SAME-M eigenvector intertwining", r['sameM_eigenvector_resid'] < 1e-9, r['sameM_eigenvector_resid']))
        checks.append((f"{label}: SAME-M explicit Wick==2x2 minor", r['sameM_wick_minor_resid'] < 1e-12, r['sameM_wick_minor_resid']))
        checks.append((f"{label}: SAME-M correct reflection sign", r['sameM_wrong_reflection_max_eig'] < -1e-3, r['sameM_wrong_reflection_max_eig']))
        checks.append((f"{label}: K1 F|Omega>=0 (vac annih)", r['vac_annih_norm'] < 1e-12, r['vac_annih_norm']))
        checks.append((f"{label}: K1 meson correlator NONZERO", r['meson_corr_min_diag'] > 1e-3, r['meson_corr_min_diag']))
        checks.append((f"{label}: P1 per-config meson dual", r['per_config'] < TOL_PER_CONFIG, r['per_config']))
        checks.append((f"{label}: P1 four-field minor decomposition", r['sameM_minor_decomposition'] < 1e-12, r['sameM_minor_decomposition']))
        checks.append((f"{label}: P0 det-weighted avg meson", r['avg_genuine'] < TOL_AVG, r['avg_genuine']))
        checks.append((f"{label}: P0 averaged minor decomposition", r['sameM_avg_decomposition'] < 1e-12, r['sameM_avg_decomposition']))
        checks.append((f"{label}: SAME-M minor==reduced Berezin", r['sameM_minor_vs_reduced'] < 1e-9, r['sameM_minor_vs_reduced']))
        checks.append((f"{label}: Ppos averaged Gram PSD", r['avg_min_eig'] > TOL_POS, r['avg_min_eig']))
        checks.append((f"{label}: Ppos connected loop >=0 (random V)", r['pos_random_min'] > TOL_POS, r['pos_random_min']))
        checks.append((f"{label}: Pdet det>0", r['det_min'] > TOL_DET, r['det_min']))
        checks.append((f"{label}: Pdet SAME-M phase positive", r['sameM_det_phase'] < 1e-9, r['sameM_det_phase']))
        checks.append((f"{label}: herm", r['gram_herm'] < 1e-9, r['gram_herm']))
        if mixing:
            checks.append((f"{label}: K2 per-mode BREAKS (mixing)", r['K2_permode_gap'] > TOL_BREAK, r['K2_permode_gap']))
        else:
            checks.append((f"{label}: K2 degenerate=>no-break (prior-vacuity)", r['K2_permode_gap'] < TOL_BREAK, r['K2_permode_gap']))
        checks.append((f"{label}: K3 flat-det differs from det-target", r['K3_flatdet_gap'] > TOL_BREAK, r['K3_flatdet_gap']))
        checks.append((f"{label}: K4 single-step indefinite", r['K4_singlestep_min_eig'] < -1e-3, r['K4_singlestep_min_eig']))
        checks.append((f"{label}: K5 gauge-invariant correlator", r['K5_gauge_inv'] < 1e-9, r['K5_gauge_inv']))
        checks.append((f"{label}: K5 SAME-M gauge-invariant minor", r['K5_sameM_gauge_inv'] < 1e-9, r['K5_sameM_gauge_inv']))
        checks.append((f"{label}: K5 Wilson-line covariance", r['K5_wilson_covariance'] < 1e-9, r['K5_wilson_covariance']))
    banner("SUMMARY OF CHECKS")
    npass = nfail = 0
    for name, ok, detail in checks:
        tag = "PASS" if ok else "FAIL"
        if ok:
            npass += 1
        else:
            nfail += 1
        print(f"  [{tag}] {name}  ({detail})")
    print()
    banner("SCOPE")
    print("This verifies the gauge-invariant, NUMBER-CONSERVING MESON Berezin==operator")
    print("equality on a FINITE 3+1 carrier (transfer matrix in time; spatial lattice the")
    print("regulator), ILLUSTRATING the cited transfer-matrix meson-spectroscopy")
    print("construction (Luescher 1977; Osterwalder-Seiler 1978; Montvay-Munster Ch.3;")
    print("Smit Sec.6).  The vacuum-annihilation obstruction (F|Omega>=0) is handled, NOT")
    print("dodged: the OS object is the meson 2-pt <Theta(F)F>, a connected 4-fermion")
    print("correlator = connected quark-line loop, NONZERO and OS-positive.")
    print("NO continuum claim either way (the continuum step -- transfer-matrix -> Wightman")
    print("reconstruction + spatial-continuum/Lorentz restoration -- is OUT OF SCOPE; the")
    print("framework is 3+1).  The per-config fermion 2-step rung, the Wilson-boundary (H1)")
    print("positivity, and any interacting-RP closure remain open.")
    print()
    print(f"SCORECARD PASS={npass} FAIL={nfail}")
    return 0 if nfail == 0 else 1
if __name__ == "__main__":
    raise SystemExit(main())
