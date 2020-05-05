"""Add trimestamp to cocktail

Revision ID: 6d9477c1330e
Revises: aacc36dde219
Create Date: 2020-04-19 13:27:51.799652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d9477c1330e'
down_revision = 'aacc36dde219'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cocktail', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_cocktail_timestamp'), 'cocktail', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cocktail_timestamp'), table_name='cocktail')
    op.drop_column('cocktail', 'timestamp')
    # ### end Alembic commands ###