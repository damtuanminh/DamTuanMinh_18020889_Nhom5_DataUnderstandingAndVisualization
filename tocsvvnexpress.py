import pandas as pd
data = pd.read_json('/Users/minhdam/PycharmProjects/test/visualization/visualization/spiders/Output/vnexpress.txt', lines=True)
data.to_csv('/Users/minhdam/PycharmProjects/test/visualization/visualization/spiders/Output/vnexpress.csv', encoding='utf8')
