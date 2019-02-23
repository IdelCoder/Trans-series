# -*- coding: UTF-8 -*-
# please use python3
import csv
import re
# tranSparse计算稀疏度\theta
fb15k = './FB15K/'
fb13 = './FB13/'
wn11 = './WN11/'
wn18 = './WN18/'
round_size = 5

# rel_ratio.txt
def oper(dire):
    # 计算每个关系连接的实体对数量
    rel_share = dict()
    # 计算每个关系连接的头实体数量
    rel_sepa_head = dict()
    rel_sepa_tail = dict()
    ff = dire + 'train2id.txt'
    with open(ff, 'r') as f:
        idx = 0
        for row in f:
            if idx == 0:
                idx += 1
                continue
            triple = row.split()
            #print(triple)
            h = triple[0]
            t = triple[1]
            r = int(triple[2])
            if r not in rel_share:
                rel_share[r] = 0
            rel_share[r] += 1
            if r not in rel_sepa_head:
                rel_sepa_head[r] = set()
            rel_sepa_head[r].add(h)
            if r not in rel_sepa_tail:
                rel_sepa_tail[r] = set()
            rel_sepa_tail[r].add(t)
    rel_sepa_head_num = {key: len(value) for (key, value) in rel_sepa_head.items()}
    rel_sepa_tail_num = {key: len(value) for (key, value) in rel_sepa_tail.items()}
    # print(rel_sepa_head_num[9])
    # rel_share_sorted = sorted(rel_share, keys=lambda k: k[0])
    # rel_sepa_h_sorted = sorted(rel_sepa_head_num, keys=lambda k: k[0])
    # rel_sepa_t_sorted = sorted(rel_sepa_tail_num, keys=lambda k: k[0])
    
    share_largest = max(rel_share.values())
    sepa_h_largest = max(rel_sepa_head_num.values())
    sepa_t_largest = max(rel_sepa_tail_num.values())
    
    # 把三个统计数据放到一个dct中
    rel_dct = dict()
    for key in rel_share.keys():
        share_ratio = round(rel_share[key] / share_largest, round_size)
        h_ratio = 0 if key not in rel_sepa_head_num else round(rel_sepa_head_num[key] / sepa_h_largest, round_size)
        t_ratio = 0 if key not in rel_sepa_tail_num else round(rel_sepa_tail_num[key] / sepa_t_largest, round_size)
        rel_dct[key] = (share_ratio, h_ratio, t_ratio)
    
    # 写入文件
    with open(dire + 'rel_ratio.txt', 'w', newline='') as f:
        cf = csv.writer(f, delimiter=' ')
        for (k,v) in rel_dct.items():
            cf.writerow([k, v[0], v[1], v[2]])

oper(fb15k)
oper(fb13)
oper(wn11)
oper(wn18)

    


            