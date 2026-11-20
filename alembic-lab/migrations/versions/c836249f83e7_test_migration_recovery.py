"""test migration recovery

Revision ID: c836249f83e7
Revises: 6a3e3a629076
Create Date: 2026-11-20 17:03:22.810421

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c836249f83e7'
down_revision: Union[str, Sequence[str], None] = '6a3e3a629076'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'anime_macha',sa.Column('recovery_test', sa.Integer(), nullable=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
