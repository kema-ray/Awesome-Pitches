"""fourth migration

Revision ID: 94aac47efd70
Revises: 891ee8476428
Create Date: 2022-05-10 18:59:41.747334

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94aac47efd70'
down_revision = '891ee8476428'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_secure', sa.String(length=255), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_secure')
    # ### end Alembic commands ###
