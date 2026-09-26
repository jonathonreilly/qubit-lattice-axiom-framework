"""Post-seal evidence authentication; never executes author checkers."""
from pathlib import Path
import ast,hashlib,json,datetime,math
import sympy as s
from itertools import product

out=Path(__file__).resolve().parent;base=out.parent
def ident(p):
    data=p.read_bytes();return dict(path=str(p),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
pre=json.loads((out/"PRE_COMPARISON_SEAL.json").read_text())
for item in pre["artifacts"]+pre["source_identities"]+pre["instruction_identities"]:
    actual=ident(Path(item["path"]))
    assert actual["sha256"]==item["sha256"] and actual["bytes"]==item["bytes"]
records=[];ids=[]
for script,prefix,total in [
    ("fourteen_label_quantum_check.py","FOURTEEN_LABEL_QUANTUM",13),
    ("fourteen_label_cubic_carrier_check.py","FOURTEEN_LABEL_CUBIC_CARRIER",5),
    ("born_compatible_fourteen_formation_check.py","BORN_COMPATIBLE_FOURTEEN_FORMATION",13)]:
    sp=base/script;rp=base/(prefix+"_RESULTS.json");lp=base/(prefix+"_RUN.log")
    data=json.loads(rp.read_text())
    assert data["source_sha256"]==ident(sp)["sha256"]
    names=[c["name"] for c in data["checks"]]
    tree=ast.parse(sp.read_text())
    calls=[node.args[0].value for node in ast.walk(tree)
           if isinstance(node,ast.Call) and isinstance(node.func,ast.Name)
           and node.func.id=="check" and node.args and isinstance(node.args[0],ast.Constant)
           and isinstance(node.args[0].value,str)]
    assert calls==names and len(names)==total and all(c["passed"] for c in data["checks"])
    assert lp.read_text().splitlines()==["PASS: "+n for n in names]+[f"TOTAL: {total} PASS"]
    records.append(dict(source=script,reported_group_count=total,all_names_logs_and_hashes_authenticated=True,rerun_by_reviewer=False))
    ids.extend([ident(sp),ident(rp),ident(lp)])
quantum=json.loads((base/"FOURTEEN_LABEL_QUANTUM_RESULTS.json").read_text())
assert len(quantum["fits"])==9
for row in quantum["fits"]:
    ref=abs(row["j"])*(3-math.sqrt(3))/14
    assert abs(ref-row["reference"])<1e-15
    assert abs(abs(row["objective"]-ref)-row["discrepancy"])<1e-15
    assert row["status"]=="optimal" and row["discrepancy"]<2e-8
    assert abs(row["largest_actual_TV"]-ref)<2e-8 and row["feasibility_residual"]<2e-9
maximum=max(r["discrepancy"] for r in quantum["fits"])
assert quantum["checks"][-1]["detail"]["maximum_objective_discrepancy"]==maximum
born=json.loads((base/"BORN_COMPATIBLE_FOURTEEN_FORMATION_RESULTS.json").read_text())
for row in born["checks"][-1]["detail"]:
    assert row["norm_comparison_violation"]<2e-9
    assert row["late_interaction_picture_difference"]<row["rigorous_tail_bound"]+2e-10
    if row["j"]==0:
        assert row["j0_integrated_phase_residual"]<2e-9
# Exact new finite control of the quantum-only marginal already derived in the initial seal.
unit=[s.eye(3)[:,i] for i in range(3)]
e=[];b=[]
for i in range(3):
    for sign in (1,-1):e.append(sign*unit[i]);b.append(s.zeros(3,1))
for signs in product((1,-1),repeat=3):e.append(s.zeros(3,1));b.append(s.Matrix(signs))
E=s.Matrix.vstack(*[v.T for v in e]);B=s.Matrix.vstack(*[v.T for v in b])
F=E.row_join(B/2);S=E+B/s.sqrt(3);j=s.symbols("j",real=True)
P=(s.ones(14)+j*F*F.T)/14
assert all(s.simplify(x)==0 for x in S.T*P-j*S.T/7)
report=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            pre_comparison_seal=ident(out/"PRE_COMPARISON_SEAL.json"),
            initial_sealed_artifacts_and_sources_unchanged=True,
            author_evidence=records,author_source_identities=ids,
            primary_numerical_results_recomputed=False,
            primary_numerical_record_arithmetic_verified=True,
            maximum_recorded_POVM_objective_error=maximum,
            numerical_scope="Primary unconstrained-effect SOCP outputs are authenticated and their arithmetic checked; no primal effect arrays are stored, and the unavailable local cvxpy program was not rerun. Exact independent twirling/primal/dual proof establishes the optimum.",
            born_j0_rounding="The recorded j=0 ODE tail difference exceeds its analytic tail bound by about 2e-11, within the declared 2e-10 numerical tolerance. This is not a counterexample to the exact ODE inequality.",
            added_exact_control="S^T P=(j/7) S^T verifies the sealed quantum-only depolarizing marginal witness.",
            actionable_mathematical_findings=[],source_code_drift_findings=[],
            source_scope_limits=["The cubic carrier check enumerates ordinary characters and verifies the positive construction numerically; the projective commutant exclusion is supplied by the reconstructed proof.",
                                 "The Born checker verifies the two-design; the independent Kraus trace argument, not a finite PASS count, proves optimal fidelity.",
                                 "Norm/scattering statements concern the six-vector block, not the separate density component.",
                                 "Quantum one-event constructions do not realize the repeated classical process."])
(out/"SOURCE_COMPARISON.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
print(json.dumps(dict(author_groups=[13,5,13],author_files_authenticated=len(ids),
                     initial_seal_unchanged=True,quantum_only_marginal_exact=True,findings=[]),sort_keys=True))
