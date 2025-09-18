"""remove quantity from foodlogsxtatus

Revision ID: e312168263f4
Revises: 7098a328b238
Create Date: 2025-08-07 15:21:56.268925

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e312168263f4'
down_revision: Union[str, None] = '7098a328b238'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
