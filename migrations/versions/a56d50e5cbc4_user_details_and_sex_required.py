"""user details and sex required

Revision ID: a56d50e5cbc4
Revises: 7d4bab0acebb
Create Date: 2017-09-14 16:36:05.071303

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a56d50e5cbc4'
down_revision = '7d4bab0acebb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('patients', 'sex',
               existing_type=sa.VARCHAR(length=1),
               nullable=False)
    op.alter_column('users', 'f_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('users', 'l_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'l_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('users', 'f_name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('patients', 'sex',
               existing_type=sa.VARCHAR(length=1),
               nullable=True)
    # ### end Alembic commands ###
