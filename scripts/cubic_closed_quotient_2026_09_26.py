"""Exact untruncated relative-component enumeration from original first output.

No database, numerical matrix or precomputed words are supplied. A guard hit
fails the runner; only an exhausted queue establishes the computed closure.
"""
from collections import deque
from pathlib import Path
import hashlib
import json
import sqlite3
import time
import cubic_one_pair_primitives_2026_09_26 as m


def canonical(s):
    negative=[v for v,q in s[0] if q==-1]
    assert len(negative)==1
    n=negative[0];ref=(0,0,0) if m.even(n) else (1,0,0)
    tau=tuple(a-b for a,b in zip(n,ref))
    return m.translate(s,m.neg(tau)),tau


def diagonal(s):
    q,e=m.unpack(s)
    occupied=[b for b,x in q.items() if not m.even(b) and x]
    active={a for b in occupied for a in m.nb(b)}
    pairs={tuple(sorted((a,c))) for a in active for c in m.partners(a)}
    value=0
    for a,c in pairs:
        oa=sum(b in occupied for b in m.nb(a))
        oc=sum(b in occupied for b in m.nb(c))
        common=sum(b in occupied and b in m.nb(c) for b in m.nb(a))
        value+=12*(oa+oc)-2*oa*oc-2*common
    return value


def build(directory):
    start=time.monotonic()
    first=m.pack({(0,0,0):-1,(1,0,0):1,(0,1,0):1},
                 {((0,0,0),(1,0,0)):-1,((0,0,0),(0,1,0)):-1})
    first,anchor=canonical(first);assert anchor==(0,0,0)
    states=[first];index={first:0};todo=deque([0]);edges=[];diags=[]
    while todo:
        i=todo.popleft();s=states[i]
        assert m.gauss(s) and m.cost(s)==0
        assert canonical(s)==(s,(0,0,0))
        h,_=m.projected_offdiag(s)
        for target,coefficient in h.items():
            assert coefficient<0 and coefficient%2==0
            assert m.gauss(target) and m.cost(target)==0
            assert all(abs(value)<=1 for edge,value in target[1])
            word,tau=canonical(target)
            neg=next(v for v,q in word[0] if q==-1)
            radius=max(sum(abs(a-b) for a,b in zip(v,neg))
                       for edge,value in word[1] for v in edge)
            assert radius<=6
            if word not in index:
                index[word]=len(states);states.append(word);todo.append(index[word])
            edges.append((i,index[word],*tau,coefficient))
        diags.append(diagonal(s))
        assert len(states)<=250000 and time.monotonic()-start<4800,'Incomplete: enumeration guard reached'
        if len(diags)%500==0:
            print(json.dumps({'closure_processed':len(diags),'discovered':len(states),
                              'queued':len(todo),'seconds':round(time.monotonic()-start,2)}),flush=True)
    assert len(states)==len(diags)==11322 and len(edges)==652416
    path=Path(directory)/'quotient-closed.sqlite3'
    db=sqlite3.connect(path)
    db.executescript('''CREATE TABLE states(id INTEGER PRIMARY KEY,word TEXT,processed INTEGER,diagonal INTEGER);
                       CREATE TABLE edges(src INTEGER,dst INTEGER,tx INTEGER,ty INTEGER,tz INTEGER,coefficient INTEGER);
                       CREATE TABLE metadata(key TEXT PRIMARY KEY,value TEXT);''')
    db.executemany('INSERT INTO states VALUES (?,?,?,?)',
                   [(i,json.dumps(s,separators=(',',':')),1,diags[i]) for i,s in enumerate(states)])
    db.executemany('INSERT INTO edges VALUES (?,?,?,?,?,?)',edges)
    db.execute('INSERT INTO metadata VALUES (?,?)',('status',json.dumps('exact_coordinate_quotient_closed')))
    db.commit();assert db.execute('PRAGMA integrity_check').fetchone()[0]=='ok';db.close()
    receipt={'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
             'status':'exact_coordinate_quotient_closed','words':len(states),'edges':len(edges),
             'remaining_queue':0,'elapsed_seconds':time.monotonic()-start}
    (Path(directory)/'QUOTIENT_CLOSURE_FREEZE.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt),flush=True)
    return receipt
