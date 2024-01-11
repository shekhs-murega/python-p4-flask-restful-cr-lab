"""creating models

Revision ID: 506b0c83d130
Revises: 67f5d67aea55
Create Date: 2024-01-11 07:03:55.643144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '506b0c83d130'
down_revision = '67f5d67aea55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('plants')
    # ### end Alembic commands ###
