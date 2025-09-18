"""initial

Revision ID: ed1f4634865e
Revises: 452fa3f87c2b
Create Date: 2025-08-02 22:34:31.114587

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed1f4634865e'
down_revision: Union[str, None] = '452fa3f87c2b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
