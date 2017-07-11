import requests
from constants import app_access_token,base_url
def get_user_id(insta_username):
    #function of logic

    request_url = (base_url + 'users/search?q=%s&access_token=%s') % (insta_username, app_access_token)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print user_info['data'][0]['id']
            return user_info['data'][0]['id']
        else:
            print "User not found"
            exit(0)
    else:
        print 'Status code other than 200 received!'
        exit(0)
