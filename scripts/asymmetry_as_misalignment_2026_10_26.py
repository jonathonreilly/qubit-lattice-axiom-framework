#!/usr/bin/env python3
"""Asymmetry as misalignment: an octonion/F_8 route fails, the [[8,3,3]] cell code's group is AGammaL(1,8),
and sector-wise residual antiunitaries give theta_bar_tree = 0 with J != 0 on the adopted slab's X-node families.

Driver. Each part is a declared helper run in an isolated interpreter (python -I); this file checks the result
each part prints against the criteria fixed before the runs (sections O, G, M of the note). Labels: [T] exact,
[F] finite diagnostic, [N] negative (failed search over the stated family only). Every line reports a RESULT:
'PASS' means the stated result reproduced, including results that are failures of a hypothesis."""
AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/asymmetry_misalignment_part_freeze_tick_rebuild_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_code_group_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_code_controls_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_logical_orbits_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_octonion_seven_sets_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_tick_singer_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_octonion_table_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_octonion_jordan_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_class_inversion_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_code_space_match_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_slab_family_characters_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_misalignment_cp_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_locality_hierarchy_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_sector_crosstalk_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_posthoc_generic_vertex_2026_10_26.py",
)
import os, re, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
NP = [0, 0]
def check(tag, ok, msg, det=""):
    ok = bool(ok); NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}" + (f"  [{det}]" if det else ""), flush=True)
def run(part):
    p = HERE / f"asymmetry_misalignment_part_{part}_2026_10_26.py"
    nt = '4' if part == 'code_space_match' else '1'      # the 8! x 6 labelling search is the one heavy part
    env = dict(os.environ, OPENBLAS_NUM_THREADS=nt, OMP_NUM_THREADS=nt)
    t = time.time(); r = subprocess.run([sys.executable, '-I', str(p)], capture_output=True, text=True, timeout=900, env=env)
    out = r.stdout + r.stderr
    print(f"  ({part}: exit {r.returncode}, {time.time() - t:.1f} s)", flush=True)
    if r.returncode != 0: print(out[-2000:])
    return r.returncode, out
def num(pat, out, cast=float, default=None):
    m = re.search(pat, out); return cast(m.group(1)) if m else default

print("== G: the [[8,3,3]] cell code's symmetry group")
rc, o = run('code_group')
check("G1 [T]", rc == 0 and "uniform-frame symmetries by frame: {'id': 56, 'ZYX': 56, 'XYZ': 56}  total 168" in o
      and "element orders: {1: 1, 2: 7, 3: 56, 6: 56, 7: 48}" in o,
      "perm x uniform-frame symmetries of Gottesman's code: 168 = 56 per frame (id, XYZ, ZYX); element orders 1:1 2:7 3:56 6:56 7:48")
check("G2 [T]", "centre order: 1" in o and "derived series orders: 168 56 8" in o and "regular on the 8 qubits: OK" in o
      and "P == AGammaL(1,8) in its natural action (explicit F_8 labelling): True" in o,
      "the group is AGammaL(1,8) = 2^3 x| (7 x| 3) in its natural action (explicit F_8 labelling); centre 1; derived series "
      "168 > 56 > 8; not PSL(2,7) (7 involutions, order-6 elements) and not AGL(1,8) x Z3 (no order 21)")
check("G3 [T]", "(Galois exponent i, frame) pairs: {(0, 'id'): 56, (1, 'ZYX'): 56, (2, 'XYZ'): 56}" in o,
      "frame lock: the uniform frame power equals the Galois (Frobenius) exponent of the element")
check("G4 [T]", "full LC x perm automorphism group order (GL(S) method): 168" in o and "automorphisms with a uniform frame: 168 of 168" in o
      and "perm images of full group == P: True" in o,
      "independent method (GL(S) permuting the 8 subspaces K_j): the full local-Clifford x permutation group is the same 168, all uniform-frame")
rc, o = run('code_controls')
check("G5 [T]", rc == 0 and "max |O_h cap code group| over all 8! labellings: 24" in o,
      "largest overlap with the cube group O_h over all 8! vertex labellings is 24 (T_h type); never a 4-fold turn")
check("G6 [T]", "|Aut(X-projection)| = 1344" in o,
      "the X, Z and X+Z support projections of the stabiliser group are each the [8,4,4] extended Hamming code RM(1,3) (Aut = AGL(3,2), 1344)")
check("G7 [F] control", "contains all 48 cube symmetries (standard labelling): True" in o
      and "cube C3 about (111), no frame: logical X_k -> [[2], [0], [1]]" in o
      and "random [[8,3]] codes with an order-7 perm x uniform-frame symmetry: 0/100" in o,
      "numerology control: the [[8,3,2]] cube colour code also has F_8/AGL(3,2) structure and a frame-free logical 3-cycle, "
      "so neither is evidence; only the frame lock and the missing 4-fold turn are specific to [[8,3,3]]; 0/100 random [[8,3]] codes have an order-7 symmetry")
rc, o = run('logical_orbits')
check("G8 [T]", rc == 0 and "orbit size 7: min weights {4: 7}; pairwise symplectic products {0: 21}; closed under product (+0): True" in o
      and "stabiliser orders in G of the decompositions (order -> how many decompositions): {1: 504, 2: 420, 3: 168, 6: 28}" in o,
      "the group acts on the 63 logical classes with orbits 7, 28, 28; the 7-orbit is a commuting Lagrangian; no splitting of the "
      "logical space into 3 qubits is invariant (largest stabiliser order 6)")

print("== O: the octonion / J3(O) route")
rc, o = run('octonion_seven_sets')
check("O1 [N]", rc == 0 and "maximal anticommuting 7-sets of logical classes: 288" in o and "G-invariant 7-sets: 0" in o,
      "T1: no group-invariant anticommuting 7-set of logical Paulis (0 of 288): the code carries no octonion (Clifford-7) structure; "
      "the F21-invariant one (1) is forced by 288 = 1 mod 7 and does not discriminate")
rc, o = run('octonion_table')
rc2, o2 = run('octonion_jordan')
check("O2 [T]", rc2 == 0 and "signed-permutation automorphisms of O: 1344 ; pure permutation automorphisms: 21" in o2
      and "pure perms are i -> a i + b with a in {1,2,4}: True" in o2,
      "the cyclic octonion table's signed automorphisms number 1344; its pure-permutation ones are i -> ai+b, a in {1,2,4} (F21): "
      "the normaliser of the 7-cycle, true of any cyclic labelling, so the F21 match to the code is generic")
jd = [num(rf"Jordan identity defect on H_{k}\(H\) \(true quaternion subalgebra\): ([0-9.e+-]+)", o2) for k in (3, 4, 5)]
check("O3 [T]", rc == 0 and all(x is not None and x < 1e-10 for x in jd),
      "control for the Jordan-von Neumann-Wigner bound: H_n(H) satisfies the Jordan identity for n = 3, 4, 5 (the n <= 3 cap is octonionic, "
      "and caps a matrix size; it does not select a family number)", f"defects {jd}")
check("O4 [S]", "preimage of F21: order 168" in o2 and "orbit sizes on the 7 imaginary lines under the preimage of F21: [7]" in o2,
      "the preimage of F21 in Aut(O) has AGammaL(1,8)'s order statistics (Schur-Zassenhaus) but fixes the real unit, while the code "
      "group is transitive on the 8 qubits: the match is abstract only")
rc, o = run('tick_singer')
check("O5 [N]", rc == 0 and o.count("order-7 (Singer-type) site permutations covariant with ANY O_h momentum map: 0") == 3
      and "FREEZE U_F(K): site permutations preserving |U(K)| for all test K (internal): 1" in o,
      "T2: no order-7 site permutation (any diagonal phases, any O_h momentum map) preserves |U(K)| of CL-1's tick (eps 0.3, 1.1) or FREEZE; "
      "their site-permutation groups are {1, one involution} and {1}")
rc, o = run('code_space_match')
leak = {k: num(rf"{re.escape(k)}\s+unitarity .*?min leak ([0-9.e+-]+)", o) for k in
        ('identity (control)', 'CL-1 intra-cell exp(-i .3 Re)', 'CL-1 intra-cell exp(-i 1.1 Re)', 'CL-1 eps .3 generic K',
         'FREEZE K=0', 'FREEZE generic K', 'random number-conserving (baseline)')}
u0 = num(r"\|\|U1\(0\) - 1\|\| = ([0-9.e+-]+)", o)
check("O6 [N]", rc == 0 and leak['identity (control)'] < 1e-10 and u0 is not None and u0 < 1e-12
      and all(leak[k] > 0.1 for k in leak if k not in ('identity (control)',)),
      "T3: the second-quantised one-cell tick (Jordan-Wigner) preserves the [[8,3,3]] code space for no site labelling x uniform frame "
      "(8! x 6): 'logical qubit = family' has no dynamics behind it. CL-1's K = 0 block is exactly the identity (trivial pass, excluded)",
      ", ".join(f"{k}: {v:.2g}" for k, v in leak.items()))

print("== M: sector misalignment of residual antiunitaries")
rc, o = run('slab_family_characters')
check("M1 [F]", rc == 0 and "A1 PASS" in o and "A2 PASS" in o,
      "A1/A2: at m = 3 the adopted Wilson-type slab (Ls = 8) has near-wall zero modes exactly at the three X points (2 states each, one hand); "
      "an antiunitary C K with k -> -k commutes with the slab Bloch Hamiltonian")
check("M2 [F]", "A3 FAIL" in o and "TEST A: FAIL" in o,
      "A3 as pre-registered FAILS: the C2 rotations' family actions carry +-i (overall operator phase unfixed). Disclosed post-hoc fix "
      "(spin-statistics g^n = (-1)^F) makes every C2 real; translations act as diag(-1,1,1) and permutations, real and non-scalar")
rc, o = run('misalignment_cp')
b1 = re.findall(r"max\|sin theta_bar\| ([0-9.e+-]+); median \|J\|/Jmax ([0-9.e+-]+)", o)
check("M3 [F]", rc == 0 and all(f"{t} PASS" in o for t in ('B1', 'B2', 'B3', 'B4')),
      "B: misaligned sectors (up keeps T g_u, down keeps T g_d, relative action real non-scalar) give theta_bar_tree = 0 (|sin| < 1e-10, "
      "2000 samples per pair) with median |J|/J_max ~ 0.28; aligned control J < 1e-13; generic complex Yukawas, Haar U(3) and "
      "incommensurate characters are theta-safe in < 0.5% (genericity control)", "; ".join(f"sin {a} J {b}" for a, b in b1[:4]))
rc, o = run('locality_hierarchy')
check("M4 [F]", rc == 0 and "-> PASS" in o and "C2 FAIL  C3 FAIL" in o and "-> FAIL" in o,
      "C: a single-site vertex gives an exactly rank-1 Yukawa (s = 3,0,0), the uniform vertex an exactly degenerate one; but local "
      "eps^|c| profiles do not give a hierarchy (C2, C3 FAIL) and the democratic term is incompatible with a non-scalar real twist (C4 FAIL)",
      (re.search(r"C2/C3: local[^\n]*", o) or re.search("x", "x")).group(0))

print("== X: sector cross-talk on the slab (the decisive test of M; its own criteria, D1-D7, were fixed before its first run)")
rc, o = run('sector_crosstalk')
st = {t: ('PASS' if re.search(rf"^PASS: {t} ", o, re.M) else 'FAIL' if re.search(rf"^FAIL: {t} ", o, re.M) else None)
      for t in ('D1', 'D2', 'D2r', 'D3', 'D4', 'D5', 'D6', 'D7')}
th2 = num(r"D2 decisive cross-talk, generic potentials: min_Delta median \|theta_bar_ind\| = ([0-9.e+-]+)", o)
th2r = num(r"D2r restricted shallow potential \(supplied\): min_Delta median \|theta_bar_ind\| = ([0-9.e+-]+)", o)
check("X1 [F]", "TOTAL: PASS=2 FAIL=6" in o and st == {'D1': 'FAIL', 'D2': 'FAIL', 'D2r': 'FAIL', 'D3': 'FAIL', 'D4': 'PASS',
                                                      'D5': 'PASS', 'D6': 'FAIL', 'D7': 'FAIL'},
      "the pre-registered cross-talk runner reproduces its outcome: PASS = D4 (generic vertex theta = O(1)), D5 (Ls convergence); "
      "FAIL = D1 (on-site vertex: scalar Yukawa ~ 1, J undefined), D2, D2r, and D3/D6/D7 on precision only (1e-10..1e-11 vs a 1e-12 threshold)",
      str(st))
check("X2 [F]", th2 is not None and th2 > 0.1,
      "DECISIVE (D2): with each order entering the other species' densities at kappa = 1, the induced theta_bar is O(1) and flat in the "
      "sector separation (Delta = 1..18, Ls = 40): separating the sectors protects nothing; theta_ind is linear in kappa, so the mechanism "
      "needs kappa < ~1e-10 (the Nelson-Barr quality problem in lattice form)", f"min_Delta median |theta_ind| = {th2}")
check("X3 [F]", th2r is not None and 1e-10 < th2r < 1e-8,
      "D2r (supplied restriction: the shallow order's density also respects the deep sector's residual antiunitary) removes the flat leak; "
      "the remainder decays with depth and reaches 4e-10 at Delta = 18, just above the 1e-10 threshold", f"{th2r}")
rc, o = run('posthoc_generic_vertex')
row18 = re.search(r"^\s+18 \| max ([0-9.e+-]+)\s+([0-9.e+-]+)\s+([0-9.e+-]+)", o, re.M)
check("X4 [F] post hoc", rc == 0 and row18 is not None and float(row18.group(1)) < 1e-9 and float(row18.group(3)) > 1,
      "post hoc (disclosed, not pre-registered): a generic vertex symmetrised to each sector's residual gives theta_tree = 0 with "
      "|J|/Jmax 0.2-0.5, but the deep sector's leak grows to O(10) with depth (Gamma/M propagation outlives the deep Yukawa)",
      row18.group(0).strip() if row18 else "")

print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
sys.exit(0 if NP[1] == 0 else 1)
