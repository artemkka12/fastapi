"""items_image_path

Revision ID: 73e7d19a1cfb
Revises: c60bd5c40c22
Create Date: 2023-02-16 17:21:37.987471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73e7d19a1cfb'
down_revision = 'c60bd5c40c22'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('image_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'image_path')
    # ### end Alembic commands ###