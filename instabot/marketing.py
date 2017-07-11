import  requests
import urllib
from constants import app_access_token,base_url
from get_user_id import get_user_id
from post_a_comment import post_a_comment

#insta_username="jyotithakur15111"


def target_a_comment(insta_username):
    #function of logic
    user_id=get_user_id(insta_username)
    request_url=(base_url+'user/%s/media/recent/?access_token=%s')%(user_id,app_access_token)

    print 'GET request url : %s'%(request_url)
    user_media=requests.get(request_url).json()

    service=['clothes','coffee','ice-cream','pizza']
    for post in user_media['data']:
        for serve in service:
            if service in post ['caption']['text']:
                post_a_comment(insta_username)

            else:
                print'Error'
target_a_comment(insta_username)
