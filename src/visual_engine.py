def get_visuals(mood, mode="dark"):
    visuals = {
        "happy": {"emoji": "😄", "color": "#2ecc71", "opacity": 0.9},
        "sad": {"emoji": "😔", "color": "#3498db", "opacity": 0.7},
        "neutral": {"emoji": "😐", "color": "#95a5a6", "opacity": 0.8},
    }

    return visuals.get(mood, visuals["neutral"])
