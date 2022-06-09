"""create address_id to users

Revision ID: 53cb18b28ac3
Revises: 0b585f136a96
Create Date: 2022-06-09 23:34:04.514198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53cb18b28ac3'
down_revision = '0b585f136a96'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table='users', referent_table='address',
                          local_cols=['address_id'], remote_cols=['id'], ondelete='CASCADE')


def downgrade():
    op.drop_constraint('address_users_fk', table_name='usres')
    op.drop_column('users', 'address_id')
