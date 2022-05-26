import json


def get_posts(s=''):
    try:
        with open('posts.json', 'r', encoding='utf-8') as f:
            if s: return [post for post in json.load(f) if s.lower() in post['content'].lower()]
            else: return json.load(f)
    except:
        return []

def add_post(post):
    posts = get_posts()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)




