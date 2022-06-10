"""Create address table

Revision ID: 0b585f136a96
Revises: e88fa208b2b2
Create Date: 2022-06-09 23:25:57.680708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b585f136a96'
down_revision = 'e88fa208b2b2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(), nullable=False),
                    sa.Column('address2', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False),
                    sa.Column('postalcode', sa.String(), nullable=False),
                    )


def downgrade():
    op.drop_table('address')
