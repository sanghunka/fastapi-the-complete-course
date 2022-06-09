"""create phone number for user col

Revision ID: e88fa208b2b2
Revises: 
Create Date: 2022-06-09 22:46:00.663732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e88fa208b2b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users', 'phone_number')
