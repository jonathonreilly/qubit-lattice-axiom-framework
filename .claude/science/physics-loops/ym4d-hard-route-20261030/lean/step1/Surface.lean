import Init

/-!
Row 1428 (b), (c): a signed closed fundamental surface of SU(2) plaquettes, evaluated by
integer contraction of the Haar second moments, with acceptance fixtures that must fail.
Only `import Init`; no mathlib, no `native_decide`.

Model (the connection to the Haar integral is NOT proved here; see the lane report):
* a surface is a list of faces, each an oriented cycle of four vertices;
* a face carries `b * tr(U_1 U_2 U_3 U_4)`; the trace is a sum over one two-valued index
  per corner of the face (the index between two consecutive links sits at their common vertex);
* each link lies in exactly two faces; with `eps = [[0,1],[-1,0]]`, for Haar measure on SU(2)
    same direction:      `2 ∫ U_ab U_cd        = eps_ac eps_bd`
    opposite directions: `2 ∫ U_ab (U^-1)_cd   = delta_ad delta_bc`
  so every link contributes two integer "end factors", one at each of its ends, and `1/2`.
-/

namespace Step1Surface

/-- `k`-th entry of a list of naturals, 0 if out of range. -/
def nth : List Nat → Nat → Nat
  | [], _ => 0
  | a :: _, 0 => a
  | _ :: l, k + 1 => nth l k

def withIdx {α : Type} : Nat → List α → List (Nat × α)
  | _, [] => []
  | n, a :: l => (n, a) :: withIdx (n + 1) l

/-- A corner slot: face number, position in the face, vertex. -/
structure Slot where
  face : Nat
  pos : Nat
  vertex : Nat
  deriving DecidableEq, Repr

def slotsOfFaces (faces : List (List Nat)) : List Slot :=
  (withIdx 0 faces).flatMap fun (f, vs) => (withIdx 0 vs).map fun (k, v) => ⟨f, k, v⟩

/-- Slots sorted by vertex (`nV` vertices): the index variables in the order they are summed. -/
def varOrder (nV : Nat) (faces : List (List Nat)) : List Slot :=
  (List.range nV).flatMap fun v => (slotsOfFaces faces).filter fun s => s.vertex == v

def findIdx (s : Slot) : List Slot → Nat
  | [] => 0
  | t :: l => if t = s then 0 else findIdx s l + 1

/-- A traversal of a link by a face: tail vertex, head vertex, row variable, column variable. -/
structure Trav where
  tail : Nat
  head : Nat
  row : Nat
  col : Nat
  deriving DecidableEq, Repr

def travs (nV : Nat) (faces : List (List Nat)) : List Trav :=
  let order := varOrder nV faces
  (withIdx 0 faces).flatMap fun (f, vs) =>
    (List.range vs.length).map fun k =>
      let k' := (k + 1) % vs.length
      let a := nth vs k
      let b := nth vs k'
      ⟨a, b, findIdx ⟨f, k, a⟩ order, findIdx ⟨f, k', b⟩ order⟩

def linkKey (t : Trav) : Nat × Nat := (min t.tail t.head, max t.tail t.head)

def dedup : List (Nat × Nat) → List (Nat × Nat)
  | [] => []
  | a :: l => a :: (dedup l).filter (· != a)

def links (ts : List Trav) : List (Nat × Nat) := dedup (ts.map linkKey)

/-- An end factor between two index variables: `eps` or `delta`. -/
structure Factor where
  i : Nat
  j : Nat
  isEps : Bool
  deriving DecidableEq, Repr

/-- How the two end factors of a link are formed.  `Rule.haar` is the correct rule. -/
structure Rule where
  /-- value of `eps_xy` on bits -/
  eps : Nat → Nat → Int
  /-- use `eps eps` when the two faces run along the link in the same direction -/
  sameDirUsesEps : Bool

def Rule.haar : Rule := ⟨fun x y => (y : Int) - (x : Int), true⟩

def linkFactors (R : Rule) (t1 t2 : Trav) : List Factor :=
  if t1.tail = t2.tail then
    [⟨t1.row, t2.row, R.sameDirUsesEps⟩, ⟨t1.col, t2.col, R.sameDirUsesEps⟩]
  else
    [⟨t1.row, t2.col, false⟩, ⟨t1.col, t2.row, false⟩]

def factors (R : Rule) (ts : List Trav) : List Factor :=
  (links ts).flatMap fun key =>
    match ts.filter (fun t => linkKey t == key) with
    | [t1, t2] => linkFactors R t1 t2
    | _ => []

/-- Every link lies in exactly two faces. -/
def closed (ts : List Trav) : Bool :=
  (links ts).all fun key => (ts.filter (fun t => linkKey t == key)).length == 2

/-- Every link is run in opposite directions by its two faces (a consistent orientation). -/
def consistent (ts : List Trav) : Bool :=
  (links ts).all fun key =>
    match ts.filter (fun t => linkKey t == key) with
    | [t1, t2] => t1.tail != t2.tail
    | _ => false

def bit (σ v : Nat) : Nat := σ / 2 ^ v % 2

/-- Number of set bits among the lowest `n` bits. -/
def popc : Nat → Nat → Nat
  | 0, _ => 0
  | n + 1, m => m % 2 + popc n (m / 2)

def Factor.val (R : Rule) (F : Factor) (σ : Nat) : Int :=
  if F.isEps then R.eps (bit σ F.i) (bit σ F.j)
  else if bit σ F.i = bit σ F.j then 1 else 0

/-- The factors whose larger variable is `v`, for `v = 0, ..., n-1`. -/
def groups (fs : List Factor) (n : Nat) : List (List Factor) :=
  (List.range n).map fun v => fs.filter fun F => max F.i F.j == v

def prodL (R : Rule) (fs : List Factor) (σ : Nat) : Int :=
  fs.foldl (fun acc F => acc * F.val R σ) 1

/-- Evaluate `n` to a numeral before continuing (only matters for the kernel's speed). -/
def force {α : Type} (n : Nat) (k : Nat → α) : α :=
  match n with
  | 0 => k 0
  | m + 1 => k (m + 1)

/-- Sum over all assignments of the remaining variables (one group of factors per variable)
of the product of all factors, given the assignment `σ` of the earlier variables, the place
value `p = 2^v` of the current variable and the partial product `acc`.
A zero partial product is abandoned (it contributes 0). -/
def go (R : Rule) : List (List Factor) → Nat → Nat → Int → Int
  | [], _, _, acc => acc
  | fs :: rest, p, σ, acc =>
      force (σ + p) fun σ1 => force (2 * p) fun p' =>
        let a0 := acc * prodL R fs σ
        let a1 := acc * prodL R fs σ1
        (if a0 = 0 then 0 else go R rest p' σ a0)
          + (if a1 = 0 then 0 else go R rest p' σ1 a1)

/-- `∏_links 2 ∫ dU  ∏_faces tr(U_face)`, as an integer. -/
def haarSum (R : Rule) (nV : Nat) (faces : List (List Nat)) : Int :=
  let ts := travs nV faces
  go R (groups (factors R ts) ts.length) 1 0 1

/-- A rational number as numerator and denominator, not reduced. -/
structure Cert where
  num : Int
  den : Nat
  deriving DecidableEq, Repr

def prodI : List Int → Int := fun l => l.foldl (· * ·) 1
def prodN : List Nat → Nat := fun l => l.foldl (· * ·) 1

/-- Value of the surface: face coefficients `bs` (numerator, denominator), one denominator
per link (`2` for the correct Haar normalisation `1/d`, `d = 2`). -/
def evalSurface (R : Rule) (nV : Nat) (faces : List (List Nat)) (bs : List (Int × Nat))
    (linkDens : List Nat) : Cert :=
  ⟨prodI (bs.map (·.1)) * haarSum R nV faces, prodN (bs.map (·.2)) * prodN linkDens⟩

/-- The checker's acceptance test: both denominators nonzero and cross-multiplied equality. -/
def accept (c : Cert) (N : Int) (D : Nat) : Bool :=
  c.den != 0 && D != 0 && decide (c.num * (D : Int) = N * (c.den : Int))

/-- The same test WITHOUT the guard on the denominators (a wrong checker). -/
def crossOnly (c : Cert) (N : Int) (D : Nat) : Bool :=
  decide (c.num * (D : Int) = N * (c.den : Int))

/-! ## The cube -/

/-- Vertices `x + 2y + 4z`; faces oriented outward. -/
def cube : List (List Nat) :=
  [[0, 2, 3, 1], [4, 5, 7, 6], [0, 1, 5, 4], [2, 6, 7, 3], [0, 4, 6, 2], [1, 3, 7, 5]]

/-- Reverse the faces whose bit in `m` is set. -/
def reorient (m : Nat) (faces : List (List Nat)) : List (List Nat) :=
  (withIdx 0 faces).map fun (f, vs) => if bit m f = 1 then vs.reverse else vs

def b16 (n : Nat) : List (Int × Nat) := List.replicate n (1, 16)
def twos (n : Nat) : List Nat := List.replicate n 2

theorem cube_counts :
    ((travs 8 cube).length, (links (travs 8 cube)).length, cube.length) = (24, 12, 6) := by
  decide +kernel
theorem cube_closed : closed (travs 8 cube) = true := by decide +kernel
theorem cube_consistent : consistent (travs 8 cube) = true := by decide +kernel
/-- One free index per vertex: `d^V = 2^8`. -/
theorem cube_haarSum : haarSum Rule.haar 8 cube = 256 := by decide +kernel
/-- (b) The closed fundamental cube at `b = 1/16` is `b^6 / 16 = 2^(-28)`. -/
theorem cube_value :
    accept (evalSurface Rule.haar 8 cube (b16 6) (twos 12)) 1 (2 ^ 28) = true := by decide +kernel
theorem cube_value_cert :
    evalSurface Rule.haar 8 cube (b16 6) (twos 12) = ⟨256, 16 ^ 6 * 2 ^ 12⟩ := by decide +kernel
/-- The sign does not depend on how the six faces are oriented (`chi_(1/2)` is real):
all 64 orientations, one theorem each; `eps eps` factors occur in 62 of them. -/
theorem cube_orient_0 : haarSum Rule.haar 8 (reorient 0 cube) = 256 := by decide +kernel
theorem cube_orient_1 : haarSum Rule.haar 8 (reorient 1 cube) = 256 := by decide +kernel
theorem cube_orient_2 : haarSum Rule.haar 8 (reorient 2 cube) = 256 := by decide +kernel
theorem cube_orient_3 : haarSum Rule.haar 8 (reorient 3 cube) = 256 := by decide +kernel
theorem cube_orient_4 : haarSum Rule.haar 8 (reorient 4 cube) = 256 := by decide +kernel
theorem cube_orient_5 : haarSum Rule.haar 8 (reorient 5 cube) = 256 := by decide +kernel
theorem cube_orient_6 : haarSum Rule.haar 8 (reorient 6 cube) = 256 := by decide +kernel
theorem cube_orient_7 : haarSum Rule.haar 8 (reorient 7 cube) = 256 := by decide +kernel
theorem cube_orient_8 : haarSum Rule.haar 8 (reorient 8 cube) = 256 := by decide +kernel
theorem cube_orient_9 : haarSum Rule.haar 8 (reorient 9 cube) = 256 := by decide +kernel
theorem cube_orient_10 : haarSum Rule.haar 8 (reorient 10 cube) = 256 := by decide +kernel
theorem cube_orient_11 : haarSum Rule.haar 8 (reorient 11 cube) = 256 := by decide +kernel
theorem cube_orient_12 : haarSum Rule.haar 8 (reorient 12 cube) = 256 := by decide +kernel
theorem cube_orient_13 : haarSum Rule.haar 8 (reorient 13 cube) = 256 := by decide +kernel
theorem cube_orient_14 : haarSum Rule.haar 8 (reorient 14 cube) = 256 := by decide +kernel
theorem cube_orient_15 : haarSum Rule.haar 8 (reorient 15 cube) = 256 := by decide +kernel
theorem cube_orient_16 : haarSum Rule.haar 8 (reorient 16 cube) = 256 := by decide +kernel
theorem cube_orient_17 : haarSum Rule.haar 8 (reorient 17 cube) = 256 := by decide +kernel
theorem cube_orient_18 : haarSum Rule.haar 8 (reorient 18 cube) = 256 := by decide +kernel
theorem cube_orient_19 : haarSum Rule.haar 8 (reorient 19 cube) = 256 := by decide +kernel
theorem cube_orient_20 : haarSum Rule.haar 8 (reorient 20 cube) = 256 := by decide +kernel
theorem cube_orient_21 : haarSum Rule.haar 8 (reorient 21 cube) = 256 := by decide +kernel
theorem cube_orient_22 : haarSum Rule.haar 8 (reorient 22 cube) = 256 := by decide +kernel
theorem cube_orient_23 : haarSum Rule.haar 8 (reorient 23 cube) = 256 := by decide +kernel
theorem cube_orient_24 : haarSum Rule.haar 8 (reorient 24 cube) = 256 := by decide +kernel
theorem cube_orient_25 : haarSum Rule.haar 8 (reorient 25 cube) = 256 := by decide +kernel
theorem cube_orient_26 : haarSum Rule.haar 8 (reorient 26 cube) = 256 := by decide +kernel
theorem cube_orient_27 : haarSum Rule.haar 8 (reorient 27 cube) = 256 := by decide +kernel
theorem cube_orient_28 : haarSum Rule.haar 8 (reorient 28 cube) = 256 := by decide +kernel
theorem cube_orient_29 : haarSum Rule.haar 8 (reorient 29 cube) = 256 := by decide +kernel
theorem cube_orient_30 : haarSum Rule.haar 8 (reorient 30 cube) = 256 := by decide +kernel
theorem cube_orient_31 : haarSum Rule.haar 8 (reorient 31 cube) = 256 := by decide +kernel
theorem cube_orient_32 : haarSum Rule.haar 8 (reorient 32 cube) = 256 := by decide +kernel
theorem cube_orient_33 : haarSum Rule.haar 8 (reorient 33 cube) = 256 := by decide +kernel
theorem cube_orient_34 : haarSum Rule.haar 8 (reorient 34 cube) = 256 := by decide +kernel
theorem cube_orient_35 : haarSum Rule.haar 8 (reorient 35 cube) = 256 := by decide +kernel
theorem cube_orient_36 : haarSum Rule.haar 8 (reorient 36 cube) = 256 := by decide +kernel
theorem cube_orient_37 : haarSum Rule.haar 8 (reorient 37 cube) = 256 := by decide +kernel
theorem cube_orient_38 : haarSum Rule.haar 8 (reorient 38 cube) = 256 := by decide +kernel
theorem cube_orient_39 : haarSum Rule.haar 8 (reorient 39 cube) = 256 := by decide +kernel
theorem cube_orient_40 : haarSum Rule.haar 8 (reorient 40 cube) = 256 := by decide +kernel
theorem cube_orient_41 : haarSum Rule.haar 8 (reorient 41 cube) = 256 := by decide +kernel
theorem cube_orient_42 : haarSum Rule.haar 8 (reorient 42 cube) = 256 := by decide +kernel
theorem cube_orient_43 : haarSum Rule.haar 8 (reorient 43 cube) = 256 := by decide +kernel
theorem cube_orient_44 : haarSum Rule.haar 8 (reorient 44 cube) = 256 := by decide +kernel
theorem cube_orient_45 : haarSum Rule.haar 8 (reorient 45 cube) = 256 := by decide +kernel
theorem cube_orient_46 : haarSum Rule.haar 8 (reorient 46 cube) = 256 := by decide +kernel
theorem cube_orient_47 : haarSum Rule.haar 8 (reorient 47 cube) = 256 := by decide +kernel
theorem cube_orient_48 : haarSum Rule.haar 8 (reorient 48 cube) = 256 := by decide +kernel
theorem cube_orient_49 : haarSum Rule.haar 8 (reorient 49 cube) = 256 := by decide +kernel
theorem cube_orient_50 : haarSum Rule.haar 8 (reorient 50 cube) = 256 := by decide +kernel
theorem cube_orient_51 : haarSum Rule.haar 8 (reorient 51 cube) = 256 := by decide +kernel
theorem cube_orient_52 : haarSum Rule.haar 8 (reorient 52 cube) = 256 := by decide +kernel
theorem cube_orient_53 : haarSum Rule.haar 8 (reorient 53 cube) = 256 := by decide +kernel
theorem cube_orient_54 : haarSum Rule.haar 8 (reorient 54 cube) = 256 := by decide +kernel
theorem cube_orient_55 : haarSum Rule.haar 8 (reorient 55 cube) = 256 := by decide +kernel
theorem cube_orient_56 : haarSum Rule.haar 8 (reorient 56 cube) = 256 := by decide +kernel
theorem cube_orient_57 : haarSum Rule.haar 8 (reorient 57 cube) = 256 := by decide +kernel
theorem cube_orient_58 : haarSum Rule.haar 8 (reorient 58 cube) = 256 := by decide +kernel
theorem cube_orient_59 : haarSum Rule.haar 8 (reorient 59 cube) = 256 := by decide +kernel
theorem cube_orient_60 : haarSum Rule.haar 8 (reorient 60 cube) = 256 := by decide +kernel
theorem cube_orient_61 : haarSum Rule.haar 8 (reorient 61 cube) = 256 := by decide +kernel
theorem cube_orient_62 : haarSum Rule.haar 8 (reorient 62 cube) = 256 := by decide +kernel
theorem cube_orient_63 : haarSum Rule.haar 8 (reorient 63 cube) = 256 := by decide +kernel
/-- The reoriented cubes do use the `eps` rule: for the mask 1 the orientation is inconsistent. -/
theorem cube_reoriented_inconsistent : consistent (travs 8 (reorient 1 cube)) = false := by
  decide +kernel

/-! ## Fixtures that must fail (each names its corruption) -/

/-- C1, "one missing 1/d": the factor `1/2` of exactly one of the twelve link integrals is
replaced by 1.  The value becomes `2^(-27)` and the target `2^(-28)` is rejected. -/
theorem C1_one_link_missing_inv_d_rejected :
    accept (evalSurface Rule.haar 8 cube (b16 6) (1 :: twos 11)) 1 (2 ^ 28) = false := by
  decide +kernel
theorem C1_one_link_missing_inv_d_is_twice :
    accept (evalSurface Rule.haar 8 cube (b16 6) (1 :: twos 11)) 1 (2 ^ 27) = true := by
  decide +kernel

/-- C3, "zero denominator": one face coefficient is given as `0/0`.  The certificate is
`0/0`; cross-multiplication alone accepts it, the guarded test rejects it. -/
theorem C3_zero_over_zero_passes_unguarded :
    crossOnly (evalSurface Rule.haar 8 cube ((0, 0) :: b16 5) (twos 12)) 1 (2 ^ 28) = true := by
  decide +kernel
theorem C3_zero_over_zero_rejected :
    accept (evalSurface Rule.haar 8 cube ((0, 0) :: b16 5) (twos 12)) 1 (2 ^ 28) = false := by
  decide +kernel
/-- C3 bis: a zero link denominator, and a zero denominator in the claimed value. -/
theorem C3_zero_link_denominator_rejected :
    accept (evalSurface Rule.haar 8 cube (b16 6) (0 :: twos 11)) 1 (2 ^ 28) = false := by
  decide +kernel
theorem C3_zero_target_denominator_rejected :
    accept (evalSurface Rule.haar 8 cube (b16 6) (twos 12)) 1 0 = false := by decide +kernel

/-- C4a, "centre source on one face": one face coefficient is `-1/16`.  The value is
`-2^(-28)`; the untwisted target `+2^(-28)` is rejected. -/
theorem C4a_one_face_centre_source_is_minus :
    accept (evalSurface Rule.haar 8 cube ((-1, 16) :: b16 5) (twos 12)) (-1) (2 ^ 28) = true := by
  decide +kernel
theorem C4a_one_face_centre_source_plus_rejected :
    accept (evalSurface Rule.haar 8 cube ((-1, 16) :: b16 5) (twos 12)) 1 (2 ^ 28) = false := by
  decide +kernel

/-- The set of links of a face, as a bit mask over the list `links`. -/
def faceMask (nV : Nat) (faces : List (List Nat)) (vs : List Nat) : Nat :=
  let ls := links (travs nV faces)
  ((List.range vs.length).map fun k =>
    let a := nth vs k
    let b := nth vs ((k + 1) % vs.length)
    2 ^ (ls.findIdx? (· == (min a b, max a b))).getD 0).foldl (· + ·) 0

/-- Sign that the face with link mask `mask` gets from the link signs `z`
(bit `l` of `z` set: link `l` carries the centre element `-1`). -/
def faceSign (mask z : Nat) : Int := if (popc 12 (mask &&& z)) % 2 = 1 then -1 else 1

/-- C4b, "a closed twist pairs trivially with the cube": the six link masks of the faces
cancel mod 2 (every link lies in two faces), so link signs change no closed-cube value. -/
theorem C4b_face_masks :
    cube.map (faceMask 8 cube) = [15, 240, 792, 3138, 1665, 2340] := by decide +kernel
theorem C4b_face_masks_cancel :
    [15, 240, 792, 3138, 1665, 2340].foldl (· ^^^ ·) 0 = 0 := by decide
/-- Direct form for the twelve single-link twists and for all links at once. -/
theorem C4b_closed_twist_trivial_generators :
    ((4095 :: (List.range 12).map (2 ^ ·)).all fun z =>
      decide (prodI ([15, 240, 792, 3138, 1665, 2340].map (faceSign · z)) = 1)) = true := by
  decide +kernel
/-- and such a twist does change individual faces (the test is not vacuous). -/
theorem C4b_twist_is_nontrivial_on_faces :
    [15, 240, 792, 3138, 1665, 2340].map (faceSign · 1) = [-1, 1, 1, 1, -1, 1] := by
  decide +kernel

/-- C4c, "pairing sign dropped": `eps` replaced by its absolute value (`eps_10 = +1`).
With one face reversed the corrupted rule gives a wrong value and is rejected. -/
def Rule.absEps : Rule := ⟨fun x y => if x = y then 0 else 1, true⟩
/-- C4d, "direction ignored": `delta delta` used also when the two faces run the same way. -/
def Rule.noEps : Rule := ⟨fun x y => (y : Int) - (x : Int), false⟩

/-! ## The hemicube: a projective plane, where the pairing sign is visible

Vertices `0..3`, the six links of `K_4`, faces the three Hamiltonian four-cycles.
Hand value of the Haar integral: `-1/4` (lane report), so the integer sum is `-(1/4) 2^6 = -16`. -/

def hemicube : List (List Nat) := [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3]]

theorem hemicube_counts :
    ((travs 4 hemicube).length, (links (travs 4 hemicube)).length, hemicube.length) = (12, 6, 3) := by
  decide +kernel
theorem hemicube_closed : closed (travs 4 hemicube) = true := by decide +kernel
theorem hemicube_not_consistent : consistent (travs 4 hemicube) = false := by decide +kernel
theorem hemicube_haarSum : haarSum Rule.haar 4 hemicube = -16 := by decide +kernel
/-- At `b = 1/16`: `-(1/16)^3 / 4 = -2^(-14)`. -/
theorem hemicube_value :
    accept (evalSurface Rule.haar 4 hemicube (b16 3) (twos 6)) (-1) (2 ^ 14) = true := by
  decide +kernel
/-- The same for all eight orientations of the three faces. -/
theorem hemicube_orient_0 : haarSum Rule.haar 4 (reorient 0 hemicube) = -16 := by decide +kernel
theorem hemicube_orient_1 : haarSum Rule.haar 4 (reorient 1 hemicube) = -16 := by decide +kernel
theorem hemicube_orient_2 : haarSum Rule.haar 4 (reorient 2 hemicube) = -16 := by decide +kernel
theorem hemicube_orient_3 : haarSum Rule.haar 4 (reorient 3 hemicube) = -16 := by decide +kernel
theorem hemicube_orient_4 : haarSum Rule.haar 4 (reorient 4 hemicube) = -16 := by decide +kernel
theorem hemicube_orient_5 : haarSum Rule.haar 4 (reorient 5 hemicube) = -16 := by decide +kernel
theorem hemicube_orient_6 : haarSum Rule.haar 4 (reorient 6 hemicube) = -16 := by decide +kernel
theorem hemicube_orient_7 : haarSum Rule.haar 4 (reorient 7 hemicube) = -16 := by decide +kernel

/-- C4c rejected: with `|eps|` the hemicube has the wrong sign. -/
theorem C4c_abs_eps_value : haarSum Rule.absEps 4 hemicube = 16 := by decide +kernel
theorem C4c_abs_eps_rejected :
    accept (evalSurface Rule.absEps 4 hemicube (b16 3) (twos 6)) (-1) (2 ^ 14) = false := by
  decide +kernel
/-- C4d rejected: with `delta delta` on every link the hemicube value is wrong. -/
theorem C4d_no_eps_value : haarSum Rule.noEps 4 hemicube = 16 := by decide +kernel
theorem C4d_no_eps_rejected :
    accept (evalSurface Rule.noEps 4 hemicube (b16 3) (twos 6)) (-1) (2 ^ 14) = false := by
  decide +kernel
/-- The cube is blind to both corruptions (here with face 0 reversed, where `eps` occurs). -/
theorem cube_blind_to_abs_eps : haarSum Rule.absEps 8 (reorient 1 cube) = 256 := by decide +kernel
theorem cube_blind_to_no_eps : haarSum Rule.noEps 8 (reorient 1 cube) = 256 := by decide +kernel

/-! ## A wrapping sheet: the 3 x 3 torus

Vertices `x + 3y`, 18 links, 9 faces, `V - E + F = 0`; value `b^9 d^(V-E) = b^9 / 2^9`. -/

def torus : List (List Nat) :=
  (List.range 9).map fun p =>
    let x := p % 3
    let y := p / 3
    [x + 3 * y, (x + 1) % 3 + 3 * y, (x + 1) % 3 + 3 * ((y + 1) % 3), x + 3 * ((y + 1) % 3)]

theorem torus_closed : closed (travs 9 torus) = true := by decide +kernel
theorem torus_consistent : consistent (travs 9 torus) = true := by decide +kernel
theorem torus_haarSum : haarSum Rule.haar 9 torus = 512 := by decide +kernel
/-- At `b = 1/16`: `2^(-36) / 2^9 = 2^(-45)`. -/
theorem torus_value :
    accept (evalSurface Rule.haar 9 torus (b16 9) (twos 18)) 1 (2 ^ 45) = true := by decide +kernel
/-- C4e, "a wrapping sheet with odd twist pairing reverses sign": one face of the sheet
carries the centre sign.  `+2^(-45)` is rejected, `-2^(-45)` accepted. -/
theorem C4e_wrapping_sheet_odd_twist_is_minus :
    accept (evalSurface Rule.haar 9 torus ((-1, 16) :: b16 8) (twos 18)) (-1) (2 ^ 45) = true := by
  decide +kernel
theorem C4e_wrapping_sheet_odd_twist_plus_rejected :
    accept (evalSurface Rule.haar 9 torus ((-1, 16) :: b16 8) (twos 18)) 1 (2 ^ 45) = false := by
  decide +kernel
/-- With one face of the sheet reversed (so `eps` occurs) the value is unchanged. -/
theorem torus_one_face_reversed : haarSum Rule.haar 9 (reorient 1 torus) = 512 := by decide +kernel

end Step1Surface

#print axioms Step1Surface.cube_counts
#print axioms Step1Surface.cube_closed
#print axioms Step1Surface.cube_consistent
#print axioms Step1Surface.cube_haarSum
#print axioms Step1Surface.cube_value
#print axioms Step1Surface.cube_value_cert
#print axioms Step1Surface.cube_orient_0
#print axioms Step1Surface.cube_orient_1
#print axioms Step1Surface.cube_orient_63
#print axioms Step1Surface.cube_reoriented_inconsistent
#print axioms Step1Surface.C1_one_link_missing_inv_d_rejected
#print axioms Step1Surface.C1_one_link_missing_inv_d_is_twice
#print axioms Step1Surface.C3_zero_over_zero_passes_unguarded
#print axioms Step1Surface.C3_zero_over_zero_rejected
#print axioms Step1Surface.C3_zero_link_denominator_rejected
#print axioms Step1Surface.C3_zero_target_denominator_rejected
#print axioms Step1Surface.C4a_one_face_centre_source_is_minus
#print axioms Step1Surface.C4a_one_face_centre_source_plus_rejected
#print axioms Step1Surface.C4b_face_masks
#print axioms Step1Surface.C4b_face_masks_cancel
#print axioms Step1Surface.C4b_closed_twist_trivial_generators
#print axioms Step1Surface.C4b_twist_is_nontrivial_on_faces
#print axioms Step1Surface.hemicube_counts
#print axioms Step1Surface.hemicube_closed
#print axioms Step1Surface.hemicube_not_consistent
#print axioms Step1Surface.hemicube_haarSum
#print axioms Step1Surface.hemicube_value
#print axioms Step1Surface.hemicube_orient_7
#print axioms Step1Surface.C4c_abs_eps_value
#print axioms Step1Surface.C4c_abs_eps_rejected
#print axioms Step1Surface.C4d_no_eps_value
#print axioms Step1Surface.C4d_no_eps_rejected
#print axioms Step1Surface.cube_blind_to_abs_eps
#print axioms Step1Surface.cube_blind_to_no_eps
#print axioms Step1Surface.torus_closed
#print axioms Step1Surface.torus_consistent
#print axioms Step1Surface.torus_haarSum
#print axioms Step1Surface.torus_value
#print axioms Step1Surface.C4e_wrapping_sheet_odd_twist_is_minus
#print axioms Step1Surface.C4e_wrapping_sheet_odd_twist_plus_rejected
#print axioms Step1Surface.torus_one_face_reversed
