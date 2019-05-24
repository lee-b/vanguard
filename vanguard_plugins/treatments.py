from sqlalchemy import Column, Integer, ForeignKey
from quart.json import jsonify
from quart_openapi import Resource

from vanguard_db import Base, User
from vanguard_api import app, APIPlugin


class Treatment(Base):
    __tablename__ = 'treatment'

    id = Column('id', Integer, primary_key=True)
    owner = Column('owner', ForeignKey(User.id), nullable=False)


@app.route('/api/v1/treatments')
class TreatmentsResource(Resource, APIPlugin):
    async def get(self):
        """
        Get all treatments matching the query
        """
        return jsonify(json_list=app.db_session.query(Treatment).all())

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
