import re

def remove_mentions(text):
    return re.sub(r'<[^>]*>', '', text)

def generate_message(pattern, content, author):
    return pattern.replace('{message}', content).replace('{author}', author)