"""Picture

Revision ID: 39e99a4900f1
Revises: 6d9477c1330e
Create Date: 2020-05-01 16:30:32.492441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39e99a4900f1'
down_revision = '6d9477c1330e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cocktail', sa.Column('picture', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_cocktail_picture'), 'cocktail', ['picture'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cocktail_picture'), table_name='cocktail')
    op.drop_column('cocktail', 'picture')
    # ### end Alembic commands ###
