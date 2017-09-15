import Assignment_2a as ass2a
import random

class RandomStory():
    def __init__(self,my_file,n_gram):
        self.file = my_file
        self.n_gram = n_gram
        self.dict_word = {}
        self.story = ""

    def train(self):
        if self.n_gram == 1:
            self.dict_word = ass2a.unigrams(self.file)
        if self.n_gram == 2:
            self.dict_word = ass2a.bigrams(self.file)
        if self.n_gram == 3:
            self.dict_word = ass2a.trigrams(self.file)

    def generate(self,num_words):
        #self.story = ass2a.make_random_story(self.file,self.n_gram,num_words)
        random.seed('Is the looking-glass is half full or half-empty?')
        story = list(random.choice(self.dict_word.keys()))
        while len(story) < num_words:
            if self.n_gram > 1:
                previous_words = tuple(story[-(self.n_gram-1):])
            else:
                previous_words = ()
            story.append(random.choice(self.dict_word[(previous_words)]))
        self.story = ' '.join(story)
