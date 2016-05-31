# -*- coding: utf-8 -*-

import os
import re
import jieba

__init_seg = False


def __init():
    user_dict_path = os.path.join(root_filepath, "f_seg/user_dict.txt")
    jieba.load_userdict(user_dict_path)
    jieba.add_word(u"快递", 10000)
    jieba.suggest_freq((u"面", u"太厚"))
    jieba.suggest_freq((u"价格", u"便宜"))
    jieba.suggest_freq((u"服务", u"周到"))
    jieba.suggest_freq((u"速度", u"快"))


def cut(sentence):
    if not __init_seg:
        __init()
    return jieba.lcut(sentence)

root_filepath = os.path.dirname(os.path.realpath(__file__))
miner_hmm_tag_num_filepath = os.path.normpath(os.path.join(
    root_filepath, "f_hmm/tag_num.txt"))
miner_hmm_init_filepath = os.path.normpath(os.path.join(
    root_filepath, "f_hmm/init_prob.txt"))
miner_hmm_emit_filepath = os.path.normpath(os.path.join(
    root_filepath, "f_hmm/emit_prob.txt"))
miner_hmm_transition_filepath = os.path.normpath(os.path.join(
    root_filepath, "f_hmm/transition_prob.txt"))
# miner_hmm_train_corpus_filepath = os.path.normpath(os.path.join(
#     root_filepath, "f_hmm/hmm_train_corpus.txt"))
# miner_hmm_user_add_corpus_filepath = os.path.normpath(os.path.join(
#     root_filepath, "f_hmm/hmm_user_add_corpus.txt"))

re_clause_findall = re.compile(u"([a-zA-Z0-9:\u4e00-\u9fa5]+[，。%、！!？?,；～~.… ]*)")
re_space_split = re.compile(u"\s+")
re_han_match = re.compile(u'[\s\u4e00-\u9fa5]+')


def final_tag_position(tags, tag, start):
    while start < len(tags):
        if tags[start] != tag:
            break
        start += 1
    return start - 1


