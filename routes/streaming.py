from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from models.movie import Movie
from services.cdn import get_stream_url
import logging

streaming_bp = Blueprint('streaming', __name__)
logger = logging.getLogger(__name__)

@streaming_bp.route('/api/movies', methods=['GET'])
@login_required
def list_movies():
    page = request.args.get('page', 1, type=int)
    movies = Movie.query.paginate(page=page, per_page=20)
    return jsonify([m.to_dict() for m in movies.items])

@streaming_bp.route('/api/stream/<int:movie_id>', methods=['GET'])
@login_required
def get_stream(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    quality = current_user.preferences.get('quality', '1080p')
    stream_url = get_stream_url(movie.cdn_path, quality)
    logger.info(f'User {current_user.id} streaming movie {movie_id}')
    return jsonify({'stream_url': stream_url, 'title': movie.title})
