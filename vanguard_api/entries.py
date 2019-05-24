from quart.json import jsonify
from quart_openapi import Resource

from .app import app


@app.route('/api/v1/entries')
class EntriesResource(Resource):
    async def get(self):
        """
        Get all entries matching the query
        """
        return jsonify({'status': 'Not implemented'})

    async def post(self):
        """
        Submit new entries
        """
        return jsonify({'status': 'Not implemented'})

    async def delete(self):
        """
        Delete entries
        """
        return jsonify({'status': 'Not implemented'})


@app.route('/api/v1/treatments')
class TreatmentsResource(Resource):
    async def get(self):
        """
        Get all treatments matching the query
        """
        return jsonify({'status': 'Not implemented'})

    async def post(self):
        """
        Submit new treatments
        """
        return jsonify({'status': 'Not implemented'})

    async def delete(self):
        """
        Delete treatments
        """
        return jsonify({'status': 'Not implemented'})
