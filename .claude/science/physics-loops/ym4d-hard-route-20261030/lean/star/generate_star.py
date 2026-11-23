"""Emit a direct-kernel replay of the six-ray plaquette counts and the 24 boundary words."""
from pathlib import Path

source = r'''import Init

namespace Star

structure Vertex where
  t : Int
  x : Int
  y : Int
  z : Int
  deriving DecidableEq, BEq, Ord, Repr

structure Dir where
  axis : Nat
  step : Int
  deriving DecidableEq, Repr

def zero : Vertex := ⟨0, 0, 0, 0⟩
def time : Dir := ⟨0, 1⟩
def rays : List Dir := [⟨1,1⟩, ⟨1,-1⟩, ⟨2,1⟩, ⟨2,-1⟩, ⟨3,1⟩, ⟨3,-1⟩]

def advance (p : Vertex) (d : Dir) (n : Int := 1) : Vertex :=
  match d.axis with
  | 0 => {p with t := p.t + d.step*n}
  | 1 => {p with x := p.x + d.step*n}
  | 2 => {p with y := p.y + d.step*n}
  | _ => {p with z := p.z + d.step*n}

structure Face where
  p : Vertex
  a : Dir
  b : Dir

def flip (f : Face) : Face := ⟨f.p, f.b, f.a⟩

structure FaceKey where
  base : Vertex
  a : Nat
  b : Nat
  deriving DecidableEq, BEq, Ord, Repr

def lower (p : Vertex) (d : Dir) : Vertex :=
  if d.step < 0 then advance p d else p

def key (f : Face) : FaceKey :=
  ⟨lower (lower f.p f.a) f.b, min f.a.axis f.b.axis, max f.a.axis f.b.axis⟩

def strip (p : Vertex) (i : Dir) : List Face :=
  [⟨p, time, i⟩, ⟨advance p time, time, i⟩]

def detour (i j : Dir) : List Face :=
  let p := advance zero i
  let q := advance p i
  strip (advance p j) i ++ strip p j ++ (strip q j).map flip ++
  [flip ⟨p, i, j⟩, ⟨advance p time 2, i, j⟩]

def normals (i : Dir) := rays.filter (fun j => j.axis != i.axis)
def patches (i : Dir) :=
  strip zero i ++ strip (advance zero i) i ++ (normals i).flatMap (detour i)
def allKeys := (rays.flatMap patches).map key

structure EdgeKey where
  base : Vertex
  axis : Nat
  deriving BEq, DecidableEq, Ord

abbrev Chain := List (EdgeKey × Int)

def edge (p : Vertex) (d : Dir) (sign : Int) : EdgeKey × Int :=
  (⟨lower p d, d.axis⟩, sign*d.step)

def boundary (f : Face) : Chain :=
  [edge f.p f.a 1, edge (advance f.p f.a) f.b 1,
   edge (advance f.p f.b) f.a (-1), edge f.p f.b (-1)]

def vertexCode (v : Vertex) : Nat :=
  (((v.t.toNat*5 + (v.x+2).toNat)*5 + (v.y+2).toNat)*5 + (v.z+2).toNat)

def faceCode (k : FaceKey) : Nat := (vertexCode k.base * 4 + k.a)*4 + k.b

def maskFrom (used : Nat) : List Face → Option Nat
  | [] => some used
  | head :: tail =>
    let n := faceCode (key head)
    if used.testBit n then none else maskFrom (used.lor (Nat.shiftLeft 1 n)) tail

def takeEdge (k : EdgeKey) : List EdgeKey → Option (List EdgeKey)
  | [] => none
  | h :: t => if k == h then some t else (takeEdge k t).map (List.cons h)

def sameMultiset : List EdgeKey → List EdgeKey → Bool
  | [], ys => ys.isEmpty
  | k :: ks, ys =>
    match takeEdge k ys with
    | none => false
    | some tail => sameMultiset ks tail

def signedKeys (c : Chain) (s : Int) : List EdgeKey :=
  c.filterMap (fun v => if v.2 == s then some v.1 else none)

def sameBoundary (xs ys : List Face) : Bool :=
  let a := xs.flatMap boundary
  let b := ys.flatMap boundary
  sameMultiset (signedKeys a 1 ++ signedKeys b (-1))
    (signedKeys a (-1) ++ signedKeys b 1)

abbrev Step := EdgeKey × Int

def reversed (e : Step) : Step := (e.1, -e.2)

def rotate : Chain → Chain
  | [] => []
  | a :: tail => tail ++ [a]

def afterStep (target : Step) : Nat → Chain → Option Chain
  | 0, _ => none
  | _ + 1, [] => none
  | n + 1, a :: tail =>
    if a == target then some tail else afterStep target n (rotate (a :: tail))

def splice (f : Chain) : Chain → Option Chain
  | [] => none
  | e :: tail =>
    match afterStep (reversed e) f.length f with
    | some path => some (path ++ tail)
    | none => (splice f tail).map (List.cons e)

def reduceLinear (es : Chain) : Chain :=
  let push (stack : Chain) (e : Step) :=
    match stack with
    | [] => [e]
    | h :: t => if h == reversed e then t else e :: stack
  (es.foldl push []).reverse

def cancelEnds : Nat → Chain → Chain
  | 0, xs => xs
  | _ + 1, [] => []
  | n + 1, h :: t =>
    match t.reverse with
    | [] => [h]
    | last :: rest =>
      if last == reversed h then cancelEnds n rest.reverse else h :: t

def tidy (xs : Chain) : Chain :=
  let y := reduceLinear xs
  cancelEnds y.length y

def glueTail : Chain → List Face → Option Chain
  | s, [] => some s
  | s, f :: rest =>
    match splice (boundary f) s with
    | none => none
    | some ns => glueTail (tidy ns) rest

def glued : List Face → Option Chain
  | [] => none
  | f :: fs => glueTail (boundary f) fs

def cyclicallyEqual : Nat → Chain → Chain → Bool
  | 0, _, _ => false
  | n + 1, a, b => (a == b) || cyclicallyEqual n (rotate a) b

def wordTest (xs ys : List Face) : Bool :=
  match glued xs, glued ys with
  | some a, some b => cyclicallyEqual (a.length + 1) a b
  | _, _ => false

set_option maxRecDepth 16000
set_option maxHeartbeats 3000000
'''

rays = [(axis, sign) for axis in (1, 2, 3) for sign in (1, -1)]

def direction(d):
    return f'(⟨{d[0]}, {d[1]}⟩ : Dir)'

checks = []
for i_idx, i in enumerate(rays):
    ni = direction(i)
    outer = f'strip (advance zero {ni}) {ni}'
    for j_idx, j in enumerate(j for j in rays if j[0] != i[0]):
        nj = direction(j)
        patch = f'detour {ni} {nj}'
        name = f'detour_{i_idx}_{j_idx}'
        source += (f'theorem {name} : ({patch}).length = 8 ∧ '
                   f'sameBoundary ({patch}) ({outer}) = true ∧ '
                   f'wordTest ({patch}) ({outer}) = true := by decide\n')
        checks.append(name)
source += r'''
theorem maskSound {fs : List Face} {used result : Nat}
    (h : maskFrom used fs = some result) :
    (fs.map key).Nodup ∧ ∀ k ∈ fs.map key, used.testBit (faceCode k) = false := by
  induction fs generalizing used with
  | nil => simp
  | cons f fs ih =>
    let n := faceCode (key f)
    cases hm : used.testBit n with
    | true => simp [maskFrom, ← show n = faceCode (key f) from rfl, hm] at h
    | false =>
      have htail : maskFrom (used ||| (1 <<< n)) fs = some result := by
        simpa [maskFrom, ← show n = faceCode (key f) from rfl, hm] using h
      obtain ⟨hd, hzero⟩ := ih htail
      constructor
      · apply List.nodup_cons.mpr
        refine ⟨?_, hd⟩
        intro hmem
        have v := hzero (key f) hmem
        change (used ||| (1 <<< n)).testBit n = false at v
        rw [Nat.testBit_or, Nat.one_shiftLeft, Nat.testBit_two_pow] at v
        simp at v
      · intro k hk
        rcases List.mem_cons.mp hk with he | he
        · simpa [he] using hm
        · have v := hzero k he
          rw [Nat.testBit_or] at v
          exact (Bool.or_eq_false_iff.mp v).1

theorem globalMask : (maskFrom 0 (rays.flatMap patches)).isSome = true := by decide
theorem disjointFaces : allKeys.Nodup := by
  obtain ⟨_, h⟩ := Option.isSome_iff_exists.mp globalMask
  exact (maskSound h).1

theorem totalCount : allKeys.length = 216 := by decide
theorem rejectsDuplicate : maskFrom 0 ([⟨zero, time, ⟨1,1⟩⟩, ⟨zero, time, ⟨1,1⟩⟩]) = none := by decide
theorem rejectsBadOrientation :
    wordTest ((strip zero ⟨1,1⟩).map flip) (strip zero ⟨1,1⟩) = false := by decide
'''
for name in checks + ['maskSound', 'globalMask', 'disjointFaces', 'totalCount', 'rejectsDuplicate', 'rejectsBadOrientation']:
    source += f'#print axioms {name}\n'
source += 'end Star\n'
Path(__file__).with_name('Star.lean').write_text(source)
