"""Bounded map theorem: r=1/2 is stable for the supplied two-sector reverse map
g(r)=sqrt(r/2); the physical-arrow selection is not derived here.

Full assumptions brainstorm (wf_919df127, 14 challenges + 3 meta, 16/17 converge on "stable under a
named condition").

THE MAP FLIP (verified): the records/Lueders SHARPENING map S(r)=2r^2 has multiplier
S'(1/2)=2>1 (REPELLER). The supplied reverse map g(r)=sqrt(r/2), on the same
two-sector coordinate, has g'(1/2)=1/2<1 (STABLE) and r=1/2 is the GLOBAL attractor
for the tested positive seeds. This proves stability for the named map only; it does
not prove that charged-lepton r physically follows that map.

GROUNDED ANCHORS (exact framework baseline / Z3-circulant algebra):
- r=1/2 <=> HS 2-SECTOR EQUIPARTITION: ||aI||^2 = 3a^2 equals ||bC+conj(b)C^2||^2 = 6|b|^2 iff |b|^2/a^2=1/2;
  the unique maximum of the 2-block (singlet vs doublet) entropy (S2=ln2).
- ENDPOINT SPECTRA: r=0 gives [1,1,1] (S_3-degenerate) and r=1 gives [0,0,3]
  (two massless). Any distinct massive-lepton use of this carrier lies in the open
  interior (0,1); r=1/2 is the balanced interior point attracted by the supplied map g.
- Q = Tr H^2/(Tr H)^2 = 1/3 + (2/3) r exact; Q=2/3 <=> r=1/2 <=> sector equipartition.

HONEST RESIDUAL (the one gate, two posited conditions, BOTH = the same det_C/2-sector + chirality gate):
(a) the selected flow must coarse-grain by the 2 ISOTYPE SECTORS (block/idempotent), NOT the 3
    eigenmodes (spectral entropy peaks at r=0) nor dimension/Plancherel (peaks at r=1). Only the 2-sector
    partition puts the max-entropy attractor at r=1/2. = the det_C / einselected-partition gate.
(b) identifying physical r evolution with g(r)=sqrt(r/2), or with any entropy-increasing flow on
    the 2-sector simplex, is not derived from framework baseline.

CORRECTION to the synth: the proposed "sigma symmetry" |b|^2 -> a^2-|b|^2 IS exactly r -> 1-r and it
CHANGES Tr H^2 (NOT Casimir-preserving) -> it is the r<->1-r RELABELING, not a dynamical symmetry; the
stability does NOT rest on symmetry-protection (it rests on equipartition + the selected map).

THREE-LANE PICTURE: r=0/Q=1/3 = unbroken-S_3 democratic/degenerate endpoint; r=1/2/Q=2/3 =
balanced two-sector fixed point of g; r=1/Q=1 = maximal-hierarchy (one heavy + two massless) endpoint.
These are algebraic strata of the exact line Q=1/3+(2/3)r; physical selection remains open.
"""
import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def main():
    passed = []

    # (1) map flip: sharpening repeller vs supplied reverse-map global attractor
    S = lambda r: 2 * r ** 2          # entropy-decreasing sharpening (Lueders r->2r^2)
    g = lambda r: np.sqrt(r / 2)      # supplied reverse map on the two-sector coordinate
    flows = []
    for r0 in [0.05, 0.25, 0.49, 0.51, 0.9, 5.0]:
        r = r0
        for _ in range(80):
            r = g(r)
        flows.append(r)
    passed.append(check(
        "1 map flip: sharpening S'(1/2)=2 (REPELLER); supplied g'(1/2)=1/2 (STABLE); every tested seed -> r=1/2 (GLOBAL attractor)",
        abs(4 * 0.5 - 2) < 1e-12 and abs(1 / (2 * np.sqrt(2 * 0.5)) - 0.5) < 1e-12 and all(abs(f - 0.5) < 1e-6 for f in flows),
        f"g-iteration from {{0.05..5.0}} all -> {np.round(flows,4).tolist()}; reversing the map flips repeller<->attractor"))

    # (2) HS 2-sector equipartition at r=1/2
    hs = lambda M: np.trace(M.conj().T @ M).real
    a, b = 1.0, np.sqrt(0.5)          # r=1/2
    passed.append(check(
        "2 r=1/2 <=> HS 2-sector equipartition: ||aI||^2 = ||bC+conj(b)C^2||^2 (3a^2=6|b|^2), the unique 2-block entropy max",
        abs(hs(a * I3) - hs(b * C + np.conj(b) * C.conj().T)) < 1e-9,
        f"||aI||^2={hs(a*I3):.3f} = ||doublet||^2={hs(b*C+np.conj(b)*C.conj().T):.3f}"))

    # (3) endpoint exclusion: r=0 degenerate, r=1 two-massless -> both forbidden for distinct massive leptons
    e0 = np.sort(np.linalg.eigvalsh(1.0 * I3))
    e1 = np.sort(np.linalg.eigvalsh(1.0 * I3 + 1.0 * C + 1.0 * C.conj().T))
    passed.append(check(
        "3 endpoint spectra: r=0 -> [1,1,1] (degenerate) and r=1 -> [0,0,3] (two massless); distinct massive use lies in the open interior",
        np.allclose(e0, [1, 1, 1]) and np.allclose(np.round(e1, 6), [0, 0, 3]),
        f"r=0 eig={e0.tolist()}, r=1 eig={np.round(e1,3).tolist()} -> admissible set is the open interior (0,1)"))

    # (4) honest caveat: the proposed sigma 'symmetry' is r<->1-r and CHANGES the Casimir Tr H^2 (not a symmetry)
    TrH2 = lambda r: 3 + 6 * r
    passed.append(check(
        "4 the 'sigma' involution |b|^2->a^2-|b|^2 IS r<->1-r and CHANGES Tr H^2 -> a relabeling, NOT a dynamical symmetry (stability rests on equipartition+selected map, not symmetry-protection)",
        abs(TrH2(0.2) - TrH2(0.8)) > 1e-6,
        f"Tr H^2(0.2)={TrH2(0.2)} != Tr H^2(0.8)={TrH2(0.8)} -> not Casimir-preserving"))

    # (5) the residual: only the 2-SECTOR coarse-graining puts the max-entropy attractor at r=1/2
    def S2(r):  # 2-sector entropy
        ps, pd = 1 / (1 + 2 * r), 2 * r / (1 + 2 * r)
        return -(ps * np.log(ps) + pd * np.log(pd))
    def Sspec(r):  # 3-eigenvalue spectral entropy (normalized |eigenvalue| as p) -- peaks at r=0 (degenerate)
        lam = np.abs([1 + 2 * np.sqrt(r) * np.cos(2 * np.pi * k / 3) for k in range(3)])
        p = lam / lam.sum()
        p = p[p > 1e-12]
        return -(p * np.log(p)).sum()
    rs = np.linspace(0.01, 3, 1500)
    r_S2 = rs[int(np.argmax([S2(r) for r in rs]))]
    r_spec = rs[int(np.argmax([Sspec(r) for r in rs]))]
    passed.append(check(
        "5 RESIDUAL: only the 2-SECTOR entropy peaks at r=1/2; the 3-eigenvalue spectral entropy peaks at r=0 -> r=1/2 stability requires selecting the 2-sector coarse-graining",
        abs(r_S2 - 0.5) < 0.03 and r_spec < 0.2,
        f"argmax S2(2-sector)={r_S2:.3f} (=1/2); argmax Sspec(3-eigenvalue)={r_spec:.3f} (->0) -> the partition is the open posit"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT (bounded map theorem): r=1/2 is STABLE for the supplied two-sector reverse map")
    print("g(r)=sqrt(r/2). The sharpening map S(r)=2r^2 has multiplier 2 at r=1/2; g has multiplier")
    print("1/2 and every tested positive seed flows to r=1/2. GROUNDED: r=1/2 is HS 2-sector")
    print("equipartition and Q=1/3+(2/3)r gives Q=2/3 there. RESIDUAL: selecting the 2-isotype")
    print("coarse-graining and binding physical r-evolution to g, or to any entropy-increasing")
    print("two-sector flow, remains outside this theorem.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
