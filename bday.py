import requests
import json


AFTER = 1353233754
TOKEN = 'CAACEdEose0cBADbU7ZBlNxi46WZAZA6A2vaJYmfbUclR7daqxsQZA8GDrjZCy3NPIGXCD4WL0Vh9MvmXZCiimX1e24pSKYWftKUZB22vQjp5Ly3YTvjP66NR0iZBMTldNfCCLCZBHQmuh4oBOUlqSFpkJWZB3IN3mTVWW7TKW0M0RR7x8fcK1fHX7tvpNnzHkUL7ekmgq1xWGI2wZDZD'

def get_posts():
    """Returns dictionary of id, first names of people who posted on my wall
    between start and end time"""
    query = ("SELECT post_id, actor_id, target_id, message,likes,comments FROM stream WHERE source_id = me() and actor_id != me() AND created_time > 1393785060 limit 200")

            

    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload)
    result = json.loads(r.text)
    print result['data']
    return result['data']

def commentall(wallposts):
   
    for wallpost in wallposts:

        r = requests.get('https://graph.facebook.com/%s' %
                wallpost['actor_id'])
        url = 'https://graph.facebook.com/%s/comments' % wallpost['post_id']
        user = json.loads(r.text)
        if wallpost['comments']['count'] is 0 :

            message = 'Thanks ! :D' 
            payload = {'access_token': TOKEN, 'message': message}
            s = requests.post(url, data=payload)
            print "s is ",s.text 
            print "Wall post %s done for user id %s" % (wallpost['post_id'],wallpost['actor_id'])
            

if __name__ == '__main__':
    commentall(get_posts())

