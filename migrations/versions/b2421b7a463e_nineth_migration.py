"""Nineth Migration

Revision ID: b2421b7a463e
Revises: e21c5531d02e
Create Date: 2022-05-12 00:04:58.035156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2421b7a463e'
down_revision = 'e21c5531d02e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_pitch_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'pitches', ['pitch_id'], ['id'])
    op.drop_column('comments', 'pitch')
    op.add_column('pitches', sa.Column('posted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'posted')
    op.add_column('comments', sa.Column('pitch', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_pitch_fkey', 'comments', 'pitches', ['pitch'], ['id'])
    op.drop_column('comments', 'pitch_id')
    # ### end Alembic commands ###