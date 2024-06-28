from mrjob.job import MRJob
from mrjob.step import MRStep

class MRWordCount(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   reducer=self.reducer_count_words)
        ]
    
    def mapper_get_words(self, _, line):
        # 將每一行的單詞拆分
        for word in line.split():
            yield word.lower(), 1
    
    def reducer_count_words(self, word, counts):
        # 將具有相同單詞的值相加
        yield word, sum(counts)

if __name__ == '__main__':
    MRWordCount.run()
