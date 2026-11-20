
"""added new colum

Revision ID: d16e18bb72b9
Revises: 3f7fa3bc9a91
Create Date: 2026-11-20 14:59:49.220687
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd16e18bb72b9'
down_revision: Union[str, Sequence[str], None] = '3f7fa3bc9a91'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Rename the existing primary key column
    op.alter_column(
        'anime_macha',
        'anime_id',
        new_column_name='anime_id'
    )

    # 2. Add the new status column
    op.add_column(
        'anime_macha',
        sa.Column('status', sa.String(length=30), nullable=True)
    )

    # 3. Update existing records
    op.execute("""
        UPDATE anime_macha
        SET status = 'ONGOING'
        WHERE status IS NULL
    """)


def downgrade() -> None:
    # 1. Remove the status column
    op.drop_column('anime_macha', 'status')

    # 2. Rename the primary key column back
    op.alter_column(
        'anime_macha',
        'anime_id',
        new_column_name='anima_id'
    )
