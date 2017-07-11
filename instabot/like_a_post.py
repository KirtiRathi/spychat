import requests
from constants import app_access_token,base_url
from get_post_id import get_post_id

def like_a_post(insta_username):
  #function of logic
  media_id = get_post_id(insta_username)
  request_url = (base_url + 'media/%s/likes') % (media_id)
  payload = {"access_token": app_access_token}
  print 'POST request url : %s' % (request_url)
  post_a_like = requests.post(request_url, payload).json()
  print 'post liked sucessfully'