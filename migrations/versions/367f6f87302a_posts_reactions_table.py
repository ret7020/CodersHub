"""Posts reactions table

Revision ID: 367f6f87302a
Revises: 985267d51042
Create Date: 2022-09-18 16:50:35.709101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '367f6f87302a'
down_revision = '985267d51042'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_reactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reaction_type', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], name=op.f('fk_post_reactions_post_id_post')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_post_reactions_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_post_reactions'))
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_email'), ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('uq_user_email'), type_='unique')

    op.drop_table('post_reactions')
    # ### end Alembic commands ###
