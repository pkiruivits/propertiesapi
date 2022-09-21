"""Added property table1

Revision ID: 319577964900
Revises: 
Create Date: 2022-09-08 12:32:04.716304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '319577964900'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_items_description'), 'items', ['description'], unique=False)
    op.create_index(op.f('ix_items_id'), 'items', ['id'], unique=False)
    op.create_index(op.f('ix_items_title'), 'items', ['title'], unique=False)
    op.create_table('propdetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('specification', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_propdetails_id'), 'propdetails', ['id'], unique=False)
    op.create_index(op.f('ix_propdetails_name'), 'propdetails', ['name'], unique=True)
    op.create_table('smsinbound',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Request_id', sa.String(), nullable=True),
    sa.Column('display_phone', sa.String(), nullable=True),
    sa.Column('phone_no_id', sa.String(), nullable=True),
    sa.Column('contact_name', sa.String(), nullable=True),
    sa.Column('contact_wa_id', sa.String(), nullable=True),
    sa.Column('sms_id', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('text_body', sa.String(), nullable=True),
    sa.Column('list_reply_id', sa.String(), nullable=True),
    sa.Column('reply_tittle', sa.String(), nullable=True),
    sa.Column('reply_description', sa.String(), nullable=True),
    sa.Column('replied', sa.Boolean(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('sms_id')
    )
    op.create_index(op.f('ix_smsinbound_Request_id'), 'smsinbound', ['Request_id'], unique=False)
    op.create_index(op.f('ix_smsinbound_id'), 'smsinbound', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('verifyurl',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hub_mode', sa.String(), nullable=True),
    sa.Column('hub_challenge', sa.String(), nullable=True),
    sa.Column('hub_verify_token', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_verifyurl_hub_verify_token'), 'verifyurl', ['hub_verify_token'], unique=True)
    op.create_index(op.f('ix_verifyurl_id'), 'verifyurl', ['id'], unique=False)
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('property_id', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['property_id'], ['propdetails.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_images_id'), 'images', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_images_id'), table_name='images')
    op.drop_table('images')
    op.drop_index(op.f('ix_verifyurl_id'), table_name='verifyurl')
    op.drop_index(op.f('ix_verifyurl_hub_verify_token'), table_name='verifyurl')
    op.drop_table('verifyurl')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_smsinbound_id'), table_name='smsinbound')
    op.drop_index(op.f('ix_smsinbound_Request_id'), table_name='smsinbound')
    op.drop_table('smsinbound')
    op.drop_index(op.f('ix_propdetails_name'), table_name='propdetails')
    op.drop_index(op.f('ix_propdetails_id'), table_name='propdetails')
    op.drop_table('propdetails')
    op.drop_index(op.f('ix_items_title'), table_name='items')
    op.drop_index(op.f('ix_items_id'), table_name='items')
    op.drop_index(op.f('ix_items_description'), table_name='items')
    op.drop_table('items')
    # ### end Alembic commands ###
