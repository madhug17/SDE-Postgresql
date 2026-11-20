"""renamed

Revision ID: 3f7fa3bc9a91
Revises: 1df70738259e
Create Date: 2026-11-20 14:57:14.554507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f7fa3bc9a91'
down_revision: Union[str, Sequence[str], None] = '1df70738259e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
