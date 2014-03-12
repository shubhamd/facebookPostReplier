import requests
import json

      # Make sure you enable publish_stream permissions while querying for access token 
      # get your access token here https://developers.facebook.com/tools/explorer
      # You might have to edit permissions for "who can post on my timline" to 'public' . 

linux_timeStamp = '1393785060' # preferably, this should be the time when your friends start posting to your wall 
TOKEN = "CAACEdEose0cBAFhpqbUjMbOlTOcxRdkkA4cZACyTVcD9HnQ33OqAbVFhStPgeRAro2k5nRhBozBqsawcJJDVKcu0yWW0Qdh4h2AvGHUNdn82uqUOQZCSTfFrFhHBKNs7RkafxqvEvxZAUEvihQBiQzgP4TosAtJoHZCh6lwLZCnO3MoefuVlrGt20jO9sntWQtXqQx7iY6wZDZD"
def list_posts():
   
    query = ("SELECT post_id, actor_id, target_id, message,comments FROM stream WHERE source_id = me() and actor_id != me() AND created_time > 1393785060 limit 200")

            # Response contains dictionary 

    payload = {'q': query, 'access_token': TOKEN}
    r = requests.get('https://graph.facebook.com/fql', params=payload) # Execute the query 
    result = json.loads(r.text)
    return result['data']

def bot(wallposts):
   
    for wallpost in wallposts:

        r = requests.get('https://graph.facebook.com/%s' %
                wallpost['actor_id'])

        url_comments  = 'https://graph.facebook.com/%s/comments' % (wallpost['post_id'])
        url_likes  = 'https://graph.facebook.com/%s/likes' % (wallpost['post_id'])
        user = json.loads(r.text)
        if wallpost['comments']['count'] is 0 :    # comment only when you haven't commented before 

            message = 'Thanks ! :D'                                     # comment text 
            payload = {'access_token': TOKEN, 'message': message}
            s = requests.post(url_comments, data=payload)                        # post your comment 
            s = requests.post(url_likes ,data= { 'access_token':TOKEN });     # like friend's post 
            print "Commented and liked %s 's post. " % (user['name'])   # log to the console 
            break 

if __name__ == '__main__':
    bot(list_posts())

