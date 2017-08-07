import os, random, shutil
from TwitterAPI import TwitterAPI

CONSUMER_KEY = 'your_twitter_customer_key'
CONSUMER_SECRET = 'your_twitter_customer_secret'
ACCESS_TOKEN_KEY = 'your_twitter_access_token_key'
ACCESS_TOKEN_SECRET = 'your_twitter_access_token_secret'

location = os.getcwd()

os.chdir(location+'/send')

pic = os.popen('ls')

p = random.sample(pic.readlines(), 1)

t = ''.join(p).split('\n')

f = open(location+"/words.txt", "r")
saved = f.readlines()
which = random.sample(saved, 1)
w = ''.join(which).split('\n')
new = []

for i in range(len(saved)):
	if saved[i] != w[0]+"\n":
		new.append(saved[i])
f.close()

f = open(location+"/words.txt", "w")
f.writelines(new)
f.close()

f = open(location+"/sentposts.txt", "a")
f.write(w[0]+"\n")
f.close()

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
file = open(t[0], 'rb')
data = file.read()
r = api.request('statuses/update_with_media', {'status':w[0]}, {'media[]':data})

k = location+"send"+t[0]

if(r.status_code == 200):
	#If you do not want the shared image to be deleted, open the comment line below and take the delete line as comment. 
	#shutil.move(k, location+"/sent/")
	os.popen('rm -rf ./'+t[0])
	print("ok")
