from SocialMedia import SocialMedia

class Twitter(SocialMedia):

	def __init__(self, name = "Twitter"):
		super().__init__(name)
		self.tweets = [] 
		
	def getTweets(self):
		return self.tweets

	def createNewTweet(self):
		tweet_text = input("Enter your tweet text :")
		if len(tweet_text)<280:
			number=0
			self.tweets.append(tweet_text)
			
			for counter in self.tweets:
				number+=1
				print("\nTweet num",str(number),"-",counter)
		else :
			print("Error : Your text length is more than valid count")

