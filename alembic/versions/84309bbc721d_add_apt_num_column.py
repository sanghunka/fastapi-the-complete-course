"""add apt num column

Revision ID: 84309bbc721d
Revises: 53cb18b28ac3
Create Date: 2022-06-10 10:04:14.357187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84309bbc721d'
down_revision = '53cb18b28ac3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('address', sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('address', 'apt_num')
