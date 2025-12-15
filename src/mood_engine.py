from collections import Counter

_emotion_memory = []

def update_memory(emotion):
    _emotion_memory.append(emotion)

    if len(_emotion_memory) > 20:
        _emotion_memory.pop(0)

def get_dominant_mood():
    if not _emotion_memory:
        return "neutral"

    return Counter(_emotion_memory).most_common(1)[0][0]
