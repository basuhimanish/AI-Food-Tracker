"""add phone_number to users

Revision ID: 127ee2ca1ba5
Revises: ed1f4634865e
Create Date: 2025-08-07 14:30:29.975875

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '127ee2ca1ba5'
down_revision: Union[str, None] = 'ed1f4634865e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
