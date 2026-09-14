#!/usr/bin/env python3
"""Read/extract the supplied finite DK graph; do not call it a periodic family."""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'scripts'))
import admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_explicit_certificate_2026_08_23 as source


def main():
    captured={}
    def capture(precision,homes,slots,record_hidden):
        edges=[(a,b,str(c)) for (a,b),c in sorted(precision.items())
               if a!=b and not source.exact_zero(c) and homes[a]!=homes[b]]
        degree=Counter()
        for a,b,c in edges:
            degree[homes[a]]+=1
            degree[homes[b]]+=1
        captured.update(
            edge_count=len(edges),
            special_home_degrees={str(site):degree[site] for site in
                                 (source.S0_SITE,source.S1_SITE,source.S2_SITE)},
            maximum_home_degree=max(degree.values()),
            special_packing={str(site):sorted(label for label in homes if homes[label]==site)
                             for site in (source.S0_SITE,source.S1_SITE,source.S2_SITE)},
            record_hidden=list(record_hidden),
            edges=edges,
            homes={label:list(site) for label,site in sorted(homes.items())},
            diagonal={a:str(c) for (a,b),c in precision.items() if a==b},
            note='finite fixture graph captured before its volume-growing crossbar; no arbitrary-cover matching')
        return False,{'reason':'probe intercepted before routing; this is not a source check failure'}
    original=source.route_graph
    source.route_graph=capture
    try:
        fixture=source.b174.Fixture(4,pattern=None,tag='personal-block4-source-probe')
        halves,thirds,_=source.arm_sets(fixture)
        bundles=(halves,thirds)
        rosters=source.row_rosters(bundles)
        changed=source.changed_rows(halves)
        changing=source.changing_sets(bundles,changed,rosters)
        pack=source.record_pack(changed,changing)
        source.build_split_certificate(fixture,4,'m2',halves,bundles,rosters,changed,changing,pack)
    finally:
        source.route_graph=original
    assert captured['edge_count']==494
    captured['source_sha256']=sha256(Path(source.__file__).read_bytes()).hexdigest()
    captured['supplier_sha256']=sha256(Path(source.b43.__file__).read_bytes()).hexdigest()
    Path(__file__).with_name('BLOCK4_DK_SOURCE_ROSTER.json').write_text(json.dumps(captured,indent=2)+'\n')
    print(json.dumps({k:v for k,v in captured.items() if k not in ('edges','homes','diagonal')},indent=2))


if __name__=='__main__':
    main()
