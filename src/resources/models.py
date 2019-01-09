from datetime import datetime
from main import db
from sqlalchemy.dialects.postgresql import JSON


class Resource(db.Model):

    __tablename__ = 'resources'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), index=True)
    label = db.Column(db.String(255))
    status = db.Column(db.String(50), default='AVAILABLE', index=True)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.now, index=True)

    def __repr__(self):
        return '<Resource {} {} {} {} {}>'.format(self.id, self.type, self.label, self.status, self.updated_at)

    def json(self):
        return {
            'id': self.id,
            'barcode': 'https://barcode.needish.com/qr/%s' % (self.id),
            'type': self.type,
            'label': self.label,
            'status': self.status,
            'updated_at': self.updated_at,
        }

    def save(self):
        self.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.session.add(self)
        return db.session.commit()
