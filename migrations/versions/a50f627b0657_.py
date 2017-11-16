"""empty message

Revision ID: a50f627b0657
Revises: f0bcbdcfb55f
Create Date: 2017-11-16 15:54:02.758882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a50f627b0657'
down_revision = 'f0bcbdcfb55f'
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
