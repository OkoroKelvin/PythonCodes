# g = open('wasteland.txt', mode='rt', encoding='utf-8')
# print(g.read())
# print(g.read())
# print(g.seek(0))
# print(g.readline())
# print(g.readline())
# g.seek(0)
# print(g.readlines())
# g.close()
# h = open('wasteland.txt', mode='at', encoding='utf-8')
# h.writelines(['I shall be called a Softwarer Engineer and a boitech Engineer,\n', ''
#                                                                                   'tHe future is rewarding and i am excited to be among the creation,'                                                                           'i have a dream'])
# h.close()
import sys

f = open(sys.argv[1], mode='rt', encoding='utf-8')
for line in f:
    sys.stdout.write(line)
f.close()

