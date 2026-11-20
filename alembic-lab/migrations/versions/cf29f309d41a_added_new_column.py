
"""added new column

Revision ID: cf29f309d41a
Revises: d16e18bb72b9
Create Date: 2026-11-20 15:25:30.042363
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'cf29f309d41a'
down_revision: Union[str, Sequence[str], None] = 'd16e18bb72b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Rename anima_name to anime_name
    op.alter_column(
        'anime_macha',
        'anima_name',
        new_column_name='anime_name'
    )

    # Add rating with default value 5
    op.add_column(
        'anime_macha',
        sa.Column(
            'rating',
            sa.Integer(),
            nullable=False,
            server_default=sa.text('5')
        )
    )


def downgrade() -> None:
    # Remove rating
    op.drop_column('anime_macha', 'rating')

    # Rename anime_name back to anima_name
    op.alter_column(
        'anime_macha',
        'anime_name',
        new_column_name='anima_name'
    )
