import requests
from constants import app_access_token,base_url
from get_post_id import get_post_id

def list_of_comment(insta_username):
    media_id=get_post_id(insta_username)
    request_url=(base_url+'media/%s/comment?access_token=$s')%(media_id,app_access_token)
    print 'Get request url :%s'%(request_url)
    get_a_comment=requests.get(request_url).json()
    if get_a_comment['meta']['code']==200:
        print "media with media id '()' is comment by following user:".format(media_id)
        for (index,user_comment)in enumerate(get_a_comment['data']):
            print "{ }.{ } ({ }) -{}".format(index+1,user_comment['full_name'],user_comment['id'],user_comment['username'])
    else:
        print "wrong input plzz try again...."
