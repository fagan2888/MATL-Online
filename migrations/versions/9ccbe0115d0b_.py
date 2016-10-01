"""empty message

Revision ID: 9ccbe0115d0b
Revises: 5688ce609630
Create Date: 2016-09-17 15:30:24.608725

"""

# revision identifiers, used by Alembic.
revision = '9ccbe0115d0b'
down_revision = '5688ce609630'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('se_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('profile_url', sa.String(), nullable=True),
    sa.Column('avatar_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_se_users_user_id'), 'se_users', ['user_id'], unique=False)
    op.create_table('answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answer_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('accepted', sa.Boolean(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('demo_url', sa.String(), nullable=True),
    sa.Column('source_code', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['se_users.user_id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('answer_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answers')
    op.drop_index(op.f('ix_se_users_user_id'), table_name='se_users')
    op.drop_table('se_users')
    ### end Alembic commands ###
