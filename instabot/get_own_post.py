import requests
from constants import app_access_token,base_url
import urllib


def get_own_post():
    #https: // api.instagram.com / v1 / users / self / media / recent /?access_token = 4631267286.cOOe824.bOabe1e188f8488fbe0966f5d7d25b88
    #function of logic
    def get_own_post():
        request_url = (base_url + 'users/self/media/recent/?access_token=%s') % (app_access_token)
        print 'GET request url : %s' % (request_url)
        own_media = requests.get(request_url).json()

        if own_media['meta']['code'] == 200:
            if len(own_media['data']):
                    image_name = own_media['data'][0]['id'] + '.jpeg'
                    image_url = own_media['data'][0]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)
                    print 'Your image has been downloaded!'

            else:
                print 'Post does not exist!'
        else:
            print 'Status code other than 200 received!'
