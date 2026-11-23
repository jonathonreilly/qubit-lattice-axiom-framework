import Init

/-!
Row 1428 (a): the N = 1 four-dimensional link inventory of row 1418
(`library/gap-rg-step-sizing-astra62.md`), checked by kernel evaluation.
Only `import Init`; no mathlib, no `native_decide`.
-/

namespace Step1

/-! ## Link inventory: 1, 15, 30, 5 and D_1 = 51 -/

/-- Coefficientwise sum of two coefficient lists. -/
def addL : List Nat → List Nat → List Nat
  | [], q => q
  | p, [] => p
  | a :: p, b :: q => (a + b) :: addL p q

/-- `pw k` lists the coefficients of `(1 + z^2)^k = z^k (z + 1/z)^k`. -/
def pw : Nat → List Nat
  | 0 => [1]
  | k + 1 => addL (pw k) (0 :: 0 :: pw k)

/-- Singlet multiplicity of `k` fundamentals of SU(2) by the weight count:
multiplicity of weight 0 minus multiplicity of weight 2 in `(z + 1/z)^k`. -/
def singlet (k : Nat) : Nat := (pw k).getD k 0 - (pw k).getD (k + 2) 0

/-- The weight used at a node of degree `k`: `Cat(k/2)` for even `k <= 6`, else 0. -/
def w : Nat → Nat
  | 0 => 1
  | 2 => 1
  | 4 => 2
  | 6 => 5
  | _ => 0

/-- Pascal's rule. -/
def choose : Nat → Nat → Nat
  | _, 0 => 1
  | 0, _ + 1 => 0
  | n + 1, k + 1 => choose n k + choose n (k + 1)

/-- Number of set bits among the lowest `n` bits. -/
def popc : Nat → Nat → Nat
  | 0, _ => 0
  | n + 1, m => m % 2 + popc n (m / 2)

theorem singlet_table : (List.range 7).map singlet = [1, 0, 1, 0, 2, 0, 5] := by decide
theorem w_is_singlet : (List.range 7).map w = (List.range 7).map singlet := by decide
theorem link_counts :
    [0, 2, 4, 6].map (fun k => choose 6 k * singlet k) = [1, 15, 30, 5] := by decide
theorem link_total_by_occupancy :
    ([0, 1, 2, 3, 4, 5, 6].map (fun k => choose 6 k * singlet k)).sum = 51 := by decide
/-- Direct enumeration of the 64 six-bit occupation patterns of a link. -/
theorem link_total_by_patterns :
    ((List.range 64).map (fun m => singlet (popc 6 m))).sum = 51 := by decide

/-! ### The generating function of row 1418

`D_N = [z^(6N)] (1 - z^(N+1))^6 (1 - z^(N+2))^6 / ((1 - z)^6 (1 - z^2)^5)`,
evaluated by integer power series truncated at degree `6N`. -/

/-- Truncate or pad to exactly `n` coefficients. -/
def fit : Nat → List Int → List Int
  | 0, _ => []
  | n + 1, [] => 0 :: fit n []
  | n + 1, a :: p => a :: fit n p

def addI : List Int → List Int → List Int
  | [], q => q
  | p, [] => p
  | a :: p, b :: q => (a + b) :: addI p q

def shift (m : Nat) (p : List Int) : List Int := List.replicate m 0 ++ p

/-- Multiply by `1 - z^m`, truncated to `n` coefficients. -/
def mulOneMinus (n m : Nat) (p : List Int) : List Int :=
  fit n (addI p ((shift m p).map (fun a => -a)))

/-- Divide by `1 - z^m` (`m >= 1`), truncated to `n` coefficients:
the sum of the shifts by `0, m, 2m, ...`. -/
def divOneMinus (n m : Nat) (p : List Int) : List Int :=
  (List.range n).foldl (fun acc j => fit n (addI acc (shift (j * m) p))) (fit n [])

def iter {α : Type} (f : α → α) : Nat → α → α
  | 0, a => a
  | k + 1, a => iter f k (f a)

def D (N : Nat) : Int :=
  let n := 6 * N + 1
  let p0 : List Int := fit n [1]
  let p1 := iter (mulOneMinus n (N + 1)) 6 p0
  let p2 := iter (mulOneMinus n (N + 2)) 6 p1
  let p3 := iter (divOneMinus n 1) 6 p2
  let p4 := iter (divOneMinus n 2) 5 p3
  p4.getD (6 * N) 0

/-- Division is the inverse of multiplication on a test series (sanity of the two helpers). -/
theorem div_mul_sanity :
    divOneMinus 9 2 (mulOneMinus 9 2 [3, -1, 4, 1, -5, 9, 2, -6, 5]) = [3, -1, 4, 1, -5, 9, 2, -6, 5] := by
  decide
theorem D_one : D 1 = 51 := by decide +kernel
theorem D_two : D 2 = 977 := by decide +kernel

/-! ## Site slots: the vertex figure K_{2,2,2,2}

Nodes `0..7` are the eight link ends at a site; the antipode of `i` is `i ^^^ 1`.
The 24 corners are the pairs `i < j` with `j ≠ i ^^^ 1`.  A degree vector is one
natural number in base 8 (every degree is at most 6).  Everything is written for
`n` nodes so that the same code runs on the octahedron K_{2,2,2} (`n = 6`). -/

def corners (n : Nat) : List (Nat × Nat) :=
  (List.range n).flatMap fun i =>
    ((List.range n).filter fun j => decide (i < j) && (j != i ^^^ 1)).map fun j => (i, j)

theorem corners_card : (corners 8).length = 24 := by decide
theorem corners_degree_six :
    (List.range 8).map (fun v => ((corners 8).filter fun e => e.1 == v || e.2 == v).length)
      = [6, 6, 6, 6, 6, 6, 6, 6] := by decide

def cornerConst (e : Nat × Nat) : Nat := 8 ^ e.1 + 8 ^ e.2

/-- Product of `w` over the lowest `n` base-8 digits. -/
def wt : Nat → Nat → Nat
  | 0, _ => 1
  | n + 1, d => w (d % 8) * wt n (d / 8)

/-- 1 if the lowest `n` base-8 digits are all even, else 0. -/
def evenAll : Nat → Nat → Nat
  | 0, _ => 1
  | n + 1, d => (if d % 2 = 0 then 1 else 0) * evenAll n (d / 8)

/-- The definition: sum over ALL subsets of the given corners of `leaf (degree vector)`. -/
def brute (leaf : Nat → Nat) : List Nat → Nat → Nat
  | [], d => leaf d
  | c :: cs, d => brute leaf cs d + brute leaf cs (d + c)

/-- A step of the pruned enumeration. -/
inductive Step where
  | corner (c : Nat)
  | check (i : Nat)
  deriving DecidableEq, Repr

/-- Corners in lexicographic order; after the block of corners `(i, _)` every corner at
node `i` is decided (those `(h, i)` with `h < i` came earlier), so its parity is tested. -/
def steps (n : Nat) : List Step :=
  (List.range n).flatMap fun i =>
    (((corners n).filter fun e => e.1 == i).map fun e => Step.corner (cornerConst e)) ++ [Step.check i]

/-- Same sum as `brute`, abandoning a branch once a completed node has odd degree
(both `wt n` and `evenAll n` vanish there). -/
def pruned (leaf : Nat → Nat) : List Step → Nat → Nat
  | [], d => leaf d
  | .corner c :: cs, d => pruned leaf cs d + pruned leaf cs (d + c)
  | .check i :: cs, d => if (d / 8 ^ i) % 2 = 1 then 0 else pruned leaf cs d

/-- `pruned` with the accumulator forced to a numeral at every step.  The kernel then
keeps the degree vector as a literal (measured: 5 times faster, 3 times less memory). -/
def prunedS (leaf : Nat → Nat) : List Step → Nat → Nat
  | [], d => leaf d
  | .corner c :: cs, d =>
      match d + c with
      | 0 => prunedS leaf cs d + prunedS leaf cs 0
      | e + 1 => prunedS leaf cs d + prunedS leaf cs (e + 1)
  | .check i :: cs, d => if (d / 8 ^ i) % 2 = 1 then 0 else prunedS leaf cs d

theorem prunedS_eq (leaf : Nat → Nat) : ∀ (cs : List Step) (d : Nat),
    prunedS leaf cs d = pruned leaf cs d
  | [], _ => rfl
  | .corner c :: cs, d => by
      have h1 := prunedS_eq leaf cs d
      have h2 := prunedS_eq leaf cs (d + c)
      show (match d + c with
        | 0 => prunedS leaf cs d + prunedS leaf cs 0
        | e + 1 => prunedS leaf cs d + prunedS leaf cs (e + 1)) = pruned leaf cs d + pruned leaf cs (d + c)
      rw [← h1, ← h2]
      generalize d + c = x
      cases x <;> rfl
  | .check i :: cs, d => by
      have h1 := prunedS_eq leaf cs d
      show (if (d / 8 ^ i) % 2 = 1 then 0 else prunedS leaf cs d)
        = (if (d / 8 ^ i) % 2 = 1 then 0 else pruned leaf cs d)
      rw [h1]

/-! ### The pruning agrees with the all-subsets definition on the octahedron K_{2,2,2}

12 corners, 4,096 subsets, `2^(12-6+1) = 128` even subgraphs. -/

theorem octahedron_even :
    brute (evenAll 6) ((corners 6).map cornerConst) 0 = 128 := by decide +kernel
theorem octahedron_even_pruned :
    prunedS (evenAll 6) (steps 6) 0 = 128 := by decide +kernel
theorem octahedron_slots_agree :
    brute (wt 6) ((corners 6).map cornerConst) 0 = prunedS (wt 6) (steps 6) 0 := by decide +kernel

/-! ### Splitting the sum by the pattern at node 0 -/

/-- All subset sums of the given constants, starting from the list `ds`. -/
def expand : List Nat → List Nat → List Nat
  | [], ds => ds
  | c :: cs, ds => expand cs (ds ++ ds.map (· + c))

theorem sum_map_add (f g : Nat → Nat) : ∀ l : List Nat,
    (l.map fun d => f d + g d).sum = (l.map f).sum + (l.map g).sum
  | [] => rfl
  | a :: l => by
      have h := sum_map_add f g l
      show f a + g a + (l.map fun d => f d + g d).sum = f a + (l.map f).sum + (g a + (l.map g).sum)
      omega

theorem sum_append_nat : ∀ l₁ l₂ : List Nat, (l₁ ++ l₂).sum = l₁.sum + l₂.sum
  | [], l₂ => by show l₂.sum = 0 + l₂.sum; omega
  | a :: l₁, l₂ => by
      have h := sum_append_nat l₁ l₂
      show a + (l₁ ++ l₂).sum = a + l₁.sum + l₂.sum
      omega

theorem map_map_nat (f : Nat → Nat) (g : Nat → Nat) : ∀ l : List Nat,
    (l.map g).map f = l.map (fun d => f (g d))
  | [] => rfl
  | a :: l => by
      show f (g a) :: (l.map g).map f = f (g a) :: l.map (fun d => f (g d))
      rw [map_map_nat f g l]

theorem map_append_nat (f : Nat → Nat) : ∀ l₁ l₂ : List Nat,
    (l₁ ++ l₂).map f = l₁.map f ++ l₂.map f
  | [], _ => rfl
  | a :: l₁, l₂ => by
      show f a :: (l₁ ++ l₂).map f = f a :: (l₁.map f ++ l₂.map f)
      rw [map_append_nat f l₁ l₂]

/-- The sum over the first block of corners, written as a sum over start vectors. -/
theorem split (leaf : Nat → Nat) (rest : List Step) : ∀ (cs : List Nat) (ds : List Nat),
    (ds.map (pruned leaf (cs.map Step.corner ++ rest))).sum
      = ((expand cs ds).map (pruned leaf rest)).sum
  | [], _ => rfl
  | c :: cs, ds => by
      have ih := split leaf rest cs (ds ++ ds.map (· + c))
      show (ds.map fun d => pruned leaf (cs.map Step.corner ++ rest) d
              + pruned leaf (cs.map Step.corner ++ rest) (d + c)).sum
          = ((expand cs (ds ++ ds.map (· + c))).map (pruned leaf rest)).sum
      rw [← ih, sum_map_add, map_append_nat, sum_append_nat, map_map_nat]

theorem map_cons_eq {f : Nat → Nat} {a v : Nat} {l vs : List Nat}
    (h1 : f a = v) (h2 : l.map f = vs) : (a :: l).map f = v :: vs := by
  subst h1; subst h2; rfl

/-! ### The step list as a literal, and its first block -/

def stepsLit : List Step :=
  [.corner 65, .corner 513, .corner 4097, .corner 32769, .corner 262145, .corner 2097153, .check 0,
   .corner 72, .corner 520, .corner 4104, .corner 32776, .corner 262152, .corner 2097160, .check 1,
   .corner 4160, .corner 32832, .corner 262208, .corner 2097216, .check 2,
   .corner 4608, .corner 33280, .corner 262656, .corner 2097664, .check 3,
   .corner 266240, .corner 2101248, .check 4,
   .corner 294912, .corner 2129920, .check 5, .check 6, .check 7]
theorem steps_eq : steps 8 = stepsLit := by decide

/-- The six corners at node 0 (to nodes 2..7). -/
def first6 : List Nat := [65, 513, 4097, 32769, 262145, 2097153]
def restLit : List Step := stepsLit.drop 6
theorem stepsLit_split : stepsLit = first6.map Step.corner ++ restLit := by decide

/-- Degree vector of the pattern `m` at node 0: bit `t` of `m` is the corner to node `t + 2`. -/
def node0Const : Nat → Nat → Nat
  | 0, _ => 0
  | t + 1, m => (if (m / 2 ^ t) % 2 = 1 then 8 ^ 0 + 8 ^ (t + 2) else 0) + node0Const t m

def starts : List Nat :=
  [0, 65, 513, 578, 4097, 4162, 4610, 4675, 32769, 32834, 33282, 33347, 36866, 36931, 37379, 37444, 262145, 262210, 262658, 262723, 266242, 266307, 266755, 266820, 294914, 294979, 295427, 295492, 299011, 299076, 299524, 299589, 2097153, 2097218, 2097666, 2097731, 2101250, 2101315, 2101763, 2101828, 2129922, 2129987, 2130435, 2130500, 2134019, 2134084, 2134532, 2134597, 2359298, 2359363, 2359811, 2359876, 2363395, 2363460, 2363908, 2363973, 2392067, 2392132, 2392580, 2392645, 2396164, 2396229, 2396677, 2396742]
theorem starts_eq : expand first6 [0] = starts := by decide
theorem starts_eq_masks : starts = (List.range 64).map (node0Const 6) := by decide

/-- Leaf for the histogram: the product of `w` over the nodes other than node 0. -/
def histLeaf (d : Nat) : Nat := wt 7 (d / 8)

/-! ### The 3 x 64 pieces, each its own kernel evaluation (generated) -/

theorem slot_0 : prunedS (wt 8) restLit 0 = 50920 := by decide +kernel
theorem slot_1 : prunedS (wt 8) restLit 65 = 0 := by decide +kernel
theorem slot_2 : prunedS (wt 8) restLit 513 = 0 := by decide +kernel
theorem slot_3 : prunedS (wt 8) restLit 578 = 114551 := by decide +kernel
theorem slot_4 : prunedS (wt 8) restLit 4097 = 0 := by decide +kernel
theorem slot_5 : prunedS (wt 8) restLit 4162 = 115144 := by decide +kernel
theorem slot_6 : prunedS (wt 8) restLit 4610 = 115144 := by decide +kernel
theorem slot_7 : prunedS (wt 8) restLit 4675 = 0 := by decide +kernel
theorem slot_8 : prunedS (wt 8) restLit 32769 = 0 := by decide +kernel
theorem slot_9 : prunedS (wt 8) restLit 32834 = 115144 := by decide +kernel
theorem slot_10 : prunedS (wt 8) restLit 33282 = 115144 := by decide +kernel
theorem slot_11 : prunedS (wt 8) restLit 33347 = 0 := by decide +kernel
theorem slot_12 : prunedS (wt 8) restLit 36866 = 114551 := by decide +kernel
theorem slot_13 : prunedS (wt 8) restLit 36931 = 0 := by decide +kernel
theorem slot_14 : prunedS (wt 8) restLit 37379 = 0 := by decide +kernel
theorem slot_15 : prunedS (wt 8) restLit 37444 = 525956 := by decide +kernel
theorem slot_16 : prunedS (wt 8) restLit 262145 = 0 := by decide +kernel
theorem slot_17 : prunedS (wt 8) restLit 262210 = 115144 := by decide +kernel
theorem slot_18 : prunedS (wt 8) restLit 262658 = 115144 := by decide +kernel
theorem slot_19 : prunedS (wt 8) restLit 262723 = 0 := by decide +kernel
theorem slot_20 : prunedS (wt 8) restLit 266242 = 115144 := by decide +kernel
theorem slot_21 : prunedS (wt 8) restLit 266307 = 0 := by decide +kernel
theorem slot_22 : prunedS (wt 8) restLit 266755 = 0 := by decide +kernel
theorem slot_23 : prunedS (wt 8) restLit 266820 = 531610 := by decide +kernel
theorem slot_24 : prunedS (wt 8) restLit 294914 = 115144 := by decide +kernel
theorem slot_25 : prunedS (wt 8) restLit 294979 = 0 := by decide +kernel
theorem slot_26 : prunedS (wt 8) restLit 295427 = 0 := by decide +kernel
theorem slot_27 : prunedS (wt 8) restLit 295492 = 531610 := by decide +kernel
theorem slot_28 : prunedS (wt 8) restLit 299011 = 0 := by decide +kernel
theorem slot_29 : prunedS (wt 8) restLit 299076 = 531610 := by decide +kernel
theorem slot_30 : prunedS (wt 8) restLit 299524 = 531610 := by decide +kernel
theorem slot_31 : prunedS (wt 8) restLit 299589 = 0 := by decide +kernel
theorem slot_32 : prunedS (wt 8) restLit 2097153 = 0 := by decide +kernel
theorem slot_33 : prunedS (wt 8) restLit 2097218 = 115144 := by decide +kernel
theorem slot_34 : prunedS (wt 8) restLit 2097666 = 115144 := by decide +kernel
theorem slot_35 : prunedS (wt 8) restLit 2097731 = 0 := by decide +kernel
theorem slot_36 : prunedS (wt 8) restLit 2101250 = 115144 := by decide +kernel
theorem slot_37 : prunedS (wt 8) restLit 2101315 = 0 := by decide +kernel
theorem slot_38 : prunedS (wt 8) restLit 2101763 = 0 := by decide +kernel
theorem slot_39 : prunedS (wt 8) restLit 2101828 = 531610 := by decide +kernel
theorem slot_40 : prunedS (wt 8) restLit 2129922 = 115144 := by decide +kernel
theorem slot_41 : prunedS (wt 8) restLit 2129987 = 0 := by decide +kernel
theorem slot_42 : prunedS (wt 8) restLit 2130435 = 0 := by decide +kernel
theorem slot_43 : prunedS (wt 8) restLit 2130500 = 531610 := by decide +kernel
theorem slot_44 : prunedS (wt 8) restLit 2134019 = 0 := by decide +kernel
theorem slot_45 : prunedS (wt 8) restLit 2134084 = 531610 := by decide +kernel
theorem slot_46 : prunedS (wt 8) restLit 2134532 = 531610 := by decide +kernel
theorem slot_47 : prunedS (wt 8) restLit 2134597 = 0 := by decide +kernel
theorem slot_48 : prunedS (wt 8) restLit 2359298 = 114551 := by decide +kernel
theorem slot_49 : prunedS (wt 8) restLit 2359363 = 0 := by decide +kernel
theorem slot_50 : prunedS (wt 8) restLit 2359811 = 0 := by decide +kernel
theorem slot_51 : prunedS (wt 8) restLit 2359876 = 525956 := by decide +kernel
theorem slot_52 : prunedS (wt 8) restLit 2363395 = 0 := by decide +kernel
theorem slot_53 : prunedS (wt 8) restLit 2363460 = 531610 := by decide +kernel
theorem slot_54 : prunedS (wt 8) restLit 2363908 = 531610 := by decide +kernel
theorem slot_55 : prunedS (wt 8) restLit 2363973 = 0 := by decide +kernel
theorem slot_56 : prunedS (wt 8) restLit 2392067 = 0 := by decide +kernel
theorem slot_57 : prunedS (wt 8) restLit 2392132 = 531610 := by decide +kernel
theorem slot_58 : prunedS (wt 8) restLit 2392580 = 531610 := by decide +kernel
theorem slot_59 : prunedS (wt 8) restLit 2392645 = 0 := by decide +kernel
theorem slot_60 : prunedS (wt 8) restLit 2396164 = 525956 := by decide +kernel
theorem slot_61 : prunedS (wt 8) restLit 2396229 = 0 := by decide +kernel
theorem slot_62 : prunedS (wt 8) restLit 2396677 = 0 := by decide +kernel
theorem slot_63 : prunedS (wt 8) restLit 2396742 = 3176590 := by decide +kernel

def slotVals : List Nat :=
  [50920, 0, 0, 114551, 0, 115144, 115144, 0, 0, 115144, 115144, 0, 114551, 0, 0, 525956, 0, 115144, 115144, 0, 115144, 0, 0, 531610, 115144, 0, 0, 531610, 0, 531610, 531610, 0, 0, 115144, 115144, 0, 115144, 0, 0, 531610, 115144, 0, 0, 531610, 0, 531610, 531610, 0, 114551, 0, 0, 525956, 0, 531610, 531610, 0, 0, 531610, 531610, 0, 525956, 0, 0, 3176590]
theorem slot_pieces : starts.map (pruned (wt 8) restLit) = slotVals :=
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_0) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_1) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_2) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_3) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_4) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_5) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_6) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_7) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_8) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_9) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_10) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_11) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_12) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_13) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_14) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_15) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_16) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_17) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_18) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_19) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_20) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_21) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_22) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_23) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_24) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_25) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_26) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_27) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_28) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_29) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_30) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_31) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_32) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_33) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_34) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_35) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_36) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_37) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_38) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_39) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_40) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_41) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_42) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_43) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_44) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_45) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_46) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_47) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_48) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_49) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_50) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_51) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_52) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_53) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_54) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_55) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_56) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_57) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_58) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_59) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_60) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_61) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_62) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans slot_63) <|
  rfl

theorem even_0 : prunedS (evenAll 8) restLit 0 = 4096 := by decide +kernel
theorem even_1 : prunedS (evenAll 8) restLit 65 = 0 := by decide +kernel
theorem even_2 : prunedS (evenAll 8) restLit 513 = 0 := by decide +kernel
theorem even_3 : prunedS (evenAll 8) restLit 578 = 4096 := by decide +kernel
theorem even_4 : prunedS (evenAll 8) restLit 4097 = 0 := by decide +kernel
theorem even_5 : prunedS (evenAll 8) restLit 4162 = 4096 := by decide +kernel
theorem even_6 : prunedS (evenAll 8) restLit 4610 = 4096 := by decide +kernel
theorem even_7 : prunedS (evenAll 8) restLit 4675 = 0 := by decide +kernel
theorem even_8 : prunedS (evenAll 8) restLit 32769 = 0 := by decide +kernel
theorem even_9 : prunedS (evenAll 8) restLit 32834 = 4096 := by decide +kernel
theorem even_10 : prunedS (evenAll 8) restLit 33282 = 4096 := by decide +kernel
theorem even_11 : prunedS (evenAll 8) restLit 33347 = 0 := by decide +kernel
theorem even_12 : prunedS (evenAll 8) restLit 36866 = 4096 := by decide +kernel
theorem even_13 : prunedS (evenAll 8) restLit 36931 = 0 := by decide +kernel
theorem even_14 : prunedS (evenAll 8) restLit 37379 = 0 := by decide +kernel
theorem even_15 : prunedS (evenAll 8) restLit 37444 = 4096 := by decide +kernel
theorem even_16 : prunedS (evenAll 8) restLit 262145 = 0 := by decide +kernel
theorem even_17 : prunedS (evenAll 8) restLit 262210 = 4096 := by decide +kernel
theorem even_18 : prunedS (evenAll 8) restLit 262658 = 4096 := by decide +kernel
theorem even_19 : prunedS (evenAll 8) restLit 262723 = 0 := by decide +kernel
theorem even_20 : prunedS (evenAll 8) restLit 266242 = 4096 := by decide +kernel
theorem even_21 : prunedS (evenAll 8) restLit 266307 = 0 := by decide +kernel
theorem even_22 : prunedS (evenAll 8) restLit 266755 = 0 := by decide +kernel
theorem even_23 : prunedS (evenAll 8) restLit 266820 = 4096 := by decide +kernel
theorem even_24 : prunedS (evenAll 8) restLit 294914 = 4096 := by decide +kernel
theorem even_25 : prunedS (evenAll 8) restLit 294979 = 0 := by decide +kernel
theorem even_26 : prunedS (evenAll 8) restLit 295427 = 0 := by decide +kernel
theorem even_27 : prunedS (evenAll 8) restLit 295492 = 4096 := by decide +kernel
theorem even_28 : prunedS (evenAll 8) restLit 299011 = 0 := by decide +kernel
theorem even_29 : prunedS (evenAll 8) restLit 299076 = 4096 := by decide +kernel
theorem even_30 : prunedS (evenAll 8) restLit 299524 = 4096 := by decide +kernel
theorem even_31 : prunedS (evenAll 8) restLit 299589 = 0 := by decide +kernel
theorem even_32 : prunedS (evenAll 8) restLit 2097153 = 0 := by decide +kernel
theorem even_33 : prunedS (evenAll 8) restLit 2097218 = 4096 := by decide +kernel
theorem even_34 : prunedS (evenAll 8) restLit 2097666 = 4096 := by decide +kernel
theorem even_35 : prunedS (evenAll 8) restLit 2097731 = 0 := by decide +kernel
theorem even_36 : prunedS (evenAll 8) restLit 2101250 = 4096 := by decide +kernel
theorem even_37 : prunedS (evenAll 8) restLit 2101315 = 0 := by decide +kernel
theorem even_38 : prunedS (evenAll 8) restLit 2101763 = 0 := by decide +kernel
theorem even_39 : prunedS (evenAll 8) restLit 2101828 = 4096 := by decide +kernel
theorem even_40 : prunedS (evenAll 8) restLit 2129922 = 4096 := by decide +kernel
theorem even_41 : prunedS (evenAll 8) restLit 2129987 = 0 := by decide +kernel
theorem even_42 : prunedS (evenAll 8) restLit 2130435 = 0 := by decide +kernel
theorem even_43 : prunedS (evenAll 8) restLit 2130500 = 4096 := by decide +kernel
theorem even_44 : prunedS (evenAll 8) restLit 2134019 = 0 := by decide +kernel
theorem even_45 : prunedS (evenAll 8) restLit 2134084 = 4096 := by decide +kernel
theorem even_46 : prunedS (evenAll 8) restLit 2134532 = 4096 := by decide +kernel
theorem even_47 : prunedS (evenAll 8) restLit 2134597 = 0 := by decide +kernel
theorem even_48 : prunedS (evenAll 8) restLit 2359298 = 4096 := by decide +kernel
theorem even_49 : prunedS (evenAll 8) restLit 2359363 = 0 := by decide +kernel
theorem even_50 : prunedS (evenAll 8) restLit 2359811 = 0 := by decide +kernel
theorem even_51 : prunedS (evenAll 8) restLit 2359876 = 4096 := by decide +kernel
theorem even_52 : prunedS (evenAll 8) restLit 2363395 = 0 := by decide +kernel
theorem even_53 : prunedS (evenAll 8) restLit 2363460 = 4096 := by decide +kernel
theorem even_54 : prunedS (evenAll 8) restLit 2363908 = 4096 := by decide +kernel
theorem even_55 : prunedS (evenAll 8) restLit 2363973 = 0 := by decide +kernel
theorem even_56 : prunedS (evenAll 8) restLit 2392067 = 0 := by decide +kernel
theorem even_57 : prunedS (evenAll 8) restLit 2392132 = 4096 := by decide +kernel
theorem even_58 : prunedS (evenAll 8) restLit 2392580 = 4096 := by decide +kernel
theorem even_59 : prunedS (evenAll 8) restLit 2392645 = 0 := by decide +kernel
theorem even_60 : prunedS (evenAll 8) restLit 2396164 = 4096 := by decide +kernel
theorem even_61 : prunedS (evenAll 8) restLit 2396229 = 0 := by decide +kernel
theorem even_62 : prunedS (evenAll 8) restLit 2396677 = 0 := by decide +kernel
theorem even_63 : prunedS (evenAll 8) restLit 2396742 = 4096 := by decide +kernel

def evenVals : List Nat :=
  [4096, 0, 0, 4096, 0, 4096, 4096, 0, 0, 4096, 4096, 0, 4096, 0, 0, 4096, 0, 4096, 4096, 0, 4096, 0, 0, 4096, 4096, 0, 0, 4096, 0, 4096, 4096, 0, 0, 4096, 4096, 0, 4096, 0, 0, 4096, 4096, 0, 0, 4096, 0, 4096, 4096, 0, 4096, 0, 0, 4096, 0, 4096, 4096, 0, 0, 4096, 4096, 0, 4096, 0, 0, 4096]
theorem even_pieces : starts.map (pruned (evenAll 8) restLit) = evenVals :=
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_0) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_1) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_2) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_3) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_4) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_5) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_6) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_7) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_8) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_9) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_10) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_11) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_12) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_13) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_14) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_15) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_16) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_17) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_18) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_19) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_20) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_21) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_22) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_23) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_24) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_25) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_26) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_27) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_28) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_29) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_30) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_31) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_32) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_33) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_34) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_35) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_36) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_37) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_38) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_39) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_40) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_41) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_42) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_43) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_44) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_45) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_46) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_47) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_48) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_49) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_50) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_51) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_52) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_53) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_54) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_55) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_56) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_57) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_58) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_59) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_60) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_61) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_62) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans even_63) <|
  rfl

theorem hist_0 : prunedS histLeaf restLit 0 = 50920 := by decide +kernel
theorem hist_1 : prunedS histLeaf restLit 65 = 0 := by decide +kernel
theorem hist_2 : prunedS histLeaf restLit 513 = 0 := by decide +kernel
theorem hist_3 : prunedS histLeaf restLit 578 = 114551 := by decide +kernel
theorem hist_4 : prunedS histLeaf restLit 4097 = 0 := by decide +kernel
theorem hist_5 : prunedS histLeaf restLit 4162 = 115144 := by decide +kernel
theorem hist_6 : prunedS histLeaf restLit 4610 = 115144 := by decide +kernel
theorem hist_7 : prunedS histLeaf restLit 4675 = 0 := by decide +kernel
theorem hist_8 : prunedS histLeaf restLit 32769 = 0 := by decide +kernel
theorem hist_9 : prunedS histLeaf restLit 32834 = 115144 := by decide +kernel
theorem hist_10 : prunedS histLeaf restLit 33282 = 115144 := by decide +kernel
theorem hist_11 : prunedS histLeaf restLit 33347 = 0 := by decide +kernel
theorem hist_12 : prunedS histLeaf restLit 36866 = 114551 := by decide +kernel
theorem hist_13 : prunedS histLeaf restLit 36931 = 0 := by decide +kernel
theorem hist_14 : prunedS histLeaf restLit 37379 = 0 := by decide +kernel
theorem hist_15 : prunedS histLeaf restLit 37444 = 262978 := by decide +kernel
theorem hist_16 : prunedS histLeaf restLit 262145 = 0 := by decide +kernel
theorem hist_17 : prunedS histLeaf restLit 262210 = 115144 := by decide +kernel
theorem hist_18 : prunedS histLeaf restLit 262658 = 115144 := by decide +kernel
theorem hist_19 : prunedS histLeaf restLit 262723 = 0 := by decide +kernel
theorem hist_20 : prunedS histLeaf restLit 266242 = 115144 := by decide +kernel
theorem hist_21 : prunedS histLeaf restLit 266307 = 0 := by decide +kernel
theorem hist_22 : prunedS histLeaf restLit 266755 = 0 := by decide +kernel
theorem hist_23 : prunedS histLeaf restLit 266820 = 265805 := by decide +kernel
theorem hist_24 : prunedS histLeaf restLit 294914 = 115144 := by decide +kernel
theorem hist_25 : prunedS histLeaf restLit 294979 = 0 := by decide +kernel
theorem hist_26 : prunedS histLeaf restLit 295427 = 0 := by decide +kernel
theorem hist_27 : prunedS histLeaf restLit 295492 = 265805 := by decide +kernel
theorem hist_28 : prunedS histLeaf restLit 299011 = 0 := by decide +kernel
theorem hist_29 : prunedS histLeaf restLit 299076 = 265805 := by decide +kernel
theorem hist_30 : prunedS histLeaf restLit 299524 = 265805 := by decide +kernel
theorem hist_31 : prunedS histLeaf restLit 299589 = 0 := by decide +kernel
theorem hist_32 : prunedS histLeaf restLit 2097153 = 0 := by decide +kernel
theorem hist_33 : prunedS histLeaf restLit 2097218 = 115144 := by decide +kernel
theorem hist_34 : prunedS histLeaf restLit 2097666 = 115144 := by decide +kernel
theorem hist_35 : prunedS histLeaf restLit 2097731 = 0 := by decide +kernel
theorem hist_36 : prunedS histLeaf restLit 2101250 = 115144 := by decide +kernel
theorem hist_37 : prunedS histLeaf restLit 2101315 = 0 := by decide +kernel
theorem hist_38 : prunedS histLeaf restLit 2101763 = 0 := by decide +kernel
theorem hist_39 : prunedS histLeaf restLit 2101828 = 265805 := by decide +kernel
theorem hist_40 : prunedS histLeaf restLit 2129922 = 115144 := by decide +kernel
theorem hist_41 : prunedS histLeaf restLit 2129987 = 0 := by decide +kernel
theorem hist_42 : prunedS histLeaf restLit 2130435 = 0 := by decide +kernel
theorem hist_43 : prunedS histLeaf restLit 2130500 = 265805 := by decide +kernel
theorem hist_44 : prunedS histLeaf restLit 2134019 = 0 := by decide +kernel
theorem hist_45 : prunedS histLeaf restLit 2134084 = 265805 := by decide +kernel
theorem hist_46 : prunedS histLeaf restLit 2134532 = 265805 := by decide +kernel
theorem hist_47 : prunedS histLeaf restLit 2134597 = 0 := by decide +kernel
theorem hist_48 : prunedS histLeaf restLit 2359298 = 114551 := by decide +kernel
theorem hist_49 : prunedS histLeaf restLit 2359363 = 0 := by decide +kernel
theorem hist_50 : prunedS histLeaf restLit 2359811 = 0 := by decide +kernel
theorem hist_51 : prunedS histLeaf restLit 2359876 = 262978 := by decide +kernel
theorem hist_52 : prunedS histLeaf restLit 2363395 = 0 := by decide +kernel
theorem hist_53 : prunedS histLeaf restLit 2363460 = 265805 := by decide +kernel
theorem hist_54 : prunedS histLeaf restLit 2363908 = 265805 := by decide +kernel
theorem hist_55 : prunedS histLeaf restLit 2363973 = 0 := by decide +kernel
theorem hist_56 : prunedS histLeaf restLit 2392067 = 0 := by decide +kernel
theorem hist_57 : prunedS histLeaf restLit 2392132 = 265805 := by decide +kernel
theorem hist_58 : prunedS histLeaf restLit 2392580 = 265805 := by decide +kernel
theorem hist_59 : prunedS histLeaf restLit 2392645 = 0 := by decide +kernel
theorem hist_60 : prunedS histLeaf restLit 2396164 = 262978 := by decide +kernel
theorem hist_61 : prunedS histLeaf restLit 2396229 = 0 := by decide +kernel
theorem hist_62 : prunedS histLeaf restLit 2396677 = 0 := by decide +kernel
theorem hist_63 : prunedS histLeaf restLit 2396742 = 635318 := by decide +kernel

def histVals : List Nat :=
  [50920, 0, 0, 114551, 0, 115144, 115144, 0, 0, 115144, 115144, 0, 114551, 0, 0, 262978, 0, 115144, 115144, 0, 115144, 0, 0, 265805, 115144, 0, 0, 265805, 0, 265805, 265805, 0, 0, 115144, 115144, 0, 115144, 0, 0, 265805, 115144, 0, 0, 265805, 0, 265805, 265805, 0, 114551, 0, 0, 262978, 0, 265805, 265805, 0, 0, 265805, 265805, 0, 262978, 0, 0, 635318]
theorem hist_pieces : starts.map (pruned histLeaf restLit) = histVals :=
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_0) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_1) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_2) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_3) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_4) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_5) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_6) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_7) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_8) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_9) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_10) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_11) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_12) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_13) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_14) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_15) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_16) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_17) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_18) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_19) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_20) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_21) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_22) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_23) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_24) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_25) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_26) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_27) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_28) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_29) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_30) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_31) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_32) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_33) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_34) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_35) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_36) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_37) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_38) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_39) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_40) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_41) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_42) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_43) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_44) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_45) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_46) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_47) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_48) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_49) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_50) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_51) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_52) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_53) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_54) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_55) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_56) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_57) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_58) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_59) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_60) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_61) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_62) <|
  map_cons_eq ((prunedS_eq _ _ _).symm.trans hist_63) <|
  rfl

/-! ### Totals -/

theorem split0 (leaf : Nat → Nat) (rest : List Step) (cs : List Nat) :
    pruned leaf (cs.map Step.corner ++ rest) 0 = ((expand cs [0]).map (pruned leaf rest)).sum := by
  have h := split leaf rest cs [0]
  have e : ([0].map (pruned leaf (cs.map Step.corner ++ rest))).sum
      = pruned leaf (cs.map Step.corner ++ rest) 0 + 0 := rfl
  omega

theorem total_of_pieces (leaf : Nat → Nat) (vals : List Nat)
    (h : starts.map (pruned leaf restLit) = vals) : pruned leaf (steps 8) 0 = vals.sum :=
  calc pruned leaf (steps 8) 0
      = pruned leaf (first6.map Step.corner ++ restLit) 0 := by rw [steps_eq, stepsLit_split]
    _ = ((expand first6 [0]).map (pruned leaf restLit)).sum := split0 leaf restLit first6
    _ = (starts.map (pruned leaf restLit)).sum := by rw [starts_eq]
    _ = vals.sum := by rw [h]

/-- Number of even subgraphs of K_{2,2,2,2}: `2^(24-8+1)`. -/
theorem even_subgraphs : pruned (evenAll 8) (steps 8) 0 = 131072 := by
  rw [total_of_pieces _ _ even_pieces]; decide
/-- The structurally admissible slots of the half-spin site tensor (row 1418). -/
theorem slots : pruned (wt 8) (steps 8) 0 = 12910079 := by
  rw [total_of_pieces _ _ slot_pieces]; decide
theorem slot_bytes : 12910079 * 32 = 413122528 := by decide

/-! ### Histogram by the pattern at node 0 (row 1418; check 1420) -/

/-- Are the two nodes of a two-bit mask antipodal? -/
def sameAxisPair (m : Nat) : Bool := m == 3 || m == 12 || m == 48

def expected (m : Nat) : Nat :=
  match popc 6 m with
  | 0 => 50920
  | 2 => if sameAxisPair m then 114551 else 115144
  | 4 => if sameAxisPair (63 - m) then 262978 else 265805
  | 6 => 635318
  | _ => 0

/-- For every pattern `m` at node 0: the sum over even subgraphs with that pattern of the
product of `w` over the other seven nodes. -/
theorem histogram :
    ((List.range 64).map (node0Const 6)).map (pruned histLeaf restLit) = (List.range 64).map expected := by
  rw [← starts_eq_masks, hist_pieces]; decide

/-- Number of fixed-leg labels in each of the six classes. -/
def classLabels (v : Nat) : Nat :=
  ((List.range 64).map fun m => if expected m = v then w (popc 6 m) else 0).sum

theorem histogram_labels :
    [50920, 114551, 115144, 262978, 265805, 635318].map classLabels = [1, 3, 12, 6, 24, 5] := by
  decide +kernel
theorem first_moment :
    ((List.range 64).map fun m => w (popc 6 m) * expected m).sum = 12910079 := by decide +kernel
theorem second_moment :
    ((List.range 64).map fun m => w (popc 6 m) * expected m * expected m).sum = 4329800859159 := by
  decide +kernel

end Step1

#print axioms Step1.singlet_table
#print axioms Step1.w_is_singlet
#print axioms Step1.link_counts
#print axioms Step1.link_total_by_occupancy
#print axioms Step1.link_total_by_patterns
#print axioms Step1.div_mul_sanity
#print axioms Step1.D_one
#print axioms Step1.D_two
#print axioms Step1.corners_card
#print axioms Step1.corners_degree_six
#print axioms Step1.prunedS_eq
#print axioms Step1.octahedron_even
#print axioms Step1.octahedron_even_pruned
#print axioms Step1.octahedron_slots_agree
#print axioms Step1.split
#print axioms Step1.steps_eq
#print axioms Step1.stepsLit_split
#print axioms Step1.starts_eq
#print axioms Step1.starts_eq_masks
#print axioms Step1.slot_pieces
#print axioms Step1.even_pieces
#print axioms Step1.hist_pieces
#print axioms Step1.split0
#print axioms Step1.total_of_pieces
#print axioms Step1.even_subgraphs
#print axioms Step1.slots
#print axioms Step1.slot_bytes
#print axioms Step1.histogram
#print axioms Step1.histogram_labels
#print axioms Step1.first_moment
#print axioms Step1.second_moment
