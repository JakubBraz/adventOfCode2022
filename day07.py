from collections import defaultdict


def get_sizes(inp):
    dir_names = ['/']
    sizes = defaultdict(int)
    for line in inp:
        if line[:4] == '$ cd':
            _, _, current_dir = line.split()
            if current_dir == '..':
                dir_names.pop()
            else:
                val = dir_names[-1] + current_dir + '/'
                dir_names.append(val)
        elif line[:4] == '$ ls':
            pass
        else:
            type_size, name = line.split()
            if type_size == 'dir':
                pass
            else:
                for d in dir_names:
                    sizes[d] += int(type_size)
    return sizes


def solve1(sizes, limit):
    return sum(x for x in sizes.values() if x <= limit)


def solve2(sizes, max_limit, needed):
    unused = max_limit - sizes['/']
    result = [x for x in sizes.values() if x + unused >= needed]
    return min(result)


def main():
    # inp = day_input_test().split('\n')
    # inp = day_input().split('\n')
    inp = day_input_kaja().split('\n')
    sizes = get_sizes(inp[1:])
    result1 = solve1(sizes, 100_000)
    print(result1)
    result2 = solve2(sizes, 70_000_000, 30_000_000)
    print(result2)


def day_input_test():
    return """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


def day_input():
    return """$ cd /
$ ls
150555 bch.lht
276291 ccqfdznj.sqg
dir csmqbhjv
dir czdqfr
dir fpfwfzrt
192660 qnbzgp
142026 rpphgdhp.jfr
dir sqphfslv
38077 tvpzh
$ cd csmqbhjv
$ ls
52822 bch.lht
dir dgj
dir fmmblb
dir hjwwtw
dir mtmhst
dir njsccfms
dir wmjsvq
$ cd dgj
$ ls
266484 bch.lht
dir brwncbh
dir dtdzsqps
216678 gvmdvcs.fmq
225948 mdjrhmhf
dir tvpzh
301487 tvpzh.wbp
2555 whsnd.spb
$ cd brwncbh
$ ls
238441 jwmr.plh
$ cd ..
$ cd dtdzsqps
$ ls
294443 fmmblb
81441 nsljm.fcz
$ cd ..
$ cd tvpzh
$ ls
186671 bch.lht
dir czdqfr
dir fgmz
300898 gvmdvcs.fmq
dir rjnv
dir szcrlzmr
dir tvpzh
dir vbrn
$ cd czdqfr
$ ls
dir czdqfr
dir hrhqhcjg
$ cd czdqfr
$ ls
8551 zmcqmq.zvf
$ cd ..
$ cd hrhqhcjg
$ ls
8255 wfvj.lnd
$ cd ..
$ cd ..
$ cd fgmz
$ ls
145921 wfvj.lnd
$ cd ..
$ cd rjnv
$ ls
305697 bch.lht
dir cdqv
dir czdqfr
288685 nsjnqh.fzq
210447 qlg
34660 rbnlc.gmc
143353 vsjg.njm
$ cd cdqv
$ ls
294789 czdqfr.nvt
$ cd ..
$ cd czdqfr
$ ls
298572 bch.lht
dir fmmblb
5599 tvpzh.pnf
47873 vmm
$ cd fmmblb
$ ls
dir cjtb
dir llg
dir rcb
190831 rwf.rzd
$ cd cjtb
$ ls
306568 fmmblb.hns
$ cd ..
$ cd llg
$ ls
68274 hbj.glq
261526 jplstj
285699 rmq
$ cd ..
$ cd rcb
$ ls
dir lmgrr
$ cd lmgrr
$ ls
306217 bch.lht
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd szcrlzmr
$ ls
dir mdjrhmhf
195828 pnllrfpr.lhl
dir rns
286738 sgzhcwj
$ cd mdjrhmhf
$ ls
dir clmdlmc
dir fmmblb
299416 fmmblb.ftr
dir mnm
22720 zpgvqpbr.glm
$ cd clmdlmc
$ ls
289014 fmmblb.njt
246797 gvmdvcs.fmq
92044 tvpzh.cfj
$ cd ..
$ cd fmmblb
$ ls
81512 czdqfr.ltc
173394 ntcdzdc.spn
$ cd ..
$ cd mnm
$ ls
260096 bch.lht
dir czdqfr
dir rwnqgjmm
$ cd czdqfr
$ ls
269467 nfphbtz
$ cd ..
$ cd rwnqgjmm
$ ls
218872 ldflbsm.rzh
256978 lwhhc
dir pgrtzw
$ cd pgrtzw
$ ls
32086 gvmdvcs.fmq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd rns
$ ls
282353 fcwhvqd.qvb
dir fwjb
dir prdd
dir rtrglmt
$ cd fwjb
$ ls
dir jlhqd
217527 tgvqql
$ cd jlhqd
$ ls
196505 qbrbcrgt.wqj
$ cd ..
$ cd ..
$ cd prdd
$ ls
144295 brwncbh
87560 dsrm
$ cd ..
$ cd rtrglmt
$ ls
219787 tcsrq.wzt
$ cd ..
$ cd ..
$ cd ..
$ cd tvpzh
$ ls
dir swrgwp
$ cd swrgwp
$ ls
dir cqzs
dir wtcsc
$ cd cqzs
$ ls
284674 rlhjp.dlf
$ cd ..
$ cd wtcsc
$ ls
50313 wfvj.lnd
$ cd ..
$ cd ..
$ cd ..
$ cd vbrn
$ ls
11650 czdqfr.ccz
dir fmmblb
145626 whsnd.spb
$ cd fmmblb
$ ls
204558 rdh.rms
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd fmmblb
$ ls
dir bhvpslz
$ cd bhvpslz
$ ls
dir jsmrb
$ cd jsmrb
$ ls
1472 fgctpsl.rgf
258119 whsnd.spb
$ cd ..
$ cd ..
$ cd ..
$ cd hjwwtw
$ ls
291890 fmmblb.zrt
$ cd ..
$ cd mtmhst
$ ls
dir dfqm
dir fmmblb
178539 jtmflfb
dir mdjrhmhf
dir rdzg
dir tvpzh
dir wqlf
$ cd dfqm
$ ls
dir czdqfr
dir fmmblb
dir gngvhs
dir ppjdlbp
dir shs
dir srdrb
$ cd czdqfr
$ ls
85242 gwqzn.ppr
$ cd ..
$ cd fmmblb
$ ls
76800 bqbnwdq.zfr
72865 fmmblb
119311 hfbtwgb.nmn
305342 wfvj.lnd
$ cd ..
$ cd gngvhs
$ ls
dir fmmblb
dir jfptn
dir jlqzq
dir mdjrhmhf
dir scmjf
dir tvpzh
$ cd fmmblb
$ ls
174392 whsnd.spb
$ cd ..
$ cd jfptn
$ ls
dir vjm
$ cd vjm
$ ls
193871 bch.lht
$ cd ..
$ cd ..
$ cd jlqzq
$ ls
dir fmmblb
187410 hcfdppj.hjh
dir mdjrhmhf
dir nhb
107865 qntnnqcp
dir wlqjpsh
$ cd fmmblb
$ ls
dir ccpvdzg
240944 fqsjc.cmc
$ cd ccpvdzg
$ ls
304195 whsnd.spb
$ cd ..
$ cd ..
$ cd mdjrhmhf
$ ls
242269 whsnd.spb
$ cd ..
$ cd nhb
$ ls
83616 mtfq
$ cd ..
$ cd wlqjpsh
$ ls
249472 gdg
$ cd ..
$ cd ..
$ cd mdjrhmhf
$ ls
213465 bbsltzd.fvd
dir tqmwn
$ cd tqmwn
$ ls
54460 bwnztql
262257 gvmdvcs.fmq
$ cd ..
$ cd ..
$ cd scmjf
$ ls
dir fhfg
268890 wqdcbprh
$ cd fhfg
$ ls
234806 whsnd.spb
$ cd ..
$ cd ..
$ cd tvpzh
$ ls
79625 zqbsb.mnq
$ cd ..
$ cd ..
$ cd ppjdlbp
$ ls
249976 zdqlmnll.nps
$ cd ..
$ cd shs
$ ls
107840 bsfcgmrw.dzw
dir fmmblb
307016 gvmdvcs.fmq
185876 jjhdj.vpn
254920 ltmp
dir rrg
312847 whsnd.spb
$ cd fmmblb
$ ls
161417 wppzrz.hjz
$ cd ..
$ cd rrg
$ ls
304639 bch.lht
$ cd ..
$ cd ..
$ cd srdrb
$ ls
dir bgchgtg
238106 hcfdppj.hjh
dir lgz
dir zmlm
$ cd bgchgtg
$ ls
dir hhbmwp
166735 psbpml.jdb
dir rtdwhlsq
171684 zcb.dlr
$ cd hhbmwp
$ ls
105599 cppw.mlb
dir dvzmpfzn
72811 fmmblb.bdd
293591 fnh.fdv
dir fspwz
dir gznwz
259403 tvpzh.bfj
$ cd dvzmpfzn
$ ls
127885 nbb.jgs
126415 whsnd.spb
$ cd ..
$ cd fspwz
$ ls
dir fzpfbcvv
dir jzrqvds
$ cd fzpfbcvv
$ ls
114984 czdqfr.pmn
157782 gzwrcdp.mtz
$ cd ..
$ cd jzrqvds
$ ls
47749 hcfdppj.hjh
$ cd ..
$ cd ..
$ cd gznwz
$ ls
77780 lnbtzj.bhz
$ cd ..
$ cd ..
$ cd rtdwhlsq
$ ls
300900 bbs
dir cchdchd
246695 djbmcmn
195895 fvwm.hrd
67210 hcfdppj.hjh
101017 zhnvhfm.wps
$ cd cchdchd
$ ls
52763 gvmdvcs.fmq
124993 tvpzh.nwc
dir zzsbq
$ cd zzsbq
$ ls
263814 zvhnm.sbv
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd lgz
$ ls
121541 wfvj.lnd
134550 whsnd.spb
$ cd ..
$ cd zmlm
$ ls
91948 cjqdnnh.hzr
250728 czdqfr.zjb
dir jnbhfnn
dir rnmghbht
dir tjhnp
144737 whsnd.spb
$ cd jnbhfnn
$ ls
49839 whsnd.spb
$ cd ..
$ cd rnmghbht
$ ls
69330 hcjspd
dir mfgbbvcc
dir qdh
$ cd mfgbbvcc
$ ls
dir gmgdfss
$ cd gmgdfss
$ ls
266023 hcfdppj.hjh
dir mdjrhmhf
dir ndcmqpc
291530 vqwf.bfc
$ cd mdjrhmhf
$ ls
dir brwncbh
$ cd brwncbh
$ ls
dir fmmblb
$ cd fmmblb
$ ls
dir ppwp
$ cd ppwp
$ ls
299841 mdjrhmhf.bdg
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ndcmqpc
$ ls
71727 mdjrhmhf.njs
218233 nwvfb.qzt
$ cd ..
$ cd ..
$ cd ..
$ cd qdh
$ ls
294005 jgbcmg.hjg
$ cd ..
$ cd ..
$ cd tjhnp
$ ls
dir vhjtqdg
$ cd vhjtqdg
$ ls
28638 gvmdvcs.fmq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd fmmblb
$ ls
111152 cnvzdz.cdb
252709 gvmdvcs.fmq
168368 lpfbzh
dir mdjrhmhf
dir mzrzzhpt
72606 qbbllr.shq
160820 whsnd.spb
$ cd mdjrhmhf
$ ls
32945 fmmblb.jpf
$ cd ..
$ cd mzrzzhpt
$ ls
dir gdsv
130898 hcfdppj.hjh
44339 hvnqt
dir mdjrhmhf
297785 mdwng.pbr
dir wwqmlhgg
281612 zvftqhm.pzl
$ cd gdsv
$ ls
10562 cprgfn
$ cd ..
$ cd mdjrhmhf
$ ls
284882 dpjs
202491 lrtgstpp.grn
3714 wfvj.lnd
$ cd ..
$ cd wwqmlhgg
$ ls
84563 fwvhfrh.cfp
4654 hcfdppj.hjh
248672 whsnd.spb
$ cd ..
$ cd ..
$ cd ..
$ cd mdjrhmhf
$ ls
dir mdjrhmhf
25175 mdjrhmhf.nrg
dir mslwjsp
207567 prrqb.qwj
282436 tvpzh.hjh
$ cd mdjrhmhf
$ ls
43516 jzrjwdd.vss
27326 wfvj.lnd
$ cd ..
$ cd mslwjsp
$ ls
141951 cqvh.zzq
$ cd ..
$ cd ..
$ cd rdzg
$ ls
312895 brwncbh.cpb
$ cd ..
$ cd tvpzh
$ ls
228240 bch.lht
dir fjtwlj
dir jnpgqsb
90201 ldh
271575 rfhh.vzr
69760 whsnd.spb
$ cd fjtwlj
$ ls
46126 rhdr.jgg
$ cd ..
$ cd jnpgqsb
$ ls
dir rllbvnm
$ cd rllbvnm
$ ls
212620 hcfdppj.hjh
$ cd ..
$ cd ..
$ cd ..
$ cd wqlf
$ ls
210864 fmmblb
dir jswfprpl
dir nztbsbq
$ cd jswfprpl
$ ls
dir fmmblb
dir lmwz
dir qvj
$ cd fmmblb
$ ls
201940 mhjlhc.npl
$ cd ..
$ cd lmwz
$ ls
dir brwncbh
dir dhff
288199 flgch
187825 gvmdvcs.fmq
203272 nvfllgvn.cjj
dir tvpzh
dir vrv
53288 zsrz.mrd
$ cd brwncbh
$ ls
174732 whsnd.spb
$ cd ..
$ cd dhff
$ ls
dir lddw
dir mfwnzprw
222134 tvpzh.gfm
$ cd lddw
$ ls
296685 bch.lht
$ cd ..
$ cd mfwnzprw
$ ls
6260 dvrcqzp.pmd
$ cd ..
$ cd ..
$ cd tvpzh
$ ls
dir gmvswdr
dir hfzdqdz
dir hhjwt
228542 htljf.tfl
57417 mdjrhmhf
248369 whsnd.spb
$ cd gmvswdr
$ ls
215582 fnzh.mhs
$ cd ..
$ cd hfzdqdz
$ ls
82080 dcw.vmt
142007 fmmblb.fnq
dir ggqcqcc
36091 hcfdppj.hjh
219562 mqb.qsm
2323 wfvj.lnd
$ cd ggqcqcc
$ ls
4679 whsnd.spb
$ cd ..
$ cd ..
$ cd hhjwt
$ ls
dir lbqpgd
dir tdb
$ cd lbqpgd
$ ls
177175 wfvj.lnd
$ cd ..
$ cd tdb
$ ls
270893 bch.lht
$ cd ..
$ cd ..
$ cd ..
$ cd vrv
$ ls
dir bqmnhdts
171679 czdqfr
$ cd bqmnhdts
$ ls
64972 pjzzs.qqd
$ cd ..
$ cd ..
$ cd ..
$ cd qvj
$ ls
dir bfwtb
dir bpnppqg
271362 gcs.srv
dir gvlqddlb
70000 gzdr.ndb
103231 pwspfm
dir swgfvtf
$ cd bfwtb
$ ls
200600 czdqfr.sbv
dir wmbhgcw
$ cd wmbhgcw
$ ls
310044 zwfrcld.mtb
$ cd ..
$ cd ..
$ cd bpnppqg
$ ls
120203 dggplss.whb
$ cd ..
$ cd gvlqddlb
$ ls
12163 bch.lht
154059 llpw
dir pglr
dir rbfpbcpd
dir rstg
209132 tvpzh.djc
287422 wlhjvsz
$ cd pglr
$ ls
145907 brwncbh.cqp
$ cd ..
$ cd rbfpbcpd
$ ls
292475 brwncbh
dir czdqfr
dir dcnh
dir fmmblb
dir qwrsrdr
$ cd czdqfr
$ ls
66107 tvpzh.wfd
$ cd ..
$ cd dcnh
$ ls
297110 rpzsrws.sft
$ cd ..
$ cd fmmblb
$ ls
25829 wmmhq
$ cd ..
$ cd qwrsrdr
$ ls
199762 fmmblb.qpm
$ cd ..
$ cd ..
$ cd rstg
$ ls
236706 bch.lht
$ cd ..
$ cd ..
$ cd swgfvtf
$ ls
227938 lrbcddd.btw
282992 rlnwrd
$ cd ..
$ cd ..
$ cd ..
$ cd nztbsbq
$ ls
116544 czdqfr
dir fhwmhvdn
68451 gvmdvcs.fmq
247136 hcfdppj.hjh
dir mzvq
dir tvpzh
dir wtllfshw
$ cd fhwmhvdn
$ ls
122155 cmtlhcdw
39927 twbfczfb.lcp
$ cd ..
$ cd mzvq
$ ls
dir lnjtfgh
$ cd lnjtfgh
$ ls
161712 phfn
$ cd ..
$ cd ..
$ cd tvpzh
$ ls
dir jgpr
dir mdjrhmhf
dir rnntmvpr
$ cd jgpr
$ ls
85238 gvmdvcs.fmq
$ cd ..
$ cd mdjrhmhf
$ ls
231007 gzrsgvp
$ cd ..
$ cd rnntmvpr
$ ls
285020 tvpzh
$ cd ..
$ cd ..
$ cd wtllfshw
$ ls
135281 gvmdvcs.fmq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd njsccfms
$ ls
dir zdddqvq
$ cd zdddqvq
$ ls
91520 whmwbpd
$ cd ..
$ cd ..
$ cd wmjsvq
$ ls
dir fmmblb
dir htmb
dir lmzhpth
dir mrjq
142052 wldwl
$ cd fmmblb
$ ls
173331 fmmblb.fbm
$ cd ..
$ cd htmb
$ ls
dir gtm
$ cd gtm
$ ls
7647 hcfdppj.hjh
$ cd ..
$ cd ..
$ cd lmzhpth
$ ls
dir tvpzh
dir vdqg
dir zvhmfm
$ cd tvpzh
$ ls
259073 wfvj.lnd
$ cd ..
$ cd vdqg
$ ls
199919 bch.lht
169430 fmmblb.ttq
231127 hcfdppj.hjh
$ cd ..
$ cd zvhmfm
$ ls
274752 gvmdvcs.fmq
$ cd ..
$ cd ..
$ cd mrjq
$ ls
dir fqcspsv
dir fvvmlbf
252802 gnclv
82538 gvmdvcs.fmq
296461 jvbnhrpd
104809 lbh
46038 tfq.gtv
$ cd fqcspsv
$ ls
dir fjqnf
$ cd fjqnf
$ ls
dir tvpzh
$ cd tvpzh
$ ls
dir lhwdrcwz
$ cd lhwdrcwz
$ ls
129410 lcd.dzd
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd fvvmlbf
$ ls
263142 brwncbh.fgg
232863 cvwv
100409 qphswnlb.vpq
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd czdqfr
$ ls
dir czdqfr
307029 lntbmr.brq
dir mdjrhmhf
dir tvpzh
$ cd czdqfr
$ ls
289585 gvmdvcs.fmq
$ cd ..
$ cd mdjrhmhf
$ ls
137110 brwncbh.dbt
$ cd ..
$ cd tvpzh
$ ls
258325 wfvj.lnd
$ cd ..
$ cd ..
$ cd fpfwfzrt
$ ls
221993 hcfdppj.hjh
56206 lphphf.thd
255850 mdjrhmhf.hqt
$ cd ..
$ cd sqphfslv
$ ls
104415 mdjrhmhf.gbr
dir pjtzm
dir spnr
61982 stbwbpzf.hwm
$ cd pjtzm
$ ls
dir brwncbh
178769 jnmgzcqh.mht
dir tvpzh
153193 tvpzh.cdc
dir zstcqndd
$ cd brwncbh
$ ls
117400 brwncbh.mvq
dir fbzvn
3239 fmmblb.hzm
73631 hqtnwbgw
dir npzf
172382 pdgg
$ cd fbzvn
$ ls
152876 bch.lht
293370 czc.jtt
43408 czdqfr
dir fqg
105569 qqmcwjz.bzd
19734 whsnd.spb
$ cd fqg
$ ls
88780 jffmmm.qff
22385 lqrhch.vlm
$ cd ..
$ cd ..
$ cd npzf
$ ls
190792 pdtlbrqt.ghq
$ cd ..
$ cd ..
$ cd tvpzh
$ ls
dir blgjrjt
dir dlzjtlbt
dir jnwm
dir qprbng
305178 tbvg
dir tvpzh
308117 wrbldl.jhp
$ cd blgjrjt
$ ls
125644 bch.lht
104319 ctglz.lmd
131972 hcfdppj.hjh
312663 tbgqwf
$ cd ..
$ cd dlzjtlbt
$ ls
98262 bvfldnd.sls
173244 dlmf.mzh
75842 rlbpgjh.wtb
$ cd ..
$ cd jnwm
$ ls
58963 vjftmflp.dcs
$ cd ..
$ cd qprbng
$ ls
308054 fzbrm.jdt
310679 gnwn.psf
257810 tpsgjjdq.mdw
dir tvpzh
305633 vpbwhqs.cqb
$ cd tvpzh
$ ls
220904 rlpj.rdc
$ cd ..
$ cd ..
$ cd tvpzh
$ ls
dir fmmblb
$ cd fmmblb
$ ls
104020 crhq.pnb
74914 czdqfr
$ cd ..
$ cd ..
$ cd ..
$ cd zstcqndd
$ ls
dir brwncbh
dir jwpbtpr
306359 ljg
dir wbssjjd
$ cd brwncbh
$ ls
114145 wfvj.lnd
$ cd ..
$ cd jwpbtpr
$ ls
94567 bch.lht
dir czdqfr
dir fsqvbv
134187 wnpcqmw.tws
$ cd czdqfr
$ ls
dir mdjrhmhf
$ cd mdjrhmhf
$ ls
122398 mdjrhmhf.zts
dir svhh
101920 whsnd.spb
dir zcsnqjj
$ cd svhh
$ ls
120875 tvpzh.jls
$ cd ..
$ cd zcsnqjj
$ ls
279979 tljnvzbq.sgj
$ cd ..
$ cd ..
$ cd ..
$ cd fsqvbv
$ ls
114278 hwrhzs.jbj
dir tvpzh
$ cd tvpzh
$ ls
17235 gvmdvcs.fmq
$ cd ..
$ cd ..
$ cd ..
$ cd wbssjjd
$ ls
dir mdjrhmhf
$ cd mdjrhmhf
$ ls
11336 fqsp
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd spnr
$ ls
298067 sznwzj"""


def day_input_kaja():
    return """$ cd /
$ ls
dir drblq
133789 fjf
dir jpfrhmw
dir jqfwd
dir ncgffsr
12962 ntnr.lrq
dir qnbq
dir rqdngnrq
dir shcvnqq
dir vsd
dir vtzvf
$ cd drblq
$ ls
133843 bglzqdd
dir brfnfhj
268201 fbqjmp.jzv
80676 shcvnqq
$ cd brfnfhj
$ ls
150447 jlcg.dsg
dir nhvgrzs
$ cd nhvgrzs
$ ls
282889 jlcg.dsg
19004 ncgffsr.gwr
dir vbzr
6338 vpsgdph.gbh
dir wdcn
$ cd vbzr
$ ls
225101 fbqjmp
243277 vbzr
$ cd ..
$ cd wdcn
$ ls
154089 dlmpbbf.psv
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd jpfrhmw
$ ls
87622 cffdsj.jzf
26165 qnbq.sbm
dir vbzr
$ cd vbzr
$ ls
dir blhstw
16919 nttftcts
dir rgdp
116477 shcvnqq
242592 tmjrnqbz.chq
dir vbzr
dir wmct
$ cd blhstw
$ ls
98023 jwdv.qct
$ cd ..
$ cd rgdp
$ ls
dir gcb
141507 shcvnqq
dir ssvzm
$ cd gcb
$ ls
189016 ncgffsr.rbq
$ cd ..
$ cd ssvzm
$ ls
82667 shcvnqq.zjq
$ cd ..
$ cd ..
$ cd vbzr
$ ls
120202 jlcg.dsg
86205 vbzr.jtr
$ cd ..
$ cd wmct
$ ls
dir fbsfcgph
155709 hpsftv
13636 lztgs
273353 ncgffsr.jsg
dir pvwhpfp
$ cd fbsfcgph
$ ls
139944 ncgffsr.gpf
$ cd ..
$ cd pvwhpfp
$ ls
111230 bscrjpzh.glp
dir dgjsddgq
37234 lwd
107139 lztgs
258111 mgtwwvwz
117638 qpdvnfb.gnf
dir szrplcdw
dir vzsl
dir wsmf
$ cd dgjsddgq
$ ls
dir qnbq
$ cd qnbq
$ ls
199119 jlcg.dsg
$ cd ..
$ cd ..
$ cd szrplcdw
$ ls
122236 qclr.cpf
269638 qnbq
$ cd ..
$ cd vzsl
$ ls
233006 twpz.tdm
$ cd ..
$ cd wsmf
$ ls
dir wcnptvtz
$ cd wcnptvtz
$ ls
183952 shcvnqq.lwt
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd jqfwd
$ ls
dir hqb
285121 jqffsjbs.jrm
dir nhpqpdn
dir qnbq
dir qtrv
dir wspztvjr
$ cd hqb
$ ls
253786 jwdv.qct
dir vbzr
$ cd vbzr
$ ls
153 gbh
dir gqpqqrgl
dir jzncgd
36914 nvdnsnls.mpd
$ cd gqpqqrgl
$ ls
206691 dmdgcwm.bgh
$ cd ..
$ cd jzncgd
$ ls
122640 vrgmf.tnp
$ cd ..
$ cd ..
$ cd ..
$ cd nhpqpdn
$ ls
86329 ntnr.lrq
$ cd ..
$ cd qnbq
$ ls
76269 fbqjmp.lbd
118968 fbqjmp.msg
190416 gfwhsb.dpc
dir lhgjrmj
dir pbv
173541 pfl
141842 srrmt.ssj
$ cd lhgjrmj
$ ls
dir ghccnw
180420 ldzcj.rwz
149356 lztgs
61792 ncgffsr
dir spmbcjhc
$ cd ghccnw
$ ls
253233 lztgs
56439 ntnr.lrq
19225 ntrmjf.gdb
31628 pdhhzjhm.lbd
$ cd ..
$ cd spmbcjhc
$ ls
dir shcvnqq
$ cd shcvnqq
$ ls
122334 drjbh
$ cd ..
$ cd ..
$ cd ..
$ cd pbv
$ ls
69436 cctsjqh.wqr
285573 ljtqddz
$ cd ..
$ cd ..
$ cd qtrv
$ ls
234568 dmwqfbwd
dir pwwsrjc
245046 qmcr
159151 qtvdjncm.rdb
dir swhzds
178915 vbzr.vgn
dir vcgv
$ cd pwwsrjc
$ ls
173975 bgdj.jnw
202714 jwdv.qct
270702 wggrgcvw.rtp
$ cd ..
$ cd swhzds
$ ls
114686 jwdv.qct
$ cd ..
$ cd vcgv
$ ls
dir fbqjmp
dir qlsgtfhf
dir vbzr
$ cd fbqjmp
$ ls
73065 fbqjmp.jfb
dir shcvnqq
$ cd shcvnqq
$ ls
231428 shcvnqq
$ cd ..
$ cd ..
$ cd qlsgtfhf
$ ls
75227 ntnr.lrq
$ cd ..
$ cd vbzr
$ ls
128050 ncgffsr.gsj
187649 vbzr
$ cd ..
$ cd ..
$ cd ..
$ cd wspztvjr
$ ls
dir pntrhtwh
dir qnbq
dir zfdzvv
$ cd pntrhtwh
$ ls
237258 cffhtr
$ cd ..
$ cd qnbq
$ ls
dir qnbq
$ cd qnbq
$ ls
dir ccwmftsj
$ cd ccwmftsj
$ ls
dir mfc
dir shcvnqq
12262 smpjmn
$ cd mfc
$ ls
198047 fbqjmp.cgh
dir gghsht
205411 wlclz
$ cd gghsht
$ ls
31767 vbzr.lmb
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
dir lgrghwf
$ cd lgrghwf
$ ls
114786 shcvnqq.vrz
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd zfdzvv
$ ls
54298 sjp
60303 tcmhrll.htm
$ cd ..
$ cd ..
$ cd ..
$ cd ncgffsr
$ ls
dir fqqsqmpr
dir gfznw
dir ncdft
dir pwmppt
dir shcvnqq
196969 vbzr
214841 vzgvr
$ cd fqqsqmpr
$ ls
dir mcdjcntr
$ cd mcdjcntr
$ ls
281856 ncgffsr.lbm
$ cd ..
$ cd ..
$ cd gfznw
$ ls
255657 fzrctbsj.lgf
dir ltfsndpd
175434 qnbq
31794 qnbq.zhd
13366 shcvnqq.wld
dir vcspqgn
235199 wmnjjd.bnh
dir wqpnp
$ cd ltfsndpd
$ ls
dir ncgffsr
dir zpzvdhb
$ cd ncgffsr
$ ls
9898 jjbsnj.gcg
$ cd ..
$ cd zpzvdhb
$ ls
106139 lnp
$ cd ..
$ cd ..
$ cd vcspqgn
$ ls
25386 dgsmmqj
$ cd ..
$ cd wqpnp
$ ls
65905 wjtbfvjp.fmd
$ cd ..
$ cd ..
$ cd ncdft
$ ls
34616 bzlpmsqc
59863 jlcg.dsg
64629 zpzjcl.fmp
$ cd ..
$ cd pwmppt
$ ls
dir dwnqgrzm
80901 vbzr.vsg
89557 vbzr.zlz
$ cd dwnqgrzm
$ ls
184770 jwdv.qct
dir vbzr
$ cd vbzr
$ ls
210329 jlcg.dsg
62272 jwdv.qct
$ cd ..
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
128433 gbh
30208 hjbw
200071 jlcg.dsg
dir sgcz
25045 tbhlwfqg.hts
$ cd sgcz
$ ls
193481 gbh
96461 jwdv.qct
$ cd ..
$ cd ..
$ cd ..
$ cd qnbq
$ ls
236171 shcvnqq
$ cd ..
$ cd rqdngnrq
$ ls
dir cprnb
280135 hshsfqwm
dir hwhm
245626 qnbq
145502 qspgdz
114231 rctg.tgt
dir zgn
$ cd cprnb
$ ls
115025 twwgmmp.wbb
$ cd ..
$ cd hwhm
$ ls
229849 cvm
190622 jwdv.qct
dir mscztz
dir ncgffsr
$ cd mscztz
$ ls
59743 bzgpzn.bds
75184 pbdgv
181089 shcvnqq.dhq
dir zqgtr
$ cd zqgtr
$ ls
189142 ffnznfs.nct
$ cd ..
$ cd ..
$ cd ncgffsr
$ ls
dir dphrnjl
dir zzfztql
$ cd dphrnjl
$ ls
117317 vbzr
$ cd ..
$ cd zzfztql
$ ls
51096 lztgs
$ cd ..
$ cd ..
$ cd ..
$ cd zgn
$ ls
dir bpbzwgz
dir gqnw
75631 ljptj
283351 ljzhsw.rbs
131158 lztgs
dir ncgffsr
3136 nnpl.swf
dir shcvnqq
dir vbzr
$ cd bpbzwgz
$ ls
29659 jlcg.dsg
15547 shcvnqq
117389 zprhsdfv
$ cd ..
$ cd gqnw
$ ls
117091 brqwhst.jgb
88406 nzjmbrrm.hmh
$ cd ..
$ cd ncgffsr
$ ls
195821 gbh
dir lbzgc
226692 llqqr.spq
247989 lztgs
231909 vnctc
157973 wqnggh
$ cd lbzgc
$ ls
251414 ffmsbscc.dqg
46840 lztgs
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
dir dvvmhzcq
dir ncgffsr
dir sqzzllv
$ cd dvvmhzcq
$ ls
dir qnbq
70226 qvvm.rpp
dir shcvnqq
$ cd qnbq
$ ls
103994 bfcjrmvr.ltq
dir fbqjmp
dir fcs
177152 gjghvvw.bzg
dir lbfjqh
78412 ntnr.lrq
dir sgjtm
286995 shcvnqq
51750 wmq.vjj
$ cd fbqjmp
$ ls
267212 qhhb.zvg
$ cd ..
$ cd fcs
$ ls
272051 znhsswwh.mjj
$ cd ..
$ cd lbfjqh
$ ls
261487 jlcg.dsg
$ cd ..
$ cd sgjtm
$ ls
dir dnznpj
dir jzsntnbs
dir nqgcbd
dir vdg
$ cd dnznpj
$ ls
173938 hrp.cjq
180485 qnbq.thj
215400 ztvt.wnt
$ cd ..
$ cd jzsntnbs
$ ls
67448 gpvgh.psg
$ cd ..
$ cd nqgcbd
$ ls
196250 fbqjmp.qcv
198482 jlcg.dsg
$ cd ..
$ cd vdg
$ ls
257343 jwdv.qct
$ cd ..
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
156769 fbqjmp.hdb
$ cd ..
$ cd ..
$ cd ncgffsr
$ ls
205473 fbqjmp
113067 gsvznzz.qtv
$ cd ..
$ cd sqzzllv
$ ls
146018 ddvjgswr.gsq
$ cd ..
$ cd ..
$ cd vbzr
$ ls
dir vbzr
$ cd vbzr
$ ls
266721 mhlfqpbs.pwr
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
dir slnvdd
$ cd slnvdd
$ ls
90875 pzqv.gnv
207484 rbrj.vcr
$ cd ..
$ cd ..
$ cd vsd
$ ls
dir dfb
dir fqqnsph
dir gbwdhjr
18837 jwdv.qct
dir ncgffsr
dir qnbq
dir rjzjrbvs
$ cd dfb
$ ls
dir bpst
66174 jwdv.qct
dir lcwhfzjw
$ cd bpst
$ ls
dir nqftnn
dir pcvgnvnp
$ cd nqftnn
$ ls
dir bbrsg
dir gjfc
dir hfql
dir shcvnqq
139226 shcvnqq.sbd
dir ssnjqbg
$ cd bbrsg
$ ls
73382 vjcf
$ cd ..
$ cd gjfc
$ ls
164310 gbh
126316 mmqnrc
133899 ntnr.lrq
102615 rgfhrt
$ cd ..
$ cd hfql
$ ls
14685 jwdv.qct
$ cd ..
$ cd shcvnqq
$ ls
119597 lztgs
34165 shcvnqq.zcg
$ cd ..
$ cd ssnjqbg
$ ls
77678 gqdfbqj.tmj
$ cd ..
$ cd ..
$ cd pcvgnvnp
$ ls
21250 lhq
266619 qps.crp
$ cd ..
$ cd ..
$ cd lcwhfzjw
$ ls
dir bhdnnbvm
dir fdnsvfh
12002 jlcg.dsg
dir lfdbzfl
46488 ncgffsr
233704 nthcv.pnc
204660 ntnr.lrq
172482 shcvnqq
dir tlw
$ cd bhdnnbvm
$ ls
37204 fwrdjw.zvv
3248 ntnr.lrq
$ cd ..
$ cd fdnsvfh
$ ls
20765 jlfgnwb.szl
$ cd ..
$ cd lfdbzfl
$ ls
dir fspntmld
183925 jlcg.dsg
$ cd fspntmld
$ ls
251568 lztgs
146785 ncgffsr.mmj
$ cd ..
$ cd ..
$ cd tlw
$ ls
dir qqn
$ cd qqn
$ ls
39232 lprqfwf
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd fqqnsph
$ ls
132318 lztgs
103863 ntnr.lrq
18793 tngbs
$ cd ..
$ cd gbwdhjr
$ ls
253798 jwdv.qct
$ cd ..
$ cd ncgffsr
$ ls
110767 blctz.tqz
dir csfssn
dir dbbfz
dir hjgm
dir hwd
249139 rgcz.gnz
dir wgw
$ cd csfssn
$ ls
dir dlcw
dir jqspd
119066 mlwlc.mql
dir ncgffsr
203475 nwnbsc
143071 qnbq
116623 qvw.gjz
83637 whm.cdg
$ cd dlcw
$ ls
232066 gqllsd.qpl
1046 mfsh
$ cd ..
$ cd jqspd
$ ls
251070 mthmm.bmh
$ cd ..
$ cd ncgffsr
$ ls
83639 ntnr.lrq
$ cd ..
$ cd ..
$ cd dbbfz
$ ls
112576 jgqf.qmj
148549 jlcg.dsg
144811 jwdv.qct
23726 ntnr.lrq
123802 pgdjchrf.vnm
dir vzfbzbcp
$ cd vzfbzbcp
$ ls
39375 fbqq
31914 jwdv.qct
165999 lztgs
$ cd ..
$ cd ..
$ cd hjgm
$ ls
dir ljqjtdmf
100534 mdw
219057 qnbq
97164 rzjwmvdw.vlv
dir shcvnqq
83034 vbzr
$ cd ljqjtdmf
$ ls
23716 dmslzv.qns
159519 gbh
dir hlvbmpg
dir nlqqshp
247315 vqt
dir wlsjnthg
$ cd hlvbmpg
$ ls
54421 jlcg.dsg
$ cd ..
$ cd nlqqshp
$ ls
dir rvzprwhp
$ cd rvzprwhp
$ ls
35024 lztgs
$ cd ..
$ cd ..
$ cd wlsjnthg
$ ls
29178 gnrlgb.bgh
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
150311 nvrd
$ cd ..
$ cd ..
$ cd hwd
$ ls
dir jzqtmm
$ cd jzqtmm
$ ls
103547 jtvdt.jtn
$ cd ..
$ cd ..
$ cd wgw
$ ls
dir mmhlt
$ cd mmhlt
$ ls
dir cmwjh
$ cd cmwjh
$ ls
243844 qnbq.shn
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd qnbq
$ ls
dir dhfng
dir fbqjmp
16855 rgrszmrh.lbl
dir rqjs
dir shcvnqq
38322 vhvrmq
$ cd dhfng
$ ls
132537 gwngz.hpt
dir lbccc
182221 ntnr.lrq
$ cd lbccc
$ ls
282448 fbqjmp.njj
267049 gbh
dir jtj
dir ntnn
dir vbfgmmvw
128500 vbzr
$ cd jtj
$ ls
dir hvmlh
$ cd hvmlh
$ ls
131886 dmww.sqc
$ cd ..
$ cd ..
$ cd ntnn
$ ls
109064 lgh.bbf
dir wfgdd
53862 wflv.ngc
$ cd wfgdd
$ ls
58756 gbh
dir lgzlndn
dir qnbq
$ cd lgzlndn
$ ls
190415 dwsqvczd
$ cd ..
$ cd qnbq
$ ls
240922 znjhmhp.ngt
$ cd ..
$ cd ..
$ cd ..
$ cd vbfgmmvw
$ ls
271827 vbzr.dfl
$ cd ..
$ cd ..
$ cd ..
$ cd fbqjmp
$ ls
144993 gvpnf
150786 jwdv.qct
49025 pdcwwtt.grs
$ cd ..
$ cd rqjs
$ ls
dir bwnzs
119390 jlcg.dsg
172042 vjzg
$ cd bwnzs
$ ls
108537 hzzgm.zrn
38699 qgfqbfr
dir vhvcfhvr
$ cd vhvcfhvr
$ ls
2783 jwdv.qct
209933 mgj.nvj
$ cd ..
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
257312 fbqjmp
193792 msdqtrpn.grn
98165 rgm
$ cd ..
$ cd ..
$ cd rjzjrbvs
$ ls
dir ftrlfg
dir mtrnl
dir rdpbbd
dir shcvnqq
dir vztnr
$ cd ftrlfg
$ ls
196590 cjjvwjb
dir ffsvh
70123 ldnbc
dir lwnfc
106499 lztgs
dir ncgffsr
dir tfdctq
dir vgthdbf
80852 zndjt.wtl
$ cd ffsvh
$ ls
20370 dvdftpvb.qcj
$ cd ..
$ cd lwnfc
$ ls
dir fgmd
dir gmdjt
274331 hmgjmq.vbz
9726 qjfdqbf.dfj
dir ssnncn
$ cd fgmd
$ ls
280608 jwdv.qct
201912 rqtbw.shd
$ cd ..
$ cd gmdjt
$ ls
202107 jwdv.qct
$ cd ..
$ cd ssnncn
$ ls
140697 jwdv.qct
$ cd ..
$ cd ..
$ cd ncgffsr
$ ls
227389 fpdfqp.fzl
164141 hzhrrvpm.hlf
$ cd ..
$ cd tfdctq
$ ls
dir cttmzlw
dir ntvtm
257094 qnbq.zjm
284928 shcvnqq
$ cd cttmzlw
$ ls
142651 rptschdv.mgv
$ cd ..
$ cd ntvtm
$ ls
176269 dhpj
88278 gbh
$ cd ..
$ cd ..
$ cd vgthdbf
$ ls
130998 ncgffsr.mnf
$ cd ..
$ cd ..
$ cd mtrnl
$ ls
86144 djwnvdj
122600 gsdpwh.cmb
$ cd ..
$ cd rdpbbd
$ ls
177384 gbh
dir gstfdm
dir qnbq
dir qtj
260302 vbzr.dhq
$ cd gstfdm
$ ls
23734 mnwzrm.hzr
$ cd ..
$ cd qnbq
$ ls
51705 gmt
205537 ntnr.lrq
94469 vbzr.bvj
$ cd ..
$ cd qtj
$ ls
dir tls
dir zvpcfhg
$ cd tls
$ ls
dir chvgwnt
dir jvgnmfjw
$ cd chvgwnt
$ ls
dir rbw
dir srhj
$ cd rbw
$ ls
174372 btjd.bvv
272995 cnqqh.dfc
$ cd ..
$ cd srhj
$ ls
134054 qwzpr
$ cd ..
$ cd ..
$ cd jvgnmfjw
$ ls
dir hdcwbwgm
236775 sdc
$ cd hdcwbwgm
$ ls
113707 ntnr.lrq
$ cd ..
$ cd ..
$ cd ..
$ cd zvpcfhg
$ ls
dir lsq
$ cd lsq
$ ls
220331 jlcg.dsg
$ cd ..
$ cd ..
$ cd ..
$ cd ..
$ cd shcvnqq
$ ls
dir cmwrqgfq
258731 fbqjmp.fvn
277895 gbh
64973 jlcg.dsg
77978 jwdv.qct
dir lttjrdn
dir sqgnhc
$ cd cmwrqgfq
$ ls
81199 gbh
$ cd ..
$ cd lttjrdn
$ ls
23355 gbh
148263 hcgfqdw
57338 hjwr
166510 jbvnmcj
$ cd ..
$ cd sqgnhc
$ ls
dir glswqrdp
dir qnbq
$ cd glswqrdp
$ ls
225761 ncgffsr.vct
$ cd ..
$ cd qnbq
$ ls
62861 pdqz.wzs
$ cd ..
$ cd ..
$ cd ..
$ cd vztnr
$ ls
189943 wvtlfsp
$ cd ..
$ cd ..
$ cd ..
$ cd vtzvf
$ ls
43248 jwdv.qct"""


if __name__ == '__main__':
    main()
