class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        ban, punc, count = set(banned), set(string.punctuation), {}
        para = list(paragraph)
        for i in range(len(paragraph)):
            if para[i] in punc: para[i] = ' '
        para = ''.join(para).split(' ')
        for word in para: 
            if word.lower() in ban or word.lower() == '': continue
            count[word.lower()] = count.get(word.lower(),0)+1
        jojo = max(list(count.values()))
        for key in list(count.keys()):
            if count[key] == jojo: return key
