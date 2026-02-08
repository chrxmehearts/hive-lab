from mrjob.job import MRJob
import csv

class MovieTitleAvg(MRJob):
    def mapper(self, _, line):
        try:
            row = next(csv.reader([line]))

            if len(row) == 3 and row[0] != 'movieId':
                yield row[0], ('M', row[1])

            elif len(row) == 4 and row[0] != 'userId':
                yield row[1], ('R', float(row[2])) 
        except:
            pass

    def reducer(self, key, values):
        title = None
        rating_sum = 0
        rating_count = 0

        for type_label, value in values:
            if type_label == 'M':
                title = value
            elif type_label == 'R':
                rating_sum += value
                rating_count += 1

        if title and rating_count > 0:
            yield title, rating_sum / rating_count

if __name__ == '__main__':
    MovieTitleAvg.run()