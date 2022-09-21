"""Added property table1

Revision ID: a3dd2cc7fd3b
Revises: 066e4090915b
Create Date: 2022-09-09 12:20:38.139411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3dd2cc7fd3b'
down_revision = '066e4090915b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('propdetails', 'specification',
               existing_type=sa.BOOLEAN(),
               type_=sa.String(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('propdetails', 'specification',
               existing_type=sa.String(),
               type_=sa.BOOLEAN(),
               existing_nullable=True)
    # ### end Alembic commands ###
