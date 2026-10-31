"""Build the source-located mapping audit. Text bookkeeping, not a physics check."""
from pathlib import Path
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[1]
STATUSES = {"LANDED", "CONDITIONAL", "OPEN", "AT-RISK"}
evidence = []
QUOTE_STARTS = {
    ("CODEX_REVIEW_NONFREE.md", 299): "Single most dangerous unverified item:",
    ("REVIEW2_REC.md", 327): "I did not establish",
    ("CODEX_REVIEW_OSLEAF.md", 281): "No unconditional continuum",
    ("CODEX_REVIEW_HINT2.md", 268): "The single most dangerous unverified bridge",
    ("REVIEW_RD.md", 217): "An integrated tail probability",
    ("CODEX_REVIEW_TUNIF2.md", 284): "Thus the quoted general-data line-sum inequality",
}


def cite(file, line, end=None, words=30):
    """Quote a bounded actual passage; keep the complete passage in evidence JSON."""
    lines = (BASE / file).read_text().splitlines()
    end = line if end is None else end
    full = " ".join(lines[line - 1:end]).strip()
    # Skip section headings in the short quote, without altering the saved passage.
    excerpt_lines = [x for x in lines[line - 1:end] if not x.lstrip().startswith("#")]
    clean = re.sub(r"\s+", " ", " ".join(excerpt_lines).replace("**", "").replace("`", "")).strip()
    clean = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", clean)
    marker = QUOTE_STARTS.get((file, line))
    if marker:
        assert marker in clean, (file, line, marker)
        clean = clean[clean.index(marker):]
    tokens = clean.split()
    quote = " ".join(tokens[:words])
    suffix = " …" if len(tokens) > words else ""
    assert quote, (file, line, end)
    item = dict(file=file, line=line, end=end, full=full, quote=quote,
                sha256=hashlib.sha256((BASE / file).read_bytes()).hexdigest())
    evidence.append(item)
    locator = f"{file}:{line}" + (f"–{end}" if end != line else "")
    return f'“{quote}{suffix}” ([{locator}]({file}))'


nodes = []


def node(id, title, status, scope, file, line, end=None):
    assert status in STATUSES
    row = dict(id=id, title=title, status=status, scope=scope,
               evidence=cite(file, line, end))
    nodes.append(row)
    return row


def table(rows, first="Node / export"):
    out = [f"| {first} | One mapping status and exact scope | Source quotation |",
           "|---|---|---|"]
    for r in rows:
        clean = lambda x: x.replace("|", "\\|").replace("\n", " ")
        out.append(f"| **{r['id']} — {clean(r['title'])}** | **{r['status']}**. {clean(r['scope'])} | {clean(r['evidence'])} |")
    return "\n".join(out)


# The 26 displayed nodes of ASSEMBLY55, with later scoped providers substituted.
node("N0", "T_OS", "OPEN", "Actual R4 SU(N) OS construction and absolute non-freeness on one algebra; neither route supplies all inputs.", "ASSEMBLY55.md", 128, 135)
node("N1F", "Flat assembly", "CONDITIONAL", "One algebra, common sequence, actual regularity/positivity, full symmetry and continuous strict witness; the original closure implication survives.", "CODEX_REVIEW_ASSEMBLY.md", 210)
node("N1S", "Sphere assembly", "CONDITIONAL", "Fixed-R continuum states, common local algebra, SO(5)/pole RP, radius-uniform regularity and witness, then R→∞; regulator admissibility is separate.", "ASSEMBLY55.md", 147, 157)
node("N2", "H_reg", "CONDITIONAL", "Actual N1 source contract plus N2 flow positivity imply separated regularity; SP→TP→EXT is available. Actual source estimates and reconstruction seed are still required; ordinary moments are not thereby supplied.", "CODEX_REVIEW_SRC2.md", 263, 270)
node("N3", "H_RP", "CONDITIONAL", "Finite bare-marginal/lattice RP and corrected geometric half-arcs are reviewed. Continuum passage needs the actual convergent hierarchy on the stated test domain.", "REVIEW_HRP_HALF_ARC_ASTRA.md", 74)
node("N4", "H_Euc", "OPEN", "All products on the same algebra. Flat needs N11/N12. Sphere uses SS: N13/Ward OR N14/full comparison, with shared sphere transfer and radius inputs. Pair invariance alone is insufficient.", "CODEX_REVIEW_ASSEMBLY.md", 233)
node("N5", "H_int", "AT-RISK", "An absolute witness on the reconstructed algebra and actual YM upper/lower/moment estimates are missing. Five alternatives are separated below.", "CODEX_REVIEW_ASSEMBLY.md", 237)
node("N6", "ALG and target contract", "OPEN", "REC now supplies a restricted flat-test construction, but the chosen witness, physical/free identification, multiplication and support maps must match it; no automatic ordinary-product extension.", "REVIEW2_REC.md", 327, 330)
node("N7", "SEQ / DIAG", "CONDITIONAL", "Common countable family, per-radius and outer convergence, compatible identifications. DIAG itself needs no new uniform-in-R cutoff-rate theorem.", "CODEX_REVIEW_ASSEMBLY.md", 206)
node("N8", "TRAJ", "OPEN", "Common normalized bare trajectory, actual finite-u/finite-volume effective flow, continuity and tuning. New volume-first one-loop coefficients do not complete this.", "CODEX_REVIEW_ASSEMBLY.md", 229, 230)
node("N9", "REC", "CONDITIONAL", "REC_CONT E0′–E3 seed plus reality/normalization and exhaustion feed REC_LIB for finite Cartesian tensors of flat tests; actual YM seed, sharp-time/general tensor extensions remain inputs.", "REVIEW2_REC.md", 3, 7)
node("N10", "SRC", "AT-RISK", "Actual all-coarse, all-order, normalized quantum source hierarchy, including failures, holes and higher-level induction. Selected-sector mechanisms exist but do not supply it.", "CODEX_REVIEW_SRC2.md", 270, 272)
node("N11", "Flat CD / SRC-I5", "OPEN", "Real/complex tilted envelopes, coarse-source control and appropriate all-order decay for actual Wilson law; exact Markov identities are not decay estimates.", "CODEX_REVIEW_SRCCD.md", 401, 407)
node("N12", "TQ", "AT-RISK", "Flat far-shell torque remains unverified; available sufficient decay criteria and pair reductions are not an actual Wilson estimate or an impossibility theorem.", "CODEX_REVIEW_TQ.md", 798, 800)
node("N13", "Sphere UV package", "AT-RISK", "Actual bulk/profile/local transfer, all-coarse seam transparency, W1/W3 for all products and radius-uniform limits. The all-coarse condition is load-bearing.", "SPHERE55.md", 657, 663)
node("N14", "Rotated universality", "CONDITIONAL", "Alternative sphere symmetry supplier: full two-theory conditional comparison, curved/profile/seam inputs, common algebra and radius bounds. Fixed-torus UNIV-T is support, not an R4/TQ bypass without the exterior-law/limit bridge.", "CODEX_REVIEW_UNIV.md", 443, 445)
node("N15", "YM witness bounds", "AT-RISK", "Route-specific lower matching and upper/moment estimates on the same observable. LGF is supplied; PL-1L and its actual consumers are not.", "CODEX_REVIEW_NONFREE.md", 299)
node("N16", "Coupling coefficient / flow", "CONDITIONAL", "UL4/every-increment B-BR now holds under normalized-tree/linear/jet/residual contracts, in volume-first convention. Nonlinear finite-u RG, finite-volume uniformity and tuning remain N8 inputs.", "REVIEW_UNIFORM_ONE_LOOP_COUPLING_ASTRA.md", 372, 378)
node("N17", "BFT-0/1/2", "CONDITIONAL", "Named linear inputs, a GV slice and a small global chart give scoped critical-point results; actual regional/background/minimum consumers still need C.", "CODEX_REVIEW_KOFF.md", 714, 724)
node("N18", "BFT-3", "CONDITIONAL", "Corrected global-chart routes retain H1/H2 and action/source matching. The local qualitative R premise has a reviewed provider; it is not a wholly missing lemma.", "CODEX_REVIEW_RLOC.md", 203, 217)
node("N19", "BFT-4", "CONDITIONAL", "E^cb global-chart estimates require their corrected linear/GV/EP/CD/Ward inputs. Gauge averaging has a finite invariant-domain theorem, not automatic full consumer identification.", "CODEX_REVIEW_BFT4B.md", 275, 283)
node("N20", "BFT-5 / background linear stability", "OPEN", "The Z=1/pure-gauge results and conditional GA/alignment reductions survive; actual general-background alignment with uniform quotient/source/defect and local-to-global bounds remains missing. Full normalized return is D, a distinct obligation.", "CODEX_REVIEW_BGT.md", 395)
node("N21", "LF mechanism", "OPEN", "Actual adequate large-field/observable-weighted control remains an input. LF-inst is one sufficient option, not a mandatory T_OS leaf or a proved no-go.", "CODEX_REVIEW_ASSEMBLY.md", 53, 57)
node("N22", "N5/N6 per-step fluctuation estimates", "OPEN", "Actual higher-level covariance decay and per-step complex/source polymer bounds on the required regions. Selected finite-sector covariance and kernel results supply parts, not the full higher-level NA-H_loc/source induction.", "ASSEMBLY55.md", 373, 375)
node("N23", "Constants / feasibility", "OPEN", "Uniform simultaneous two-sided smallness and complex-width windows. Acyclicity of a strict subgraph does not establish their feasibility.", "CODEX_REVIEW_DAG.md", 337, 338)
node("N24", "Linear package", "CONDITIONAL", "Seventeen estimates have a reviewed restricted scope with coefficient 9 and a smaller unprimed decay range. Do not reuse the original entire primed range; other consumers retain their exact hypotheses.", "CODEX_REVIEW_LANEA.md", 425, 429)
assembly_nodes = list(nodes)

# Unresolved terminal interfaces for the candidate chains, not independent walls.
node("O", "Common target and observable contract", "OPEN", "Pin algebra, normalization, support/quotient maps and comparator class; e-only canonical separation is not silently an absolute physical free-class theorem.", "CODEX_REVIEW_ASSEMBLY.md", 219, 220)
node("C", "Actual local/background/action interface", "OPEN", "Curvature-small, regional/frozen-boundary, holonomy and minimum/critical-value matching for the selected return, including N20. MIN-cb is sufficient, not uniquely necessary; scoped restricted-minimum and alignment mechanisms survive.", "CODEX_REVIEW_MINCB.md", 254)
node("D", "Complete normalized return", "AT-RISK", "RD B1–B3: actual identity retaining failures and complements, common complex domains/nonzero reference, full source norm through holes and level induction. Concrete hard-indicator norm mismatch makes this more than missing bookkeeping.", "REVIEW_RD.md", 217, 234)
node("U", "Coupled actual flow and trajectory", "OPEN", "Close flow/large-field construction without mutual assumptions, finite-u remainder and finite-volume/continuity inputs, FI-1 and F-tune. One-loop/tree output is only an input.", "CODEX_REVIEW_ASSEMBLY.md", 229, 230)
node("S", "Actual all-order source / seed estimates", "AT-RISK", "Prove N1+N2/SP, all-coarse source radii, mixed products, insertion growth and large-distance bounds on the chosen trajectory. This then feeds the existing EXT/REC implications; EXT is not charged as another missing abstract theorem.", "CODEX_REVIEW_OSLEAF.md", 281)
node("K", "Simultaneous quantitative windows", "OPEN", "Actual constants must satisfy all two-sided feasibility requirements uniformly; use corrected conventions and consumer-specific bounds.", "CODEX_REVIEW_DAG.md", 337, 338)
node("FT", "Flat torque / TQ", "AT-RISK", "Actual normalized far-shell torque vanishes, with all-order extension as required; reviewed RA/RA-1 criteria have not been supplied for Wilson YM.", "CODEX_REVIEW_TQ.md", 776, 800)
node("FA", "Flat all-product symmetry inputs", "OPEN", "CD/SRC-O/SRC-W and source-contact/covariance identities for every product, not only the centered two-point orbit. An alternate reflection/universality route must supply its own full law and same-state transfer.", "REVIEW_EUCLIDEAN_ROTATION_IMPORT_ASTRA.md", 455, 457)
node("SP", "Sphere geometry / local transfer", "AT-RISK", "F13: transfer torus estimates to sphere cells with boundaries, weights/profile and locality; five exact RP planes do not supply global chessboard estimates.", "ASSEMBLY55.md", 475, 480)
node("SS", "All-coarse sphere symmetry / seam interface", "AT-RISK", "Two alternative suppliers, not cumulative requirements: (W) all-product Ward W0/N5-RG/W1/W3, OR (V) N14's complete two-theory all-coarse comparison with curved/profile and transparent-seam inputs. Neither is implemented; typical-field-only Ward bounds leave an infrared covariance.", "CODEX_REVIEW_UNIV.md", 496)
node("SR", "Radius-uniform sphere hierarchy", "OPEN", "Actual fixed-R continuum states, position/radius-uniform U-sep and witness bounds on common domains; then the already proved diagonal applies.", "ASSEMBLY55.md", 147, 157)
node("SW", "Flat-Wilson selection identification", "OPEN", "Additional sphere obligation only under the strict reading requiring a limit of flat Wilson lattices; omit only after the target admits sphere regulators independently.", "SPHERE55.md", 664, 666)
node("E4I", "4D-flowed E: OS/free identification", "AT-RISK", "A product-preserving physical/OS identification is missing; the proposed ID-natural contraction fails to preserve products. A flowed one-point statistic alone is not an OS invariant.", "CODEX_REVIEW_HINT2.md", 268, 268)
node("E4M", "4D-flowed E: YM estimates", "AT-RISK", "Actual TS-up/TS-low/MOM-E with the right uniformity. LF-inst is an optional sufficient method, with observable-weighted/localized alternatives not excluded.", "CODEX_REVIEW_ASSEMBLY.md", 234)
node("BI", "Sharp-time B: algebra and free class", "AT-RISK", "ALG-B mixed hierarchy, SHARP and support/covariance with strict-local comparator identification. Reviewed WT0 separates marked systems, not arbitrary identifications or e-only F1.", "REVIEW2_WT0.md", 246, 247)
node("BM", "Sharp-time B: YM estimates", "AT-RISK", "MOM2 and TS-up/TS-low plus uniform sharp-time localization/approximation. Finite-t finiteness does not prove SHARP.", "REVIEW2_WT0.md", 276, 283)
node("EI", "Separated e: absolute comparator", "AT-RISK", "AF-e excludes the declared finite canonical Wick/free class and stated mixtures, but a scalar GFF meets AF-e. Broader absolute non-freeness needs a valid identification/classification or another witness.", "CODEX_REVIEW_NONFREE.md", 297)
node("EM", "Separated e: actual lower/upper match", "AT-RISK", "PL-1L, K-dec and FLOW-pw for the actual normalized clover observable, at all short scales; LGF is supplied. Lower matching cannot be inferred from RP or source upper bounds.", "CODEX_REVIEW_TSE.md", 243)
node("HI", "Hard block Psi: OS/free identification", "AT-RISK", "Block-observable covariance/OS identification and absolute comparator, including valid transfer from the specified S4c comparator, are not inherited from the soft field or ID-natural.", "ASSEMBLY55.md", 558, 560)
node("HM", "Hard block Psi: witness matching", "AT-RISK", "Witness-specific H-Bal-1/H-loc-LF/H-sg lower/upper estimates for the actual hard law. D/U/S already carry shared hard construction/flow/hierarchy work; HRT is one proposed sufficient construction, not another mandatory duplicate. For bounded block generators MOM/CONV are automatic under the matched law; no extra flowed SRC or LF-inst witness condition.", "HINT2_55.md", 415, 418)
node("PI", "Soft block Psi: OS/free identification", "AT-RISK", "The soft block needs its own common-algebra/free identification; changing block scheme does not solve the observable mismatch.", "ASSEMBLY55.md", 744, 747)
node("PM", "Soft block Psi: NOISE-ADD and ANTI-flat", "AT-RISK", "Both actual YM noise-addition and anti-concentration/lower-bound inputs remain unproved; the fifth witness is not omitted merely because it was appended later.", "ASSEMBLY55.md", 744, 747)
leaf_nodes = nodes[len(assembly_nodes):]

common = ["O", "C", "D", "U", "S", "K"]
geometry = {"flat": ["FT", "FA"], "sphere": ["SP", "SS", "SR", "SW"]}
witnesses = {"4D-flowed E": ["E4I", "E4M"], "sharp-time B / W_T0": ["BI", "BM"],
             "separated e": ["EI", "EM"], "hard block Psi": ["HI", "HM"],
             "soft block Psi": ["PI", "PM"]}
routes = [dict(id=f"{g}-{i}", geometry=g, witness=w, leaves=common + geometry[g] + v)
          for g in geometry for i, (w, v) in enumerate(witnesses.items(), 1)]

# Full legacy registry crosswalk: each export has one status at its quoted scope.
inventory = []


def result(id, name, status, scope, file, line, end=None):
    assert status in STATUSES
    inventory.append(dict(id=id, title=name, status=status, scope=scope,
                          evidence=cite(file, line, end)))


result("L01", "TUNIF", "CONDITIONAL", "Trivial-background cubic control under NQ-1 and named linear imports → N24/N16. Not general backgrounds.", "PROOF.md", 486)
result("L02", "COfun", "CONDITIONAL", "Composite-co-closed source estimates under lane-A/package inputs → N24/N17.", "CODEX_REVIEW_C2.md", 306, 312)
result("L03", "GZ no-go withdrawal", "LANDED", "Correction of the fixed-representative inference; preserve it as a guard on C, not as a constructive theorem or universal obstruction.", "PROOF.md", 488)
result("L04", "CC0 at every critical point: counterexample", "LANDED", "Specified pure-gauge counterexample; Lemma CD retains root-pinned scope. Distinct from TOP-cc's stronger axial-order independence claim.", "PROOF.md", 489)
result("L05", "NLOC line-sum proof-step failure", "LANDED", "Actual chain counterexample to the quoted line-sum bound, not to the repaired T-free representative; protects N24 scope.", "CODEX_REVIEW_TUNIF2.md", 284, 285)
result("L06", "TOP-cc", "CONDITIONAL", "Trivial-background source/top response under named inputs → N17/N24; higher-order frontier superseded by L18.", "CODEX_REVIEW_TOPCC.md", 348, 363)
result("L07", "TR quadratic", "CONDITIONAL", "Exact critical-point family and named source estimates → N17; L18 supplies the later full nonlinear critical-point implication.", "CODEX_REVIEW_TR.md", 272, 284)
result("L08", "Sphere equatorial RP", "LANDED", "Finite equatorial construction → N3; later pole/half-arc reviews extend only their stated geometries and conditional limits.", "PROOF.md", 493)
result("L09", "Smallness DAG", "LANDED", "Strict subgraph acyclicity is checked bookkeeping → K. It does not prove full quantitative feasibility or dissolve coupled windows.", "CODEX_REVIEW_DAG.md", 333, 338)
result("L10", "K-sigma", "CONDITIONAL", "GV slice and corrected linear package → global-chart N17; no local curvature-small extension.", "CODEX_REVIEW_KOFF.md", 714, 724)
result("L11", "GF-E", "CONDITIONAL", "Named S_E/slice or orbit norm at zero weight → N24/N17; not every gauge representative.", "CODEX_REVIEW_GSHARP.md", 492, 505)
result("L12", "COF-m", "CONDITIONAL", "Weighted composite source estimates → N17/N18, with later LANEA smaller unprimed range controlling applicable reuses.", "CODEX_REVIEW_COFM.md", 373, 394)
result("L13", "ROTDEF", "CONDITIONAL", "Exact finite Ward identities plus CD/SRC inputs reduce tested-orbit invariance to normalized torque → FT/FA; not all-order OS1.", "CODEX_REVIEW_ROTDEF.md", 465, 469)
result("L14", "HINT", "CONDITIONAL", "Comparator theorem for specified quadratic abelian observables; H-RED needs actual matching/identification → E4I/E4M.", "CODEX_REVIEW_HINT.md", 287, 293)
result("L15", "RLARGE W-cb / FI-1", "CONDITIONAL", "Uniform trial/continuity hypotheses give per-level coupling fixed point → U/K; no actual all-level flow or final live margin.", "CODEX_REVIEW_RLU.md", 377, 383)
result("L16", "NODEA", "CONDITIONAL", "Gaussian convex-core reductions and DOM bounds → D; actual nonlinear return remains open.", "CODEX_REVIEW_NODEA.md", 269, 276)
result("L17", "Node A residual", "LANDED", "Scoped counterexamples and repaired BL-TILT theorem; diagnostic for D, not a no-go for all possible return mechanisms.", "CODEX_REVIEW_NRES.md", 469, 478)
result("L18", "HIGHER / TR-infinity", "CONDITIONAL", "Full nonlinear critical-point implication under accepted linear/critical-point hypotheses → N17/N18; not off-critical or arbitrary-background control.", "CODEX_REVIEW_HIGHER.md", 310, 320)
result("L19", "GV-E", "CONDITIONAL", "Slice contraction/weighted estimates under named inputs → N17; direct restriction identity fails, NSL is a sufficient repair.", "CODEX_REVIEW_GV.md", 422, 429)
result("L20", "FLOW55", "CONDITIONAL", "Corrected phi-normalized coefficient reduction → N16; later coordinator chain advances UIR, not full nonlinear U.", "CODEX_REVIEW_FLOW55.md", 332, 339)
result("L21", "UNIV", "CONDITIONAL", "All-background conditional comparison hypotheses → N14; actual comparisons and all-algebra limit identification remain open.", "CODEX_REVIEW_UNIV.md", 482, 497)
result("L22", "a_RS / KN pricing", "LANDED", "No consumer on the cited live v3 unreturned-defect pricing route; historical/local kernel statements are not live margin gains. Off that critical path.", "PROOF.md", 509)
result("L23", "BGT", "CONDITIONAL", "Alignment/quotient hypotheses give transfer; exact pure-gauge case reviewed → C. Nontrivial holonomy and general backgrounds are additional work.", "CODEX_REVIEW_BGT.md", 387, 396)
result("L24", "TQ reductions", "CONDITIONAL", "Normalized centered-orbit identity and sufficient decay criteria → FT. No Wilson TQ proof, universal impossibility or all-order invariance.", "CODEX_REVIEW_TQ.md", 755, 779)
result("L25", "SRCCD", "CONDITIONAL", "Recursions and decay consequences under actual source/correlation hypotheses → S/FA; no automatic decay from Markov recursion.", "CODEX_REVIEW_SRCCD.md", 401, 407)
result("L26", "BFT3", "CONDITIONAL", "Global-chart derivative routes with exact H1/H2 etc. → N18. RLOC supplies the local R premise only at its scope.", "CODEX_REVIEW_BFT34.md", 255, 262)
result("L27", "BALX", "LANDED", "Scalar/abelian finite-model calculations are useful methods for C/U, not a supplied actual 4D nonlinear inverse or flow.", "CODEX_REVIEW_BALX.md", 245, 251)
result("L28", "NSL", "CONDITIONAL", "Global-chart tower identification with named radii/hypotheses → N17; no uniform BR1/local/minimum identification.", "CODEX_REVIEW_NSL.md", 211, 218)
result("L29", "UIR", "CONDITIONAL", "Finite Schur/weighted-jet plus rho-null criterion → N16; later residual/jet/UL providers replace portions of its old open frontier.", "CODEX_REVIEW_UIR.md", 211, 219)
result("L30", "BFT4(a)", "CONDITIONAL", "Centered cancellations and H2W/global-chart estimates with actual linear/projection inputs → N19; RLOC discharges local R only.", "CODEX_REVIEW_BFT4W.md", 241, 249)
result("L31", "SRCAN", "CONDITIONAL", "Finite source/tree/analytic implications with n-uniform radius and matching norms → S; not an actual full source hierarchy.", "CODEX_REVIEW_SRCAN.md", 328, 339)
result("L32", "HINT2", "CONDITIONAL", "Expanded explicit comparator mathematics and H-RED under F-tune/TS/MOM → witness leaves; absolute ID-natural bridge remains open.", "CODEX_REVIEW_HINT2.md", 265, 268)
result("L33", "SPHERE", "CONDITIONAL", "Finite geometry/RP and corrected Ward pair reductions → N3/SS; all-product actual hypotheses and construction remain open.", "CODEX_REVIEW_SPHERE.md", 329, 337)
result("L34", "ALIGN", "CONDITIONAL", "RED-prime from actual alignment/NC data → C; source-specific chart obstruction is not universal nonexistence.", "CODEX_REVIEW_ALIGN.md", 245, 251)
result("L35", "ASSEMBLY", "CONDITIONAL", "DIAG, finite-chain GERM, row-sum and original closure implications → N1/N7/C/N16; scoped logical counterexamples constrain arrows.", "CODEX_REVIEW_ASSEMBLY.md", 204, 213)
result("L36", "LCONV", "LANDED", "Specified bare convexity counterexamples → D mechanism selection; no unrestricted LC1 or universal convexity/Peierls no-go.", "CODEX_REVIEW_LCONV.md", 261, 267)
result("L37", "BFT4(b)", "CONDITIONAL", "Finite invariant-domain averaging, factors one uncentered/two centered → N19; actual representation/consumer identification remains input.", "CODEX_REVIEW_BFT4B.md", 275, 283)
result("L38", "OFFGLOB", "CONDITIONAL", "Local algebra and conditional off-chart pieces → C; no full off-background inverse or universal no-go.", "CODEX_REVIEW_OFFGLOB.md", 331, 340)
result("L39", "LARGE", "LANDED", "Scoped TL/PP/DENSE/MIS/COLKA facts and counterexamples → D; no full returned zero-free theorem or endorsed replacement v3.", "CODEX_REVIEW_LARGE.md", 305, 309)
result("L40", "SEAM", "CONDITIONAL", "Repaired coarse-image and Ward/source identities, N5 sum under three uniform inputs → SS; no actual all-coarse/all-product closure.", "CODEX_REVIEW_SEAM.md", 231, 238)
result("L41", "RLOC", "CONDITIONAL", "Qualitative local R follows from finite-word/maximizer identities → N18/N19. Finite replacement constant is proved, original printed K1 is not certified.", "CODEX_REVIEW_RLOC.md", 203, 217)
result("L42", "OSLEAF", "CONDITIONAL", "Separated domain/RP geometry and SP→TP→EXT→closure under actual estimates → N2/N3/N9. REC now supplies explicit reconstruction machinery.", "CODEX_REVIEW_OSLEAF.md", 278, 281)
result("L43", "ALIGN2", "CONDITIONAL", "Flat log-chart/alignment pieces and corrected RED under actual input → C; full periodic/covariant transfer not supplied.", "CODEX_REVIEW_ALIGN2.md", 316, 328)
result("L44", "NONFREE", "CONDITIONAL", "Canonical finite Wick/free comparator theorem plus conditional H-RED-e → EI/EM; GFF counterexample limits the conclusion.", "CODEX_REVIEW_NONFREE.md", 294, 299)

# Eight later assembly-support reviews.
result("A01", "STEP", "CONDITIONAL", "Linear threshold, exact action/single-normalizer statements → D/N22; full normalized history step remains OPEN.", "CODEX_REVIEW_STEP.md", 313, 318)
result("A02", "MINCB", "CONDITIONAL", "Restricted-minimum mechanism under radius/residual inputs → C; regional centered/boundary consumer remains open.", "CODEX_REVIEW_MINCB.md", 248, 254)
result("A03", "B2", "CONDITIONAL", "Conditional critical-value Hessian estimates → C/N17; no critical/minimum-action identification.", "CODEX_REVIEW_B2.md", 232, 237)
result("A04", "LANEA", "CONDITIONAL", "Seventeen scoped estimates, coefficient 9, smaller unprimed rate → N24. Do not promote the original full primed interval.", "CODEX_REVIEW_LANEA.md", 425, 429)
result("A05", "SRC2", "CONDITIONAL", "N1+N2 imply separated H_reg → N2; actual complete source representation and both hypotheses remain inputs.", "CODEX_REVIEW_SRC2.md", 263, 272)
result("A06", "TSE", "CONDITIONAL", "PL-1L/K-dec/flow/LGF imply two-sided e bounds → EM; LGF supplied by later lane, PL-1L not supplied.", "CODEX_REVIEW_TSE.md", 237, 243)
result("A07", "SPHERE2", "CONDITIONAL", "Ward/matching implications and allowed two-sided dimension-3 mixed seam operator → SS. No established no-tuning theorem.", "CODEX_REVIEW_SPHERE2.md", 242, 250)
result("A08", "OFFGLOB2", "CONDITIONAL", "Corrected algebra/relative-root patching → C; actual paired reset self-map, OFF/ID/BFT3-off/HINV remain open.", "CODEX_REVIEW_OFFGLOB2.md", 341, 347)

# Queue lanes explicitly named in the author brief, with latest affected review.
result("Q01", "HRP", "CONDITIONAL", "Finite bare/pole RP plus repaired half-arc geometry → N3; actual continuum hierarchy is an input. REVIEW2_HRP and R2 are superseded only on the half-arc correction.", "REVIEW_HRP_HALF_ARC_ASTRA.md", 74)
result("Q02", "REC_LIB", "CONDITIONAL", "Finite Cartesian flat-test hierarchy satisfying explicit seed/growth/RP inputs → reconstruction N9, not actual YM/unique vacuum/gap.", "REVIEW2_REC.md", 3, 7)
result("Q03", "REC_CONT", "CONDITIONAL", "E0′–E3 plus reality/normalization/exhaustion → REC_LIB. Cross-family spot review (REVIEW_XFAM_REC_CONT_SPOT:13–18) covers part-(2) exhaustion only, not the seed or whole theorem.", "REVIEW_REC_CONT_R2.md", 3, 9)
result("Q04", "LGF", "LANDED", "Free order-two kernel/magnetic-variance library now adopted by TSE → EM; actual YM lower matching remains separate.", "REVIEW2_LGF.md", 8, 28)
result("Q05", "W_T0", "CONDITIONAL", "Marked-system separation under exact comparator/domain/SHARP and moment assumptions → BI/BM; not absolute arbitrary free identification or the older e-only F1 claim.", "REVIEW2_WT0.md", 7, 10)
result("Q06", "LIB1", "CONDITIONAL", "Finite-graph A–C/H24 analytic machinery with actual identity, prefactors and strong full-history norm inputs → D/S; holes/sea/induction not supplied.", "REVIEW2_LIB1.md", 230, 240)
result("Q07", "SOFTHARD", "CONDITIONAL", "Finite comparison memo under return/kernel/existence hypotheses → HM and route selection; KEEP-SOFT is provisional, not a proved optimality theorem.", "REVIEW2_SOFTHARD.md", 100, 108)
result("Q08", "RD requested full theorem", "OPEN", "Source review HOLD; exact bare identities and abstract mixed expansion survive, but B1–B3 actual full returned density/complex normalization/induction are missing. No pass-2 source edit at this snapshot.", "REVIEW_RD.md", 3, 15)

# Coordinator units: branch-reviewed exports, not retained promotions.
result("C01", "RECOVERY_UIR", "CONDITIONAL", "Finite-volume germ and fixed-depth periodization reviewed; common weighted cubic/quartic kernels need H1/H2/H3 → N16. Later jet/residual chain strengthens only named parts.", "REVIEW_RECOVERY_UIR_ASTRA.md", 152, 156)
result("C02", "RECOVERY_ALIGNMENT", "CONDITIONAL", "Finite-lattice implications → C; generic NC/log, weighted/global/background inverse interfaces remain inputs.", "REVIEW_RECOVERY_ALIGNMENT_ASTRA.md", 168)
result("C03", "RECOVERY_CLUSTER", "CONDITIONAL", "Generic polymer construction under corrected ID/nonzero-prefactor/norm hypotheses → D/S; actual history/source induction not supplied.", "REVIEW_RECOVERY_CLUSTER_ASTRA.md", 23, 35)
result("C04", "SOURCE_LOCAL_RETURN", "CONDITIONAL", "Level-zero finite-volume trivial-coarse/global-chart atoms and return → D/S; not full normalized faces, complements, holes, arbitrary coarse fields or higher levels.", "REVIEW_SOURCE_LOCAL_RETURN_ASTRA.md", 517, 530)
result("C05", "SOURCE_LOCAL_RETURN_CONTINUATION", "CONDITIONAL", "Selected empty-history small-chart sector → D/S; general Xi_h/Den_Y/collars/holes and induction outside scope.", "REVIEW_SOURCE_RETURN_CONTINUATION_ASTRA.md", 3, 8)
result("C06", "SOURCE_LOCAL_HISTORY_RETURN", "CONDITIONAL", "Level-zero exact replacement and successful pointwise gas → D/S; failure f_Y and final interacting sea expectation remain unestimated.", "REVIEW_SOURCE_HISTORY_RETURN_ASTRA.md", 3, 7)
result("C07", "SOURCE_SEA_CONSTRUCTION", "CONDITIONAL", "Bounded sea-model unit → D/S; actual correlated integrated activities and nonzero complex average remain inputs, not a fixed-V full logarithm.", "REVIEW_SOURCE_SEA_CONSTRUCTION_ASTRA.md", 215, 221)
result("C08", "SOFT_FLUCTUATION_COVARIANCE", "CONDITIONAL", "Identity-background Gaussian reference/restricted integral after chart repair → C/D; arbitrary coarse fields, hard histories and complement remain outside scope.", "REVIEW_SOFT_FLUCTUATION_COVARIANCE_ASTRA.md", 3, 11)
result("C09", "COVARIANT_SOFT_BACKGROUND", "CONDITIONAL", "Actual finite-u critical density/Gaussian reference on very small coarse-curvature domain → C/D; full cut/complement expectation remains outside scope.", "REVIEW_COVARIANT_SOFT_BACKGROUND_ASTRA.md", 15, 19)
result("C10", "COVARIANT_SOURCE_ACTIVITY", "CONDITIONAL", "Selected-sector SA1–SA34 → D/S; both complements excluded, original growing-p radius narrowed. FR later repairs radius on a matched selected domain only.", "REVIEW_COVARIANT_SOURCE_ACTIVITY_ASTRA.md", 3, 15)
result("C11", "FIXED_SOURCE_RADIUS", "CONDITIONAL", "Positive rho independent of u/T/p and selected nonlinear zero-free integral, under its shrinking-curvature/size conditions → D/S; both complements, excluded coarse fields/holes and full normalization remain.", "REVIEW_FIXED_SOURCE_RADIUS_ASTRA.md", 9, 11)
result("C12", "COVARIANT_COMPLEMENT", "CONDITIONAL", "Original-Haar cap/conditional-density/shell estimates → D; not full connected complement, selector boundaries, whitening locality or normalized sea nonvanishing.", "REVIEW_COVARIANT_COMPLEMENT_ASTRA.md", 3, 7)
result("C13", "CUT_SECTOR_COERCIVITY", "CONDITIONAL", "CS1–29 displayed model and CS30–33 under SA/CB/H → D; connected complement paying exterior/reference cost and full complex source log remain open.", "REVIEW_CUT_SECTOR_COERCIVITY_ASTRA.md", 13, 14)
result("C14", "FINITE_COUPLING_KERNEL", "CONDITIONAL", "Scalar-kernel/local preintegration FK2/FK16 and restricted CB14 → U/D; interacting remainder with hard/history complements and marginal projection remains input.", "REVIEW_FINITE_COUPLING_KERNEL_ASTRA.md", 5, 10)
result("C15", "RESIDUAL_DETERMINANT", "CONDITIONAL", "Finite Hodge/Schur/moving-Gram/model-pole identities; model zero residue under named contracts → N16; actual matching supplied only by later scoped stages.", "REVIEW_RESIDUAL_DETERMINANT_ASTRA.md", 121, 130)
result("C16", "Residual lattice bridge", "CONDITIONAL", "Finite charged determinant/free fixed-depth harmonic bridge → N16; later stages supply particular vertex/full-colour extensions, not nonlinear RG.", "REVIEW_RESIDUAL_LATTICE_BRIDGE_ASTRA.md", 3)
result("C17", "Residual vertices", "CONDITIONAL", "Paired charged-root antiperiodic, fixed-depth volume-before-momentum zero F-squared coefficient → N16; later full-colour result extends only its convention.", "REVIEW_RESIDUAL_VERTICES_ASTRA.md", 3)
result("C18", "RESIDUAL_FULL_COLOUR", "CONDITIONAL", "Zero residual F-squared coefficient at fixed finite depth, infinite-volume/a.e.-Bloch convention → N16; no nonlinear finite-torus functional.", "REVIEW_RESIDUAL_FULL_COLOUR_ASTRA.md", 3)
result("C19", "UNIFORM_SOFT_MINIMIZER", "CONDITIONAL", "Scope-corrected normalized tree energy gives FC19/FC20 → N16; exact finite-u Hessian has an extra positive normalizer spread. Original broader reading superseded.", "checks/review_uniform_soft_scope_confirmation.md", 3, 13)
result("C20", "CHARGED_STATIONARY_JET", "CONDITIONAL", "u-stripped cubic/completed-quartic identities and lift/current bounds → N16; later BC conditionally supplies CJ18, not finite-u RG.", "REVIEW_CHARGED_STATIONARY_JET_ASTRA.md", 10, 17)
result("C21", "BOTTOM_SECOND_CURVATURE", "CONDITIONAL", "BC3/CJ18 and BC26 under normalized-tree/linear/current contracts → N16; bounded jets do not imply nonlinear uniform neighborhoods or finite-u convergence.", "REVIEW_BOTTOM_SECOND_CURVATURE_ASTRA.md", 83)
result("C22", "UNIFORM_ONE_LOOP_COUPLING", "CONDITIONAL", "UL4 and every-increment B-BR under exact normalized fixed-kappa contracts → N16; volume first, no depth-uniform finite-volume rate, nonlinear U remains open.", "REVIEW_UNIFORM_ONE_LOOP_COUPLING_ASTRA.md", 372, 378)
result("C23", "EUCLIDEAN_ROTATION_IMPORT", "CONDITIONAL", "Spectral-cone/diagonal free-box reflection implications → FA; common ordinary law, real-Schwartz-source bound, all mirrors and periodic same-state transfer remain inputs.", "REVIEW_EUCLIDEAN_ROTATION_IMPORT_ASTRA.md", 13, 17)
result("C24", "CROSSOVER_LITERATURE_BRIDGE", "CONDITIONAL", "Bounded calculations/scoped import screen → infrared strategy and D; trace-aware stronger suppliers remain live. No wholesale literature rejection or continuum bridge.", "REVIEW_CROSSOVER_LITERATURE_BRIDGE_ASTRA.md", 5)
result("C25", "MASS_GAP_TARGET", "CONDITIONAL", "Dense-family spectral criterion under physical uniform decay/onset and reconstruction → gap; MG0–MG5 stay open.", "REVIEW_MASS_GAP_TARGET_ASTRA.md", 3)
result("C26", "MASS_GAP_CONSTRUCTION", "CONDITIONAL", "Finite transfer, normalized SU(2) forward images and source identities in stated model → MG2; review is bounded support, expressly not landing approval or MG closure.", "REVIEW_MASS_GAP_CONSTRUCTION_ASTRA.md", 219, 229)
result("C27", "MASS_GAP_LOCAL_BLOCK / injectivity", "CONDITIONAL", "Fixed a>0, N≥2, 0<beta≤1/32 physical thermodynamic slice Hamiltonian, unique vacuum and finite positive nonvacuum threshold → MG1 strategy; bounded-support review, no continuum or landing certification.", "REVIEW_MASS_GAP_LOCAL_BLOCK_ASTRA.md", 280, 302)
result("C28", "INTERACTING_SELECTED_CORE / graded complement", "OPEN", "Current author/pending-review work feeds D/S, not a banked producer. Do not execute or assume these active lanes.", "HANDOFF.md", 367, 371)

mg_nodes = []
for id, title, status, scope, line in [
    ("MG0", "Existence and reconstruction", "OPEN", "Actual common hierarchy, physical normalization and full domain; includes T_OS producer work.", 97),
    ("MG1", "Physical infrared producer", "OPEN", "Uniform dense-family reflected decay or physical transfer gap on the continuum trajectory. Fixed-spacing strong-coupling mechanism exists; no such continuum estimate supplied.", 98),
    ("MG2", "Source transport", "OPEN", "Exact full product/source/normalizer transport, failed returns and decaying tails into the infrared regime.", 99),
    ("MG3", "Uniform continuum passage", "AT-RISK", "Positive physical rate, prefactors and onset uniform in cutoff/volume on one trajectory; the fixed-spacing theorem does not supply this bridge.", 100),
    ("MG4", "Surviving excited sector", "OPEN", "Non-vacuum state survives the same limit; finite-lattice positivity or one test observable is not enough.", 101),
    ("MG5", "Yang–Mills identification", "OPEN", "Correct local theory, gauge group and observable quantifiers; no whole-target certification.", 102),
]:
    mg_nodes.append(node(id, title, status, scope, "MASS_GAP_TARGET.md", line))

route_rows = ["| Chain | Minimal unresolved interface set, relative to the declared contracts | At-risk leaf? |", "|---|---|---|"]
for r in routes:
    route_rows.append(f"| {r['id']}: {r['geometry']} + {r['witness']} | C0 + {' + '.join(geometry[r['geometry']])} + {' + '.join(witnesses[r['witness']])} | Yes |")

report = """# Critical-path mapping audit of the YM4D program

The branch contains a connected conditional proof program and useful reviewed mechanisms, but **no complete chain to T_OS**. Every presently specified flat/sphere witness chain retains at-risk interfaces. This is not evidence that Yang–Mills is impossible or that the missing interfaces are mutually independent. The highest-value next work is to test the absolute witness and full normalized return contracts before expanding their supporting libraries.

## Snapshot, meaning of status, and coverage

Audit type: **ARGUED dependency/scope assessment**, with existing PROVEN/conditional results attributed to their reviews; no new proof or numerical evidence. HEAD is `814364fcc7dbcf0ff4146f6766e98890124ac905` (`claude/q-L1`). Cached `origin/main` is `01589af3faf806b736c42dc2f3bd625e9edead9f`; cached execution ref is `56c5c0ab64f532c5784e895b2f9aa6894fa334e0`. Fetch failed because shared `FETCH_HEAD` is not writable, so remote freshness is not certified. Source bytes are frozen in [audit_source_manifest.json](checks/audit_source_manifest.json); quotation passages and the graph are recorded in [audit_graph.json](checks/audit_graph.json). The final source/scope check and independent mapping review are separate artifacts.

**LANDED** here means a reviewed/admitted *branch export at the stated finite/model/correction scope*, not mainline landing or formal retained status. **CONDITIONAL** means a reviewed implication with the table's named hypotheses, not those hypotheses proved for YM. **OPEN** means the needed actual producer/compatibility is unproved. **AT-RISK** marks an OPEN interface with a specific suspected obstruction or unsupported shortcut identified in the quoted evidence. Risk labels and rankings are this audit's ARGUED assessment; the adjacent quotation is the source evidence, not a fabricated source verdict using that word. A row containing several finite facts is classified by its stated export/consumer contract, never by its strongest isolated calculation.

Coverage is the 26-node assembly, all 44 S26 registry entries, the eight later assembly-support reviews, the eight named queue units, and 27 reviewed coordinator units plus the pending selected-core/complement assignment. This is a map of claimed exports and their source reviews, **not** a new producer-by-producer proof audit or a claim that every file in the 3,313-file snapshot is a new theorem. Historical check scripts are not promoted into additional scientific results. References retain the exact snapshot's line numbers. Longer quoted passages are shortened only after the displayed words; complete passages are in the evidence JSON.

## Updated implication DAG

The following picture groups the coupled flow/return induction into one **unclosed construction block**. It does not pretend that assuming flow to prove return and return to prove flow is a solved DAG. A valid common induction/fixed-point construction is an explicit U obligation. All arrows are conditional interfaces; boxes labelled as actual inputs are not available objects.

```mermaid
flowchart TD
  O[O: target, observable and source dictionaries] --> J
  C[C: local/background/action interfaces] --> J
  K[K: simultaneous quantitative windows] --> J
  L[Reviewed linear, tree, residual and finite-sector libraries] --> J
  J[Unclosed joint construction: D full return + U actual flow/trajectory] --> S[S: actual all-order source/seed estimates]
  S --> REG[N2 H_reg and N9 REC, conditional]
  S --> RP[N3 RP on the same limit, conditional]
  S --> GEO{Geometry choice}
  GEO --> F[FT + FA: flat all-product symmetry]
  GEO --> P[SP + SS + SR, and SW if strict: sphere symmetry/limits]
  S --> W{One of five witness contracts}
  W --> INT[N5 H_int, actual absolute witness]
  O --> ALG[N6 common algebra and identifications]
  REG --> A[N1F or N1S common assembly]
  RP --> A
  F --> A
  P --> A
  INT --> A
  ALG --> A
  A --> DIAG[N7 already proved conditional diagonal/closure]
  DIAG --> T[N0 T_OS: OPEN]
```

### Original 26 nodes, updated rather than copied from old status paragraphs

""" + table(assembly_nodes) + """

The main supersessions are substantive: **REC** is now an explicit conditional construction; **HRP** includes reviewed pole geometry and the half-arc repair; **LGF** supplies the free kernel used by TSE; qualitative local **R** and a restricted **LANEA** package have providers; and the residual/tree/jet chain reaches conditional every-increment **UL4/B-BR**. None is still listed as a wholly missing lemma. Conversely RD's full requested theorem remains HOLD, and abstract analytic libraries/selected-sector zero-freeness do not constitute its full return.

### Terminal unresolved interfaces used in the route sets

These are minimal *named interfaces for the selected architecture*: an interface is listed once, and no already available conditional library is counted again as a missing leaf. They are not a proof of logical necessity among all conceivable constructions, nor a count of independent mathematical walls. D, U and S can share work; a new mechanism may replace a contract only by proving its consumer output. Hard and soft schemes must instantiate D/U/S for their own actual measure, not borrow another scheme's completion.

""" + table(leaf_nodes) + """

## Candidate chains and minimal unresolved sets

Let **C0 = {O, C, D, U, S, K}**. Flat geometry adds **{FT, FA}**; sphere geometry adds **{SP, SS, SR}**, plus **SW** under the strict flat-Wilson reading. Each row adds precisely the two listed witness interfaces. **SS has two alternative suppliers: W (Ward) OR V (N14 universality)**; the route does not require both. The remaining assembly, RP, diagonal and reconstruction steps are conditional exports already represented above; their actual hypotheses are contained in these sets, not silently discharged. The sets concern T_OS, not the extra mass-gap target.

""" + "\n".join(route_rows) + """

**No row has no AT-RISK leaf.** Even if the target explicitly accepted the finite canonical free class and thereby removed the broad-class part of EI, D, S, EM and a geometry risk would remain. Accepting sphere regulators removes SW only. The fifth, soft-block witness is required by ASSEMBLY55's late addition; it has not been discarded. The hard-block row is prospective: its hard-return/HRT and flow inputs are not supplied by the current soft work.

N14 is the assembly's alternative **sphere** symmetry supplier: its complete two-theory comparison (all coarse data, observables, curved/profile variants and seam) can replace the Ward supplier inside SS. Its fixed-torus UNIV-T result is UV comparison support; conditional interior comparison alone does not identify exterior laws or establish orientation independence on R4. A flat replacement of FT/FA would need that state/limit bridge, or the rotation-import proposal's common ordinary law, all-mirror bounds and periodic same-state transfer. None is a risk-free bypass. Uniform MIN-cb and LF-inst likewise remain sufficient subroutes, not mandatory leaves of all constructions.

""" + cite("ASSEMBLY55.md", 289, 292, 50) + "\n\n" + cite("UNIV55.md", 130, 133, 55) + """

## At-risk ranking and what the evidence does—and does not—show

Route counts below refer to the **ten declared candidate chains**, not probabilities or independent proofs. A witness-family interface counts on both geometries; alternatives within one chain do not inflate coverage. Ordering combines coverage and the strength of the identified mismatch. “Obstruction” means obstruction to the *specified argument*, not to the physical theory.

| Priority | At-risk interface | Chains affected | Evidence and obstruction assessment |
|---|---|---:|---|
| 1 | D: full normalized return | 10/10, each in its own chosen scheme | REVIEW_RD B1–B3 gives a concrete hard-boundary norm mismatch: an indicator attaining zero has supremum difference one; an integrated rare-tail bound cannot meet the small uniform activity budget. Complete histories/reference/sea/induction are missing. **High risk for the current naive norm expansion; repair mechanisms exist**, including selected integrals, connected activities and alternative expansions. No global no-go follows. |
| 2 | Absolute OS witness identification: E4I/BI/EI/HI/PI | 10/10 as a family; 2/10 per witness | ASSEMBLY review R1/R13 and final warning; HINT2's failed product-preserving ID; WT0 marked-system limitation; NONFREE scalar-GFF counterexample. **Known failures of broad shortcut claims**, with different possible repairs per witness. This can invalidate an entire witness route even if its estimates are proved. |
| 3 | S: actual all-order source/seed estimates | 10/10 | SRC2's actual all-coarse normalized representation and OSLEAF's all-order separation are not supplied. Selected fixed-rho results are real progress, but exclude both complements/coarse sectors. **High interface risk**, not absence of mechanisms. Restricted REC solves the abstract reconstruction step; it does not produce the YM seed. |
| 4 | SS: all-coarse sphere symmetry/seam, W or V | 5/10 sphere | SPHERE55:659–663 identifies the possible reappearance of covariance across pi R/2 if Ward estimates are only typical-field. SPHERE2's allowed mixed dimension-3 operator defeats the stated complete no-tuning list, not every transparency theorem. Universality also retains an actual all-coarse two-theory/profile/seam comparison. **Specific plausible obstruction to “UV-only”**, unproved for either full conditional supplier. |
| 5 | FT: actual TQ / flat replacement | 5/10 flat | N12 and CODEX_REVIEW_TQ keep the Wilson torque estimate unverified. Generic RP has no universal rate, but the rotlet is not a Wilson/RP counterexample and a stronger Wilson no-go was not proved. **Substantial uncertainty; no established inevitable obstruction**. UV conditional comparison alone does not settle exterior-law/IR selection. |
| 6 | SP: torus-to-sphere local transfer | 5/10 sphere | F13 identifies digital boundaries, prism/weight/profile changes and loss of global chessboard estimates. **Concrete unmatched hypotheses**, partly approachable by local estimates; no proof that transfer is impossible. |
| 7 | Actual witness estimates: E4M/BM/EM/HM/PM | 10/10 as a family; 2/10 each | PL-1L/TS lower matching, sharp-time uniformity, hard-law H-Bal/H-loc-LF/H-sg or NOISE-ADD/ANTI-flat remain actual YM obligations. RP supplies a sign, not a strict lower bound. **Route-dependent high risk**; bounded hard-block MOM/CONV need no additional flowed-witness estimate under the matched law. |

F17 is deliberately **not** ranked as an unavoidable “instanton-strength barrier.” Its old necessity inference is refuted by CODEX_REVIEW_ASSEMBLY R4: a probability estimate is sufficient for a particular supremum-bound proof, while an observable-weighted or localized argument could succeed differently. Neither success of such alternatives nor necessity of LF-inst is established. The exact-risk quotations for all rows are in the leaf table; see also the explicit review boundary:

""" + cite("CODEX_REVIEW_ASSEMBLY.md", 53, 57, 65) + "\n\n" + cite("SPHERE55.md", 659, 663, 70) + "\n\n" + cite("CODEX_REVIEW_SPHERE2.md", 43, 54, 65) + """

## Work with no present critical-path consumer

1. **Historical a_RS live-margin optimization:** the cited live v3 unreturned-defect pricing consumer was retired. Its local kernel calculations remain evidence, but improving the obsolete margin does not advance any declared chain. This is a scoped no-consumer finding, not retirement of every large-field alternative. """ + cite("PROOF.md", 509, words=45) + """
2. **Per-level NBG/GREENT families (assembly C3/C7):** the assembly marks these off the displayed proof route; do not count further per-level constants as progress on the composite tower without a named live consumer. They remain a possible alternative only after an explicit matching interface is supplied. """ + cite("ASSEMBLY55.md", 93, 98, 60) + """
3. **Repeating closed abstract glue:** new standalone proofs of DIAG, the already reviewed finite RP geometry, free LGF, or the same restricted REC implication do not discharge a new leaf. Their current results *do* feed surviving routes; only redundant repetition has no marginal critical-path output. """ + cite("CODEX_REVIEW_ASSEMBLY.md", 235, words=50) + """
4. **Discarded argument shortcuts:** ordinary-product closure from separated convergence alone; absolute freeness exclusion from the 4D one-point comparator; AF-e as exclusion of all GFFs; universal convexity/Peierls conclusions from the scoped LCONV examples; and depth-uniform finite-u flow from tree/one-loop bounds do not survive their reviews. Preserve the counterexamples and scoped positive parts. They are diagnostic work, not successful closures. """ + cite("CODEX_REVIEW_ASSEMBLY.md", 209, words=60) + """

No current reviewed coordinator unit is shown to be wholly useless. Source/sea/complement/radius/coercivity/kernel work feeds D/U/S; tree/residual work feeds N16; rotation work feeds FA or a replacement; physical transfer work feeds the added infrared objective. SOFTHARD is a useful route-selection memo, not a missing proof node. The pending selected-core and graded-complement work has a live consumer but cannot yet be counted as reviewed progress. No deletion or source change is recommended by this map.

## Infrared mass gap: addressed on disk, continuum target still open

**Yes, there are actual infrared nodes.** MASS_GAP_TARGET supplies a conditional spectral criterion for reflected correlations of a dense physical observable family. The later construction and local-block work goes beyond an auxiliary Gaussian gap: its bounded-support review includes a **fixed-spacing**, strong-coupling, thermodynamic physical gauge-invariant slice Hamiltonian with unique vacuum and a finite positive nonvacuum threshold (a>0, N≥2, 0<beta≤1/32). Do not relabel that review as landing approval, or confuse this model/regime result with a continuum YM mass gap.

""" + cite("REVIEW_MASS_GAP_LOCAL_BLOCK_ASTRA.md", 280, 302, 75) + "\n\n" + table(mg_nodes) + """

The missing bridge is a quantitative crossover/physical-block comparison or exact source-preserving RG transport into a proved endpoint regime, with all products, normalizers and boundary/failure terms. The fixed-t continuum limit must precede the large-t spectral inference, with a positive physical decay rate, prefactors and onset uniform in cutoff and volume. No current reviewed unit closes an MG row. In particular, the local-block result does not provide that uniform bridge, and a Schur/Hessian gap in an auxiliary fluctuation field is not the physical spectral gap.

""" + cite("REVIEW_MASS_GAP_LOCAL_BLOCK_ASTRA.md", 380, 386, 70) + "\n\n" + cite("MASS_GAP_TARGET.md", 81, 91, 60) + """

MG3 is an additional risk for the **expanded existence-plus-gap target**, not an eleventh required leaf of the historical T_OS definition. MG1 is OPEN, rather than “no mechanism on disk”: fixed-spacing strong coupling and the proposed direct transfer/crossover routes are real candidate mechanisms. Their continuum applicability is exactly what remains to establish.

## Recommended ordering: decisive tests before the common core

This is a recommendation for subsequent authorized research, not new work performed by this mapping audit. A failed shortcut is recorded and its named alternative considered; failure is not promoted into a global no-go.

1. **Freeze the target and test a witness.** Select the exact algebra, free class and support/OS quotient maps. Prefer testing the already concrete separated-e or time-zero-B contracts first, while preserving the other three alternatives. Determine whether the claimed comparator excludes the required physical free class and whether mixed products/SHARP really live on that algebra. Pass means an exact absolute witness contract; a relative comparator alone is not enough. This is O plus the chosen identification leaf.
2. **Test one complete returned normalized step.** Instantiate RD B1–B3 at a real history with a nonempty failed region/hole. Retain both complements, all prefactors and the remaining correlated sea expectation; prove the common complex-source zero-free/norm bound or expose exactly where the norm fails. Do not rerun a successful selected-sector integral as if it were this test. This directly probes D before extending LIB1-style libraries.
3. **Choose geometry after its decisive conditional test.** Sphere: select the Ward or N14 comparison supplier, test arbitrary coarse data and the allowed mixed seam operator, including full local/profile transfer and any residual coarse covariance. Flat: produce an actual Wilson all-order torque/decay estimate or a replacement that also closes the exterior-law/same-state and R4 limit bridge. Decide sphere admissibility under the target explicitly. These test SS/SP or FT/FA, not merely finite RP already available.
4. **For the expanded gap target, test the physical crossover/transport early.** Match the fixed-spacing strong-coupling physical endpoint to a fixed physical block on the proposed continuum trajectory, or specify a direct uniform transfer estimate for a dense family. This probes MG2/MG3 without mistaking the endpoint theorem for a continuum gap. It can inform whether the existence program is being extended toward the stated gap objective.
5. **Then finish the actual core contracts.** Match phi/kappa normalization, critical versus minimum action, gauge slices, local/background/holonomy and boundary domains (C); retain the corrected LANEA/RLOC/jet/residual providers instead of re-proving them. Supply actual connected interacting finite-u remainders and full return induction, together with simultaneous quantitative windows (D/K). Close U as one noncircular flow/return construction, including finite-volume rates, continuity, FI-1, tuning and one common trajectory.
6. **Build the actual hierarchy and finish assembly.** Prove S with fixed source radius on all required sectors, all-product growth and large-distance bounds; feed the existing SP→EXT and REC_CONT→REC_LIB theorems. Supply the selected geometry's full-algebra symmetry and the chosen witness's actual upper/lower/moment limits on that same hierarchy. Apply the already proved common-sequence/diagonal closure. The additional gap criterion is invoked only after its independent physical uniformity and identification inputs are present.

This ordering updates the old ordered list: qualitative R, abstract DIAG, finite/pole RP, LGF and conditional REC are no longer separate wholly missing tasks; the volume-first one-loop chain is no longer the original unproved rho-null placeholder. Actual finite-u flow, full normalization, all-order source inputs and the absolute physical witness remain the critical contracts.

## Complete export-to-DAG crosswalk

The 44 legacy rows below correspond one-for-one to the S26 registry, followed by eight later support reviews, eight queue lanes and 27 reviewed coordinator units plus their pending successor. Exact scope is controlled by the quoted actual review, not by an old HANDOFF paragraph or a registry's headline. L01/L03/L04/L08/L22 additionally quote the registry for its precise corrected classification; the matching review scopes are reflected in their notes. DICT's corrections apply across the table: small chosen global gauge is not curvature-small, E^cb is not automatically the minimum tower, phi is not literal k-tilde, and source/weighted norms may not be exchanged.

""" + cite("CODEX_REVIEW_DICT.md", 283, 308, 55) + "\n\n" + table(inventory, "Export / result family") + """

### Supersession and review boundaries that must survive reuse

- **HRP:** REVIEW2_HRP/HRP_R2 finite and conditional scope, followed by REVIEW_HRP_HALF_ARC_ASTRA on the repaired geometric arc. A prior endpoint-only half-circle argument is not current evidence. REC consumers still require their common actual hierarchy.
- **REC:** REVIEW2_REC controls the finite Cartesian/flat-test scope. The cross-family spot check covers part-(2) exhaustion only; no cross-family certification of the seed or the whole reconstruction is claimed. There is no automatic sharp-time/ordinary-product extension or unique-vacuum/gap conclusion.
- **LGF:** the newer consumer review and REVIEW2_LGF recognize actual TSE adoption. “LGF still missing” is stale; “YM lower bound proved” is also false.
- **LIB1:** keep full-source norms, prefactors and history/hole hypotheses. A historical norm-control review of another revision is not evidence for the current source's stronger consumer claims.
- **RD:** the current 583-line source has SHA-256 `06ad2b5b52bfa66f7784a1fb97936337c59f5164318f89af9a2a065226671e5f`, matching REVIEW_RD. No pass-2 producer change exists at this snapshot. RD_LOG's research-note LAND does not override the full-theorem HOLD.
- **Coordinator flow chain:** later full-colour, scope-corrected uniform tree, charged jets, bottom-curvature and UL4 results supersede older *scoped* open clauses. CJ18/BC26 and the every-increment B-BR implication must not be left at their obsolete earlier status. Exact finite-u normalizer spread, nonlinear integration and finite-volume uniformity remain separate.
- **Fixed source radius:** its fixed-rho selected-domain theorem supersedes the older shrinking-rho claim only on the matched domain (including its small curvature/size constraints). Both complements/full normalization remain absent.
- **Mass gap:** bounded-support is not LAND; fixed-spacing physical thermodynamic scope is stronger than an auxiliary Hessian statement but weaker than uniform continuum gap closure.

## Verification and limits

The audit performs only source reads, quotation extraction, hashing, dependency bookkeeping and independent review of the mapping. No scientific numerical experiment was run; the sandbox rejected the required nice priority, and resource-limit diagnostics also failed, as recorded in AUDIT_LOG. No existing result is claimed freshly reproduced. Source-status reconciliation is not a new retained audit verdict. Remote branch freshness and uninspected underlying mathematical arguments remain outside certification.

See [audit_validation.json](checks/audit_validation.json) for deterministic quotation/source/scope/route checks and [audit_review.md](checks/audit_review.md) for the independent hostile mapping verdict. Any LAND there concerns this mapping document's readiness only. Editable prompts, original science files, audit authority/ledger files and axioms are unchanged; no commit is made.
"""

(BASE / "AUDIT.md").write_text(report)
payload = dict(nodes=nodes, inventory=inventory, routes=routes, common_leaves=common,
               geometry=geometry, witnesses=witnesses, evidence=evidence)
(BASE / "checks/audit_graph.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(dict(nodes=len(nodes), exports=len(inventory), routes=len(routes),
                      quotations=len(evidence), report_lines=len(report.splitlines()),
                      report_words=len(report.split()), report_sha256=hashlib.sha256(report.encode()).hexdigest())))
