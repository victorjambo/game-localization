"""empty message

Revision ID: a16eaa2369d6
Revises: 45af207fad57
Create Date: 2022-01-19 01:22:46.240166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a16eaa2369d6'
down_revision = '45af207fad57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('deleted', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games', 'deleted')
    # ### end Alembic commands ###