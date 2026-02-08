from mrjob.job import MRJob

class AvgRating(MRJob):
    def mapper(self, _, line):
        try:
            row = line.split(',')
            if row[0] != 'userId':
                yield row[1], float(row[2])
        except:
            pass

    def reducer(self, key, values):
        total = 0
        count = 0
        for v in values:
            total += v
            count += 1
        if count > 0:
            yield key, total / count

if __name__ == '__main__':
    AvgRating.run()