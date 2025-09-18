"""initial tables

Revision ID: 256e687bfecb
Revises: 127ee2ca1ba5
Create Date: 2025-08-07 14:31:30.007640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '256e687bfecb'
down_revision: Union[str, None] = '127ee2ca1ba5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
