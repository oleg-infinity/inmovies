"""empty message

Revision ID: 3ae28a74be69
Revises: c1b2d5df88c8
Create Date: 2024-03-14 19:29:24.611790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ae28a74be69'
down_revision = 'c1b2d5df88c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_user')
    op.drop_table('second_model')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=True))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.create_unique_constraint('uq_email', ['email'])  # Assign name to unique constraint
        batch_op.drop_column('nickname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nickname', sa.VARCHAR(length=80), nullable=True))
        batch_op.drop_constraint('uq_email', type_='unique')  # Specify the name of the unique constraint to drop
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.drop_column('is_active')

    op.create_table('second_model',
    sa.Column('id', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('_alembic_tmp_user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), nullable=False),
    sa.Column('password', sa.VARCHAR(length=120), nullable=False),
    sa.Column('role', sa.INTEGER(), nullable=True),
    sa.Column('slug', sa.VARCHAR(length=50), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.Column('nickname', sa.VARCHAR(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email', name='uq_email'),  # Adjust name for unique constraint
    sa.UniqueConstraint('nickname', name='uq_nickname'),
    sa.UniqueConstraint('slug'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###