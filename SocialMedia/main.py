from Instagram import Instagram
from Twitter import Twitter

twitter = Twitter()
instagram = Instagram()

def menuBar():
	
	print("\nChoose an option :")
	print("1- Instagram")
	print("2- Twitter")
	print("3- Watch tweets")
	print("4- Watch posts")
	print("Press 'q' to Quit")



def chooseApplication(choose_app):
    return {
        '1': instagram.getName(),
        '2': twitter.getName(),
        '3': "(Watch Twitter tweets)",
        '4': "(Watch Instagram posts)",
    }.get(choose_app,"Invalid Input")

while True :
	menuBar()
	choose_app = input("your choice :")
	if choose_app != 'q':
		
		print("You Chose :", chooseApplication(choose_app))
		
		if chooseApplication(choose_app) == "Instagram":
			instagram.publishNewPost()
		elif chooseApplication(choose_app) == "Twitter":
			twitter.createNewTweet()
		elif chooseApplication(choose_app) == "(Watch Twitter tweets)":
			print("\nYour all tweets are :",twitter.getTweets())
		elif chooseApplication(choose_app) == "(Watch Instagram posts)":
			print("\nYour all posts are :",instagram.getPosts())

	else :
		break


