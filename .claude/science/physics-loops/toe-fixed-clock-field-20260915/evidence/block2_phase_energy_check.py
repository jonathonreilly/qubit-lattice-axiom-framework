"""Exact cochain and high-precision phase challenges for the two-root estimate.

Constructs all cubical incidences here; does not import the proposed proof or
previous campaign's projector helper. Finite author check, not independent
scientific review and not an infinite-volume gas calculation.
"""
import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

mp.mp.dps = 70


def complex_matrices(width=(1, 1, 1, 1)):
    vertices = list(itertools.product(*(range(w+1) for w in width)))
    cells = [[(x, axes) for x in vertices
              for axes in itertools.combinations(range(4), degree)
              if all(x[a] < width[a] for a in axes)] for degree in range(5)]
    boundaries = []
    for degree in range(1, 5):
        lower = {cell: i for i, cell in enumerate(cells[degree-1])}
        C = sp.zeros(len(cells[degree]), len(cells[degree-1]))
        for row, (x, axes) in enumerate(cells[degree]):
            for k, a in enumerate(axes):
                remaining = axes[:k]+axes[k+1:]
                xp = list(x)
                xp[a] += 1
                C[row, lower[(tuple(xp), remaining)]] += (-1)**k
                C[row, lower[(x, remaining)]] -= (-1)**k
        boundaries.append(C)
    for C, Cnext in zip(boundaries, boundaries[1:]):
        assert Cnext*C == sp.zeros(Cnext.rows, C.cols)
    D, B = boundaries[1:3]
    pivots = D.rref()[1]
    U = D[:, pivots]
    P = U*(U.T*U).inv()*U.T
    Q = sp.eye(P.rows)-P
    if width == (1, 1, 1, 1):
        assert D.shape == (24, 32) and len(pivots) == 17
    assert P*P == P and Q*Q == Q and P*Q == sp.zeros(D.rows)
    assert B*P == sp.zeros(B.rows, D.rows)
    assert D.T*Q == sp.zeros(D.cols, D.rows)
    # For the exact idempotent Q, rank equals trace. Direct elimination on
    # this rational dense matrix causes unnecessary coefficient growth.
    assert sp.trace(Q) == B.rank() == D.rows-len(pivots)
    return D, B, P, Q, boundaries, cells


def real(x):
    x = sp.Rational(x)
    return mp.mpf(int(x.p))/int(x.q)


def norm2(x):
    return (x.T*x)[0]


def phase_cos(N, n, P, S):
    return mp.cos(2*mp.pi*real(N*(n.T*P*S)[0]))


def main():
    D, B, P, Q, _, _ = complex_matrices()
    N = 3
    c = 2*mp.pi*N
    fills = [sp.eye(24)[:, i] for i in range(24)]
    weights = [sp.Rational(1, i+1) for i in range(24)]
    # The finite frame is diagonal and its exact operator norm is 1.
    K = sp.diag(*weights)
    assert max(weights) == 1
    errors, ratios, root_rows = [], [], []
    for i in [0, 5, 13, 23]:
        n0, S0 = fills[i], fills[(i+3) % 24]
        nk = n0 + 17*D[:, i % D.cols]
        Sk = S0 + 19*B.T[:, i % B.rows]
        assert Q*nk == Q*n0 and P*Sk == P*S0
        for n in [n0, nk]:
            for S in [S0, Sk]:
                thetaP = N*(n.T*P*S)[0]
                thetaQ = -N*(n.T*Q*S)[0]
                assert thetaP-thetaQ == N*(n.T*S)[0]
                assert (thetaP-thetaQ).q == 1
                err = abs(mp.cos(2*mp.pi*real(thetaP))
                          -mp.cos(2*mp.pi*real(thetaQ)))
                errors.append(err)
                assert err < mp.mpf('1e-62')
                assert abs(phase_cos(N,n,P,S)-phase_cos(N,n0,P,S0)) < mp.mpf('1e-62')
        for species, root in [('electric', Sk), ('magnetic', nk)]:
            z = P*root if species == 'electric' else Q*root
            E = norm2(z)
            lhs = mp.mpf(0)
            for fill, weight in zip(fills, weights):
                n, S = (fill, root) if species == 'electric' else (root, fill)
                lhs += real(weight)*(1-phase_cos(N,n,P,S))
            frame_bound = c*c*real((z.T*K*z)[0])/2
            energy_bound = c*c*real(E)/2
            assert lhs <= frame_bound+mp.mpf('1e-60')
            assert frame_bound <= energy_bound+mp.mpf('1e-60')
            root_rows.append(dict(species=species, root=i, integral=float(lhs),
                                  frame_bound=float(frame_bound),
                                  physical_energy=str(E), energy_bound=float(energy_bound)))
        ratios.append(norm2(P*nk)/norm2(Q*nk))
    assert min(ratios) > 1000

    # A contractible four-cube chain supports two COMPATIBLE components of
    # each species. Check support adjacency rather than assume compatibility.
    Dc, Bc, Pc, _, boundaries, cells = complex_matrices((4, 1, 1, 1))
    es, ms = (0, 6), (0, 18)
    def electric_vertices(p):
        edges = [e for e in range(Dc.cols) if Dc[p,e]]
        return {v for e in edges for v in range(boundaries[0].cols)
                if boundaries[0][e,v]}
    def magnetic_support(p):
        three_cells = {q for q in range(Bc.rows) if Bc[q,p]}
        four_cells = {v for q in three_cells for v in range(boundaries[3].rows)
                      if boundaries[3][v,q]}
        return three_cells, four_cells
    assert not electric_vertices(es[0]) & electric_vertices(es[1])
    m0, m1 = magnetic_support(ms[0]), magnetic_support(ms[1])
    assert not m0[0] & m1[0] and not m0[1] & m1[1]
    ts = [c*real(Pc[m,e]) for e in es for m in ms]
    assert all(abs(mp.sin(t)) > mp.mpf('.1') for t in ts)
    direct = mp.mpc(0)
    for signs in itertools.product([-1,1], repeat=4):
        angle = sum(signs[e]*signs[2+m]*ts[2*e+m]
                    for e in range(2) for m in range(2))
        direct += mp.exp(1j*angle)/16
    empty = mp.fprod(mp.cos(t) for t in ts)
    cycle = mp.fprod(mp.sin(t) for t in ts)
    assert abs(direct-empty-cycle) < mp.mpf('1e-65')
    assert abs(direct-empty) > mp.mpf('.001')

    # Nonintegral N destroys the needed phase periodicity: a negative control.
    fractional_N = sp.Rational(1,2)
    e = fills[0]
    p_angle = 2*mp.pi*real(fractional_N*(e.T*P*e)[0])
    q_angle = -2*mp.pi*real(fractional_N*(e.T*Q*e)[0])
    noninteger_difference = abs(mp.cos(p_angle)-mp.cos(q_angle))
    assert noninteger_difference > mp.mpf('.5')

    x = mp.mpf(2048)
    reserve = 128*1562500*x*mp.exp(-x/64)/(1-100608*mp.exp(-x/64))
    assert 100608*mp.exp(-x/64) < 1 and reserve < mp.mpf('.006')
    out = dict(status='finite_exact_cochain_and_phase_checks_passed',
               phase_periodicity_max_error=str(max(errors)),
               gauge_dependent_wrong_energy_ratios=[str(x) for x in ratios],
               rooted_checks=root_rows,
               mixed_four_cycle=dict(electric_labels=es, magnetic_labels=ms,
                                     width=[4,1,1,1], same_species_compatible=True,
                                     fill_cells=[cells[2][p] for p in (*es,*ms)],
                                     exact_P_entries=[str(Pc[m,e]) for e in es for m in ms],
                                     average_real=float(mp.re(direct)), empty_term=float(empty),
                                     cycle_term=float(cycle)),
               noninteger_N_periodicity_failure=float(noninteger_difference),
               uniform_reserve_upper_at_x2048=float(reserve),
               scope='Author finite diagnostic; no complete gas sum, continuum limit, '
                     'interval certification, or independent review.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__ == '__main__':
    main()
