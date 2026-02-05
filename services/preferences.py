from models.user import User
from database import db

ALLOWED_QUALITIES = ['480p', '720p', '1080p', '4k']
ALLOWED_SUBTITLE_SIZES = ['small', 'medium', 'large']

def validate_preferences(data):
    if not isinstance(data, dict):
        return None
    validated = {}
    if 'quality' in data and data['quality'] in ALLOWED_QUALITIES:
        validated['quality'] = data['quality']
    if 'subtitles_enabled' in data:
        validated['subtitles_enabled'] = bool(data['subtitles_enabled'])
    if 'subtitle_language' in data:
        validated['subtitle_language'] = str(data['subtitle_language'])[:5]
    if 'subtitle_size' in data and data['subtitle_size'] in ALLOWED_SUBTITLE_SIZES:
        validated['subtitle_size'] = data['subtitle_size']
    if 'autoplay' in data:
        validated['autoplay'] = bool(data['autoplay'])
    return validated if validated else None

def save_user_preferences(user_id, preferences):
    user = User.query.get(user_id)
    if user:
        current_prefs = user.preferences or {}
        current_prefs.update(preferences)
        user.preferences = current_prefs
        db.session.commit()
