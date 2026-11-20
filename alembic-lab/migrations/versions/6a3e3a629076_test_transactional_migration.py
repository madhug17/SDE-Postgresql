"""test transactional migration

Revision ID: 6a3e3a629076
Revises: cf29f309d41a
Create Date: 2026-11-20 16:04:44.193550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a3e3a629076'
down_revision: Union[str, Sequence[str], None] = 'cf29f309d41a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'anime_macha', sa.Column('test_age', sa.Integer(), nullable=True)
    )
    op.add_column(
        'anime_macha',sa.Column('test_city',sa.String(50),nullable=True)
    )


def downgrade() -> None:
    op.drop_column('anime_macha', 'test_city')
    op.drop_column('anime_macha','test_age')
