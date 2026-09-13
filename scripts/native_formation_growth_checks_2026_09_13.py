#!/usr/bin/env python3
"""Finite geometry, exact probability, and bound checks; no growth simulation."""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 180
from collections import deque
import hashlib
import itertools
import json
import math
from pathlib import Path
import time

import sympy as s

HERE=Path(__file__).resolve().parents[1]
STEPS=tuple(tuple(sign if axis==j else 0 for j in range(3)) for axis in range(3) for sign in (-1,1))


def adjacent(v):
    return [tuple(x+y for x,y in zip(v,d)) for d in STEPS]


def program(v):
    return sum(x%2 for x in v)>=2


def candidate(v):
    return v[0]%2==1 and v[1]%4==2 and v[2]%2==0


def run():
    start=time.monotonic();checks=[]
    def checked(name,condition,**evidence):
        assert condition,name
        checks.append({"name":name,**evidence})
    cell=list(itertools.product(range(4),repeat=3))
    ps={v for v in cell if program(v)};rs={v for v in cell if candidate(v)}
    native={v for v in cell if sum(x%2 for x in v)==1}
    fuels={(v[0]-1,v[1],v[2]) for v in rs}
    checked("periodic_role_counts",len(ps)==32 and len(rs)==4 and len(native)==24 and len(fuels)==4)
    checked("program_native_fuel_disjoint",not(ps&native or ps&fuels or native&fuels))
    checked("all_four_native_transverse_neighbors_programs",all(sum(program(w) for w in adjacent(v))==4 for v in rs))
    checked("program_degrees_two_or_six",all(sum(program(w) for w in adjacent(v))==(6 if sum(x%2 for x in v)==3 else 2) for v in ps))
    checked("old_transverse_fuel_would_collide_with_program",all(program((v[0],v[1],v[2]+1)) for v in rs))
    root=(1,1,1);box=set(itertools.product(range(-7,10),repeat=3))
    distance={root:0};queue=deque([root])
    while queue:
        v=queue.popleft()
        for w in adjacent(v):
            if w in box and program(w) and w not in distance:
                distance[w]=distance[v]+1;queue.append(w)
    checked("program_geodesics_equal_Manhattan",all(d==sum(abs(x-y) for x,y in zip(v,root)) for v,d in distance.items()),vertices=len(distance))
    for n in range(7,25):
        m=(n-1)//3
        points=itertools.product(*(range(x-m,x+m+1) for x in root))
        number=sum(candidate(v) for v in points)
        checked(f"candidate_cube_lower_count_{n}",number>=m*m*(m//2),actual=number,lower_bound=m*m*(m//2))
    # Actual one-qubit program Born rule, not a copied probability table.
    plus=s.Matrix([1,1])/s.sqrt(2);Y=s.Matrix([[0,-s.I],[s.I,0]])
    theta=s.symbols('theta',real=True)
    U=s.cos(theta/2)*s.eye(2)+s.I*s.sin(theta/2)*Y
    out=U*plus
    checked("program_rotation_Born_identity",s.trigsimp(out[0]**2-(1+s.sin(theta))/2)==0)
    wrong=s.cos(theta/2)*s.eye(2)-s.I*s.sin(theta/2)*Y
    checked("wrong_program_rotation_sign_rejected",s.simplify(((wrong*plus)[0]**2).subs(theta,s.pi/6))!=s.Rational(3,4))
    for count in range(1,7):
        for positives in range(count+1):
            b=2*positives-count
            mixture=(3*s.Rational(positives,count)+s.Rational(count-positives,count))/4
            checked(f"common_kernel_n{count}_positive{positives}",mixture==s.Rational(1,2)+s.Rational(b,4*count))
    # Three present + Records and an unrecorded fourth |+x> program.
    early=(s.Rational(1,2)+s.Rational(2,16)+s.Rational(1,2)+s.Rational(4,16))/2
    checked("premature_native_activation_rejected",early==s.Rational(11,16) and early!=s.Rational(3,4),gap=str(s.Rational(3,4)-early))
    # Verify the analytical parameter substitutions, retaining loose/vacuous cases.
    for duration in (1.,10.,100.,1000.):
        n=math.floor(duration/(8*math.log(2)))
        checked(f"lower_front_exponent_{duration}",n*math.log(2)-duration/4<=-duration/8+1e-12)
        upper=math.ceil(12*math.e*duration)
        checked(f"upper_front_base_{duration}",6*math.e*duration/upper<=.5)
    return {"status":"passed","count":len(checks),"checks":checks,"seconds":time.monotonic()-start,
            "source_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "note_sha256":hashlib.sha256((HERE/'docs/NATIVE_GROWING_FORMATION_CURRENT_BOUNDED_THEOREM_NOTE_2026-09-13.md').read_bytes()).hexdigest(),
            "scope":"same-author exact finite role/probability checks; front bounds are analytical"}
