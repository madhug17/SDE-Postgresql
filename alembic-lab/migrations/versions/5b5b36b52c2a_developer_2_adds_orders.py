"""developer 2 adds orders

Revision ID: 5b5b36b52c2a
Revises: 037ab107ee30
Create Date: 2026-11-20 14:37:09.212377

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b5b36b52c2a'
down_revision: Union[str, Sequence[str], None] = 'd866c0a69b8f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    'orders',
    sa.Column('order_id', sa.Integer(), primary_key=True),
    sa.Column('order_amount', sa.Integer(), nullable=False)
)


def downgrade() -> None:
    op.drop_table('orders')
