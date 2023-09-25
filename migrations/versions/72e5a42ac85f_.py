"""empty message

Revision ID: 72e5a42ac85f
Revises: 08f038fa9bd8
Create Date: 2023-09-21 10:50:34.338248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72e5a42ac85f'
down_revision = '08f038fa9bd8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('record_tbl', sa.Column('create_user_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('record_tbl', 'create_user_id')
    # ### end Alembic commands ###