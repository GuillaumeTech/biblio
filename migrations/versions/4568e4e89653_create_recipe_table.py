"""create recipe table

Revision ID: 4568e4e89653
Revises: 
Create Date: 2022-12-02 19:30:30.921232

"""
from alembic import op
import sqlalchemy as sa 
from sqlalchemy.dialects.postgresql import ARRAY
# revision identifiers, used by Alembic.
revision = '4568e4e89653'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'recipe',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('link', sa.String, nullable=False),
        sa.Column('image', sa.String, nullable=True),
        sa.Column('ingredients', ARRAY(sa.String,dimensions=1), nullable=True),
        sa.Column('cook_time', sa.String, nullable=True),
        sa.Column('prep_time', sa.String, nullable=True),
        sa.Column('rest_time', sa.String, nullable=True),
    )
    pass


def downgrade() -> None:
    op.drop_table('recipe')
    pass
