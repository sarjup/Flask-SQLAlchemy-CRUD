"""empty message

Revision ID: e6d8fff7f9df
Revises: 44e074ba7a63
Create Date: 2017-11-16 17:26:20.525236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6d8fff7f9df'
down_revision = '44e074ba7a63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tbl_student', sa.Column('pin', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tbl_student', 'pin')
    # ### end Alembic commands ###
