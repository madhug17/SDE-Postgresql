"""developer 1 adds production 

Revision ID: 037ab107ee30
Revises: d866c0a69b8f
Create Date: 2026-11-20 14:35:17.895641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '037ab107ee30'
down_revision: Union[str, Sequence[str], None] = 'd866c0a69b8f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    'products',
    sa.Column('product_id', sa.Integer(), primary_key=True),
    sa.Column('product_name', sa.String(100), nullable=False)
)

def downgrade() -> None:
    op.drop_table('products')
