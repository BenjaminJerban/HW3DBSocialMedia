from SocialMedia import SocialMedia

class Instagram(SocialMedia):

	def __init__(self, name = "Instagram"):
		super().__init__(name)
		self.posts = [] 
		
	def getPosts(self):
		return self.posts

	def publishNewPost(self):
		post_text = input("Enter your post text :")
		if len(post_text)<2200:
			number=0
			self.posts.append(post_text)
			
			for counter in self.posts:
				number+=1
				print("\nPost num",str(number),"-",counter)
		else :
			print("Error : Your text length is more than valid count")

