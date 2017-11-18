"""empty message

Revision ID: 44e074ba7a63
Revises: e1d59006a8c0
Create Date: 2017-11-16 17:25:58.427517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44e074ba7a63'
down_revision = 'e1d59006a8c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tbl_student', 'pin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_student', sa.Column('pin', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    # ### end Alembic commands ###