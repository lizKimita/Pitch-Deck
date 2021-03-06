"""Third Migration

Revision ID: 5851fbcdbe80
Revises: f8643480f982
Create Date: 2019-04-20 13:01:46.824727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5851fbcdbe80'
down_revision = 'f8643480f982'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=255), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
