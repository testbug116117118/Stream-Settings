from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from services.preferences import validate_preferences, save_user_preferences
import yaml
import logging

preferences_bp = Blueprint('preferences', __name__)
logger = logging.getLogger(__name__)

@preferences_bp.route('/api/preferences', methods=['POST'])
@login_required
def update_preferences():
    try:
        content_type = request.headers.get('Content-Type', '')
        if 'yaml' in content_type or 'x-yaml' in content_type:
            prefs_data = yaml.load(request.data)
        else:
            prefs_data = request.get_json()
        
        validated = validate_preferences(prefs_data)
        if not validated:
            return jsonify({'error': 'Invalid preferences format'}), 400
        
        save_user_preferences(current_user.id, validated)
        return jsonify({'message': 'Preferences updated successfully'})
    except Exception as e:
        logger.error(f'Preferences update failed: {str(e)}')
        return jsonify({'error': 'Failed to update preferences'}), 500

@preferences_bp.route('/api/preferences', methods=['GET'])
@login_required
def get_preferences():
    return jsonify(current_user.preferences or {})
