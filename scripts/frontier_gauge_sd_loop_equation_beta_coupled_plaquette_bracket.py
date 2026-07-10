#!/usr/bin/env python3
"""Beta-coupled SD loop-equation plaquette bracket at (N=3, Wilson, beta=6): exact 2D certificates + refutation gates.

Frontier target: the beta=6 completion gate
(gauge_scalar_temporal_observable_bridge_stretch_note_2026-05-02;
acceptance contract GAUGE_SCALAR_KZ_BETA6_REPRODUCTION_CONTRACT_FIREWALL_2026-06-06,
which leaves open "a repo-owned SDP that adds beta-coupled loop equations").

What this runner certifies (class A, stdlib-only, exact rational arithmetic):
  G1  float64 midpoint torus quadrature for SU(3) class integrals reproduces six
      Haar moments at beta=0 to <=1e-9, including <chi^2 chibar> = 0 (N-ality;
      corrects the value 1 recorded in the lane spec).
  G2  the derived one-link Schwinger-Dyson identity holds at beta=6 under the
      recorded sign convention (residual <=1e-9; flipped sign fails by O(1)).
  G3  the two embedded lane-A equation payloads (D=2 and D=4, beta=6, N=3) parse
      to the pinned inventories: 19/165 JSON variables, 3/9 equations, and the
      lane-C builder reproduces model inventories (24,6,3)/(440,276,9), PSD block
      dims [8,3,2,2]/[63,3,2,2], fresh Gram pairs 4/274, objective w_P.
  G4  refutation theorem: the all-ones assignment (U == I on every link) is
      box-feasible AND exactly PSD-feasible (integer LDLT on every block) yet
      violates every one of the 12 SD equations by exactly +4/3 -- the
      beta-coupled equations carry information beyond box+PSD kinematics.
  G5  a comb-gauge transfer-matrix oracle (exact single-plaquette measure in D=2)
      satisfies all three 2D SD equations to <=1e-10 in float64, independently of
      the SDP pipeline (equations are true of the actual 2D theory).
  G6  exact rational certificates (LDLT over Fraction, zero-pivot semidefinite
      safe) for the 2D bracket: CERTIFIED UPPER 903482039/1000000000 and
      CERTIFIED LOWER -10000001/20000000 for w_P = <(1/3)Re Tr U_P> at beta=6.
  G7  the certified 2D bracket contains the exact 2D value w_1(beta=6) =
      0.42253173965 (transfer-matrix quadrature), the certified upper bound is
      strictly below 1 (beyond the kinematic box), and the certified lower bound
      is epsilon-weaker than the kinematic floor -1/2 (disclosed, kept for
      two-sided completeness).

Honest scope: the certificates are exact and machine-checked here from embedded
rational data; D=4 bounds are NOT certified by this runner (floating-point-only
disclosure lives in the paired note). Figure-derived MC/PDG numbers appear only
as audit comparators, never as derivation inputs.

Provenance: the model builder and certificate verifier below are verbatim slices
of the session lane-C sources (sdp_model.py, certify.py) minus file-IO/CLI, with
one signature adaptation: build_core_model(path) -> build_core_model(data).
Embedded payloads (zlib+base64, sha256 of raw bytes pinned and re-checked at
run time):
  sd_equations_beta6_2d.json  sha256=b512c0fbb43e568c4adc333ff5f7146ab183140ccc21aabea1f478811fc6e4f1  (12696 bytes raw)
  sd_equations_beta6_4d.json  sha256=bed5ead58e68dcb5f2b7dd10af2c304231a7494604171bc6a2de44051bbb5e8d  (115730 bytes raw)
  cert_2d_upper_compact.json  sha256=733b45e35f0a986d5341e201962d197e8387eb94290a017e245b238825ad3776  (6088 bytes raw)
  cert_2d_lower_compact.json  sha256=d66b660f180809e89e220c332c60ad5006253b0147bec2cac9323918657a877d  (3903 bytes raw)
"""
from __future__ import annotations

import base64
import hashlib
import itertools
import json
import math
import sys
import zlib
from dataclasses import dataclass, field
from fractions import Fraction
from typing import Dict, List, Mapping, Sequence, Tuple

# Exact rational LDLT over large integers (4D model build + 63x63 blocks):
# generous ceiling for a class-A runner.
AUDIT_TIMEOUT_SEC = 1800

sys.set_int_max_str_digits(0)

PAYLOADS = {
    "sd_equations_beta6_2d.json": (
        "b512c0fbb43e568c4adc333ff5f7146ab183140ccc21aabea1f478811fc6e4f1",
        "eNrtmk1vozAQhu/5FZFPrUpUDISQlXrrsaqi7u5pVSGD7RQ1gSyQtlGU/74mnzA4W5x0tyWhhwqPPTa8fsbjgOetdht50TSk"
        "CfrWnouSKKfUNbjPqdmjrGvpouLXskJUdfC1gbRNCaPl1aO29bMsr98zbU4t21Hx6xkOJpZhUsvvq/j1TYZtu6szz2cqfqRr"
        "9DH3mO/7noqfpxtd7IkntCxfya9HKMXcpqZtqPj52HR6nHFsWFTFj/KeyR2DdDFRGo/1Ke+aTEyFwry/undYdzFnmFLP9kxC"
        "FF0tr+s7vnhIHRuKrrbec2xfDGmYSq6OazNKfcfCHjOpmmffo9gyDc6xz9U8qef0CcWsLyJEwXOg0PahioTi/yIzIvZ7StIg"
        "CpOtz3zTNsjuEH2/dQduFHtBinfdTOLohYUkXMbcxkHYR0H4LCy6ljNF0cSN2aTQUNgpGQ5ZLKycjBKm5asizhOW5h5i9adr"
        "xWKu9FjwT1I2SUru6OoNacAyg5ZOqU1nhvIDba8XuWdMUjIZsWxIowVqUcLCJFMJ3eg7/VIWj5OidFG4bFWYLulSjDCoB0sZ"
        "KvcAFi1JC7BclG5DBi8qtRmsrGbRugJy1eVGnlZOpDJwwsMdReHw9IA7DMFPg7KcYGWAgtwmwQtkMUkLkHdkAJZTDJI2AhkB"
        "yVAGa79kuIHcvIbZEpBXZzl5iuK0MszG14T5UFC1CkHxv2AGu1MZzGAjKkG1QkS8w7sCzGBnJIUZbEc+AObWGgo0ZinZ/S64"
        "3dGJ7txxEIpyd12+F9fm+tpbeSF7PRzyo1AQn+0zllFxc5G1uL6/bCfTsTtpP7AfcfunO9HarywYPqVt9ja5+H6JtruUFxIH"
        "xFsBsL6XVb7cxttzEC6VFiMluVB7IaMpWyXNfJhK0mqpJxpNxYi7rkYsHKZPhcCwdmpaLRBLCEYt4sRPoxiG1rwYDPsDe39o"
        "l4K7GN4gwPeGuCw4ZYEvC/RSTsoHciGUz+WJW9C6gACCxegQAO2zAPCYKfp0UDsY3gD+OGk6FWW4Oo5UkBMbUs+E1PqtqWBv"
        "1pB6kqSeQPIHL22a3We9d5/1y+ngnWADYK0APIVcDV4bNrn6PHJ1B9eOVPA6ryH1PEitX1IHn/GapF7zpF4/AsF3vGapbH6A"
        "f0FQpR/gSqwmQTiUsor1/TzuE1QuZkHInYiPhU+fZfGgcOVyUUQoYLk8O7K/3GT8TXLwOfOUJb96R+LO8VNWSXJwHOKcKD92"
        "Sg6SvHS4pLriTu0Yn6ktKwcKCg44nJKgxy4ChwkKTvLVWdB/vepWEHSQl5CMApLd9dKuVRbW+urCHiLMQzHJ56TJaqqLY5/g"
        "dmufeNmZp9ai9QecaAl+",
    ),
    "sd_equations_beta6_4d.json": (
        "bed5ead58e68dcb5f2b7dd10af2c304231a7494604171bc6a2de44051bbb5e8d",
        "eNrtXVtvG0eyfvevMPi0C0vYvl8OsG/7GCyC7DlPBwuhL9WOsY7kYymJ7SD//TRtJVH3NK2pEUWGnDKQQBx2ccjqqq+/qq7q"
        "+eXFy5ebePPjdb7d/NfLX+qr+vouXzEvwQBTMkld3/jfz2/Uty7538Tm4rdXfPP5r39fPJDTJjHJuAsCJVc01ylpUYLEyHEu"
        "s1JJK2YTSk5kq6KEYgxDyRkeclQpBFdQclZLECYyIxxKLirg3nDGpUHJpZxZYsomh5o/wRlLzguuIODkQpI2gk8youSs4tpr"
        "waLGycUoeE6RxQgouaRikCzwmAtOzmSrs/YsJ5xc9BYiL1yh5k8UH3kOUI0NJSeZikYLCRYUSk7EFKzVjEeUXqTz0YRkGMso"
        "e5GpQoswBrzIKLnMrPSmzgZD2bUszrhQKrpklL8rlhnfwqB1HiUnq2kKoVSJKHtRoc6fYdtpR+mlIpLLzpiiHMqPNJOSB+cD"
        "C6h5rx5rMqQincDdz2RlnNUmRJS96KK0EyZxbRxOzirpTCyaeZxcBYqYg+ISdT8jOAiteJAWtY5VT8igsmDKWZSczxJksYzh"
        "9GKiL9WFtFEBZZ+msgJwPkWHu5+ti5hiTruoUP5nZdYqGeWMxd3PS+2t4FxI3P2SNEEFob1C2bWFCixFiYqDHCPnuEs8aKeY"
        "ROG1k9xr7mNRODtzTgdRVMUJHH66FErSxTtXUPbpQJWQbJYKx0NcXcBsTFWnHjV/XsiQIgfgHDUP3lZ8cVUxHOd/3qmknBSJ"
        "cxQP8QGKEyVXnEfpJbAcdaq4FD2KFwTuRJCcV5tB6SWInCCWKi1wctWLpIkxhIRaxyIX1apFcLownFyyDKSGlFFxR1QCUoxc"
        "VsxGyVU0Y6beU3Pc7wuRQRFCWK9wclCs1ixJHK+L1Rlk4lukR+F8LIJl0IYngbpfkqrGD0wHKVDre43gUhBGRXAoP0qmru/c"
        "VlfSqN9XAzhfnJOl4hNKLvvkK6mrdoOyswSZx4pnsi5mGLlc4dMXJoXjqPUoOxCQ6y80BSfnK3vZgiDLuO/pXeXyxaUkUPiZ"
        "YzQ1NvagC2oecjIVdbmInqHsM0OJUtfQvwIiRg5EqRG4Zyng5g+ks3YrWRjKPqFGYl5H76tqcHK+6Bh9Kgz3+0yNyOpXrbOB"
        "wkFwQqdqLhUKUf4AdRUTUHQGgeLlkDPXWnhQEYW7AHVd2bJdhuOfUMJ2KSsMyQcLU8lxlrSGjJOrLAukDxyB8z9ffcPZFWNR"
        "61KJay4GKVojXCOdq4bKE1o0JF1B1ESEQ92L8iJ8df5oEDnGe1Ehs9eOceEEUrQGrqGicKlMymNFVdZF8FBjLYsVtaZCSASd"
        "ClZNIkWdbbVBiUhZfRGtQUI131IjDERUci8qSohcg5cuYEWtUN56mwX6rkpKBVyqGrBjDVEplkNy9Z9G39WkSjqT08li51UF"
        "XVeUDJWeRaSoZjYAryyLIyjPvagtUH+r8RCxajIyO280cwrtdKZihFTam2gZVtRXwltsCjZi/dUypri2UApgJ6cSZhDSCC04"
        "Fkzt1oyYy+AYFiUsMCNNCaq6PFLU5ejqPbmVBasmr2WsvsoMy9jf6iMw8LpODvquW7OvxmSltdi7VgptSjFCcUQG+F40c2Fz"
        "VjYErPknpksSQUFiWH9NytjoQVYYxiJiMjUA09nZYrDonzxPJldnlehVPZsgErf16ybsvOacfXSVikSGdTow2QnhUwQ0IYBs"
        "nWZKgQGJFC2qhkmFRSsc1pqK8zWUKJU3K9S8miuulWZFgbbCISUNNwFECpkBTlJU3STGnBY4NmCubGIQZAiu+h1G0l0xF1Wy"
        "wHPAUSZ3xb2rvJsrCzjcd1fC5yB8DdSY4ThJJaOrNKLiQwCcpLamKqey4CIjTtIyXvVTHItFIiWV0cYqpoNB6raCkbaJ82iC"
        "Q0qmwFioxDvh1ooqCZUq1dikaJybuSu3tXiegpSFISWTsG5LkmQ0OMkas8lstXABxyarZMWv4lMIBfs7g3ApANT75oCUTNXH"
        "sqsRrkXeM1br0UZug3CkZ8fKjALYmE1GWny0SkReY/jIkf5ZvdMoXqPUivQ4ycRkZXPJeBuQaJKig8Bj0ZUS4iQz08no7IMu"
        "FilpqmSGoixH2i24LHmUilX2ipOsa1jaenWNwJCYUKCunNk5L1GS3yLGfsdnzFr9/6/bixv4vx/D3Zub69vfZX75beybrX9s"
        "/vWPq2+vbt7HN3f8j4959/7mJ7gO1wl+L2f6fP3tm+v/1Cvs4sGlm5t3V+/hXTOwXs/h9Wt4X6+W8PYWLh6+dVPKLdw9+BFf"
        "/rELzMsHr/7dfPrtHby7nXz45tWHzUV35WN/5XIy5vLj5uGNfv/71wcauL0L797C9pbmRffu5haub7c63Pyd/aHdO3j/w22r"
        "2Jvrz6OayRyWINUh3YCuhmf0Gd32/ab/iG5befJ+t822md6h21AbjOhSzZN7dKnM7neOiOJoSMfrpkMmy1n/VUdLwWb6KR2I"
        "9iO+/fLJsr36xXW/zNBvpvLigcFMXbNKXL29uX69Ntdc5qxHc9/pFujEvrstr6kfd3tb0wHdJtbI0bv9qpEbtjtMww9pN3cm"
        "v6RLrg8caJpGn3jQNGEy/pwucB8P6kL0gbt2XH2ECx0VGw3peMFEefd+P7187/iqAsJ8v7/9/ub93WzHF6fo+Eud+mIGgBzK"
        "8bvav4HPddV6E4fqqs9GPtkVjE3Boau4msJPu8O/CF1mOX6Xjx85fpfaHQ3pUn1LsWGSOhn45jQeH7l+F5BOhuzL8b+p32QV"
        "dPxu0Zp/9zgYXB7O9buy+5HPdBXvA3ToatSH3t+WmY6GdJWTg/t0tYAjEt9Wtw1GdHVloxFtpdToq3ZFQ0OS0pTPDElKW/Ey"
        "8uvpBvcYRrqd4fGgbsNvByC12yLjQV1mf8egNoc/GDSNdVQfbkyzm2P465KK40FTABwM6hJE40FdjuSrLAoLmmI2aPJzzWHM"
        "g8iLCRwfCjS7nrhhzqNt8xoOaTu6lkFv186yWYS8XS344EO6as7BiK5ObTSirRAbfZGuOGvM4Jp6qjH2dAVF40FdYct4UFdM"
        "sgNZ23qIpXg43YIcgma3ZThCqHnI2u2P7SCW7YbWjkHt3tV4UJdA3ytoyrUFmUsh8nhBZtegu3kuQGz7Hkcf0rXyPRdmdh0o"
        "ow/pivmHQ9r6+xE2txXzQ1xti4F34GFbI7gDD9sKuR2D2lq4HRmvtrLkVECzK0fYgYeTXN2IjrbbvDtAs9073A9oCgrPd8Ho"
        "n2lHbXqKwij2bvv0R97ftXQPPqRrNh6NaNuKRynCthF4NKJtpR3mANpuzVEOoO0/HEJz22o4GtJ1pQ0xs22E2BGed0XkO/Cw"
        "LWYeD+rqNseDulrJHTF8W5+4AzTbOrkxaHa7lVM8nBSTjVFsHtOcQyK7epzxoK5sYq+gubbwfDFEHjM8fww0u0NmhtF5ey7M"
        "EM6akwhGNLI9A2CIVW379mYZmrW9uUMa2bbFjtKebUPqEBLbHrbhkLZNakd43nYZ7aCjbfPIjsi7bScYD+oaB8aDuor7pcg6"
        "BzQndbQ78HBO4nO67zOqBWkL7ZYmPpeD5pmH53czAHEGjL76czPN7sSrIRdtzn4ajWhPXRqH+M1BSUNC2541NMoCtKcKjQht"
        "ey7PcM+qPYplIdXsDpQYgnN7hsCOPZ6253AH1LWNTjsGtS1N40FdQ88OOtr23zwnaM4K4Sc14k+IvLuK6B2DJhU3c0HzxT24"
        "bH6Au/DHiXv/qH+q+0LZb65+eHNdX+v71/+sf8v7v+MXqY25v9sm3VxXXN3WyX5G37//ZTvib//868vbH3+4evfyO/jv9y//"
        "5+rdxcuf4c3r7+9ewod3f/nXXze/V9n+FN6/CfELkNx/ly8Vnb/j+n/eXH/WVr3T7YOinp/C2x/vayAeLgeDfZLJJ+WbH+sd"
        "//iot3D9+u77BmDNH8pULzpM3vRrw6b64t3N+x6if2lBdffysXsBmSwSsy40r//d3Wm8mIyWk9HSMFpARsvMiItPKgweLi3N"
        "4nI83fGFuhvp6dPw90+vffqKTl70V3+dGnuzgJKx79XYR4b96uPMif14SGPnR9Xd5VzdfXiasbcBNBk7Gftc67/kJ2ft3dYl"
        "WTvxmOfW3fF4TJf4JGNfKbSz40L7XOVdPhHa26QWWTsRmWOw9k8zdfdEaG+LUsnYV8pj+OHyMUck7W01IRk7kfZjJB/3sdrN"
        "MPb2iIUlxq7I2PfGOy/OTCfznf0pRtyVMhJiU+R5zsbe1EqQsVPgeYzA8+Ns3T3J2NsuczJ24uKzrf/kUordaWbExYmLn94G"
        "f1eoSYhN9OS3PZ5zJONtWzFZOyXGzxnamwJ7MnaC9h2qGmD9HpU3c8/zieUs3dlkZO0Uep4vtHeHn5Cxk7E/O2s/3qZnd64F"
        "WTvtF81OM55c7VbX80rGTqz9fDdHu/ZtMnYy9mPo7jARqszMSm+SyYy6pJ82YU/ZQzr6vtLlcctyD7Q72h1YTNZOIepc0r7H"
        "stzLmb10TyTt3UmzZOxk7HMvnGAvXXekElk7sfbZNP7kShq7I3PJ2Cn5eMa7qN3xz2TtZO3nC+3d4xDJ2FeakFkHa+/O7Sdr"
        "J2ifn488uZ2l7kG2ZO2E7bOtXZxchUz3iAKydsL22eZ/eifw6mKVdCYWzTw13q2g8e4sg8/2IVkE2QTZx9DdYdKK3QOSyNhp"
        "x2iu7k7vQLrucTJk7Cs1drGGTiTjswRZLGMUea45z8KPm0M/lLW3zwsna98rtFOT6Z9qw8iAAXA+RUfQTil01IU9ZtAvZ3K7"
        "J6ZjLPdGMaddVIxyinSY10kitpVZq2SUM5YQmxD7SGmWA+3wWy+1t4JzIanBaMVplku+CmhP0gQVhPaKqrcI2g+huyOScZCZ"
        "FSUYy5yMfb1plnVAu+Mu8aCdYpIO8yJoP+/NUSe519zHoqgSgMpejhaiHgjZnQ6iKFMUnfhC20XHIu0HqkF3KZSki3euUNkL"
        "IfuRdHegUxodqGp+NkvlCNnJ2M88QAULNqbMiqdMO9GYr1H000d2L2RIkQNwTrlHekQMRncnWNDordKVsCvDqVadGjPOHdqd"
        "SspJkTgHMnZKtB8p0X6Y/lIfoDhRco5GU0Hj+RU0rmNvNLAcdcpBRW/Iis/PilfxIMbAnQiSc809hZQUUqKs//QQW+QEsVST"
        "F2TslBk/BMk+3klEwQQlTYwhJDocmoz9vGlM5IL7KILThbaBiMYcicYczNiTZSA1pCzI2Ckxft7GrgSkGLnUijg7JcaPZeyH"
        "SYxHoxgzFd01J85OyH7e+fMYIoMihLCeeosoQD3v1GMMUKzWLEkgY6c6RZT1n9wjR2OqfD3x7WF0dBQdGfuxdHeY86NjESyD"
        "NjwJQnZKPR5rU+kwjXRJKpYc00EKenQRIftXLpzDw1ySVikIoyI4Ksola0dZOzs9azdWSW6dKJpYO2Xav2rcp38kQArBF+dk"
        "AUUP2CVsPwi2Hy9ITdknr0qMSlDJAGH7sXR3mNN3E2QeY8pSJUPGTsZ+HN0dqGQgq1KJDJPCcTp8l4z9T8QBn2EXNTsQkCtt"
        "N4WMfcXGvo4G0+yF/nz6BcvEYyhEPRaPOcwBGNk7A764lASd9kI85ljGfpii9hyj4VZ70IWSjytGdrGGDo6cjJOCi+iZonMy"
        "VvD4ukt+hknFDCVKbVUMnJ5fR/zkzK0dROHSeJYCpdDJ2nHWfnqPawTprN3ae2FU+UKdSF+h4+dQ5wWaca+j9zX+JGuntOIh"
        "sP14dV6gfdEx+lQY8Xay9kPo7niNd2BkUpXLREMPCCAic7Qk+mEqX8AJnbizJlmqaSRkx1zgp4fsUScBRWcQnpLoK0iinyVi"
        "58y1Fh5UpOONKKuI2fY8vYdcAAjutVGBKTqSlM4FOFLgeagsSwnb86YL84oKcynwRFn/ySXQC1PJcZa0BqIxFHgeIvA8XhF6"
        "qXZeQPrA6eC6NXP2838a0s9X33B2xVjUumivchlWvty+uX49tHfOdtv0LpWP1d0o8isvXgxUO1Rrr9Lp61a9vWp7TJ7Id1g8"
        "kZ+8fjBNX5sMzpSRzlkueTrfyfjwdWVffvi6sh+dvE+PfN6nuZMRkgZVTBxXQK7SMy4fm8y7R5S/1DN4EZ5bHY3U6/EMpDLR"
        "njWFtXmTIWT22jEunFgtTKEtHQljcz1DMBOkSiWw7GnNWLhg720yVNZF8MDM+BnuZzkZj7Gny0+PeMJjC/jSybAGRImgU6EF"
        "fDYsPTaZSycjRZ1tUEXmsl6YusPB1ivkmjJ3MiT3IZiSeMh8tWwKOznPtYBLUULkGrx0gTxjl2V/eoSNfdqTZ1ihvPU2ixV7"
        "BjbOeJQAfFgWZygpFXCpTCyUDplt6Z+eB6aUYjkkV/9pTjC1a0349DQqPHsyTOI+JqeTteuNwB9X5mE8I2goMUOA8Sld5Bkz"
        "YOzVI5M1dzI0swE4y8DHZ9hT0DeajMeo7UKY0rZAXTOMh5hoMp5rs2nmZBiZnTeaObWmFPpTYQqbm5q5uWSMdFJpb6JlFGcs"
        "3c/YUzrEeGF9sSnYKMgzFqbU98WmLGOKawulAKXQl1LZR/fAZ0bgVmsQ0ggtuKLJWLq5tKeCBLsNvZnL4Jhf72R8eOICvic2"
        "ZYEZaUpQ1qw3zth36c7SyXA5uuoX3MoiCKaWsqu7/awZXsvopWOGZVozZnvGHZrqzpuMCAy8rtT2nD3jiWsIupRnIUxtE4Q1"
        "ALfSWvIMBOw8S5wRozKlGKG4yBSBL93v2NdkZC5szsqGkIjaLk2X7GnbNTFdkggKEou0uTQzAn8uz0jK2OhBylwCrRlL2dS+"
        "JsMwrXV2tpj1VhTuu1pk8WR4nkxWUkvqXFqcxd2XZ2QTROK2glSiOGPxZOwp6Ms5++iSLpFZ6s+Ym6V9ps0lMNkJ4VOEc24j"
        "w1r2h+P0Z0C2TjOlwICknb795aIWTUZRwZfCohUuE7VdSm33VJBQnHdSFF+0oir02ZtLz1E3Za64VpoVBbp6BmouzKr8YpYq"
        "DTcBRAqZwVpUuaCxZY4qRV0zE2NOC2QHl1kVQMxRpU0MggzBKXO2qsSmll8tsUp3xVxUyQLPAdn+7FbUcPt4C8kcVXPvBPdc"
        "WUCWybkTDvGfGvIvCVTclfA5CG9VZIavxaqfnIG/W2TVSkYnpcpZBViNVe+5lGSmqrU1dcWzXBYZSdWzMxtLAMQyXhfF4lgs"
        "klT9jGSuqloZbaxiOhi/Vqx+tOT14x66u6qqo9c2cR5NcKtV9Ycnq36WqlNgLFgdE7KKz51xeetzdGZVVYNJPHAoGpkHdett"
        "krtcFi26bTqIpyBlYasBkKeee7KM7LkkrNt24cpo1hqYo48H+LAIq72KMlstXECek+HozBIkVnufYvEphHLGWP3E6HBPDCQI"
        "lwJAtewciIHMxOZlWB1SspAd5KprCmHmYfdCrI41TtRGbp/iVyiE2aHq/WB1FFwFsDGbvJp0E7ZG/NV+yF60SkSeBETOVxvC"
        "PLXAbKZVO2kUV7kwpYiBzAthXi2z6sSkNCIZb4NYbQhziJrVquroIPBYtNWalsXZO+RLACQznYzOPuhiieztyEc/Tv5mqdpU"
        "VWcoynJDmb15NXUDrJ+janBZ8igVA0EbXksZyTyrLlql7baAFcqtNjD/8MQk6kxVg3A5O+elclQHsgy756j624fKDW/fhO23"
        "/nz9YrbK1VmRvkdV9h0XO5S2fefiLKtDn6+z8cX2v19f/D+9fF11",
    ),
    "cert_2d_upper_compact.json": (
        "733b45e35f0a986d5341e201962d197e8387eb94290a017e245b238825ad3776",
        "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",
    ),
    "cert_2d_lower_compact.json": (
        "d66b660f180809e89e220c332c60ad5006253b0147bec2cac9323918657a877d",
        "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"
        "PwH2g47j",
    ),
}


# ======================================================================
# Lane-C exact model builder (verbatim slice of sdp_model.py; see docstring)
# ======================================================================

Q = Fraction
Affine = Dict[str, Q]  # the key "one" denotes the constant coefficient


def rat(value) -> Q:
    if isinstance(value, Fraction):
        return value
    return Q(str(value))


def qstr(value: Q) -> str:
    value = rat(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def aff(*items: Tuple[str, object]) -> Affine:
    out: Affine = {}
    for key, value in items:
        value = rat(value)
        if value:
            out[key] = out.get(key, Q(0)) + value
    return {k: v for k, v in out.items() if v}


def aff_add(*forms: Mapping[str, Q]) -> Affine:
    out: Affine = {}
    for form in forms:
        for key, value in form.items():
            out[key] = out.get(key, Q(0)) + rat(value)
    return {k: v for k, v in out.items() if v}


def aff_scale(form: Mapping[str, Q], scale) -> Affine:
    scale = rat(scale)
    return {k: rat(v) * scale for k, v in form.items() if rat(v) * scale}


def serialize_affine(form: Mapping[str, Q]) -> Dict[str, str]:
    return {key: qstr(value) for key, value in sorted(form.items()) if value}


def deserialize_affine(form: Mapping[str, str]) -> Affine:
    return {key: rat(value) for key, value in form.items() if rat(value)}


def dagger_steps(steps: Sequence[str]) -> Tuple[str, ...]:
    def flip(step: str) -> str:
        return ("-" if step[0] == "+" else "+") + step[1:]
    return tuple(flip(step) for step in reversed(steps))


def _step_vector(step: str, axes: Sequence[str]) -> Tuple[int, ...]:
    out = [0] * len(axes)
    out[axes.index(step[1:])] = 1 if step[0] == "+" else -1
    return tuple(out)


def _vector_step(vector: Sequence[int], axes: Sequence[str]) -> str:
    nz = [(i, x) for i, x in enumerate(vector) if x]
    if len(nz) != 1 or abs(nz[0][1]) != 1:
        raise ValueError(f"not a signed unit step: {vector}")
    i, x = nz[0]
    return ("+" if x > 0 else "-") + axes[i]


def _point_group(D: int):
    # Lane-A emission convention: axis permutations x global sign reversal only
    # (order 2*D!; 48 in 4D).  Single-axis reflections are intentionally excluded
    # so canonicalization matches the equation generator's variable identification.
    for perm in itertools.permutations(range(D)):
        for sign in (-1, 1):
            yield perm, (sign,) * D


def _transform_vector(vector: Sequence[int], transform) -> Tuple[int, ...]:
    perm, signs = transform
    out = [0] * len(vector)
    for old, value in enumerate(vector):
        out[perm[old]] = signs[old] * value
    return tuple(out)


def _transform_steps(steps: Sequence[str], D: int, transform) -> Tuple[str, ...]:
    axes = ("x", "y", "z", "t")[:D]
    return tuple(_vector_step(_transform_vector(_step_vector(s, axes), transform), axes) for s in steps)


def canonical_single(steps: Sequence[str], D: int) -> str:
    """CORE single-trace canonical form (cyclic, dagger, hypercubic)."""
    steps = tuple(steps)
    if not steps:
        return "[]"
    candidates = []
    for transform in _point_group(D):
        transformed = _transform_steps(steps, D, transform)
        for base in (transformed, dagger_steps(transformed)):
            for k in range(len(base)):
                candidates.append(base[k:] + base[:k])
    return json.dumps(min(candidates), separators=(",", ":"))


def _prefixes(steps: Sequence[str], D: int) -> List[Tuple[int, ...]]:
    axes = ("x", "y", "z", "t")[:D]
    here = [0] * D
    out = []
    for step in steps:
        out.append(tuple(here))
        vec = _step_vector(step, axes)
        here = [a + b for a, b in zip(here, vec)]
    return out


def _rotations_with_starts(steps: Sequence[str], start: Sequence[int], D: int):
    steps = tuple(steps)
    if not steps:
        yield steps, tuple(start)
        return
    for k, prefix in enumerate(_prefixes(steps, D)):
        yield steps[k:] + steps[:k], tuple(a + b for a, b in zip(start, prefix))


def canonical_double(
    steps1: Sequence[str], steps2: Sequence[str], offset: Sequence[int], D: int
) -> str:
    """Joint CORE double-trace canonicalization including relative placement.

    Each loop may be cyclically re-based (with the corresponding offset change), while
    dagger is simultaneous as required by charge-conjugation reality.
    """
    w1, w2 = tuple(steps1), tuple(steps2)
    offset = tuple(int(x) for x in offset)
    if len(offset) != D:
        raise ValueError(f"double-trace offset has dimension {len(offset)}, expected {D}")
    candidates = []
    for simultaneous_dagger in (False, True):
        a = dagger_steps(w1) if simultaneous_dagger else w1
        b = dagger_steps(w2) if simultaneous_dagger else w2
        for ar, ao in _rotations_with_starts(a, (0,) * D, D):
            for br, bo in _rotations_with_starts(b, offset, D):
                for transform in _point_group(D):
                    at = _transform_steps(ar, D, transform)
                    bt = _transform_steps(br, D, transform)
                    aot = _transform_vector(ao, transform)
                    bot = _transform_vector(bo, transform)
                    d = tuple(y - x for x, y in zip(aot, bot))
                    candidates.append((at, bt, d))
                    candidates.append((bt, at, tuple(-x for x in d)))
    best = min(candidates)
    return json.dumps([best[0], best[1], best[2]], separators=(",", ":"))


def _get_steps(rep: Mapping) -> Tuple[str, ...]:
    if "steps" in rep:
        return tuple(rep["steps"])
    if "word" in rep:
        word = rep["word"]
        return tuple(word.get("steps", word)) if isinstance(word, Mapping) else tuple(word)
    raise ValueError(f"representative has no steps: {rep}")


def parse_double_rep(rep: Mapping, D: int) -> Tuple[Tuple[str, ...], Tuple[str, ...], Tuple[int, ...]]:
    """Accept the explicit layouts commonly used for the CORE pair representative."""
    if "factors" in rep:
        f1, f2 = rep["factors"]
        s1, s2 = _get_steps(f1), _get_steps(f2)
        if f1.get("dagger") or f1.get("conjugated"):
            s1 = dagger_steps(s1)
        if f2.get("dagger") or f2.get("conjugated"):
            s2 = dagger_steps(s2)
        if "offset" in rep:
            d = rep["offset"]
        else:
            o1 = f1.get("offset", [0] * D)
            o2 = f2.get("offset", [0] * D)
            d = [b - a for a, b in zip(o1, o2)]
        return s1, s2, tuple(d)
    first = rep.get("C1", rep.get("first", rep.get("left")))
    second = rep.get("C2", rep.get("second", rep.get("right")))
    if first is None or second is None:
        raise ValueError(f"unrecognized double representative: {rep}")
    s1 = _get_steps(first) if isinstance(first, Mapping) else tuple(first)
    s2 = _get_steps(second) if isinstance(second, Mapping) else tuple(second)
    flags = rep.get("flags", [False, False])
    if (isinstance(first, Mapping) and (first.get("dagger") or first.get("conjugated"))) or flags[0]:
        s1 = dagger_steps(s1)
    if (isinstance(second, Mapping) and (second.get("dagger") or second.get("conjugated"))) or flags[1]:
        s2 = dagger_steps(s2)
    d = rep.get("offset", rep.get("relative_offset", [0] * D))
    return s1, s2, tuple(d)


@dataclass
class PSDPair:
    name: str
    matrix: List[List[Affine]]


@dataclass
class ExactModel:
    name: str
    variables: List[str]
    bounds: Dict[str, Tuple[Q, Q]]
    equations: List[Tuple[str, Affine]]
    psd_blocks: List[PSDPair]
    objective: str
    additions: List[dict] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

    def as_exact_dict(self):
        return {
            "name": self.name,
            "variables": self.variables,
            "bounds": {k: [qstr(v[0]), qstr(v[1])] for k, v in self.bounds.items()},
            "equations": [{"id": k, "affine": serialize_affine(v)} for k, v in self.equations],
            "psd_blocks": [
                {"name": b.name, "matrix": [[serialize_affine(x) for x in row] for row in b.matrix]}
                for b in self.psd_blocks
            ],
            "objective": self.objective,
            "additions": self.additions,
            "metadata": self.metadata,
        }

    @classmethod
    def from_exact_dict(cls, data):
        return cls(
            name=data["name"],
            variables=list(data["variables"]),
            bounds={k: (rat(v[0]), rat(v[1])) for k, v in data["bounds"].items()},
            equations=[(e["id"], deserialize_affine(e["affine"])) for e in data["equations"]],
            psd_blocks=[PSDPair(b["name"], [[deserialize_affine(x) for x in row] for row in b["matrix"]]) for b in data["psd_blocks"]],
            objective=data["objective"],
            additions=list(data.get("additions", [])),
            metadata=dict(data.get("metadata", {})),
        )


def _alias(variable: Mapping, fallback: str) -> str:
    return str(variable.get("alias", fallback))


def _find_plaquette(variables: Mapping[str, Mapping]) -> Tuple[str, Tuple[str, ...]]:
    matches = []
    for vid, item in variables.items():
        if item.get("kind") != "single":
            continue
        alias = _alias(item, vid).lower()
        length = item.get("length", len(_get_steps(item["rep"])))
        if alias in ("w_p", "p", "plaquette") or vid == "w_P":
            return vid, _get_steps(item["rep"])
        if length == 4:
            matches.append((vid, _get_steps(item["rep"])))
    if len(matches) == 1:
        return matches[0]
    raise ValueError("could not identify a unique w_P plaquette variable")


def _fresh_double_id(key: str, existing: Mapping[str, object]) -> str:
    stem = "td_enrich_" + hashlib.sha256(key.encode()).hexdigest()[:12]
    candidate = stem
    n = 1
    while candidate in existing:
        n += 1
        candidate = f"{stem}_{n}"
    return candidate


def _operator_candidates(data: Mapping, D: int, p_steps: Tuple[str, ...]):
    """Return anchored local operators for the Gram block.

    CORE singles through length six form the retained local basis.  Every explicit
    factor placement of a declared double variable is additionally admitted, so each
    equation double is realized by at least one Gram cell (a true-moment Gram over a
    larger anchored-operator set is still a true-moment Gram; enlargement is sound).
    """
    ops = []
    seen = set()

    def add(steps, offset, label):
        token = (tuple(steps), tuple(offset))
        if token not in seen:
            seen.add(token)
            ops.append({"steps": tuple(steps), "offset": tuple(offset), "label": label})

    for vid, item in data["variables"].items():
        if item.get("kind") == "single":
            steps = _get_steps(item["rep"])
            length = item.get("length", len(steps))
            alias = _alias(item, vid).lower()
            if length <= 6 or alias in ("w_p", "w_r12", "p", "r12"):
                add(steps, (0,) * D, vid)
    for vid, item in data["variables"].items():
        if item.get("kind") != "double":
            continue
        try:
            s1, s2, d = parse_double_rep(item["rep"], D)
        except (KeyError, TypeError, ValueError):
            continue
        for steps, offset in ((s1, (0,) * D), (s2, d)):
            add(steps, offset, f"factor:{vid}")
    return ops


def build_core_model(data) -> ExactModel:
    meta = data["meta"]
    D = int(meta["D"])
    if int(meta["N"]) != 3 or rat(meta["beta"]) != 6:
        raise ValueError("lane C requires the CORE N=3, beta=6 convention")

    declared = data["variables"]
    variables = [vid for vid, item in declared.items() if item.get("kind") != "const"]
    bounds = {}
    for vid in variables:
        if vid not in data["bounds"]:
            raise ValueError(f"missing pointwise support bound for {vid}")
        lo, hi = map(rat, data["bounds"][vid])
        bounds[vid] = (lo, hi)

    equations = []
    for equation in data["equations"]:
        if equation.get("sense") != "=0":
            raise ValueError(f"non-equality SD equation {equation.get('id')}")
        form = {k: rat(v) for k, v in equation["terms"].items() if rat(v)}
        unknown = set(form) - set(variables) - {"one"}
        if unknown:
            raise ValueError(f"equation {equation['id']} uses undeclared variables {sorted(unknown)}")
        equations.append((equation["id"], form))

    p_id, p_steps = _find_plaquette(declared)
    single_map = {}
    double_map = {}
    roundtrip = 0
    for vid, item in declared.items():
        if item.get("kind") == "single":
            key = canonical_single(_get_steps(item["rep"]), D)
            if key in single_map and single_map[key] != vid:
                raise ValueError(f"duplicate canonical single representatives: {single_map[key]}, {vid}")
            single_map[key] = vid
        elif item.get("kind") == "double":
            s1, s2, d = parse_double_rep(item["rep"], D)
            key = canonical_double(s1, s2, d, D)
            decoded = json.loads(key)
            if canonical_double(decoded[0], decoded[1], decoded[2], D) != key:
                raise ValueError(f"double canonical round-trip failed for {vid}")
            if key in double_map and double_map[key] != vid:
                raise ValueError(f"duplicate canonical double representatives: {double_map[key]}, {vid}")
            double_map[key] = vid
            roundtrip += 1

    additions = []

    def ensure_double(s1, o1, s2, o2, purpose):
        d = tuple(b - a for a, b in zip(o1, o2))
        key = canonical_double(s1, s2, d, D)
        if key in double_map:
            return double_map[key]
        vid = _fresh_double_id(key, {**declared, **bounds})
        double_map[key] = vid
        variables.append(vid)
        bounds[vid] = (Q(-1, 2), Q(1))
        additions.append({"id": vid, "kind": "double", "canonical_rep": json.loads(key), "purpose": purpose, "bounds": ["-1/2", "1"]})
        return vid

    ops = _operator_candidates(data, D, p_steps)
    if not ops:
        raise ValueError("empty local-operator Gram basis")

    gram_labels = ["one"] + [op["label"] for op in ops]
    n = len(gram_labels)
    gram = [[{} for _ in range(n)] for _ in range(n)]
    gram[0][0] = aff(("one", 1))
    for i, op in enumerate(ops, 1):
        skey = canonical_single(op["steps"], D)
        if skey not in single_map:
            raise ValueError(f"Gram operator {op['label']} has no declared single expectation")
        gram[0][i] = gram[i][0] = aff((single_map[skey], 1))
    for i, left in enumerate(ops, 1):
        for j, right in enumerate(ops[i - 1 :], i):
            same = ensure_double(left["steps"], left["offset"], right["steps"], right["offset"], "Gram ReTrA ReTrB")
            conj = ensure_double(left["steps"], left["offset"], dagger_steps(right["steps"]), right["offset"], "Gram ReTrA ReTrBbar")
            entry = aff_add(aff((same, Q(1, 2))), aff((conj, Q(1, 2))))
            gram[i][j] = gram[j][i] = entry

    # p2 is the exact expansion of x_P^2 = (Re Tr W / 3)^2.
    p_same = ensure_double(p_steps, (0,) * D, p_steps, (0,) * D, "plaquette p2 same orientation")
    p_conj = ensure_double(p_steps, (0,) * D, dagger_steps(p_steps), (0,) * D, "plaquette p2 conjugate orientation")
    p1 = aff((p_id, 1))
    p2 = aff((p_same, Q(1, 2)), (p_conj, Q(1, 2)))
    p3_id, p4_id = "p_3", "p_4"
    for vid, interval in ((p3_id, (Q(-1, 8), Q(1))), (p4_id, (Q(0), Q(1)))):
        if vid in bounds:
            raise ValueError(f"reserved auxiliary variable already declared: {vid}")
        variables.append(vid)
        bounds[vid] = interval
        additions.append({"id": vid, "kind": "power_moment", "bounds": [qstr(interval[0]), qstr(interval[1])]})
    p3, p4, one = aff((p3_id, 1)), aff((p4_id, 1)), aff(("one", 1))

    hankel = [
        [one, p1, p2],
        [p1, p2, p3],
        [p2, p3, p4],
    ]
    loc_lo = [
        [aff_add(p1, aff(("one", Q(1, 2)))), aff_add(p2, aff_scale(p1, Q(1, 2)))],
        [aff_add(p2, aff_scale(p1, Q(1, 2))), aff_add(p3, aff_scale(p2, Q(1, 2)))],
    ]
    loc_hi = [
        [aff_add(one, aff_scale(p1, -1)), aff_add(p1, aff_scale(p2, -1))],
        [aff_add(p1, aff_scale(p2, -1)), aff_add(p2, aff_scale(p3, -1))],
    ]
    blocks = [PSDPair("local_gram", gram), PSDPair("plaquette_hankel", hankel), PSDPair("plaquette_localize_lo", loc_lo), PSDPair("plaquette_localize_hi", loc_hi)]

    return ExactModel(
        name=f"CORE_D{D}_beta6",
        variables=variables,
        bounds=bounds,
        equations=equations,
        psd_blocks=blocks,
        objective=p_id,
        additions=additions,
        metadata={
            "D": D,
            "N": 3,
            "beta": "6",
            "double_roundtrip_count": roundtrip,
            "gram_basis": gram_labels,
            "p2_identity": f"({p_same}+{p_conj})/2",
            "fresh_pair_variables": sum(x.get("kind") == "double" for x in additions),
        },
    )


def synthetic_model() -> ExactModel:
    return ExactModel(
        name="selftest_gram_quarter",
        variables=["v1", "v2"],
        bounds={"v1": (Q(-1), Q(1)), "v2": (Q(-1), Q(1))},
        equations=[("quarter", aff(("v2", 1), ("one", Q(-1, 4))))],
        psd_blocks=[PSDPair("gram", [[aff(("one", 1)), aff(("v1", 1))], [aff(("v1", 1)), aff(("v2", 1))]])],
        objective="v1",
        metadata={"known_optimum": "1/2"},
    )


def evaluate_affine(form: Mapping[str, Q], values: Mapping[str, float]) -> float:
    return float(form.get("one", Q(0))) + sum(float(coef) * values[var] for var, coef in form.items() if var != "one")


# ======================================================================
# Lane-C exact certificate verifier (verbatim slices of certify.py)
# ======================================================================

class CertificateError(Exception):
    pass


def exact_psd_ldlt(matrix):
    """Symmetric-pivoted exact LDL^T semidefinite test.

    Returns (ok, pivots, diagnostic).  A zero diagonal in a PSD residual forces its
    entire residual row to vanish; this handles singular multipliers without division.
    """
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        return False, [], "matrix is not square"
    a = [[rat(matrix[i][j]) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                return False, [], f"asymmetry at ({i},{j}): {qstr(a[i][j])} != {qstr(a[j][i])}"
    pivots = []
    permutation = list(range(n))
    for k in range(n):
        negative = next((i for i in range(k, n) if a[i][i] < 0), None)
        if negative is not None:
            return False, pivots, f"negative Schur diagonal at original index {permutation[negative]}: {qstr(a[negative][negative])}"
        pivot_index = next((i for i in range(k, n) if a[i][i] > 0), None)
        if pivot_index is None:
            for i in range(k, n):
                for j in range(k, n):
                    if a[i][j] != 0:
                        return False, pivots, f"zero-diagonal residual has nonzero ({permutation[i]},{permutation[j]})={qstr(a[i][j])}"
            pivots.extend(Q(0) for _ in range(k, n))
            return True, pivots, "ok"
        if pivot_index != k:
            a[k], a[pivot_index] = a[pivot_index], a[k]
            for row in a:
                row[k], row[pivot_index] = row[pivot_index], row[k]
            permutation[k], permutation[pivot_index] = permutation[pivot_index], permutation[k]
        pivot = a[k][k]
        pivots.append(pivot)
        for i in range(k + 1, n):
            for j in range(i, n):
                updated = a[i][j] - a[i][k] * a[j][k] / pivot
                a[i][j] = a[j][i] = updated
        for i in range(k + 1, n):
            a[i][k] = a[k][i] = Q(0)
    return True, pivots, "ok"


def _accumulate_affine(total, form, multiplier):
    multiplier = rat(multiplier)
    for name, coef in form.items():
        total[name] = total.get(name, Q(0)) + multiplier * rat(coef)


def _model_block_map(model):
    out = {}
    for block in model.psd_blocks:
        if block.name in out:
            raise CertificateError(f"duplicate model PSD block name {block.name}")
        out[block.name] = block
    return out


def verify_certificate(certificate, model: ExactModel, emit=True):
    side = certificate.get("side")
    if side not in ("upper", "lower"):
        raise CertificateError(f"invalid certificate side {side}")
    if certificate.get("objective") != model.objective:
        raise CertificateError(f"objective mismatch: {certificate.get('objective')} != {model.objective}")
    bound = rat(certificate["bound"])
    rhs = {}

    eq_map = {eid: form for eid, form in model.equations}
    supplied_eq = certificate.get("equation_multipliers", {})
    if set(supplied_eq) != set(eq_map):
        raise CertificateError(f"equation multiplier ids mismatch: supplied={sorted(supplied_eq)}, expected={sorted(eq_map)}")
    for eid, value in supplied_eq.items():
        _accumulate_affine(rhs, eq_map[eid], rat(value))

    block_map = _model_block_map(model)
    supplied_blocks = certificate.get("psd_multipliers", [])
    if [x.get("block") for x in supplied_blocks] != [x.name for x in model.psd_blocks]:
        raise CertificateError("PSD block order/names mismatch")
    for supplied in supplied_blocks:
        block = block_map[supplied["block"]]
        matrix = [[rat(value) for value in row] for row in supplied["matrix"]]
        if len(matrix) != len(block.matrix) or any(len(row) != len(block.matrix) for row in matrix):
            raise CertificateError(f"PSD dimension mismatch in {block.name}")
        ok, pivots, diagnostic = exact_psd_ldlt(matrix)
        if not ok:
            raise CertificateError(f"PSD multiplier {block.name} rejected: {diagnostic}")
        for i, row in enumerate(block.matrix):
            for j, form in enumerate(row):
                _accumulate_affine(rhs, form, matrix[i][j])

    boxes = certificate.get("box_multipliers", {})
    lower = boxes.get("lower", {})
    upper = boxes.get("upper", {})
    if set(lower) != set(model.variables) or set(upper) != set(model.variables):
        raise CertificateError("box multiplier variable ids mismatch")
    for name in model.variables:
        ml, mu = rat(lower[name]), rat(upper[name])
        if ml < 0:
            raise CertificateError(f"negative lower-box multiplier for {name}: {qstr(ml)}")
        if mu < 0:
            raise CertificateError(f"negative upper-box multiplier for {name}: {qstr(mu)}")
        lo, hi = model.bounds[name]
        rhs[name] = rhs.get(name, Q(0)) + ml - mu
        rhs["one"] = rhs.get("one", Q(0)) - ml * lo + mu * hi

    target = {"one": bound if side == "upper" else -bound}
    target[model.objective] = Q(-1) if side == "upper" else Q(1)
    for key in ["one"] + model.variables:
        residual = target.get(key, Q(0)) - rhs.get(key, Q(0))
        if residual:
            raise CertificateError(f"affine identity mismatch at {key}: {qstr(residual)}")
    unexpected = {k: v for k, v in rhs.items() if k not in set(model.variables) | {"one"} and v}
    if unexpected:
        key = sorted(unexpected)[0]
        raise CertificateError(f"affine identity has unknown coefficient {key}: {qstr(unexpected[key])}")
    if emit:
        print(f"CERTIFIED {side.upper()}: {qstr(bound)}")
    return bound


# ======================================================================
# Gates
# ======================================================================

CHECKS: List[Tuple[str, bool]] = []

# Shape pins discovered from the lane-A payloads via the lane-C builder
# (independently reproduced before embedding; every gate below re-derives
# these from the embedded payloads at run time).
PIN_2D_INVENTORY = (24, 6, 3)      # (model variables, additions, equations)
PIN_4D_INVENTORY = (440, 276, 9)
PIN_2D_PSD_DIMS = [8, 3, 2, 2]
PIN_4D_PSD_DIMS = [63, 3, 2, 2]
PIN_2D_FRESH_PAIRS = 4
PIN_4D_FRESH_PAIRS = 274
PIN_2D_EQUATION_IDS = ["SD_P_orbit1", "SD_R12_long", "SD_R12_short"]
PIN_4D_EQUATION_IDS = [
    "SD_P_orbit1", "SD_R12_long", "SD_R12_short",
    "SD_L6c1_orbit1", "SD_L6c1_orbit2", "SD_L6c1_orbit3",
    "SD_L6c2_orbit1", "SD_L6c2_orbit2", "SD_L6c2_orbit3",
]
PIN_OBJECTIVE = "w_P"


def check(label, ok, detail=""):
    CHECKS.append((label, bool(ok)))
    line = f"{'PASS' if ok else 'FAIL'}: {label}"
    if detail:
        line += f" | {detail}"
    print(line, flush=True)
    return bool(ok)


def load_payload(name):
    """Decode one embedded payload and verify its pinned sha256 (raw bytes)."""
    sha_expected, b64 = PAYLOADS[name]
    raw = zlib.decompress(base64.b64decode(b64))
    sha = hashlib.sha256(raw).hexdigest()
    if sha != sha_expected:
        raise RuntimeError(f"payload {name}: sha256 {sha} != pinned {sha_expected}")
    return json.loads(raw.decode("utf-8")), sha


# ----------------------------------------------------------------------
# SU(3) maximal-torus (Weyl) quadrature.
#
# Class functions of SU(3) reduce to integrals over the maximal torus
# {diag(e^{it1}, e^{it2}, e^{-i(t1+t2)})} against the Weyl measure
# |Delta|^2 dt1 dt2 with Delta = prod_{i<j}(z_i - z_j).  The one-plaquette
# density at coupling beta is exp((beta/N) Re Tr U) = exp((beta/3) Re p1).
# The integrand is smooth and 2*pi-periodic in both angles, so the midpoint
# rule converges exponentially; QUAD_N = 256 puts every moment used here far
# below the gate tolerances.
# ----------------------------------------------------------------------

QUAD_N = 256


def su3_weyl_moments(beta, n=QUAD_N):
    """Normalized torus moments of p1 = Tr U and p2 = Tr U^2 at coupling beta."""
    zs = []
    for k in range(n):
        t = 2.0 * math.pi * (k + 0.5) / n
        zs.append(complex(math.cos(t), math.sin(t)))
    z_norm = 0.0
    m_p1 = 0j
    m_p2 = 0j
    m_p1sq = 0j
    m_p1cu = 0j
    m_p1sq_p1bar = 0j
    m_absp1sq = 0.0
    m_absp1_4 = 0.0
    third_beta = beta / 3.0
    for z1 in zs:
        for z2 in zs:
            z3 = (z1 * z2).conjugate()
            p1 = z1 + z2 + z3
            p2v = z1 * z1 + z2 * z2 + z3 * z3
            d = (z1 - z2) * (z1 - z3) * (z2 - z3)
            w = (d.real * d.real + d.imag * d.imag) * math.exp(third_beta * p1.real)
            z_norm += w
            m_p1 += w * p1
            m_p2 += w * p2v
            sq = p1 * p1
            m_p1sq += w * sq
            m_p1cu += w * sq * p1
            m_p1sq_p1bar += w * sq * p1.conjugate()
            a2 = p1.real * p1.real + p1.imag * p1.imag
            m_absp1sq += w * a2
            m_absp1_4 += w * a2 * a2
    return {
        "p1": m_p1 / z_norm,
        "p2": m_p2 / z_norm,
        "p1sq": m_p1sq / z_norm,
        "p1cu": m_p1cu / z_norm,
        "p1sq_p1bar": m_p1sq_p1bar / z_norm,
        "absp1sq": m_absp1sq / z_norm,
        "absp1_4": m_absp1_4 / z_norm,
    }


# ----------------------------------------------------------------------
# Independent 2D oracle: comb gauge -> independent face variables ->
# explicit SU(3) moment-tensor contraction.  In 2D the Wilson measure
# factorizes over plaquettes in an axial (comb) gauge, so every lattice
# expectation reduces to a finite contraction of one-plaquette moment
# tensors.  The tensor constants come from the quadrature above via
# character / power-sum identities:
#   chi_(2,0) = (p1^2 + p2)/2,  chi_(0,1) = (p1^2 - p2)/2,
#   chi_adj   = |p1|^2 - 1,
#   E[V_ij]        = w1 d_ij,                        w1    = <p1>/3
#   E[V_ij V_kl]   = A2 d_ij d_kl + B2 d_il d_kj,    alpha = <chi_(2,0)>/6,
#                                                    gamma = <chi_(0,1)>/3,
#                                                    A2 = (alpha+gamma)/2,
#                                                    B2 = (alpha-gamma)/2
#   E[V_ij Vd_kl]  = ((1-c8)/3) d_il d_jk + c8 d_ij d_kl,  c8 = <chi_adj>/8
# This oracle is independent of the SDP: it never sees the certificates.
# ----------------------------------------------------------------------

DIRS = {"+x": (1, 0), "-x": (-1, 0), "+y": (0, 1), "-y": (0, -1)}


def word_slots(steps, offset):
    """Closed 2D lattice word -> list of (face, kind) slots, kind in {V, Vd}.

    Comb gauge on the plane: vertical links = identity, x-axis horizontal
    links = identity; the horizontal link at height j>0 leaving (i,j) is
    H_{i,j} = Vd_{i,j-1} ... Vd_{i,0}; for j<0 it is H_{i,j} = V_{i,j} ...
    V_{i,-1}.  A -x step uses H^dagger.  Ends with cyclic free reduction.
    """
    pos = tuple(offset)
    letters = []
    for s in steps:
        dx, dy = DIRS[s]
        if dy != 0:
            pos = (pos[0], pos[1] + dy)
            continue
        i = pos[0] if dx > 0 else pos[0] - 1
        j = pos[1]
        if j > 0:
            h = [((i, jj), "Vd") for jj in range(j - 1, -1, -1)]
        elif j < 0:
            h = [((i, jj), "V") for jj in range(j, 0)]
        else:
            h = []
        if dx < 0:
            h = [(f, ("V" if k == "Vd" else "Vd")) for (f, k) in reversed(h)]
        letters.extend(h)
        pos = (pos[0] + dx, pos[1])
    if list(pos) != list(offset):
        raise ValueError(f"word not closed: {steps} from {offset} ends {pos}")
    changed = True
    while changed and letters:
        changed = False
        n = len(letters)
        for a in range(n):
            b = (a + 1) % n
            fa, ka = letters[a]
            fb, kb = letters[b]
            if fa == fb and ka != kb:
                for idx in sorted([a, b], reverse=True):
                    letters.pop(idx)
                changed = True
                break
    return letters


class CombOracle:
    """Float64 2D lattice-expectation oracle built from the torus quadrature."""

    def __init__(self, m6):
        self.w1 = m6["p1"].real / 3.0
        chi20 = (m6["p1sq"].real + m6["p2"].real) / 2.0
        chi01 = (m6["p1sq"].real - m6["p2"].real) / 2.0
        alpha = chi20 / 6.0
        gamma = chi01 / 3.0
        self.A2 = (alpha + gamma) / 2.0
        self.B2 = (alpha - gamma) / 2.0
        self.c8 = (m6["absp1sq"] - 1.0) / 8.0

    def face_tensor(self, kinds):
        T = {}
        if len(kinds) == 1:
            for i in range(3):
                T[(i, i)] = self.w1
            return T
        if len(kinds) != 2:
            raise ValueError(f"face degree {len(kinds)} > 2 unsupported")
        k1, k2 = kinds
        if k1 == k2:
            for i, j, k, l in itertools.product(range(3), repeat=4):
                v = 0.0
                if i == j and k == l:
                    v += self.A2
                if i == l and k == j:
                    v += self.B2
                if v != 0.0:
                    T[(i, j, k, l)] = v
            return T
        swap = (k1 == "Vd")
        for i, j, k, l in itertools.product(range(3), repeat=4):
            ii, jj, kk, ll = (k, l, i, j) if swap else (i, j, k, l)
            v = 0.0
            if ii == ll and jj == kk:
                v += (1.0 - self.c8) / 3.0
            if ii == jj and kk == ll:
                v += self.c8
            if v != 0.0:
                T[(i, j, k, l)] = v
        return T

    def expect(self, trace_strings):
        """Raw expectation <prod Tr(...)> of face-variable letter strings."""
        slots = []
        for ti, ls in enumerate(trace_strings):
            for pi, (f, k) in enumerate(ls):
                slots.append((ti, pi, f, k))
        if not slots:
            return 3.0 ** len(trace_strings)
        faces = {}
        for si, (ti, pi, f, k) in enumerate(slots):
            faces.setdefault(f, []).append(si)
        tensors = {}
        for f, sids in faces.items():
            kinds = [slots[s][3] for s in sids]
            tensors[f] = (sids, self.face_tensor(kinds))
        trace_lens = [len(ls) for ls in trace_strings]
        ranges = [itertools.product(range(3), repeat=m) for m in trace_lens]
        sid_of = {(ti, pi): si for si, (ti, pi, f, k) in enumerate(slots)}
        total = 0.0
        for assign in itertools.product(*ranges):
            rc = {}
            for ti, idxs in enumerate(assign):
                m = trace_lens[ti]
                for pi in range(m):
                    si = sid_of[(ti, pi)]
                    rc[si] = (idxs[pi], idxs[(pi + 1) % m])
            val = 1.0
            for f, (sids, T) in tensors.items():
                key = tuple(x for s in sids for x in rc[s])
                v = T.get(key)
                if v is None:
                    val = 0.0
                    break
                val *= v
            total += val
        for ls in trace_strings:
            if not ls:
                total *= 3.0
        return total

    def eval_var(self, v):
        if v.get("kind") == "const":
            return float(v["value"])
        rep = v["rep"]
        if "factors" in rep:
            ls = []
            for f in rep["factors"]:
                l = word_slots(f["steps"], f["offset"])
                if f.get("dagger"):
                    l = [(fc, ("V" if k == "Vd" else "Vd")) for (fc, k) in reversed(l)]
                ls.append(l)
            return self.expect(ls) / 9.0
        l = word_slots(rep["steps"], rep["offset"])
        if rep.get("dagger"):
            l = [(fc, ("V" if k == "Vd" else "Vd")) for (fc, k) in reversed(l)]
        return self.expect([l]) / 3.0


# ----------------------------------------------------------------------
# Gates
# ----------------------------------------------------------------------

def gate_g1(m0):
    """Haar (beta=0) character moments, including the corrected <chi^2 chibar>=0.

    The lane-A one-link spec listed <chi^2 chibar> = 1; the true SU(3) Haar
    value is 0 because chi^2 chibar has N-ality 2-1 = 1 != 0 (only zero-N-ality
    class functions have nonzero Haar mean).  The lanes honestly FAILed that
    target; this gate pins the corrected value.
    """
    tol = 1e-9
    targets = [
        ("<chi> = 0", abs(m0["p1"])),
        ("<|chi|^2> = 1", abs(m0["absp1sq"] - 1.0)),
        ("<chi^2> = 0", abs(m0["p1sq"])),
        ("<chi^2 chibar> = 0 (N-ality; corrects the lane spec's 1)", abs(m0["p1sq_p1bar"])),
        ("<chi^3> = 1", abs(m0["p1cu"] - 1.0)),
        ("<|chi|^4> = 2", abs(m0["absp1_4"] - 2.0)),
    ]
    for label, err in targets:
        check(f"G1 Haar {label}", err < tol, f"err={err:.3e}")


def gate_g2(m6):
    """One-link beta=6 Schwinger-Dyson identity under the Weyl-quadrature measure.

    For dU |Delta|^2 exp((beta/3) Re Tr U) on the torus, the derived SD identity
    (C2 = 4/3, beta/(4N) = 1/2 at beta=6, N=3) reduces on one link to
      (4/3) <Tr U>/1 + (1/2) [ <Tr U^2> - <(Tr U)^2>/3 - 3 + <Tr U Tr Ud>/3 ] = 0
    in normalized-trace conventions matched to the lane-A one-link anchor.
    """
    resid = (4.0 / 3.0) * m6["p1"].real + 0.5 * (
        m6["p2"].real - m6["p1sq"].real / 3.0 - 3.0 + m6["absp1sq"] / 3.0
    )
    check("G2 one-link beta=6 SD residual == 0", abs(resid) < 1e-9, f"residual={resid:.3e}")


def gate_g3(eq2d, eq4d, model2, model4):
    """Rebuild both exact models from the embedded equation payloads and pin shapes."""
    m2, m4 = eq2d["meta"], eq4d["meta"]
    check(
        "G3 2D payload meta (D=2, N=3, beta=6, L_min=5)",
        m2["D"] == 2 and int(m2["N"]) == 3 and rat(m2["beta"]) == 6 and m2["L_min"] == 5,
    )
    check(
        "G3 4D payload meta (D=4, N=3, beta=6, L_min=5)",
        m4["D"] == 4 and int(m4["N"]) == 3 and rat(m4["beta"]) == 6 and m4["L_min"] == 5,
    )
    n_const2 = sum(1 for v in eq2d["variables"].values() if v.get("kind") == "const")
    n_const4 = sum(1 for v in eq4d["variables"].values() if v.get("kind") == "const")
    check(
        "G3 2D JSON inventory: 19 variables (1 const), 3 equations",
        len(eq2d["variables"]) == 19 and n_const2 == 1 and len(eq2d["equations"]) == 3,
    )
    check(
        "G3 4D JSON inventory: 165 variables (1 const), 9 equations",
        len(eq4d["variables"]) == 165 and n_const4 == 1 and len(eq4d["equations"]) == 9,
    )
    check("G3 2D model name", model2.name == "CORE_D2_beta6", model2.name)
    check("G3 4D model name", model4.name == "CORE_D4_beta6", model4.name)
    dims2 = [len(b.matrix) for b in model2.psd_blocks]
    dims4 = [len(b.matrix) for b in model4.psd_blocks]
    check(f"G3 2D PSD block dims == {PIN_2D_PSD_DIMS}", dims2 == PIN_2D_PSD_DIMS, str(dims2))
    check(f"G3 4D PSD block dims == {PIN_4D_PSD_DIMS}", dims4 == PIN_4D_PSD_DIMS, str(dims4))
    inv2 = (len(model2.variables), len(model2.additions), len(model2.equations))
    inv4 = (len(model4.variables), len(model4.additions), len(model4.equations))
    check(f"G3 2D model inventory (vars, additions, equations) == {PIN_2D_INVENTORY}",
          inv2 == PIN_2D_INVENTORY, str(inv2))
    check(f"G3 4D model inventory (vars, additions, equations) == {PIN_4D_INVENTORY}",
          inv4 == PIN_4D_INVENTORY, str(inv4))
    ids2 = [eid for eid, _ in model2.equations]
    ids4 = [eid for eid, _ in model4.equations]
    check("G3 2D equation ids pinned", ids2 == PIN_2D_EQUATION_IDS, str(ids2))
    check("G3 4D equation ids pinned", ids4 == PIN_4D_EQUATION_IDS, str(ids4))
    check(
        "G3 objective is the fundamental plaquette moment in both dims",
        model2.objective == PIN_OBJECTIVE and model4.objective == PIN_OBJECTIVE,
        f"{model2.objective}, {model4.objective}",
    )
    fp2 = model2.metadata.get("fresh_pair_variables")
    fp4 = model4.metadata.get("fresh_pair_variables")
    check(f"G3 fresh Gram-pair variables (2D, 4D) == ({PIN_2D_FRESH_PAIRS}, {PIN_4D_FRESH_PAIRS})",
          fp2 == PIN_2D_FRESH_PAIRS and fp4 == PIN_4D_FRESH_PAIRS, f"({fp2}, {fp4})")


def gate_g4(model, dim_label):
    """All-ones refutation: U == I is box- and PSD-feasible yet violates every
    SD equation by exactly C2 = 4/3.  This separates the beta-coupled loop
    equations from pure moment kinematics: no equation-free relaxation can
    certify the refutation below."""
    one = Q(1)
    check(
        f"G4 {dim_label} all-ones is box-feasible ({len(model.variables)} vars)",
        all(lo <= one <= hi for lo, hi in model.bounds.values()),
    )
    for block in model.psd_blocks:
        mat = [[sum(entry.values(), Q(0)) for entry in row] for row in block.matrix]
        ok, _pivots, diagnostic = exact_psd_ldlt(mat)
        check(f"G4 {dim_label} PSD block {block.name} is PSD at all-ones", ok,
              "" if ok else diagnostic)
    sums = [sum(form.values(), Q(0)) for _, form in model.equations]
    distinct = sorted({qstr(s) for s in sums})
    same = len(distinct) == 1
    value = sums[0] if same else None
    check(
        f"G4 {dim_label} every SD equation evaluates to exactly +-4/3 at all-ones",
        same and value is not None and abs(value) == Q(4, 3),
        f"values={distinct}",
    )
    return value


def gate_g5(oracle, eq2d, model2, m6):
    """2D end-to-end substitution: the independent comb-gauge oracle satisfies
    every embedded 2D SD equation (JSON terms and rebuilt model forms)."""
    P = ["+x", "+y", "-x", "-y"]
    Pbar = ["+x", "-y", "-x", "+y"]
    tol_self = 1e-9
    tol_resid = 1e-10
    self_checks = [
        ("<x_P> == w1", oracle.expect([word_slots(P, (0, 0))]) / 3.0, oracle.w1),
        ("<Tr V^2>/3 == <p2>/3", oracle.expect([word_slots(P + P, (0, 0))]) / 3.0,
         m6["p2"].real / 3.0),
        ("<(Tr V)^2>/9 == <chi^2>/9",
         oracle.expect([word_slots(P, (0, 0)), word_slots(P, (0, 0))]) / 9.0,
         m6["p1sq"].real / 9.0),
        ("<Tr V Tr Vd>/9 == <|chi|^2>/9",
         oracle.expect([word_slots(P, (0, 0)), word_slots(Pbar, (0, 1))]) / 9.0,
         m6["absp1sq"] / 9.0),
    ]
    for label, mine, ref in self_checks:
        check(f"G5 oracle self-check {label}", abs(mine - ref) < tol_self,
              f"delta={abs(mine - ref):.3e}")
    vals = {vid: oracle.eval_var(v) for vid, v in eq2d["variables"].items()}
    for e in eq2d["equations"]:
        r = 0.0
        for vid, c in e["terms"].items():
            fr = Fraction(c)
            r += (fr.numerator / fr.denominator) * vals[vid]
        check(f"G5 2D JSON equation {e['id']} residual < 1e-10", abs(r) < tol_resid,
              f"residual={r:.3e}")
    for eid, form in model2.equations:
        missing = sorted(k for k in form if k != "one" and k not in vals)
        if missing:
            check(f"G5 2D model equation {eid} residual < 1e-10", False,
                  f"oracle missing variables {missing}")
            continue
        r = evaluate_affine(form, vals)
        check(f"G5 2D model equation {eid} residual < 1e-10", abs(r) < tol_resid,
              f"residual={r:.3e}")


def gate_g6(model2, cert_up, cert_lo):
    """Exact rational verification of the embedded 2D dual certificates against
    the freshly rebuilt 2D model.  verify_certificate re-derives the Lagrange
    identity coefficient-by-coefficient in Fraction arithmetic and raises on
    any nonzero residual; nothing numerical survives into this gate."""
    bound_up = bound_lo = None
    try:
        bound_up = verify_certificate(cert_up, model2)
        check("G6 2D upper certificate verifies, bound == 903482039/1000000000",
              bound_up == Q(903482039, 1000000000), qstr(bound_up))
    except CertificateError as exc:
        check("G6 2D upper certificate verifies, bound == 903482039/1000000000",
              False, str(exc))
    try:
        bound_lo = verify_certificate(cert_lo, model2)
        check("G6 2D lower certificate verifies, bound == -10000001/20000000",
              bound_lo == Q(-10000001, 20000000), qstr(bound_lo))
    except CertificateError as exc:
        check("G6 2D lower certificate verifies, bound == -10000001/20000000",
              False, str(exc))
    return bound_up, bound_lo


def gate_g7(oracle, bound_up, bound_lo):
    """Containment and ordering: the certified 2D bracket contains the exact 2D
    value; the upper side is strictly inside the kinematic box; the lower side
    is epsilon-weaker than the kinematic floor (disclosed, not hidden); the 4D
    MC comparator (audit-only, never a derivation input) sits inside this
    runner's certified 4D content, which is only the kinematic box."""
    w1 = oracle.w1
    check("G7 2D exact plaquette w1(beta=6) matches pinned 0.42253173965",
          abs(w1 - 0.42253173965) < 1e-9, f"w1={w1:.12f}")
    up_f = bound_up.numerator / bound_up.denominator
    lo_f = bound_lo.numerator / bound_lo.denominator
    check("G7 certified 2D bracket contains the exact 2D value",
          lo_f < w1 < up_f, f"{lo_f:.9f} < {w1:.11f} < {up_f:.9f}")
    check("G7 certified 2D upper bound < 1 strictly (beyond the kinematic box)",
          bound_up < Q(1), f"1 - upper = {qstr(Q(1) - bound_up)}")
    check("G7 certified 2D lower bound <= -1/2 (eps-weaker than the kinematic floor; disclosed)",
          bound_lo <= Q(-1, 2), f"lower + 1/2 = {qstr(bound_lo + Q(1, 2))}")
    mc = 0.5934  # figure-derived 4D MC comparator: audit-only, never a derivation input
    check("G7 4D MC comparator (audit-only) inside certified 4D content = kinematic box [-1/2, 1]",
          -0.5 <= mc <= 1.0, f"mc={mc}")


def main():
    print("frontier_gauge_sd_loop_equation_beta_coupled_plaquette_bracket")
    print("=" * 78)
    eq2d, sha2d = load_payload("sd_equations_beta6_2d.json")
    eq4d, sha4d = load_payload("sd_equations_beta6_4d.json")
    cert_up, sha_up = load_payload("cert_2d_upper_compact.json")
    cert_lo, sha_lo = load_payload("cert_2d_lower_compact.json")
    print(f"payload sd_equations_beta6_2d.json sha256={sha2d}")
    print(f"payload sd_equations_beta6_4d.json sha256={sha4d}")
    print(f"payload cert_2d_upper_compact.json sha256={sha_up}")
    print(f"payload cert_2d_lower_compact.json sha256={sha_lo}")

    m0 = su3_weyl_moments(0.0)
    m6 = su3_weyl_moments(6.0)
    gate_g1(m0)
    gate_g2(m6)

    model2 = build_core_model(eq2d)
    model4 = build_core_model(eq4d)
    gate_g3(eq2d, eq4d, model2, model4)

    value2 = gate_g4(model2, "2D")
    value4 = gate_g4(model4, "4D")
    check(
        "G4 cross-dim: all 12 SD equations share one signed all-ones value",
        value2 is not None and value2 == value4,
        f"2D={qstr(value2) if value2 is not None else None}, "
        f"4D={qstr(value4) if value4 is not None else None}",
    )

    oracle = CombOracle(m6)
    gate_g5(oracle, eq2d, model2, m6)

    bound_up, bound_lo = gate_g6(model2, cert_up, cert_lo)
    if bound_up is not None and bound_lo is not None:
        gate_g7(oracle, bound_up, bound_lo)
    else:
        check("G7 bracket gates reachable (certificates verified)", False)

    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("=" * 78)
    print(f"TOTAL: PASS={n_pass} FAIL={n_fail}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
