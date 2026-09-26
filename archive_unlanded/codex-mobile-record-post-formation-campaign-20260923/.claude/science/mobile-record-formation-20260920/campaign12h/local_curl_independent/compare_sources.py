"""Authenticate supplied author evidence without executing author checkers."""
from pathlib import Path
from fractions import Fraction
import ast, hashlib, json, datetime
import sympy as s

out=Path(__file__).resolve().parent
base=out.parent
def ident(p):
    d=p.read_bytes()
    return dict(path=str(p),bytes=len(d),lines=len(d.splitlines()),sha256=hashlib.sha256(d).hexdigest())
seal=json.loads((out/"PRE_COMPARISON_SEAL.json").read_text())
for it in seal["artifacts"]+seal["source_identities"]+seal["instruction_identities"]:
    p=Path(it["path"])
    assert ident(p)["sha256"]==it["sha256"] and ident(p)["bytes"]==it["bytes"]
groups=[]
files=[]
for script,prefix,count in [
    ("loop_birth_locality_check.py","LOOP_BIRTH_LOCALITY",5),
    ("local_curl_native_formation_check.py","LOCAL_CURL_NATIVE_FORMATION",13),
    ("late_state_canonical_check.py","LATE_STATE_CANONICAL",7),
]:
    src=base/script
    rp=base/(prefix+"_RESULTS.json")
    lp=base/(prefix+"_RUN.log")
    data=json.loads(rp.read_text())
    assert data["source_sha256"]==ident(src)["sha256"]
    names=[v["name"] for v in data["checks"]]
    assert len(names)==count and all(v["passed"] for v in data["checks"])
    tree=ast.parse(src.read_text())
    declared=[node.args[0].value for node in ast.walk(tree)
              if isinstance(node,ast.Call) and isinstance(node.func,ast.Name)
              and node.func.id=="check" and node.args
              and isinstance(node.args[0],ast.Constant)
              and isinstance(node.args[0].value,str)]
    assert declared==names
    assert lp.read_text().splitlines()==["PASS: "+name for name in names]+[f"TOTAL: {count} PASS"]
    files += [ident(src),ident(rp),ident(lp)]
    groups.append(dict(script=script,reported_controls=count,source_and_result_hash_match=True,
                       declared_names_and_raw_log_match=True,executed_by_reviewer=False))
# The added primary TV value follows from the independently derived exact odds.
tv=(4*abs(Fraction(1,12)-Fraction(1,10))+8*abs(Fraction(1,12)-Fraction(3,40)))/2
assert tv==Fraction(1,15)
print("Exact template-odds total variation:",tv)
# Check the complete preserved author development change.
oldp=base/"local_curl_development/first_structural_equality/local_curl_native_formation_check.py"
oldlog=base/"local_curl_development/first_structural_equality/LOCAL_CURL_NATIVE_FORMATION_RUN.log"
old=oldp.read_text()
oldline="check('nearest_neighbor_birth_law_is_nonconstant_for_nonzero_j',sum(probabilities)==1 and probabilities[1]==(1+j)/14 and probabilities[0]==(1-j)/14)"
newline="check('nearest_neighbor_birth_law_is_nonconstant_for_nonzero_j',all(s.simplify(q)==0 for q in (sum(probabilities)-1,probabilities[1]-(1+j)/14,probabilities[0]-(1-j)/14)))"
assert old.count(oldline)==1
assert old.replace(oldline,newline)==(base/"local_curl_native_formation_check.py").read_text()
assert "AssertionError: ('nearest_neighbor_birth_law_is_nonconstant_for_nonzero_j', None)" in oldlog.read_text()
j=s.symbols("j",real=True)
assert s.simplify(-(j-1)/14-(1-j)/14)==0
files += [ident(oldp),ident(oldlog)]
summary=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
             pre_comparison_seal=ident(out/"PRE_COMPARISON_SEAL.json"),
             initial_artifacts_and_sources_unchanged=True,
             primary_evidence=groups,primary_source_identities=files,
             independently_verified_additional_tv=str(tv),
             preserved_author_failure=dict(scope="Only structural equality changed to simplified difference equality; mathematical target unchanged.",
                                           complete_replacement_reproduces_final_checker=True),
             primary_checkers_executed=False,new_mathematical_findings=[],
             caveats=["The 25 recorded author groups are selective controls, not proofs of the entropy or ordered-limit statements.",
                      "The primary late-state feature check concerns U/V from the fourteen labels; the independent checker additionally tests all fourteen field covariances and rank thirteen at full occupancy."])
(out/"SOURCE_COMPARISON.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n")
print(json.dumps(dict(primary_group_counts=[g["reported_controls"] for g in groups],
                     authenticated_author_files=len(files),findings=[]),sort_keys=True))
