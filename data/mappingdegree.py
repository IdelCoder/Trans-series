# -*- coding: UTF-8 -*-
# please use python3
#获取hpt和tph
# mdegree: relation tph hpt
import csv
import math
import numpy as np
fb15k = './FB15K/'
fb13 = './FB13/'
wn11 = './WN11/'
wn18 = './WN18/'

def read_file(dire):
    # hpt {rel: {tail: head_cnt}}
    hpt = dict()
    tph = dict()
    with open(dire + 'train2id.txt', 'r', newline='') as f:
        cf = csv.reader(f, delimiter=' ')
        line = 0
        for row in cf:
            if line == 0:
                line += 1
                continue
            h = row[0]
            t = row[1]
            r = row[2]
            if r not in hpt:
                hpt[r] = dict()
            if t not in hpt[r]:
                hpt[r][t] = 0
            hpt[r][t] += 1
            if r not in tph:
                tph[r] = dict()
            if h not in tph[r]:
                tph[r][h] = 0
            tph[r][h] += 1
    hpt_cnt = {key: np.mean(list(value.values())) for (key, value) in hpt.items()}
    tph_cnt = {key: np.mean(list(value.values())) for (key, value) in tph.items()}
    with open(dire + 'mdegree.txt', 'w', newline='') as f:
        cf = csv.writer(f, delimiter=' ')
        for key in hpt_cnt.keys():
            r = key
            hpt_avg = hpt_cnt[r]
            tph_avg = tph_cnt[r]
            cf.writerow([r, tph_avg, hpt_avg])
            

read_file(fb13)
read_file(fb15k)
read_file(wn11)
read_file(wn18)


