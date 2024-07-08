import re

def remove_mentions(text):
    return re.sub(r'<[^>]*>', '', text)

def generate_message(pattern, message):
    return pattern.replace('{message}', message.content).replace('{author}', message.author.display_name)