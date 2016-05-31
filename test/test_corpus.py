# -*- coding: utf-8 -*-

from fgom2.corpus import *
from fgom2 import HMM


def test_GetToTagCorpus():
    input_filename = "files/waimai_corpus.txt"
    output_filepath = "files/tag_corpus/"

    corpus = GetToTagCorpus(input_filename, output_filepath)
    corpus.run()


def test_GetTaggedCorpus():
    input_filepath = "files/tagged_corpus/"
    output_filename = "files/hmm_train_corpus.txt"

    corpus = GetTaggedCorpus(input_filepath, output_filename)
    corpus.run()


def test_BootstrappingMaster():
    bootstrapping_filename = "files/bootstrap_corpus.txt"
    origin_tag_filename = "files/hmm_train_corpus.txt"

    bootstrap = BootstrappingMaster(bootstrapping_filename, origin_tag_filename)
    bootstrap.run()


def test_train_OpinionMinerHMM():
    corpus_filename = "files/hmm_train_corpus.txt"

    HMM.train(corpus_filename)

    sentence = u"味道好，送餐快，分量足"
    print(HMM.tag(sentence))
    print(["%s/%s" % (word, tag) for word, tag in HMM.tag(sentence, False)])


def test_use_OpinionMinerHMM():
    sentence = u"味道好，送餐快，分量足"
    print(HMM.tag(sentence))
    print(["%s/%s" % (word, tag) for word, tag in HMM.tag(sentence, False)])

    print(HMM.parse(sentence))

if __name__ == "__main__":
    pass
    # test_GetToTagCorpus()
    # test_GetTaggedCorpus()
    # test_BootstrappingMaster()
    test_train_OpinionMinerHMM()
    test_use_OpinionMinerHMM()

