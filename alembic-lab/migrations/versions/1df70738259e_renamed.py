"""renamed

Revision ID: 1df70738259e
Revises: b78e93ce20fa
Create Date: 2026-11-20 14:56:25.834760

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1df70738259e'
down_revision: Union[str, Sequence[str], None] = 'b78e93ce20fa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
