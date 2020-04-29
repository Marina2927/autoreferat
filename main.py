from rutermextract import TermExtractor
import codecs
import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

text = []
procent = 20

def check(text, new_text, k):
    sym_cnt_0 = 0
    sym_cnt = 0
    for part in text:
        sym_cnt_0 += len(part)
    for part in new_text:
        sym_cnt += len(part)
    m = sym_cnt_0 * (100 - k) / 100
    #print(sym_cnt_0)
    #print(sym_cnt)
    return sym_cnt <= m

fin = codecs.open("text.txt", "r", "utf-8")
data = fin.read()
text = list(tokenizer.tokenize(data))

keywords_0 = []
keywords_cnt_0 = []

term_extractor = TermExtractor()
for term in term_extractor(data):
    #print(term.normalized, term.count)
    if term.count > 1:
        keywords_0.append(term.normalized)
        keywords_cnt_0.append(term.count)

print(keywords_0)
print(keywords_cnt_0)

file.close()

def del_sent(text, k):
    if k == 0:
        keywords = keywords_0[:]
        keywords_cnt = keywords_cnt_0[:]
    else:
        keywords = keywords_0[:k]
        keywords_cnt = keywords_cnt_0[:k]
    print(keywords)
    print(keywords_cnt)

    for sent in new_text:
        cnt = 0
        for term in term_extractor(sent):
            if term.normalized in keywords:
                cnt += 1
        if cnt == 0:
            new_text.remove(sent)
        if check(text, new_text, procent):
            return new_text

    return new_text

new_text = text[:]

k = 0

while not check(text, new_text, procent):
    new_text = del_sent(text, k)
    k -= 1

def output(text):
    fout = codecs.open("output.txt", "w", "utf-8")

    for sent in new_text:
        fout.write(sent)
        fout.write(" ")
    fout.close()

output(new_text)


