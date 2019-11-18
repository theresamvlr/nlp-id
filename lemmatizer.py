import json
import re

class lemmatizer:
    def __init__(self):
        with open('kata-dasar.txt') as f:
            self.kata_dasar = set(f.read().splitlines())
        with open ('generated_dict/final_dict.json') as file:
            self.lemma_dict = json.load(file)
    
    def stem1(self, word):
        if word.endswith(('lah','kah','pun')):
            return word[:-3]
        else:
            return word
    
    def stem2(self, word):
        if word.startswith('ku'):
            return word[2:]
        elif word.startswith('kau'):
            return word[3:]
        else:
            return word
        
    def stem3(self, word):
        if word.endswith(('ku','mu')):
            return word[:-2]
        elif word.endswith('nya'):
            return word[:-3]
        else:
            return word
        
    def stem4(self, word):
        if word.endswith('kan'):
            return [word[:-3],word[:-2]]
        elif word.endswith('an'):
            return word[:-2]
        elif word.endswith('i'):
            return word[:-1]
        else:
            return word
    
    def stem5(self, word):
        if word.startswith(('di','ke','se')):
            return word[2:]
        else:
            return word
    
    def lemmatize(self, text):
        final_result = ''
        text = text.lower()
        for word in text.split():
            word = re.sub('[^a-zA-Z0-9-]+','',word)
            result = word.lower()
            if word.isdigit() or len(word)<=3 or word in self.kata_dasar:
                result = word.lower()
            elif word in self.lemma_dict:
                result = self.lemma_dict[word]
            else:
                word1 = self.stem1(word)
                word2 = self.stem2(word)
                word13 = self.stem3(word1)
                word134 = self.stem4(word13) 
                word25 = self.stem5(word2)
                if word1 in self.kata_dasar:
                    result = word1
                elif word1 in self.lemma_dict:
                    result = self.lemma_dict[word1]
                elif word2 in self.kata_dasar:
                    result = word2
                elif word2 in self.lemma_dict:
                    result = self.lemma_dict[word2]
                elif word13 in self.kata_dasar:
                    result = word13
                elif word13 in self.lemma_dict:
                    result = self.lemma_dict[word13]
                elif len(word134)>0 and len(word134[0]) > 1:
                    for word in word134:
                        if word in self.kata_dasar:
                            result = word
                        elif word in self.lemma_dict:
                            result = self.lemma_dict[word]
                elif word134 in self.kata_dasar:
                    result = word134
                elif word134 in self.lemma_dict:
                    result = self.lemma_dict[word134]
                elif word25 in self.kata_dasar:
                    result = word25
                elif word25 in self.lemma_dict:
                    result = self.lemma_dict[word25]
                else:
                    word12 = self.stem2(word1)
                    word125 = self.stem1(word25)
                    if word12 in self.kata_dasar:
                        result = word12
                    elif word12 in self.lemma_dict:
                        result = self.lemma_dict[word12]
                    elif word125 in self.kata_dasar:
                        result = word125
                    elif word125 in self.lemma_dict:
                        result = self.lemma_dict[word125]
                    else:
                        word123 = self.stem3(word12)
                        word1234 = self.stem4(word123)
                        word1235 = self.stem5(word123)
                        if word123 in self.kata_dasar:
                            result = word123
                        elif word123 in self.lemma_dict:
                            result = self.lemma_dict[word123]
                        elif len(word1234)>0 and len(word1234[0]) > 1:
                            for word in word1234:
                                if word in self.kata_dasar:
                                    result = word
                                elif word in self.lemma_dict:
                                    result = self.lemma_dict[word]
                        elif word1234 in self.kata_dasar:
                            result = word1234
                        elif word1234 in self.lemma_dict:
                            result = self.lemma_dict[word1234]
                        elif word1235 in self.kata_dasar:
                            result = word1235
                        elif word1235 in self.lemma_dict:
                            result = self.lemma_dict[word1235]
                        else:
                            word12345 = self.stem5(word1234)
                            if word12345 in self.kata_dasar:
                                result = word12345
                            elif word12345 in self.lemma_dict:
                                result = self.lemma_dict[word12345]
            final_result+=' {}'.format(result)
        return final_result.strip()