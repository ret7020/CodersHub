"""Posts reactions table

Revision ID: 19d12ce366b9
Revises: 367f6f87302a
Create Date: 2022-09-18 16:57:23.726533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19d12ce366b9'
down_revision = '367f6f87302a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post_reactions', schema=None) as batch_op:
        batch_op.drop_constraint('fk_post_reactions_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post_reactions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_post_reactions_user_id_user', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###
