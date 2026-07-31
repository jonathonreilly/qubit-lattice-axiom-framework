#!/usr/bin/env python3
"""Cycle 830 v2: exact collision hierarchy of the S* funnel state.

The landed k=2 update is reimplemented here as an exact Boolean circuit.
Its provenance is the SHA-pinned Cycle-719 ``mapped_macro`` update used by
the tracked Cycle-822 primary copy.  The copied Cycle-822 primary and the
Cycle-819/820 primaries are text/AST-only inputs: an import firewall makes
executing any of them a hard failure.

Only stdlib modules are imported.  The embedded fixtures are a mechanical
serialization of (i) the 11 landed macro gate rows, (ii) the 176 lawful
t=0 data states built by Cycle 822, and (iii) the Cycle-822 S* anatomy pin.
Their raw SHA-256 values are checked before use.  Forward evolution and all
reverse constraints are independently reimplemented below with integer
X/CNOT/Toffoli arithmetic.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle819_deep_k2_continuation_2026_07_28.py",
    "scripts/frontier_cycle820_shared_moment_mechanism_2026_07_28.py",
    "scripts/frontier_cycle822_sstar_basin_2026_07_28.py",
)

import ast
import base64
from collections import defaultdict
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from pathlib import Path
import struct
import sys
from time import monotonic
import zlib


ROOT = Path(__file__).resolve().parents[1]
TEXT_AST_ONLY_PATHS = AUDIT_INPUT_PATHS[1:]
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in TEXT_AST_ONLY_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "e1c18187a4082fc534b9bd94055258a9aedc05c8dda37bb84f6a0d84592308fe",
    AUDIT_INPUT_PATHS[2]:
        "7344bee5d5f0bcbddcea7b9d83f40a552c90188bf30b4905f2649a49e4bf1649",
    AUDIT_INPUT_PATHS[3]:
        "269d235c4981eaa4b94cfc200a0d472bf9f1ca8b57c2e14880afe754a9d41c56",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c123b8d681c3d76fce08ef13d7673622deac64ad",
    AUDIT_INPUT_PATHS[1]: "c3a071835a61e78a4919decfede8534cbf95e1d9",
    AUDIT_INPUT_PATHS[2]: "6385dfa0dce58e86345483cc521ffa325e0d1cce",
    AUDIT_INPUT_PATHS[3]: "56fd26ec1f09e3690aa0e9cacd1447c289fd7ac0",
}


class _BlocklistFinder(importlib.abc.MetaPathFinder):
    """Fail closed if a text/AST-only predecessor is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


IMPORT_FIREWALL = _BlocklistFinder()
sys.meta_path.insert(0, IMPORT_FIREWALL)

RING_STATIONS = 11
FIXTURE_BANKS = 2
FAMILY_SIZE = 176
STATE_BITS = 5815
STATE_BYTES = (STATE_BITS + 7) // 8
MECHANISM_ENTRY = 14739
TREE_DEPTH = 8
GATE_COUNT = 3106
WORD_GATE_COUNT = 6212
EXPECTED_SSTAR_SHA256 = (
    "cdf7e03092c6278b686c1f0edb9ebd716f4a285b1eabc8a7e2780695284a8f1a"
)
EXPECTED_GATE_RAW_SHA256 = (
    "1ef101b5745147bd43c116d87e2774635657e520d744b380bd8bad6d27884f4c"
)
EXPECTED_FAMILY_RAW_SHA256 = (
    "54fbb59c9d2232e77af6204f0c01b079148560bef1409cc74f311b5373784282"
)
EXPECTED_SSTAR_PACKED_SHA256 = (
    "aa15cde162d859356852859309ddbaba74c502ce385212abd476b97405326320"
)
NINE_KEYS = (
    (0, (1, 6)),
    (0, (1, 7)),
    (0, (2, 7)),
    (0, (2, 8)),
    (0, (3, 8)),
    (0, (3, 9)),
    (0, (4, 9)),
    (0, (4, 10)),
    (0, (5, 10)),
)
EXPECTED_NINE_KEY_PARTITIONS = (
    (NINE_KEYS,),
    ((NINE_KEYS[0],), NINE_KEYS[1:4], NINE_KEYS[4:]),
    (
        (NINE_KEYS[0],),
        (NINE_KEYS[1],),
        NINE_KEYS[2:4],
        NINE_KEYS[4:],
    ),
    (
        (NINE_KEYS[0],),
        (NINE_KEYS[1],),
        NINE_KEYS[2:4],
        NINE_KEYS[4:7],
        NINE_KEYS[7:],
    ),
    ((NINE_KEYS[0],), NINE_KEYS[1:4], NINE_KEYS[4:]),
    (
        (NINE_KEYS[0],),
        (NINE_KEYS[1],),
        NINE_KEYS[2:4],
        NINE_KEYS[4:7],
        NINE_KEYS[7:],
    ),
    (
        (NINE_KEYS[0],),
        (NINE_KEYS[1],),
        NINE_KEYS[2:4],
        NINE_KEYS[4:7],
        NINE_KEYS[7:],
    ),
    (
        (NINE_KEYS[0],),
        (NINE_KEYS[1],),
        NINE_KEYS[2:4],
        NINE_KEYS[4:7],
        NINE_KEYS[7:],
    ),
    (
        (NINE_KEYS[0],),
        NINE_KEYS[1:4],
        NINE_KEYS[4:7],
        NINE_KEYS[7:],
    ),
)
EXPECTED_NINE_KEY_OCCUPANCY = (1, 3, 4, 5, 3, 5, 5, 5, 4)
EXPECTED_SHARED_PAIR_COUNTS = (36, 13, 11, 5, 13, 5, 5, 5, 7)
EXPECTED_FORWARD_PARTITION_RELATIONS = (
    "SPLIT_TO_FINER",
    "UNCHANGED",
    "UNCHANGED",
    "COALESCE_TO_COARSER",
    "SPLIT_TO_FINER",
    "COALESCE_TO_COARSER",
    "COALESCE_TO_COARSER",
    "COALESCE_TO_COARSER",
)

# Replaced mechanically from /tmp/cycle830_constants.txt after extraction
# through the tracked, SHA-pinned Cycle-822 build_family/mapped_macro path.
GATE_CONSTANTS_B85 = (
    'c-rk;XVg{26+Ls1Ga_Aj@4dv>VvI4yD6vsRL9ieyQj{hgrAY6+_uf?Oh#eas(xuz6As}6vK<3@OKXg{2QP;vhlErf8zIWffGpFn`Glxxj+2!_XE0-ytlT6aW)zpmQ%1UPu(XwLla0;9}BJN@75k7Q}0NTr=Dd>=Zl#}Ft<pC7{6#<n1l>vVOTmbkp;6lJffQtc_04@dm1#lVQuYk(|e*;_r_&eZAz&`+20saZN8t^Z`HGpdYRRI46TnD%wa6|H6P0hWhXwP7!UZTB%L3)e!mM+pqw2yR^zM_4loAeXyC*7sLX#ZfK0ipwffd+~W3<eq`Iw%-uu;}1mpdq3|f`NvL4h;qxCORw_Xt?O`V4xAABZ7fOijE8h8YMa^7-+QU=wP5RqGN)A#)^&&1{x<iE*NOM==flu38E8%fhLMh3<jDcIw=@vvgqVspedqLf`O)rP7MZ{CORz`Xu9b1V4xYIGlGF;ip~rMnk70b7-+WW>|mfdqH}_Q=8Db@2AU^2FBoXP==@-y1)>XrfjXYP;&;50zvEN*Oum8d<J&nFj*R2vs5uADi1XuYId@uucA=GMGg^@Lq;+X)TAqHOSLh>pjQ*oH>05f5erFUgCKw@z7e-H7EL|7HS(PXTuZiOG>L_-visJgpDCVz-^5OC*S1yb4=+Y?1E{^i=!YDT{i1M~_l+zWXd}sEP3vLA51gHwA2B;3G0jLS61-Kbd8*mHYRzMv<UBGRCdVu<X+W~g~?gZQgXaKky&=7DB;9kIefJT7(0gVAo08IhS01to?I{bP{xDk|a6DXl7D4`lCp*kp`1}LE>D4`Z8;bu@mZBW83poCjN33WgTbwLTYffDM066%8zZU-gY0ZO<NlyDa)p#do2Zcsu)P{KW+gnK~=_kj``ffDWqB{T*lGyx?v1tl~CB|IRVPG9jm-pSwbDSRg1!1wX(91BOradOn0182nfakiX0EkV1`O0*d*NPE({v^6bHKhP`m5j{r#(VM@V5)dzpp0rqM8pT=TC<Yrv@p*3)yA7kbZV<)%ol!pA9_32CD39t!Id*H5f3>6BtQF;LjVPz9MfrZykGbH7y4ev)(iut814+^aNzxTb(hW({Jry>*;&;50zvEN*Ouk`(JQ!#wK=VLK0a^r#3eYkTR)AK4z5=ukWES9|Ky3lq1fmPjHqc&xc7X(w?~>uR!EoDRxa|Umrd{zn-ud4@X!kR>w2eM&BQ6DktBWwCi!r22Fr-UUx1`uSz?Fb&0M`Pl0ImaE54Zu(d^l8^0Of*Z0+bJy2~Z(eCP2ktnE;i7Wdc+Vmihf$b(%Okoq-p1`XSYln79!!aT8*qDq^A<Vxl@?q6QpL6Aq{a2iyz?)c%>6xb2L`#4Q-otr$`r45@DFmiq8?13)9d{eZ@RrhsOE2hw7qNeXU6Ox%Q+sEU}VhM1_1n5Ypf<5Cus-_c|3L!cxP(kVdLX|zwhy=Q<9r?1*4--TOJce;+)nsiD4{}JsGZcm0=B^vHeROXI9$=)1b@)SO^M;Ju%=*GX~(VhO^qZ{MVsb_NV++K0BC69qk9|t@ESO|C$@D$)_z%zhn0nY)R2P^`-09Xuo5%3b=Wxy+dR{^g9UI#1zya9L<@D|{0z&n7YfMtN?fOi2a0Pg`-0#*T51J(f60@eZ61KtO00Bi(o0&E6s0c-_q1AGAZ5bzP;W56eXPXV6+wgWx~d;$0p@D<=|zz)DSfSrI{fZc#^0eb-715N;r0geOq0`>v+0}cQV0uBMb0~`h%0UQN*m%zDz41n_h83CC9nE_b<SpnGq*#YMRasYAyashG!@&NJz@&WP#3IGZM3IPfOiU5iNiUEoPN&rd%N&!j($^gm&$^ps)DgY`1Dgi13(gRMyN~ZvV4-L=(pLGOu0`vs*0`vy-0rUm*1M~+B01N~S0t^NW0SpBU0}Ka@0E`5T0*nTX0gMHV1B?eu089i-0!#)>0Zau<155|Z0L%o;0?Y=?0n7!=1I!0306dzu*sCJdOsiRAscu@`I!g`H8rDN<n%1-~Qp>cKb(Nb<Z?<ky+qAZIms?D4G3RbI4S!r6(>j*U)itea=eXNUZ?ngwo@qUMT<V+Fw<qLw)7x#K++li$Jt=pZ-f2(CU8Z;0)6&4SfjuL4o8E2DN<-6z_MF^fdXGIX_nO{oi{w7j`|Jg2WZK9U%l)SJ+l$iJw6VP;O-!5E%hJ@esl6i2Oq<!O@_^|B_L@9s`k=io%}txz5@})D!rqXUrY-GFX=U2V-jdd)t?g}j$n+t5N7|USv8B@1w5=_ZcBbuYxwJQJZ|_P6(+;*mI+}L0_oS0)CtE3<O*`8vdD!$}TP=^6K4NR6i)j~ID_u>y+B)fG+RfHWchm0nzC3FBsBMrQraf$<^fc{ho1~X%FWW4=O?%rG>0{c*wn|^qzP3&Jnf9{}q`zr@`%ng$4zQ18py@#SSO%F6vQK2N>0tX*hL{eq&t$0SP}?rUOo!R$GTd~yeIX-EN7$D#(sZPKC8JD7+1E1KbhPb|F{Wee8yRal)^^G`({Z*-#+#0}-7>*+f_*C!O()tOnPfW2zL&|SlkJ2|F`Z(^WUA>@J1)~qr`cYaZaUre$qdsOwqItN&a?wE%XF3<l-Z`U?U2kdonzn0T+_LBSmv3|vm-L!biN&x1*QwkyT?o)vvb|!rjJ_&_k`&acAi^ky3jJZCrzKUOztVur!2F3+VpA5;+`>m#<IF+O`o-F?m5%vEW3N&^m#kqEizqXIou1TFIY~u*mSYwaxa>`Xt~`>rY~6@_p<5Bme;*v`ikXqubRGU`Q2-#uUP^2y6Njy&@C}tVujorrf*nb_onHaR>Zw!`j!=SZ=1et#oRll?^toS)O4wpaLY`WSxL9tbh(vs@0z}ArQHhC6;{T*XZoI%bt_F*S~<7Mbd{BNt4&v11-Hg@ja77OP1jl_x6X8(Rd(x5*IRn`zUljRQZ|@wuv4<pbfbyeWV*@BZ8qI(9b}8?7V9WmO}APn*=D-Udddf;A6PH>(DXy=EgzYFWPRjg(~qsMd}8{E^^;FcKehhyndxUXK(?E1w}JAx>E|{`zA*j52FsVGU)m7)%JeH6Dqov^ZNp@T=?)t%-<W=5BV?!PP8%t^On2ER*=@SpM$5OR-`W`2W4g!2%3jmGHcs}L?z8c--*mrCkOQU%Y@!@AJ!q5Ukm(_tEZ>=aXH(>`>0z5HM@)~{G&yQ|)TYZZ(_=P6j+-90nex5q_clvTn4YlNa?<pq&5={4rz}vQSMl@2d3Aois8{t1B%RlE{!yuFX;=J?ck*|93ZKb0@O^wc$HI|uoE$ahz!`CVoGs^0OVBQ~5^Y8c(w?*~ZB5J55A+IsM32#b^d@~vPt)&=0>%U*gz>`YVJtDS7-x(+#vmh-@yTdq>@t!W*Nk$;JTrj#!0ceIFmsqk%qr#>GmiPkY-DaSQ<=BSV&*h6ocYe|Cl`<z$P;7@atIlP{6e-N_mGLmOJpf>78#6uMs_3Dk@?7jWJPi$8I$};HYK-`Y00}}VRAAVntV<6CYO`h$@64=)&N!n)(2J#)(%z@))iJ6)*MzK)+1IY)+$ym)-hH!);Lx?)<0H5)<#xJ)=gGX)>Kwl)>~Fz)?!v>)@fF4)^JvI)^}EW)_$%8xGvx-fole?Ah@33>Vj(xt~|I7;i`md6s}mfe&K3{Ya6a~xbER9h-)IQkhosr>WOP9uB^Du;;M^lFs{hBKI3YQYd5asxUS<W4{JWI0Mpik^P{!m+-My+J6dDTjMksiqqXVOXx%zFTGLL9*1O}QweZ+zojf{PLywHs*TbW=_t0ovJ~&#l4~*9H{iC&h-)JAuJK7`kjP?)QO>l3)od)+E+=XyYl0Mq6REqX86{3Akxo8hmCfXmBiuO(=qJ34dXwOw7+K&~A_G$&9eO$h1kC!Lf|K*DIhB=~rWA<oInKjyPW{&ov8KZq_hG-AV9qrL*w|h9+2_K4f$p@kx^uB0!eLUKEpNMwld!ilt?r1l^Gur9zh)w~%icSc=h)xf-M<)xPMyC!RM<)^=MyD0qqLYj*(J9BK=mca#bULy=IyqSzovN&kPFz+-r!gy{lbYqxDbCX9gy-$(^ykg!WN1lrYV=xkqV!61+VoO%616xwrCJo7U_BR|Zaov7d_5JNiY<&z%y@o=(=>MsCy7<9eegZ6++G}YR<#F1c<{>Yljiuac?ca|x&6`tAGQc##VdC}TH?c&A>?@F4oWM0*eZl0uiPPNjSpLgQ00~T4u`%~?V%9HymE)74L)oWLY!Cbh_uCrZA19;${m$<_^@3_4PLpE_$wV%17Dv^yK<-GVSM;-U>sh#)L-#PJ`CV^<;?ZKhdlyQ@hUOZ4-9tpJmlxjL(U$*{pRC0?Gd6iv)9bNi)8Vd#dnpgUbFgclFe&2-(9kM&F-B$-)s2ea(K<*)47~pbNX{!F0Z+Kd&%uJx9=c%yyo#eC9l`KzL(_ln$P!^{9g0>K2pGI0pC{&dM)VtNg=O=e19qIwXh!`MZ6aA1Er|fqJEGR^IFUgmf~KE`yo=oYY9J8N_s8nhe;`~rTlOy?X|QYA!WRl@gt?I*Rp<;l=E87kCyUY%lk1>!D|ISRw{a}=*LMVua*3GsqD3~pCEto`X@h8F7SGRpCo_w`e#2`F7$e#pCT7|y~t0Mi@jd#r^zK=FY(jmQm>c#8S)pefAKTrGOw5US@Kt}fAzEFa<7;BIr2BJfAe$Y3a?j$z3AV){ypqWuk?Cl*r)!(>p#M-^(wDddGG$|^`HJ+ceU56eFpb0umAGrxof;$<1@Nzy<Y1xxhh_(_{{F#UjOa0xa+)L=d-%&y<YFLxf{IR;Iq3Mz24~0cQ<*x$>(rYy;k)(T{W-Od@fhrYjvO7)$m%w=W#W?*7SK@Ew8nFK6kU%n|*#)+iPuKz}@2Y7GKca>h)G%$kp*$#}{^Wz1H<b+-+WO^F>`ful0N}SKn)WU)<g9^>$yv-Qo2PU((&_^-f>P-R1QzU)nYB+Q64_cYD3tmvs%jHuUA(Jznqe<=wqr@AVbjeO~YL6<s5*jeI3{zt{VHW!KniW1rqN@!G_nl%`&r`cu-(YcntI0k02ubD2(G@jKqh-|;DYCf~sK@$DQ7N5*k-)SLrn#QAZyoI5Q+yU<Fs87)YA(z>)YEl)qtEA$aPM*q>9^esJ2zcUIL6O0hX3!{gz#K>ZtG3pqDj7Y{Oqm{ACNM>9!${F*_0OkX;gSo=YVIDE7m}AU1<{z_>xyejr-ZG1s)68(@JF}l$KxQCMkTu95WEAoX*@oOhCL%A9rN~)iF!CAMja*0OBM*`l$&qAC@aNer#&6$ZoZZp>?2eWzK&%JTmYSLT|5$2f^8aJ0naTf;rDi7oqorn8m!~4s9Y>)4p&H?un!9)EgDKB-dTuaD2B#UEbLTk?e_TeV8C^P;$!R8cj?3&cvwJK=x@K{Yhq%|Q?un2En$0Z?IicCzlOaR&eD_qy7tP_G4%wqQ-7_JVG?#leWR~W3&xJhGJns3Bb(+^L3OT6x+zTNiHNRUN@>2`A7elscLHAO~T`lBZ4w<Zl-76ulwTOE)WVse~uZ5h~V(#_809xEF34EX>+#7)%w4{48aD|p~Zw2Pi((diRBU;A26Ieydx}||*w47TO7)Q&y<$-^+f_pcxkydmo0yk+T_g-Kst?X8Y4SL!YzvG?!9iPHy@(p|+-_EgcWE>|)%{g#JoF8Y)xziG~3#~+((So!mtxH?e^7I3}LLbp%^dG%R-_q0cJEMRx!3aUT{IRz2f2_YPqQ`$dC9DD^tOg~l0VS*jC9DG_tOq5$4@%eoO4tZW*aS-03`*DnO4tfY*ak}Y0F>|{DB&Ye!pES5Pe2Kuf)YLhC2R*Jd=5(Z0+jG2DB&wm!q=dL9iW77KnXiR3A;cEyFm%xf)e(~2}!%+cf6Co<5T!dzJc%K+c_4FjN{~}IS0;&^W$tecUppWp_OPeT9Ednb!lr_o_?TL=p%ZJ{-Za4IVB)o{#fUjKh(|dkt8Q2NfJYnI3$T8Nzx%n&T*AbU-3KM$=~rQd?w#e+3gK96kuN<r2zW_MFltz2rIzBKwkk41u_fpU7)rAhXc_CI1*?tz|la0$#=<c4`aATFx;boL({JK9q;__9~_mRzU7Gg_`}2EQXu&7c?@Y0hV%l4v^aH3ip>Ko0W1Y911txu0K5lSiD#Y)l_tPrvNr{f%f1vmA^TIXP!6QvNjaE;r{vJ@=&IAidEyMb=)@1Hmc+y=#KdaE#2UoJTExUU#Kd|y;C(n?101js4%qZFG4a6}kBQ9~(iRM9D~7Z!b<0Qa^mf1wz&C)MfZc#^0ejM7Vpj@QAtqKMCe|P()*>d>Atu(R4#QIx{Bfx}(;hn(7L!SYoCpwh8mUfDxaF7}m$a*6$#>zF)SV%&QakGKjAUcYvq}s1Cc|AG4fiK1b6CFq1bcIU$y4}D3u8$hz4Mnm`o#Zx^iDiF^-K<)+pDzAR#kia3~lGmb`H*V4t|%;L1*cL&Oujn4!WUp&>fuv=aSBWqH~ZAor81GIcP6Q=b!^R2R+d_=!MQfZ*&g&pmWd{or8Yp9P~%$U;sJ?1JOAcgwDZWbPk4~b1)R0gJI|#3`gf+1Ud&J(K#4}&cSGO4#uE!FczJIap)Y3N9SMyItLTcIhcgb!DMs}rl4~$6`g}==p0N(=U@gp2Q$$*n1#;4Y;+FhpmQ)6or8Jk9Lz`OU;#P@kD_znUD7!?7oCF)=p3Af&Ot_W4l<#0kQtqWEa)6$Mdu(JItSU&IXEAkgB<7_<V5En7di*I(K*P2&Ou&u4)URMkRP3c0_YqRMCYIoItPW(IVgh8K~Z!LilK8*9G!y_=p2+p=b#ii2c^+DD1**HS#%D{p>t3kor4PK98^T-pb|O<mC-p!kIunKNje9o&^Zv7bPkf10k8NS@8s|J6h4!0;QRP?j)f!RI5}$0fivR#I9tx0mY`i|CEAP@q&;a}+M1T9ALteOh#sT==uP^To~GX!1&j$s2;+s(!&qWuG0qruj6p^u<CD?K*kvR$t{LTwd1e6ff!V=aVdgN8m{rU%W*qa6*~r{vrZR7t#ms4DIP;y^Pc9%ckSE9*<Pb6n`Gssl?jaMAm&j7&EHW7RjO<3PBlD35$%^DiFy`4_!P#EH@7XIjgMTgMK|pgr3qVUiD?n?&Lx47bwt#kLr9Z!V!FpD?cXrMG+t=(>q%nkJogp0S0^wL!2*<iXIMyA)vEvYqEr)PysU*U&Ws(TTR!AZodruPK*h&b;oJ)jb>Js5tI+qB?&T)xwtUZKd9UvTg5W=zM5RSEgaI7VSW33<@YYpMpLlBO&fpDxXgk$X>9P0?-SSJX_dO|qX3&OG95RUbMaI7zcWBni;>kr}B00_qhLO3=E!m+^+jtzluY$$|d!yp_R4&m4c2**Z3I5rBxvC$BYje&4%EQDj@ARHSH;n)NS$0kBJHVMM9$q<fBfpBapgk#en9Gec|*bE5AW<oeN3&OG45RT1(aBMDwWAh*!n-AgG0tm+*g>Y;Ygk!5A99sk7*jfn3)<HP79>THrAspKP;n+q9$2LJYwi&{)Ef9`vg>Y;egkv8-IQAigV;?~{_A!KGpFlYFDTHI6K{&P@!m-aK5srN!iE!*oNrYoxNg^EkS`y*d4oQS#-$)`H+bM}~Y?ma$vE7mg$G(+BIJQR;;n??*2**xHA{;v=iEzwAICd_CV;LYEI}gIKj1Z1xf^aM|gkxDC9LoyfST+d9vO_p_K7?aAARNmH;aDyR$8tkBmIuPIybzA%gK#WAgkuFD94iRnSRn|<3PU(n1j4bR5RMgdiEymAON3)3ARH?R;aDk`2**mhL^xK)CBm_?E)kBEbBS=Qyi0^*6<i`5tLPHpSS6PT$11x-IF{Ze!m*POj-7&VOk5%yGgtNW6~E)1{2iadXYvhvAK%WgaAX`ON6k5KMw}mK%em7Mv<t07o6&-_C#_3c)AIBKy+R++WAq=rN#D}b^gE+~F~JC7yfAtgON=bW8KaId$cSWoGFlnCjAX_&qnt6%3}8MmJD4lX9Oe<TiaExNWBxH4nVZa1<}I_BIn4}bzBBvD1!M;D1X+U|LPjCKkZs64WFqnsS&E!R1|y%5-N<!hKJp-0ksL|JB!7}k$*p8s@-A7JoJ@u$Uz5Gb<z#m9JXxPLfE9uDfz^VwgO!AJg;j<%hZTtRh}DU;ij|9Xj8%;_junsfkJXU1k(H8llU0;8l@*rtmerTFn3b7znpK-MoE4q*oz<STpDO{b3%E+)nt>|_t|zd%IJ>|7?fcua3YoK8{9hw*YZvXO+eCZq*3mw^Wwb|c9_`<wV}l?5ZJ)CE2Y8Zyr<7NxKTQ3rr9b|#a|&GeKLIQNpYk70{d9u'
)

FAMILY_STATES_B85 = (
    'c-rmVJx&`@6oAoZKw^ZODQRq6umEoWF+wR=MQB(=sz6wokyr#p7T_vk31EH<^CUzHWX-)kr-&j^MSOa?_l?Kt%9E?BvxoiFUw+;0mcD6$a5`BdYmha_8e|Q!M%J=M)*x$;HOLxS%NkjOtU=ZwYmhavmNl{lS%a)W*2r4c$Qon~vIbd$tdX^>ku}H~WDT-L*0M&{AZw5{$QopgtYwX?LDnE^_<uX=tfvRJC)W#EBWsW~$Qon~vPRY*Ymha_8f1;EWsR&s)*x$;HOLxSgRDW;AZw5{vX(Wn23dowLDnE^WDT+gS%a)W*2r4c$Qon~vIbd$tdTXy8e|Q!23fORy44@Q*ID0>`#)a%jPehe`CZb_`t7uyG%u%h+qE~R&p$q#%9`L=KMf({s6&XX`6BC?tdX^>8TQIp--Lu;8C$<&S-T0r$_OEc5Lpxbw4Rh|2pQcOLWq7^PfGRhd~_H7CdA4p>rxFNqdgaVWXXCaYn;}yX3#5R^--tJN1X_twZ}0e970a6|GKv(-w@*7nuIH(dutMA?Sc<k%bGY@mqb|`LadDLt;u&<yWk_?Y3*?gDNpNaWlZpjuGw1FuU}U7p2)&%jjUzOV26;1E2ANVPqTItLYl1Wn~)Dfh?@}1)`k#d?X+fdE8{HD%80D3j93|+))+#pjL6z)joBK^)@;#f?Qsl-5QsB`6hjD3YZ#WDkEiw9o9FY@o9FFW^Y71|tjU-4armsQjIwTC{sX)9_k@(j;}~QuYh*2JHkb8W*2K^H{i`LH<NnHcc@#ZsE2FH-a<_L{ca6s}gwMKJ^s_GKN3tgTY`v^z>+=gk2>FH(D<iU&HG|E%l{K=KHA7w*ebk9<$l3=}i9dw6w<h6f?cSQaE29fO5@zit1X;@(S(~ld?8@lg8Y`nAgb=57{dUX`Z^sb+w0?aY(|R0(tYwX?WzA-@t}ghB3qIm!?IwggS=Toqt(y?c)=q0=Eo-cdvgTV>MxWrr%4lW8Z0)qhY%Ocd*6`(Q?Q7dfID{NJt;sTk%)QG<sv)F$m+{iq-{7<!9$9arM<q*r%>'
)

SSTAR_PACKED_B85 = "c-nJd00PFHP9NCWI1k=met??+705A+f>AK!002I|1#<"


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    matches = [
        node.value
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        )
    ]
    if len(matches) != 1:
        return None
    try:
        return ast.literal_eval(matches[0])
    except (TypeError, ValueError):
        return None


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_certificate() -> dict[str, object]:
    payloads = {
        path: (ROOT / path).read_bytes()
        for path in AUDIT_INPUT_PATHS
        if (ROOT / path).is_file()
    }
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads.items()
    }
    actual_blobs = {
        path: git_blob_sha(payload)
        for path, payload in payloads.items()
    }
    trees = {
        path: ast.parse(payload, filename=path)
        for path, payload in payloads.items()
    }
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    imports = set()
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            imports.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imports.add(node.module.split(".")[0])
    direct_frontier_imports = tuple(
        sorted(name for name in imports if name.startswith("frontier_cycle"))
    )
    stdlib_roots = set(sys.stdlib_module_names) | {"__future__"}
    basis = {
        "cycle819": {
            "build_family", "advance_population", "verify_transient",
            "verify_cycle",
        } <= function_names(trees[AUDIT_INPUT_PATHS[1]]),
        "cycle820": {
            "build_family", "evolve_nine", "population_state_at_entry",
            "mechanism_candidates",
        } <= function_names(trees[AUDIT_INPUT_PATHS[2]]),
        "cycle822_copy": {
            "build_family", "evolve_sstar_pair", "sstar_anatomy",
            "entry_predictors", "basin_census",
        } <= function_names(trees[AUDIT_INPUT_PATHS[3]]),
    }
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_INPUT_PATHS_literal":
            literal_assignment(self_tree, "AUDIT_INPUT_PATHS")
            == AUDIT_INPUT_PATHS,
        "existing_worktree_relative": (
            len(payloads) == len(AUDIT_INPUT_PATHS)
            and all(
                not Path(path).is_absolute() and (ROOT / path).is_file()
                for path in AUDIT_INPUT_PATHS
            )
        ),
        "plain_reading_named_files": len(AUDIT_INPUT_PATHS),
        "maximum_named_files": 6,
        "sha256": actual_sha,
        "expected_sha256": EXPECTED_SHA256,
        "git_blobs": actual_blobs,
        "expected_git_blobs": EXPECTED_GIT_BLOBS,
        "tracked_cycle822_copy_sha256": actual_sha.get(AUDIT_INPUT_PATHS[3]),
        "self_sha256": sha256(self_payload).hexdigest(),
        "self_git_blob": git_blob_sha(self_payload),
        "text_AST_only_paths": TEXT_AST_ONLY_PATHS,
        "AST_basis": basis,
        "blocked_modules": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(IMPORT_FIREWALL.hits),
        "direct_frontier_imports": direct_frontier_imports,
        "stdlib_import_roots": tuple(sorted(imports)),
        "stdlib_only": imports <= stdlib_roots,
    }
    result["pass"] = (
        result["AUDIT_INPUT_PATHS_literal"]
        and result["existing_worktree_relative"]
        and len(AUDIT_INPUT_PATHS) <= 6
        and actual_sha == EXPECTED_SHA256
        and actual_blobs == EXPECTED_GIT_BLOBS
        and all(basis.values())
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
        and not direct_frontier_imports
        and result["stdlib_only"]
    )
    return result


def separated_pairs() -> tuple[tuple[int, int], ...]:
    return tuple(
        (left, right)
        for left, right in combinations(range(RING_STATIONS), 2)
        if min(
            (right - left) % RING_STATIONS,
            (left - right) % RING_STATIONS,
        ) > 1
    )


def state_sha256(state: int) -> str:
    """Cycle-822 identity convention: hash one byte per Boolean bit."""
    return sha256(bytes(
        (state >> wire) & 1 for wire in range(STATE_BITS)
    )).hexdigest()


def packed_sha256(state: int) -> str:
    return sha256(state.to_bytes(STATE_BYTES, "little")).hexdigest()


def active_indices(state: int) -> tuple[int, ...]:
    rows = []
    value = state
    while value:
        bit = value & -value
        rows.append(bit.bit_length() - 1)
        value ^= bit
    return tuple(rows)


def decode_fixtures() -> dict[str, object]:
    gate_raw = zlib.decompress(base64.b85decode(GATE_CONSTANTS_B85))
    family_raw = zlib.decompress(base64.b85decode(FAMILY_STATES_B85))
    sstar_raw = zlib.decompress(base64.b85decode(SSTAR_PACKED_B85))
    lengths = struct.unpack("<11H", gate_raw[:22])
    offset = 22
    macros = []
    for length in lengths:
        rows = []
        for _index in range(length):
            rows.append(struct.unpack("<BHHH", gate_raw[offset:offset + 7]))
            offset += 7
        macros.append(tuple(rows))
    positions = separated_pairs()
    keys = tuple(sorted(
        (event, positions0)
        for event in range(2 * FIXTURE_BANKS)
        for positions0 in positions
    ))
    states = {}
    for index, key in enumerate(keys):
        start = index * STATE_BYTES
        states[key] = int.from_bytes(
            family_raw[start:start + STATE_BYTES], "little"
        )
    sstar = int.from_bytes(sstar_raw, "little")
    result = {
        "macros": tuple(macros),
        "positions": positions,
        "keys": keys,
        "states": states,
        "sstar": sstar,
        "certificate": {
            "fixture_import":
                "supplied mechanical serialization of the tracked "
                "Cycle-822 build_family and SHA-pinned Cycle-719 "
                "mapped_macro outputs",
            "fixture_import_status":
                "DISCLOSED_CONDITIONAL_INPUT: the payload hashes prevent "
                "drift but do not independently prove the extraction from "
                "the source texts",
            "cycle822_copy_sha256": EXPECTED_SHA256[AUDIT_INPUT_PATHS[3]],
            "gate_raw_bytes": len(gate_raw),
            "gate_raw_sha256": sha256(gate_raw).hexdigest(),
            "expected_gate_raw_sha256": EXPECTED_GATE_RAW_SHA256,
            "family_raw_bytes": len(family_raw),
            "family_raw_sha256": sha256(family_raw).hexdigest(),
            "expected_family_raw_sha256": EXPECTED_FAMILY_RAW_SHA256,
            "sstar_packed_bytes": len(sstar_raw),
            "sstar_packed_sha256": sha256(sstar_raw).hexdigest(),
            "expected_sstar_packed_sha256": EXPECTED_SSTAR_PACKED_SHA256,
            "macro_gate_counts": lengths,
            "macro_gates": sum(lengths),
            "positions": len(positions),
            "family_states": len(states),
            "state_bits": STATE_BITS,
            "pass": (
                offset == len(gate_raw)
                and sha256(gate_raw).hexdigest()
                == EXPECTED_GATE_RAW_SHA256
                and len(family_raw) == FAMILY_SIZE * STATE_BYTES
                and sha256(family_raw).hexdigest()
                == EXPECTED_FAMILY_RAW_SHA256
                and len(sstar_raw) == STATE_BYTES
                and sha256(sstar_raw).hexdigest()
                == EXPECTED_SSTAR_PACKED_SHA256
                and sum(lengths) == GATE_COUNT
                and len(positions) == 44
                and len(states) == FAMILY_SIZE
                and sstar.bit_length() <= STATE_BITS
            ),
        },
    }
    return result


def build_words(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    positions: tuple[tuple[int, int], ...],
) -> dict[tuple[int, int], tuple[tuple[int, int, int, int], ...]]:
    words = {}
    for positions0 in positions:
        rows = []
        for step in range(RING_STATIONS):
            live = {
                (positions0[0] + step) % RING_STATIONS,
                (positions0[1] + step) % RING_STATIONS,
            }
            for station, macro in enumerate(macros):
                if station in live:
                    rows.extend(macro)
        words[positions0] = tuple(rows)
    return words


def apply_word(
    state: int,
    word: tuple[tuple[int, int, int, int], ...],
    *,
    reverse: bool = False,
) -> int:
    rows = reversed(word) if reverse else word
    for kind, first, second, third in rows:
        if kind == 0:
            state ^= 1 << first
        elif kind == 1:
            state ^= ((state >> first) & 1) << second
        elif kind == 2:
            state ^= (
                ((state >> first) & 1)
                & ((state >> second) & 1)
            ) << third
        else:
            raise ValueError(("unknown gate kind", kind))
    return state


def local_involution_certificate() -> dict[str, object]:
    rows = failures = 0
    for kind, width, first, second, third in (
        (0, 1, 0, 0, 0),
        (1, 2, 0, 1, 0),
        (2, 3, 0, 1, 2),
    ):
        word = ((kind, first, second, third),)
        for state in range(1 << width):
            rows += 1
            failures += apply_word(apply_word(state, word), word) != state
    return {
        "truth_table_rows": rows,
        "failures": failures,
        "X_inverse": "x_t(before)=x_t(after) XOR 1",
        "CNOT_inverse":
            "x_t(before)=x_t(after) XOR x_c(after); control unchanged",
        "TOF_inverse":
            "x_t(before)=x_t(after) XOR "
            "(x_c1(after) AND x_c2(after)); controls unchanged",
        "composition_inverse_order":
            "reverse the landed gate row; every primitive is self-inverse",
        "pass": rows == 14 and failures == 0,
    }


def build_masked_schedule(
    macros: tuple[tuple[tuple[int, int, int, int], ...], ...],
    lane_keys: tuple[tuple[int, tuple[int, int]], ...],
) -> tuple[tuple[int, int, int, int, int], ...]:
    rows = []
    for step in range(RING_STATIONS):
        for station, macro in enumerate(macros):
            lane_mask = sum(
                1 << lane_index
                for lane_index, key in enumerate(lane_keys)
                if station in {
                    (key[1][0] + step) % RING_STATIONS,
                    (key[1][1] + step) % RING_STATIONS,
                }
            )
            if lane_mask:
                rows.extend(
                    (kind, first, second, third, lane_mask)
                    for kind, first, second, third in macro
                )
    return tuple(rows)


def bit_slice(states: tuple[int, ...]) -> list[int]:
    columns = [0] * STATE_BITS
    for lane_index, state in enumerate(states):
        value = state
        while value:
            bit = value & -value
            columns[bit.bit_length() - 1] |= 1 << lane_index
            value ^= bit
    return columns


def un_slice(columns: list[int], lane_index: int) -> int:
    state = 0
    for wire, column in enumerate(columns):
        state |= ((column >> lane_index) & 1) << wire
    return state


def apply_masked(
    columns: list[int],
    schedule: tuple[tuple[int, int, int, int, int], ...],
) -> None:
    for kind, first, second, third, lane_mask in schedule:
        if kind == 0:
            columns[first] ^= lane_mask
        elif kind == 1:
            columns[second] ^= columns[first] & lane_mask
        else:
            columns[third] ^= (
                columns[first] & columns[second] & lane_mask
            )


def matching_mask(
    columns: list[int],
    target: int,
    lane_mask: int,
    signature_wires: tuple[int, ...],
) -> int:
    candidates = lane_mask
    for wire in signature_wires:
        column = columns[wire] & lane_mask
        candidates &= column if (target >> wire) & 1 else lane_mask ^ column
        if not candidates:
            return 0
    for wire in range(STATE_BITS):
        column = columns[wire] & lane_mask
        candidates &= column if (target >> wire) & 1 else lane_mask ^ column
        if not candidates:
            return 0
    return candidates


def lane_indices(mask: int) -> tuple[int, ...]:
    rows = []
    while mask:
        bit = mask & -mask
        rows.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(rows)


def forward_lawful_census(
    fixtures: dict[str, object],
    target: int,
) -> dict[str, object]:
    keys = fixtures["keys"]
    states = fixtures["states"]
    macros = fixtures["macros"]
    assert isinstance(keys, tuple)
    assert isinstance(states, dict)
    assert isinstance(macros, tuple)
    replay_key = NINE_KEYS[0]
    lane_keys = keys + (replay_key,)
    lane_states = tuple(states[key] for key in keys) + (states[replay_key],)
    columns = bit_slice(lane_states)
    schedule = build_masked_schedule(macros, lane_keys)
    primary_mask = (1 << len(keys)) - 1
    key_index = {key: index for index, key in enumerate(keys)}
    replay_index = len(keys)
    snapshot_times = set(
        range(MECHANISM_ENTRY - TREE_DEPTH, MECHANISM_ENTRY + 1)
    )
    snapshots: dict[int, dict[object, int]] = {}
    exact_hits = []
    target_active = active_indices(target)
    spread = tuple(sorted(set(
        index * (STATE_BITS - 1) // 191
        for index in range(192)
    )))
    signature = tuple(sorted(set(target_active + spread)))

    for update in range(MECHANISM_ENTRY + 1):
        if update in snapshot_times:
            snapshots[update] = {
                key: un_slice(columns, key_index[key])
                for key in NINE_KEYS
            }
            snapshots[update]["replay"] = un_slice(columns, replay_index)
        matches = matching_mask(
            columns, target, primary_mask, signature
        )
        exact_hits.extend(
            (update, keys[index]) for index in lane_indices(matches)
        )
        if update < MECHANISM_ENTRY:
            apply_masked(columns, schedule)

    entry_states = tuple(
        snapshots[MECHANISM_ENTRY][key] for key in NINE_KEYS
    )
    replay_exact = all(
        snapshots[update]["replay"]
        == snapshots[update][replay_key]
        for update in snapshot_times
    )
    expected_hits = tuple(
        (MECHANISM_ENTRY, key) for key in NINE_KEYS
    )
    result = {
        "snapshots": snapshots,
        "public": {
            "scope": "all 176 lawful t=0 states through the first S* hit",
            "updates": MECHANISM_ENTRY,
            "bit_sliced_lanes": len(lane_keys),
            "primary_lanes": len(keys),
            "duplicate_determinism_lanes": 1,
            "masked_gate_rows_per_update": len(schedule),
            "signature_prefilter_wires": len(signature),
            "exact_hit_metric": "full 5815-bit tuple equality",
            "all_exact_hits_through_horizon": tuple(exact_hits),
            "expected_exact_hits": expected_hits,
            "first_exact_hit_depth":
                min((update for update, _key in exact_hits), default=None),
            "first_exact_hit_keys": tuple(
                key for update, key in exact_hits
                if update == min(
                    (time for time, _key in exact_hits),
                    default=-1,
                )
            ),
            "nine_entry_exact_tuple_equal":
                all(state == entry_states[0] for state in entry_states[1:]),
            "nine_entry_state_sha256":
                tuple(state_sha256(state) for state in entry_states),
            "entrant_reconstruction_key": NINE_KEYS[0],
            "entrant_t0_state_sha256":
                state_sha256(states[NINE_KEYS[0]]),
            "entrant_t14739_state_sha256":
                state_sha256(entry_states[0]),
            "replay_exact_at_t14731_through_t14739": replay_exact,
        },
    }
    result["public"]["pass"] = (
        tuple(exact_hits) == expected_hits
        and result["public"]["first_exact_hit_depth"] == MECHANISM_ENTRY
        and entry_states[0] == target
        and state_sha256(entry_states[0]) == EXPECTED_SSTAR_SHA256
        and replay_exact
    )
    return result


def one_step_certificate(
    target: int,
    words: dict[
        tuple[int, int], tuple[tuple[int, int, int, int], ...]
    ],
) -> dict[str, object]:
    classes: dict[int, list[tuple[int, int]]] = defaultdict(list)
    failures = 0
    for positions0, word in words.items():
        predecessor = apply_word(target, word, reverse=True)
        classes[predecessor].append(positions0)
        failures += apply_word(predecessor, word) != target
    rows = tuple(sorted(
        (
            {
                "preimage_state_sha256": state_sha256(state),
                "packed_sha256": packed_sha256(state),
                "position_labels": tuple(labels),
                "label_multiplicity": len(labels),
            }
            for state, labels in classes.items()
        ),
        key=lambda row: (
            row["label_multiplicity"],
            row["position_labels"],
        ),
    ))
    local = local_involution_certificate()
    result = {
        "state_space": "{0,1}^5815",
        "external_word_labels": tuple(words),
        "constraint_definition":
            "P_p={x in {0,1}^5815 : F_p(x)=S*}; "
            "P=union over the 44 separated position pairs p",
        "constraint_elimination":
            "apply the displayed local inverse equations in reverse landed "
            "gate order; this gives the sole solution x=F_p^{-1}(S*)",
        "local_inverse_constraints": local,
        "fixed_position_word_preimage_count": 1,
        "position_labeled_preimage_count": len(words),
        "event_and_position_labeled_preimage_count":
            2 * FIXTURE_BANKS * len(words),
        "distinct_5815_bit_data_preimage_count": len(classes),
        "label_class_multiplicities":
            tuple(sorted(len(labels) for labels in classes.values())),
        "preimage_classes": rows,
        "forward_recheck_failures": failures,
        "determinism_scope":
            "F_p is deterministic and bijective for fixed p; projecting "
            "away p permits collisions between different F_p",
        "pass": (
            local["pass"]
            and len(words) == 44
            and all(len(word) == WORD_GATE_COUNT for word in words.values())
            and len(classes) == 14
            and tuple(sorted(map(len, classes.values())))
            == (1, 1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 7, 8, 9)
            and failures == 0
        ),
    }
    return result


def state_set_digest(states: set[int]) -> str:
    hasher = sha256()
    for state in sorted(states):
        hasher.update(state.to_bytes(STATE_BYTES, "little"))
    return hasher.hexdigest()


def preimage_tree_certificate(
    target: int,
    words: dict[
        tuple[int, int], tuple[tuple[int, int, int, int], ...]
    ],
) -> tuple[dict[str, object], dict[int, set[int]]]:
    levels = {0: {target}}
    rows = [{
        "depth": 0,
        "fixed_position_labeled_nodes": 1,
        "projected_unique_state_count": 1,
        "projected_unique_state_count_status": "EXACT_MATERIALIZED",
        "state_set_sha256": state_set_digest(levels[0]),
        "characterization": "S_0={S*}",
    }]
    rays = {positions0: target for positions0 in words}
    for depth in range(1, TREE_DEPTH + 1):
        rays = {
            positions0: apply_word(
                rays[positions0], word, reverse=True
            )
            for positions0, word in words.items()
        }
        current = set(rays.values())
        levels[depth] = current
        classes: dict[int, list[tuple[int, int]]] = defaultdict(list)
        for positions0, state in rays.items():
            classes[state].append(positions0)
        rows.append({
            "depth": depth,
            "fixed_position_labeled_nodes": len(rays),
            "event_and_position_labeled_nodes":
                2 * FIXTURE_BANKS * len(rays),
            "projected_unique_state_count": len(current),
            "projected_unique_state_count_status": "EXACT_MATERIALIZED",
            "state_set_sha256": state_set_digest(current),
            "projected_position_classes": tuple(sorted(
                (
                    {
                        "state_sha256": state_sha256(state),
                        "position_labels": tuple(labels),
                        "label_multiplicity": len(labels),
                    }
                    for state, labels in classes.items()
                ),
                key=lambda row: (
                    row["label_multiplicity"],
                    row["position_labels"],
                ),
            )),
            "characterization":
                "S_d={F_p^{-d}(S*) : p is one of the 44 separated "
                "pairs}; the same p is retained at every reverse step",
        })
    exact_counts = tuple(
        len(levels[depth]) for depth in range(TREE_DEPTH + 1)
    )
    result = {
        "declared_depth": TREE_DEPTH,
        "tree_shape":
            "one projected root with 44 fixed-position labeled reverse "
            "rays; after p is selected it never changes",
        "fixed_position_rays": len(words),
        "switching_position_words_between_depths_allowed": False,
        "depth_rows": tuple(rows),
        "exact_materialized_counts": exact_counts,
        "all_depths_materialized_exactly": True,
        "pass": (
            TREE_DEPTH >= 8
            and exact_counts == (1, 14, 18, 21, 16, 18, 26, 26, 25)
            and all(
                row["fixed_position_labeled_nodes"] == 44
                for row in rows[1:]
            )
        ),
    }
    return result, levels


def partition_keys(
    states: tuple[int, ...],
) -> tuple[tuple[tuple[int, tuple[int, int]], ...], ...]:
    groups: dict[int, list[tuple[int, tuple[int, int]]]] = {}
    for key, state in zip(NINE_KEYS, states):
        groups.setdefault(state, []).append(key)
    return tuple(
        tuple(group)
        for _state, group in sorted(
            groups.items(),
            key=lambda item: (item[1][0], len(item[1])),
        )
    )


def partition_nodes(
    states: tuple[int, ...],
) -> tuple[dict[str, object], ...]:
    groups: dict[int, list[tuple[int, tuple[int, int]]]] = {}
    for key, state in zip(NINE_KEYS, states):
        groups.setdefault(state, []).append(key)
    return tuple(
        {
            "node_state_sha256": state_sha256(state),
            "keys": tuple(group),
            "key_count": len(group),
        }
        for state, group in sorted(
            groups.items(),
            key=lambda item: (item[1][0], len(item[1])),
        )
    )


def partition_refines(
    finer: tuple[tuple[tuple[int, tuple[int, int]], ...], ...],
    coarser: tuple[tuple[tuple[int, tuple[int, int]], ...], ...],
) -> bool:
    coarse_blocks = tuple(frozenset(group) for group in coarser)
    return all(
        any(frozenset(group) <= block for block in coarse_blocks)
        for group in finer
    )


def partition_relation(
    before: tuple[tuple[tuple[int, tuple[int, int]], ...], ...],
    after: tuple[tuple[tuple[int, tuple[int, int]], ...], ...],
) -> str:
    if before == after:
        return "UNCHANGED"
    if partition_refines(after, before):
        return "SPLIT_TO_FINER"
    if partition_refines(before, after):
        return "COALESCE_TO_COARSER"
    return "INCOMPARABLE_REARRANGEMENT"


def varying_wires(states: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        wire for wire in range(STATE_BITS)
        if len({(state >> wire) & 1 for state in states}) > 1
    )


def trajectory_and_mechanism_certificates(
    target: int,
    words: dict[
        tuple[int, int], tuple[tuple[int, int, int, int], ...]
    ],
    snapshots: dict[int, dict[object, int]],
    levels: dict[int, set[int]],
    all_keys: tuple[tuple[int, tuple[int, int]], ...],
) -> tuple[
    dict[str, object], dict[str, object], dict[str, object]
]:
    reverse_states = [target] * len(NINE_KEYS)
    rows = []
    for depth in range(TREE_DEPTH + 1):
        if depth:
            reverse_states = [
                apply_word(state, words[key[1]], reverse=True)
                for key, state in zip(NINE_KEYS, reverse_states)
            ]
        states = tuple(reverse_states)
        observed = tuple(
            snapshots[MECHANISM_ENTRY - depth][key]
            for key in NINE_KEYS
        )
        varying = varying_wires(states)
        partition = partition_keys(states)
        rows.append({
            "depth": depth,
            "forward_time": MECHANISM_ENTRY - depth,
            "distinct_nine_state_nodes": len(set(states)),
            "branch_partition": partition,
            "partition_nodes": partition_nodes(states),
            "shared_state_groups": tuple(
                group for group in partition if len(group) > 1
            ),
            "shared_pair_count": sum(
                len(group) * (len(group) - 1) // 2
                for group in partition
            ),
            "varying_wire_indices": varying,
            "key_distinguishing_wire_count": len(varying),
            "equal_across_nine_wire_count": STATE_BITS - len(varying),
            "state_sha256_by_key":
                tuple(state_sha256(state) for state in states),
            "constant_word_path_labels":
                tuple((key, (key[1],) * depth) for key in NINE_KEYS),
            "independent_forward_snapshot_exact": states == observed,
            "materialized_tree_membership":
                all(state in levels[depth] for state in states),
        })
    postroot = tuple(
        apply_word(target, words[key[1]]) for key in NINE_KEYS
    )
    selected = tuple(
        key for key in all_keys
        if (
            key[0] == 0
            and 0 not in key[1]
            and min(
                (key[1][1] - key[1][0]) % RING_STATIONS,
                (key[1][0] - key[1][1]) % RING_STATIONS,
            ) == 5
        )
    )
    partition_sequence = tuple(
        row["branch_partition"] for row in rows
    )
    occupancy = tuple(
        row["distinct_nine_state_nodes"] for row in rows
    )
    shared_pair_counts = tuple(
        row["shared_pair_count"] for row in rows
    )
    positive_depth_collision_depths = tuple(
        row["depth"] for row in rows[1:]
        if row["shared_state_groups"]
    )
    all_nine_merge_depths = tuple(
        row["depth"] for row in rows
        if row["distinct_nine_state_nodes"] == 1
    )
    collision_map = {
        "version": 2,
        "scope": "nine actual fixed-position trajectories",
        "claim":
            "Exact partition by shared 5815-bit projected state at every "
            "reverse depth 0..8.",
        "v1_retraction":
            "RETRACTED: the nine do not merge only at depth 0 under the "
            "pairwise/shared-state meaning.  Pairwise projected collisions "
            "occur at every positive depth 1..8.  Only the common merger of "
            "all nine is confined to depth 0.",
        "depth_rows": tuple(rows),
        "full_partition_sequence_depth_0_through_8": partition_sequence,
        "node_occupancy_counts_depth_0_through_8": occupancy,
        "shared_pair_counts_depth_0_through_8": shared_pair_counts,
        "positive_depth_collision_depths":
            positive_depth_collision_depths,
        "positive_depth_shared_state_groups": tuple(
            (
                row["depth"],
                row["shared_state_groups"],
            )
            for row in rows[1:]
        ),
        "all_forward_snapshot_checks_exact":
            all(row["independent_forward_snapshot_exact"] for row in rows),
        "all_materialized_memberships_exact":
            all(
                row["materialized_tree_membership"] is True
                for row in rows
            ),
        "all_nine_common_merger_depths": all_nine_merge_depths,
        "maximum_distinct_nine_nodes_through_D": max(
            row["distinct_nine_state_nodes"] for row in rows
        ),
    }
    collision_map["pass"] = (
        collision_map["all_forward_snapshot_checks_exact"]
        and collision_map["all_materialized_memberships_exact"]
        and partition_sequence == EXPECTED_NINE_KEY_PARTITIONS
        and occupancy == EXPECTED_NINE_KEY_OCCUPANCY
        and shared_pair_counts == EXPECTED_SHARED_PAIR_COUNTS
        and positive_depth_collision_depths
        == tuple(range(1, TREE_DEPTH + 1))
        and all_nine_merge_depths == (0,)
    )
    transition_rows = []
    for before_depth in range(TREE_DEPTH, 0, -1):
        after_depth = before_depth - 1
        before = partition_sequence[before_depth]
        after = partition_sequence[after_depth]
        relation = partition_relation(before, after)
        transition_rows.append({
            "from_depth": before_depth,
            "from_forward_time": MECHANISM_ENTRY - before_depth,
            "to_depth": after_depth,
            "to_forward_time": MECHANISM_ENTRY - after_depth,
            "relation": relation,
            "from_partition": before,
            "to_partition": after,
            "dissolved_blocks": tuple(
                group for group in before if group not in after
            ),
            "formed_blocks": tuple(
                group for group in after if group not in before
            ),
        })
    forward_relations = tuple(
        row["relation"] for row in transition_rows
    )
    hierarchy = {
        "version": 2,
        "scope":
            "partition sequence from reverse depth 8 to 0, equivalently "
            "forward times t=14731 through t=14739",
        "full_partition_sequence_depth_8_through_0":
            tuple(reversed(partition_sequence)),
        "node_occupancy_depth_8_through_0":
            tuple(reversed(occupancy)),
        "transition_rows": tuple(transition_rows),
        "transition_relations_depth_8_through_0": forward_relations,
        "monotone_coarsening_toward_depth_0": all(
            relation in {"UNCHANGED", "COALESCE_TO_COARSER"}
            for relation in forward_relations
        ),
        "ruling":
            "NONMONOTONE: the approach contains exact subgroup splits "
            "(8->7 and 4->3), unchanged stages, and coalescences.  It is a "
            "hierarchical collision profile, not a monotone partition "
            "coarsening.",
        "split_transitions": tuple(
            (row["from_depth"], row["to_depth"])
            for row in transition_rows
            if row["relation"] == "SPLIT_TO_FINER"
        ),
        "unchanged_transitions": tuple(
            (row["from_depth"], row["to_depth"])
            for row in transition_rows
            if row["relation"] == "UNCHANGED"
        ),
        "coalescence_transitions": tuple(
            (row["from_depth"], row["to_depth"])
            for row in transition_rows
            if row["relation"] == "COALESCE_TO_COARSER"
        ),
        "final_tick": {
            "transition": (1, 0),
            "predecessor_partition": partition_sequence[1],
            "predecessor_distinct_nodes": occupancy[1],
            "image_partition": partition_sequence[0],
            "image_distinct_nodes": occupancy[0],
            "all_nine_one_state": partition_sequence[0] == (NINE_KEYS,),
            "reading":
                "The final tick completes synchronization by coalescing "
                "the remaining three projected nodes into the one all-nine "
                "S* node.",
        },
    }
    hierarchy["pass"] = (
        collision_map["pass"]
        and forward_relations == EXPECTED_FORWARD_PARTITION_RELATIONS
        and not hierarchy["monotone_coarsening_toward_depth_0"]
        and hierarchy["split_transitions"] == ((8, 7), (4, 3))
        and hierarchy["unchanged_transitions"] == ((7, 6), (6, 5))
        and hierarchy["coalescence_transitions"]
        == ((5, 4), (3, 2), (2, 1), (1, 0))
        and hierarchy["final_tick"]["all_nine_one_state"]
    )
    reverse_varying = tuple(
        row["key_distinguishing_wire_count"] for row in rows
    )
    full_level_rows = []
    for depth in range(TREE_DEPTH + 1):
        level_states = tuple(levels[depth])
        varying = varying_wires(level_states)
        full_level_rows.append({
            "depth": depth,
            "projected_state_count": len(level_states),
            "varying_wire_indices": varying,
            "varying_wire_count": len(varying),
            "forced_equal_wire_count": STATE_BITS - len(varying),
            "forced_equal_wire_characterization":
                "all wire indices 0..5814 except varying_wire_indices",
        })
    mechanism = {
        "classification":
            "NONMONOTONE_HIERARCHICAL_PARAMETERIZED_BIJECTION_"
            "SYNCHRONIZATION_NOT_SINGLE_MAP_ATTRACTION",
        "exact_reading":
            "Scoped to these nine data trajectories, partial synchronization "
            "is present throughout the funnel approach as exact shared-state "
            "subgroups.  Those subgroups split as well as coalesce, so the "
            "hierarchical profile is nonmonotone.  At t=14738 the nine "
            "projected data states occupy three nodes: 5800 of 5815 wires "
            "are common and 15 distinguish the nodes.  The key-specific "
            "final tick maps those three predecessors to the same S*, "
            "erasing the last differences and completing synchronization.  "
            "Retaining each position parameter keeps its update bijective; "
            "projecting the parameter away permits the collisions.",
        "collision_correction":
            "V1's pairwise depth-0-only merger wording is retracted.  "
            "Positive-depth shared projected states occur at all depths "
            "1..8; depth 0 is special only as the all-nine common state.",
        "hierarchical_profile": {
            "partition_transition_relations":
                hierarchy["transition_relations_depth_8_through_0"],
            "monotone_coarsening_toward_depth_0":
                hierarchy["monotone_coarsening_toward_depth_0"],
            "ruling": hierarchy["ruling"],
        },
        "full_fixed_position_preimage_levels": tuple(full_level_rows),
        "forced_equal_scope":
            "within each exact 44-ray projected level, not over arbitrary "
            "states satisfying any broader dynamical condition",
        "reverse_depth_key_distinguishing_counts": reverse_varying,
        "forward_t14731_through_t14739_key_distinguishing_counts":
            tuple(reversed(reverse_varying)),
        "progressive_monotone_erasure": all(
            left >= right
            for left, right in zip(
                reversed(reverse_varying),
                tuple(reversed(reverse_varying))[1:],
            )
        ),
        "last_tick": {
            "predecessor_distinct_nodes": rows[1][
                "distinct_nine_state_nodes"
            ],
            "predecessor_varying_wire_indices":
                rows[1]["varying_wire_indices"],
            "predecessor_varying_wire_count":
                rows[1]["key_distinguishing_wire_count"],
            "image_distinct_nodes": rows[0]["distinct_nine_state_nodes"],
            "image_varying_wire_count":
                rows[0]["key_distinguishing_wire_count"],
            "status": "HOLDS_EXACTLY",
        },
        "after_Sstar": {
            "distinct_nine_images_at_t14740": len(set(postroot)),
            "key_distinguishing_wire_count": len(varying_wires(postroot)),
            "Sstar_is_common_fixed_point": len(set(postroot)) == 1
                and postroot[0] == target,
        },
        "entry_predicate": {
            "statement":
                "event=0 AND origin absent AND maximum cyclic separation=5",
            "selected_keys": selected,
            "equals_exact_nine": selected == NINE_KEYS,
            "reverse_feasibility_connection":
                "NONE: every one of the 44 position words has a unique "
                "one-step preimage because it is bijective; event does not "
                "enter the update word.  The predicate selects lawful "
                "forward histories, not unrestricted reverse feasibility.",
        },
        "honest_gap":
            "The tree identifies the exact final synchronization and the "
            "component equalities within the finite 44-ray levels, but the "
            "nonmonotone hierarchical nine-history profile does not support "
            "a claim of progressive component erasure and does not derive "
            "the entry predicate or a universal attraction mechanism.",
    }
    mechanism["pass"] = (
        collision_map["pass"]
        and hierarchy["pass"]
        and reverse_varying
        == (0, 15, 19, 23, 19, 23, 21, 12, 11)
        and not mechanism["progressive_monotone_erasure"]
        and full_level_rows[1]["varying_wire_count"] == 23
        and mechanism["last_tick"]["status"] == "HOLDS_EXACTLY"
        and mechanism["after_Sstar"]["distinct_nine_images_at_t14740"] > 1
        and not mechanism["after_Sstar"]["Sstar_is_common_fixed_point"]
        and mechanism["entry_predicate"]["equals_exact_nine"]
    )
    return collision_map, hierarchy, mechanism


def moment_certificate(
    census: dict[str, object],
    target: int,
) -> dict[str, object]:
    public = census["public"]
    first = public["first_exact_hit_depth"]
    result = {
        "tenth_mechanism_attempt":
            "pair each lawful t=0 state with its fixed position word and "
            "ask for the least d satisfying x0=F_p^{-d}(S*)",
        "equivalence_used":
            "because F_p is bijective, x0=F_p^{-d}(S*) iff "
            "F_p^d(x0)=S*",
        "exact_search":
            "the all-176 forward census is the exact low-memory decision "
            "procedure for those reverse constraints at every depth "
            "0<=d<=14739",
        "first_satisfiable_reverse_depth": first,
        "satisfying_lawful_keys": public["first_exact_hit_keys"],
        "Sstar_sha256_input": state_sha256(target),
        "outcome":
            "TENTH_MECHANISM_FAILS_EQUIVALENT_FORWARD_REPLAY",
        "exact_support_status":
            "CONDITIONAL_MINIMAL_DEPTH_VERIFICATION: given the supplied "
            "S*, lawful t=0 fixtures, and landed gate rows, every depth "
            "below 14739 is rejected and the nine keys satisfy at 14739",
        "noncircular_account_of_14739": False,
        "why_not_noncircular":
            "the reverse condition is converted by bijectivity into the "
            "target-equivalent forward orbit census, run to the already "
            "declared horizon 14739; this verifies minimality but introduces "
            "no independent invariant or mechanism selecting that integer",
        "closed_form_or_orbit_phase_explanation": False,
        "honest_gap":
            "The exact constraint-equivalent replay is support, not a tenth "
            "mechanism and not an explanation of why the first satisfying "
            "depth is 14739.",
    }
    result["pass"] = (
        first == MECHANISM_ENTRY
        and result["satisfying_lawful_keys"] == NINE_KEYS
        and public["all_exact_hits_through_horizon"]
        == tuple((MECHANISM_ENTRY, key) for key in NINE_KEYS)
        and not result["noncircular_account_of_14739"]
    )
    return result


def stable_render(
    certificates: dict[str, object],
    report: dict[str, object],
) -> str:
    return "\n".join([
        *(
            f"CERTIFICATE_{name}={compact(value)}"
            for name, value in certificates.items()
        ),
        f"REPORT={compact(report)}",
    ]) + "\n"


def run() -> int:
    started = monotonic()
    sources = source_certificate()
    fixtures = decode_fixtures()
    macros = fixtures["macros"]
    positions = fixtures["positions"]
    target = fixtures["sstar"]
    assert isinstance(macros, tuple)
    assert isinstance(positions, tuple)
    assert isinstance(target, int)
    words = build_words(macros, positions)
    word_shape = {
        "positions": len(words),
        "gate_counts": tuple(sorted(set(map(len, words.values())))),
        "landed_order":
            "11 controller steps; within each step stations scan 0..10; "
            "the two live station macros are appended in station order",
        "pass": (
            len(words) == 44
            and set(map(len, words.values())) == {WORD_GATE_COUNT}
        ),
    }
    census = forward_lawful_census(fixtures, target)
    certificate_a = {
        "claim_boundary":
            "exact conditional reconstruction from disclosed embedded "
            "fixtures; fixture hashes prevent drift but do not independently "
            "prove their extraction from the pinned source texts",
        "tracked_copy_and_fixture_provenance": fixtures["certificate"],
        "word_reimplementation": word_shape,
        "reconstruction": census["public"],
        "Sstar_identity": {
            "state_bits": STATE_BITS,
            "hamming_weight": target.bit_count(),
            "state_sha256": state_sha256(target),
            "expected_cycle822_state_sha256": EXPECTED_SSTAR_SHA256,
            "packed_sha256": packed_sha256(target),
        },
    }
    certificate_a["pass"] = (
        sources["pass"]
        and fixtures["certificate"]["pass"]
        and word_shape["pass"]
        and census["public"]["pass"]
        and target.bit_count() == 44
        and state_sha256(target) == EXPECTED_SSTAR_SHA256
    )
    certificate_b = one_step_certificate(target, words)
    certificate_c, levels = preimage_tree_certificate(target, words)
    (
        certificate_collision,
        certificate_hierarchy,
        certificate_mechanism,
    ) = (
        trajectory_and_mechanism_certificates(
            target, words, census["snapshots"], levels, fixtures["keys"]
        )
    )
    certificate_c["nine_actual_trajectories"] = (
        certificate_collision
    )
    certificate_c["pass"] = (
        certificate_c["pass"] and certificate_collision["pass"]
    )
    certificate_e = moment_certificate(census, target)
    certificate_unchanged = {
        "scope":
            "Cycle-830 v1 results unaffected by the adopted collision "
            "correction and reproduced without weakening their checks.",
        "preimage_derivations": {
            "Sstar_reconstruction": certificate_a,
            "one_step_44_labels_to_14_data_states": certificate_b,
            "depth_0_through_8_tree": certificate_c,
        },
        "erasure_accounting": {
            "status": "STANDS_EXACTLY",
            "depth1_distinct_nodes":
                certificate_mechanism["last_tick"][
                    "predecessor_distinct_nodes"
                ],
            "depth1_varying_wire_indices":
                certificate_mechanism["last_tick"][
                    "predecessor_varying_wire_indices"
                ],
            "depth1_varying_wire_count":
                certificate_mechanism["last_tick"][
                    "predecessor_varying_wire_count"
                ],
            "image_distinct_nodes":
                certificate_mechanism["last_tick"][
                    "image_distinct_nodes"
                ],
            "image_varying_wire_count":
                certificate_mechanism["last_tick"][
                    "image_varying_wire_count"
                ],
            "all_key_specific_final_ticks_equal_Sstar":
                certificate_hierarchy["final_tick"]["all_nine_one_state"],
        },
        "tenth_mechanism_failure": certificate_e,
    }
    certificate_unchanged["pass"] = (
        certificate_a["pass"]
        and certificate_b["pass"]
        and certificate_c["pass"]
        and certificate_unchanged["erasure_accounting"]["status"]
        == "STANDS_EXACTLY"
        and certificate_unchanged["erasure_accounting"][
            "depth1_distinct_nodes"
        ] == 3
        and certificate_unchanged["erasure_accounting"][
            "depth1_varying_wire_count"
        ] == 15
        and certificate_unchanged["erasure_accounting"][
            "image_distinct_nodes"
        ] == 1
        and certificate_unchanged["erasure_accounting"][
            "image_varying_wire_count"
        ] == 0
        and certificate_unchanged["erasure_accounting"][
            "all_key_specific_final_ticks_equal_Sstar"
        ]
        and certificate_e["pass"]
    )
    elapsed = monotonic() - started
    checks = {
        "A_COLLISION_MAP": certificate_collision["pass"],
        "B_HIERARCHICAL_PROFILE": certificate_hierarchy["pass"],
        "C_CORRECTED_MECHANISM_READING":
            certificate_mechanism["pass"],
        "D_UNCHANGED_RESULTS": certificate_unchanged["pass"],
        "E_CONTROLS": False,
    }
    controls = {
        **sources,
        "fixture_exact_arithmetic":
            "all state evolution, equality, hashes, prefilters, and reverse "
            "constraints use Python unbounded integers over GF(2); only "
            "wall-clock runtime reporting uses a monotonic float",
        "gate_word_reimplementation": word_shape,
        "population_determinism":
            census["public"]["replay_exact_at_t14731_through_t14739"],
        "blocked_modules_loaded_at_end": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_at_end": tuple(IMPORT_FIREWALL.hits),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "pass": False,
    }
    controls_base = (
        sources["pass"]
        and fixtures["certificate"]["pass"]
        and word_shape["pass"]
        and controls["population_determinism"]
        and not controls["blocked_modules_loaded_at_end"]
        and not controls["firewall_hits_at_end"]
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    certificates = {
        "A_COLLISION_MAP": certificate_collision,
        "B_HIERARCHICAL_PROFILE": certificate_hierarchy,
        "C_CORRECTED_MECHANISM": certificate_mechanism,
        "D_UNCHANGED_PREIMAGE_ERASURE_TENTH_MECHANISM":
            certificate_unchanged,
        "E_CONTROLS": controls,
    }
    report = {
        "cycle": 830,
        "version": 2,
        "target": "S* hierarchical preimage merger profile",
        "actual_status":
            "exact support conditional on disclosed landed-fixture import",
        "one_step_distinct_data_preimages":
            certificate_b["distinct_5815_bit_data_preimage_count"],
        "tree_declared_depth": TREE_DEPTH,
        "tree_exact_materialized_counts":
            certificate_c["exact_materialized_counts"],
        "nine_distinct_nodes_by_reverse_depth": tuple(
            row["distinct_nine_state_nodes"]
            for row in certificate_collision["depth_rows"]
        ),
        "full_partition_sequence_depth_0_through_8":
            certificate_collision[
                "full_partition_sequence_depth_0_through_8"
            ],
        "partition_relations_depth_8_through_0":
            certificate_hierarchy[
                "transition_relations_depth_8_through_0"
            ],
        "monotone_partition_coarsening_toward_depth_0":
            certificate_hierarchy[
                "monotone_coarsening_toward_depth_0"
            ],
        "mechanism": certificate_mechanism["classification"],
        "moment_outcome": certificate_e["outcome"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "checks": {},
        "pass": False,
        "terminal": "CYCLE830_V2_HIERARCHICAL_MERGER_HONEST_FAIL",
    }
    for _iteration in range(8):
        controls["pass"] = controls_base
        checks["E_CONTROLS"] = controls["pass"]
        report["checks"] = dict(checks)
        report["pass"] = all(checks.values())
        report["terminal"] = (
            "CYCLE830_V2_HIERARCHICAL_MERGER_EXACT_PASS"
            if report["pass"]
            else "CYCLE830_V2_HIERARCHICAL_MERGER_HONEST_FAIL"
        )
        output = stable_render(certificates, report)
        total_bytes = len(output.encode("utf-8"))
        stdout_ok = total_bytes < STDOUT_LIMIT_BYTES
        controls["stdout_bytes"] = total_bytes
        controls["pass"] = controls_base and stdout_ok
        checks["E_CONTROLS"] = controls["pass"]
        report["stdout_bytes"] = total_bytes
    output = stable_render(certificates, report)
    final_bytes = len(output.encode("utf-8"))
    if final_bytes >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(compact({
            "pass": False,
            "terminal": "CYCLE830_V2_HIERARCHICAL_MERGER_HONEST_FAIL",
            "failure": "stdout bound exceeded",
            "stdout_bytes": final_bytes,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }) + "\n")
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


def main() -> int:
    try:
        return run()
    except Exception as error:
        sys.stdout.write(compact({
            "pass": False,
            "terminal": "CYCLE830_V2_HIERARCHICAL_MERGER_HONEST_FAIL",
            "exception_type": type(error).__name__,
            "exception": str(error),
        }) + "\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
