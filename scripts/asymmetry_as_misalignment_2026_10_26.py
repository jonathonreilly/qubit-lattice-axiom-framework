#!/usr/bin/env python3
"""Asymmetry as misalignment: the tested octonion/F_8 constructions fail, the [[8,3,3]] cell code's phase-forgetting binary
symmetry group (qubit permutations x binary symplectic local frames, Pauli and sign lifts not counted) is AGammaL(1,8),
and sector-wise residual antiunitaries fix theta_bar_tree in {0, pi} (sign branch not selected) with J != 0 on the supplied
slab's X-node families.

Driver. Each part is a declared helper run in a separate interpreter (python -E -P since 2026-11-14: environment variables
ignored and the script directory not prepended; -s, which also hides user site-packages, is not used because numpy is
installed there on the machine that regenerated the cache; the source version used -I); this file checks the result
each part prints against the criteria fixed before the runs (sections O, G, M of the note). Labels: [T] exact,
[F] finite diagnostic, [N] negative (failed search over the stated family only). Every line reports a RESULT:
'PASS' means the stated result reproduced, including results that are failures of a hypothesis.
Since 2026-11-14 (PR 10129 second hold, finding F7) every check that reads a part's output also requires that part's
exit code to be 0: a part that crashes or exits nonzero fails every check built on it, while a part's own documented
scientific FAIL rows (printed with exit 0) remain valid output."""
AUDIT_TIMEOUT_SEC = 2700
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
    "scripts/asymmetry_misalignment_part_posthoc_degeneracy_check_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_charged_orders_2026_10_26.py",
    "scripts/asymmetry_misalignment_part_wrong_sector_2026_10_26.py",
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
    flags = ['-E', '-P'] if sys.version_info >= (3, 11) else ['-E']
    t = time.time(); r = subprocess.run([sys.executable, *flags, str(p)], capture_output=True, text=True, timeout=1500, env=env)
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
      "phase-forgetting binary symmetry group of Gottesman's code (qubit permutations x uniform binary symplectic frames; Pauli and "
      "sign lifts not counted): 168 = 56 per frame (id, XYZ, ZYX); element orders 1:1 2:7 3:56 6:56 7:48")
check("G2 [T]", rc == 0 and "centre order: 1" in o and "derived series orders: 168 56 8" in o and "regular on the 8 qubits: OK" in o
      and "P == AGammaL(1,8) in its natural action (explicit F_8 labelling): True" in o,
      "this binary group is AGammaL(1,8) = 2^3 x| (7 x| 3) in its natural action (explicit F_8 labelling); centre 1; derived series "
      "168 > 56 > 8; not PSL(2,7) (7 involutions, order-6 elements) and not AGL(1,8) x Z3 (no order 21)")
check("G3 [T]", rc == 0 and "(Galois exponent i, frame) pairs: {(0, 'id'): 56, (1, 'ZYX'): 56, (2, 'XYZ'): 56}" in o,
      "frame lock: the uniform frame power equals the Galois (Frobenius) exponent of the element")
check("G4 [T]", rc == 0 and "binary local-frame x perm automorphism group order (GL(S) method): 168" in o
      and "automorphisms with a uniform frame: 168 of 168" in o and "perm images of full group == P: True" in o
      and "projective Paulis commuting with the five generators (not counted in the orders above): 2048" in o,
      "independent method (GL(S) on the binary stabiliser space, permuting the 8 subspaces K_j): the binary symplectic local-frame x "
      "permutation automorphism group of the phase-forgetting stabiliser is the same 168, all uniform-frame; Pauli and sign lifts are "
      "not counted (2048 projective Paulis commute with the five generators and are invisible to the binary frame map), so 168 is "
      "not the order of the full physical local-Clifford x permutation group")
rc, o = run('code_controls')
check("G5 [T]", rc == 0 and "max |O_h cap code group| over all 8! labellings: 24" in o,
      "largest overlap with the cube group O_h over all 8! vertex labellings is 24 (T_h type); never a 4-fold turn")
check("G6 [T]", rc == 0 and "|Aut(X-projection)| = 1344" in o,
      "the X, Z and X+Z support projections of the stabiliser group are each the [8,4,4] extended Hamming code RM(1,3) (Aut = AGL(3,2), 1344)")
check("G7 [F] control", rc == 0 and "contains all 48 cube symmetries (standard labelling): True" in o
      and "cube C3 about (111), no frame: logical X_k -> [[2], [0], [1]]" in o
      and "random [[8,3]] codes with an order-7 perm x uniform-frame symmetry: 0/100" in o,
      "numerology control: the [[8,3,2]] cube colour code also has F_8/AGL(3,2) structure and a frame-free logical 3-cycle, "
      "so neither is evidence; only the frame lock and the missing 4-fold turn are specific to [[8,3,3]]; 0/100 random [[8,3]] codes have an order-7 symmetry")
rc, o = run('logical_orbits')
check("G8 [T]", rc == 0 and "orbit size 7: min weights {4: 7}; pairwise symplectic products {0: 21}; closed under product (+0): True" in o
      and "stabiliser orders in G of the decompositions (order -> how many decompositions): {1: 504, 2: 420, 3: 168, 6: 28}" in o,
      "the binary group acts on the 63 logical Pauli classes with orbits 7, 28, 28; the 7-orbit is a commuting Lagrangian; no "
      "decomposition of the binary logical Pauli space into three orthogonal symplectic planes (three logical Pauli qubits) is "
      "invariant in the enumerated class of 1120 decompositions (largest stabiliser order 6); other tensor factorisations not searched")

print("== O: the octonion / J3(O) route")
rc, o = run('octonion_seven_sets')
check("O1 [N]", rc == 0 and "maximal anticommuting 7-sets of logical classes: 288" in o and "G-invariant 7-sets: 0" in o,
      "T1: no anticommuting 7-set of logical Paulis is invariant under the binary group (0 of 288); this rules out only such a set of "
      "logical Paulis, not octonion structure in general; the F21-invariant one (1) is forced by 288 = 1 mod 7 and does not discriminate")
rc, o = run('octonion_table')
rc2, o2 = run('octonion_jordan')
check("O2 [T]", rc2 == 0 and "signed-permutation automorphisms of O: 1344 ; pure permutation automorphisms: 21" in o2
      and "pure perms are i -> a i + b with a in {1,2,4}: True" in o2,
      "the cyclic octonion table's signed automorphisms number 1344; its pure-permutation ones are i -> ai+b, a in {1,2,4} (F21): "
      "the normaliser of the 7-cycle, true of any cyclic labelling, so the F21 match to the code is generic")
jd = [num(rf"Jordan identity defect on H_{k}\(H\) \(true quaternion subalgebra\): ([0-9.e+-]+)", o2) for k in (3, 4, 5)]
check("O3 [T]", rc == 0 and rc2 == 0 and all(x is not None and x < 1e-10 for x in jd),
      "control for the Jordan-von Neumann-Wigner bound: H_n(H) satisfies the Jordan identity for n = 3, 4, 5 (the n <= 3 cap is octonionic, "
      "and caps a matrix size; it does not select a family number)", f"defects {jd}")
check("O4 [S]", rc2 == 0 and "preimage of F21: order 168" in o2 and "orbit sizes on the 7 imaginary lines under the preimage of F21: [7]" in o2,
      "the preimage of F21 in Aut(O) has AGammaL(1,8)'s order statistics (Schur-Zassenhaus) but fixes the real unit, while the code "
      "group is transitive on the 8 qubits: the match is abstract only")
ga = num(r"generated associative algebra dim (\d+)", o2, int); ca = num(r"complex associator ([0-9.e+-]+)", o2)
gh = num(r"quaternion subalgebra: generated dim (\d+)", o2, int)
check("O7 [T]", rc2 == 0 and ga == 64 and ca is not None and ca > 1e-6 and gh == 4,
      "C x O is not M_8(C) (2026-11-14 correction of the source text): C x O has complex dimension 8 and a nonzero associator, "
      "while M_8(C) has dimension 64 and is associative; the associative algebra generated by the left multiplications of "
      "C x O on itself (C^8) is the full M_8(C); control: for the associative quaternion subalgebra the same routine gives "
      "dimension 4 (H itself), not 16", f"generated dim {ga}, complex associator {ca}, quaternion control {gh}")
print("== C: class-inverting automorphisms (Chen-Fallbacher-Mahanthappa-Ratz-Trautner type test), executed since 2026-11-14")
rc, o = run('class_inversion')
ci = {nm: (num(rf"{re.escape(nm)}[^\n]*\|Aut\| = (\d+)", o, int), num(rf"{re.escape(nm)}[^\n]*class-inverting automorphisms: (\d+)", o, int))
      for nm in ("F21 = Z7 x| Z3 (T7)", "Delta(27) = Heis(Z3)", "S3 control")}
check("C1 [T]", rc == 0 and ci["F21 = Z7 x| Z3 (T7)"] == (42, 0) and ci["Delta(27) = Heis(Z3)"] == (432, 0) and ci["S3 control"] == (6, 6),
      "brute force over generator images: F21 has 0 class-inverting automorphisms out of 42 and Delta(27) 0 out of 432; control S3 "
      "(all classes real) 6 out of 6", str(ci))
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
      "A1/A2: at m = 3 the supplied Wilson-type slab (Ls = 8) has near-wall zero modes exactly at the three X points (2 states each, one hand); "
      "an antiunitary C K with k -> -k commutes with the slab Bloch Hamiltonian")
check("M2 [F]", rc == 0 and "A3 FAIL" in o and "TEST A: FAIL" in o,
      "A3 as pre-registered FAILS: the C2 rotations' family actions carry +-i (overall operator phase unfixed). Disclosed post-hoc fix "
      "(spin-statistics g^n = (-1)^F) makes every C2 real; translations act as diag(-1,1,1) and permutations, real and non-scalar")
rc, o = run('misalignment_cp')
b1 = re.findall(r"max\|sin theta_bar\| ([0-9.e+-]+); median \|J\|/Jmax ([0-9.e+-]+)", o)
bpi = re.findall(r"branch theta_bar = pi in (\d+) of (\d+); Y_u -> -Y_u flips the branch in (\d+) of 50", o)
check("M3 [F]", rc == 0 and all(f"{t} PASS" in o for t in ('B1', 'B2', 'B3', 'B4')),
      "B: misaligned sectors (up keeps T g_u, down keeps T g_d, relative action real non-scalar) give a real tree determinant, "
      "theta_bar_tree in {0, pi} (|sin| < 1e-10, 2000 samples per pair), with median |J|/J_max ~ 0.28; aligned control J < 1e-13; "
      "generic complex Yukawas, Haar U(3) and incommensurate characters are theta-safe in < 0.5% (genericity control)",
      "; ".join(f"sin {a} J {b}" for a, b in b1[:4]))
check("M3b [F]", rc == 0 and "B1s PASS" in o and "B5 PASS" in o and len(bpi) >= 4 and all(0 < int(a) < int(n) and int(f) == 50 for a, n, f in bpi[:4]),
      "the sign branch is not selected (2026-11-14 correction of 'theta_bar_tree = 0'): in every misaligned pair both "
      "theta_bar = 0 and theta_bar = pi occur, Y_u -> -Y_u keeps the residual constraint and flips the branch, and the witness "
      "F_u = diag(-1,1,1), F_d = 1, Y_u = diag(-1,2,3), Y_d = diag(4,5,6) satisfies the residuals with theta_bar = pi",
      "; ".join(f"pi in {a}/{n}, flips {f}/50" for a, n, f in bpi[:4]))
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
check("X1 [F]", rc == 0 and "TOTAL: PASS=2 FAIL=6" in o and st == {'D1': 'FAIL', 'D2': 'FAIL', 'D2r': 'FAIL', 'D3': 'FAIL', 'D4': 'PASS',
                                                      'D5': 'PASS', 'D6': 'FAIL', 'D7': 'FAIL'},
      "the pre-registered cross-talk runner reproduces its outcome: PASS = D4 (generic vertex theta = O(1)), D5 (Ls convergence); "
      "FAIL = D1 (on-site vertex: scalar Yukawa ~ 1, J undefined), D2, D2r, and D3/D6/D7 on precision only (1e-10..1e-11 vs a 1e-12 threshold)",
      str(st))
check("X2 [F]", rc == 0 and th2 is not None and th2 > 0.1,
      "DECISIVE (D2): with each order entering the other species' densities at kappa = 1, the induced theta_bar is O(1) and flat in the "
      "sector separation (Delta = 1..18, Ls = 40): separating the sectors protects nothing; theta_ind is linear in kappa, so the mechanism "
      "needs kappa < ~1e-10 (the Nelson-Barr quality problem in lattice form)", f"min_Delta median |theta_ind| = {th2}")
check("X3 [F]", rc == 0 and th2r is not None and 1e-10 < th2r < 1e-8,
      "D2r (supplied restriction: the shallow order's density also respects the deep sector's residual antiunitary) removes the flat leak; "
      "the remainder decays with depth and reaches a few 1e-10 at Delta = 18 (4e-10 in the source's run; platform-dependent), "
      "just above the 1e-10 threshold", f"{th2r}")
rc, o = run('posthoc_degeneracy_check')
rows = re.findall(r"sv_d/sv0 \[1\.\s+1\.\s+[0-9.]+\] commutator invariant ([0-9.e+-]+)", o)
check("X4 [F] correction", rc == 0 and len(rows) >= 6 and all(float(x) < 1e-15 for x in rows),
      "post hoc symmetrised vertex (disclosed): its down Yukawa has an exactly degenerate pair (on-site scalar vertex on this slab is "
      "lambda*1 + antisymmetric, the X-node frames being quaternion units), so J = 0 exactly (commutator invariant < 1e-15); an earlier "
      "reading of |J|/Jmax 0.2-0.5 from this vertex was 0/0 noise and is withdrawn", f"{len(rows)} draws, max {max(map(float, rows)) if rows else None}")

print("== R: deriving the D2r restriction from a charge on the sector orders (criteria fixed before each run; v2 changes disclosed before its run)")
rc, o = run('charged_orders')
st = {t_: ('PASS' if re.search(rf"^PASS: {t_} ", o, re.M) else 'FAIL' if re.search(rf"^FAIL: {t_} ", o, re.M) else None)
      for t_ in ('E0', 'E1', 'E2', 'E3', 'E3h', 'E4', 'E5', 'E6', 'E7')}
c2 = num(r"E7 quality bound: c2_min = ([0-9.e+-]+)", o); e3h = num(r"E3h lattice-scale order eps = 0\.2: min_Delta median theta_bar_ind = ([0-9.e+-]+)", o)
check("R1 [F]", rc == 0 and "TOTAL: PASS=8 FAIL=1" in o and st == dict(E0='PASS', E1='PASS', E2='PASS', E3='PASS', E3h='FAIL', E4='PASS', E5='PASS',
                                                         E6='PASS', E7='PASS'),
      "charged orders (U(1)_H, bond Yukawa vertices allowed), with the thresholds as run: every density coupling linear in an order "
      "is forbidden exactly (E0); a real tree determinant, theta_bar_tree in {0, pi} with the branch not selected, median |J|/Jmax "
      "0.09 and no degenerate draws (E1); the breaking control restores theta = c1*eps (E4); aligned control J < 1e-15 (E5); "
      "Ls-converged (E6)", str(st))
for line in re.findall(r"CRITERIA [^\n]*", o):
    print("  " + line)
check("R2 [F]", rc == 0 and c2 is not None and 1 < c2 < 1e3 and e3h is not None and e3h > 1e-2,
      "but the charge-allowed bilinears (bond currents Im phi*(r) phi(r+e), |phi_d|^2 patterns, phi_u phi_d) leak at second order, "
      "theta = c2*eps^2: quality bound eps = v/Lambda < ~1e-6; a lattice-scale order (eps = 0.2) gives theta = O(0.1) (E3h FAIL)",
      f"c2_min {c2}, theta(eps=0.2) {e3h}")
rc, o = run('wrong_sector')
cw = num(r"min median c_w = ([0-9.e+-]+)", o)
check("R3 [F]/[T]", rc == 0 and "TOTAL: PASS=7 FAIL=0" in o and cw is not None and cw > 1,
      "the same charge leaves the wrong-sector Yukawas phi_u^* Q D, phi_d^* Q U neutral; they leak at dimension 4 (needs kappa_w < ~1e-11). "
      "A U(1) forbidding both exists iff it has a QCD anomaly (PQ); an anomaly-free Z_N (N <= 12) iff 3 | N, and each leaves an accidental "
      "PQ in the renormalisable order potential (electroweak-scale axion); the D2r rule is therefore not derived by a charge",
      f"min median c_w {cw}")

print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
sys.exit(0 if NP[1] == 0 else 1)
