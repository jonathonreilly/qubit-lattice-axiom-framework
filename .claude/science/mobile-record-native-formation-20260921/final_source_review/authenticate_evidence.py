#!/usr/bin/env python3
"""Authenticate frozen source/evidence; do not rerun the author mathematics."""
from pathlib import Path
import ast, hashlib, json
import numpy as np
HERE=Path(__file__).resolve().parent
PACKET=HERE.parent
ROOT=PACKET.parents[2]
sha=lambda data:hashlib.sha256(data).hexdigest()
file_sha=lambda path:sha(path.read_bytes())
checks=[]
def check(name, condition, detail=None):
    assert condition,(name,detail)
    checks.append(dict(name=name,detail=detail))
    print("VERIFIED",name,json.dumps(detail,sort_keys=True),flush=True)
note=ROOT/'docs/MOBILE_RECORDS_NATIVE_FORMATION_EULER_AND_CUBIC_CENTERING_BOUNDED_THEOREM_NOTE_2026-09-21.md'
runner=ROOT/'scripts/mobile_records_native_formation_euler_and_cubic_centering_2026_09_21.py'
check("frozen_note",file_sha(note)=="2cb9e232400292ef28f75b16ebca67f30a335ed48c03af060180a4f4e7a8bf38")
check("frozen_runner",file_sha(runner)=="fa22aa845d9aef1a1e0d99072ec93c719ec94abfa50e86d674022c0f067f450a")
namespace={}
for node in ast.parse(runner.read_text()).body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id in ("SUITES","MUTATIONS") for t in node.targets):
        exec(compile(ast.Module(body=[node],type_ignores=[]),str(runner),"exec"),namespace)
suites=namespace["SUITES"];mutations=namespace["MUTATIONS"]
runs=json.loads((PACKET/'AUTHOR_RUNS.json').read_text())
summary=json.loads((PACKET/'AUTHOR_VERIFICATION.json').read_text())
identities=runs["identities"]
check("recorded_current_identities",all(file_sha(ROOT/p)==h for p,h in identities.items()) and summary["identities"]==identities)
check("baseline_and_complete_mutation_menu", [r["mutation"] for r in runs["runs"]]==[None,*mutations],len(mutations))
for record in runs["runs"]:
    path=PACKET/record["result_path"]
    assert file_sha(path)==record["result_sha256"]
    data=json.loads(path.read_text())
    assert data["identities"]==identities and data["mutation"]==record["mutation"]
    name=record["mutation"]
    if name is None:
        assert record["returncode"]==0 and data["passed"] and data["control_count"]==25
        assert len(data["suites"])==3
        for row,(filename,resultname,count) in zip(data["suites"],suites):
            source=(PACKET/'author_checks'/filename).read_bytes()
            assert row["suite"]==filename and row["returncode"]==0
            assert row["source_sha256"]==row["executed_source_sha256"]==row["results"]["source_sha256"]==sha(source)
            assert len(row["results"]["checks"])==count and all(c["passed"] for c in row["results"]["checks"])
        check("authenticated_existing_baseline",True,dict(controls=25,suites=[s[0] for s in suites]))
    else:
        filename,old,new=mutations[name]
        source=(PACKET/'author_checks'/filename).read_text()
        assert source.count(old)==1
        assert record["returncode"]==1 and not data["passed"] and len(data["suites"])==1
        row=data["suites"][0]
        assert row["suite"]==filename and row["source_sha256"]==sha(source.encode())
        assert row["executed_source_sha256"]==sha(source.replace(old,new,1).encode())
        assert row["returncode"]!=0 and "AssertionError" in row["stderr"] and "SyntaxError" not in row["stderr"]
        check("authenticated_mutation_"+name,True,dict(suite=filename,executed_source_sha256=row["executed_source_sha256"],failure=row["stderr"].splitlines()[-1]))
old=PACKET/'author_development/initial_count_bookkeeping'
oldruns=json.loads((old/'AUTHOR_RUNS.json').read_text())
oldresult=json.loads((old/'PRIMARY_RESULTS.json').read_text())
receipt=json.loads((old/'RECEIPT.json').read_text())
check("preserved_nonmathematical_bookkeeping_failure",
 len(oldruns["runs"])==1 and oldruns["runs"][0]["mutation"] is None and oldresult["passed"] and oldresult["control_count"]==25
 and "TOTAL: PASS=91 FAIL=0" in (old/'run_author_checks.py').read_text()
 and file_sha(old/'PRIMARY_RESULTS.json')==receipt["baseline_sha256"]
 and "AssertionError" in (old/'RUN.log').read_text())
development=json.loads((PACKET/'author_development/NATIVE_FORMATION_CENTERING_RESULTS.json').read_text())
assert development["source_sha256"]==file_sha(PACKET/'author_checks/native_formation_centering_check.py')
cases=development["cases"]
assert cases==json.loads((PACKET/'author_development/native_formation_centering/COMPLETED_CASES.json').read_text())
for case in cases:
    path=PACKET/'author_development/native_formation_centering'/("three_dimensional_L%d.npz"%case["side"])
    assert file_sha(path)==case["raw_sha256"]
    with np.load(path) as data:
        assert float(data["scaled_density_coefficient"][-1])==case["scaled_final_density_coefficient"]
        assert float(data["target_scaled_density_coefficient"][-1])==case["target_final_coefficient"]
check("seven_preserved_raw_size_cases",len(cases)==7,[dict(side=c["side"],coefficient=c["scaled_final_density_coefficient"]) for c in cases])
with np.load(PACKET/'author_development/native_formation_centering/four_cycle_jet.npz') as data:
    firsttwo=float(np.max(abs(data["density_jet"][:,1:3])))
    cubic=float(np.max(abs(data["density_jet"][:,3]-data["closed_density_coefficient"])))
    assert firsttwo<4e-17 and cubic<4.8e-18
    check("cycle_prose_tolerances_match_preserved_arrays",True,dict(first_two=firsttwo,cubic=cubic,final=float(data["density_jet"][-1,3])))
source_paths=set(ROOT/p for p in identities)
source_paths.update(PACKET/p for p in ("AUTHOR_RUNS.json","AUTHOR_VERIFICATION.json","PRIMARY_RESULTS.json","INDEPENDENT_CAPSULES.json","verify_capsules.py","run_author_checks.py"))
source_paths.update((PACKET/'mutation_results').glob('*.json'))
source_paths.update(p for p in (PACKET/'author_development').rglob('*') if p.is_file())
new_manifest=json.loads((PACKET/'INDEPENDENT_CAPSULES.json').read_text())
base_manifest=(PACKET/new_manifest["base_capsule_manifest"]).resolve()
source_paths.add(base_manifest)
for location,manifest in [(PACKET,new_manifest),(base_manifest.parent,json.loads(base_manifest.read_text()))]:
    for capsule in manifest["capsules"]:
        source_paths.update(location/(capsule["name"]+ending) for ending in (".zip","_REPORT.md"))
inventory=[dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,sha256=file_sha(p)) for p in sorted(source_paths)]
result=dict(scope="Authentication of existing evidence, not rerunning or independently validating the claimed mathematics.",checks=checks,sources=inventory)
(HERE/'AUTHENTICATION_RESULTS.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
print("AUTHENTICATED_SOURCE_FILES",len(inventory),flush=True)
