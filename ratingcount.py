from mrjob.job import MRJob
class RatingCount(MRJob):
    def mapper(self, _, line):
        try:
            row = line.split(',')
            if row[2] != 'rating':
                yield row[2], 1
        except:
            pass
    def reducer(self, key, values):
        yield key, sum(values)
if __name__ == '__main__':
    RatingCount.run()