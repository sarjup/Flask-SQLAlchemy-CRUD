"""empty message

Revision ID: 303f14d5aa6b
Revises: e6d8fff7f9df
Create Date: 2017-11-16 23:18:30.912071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '303f14d5aa6b'
down_revision = 'e6d8fff7f9df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'tbl_student_id_key', 'tbl_student', type_='unique')
    op.create_unique_constraint(None, 'tbl_student', ['pin'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tbl_student', type_='unique')
    op.create_unique_constraint(u'tbl_student_id_key', 'tbl_student', ['id'])
    # ### end Alembic commands ###