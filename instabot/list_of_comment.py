
from constants import app_access_token,base_url
from get_post_id import get_post_id
from post_a_comment import post_a_comment

def list_of_comment(insta_username):
    media_id=get_post_id(insta_username)
    request_url=(base_url+'media/%s/comments?access_token=%s')%(media_id,app_access_token)
    print 'Get request url :%s'%(request_url)

    if post_a_comment(insta_username)['meta']['code']==200:
        print "media with media id '()' is comment by following users:".format(media_id)
        for (index,users_comments)in enumerate(post_a_comment()['data']):
            print "%d. %s (%s) - %d "% (index+1,users_comments['full_name':],users_comments['id':],users_comments['username':])
    else:
        print "wrong input plzz try again...."
