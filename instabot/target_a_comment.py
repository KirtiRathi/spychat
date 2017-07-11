import requests
import urllib
from constants import app_access_token,base_url
from get_user_id import get_user_id
from post_a_comment import post_a_comment





def target_a_comment(insta_username):
    #function of logic
    user_id=get_user_id(insta_username)
    print user_id
    request_url = (base_url+'users/%s/media/recent/?access_token=%s')%(user_id,app_access_token)
    print 'GET request url : %s' %(request_url)
    user_media = requests.get(request_url).json()
    print user_media
    service = ['clothes','coffee','ice-cream','pizza']
    for post in user_media['data']:
        print post

        for serve in service:
            if post['caption'] == None:
                print "This post has no caption"
            else:
                if serve in post['caption']['text']:
                    post_a_comment(insta_username)


