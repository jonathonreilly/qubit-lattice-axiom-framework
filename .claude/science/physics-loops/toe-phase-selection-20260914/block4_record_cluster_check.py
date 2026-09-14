#!/usr/bin/env python3
"""Protected finite Record-star geometry inside the periodic routing template.

Port demands (8,1,1) are extracted from the actual width-four fixture.
The periodic edge roster below is a stress family, not an arbitrary-cover DK
source. It tests the local cluster template and its finite-period extension.
"""
import json
from math import isqrt
from pathlib import Path

from block4_periodic_routing_check import Compiler, Edge, add


class RecordCompiler(Compiler):
    OFFSETS=((1,0,0),(0,1,0),(0,0,1),(0,0,0))
    BLANKS={(-1,0,0),(0,-1,0),(0,0,-1)}

    def __init__(self, edges):
        super().__init__((4,3,2,3),edges)
        self.columns=isqrt(self.colors)
        if self.columns*self.columns<self.colors:
            self.columns+=1
        assert [sum(e.left==h for e in edges)+sum(e.right==h for e in edges)
                for h in range(4)]==[8,1,1,0]

    def cluster_center(self,n):
        index=self.color_id(n)
        offset=(10+20*(index % self.columns),10+20*(index//self.columns),self.z0)
        return tuple(self.side*a+b for a,b in zip(n,offset))

    def home(self,n,h):
        return add(self.cluster_center(n),self.OFFSETS[h])

    def escape(self,home,port):
        coarse=tuple(a//self.side for a in home)
        center=self.cluster_center(coarse)
        offset=tuple(a-b for a,b in zip(home,center))
        h=self.OFFSETS.index(offset)
        if h==0:
            legacy=(0,1,2,6,7,8,9,10)[port]
        else:
            assert h in (1,2) and port==0
            legacy=3  # negative x direction and branch -1
        group,slot=divmod(legacy,3)
        branch=(-1,0,1)[slot]
        if group in (0,1):
            sign=1 if group==0 else -1
            relative=[(sign,0,0),(2*sign,0,0),(3*sign,0,0)]
            if branch:
                relative.append((3*sign,branch,0))
            relative.append((3*sign,branch,1))
        else:
            assert group in (2,3)
            sign=1 if group==2 else -1
            relative=[(0,sign,0),(0,2*sign,0),(0,3*sign,0)]
            if branch:
                relative.append((branch,3*sign,0))
            relative.append((branch,3*sign,1))
        return [add(home,r) for r in relative]

    def forbidden(self,site):
        if site[2] % self.side not in (self.z0-1,self.z0):
            return False
        coarse=tuple(a//self.side for a in site)
        center=self.cluster_center(coarse)
        return tuple(a-b for a,b in zip(site,center)) in self.BLANKS


def main():
    source=json.loads(Path(__file__).with_name('BLOCK4_DK_SOURCE_ROSTER.json').read_text())
    assert list(source['special_home_degrees'].values())==[8,1,1]
    edges=[Edge(0,0,0,1,(1,0,0)),Edge(0,2,0,3,(0,1,0)),
           Edge(0,0,0,2,(0,0,1)),Edge(0,1,1,0,(-1,0,1)),
           Edge(0,3,2,0,(0,-1,-1))]
    compiler=RecordCompiler(edges)
    p=compiler.period
    first,roster=compiler.coordinates((p,p,p))
    second,_=compiler.coordinates((2*p,p,p),roster)
    assert second['active_sites']==2*first['active_sites']
    assert second['hidden_variables']==2*first['hidden_variables']
    assert first['ordinary_maximum']<=3
    assert first['maximum_payload_load']==4
    result=dict(source_revision=source['source_sha256'],ports=[8,1,1],
                cluster_payloads=[4,3,2,3],blank_neighbors_preserved=True,
                microcell_side=compiler.side,fundamental=first,doubled=second,
                scope='actual finite-fixture cluster port/geometry match; periodic DK source still not matched')
    Path(__file__).with_name('BLOCK4_RECORD_CLUSTER_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
