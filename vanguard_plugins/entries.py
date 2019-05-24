from sqlalchemy import Column, Integer, ForeignKey
from quart.json import jsonify
from quart_openapi import Resource

from vanguard_db import Base, User
from vanguard_api import app, APIPlugin


class Entry(Base):
    __tablename__ = 'entry'

    id = Column('id', Integer, primary_key=True)
    owner = Column('owner', ForeignKey(User.id), nullable=False)


@app.route('/api/v1/entries')
class EntriesResource(Resource, APIPlugin):
    async def get(self):
        """
        Get all entries matching the query
        """
        return jsonify(json_list=app.db_session.query(Entry).all())

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
