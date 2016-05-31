# -*- coding: utf-8 -*-

with open("test", "w")as f:
    f.write("%s" % u"你好".encode("utf-8"))


with open("test") as f:
    print(f.read().decode("utf-8"))


