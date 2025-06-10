import json
import os

INPUT_DIR = 'data/discourse_json'
OUTPUT_FILE = 'data/processed_posts.json'

def preprocess():
    posts = []

    for filename in os.listdir(INPUT_DIR):
        if filename.endswith('.json'):
            with open(os.path.join(INPUT_DIR, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                for post in data:
                    posts.append({
                        'id': post.get('id'),
                        'topic_id': post.get('topic_id'),
                        'username': post.get('username'),
                        'raw': post.get('raw'),
                        'created_at': post.get('created_at')
                    })

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

    print(f"✅ Processed {len(posts)} posts.")
    print(f"📁 Saved to: {OUTPUT_FILE}")

if __name__ == '__main__':
    preprocess()
