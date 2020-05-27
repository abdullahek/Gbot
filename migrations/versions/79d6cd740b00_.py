"""empty message

Revision ID: 79d6cd740b00
Revises: 
Create Date: 2020-05-27 14:35:25.373043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79d6cd740b00'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.String(length=4096), nullable=True),
    sa.Column('user_input', sa.String(length=4096), nullable=True),
    sa.Column('date', sa.String(length=4096), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gdata')
    # ### end Alembic commands ###
