#!/usr/bin/env python3
"""Narrow completion-model qualification: byte authentication, no math rerun."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json

OUT=Path(__file__).resolve().parent
PRIOR=OUT.parent
BASE=PRIOR.parent
ARCHIVE=BASE/'autonomy_count_source_history/before_completion_model_qualification'
ORIGINAL='AUTONOMY_AND_FORMATION_COUNT_AUTHOR_SEAL.json'
CORRECTED='AUTONOMY_AND_FORMATION_COUNT_CORRECTED_AUTHOR_SEAL.json'
NOTE='FORMATION_COUNT_CONTROLS_GAUGE_COHERENCE.md'
SHA_ORIGINAL='fc3e56328ffbf995b9ee34432e6fd9187a48a9cc6bff48d549c928d7c4499358'
SHA_CORRECTED='94a2d29fb680aa7e5c10c78110593f4f84433d67cac5ee3858f0ba175f885f1c'
SHA_PRE='2fca7f6f5052aed71e25f24120eb2e8813e60d6e489e9093c8f3da29b0c13e14'
SHA_FINAL='cc2d4ba43fcdd61d79758c1f691b17bc3f1071c42b410d6edd4e21575921da63'
BINDINGS={}


def read(path, expected=None):
    path=Path(path).resolve();raw=path.read_bytes()
    row={'path':str(path),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
    if isinstance(expected,str):assert row['sha256']==expected,(path,row,expected)
    elif expected is not None:
        assert row['sha256']==expected['sha256'] and row['bytes']==expected['bytes'],(path,row,expected)
    if str(path) in BINDINGS:assert BINDINGS[str(path)]==row
    BINDINGS[str(path)]=row
    return raw


def main():
    old=json.loads(read(ARCHIVE/ORIGINAL,SHA_ORIGINAL))
    new=json.loads(read(BASE/CORRECTED,SHA_CORRECTED))
    read(BASE/ORIGINAL,SHA_ORIGINAL)
    assert new['original_author_seal_sha256']==SHA_ORIGINAL
    assert new['independent_final_seal_sha256']==SHA_FINAL
    before={row['path']:row for row in old['artifacts']}
    after={row['path']:row for row in new['artifacts']}
    assert len(before)==len(after)==13 and before.keys()==after.keys()
    moved={};archive_mapping=[]
    for path,row in before.items():
        original=Path(path);assert original.parent==BASE
        archived=ARCHIVE/original.name
        read(archived,row);read(original,after[path]);moved[path]=archived
        archive_mapping.append({'original_path':path,'archive_path':str(archived),
                                'bytes':row['bytes'],'sha256':row['sha256']})
    moved[str(BASE/ORIGINAL)]=ARCHIVE/ORIGINAL
    changed=[path for path in before if (before[path]['bytes'],before[path]['sha256'])!=
             (after[path]['bytes'],after[path]['sha256'])]
    assert changed==[str(BASE/NOTE)]
    assert after[str(BASE/NOTE)]['sha256']=='43aae29ef21aca04cc3fd096368ad2bdb5172c7aff31966fe118ad9597a6bbb5'

    counts={}
    for name,sha in [('PRE_COMPARISON_SEAL.json',SHA_PRE),('FINAL_COMPARISON_SEAL.json',SHA_FINAL)]:
        prior=json.loads(read(PRIOR/name,sha))
        for kind in ['sources','artifacts']:
            for row in prior[kind]:read(moved.get(row['path'],row['path']),row)
        counts[name]={kind:len(prior[kind]) for kind in ['sources','artifacts']}

    replacements=[
        ('No ordinary hopping is omitted in this ring family.\n',
         'No ordinary hopping is omitted in this ring family. The completion assertion\n'
         'contains only the specified hopping, occupation-preserving H0,\n'
         'occupation-monitoring jumps and birth terms. It does not extend to arbitrary\n'
         'additional N,T-commuting jumps allowed for the Section 1 count identity.\n'),
        ('the Hamiltonian commutes with T, and the other jumps commute with T.\n',
         'the Hamiltonian commutes with T, and the occupation-monitoring jumps commute\n'
         'with T. This section uses precisely the restricted completion model of\n'
         'Section 3.\n')]
    original=read(ARCHIVE/NOTE,before[str(BASE/NOTE)]).decode()
    current=read(BASE/NOTE,after[str(BASE/NOTE)]).decode()
    forward=original
    for removed,inserted in replacements:
        assert forward.count(removed)==1
        forward=forward.replace(removed,inserted)
    assert forward==current,'Unexpected additional source delta'
    inverse=current
    for removed,inserted in reversed(replacements):
        assert inverse.count(inserted)==1
        inverse=inverse.replace(inserted,removed)
    assert inverse==original,'Inverse byte recovery failed'
    diff=''.join(difflib.unified_diff(original.splitlines(True),current.splitlines(True),
                                    fromfile='archived/'+NOTE,tofile='corrected/'+NOTE))
    (OUT/'VERIFIED_DELTA.diff').write_text(diff)
    result={'created_utc':datetime.now(timezone.utc).isoformat(),
            'status':'PASS; F1 resolved at the corrected note identity.',
            'scope':'Only complete source delta and source/evidence authentication; no mathematical rerun.',
            'original_author_artifacts_archived':13,'original_author_seals_archived':1,
            'corrected_author_artifacts_authenticated':13,'unchanged_author_artifacts':12,
            'prior_sealed_bindings_authenticated':counts,
            'changed_source':{'before':before[str(BASE/NOTE)],'after':after[str(BASE/NOTE)]},
            'complete_delta_is_exactly_two_unique_replacements':True,'inverse_byte_recovery':True,
            'assessment':'Section3 explicitly excludes arbitrary added N,T-commuting jumps; Section4 expressly inherits that restricted model and names occupation-monitoring jumps. The broader Section1 count identity remains intact.',
            'archive_mapping':archive_mapping,'failed_attempts':[],
            'sources':sorted(BINDINGS.values(),key=lambda row:row['path'])}
    (OUT/'CORRECTION_ACK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['sources','archive_mapping']},indent=2))
    print('Unique authenticated inputs:',len(BINDINGS))


if __name__=='__main__':main()
