"""merge developer migrations

Revision ID: b78e93ce20fa
Revises: 037ab107ee30, 5b5b36b52c2a
Create Date: 2026-11-20 14:44:08.832939

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b78e93ce20fa'
down_revision: Union[str, Sequence[str], None] = ('037ab107ee30', '5b5b36b52c2a')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
