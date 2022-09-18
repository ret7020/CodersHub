"""Posts comments

Revision ID: c6556ae31496
Revises: ac946a5c1959
Create Date: 2022-09-18 22:36:02.094706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6556ae31496'
down_revision = 'ac946a5c1959'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post_comments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_post_comments_post_id_post'), 'post', ['post_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post_comments', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_post_comments_post_id_post'), type_='foreignkey')
        batch_op.drop_column('post_id')

    # ### end Alembic commands ###
