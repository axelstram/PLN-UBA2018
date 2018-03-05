from sentiment.tass import GeneralTASSReader, InterTASSReader
from collections import defaultdict




if __name__ == '__main__':
	interTASSReader = InterTASSReader('TASS/InterTASS/tw_faces4tassTrain1000rc.xml')
	generalTASSReader = GeneralTASSReader('TASS/GeneralTASS/general-tweets-train-tagged.xml')

	print('InterTASS statistics:')
	print('====================================')

	tweets = list(interTASSReader.tweets())
	tweets_polarity = defaultdict(int)

	for polarity in interTASSReader.y():
		tweets_polarity[polarity] += 1

	print('Total amount of tweets: ' + str(len(tweets)))
	print('Tweets with [P] polarity: ' + str(tweets_polarity['P']))
	print('Tweets with [N] polarity: ' + str(tweets_polarity['N']))
	print('Tweets with [NEU] polarity: ' + str(tweets_polarity['NEU']))
	print('Tweets with [NONE] polarity: ' + str(tweets_polarity['NONE']))


	print(' ')
	print('GeneralTASS statistics:')
	print('====================================')
	
	tweets = list(generalTASSReader.tweets())
	tweets_polarity = defaultdict(int)

	for polarity in generalTASSReader.y():
		tweets_polarity[polarity] += 1

	print('Total amount of tweets: ' + str(len(tweets)))
	print('Tweets with [P] polarity: ' + str(tweets_polarity['P']))
	print('Tweets with [N] polarity: ' + str(tweets_polarity['N']))
	print('Tweets with [NEU] polarity: ' + str(tweets_polarity['NEU']))
	print('Tweets with [NONE] polarity: ' + str(tweets_polarity['NONE']))