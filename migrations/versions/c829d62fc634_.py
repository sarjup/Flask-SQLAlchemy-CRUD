"""empty message

Revision ID: c829d62fc634
Revises: b989086429b9
Create Date: 2017-11-16 15:49:22.159110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c829d62fc634'
down_revision = 'b989086429b9'
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