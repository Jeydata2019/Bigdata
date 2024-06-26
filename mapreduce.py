from mrjob.job import MRJob
from mrjob.step import MRStep
import re

# This is a pattern to find words
WORD_RE = re.compile(r"[\w']+")

class MRWordCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   reducer=self.reducer_count_words)
        ]

    # Mapper looks at each line and finds words
    def mapper_get_words(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    # Reducer counts all the "1"s for each word
    def reducer_count_words(self, word, counts):
        yield (word, sum(counts))

if __name__ == '__main__':
    MRWordCount.run()
