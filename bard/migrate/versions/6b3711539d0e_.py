"""empty message

Revision ID: 6b3711539d0e
Revises: 3640ab086153
Create Date: 2021-05-21 23:21:51.930715

"""

# revision identifiers, used by Alembic.
revision = '6b3711539d0e'
down_revision = '3640ab086153'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('document', sa.Column('content_hash', sa.Unicode(length=65), nullable=True))
    op.create_index(op.f('ix_document_content_hash'), 'document', ['content_hash'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_document_content_hash'), table_name='document')
    op.drop_column('document', 'content_hash')
    # ### end Alembic commands ###
